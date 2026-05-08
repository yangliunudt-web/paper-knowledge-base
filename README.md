# Paper Knowledge Base

Obsidian vault for managing and organizing academic papers, focused on ferroelectric FETs (FeFETs), in-memory computing, neuromorphic computing, and related semiconductor devices.

## Structure

```
Papers/
├── .agents/                # Agent configurations (Stork, literature, citation)
│   └── skills/             # Installed Obsidian skill definitions
├── .claude/skills/         # Symlinks to active skills
├── .obsidian/              # Obsidian vault settings & plugins
├── skills/                 # Symlinks to .agents/skills/
├── Stork/                  # Stork literature alert reports
│   └── {YYYY-MM-DD}_{主题}/
│       ├── {日期}_Stork文献报告.md
│       └── *.pdf
├── CLAUDE.md               # Project instructions for Claude Code
├── PaperProcess.md         # Paper formatting quality standards
├── check_frontmatter.sh    # Fast frontmatter audit
├── deep_quality_check.py   # Deep quality scoring
├── batch_fix_v3.py         # Batch frontmatter fixer
└── skills-lock.json        # Skill version lockfile
```

## Key Workflows

### Stork Digest Processing
1. Parse Stork email PDF → extract paper list
2. Download PDFs via university library portal (journal database → direct article links)
3. Generate report with scoring, abstracts, and literature association analysis
4. Reports saved to `Stork/{YYYY-MM-DD}_{subject}/`

### Paper Importing
Use the `literature-importer` agent to import individual PDFs into the Obsidian vault with proper frontmatter.

### Quality Checks
```bash
bash check_frontmatter.sh        # Fast audit of all papers
python3 deep_quality_check.py    # Deep quality scoring
python3 batch_fix_v3.py          # Batch fix frontmatter issues
```

## Agents

| Agent | Purpose |
|-------|---------|
| `stork-processor` | Parse Stork digest, download papers, generate reports |
| `literature-importer` | Import PDF papers into Obsidian with frontmatter |
| `literature-searcher` | Search papers by keyword/author/numerical values |
| `literature-keyword-indexer` | Generate keyword index reports |
| `literature-summarizer` | Create WeChat-style paper summaries |
| `citation-assistant` | Insert citations, generate .canvas citation maps |
| `obsidian-ai-importer` | Save AI-generated content to Obsidian |

## Notes

- Paper PDFs in `Outputs/` are excluded from git (managed via iCloud)
- `Writing/` drafts are excluded from git
- Agent session data is excluded from git
