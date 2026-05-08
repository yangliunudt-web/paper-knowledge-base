# Literature Importer Agent 配置

## Agent 功能描述

处理PDF导入Obsidian文献库的完整流程，包括导入检测、文件重命名、frontmatter格式化。

---

## 核心流程

### 1. 导入前检测机制

**步骤1：检查是否已导入到Obsidian**
- 检查`Outputs/`目录中是否已存在对应PDF编号的文件夹
- 如果已存在，跳过automator导入步骤

**步骤2：检查frontmatter是否已添加**
- 检查文件夹内的.md文件是否包含frontmatter
- 检查frontmatter格式是否正确（双引号、必需字段完整）

**步骤3：决定下一步操作**
- 已导入且frontmatter正确 → 跳过automator，只检查文件名
- 已导入但frontmatter缺失/错误 → 只处理frontmatter
- 未导入 → 执行完整automator导入流程

### 2. 文件命名规则（重要）

- **文件夹名**：保持为原始编号（如`s41467-024-55558-3`），**不要修改**
- **MD文件名**：必须重命名为完整论文标题（如`Spectral convolutional neural network chip for in-sensor edge computing of incoherent natural light.md`）
- **其他文件**：PDF、JSON、images保持不变

```bash
# 重命名命令
mv "原文件名.md" "论文标题.md"
```

### 3. Frontmatter格式规范（关键）

**⚠️ 必须使用双引号格式**：

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
confidence: high | medium | low
wiki_concepts:
  - "[[ConceptPage1]]"
  - "[[ConceptPage2]]"
---
```

**关键要求**：
- ✅ 所有字符串值必须用双引号`"`包裹
- ❌ 不要用单引号`'`
- 作者使用数组格式，每个作者单独一行
- 关键词使用数组格式，包含wikilinks`[[ ]]`
- abstract_cn必须是完整中文翻译
- confidence 根据来源可靠性判断：Nature/Science/IEDM/VLSI/IEEE → high，SCI 期刊 → medium，arXiv/预印本 → low

### 4. 必需字段检查

| 字段 | 必需 | 说明 |
|------|------|------|
| title | ✅ | 论文标题（双引号） |
| authors | ✅ | 作者列表（数组格式） |
| year | ✅ | 发表年份 |
| journal | ✅ | 期刊名称 |
| abstract | ✅ | 英文摘要 |
| abstract_cn | ✅ | 中文摘要翻译 |
| keywords | ✅ | 关键词（wikilinks格式） |
| cite | ✅ | GB/T 7714-2015格式 |
| aiSum | ✅ | 包含问题/方法/结论/局限 |
| confidence | ✅ | high（顶刊/顶会）medium（SCI期刊）low（arXiv/预印本） |
| wiki_concepts | ✅ | 显式引用 wiki/概念/ 页面（wikilinks 格式），ingest 时自动填充 |

**Cite格式要求**：
```
作者. 题名[J]. 刊名, 年, 卷(期): 页码. DOI:...
```

### 5. 处理评分标准

**完整性（100分基础）**：
- 每缺1个必需字段 -10分（最低0分）

**正确性（100分基础）**：
- 文件名与title不一致：-10分
- 引用格式明显不对：-10到-40分
- abstract_cn明显非全文翻译：-10到-40分

---

### 5. Wiki 知识层维护（ingest 后半段）

> 导入论文后必须同步更新 wiki/ 知识层。wiki/ 是 agent 搜索的预计算缓存，跳过此步骤将导致概念页和分组索引与实际论文库不同步。

**步骤5：概念提取与更新**
- 从论文 keywords 中提取所有概念（wikilink 去除 `[[ ]]` 后的名称）
- 对每个概念，检查 `wiki/概念/` 是否已有对应页面（同时检查每个概念页面的 `aliases` 字段）：
  - **无** → 读取 `templates/concept.md` 模板，创建概念页：
    - 填入定义、aliases（统一中英文/缩写等不同叫法）
    - 在"相关论文"表格中添加该论文行
    - `confidence: high` 如果期刊为 Nature/Science/IEDM/VLSI/IEEE T-ED，否则 `medium`
  - **有** → 更新已有概念页：
    - 在"相关论文"表格中追加该论文行
    - 如有新的 aliases 补入
    - 更新 `updated` 日期
- **填充 wiki_concepts**：将匹配到的概念页名称填入论文 frontmatter 的 `wiki_concepts` 字段（`"[[ConceptName]]"` 格式）
- 如果关键词未匹配到任何概念页，`wiki_concepts` 留空，后续 lint 会检测到

**步骤6：分组索引更新**
- 检查 `wiki/论文分组索引.md`，判断论文主题是否匹配已有分组
- 同主题论文 >=2 篇时自动创建/更新分组条目
- 分区名使用领域通用术语，保持精简

**步骤6.5：领域编译页更新**

> 领域编译页（`wiki/领域/<领域名> 研究.md`）是 agent 搜索的顶级入口。每篇新论文必须归入至少一个领域页。

**检测匹配：**
- 读取所有已有领域页的 `domain_keywords` 字段（在 frontmatter 中）
- 将论文的 keywords、abstract、title 与每个领域页的 `domain_keywords` 做大小写不敏感匹配
- 计算匹配分数：每个命中的 domain_keyword +1 分
- 匹配分数 ≥ 1 → 该论文属于此领域

**更新已有领域页：**
- 在"关键论文"表格中追加新论文行：`[[论文完整标题\|简短显示名]] | 年份 | 期刊 | 一句话贡献`
- 检查论文是否报告了新的最佳指标值（如更低功耗、更高耐久性），如有则更新"关键指标进展"表格
- 如果论文代表一个新的研究方向（keywords 中包含该领域新出现的概念），在"研究趋势"列表中添加一条
- 更新 frontmatter 中的 `updated` 日期

**新建领域页（触发条件）：**
- 当 `wiki/论文分组索引.md` 中某个分组积累 ≥ 5 篇论文，但尚无对应领域编译页时
- 读取 `templates/topic.md` 模板创建，填入 `domain_keywords`（从该分组的核心关键词中提取）
- 初始"关键论文"表格填入该分组中 `confidence: high` 的论文（最多 8 篇）

**论文属于多领域时：** 同时更新所有匹配的领域页。这使跨领域论文成为知识库中的连接节点。

**步骤7：交叉引用**
- 在新论文和相关概念页面间双向添加 `[[wikilinks]]`
- 检查是否有矛盾声明（如 A 论文宣称某指标为最佳，B 论文给出更优值），如有则标注双方立场

**步骤8：更新 Wiki 目录**
- 在 `wiki/Wiki 目录.md` 的对应章节添加新页面链接
- 更新"最近更新"列表

**步骤9：追加操作日志**
- 在 `wiki/操作日志.md` 中追加条目：
  ```
  ## [YYYY-MM-DD] ingest | 论文标题
  - 来源：Outputs/<文件夹>/hybrid_auto/<文件名>.md
  - 新建页面：列表
  - 更新页面：列表
  - 新增概念：列表（如有）
  - 核心洞察：一句话
  ```

**步骤10：验证**
- 确认新论文中所有 `[[keyword]]` 在 `wiki/概念/` 中均有对应页面
- 确认 `wiki/Wiki 目录.md` 和 `wiki/操作日志.md` 已更新

---

## 常见问题

### Frontmatter不显示为属性
- 检查是否使用双引号而非单引号
- 检查YAML格式是否正确（三个短横线开头结尾）
- 确保在文件最开始，无空行

### Keywords不链接
- 确保使用`[[ ]]`格式
- 检查是否用双引号包裹

### 文件路径问题
- 使用绝对路径避免相对路径问题
- 注意iCloud Drive路径中的空格处理

---

## 更新记录

- **2024-04-10**: 创建配置文档
  - 确定双引号格式为标准
  - 文件夹名保持不变，只重命名.md文件
  - 添加中英文关键词双向搜索支持
