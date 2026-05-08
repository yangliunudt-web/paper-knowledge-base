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
---
```

**关键要求**：
- ✅ 所有字符串值必须用双引号`"`包裹
- ❌ 不要用单引号`'`
- 作者使用数组格式，每个作者单独一行
- 关键词使用数组格式，包含wikilinks`[[ ]]`
- abstract_cn必须是完整中文翻译

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
