#!/usr/bin/env python3
"""PaddleOCR-VL PDF -> Markdown extraction pipeline.

Replaces MinerU (Step 1) with PaddleOCR-VL cloud API.
Output folder structure matches MinerU exactly:
  Outputs/{pdf_basename}/hybrid_auto/
    {pdf_basename}.md         # Markdown body (Step 2 renames to paper title)
    {pdf_basename}_origin.pdf # Copy of original PDF
    images/                   # Downloaded images (img_001.jpg ...)

Usage:
  # Single PDF
  python3 pipeline_paddleocr.py --pdf "path/to/paper.pdf"

  # Batch all PDFs under a directory tree
  python3 pipeline_paddleocr.py --batch --input-dir "path/to/pdfs/"

  # With custom output base
  python3 pipeline_paddleocr.py --pdf "paper.pdf" --output-dir "/custom/Outputs/"
"""

import argparse
import asyncio
import base64
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path
from typing import Optional

import httpx

# ---- Config ----
DEFAULT_SERVER_URL = "https://e6e4w1e7x2td00i8.aistudio-app.com"
DEFAULT_ACCESS_TOKEN = os.environ.get("PADDLEOCR_TOKEN", "")
DEFAULT_OUTPUT_BASE = os.path.expanduser(
    "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs"
)
API_TIMEOUT = 180  # seconds per PDF
IMG_DOWNLOAD_TIMEOUT = 30  # seconds per image
MAX_CONCURRENT = 3
API_DELAY = 0.0  # seconds between API calls to same domain (semaphore handles limiting)
MAX_RETRIES = 2


class PaddleOCRPipeline:
    def __init__(
        self,
        output_base: str = DEFAULT_OUTPUT_BASE,
        server_url: str = DEFAULT_SERVER_URL,
        access_token: str = DEFAULT_ACCESS_TOKEN,
        max_concurrent: int = MAX_CONCURRENT,
    ):
        self.output_base = Path(output_base)
        self.server_url = server_url.rstrip("/")
        self.access_token = access_token
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self._last_api_call = 0.0

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def process_pdf(self, pdf_path: str) -> dict:
        """Process a single PDF. Returns result dict with keys:
        ok, folder, md_path, pages, image_count, error (if failed).
        """
        pdf_path = Path(pdf_path)
        result = {"pdf": str(pdf_path), "ok": False}

        try:
            folder_name = pdf_path.stem
            hybrid_dir = self.output_base / folder_name / "hybrid_auto"
            images_dir = hybrid_dir / "images"
            images_dir.mkdir(parents=True, exist_ok=True)

            # 1. Call PaddleOCR-VL API
            api_data = await self._call_api(pdf_path)
            markdown_text = api_data["markdown"]
            image_map = api_data["images"]  # key -> url_or_base64

            # 2. Download images & build replacement map
            img_replacements = await self._download_images(image_map, images_dir)

            # 3. Clean LaTeX (fix inline formula spaces, letter-spacing)
            markdown_text = self._clean_latex(markdown_text)

            # 4. Rewrite image references in markdown
            markdown_text = self._replace_image_refs(markdown_text, img_replacements)

            # 4. Save markdown
            md_path = hybrid_dir / f"{folder_name}.md"
            md_path.write_text(markdown_text, encoding="utf-8")

            # 5. Copy original PDF
            origin_pdf = hybrid_dir / f"{folder_name}_origin.pdf"
            if not origin_pdf.exists():
                shutil.copy2(pdf_path, origin_pdf)

            result.update({
                "ok": True,
                "folder": str(hybrid_dir.parent),
                "md_path": str(md_path),
                "pages": api_data["pages"],
                "image_count": len(img_replacements),
            })

        except Exception as exc:
            result["error"] = str(exc)

        return result

    async def process_batch(
        self, pdf_paths: list, progress_callback=None
    ) -> list:
        """Process multiple PDFs concurrently. Returns list of result dicts."""
        sem = self.semaphore

        async def worker(pdf_path, idx, total):
            async with sem:
                if progress_callback:
                    progress_callback(idx, total, f"Processing: {Path(pdf_path).name}")
                return await self._process_with_retry(pdf_path)

        tasks = [worker(p, i + 1, len(pdf_paths)) for i, p in enumerate(pdf_paths)]
        results = await asyncio.gather(*tasks)
        return results

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    async def _process_with_retry(self, pdf_path: Path) -> dict:
        for attempt in range(MAX_RETRIES + 1):
            result = await self.process_pdf(pdf_path)
            if result["ok"]:
                return result
            if attempt < MAX_RETRIES:
                wait = (attempt + 1) * 5
                print(f"  Retry {attempt + 1}/{MAX_RETRIES} in {wait}s: {result.get('error', 'unknown')}")
                await asyncio.sleep(wait)
        return result

    async def _rate_limit(self):
        """Ensure minimum delay between API calls."""
        now = time.monotonic()
        gap = now - self._last_api_call
        if gap < API_DELAY:
            await asyncio.sleep(API_DELAY - gap)
        self._last_api_call = time.monotonic()

    async def _call_api(self, pdf_path: Path) -> dict:
        """Send PDF to PaddleOCR-VL, return {markdown, pages, images}."""
        await self._rate_limit()

        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        b64_data = base64.b64encode(pdf_bytes).decode("ascii")

        url = f"{self.server_url}/layout-parsing"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"token {self.access_token}",
        }
        payload = {"file": b64_data, "fileType": 0}

        async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
            resp = await client.post(url, json=payload, headers=headers)
            resp.raise_for_status()
            data = resp.json()

        if data.get("errorCode") != 0:
            raise RuntimeError(f"API error {data.get('errorCode')}: {data.get('errorMsg')}")

        return self._unpack_api_response(data)

    def _unpack_api_response(self, data: dict) -> dict:
        """Extract markdown + images from API response."""
        result = data.get("result", data)
        layouts = result.get("layoutParsingResults", [])

        all_markdown = []
        all_images = {}

        for page in layouts:
            md = page.get("markdown", {})
            all_markdown.append(md.get("text", ""))
            page_images = md.get("images", {})
            all_images.update(page_images)

        return {
            "markdown": "\n\n".join(all_markdown),
            "pages": len(layouts),
            "images": all_images,
        }

    async def _download_images(self, image_map: dict, images_dir: Path) -> dict:
        """Download cloud images to local dir. Returns {old_ref: new_filename}."""
        replacements = {}
        if not image_map:
            return replacements

        async with httpx.AsyncClient(timeout=IMG_DOWNLOAD_TIMEOUT) as client:
            tasks = []
            for idx, (key, data) in enumerate(image_map.items(), 1):
                new_name = f"img_{idx:03d}.jpg"
                dest = images_dir / new_name
                tasks.append(self._download_one(client, key, data, dest, new_name))

            results = await asyncio.gather(*tasks)
            for key, new_name in results:
                if new_name:
                    replacements[key] = new_name

        return replacements

    async def _download_one(
        self, client: httpx.AsyncClient, key: str, data, dest: Path, new_name: str
    ) -> tuple:
        """Download a single image. Returns (key, new_name) or (key, None)."""
        try:
            if isinstance(data, str) and data.startswith("http"):
                # Cloud URL
                resp = await client.get(data)
                resp.raise_for_status()
                dest.write_bytes(resp.content)
            elif isinstance(data, str) and len(data) > 100:
                # Base64 encoded
                dest.write_bytes(base64.b64decode(data))
            else:
                return (key, None)

            return (key, new_name)
        except Exception:
            return (key, None)

    @staticmethod
    def _clean_latex(markdown: str) -> str:
        """Fix LaTeX rendering issues from PaddleOCR-VL.

        1. Strip spaces inside $ delimiters: $ V_{TH} $ → $V_{TH}$
        2. Fix spaces around _ and ^: V _ {TH} → V_{TH}
        3. Fix spaces before LaTeX braces: \\mathcal {X} → \\mathcal{X}
        4. Fix letter-spacing in font commands: \\mathrm{s i m} → \\mathrm{sim}
        5. Remove spaces between letters/numbers in math mode
        """

        # --- 1. Fix font commands with spaced braces ---
        # \\mathcal { X } → \\mathcal{X}
        font_cmds = ['mathrm', 'mathtt', 'mathbb', 'mathcal', 'mathbf', 'mathit', 'mathsf', 'textit', 'textbf']
        for cmd in font_cmds:
            # Fix: \\cmd { content } → \\cmd{content}
            markdown = re.sub(
                r'\\' + cmd + r'\s+\{([^}]*)\}',
                lambda m: '\\' + cmd + '{' + re.sub(r'\s+', '', m.group(1).strip()) + '}',
                markdown
            )
            # Fix: {\\cmd{content}} with spaces in content
            def _fix_spaced_content(m, cmd=cmd):
                content = m.group(1)
                content = re.sub(r'(?<=[A-Za-z0-9])\s+(?=[A-Za-z0-9])', '', content)
                return '{\\' + cmd + '{' + content + '}'
            markdown = re.sub(
                r'\{\\' + cmd + r'\{([^}]+)\}\}',
                _fix_spaced_content, markdown
            )

        # --- 2. Fix inline math: $ ... $ → $...$ (strip leading/trailing spaces) ---
        def _clean_inline_math(m):
            content = m.group(1)
            # Strip outer spaces
            content = content.strip()
            # Remove spaces around _ and ^: V _ {TH} → V_{TH}
            content = re.sub(r'\s+_\s+', '_', content)
            content = re.sub(r'\s+\^\s+', '^', content)
            # Remove spaces before { } braces in subscripts: _{ TH } → _{TH}
            content = re.sub(r'_\{\s+([^}]*?)\s+\}', r'_{\1}', content)
            content = re.sub(r'\^\{\s+([^}]*?)\s+\}', r'^{\1}', content)
            # Remove spaces between adjacent letters/numbers (not operators)
            # "h i g h" → "high", but don't touch "a + b" or "x = 1"
            content = re.sub(r'(?<=[A-Za-z0-9])\s+(?=[A-Za-z0-9])', '', content)
            return '$' + content + '$'

        markdown = re.sub(r'(?<!\$)\$(.+?)\$(?!\$)', _clean_inline_math, markdown)

        # --- 3. Fix display math: $$...$$ ---
        def _clean_display_math(m):
            inner = m.group(1)
            inner = re.sub(r'(?<=[A-Za-z0-9])\s+(?=[A-Za-z0-9])', '', inner)
            # Fix spaced subscripts/superscripts in display math
            inner = re.sub(r'\s+_\s+', '_', inner)
            inner = re.sub(r'\s+\^\s+', '^', inner)
            return '$$' + inner + '$$'

        markdown = re.sub(r'\$\$(.+?)\$\$', _clean_display_math, markdown, flags=re.DOTALL)

        # --- 4. Fix missing closing } before $ ---
        # Pattern: \mathbf{xy$ → \mathbf{xy}$  or  _{\mathbf{xy$ → _{\mathbf{xy}}$
        # Within $...$, find {word$ where word has no braces and add missing }
        def _fix_missing_brace(m):
            inner = m.group(0)
            # Fix {text$ → {text}$ when text contains only alphanumeric chars
            inner = re.sub(r'\{([A-Za-z0-9]+)\$', r'{\1}$', inner)
            # Fix {text_{sub$ → {text_{sub}}$
            inner = re.sub(r'\{([A-Za-z0-9]+)_\{([A-Za-z0-9]+)\$', r'{\1_{\2}}$', inner)
            return inner

        markdown = re.sub(r'(?<!\$)\$(.+?)\$(?!\$)', _fix_missing_brace, markdown)

        # --- 5. Fix remaining LaTeX commands with space before brace ---
        markdown = re.sub(r'\\([a-zA-Z]+)\s+\{', r'\\\1{', markdown)

        return markdown

    @staticmethod
    def _replace_image_refs(markdown: str, replacements: dict) -> str:
        """Replace <img src='imgs/...'> with Obsidian image links."""
        if not replacements:
            # Still normalize any img tags to standard markdown
            markdown = re.sub(
                r'<img[^>]+src="([^"]+)"[^>]*>',
                r'![\1](images/unknown.jpg)',
                markdown,
            )
            return markdown

        def _replacer(match):
            src = match.group(1)
            # Match key from replacements (fuzzy — check if any key is in src)
            for old_key, new_name in replacements.items():
                if old_key in src or src in old_key:
                    return f"![{new_name}](images/{new_name})"
            # Fallback: use the src basename
            basename = src.rsplit("/", 1)[-1] if "/" in src else src
            return f"![{basename}](images/{basename})"

        # Pattern 1: <img src="imgs/img_in_image_box_xxx.jpg" ... />
        markdown = re.sub(
            r'<img[^>]+src="([^"]+)"[^>]*>',
            _replacer,
            markdown,
        )

        # Pattern 2: <div style="text-align: center;"><img ...></div>
        markdown = re.sub(
            r'<div[^>]*>\s*<img[^>]+src="([^"]+)"[^>]*>\s*</div>',
            lambda m: _replacer(m),
            markdown,
        )

        # Pattern 3: Standalone <div> captions (keep as text)
        markdown = re.sub(r'<div[^>]*>(.*?)</div>', r'\1', markdown)

        return markdown


# ---- CLI ----

def find_pdfs(input_dir: str) -> list:
    """Recursively find all PDFs under input_dir."""
    pdfs = []
    for root, _, files in os.walk(input_dir):
        for f in files:
            if f.lower().endswith(".pdf") and not f.startswith("."):
                pdfs.append(os.path.join(root, f))
    return sorted(pdfs)


def print_progress(idx: int, total: int, msg: str):
    print(f"[{idx:3d}/{total}] {msg}")


async def main():
    parser = argparse.ArgumentParser(description="PaddleOCR-VL PDF Extraction Pipeline")
    parser.add_argument("--pdf", help="Single PDF file path")
    parser.add_argument("--batch", action="store_true", help="Batch mode")
    parser.add_argument("--input-dir", help="Directory to scan for PDFs recursively")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_BASE, help="Output base directory")
    parser.add_argument("--concurrency", type=int, default=MAX_CONCURRENT, help="Max concurrent API calls")
    parser.add_argument("--dry-run", action="store_true", help="List PDFs without processing")
    args = parser.parse_args()

    pipeline = PaddleOCRPipeline(
        output_base=args.output_dir,
        max_concurrent=args.concurrency,
    )

    if args.dry_run:
        if args.pdf:
            pdfs = [args.pdf]
        elif args.input_dir:
            pdfs = find_pdfs(args.input_dir)
        else:
            print("Error: --pdf or --input-dir required")
            sys.exit(1)
        print(f"Found {len(pdfs)} PDF(s):")
        for p in pdfs:
            print(f"  {p}")
        return

    if args.pdf:
        # Single PDF mode
        print(f"Processing: {args.pdf}")
        result = await pipeline.process_pdf(args.pdf)
        if result["ok"]:
            print(f"OK  folder={result['folder']}  pages={result['pages']}  images={result['image_count']}")
        else:
            print(f"FAIL  {result.get('error')}")
            sys.exit(1)

    elif args.input_dir:
        # Batch mode
        pdfs = find_pdfs(args.input_dir)
        if not pdfs:
            print("No PDFs found.")
            return

        print(f"Batch processing {len(pdfs)} PDFs (concurrency={args.concurrency})...")
        start = time.monotonic()

        results = await pipeline.process_batch(pdfs, progress_callback=print_progress)

        elapsed = time.monotonic() - start
        ok = sum(1 for r in results if r["ok"])
        fail = len(results) - ok
        total_images = sum(r.get("image_count", 0) for r in results)

        print(f"\n{'='*60}")
        print(f"Done: {ok} OK, {fail} FAILED ({elapsed:.0f}s, {total_images} images)")
        print(f"{'='*60}")

        # Report failures
        if fail:
            print("\nFailures:")
            for r in results:
                if not r["ok"]:
                    print(f"  {r['pdf']}: {r.get('error', 'unknown')}")

        # Save report
        report_path = Path(args.output_dir).parent / "_NonPapers" / "pipeline_paddleocr_report.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_lines = [
            "# PaddleOCR-VL Pipeline Report\n",
            f"**Date**: {time.strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Input**: {args.input_dir}",
            f"**Total**: {len(pdfs)} PDFs",
            f"**OK**: {ok}",
            f"**Failed**: {fail}",
            f"**Duration**: {elapsed:.0f}s",
            f"**Images**: {total_images}",
            "",
            "## Successful\n",
        ]
        for r in results:
            if r["ok"]:
                report_lines.append(f"- [{Path(r['folder']).name}]({r['md_path']}) — {r['pages']}pp, {r['image_count']} images")
        if fail:
            report_lines.append("\n## Failed\n")
            for r in results:
                if not r["ok"]:
                    report_lines.append(f"- `{r['pdf']}`: {r.get('error', 'unknown')}")

        report_path.write_text("\n".join(report_lines), encoding="utf-8")
        print(f"\nReport saved: {report_path}")

    else:
        print("Error: --pdf or --batch --input-dir required")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
