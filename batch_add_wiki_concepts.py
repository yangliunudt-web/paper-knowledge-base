#!/usr/bin/env python3
"""
Batch add wiki_concepts field to all existing papers.
Maps paper keywords → wiki concept pages (checking aliases).
Only adds concepts that actually have wiki pages.

Usage:
  python3 batch_add_wiki_concepts.py --dry-run     # Preview only
  python3 batch_add_wiki_concepts.py               # Apply changes
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

VAULT = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers")
OUTPUTS_DIR = VAULT / "Outputs"
CONCEPT_DIR = VAULT / "wiki" / "概念"

DRY_RUN = "--dry-run" in sys.argv


def load_concept_aliases():
    """Build {alias → concept_page_name} mapping from all concept pages."""
    alias_map = {}
    for cf in CONCEPT_DIR.glob("*.md"):
        name = cf.stem
        alias_map[name.lower()] = name  # page name itself
        try:
            content = cf.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if not m:
                continue
            fm = m.group(1)
            # Extract aliases list
            for line in fm.split("\n"):
                if "aliases:" in line:
                    # Handle both inline [a, b] and multi-line formats
                    aliases_str = line.split(":", 1)[1].strip()
                    if aliases_str.startswith("["):
                        # Inline format: aliases: [a, b, c]
                        vals = re.findall(r"[\"']?([^\"',\[\]]+)[\"']?", aliases_str)
                        for v in vals:
                            v = v.strip()
                            if v and v.lower() not in alias_map:
                                alias_map[v.lower()] = name
        except Exception:
            pass
    return alias_map


def extract_paper_keywords(paper_path):
    """Get list of keyword strings (without [[ ]]) from a paper."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return []
        fm = m.group(1)
        keywords = re.findall(r"\[\[(.*?)\]\]", fm)
        return [kw.strip() for kw in keywords]
    except Exception:
        return []


def has_wiki_concepts(paper_path):
    """Check if paper already has wiki_concepts field."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return True
        return "wiki_concepts:" in m.group(1)
    except Exception:
        return True


def map_keywords_to_concepts(keywords, alias_map):
    """Map paper keywords to wiki concept page names."""
    concepts = set()
    for kw in keywords:
        name = alias_map.get(kw.lower())
        if name:
            concepts.add(name)
    return sorted(concepts)


def add_wiki_concepts(paper_path, concepts):
    """Add wiki_concepts field to a paper's frontmatter (after confidence or aiSum)."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        concept_lines = "\n".join(f'  - "[[{c}]]"' for c in concepts)
        new_field = f"wiki_concepts:\n{concept_lines}"

        # Insert after confidence line (preferred) or aiSum
        if "confidence:" in content:
            new_content = re.sub(
                r'(confidence:.*\n)',
                rf'\1{new_field}\n',
                content,
                count=1
            )
        elif "aiSum:" in content:
            new_content = re.sub(
                r'(aiSum:.*\n)',
                rf'\1{new_field}\n',
                content,
                count=1
            )
        else:
            # Insert before closing ---
            new_content = re.sub(
                r'(\n---\s*\n)',
                rf'\n{new_field}\n\1',
                content,
                count=1
            )

        if new_content != content:
            if not DRY_RUN:
                paper_path.write_text(new_content, encoding="utf-8")
            return True, len(concepts)
        return False, 0
    except Exception as e:
        print(f"  Error: {paper_path.name}: {e}")
        return False, 0


def main():
    print("=" * 55)
    print("BATCH ADD wiki_concepts FIELD")
    print("=" * 55)
    if DRY_RUN:
        print("MODE: DRY RUN (no changes will be made)")
    print()

    alias_map = load_concept_aliases()
    print(f"Loaded {len(alias_map)} aliases from {len(list(CONCEPT_DIR.glob('*.md')))} concept pages")
    print()

    paper_files = [p for p in OUTPUTS_DIR.rglob("*.md") if p.parent.name == "hybrid_auto"]
    print(f"Total papers: {len(paper_files)}")

    stats = {"already_has": 0, "updated": 0, "no_match": 0, "skipped": 0}
    no_match_examples = []

    for paper in paper_files:
        if has_wiki_concepts(paper):
            stats["already_has"] += 1
            continue

        keywords = extract_paper_keywords(paper)
        concepts = map_keywords_to_concepts(keywords, alias_map)

        if not concepts:
            stats["no_match"] += 1
            if len(no_match_examples) < 10:
                no_match_examples.append((paper.stem[:60], keywords[:5]))
            continue

        success, count = add_wiki_concepts(paper, concepts)
        if success:
            stats["updated"] += 1
            if DRY_RUN and stats["updated"] <= 5:
                print(f"  → {paper.stem[:55]}...")
                print(f"    wiki_concepts: {concepts}")
        else:
            stats["skipped"] += 1

    print()
    print("─" * 55)
    print("SUMMARY")
    print("─" * 55)
    print(f"  Already have wiki_concepts: {stats['already_has']}")
    print(f"  Added wiki_concepts:        {stats['updated']}")
    print(f"  No matching concepts:       {stats['no_match']}")
    print(f"  Skipped/errors:             {stats['skipped']}")

    if no_match_examples:
        print(f"\n  Example papers with no matching concepts:")
        for title, kws in no_match_examples:
            print(f"    {title}")
            print(f"      keywords: {kws}")

    if DRY_RUN:
        print("\nDRY RUN — no changes made. Run without --dry-run to apply.")


if __name__ == "__main__":
    main()
