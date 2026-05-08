#!/usr/bin/env python3
"""
Unified knowledge base maintenance tool.
One command to check and fix everything.

Usage:
  python3 maintain.py --check        Read-only: run all checks, show report
  python3 maintain.py --fix          Run checks + apply auto-fixes
  python3 maintain.py --phase 2      Run only phase 2 (keyword quality)
  python3 maintain.py --phase 3 --fix Run only phase 3 with auto-fix
  python3 maintain.py --check --json Output machine-readable report

Phases:
  1  Frontmatter format
  2  Keyword quality
  3  Journal name consistency
  4  Body text quality
  5  Wiki layer health
  6  Wiki data sync

Checks (6 phases):
  1. Frontmatter format    — check_frontmatter.sh + deep_quality_check.py
  2. Keyword quality       — generic terms, paper-title-as-keyword, language balance
  3. Journal consistency   — detect name variants
  4. Body text quality     — LaTeX errors, short body, broken images
  5. Wiki layer health     — lint-wiki.py 8 dimensions
  6. Wiki data sync        — wiki_concepts + concept page tables
"""

import subprocess
import sys
import os
import json
import re
import datetime
from pathlib import Path
from collections import Counter, defaultdict

VAULT = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers")
OUTPUTS_DIR = VAULT / "Outputs"
CONCEPT_DIR = VAULT / "wiki" / "概念"
TODAY = datetime.date.today().isoformat()

CHECK_ONLY = "--check" in sys.argv or "--fix" not in sys.argv
FIX_MODE = "--fix" in sys.argv
JSON_OUT = "--json" in sys.argv
PHASE_ONLY = None
for a in sys.argv:
    if a.startswith("--phase="):
        PHASE_ONLY = int(a.split("=")[1])
    elif a == "--phase":
        idx = sys.argv.index("--phase")
        if idx + 1 < len(sys.argv):
            PHASE_ONLY = int(sys.argv[idx + 1])

report = {"phases": {}, "summary": {}}


def run(cmd, timeout=120):
    """Run a shell command, return (returncode, stdout)."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout, cwd=str(VAULT))
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"
    except Exception as e:
        return -1, "", str(e)


def phase(name, func):
    """Run a check phase and record results."""
    print(f"\n{'='*55}")
    print(f"  PHASE: {name}")
    print(f"{'='*55}")
    try:
        result = func()
        report["phases"][name] = result
        return result
    except Exception as e:
        print(f"  ERROR: {e}")
        report["phases"][name] = {"error": str(e)}
        return {"error": str(e)}


ISSUE_FIELDS = {
    "fm_format_failures", "fm_missing", "deep_quality_issues",
    "generic", "title_as_keyword", "single_language",
    "inconsistent",
    "short_body", "latex_issues", "broken_images",
    "total_issues", "dead_links", "orphans", "outdated", "missing_concepts", "bad_tags", "unreferenced",
    "missing_wc", "concept_table_outdated",
}

def count_issues(phase_result):
    """Count total issues from a phase result dict."""
    if not phase_result or "error" in phase_result:
        return 0
    return sum(v for k, v in phase_result.items() if k in ISSUE_FIELDS and isinstance(v, int))


# ════════════════════════════════════════════
# Phase 1: Frontmatter Format
# ════════════════════════════════════════════
def check_frontmatter():
    result = {}
    print("  Running check_frontmatter.sh...")
    rc, out, err = run("bash check_frontmatter.sh", timeout=60)
    # Parse output: count FAIL lines
    fail_count = out.count("FAIL |")
    fm_missing = out.count("MISSING-FM")
    result["fm_format_failures"] = fail_count
    result["fm_missing"] = fm_missing

    print("  Running deep_quality_check.py...")
    rc, out, err = run("python3 deep_quality_check.py", timeout=120)
    # Parse last line for summary
    total_issues = 0
    for line in out.strip().split("\n"):
        if "issues found" in line.lower() or "total" in line.lower():
            try:
                total_issues = int(re.search(r'(\d+)', line).group(1))
            except:
                pass
    result["deep_quality_issues"] = total_issues

    print(f"  → Frontmatter format: {fail_count} failures, {fm_missing} missing FM, {total_issues} quality issues")
    return result


# ════════════════════════════════════════════
# Phase 2: Keyword Quality
# ════════════════════════════════════════════
GENERIC_TERMS = {
    "memory", "learning", "power", "performance", "integration", "reliability",
    "training", "design", "optimization", "application", "demonstration",
    "device", "devices", "system", "systems", "technology", "semiconductor",
    "memory", "computation", "computing", "electronics", "fabrication",
    "Memory", "Learning", "Power", "Integration", "Performance",
}

def check_keywords():
    result = {"generic": 0, "title_as_keyword": 0, "single_language": 0, "total_papers": 0}
    generic_examples = []
    title_kw_examples = []
    lang_examples = []

    for paper in OUTPUTS_DIR.rglob("*.md"):
        if paper.parent.name != "hybrid_auto":
            continue
        result["total_papers"] += 1
        try:
            content = paper.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if not m:
                continue
            fm = m.group(1)
            # Extract keywords
            kw_match = re.search(r'keywords:\s*\n((?:\s*-.*\n)*)', fm)
            if not kw_match:
                continue
            kws = re.findall(r'\[\[(.*?)\]\]', kw_match.group(1))
            has_cn = any(re.search(r'[一-鿿]', k) for k in kws)
            has_en = any(re.search(r'[a-zA-Z]', k) for k in kws)

            # Check generic terms
            for kw in kws:
                kw_clean = kw.strip()
                if kw_clean in GENERIC_TERMS:
                    result["generic"] += 1
                    if len(generic_examples) < 5:
                        generic_examples.append((paper.stem[:40], kw_clean))
                if len(kw_clean) > 60:
                    result["title_as_keyword"] += 1
                    if len(title_kw_examples) < 5:
                        title_kw_examples.append((paper.stem[:40], kw_clean[:60]))

            # Check language balance
            if has_cn and not has_en:
                result["single_language"] += 1
                if len(lang_examples) < 5:
                    lang_examples.append((paper.stem[:40], "仅中文"))
            elif has_en and not has_cn:
                result["single_language"] += 1
                if len(lang_examples) < 5:
                    lang_examples.append((paper.stem[:40], "仅英文"))
        except:
            pass

    print(f"  → Generic keywords: {result['generic']}, Title-as-keyword: {result['title_as_keyword']}")
    print(f"  → Single-language: {result['single_language']}")

    if generic_examples:
        print("  Generic examples:")
        for t, k in generic_examples[:3]:
            print(f"    [[{k}]] in {t}...")
    if title_kw_examples:
        print("  Title-as-keyword examples:")
        for t, k in title_kw_examples[:3]:
            print(f"    {k}... in {t}...")

    # Auto-fix in --fix mode: only report, don't auto-delete (too risky for YAML integrity)
    return result


# ════════════════════════════════════════════
# Phase 3: Journal Name Consistency
# ════════════════════════════════════════════
JOURNAL_MAP = {
    "IEEE Transactions on Electron Devices": ["IEEE Trans. Electron Devices", "IEEE T-ED", "IEEE Trans Electron Devices", "IEEE Transactions on Electron Device"],
    "IEEE Electron Device Letters": ["IEEE EDL", "IEEE Electron Device Letter", "IEEE Elect. Dev. Lett."],
    "Nature Communications": ["Nature Comms", "Nature Comms.", "Nat. Commun.", "Nature communication"],
    "Science Advances": ["Sci. Adv.", "Science Advance"],
    "Advanced Materials": ["Adv. Mater.", "Advanced Material"],
    "Nano Letters": ["Nano Lett."],
    "ACS Nano": ["ACS Nano."],
    "Applied Physics Letters": ["Appl. Phys. Lett.", "APL", "Applied Physics Letter"],
    "Journal of Applied Physics": ["J. Appl. Phys.", "Journal of Applied Physic"],
    "Scientific Reports": ["Sci. Rep.", "Scientific Report"],
    "ACS Applied Materials & Interfaces": ["ACS Appl. Mater. Interfaces", "ACS AMI", "ACS Applied Materials and Interfaces"],
    "Advanced Functional Materials": ["Adv. Funct. Mater."],
    "Nature Electronics": ["Nat. Electron.", "Nature Electronic"],
    "Nature": [],
    "Science": [],
    "Neuromorphic Computing and Engineering": ["NCE"],
    "IEEE Access": [],
    "Proceedings of the IEEE": ["Proc. IEEE"],
    "Nature Reviews Materials": ["Nat. Rev. Mater.", "Nature Reviews Material"],
    "Nature Nanotechnology": ["Nat. Nanotechnol."],
    "Science Robotics": ["Sci. Robot."],
}

def build_journal_lookup():
    """Build {variant_lower → standard_name} from JOURNAL_MAP."""
    lookup = {}
    for standard, variants in JOURNAL_MAP.items():
        lookup[standard.lower()] = standard
        for v in variants:
            lookup[v.lower()] = standard
    return lookup


def check_journals():
    result = {"inconsistent": 0, "unknown": 0, "unique_journals": 0}
    journals = Counter()
    lookup = build_journal_lookup()

    for paper in OUTPUTS_DIR.rglob("*.md"):
        if paper.parent.name != "hybrid_auto":
            continue
        try:
            content = paper.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if not m:
                continue
            fm = m.group(1)
            jm = re.search(r'journal:\s*"?(.*?)"?\s*$', fm, re.MULTILINE)
            if jm:
                journals[jm.group(1).strip()] += 1
        except:
            pass

    result["unique_journals"] = len(journals)
    # Count journals not in lookup
    for j, c in journals.most_common():
        std = lookup.get(j.lower())
        if std and std.lower() != j.lower():
            result["inconsistent"] += 1

    print(f"  → {result['unique_journals']} unique journal names, {result['inconsistent']} non-standard variants")

    # Show top variants
    if result["inconsistent"] > 0:
        print("  Non-standard variants:")
        shown = 0
        for j, c in journals.most_common():
            std = lookup.get(j.lower())
            if std and std.lower() != j.lower():
                print(f"    '{j}' → '{std}' ({c} papers)")
                shown += 1
                if shown >= 8:
                    break

    # Auto-fix in --fix mode
    if FIX_MODE and result["inconsistent"] > 0:
        print("  → Auto-fixing journal names...")
        fixed = fix_journals(lookup)
        result["fixed_papers"] = fixed

    return result


def fix_journals(lookup):
    """Normalize journal names to standard forms."""
    fixed = 0
    for paper in OUTPUTS_DIR.rglob("*.md"):
        if paper.parent.name != "hybrid_auto":
            continue
        try:
            content = paper.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if not m:
                continue
            fm = m.group(1)
            jm = re.search(r'(journal:\s*)"?(.*?)"?\s*$', fm, re.MULTILINE)
            if not jm:
                continue
            current = jm.group(2).strip()
            std = lookup.get(current.lower())
            if std and std.lower() != current.lower():
                new_content = content.replace(f'journal: "{current}"', f'journal: "{std}"')
                new_content = new_content.replace(f"journal: '{current}'", f'journal: "{std}"')
                new_content = new_content.replace(f"journal: {current}", f'journal: "{std}"')
                if new_content != content:
                    paper.write_text(new_content, encoding="utf-8")
                    fixed += 1
        except:
            pass
    return fixed


# ════════════════════════════════════════════
# Phase 4: Body Text Quality
# ════════════════════════════════════════════
def check_body_text():
    result = {"short_body": 0, "latex_issues": 0, "broken_images": 0, "total_papers": 0}
    short_examples = []
    latex_examples = []

    for paper in OUTPUTS_DIR.rglob("*.md"):
        if paper.parent.name != "hybrid_auto":
            continue
        result["total_papers"] += 1
        try:
            content = paper.read_text(encoding="utf-8")
            _, body = split_fm_body(content)

            # Check body length
            lines = [l for l in body.split("\n") if l.strip() and not l.strip().startswith("!")]
            if len(lines) < 50:
                result["short_body"] += 1
                if len(short_examples) < 5:
                    short_examples.append((paper.stem[:50], len(lines)))

            # Check LaTeX: unmatched $ signs
            dollar_count = body.count("$") - body.count("$$") * 2
            if dollar_count % 2 != 0:
                result["latex_issues"] += 1
                if len(latex_examples) < 5:
                    latex_examples.append((paper.stem[:50], "unmatched $"))

            # Check LaTeX: common typos
            for bad in [r'\mathxx', r'\mathrrm', r'\mathrmm', r'\mathbff']:
                if bad in body:
                    result["latex_issues"] += 1
                    if len(latex_examples) < 5:
                        latex_examples.append((paper.stem[:50], f"typo: {bad}"))

            # Check broken image references
            imgs = re.findall(r'!\[\[([^\]]+)\]\]', body)
            for img in imgs:
                img_path = paper.parent / img
                if not img_path.exists():
                    result["broken_images"] += 1
                    break  # one per paper
        except:
            pass

    print(f"  → Short bodies (<50 lines): {result['short_body']}")
    print(f"  → LaTeX issues: {result['latex_issues']}")
    print(f"  → Broken images: {result['broken_images']}")

    if short_examples:
        print("  Short body examples:")
        for t, n in short_examples[:3]:
            print(f"    {t}... ({n} lines)")

    return result


def split_fm_body(content):
    parts = content.split("---", 2)
    if len(parts) >= 3:
        return parts[1], parts[2]
    return "", content


# ════════════════════════════════════════════
# Phase 5: Wiki Layer Health
# ════════════════════════════════════════════
def check_wiki_health():
    print("  Running lint-wiki.py...")
    rc, out, err = run("python3 lint-wiki.py", timeout=120)

    # Parse summary table
    result = {"dead_links": 0, "orphans": 0, "outdated": 0, "missing_concepts": 0,
              "bad_tags": 0, "unreferenced": 0, "total_issues": 0}
    for line in out.split("\n"):
        if "Dead wikilinks" in line:
            result["dead_links"] = int(re.search(r'(\d+)', line).group(1))
        elif "Orphan pages" in line:
            result["orphans"] = int(re.search(r'(\d+)', line).group(1))
        elif "Outdated pages" in line:
            result["outdated"] = int(re.search(r'(\d+)', line).group(1))
        elif "Missing concepts" in line:
            result["missing_concepts"] = int(re.search(r'(\d+)', line).group(1))
        elif "Bad tags" in line:
            result["bad_tags"] = int(re.search(r'(\d+)', line).group(1))
        elif "Unreferenced papers" in line:
            result["unreferenced"] = int(re.search(r'(\d+)', line).group(1))
        elif "Issues found" in line:
            result["total_issues"] = int(re.search(r'(\d+)', line).group(1))

    print(f"  → Wiki lint: {result['total_issues']} issues (dead:{result['dead_links']} orphan:{result['orphans']} outdated:{result['outdated']} missing_concept:{result['missing_concepts']})")
    return result


# ════════════════════════════════════════════
# Phase 6: Wiki Data Sync
# ════════════════════════════════════════════
def check_wiki_sync():
    result = {"missing_wc": 0, "concept_table_outdated": 0}

    # Count papers without wiki_concepts
    for paper in OUTPUTS_DIR.rglob("*.md"):
        if paper.parent.name != "hybrid_auto":
            continue
        try:
            content = paper.read_text(encoding="utf-8")
            fm, _ = split_fm_body(content)
            if "wiki_concepts:" not in fm:
                result["missing_wc"] += 1
        except:
            pass

    print(f"  → Papers without wiki_concepts: {result['missing_wc']}")

    if FIX_MODE and result["missing_wc"] > 0:
        print("  → Running batch_add_wiki_concepts.py...")
        rc, out, err = run("python3 batch_add_wiki_concepts.py", timeout=120)
        print("  → Running batch_populate_concepts.py...")
        rc, out2, err2 = run("python3 batch_populate_concepts.py", timeout=120)
        result["synced"] = True

    return result


# ════════════════════════════════════════════
# Main
# ════════════════════════════════════════════
def main():
    mode = "CHECK (read-only)" if CHECK_ONLY else "FIX (auto-repair)"
    print("╔══════════════════════════════════════════╗")
    print("║   KNOWLEDGE BASE MAINTENANCE            ║")
    print("╚══════════════════════════════════════════╝")
    print(f"  Mode: {mode}")
    print(f"  Date: {TODAY}")
    print(f"  Vault: {VAULT}")

    all_phases = [
        ("1. Frontmatter Format", check_frontmatter),
        ("2. Keyword Quality", check_keywords),
        ("3. Journal Name Consistency", check_journals),
        ("4. Body Text Quality", check_body_text),
        ("5. Wiki Layer Health", check_wiki_health),
        ("6. Wiki Data Sync", check_wiki_sync),
    ]

    results = {}
    for i, (name, func) in enumerate(all_phases, 1):
        if PHASE_ONLY and i != PHASE_ONLY:
            continue
        results[i] = phase(name, func)

    # Summary
    total = 0
    for i, (name, _) in enumerate(all_phases, 1):
        if PHASE_ONLY and i != PHASE_ONLY:
            continue
        if i == 5:
            total += results.get(i, {}).get("total_issues", 0)
        else:
            total += count_issues(results.get(i, {}))

    print(f"\n{'='*55}")
    print(f"  MAINTENANCE SUMMARY")
    print(f"{'='*55}")
    labels = ["1. Frontmatter", "2. Keywords", "3. Journal names", "4. Body text", "5. Wiki health", "6. Wiki sync"]
    for i, (name, _) in enumerate(all_phases, 1):
        if PHASE_ONLY and i != PHASE_ONLY:
            continue
        ci = count_issues(results.get(i, {}))
        if i == 5:
            ci = results.get(i, {}).get("total_issues", 0)
        print(f"  {labels[i-1]:22s} {ci:4d} issues")
    print(f"  {'─'*28}")
    print(f"  TOTAL:                {total:4d} issues")

    if CHECK_ONLY:
        print(f"\n  Run 'python3 maintain.py --fix' to auto-repair detected issues.")

    if JSON_OUT:
        report["summary"]["total_issues"] = total
        report["summary"]["mode"] = mode
        report["summary"]["date"] = TODAY
        out_path = VAULT / f"maintain-report-{TODAY}.json"
        json.dump(report, open(out_path, "w"), indent=2, ensure_ascii=False)
        print(f"\n  JSON report saved to: {out_path}")


if __name__ == "__main__":
    main()
