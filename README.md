# Paper Knowledge Base

一个基于 [Obsidian](https://obsidian.md) 的学术论文知识库，使用 **Karpathy LLM Wiki 3 层架构**管理 300+ 篇论文，由 [Claude Code](https://claude.ai/code) 驱动的 7 个 AI Agent 自动化维护。覆盖 FeFET 器件、存内计算、神经形态计算、测试时自适应（TTA）等前沿半导体与 AI 交叉领域。

> **版本**: v1.43 | **论文数**: 300+ | **概念页**: 30+ | **Agent 数**: 7

---

## 研究领域

| 领域 | 论文数 | 核心主题 |
|------|--------|----------|
| FeFET 器件与材料 | ~68 | HfO₂ 基铁电、IGZO 沟道、耐久性、多值存储、BEOL 兼容 |
| 存内计算架构 (CIM) | ~47 | 交叉开关阵列、近存计算、FeFET/RRAM/PCM 突触核、ADC/DAC |
| 神经形态计算 | ~38 | 储备池计算、SNN、STDP、Hebbian 学习、事件驱动 |
| 测试时自适应 (TTA) | ~101 | BN 自适应、提示词优化、扩散模型修复、持续在线 TTA、TTT |
| 忆阻器与阻变存储 | ~34 | ReRAM、PCM、MTJ、选通管、组合优化 |
| 持续学习与模型适配 | ~20 | 灾难性遗忘、LoRA、模型动物园、弹性权重巩固 |
| 边缘计算与 AI | ~17 | 边缘推理、6G、传感器内计算、CIM 基准测试 |

---

## 知识架构（Karpathy 3 层模型）

```
┌──────────────────────────────────────────────────┐
│  Layer 3: CLAUDE.md                              │
│  Schema 规范 — Agent 行为定义、格式标准、工作流     │
├──────────────────────────────────────────────────┤
│  Layer 2: wiki/                                  │
│  AI 维护的知识层 — 概念页、领域编译页、分组索引、日志│
├──────────────────────────────────────────────────┤
│  Layer 1: Outputs/                               │
│  论文源文件 — Markdown 全文 + YAML frontmatter     │
│  (PDF 和图片 gitignored，仅 Markdown 进版本控制)    │
└──────────────────────────────────────────────────┘
```

1. **`Outputs/`** = `raw/` — 不可变论文源文件。每篇一个文件夹，含 Markdown 全文 + YAML 元数据 + 提取图片
2. **`wiki/`** = `wiki/` — AI 维护的知识层。概念页是预计算的搜索缓存（含别名归一化和论文索引），领域页是研究方向的综合编译
3. **`CLAUDE.md`** = `AGENTS.md` — Schema 规范文件。定义 Agent 行为、格式标准、工作流

---

## 目录结构

```
Papers/
├── Outputs/                         # Layer 1: 论文源文件
│   └── [Paper Title]/               # 每篇论文一个文件夹
│       └── hybrid_auto/             # PDF 处理自动生成
│           ├── [paper].md           # Markdown 全文 + YAML frontmatter
│           ├── [paper]_origin.pdf   # 原始 PDF
│           └── images/              # 提取的图片 (img_001.jpg ~)
│
├── wiki/                            # Layer 2: 知识层
│   ├── 概念/                        # 概念页 (30+ 页: FeFET, TTA, BN, CLIP...)
│   ├── 领域/                        # 领域编译页 (FeFET研究, 存内计算研究 等)
│   ├── Wiki 目录.md                 # 内容目录
│   ├── 操作日志.md                  # 操作时间线
│   ├── 论文分组索引.md              # 论文主题分组
│   └── 知识库概览.md                # 知识库总览
│
├── templates/                       # 页面模板
│   ├── concept.md                   # 概念页模板
│   ├── topic.md                     # 领域页模板
│   └── synthesis.md                 # 综合分析模板
│
├── .agents/                         # Agent 配置文件
│   ├── literature-importer-config.md     # 论文导入 Agent
│   ├── literature-searcher-config.md     # 论文搜索 Agent
│   ├── literature-downloader-config.md   # 批量下载 Agent
│   ├── literature-summarizer-config.md   # 公众号总结 Agent
│   ├── citation-enhancer-config.md       # 引用助手 Agent
│   ├── stork-processor-config.md         # Stork 文献鸟处理 Agent
│   ├── pipeline_paddleocr.py             # PaddleOCR-VL PDF 提取
│   ├── batch_fill_metadata.py            # 批量元数据填充
│   ├── batch_fill_tta_frontmatter.py     # TTA 论文 frontmatter 填充
│   ├── batch_frontmatter.py              # 通用 frontmatter 处理
│   ├── batch_process.py                  # 批量处理
│   └── skills/                           # Obsidian 技能
│       ├── defuddle/                     # 网页清洗
│       ├── json-canvas/                  # Canvas 画布
│       ├── obsidian-bases/               # Bases 数据库
│       ├── obsidian-cli/                 # Obsidian CLI
│       └── obsidian-markdown/            # Obsidian Markdown
│
├── Citation/                        # 引用地图 (.canvas) 和引用报告 (.md)
├── Keywords-Report/                 # 关键词索引报告
├── Summary/                         # 公众号风格文献总结
├── Stork/                           # Stork 文献推送报告
├── Writing/                         # 论文手稿 (gitignored)
├── _NonPapers/                      # 非学术内容
│
├── check_frontmatter.sh             # Frontmatter 快速审计
├── deep_quality_check.py            # 深度质量评分
├── batch_fix_v3.py                  # 批量修复 frontmatter
├── batch_add_confidence.py          # 批量 confidence 评级
├── batch_add_wiki_concepts.py       # 批量 wiki_concepts 填充
├── batch_populate_concepts.py       # 批量概念页表格填充
├── lint-wiki.py                     # Wiki 8 维健康检查
├── maintain.py                      # 统一维护工具 (6 阶段)
├── REFERENCES.md                    # GB/T 7714 引用标准参考
├── PaperProcess.md                  # 论文处理质量标准
├── CLAUDE.md                        # Layer 3: Claude Code Schema
└── README.md                        # 本文件
```

---

## Paper Frontmatter 标准

所有论文 Markdown 文件必须使用此 YAML 格式（用**双引号**包裹字符串值）：

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
abstract_cn: "Complete Chinese translation..."  # 翻译，非改写
cite: "Author. Title[J]. Journal, Year, Vol(Issue): Pages. DOI:..."
aiSum: "Research problem / method / conclusions / limitations (≥2项)"
confidence: high | medium | low
pipeline: "PaddleOCR-VL"  # 仅 PaddleOCR 处理时添加
wiki_concepts:
  - "[[ConceptPage1]]"
  - "[[ConceptPage2]]"
---
```

### 字段要求

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| `title` | ✅ | string | 论文完整标题，双引号 |
| `authors` | ✅ | array | 作者列表 |
| `date` | ✅ | string | 出版日期 YYYY-MM-DD |
| `year` | ✅ | int | 出版年份 |
| `journal` | ✅ | string | 期刊/会议全名 |
| `keywords` | ✅ | array | `[[wikilink]]` 格式，匹配概念页 |
| `abstract` | ✅ | string | 完整英文摘要 |
| `abstract_cn` | ✅ | string | 完整中文翻译（不是摘要改写） |
| `cite` | ✅ | string | GB/T 7714-2015 标准引用格式 |
| `aiSum` | ✅ | string | AI 摘要：至少含 2/4（问题/方法/结论/局限） |
| `confidence` | ✅ | enum | `high` / `medium` / `low` |
| `pipeline` | 可选 | string | PaddleOCR-VL 时添加，MinerU 时不添加 |
| `wiki_concepts` | 自动 | array | ingest 时 Agent 自动填充 |

### Confidence 评级

| 等级 | 标准 | 示例 |
|------|------|------|
| **high** | 顶刊/顶会 | Nature, Science, IEDM, VLSI, ICLR, NeurIPS, CVPR, IEEE T-ED |
| **medium** | 正规 SCI 期刊 | IEEE EDL, IEEE T-Nano, APL, Scientific Reports |
| **low** | 预印本/Workshop | arXiv 预印本、会议 Workshop 论文 |

---

## PDF 导入工作流

完整的 10 步流程将 PDF 转化为论文条目并同步所有 wiki 层：

### Step 1: PDF → Markdown 提取

```bash
# 默认：PaddleOCR-VL 云端 API（公式/表格/阅读顺序质量更优）
python3 .agents/pipeline_paddleocr.py --pdf "PDF路径"

# 备选：MinerU 本地处理（仅在用户明确说"本地处理"时使用）
automator -i "PDF路径" ~/Library/Services/PDFtoObsidian.workflow
```

### Steps 2-10: 导入 + Wiki 同步

使用 `literature-importer` Agent 自动完成，或手动执行：

| Step | 操作 | 产出 |
|------|------|------|
| 2 | 重命名 .md | 匹配论文标题 |
| 3 | 填写 frontmatter | keywords, abstract, aiSum, cite, confidence |
| 4 | 质量检查 | `deep_quality_check.py` |
| 5 | 概念提取与更新 | 匹配/创建 `wiki/概念/` 页面，填充 `wiki_concepts` |
| 6 | 分组索引更新 | 归入 `wiki/论文分组索引.md` |
| 6.5 | 领域编译页更新 | 匹配 `domain_keywords`，更新关键论文表格 |
| 7 | 交叉引用 | 双向 `[[wikilinks]]`，检查矛盾声明 |
| 8 | 更新 Wiki 目录 | `wiki/Wiki 目录.md` |
| 9 | 追加操作日志 | `wiki/操作日志.md` |
| 10 | 验证 | 确认所有 keywords 都有对应概念页 |

> **⚠️ 重要**：Steps 1-4 完成后必须继续 Steps 5-10。跳过 wiki 同步将导致：概念页表格缺失新论文、分组索引不同步、双向链接断裂。

---

## Wiki 知识层操作

### 概念页 (`wiki/概念/`)

概念页是**预计算的搜索缓存**，核心价值：
- **别名归一化**：`aliases` 字段统一同义词（如 TTA = Test-Time Adaptation = 测试时适应 = Fully Test-Time Adaptation）
- **论文索引**：`相关论文` 表格列出所有引用该概念的文章，含年份和核心发现
- **知识链接**：`相关概念` 节建立概念间图谱

### 双向引用体系

```
Paper → Wiki:   keywords ([[wikilinks]]) + wiki_concepts (显式引用)
Wiki → Paper:   概念页表格 ([[完整论文标题|简短显示名]])
```

`wiki_concepts` 匹配来源：
1. **frontmatter keywords** — 直接匹配概念页名或 aliases
2. **正文 wikilinks**（≥2 次出现）— 补充未被列为 formal keyword 的重要概念

### 维护命令

```bash
# Wiki 健康检查（8 维度）
python3 lint-wiki.py --report

# 批量 wiki_concepts 填充（keyword → 概念页映射）
python3 batch_add_wiki_concepts.py --dry-run   # 预览
python3 batch_add_wiki_concepts.py             # 执行

# 批量概念页表格填充（wiki_concepts → 概念页反向索引）
python3 batch_populate_concepts.py --dry-run
python3 batch_populate_concepts.py

# 统一维护（6 阶段 check + fix）
python3 maintain.py --check        # 只读检查
python3 maintain.py --fix          # 检查 + 自动修复
python3 maintain.py --check --json # 机器可读报告
```

---

## 文献下载方法

> 经 138 篇 TTA 论文批量下载实战验证，详见 `.agents/literature-downloader-config.md`

### 渠道优先级

| 优先级 | 平台 | 格式 | 备注 |
|--------|------|------|------|
| 1 | **arXiv** | `arxiv.org/pdf/{id}.pdf` | 最可靠，直接下载 |
| 2 | **OpenReview** | `openreview.net/pdf?id={id}` | 正常直连 |
| 3 | **PMLR** | `proceedings.mlr.press/v{vol}/{id}/{id}.pdf` | ⚠️ 注意双层目录 |
| 4 | **NeurIPS** | `proceedings.neurips.cc/.../file/{hash}-Paper-Conference.pdf` | ⚠️ `/hash/` → `/file/` |
| 5 | **Zenodo** | `zenodo.org/records/{id}/files/{filename}.pdf` | 部分论文有备份 |
| 6 | **arXiv Web 搜索** | `arxiv.org/search/?query={keywords}` | 非 API，避免 429 |
| 7 | **Semantic Scholar** | API 获取 OA PDF 链接 | 辅助发现 |
| 8 | **WebSearch** | Google 搜索 arXiv ID | 兜底搜索 |
| 9 | **CARSI / Sci-Hub** | 机构认证 / `sci-hub.se/{DOI}` | 最后手段 |

### 下载流程

```
1. 拿到论文列表（标题 + DOI/URL）
2. 识别平台 → 分类 URL
3. 修复已知问题：
   - NeurIPS: /hash/ → /file/
   - PMLR: 单层目录 → 双层目录（/v202/id/id.pdf）
4. 直接下载开放平台论文（arXiv / OpenReview / PMLR）
5. CVF 论文 → arXiv Web 搜索（CVF 国内被墙，别直连！）
6. 付费论文 → WebSearch 找 arXiv ID → 下载
7. 仍未找到 → Semantic Scholar OA PDF
8. 最后手段 → CARSI 机构认证（需浏览器交互）
9. 统计结果，列出缺失
```

### 国内网络注意事项

| 被墙（别浪费时间） | 可直连 |
|-------------------|--------|
| `openaccess.thecvf.com` | `arxiv.org` |
| `sci-hub.se` (SSL 错误) | `openreview.net` |
| `sci-hub.ru`, `sci-hub.st` (403) | `proceedings.mlr.press` |
| | `proceedings.neurips.cc` (慢但不被墙) |
| | `api.semanticscholar.org` (偶尔 429) |
| | `zenodo.org` |

### arXiv 搜索策略

- **不要用 API**：`export.arxiv.org/api/query` 限流极严（429 频繁），20s+ 封禁
- **用 Web 搜索**：`arxiv.org/search/?query={keywords}`
- **搜索顺序**：精确标题 → 宽泛关键词 → 缩写/别名 → 作者+主题

---

## 质量检查工具

```bash
# Frontmatter 快速审计（所有论文）
bash check_frontmatter.sh

# 深度质量检查（逐篇 100 分制评分）
python3 deep_quality_check.py

# 批量修复 frontmatter
python3 batch_fix_v3.py

# 批量 confidence 评级
python3 batch_add_confidence.py --dry-run   # 预览
python3 batch_add_confidence.py             # 执行

# 批量 wiki_concepts 填充
python3 batch_add_wiki_concepts.py --dry-run
python3 batch_add_wiki_concepts.py

# 批量概念页表格填充
python3 batch_populate_concepts.py --dry-run
python3 batch_populate_concepts.py

# Wiki 8 维健康检查
python3 lint-wiki.py --report

# 6 阶段统一维护
python3 maintain.py --check         # 只读
python3 maintain.py --fix           # 检查+修复
python3 maintain.py --phase=2 --fix # 仅修复 keywords
python3 maintain.py --phase=3 --fix # 仅修复 journal
```

---

## 可用 Agent

通过 Claude Code 的 Agent 工具调用：

| Agent | 配置 | 功能 |
|-------|------|------|
| `literature-importer` | `literature-importer-config.md` | PDF → Obsidian 完整 10 步流程 |
| `literature-searcher` | `literature-searcher-config.md` | 关键词/作者/数值搜索（精确+模糊） |
| `literature-downloader` | `literature-downloader-config.md` | 批量下载 PDF，自动渠道+URL修正 |
| `literature-keyword-indexer` | (内置) | 关键词索引报告生成 |
| `literature-summarizer` | `literature-summarizer-config.md` | 公众号风格论文总结 |
| `citation-assistant` | `citation-enhancer-config.md` | 插入引用 + .canvas 引用地图 |
| `obsidian-ai-importer` | (内置) | 保存 AI 对话到 Obsidian |

---

## Git 工作流

```bash
# 仓库
git clone git@github.com:yangliunudt-web/paper-knowledge-base.git

# 提交规范
git tag v1.XX -m "描述" && git push && git push --tags
```

### .gitignore 排除项

| 路径 | 原因 |
|------|------|
| `Outputs/**/*.{pdf,jpg,png,json}` | 论文 PDF/图片太大 |
| `Stork/**/*.pdf` | 文献推送 PDF |
| `Writing/` | 手稿草稿 |
| `.obsidian/workspace*.json` | 工作区状态 |
| `.obsidian/cache` | 缓存 |
| `.obsidian/plugins/agent-client/` | 含 API 密钥 |
| `.obsidian/bookmarks.json` | 个人书签 |
| `.claude/settings.local.json` | 个人权限 |
| `_NonPapers/` | 非学术内容 |
| `__pycache__/`, `*.pyc` | Python 缓存 |

### 同步方案

- **Git**：版本控制 + GitHub 远程备份
- **iCloud**：Obsidian 跨设备同步（Mac / iPhone / iPad）
- `Outputs/` 通过 iCloud 同步，但 PDF/图片不进 git

---

## 关键参考文档

| 文件 | 内容 |
|------|------|
| `PaperProcess.md` | 论文处理质量标准与评分细则 |
| `REFERENCES.md` | GB/T 7714-2015 引用标准参考 |
| `templates/concept.md` | 概念页模板 |
| `templates/topic.md` | 领域页模板 |
| `.agents/literature-importer-config.md` | 完整 10 步 ingest 流程定义 |
| `.agents/literature-downloader-config.md` | 下载渠道、URL 修正、网络策略 |
| `Outputs/2411.03687v1/download/TTA-方法分类报告.md` | 134 篇 TTA 文献分类案例 |
| `Outputs/3665898/download/NVM-TTA-Literature-Map.md` | NVM-TTA 文献地图案例 |

---

## License

MIT
