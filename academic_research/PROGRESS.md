# academic_research · PROGRESS 台账

## 2026-10-28 · 模块立项 + frontier_scan v1

**动因**：用户新开「学术研究」方向，要求认真检索/分析/梳理/评估前沿学术与科研方向及相关学者（基础科学、interdiscipline、transdiscipline、AI、数据科学、计算科学、文化/文明/人文），作为开拓视野与发起跨学科合作的依据。

**落盘产物**：
- `README.md` —— 范围（六轴）· 方法（回源优先/三问过滤/锚点三元）· 五维评估标尺 · 立场
- `frontier_scan.md` —— v1 侦察图：10 条方向（A1/A2/B1/B2/C1/C2/D1/D2/E1/E2），每条含定义、为什么是现在、锚点、五维评分、合作切入点

**配套（discovery_atlas）**：同日新开第五域 `science`，登记 15 条学术发现基础设施（详见 `../discovery_atlas/PROGRESS.md` 同日条目）。

**检索记录（9 组 WebSearch · 2026-10-28）**：

| 检索问题 | 关键命中（来源域） | 用于 |
|---|---|---|
| frontier interdisciplinary research 2025-26 AI for science | UChicago DSI AI+Science；NSF "Super Intelligence"；GOV.UK AI for Science Strategy/AIRR | A1 |
| fundamental physics/math frontiers 2025 | Breakthrough Prize 2026 laureates；NSF MPS；PIRSA Cosmological Frontiers 2026 | C1 |
| computational social science / digital humanities 2025 | Inria CSSH；NUS Centre；Nature Human Behaviour LLM-CSS 综述；UCLA 首个 DH 系 | A2/D1 |
| AI-for-science scholars（Hassabis/Baker/Jumper Nobel） | GEN（Baker communal brain）；MIT Daedalus；Cambridge（Nobel 2024 三人） | A1/B2 |
| LLM science frontier / scientific discovery | Nature HBS 综述；OpenAI FrontierScience benchmark；van der Schaar Lab ICML2026 | A1/A2 |
| network science / complex systems 2025 | NetSI London 高阶交互范式；Northeastern（Vespignani）；NYU NETS；Schmidt Sciences RFN | B1/E2 |
| cultural analytics / computational humanities | LISER DH trends；ADHO DH2026 program | D1 |
| contemplative science / Davidson | Center for Healthy Minds（Richie Davidson 正念神经科学） | D2 |
| transdisciplinarity / co-production | ResearchGate co-production 概念综述；co-production Collective | E1 |

**零臆造纪律**：所有方向锚点均来自上表命中；机构/人名以命中原文为准。凡未逐条复核者（高阶网络代表作者、Lean/mathlib 推动者、现象学一侧人物、co-production 具体机构、NSF MPS 归属细节）在 frontier_scan 中以 ◇ 标注，列入「下批待办」，不写成断言。

**诚实缺口（下批改做）**：
1. 具名学者名录逐条 WebSearch 核实机构 + 代表作（f5）。
2. 代表性一手论文/基准补 DOI/arXiv id。
3. 「公开数据/工具」做成可点链接并评估独立介入成本。
4. ◇ 全部转 ✔ 或删除。

## 2026-10-28 · 学者名录回源核实（scholars.md 交付）

**动因**：用户授权继续深入。优先闭合 frontier_scan 的最大零臆造缺口——把点名学者逐条回源，机构/姓名不凭标签。

**检索记录（第 2 批·6 组 WebSearch）**：

| 学者 | 命中关键（来源域） | 状 |
|---|---|:--:|
| Hassabis & Jumper | nobelprize.org 2024-10-09；deepmind.google；APS Physics 17.149 | ✔ |
| David Baker | ipd.uw.edu；nobelprize.org；hhmi.org；PNAS doi:10.1073/pnas.2422539123 | ✔ |
| Matthew Salganik | princeton.edu；bitbybitbook.com；scholar.google（《Bit by Bit》 2018） | ✔ |
| 高阶网络（Bick/Lambiotte/Battiston） | SIAM Review（ora.ox.ac.uk）；PMC6445364；research.ceu.edu；arXiv:2203.06601 | ✔ |
| Vespignani | theinterplex.org 2026-09（Northeastern NetSI） | ✔ |
| Leo de Moura | leodemoura.github.io；en.wikipedia Lean_(proof_assistant)（2025 ACM SIGPLAN 奖） | ✔ |
| Lev Manovich | manovich.net/about（CUNY Graduate Center·Cultural Analytics Lab） | ✔ |
| Franco Moretti | english.stanford.edu；en.wikipedia（Stanford Literary Lab 2010） | ✔ |
| Richard Davidson | centerhealthyminds.org；psychiatry.wisc.edu（UW–Madison） | ✔ |

**正名纠偏**：上一轮查询中把 Davidson 误拼为 “Ricardo”→ 回源正名为 **Richard (Richie) J. Davidson**；frontier_scan 与 scholars.md 均已标注媒体常见误记。

**产物**：`scholars.md`（A1/A2/B1/C2/D1/D2 六轴共 **10 名已核实学者**，每人机构·代表作·回源锚·介入线索）；frontier_scan 对应锚点 ◇→✔（B1 代表作者、C2 推动者）并回链 scholars.md；README 产物清单新增 scholars.md。

**仍存缺（下批）**：B2（除 Baker 外）、C1 宇宙学、E1 co-production 的具名学者未逐条命中→仍 ◇，不臆造；待补 ORCID/QID 入正式档案。

## 2026-10-28 · 四项诚实缺口清欠（references / entry_points / QID / B2-C1-E1）

**动因**：用户命「continue to solve these gaps」——逐项闭合上一轮列出的四项缺口。

**回源检索（第 3 批·6 组 WebSearch）**：

| 目标 | 关键命中 | 成果 |
|---|---|---|
| B2 RFdiffusion 作者 | nature.com/articles/s41586-023-06415-8（Watson/Juergens/Bennett/Trippe，被引~3744）；ipd.uw.edu 开源 | ✔ 锁定 Watson & Juergens |
| C1 暗物质 | newscenter.lbl.gov·2026-09-01（LZ spokesperson **Kevin Lesko**，LBNL）；lz.lbl.gov | ✔ 首落具名实验人 |
| E1 co-production | doi:10.1038/s41893-019-0448-2（**Norström** et al. 2020 Nat Sustain，被引~2197）；Chambers 2021 | ✔ 奠基作者 |
| AlphaFold DOI | nature.com/articles/s41586-021-03819-2（Jumper 2021，被引~57133） | ✔ |
| FrontierScience | arXiv:2601.21165；openai.com/index/frontierscience（160 题）；github EnvCommons | ✔ |
| PNAS 三人 profile | doi:10.1073/pnas.2422539123（Berger 2026） | ✔ |

**Wikidata QID 实体消解**（临时脚本 `_resolve_scholars.py`，跑 wikidata API，**仅当 en-label 一致且有 enwiki 站点链时采**，同 resolve_qid.py 纪律）：命中 **10**——Hassabis Q3022141·Jumper Q89620738·Baker Q3814528·Salganik Q56273186·Lambiotte Q37838557·Vespignani Q4716441·de Moura Q84844322·Manovich Q716367·Moretti Q971600·Davidson Q2149302。**诚实留空 7**（Charles Bick 首命中为 1891 演员——同名异人拒采；Battiston/Watson/Juergens/Lesko/Norström/Klein 无可靠实体）。脚本用后即删。

**正名与纠偏**：① Lambiotte 前名误写 “Reiko”→正为 **Renaud**；机构据 Q37838557 改为 **University of Oxford**（原注 Namur）。② E1 奠基框架 frontier_scan v1 曾记为 “Bergmann”→据回源正为 **Norström et al. 2020**（Bergmann 系另一篇 2021 参与式综述）。

**产物**：新增 `references.md`（逐字照录一手 DOI/arXiv/PMCID/ISBN，未确证者标 ◇）与 `entry_points.md`（10 方向可复现入口×🟢🟡🔴成本×本地接缝）；`scholars.md` 补 B2/C1/E1 三节 + Wikidata QID 回填表；frontier_scan 下批待办 1-4 均标 ✔；README 产物清单新增两文件。

**诚实缺口（仍存）**：① 7 人无可靠 QID（多为新一代学者）；② ORCID 未接入；③ Bick/Lambiotte/LZ/Chambers 的确切 DOI 本会话未直接命中→标 ◇，下批经 Crossref 解析补全。
