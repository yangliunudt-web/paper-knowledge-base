# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is an Obsidian vault for managing and organizing academic papers, primarily focused on:
- Ferroelectric FETs (FeFETs) and memory devices
- In-memory computing (IMC) and compute-in-memory (CIM) architectures
- Neuromorphic computing and reservoir computing
- ReRAM/memristor-based computing systems
- Graph neural networks for edge computing
- 3D monolithic integration of semiconductor devices

**Knowledge Architecture**: Karpathy LLM Wiki 3-layer model:
1. **`Outputs/`** (like `raw/`) — immutable paper source files. Papers imported here with frontmatter metadata.
2. **`wiki/`** (like `wiki/`) — LLM-maintained knowledge layer. Concept pages, domain pages, synthesis, logs.
3. **`CLAUDE.md`** (like `AGENTS.md`) — Schema specification. Defines structure, conventions, and workflows for agents.

## Repository Structure

```
Papers/
├── Outputs/                    # Layer 1: immutable paper source files (200+ papers)
│   └── [Paper ID]/            # Keep original folder name (e.g., "3665898")
│       └── hybrid_auto/       # Auto-generated from PDF processing
│           ├── [paper].md     # Markdown with frontmatter
│           ├── [paper]_origin.pdf
│           ├── [paper]_layout.pdf
│           └── images/        # Extracted figures
├── wiki/                       # Layer 2: LLM-maintained knowledge layer
│   ├── 概念/                   # Concept pages (aliases, definitions, paper index)
│   ├── Wiki 目录.md            # Content directory (LLM-maintained)
│   ├── 操作日志.md             # Operation timeline log
│   ├── 论文分组索引.md         # Paper topic grouping index
│   └── 知识库概览.md           # Knowledge base landing page
├── templates/                  # Page templates for each type
│   ├── concept.md
│   ├── topic.md
│   └── synthesis.md
├── Citation/                  # Citation maps (.canvas) and reports (.md)
├── Keywords-Report/           # Keyword index reports from literature-keyword-indexer
├── Summary/                   # WeChat-style literature summaries
├── Writing/                   # Paper drafts (Introduction.md, Results.md, etc.)
├── _NonPapers/                # Non-academic imported content
├── .agents/                   # Agent configuration files
│   └── skills/                # Installed Obsidian skills (defuddle, json-canvas, etc.)
├── skills/                    # Symlinks to .agents/skills/
├── CLAUDE.md                  # Layer 3: Schema specification for Claude Code
└── .obsidian/                 # Obsidian vault configuration
```

## Paper Frontmatter Standard (CRITICAL)

All paper markdown files MUST use this exact YAML format with **double quotes**:

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
abstract_cn: "Full Chinese translation..."
cite: "Author. Title[J]. Journal, Year, Vol(Issue): Pages. DOI:..."
aiSum: "Research summary: problem/method/conclusions/limitations"
confidence: high | medium | low
  # high: Nature/Science/IEDM/VLSI/IEEE T-ED 等级别期刊或顶会
  # medium: 正规 SCI 期刊
  # low: arXiv 预印本、会议 workshop
wiki_concepts:
  - "[[ConceptPage1]]"
  - "[[ConceptPage2]]"
  # 显式引用 wiki/概念/ 中已有页面的双向链接
  # ingest 时由 literature-importer 自动填充
---
```

- `abstract_cn` must be a complete Chinese translation (not a summary rewrite). Update it when `abstract` changes.
- `cite` follows GB/T 7714-2015: `Author. Title[J]. Journal, Year, Vol(Issue): Pages. DOI:...`
- `aiSum` must contain at least 2 of: research problem / method / conclusions / limitations
- For supplement papers: add `parent: "[[Main Paper]]"` and prefix filename with `sub-`
- Reference: `PaperProcess.md` for full quality standards and scoring rubric

## Quality Check Tools

```bash
# Fast frontmatter audit (all papers)
bash check_frontmatter.sh

# Deep quality check (scoring per paper)
python3 deep_quality_check.py

# Batch fix frontmatter issues
python3 batch_fix_v3.py

# Wiki knowledge layer health check (8 dimensions)
python3 lint-wiki.py --report

# Batch add confidence field to all papers
python3 batch_add_confidence.py --dry-run  # preview first
python3 batch_add_confidence.py            # apply

# Batch add wiki_concepts field (bidirectional linking paper ↔ wiki)
python3 batch_add_wiki_concepts.py --dry-run  # preview first
python3 batch_add_wiki_concepts.py            # apply
```

## Available Agents

The `.agents/` directory contains configuration for these specialized agents. Call them via the Agent tool:

| Agent                        | Config                            | Purpose                                                                   |
| ---------------------------- | --------------------------------- | ------------------------------------------------------------------------- |
| `literature-importer`        | `literature-importer-config.md`   | Import new PDF papers → Obsidian with full frontmatter                    |
| `literature-searcher`        | `literature-searcher-config.md`   | Search papers by keyword/author/numerical values; supports fuzzy matching |
| `literature-downloader`      | `literature-downloader-config.md` | Batch download PDFs with channel priority and URL correction              |
| `literature-keyword-indexer` | (in agent definition)             | Generate keyword index reports from search queries                        |
| `literature-summarizer`      | `literature-summarizer-config.md` | Create WeChat Official Account style paper summaries                      |
| `citation-assistant`         | `citation-enhancer-config.md`     | Insert citations, generate .canvas citation maps, score paper quality     |
| `obsidian-ai-importer`       | (in agent definition)             | Save AI-generated content to Obsidian vault                               |

## PDF Import Workflow

```bash
# Step 1: Run Automator workflow
automator -i "PDF路径" ~/Library/Services/PDFtoObsidian.workflow

# Step 2: Rename .md file to paper title
# Step 3: Apply frontmatter following the standard above
# Step 4: Run quality check
```

Use the `literature-importer` agent to handle steps 2-4 automatically.

**Steps 5-10 (Wiki 同步)**: importer 完成 frontmatter 后必须继续执行：
```bash
# These are defined in .agents/literature-importer-config.md
# Step 5:  概念提取与更新 → 匹配/创建 wiki/概念/ 页面，填充 wiki_concepts
# Step 6:  分组索引更新 → 归入 wiki/论文分组索引.md
# Step 6.5: 领域编译页更新 → 匹配 domain_keywords，更新关键论文表格
# Step 7:  交叉引用 → 双向 [[wikilinks]]，检查矛盾声明
# Step 8:  更新 Wiki 目录
# Step 9:  追加操作日志
# Step 10: 验证 → 所有 keywords 都有对应概念页
```

**重要**: 如果只完成 Steps 1-4 而没有完成 Steps 5-10，wiki 知识层将不会更新，导致概念页表格缺失新论文、分组索引不同步、双向链接断裂。每次导入论文后必须完整执行 10 步。

## Feishu/Lark Wiki Import

When importing from Feishu wiki URLs:
1. Extract wiki token from URL (e.g., `https://my.feishu.cn/wiki/{token}`)
2. Get tenant_access_token via `POST /open-apis/auth/v3/tenant_access_token/internal`
3. Get node info via `GET /open-apis/wiki/v2/spaces/get_node?token={token}`
4. Get raw content via `GET /open-apis/docx/v1/documents/{obj_token}/raw_content`
5. Use `obsidian-ai-importer` agent to format and save

Credentials are available in session when needed.

## Non-Paper Content

- `_NonPapers/` — for non-academic imports (books, general articles)
- Root-level `.md` files — tutorials, reference docs (e.g., Claude Code tutorial)
- These do NOT follow the paper frontmatter standard

## Git & Sync

Git repo: `git@github.com:yangliunudt-web/paper-knowledge-base.git`
- This vault is on iCloud Drive. Git for version control, iCloud for sync.
- `Outputs/*` is gitignored (papers too large). Only 3 example papers committed.
- `Stork/**/*.pdf` gitignored. Reports (.md) are tracked.
- `Writing/` gitignored (draft manuscripts).
- Tag before major changes for rollback: `git tag v<version> && git push --tags`

## Wiki Layer (Karpathy Model)

### Architecture
1. **`Outputs/`** = `raw/` — immutable source files. Agents read papers here, never modify.
2. **`wiki/`** = `wiki/` — LLM-maintained knowledge layer. Concept pages, grouping index, operation log.
3. **`CLAUDE.md`** = `AGENTS.md` — this schema file. Defines agent behavior.

### Key Rules
- **绝不修改 Outputs/ 中的论文文件**（除非 ingest 新论文时新增）
- **Agent 搜索优先经过 wiki/概念/ 页面** → 概念页是预计算的搜索缓存，含别名归一化和论文索引
- **ingest 新论文后必须同步更新 wiki 层**：更新概念页 → 更新分组索引 → 更新 Wiki 目录 → 追加操作日志
- **论文不移动**：论文分组通过 `wiki/论文分组索引.md` 维护逻辑关系，不移动 Outputs/ 中的文件
- **wiki/ 页面格式**：所有页面必须有 frontmatter；概念页使用 `templates/concept.md` 模板

### Wiki Operations
| 操作 | 触发 | 说明 |
|------|------|------|
| ingest | 导入新论文 | 更新概念页、分组索引、目录、日志 |
| query | 用户提问 | 先查 wiki/概念/ → 再查论文 frontmatter |
| lint | 健康检查 | 死链、孤页、过时页面、矛盾声明 |

## File Path Handling

- Always use absolute paths with this pattern: `/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/`
- When embedding images in summaries: `![[../Outputs/[folder]/hybrid_auto/images/[filename]]]` (Obsidian wiki-link, no `%20` encoding)
- Canvas file nodes: `Outputs/[folder]/hybrid_auto/[paper].md` (vault-relative, no `[[ ]]`)
