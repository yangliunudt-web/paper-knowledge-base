#!/usr/bin/env python3
"""
Batch frontmatter adder for PaddleOCR-VL extracted papers.
Extracts title + abstract from markdown body, adds minimal frontmatter.
"""

import re
import sys
from pathlib import Path
from pipeline_paddleocr import PaddleOCRPipeline

OUTPUTS = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs")
DOWNLOAD = OUTPUTS / "2411.03687v1/download"
PIPELINE = "PaddleOCR-VL"


def extract_title(text: str) -> str:
    """Extract paper title from # Heading."""
    m = re.search(r'^#\s+(.+?)$', text, re.MULTILINE)
    if m:
        title = m.group(1).strip()
        # Clean LaTeX artifacts from title
        title = re.sub(r'\$', '', title)
        title = re.sub(r'\\mathrm\{([^}]+)\}', r'\1', title)
        title = re.sub(r'\\[a-zA-Z]+\{([^}]+)\}', r'\1', title)
        title = re.sub(r'\s+', ' ', title).strip()
        return title
    return ""


def extract_abstract(text: str) -> str:
    """Extract abstract from body (section after '# Abstract' or '## Abstract')."""
    # Find abstract heading
    m = re.search(r'^#+\s*[Aa]bstract\s*$', text, re.MULTILINE)
    if not m:
        return ""
    start = m.end()
    # Find next heading or end of text
    rest = text[start:]
    m2 = re.search(r'^\s*#+\s+\w', rest, re.MULTILINE)
    if m2:
        abstract = rest[:m2.start()].strip()
    else:
        abstract = rest.strip()
    # Clean: remove leading/trailing whitespace, collapse newlines
    abstract = re.sub(r'\s+', ' ', abstract)
    return abstract[:2000]  # Limit length


def extract_authors(text: str) -> list[str]:
    """Extract author line (after title, before abstract)."""
    # Look for author line: after title, before abstract heading
    title_m = re.search(r'^#\s+.+$', text, re.MULTILINE)
    if not title_m:
        return []
    start = title_m.end()
    abstract_m = re.search(r'^#+\s*[Aa]bstract', text[start:], re.MULTILINE)
    if not abstract_m:
        return []
    end = start + abstract_m.start()
    author_block = text[start:end].strip()
    # Extract names from lines like "Name1, Name2, Name3..."
    # Remove affiliation markers like $^{1}$, $^{*}$, etc.
    author_block = re.sub(r'\$\^?\{[^}]*\}\$', '', author_block)
    author_block = re.sub(r'\$[^$]*\$', '', author_block)
    author_block = re.sub(r'\([^)]*\d+[^)]*\)', '', author_block)  # (1), (2)
    author_block = re.sub(r'Department.*$', '', author_block, flags=re.MULTILINE)
    author_block = re.sub(r'School.*$', '', author_block, flags=re.MULTILINE)
    author_block = re.sub(r'University.*$', '', author_block, flags=re.MULTILINE)
    author_block = re.sub(r'College.*$', '', author_block, flags=re.MULTILINE)
    author_block = re.sub(r'Institute.*$', '', author_block, flags=re.MULTILINE)
    author_block = re.sub(r'\{[^}]*\}', '', author_block)
    # Split by comma and filter
    names = []
    for part in re.split(r'[,;]\s*|\s+and\s+|\n', author_block):
        part = part.strip()
        # Must look like a name (2+ words, or First Last format)
        if len(part) > 3 and re.match(r'^[A-Z][a-z]', part):
            names.append(part)
    return names[:20]  # Max 20 authors


def extract_year(text: str, pdf_path: Path) -> int:
    """Try to infer year."""
    # Look for copyright year in text
    m = re.search(r'(?:Copyright|©)\s*(\d{4})', text)
    if m:
        return int(m.group(1))
    m = re.search(r'(?:Published|Accepted).*?(\d{4})', text)
    if m:
        return int(m.group(1))
    # Look in first page header/footer
    m = re.search(r'20\d{2}', text[:500])
    if m:
        return int(m.group(0))
    return 0


def detect_confidence(text: str, title: str) -> str:
    """Heuristic confidence detection."""
    # Check for top venue indicators
    text_start = text[:2000]
    if re.search(r'(?:CVPR|ICCV|ECCV|NeurIPS|ICML|ICLR|AAAI|IJCAI|ACL|EMNLP)', text_start):
        return "high"
    if re.search(r'(?:IEEE|ACM|Springer|Nature|Science|arXiv|preprint)', text_start):
        return "medium"
    return "low"


def extract_keywords(text: str) -> list[str]:
    """Extract keywords from paper body."""
    # Look for keywords section
    m = re.search(r'(?:Keywords|Index Terms|Key words)[:—\-]\s*(.+?)(?:\n|$)', text, re.IGNORECASE)
    if m:
        kw_text = m.group(1).strip()
        kws = re.split(r'[,;•·]\s*', kw_text)
        return [f"[[{k.strip()}]]" for k in kws if len(k.strip()) > 2]
    return []


def add_frontmatter(md_path: Path, pdf_path: Path) -> bool:
    """Add frontmatter to a single paper."""
    text = md_path.read_text(encoding="utf-8")
    if text.startswith("---"):
        return False  # Already has frontmatter

    # Apply LaTeX cleanup before extracting metadata
    text = PaddleOCRPipeline._clean_latex(text)
    md_path.write_text(text, encoding="utf-8")  # save cleaned version

    title = extract_title(text)
    if not title:
        return False

    abstract = extract_abstract(text)
    authors = extract_authors(text)
    year = extract_year(text, pdf_path)
    keywords = extract_keywords(text)
    confidence = detect_confidence(text, title)

    # Build frontmatter
    fm_lines = ["---", f'title: "{title}"']
    if authors:
        fm_lines.append("authors:")
        for a in authors:
            fm_lines.append(f'  - "{a}"')
    else:
        fm_lines.append("authors: []")
    fm_lines.append(f'date: "{year}-01-01"')
    fm_lines.append(f"year: {year}")
    fm_lines.append('journal: ""')
    if abstract:
        fm_lines.append(f'abstract: "{abstract}"')
    fm_lines.append('abstract_cn: ""')
    if keywords:
        fm_lines.append("keywords:")
        for k in keywords:
            fm_lines.append(f'  - "{k}"')
    else:
        fm_lines.append("keywords: []")
    fm_lines.append('cite: ""')
    fm_lines.append(f'aiSum: ""')
    fm_lines.append(f'confidence: "{confidence}"')
    fm_lines.append(f'pipeline: "{PIPELINE}"')
    fm_lines.append('wiki_concepts: []')
    fm_lines.append("---")
    fm_lines.append("")

    new_text = "\n".join(fm_lines) + "\n" + text
    md_path.write_text(new_text, encoding="utf-8")
    return True


def main():
    # Collect all PDF stems from download/
    pdf_stems = {}
    for pdf in DOWNLOAD.rglob("*.pdf"):
        if not pdf.name.startswith("."):
            pdf_stems[pdf.stem] = pdf

    # Match with output md files
    processed = 0
    skipped = 0
    for md_file in sorted(OUTPUTS.glob("*/hybrid_auto/*.md")):
        stem = md_file.stem
        if stem in pdf_stems:
            pdf_path = pdf_stems[stem]
            try:
                if add_frontmatter(md_file, pdf_path):
                    processed += 1
                else:
                    skipped += 1
            except Exception as e:
                print(f"  Error: {stem[:60]} — {e}")

    print(f"Frontmatter added: {processed}, skipped (already had): {skipped}")
    print(f"Total: {processed + skipped}/{len(pdf_stems)}")


if __name__ == "__main__":
    main()
