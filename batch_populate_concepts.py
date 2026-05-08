#!/usr/bin/env python3
"""
Populate concept page "相关论文" tables from wiki_concepts data.
Reverse-lookup: for each concept, find all papers that reference it.

Filters:
  - Skips supplement/sub papers (parent: field or sub- prefix)
  - Deduplicates papers with same stem (keeps first)
  - Skips papers with uninformative aiSum placeholders

Usage:
  python3 batch_populate_concepts.py --dry-run     # Preview only
  python3 batch_populate_concepts.py               # Apply changes
"""

import re
import sys
from pathlib import Path
from collections import defaultdict, OrderedDict

VAULT = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers")
OUTPUTS_DIR = VAULT / "Outputs"
CONCEPT_DIR = VAULT / "wiki" / "概念"

DRY_RUN = "--dry-run" in sys.argv


def is_supplement(paper_path):
    """Check if paper is a supplement (has parent field or sub- prefix)."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return False
        fm = m.group(1)
        if "parent:" in fm:
            return True
        if paper_path.stem.startswith("sub-"):
            return True
        return False
    except Exception:
        return False


def get_paper_info(paper_path):
    """Extract year, confidence, and a meaningful one-line summary."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return None
        fm = m.group(1)
        year = ""
        journal = ""
        confidence = "medium"
        ai_sum = ""

        for line in fm.split("\n"):
            line = line.strip()
            if line.startswith("year:"):
                year = line.split(":", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("journal:"):
                journal = line.split(":", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("confidence:"):
                confidence = line.split(":", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("aiSum:"):
                ai_sum = line.split(":", 1)[1].strip().strip('"').strip("'")

        # Build contribution string
        if ai_sum and len(ai_sum) > 15:
            # Only filter truly empty/placeholder content (very short generic boilerplate)
            generic_patterns = [
                "一句话总结：本文针对",
                "采用铁电存储器器件，研究其在神经形态计算中的应用",
            ]
            if any(p in ai_sum for p in generic_patterns):
                contribution = journal if journal else "-"
            else:
                contribution = ai_sum[:100]
        else:
            contribution = journal if journal else "-"

        return {"year": year, "journal": journal, "contribution": contribution, "confidence": confidence}
    except Exception:
        return None


def get_wiki_concepts(paper_path):
    """Extract wiki_concepts list using yaml.safe_load."""
    try:
        import yaml
        content = paper_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return []
        fm = yaml.safe_load(m.group(1))
        if not isinstance(fm, dict):
            return []
        wc = fm.get("wiki_concepts", [])
        if isinstance(wc, list):
            return [str(v).strip().strip('"').strip("'").replace("[[", "").replace("]]", "") for v in wc]
        return []
    except Exception:
        return []


def build_concept_to_papers():
    """Build {concept_name: [(paper_stem, info), ...]} mapping, deduplicated."""
    c2p = OrderedDict()
    seen_stems = set()

    papers = [p for p in OUTPUTS_DIR.rglob("*.md") if p.parent.name == "hybrid_auto"]

    # Sort by year desc for better ordering
    paper_list = []
    for paper in papers:
        if is_supplement(paper):
            continue
        info = get_paper_info(paper)
        if info:
            paper_list.append((paper, info))
    # Sort: high confidence first, then by year desc
    conf_order = {"high": 0, "medium": 1, "low": 2}
    paper_list.sort(key=lambda x: (conf_order.get(x[1]["confidence"], 1), x[1]["year"] == "", x[1]["year"]), reverse=False)

    for paper, info in paper_list:
        stem_lower = paper.stem.lower()
        # Deduplicate: skip if exact match or if this stem starts with another seen stem
        if stem_lower in seen_stems:
            continue
        # Check for prefix duplicates (e.g. "Paper Title" and "Paper Title for Xxx")
        is_dup = False
        for seen in seen_stems:
            if stem_lower.startswith(seen) and len(stem_lower) > len(seen) + 3:
                is_dup = True
                break
            if seen.startswith(stem_lower) and len(seen) > len(stem_lower) + 3:
                is_dup = True
                break
        if is_dup:
            continue
        seen_stems.add(stem_lower)

        concepts = get_wiki_concepts(paper)
        for c in concepts:
            if c not in c2p:
                c2p[c] = []
            c2p[c].append((paper.stem, info))

    return c2p


def update_concept_page(concept_path, papers):
    """Replace the existing table with actual paper rows."""
    try:
        content = concept_path.read_text(encoding="utf-8")

        rows = []
        for title, info in papers[:12]:
            short = title[:40] + "..." if len(title) > 43 else title
            year = info["year"] or "-"
            contrib = info["contribution"]
            # Escape pipes in contribution text
            contrib = contrib.replace("|", "/")
            rows.append("| [[" + title + "\\|" + short + "]] | " + year + " | " + contrib + " |")

        new_table = "| 论文 | 年份 | 核心发现 |\n|------|------|----------|\n" + "\n".join(rows)

        # Replace old table between ## 相关论文 and ## 相关概念
        old_pattern = r'(## 相关论文\n\n)\| 论文 \| 年份 \| 核心发现 \|\n\|------\|------\|----------\|\n.*?(?=\n## 相关概念)'
        new_content = re.sub(old_pattern, r'\1' + new_table, content, flags=re.DOTALL)

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
    print("POPULATE CONCEPT PAGE PAPER TABLES (v2)")
    print("=" * 55)
    if DRY_RUN:
        print("MODE: DRY RUN (no changes will be made)")
    print()

    c2p = build_concept_to_papers()

    total_refs = sum(len(v) for v in c2p.values())
    print(f"Unique papers: {len(set(p[0] for v in c2p.values() for p in v))}")
    print(f"Concept → paper mappings: {total_refs}")
    print()

    updated = 0
    empty = 0

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
                display = [(t[:40], i['year']) for t, i in papers[:3]]
                print(f"  {name}: {count} papers → 表格  e.g. {display}")

    print()
    print("─" * 55)
    print("SUMMARY")
    print("─" * 55)
    print(f"  Updated concept pages: {updated}")
    print(f"  Empty (no papers match): {empty}")

    if empty > 0:
        print(f"\n  Concepts with no papers yet:")
        for cf in sorted(CONCEPT_DIR.glob("*.md")):
            if cf.stem not in c2p:
                print(f"    - {cf.stem}")

    if DRY_RUN:
        print("\nDRY RUN — no changes made. Run without --dry-run to apply.")


if __name__ == "__main__":
    main()
