# TOOLING.md · 读物提取工具版图调研 · Extraction Tooling Survey (RKF-mapped)

全网调研（GitHub / arXiv / 官方文档，检索于 2026-09）后的工具梳理。每项标注：**能力 · 许可/依赖 · 映射到 RKF 哪一层 · 采纳决策**。
设计不变量：所有工具都只服务 L0/L1（把外部读物变成 Corpus IR）或 L3（把语料变成图/结构化主张），**语义判断仍由本域 `framework.md` 五维无损透镜完成**，不把编辑权外包给第三方黑盒。

> 图例：`ADOPT` 立即纳入 · `ADAPTER` 注册为新适配器 · `DEFER` 记录备用（触发信号再启用）· `AVOID` 明确不采纳。

---

## A · 通用多格式转换器（"任意文件 → Markdown" 前门）

### microsoft/markitdown  →  `ADAPTER`（通用兜底适配器）
- 能力：PDF / Word / PowerPoint / Excel / 图片(EXIF+OCR) / 音频(转写) / HTML / CSV·JSON·XML / **ZIP(遍历内容)** / **YouTube URL(字幕)** / **EPUB** → 结构保留的 Markdown。Python 3.10–3.14，`pip install 'markitdown[all]'`，MIT。
- 官方自我定位：类比 `textract`，输出"供文本分析工具消费"，**明说不是高保真人类可读转换**。
- 对 RKF 的判断：**它是"没有专用适配器时的万能入口"，不是 epub/pdf 专用适配器的替代**。
  - 我的 `extract_corpus.py`（ebooklib+PyMuPDF）对 EPUB/PDF 能保留 *spine 顺序 / TOC / 标题树 / 每文档字数* 这些结构；markitdown 会把它压平成一段 Markdown，反而丢结构（违反结构无损）。
  - 但 markitdown 独家覆盖 DOCX/PPTX/XLSX/扫描件(配 Azure)/音频/YouTube —— 这些正是"后续各种不同读物"会用到的输入，且能一次调用出文本。
  - 结论：注册为 `file-universal` 适配器（`.docx/.pptx/.xlsx/.zip/.eml/.wav/.mp3` + YouTube URL），EPUB/PDF 仍走专用适配器。`markitdown-ocr` 插件与 Azure Content Understanding 属可选增强（需 LLM client / 云端点，非离线）。
- 安装（按需 extras，避免 [all] 拉重依赖）：`pip install markitdown[pdf,docx,pptx,xlsx]`。

---

## B · 高保真版式解析（扫描版 PDF / 复杂表格 / 公式）

| 工具 | 能力 | 许可 | RKF 映射 | 决策 |
|---|---|---|---|---|
| **opendatalab/MinerU** | 复杂文档→LLM 友好 Markdown；版面/公式/表格强；本地部署 | AGPL-3.0 | L0 `file-pdf-hifi` 可选增强 | `DEFER`（AGPL 许可需评估；扫描件出现时再引） |
| **docling (IBM)** | 版面/表格精度标杆（基准 ~97.9% 单元格），结构保留强 | MIT | L0 PDF 高保真备选 | `DEFER` |
| **marker (Datalab)** | 速度标杆（~6 页/秒），多栏处理强 | GPL-3.0 | L0 PDF 备选 | `DEFER`（GPL 注意） |
| **Unstructured** | 多源(PDF/邮件/HTML/Office/图)→语义分块，RAG 生态广 | Apache-2.0 | L0/L2 切块 | `DEFER` |
| **PyMuPDF (`fitz`)** | 高性能 PDF/多格式抽取，已装 | AGPL/commercial | **L0 已在 `extract_corpus.read_pdf` 用** | `ADOPT`（已用） |

判断：本域读物质心是 **born-digital EPUB 史书**，版面解析只有遇到扫描版/图表密集 PDF 才需要 → MinerU/docling/marker 记为 DEFER，靠 `adapters.manifest.json` 的开放插槽，信号触发再挂（S4 裂变）。

---

## C · 网页/正文抽取（"网络相关信息"输入）

| 工具 | 能力 | 决策 |
|---|---|---|
| **trafilatura**（已装 2.2.0） | 网页主正文去噪 + 元数据 + 时间推断 | `ADOPT`：L0 `web-article` 适配器主干 |
| **defuddle**（kepano skills） | 网页→干净 markdown，Obsidian 生态 | `DEFER`：与 trafilatura 重叠 |

---

## D · LLM 结构化抽取（带出处锚定）—— 服务 L2

### google/langextract  →  `DEFER`（高价值，观察）
- LLM 驱动、**按用户指令抽取结构化信息 + precise source grounding（命中定位到原文偏移）**、长文优化、交互式可视化。Apache-2.0。
- 与 RKF 高度契合：L2 的"每主张可指到证据"（信息无损）正是 langextract 的 source grounding 强项。但它把抽取交给 LLM+prompt，需保证不违反本域编辑权与 IP 纪律。
- 判断：作为 `extract_driver.py` 的**可选后端**接口预留（slot 驱动 vs prompt 驱动二选一），默认走"我读语料→填 slot"，需要批量/跨书抽取时再切 langextract。

### ContextGem / NuExtract  →  `DEFER`（同类 LLM schema 抽取，记录）

---

## E · 知识图谱 / GraphRAG —— 服务 L3

| 工具 | 能力 | 决策 |
|---|---|---|
| **Microsoft GraphRAG** | 从语料自动构图 + 社区摘要 | `DEFER`：重量级；本域图是"人工核验的实体/关系"，非自动涌现 |
| **Neo4j LLM KG Builder** | 文档→(节点/关系)→Neo4j，schema 可配 | `ADAPTER`(导出侧)：`graph_export_neo4j.py` 借鉴其 schema-driven MERGE 约定 |
| **HelixDB** | 面向 Graph+Hybrid RAG 的图库 | `DEFER`：A1 已定"文件权威 + Neo4j 可选导出"，暂不引新库 |
| **Awesome-GraphRAG (DEEP-PolyU)** | 图RAG 论文/工具清单 | 参考文献源，见 §H |

判断：与既定 A1 一致 —— **图权威是文件（nodes/edges.jsonl），Neo4j 只是 schema 驱动的可重放投影**。不引入 GraphRAG 黑盒自动构图，避免"过度耦合 + 编辑权旁落"。

---

## F · 历史文本实体识别（人名/地名/事件）—— 服务 L2/L3 的 names 维

| 资源 | 说明 | 决策 |
|---|---|---|
| **HIPE / HistText** | 历史文本 NER 共享任务与手册（人/地/其他实体） | 方法论参考；史书 `names` 维可借其分类 |
| **LLM NER of Historical Text**（arXiv 2508.18090） | 零/少样本 LLM 做历史文档 NER 可行性 | `DEFER`：可作为 names 维半自动预填 |
| **spaCy** | 通用 NER/依存 | `DEFER`：多语种史书需专训模型 |

判断：史书的人名/地名/事件是**事实性实体**（非作者独创表达），提取入图无版权障碍；`names` 维可先人工/半自动，后续用 HIPE 分类法规范化。

---

## G · 书目元数据 API —— 服务 L1 `meta` 富化（`web-catalog`）

| API | 覆盖 | 成本 | 决策 |
|---|---|---|---|
| **OpenAlex** | 5 亿学术作品/作者/概念，全开放 | 免费，REST | `ADOPT` |
| **Semantic Scholar** | 学术作品+引用图 | 免费 API | `ADOPT`（引用/关联边） |
| **Crossref** | DOI/出版物元数据 | 免费 | `ADOPT` |
| **OpenLibrary** | 大众书 ISBN/封面/作者 | 免费 | `ADOPT`（史书封面/版次） |

判断：L1 的 `meta`（出版社/页数/ISBN/封面链/主题词）由这些**结构化元数据 API** 权威富化，只取事实性字段，不抓正文。`web-catalog` 适配器专责此。

---

## H · 基准与方法参考（检索锚点）
- **OmniDocBench**（arXiv 2412.07626）：多样 PDF 文档理解基准，MinerU/Marker/Mathpix 评测口径 —— 选 B 类工具的权威依据。
- PDF 抽取横评（procycons 2025、ertas、firecrawl 2026）：Docling 精度 / Marker 速度 / Unstructured 广度的分化。
- **Awesome-GraphRAG**（DEEP-PolyU）：图RAG 综述/工具清单。
- OpenAlex 论文（Priem 2022）+ arXiv 2406.15154：学术元数据库对比。

---

## 落地到 RKF（下一步）
1. `adapters.manifest.json` 增行：`file-universal`(markitdown) 覆盖 office/zip/音视频/YouTube；`web-article`(trafilatura)；`web-catalog`(OpenAlex/Crossref/OpenLibrary/S2)。EPUB/PDF 保专用适配器。
2. L3 `graph_export_neo4j.py` 采用 Neo4j 官方 KG-Builder 的 schema-driven MERGE 约定。
3. L2 `extract_driver.py` 预留 `backend: slot | langextract` 二选一接口，默认 slot。
4. 许可护栏：AGPL/MySQL(GPL) 类（MinerU/marker）仅 DEFER，不引入运行时依赖。
