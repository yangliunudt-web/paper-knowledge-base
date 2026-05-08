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

## Repository Structure

```
Papers/
├── Outputs/                    # 200+ papers organized in individual directories
│   └── [Paper ID]/            # Keep original folder name (e.g., "3665898")
│       └── hybrid_auto/       # Auto-generated from PDF processing
│           ├── [paper].md     # Markdown with frontmatter
│           ├── [paper]_origin.pdf
│           ├── [paper]_layout.pdf
│           └── images/        # Extracted figures
├── Citation/                  # Citation maps (.canvas) and reports (.md)
├── Keywords-Report/           # Keyword index reports from literature-keyword-indexer
├── Summary/                   # WeChat-style literature summaries
├── Writing/                   # Paper drafts (Introduction.md, Results.md, etc.)
├── _NonPapers/                # Non-academic imported content
├── .agents/                   # Agent configuration files
│   └── skills/                # Installed Obsidian skills (defuddle, json-canvas, etc.)
├── skills/                    # Symlinks to .agents/skills/
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
automator -i "PDF文件路径" ~/Library/Services/PDFtoObsidian.workflow

# Step 2: Rename .md file to paper title (keep folder name as original ID)
# Step 3: Apply frontmatter following the standard above
# Step 4: Run quality check
```

Use the `literature-importer` agent to handle steps 2-4 automatically.

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

This vault is on iCloud Drive (`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers`). Not a git repo — no version control. Changes are synced via iCloud.

## File Path Handling

- Always use absolute paths with this pattern: `/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/`
- When embedding images in summaries: `![[../Outputs/[folder]/hybrid_auto/images/[filename]]]` (Obsidian wiki-link, no `%20` encoding)
- Canvas file nodes: `Outputs/[folder]/hybrid_auto/[paper].md` (vault-relative, no `[[ ]]`)
