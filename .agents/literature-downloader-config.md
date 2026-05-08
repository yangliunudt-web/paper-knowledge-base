# Literature-Downloader Agent 配置

## Agent 功能描述

批量下载学术论文PDF，自动选择最优下载渠道，处理各种平台URL修正和网络限制。

---

## 渠道优先级

### 第一梯队：开放平台（直接下载）

| 优先级 | 平台 | URL格式 | 备注 |
|--------|------|---------|------|
| 1 | **arXiv** | `https://arxiv.org/pdf/{id}.pdf` | 最可靠，大部分顶会论文都有 |
| 2 | **OpenReview** | `https://openreview.net/pdf?id={id}` | 正常直连 |
| 3 | **PMLR** | `https://proceedings.mlr.press/v{vol}/{id}/{id}.pdf` | 注意双层目录！ |
| 4 | **NeurIPS** | `https://proceedings.neurips.cc/paper_files/paper/{year}/file/{hash}-Paper-Conference.pdf` | 注意 /file/ 非 /hash/ |
| 5 | **Zenodo** | `https://zenodo.org/records/{id}/files/{filename}.pdf` | 部分论文有备份 |

### 第二梯队：需要搜索发现

| 优先级 | 方法 | 说明 |
|--------|------|------|
| 6 | **arXiv Web搜索** | `https://arxiv.org/search/?query={keywords}` 非API |
| 7 | **Semantic Scholar** | API获取OA PDF链接或arXiv ID |
| 8 | **WebSearch** | 用Google找arXiv ID或其他开放版本 |

### 第三梯队：需要认证

| 优先级 | 方法 | 说明 |
|--------|------|------|
| 9 | **CARSI** | 支持Springer/Wiley/IEEE（不支持AAAI） |
| 10 | **图书馆代理** | `library.xxx.edu.cn/application/url-login-proxy?url=...` |
| 11 | **Sci-Hub** | `https://sci-hub.se/{DOI}` |

---

## URL修正规则

### NeurIPS
```python
# /hash/ → /file/
url = url.replace('/hash/', '/file/')
```

旧格式: `proceedings.neurips.cc/paper/{year}/hash/{id}-Paper.pdf`
新格式: `proceedings.neurips.cc/paper_files/paper/{year}/file/{id}-Paper-Conference.pdf`

### PMLR
```python
# 双层目录
# 404: /v202/zhang23am.pdf
# 200: /v202/zhang23am/zhang23am.pdf
if '/papers/' not in url:  # 单层目录，修复为双层
    parts = url.split('/')
    paper_id = parts[-1].replace('.pdf', '')
    url = '/'.join(parts[:-1]) + f'/{paper_id}/{paper_id}.pdf'
```

### CVF (openaccess.thecvf.com)
```python
# 国内无法直连 → 直接走arXiv搜索，不要尝试直连！
# 浪费时间等待超时
if 'openaccess.thecvf.com' in url:
    arxiv_url = search_arxiv_web(title)  # 直接搜索arXiv
```

---

## arXiv搜索策略（核心）

### ❌ 不要用API
`export.arxiv.org/api/query` — 限流极严（429频繁），3秒/请求还不够，20秒+封禁

### ✅ 用Web搜索
```python
def search_arxiv_web(title):
    q = re.sub(r'[^\w\s-]', ' ', title)
    q = re.sub(r'\s+', '+', q).strip()
    url = f"https://arxiv.org/search/?query={q}&searchtype=all"
    r = requests.get(url, headers=HEADERS, timeout=30)
    match = re.search(r'href="(?:https://arxiv\.org)?/abs/(\d+\.\d+(?:v\d+)?)"', r.text)
    if match:
        arxiv_id = re.sub(r'v\d+$', '', match.group(1))
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"
```

### 搜索尝试顺序
1. 精确标题关键词: `ti:"key words"`
2. 宽泛关键词: `all:word1+word2+word3`
3. 缩写/别名: 如 "ADAPROMPT" 替代全标题
4. 作者+主题: `au:lastname+AND+all:topic`

### 为什么第一次搜不到？
- arXiv标题可能不同于论文标题
- 特殊字符/标点差异
- 解决方案：用 **WebSearch** 先找到arXiv ID，再下载

---

## 下载脚本关键要素

### 请求头
```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}
```

### 速率控制
```python
# 同一域名请求间隔
DOMAIN_DELAY = {
    "arxiv.org": (2.0, 4.0),
    "openaccess.thecvf.com": None,  # 不尝试直连！
    "proceedings.neurips.cc": (2.0, 5.0),
    "openreview.net": (2.0, 4.0),
}
```

### PDF验证
```python
with open(path, 'rb') as f:
    assert f.read(4) == b'%PDF' and os.path.getsize(path) > 2000
```

### 原子写入
```python
tmp = path + ".part"
# ... download to tmp ...
shutil.move(tmp, path)  # 成功后再改名
```

---

## 国内网络特殊处理

### 被墙（不要浪费时间尝试直连）
- `openaccess.thecvf.com` — Azure IP被墙
- `sci-hub.se` — SSL错误
- `sci-hub.ru`, `sci-hub.st` — 403

### 可直连
- `arxiv.org`, `export.arxiv.org`
- `openreview.net`
- `proceedings.mlr.press`
- `proceedings.neurips.cc` — 可能较慢但不被墙
- `api.semanticscholar.org` — 偶尔429
- `zenodo.org`

---

## 付费平台处理

### Springer
- CARSI wayfless: `https://fsso.springer.com/federation/init?entityId={IDP}&returnUrl={URL}`
- 需浏览器SAML认证，无法脚本化

### AAAI
- CARSI不支持AAAI
- 多数有arXiv版本
- Semantic Scholar可获取direct download URL
- `/article/download/{submissionId}/{paperId}` 可能可直接下载

---

## 标准下载流程

```
1. 拿到论文列表（标题+URL）
2. 分类URL → 识别平台（arXiv/NeurIPS/PMLR/CVF/付费）
3. 修复已知URL问题（NeurIPS /hash/→/file/, PMLR双层目录）
4. 直接下载可直连平台的论文（arXiv/OpenReview/PMLR）
5. CVF论文 → arXiv Web搜索 → 下载
6. 付费论文 → WebSearch找arXiv ID → 下载
7. 没找到arXiv的 → Semantic Scholar查OA PDF
8. 全没找到的 → CARSI/机构代理（需用户交互）
9. 统计结果，列出仍缺失的论文
```

---

## 配置参数

| 参数 | 值 |
|------|-----|
| 请求超时(连接) | 30秒 |
| 请求超时(读取) | 120秒 |
| 域名间延迟 | 2-5秒 |
| 重试次数 | 3次 |
| 429退避 | 10-30秒 |
| 最小PDF大小 | 2000字节 |
| arXiv搜索延迟 | 2-4秒 |

---

## 更新日志

- **2026-04-28**: 创建配置
  - 总结批量下载138篇论文的经验
  - 渠道优先级：arXiv > OpenReview > PMLR > NeurIPS > Zenodo
  - 关键URL修正：NeurIPS /hash/→/file/, PMLR双层目录
  - 国内网络：CVF被墙直接绕行，arXiv API限流用Web搜索替代
  - 付费平台：CARSI（Springer）、Semantic Scholar OA（AAAI）
