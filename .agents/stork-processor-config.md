# Stork Processor Agent 配置

## Agent 功能描述

解析 Stork（文献鸟）推送的"Hot papers in your field"邮件 PDF，批量下载论文（含付费论文），生成情报报告。

---

## 工作流程

### Step 1: 解析邮件 PDF
```bash
pip3 install PyPDF2 -q
python3 -c "
from PyPDF2 import PdfReader
reader = PdfReader('邮件PDF路径')
for page in reader.pages:
    print(page.extract_text())
"
```
从文本中解析：Rank、Title、Authors、Journal、Impact Factor。

### Step 2: 创建目录结构
```
Stork/
└── {YYYY-MM-DD}_{邮件主题}/
    ├── 报告.md
    ├── {FirstAuthorLastName}_{Year}_{ShortTitle}.pdf
    ├── {FirstAuthorLastName}_{Year}_{ShortTitle}.pdf
    └── ...
```
PDF 统一放在邮件文件夹根目录，不再建子文件夹。

文件命名规则：`{第一作者姓}_{年份}_{简化关键词}.pdf`
- 示例：`Chen_2026_HfO2_Ferroelectric_Post-Moore.pdf`
- 简化关键词取标题中最有辨识度的 2-4 个单词

### Step 3: 下载每篇论文（完整下载流）

#### 3.1 渠道优先级

| 优先级 | 渠道 | 方法 |
|--------|------|------|
| 1 | **arXiv** | Web 搜索 `https://arxiv.org/search/?query={keywords}` 找到 ID → 下载 `https://arxiv.org/pdf/{id}.pdf` |
| 2 | **Semantic Scholar** | `GET https://api.semanticscholar.org/graph/v1/paper/search?query={title}&limit=3&fields=title,externalIds,openAccessPdf,year` → 获取 OA PDF 或 arXiv ID |
| 3 | **WebSearch** | 用 Claude Code 的 WebSearch 找 arXiv ID、ResearchGate、作者主页 PDF |
| 4 | **Sci-Hub** | `https://sci-hub.se/{DOI}` — 备选，国内可能被墙 |
| 5 | **CARSI/机构代理** | NUDT 图书馆代理，需浏览器交互，标记为"需手动下载" |

#### 3.2 arXiv Web 搜索（不用 API）

```python
import urllib.request, urllib.parse, re, ssl

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

def search_arxiv(title):
    """用 Web 搜索找 arXiv ID，不用 API（限流严重）"""
    words = re.findall(r'[A-Za-z]{4,}', title)
    query = urllib.parse.quote('+'.join(words[:5]))
    url = f"https://arxiv.org/search/?query={query}&searchtype=all"
    req = urllib.request.Request(url, headers=HEADERS)
    resp = urllib.request.urlopen(req, timeout=20, context=ssl_ctx)
    html = resp.read().decode('utf-8', errors='ignore')
    ids = list(set(re.findall(r'/abs/(\d+\.\d+)', html)))
    return ids[:3]  # 返回前3个候选

def download_arxiv(arxiv_id, output_path):
    """下载 arXiv PDF，带原子写入和验证"""
    tmp = output_path + ".part"
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    req = urllib.request.Request(url, headers=HEADERS)
    resp = urllib.request.urlopen(req, timeout=60, context=ssl_ctx)
    with open(tmp, 'wb') as f:
        f.write(resp.read())
    with open(tmp, 'rb') as f:
        assert f.read(4) == b'%PDF', "Not a valid PDF"
        assert os.path.getsize(tmp) > 2000, "PDF too small"
    import shutil
    shutil.move(tmp, output_path)
    return True
```

#### 3.3 Semantic Scholar 搜索

```python
def search_semantic_scholar(title):
    """搜索 Semantic Scholar，返回 arXiv ID 或 OA PDF URL"""
    query = urllib.parse.quote(title[:200])
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=3&fields=title,externalIds,openAccessPdf,year"
    req = urllib.request.Request(url, headers=HEADERS)
    resp = urllib.request.urlopen(req, timeout=15, context=ssl_ctx)
    data = json.loads(resp.read().decode('utf-8'))
    if 'data' in data and len(data['data']) > 0:
        p = data['data'][0]
        arxiv = p.get('externalIds', {}).get('ArXiv', '')
        oa_url = p.get('openAccessPdf', {}).get('url', '') if p.get('openAccessPdf') else ''
        doi = p.get('externalIds', {}).get('DOI', '')
        return {'arxiv': arxiv, 'oa_url': oa_url, 'doi': doi, 'title': p.get('title', '')}
    return None
```

#### 3.4 期刊下载策略（含付费期刊）

| 期刊/出版商 | 策略优先级 | 备注 |
|------------|-----------|------|
| **Nature** (~50) | arXiv → S2 → WebSearch → CARSI/NUDT代理 → Sci-Hub | Springer Nature 支持 CARSI |
| **Science** (~45) | arXiv → S2 → WebSearch → CARSI → Sci-Hub | AAAS 支持 CARSI |
| **Advanced Materials** (~27) | arXiv → S2 → WebSearch → CARSI/NUDT代理 → Sci-Hub | Wiley 期刊，支持 CARSI |
| **Nature Comms** (~16) | 直接下载 OA PDF: `nature.com/articles/{id}_reference.pdf` | **Gold OA，无需付费** |
| **Nano-Micro Letters** (~36) | 直接下载 OA PDF: `link.springer.com/content/pdf/{doi}.pdf` | **Springer OA，无需付费** |
| **PRL/PRB** (~8-9) | arXiv 优先（覆盖率极高）→ APS 页面 | arXiv 覆盖 >90% |
| **Wiley 期刊** | arXiv → S2 → CARSI | Wiley 支持 CARSI wayfless |
| **IEEE 期刊** | arXiv → IEEE Xplore → CARSI | 部分 OA |
| **ACS 期刊** | arXiv → ACS 页面 → CARSI | 部分 OA |

#### 3.5 CARSI / 图书馆代理下载（付费论文的最后手段）

当 arXiv/Semantic Scholar/Sci-Hub 均失败时，使用 NUDT 图书馆的 CARSI 认证下载。

**NUDT 认证信息**：
- CARSI IDP: `https://idp.nudt.edu.cn/idp/shibboleth`
- 图书馆: `https://library.nudt.edu.cn/`

**构造 CARSI wayfless URL 的规则**：

| 出版商 | CARSI URL 模板 |
|--------|---------------|
| **Springer Nature** (Nature) | `https://fsso.springer.com/federation/init?entityId={IDP}&returnUrl={URL_ENCODED_PDF_URL}` |
| **Wiley** (Adv. Mater.等) | `https://onlinelibrary.wiley.com/action/ssostart?idp={IDP_ENCODED}&redirectUri={URL_ENCODED_PDF_URL}` |

**流程**：
1. 从 Semantic Scholar 获取 DOI
2. 构造期刊 PDF 直链：
   - Nature: `https://www.nature.com/articles/{article_id}.pdf`
   - Wiley: `https://onlinelibrary.wiley.com/doi/pdfdirect/{doi}`
3. 用模板生成 CARSI wayfless URL
4. 生成 HTML 下载页面，保存到邮件目录下
5. 用户在浏览器中点击链接 → 跳转 NUDT 统一认证 → 登录 → 自动下载 PDF
6. 下载后手动将 PDF 放入 Stork 目录

**HTML 页面示例**：
```html
<!-- Nature 论文示例 -->
<a href="https://fsso.springer.com/federation/init?entityId=https://idp.nudt.edu.cn/idp/shibboleth&returnUrl=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-026-10470-2.pdf">
  CARSI 下载 (Nature)
</a>

<!-- Wiley 论文示例 -->
<a href="https://onlinelibrary.wiley.com/action/ssostart?idp=https%3A%2F%2Fidp.nudt.edu.cn%2Fidp%2Fshibboleth&redirectUri=https%3A%2F%2Fonlinelibrary.wiley.com%2Fdoi%2Fpdfdirect%2F10.1002%2Fadma.202523562">
  CARSI 下载 (Wiley)
</a>
```

**注意**：CARSI 需要浏览器交互（SAML 认证），无法脚本化。这是自动化下载的最后一步。

#### 3.5 PDF 验证
```python
def verify_pdf(path):
    with open(path, 'rb') as f:
        return f.read(4) == b'%PDF' and os.path.getsize(path) > 2000
```

#### 3.7 完整下载流程（更新）

```
for each paper:
    1. 判断期刊是否 OA：
        → Nature Comms → nature.com/articles/{id}_reference.pdf 直接下载 ✅
        → Nano-Micro Letters → link.springer.com/content/pdf/{doi}.pdf 直接下载 ✅
        → 其他 OA 期刊 → 期刊 PDF 直链 ✅
    2. arXiv Web 搜索 → 找到 ID → 下载 PDF → 验证 ✅
    3. 没找到 → Semantic Scholar API（找 arXiv ID 或 OA PDF）
        → 找到 arXiv ID → 回到步骤2 ✅
        → 找到 OA PDF → 直接下载 ✅
    4. 没找到 → WebSearch（找 ResearchGate/作者主页/其他）
    5. 都没找到 → 尝试 Sci-Hub `https://sci-hub.se/{DOI}`
    6. 仍失败 → CARSI/图书馆代理：
        → 构造 CARSI wayfless URL
        → 生成 HTML 下载页面
        → 标记为 "需手动下载"，提供 CARSI 链接
```

### Step 4: 文件重命名

下载完成后，所有 PDF 统一放在邮件目录根级别，按规范重命名：

```
{FirstAuthorLastName}_{Year}_{KeyWords}.pdf
```

- 取第一作者姓（首字母大写）
- 年份用论文发表的年份
- 关键词取标题中 2-4 个最有辨识度的词（用下划线连接）
- 示例：`Chen_2026_HfO2_Ferroelectric_Post-Moore.pdf`

```bash
mv "下载时的原始文件名.pdf" "{第一作者姓}_{年份}_{关键词}.pdf"
```

### Step 5: 更新报告

**⚠️ 每次下载/重命名操作后必须同步更新报告。**

报告格式（注意：推荐总览表必须在下载情况总览之前）：
```markdown
# Stork 文献报告：{邮件主题}

**邮件日期**: YYYY-MM-DD
**论文总数**: N 篇
**成功下载**: N 篇 | **未找到**: N 篇

---

## 推荐总览

| 优先级 | # | 论文简写 | 评分 | 推荐等级 | 一句话建议 |
|--------|---|---------|------|---------|-----------|
| 1 | | | | ⭐⭐⭐⭐⭐ | **必读**：... |
| 2 | | | | ⭐⭐⭐⭐ | **推荐**：... |
| ... | | | | ⭐⭐⭐ | **浏览**：... |

---

## 下载情况总览

| # | 论文标题（简写） | 期刊 | IF | 状态 | 文件名 | 下载渠道 |
|---|---------|------|-----|------|--------|---------|
| 1 | ... | ... | ... | ✅/❌ | xxx.pdf | OA直链/arXiv/CARSI |

---

## Paper N: {完整标题}

### 基本信息
- **标题**: {title}
- **作者**: {authors}
- **期刊**: {journal} (IF: {if})
- **下载状态**: ✅ / ❌
- **PDF**: {filename}.pdf（如已下载）

### 摘要翻译
**英文原文**: {abstract}
**中文翻译**: {abstract_cn}

### 与文献库关联分析

搜索 Outputs/ 中的相关论文，用 [[wikilinks]]：

| 相关论文 | 关联度 | 关联说明 |
|---------|--------|---------|
| [[论文标题]] | ⭐⭐⭐⭐⭐ | ... |

### 价值评估（9 维度评分）

| 维度 | 满分 | 评分 | 说明 |
|------|------|------|------|
| 主题匹配度 | 15 | | 与 FeFET/存内计算/神经形态的相关性 |
| 技术细节匹配 | 15 | | 技术方法可借鉴性 |
| 时效性 | 10 | | 2026=10, 2025=9, 更早递减 |
| 研究方法质量 | 10 | | 实验/理论严谨性 |
| 实证支撑强度 | 10 | | 实验数据充分性 |
| 理论与应用贡献 | 10 | | 学术/工程贡献 |
| 期刊/会议等级 | 15 | | 按 IF 和声誉 |
| 作者影响力 | 10 | | 第一/通讯作者领域知名度 |
| 引用影响力 | 5 | | 新论文默认 2-3 分 |
| **总分** | **100** | | |

**推荐等级**: ⭐⭐⭐⭐⭐ (85+) / ⭐⭐⭐⭐ (70-84) / ⭐⭐⭐ (55-69) / ⭐⭐ (40-54)
**💡 建议**: {阅读优先级和理由}

---
```

### Step 6: 总评

```markdown
## 总评与推荐阅读优先级

| 优先级 | Paper # | 标题 | 评分 | 推荐理由 |
|--------|---------|------|------|---------|
| 1 | | | | |

### 关键建议
1. 优先获取全文：列出最值得深入阅读的 Top 3
2. 研究方向启示：各论文对用户研究的启发
3. 期刊分布概览：评估领域热度
```

---

## 目录与路径

**文献库**: `/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs/`
**Stork 存档**: `/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Stork/`
**报告模板**: `.agents/stork-processor-config.md`

---

## 网络注意事项

### 国内可直连
- `arxiv.org`、`export.arxiv.org`
- `openreview.net`、`proceedings.mlr.press`
- `api.semanticscholar.org`（偶尔 429，控制频率 3s/请求）
- `zenodo.org`

### 可能被墙
- `openaccess.thecvf.com` — 不要尝试直连
- `sci-hub.se` — SSL 错误

### 速率控制
- arXiv: 2-4 秒间隔
- Semantic Scholar: 3 秒间隔（429 时退避 30 秒）
- 并行搜索的论文数不超过 5

---

## 论文评分体系

参考 `citation-enhancer-config.md` 三维评分：
- **相关性**（40分）：主题匹配 15 + 技术细节 15 + 时效性 10
- **文献价值**（30分）：方法质量 10 + 实证支撑 10 + 理论贡献 10
- **权威性**（30分）：期刊等级 15 + 作者影响 10 + 引用影响 5

---

## 与其他 Agent 的关系

| Agent | 关系 |
|-------|------|
| `literature-downloader` | 下载策略来源，Stork 场景是批量下载的特殊应用 |
| `literature-importer` | Stork 论文不导入 Outputs/（除非决定精读），但评分标准一致 |
| `literature-searcher` | 关联分析时调用其搜索策略 |
| `citation-assistant` | 评分体系参考 |

---

## 完整处理流程总览

```
收到 Stork 邮件 PDF
    │
    ▼
Step 1: 解析邮件 → 提取论文列表（标题/作者/期刊/IF）
    │
    ▼
Step 2: 创建目录 → Stork/{YYYY-MM-DD}_{主题}/
    │
    ▼
Step 3: 批量下载（每篇逐一尝试）:
    ├── 3a. OA 期刊直链（Nature Comms, Nano-Micro Letters）
    ├── 3b. arXiv Web 搜索
    ├── 3c. Semantic Scholar API
    ├── 3d. WebSearch 全网页搜索
    ├── 3e. Sci-Hub
    └── 3f. CARSI/图书馆代理 → 生成 download_links.html → 用户手动下载
    │
    ▼
Step 4: 文件重命名 → {FirstAuthorLastName}_{Year}_{KeyWords}.pdf
    │
    ▼
Step 5: 更新报告:
    ├── 推荐总览表（开头，优先级排序 + 一句话建议）
    ├── 下载情况总览表（含文件名 + 下载渠道）
    ├── 逐篇详细分析（摘要翻译 + 文献库关联 + 9维评分）
    └── 总评（推荐阅读优先级排序 + 关键建议）
    │
    ▼
完成 ✅
```

---

## 更新记录

- **2026-05-06 v4**: 报告模板新增「推荐总览表」（开头）；新增 Step 4 文件重命名规范；新增完整处理流程总览图；修正步骤编号
- **2026-05-06 v3**: 新增 CARSI/图书馆代理下载方法（含 NUDT 认证信息、各出版商 wayfless URL 模板、HTML 下载页面生成）；Nature Comms OA PDF 格式修正（`_reference.pdf`）；重构下载流程为 6 级优先级
- **2026-05-06 v2**: 整合完整下载工作流（literature-downloader 渠道策略 + 付费期刊处理），改为扁平目录结构 + 规范文件命名
- **2026-05-06 v1**: 创建初始配置
