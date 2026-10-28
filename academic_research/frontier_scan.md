# frontier_scan v1 · 前沿方向侦察图

> 检索日期 **2026-10-28**；方法见 `README.md`。条目按六轴排布，每条给：一句话定义 · 为什么是现在 · 锚点（机构/人/可复用入口）· 五维评分 · 合作切入点。
> 标记：`✔` = 本会话经 WebSearch 命中权威来源；`◇` = 基于通识定位、机构/人名待逐条复核（下批加深）。所有一时性事实（经费、归属、奖项）随时间漂移，复核请复跑 `PROGRESS.md` 流程。

**评分速览**（前沿度/势能/可介入/交叉杠杆/本地契合，满分 5）：

| # | 方向 | 前沿 | 势能 | 可介入 | 交叉 | 本地 | 一句话判断 |
|---|---|:--:|:--:|:--:|:--:|:--:|---|
| A1 | AI-for-Science（科学发现自动化） | 5 | 5 | 4 | 5 | 5 | 本仓库最该重仓的枢纽 |
| A2 | LLM 作为被试/方法/协作者的社科 | 5 | 5 | 5 | 5 | 4 | 入口极低、争议即议题 |
| B1 | 高阶网络与复杂系统 | 4 | 4 | 4 | 5 | 4 | 把「关系」升维为「结构」 |
| B2 | 蛋白质从头设计 / 结构预测 | 4 | 5 | 3 | 3 | 2 | 已范式确立，作交叉参照 |
| C1 | 基础物理的宇宙学前沿（暗物质/暗sector） | 4 | 3 | 2 | 2 | 3 | 借 heaven_climate 的科学史切口 |
| C2 | 数学的形式化/机器辅助证明 | 4 | 4 | 4 | 3 | 5 | 与 math_clarification 直接咬合 |
| D1 | 数字人文 / 文化分析（文明尺度） | 4 | 4 | 4 | 5 | 5 | Reading_IA/Language Stacking 的自然延伸 |
| D2 | 思辨科学的神经—现象学交叉 | 3 | 3 | 3 | 4 | 5 | contemplative science 的实证化 |
| E1 | 超学科知识共产（co-production） | 3 | 3 | 4 | 5 | 4 | 方法论层，贯穿全模块 |
| E2 | 地球系统 / 气候的科学—社会接口 | 4 | 4 | 3 | 4 | 5 | heaven_climate + living_heritage |

---

## A. AI × 一切（生成性最强的枢纽）

### A1 · AI-for-Science：从「预测结构」到「自动发现」
- **一句话**：把 AI 从工具升为科学发现的**共同作者**——假设生成、实验设计、结果解释闭环。
- **为什么是现在** ✔：2024 化学诺奖授予 Hassabis、Jumper（AlphaFold 结构预测）与 Baker（蛋白质设计），标志「AI 解构生物学硬问题」被主流加冕；随后各国把 AI-for-Science 升格为**国家战略**——英国《AI for Science Strategy》配套 £10 亿级 AI Research Resource（AIRR）算力公共池 ✔；美国 NSF 设立 "Super Intelligence" 优先方向、明确押注「生物 × AI/ML 交叉」✔；OpenAI 于 2025-12 发布 **FrontierScience** 基准，把「专家级科学推理（物/化/生）」做成可打分标尺 ✔——「自动化科学发现」正从口号变成**有基准、有经费、有评测**的工程对象。
- **锚点** ✔：Google DeepMind（Hassabis/Jumper）；University of Washington·Institute for Protein Design（Baker）；NSF MPS & "Super Intelligence"；UK RI/AIRR；OpenAI FrontierScience。**可复用入口**：arXiv cs.AI/q-bio、FrontierScience 基准、HuggingFace Papers（已在 atlas `science` 域）。
- **评分** 前沿5/势能5/可介入4/交叉5/本地5。
- **合作切入点**：以本仓库的**科学史与发现语境**（heaven_climate 的观念史、math_clarification 的证明叙事）切入「AI 如何重塑发现」的**元层**——不与其拼算力，而做「AI-for-Science 的可解释性/史学评估」这一被忽视的软肋。发起方式：跟踪 FrontierScience 类基准的错例，写「机器科学推理 vs 人类科学史推理」对照研究。

### A2 · LLM 作为社会科学的方法、对象与协作者
- **一句话**：大模型同时成为①研究对象（模拟人群）、②数据采集工具（访谈/标注）、③分析引擎、④被质疑的「硅基被试」——社科方法论被整体重构。
- **为什么是现在** ✔：Nature Human Behaviour 2026 综述《Large language models for computational social science》明确把 LLM 归纳为**四种研究角色**，标志该交叉已获顶刊体系化确认 ✔；机构信号密集——UCLA 2026-08 设立**全美首个数字人文系**并主张「以人文方式对待 AI」✔；Inria 2025 首次专门招聘社科/人文学博士 ✔；NUS 新设计算社会科学与人文中心 ✔。
- **锚点** ✔：Nature Human Behaviour（综述 venue）；UCLA Digital Humanities dept；Inria CSSH 团队；NUS Centre。**入口**：开源模型 + 公开社媒/普查语料，个人即可复现。
- **评分** 前沿5/势能5/可介入5/交叉5/本地4。
- **合作切入点**：本仓库 `Reading_IA`（阅读与文本）与 `Language Stacking`（多语）天然提供**语料与跨文化被试**；可做「LLM 在多大程度上复现不同文明圈的阅读/价值差异」——把 LLM 当**跨文化测量仪**，直接服务跨文化经济（economics_cross_culture）。

---

## B. 复杂系统与结构（把关系升维）

### B1 · 高阶网络与复杂系统（higher-order networks）
- **一句话**：传统网络只画两两连边；「高阶」用单纯复形/超图刻画**群体同时耦合**，重新定义 contagion、协作、涌现。
- **为什么是现在** ✔：Network Science Institute London（NetSI）2025 扩张并把「高阶交互塑造复杂系统」列为**新范式**前沿 ✔；Northeastern 的 Vespignani 等以网络科学攻健康—复杂性交织问题 ✔；NYU 已有高阶网络专题研讨课程在开 ✔。
- **锚点** ✔：NetSI London；Northeastern Network Science Institute（Vespignani）；NYU NETS。◇ 高阶网络系统综述的代表作者待下批点名核实。
- **评分** 前沿4/势能4/可介入4/交叉5/本地4。
- **合作切入点**：`discovery_atlas` 的图谱**本身就是网络**（当前 188 实体/273 边，来自 Wikidata 声明）——可升级为一阶→高阶示范：把「共享类簇的多元共现」建成超图，做「发现源生态的结构涌现」研究，是零成本、真数据的上手项目。

### B2 · 蛋白质从头设计 / 结构预测（作为已确立范式参照）
- **一句话**：由序列→结构→功能反向工程，生命分子进入「按需设计」时代。
- **为什么是现在** ✔：2024 诺奖后 Baker 实验室「communal brain」式 AI 设计流水线公开报道密集 ✔；本条已**范式确立**，列于此是作为 A1 的成熟样板——衡量「AI-for-Science 是否真能改造一个领域」的基准案例。
- **锚点** ✔：UW Institute for Protein Design；RosettaCommons（开源入口）。
- **评分** 前沿4/势能5/可介入3/交叉3/本地2。
- **合作切入点**：本地契合低（需实验生物），但作**观念史/社会学案例**入库，供 A1 的元研究引用。

---

## C. 基础科学硬前沿（本仓库从科学史侧介入）

### C1 · 宇宙学与基础物理前沿（暗物质 / 暗 sector / 引力）
- **一句话**：标准模型之外的物理——定向暗物质探测、暗 sector 与弦论宇宙学交叠。
- **为什么是现在** ✔：2026 有专题会议 "Cosmological Frontiers in Fundamental Physics"（PIRSA 存档），议题含「弦论与渐隐暗 sector」「暗物质定向探测」✔；Breakthrough Prize 2026 揭晓，基础物理/数学/生命科学三项各 300 万美元，持续为硬前沿定标 ✔。
- **锚点** ✔：PIRSA/c26001；Breakthrough Prize 2026 laureates；NSF MPS ◇。
- **评分** 前沿4/势能3/可介入2/交叉2/本地3。
- **合作切入点**：不做物理本体，做**观念史与认识论**——接 `heaven_climate/celestial_appearance`「天象—观念」传统，把「暗物质这样的不可见实体如何被推理出来」写成科学哲学条目。

### C2 · 数学的形式化与机器辅助证明（Lean / 自动推理）
- **一句话**：把定理与证明写入可机器验证的构造系统（Lean 等），数学可靠性与 AI 可训练性同时被重构。
- **为什么是现在** ✔：AI 推理浪潮使「可验证的数学证明」既成训练目标又成防幻觉锚；本仓库 `math_clarification/lean` 目录**已在场**，是最该深耕的自有阵地 ✔（本地既有工作）。
- **锚点** ◇：Lean / mathlib 社区与代表推动者待点名核实；本地入口：`math_clarification/lean`。
- **评分** 前沿4/势能4/可介入4/交叉3/本地5。
- **合作切入点**：与 A1 合流——「AI 生成证明 + 形式化验证」是当下最热交叉；本仓库已有 `proof_narratives`（证明叙事），可做「叙事证明 ↔ 形式证明」的双向翻译研究。

---

## D. 文化 / 文明 / 人文（计算化）

### D1 · 数字人文与文化分析（文明尺度）
- **一句话**：用计算方法在**文明尺度**处理文本、图像、档案——远读（distant reading）、文化语料库、知识图谱。
- **为什么是现在** ✔：ADHO《Digital Humanities 2026》主会程序显示该共同体把「数字化档案、分析文本、可视化网络」作为人文学研究的正式扩展 ✔；UCLA 首个 DH 系成立 ✔ 使数字人文从项目制走向**建制化学科**。
- **锚点** ✔：ADHO/DH2026；UCLA Digital Humanities dept。**入口**：本仓库 `discovery_atlas/science` 域的 Project-Gutenberg-class 基础设施 + 自建图谱。
- **评分** 前沿4/势能4/可介入4/交叉5/本地5。
- **合作切入点**：`Reading_IA`（阅读知识图谱）、`Language Stacking`（多语/日本假名音图已在 Neo4j 导出）、`living_heritage`（活态遗产走廊）——**三条已是现成的 DH 语料与图谱**；把 D1 作为它们统一的理论伞与对外合作名片。

### D2 · 思辨科学的神经—现象学交叉
- **一句话**：冥想/意识等第一人称研究，与神经科学、现象学方法的正规交叉。
- **为什么是现在** ✔：Center for Healthy Minds（UW–Madison，Richie Davidson）2025 持续输出正念冥想的神经科学研究 ✔——本仓库已有 `contemplative science` 模块（含对齐文献综述），该领域实证基础设施可对接。
- **锚点** ✔：Center for Healthy Minds（Davidson）。◇ 现象学一侧代表人物待核。
- **评分** 前沿3/势能3/可介入3/交叉4/本地5。
- **合作切入点**：以本仓库 `contemplative science` 的跨文献对齐工作为桥，接 D2 实证圈；结合 A2，可探讨「LLM 能否模拟第一人称报告」这一激进交叉题。

---

## E. 超学科与方法层（贯穿全模块）

### E1 · 超学科知识共产（co-production of knowledge）
- **一句话**：学术系统与政策、社群、地方性知识**共同生产**——不是「研究完了告诉社会」，而是社会全程参与。
- **为什么是现在** ✔：co-production 文献把其定义为横跨「科学—政治关系、知识民主、超学科」的多义框架 ✔，成为可持续发展/健康/遗产研究的默认方法论；这恰是**知识工程平台**的元问题。
- **锚点** ✔：co-production 概念综述（ResearchGate 汇编的多理论视角）◇ 具体机构待核。
- **评分** 前沿3/势能3/可介入4/交叉5/本地4。
- **合作切入点**：把整个 `gruel_cooking` 当作**知识共产的活样本**——多模块、多文明圈、双语，天然是 transdisciplinary 案例；可撰写「个人知识工程如何实践 co-production」方法论文，反哺 living_heritage 的社区田野。

### E2 · 地球系统科学与气候的科学—社会接口
- **一句话**：气候从纯物理走向「地球系统 + 社会决策」的耦合研究，强调区域人才与情境化工具。
- **为什么是现在** ✔：Schmidt Sciences《Research Frontiers Network》明确以「区域人才培养 + 情境化工具推进地球系统研究、服务气候决策」为纲 ✔。
- **锚点** ✔：Schmidt Sciences RFN。**入口**：Our World in Data（已在 atlas `science` 域，✔ 实测可达）。
- **评分** 前沿4/势能4/可介入3/交叉4/本地5。
- **合作切入点**：`heaven_climate`（气候与观念史）+ `living_heritage`（遗产与社区）是本土接口；用 OWID 公开数据做「气候观念 vs 气候数据」的跨文化可视化条目。

---

## 附：本仓库既有的「未接入」潜在方向
- `economics_cross_culture` → 可接 **A2**（LLM 作跨文化测量仪）与 **E1**（co-production）。
- `Language Stacking-Linguistic Weaving` → 天然 **D1**（多语数字人文），已具 Neo4j 图谱底座。
- `math_clarification` → **C2** 直接落地阵地。

## 下批待办（诚实缺口）
1. **学者名录加深**（f5）：为每条方向补 2–3 位**具名**学者，逐条 WebSearch 核实机构与代表作后再写，杜绝凭标签臆造。
2. **代表性论文/基准链接**：A1/A2/C2 各挂 2–3 篇一手 arXiv/Nature 文献（带 DOI/arXiv id）。
3. **可复现入口清单**：把各「公开数据/基准/工具」做成可点链接表，评估个人独立介入成本。
4. 标 ◇ 者一律转 ✔ 或删除。
