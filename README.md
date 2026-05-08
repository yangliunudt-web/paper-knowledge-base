# Paper Knowledge Base

Obsidian vault for managing academic papers on ferroelectric FETs (FeFETs), in-memory computing (IMC), neuromorphic computing, and related semiconductor devices. 200+ papers with structured frontmatter, wiki knowledge layer, and automated agent workflows.

---

## Architecture (Karpathy LLM Wiki Model)

```
Layer 1: Outputs/         原始论文（不可变）            Agents 只读
Layer 2: wiki/            LLM 维护的知识层              概念页、领域页、日志
Layer 3: CLAUDE.md        Schema 规范                   Agent 行为定义
```

```
Papers/
├── Outputs/                    # Layer 1: 200+ papers
│   └── {Paper ID}/hybrid_auto/
│       ├── {Title}.md          # Full paper with frontmatter
│       ├── {Title}_origin.pdf
│       └── images/
├── wiki/                       # Layer 2: LLM-maintained knowledge
│   ├── 概念/                   # 21 concept pages (aliases, definitions, paper tables)
│   ├── 领域/                   # 4 domain compilation pages
│   ├── Wiki 目录.md            # Content directory (LLM-maintained)
│   ├── 操作日志.md             # Operation timeline
│   ├── 论文分组索引.md         # Paper topic grouping index
│   └── 知识库概览.md           # Landing page
├── templates/                  # Page templates
│   ├── concept.md              # Concept page template
│   ├── topic.md                # Domain topic template
│   └── synthesis.md            # Cross-analysis template
├── .agents/                    # Agent configs
├── Stork/                      # Stork digest reports
├── Citation/                   # Citation maps (.canvas)
├── Keywords-Report/            # Keyword index reports
├── Summary/                    # WeChat-style summaries
├── Writing/                    # Paper drafts (gitignored)
├── CLAUDE.md                   # Layer 3: Schema + agent specs
└── README.md
```

### Wiki Key Rules

- **绝不修改 Outputs/**（除非 ingest 新论文）
- **Agent 搜索优先经过 wiki/概念/** → 概念页是预计算搜索缓存，含别名归一化和论文索引
- **ingest 后必须同步更新 wiki 层** → 概念页 → 分组索引 → 领域页 → 目录 → 日志
- **论文不移动** → 分组通过 `wiki/论文分组索引.md` 维护逻辑关系
- **所有 wiki 页面必须有 frontmatter** → 概念页用 `templates/concept.md` 模板

---

## Wiki Operations

### 1. Ingest（摄取新论文）

```
1. PDF → automator → Outputs/{id}/hybrid_auto/{Title}.md
2. Rename .md → full paper title
3. Write frontmatter (keywords, abstract, aiSum, cite, confidence)
4. Quality check (check_frontmatter.sh)
5. 概念提取与更新 → 匹配/创建 wiki/概念/ 页面，填充 wiki_concepts
6. 分组索引更新 → 归入 论文分组索引
7. 领域编译页更新 → 匹配 domain_keywords，更新关键论文表格
8. 交叉引用 → 双向 wikilinks，检查矛盾声明
9. 更新 Wiki 目录 + 追加操作日志
10. 验证 → 所有 keywords 都有对应概念页
```

### 2. Query（搜索）

```
Phase 0: wiki/概念/ 页面优先（毫秒级，aliases 归一化命中率高）
Phase 1: frontmatter grep（补充 Phase 0 未覆盖的论文）
Phase 2: 全文深度 grep（精确数值/正则匹配）
→ 结果标注 confidence + wiki 概念页链接
→ 追加操作日志
```

### 3. Lint（健康检查）

```
python3 lint-wiki.py --report

8 维检查：
  1. 死链 — [[wikilinks]] 指向不存在的页面
  2. 孤页 — 零入站链接的页面
  3. 过时页面 — >30 天未更新 + 易过时标签
  4. 缺失概念页 — 关键词出现 ≥5 次但 wiki/概念/ 无页面（含 aliases 感知）
  5. 标签规范 — 不在受控词汇表中的标签
  6. 矛盾声明 — superalitive claims flag 人工审核
  7. 论文覆盖 — 未被 wiki 引用的论文
  8. Frontmatter 质量 — wiki 页面必需字段检查
```

### 双向引用体系

```
Paper → Wiki:  keywords ([[wikilinks]]) + wiki_concepts (显式引用)
Wiki → Paper:  概念页/领域页表格 ([[完整论文标题|简短显示名]])
```

`wiki_concepts` 匹配源：
- **frontmatter keywords** — 直接匹配概念页名或 aliases
- **正文 wikilinks**（≥2 次出现）— 补充未被列为 formal keyword 的重要概念

---

## Agents

### 1. Literature Importer

**触发**: 用户提供 PDF → "导入这篇论文"

**10 步 ingest 流程**: 导入检测 → automator → 重命名 → frontmatter → wiki 概念更新 → 分组索引 → 领域页 → 交叉引用 → 目录/日志 → 验证

**新增 wiki 层步骤（Step 5-10）**:
- 关键词匹配概念页 aliases → 自动填充 `wiki_concepts`
- 新概念自动创建概念页（`templates/concept.md`）
- 领域页 key paper 表格自动追加
- 跨领域论文同时更新多个领域页

### 2. Literature Searcher

**触发**: 用户搜索论文关键词/作者/数值

**3 阶段搜索**: wiki/概念/ (毫秒级) → frontmatter grep → 全文 regex

**特色**: 数值智能搜索（精确/模糊/范围）、多单位统一（fJ/pJ/nJ/µJ）、搜索记忆 + 文献库更新感知、结果标注 confidence + wiki 概念页链接

### 3. Literature Downloader

**触发**: 批量下载 PDF

**10 级下载渠道优先级**: arXiv → OpenReview → PMLR → NeurIPS → Zenodo → arXiv Web Search → Semantic Scholar → WebSearch → Library Portal → Sci-Hub

**中国网络适配**: arXiv/OpenReview 直连；Sci-Hub 被封；Library Portal（gfkd.chaoxing.com）验证通过

### 4. Stork Processor

**触发**: 用户转发 Stork 文献鸟 digest PDF

**6 步流程**: 解析 PDF → 筛选相关论文 → 多渠下载 → 重命名 PDF → 生成评分报告（9 维 100 分制）

**边界**: 只到报告 + PDF 下载，不导入 Outputs/（那是 Importer 的工作）

### 5. Literature Keyword Indexer

**触发**: "帮我找所有关于 XX 的文章"

**流程**: 模糊匹配 → 提取 frontmatter → 关联度评分 → 生成 Keywords-Report/

### 6. Literature Summarizer

**触发**: 对某篇论文生成摘要

**产出**: WeChat 公众号风格 markdown（10 章节模板），双语、嵌入图片

### 7. Citation Assistant

**触发**: "给我这段文字添加引用"

**流程**: 解析声明 → 搜索匹配论文 → 3 维评分 → 插入 GB/T 7714-2015 引用 → 生成 .canvas 引用地图

### 8. Obsidian AI Importer

**触发**: "保存到 Obsidian"

**流程**: 格式化对话内容 → YAML frontmatter → wikilinks → 写入 vault

---

## Quality Tools

```bash
# Frontmatter audit
bash check_frontmatter.sh

# Deep quality scoring
python3 deep_quality_check.py

# Batch fix frontmatter
python3 batch_fix_v3.py

# Wiki health check (8 dimensions)
python3 lint-wiki.py --report

# Batch add confidence (high/medium/low by journal tier)
python3 batch_add_confidence.py --dry-run
python3 batch_add_confidence.py

# Batch add wiki_concepts (keywords + body text → concept mapping)
python3 batch_add_wiki_concepts.py --dry-run
python3 batch_add_wiki_concepts.py
python3 batch_add_wiki_concepts.py --body-only  # body text only

# Populate concept page tables (wiki_concepts → 相关论文)
python3 batch_populate_concepts.py --dry-run
python3 batch_populate_concepts.py
```

---

## Paper Frontmatter Standard

```yaml
---
title: "Paper Title"
authors:
  - "Author One"
date: "2024-07-01"
year: 2024
journal: "Journal Name"
keywords:
  - "[[EnglishKeyword]]"
  - "[[中文关键词]]"
abstract: "Full English abstract..."
abstract_cn: "完整中文翻译..."
cite: "Author. Title[J]. Journal, Year, Vol(Issue): Pages. DOI:..."
aiSum: "研究问题/方法/结论/局限（至少含 2 项）"
confidence: high | medium | low
wiki_concepts:
  - "[[ConceptPage1]]"
  - "[[ConceptPage2]]"
---
```

---

## Git

- **Repo**: `git@github.com:yangliunudt-web/paper-knowledge-base.git`
- **Auth**: SSH (ed25519)
- **Ignored**: Outputs/* (except 3 examples), Stork PDFs, Writing/, sessions, .obsidian/workspace.json

```bash
git tag v{version} -m "..." && git push --tags  # 大改动前打 tag
```

---

## Version History

| Tag | Content |
|-----|---------|
| v1.0 | Baseline: 8 agents, README v1, example papers |
| v1.1 | Wiki infrastructure: 21 concept pages, templates, Wiki 目录, 操作日志 |
| v1.2 | Lint system, 4 domain compilation pages, confidence batch (202 papers) |
| v1.3 | Bidirectional linking: wiki_concepts field, concept aliases, 3 new concept pages |
| v1.4 | Domain page creation/update logic: domain_keywords, Step 6.5 in importer |
| v1.5 | Concept page paper tables populated (311 refs from wiki_concepts), lint green |
| v1.6 | Deduplicate concept tables, filter supplements, move domains to wiki/领域/ |
| v1.7 | Body text wikilinks → wiki_concepts + keywords (0 empty concept pages) |
