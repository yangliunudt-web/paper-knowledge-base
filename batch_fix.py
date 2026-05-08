#!/usr/bin/env python3
"""Safe batch fix for frontmatter: author quotes + year string->number."""

import os
import re
import sys

OUTPUTS = "/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs"
DRY_RUN = '--apply' not in sys.argv


def fix_file(filepath):
    """Fix author quoting and year format. Returns (changed, changes_list)."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    if not content.startswith('---'):
        return False, []

    m = re.match(r'^(---\s*\n)(.*?)(\n---)', content, re.DOTALL)
    if not m:
        return False, []

    header, body, tail = m.group(1), m.group(2), m.group(3)
    after_fm = content[len(header) + len(body) + len(tail):]
    lines = body.split('\n')
    new_lines = []
    changes = []

    in_authors = False
    for line in lines:
        stripped = line.strip()

        # Track authors section
        if stripped == 'authors:' or stripped.startswith('authors:'):
            in_authors = True
            new_lines.append(line)
            continue
        if in_authors and stripped and not stripped.startswith('-') and not stripped.startswith('#'):
            in_authors = False

        # P3: Fix unquoted authors
        if in_authors and stripped.startswith('- ') and len(stripped) > 2:
            after = stripped[2:]
            if not after.strip():
                new_lines.append(line)
                continue
            # Skip if already properly double-quoted
            if after.startswith('"') and after.endswith('"'):
                new_lines.append(line)
                continue

            # Strip single quotes if present
            if after.startswith("'") and after.endswith("'"):
                after = after[1:-1]

            indent = line[:len(line) - len(line.lstrip())]
            new_line = f'{indent}- "{after}"'
            changes.append(f"AUTHOR: {stripped[:60]} -> - \"{after[:50]}\"")
            new_lines.append(new_line)
            continue

        # P2: Fix year as string
        ym = re.match(r'^(\s*year:\s*)[\'"](\d{4})[\'"](\s*)$', line)
        if ym:
            new_line = f'{ym.group(1)}{ym.group(2)}{ym.group(3)}'
            changes.append(f"YEAR: {line.strip()} -> {new_line.strip()}")
            new_lines.append(new_line)
            continue

        new_lines.append(line)

    if not changes:
        return False, []

    new_body = '\n'.join(new_lines)
    new_content = header + new_body + tail + after_fm

    if not DRY_RUN:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return True, changes


def main():
    print("=" * 60)
    if DRY_RUN:
        print("DRY-RUN MODE (preview only — use --apply to write)")
    else:
        print("APPLY MODE (writing changes)")
    print("=" * 60)

    total = ok = fixed = 0
    total_changes = 0

    for root, dirs, files in os.walk(OUTPUTS):
        dirs[:] = [d for d in dirs if d != '.claude']
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            filepath = os.path.join(root, fname)
            total += 1
            try:
                changed, details = fix_file(filepath)
            except Exception as e:
                print(f"ERROR {os.path.relpath(filepath, OUTPUTS)}: {e}")
                continue

            if changed:
                fixed += 1
                total_changes += len(details)
                print(f"{'WOULD-FIX' if DRY_RUN else 'FIXED'}: {os.path.relpath(filepath, OUTPUTS)}")
                for d in details:
                    print(f"   {d}")
            else:
                ok += 1

    print()
    print(f"Summary: Total={total}  Fixed={fixed}  OK={ok}  Changes={total_changes}")
    if DRY_RUN:
        print(">>> DRY RUN — no files modified. Use --apply to write. <<<")


if __name__ == '__main__':
    main()
