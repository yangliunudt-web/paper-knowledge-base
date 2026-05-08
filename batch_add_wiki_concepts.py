#!/usr/bin/env python3
"""
Batch add wiki_concepts field to all existing papers.
Maps paper keywords AND body-text wikilinks → wiki concept pages (checking aliases).
Only adds concepts that actually have wiki pages.

When a concept appears as a body-text [[wikilink]] ≥2 times and matches a wiki page,
it's also added to the paper's keywords list.

Usage:
  python3 batch_add_wiki_concepts.py --dry-run     # Preview only
  python3 batch_add_wiki_concepts.py               # Apply changes
  python3 batch_add_wiki_concepts.py --body-only   # Only scan body text (skip frontmatter keywords)
"""

import re
import sys
from pathlib import Path
from collections import Counter

VAULT = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers")
OUTPUTS_DIR = VAULT / "Outputs"
CONCEPT_DIR = VAULT / "wiki" / "概念"

DRY_RUN = "--dry-run" in sys.argv
BODY_ONLY = "--body-only" in sys.argv


def load_concept_aliases():
    """Build {alias → concept_page_name} mapping from all concept pages."""
    alias_map = {}
    for cf in CONCEPT_DIR.glob("*.md"):
        name = cf.stem
        alias_map[name.lower()] = name
        try:
            content = cf.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if not m:
                continue
            fm = m.group(1)
            for line in fm.split("\n"):
                if "aliases:" in line:
                    aliases_str = line.split(":", 1)[1].strip()
                    if aliases_str.startswith("["):
                        vals = re.findall(r"[\"']?([^\"',\[\]]+)[\"']?", aliases_str)
                        for v in vals:
                            v = v.strip()
                            if v and v.lower() not in alias_map:
                                alias_map[v.lower()] = name
        except Exception:
            pass
    return alias_map


def split_frontmatter_and_body(content):
    """Return (frontmatter_text, body_text) for a markdown file."""
    # Find the second --- (closing frontmatter)
    parts = content.split("---", 2)
    if len(parts) >= 3:
        return parts[1], parts[2]
    return "", content


def extract_frontmatter_keywords(paper_path):
    """Get list of keyword strings (without [[ ]]) from frontmatter."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        fm, _ = split_frontmatter_and_body(content)
        keywords = re.findall(r"\[\[(.*?)\]\]", fm)
        return [kw.strip() for kw in keywords]
    except Exception:
        return []


def extract_body_wikilinks(paper_path):
    """Get [[wikilinks]] from body text (after frontmatter), with occurrence count."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        _, body = split_frontmatter_and_body(content)
        links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", body)
        # Count occurrences, filter out file/image links
        counter = Counter()
        for l in links:
            l = l.strip()
            if re.search(r'\.(png|jpg|jpeg|pdf|excalidraw)$', l, re.IGNORECASE):
                continue
            counter[l] += 1
        return counter
    except Exception:
        return Counter()


def current_keywords_list(paper_path):
    """Get existing keywords as a list of strings (with [[ ]])."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return []
        fm = m.group(1)
        # Find the keywords: section
        kw_match = re.search(r'keywords:\s*\n((?:\s*-.*\n)*)', fm)
        if kw_match:
            kws = re.findall(r'-\s*"(\[\[[^\]]+\]\])"', kw_match.group(1))
            return kws
        return []
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


def map_to_concepts(terms, alias_map):
    """Map a list of terms to wiki concept page names via aliases."""
    concepts = set()
    for t in terms:
        name = alias_map.get(t.lower())
        if name:
            concepts.add(name)
    return sorted(concepts)


def add_wiki_concepts(paper_path, concepts):
    """Add or update wiki_concepts field using safe rebuild (never breaks frontmatter)."""
    try:
        # Use repair_frontmatter's safe rebuild approach
        sys.path.insert(0, str(VAULT))
        from repair_frontmatter import rebuild_frontmatter, extract_field

        content = paper_path.read_text(encoding="utf-8")

        # Get existing wiki_concepts
        existing = set(extract_field(content, "wiki_concepts"))
        all_concepts = existing | set(concepts)

        if all_concepts == existing:
            return False  # No change needed

        # Rebuild with safe function
        new_content = rebuild_frontmatter(content)

        # Now update wiki_concepts in the rebuilt content
        concept_lines = "\n".join(f'  - "[[{c}]]"' for c in sorted(all_concepts))
        new_field = f"wiki_concepts:\n{concept_lines}"

        # Replace the wiki_concepts block (always present in rebuilt content)
        new_content = re.sub(
            r'wiki_concepts:\s*\n(?:.*\n)*?(?=\n\S|\n---)',
            new_field + '\n',
            new_content,
            count=1,
            flags=re.DOTALL
        )

        if not DRY_RUN:
            paper_path.write_text(new_content, encoding="utf-8")
        return True
    except Exception as e:
        print(f"  Error: {paper_path.name}: {e}")
        return False


def add_keywords_to_frontmatter(paper_path, new_keywords):
    """Add new keywords using safe rebuild approach."""
    try:
        from repair_frontmatter import rebuild_frontmatter, extract_field

        content = paper_path.read_text(encoding="utf-8")
        existing = set(extract_field(content, "keywords"))
        all_keywords = existing | set(new_keywords)

        if all_keywords == existing:
            return False, 0

        # Rebuild with correct frontmatter
        new_content = rebuild_frontmatter(content)

        # Replace keywords block
        kw_lines = "\n".join(f'  - "[[{kw}]]"' for kw in sorted(all_keywords))
        new_field = f"keywords:\n{kw_lines}"

        new_content = re.sub(
            r'keywords:\s*\n(?:.*\n)*?(?=\n\S|\n---)',
            new_field + '\n',
            new_content,
            count=1,
            flags=re.DOTALL
        )

        if not DRY_RUN:
            paper_path.write_text(new_content, encoding="utf-8")
        return True, len(all_keywords) - len(existing)
    except Exception as e:
        print(f"  Error adding keywords to {paper_path.name}: {e}")
        return False, 0


def main():
    print("=" * 55)
    print("BATCH ADD wiki_concepts FIELD (v2 — body text aware)")
    print("=" * 55)
    if DRY_RUN:
        print("MODE: DRY RUN (no changes will be made)")
    if BODY_ONLY:
        print("MODE: Body text only (skip existing keywords)")
    print()

    alias_map = load_concept_aliases()
    print(f"Loaded {len(alias_map)} aliases from {len(list(CONCEPT_DIR.glob('*.md')))} concept pages")
    print()

    paper_files = [p for p in OUTPUTS_DIR.rglob("*.md") if p.parent.name == "hybrid_auto"]
    print(f"Total papers: {len(paper_files)}")

    stats = {"already_ok": 0, "updated_wc": 0, "updated_kw": 0, "no_match": 0, "new_body_hits": 0}
    body_hit_examples = []

    for paper in paper_files:
        # Collect concepts from all sources
        all_concepts = set()

        # Source 1: frontmatter keywords (unless --body-only)
        if not BODY_ONLY:
            fm_keywords = extract_frontmatter_keywords(paper)
            fm_concepts = map_to_concepts(fm_keywords, alias_map)
            all_concepts.update(fm_concepts)

        # Source 2: body text wikilinks (appear ≥2 times)
        body_links = extract_body_wikilinks(paper)
        body_concepts = set()
        for term, count in body_links.items():
            if count >= 2:
                name = alias_map.get(term.lower())
                if name:
                    body_concepts.add(name)

        old_concepts = all_concepts.copy()
        all_concepts.update(body_concepts)
        new_from_body = all_concepts - old_concepts

        if not all_concepts:
            stats["no_match"] += 1
            continue

        # Re-read current wiki_concepts to check if update needed
        existing_wc = set()
        try:
            content = paper.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if m:
                wc_match = re.findall(r'\[\[(.*?)\]\]', re.search(r'wiki_concepts:\s*\n((?:.*\n)*?)(?=\n\S|\n---|\n\w+:|$)', m.group(1)).group(1) if re.search(r'wiki_concepts:\s*\n((?:.*\n)*?)(?=\n\S|\n---|\n\w+:|$)', m.group(1)) else '')
                existing_wc = set(wc_match)
        except Exception:
            pass

        # Update wiki_concepts if new concepts found
        if all_concepts != existing_wc:
            if add_wiki_concepts(paper, sorted(all_concepts)):
                stats["updated_wc"] += 1
                if new_from_body:
                    stats["new_body_hits"] += 1
                    if len(body_hit_examples) < 8:
                        body_hit_examples.append((paper.stem[:50], sorted(new_from_body)))
        else:
            stats["already_ok"] += 1

        # Add new body concepts to keywords list
        if new_from_body:
            added, count = add_keywords_to_frontmatter(paper, sorted(new_from_body))
            if added:
                stats["updated_kw"] += 1

    print()
    print("─" * 55)
    print("SUMMARY")
    print("─" * 55)
    print(f"  Already up to date:        {stats['already_ok']}")
    print(f"  Updated wiki_concepts:     {stats['updated_wc']}")
    print(f"  New from body text:        {stats['new_body_hits']} papers")
    print(f"  Keywords updated:          {stats['updated_kw']} papers")
    print(f"  No matching concepts:      {stats['no_match']}")

    if body_hit_examples:
        print(f"\n  Papers with body-text concept hits:")
        for title, concepts in body_hit_examples:
            print(f"    {title}...")
            print(f"      +keywords: {concepts}")

    if DRY_RUN:
        print("\nDRY RUN — no changes made. Run without --dry-run to apply.")


if __name__ == "__main__":
    main()
