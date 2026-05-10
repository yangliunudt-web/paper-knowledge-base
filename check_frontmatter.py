#!/usr/bin/env python3
"""
Frontmatter Quality Checker v2 — CLAUDE.md 规范逐条对照
================================================================
FAIL: YAML 结构错误、缺失必填字段、数据完整性风险 — 必须修复
WARN: wikilink 死链、摘要截断、格式不规范 — 应该修复
INFO: 改进建议 — 非强制

覆盖 gap（原 check_frontmatter.sh 未覆盖）:
   YAML 重复 key / 孤儿列表项 / [[[[...]]]] / 作者 artifact
   日期-年份一致性 / 摘要截断 / LaTeX 残留 / cite 格式
   wiki_concepts 覆盖率 / 死 wikilink / 前端多余空行
"""

import os, re, sys, yaml
from collections import Counter

VAULT = "/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers"
OUTPUTS = os.path.join(VAULT, "Outputs")
WIKI_CONCEPTS = os.path.join(VAULT, "wiki/概念")

REQUIRED_FIELDS = ["title", "authors", "date", "year", "journal",
                   "abstract", "abstract_cn", "cite", "aiSum", "keywords"]
VALID_CONFIDENCE = {"high", "medium", "low"}

# ── helpers ──────────────────────────────────────────────

def load_concept_aliases():
    """Return {lower_alias} -> page_name for all concept pages."""
    aliases = {}
    if not os.path.isdir(WIKI_CONCEPTS):
        return aliases
    for f in os.listdir(WIKI_CONCEPTS):
        if not f.endswith(".md"):
            continue
        path = os.path.join(WIKI_CONCEPTS, f)
        try:
            with open(path) as fh:
                content = fh.read()
        except:
            continue
        m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except:
            continue
        name = fm.get("title", f.replace(".md", ""))
        aliases[str(name).lower()] = str(name)
        for a in (fm.get("aliases") or []):
            aliases[str(a).lower()] = str(name)
    return aliases


def concept_exists(target, alias_map):
    """Check a wikilink target against concept aliases."""
    return target.lower().strip() in alias_map


def check_yaml(fm_text):
    """Return (errors: list[str]) — empty means OK."""
    errors = []
    # 1) Structural YAML parse
    try:
        parsed = yaml.safe_load(fm_text)
        if not isinstance(parsed, dict):
            errors.append("YAML-PARSE: not a mapping")
    except yaml.YAMLError as e:
        errors.append(f"YAML-PARSE: {str(e)[:100]}")
        return errors  # can't continue checking

    # 2) Duplicate keys (double-check manually — yaml.safe_load may silently merge)
    keys_seen = {}
    for line in fm_text.split("\n"):
        m = re.match(r'^(\w+):', line)
        if m:
            key = m.group(1)
            if key in keys_seen:
                errors.append(f"DUPLICATE-KEY: {key}")
            keys_seen[key] = True

    # 3) Orphaned list items (e.g. "- [[X]]" after a scalar string field)
    lines = fm_text.split("\n")
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("- ") and i > 0:
            prev = lines[i - 1].strip()
            if re.match(r'^\w+:\s*".*"$', prev):
                errors.append(f"ORPHANED-ITEM: line {i+1} after scalar at line {i}")
                break
    return errors


def is_supplement(filepath, fm_text):
    return bool(
        re.search(r'parent:\s', fm_text)
        or os.path.basename(filepath).startswith("sub-")
        or "-sm/" in filepath or "_sm/" in filepath
        or "Supplementary" in os.path.basename(filepath)
        or "Reference" in filepath
    )


def check_all(verbose=False):
    alias_map = load_concept_aliases()
    print(f"概念页: {len(alias_map)} 别名 — {len(set(alias_map.values()))} 个唯一页面\n")

    results = []  # (path, errors, warnings)
    stats_err = Counter()
    stats_warn = Counter()

    for root, dirs, files in os.walk(OUTPUTS):
        if ".claude" in root:
            continue
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            filepath = os.path.join(root, f)
            try:
                with open(filepath) as fh:
                    content = fh.read()
            except:
                continue

            fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if not fm_match:
                # Only flag if this looks like it SHOULD have frontmatter
                if not os.path.basename(filepath).startswith("README"):
                    results.append((filepath, ["NO-FRONTMATTER"], []))
                    stats_err["NO-FRONTMATTER"] += 1
                continue

            fm_text = fm_match.group(1)
            errors = []
            warnings = []
            supp = is_supplement(filepath, fm_text)

            # ── FAIL-level checks ──────────────────────────

            # 0) Blank line after opening ---
            if content.startswith("---\n\n"):
                warnings.append("format: frontmatter 首行后多余空行")

            # 1) YAML integrity
            yaml_errs = check_yaml(fm_text)
            errors.extend(yaml_errs)

            # 2) Required fields (all 10 must exist and be non-empty)
            for field in REQUIRED_FIELDS:
                if not re.search(rf'^{field}:\s', fm_text, re.MULTILINE):
                    errors.append(f"missing: {field}")
                elif re.search(rf'^{field}:\s*""?\s*$', fm_text, re.MULTILINE):
                    errors.append(f"empty: {field}")

            # 3) authors must be a YAML list
            auth_sec = re.search(r'^authors:\s*\n((?:\s+-.*\n?)*)', fm_text, re.MULTILINE)
            if auth_sec:
                auth_block = auth_sec.group(1)
                if not re.search(r'^\s+-', auth_block, re.MULTILINE):
                    errors.append("authors: not a YAML list")
                # Author artifacts from PDF extraction
                for line in auth_block.split("\n"):
                    if re.search(r'\{\s*\}', line):
                        warnings.append(f"authors: PDF artifact {{}} in '{line.strip()[:50]}'")
            elif re.search(r'^authors:\s*"[^"]*"', fm_text, re.MULTILINE):
                if '[' not in fm_text.split('authors:')[1].split('\n')[0]:
                    errors.append("authors: not a YAML list (single string)")

            # 4) Single-quoted YAML values (real issue, not apostrophes in text)
            for line in fm_text.split("\n"):
                if re.search(r':\s*\'[^\']*\'', line):
                    errors.append("format: single-quoted YAML value")
                    break

            # 5) Double-bracketed wikilinks
            if "[[[[" in fm_text or "]]]]" in fm_text:
                errors.append("wikilinks: double-bracketed [[[[...]]]]")

            # 6) cite completeness
            cite_m = re.search(r'^cite:\s*"(.*?)"', fm_text, re.MULTILINE)
            cite_text = ""
            if cite_m:
                cite_text = cite_m.group(1)
                if cite_text.startswith("待补充"):
                    errors.append("cite: 待补充 — 需要填写完整引用")
                elif len(cite_text) < 20:
                    errors.append("cite: too short (<20 chars)")

            # 7) date-year consistency
            date_m = re.search(r'^date:\s*"(\d{4})-', fm_text, re.MULTILINE)
            year_m = re.search(r'^year:\s*(\d{4})', fm_text, re.MULTILINE)
            if date_m and year_m and date_m.group(1) != year_m.group(1):
                errors.append(f"date-year: date={date_m.group(1)} vs year={year_m.group(1)}")

            # 8) confidence value
            conf_m = re.search(r'^confidence:\s*"?(\w+)"?', fm_text, re.MULTILINE)
            if conf_m and conf_m.group(1).lower() not in VALID_CONFIDENCE:
                errors.append(f"confidence: invalid value '{conf_m.group(1)}'")

            # ── WARN-level checks ──────────────────────────

            # 9) Keywords should use wikilinks
            kw_match = re.search(r'^keywords:\s*\n((?:\s+-.*\n?)*)', fm_text, re.MULTILINE)
            if kw_match:
                kw_block = kw_match.group(1)
                if "[[" not in kw_block:
                    warnings.append("keywords: no wikilinks (should use [[...]])")

            # 10) wiki_concepts coverage (soft requirement for non-supplements)
            if not supp:
                wc_match = re.search(r'^wiki_concepts:\s*\n((?:\s+-.*\n?)*)', fm_text, re.MULTILINE)
                if not wc_match:
                    warnings.append("wiki_concepts: missing (建议添加)")
                else:
                    wc_block = wc_match.group(1)
                    dead = []
                    for wc in re.findall(r'\[\[([^\[\]]+)\]\]', wc_block):
                        if not concept_exists(wc.split("|")[0].strip(), alias_map):
                            dead.append(wc.split("|")[0].strip())
                    if dead:
                        errors.append(f"wiki_concepts: dead links -> {', '.join(dead)}")

            # 11) Dead wikilinks in keywords (WARN only — informational)
            if kw_match:
                kw_dead = []
                for kw in re.findall(r'\[\[([^\[\]]+)\]\]', kw_match.group(1)):
                    target = kw.split("|")[0].strip()
                    if not concept_exists(target, alias_map):
                        kw_dead.append(target)
                if kw_dead:
                    warnings.append(f"keywords: 无对应概念页 -> {', '.join(kw_dead[:5])}"
                                    + ("..." if len(kw_dead) > 5 else ""))

            # 12) Abstract quality
            ab_m = re.search(r'^abstract:\s*"(.*?)"', fm_text, re.MULTILINE | re.DOTALL)
            if ab_m and not supp:
                ab = ab_m.group(1)
                if len(ab) < 80:
                    warnings.append(f"abstract: 偏短 ({len(ab)} chars), 可能截断")
                if re.search(r'\\mathrm|\\mathsf|\\mathbf|\\mathcal|\\begin\{|\\frac|\\sum', ab):
                    warnings.append("abstract: 含 LaTeX 残留")
            abcn_m = re.search(r'^abstract_cn:\s*"(.*?)"', fm_text, re.MULTILINE | re.DOTALL)
            if abcn_m and not supp:
                abcn = abcn_m.group(1)
                if len(abcn) < 50:
                    warnings.append(f"abstract_cn: 偏短 ({len(abcn)} chars), 可能截断")
                if not re.search(r'[。！？」』]$', abcn.strip()):
                    warnings.append("abstract_cn: 未以中文标点结尾，可能截断")

            # 13) Cite format (GB/T 7714 rough check)
            if cite_text and not cite_text.startswith("待补充") and len(cite_text) >= 20:
                # Should contain author. title[J]. journal, year or similar
                if not re.search(r'[A-Z]\w*[\s,].*\..*\[[JCMP]\]', cite_text):
                    if not re.search(r'[A-Z].*et al\.', cite_text):
                        warnings.append("cite: 格式可能不符合 GB/T 7714")

            # 14) aiSum should contain problem/method/result
            ai_m = re.search(r'^aiSum:\s*"(.*?)"', fm_text, re.MULTILINE | re.DOTALL)
            if ai_m:
                ai = ai_m.group(1)
                score = 0
                if re.search(r'问题|problem|challenge|limitation|瓶颈|挑战', ai, re.I):
                    score += 1
                if re.search(r'方法|method|propos|提出|采用|设计|实现|展示|本文|方案', ai, re.I):
                    score += 1
                if re.search(r'结论|result|发现|demonstrat|achiev|accura|性能|达到|验证', ai, re.I):
                    score += 1
                if re.search(r'局限|limit|不足|限制|future|展望|挑战', ai, re.I):
                    score += 1
                if score < 2:
                    warnings.append(f"aiSum: 可能不完整 (problem/method/result/limit={score}/4)")

            # 15) Supplements should have parent field
            if supp and "parent:" not in fm_text:
                warnings.append("supplement: 缺少 parent 字段")

            # ── Record ──
            display = re.sub(r'/hybrid_auto/', '/',
                             os.path.relpath(filepath, VAULT))
            results.append((display, errors, warnings))
            for e in errors:
                stats_err[e.split(":")[0].split("-")[0]] += 1
            for w in warnings:
                stats_warn[w.split(":")[0]] += 1

    # ── Print report ────────────────────────────────────────
    print("=" * 72)
    print("FRONTMATTER QUALITY AUDIT REPORT")
    print("=" * 72)

    fail_list = [(p, e, w) for p, e, w in results if e]
    warn_list = [(p, e, w) for p, e, w in results if not e and w]
    passed = len(results) - len(fail_list) - len(warn_list)

    # Show ALL FAIL papers with details
    for path, errors, warnings in fail_list:
        print(f"\n  FAIL | {path}")
        for e in errors:
            print(f"         ❌ {e}")
        for w in warnings:
            print(f"         ⚠️  {w}")

    # Show WARN papers only if verbose
    if verbose:
        for path, errors, warnings in warn_list:
            print(f"\n  WARN | {path}")
            for w in warnings:
                print(f"         ⚠️  {w}")

    print(f"\n{'=' * 72}")
    print("SUMMARY")
    print(f"{'=' * 72}")
    print(f"  Total: {len(results)}  |  ✅ Pass: {passed}  |  ⚠️  Warn: {len(warn_list)}  |  ❌ Fail: {len(fail_list)}")

    if stats_err:
        print(f"\n  ── FAIL 类型 ──")
        for k, c in stats_err.most_common():
            print(f"    {k}: {c}")

    if stats_warn:
        print(f"\n  ── WARN 类型 ──")
        for k, c in stats_warn.most_common():
            print(f"    {k}: {c}")

    print(f"\n  运行 verbose 模式查看全部 WARN: python3 check_frontmatter.py -v")
    return len(fail_list) == 0


if __name__ == "__main__":
    verbose = "-v" in sys.argv or "--verbose" in sys.argv
    ok = check_all(verbose=verbose)
    sys.exit(0 if ok else 1)
