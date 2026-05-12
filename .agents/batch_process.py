#!/usr/bin/env python3
"""
Batch process PDFs with progress tracking.
Generates/updates Process.md in the input directory.
"""

import asyncio
import os
import sys
import time
from pathlib import Path

# Add parent to path for import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pipeline_paddleocr import PaddleOCRPipeline, find_pdfs

INPUT_DIR = "/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs/2411.03687v1/download"
OUTPUT_BASE = "/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs"
PROCESS_FILE = os.path.join(INPUT_DIR, "Process.md")
CONCURRENCY = 6


def collect_papers(input_dir: str) -> list[dict]:
    """Scan download directory and build paper list by category."""
    papers = []
    for root, dirs, files in os.walk(input_dir):
        for f in sorted(files):
            if f.lower().endswith(".pdf") and not f.startswith("."):
                rel_dir = os.path.relpath(root, input_dir)
                if rel_dir == ".":
                    category = "(root)"
                else:
                    category = rel_dir
                papers.append({
                    "category": category,
                    "filename": f,
                    "pdf_path": os.path.join(root, f),
                    "stem": Path(f).stem,
                })
    return papers


def init_process_file(papers: list[dict]) -> None:
    """Create initial Process.md tracking file."""
    # Group by category
    cats: dict[str, list] = {}
    for p in papers:
        cats.setdefault(p["category"], []).append(p)

    lines = [
        "# Process — PaddleOCR-VL Extraction Progress",
        f"**Date**: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Total**: {len(papers)} PDFs across {len(cats)} categories",
        f"**Pipeline**: PaddleOCR-VL (cloud API)",
        "",
        "| Category | Total | Extracted | Frontmatter |",
        "|----------|-------|-----------|-------------|",
    ]

    for cat_name, cat_papers in sorted(cats.items()):
        lines.append(f"| {cat_name} | {len(cat_papers)} | 0 | 0 |")

    lines.append("")
    lines.append("---")
    lines.append("")

    for cat_name, cat_papers in sorted(cats.items()):
        lines.append(f"## {cat_name} ({len(cat_papers)} papers)")
        lines.append("")
        lines.append("| # | Paper | Extraction | Frontmatter | Output |")
        lines.append("|---|-------|-----------|-------------|--------|")
        for i, p in enumerate(cat_papers, 1):
            lines.append(f"| {i} | {p['filename']} | ⏳ | ⏳ | — |")
        lines.append("")

    with open(PROCESS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def update_process_status(pdf_path: str, status: str, output_folder: str = "") -> None:
    """Update a paper's status in Process.md."""
    if not os.path.exists(PROCESS_FILE):
        return
    with open(PROCESS_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    basename = os.path.basename(pdf_path)
    stem = Path(pdf_path).stem

    if status == "done":
        content = content.replace(
            f"| {basename} | ⏳ |",
            f"| {basename} | ✅ |"
        )
        # Update total count for category
    elif status == "fail":
        content = content.replace(
            f"| {basename} | ⏳ |",
            f"| {basename} | ❌ |"
        )

    # Update output link
    if output_folder:
        # Use Obsidian wikilink format: [[paper title]]
        # The .md file name matches the paper title (stem)
        content = content.replace(
            f"| {basename} | ✅ | ⏳ | — |",
            f"| {basename} | ✅ | ⏳ | [[{stem}]] |"
        )
        content = content.replace(
            f"| {basename} | ✅ | ✅ | — |",
            f"| {basename} | ✅ | ✅ | [[{stem}]] |"
        )

    with open(PROCESS_FILE, "w", encoding="utf-8") as f:
        f.write(content)


def refresh_summary(papers: list[dict]) -> None:
    """Recalculate and update category summary counts."""
    if not os.path.exists(PROCESS_FILE):
        return
    with open(PROCESS_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Count ✅ per category section
    import re
    for cat_name in sorted(set(p["category"] for p in papers)):
        section_start = content.find(f"## {cat_name}")
        if section_start == -1:
            continue
        next_section = content.find("## ", section_start + len(f"## {cat_name}"))
        if next_section == -1:
            section = content[section_start:]
        else:
            section = content[section_start:next_section]

        total = section.count("| ⏳ |") + section.count("| ✅ |") + section.count("| ❌ |")
        done = section.count("| ✅ |")

        # Update summary line
        old_line = f"| {cat_name} | "
        # Find the summary line
        cat_esc = re.escape(cat_name)
        content = re.sub(
            rf"\| {cat_esc} \| \d+ \| \d+ \| \d+ \|",
            f"| {cat_name} | {total} | {done} | 0 |",
            content
        )

    with open(PROCESS_FILE, "w", encoding="utf-8") as f:
        f.write(content)


async def process_all(papers: list[dict]) -> None:
    """Process all papers with concurrency control."""
    pipeline = PaddleOCRPipeline(output_base=OUTPUT_BASE, max_concurrent=CONCURRENCY)
    total = len(papers)

    sem = asyncio.Semaphore(CONCURRENCY)
    processed = 0
    ok_count = 0
    fail_count = 0
    skip_count = 0

    async def worker(p: dict, idx: int):
        nonlocal processed, ok_count, fail_count, skip_count
        pdf_path = p["pdf_path"]
        stem = Path(pdf_path).stem
        out_dir = Path(OUTPUT_BASE) / stem / "hybrid_auto"
        out_md = out_dir / f"{stem}.md"

        async with sem:
            # Skip if already processed
            if out_md.exists() and out_md.stat().st_size > 1000:
                skip_count += 1
                processed += 1
                ok_count += 1
                update_process_status(pdf_path, "done", str(out_dir.parent))
                print(f"[{idx:3d}/{total}] ⏭️  SKIP {Path(pdf_path).name[:60]}")
                return

            print(f"[{idx:3d}/{total}] {Path(pdf_path).name[:60]}...")
            try:
                result = await pipeline._process_with_retry(pdf_path)
                processed += 1
                if result["ok"]:
                    ok_count += 1
                    update_process_status(pdf_path, "done", result.get("folder", ""))
                    print(f"  ✅ OK  pages={result.get('pages', '?')}  images={result.get('image_count', '?')}")
                else:
                    fail_count += 1
                    update_process_status(pdf_path, "fail")
                    print(f"  ❌ FAIL  {result.get('error', 'unknown')}")
            except Exception as e:
                processed += 1
                fail_count += 1
                update_process_status(pdf_path, "fail")
                print(f"  ❌ ERROR  {e}")

            ref = ok_count + fail_count + skip_count
            rem = total - ref
            print(f"  📊 {ok_count} OK / {fail_count} FAIL / {skip_count} SKIP / {rem} remaining")

    tasks = [worker(p, i + 1) for i, p in enumerate(papers)]
    await asyncio.gather(*tasks)

    print(f"\n{'='*60}")
    print(f"Batch complete: {ok_count} OK, {fail_count} FAILED, {skip_count} SKIPPED")
    print(f"{'='*60}")


async def main():
    papers = collect_papers(INPUT_DIR)
    if not papers:
        print("No PDFs found.")
        return

    print(f"Found {len(papers)} PDFs across {len(set(p['category'] for p in papers))} categories")

    # Init Process.md
    init_process_file(papers)
    print(f"Created {PROCESS_FILE}")

    # Process all
    print(f"Starting batch with concurrency={CONCURRENCY}...")
    start = time.monotonic()
    await process_all(papers)
    elapsed = time.monotonic() - start
    print(f"Elapsed: {elapsed:.0f}s ({elapsed/60:.1f} min)")

    # Final summary refresh
    refresh_summary(papers)
    print(f"Updated {PROCESS_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
