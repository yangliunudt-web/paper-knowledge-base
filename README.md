# Paper Knowledge Base

Obsidian vault for managing and organizing academic papers, focused on ferroelectric FETs (FeFETs), in-memory computing (IMC), neuromorphic computing, and related semiconductor devices.

## Repository Structure

```
Papers/
├── .agents/                    # Agent configuration files
│   ├── stork-processor-config.md
│   ├── literature-downloader-config.md
│   ├── literature-importer-config.md
│   ├── literature-searcher-config.md
│   ├── literature-summarizer-config.md
│   ├── citation-enhancer-config.md
│   └── skills/                 # Installed Obsidian skill definitions
├── .claude/skills/             # Symlinks to active skills
├── .obsidian/                  # Obsidian vault settings & plugins
├── skills/                     # Symlinks to .agents/skills/
├── Outputs/                    # 200+ papers (git: 3 examples only)
│   └── {Paper ID}/hybrid_auto/
│       ├── {Paper Title}.md    # Markdown with YAML frontmatter
│       ├── {Paper}_origin.pdf  # Original PDF
│       ├── {Paper}_layout.pdf  # Layout PDF
│       └── images/             # Extracted figures
├── Stork/                      # Stork literature alert digests
│   └── {YYYY-MM-DD}_{主题}/
│       ├── {日期}_Stork文献报告.md
│       └── {Author}_{Year}_{Keywords}.pdf
├── Summary/                    # WeChat-style paper summaries
├── Citation/                   # Citation maps (.canvas) and reports
├── Keywords-Report/            # Keyword index reports
├── CLAUDE.md                   # Project instructions for Claude Code
├── PaperProcess.md             # Paper formatting quality standards
├── check_frontmatter.sh        # Fast frontmatter audit
├── deep_quality_check.py       # Deep quality scoring script
├── batch_fix_v3.py             # Batch frontmatter fixer
└── skills-lock.json            # Skill version lockfile
```

---

## Agents

### 1. Stork Processor

**Purpose**: Process Stork (文献鸟) literature alert digest PDFs — parse, download, and score papers.

**Workflow**:
1. **Parse** — Extract paper metadata from the Stork email PDF using PyPDF2 (title, authors, journal, IF, DOI, PMID)
2. **Filter** — Select papers relevant to FeFET/ferroelectric/IGZO/neuromorphic domains
3. **Download** — Multi-channel PDF acquisition (see priority below)
4. **Score** — 9-dimension evaluation (100-point scale): topic match, technical detail, timeliness, method quality, empirical support, theoretical contribution, journal tier, author influence, citation impact
5. **Generate Report** — Structured markdown report with recommendation overview, download status, per-paper analysis (abstract translation, literature association), and overall assessment

**Download Channel Priority**:

| Priority | Channel | Method |
|----------|---------|--------|
| 1 | arXiv | Web search `arxiv.org/search/?query={keywords}` → get ID → `arxiv.org/pdf/{id}.pdf` |
| 2 | OA direct | Nature Comms, Nano-Micro Letters, other Gold OA journals |
| 3 | Semantic Scholar | API search for OA PDF or arXiv ID |
| 4 | WebSearch | Find arXiv ID, ResearchGate, or author homepage PDF |
| 5 | Sci-Hub | `sci-hub.se/{DOI}` (may be blocked in China) |
| 6 | Library Portal | gfkd.chaoxing.com → activate database permissions → direct journal links |

**Report Format** (see `memory/stork-report-format.md` for full spec):
- Filename: `{YYYY-MM-DD}_Stork文献报告.md`
- Tables use clean `|---|---|` separators
- Paper brief names in Chinese
- PDF column with clickable links to local files

**Scope**: Stork processor ends at report generation. Does NOT import papers into Outputs/.

---

### 2. Literature Importer

**Purpose**: Import paper PDFs into the Obsidian vault with proper YAML frontmatter and formatting.

**Workflow**:
1. **Pre-import Check** — Scan `Outputs/` for existing folders matching the paper ID; check if frontmatter already exists and is correct
2. **PDF Import** — Run `PDFtoObsidian` Automator workflow to generate markdown, extract images, and create directory structure
3. **File Rename** — Keep folder as original ID; rename `.md` to full paper title
4. **Frontmatter** — Apply standard YAML format with double quotes (see `PaperProcess.md`)

**Frontmatter Standard**:
```yaml
---
title: "Paper Title"
authors:
  - "Author One"
  - "Author Two"
date: "2024-07-01"
year: 2024
journal: "Journal Name"
keywords:
  - "[[EnglishKeyword]]"
  - "[[中文关键词]]"
abstract: "Full English abstract..."
abstract_cn: "Chinese translation..."
cite: "Author. Title[J]. Journal, Year, Vol(Issue): Pages. DOI:..."
aiSum: "Summary: problem/method/conclusions/limitations"
---
```

**Quality Requirements**:
- `abstract_cn` must be a complete Chinese translation (not a summary rewrite)
- `cite` follows GB/T 7714-2015 standard
- `aiSum` must contain at least 2 of: research problem / method / conclusions / limitations
- Supplement papers: add `parent: "[[Main Paper]]"` and prefix filename with `sub-`

**Validation Tools**:
```bash
bash check_frontmatter.sh        # Fast frontmatter audit (all papers)
python3 deep_quality_check.py    # Deep quality check (per-paper scoring)
python3 batch_fix_v3.py          # Batch fix frontmatter issues
```

---

### 3. Literature Downloader

**Purpose**: Batch download academic paper PDFs with automatic channel selection and URL correction.

**Channel Priority**:

| Tier | Channel | URL Pattern | Notes |
|------|---------|-------------|-------|
| 1 | **arXiv** | `arxiv.org/pdf/{id}.pdf` | Most reliable, high coverage |
| 2 | **OpenReview** | `openreview.net/pdf?id={id}` | Direct access |
| 3 | **PMLR** | `proceedings.mlr.press/v{vol}/{id}/{id}.pdf` | Double directory required |
| 4 | **NeurIPS** | `proceedings.neurips.cc/paper_files/paper/{year}/file/{hash}-Paper-Conference.pdf` | `/file/` not `/hash/` |
| 5 | **Zenodo** | `zenodo.org/records/{id}/files/{filename}.pdf` | Backup source |

**URL Fixes**:
- NeurIPS: `/hash/` → `/file/`
- PMLR: single directory → double directory (`/v202/paper.pdf` → `/v202/paper/paper.pdf`)
- CVF (`openaccess.thecvf.com`): blocked in China, skip and go to arXiv directly

**arXiv Search Strategy** (NOT using API due to severe rate limiting):
```python
# Web search instead of export.arxiv.org API
url = f"https://arxiv.org/search/?query={keywords}&searchtype=all"
# Extract: href="/abs/(\d+\.\d+)"
# Download: https://arxiv.org/pdf/{id}.pdf
```

**Network Notes (China)**:
- ✅ Accessible: `arxiv.org`, `openreview.net`, `proceedings.mlr.press`, `api.semanticscholar.org`, `zenodo.org`
- ❌ Blocked: `openaccess.thecvf.com`, `sci-hub.se` (SSL error), `sci-hub.ru/.st` (403)
- 🔑 Library: Use gfkd.chaoxing.com journal portal to activate database access, then direct journal links

**Paywalled Journal Strategy**:

| Publisher | Strategy |
|-----------|----------|
| Nature/Science | arXiv → S2 → library portal → Sci-Hub |
| Wiley (Adv. Mater., etc.) | arXiv → S2 → library portal → Sci-Hub |
| ACS (ACS Nano, Langmuir, etc.) | arXiv → S2 → library portal |
| Nature Comms | Direct OA: `nature.com/articles/{id}_reference.pdf` |
| IEEE | arXiv → IEEE Xplore → library portal |
| Springer | CARSI wayfless: `fsso.springer.com/federation/init?entityId={IDP}&returnUrl={URL}` |

**Script Essentials**:
- Headers: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36`
- Domain delay: 2-5 seconds between requests
- PDF validation: `assert f.read(4) == b'%PDF' and size > 2000`
- Atomic writes: download to `.part` temp file, rename on success

---

### 4. Literature Searcher

**Purpose**: Search the Obsidian literature library with smart memory and numerical intelligence.

**Core Capabilities**:
- **Multi-mode Search** — keyword, author, research topic matching with fuzzy and exact modes
- **Numerical Search** — support for exact values, ranges, and fuzzy descriptions (e.g., "22.7 fJ", "20几fJ", "sub-100 fJ")
- **Search Memory** — remembers user's historical search topics; avoids returning duplicate results; re-evaluates when library updates
- **Library Update Awareness** — detects newly added papers; re-runs historical searches against new content; prioritizes latest relevant literature

**Search Path**: `Outputs/{Paper ID}/hybrid_auto/{Paper Title}.md` — searches frontmatter and body text

**Numerical Search Strategy** (two-phase):
1. Keyword search to narrow candidate papers
2. Grep with regex on matched papers for specific numerical patterns

---

### 5. Literature Keyword Indexer

**Purpose**: Generate keyword index reports from search queries across the paper library.

**Workflow**:
1. Accept search keywords from user
2. Fuzzy-match across all papers in `Outputs/`
3. Generate a structured keyword index report
4. Save to `Keywords-Report/` directory

**Use when**: User wants a batch report of all papers matching a topic, rather than finding one specific paper.

---

### 6. Literature Summarizer

**Purpose**: Create WeChat Official Account (微信公众号) style paper summaries.

**Template Structure**:
```
# [Engaging Title]

## 📄 论文基本信息
- Title, authors, journal, DOI, citation

## 🎯 研究背景与动机
## 💡 核心方法与创新点
## 📊 关键结果与分析
## 🔮 总结与展望
## 💬 个人点评
```

**Features**:
- Embedded figures from paper images directory
- Chinese-English bilingual
- Saved to `Summary/` directory
- Wikilinks to source paper in Outputs

---

### 7. Citation Assistant

**Purpose**: Insert citations with bidirectional wikilinks and generate visual citation maps.

**Workflow**:
1. **Analyze** — Read user's academic text and identify claims needing citations
2. **Search** — Find relevant papers from Outputs/ matching each claim
3. **Cite** — Insert citations formatted per the paper's `cite` field (GB/T 7714-2015) with Obsidian wikilinks
4. **Visualize** — Generate `.canvas` citation map showing paper relationships, saved to `Citation/`

**Citation Format**: GB/T 7714-2015
```
Author. Title[J]. Journal, Year, Vol(Issue): Pages. DOI:...
```

**Scoring** (3-dimension, 100-point):
- Relevance (40pts): topic match + technical detail + timeliness
- Literature Value (30pts): method quality + empirical support + theoretical contribution
- Authority (30pts): journal tier + author influence + citation impact

---

### 8. Obsidian AI Importer

**Purpose**: Save AI-generated content from conversations directly into the Obsidian vault.

**Workflow**:
1. Accept content (analysis, summaries, technical notes) from the conversation
2. Format with proper YAML frontmatter and wikilinks
3. Save to the configured Obsidian directory

**Use when**: User says "save this to Obsidian", "import this note", "save this analysis".

---

## Key Workflows

### Stork Digest Processing (Full Pipeline)
```
Receive Stork email PDF
    │
    ▼
Parse → extract paper list (title, authors, journal, IF, DOI)
    │
    ▼
Filter → keep FeFET/ferroelectric/IGZO/neuromorphic papers
    │
    ▼
Download (per paper):
    ├── OA journal direct (Nature Comms, etc.)
    ├── arXiv Web search → download PDF
    ├── Semantic Scholar API → find arXiv ID or OA PDF
    ├── WebSearch → find alternative sources
    ├── Sci-Hub → last resort
    └── Library Portal → gfkd.chaoxing.com activate → journal direct link
    │
    ▼
Rename PDFs → {FirstAuthorLastName}_{Year}_{Keywords}.pdf
    │
    ▼
Generate Report:
    ├── Recommendation overview table (with PDF links)
    ├── Download status table
    ├── Per-paper analysis (abstract translation + literature association + 9D scoring)
    └── Overall assessment
    │
    ▼
Done ✅ (literature-importer is a separate, optional next step)
```

### Paper Importing
```
User triggers literature-importer agent
    │
    ▼
Pre-check: scan Outputs/ for existing paper
    │
    ├── Already imported → check frontmatter quality → fix if needed
    └── Not imported → run PDFtoObsidian automator → format frontmatter
    │
    ▼
Quality validation → done
```

### Quality Checks
```bash
bash check_frontmatter.sh        # Fast audit of all papers
python3 deep_quality_check.py    # Deep quality scoring per paper
python3 batch_fix_v3.py          # Batch fix frontmatter issues
```

---

## Notes

- Paper PDFs in `Outputs/` are excluded from git (managed via iCloud); 3 example papers are included for demonstration
- `Writing/` drafts are excluded from git
- Agent session data (`.obsidian/plugins/agent-client/sessions/`) is excluded from git
- `.claude/settings.local.json` (personal permissions) is excluded from git
- Repository: https://github.com/yangliunudt-web/paper-knowledge-base
