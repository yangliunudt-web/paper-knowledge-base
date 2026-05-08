#!/usr/bin/env python3
"""
Extract metadata from paper body text and rebuild missing frontmatter fields.
Only adds missing fields; preserves any existing field values.
Body text is never modified.
"""

import re
import sys
import yaml
from pathlib import Path

VAULT = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers")
OUTPUTS = VAULT / "Outputs"
DRY_RUN = "--dry-run" in sys.argv


def extract_from_body(body):
    """Extract title, authors, keywords, abstract from body text."""
    result = {}

    # Title: first ## heading or first bold text
    m = re.search(r'^##?\s*(.+?)$', body, re.MULTILINE)
    if not m:
        m = re.search(r'^#\s*(.+?)$', body, re.MULTILINE)
    if m:
        title = m.group(1).strip()
        title = re.sub(r'\$\\[a-z]+\s*\{[^}]*\}\s*\$', '', title)  # strip LaTeX
        title = re.sub(r'\$[^$]*\$', '', title)  # strip inline math
        title = re.sub(r'\s+', ' ', title).strip()
        if 10 < len(title) < 300:
            result['title'] = title

    # Authors: line after title with many capitalized words
    # Look for author block (multiple capitalized names separated by spaces or commas)
    author_patterns = [
        # "Author1, Author2, ..., AuthorN"
        r'(?:[A-Z][a-z]+(?:\s+[A-Z]\.?\s*)?(?:[A-Z][a-z]+)?(?:,\s*|$|\s+and\s+|\s+\d)){2,}',
    ]
    lines = body.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip title lines and short lines
        if len(line) < 20 or line.startswith('#'):
            continue
        if i < 5:  # Authors usually in first few non-heading lines
            # Count words that look like names (start with capital)
            words = line.split()
            caps = [w for w in words if re.match(r'^[A-Z][a-z]+$', w)]
            if len(caps) >= 3:
                # Split concatenated names: "Yifei Pei Yufei Shang" → ["Yifei Pei", "Yufei Shang"]
                authors = []
                j = 0
                while j < len(caps):
                    if j + 1 < len(caps):
                        authors.append(f"{caps[j]} {caps[j+1]}")
                        j += 2
                    else:
                        authors.append(caps[j])
                        j += 1
                if 2 <= len(authors) <= 30:
                    result['authors'] = authors
                    break

    # Keywords: "Keywords:" or "KEYWORDS:" line
    m = re.search(r'(?:Keywords?|KEYWORDS?)\s*:\s*(.+?)$', body, re.MULTILINE | re.IGNORECASE)
    if m:
        kw_text = m.group(1).strip()
        # Split by | , ; or •
        kws = re.split(r'\s*[|,;•]\s*|\s{2,}', kw_text)
        kws = [k.strip() for k in kws if 2 < len(k.strip()) < 60]
        if kws:
            result['keywords'] = kws

    # Abstract: "# ABSTRACT" or "## Abstract" section until next heading
    m = re.search(r'(?:^|\n)#+\s*ABSTRACT\s*\n+(.*?)(?=\n#+\s|\n*$)', body, re.DOTALL | re.IGNORECASE)
    if m:
        abstract = m.group(1).strip()
        abstract = re.sub(r'\s+', ' ', abstract)
        if len(abstract) > 100:
            result['abstract'] = abstract[:3000]

    return result


def safe_dq(s):
    """Safely double-quote a string for YAML."""
    if not s:
        return '""'
    return yaml.dump(s, default_style='"', allow_unicode=True).strip()


def main():
    print("=" * 55)
    print("REPAIR METADATA")
    print("=" * 55)
    if DRY_RUN:
        print("DRY RUN")

    stats = {'repaired': 0, 'already_ok': 0, 'no_body': 0}
    required = ['title', 'authors', 'year', 'journal', 'abstract', 'keywords', 'aiSum']

    for p in OUTPUTS.rglob("*.md"):
        if p.parent.name != "hybrid_auto":
            continue
        content = p.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        if len(parts) < 3:
            stats['no_body'] += 1
            continue

        fm_text = parts[1]
        body = parts[2]

        # Parse current frontmatter
        try:
            fm = yaml.safe_load(fm_text)
            if not isinstance(fm, dict):
                fm = {}
        except Exception:
            fm = {}

        # Check what's missing
        missing = [f for f in required if f not in fm or not fm[f] or
                   (isinstance(fm[f], list) and len(fm[f]) == 0)]

        if not missing:
            stats['already_ok'] += 1
            continue

        # Try to extract from body
        extracted = extract_from_body(body)

        # Fill missing fields from extracted data (don't overwrite existing)
        for field in missing:
            if field in extracted and extracted[field]:
                fm[field] = extracted[field]

        # Build new frontmatter
        field_order = ["title", "authors", "date", "year", "journal", "doi",
                       "abstract", "abstract_cn", "keywords",
                       "cite", "aiSum", "confidence", "wiki_concepts"]
        lines = ["---"]
        for key in field_order:
            if key not in fm or fm[key] is None:
                continue
            val = fm[key]
            if key == "authors":
                if isinstance(val, list) and len(val) > 0:
                    lines.append("authors:")
                    for a in val:
                        a_str = str(a).strip().strip('"').strip("'")
                        if a_str:
                            lines.append(f"  - {safe_dq(a_str)}")
            elif key in ("keywords", "wiki_concepts"):
                if isinstance(val, list) and len(val) > 0:
                    lines.append(f"{key}:")
                    for item in val:
                        s = str(item).strip().strip('"').strip("'")
                        if s:
                            if not s.startswith("[["):
                                s = f"[[{s}]]"
                            lines.append(f"  - {safe_dq(s)}")
            elif isinstance(val, str):
                s = val.strip().strip('"').strip("'")
                if s:
                    lines.append(f"{key}: {safe_dq(s)}")
            else:
                lines.append(f"{key}: {val}")
        lines.append("---")

        new_content = "\n".join(lines) + "\n\n" + body.lstrip("\n")

        if not DRY_RUN:
            p.write_text(new_content, encoding="utf-8")
        stats['repaired'] += 1
        if stats['repaired'] <= 5:
            gained = [f for f in missing if f in extracted]
            print(f"  {p.stem[:50]}...")
            print(f"    missing: {missing}, recovered: {gained}")

    print(f"\nRepaired: {stats['repaired']}, Already OK: {stats['already_ok']}, No body: {stats['no_body']}")


if __name__ == "__main__":
    main()
