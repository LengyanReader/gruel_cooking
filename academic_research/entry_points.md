# entry_points · 可复现介入入口

> 面向「个人/小团队独立发起合作」的现实评估。每条给：**公开数据/工具/基准 → 介入成本 → 与本地模块的接缝**。
> 成本标尺：🟢 免费开放（下载即用）· 🟡 需注册/算力/许可（低-中门槛）· 🔴 实验/机构门槛（个人难以独立介入，只能做外围/元研究）。
> 链接均为 `references.md` / `scholars.md` 回源命中所得。日期 2026-10-28。

| 方向 | 公开入口（数据/工具/基准） | 成本 | 独立可做的一件具体事 | 本地接缝 |
|---|---|:--:|---|---|
| **A1** AI-for-Science | FrontierScience 基准（github.com/EnvCommons/FrontierScience，160 题）；arXiv cs.AI；HuggingFace Papers（atlas 已登记✔） | 🟡 | 跑开源模型答 FrontierScience 子集，统计「机器科学推理 vs 人类科学史推理」错例谱 | `heaven_climate/history_of_ideas` |
| **A2** 计算社科×LLM | 《Bit by Bit》开放评审版（bookdown.org/paul/…）；sicss.io 课程；开源 LLM | 🟢 | 用开源模型对多文明圈文本做「价值/阅读差异」探测，当跨文化测量仪 | `Reading_IA`·`Language Stacking`·`economics_cross_culture` |
| **B1** 高阶网络 | xgi / HyperNetX（Python 开源超图库）；arXiv:2203.06601 综述；**本仓 `docs/discovery_atlas/graph.json` 现成一阶图** | 🟢 | 把 graph.json 的共享类簇共现升维为超图，写「发现源生态高阶结构」 | `discovery_atlas`（自有数据） |
| **B2** 蛋白质设计 | RFdiffusion 开源权重（ipd.uw.edu·2023-03）；AlphaFold DB 开放结构 | 🟡（需 GPU） | 不做本体，取公开结构案例写「AI 攻克结构生物学」观念史 | `heaven_climate/celestial_appearance`（类比法） |
| **C1** 暗物质 | LZ 公开成果页 lz.lbl.gov（数据非开放）；Breakthrough Prize 公告 | 🔴 | 仅认识论/科学哲学切入：「不可见实体如何被推理出来」 | `heaven_climate/celestial_appearance`·`core/metathinking` |
| **C2** 形式化数学 | Lean 4 + mathlib（全开源）；de Moura 2026-03 博文 | 🟢 | 把 `proof_narratives` 一篇（Erdős 单位距离反证）做 Lean 化尝试 | **`math_clarification/lean`**（已在场） |
| **D1** 数字人文 | Stanford Literary Lab Pamphlets 开放 PDF；Project Gutenberg（atlas✔）；Manovich 方法 | 🟢 | 对多文明圈藏书做远读趋势图 / 文化数据可视化 | `Reading_IA`·`Language Stacking`·`living_heritage` |
| **D2** 正念神经科学 | Center for Healthy Minds 公开研究综述（原始数据多不开放） | 🔴（临床门槛） | 以 `contemplative science` 对齐文献做方法论对话；探「LLM 能否模拟第一人称报告」 | **`contemplative science`**（已在场） |
| **E1** 知识共产 | Norström 2020 原则（开放获取·Stockholm Resilience）；Chambers 六模式 PDF（ora.ox.ac.uk 开放） | 🟢 | 用 8 条 co-production 原则自评本仓库，写方法论文条目 | `living_heritage`（社区田野）·全仓 |
| **E2** 地球系统 | Our World in Data（开放数据·atlas 已登记✔）；Schmidt RFN 公报 | 🟢 | 用 OWID 数据做「气候观念 vs 气候数据」跨文化可视化 | `heaven_climate/climate_dynamics`·`living_heritage` |
| **F1** 流动与旅游 | Annals of Tourism Research / Mobilities 期刊（文摘开放）；Sheller 开放著作 PDF | 🟡 | 用 mobilities 框架重读大运河走廊，写「移动·场所·正义」条目 | **`living_heritage`**（已在场） |
| **F2** 食物研究 | food-studies.com 开放期刊；Barnard 食物研究指南；ASFS 书目 | 🟢 | 写「清谈食物哲学 vs 食物科学」双语条目（本仓即名「粥」） | `economics_cross_culture`·仓题本身 |
| **F3** 幸福科学 | 《Bit by Bit》式开放课程；Lyubomirsky 开放页；Handbook of Wellbeing 章节 | 🟢 | 做「幸福可训练性：儒/道/佛 vs 积极心理学」对照条目 | `contemplative science`·`core/metathinking` |
| **F4** 日常美学 | SEP《Aesthetics of the Everyday》（全文开放）；Marquette 开放 PDF | 🟢 | 纯文本即可产出：「一碗粥的日常美学」札记系列 | **`core/metathinking`**（已在场） |
| **F5** 生命修行 | Center for Contemplative Research 开放文章；顶刊正念综述 | 🟡 | 发布沉思实践的双语论说；接 D2 实证 | **`contemplative science`**（已在场） |

## 按「可独立介入」排序（最易 → 最难）
1. 🟢 **B1 / C2 / D1 / E1 / E2 / A2 / F2 / F3 / F4** —— 全开源、自有数据、或纯文本即可产出真结果；**建议首批选这三个自有数据接缝**：B1（discovery_atlas graph）、C2（math_clarification/lean）、D1/E2（Reading_IA + OWID）。**用户新好轴里 F4（日常美学）与 F2（食物）门槛最低**，无需实验、只靠思辨与双语即可开工。
2. 🟡 **A1 / B2** —— 需模型权重或 GPU，可做元研究而非本体。
3. 🔴 **C1 / D2** —— 实验/临床门槛，只从科学史与认识论外围介入（与本仓库 `heaven_climate`、`contemplative science` 的取向天然一致）。

## 诚实标注
- 成本评级为**判断**非事实，附一句由；🟡/🔴 的具体许可与算力随时间/地区变动，动手前以官方页当期条款复核。
- 「开源/开放」仅指链接所证可公开获取；不代表可商用或无版权限制——用前查各仓库 LICENSE / 各站条款。
