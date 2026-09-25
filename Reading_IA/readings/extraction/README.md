# extraction/ · 读物内容提取管线 · Lossless Intake Pipeline

Domain: Reading & IA. The **decode half** of intake: from a text in hand to a complete, accurate,
deep card — with no information, content, or depth lost. One pipeline per *kind* of material.

本目录是 reading → 卡片的「解码侧」：确保信息无损、内容无损、深度无损、证据无损、结构无损。
不同读物走不同透镜（kind-route），每层有最低捕获阈值（lossless ledger），由 `audit.py` 验账。

> Register 注册表：本目录接入根 harness 的 `Reading_IA/docs/workflows.md` **W1·Reading intake**。

---

## 结构 Structure

| 文件 | 作用 |
|---|---|
| `framework.md` | 无损原则 + 读物分型路由 + 分层透镜堆栈（唯一权威） |
| `extract_corpus.py` | **Layer-1 语料提取器**：EPUB/PDF/HTML → `web/data/corpus/<id>.json`（整书结构+全文，本地用，禁入库） |
| `audit.py` | 无损账本校验脚本；`--corpus` 模式核验每本 history 书的章节 brief 完整性与语料回填 |
| `prompts/novel.md` | 小说/虚构透镜提示词（literary fiction · sci-fi · crime） |
| `prompts/memoir.md` | 回忆录/证词透镜（life-writing · testimony） |
| `prompts/essay.md` | 论说/非虚构透镜（argument · medicine · social science） |
| `prompts/generic.md` | 通用兜底透镜（film · poetry · paper · 其他） |
| `audit.py` | 无损账本校验脚本（测试即文档） |

---

## 怎么用 How to use

1. **分型 kind-route**：读前先按 `framework.md` §2 给读物定 kind（novel / memoir / essay / generic）。
2. **加载透镜**：打开对应 `prompts/<kind>.md`，按其 10–12 层堆栈逐层提取。
3. **写账本 ledger**：卡片末尾填 `提取账本` 块（`framework.md` §4 的最小捕获阈值）。
4. **验账 audit**：`py -X utf8 Reading_IA/readings/extraction/audit.py` —— 任一阈值不达标 = 卡片未完成，补足而非删除。

> 原则（`framework.md` §8）：样本不足时宁可标 `◐` 进「未核」，绝不为了凑数编造；无损 = 完整 + 诚实，不是长。

---

## Layer-1 语料提取 · Corpus extractor

把「读完再手抄要点」升级为「先机器无损提取全文，再做语义提炼」的稳定管线。提取器只负责**surfacing**（暴露结构、段落、指标），不判断章节含义——含义由 `framework.md` 的五维无损透镜在其上完成。

```powershell
# 单本（显式 id）
python -X utf8 extract_corpus.py --source "C:\\path\\book.epub" --id pe-volume7-pursuit-power
# 整架企鹅欧洲，按书名自动映射到 books.json 的 volume id
python -X utf8 extract_corpus.py --penguin-dir "C:\\Docs_Here\\newReading\\企鹅欧洲"
# 提取后核验 brief 完整性 + 语料回填
python -X utf8 audit.py --corpus
```

依赖见 `requirements.txt`（装入 conda 环境 `hy_py312`）。`textstat` 的可读度指标在沙箱代理下取不到 NLTK `cmudict` 时会自动跳过——核心提取不硬依赖它。

**IP 纪律**：整书原文只落在 `web/data/corpus/`（已 `.gitignore`），是本地阅读工作产物，绝不入库；进入 `books.json` 的只有本框架下的自撰摘要与 ≤300 字引句（`framework.md` §5）。

---

## RKF · Reading Knowledge Fabric（进行中）

本目录是 RKF 的 **L0/L1 骨干**。RKF 是一套知识驱动、无硬编码、低耦合的读物信息提取 + 知识图谱 + 页面生成系统，规划见 `Reading_Knowledge_Fabric` 方案：`Reading_IA/knowledge/`（声明式 JSON 注册表：adapters/kinds/lenses/graph schema/page_spec/theme/templates）+ `Reading_IA/engine/`（薄引擎：ingest/extract_driver/graph_build/render）。设计不变量：加一本书、一种关系、一个页面区块、一种新输入格式 = 改数据，不改代码。