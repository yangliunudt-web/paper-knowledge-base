#!/usr/bin/env python3
"""
lint-wiki.py — Wiki Knowledge Layer Health Check
Checks 8 dimensions of knowledge base health.
Usage: python3 lint-wiki.py [--fix] [--report]

Based on Karpathy LLM Wiki lint workflow.
"""

import os
import re
import sys
import datetime
from pathlib import Path
from collections import defaultdict

VAULT = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers")
WIKI_DIR = VAULT / "wiki"
CONCEPT_DIR = WIKI_DIR / "概念"
OUTPUTS_DIR = VAULT / "Outputs"
TODAY = datetime.date.today().isoformat()
NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

AUTO_FIX = "--fix" in sys.argv
SAVE_REPORT = "--report" in sys.argv

# ── Controlled tag vocabulary ──
VALID_TAGS = {
    "概念", "教程", "深度", "综述", "观点", "资讯", "工具", "范式", "反模式", "案例", "基准", "最佳实践",
    "长青", "易过时", "基础", "进阶",
    "大模型", "智能体", "AI编程", "提示工程", "基础设施", "生态", "研究",
    "前端", "后端", "架构", "运维", "数据库", "安全", "团队",
    "文献", "方法论", "实验", "数据分析", "写作",
    "目录", "导航", "日志", "操作", "概览", "索引", "分组", "综合分析",
}

SKIP_PAGES = {"Wiki 目录", "操作日志", "论文分组索引", "知识库概览"}
SKIP_DEADLINK_CHECK = {"操作日志.md"}  # Documentation pages that use [[ ]] in examples

issues_count = 0
dead_links = defaultdict(list)
orphan_pages = {}
outdated_pages = {}
missing_concepts = {}
bad_tags = defaultdict(int)
all_used_tags = set()
unreferenced_papers = 0

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
CYAN = "\033[0;36m"
NC = "\033[0m"


def log_section(s):
    print(f"\n{CYAN}━━━ {s} ━━━{NC}")


def log_ok(s):
    print(f"  {GREEN}✔{NC} {s}")


def log_warn(s):
    global issues_count
    print(f"  {YELLOW}⚠{NC} {s}")
    issues_count += 1


def log_error(s):
    global issues_count
    print(f"  {RED}✘{NC} {s}")
    issues_count += 1


def frontmatter_field(filepath, field):
    """Extract a frontmatter field value from a markdown file."""
    try:
        content = filepath.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return ""
        fm = m.group(1)
        # Match the field (supports quoted and unquoted values)
        pat = rf"^{re.escape(field)}\s*:\s*(.*)"
        for line in fm.split("\n"):
            match = re.match(pat, line.strip())
            if match:
                val = match.group(1).strip().strip('"').strip("'")
                return val
        return ""
    except Exception:
        return ""


def frontmatter_list_field(filepath, field):
    """Extract a list-type frontmatter field (like keywords or tags)."""
    try:
        content = filepath.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            return []
        fm = m.group(1)
        lines = fm.split("\n")
        capturing = False
        results = []
        for line in lines:
            if re.match(rf"^{re.escape(field)}\s*:", line):
                capturing = True
                # Check if inline value like `field: [val1, val2]`
                inline = re.match(rf"^{re.escape(field)}\s*:\s*\[(.*)\]", line)
                if inline:
                    return [v.strip().strip('"').strip("'") for v in inline.group(1).split(",")]
                continue
            if capturing:
                if line.strip().startswith("- "):
                    val = line.strip()[2:].strip().strip('"').strip("'")
                    results.append(val)
                elif line.strip() == "" or re.match(r"^\w+\s*:", line):
                    break
        return results
    except Exception:
        return []


def extract_wikilinks(filepath):
    """Extract all [[wikilinks]] from a file."""
    try:
        content = filepath.read_text(encoding="utf-8")
        links = re.findall(r"\[\[([^\]]+)\]\]", content)
        # Filter out image/file links
        return [l for l in links if not re.search(r'\.(png|jpg|jpeg|pdf|excalidraw)$', l, re.IGNORECASE)]
    except Exception:
        return []


def find_page(title):
    """Find a .md file by title (case-insensitive search in vault, excluding Outputs)."""
    title = title.strip()
    # Handle [[page|display]] or [[page\|display]] (markdown table escape)
    if "\\|" in title:
        title = title.split("\\|", 1)[0].strip()
    elif "|" in title:
        title = title.split("|", 1)[0].strip()
    # Exact match first (wiki/ area)
    for md in VAULT.rglob("*.md"):
        if "Outputs" in str(md) or ".obsidian" in str(md) or ".git" in str(md):
            continue
        if md.stem == title:
            return md
    # Case-insensitive
    for md in VAULT.rglob("*.md"):
        if "Outputs" in str(md) or ".obsidian" in str(md) or ".git" in str(md):
            continue
        if md.stem.lower() == title.lower():
            return md
    # Try Outputs/
    for md in OUTPUTS_DIR.rglob("*.md"):
        if md.stem == title:
            return md
    for md in OUTPUTS_DIR.rglob("*.md"):
        if md.stem.lower() == title.lower():
            return md
    return None


def is_valid_tag(tag):
    return tag in VALID_TAGS


# ════════════════════════════════════════════
print("╔══════════════════════════════════════════╗")
print("║   WIKI KNOWLEDGE BASE HEALTH CHECK      ║")
print("╚══════════════════════════════════════════╝")
print(f"  Vault: {VAULT}")
print(f"  Time:  {NOW}")
print()

# Collect all wiki markdown files
wiki_files = list(WIKI_DIR.rglob("*.md"))
concept_files = list(CONCEPT_DIR.rglob("*.md")) if CONCEPT_DIR.exists() else []
paper_files = list(OUTPUTS_DIR.rglob("*.md"))
paper_files = [p for p in paper_files if p.parent.name == "hybrid_auto"]  # only actual papers

# ════════════════════════════════════════════
# CHECK 1: Dead Wikilinks
# ════════════════════════════════════════════
log_section("Check 1: Dead Wikilinks")

dead_count = 0
for wf in wiki_files:
    if wf.name in SKIP_DEADLINK_CHECK:
        continue
    links = extract_wikilinks(wf)
    for link in links:
        if link in SKIP_PAGES:
            continue
        target = find_page(link)
        if target is None:
            log_warn(f"Dead link in {wf.name}: [[{link}]]")
            dead_links[link].append(str(wf.relative_to(VAULT)))
            dead_count += 1

if dead_count == 0:
    log_ok("No dead wikilinks found")

# ════════════════════════════════════════════
# CHECK 2: Orphan Pages
# ════════════════════════════════════════════
log_section("Check 2: Orphan Pages (zero inbound links)")

for cf in concept_files:
    page_name = cf.stem
    incoming = 0
    for wf in wiki_files:
        content = wf.read_text(encoding="utf-8")
        incoming += content.count(f"[[{page_name}]]")
    # Also check CLAUDE.md and agent configs
    for extra in [VAULT / "CLAUDE.md"] + list((VAULT / ".agents").glob("*.md")):
        if extra.exists():
            incoming += extra.read_text(encoding="utf-8").count(f"[[{page_name}]]")
    if incoming == 0:
        log_warn(f"Orphan page: {page_name} (no inbound links)")
        orphan_pages[page_name] = True

# ════════════════════════════════════════════
# CHECK 3: Outdated Pages
# ════════════════════════════════════════════
log_section("Check 3: Outdated Pages (>30 days + 易过时 tag)")

cutoff = datetime.date.today() - datetime.timedelta(days=30)

for wf in wiki_files:
    tags_raw = frontmatter_field(wf, "tags")
    updated = frontmatter_field(wf, "updated")
    if "易过时" in tags_raw and updated:
        try:
            updated_date = datetime.date.fromisoformat(updated)
            if updated_date < cutoff:
                days_old = (datetime.date.today() - updated_date).days
                log_warn(f"Outdated: {wf.name} (updated {updated}, ~{days_old}d old, tagged 易过时)")
                outdated_pages[wf.name] = updated
        except ValueError:
            pass

# ════════════════════════════════════════════
# CHECK 4: Missing Concept Pages
# ════════════════════════════════════════════
log_section("Check 4: Missing Concept Pages (keywords >5 papers, no wiki page)")

# Build alias→concept mapping
alias_to_concept = {}
for cf in CONCEPT_DIR.glob("*.md"):
    name = cf.stem
    alias_to_concept[name.lower()] = name
    aliases_raw = frontmatter_field(cf, "aliases")
    for a in re.findall(r"[\"']?([^\"',\[\]]+)[\"']?", aliases_raw):
        a = a.strip()
        if a and a.lower() not in alias_to_concept:
            alias_to_concept[a.lower()] = name

kw_count = defaultdict(int)
for paper in paper_files:
    keywords = frontmatter_list_field(paper, "keywords")
    for kw in keywords:
        kw_clean = kw.replace("[[", "").replace("]]", "").strip()
        if kw_clean:
            kw_count[kw_clean] += 1

missing_concept_count = 0
for kw, count in sorted(kw_count.items(), key=lambda x: -x[1]):
    if count >= 5:
        # Check both direct page name match and alias match
        concept_file = find_page(kw)
        alias_match = alias_to_concept.get(kw.lower())
        if concept_file is None and alias_match is None:
            log_warn(f"Missing concept page: [[{kw}]] (appears in {count} papers)")
            missing_concepts[kw] = count
            missing_concept_count += 1

if missing_concept_count > 0:
    print(f"  → {missing_concept_count} concepts need pages created")
else:
    log_ok("All frequent keywords have concept pages")

# ════════════════════════════════════════════
# CHECK 5: Tag Consistency
# ════════════════════════════════════════════
log_section("Check 5: Tag Consistency")

bad_tag_count = 0
for wf in wiki_files:
    tags_raw = frontmatter_field(wf, "tags")
    if not tags_raw:
        log_warn(f"No tags: {wf.name}")
        bad_tag_count += 1
        continue
    # Tags can be [tag1, tag2] or tag1, tag2
    tags_str = tags_raw.strip("[]")
    for tag in tags_str.split(","):
        tag = tag.strip().strip('"').strip("'")
        if not tag:
            continue
        all_used_tags.add(tag)
        if not is_valid_tag(tag):
            log_warn(f"Non-standard tag in {wf.name}: [{tag}]")
            bad_tags[tag] += 1
            bad_tag_count += 1

if bad_tag_count == 0:
    log_ok("All tags in controlled vocabulary")

print(f"\n  Tags in use: {', '.join(sorted(all_used_tags))}")

# ════════════════════════════════════════════
# CHECK 6: Contradictory Claims
# ════════════════════════════════════════════
log_section("Check 6: Contradictory Claims (heuristic scan)")

superlatives = []
pattern = re.compile(r"(first|highest|best|record|state-of-the-art|lowest|smallest|largest)", re.IGNORECASE)
for cf in concept_files:
    try:
        for i, line in enumerate(cf.read_text(encoding="utf-8").split("\n")):
            if pattern.search(line) and not line.strip().startswith("<!--"):
                superlatives.append(f"    {cf.name}:{i+1}: {line.strip()[:100]}")
    except Exception:
        pass

if superlatives:
    print(f"  {YELLOW}⚠ Superlative claims found (manual review recommended):{NC}")
    for s in superlatives[:20]:
        print(s)
else:
    log_ok("No superlative claims flagged")

# ════════════════════════════════════════════
# CHECK 7: Papers Not Referenced in Wiki
# ════════════════════════════════════════════
log_section("Check 7: Papers Not Referenced in Wiki")

total_papers = len(paper_files)
referenced = 0

for paper in paper_files:
    paper_title = paper.stem
    for wf in wiki_files:
        try:
            if f"[[{paper_title}]]" in wf.read_text(encoding="utf-8"):
                referenced += 1
                break
        except Exception:
            pass

unreferenced = total_papers - referenced

print(f"  Total papers: {total_papers}")
print(f"  Referenced in wiki: {referenced}")
print(f"  Not referenced: {YELLOW}{unreferenced}{NC}")
if unreferenced > total_papers * 0.8:
    log_warn(">80% papers unreferenced — consider batch ingest")

# ════════════════════════════════════════════
# CHECK 8: Frontmatter Quality (Wiki Pages)
# ════════════════════════════════════════════
log_section("Check 8: Frontmatter Quality (Wiki Pages)")

fm_ok = 0
fm_bad = 0
for wf in wiki_files:
    issues = []
    if not frontmatter_field(wf, "title"):
        issues.append("missing:title")
    if not frontmatter_field(wf, "type"):
        issues.append("missing:type")
    if not frontmatter_field(wf, "tags"):
        issues.append("missing:tags")
    if not frontmatter_field(wf, "created"):
        issues.append("missing:created")
    if not frontmatter_field(wf, "updated"):
        issues.append("missing:updated")

    if issues:
        log_warn(f"{wf.name}: {', '.join(issues)}")
        fm_bad += 1
    else:
        fm_ok += 1

print(f"  OK: {fm_ok}, Issues: {fm_bad}")

# ════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════
print()
print("╔══════════════════════════════════════════╗")
print("║   LINT SUMMARY                           ║")
print("╚══════════════════════════════════════════╝")
print(f"  Date: {NOW}")
print(f"  Wiki pages: {len(wiki_files)}")
print(f"  Total papers: {total_papers}")
print(f"  Issues found: {issues_count}")
print()
print("  ┌─────────────────────┬────┐")
print(f"  │ {'Dead wikilinks':19s} │ {dead_count:2d} │")
print(f"  │ {'Orphan pages':19s} │ {len(orphan_pages):2d} │")
print(f"  │ {'Outdated pages':19s} │ {len(outdated_pages):2d} │")
print(f"  │ {'Missing concepts':19s} │ {missing_concept_count:2d} │")
print(f"  │ {'Bad tags':19s} │ {bad_tag_count:2d} │")
print(f"  │ {'Unreferenced papers':19s} │ {unreferenced:2d} │")
print("  └─────────────────────┴────┘")

if issues_count == 0:
    print(f"\n  {GREEN}✔ All checks passed!{NC}")
else:
    print(f"\n  {YELLOW}⚠ {issues_count} issue(s) need attention{NC}")

# ── Save report ──
if SAVE_REPORT:
    report_path = WIKI_DIR / f"lint-报告-{TODAY}.md"
    report = f"""---
title: "Lint 报告 {TODAY}"
type: synthesis
tags: [lint, 巡检]
created: {TODAY}
updated: {TODAY}
---

# Lint 巡检报告

> 自动生成于 {NOW}

## 检查结果

| 维度 | 问题数 |
|------|:---:|
| 死链 | {dead_count} |
| 孤页 | {len(orphan_pages)} |
| 过时页面 | {len(outdated_pages)} |
| 缺失概念页 | {missing_concept_count} |
| 违规标签 | {bad_tag_count} |
| 未引用论文 | {unreferenced} |

## 缺失概念页列表

{chr(10).join(f'- [[{kw}]] ({cnt} 篇论文)' for kw, cnt in sorted(missing_concepts.items(), key=lambda x: -x[1])[:30])}

## 建议操作

<!-- 手动审核后填入 -->

## 关联

- [[操作日志]]
- [[Wiki 目录]]
"""
    report_path.write_text(report, encoding="utf-8")
    print(f"\n  {GREEN}Report saved to: {report_path}{NC}")

sys.exit(0)
