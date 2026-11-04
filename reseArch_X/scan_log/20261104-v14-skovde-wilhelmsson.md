# 20261104 · v14 舍夫德大学扫描——过闸建档 Ulf Wilhelmsson·Engström 保留 ◇ 线索

**触发**：用户问「舍夫德大学的相关工作和学科有值得考虑的吗」。本轮为**实检索**（非 schema 变更）：扫 University of Skövde（his.se）游戏学科生态，按连接闸口（README §〇·宁可少不可滥）判定建档与否。

## 一、Query 与命中

| # | Query | 命中（✔ 直采 / ◇ 未直证） |
|---|---|---|
| 1 | University of Skövde game development research（总览） | 约 12 项目/50 教研聚落·Sweden Game Arena 产业绑定；Henrik Engström（Informatics 教授·gamedevresearch.se）·Per Backlund·Ulf Wilhelmsson ✔ |
| 2 | Henrik Engström game development research professor | his.se 新闻页 2021-01-21「Professor of Informatics」+《Game Development Research》(2020/2021 开放获取) ✔；Scholar fnbCA2wAAAAJ 标签 Game Development/Serious Games ✔ |
| 3 | Skövde serious games Per Backlund | Scholar bpmrQVQAAAAJ（教育游戏效果综述 2008 起点）✔；LinkedIn 2025-10「Chair of the Council of Swedish Games Researchers」✔；MSc Serious Games 项目页 ✔ |
| 4 | Ulf Wilhelmsson philosophy of games / site:his.se | 员工页（瑞典文）「docent och biträdande professor i medier, estetik och berättande…excellent lärare」✔；SAGE 论文页注「head of the Department of Game Development」（2017 印刷版）✔·现职 ◇ |
| 5 | Game Philosophy workshop Skövde | gamephilosophy.org「Game Philosophy Network」现行 ✔；Nordic Workshops on the Philosophy of Games 由 Bergen/ITU Copenhagen/Tampere（Convergence, 2023-10/11 帖）轮办 ✔；Wilhelmsson 具体角色 ◇ |

## 二、回源核实（Wilhelmsson 建档底座）

- **Google Scholar 2iCS-zcAAAAJ 全档直读**（2026-11-04）：被引 277·h-index 10；标签 game studies/computer games/film theory/game sound；合著者列名 Backlund/Susi/Torstensson/Engström/Toftedahl/Berg Marklund/Wang/Brusk/Kävrestad。关键条目全部带卷期/年份/被引：Caillois×Marxism（Games and Culture 12(4):381–400, 2017, 引17）、Game Ego 专著（Lapland UP 2008, 引30）、「Computer Games as Playground and Stage」（DiGRA 2006, 引21）、「Everyone is not a gamer」（Springer 2020, 引9）、Inclusive audio interface（Audio Mostly 2014, 引23）、儿童防诱饵游戏（DiGRA 2019, 引11）、Mixed media（M&C 9(1) 2021）。
- **his.se 页面直采限制**：英文员工页/研究组页为 JS 渲染，WebFetch 仅得课程模块——现职/头衔以**瑞典文页搜索快照 + Scholar 署名**为准（已记入档案 stamps ◇ 注）；DAL21 keynote 由 play.his.se 媒体页 ✔。
- **同名消歧**：Lund 大学哲学家 Ulf Wilhelmsson（伦理学，philo.org 在列）与本档主体**非同一人**——已写入 `risk` 与 `open_questions`，检索以 Scholar profile 为界。

## 三、判断（闸口口径）

- **Wilhelmsson 过闸建档**：玩现象学（Game Ego）+ 玩理论 canon 重读（Caillois×Marxism）+ 遗产/包容/儿童的设计伦理落点——与 v10 所立 `play` 轴谱系（Huizinga/Caillois）及 `herit` 轴双咬合；产业腹地（舍夫德）内的人文正题守人，与 Rusch（乌普萨拉）构成「瑞典人文游戏研究两翼」。产出量中等（h-index 10），故「卓越」判据落在**脉络独特性**而非体量（◐，已注明）。
- **Engström 保留 ◇ 线索不入档**：其正题（游戏研发如何成立研究/严肃游戏设计知识）是**研发方法论与产业向**——与本库「玩×人文」轴契合度低；依「名气大不够格者不进」的同款纪律（v8 Bogost 先例），只入 dialogue_map 作可见线索。
- **Backlund 只作 circle 节点**：教育游戏效果研究（2008 起）+ 瑞典游戏研究委员会 Chair——网络价值大于对话价值，暂不单列。
- **总判定**：舍夫德值得考虑的是**一个人加一张网**（Wilhelmsson + Game Philosophy Network/DiGRA 圈），不是一个学科——其游戏学科主体（CS/serious games/产业）不在本库人文议程内。

## 四、落子清单

1. 建档 `../scholars/wilhelmsson-ulf.md`（22 维全 schema·不可证四条 ◇：系主任现职/Game Philosophy Network 角色/2022–2026 新篇全目/his.se 直采限制）
2. `indexes/dialogue_map.md`：Wilhelmsson 行（v14 新档）+ Engström ◇ 线索行 + 表尾 v14 段
3. `mvp/MVP-004-homo-ludens-roundtable.md`：增列**第五席候选（玩现象学·待确认）**，未确认前全文仍按四席口径
4. 场景作品登记：《游戏的人》圆桌 +《走廊的 AR 复原》各加 Wilhelmsson 进言位
5. `web/build_reseArch_X.py` SCHOLAR_AXES：`wilhelmsson-ulf: ["play","herit","xsci"]`（策展判断，不入 .md）

## 五、空手而归

- his.se 英文员工页与 Game Research Group 页正文（JS 渲染，直采只得课程名）——主任现职因此停在 ◇。
- Wilhelmsson 2024–2026 新篇：Scholar 目录本轮只取到 top-20，最新条目未整刷 ◇。
- Game Philosophy Network「关于」页成员名单：站体在、名录未直采到，其角色记 ◇。
