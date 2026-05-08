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
import yaml


def yaml_dq(s):
    """Return a YAML-safe double-quoted representation of string s.
    Uses yaml.dump which properly handles LaTeX backslash escaping.
    e.g. \\mathrm → \\\\mathrm  (\\m is invalid YAML escape, backslash gets doubled)"""
    if not s:
        return '""'
    # yaml.dump with double-quote style handles all edge cases
    dumped = yaml.dump(s, default_style='"', allow_unicode=True)
    return dumped.strip()  # remove trailing newline

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
    """Extract a YAML field value using yaml.safe_load (handles all formats)."""
    parts = content.split("---", 1)
    if len(parts) < 2:
        return "" if field not in ("authors", "keywords", "wiki_concepts") else []

    rest = parts[1]
    fm_end = rest.find("\n---")
    if fm_end < 0:
        fm_end = len(rest)
    fm_text = rest[:fm_end]

    # Try yaml.safe_load first (handles yaml.dump format correctly)
    try:
        fm = yaml.safe_load(fm_text)
        if isinstance(fm, dict):
            val = fm.get(field, "")
            if val is None:
                return "" if field not in ("authors", "keywords", "wiki_concepts") else []
            # Convert lists to string items for list-type fields
            if field in ("authors", "keywords", "wiki_concepts"):
                if isinstance(val, list):
                    return [str(v).strip().strip('"').strip("'") for v in val]
                return []
            return str(val).strip().strip('"').strip("'")
    except yaml.YAMLError:
        pass

    # Fallback to regex for broken YAML
    if field in ("authors", "keywords", "wiki_concepts"):
        m = re.search(rf"^{field}\s*:\s*\n((?:\s+-.*\n)*)", fm_text, re.MULTILINE)
        if m:
            items = re.findall(r'-\s*"?(.*?)"?\s*$', m.group(1), re.MULTILINE)
            return items
        return []

    m = re.search(rf'^{field}\s*:\s*"?(.*?)"?\s*$', fm_text, re.MULTILINE)
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

    # Build YAML frontmatter — each key appears exactly once
    lines = ["---"]
    seen_keys = set()

    def add(key, line):
        if key not in seen_keys:
            seen_keys.add(key)
            lines.append(line)

    if title:
        add("title", f'title: {yaml_dq(title)}')
    if authors:
        add("authors", "authors:")
        for a in authors:
            a_clean = a.strip().strip('"').strip("'")
            if a_clean:
                lines.append(f'  - {yaml_dq(a_clean)}')
    if date:
        add("date", f'date: "{date}"')
    if year:
        add("year", f"year: {year}")
    if journal:
        add("journal", f'journal: {yaml_dq(journal)}')
    if doi:
        add("doi", f'doi: "{doi}"')
    if abstract:
        add("abstract", f'abstract: {yaml_dq(abstract)}')
    if abstract_cn:
        add("abstract_cn", f'abstract_cn: {yaml_dq(abstract_cn)}')
    if keywords:
        add("keywords", "keywords:")
        for kw in keywords:
            kw_clean = kw.strip().strip('"').strip("'")
            if kw_clean:
                if not kw_clean.startswith("[["):
                    kw_clean = f"[[{kw_clean}]]"
                lines.append(f'  - {yaml_dq(kw_clean)}')
    if cite_val:
        add("cite", f'cite: {yaml_dq(cite_val)}')
    if ai_sum:
        add("aiSum", f'aiSum: {yaml_dq(ai_sum)}')
    if confidence:
        add("confidence", f"confidence: {confidence}")
    if wiki_concepts:
        add("wiki_concepts", "wiki_concepts:")
        for wc in wiki_concepts:
            wc_clean = wc.strip().strip('"').strip("'")
            if wc_clean:
                if not wc_clean.startswith("[["):
                    wc_clean = f"[[{wc_clean}]]"
                lines.append(f'  - {yaml_dq(wc_clean)}')
    add("end", "---")

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
