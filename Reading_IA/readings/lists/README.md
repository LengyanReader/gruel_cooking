# lists/ 书单登记注册 · Reading-list registry

A reading list (`书单`) is a dated, W2-verified crop of books bound to one reading window. The registry below is the **single source of truth** for which crops exist; the web mirror lives in `docs/reading_ia/read/` (one page per crop + `index.html` archive). Design & update protocol: `docs/reading_lists_design.md`.

书单 = 一个带日期、经 W2 核验的读物批次，绑在一个阅读窗口上。本表是书单的**唯一注册表**；web 镜像在 `docs/reading_ia/read/`（每批一页 + 档案索引 `index.html`）。设计与更新协议见 `docs/reading_lists_design.md`。

**铁律 R1**：书单不入思潮之文——思潮文章只放指针（链接+一句定位），不内嵌清单。**R3**：页名定稿后不复用、不改名。

## Registry 登记（新批在上 / newest first）

| crop id | date | glyph | books（library 卡） | verdict | href | keel 下个窗口 |
|---|---|---|---|---|---|---|
| `2026-games-play-culture` | 2026-11-10 | 游戏·技艺·文化系统 PLAY & CULTURE | 四圈二十书（Moretti 四书 + Jockers/Underwood；Rusch + Salen & Zimmerman/Bogost/Juul；Parasecoli 四书 + Mintz/Appadurai；Gobet 三书 + de Groot）＋ 附录五组 | `gaps`（20 部均补齐概念/接受/局限/意图/长评；Rusch/Jockers/Underwood/Mintz/Appadurai/de Groot 的 ISBN/页数待核；多数未通读） | `read/games-play-culture-books.html` | 2026-12 冬至 Winter solstice |
| `2026-go-culture` | 2026-11-08 | 围弈·观心与棋道 GO CULTURE | 核心书架 15 部（Cobb 三书 · 何云波四书 · 吴清源 · Shotwell 二书 · Fairbairn–Hall · Moskowitz · 棋经十三篇 · 忘忧清乐集 · 玄玄棋经）＋ 附录五组收其余提及文献 | `gaps`（Cobb《佛教哲学与围棋》出版信息待核；何云波四书版次/ISBN 待核；玄玄棋经编纂者待核；Go Nation 正文未读；实践建议不入正文） | `read/go-culture-books.html` | 2026-12 冬至 Winter solstice |
| `2026-japan-culture` | 2026-11-07 | 读日本·回归东方 JAPAN CULTURE | 特辑八册：[[jp-fenshen]] · [[jp-iki-kouzou]] · [[jp-masshitsu]] · [[jp-wabisabi]] · [[jp-shikike]] · [[jp-furoki]] · [[jp-usei]] · [[jp-mososhu]] ＋ 第二圈 16 书（源头原典 · 英译通道 · 文化自述 · 论日本对手 · 文豪侧翼；共 24 单书档案 `read/books/jp-*.html`） | `gaps`（特辑 8 册 + 源头原典/英译/论日本对手共 24 书；川端版目、荷风篇目对应、Onishi 英译书目待核，色气 Kuki 章节重编已记 ◐，见页内缺口） | `read/japan-culture-books.html` | 2026-12 冬至 Winter solstice |
| `2026-writing-canon` | 2026-09-27 | 学术写作正典 WRITING CANON | [[wcs-elements-of-style]] · [[wcs-sense-of-style]] · [[wcs-they-say-i-say]] · [[wcs-on-being-a-scientist]] | `gaps`（wr_ref 23 本正典，仅 4 本有授权原书可通读；19 本待读，见页内缺口） | `read/writing-canon-books.html` | 2026-12 冬至 Winter solstice |
| `2026-penguin-europe` | 2026-09-25 | 企鹅欧洲史 PENGUIN EUROPE | [[pe-volume1-birth-classical]] · [[pe-volume2-inheritance-rome]] · [[pe-volume3-high-middle-ages]] · [[pe-volume4-renaissance-europe]] · [[pe-volume5-christendom-destroyed]] · [[pe-volume6-pursuit-glory]] · [[pe-volume7-pursuit-power]] · [[pe-volume8-hell-and-back]] · [[pe-volume9-global-age]] | `sufficient`（Vol.4 待出版；全套覆盖 1700BC–2017AD） | `read/penguin-europe-books.html` | 2026-12 冬至 Winter solstice |
| `2026-autumn` | 2026-09-23 | 秋分 Autumn | [[library/2026-mandel-exit-party]] · [[library/2026-vargas-une-unique-lueur]] · [[library/2026-lemaitre-belles-promesses]] · [[library/2026-pelicot-joie-de-vivre]] · [[library/2026-manda-kanoke-made]] | `gaps`（缺 AI 反思轴等 5 项，见 `readings/review_2026-09-23.md`） | `read/2026-09-books.html`（= 规范页名） | 2026-12 冬至 Winter solstice |

## Crops 各批（每批在 `docs/reading_ia/read/<crop>-books.html` 一页）

- **2026-games-play-culture · 游戏、技艺与文化系统**（2026-11-10）：主题批，四圈二十书：尺度（Moretti 四书 + Jockers/Underwood）、意义（Rusch + Salen & Zimmerman/Bogost/Juul）、身份（Parasecoli 四书 + Mintz/Appadurai）、专长（Gobet 三书 + de Groot）。四条读轴（甲 尺度、乙 意义、丙 身份、丁 专长）＋一条阅读路径（入门/深入/贯通）。核心书目事实经出版社/作者页核对；未见全文者标 ◐/○。本轮补齐 4 部旗舰（Moretti《Distant Reading》、Rusch《Making Deep Games》、Parasecoli《Gastronativism》、Gobet《The Psychology of Chess》）的概念/接受/局限/意图/长评；其余 16 部为基线档案，待下一批加深。
- **2026-go-culture · 围棋：观心、棋道与思想传统**（2026-11-08）：主题批，四圈十五书：观心（Cobb 三书）／中国思想史（何云波四书）／棋手自述与跨文化（吴清源、Shotwell 二书、Fairbairn–Hall、Moskowitz）／原典（《棋经十三篇》《忘忧清乐集》《玄玄棋经》）。三条读轴（甲 观心：Cobb→吴清源；乙 中国思想：何云波→棋经；丙 原典谱系：棋经→忘忧→玄玄）＋一条阅读路径（入门 3／深入 3／贯通 3）＋六条外部指针。核心书目事实经出版社/馆藏/书评核对：Cobb 三书（Sensei's Library）、The Book of Go（Sterling 2000，注意与部分 2002 零售页的出入）、The Go Companion（BritGo BGJ 148，ISBN 1-932001-43-3）、Go! More Than a Game（Google Books，Tuttle 2011）、吴清源《中的精神》（新浪体育节选：2001 连载/2003 中译/2010 中信）、《围棋文献集成（8）》（浙江古籍 2017-10，收《忘忧清乐集》等）。未见全文者一律 ◐/○；原清单标为待核的篇名不升级。附录五组收拢其余提及文献（Cobb 论文/专栏/小册子；何云波其他著作；Shotwell/Bozulich 与文献集成其他册；古代棋论/棋谱；未核论文、介绍文章与儒家原典）。判定 `gaps`。本批不建 library/ W1 卡（以 dossier HTML 页承担单书深度，md 卡待通读后回填）。
- **2026-japan-culture · 读日本·回归东方**（2026-11-07）：主题批，围绕北京联合「日本文化特辑（第一辑）八册」向两端梳理。两圈 24 书：核心特辑 8 册 / 源头原典·英译通道·文化自述·论日本对手·文豪侧翼 16 册；另设四个外部指针（日语模块 / 作者图谱 / 2026 秋分 / 企鹅欧洲）。每书卡带「核心主张 + 情绪基调 + 可信度 ✓/◐/○」；三条读轴（甲 思想史：黄遵宪→戴季陶→菊与刀→加藤→分身；乙 美学：物哀→幽玄→粹→侘寂→阴翳→摩灭；丙 文学：徒然草→荷风→漱石→芥川→川端）；一条阅读路径（入门 3 / 深入 4 / 贯通 7）。**深度已接入**：每书一张 `read/books/jp-*.html` 档案页（共 24，含来源说明 + 原文获取 + 核心论题 + 评价与合成 + 相关定位 + 核对账本 + 未核栏）；24 页均有摘录栏，公版文本用逐字原文，在版权文本用「论旨概述 · 非逐字原文」并标 ◐。**特辑八册本轮扩为全维度档案**：章节结构（分辑篇目表）＋ 关键概念（原语·释义·出处·conf）＋ 方法与材料 ＋ 接受史四层（当时/后世/影响/争议，逐条附出处）＋ 局限与争议（4 条）＋ **作者所欲言**（意图推断五段式：可反驳的推断 → 五条理由 → 7 条分类证据表〔文本/版本/生平/自述/接受/研究，逐条附出处与把握〕→ 最强反读 → 推断的边界；每册中文约 1300 字、英文约 700 词，推断本身一律标 ◐）＋ 3000–4500 字中文长评 ＋ 350–500 词英文 critical abstract（独立成篇，不逐句对译）＋ 逐章读法卡；八册均如实标注 `read_status`「未逐页通读（◐）」。读法图（rings/axes/reading_order/pointers）存于 `web/data/site.json`，由生成器渲染。术语架上共 9 条日本美学条目（物哀/幽玄/侘寂/粹/摩灭/阴翳/一期一会/杂种文化/则天去私）；作者架接入 18 位（含漱石/芥川/川端/谷崎/荷风/冈仓/九鬼/大西/本尼迪克特/加藤/戴季陶/黄遵宪/李永晶/四方田/阿部）。判定 `gaps`（川端版目、荷风篇目对应、Onishi 英译书目待核；色气 2019 版删去藤本箕山译文、Kuki 章节为中译重编，已记 ◐）。本批不建 library/ W1 卡（以 dossier HTML 页承担单书深度，md 卡留待通读后回填）。
- **2026-writing-canon · 学术写作正典**（2026-09-27）：源自 `docs/wr_ref.md` 的五层 23 本正典。本轮只发布能合法取得原书并实际通读的 4 种（Elements of Style / Sense of Style / They Say·I Say / On Being a Scientist）；其余 19 本本地无原书、无授权渠道，标为待读。读点 = 清晰·认知·对话·诚信四条根。
- **2026-penguin-europe · 企鹅欧洲史**（2026-09-25）：英国学术通史×9（全英文原版）。读点 = 三千年欧洲通读；判定 `sufficient`（Vol.4 Grafton 尚未出版，实际可读八卷）。来源 `C:\Docs_Here\newReading\企鹅欧洲`。
- **2026-autumn · 秋分书单**（2026-09-23）：美国×1、法国×3、日本×1。读点 = 每书核心主张 + 为何读；判定 `gaps`。来源 `docs/read_moment_list/eg_20260923.md`；过程 W2。
- *下一批去往*：2026-12 冬至书单（seasonal crop），届时按协议 §5 场景 B 执行。

## Structure 单批页结构

```markdown
# <crop> 书单
`YYYY-MM-DD` · glyph · N 书（原文+语种）· 判定 verdict
- provenance 来源说明（read_moment_list / W2）
- 每书：书名 · 作者 · 版本语言 · 核心主张(2–5) · 为何读 · 来源可信度 ✓/◐/○/✗
- verdict 判定 + 补缺线索（进 leads.md）
- keel 下个窗口（如「2026-12 冬至」）
```