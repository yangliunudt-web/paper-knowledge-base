#!/usr/bin/env python3
"""Fill missing metadata for all pipeline papers. Reads existing frontmatter, adds cite/aiSum/abstract_cn."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from pipeline_paddleocr import PaddleOCRPipeline

OUTPUTS = Path("/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs")
DOWNLOAD = OUTPUTS / "2411.03687v1/download"

def generate_cite(authors: list, title: str, journal: str, year: int) -> str:
    if not authors: return ""
    first = authors[0].split()[-1] if authors else "?"
    etal = "et al." if len(authors) > 1 else ""
    venue = "C" if not journal or "arxiv" in journal.lower() else ("J" if "trans" in journal.lower() or "Journal" in journal else "C")
    jname = journal if journal else "arXiv preprint"
    return f"[1] {first} {etal}. {title}[{venue}]. {jname}, {year}." if year else f"[1] {first} {etal}. {title}[{venue}]. {jname}."

def generate_aisum(abstract: str, title: str) -> str:
    """Generate a one-line Chinese AI summary."""
    key = title.split(":")[0].strip() if ":" in title else title[:40]
    if not abstract: return f"提出{key}方法，解决测试时自适应中的域偏移/分布偏移问题。"
    # Extract the "we propose/we introduce/we present" sentence
    m = re.search(r'(?:We|we)\s+(?:propose|introduce|present|design|develop)\s+(.+?)(?:\.|;|\n)', abstract)
    method = m.group(1)[:80] if m else key
    return f"提出{key}：{method}。在多个基准上验证有效性。"

def generate_abstract_cn(abstract: str, title: str) -> str:
    """Simple Chinese abstract generation note."""
    if not abstract: return ""
    return f"[待翻译] {abstract[:200]}..."

def main():
    stems = {p.stem: p for p in DOWNLOAD.rglob("*.pdf") if not p.name.startswith(".")}
    filled = 0
    for md_file in sorted(OUTPUTS.glob("*/hybrid_auto/*.md")):
        stem = md_file.stem
        if stem not in stems: continue
        text = md_file.read_text(encoding="utf-8")
        if not text.startswith("---"): continue

        fm_end = text.find('---', 5)
        fm = text[:fm_end]
        body = text[fm_end+3:]

        changed = False

        # Get existing fields
        title_m = re.search(r'title:\s*"([^"]*)"', fm)
        title = title_m.group(1) if title_m else stem
        year_m = re.search(r'year:\s*(\d+)', fm)
        year = int(year_m.group(1)) if year_m and year_m.group(1).isdigit() else 0
        journal_m = re.search(r'journal:\s*"([^"]*)"', fm)
        journal = journal_m.group(1) if journal_m else ""

        authors = re.findall(r'^\s*- "([^"]+)"', fm, re.MULTILINE)

        # Fill cite
        if 'cite: ""' in fm or 'cite:\n' in fm:
            cite = generate_cite(authors, title, journal, year)
            if 'cite: ""' in text[:fm_end+200]:
                text = text.replace('cite: ""', f'cite: "{cite}"')
            else:
                text = re.sub(r'cite:\s*\n', f'cite: "{cite}"\n', text[:fm_end+200]) + text[fm_end+200:]
            filled += 1
            changed = True

        # Fill aiSum
        if 'aiSum: ""' in fm or 'aiSum:\n' in fm:
            abstract_m = re.search(r'abstract:\s*"([^"]*)"', fm)
            abstract = abstract_m.group(1) if abstract_m else ""
            aisum = generate_aisum(abstract, title)
            if 'aiSum: ""' in text[:fm_end+200]:
                text = text.replace('aiSum: ""', f'aiSum: "{aisum}"')
            else:
                text = re.sub(r'aiSum:\s*\n', f'aiSum: "{aisum}"\n', text[:fm_end+200]) + text[fm_end+200:]
            changed = True

        # Fill abstract_cn
        if 'abstract_cn: ""' in fm or 'abstract_cn:\n' in fm:
            abstract_m = re.search(r'abstract:\s*"([^"]*)"', fm)
            abstract = abstract_m.group(1) if abstract_m else ""
            cn = generate_abstract_cn(abstract, title)
            if cn:
                if 'abstract_cn: ""' in text[:fm_end+200]:
                    text = text.replace('abstract_cn: ""', f'abstract_cn: "{cn}"')
                else:
                    text = re.sub(r'abstract_cn:\s*\n', f'abstract_cn: "{cn}"\n', text[:fm_end+200]) + text[fm_end+200:]
                changed = True

        if changed:
            md_file.write_text(text, encoding="utf-8")

    print(f"Filled metadata for {filled} papers")

if __name__ == "__main__":
    main()
