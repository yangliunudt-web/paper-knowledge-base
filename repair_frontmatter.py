#!/usr/bin/env python3
"""
Robust frontmatter repair: rebuild every paper's frontmatter with correct --- delimiters.
Handles corrupted frontmatter gracefully by extracting fields via regex.
Body text is preserved unchanged.

Usage:
  python3 repair_frontmatter.py --dry-run   # Check how many are broken
  python3 repair_frontmatter.py             # Repair all broken papers
"""

import re
import sys
from pathlib import Path

VAULT = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers")
OUTPUTS = VAULT / "Outputs"
DRY_RUN = "--dry-run" in sys.argv

# Fields to preserve (in order)
FM_FIELDS = [
    "title", "authors", "date", "year", "journal", "doi",
    "abstract", "abstract_cn", "keywords",
    "cite", "aiSum", "confidence", "wiki_concepts"
]


def is_broken(content):
    """Check if frontmatter is properly closed."""
    return content[:5000].count("---") < 2


def extract_field(content, field):
    """Extract a YAML field value from possibly-broken frontmatter."""
    # Get everything after first --- up to body text or end
    parts = content.split("---", 1)
    if len(parts) < 2:
        fm_area = content
    else:
        fm_area = parts[1]

    # For list-type fields (authors, keywords, wiki_concepts)
    if field in ("authors", "keywords", "wiki_concepts"):
        # Find the field header
        m = re.search(rf"^{field}\s*:\s*\n((?:\s+-.*\n)*)", fm_area, re.MULTILINE)
        if m:
            items = re.findall(r'-\s*"?(.*?)"?\s*$', m.group(1), re.MULTILINE)
            return items
        return []

    # Scalar fields
    m = re.search(rf'^{field}\s*:\s*"?(.*?)"?\s*$', fm_area, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return ""


def extract_body(content):
    """Extract body text. For broken frontmatter, find where the body starts."""
    # If frontmatter is properly closed, use the last ---
    parts = content.split("---", 2)
    if len(parts) >= 3:
        return parts[2].lstrip("\n")

    # For broken frontmatter: body starts after the last frontmatter field
    # Find the block after wiki_concepts/aiSum/confidence
    fm_body = content.split("---", 1)[1] if "---" in content else content
    last_fields = ["wiki_concepts", "confidence", "aiSum", "cite", "abstract_cn", "abstract", "keywords"]
    last_pos = 0
    for field in last_fields:
        m = re.search(rf'^{field}\s*:', fm_body, re.MULTILINE)
        if m:
            # Find end of this block
            pos = m.end()
            # Find next blank line
            rest = fm_body[pos:]
            blank = rest.find("\n\n")
            if blank >= 0:
                body_start = pos + blank + 2
            else:
                # Find first line that looks like body text (starts with # or not a YAML line)
                for i, line in enumerate(rest.split("\n")):
                    if line.strip() and not re.match(r'^\s+-|^\s+\w+\s*:', line):
                        body_start = pos + rest.find(line)
                        break
                else:
                    body_start = pos
            if body_start > last_pos:
                last_pos = body_start

    if last_pos > 0:
        return fm_body[last_pos:].lstrip("\n")
    return fm_body


def rebuild_frontmatter(content):
    """Rebuild a paper with correct frontmatter. Body text is unchanged."""
    body = extract_body(content)

    # Extract all fields
    title = extract_field(content, "title")
    authors = extract_field(content, "authors")
    date = extract_field(content, "date")
    year = extract_field(content, "year")
    journal = extract_field(content, "journal")
    doi = extract_field(content, "doi")
    abstract = extract_field(content, "abstract")
    abstract_cn = extract_field(content, "abstract_cn")
    keywords = extract_field(content, "keywords")
    cite_val = extract_field(content, "cite")
    ai_sum = extract_field(content, "aiSum")
    confidence = extract_field(content, "confidence")
    wiki_concepts = extract_field(content, "wiki_concepts")

    # Build YAML frontmatter
    lines = ["---"]
    if title:
        lines.append(f'title: "{title}"')
    if authors:
        lines.append("authors:")
        for a in authors:
            a_clean = a.strip().strip('"').strip("'")
            if a_clean:
                lines.append(f'  - "{a_clean}"')
    if date:
        lines.append(f'date: "{date}"')
    if year:
        lines.append(f"year: {year}")
    if journal:
        lines.append(f'journal: "{journal}"')
    if doi:
        lines.append(f'doi: "{doi}"')
    if abstract:
        lines.append(f'abstract: "{abstract}"')
    if abstract_cn:
        lines.append(f'abstract_cn: "{abstract_cn}"')
    if keywords:
        lines.append("keywords:")
        for kw in keywords:
            kw_clean = kw.strip().strip('"').strip("'")
            if kw_clean:
                # Ensure wikilink format
                if not kw_clean.startswith("[["):
                    kw_clean = f"[[{kw_clean}]]"
                lines.append(f'  - "{kw_clean}"')
    if cite_val:
        lines.append(f'cite: "{cite_val}"')
    if ai_sum:
        lines.append(f'aiSum: "{ai_sum}"')
    if confidence:
        lines.append(f"confidence: {confidence}")
    if wiki_concepts:
        lines.append("wiki_concepts:")
        for wc in wiki_concepts:
            wc_clean = wc.strip().strip('"').strip("'")
            if wc_clean:
                if not wc_clean.startswith("[["):
                    wc_clean = f"[[{wc_clean}]]"
                lines.append(f'  - "{wc_clean}"')
    lines.append("---")

    fm = "\n".join(lines) + "\n"
    return fm + "\n" + body


def main():
    print("=" * 55)
    print("FRONTMATTER REPAIR")
    print("=" * 55)
    if DRY_RUN:
        print("MODE: DRY RUN")
    print()

    papers = [p for p in OUTPUTS.rglob("*.md") if p.parent.name == "hybrid_auto"]
    broken_before = sum(1 for p in papers if is_broken(p.read_text()))
    print(f"Total papers: {len(papers)}")
    print(f"Broken before: {broken_before}")

    if DRY_RUN:
        print("\nDRY RUN — no changes made.")
        return

    repaired = 0
    for paper in papers:
        content = paper.read_text(encoding="utf-8")
        if not is_broken(content):
            continue
        try:
            new_content = rebuild_frontmatter(content)
            paper.write_text(new_content, encoding="utf-8")
            repaired += 1
        except Exception as e:
            print(f"  Error: {paper.stem[:50]}... — {e}")

    print(f"Repaired: {repaired}")

    # Verify
    broken_after = sum(1 for p in papers if is_broken(p.read_text()))
    print(f"Broken after: {broken_after}")
    if broken_after > 0:
        print("\nStill broken:")
        for p in papers:
            if is_broken(p.read_text()):
                print(f"  {p.stem[:60]}...")


if __name__ == "__main__":
    main()
