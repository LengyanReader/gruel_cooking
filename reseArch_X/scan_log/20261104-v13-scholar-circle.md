# 20261104 · v13 学者档案介绍增维续——「学术圈子」字段（第九维）· 游戏线 9 档补全

**触发**：用户指令「各个学者的圈子也需要添加」。本轮续 v12 schema 扩展，**追加第九个维度字段** `circle`，仍属 schema 变更（方法学，依 README §六记档），不新入库学者。

## 一、字段定义

| 字段 | 义 | 落点 |
|---|---|---|
| `circle` | 学术圈子·人际网络节点：机构（现任+历任）、学会/会议网络、研究中心/实验室、关键合作者（**本库外学者**）、思想脉络/学派 | 渲染置于 `peer_bridges` 之前，区别于「本库连线」；紫色调 `.dim.circle` |

**与 `peer_bridges` 的分工**：`peer_bridges` 专指本库已建档学者之间的对话连线；`circle` 涵盖其**外围网络**——未建档合作者、学术共同体、学派传统、建制平台。两者互补，共同呈现「此人嵌在哪个网里」。

## 二、取证纪律

全部 9 档的 `circle` 内容**只从各档已 ✔ 字段（`affiliation`/`current_work`/`key_works`/`entry`/`mvp`/`trends_analysis`/`why_open`）中重抽**，不新增任何事实主张，不做外网检索。逐条来源均可在对应档 yaml 字段内找到原文。

已知例外：rusch 档 `circle` 中 **Kjell Hedgard Hugaas** 的名字来源——v11 台账（`20261104-v11-sweden-deep-dive.md`）中 WebFetch uu.se TPI 页直接核实，已写入 rusch `peer_bridges`（v11 建档时即填），故本轮 `circle` 条目属已核内容之再结构化。

## 三、9 档圈子节点摘要

| 学者 | 圈层节点（摘） |
|---|---|
| Sotamaa | 坦佩雷 Game Research Lab / CoE · HEVGA · DiGRA · Jan Svelch · 芬兰—北欧游戏研究学派 |
| Juul | 丹麦皇家艺术学院 · 前 MIT/NYU/ITU · MIT Playful Thinking 书系 · Nordic Game · 独立开发者圈 · spillhistorie.no |
| Liestøl | 奥斯陆大学媒体系 · C2HO · Journal of Computer Archaeology · CAA 会议 · SARVI（旧 EU 项目 ◇） |
| Klein | SEI · IPCC AR5 WGII · climatestrategies.org · COP side-event · 瑞典气候严肃游戏圈（Cancun Game ◐） |
| Rusch | 乌普萨拉游戏设计系/Campus Gotland · TPI/Games & Society Lab · Phelps/Bowman/Westborg/Baird/Hugaas · DiGRA·FDG·Nordic Game·Knutepunkt·GDC·TEDx · 维也纳大学（博士）· DePaul（前机构） |
| Sicart | ITU Center for Digital Play · MIT Press · SAGE · DiGRA · IJGC · 游戏伦理/play as praxis 学派 |
| Gobet | LSE · 前利物浦 · H. A. Simon（卡内基梅隆导师）· Royal Institution · 亚美尼亚棋院 · IM · CHREST 学派 · chessprogramming |
| Boellstorff | UC Irvine · RAI Play & Games 系列 · Hazel Andrews/Kellynn Wee（RAI 组织者）· Princeton UP · UNESCO Courier · 虚拟世界民族志学派 |
| 张厚泉 | 上财外国语学院 · 日中关系学会 · 羽田正（东大座谈发起人·谱系开端）· 围棋·AI·人类跨界论坛 · 江南大学讲座 · 前东华大学 |

## 四、渲染

`template.html`：`circle` 走 `listDim` 助手（同 `key_works` 等 `.dim` 块），class=`.circle` 附独立紫色调 CSS（`rgba(107,82,155,.06)` 背景 + `#5C3D7A` 标签色）；中英双语「学术圈子」/「ACADEMIC CIRCLE」；注入位置：MVP 对钩之后、`peer_bridges` 胶囊组之前。

## 五、推广待办

- **剩余 45 档**推广时同步填 `circle`，按线分波，取证纪律照 v12/v13（不新增主张，只从已 ✔ 内容重抽）。
- Klein「瑞典气候严肃游戏圈」条目 ◐（Cancun Game 命名/现行版本待直证），推广时若启动触达须先补此证。
