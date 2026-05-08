自动检查安装Obsidian的Skill：npx skills add git@github.com:kepano/obsidian-skills.git
1) title
- 文件名是否与 `title` 一致（忽略扩展名）；一致性允许的差异：标点/大小写/多余空格
- 若不一致：报告"以哪个为准"的建议（**默认以 frontmatter `title` 为准，重命名 `.md` 文件本身**；除非 title 明显缺失/错误）
  - **辅助材料（supplement）特殊规则**：文件名统一加 `sub-` 前缀，即 `sub-<title>.md`，以与其他主条目明显区分

2) journal / 3) year / 4) authors
- 是否存在；是否可从正文/引用/元信息块中找到证据片段
- authors 是否"完整列表"：至少包含前 3 位作者并标注是否截断；若正文/引用只给出 et al. 则标记为"不完整（需补全来源）"
  - **重点检查**：作者行通常紧跟在 `# 标题` 之后，格式多样，需处理：
    - LaTeX 上标：`Qiang Zhao $^{1,2}$, Hanlin Wang $^{3}$` → 去掉 ` $^{...}$` 得人名
    - 数字编号紧跟：`Name 1,8, Name 2,3` → 去掉末尾数字
    - 和 `and` 连接：`Name, Name, and Name Department` → 按逗号分割，取人名部分

5) abstract / 6) abstract_cn
- **abstract**：从 body 第一段找到 `Abstract— ...` 或 `Abstract: ...` 行，直接作为英文原文填入（保留原文，不翻译）
- **abstract_cn**：abstract 的**完整中文翻译**（允许 AI 翻译，但必须覆盖全文而非摘要性改写），且不可：
  - 用通用句式改写（如"综述 X 用于 Y，讨论 Z"）
  - 用模板翻译（所有文献 abstract_cn 都用同一格式）
  - 留空或填 `待补充`
- 若 abstract 更新/变更，abstract_cn 需提示"可能过期"

7) keywords（含双向链接）
- keywords 是否存在；来源是"原文提取"或"摘要总结"
- 是否创建了双向链接：
  - 标准：keywords 中每个词条为 `[[...]]`
  - 如果不想全部链接：可允许纯文本，但需在报告中标注"未链接"

8) cite（GB/T 7714-2015）
- cite 是否存在；格式是否接近 GB/T 7714-2015
- 最低要求：作者. 题名[J]. 刊名, 年, 卷(期): 页码. DOI/URL（缺项要标注）
- 若无法确定卷期页码：允许留空但要在报告里标注"缺失卷期页码"

9) aiSum
- 是否存在且"有实质内容"：
  - 至少包含：研究问题/方法/主要结论/局限 或 其中 >=2 项
  - 过短/空泛（如"很有启发"）标记为低质量

10) parent（仅 supplement）
- 若 type=supplement：`parent` 必填，且应为可点击的双向链接
- 同时检查主条目是否也反向链接了该 supplement（例如在主条目中列出 Supporting materials）


给出处理评分
- paper 必需字段：title, journal, year, authors, abstract, abstract_cn, keywords, cite, aiSum（9 项）
- supplement 必需字段：title, parent, year(可选), authors(可选), aiSum(可选)（按你库习惯可改）
- 完整性：
  - paper：每缺 1 项 -10 分（最低 0）
  - supplement：每缺 1 项 -20 分（因为 parent 关键）
- 正确性：
  - 标题不一致、引用格式明显不对、abstract_cn 明显非全文翻译等，按严重程度 -10 到 -40

---

## 文献导入自动化流程

### 1. Automator工作流程
- 使用命令：`automator -i "PDF文件路径" ~/Library/Services/PDFtoObsidian.workflow`
- 等待工作流程完成（约5-10秒）
- 自动生成文件夹结构和文件

### 2. 文件重命名规则（重要更新）
- **文件夹名**：保持为原始编号（如`3665898`），**不要修改**
- **MD文件名**：重命名为论文标题（如`Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory.md`）
- 其他文件（PDF、JSON）保持原始名称

### 3. Frontmatter格式要求（重要更新）
**必须使用双引号格式**以确保Obsidian正确显示属性：

```yaml
---
title: "论文标题"
authors:
  - "作者1"
  - "作者2"
  - "作者3"
date: "YYYY-MM-DD"
year: YYYY
journal: "期刊名称"
keywords:
  - "[[英文关键词1]]"
  - "[[英文关键词2]]"
  - "[[中文关键词1]]"
  - "[[中文关键词2]]"
abstract: "完整的英文摘要"
abstract_cn: "完整的中文翻译"
cite: "作者. 题名[J]. 刊名, 年, 卷(期): 页码. DOI:..."
aiSum: "AI总结：研究问题/方法/主要结论/局限"
---
```

**关键格式要求：**
- ✅ 所有字符串值使用双引号`"`包裹
- ❌ 不要使用单引号`'`
- ✅ 作者使用数组格式，每个作者单独一行
- ✅ 关键词使用数组格式，包含wikilinks`[[ ]]`
- ✅ 同时包含中英文关键词以支持双向搜索

### 4. Skills安装位置
- 项目根目录：`/Papers/.agents/skills/`
- 不要安装在子文件夹中
- 安装命令：`cd "/Papers" && npx skills add https://github.com/kepano/obsidian-skills.git --yes`

### 5. 常见问题解决
**Frontmatter不显示为属性：**
- 检查是否使用双引号而非单引号
- 检查YAML格式是否正确（三个短横线开头结尾）
- 确保在文件最开始，无空行

**Keywords不链接：**
- 确保使用`[[ ]]`格式
- 检查是否用双引号包裹

详细配置见：`.agents/literature-importer-config.md`


