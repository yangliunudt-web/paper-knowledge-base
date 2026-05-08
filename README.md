# Paper Knowledge Base

Obsidian vault for managing academic papers on ferroelectric FETs (FeFETs), in-memory computing (IMC), neuromorphic computing, reservoir computing, and related semiconductor devices.

---

## Repository Map

```
Papers/
├── .agents/                          # Agent configuration files
│   ├── stork-processor-config.md     # Stork digest → download → report
│   ├── literature-downloader-config.md # Batch PDF download strategies
│   ├── literature-importer-config.md   # PDF → Obsidian with frontmatter
│   ├── literature-searcher-config.md   # Smart search with memory
│   ├── literature-searcher-memory.md   # Search history persistence
│   ├── literature-summarizer-config.md # WeChat-style summaries
│   ├── citation-enhancer-config.md     # Citation insertion + canvas maps
│   └── skills/                         # Installed skill definitions
├── .claude/skills/                   # Symlinks to active skills
├── .obsidian/                        # Vault config & plugins
├── skills/                           # Symlinks to .agents/skills/
├── Outputs/                          # 200+ papers (git: 3 examples)
│   └── {Paper ID}/hybrid_auto/
│       ├── {Title}.md                # Full paper markdown
│       ├── {Title}_origin.pdf        # Original PDF
│       ├── {Title}_layout.pdf        # Reflowed PDF
│       ├── *_content_list.json       # Extracted content metadata
│       ├── *_model.json              # AI model output
│       └── images/                   # Extracted figures
├── Stork/                            # Stork literature alert reports
│   └── {YYYY-MM-DD}_{subject}/
│       ├── {日期}_Stork文献报告.md
│       └── {Author}_{Year}_{Keywords}.pdf
├── Summary/                          # WeChat-style paper summaries
├── Citation/                         # Citation maps (.canvas) + reports
├── Keywords-Report/                  # Keyword index search reports
├── Writing/                          # Paper drafts (gitignored)
├── _NonPapers/                       # Non-academic imports (gitignored)
├── CLAUDE.md                         # Project instructions
├── PaperProcess.md                   # Frontmatter quality standard
├── check_frontmatter.sh              # Fast frontmatter audit
├── deep_quality_check.py             # Per-paper quality scoring
├── batch_fix_v3.py                   # Batch frontmatter fixer
└── skills-lock.json                  # Skill version lockfile
```

---

# Agents

## 1. Stork Processor

**Purpose**: Parse Stork (文献鸟) digest PDFs, download papers, generate scored intelligence reports.

**Trigger**: User forwards a Stork digest PDF ("Stork导入：xxx.pdf").

**Scope**: Ends at report + PDF download. Does NOT import into Outputs/ — that is `literature-importer`'s job.

### Tools Used

| Tool | Purpose |
|------|---------|
| `Read` | Read Stork PDF, read config |
| `Bash` | PyPDF2 text extraction, mkdir, cp/mv/rename, file checks |
| `WebSearch` | Find arXiv IDs, ResearchGate links |
| `WebFetch` | Fetch journal pages, arXiv search results |
| `Write` | Generate report.md |
| `Edit` | Update report after downloads complete |

### Workflow

```
1. Parse PDF → PyPDF2 extracts text from digest pages
2. Filter → keep FeFET/ferroelectric/IGZO/neuromorphic papers
3. Download per paper (6-tier priority):
   3a. OA direct (Nature Comms, Nano-Micro Letters)
   3b. arXiv Web search → download PDF → verify %PDF header
   3c. Semantic Scholar API → find arXiv ID or OA PDF URL
   3d. WebSearch → find arXiv ID, ResearchGate, author homepage
   3e. Sci-Hub → sci-hub.se/{DOI} (often blocked in China)
   3f. Library Portal → gfkd.chaoxing.com activate DB → direct journal link
4. Rename PDFs → {FirstAuthor}_{Year}_{Keywords}.pdf
5. Generate report with:
   - 推荐总览 table (priority, Chinese title, score, PDF link)
   - 下载情况总览 table (file names, download channels)
   - Per-paper: abstract CN/EN, literature association, 9D scoring
   - 总评: ranked reading priority + research insights
```

### Download Channel Details

#### arXiv (Priority 1)
- **Why not API**: `export.arxiv.org/api/query` rate-limits aggressively (429 after few requests, 20s+ bans)
- **Web search instead**: `arxiv.org/search/?query={keywords}&searchtype=all`
- **Regex extract**: `href="(?:https://arxiv\.org)?/abs/(\d+\.\d+(?:v\d+)?)"`
- **Strip version**: `re.sub(r'v\d+$', '', arxiv_id)`
- **PDF**: `arxiv.org/pdf/{id}.pdf`

#### Semantic Scholar (Priority 2)
- **API**: `api.semanticscholar.org/graph/v1/paper/search?query={title}&limit=3&fields=title,externalIds,openAccessPdf,year`
- **2026 papers**: Usually not indexed yet → 404
- **Rate limit**: 3s interval, back off 30s on 429

#### Library Portal (Priority 6 — validated 2026-05-08)
- **URL**: `fx.gfkd.chaoxing.com/v2/magguide/door/search?pageId=14132&wfwfid=182&sw={DB}&uid=152142963&choren=1`
- **Databases**: Wiley, ACS, Springer Nature
- **Method**: Open portal → search for database → click to activate → then open direct journal article links
- **Why this works**: Session carries library auth to journal sites; PDF buttons appear automatically
- **Key mistake avoided**: The `nav/cp/door/search` path is for conferences, NOT journals. Always use `v2/magguide/door/search`

### Report Format Rules (evolved through 2026-05-08 session)

1. **Filename**: `{YYYY-MM-DD}_Stork文献报告.md` (NOT `报告.md`)
2. **Table separators**: `|---|---|---|` (3 dashes, no extra padding — Obsidian auto-formats anyway)
3. **论文简写 column**: Use Chinese short titles (自支撑涡旋管FeFET), NOT English filenames
4. **PDF column**: Between 推荐等级 and 一句话建议, with `[PDF](filename.pdf)` links
5. **Download method noted**: "期刊库直连" not "CARSI"
6. **Two tables**: 推荐总览 first, 下载情况总览 second

### Key Improvements from User Interaction

| Issue | Original | Fixed |
|-------|----------|-------|
| Download method | CARSI wayfless URL + HTML page (unreliable) | Library portal + direct journal links |
| Report filename | `报告.md` | `{日期}_Stork文献报告.md` |
| Paper names | English filenames in table | Chinese short titles |
| PDF access | No link in overview table | Clickable PDF column |
| Table formatting | Aligned padding gets re-formatted | Clean `\|---\|` separators |
| Workflow boundary | Unclear if import happens | Explicit: Stork ends at report |

---

## 2. Literature Importer

**Purpose**: Import individual paper PDFs into the Obsidian vault with proper YAML frontmatter.

**Trigger**: User provides a PDF and says "导入这篇论文" or calls the agent directly.

### Tools Used

| Tool | Purpose |
|------|---------|
| `Bash` | Run automator workflow, mkdir, mv, file checks |
| `Read` | Read paper .md, check frontmatter |
| `Edit` | Fix frontmatter fields |
| `Write` | Write corrected .md with full frontmatter |

### Workflow

```
1. Pre-import check:
   ├── Scan Outputs/ for matching folder (by paper ID)
   ├── If exists → check .md frontmatter quality
   └── If missing → proceed to full import

2. PDF Import:
   └── automator -i "PDF path" ~/Library/Services/PDFtoObsidian.workflow
       → Creates Outputs/{folder}/hybrid_auto/{paper}.md + images/

3. File rename:
   ├── Folder: keep original ID (DO NOT rename)
   └── .md file: rename to full paper title

4. Frontmatter (see PaperProcess.md):"""
   - All strings double-quoted (NOT single-quoted)
   - authors as YAML array
   - keywords as array with [[wikilinks]]
   - cite in GB/T 7714-2015 format
   - abstract_cn = complete Chinese translation (not summary rewrite)
   - aiSum = at least 2 of: problem/method/conclusions/limitations
```

### Frontmatter Standard

```yaml
---
title: "Paper Title Here"
authors:
  - "Author One"
  - "Author Two"
date: "2024-07-01"
year: 2024
journal: "Journal Name"
keywords:
  - "[[EnglishKeyword]]"
  - "[[中文关键词]]"
abstract: "Full English abstract text..."
abstract_cn: "完整的中文翻译..."
cite: "Author. Title[J]. Journal, Year, Vol(Issue): Pages. DOI:..."
aiSum: "研究问题：... 方法：... 结论：..."
---
```

### Validation Scripts

```bash
bash check_frontmatter.sh        # Fast audit — checks all papers have required fields
python3 deep_quality_check.py    # Deep scoring — per-paper quality metric
python3 batch_fix_v3.py          # Batch repair — fixes common frontmatter issues
```

### Key Rules

- **Folder name**: Keep as original number/ID (e.g., `s41467-024-55558-3`) — DO NOT rename
- **MD filename**: Must be full paper title
- **Double quotes**: Critical for Obsidian to display frontmatter as properties
- **Keywords with wikilinks**: `[[English]]` and `[[中文]]` for bidirectional search
- **Supplement papers**: Add `parent: "[[Main Paper]]"`, prefix filename with `sub-`

---

## 3. Literature Downloader

**Purpose**: Batch download academic paper PDFs with automatic channel selection, URL correction, and network constraint handling. Used both standalone and as the download engine inside Stork Processor.

### Tools Used

| Tool | Purpose |
|------|---------|
| `Bash` | Python download scripts, curl/wget, file verification |
| `WebSearch` | Find arXiv IDs, alternative PDF sources |
| `WebFetch` | Fetch Semantic Scholar API, journal pages |

### Download Priority

| Tier | Channel | URL Pattern | When |
|------|---------|-------------|------|
| 1 | arXiv | `arxiv.org/pdf/{id}.pdf` | Most papers have preprints |
| 2 | OpenReview | `openreview.net/pdf?id={id}` | ML conference papers |
| 3 | PMLR | `proceedings.mlr.press/v{vol}/{id}/{id}.pdf` | Double directory required |
| 4 | NeurIPS | `proceedings.neurips.cc/paper_files/paper/{year}/file/{hash}-Paper-Conference.pdf` | `/file/` not `/hash/` |
| 5 | Zenodo | `zenodo.org/records/{id}/files/{filename}.pdf` | Backup source |
| 6 | arXiv Web Search | `arxiv.org/search/?query={keywords}` | When you only have title |
| 7 | Semantic Scholar | API: `api.semanticscholar.org/graph/v1/paper/search` | Find arXiv ID or OA PDF |
| 8 | WebSearch | Google/Bing for ResearchGate, author pages | Last open-source resort |
| 9 | Library Portal | gfkd.chaoxing.com → activate DB → journal link | Paid papers (validated) |
| 10 | Sci-Hub | `sci-hub.se/{DOI}` | May be blocked in China |

### URL Correction Rules

```
NeurIPS: /hash/ → /file/  (old format returns 404)
PMLR:    single dir → double dir  (/v202/paper.pdf → /v202/paper/paper.pdf)
CVF:     DON'T attempt direct (Azure IP blocked in China) → go to arXiv immediately
```

### Script Essentials

```python
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

# Rate control
DOMAIN_DELAY = {"arxiv.org": (2.0, 4.0), "proceedings.neurips.cc": (2.0, 5.0)}

# PDF validation
assert f.read(4) == b'%PDF' and os.path.getsize(path) > 2000

# Atomic write
download to path + ".part" → verify → os.rename(tmp, path)
```

### Network Notes (China)

| Accessible | Blocked |
|------------|---------|
| `arxiv.org`, `export.arxiv.org` | `openaccess.thecvf.com` (Azure IP) |
| `openreview.net`, `proceedings.mlr.press` | `sci-hub.se` (SSL error) |
| `api.semanticscholar.org` (occasional 429) | `sci-hub.ru`, `sci-hub.st` (403) |
| `zenodo.org`, `proceedings.neurips.cc` | |

### Journal-Specific Strategies

| Publisher | Path |
|-----------|------|
| Nature Comms | Direct OA: `nature.com/articles/{id}_reference.pdf` |
| Nano-Micro Letters | Direct OA: `link.springer.com/content/pdf/{doi}.pdf` |
| Nature / Science | arXiv → Semantic Scholar → Library Portal |
| Wiley (Adv. Mater., etc.) | arXiv → Semantic Scholar → Library Portal |
| ACS (ACS Nano, Langmuir, etc.) | arXiv → Semantic Scholar → Library Portal |
| IEEE | arXiv → IEEE Xplore → Library Portal |

### Key Improvement (2026-05-08)

**Original CARSI method**: Generate CARSI wayfless URLs → HTML page → user clicks → SAML redirect → download. Unreliable — URLs break, SAML fails, too many steps.

**New library portal method**: Open `gfkd.chaoxing.com/v2/magguide/door/search` → activate Wiley/ACS/Springer → direct journal links. One step, session carries auth everywhere. Saved as `paper-download-strategies.md` memory.

---

## 4. Literature Searcher

**Purpose**: Search the paper library with smart memory, numerical intelligence, and library update awareness.

**Trigger**: User asks "找文献", "有一篇关于...的论文", "查XX fJ的功耗", etc.

### Tools Used

| Tool | Purpose |
|------|---------|
| `Bash` | Grep with regex, find files, list directories |
| `Read` | Read paper .md files (frontmatter + full text) |
| `Glob` | Find paper directories by pattern |

### Search Architecture

```
Simple Search (milliseconds)          Detailed Search (seconds)
├── Target: frontmatter only          ├── Target: full .md file content
├── Index: .json metadata files       ├── Method: recursive grep
├── Use: quick lookup by title/author └── Use: deep analysis, numerical search
└── Fallback → triggers detailed search if results insufficient
```

### Numerical Search (Two-Phase)

**Phase 1 — Breadth**: Keyword filter to narrow candidate papers (search frontmatter: title, keywords, abstract)

**Phase 2 — Depth**: Grep with precise regex on matched papers:
```bash
# Exact: "22.7 fJ"
grep -r "22\.7\s*fJ" Outputs/

# Fuzzy: "20几 fJ" → 20.0-29.9
grep -rE "2[0-9]\.?\d*\s*fJ" Outputs/

# Multi-unit: fJ, pJ, nJ, µJ
grep -rE "2[0-9]\.?\d*\s*(fJ|pJ|nJ|µJ|μJ)" Outputs/
```

### Semantic Number Mapping

| User says | Regex generated | Match range |
|-----------|----------------|-------------|
| "22.7 fJ" | `22\.7\s*fJ` | Exact |
| "20几 fJ" | `2[0-9]\.?\d*\s*fJ` | 20.0–29.9 |
| "20多" | `2[1-9]\.?\d*` | 21.0–29.9 |
| "几百 fJ" | `[1-9]\d{2}\.?\d*\s*fJ` | 100–999.9 |
| "小于20" | `(0*\.\d+\|[01]\d)\.?\d*` | 0–19.9 |

### Unit Conversion Awareness

Searches all unit variants simultaneously:
```
fJ, pJ, nJ, µJ, μJ, uJ, mJ, J
飞焦, 皮焦, 纳焦, 微焦, 毫焦, 焦耳
```

### Search Memory

- Stores search history in `.agents/literature-searcher-memory.md`
- Re-evaluates past searches when library updates detected
- 7-day re-check interval; 30-day history retention
- 80% topic similarity threshold for "related search" detection

### Output Format

Always includes: vault-relative file path + Obsidian wikilink + full metadata.
```
📁 文件路径: Outputs/{folder}/hybrid_auto/{title}.md
🔗 Obsidian 位置: [[{title}]]
```

### Key Improvement

**Numerical regression fix**: Original regex `2[0-9]` only matched integers (20-29), missing "22.7 fJ". Fixed to `2[0-9]\.?\d*` to include all real numbers (20.0–29.999...). Same fix applied to all fuzzy numerical patterns.

---

## 5. Literature Keyword Indexer

**Purpose**: Generate batch keyword index reports — search entire library by topic and produce a structured report with all matching papers, their key metrics, and relevance ratings.

**Trigger**: User says "帮我找所有关于XX的文章", "生成XX关键词索引报告".

### Tools Used

| Tool | Purpose |
|------|---------|
| `Bash` | Grep across Outputs/, count matches, list files |
| `Read` | Read paper frontmatter for metadata extraction |
| `Write` | Generate report in Keywords-Report/ |

### Workflow

```
1. Accept keywords (Chinese or English)
2. Fuzzy match across all Outputs/ paper .md files
3. Extract frontmatter from matched papers (title, journal, year, keywords)
4. Score relevance based on keyword match density
5. Generate structured index report → Keywords-Report/
```

---

## 6. Literature Summarizer

**Purpose**: Create WeChat Official Account (微信公众号) style summaries of papers — engaging, bilingual, richly formatted.

**Trigger**: User provides a paper path or title and requests a summary.

### Tools Used

| Tool | Purpose |
|------|---------|
| `Read` | Read paper .md, read images directory |
| `Bash` | `ls` images, `test -f` verify file existence |
| `Write` | Write summary .md to Summary/ |
| `Edit` | Polish/fix after initial generation |

### Template Structure

```markdown
# [Engaging Title with Emoji]

## 📄 论文基本信息 (bilingual: title, authors, journal, DOI, citation)
## 🎯 研究背景与动机 (why this problem, limitations of prior work)
## 💡 核心创新点 (5 key contributions)
## 🔬 技术实现与方法 (device structure, fabrication, architecture)
## 📊 关键实验结果与性能指标 (tables with parameters and values)
## 🎯 核心意义与影响 (technical, academic, application)
## 🔍 器件特性总结 (electrical characteristics table)
## 🚀 未来发展方向 (short-term optimization, long-term outlook)
## 💡 个人见解 (personal analysis)
## 📚 关键术语解释
## 🔗 相关文献
```

### Image Embedding Rules (CRITICAL)

```
✅ ![[../Outputs/{folder}/hybrid_auto/images/{exact_hash}.jpg]]  (wiki-link, no %20)
❌ ![](path)    — standard markdown, won't render in Obsidian
❌ %20 in path — Obsidian wiki-links handle spaces natively
❌ Guessed hash — MUST verify exact filename with ls/test -f
```

### File Naming

`Summary/{Key-Term}-{Year}-{Short-Topic}.md`

Example: `FeFET-2026-vortex-tubes-flexible-memory.md`

### Key Improvement

**Image verification**: Originally images were embedded with guessed filenames. Now requires `ls` / `test -f` verification of exact hash filenames before embedding. Missing images are skipped with a note, not guessed.

---

## 7. Citation Assistant

**Purpose**: Read user's academic writing, find matching papers from the library, insert formatted citations with bidirectional wikilinks, and generate visual citation maps.

**Trigger**: User writes a paragraph and says "帮我添加引用", "citation", or calls the agent.

### Tools Used

| Tool | Purpose |
|------|---------|
| `Read` | Read user's writing, read paper frontmatter |
| `Bash` | Search Outputs/ with grep, find matching papers |
| `Write` | Generate .canvas citation map files |
| `Edit` | Insert citations into user's text |

### Workflow

```
1. Parse user text → identify claims/sentences needing support
2. For each claim → search Outputs/ for matching papers
3. Score each candidate (3D: relevance + value + authority)
4. Extract cite field (GB/T 7714-2015 format) + wikilink
5. Two modes:
   - 学习模式 (default): suggest citations, don't modify text
   - 插入模式: actually insert citations into document
6. Generate .canvas → Citation/{topic}_Citation_Map.canvas
```

### Citation Format (GB/T 7714-2015)

```
Author. Title[J]. Journal, Year, Vol(Issue): Pages. DOI:...

Example:
Fan Z, Wan Z, Liu C K, et al. Benchmarking Test-Time DNN Adaptation at Edge
with Compute-In-Memory[J]. ACM J. Auton. Transport. Syst., 2024, 1(3): Article
16. DOI:10.1145/3665898.
```

### Scoring System (100 points)

| Category | Points | Dimensions |
|----------|--------|------------|
| 相关性 | 40 | Topic match (15) + Technical detail (15) + Timeliness (10) |
| 文献价值 | 30 | Method quality (10) + Empirical support (10) + Contribution (10) |
| 权威性 | 30 | Journal tier (15) + Author influence (10) + Citation impact (5) |

### Canvas Map Defaults (hard-won)

```
Group vertical spacing: 1000px
Text node: 320x220px
Paper node: 420x220px
Group width: 2200px, height: 600px
Edges: dashed, fromSide=right, toSide=left
Path format: Outputs/{paper_id}/hybrid_auto/{Title}.md (vault-relative, NO [[ ]])
```

### Key Improvements

| Issue | Fix |
|-------|-----|
| Edge labels too verbose | Enforced single-line, no `\n` |
| Canvas nodes "not found" | Uses vault-relative path, not wikilink |
| Scoring too vague | Adopted 3D scoring from citation-enhancer-config |
| Path format inconsistent | Standardized: `Outputs/{id}/hybrid_auto/{title}.md` |

---

## 8. Obsidian AI Importer

**Purpose**: Save AI-generated content from conversations directly into the Obsidian vault with proper formatting and wikilinks.

**Trigger**: User says "保存到Obsidian", "import this note", "save this analysis".

### Tools Used

| Tool | Purpose |
|------|---------|
| `Write` | Create .md file with frontmatter |
| `Read` | Check existing vault content for linking |

### Workflow

```
1. Accept content from conversation (analysis, notes, summaries)
2. Format with YAML frontmatter + Obsidian wikilinks
3. Save to appropriate vault directory
```

---

# Cross-Cutting Patterns

## Path Conventions

All paths use absolute format with the vault root:
```
/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/
```

- **wikilinks**: `[[Paper Title]]` for in-note references
- **Canvas paths**: `Outputs/{folder}/hybrid_auto/{Title}.md` (vault-relative, no brackets)
- **Image embeds**: `![[../Outputs/{folder}/hybrid_auto/images/{file}.jpg]]` (from Summary/)
- **PDF links in Stork reports**: `[PDF](filename.pdf)` (same-directory relative)

## Network Strategy (China)

```
Accessible directly:
  arxiv.org, openreview.net, proceedings.mlr.press, zenodo.org
  api.semanticscholar.org (rate-limit 3s, back off 30s on 429)

Blocked (don't waste time):
  openaccess.thecvf.com, sci-hub.se/.ru/.st

GitHub:
  SSH works (git@github.com), HTTPS unstable (HTTP/2 errors)
  gh auth login --web times out (OAuth device flow blocked)
```

## Agent Boundaries

```
Stork Processor  ──→  Report + PDFs in Stork/    (DOES NOT import)
Literature Importer ──→  Paper in Outputs/ with frontmatter
Literature Searcher ──→  Find papers in Outputs/
Literature Summarizer ──→  Summary in Summary/
Citation Assistant ──→  Citations + Canvas in Citation/
Keyword Indexer ──→  Report in Keywords-Report/
AI Importer ──→  Save content anywhere in vault
```

## Git Version Control

- **Repo**: https://github.com/yangliunudt-web/paper-knowledge-base
- **Auth**: SSH key (ed25519) — `git push` directly, no token needed
- **Excluded**: most of Outputs/ (200+ papers), Writing/, Stork PDFs, session data, settings.local.json
- **Included**: 3 example papers, all agent configs, Stork reports, scripts, README

---

## Quality Scripts Reference

```bash
# Fast check — are all frontmatter fields present?
bash check_frontmatter.sh

# Deep check — score each paper on completeness + correctness  
python3 deep_quality_check.py

# Batch repair — auto-fix common frontmatter issues
python3 batch_fix_v3.py
```

`PaperProcess.md` defines the full quality standard and scoring rubric.
