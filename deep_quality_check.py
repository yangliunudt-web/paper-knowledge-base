#!/usr/bin/env python3
"""Deep frontmatter quality audit for paper library."""

import os
import re
import yaml

OUTPUTS = "/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs"

def extract_frontmatter(filepath):
    """Extract YAML frontmatter between --- markers."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    # Match frontmatter block
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return None, "NO_FRONTMATTER"
    return m.group(1), None

def check_quality(frontmatter_text, filepath):
    """Deep quality check of frontmatter content."""
    issues = []
    warnings = []
    rel = os.path.relpath(filepath, OUTPUTS)

    try:
        fm = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        return [f"YAML_PARSE_ERROR: {str(e)[:80]}"], [], rel

    if not isinstance(fm, dict):
        return ["NOT_A_DICT"], [], rel

    raw_lines = frontmatter_text.split('\n')

    # Check for single quotes in raw YAML (should use double quotes)
    for i, line in enumerate(raw_lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        # Check value part for single-quoted strings
        if ':\s*\'' in line or ":'" in line:
            # Allow if inside a larger string
            if re.search(r":\s*'.*'", stripped) or re.search(r":\s*'\[\[.*\]\]'", stripped):
                issues.append(f"单引号 (line {i}): {stripped[:80]}")
            break  # Just flag once per file

    # --- TITLE ---
    if 'title' not in fm:
        issues.append("MISSING: title")
    else:
        title = str(fm['title'])
        if len(title) < 10:
            issues.append(f"title 过短: '{title}'")
        if '$' in title or 'mathbf' in title or 'mathrm' in title:
            issues.append(f"title 含LaTeX math: ...{title[-60:]}")
        if title.startswith('sub-') or title.startswith('Sub-'):
            warnings.append(f"title 以 sub-/Sub- 开头: '{title[:60]}'")

    # --- AUTHORS ---
    if 'authors' not in fm:
        issues.append("MISSING: authors")
    elif fm['authors'] is None:
        issues.append("authors 为 null/空")
    elif isinstance(fm['authors'], str):
        issues.append(f"authors 是字符串而非列表: '{fm['authors'][:60]}'")
    elif isinstance(fm['authors'], list):
        if len(fm['authors']) == 0:
            issues.append("authors 列表为空")
        for j, author in enumerate(fm['authors']):
            author_str = str(author)
            if 'Unknown' in author_str or 'unknown' in author_str:
                issues.append(f"authors[{j}] 占位符: '{author_str}'")
            # Check if author names lack quotes in raw YAML
        # Check raw YAML for unquoted authors
        in_authors = False
        for line in raw_lines:
            s = line.strip()
            if s.startswith('authors:'):
                in_authors = True
                continue
            if in_authors and s.startswith('- ') and not s.startswith('- "') and not s.startswith('- \''):
                if re.match(r'^-\s+\S', s):
                    issues.append(f"author 无引号: {s[:60]}")
                    break  # flag once
            if in_authors and not s.startswith('-') and s.strip() and not s.startswith('  '):
                break

    # --- DATE ---
    if 'date' not in fm:
        issues.append("MISSING: date")
    else:
        date_val = str(fm['date'])
        if date_val in ('Unknown', 'unknown', '', 'None'):
            issues.append(f"date 占位符: '{date_val}'")
        elif not re.match(r'\d{4}', date_val):
            issues.append(f"date 格式异常: '{date_val}'")

    # --- YEAR ---
    if 'year' not in fm:
        issues.append("MISSING: year")
    else:
        year_val = fm['year']
        if isinstance(year_val, str):
            issues.append(f"year 是字符串而非数字: '{year_val}'")
        elif isinstance(year_val, (int, float)):
            if year_val < 1900 or year_val > 2030:
                issues.append(f"year 异常值: {year_val}")

    # --- JOURNAL / TYPE ---
    if 'journal' not in fm and 'type' not in fm:
        issues.append("MISSING: journal (及 type)")
    elif 'journal' in fm:
        jval = str(fm['journal'])
        if jval in ('Unknown', 'unknown', '', 'None'):
            issues.append(f"journal 占位符: '{jval}'")

    # --- ABSTRACT ---
    if 'abstract' not in fm:
        issues.append("MISSING: abstract")
    else:
        abstract = str(fm['abstract'])
        if len(abstract) < 50:
            issues.append(f"abstract 过短 ({len(abstract)}字符)")
        if abstract.startswith('（自动生成摘要）') or abstract.startswith('(自动生成'):
            issues.append("abstract 是自动生成的占位符")

    # --- ABSTRACT_CN ---
    if 'abstract_cn' not in fm:
        issues.append("MISSING: abstract_cn")
    else:
        abs_cn = str(fm['abstract_cn'])
        if len(abs_cn) < 20:
            issues.append(f"abstract_cn 过短 ({len(abs_cn)}字符)")
        if '（自动生成摘要）' in abs_cn or '(自动生成' in abs_cn:
            issues.append("abstract_cn 是自动生成的占位符")
        if abs_cn.startswith('（自动生成') or abs_cn.startswith('(自动'):
            issues.append("abstract_cn 是自动生成的占位符")

    # --- KEYWORDS ---
    if 'keywords' not in fm:
        issues.append("MISSING: keywords")
    elif fm['keywords'] is None:
        issues.append("keywords 为 null")
    elif isinstance(fm['keywords'], list):
        if len(fm['keywords']) == 0:
            issues.append("keywords 列表为空")
        has_wikilinks = False
        for kw in fm['keywords']:
            kw_str = str(kw)
            if '[[' in kw_str and ']]' in kw_str:
                has_wikilinks = True
            else:
                issues.append(f"keyword 非wikilink: '{kw_str[:50]}'")
                break  # flag once
        if not has_wikilinks and len(fm['keywords']) > 0:
            pass  # already flagged above
        # Check for single quotes around wikilinks in raw
    elif isinstance(fm['keywords'], str):
        issues.append(f"keywords 是字符串而非列表: '{fm['keywords'][:60]}'")

    # --- CITE ---
    if 'cite' not in fm:
        issues.append("MISSING: cite")
    else:
        cite_val = str(fm['cite'])
        if len(cite_val) < 20:
            issues.append(f"cite 过短: '{cite_val}'")
        if cite_val.startswith('[1] 作者') or '作者.' in cite_val[:20]:
            issues.append(f"cite 为占位格式: '{cite_val[:60]}'")

    # --- AISUM ---
    if 'aiSum' not in fm:
        issues.append("MISSING: aiSum")
    else:
        aisum = str(fm['aiSum'])
        if len(aisum) < 20:
            issues.append(f"aiSum 过短 ({len(aisum)}字符)")
        # Check if aiSum is just a copy of abstract
        if 'abstract' in fm:
            abstract_start = str(fm['abstract'])[:100]
            if aisum[:100] == abstract_start:
                warnings.append("aiSum 与 abstract 开头相同(可能为复制)")

    # --- EXTRA FIELDS ---
    # Check for legacy fields that should be migrated
    if 'doi' in fm and 'cite' not in fm:
        warnings.append("有 'doi' 字段但无 'cite' 字段")
    if 'type' in fm and 'journal' not in fm:
        pass  # type is acceptable as journal alternative

    return issues, warnings, rel


def main():
    print("=" * 80)
    print("FRONTMATTER 深度质量审计报告")
    print("=" * 80)
    print()

    total = 0
    clean = 0
    has_issues = 0
    has_warnings = 0
    all_results = []

    for root, dirs, files in os.walk(OUTPUTS):
        # Skip .claude directories
        dirs[:] = [d for d in dirs if d != '.claude']
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = os.path.join(root, f)
            total += 1

            fm_text, err = extract_frontmatter(filepath)
            if err:
                all_results.append((filepath, [err], [], os.path.relpath(filepath, OUTPUTS)))
                has_issues += 1
                continue

            issues, warnings, rel = check_quality(fm_text, filepath)
            all_results.append((filepath, issues, warnings, rel))

            if issues:
                has_issues += 1
            elif warnings:
                has_warnings += 1
            else:
                clean += 1

    # Sort: issues first, then by severity (issue count)
    all_results.sort(key=lambda x: (-len(x[1]), x[3]))

    # --- DETAILED OUTPUT ---
    print(f"{'='*80}")
    print(f"一、存在严重问题的论文 ({has_issues}篇)")
    print(f"{'='*80}")
    print()

    for filepath, issues, warnings, rel in all_results:
        if not issues:
            continue
        print(f"📄 {rel}")
        for iss in issues:
            print(f"   ❌ {iss}")
        for warn in warnings:
            print(f"   ⚠️  {warn}")
        print()

    print()
    print(f"{'='*80}")
    print(f"二、仅有警告的论文 ({has_warnings}篇)")
    print(f"{'='*80}")
    print()

    for filepath, issues, warnings, rel in all_results:
        if issues:
            continue
        if not warnings:
            continue
        print(f"📄 {rel}")
        for warn in warnings:
            print(f"   ⚠️  {warn}")
        print()

    print()
    print(f"{'='*80}")
    print(f"三、通过检查的论文 ({clean}篇)")
    print(f"{'='*80}")
    for filepath, issues, warnings, rel in all_results:
        if not issues and not warnings:
            print(f"   ✅ {rel}")

    # --- SUMMARY ---
    print()
    print(f"{'='*80}")
    print("统计汇总")
    print(f"{'='*80}")
    print(f"  总计: {total} 篇")
    print(f"  合格 (0问题): {clean} 篇")
    print(f"  仅警告:      {has_warnings} 篇")
    print(f"  有问题:      {has_issues} 篇")
    print()

    # Categorize issues
    issue_categories = {}
    for _, issues, _, _ in all_results:
        for iss in issues:
            cat = iss.split(':')[0].split('(')[0].strip()
            issue_categories[cat] = issue_categories.get(cat, 0) + 1

    print("问题类型分布 (Top 15):")
    for cat, count in sorted(issue_categories.items(), key=lambda x: -x[1])[:15]:
        print(f"  {count:4d}  {cat}")

    issue_keywords_count = {}
    for _, issues, _, _ in all_results:
        for iss in issues:
            # Extract keyword from issue
            for kw in ['MISSING:', 'keyword 非wikilink', 'author 无引号', '是字符串而非列表',
                       'aicSum 与 abstract', '无引号', '占位符', '过短', 'LaTeX',
                       '自动生成', '格式异常', '异常值']:
                if kw.lower() in iss.lower() or kw in iss:
                    issue_keywords_count[kw] = issue_keywords_count.get(kw, 0) + 1
                    break

    print()
    print("问题关键词统计:")
    for kw, count in sorted(issue_keywords_count.items(), key=lambda x: -x[1]):
        print(f"  {count:4d}  {kw}")

if __name__ == '__main__':
    main()
