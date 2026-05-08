#!/usr/bin/env python3
"""
Populate concept page "相关论文" tables from wiki_concepts data.
Reverse-lookup: for each concept, find all papers that reference it.

Usage:
  python3 batch_populate_concepts.py --dry-run     # Preview only
  python3 batch_populate_concepts.py               # Apply changes
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

VAULT = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers")
OUTPUTS_DIR = VAULT / "Outputs"
CONCEPT_DIR = VAULT / "wiki" / "概念"

DRY_RUN = "--dry-run" in sys.argv


def get_paper_info(paper_path):
    """Extract title, year, journal, aiSum from a paper."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return None
        fm = m.group(1)

        title = paper_path.stem
        year = ""
        journal = ""
        ai_sum = ""

        for line in fm.split("\n"):
            line = line.strip()
            if line.startswith("year:"):
                year = line.split(":", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("journal:"):
                journal = line.split(":", 1)[1].strip().strip('"').strip("'")
                if len(journal) > 50:
                    journal = journal[:47] + "..."
            elif line.startswith("aiSum:"):
                ai_sum = line.split(":", 1)[1].strip().strip('"').strip("'")
                if len(ai_sum) > 80:
                    ai_sum = ai_sum[:77] + "..."

        contribution = ai_sum if ai_sum else journal
        return {
            "title": title,
            "year": year,
            "journal": journal,
            "contribution": contribution,
        }
    except Exception:
        return None


def get_wiki_concepts(paper_path):
    """Extract wiki_concepts list from a paper."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return []
        fm = m.group(1)
        concepts = re.findall(r'\[\[(.*?)\]\]', fm)
        # Only those from the wiki_concepts section
        in_wiki_concepts = False
        result = []
        for line in fm.split("\n"):
            if "wiki_concepts:" in line:
                in_wiki_concepts = True
                continue
            if in_wiki_concepts:
                if line.strip().startswith("- "):
                    c = re.findall(r'\[\[(.*?)\]\]', line)
                    result.extend(c)
                elif line.strip() and not line.strip().startswith("-") and ":" in line:
                    break
        return result
    except Exception:
        return []


def build_concept_to_papers():
    """Build {concept_name: [(paper_title, info), ...]} mapping."""
    c2p = defaultdict(list)
    papers = [p for p in OUTPUTS_DIR.rglob("*.md") if p.parent.name == "hybrid_auto"]

    for paper in papers:
        concepts = get_wiki_concepts(paper)
        if not concepts:
            continue
        info = get_paper_info(paper)
        if not info:
            continue
        for c in concepts:
            c2p[c].append((paper.stem, info))

    # Sort each list: papers with year first, then by title
    for c in c2p:
        c2p[c].sort(key=lambda x: (x[1]["year"] == "", x[1]["year"], x[0]))
    return c2p


def update_concept_page(concept_path, papers):
    """Replace the empty '相关论文' table with actual paper rows."""
    try:
        content = concept_path.read_text(encoding="utf-8")

        # Build new table rows
        rows = []
        for title, info in papers[:12]:  # max 12 papers per concept
            short = title[:45] + "..." if len(title) > 48 else title
            year = info["year"] or "-"
            contrib = info["contribution"] or info["journal"] or "-"
            rows.append("| [[" + title + "|" + short + "]] | " + year + " | " + contrib + " |")

        new_table = "| 论文 | 年份 | 核心发现 |\n|------|------|----------|\n" + "\n".join(rows)

        # Replace the placeholder table (between "## 相关论文" and "## 相关概念")
        # Pattern: the old table with placeholder rows
        old_pattern = r'(## 相关论文\n\n)\| 论文 \| 年份 \| 核心发现 \|\n\|------\|------\|----------\|\n(\| \| \| \|\n)*'
        new_content = re.sub(old_pattern, r'\1' + new_table + '\n', content)

        if new_content != content:
            if not DRY_RUN:
                concept_path.write_text(new_content, encoding="utf-8")
            return True, len(papers)
        return False, 0
    except Exception as e:
        print(f"  Error updating {concept_path.name}: {e}")
        return False, 0


def main():
    print("=" * 55)
    print("POPULATE CONCEPT PAGE PAPER TABLES")
    print("=" * 55)
    if DRY_RUN:
        print("MODE: DRY RUN (no changes will be made)")
    print()

    c2p = build_concept_to_papers()
    print(f"Papers with wiki_concepts: {sum(1 for p in OUTPUTS_DIR.rglob('*.md') if p.parent.name == 'hybrid_auto' and get_wiki_concepts(p))}")
    print(f"Concept → paper mappings: {sum(len(v) for v in c2p.values())}")
    print()

    updated = 0
    empty = 0
    skipped = 0

    for cf in sorted(CONCEPT_DIR.glob("*.md")):
        name = cf.stem
        papers = c2p.get(name, [])

        if not papers:
            empty += 1
            continue

        success, count = update_concept_page(cf, papers)
        if success:
            updated += 1
            if DRY_RUN:
                print(f"  {name}: {count} papers → 相关论文表格")
        else:
            skipped += 1

    print()
    print("─" * 55)
    print("SUMMARY")
    print("─" * 55)
    print(f"  Updated concept pages: {updated}")
    print(f"  Empty (no papers match): {empty}")
    print(f"  Skipped: {skipped}")

    if empty > 0:
        print(f"\n  Concepts with no papers yet:")
        for cf in sorted(CONCEPT_DIR.glob("*.md")):
            if cf.stem not in c2p:
                print(f"    - {cf.stem}")

    if DRY_RUN:
        print("\nDRY RUN — no changes made. Run without --dry-run to apply.")


if __name__ == "__main__":
    main()
