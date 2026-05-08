#!/usr/bin/env python3
"""
Batch add confidence field to all existing papers.
- high: Nature, Science, IEDM, VLSI, ISSCC, IEEE T-ED, IEEE EDL, Advanced Materials, Nano Letters, ACS Nano
- medium: Regular SCI journals (IEEE, AIP, AIP, etc.)
- low: arXiv preprints, conference workshops

Usage:
  python3 batch_add_confidence.py --dry-run     # Preview only
  python3 batch_add_confidence.py               # Apply changes
"""

import os
import re
import sys
from pathlib import Path
from collections import Counter

VAULT = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers")
OUTPUTS_DIR = VAULT / "Outputs"

HIGH_JOURNALS = [
    "nature", "science", "cell",
    "nature electronics", "nature nanotechnology", "nature materials", "nature photonics",
    "advanced materials", "advanced functional materials", "advanced electronic materials",
    "nano letters", "acs nano", "acs applied materials", "science advances",
    "ieee transactions on electron devices", "ieee electron device letters",
    "ieee journal of solid-state circuits",
    "applied physics letters", "journal of applied physics",
]

HIGH_CONFERENCES = [
    "IEDM", "VLSI", "ISSCC", "VLSI Technology", "VLSI Circuits",
    "International Electron Devices Meeting",
]

MEDIUM_JOURNALS = [
    "ieee", "aip", "iop", "elsevier", "springer", "wiley",
    "applied physics", "journal of", "acs", "rsc", "iop",
    "semiconductor science and technology",
    "japanese journal of applied physics",
    "microelectronic engineering",
    "solid-state electronics",
    "ieee access",
]

DRY_RUN = "--dry-run" in sys.argv


def get_journal(paper_path):
    """Extract journal field from frontmatter."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return ""
        fm = m.group(1)
        for line in fm.split("\n"):
            match = re.match(r"^journal\s*:\s*[\"']?(.*?)[\"']?\s*$", line.strip())
            if match:
                return match.group(1).strip().strip('"').strip("'")
        return ""
    except Exception:
        return ""


def has_confidence(paper_path):
    """Check if paper already has confidence field."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return True  # assume has it, skip broken files
        return "confidence:" in m.group(1)
    except Exception:
        return True


def determine_confidence(journal):
    """Determine confidence level based on journal."""
    journal_lower = journal.lower().strip()

    for hj in HIGH_JOURNALS:
        if hj in journal_lower:
            return "high"
    for hc in HIGH_CONFERENCES:
        if hc.lower() in journal_lower:
            return "high"

    for mj in MEDIUM_JOURNALS:
        if mj in journal_lower:
            return "medium"

    # arXiv / preprints
    if "arxiv" in journal_lower or "preprint" in journal_lower:
        return "low"
    # Conference proceedings (not top-tier)
    if "conference" in journal_lower or "proceedings" in journal_lower:
        return "medium"
    # Empty or unknown
    if not journal_lower:
        return "low"
    return "medium"  # Default: assume SCI journal


def add_confidence(paper_path, confidence):
    """Add confidence field to frontmatter after aiSum."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        # Find the aiSum line (last required field before closing ---)
        # Insert confidence after aiSum
        new_content = re.sub(
            r'(aiSum:.*\n)',
            rf'\1confidence: {confidence}\n',
            content,
            count=1
        )
        if new_content == content:
            # Fallback: insert before closing ---
            new_content = re.sub(
                r'(\n---\s*\n)',
                rf'\nconfidence: {confidence}\1',
                content,
                count=1
            )
        if not DRY_RUN:
            paper_path.write_text(new_content, encoding="utf-8")
        return True
    except Exception as e:
        print(f"  Error: {paper_path.name}: {e}")
        return False


def main():
    print("=" * 50)
    print("BATCH ADD CONFIDENCE FIELD")
    print("=" * 50)
    if DRY_RUN:
        print("MODE: DRY RUN (no changes will be made)")
    print()

    paper_files = [p for p in OUTPUTS_DIR.rglob("*.md") if p.parent.name == "hybrid_auto"]
    print(f"Total papers: {len(paper_files)}")

    stats = Counter()
    skipped = 0
    failed = 0

    for paper in paper_files:
        if has_confidence(paper):
            stats["already_has"] += 1
            continue

        journal = get_journal(paper)
        confidence = determine_confidence(journal)
        stats[confidence] += 1
        stats["total_processed"] += 1

        if DRY_RUN:
            print(f"  [{confidence:6s}] {paper.stem[:70]}...  (journal: {journal[:50]})")

        if not add_confidence(paper, confidence):
            failed += 1

    print()
    print("─" * 50)
    print("SUMMARY")
    print("─" * 50)
    print(f"  Already have confidence: {stats['already_has']}")
    print(f"  Added high:   {stats['high']}")
    print(f"  Added medium: {stats['medium']}")
    print(f"  Added low:    {stats['low']}")
    print(f"  Total processed: {stats['total_processed']}")
    if failed:
        print(f"  Failed: {failed}")

    if DRY_RUN:
        print()
        print("DRY RUN — no changes made. Run without --dry-run to apply.")
        # Show journal distribution
        journals = Counter()
        for paper in paper_files:
            j = get_journal(paper)
            if j:
                journals[j] += 1
        print()
        print("Journal distribution (top 15):")
        for j, c in journals.most_common(15):
            print(f"  [{determine_confidence(j):6s}] {j}: {c}")


if __name__ == "__main__":
    main()
