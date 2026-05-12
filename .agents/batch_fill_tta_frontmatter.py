#!/usr/bin/env python3
"""Batch-fill frontmatter for TTA papers: extract abstract/authors from body text.

Only modifies papers where abstract or authors are empty.
Never touches papers with complete frontmatter.
"""

import os, re, glob, sys

OUTPUTS = os.path.expanduser(
    "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs"
)

TTA_KEYWORDS = [
    'TTA', 'test-time', 'test_time', 'domain adaptation', 'domain generalization',
    'domain shift', 'prompt tuning', 'diffusion.*adapt', 'feature align',
    'entropy minim', 'batch norm', 'distribution shift', 'covariate',
    'continual.*adapt', 'online.*adapt', 'test-time training'
]

def is_tta(dirname):
    dlower = dirname.lower()
    for kw in TTA_KEYWORDS:
        if re.search(kw, dlower):
            return True
    return False


def extract_abstract_from_body(body):
    """Extract abstract from paper body text (between ABSTRACT heading and INTRODUCTION)."""
    # Try to find ABSTRACT section
    patterns = [
        r'##\s*ABSTRACT\s*\n+(.*?)(?=\n##\s*\d+\s+INTRODUCTION)',
        r'##\s*Abstract\s*\n+(.*?)(?=\n##\s*\d+\s+Introduction)',
        r'##\s*ABSTRACT\s*\n+(.*?)(?=\n##\s*\d)',
        r'##\s*Abstract\s*\n+(.*?)(?=\n##\s*\d)',
        r'##\s*ABSTRACT\s*\n+(.*?)(?=\n##)',
        r'##\s*Abstract\s*\n+(.*?)(?=\n##)',
    ]
    for pat in patterns:
        m = re.search(pat, body, re.DOTALL)
        if m:
            abstract = m.group(1).strip()
            # Clean up: remove image references, extra newlines
            abstract = re.sub(r'!\[.*?\]\(.*?\)', '', abstract)
            abstract = re.sub(r'\n{3,}', '\n\n', abstract)
            abstract = ' '.join(abstract.split())
            if len(abstract) > 100:
                return abstract
    return None


def extract_authors_from_body(body):
    """Extract author names from the beginning of the paper body."""
    # Authors typically appear right after the title, before affiliations
    # Pattern: "Name Surname1, Name Surname2, ..." or "Name Surname$^{1}$, ..."
    # Find the first meaningful text after the title line
    lines = body.split('\n')
    author_candidates = []
    in_authors = False
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if i < 30:  # Authors should be in first 30 lines
            # Clean LaTeX markers
            cleaned = re.sub(r'\$\^?\{?[\*†‡§¶∥\d,]+}?\$', '', line)
            cleaned = re.sub(r'\$\^?[{\[]?[\*†‡§¶∥\d]+[}\]]?\$', '', cleaned)
            cleaned = cleaned.strip()
            if cleaned and len(cleaned) > 3:
                author_candidates.append(cleaned)

    if not author_candidates:
        return None

    # Try to find comma-separated or and-separated names
    combined = ' '.join(author_candidates[:5])
    # Remove affiliation info
    combined = re.sub(r'\b(Department|University|Institute|School|College|Laboratory|Lab|Center|Centre)\b.*', '', combined)
    combined = re.sub(r'\b(de|of|at|in|the)\b.*', '', combined)

    # Split by common separators
    names = []
    # Try splitting by numbers (superscript affiliations)
    parts = re.split(r'\d', combined)
    for part in parts:
        part = part.strip().strip(',').strip()
        if len(part) > 3 and not re.match(r'^[\s,]+$', part):
            # Check if it looks like a name (contains at least one space, not all caps)
            if ' ' in part and not re.match(r'^[A-Z\s]+$', part):
                names.append(part)

    if len(names) >= 1:
        return names[:15]  # Max 15 authors
    return None


def extract_journal_from_body(body):
    """Try to detect journal/venue from paper body."""
    # Check first 2000 chars and last 1000 chars for venue info
    head = body[:2000]
    tail = body[-2000:]

    venues = {
        'CVPR': r'\bCVPR\b',
        'ICCV': r'\bICCV\b',
        'ECCV': r'\bECCV\b',
        'NeurIPS': r'\bNeurIPS\b',
        'ICML': r'\bICML\b',
        'ICLR': r'\bICLR\b',
        'AAAI': r'\bAAAI\b',
        'IJCAI': r'\bIJCAI\b',
        'ACL': r'\bACL\b',
        'EMNLP': r'\bEMNLP\b',
        'ICASSP': r'\bICASSP\b',
        'WACV': r'\bWACV\b',
        'BMVC': r'\bBMVC\b',
        'MICCAI': r'\bMICCAI\b',
        'IEEE T-ED': r'IEEE\s*Trans.*Electron',
        'IEEE TED': r'IEEE\s*Trans.*Electron',
        'Nature': r'\bNature\b',
        'Science': r'\bScience\b',
        'arXiv': r'arXiv',
    }

    for venue, pattern in venues.items():
        if re.search(pattern, head + tail, re.IGNORECASE):
            return venue

    # Check for "Proceedings of" or "Conference on"
    conf_match = re.search(r'(?:Proceedings|Conference|Workshop)\s+(?:of|on)\s+([^,\.\n]+)', head)
    if conf_match:
        return conf_match.group(0).strip()

    return None


def fill_frontmatter(filepath, dry_run=False):
    """Fill missing frontmatter fields from body text."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Split frontmatter from body
    if not content.startswith('---'):
        return None, "no frontmatter"

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, "malformed frontmatter"

    fm = parts[1]
    body = parts[2]

    changes = []

    # Check abstract
    if re.search(r'abstract:\s*""', fm):
        abstract = extract_abstract_from_body(body)
        if abstract:
            # Escape double quotes in abstract
            abstract_escaped = abstract.replace('"', '\\"')
            old = 'abstract: ""'
            new = f'abstract: "{abstract_escaped}"'
            changes.append(('abstract', old, new))

    # Check authors
    if re.search(r'authors:\s*\[\s*\]', fm):
        authors = extract_authors_from_body(body)
        if authors:
            old = 'authors: []'
            new = 'authors:\n' + '\n'.join(f'  - "{a}"' for a in authors)
            changes.append(('authors', old, new))

    # Check journal
    journal_match = re.search(r'journal:\s*""', fm)
    if journal_match:
        journal = extract_journal_from_body(body)
        if journal:
            old = 'journal: ""'
            new = f'journal: "{journal}"'
            changes.append(('journal', old, new))

    if not changes:
        return None, "nothing to auto-fill"

    if dry_run:
        for field, old, new in changes:
            print(f"  [{field}] {old[:60]} -> {new[:80]}")
        return changes, "dry_run"

    # Apply changes
    new_fm = fm
    for field, old, new in changes:
        new_fm = new_fm.replace(old, new, 1)

    new_content = f'---{new_fm}---{body}'

    with open(filepath, 'w') as f:
        f.write(new_content)

    return changes, "applied"


def main():
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv

    total = 0
    filled = 0
    skipped = 0

    for d in sorted(os.listdir(OUTPUTS)):
        if not is_tta(d):
            continue

        ha_dir = os.path.join(OUTPUTS, d, 'hybrid_auto')
        if not os.path.isdir(ha_dir):
            continue

        md_files = glob.glob(os.path.join(ha_dir, '*.md'))
        if not md_files:
            continue

        total += 1
        md = md_files[0]

        changes, status = fill_frontmatter(md, dry_run)

        if changes:
            filled += 1
            print(f"[{status}] {d[:70]}")
            if dry_run:
                for field, old, new in changes:
                    short_new = new[:70] + '...' if len(new) > 70 else new
                    print(f"  {field}: {short_new}")
        else:
            skipped += 1

    print(f"\nTotal: {total}, Filled: {filled}, Skipped: {skipped}")


if __name__ == '__main__':
    main()
