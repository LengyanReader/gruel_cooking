# lists/ 书单登记注册 · Reading-list registry

A reading list (`书单`) is a dated, W2-verified crop of books bound to one reading window. The registry below is the **single source of truth** for which crops exist; the web mirror lives in `docs/reading_ia/read/` (one page per crop + `index.html` archive). Design & update protocol: `docs/reading_lists_design.md`.

书单 = 一个带日期、经 W2 核验的读物批次，绑在一个阅读窗口上。本表是书单的**唯一注册表**；web 镜像在 `docs/reading_ia/read/`（每批一页 + 档案索引 `index.html`）。设计与更新协议见 `docs/reading_lists_design.md`。

**铁律 R1**：书单不入思潮之文——思潮文章只放指针（链接+一句定位），不内嵌清单。**R3**：页名定稿后不复用、不改名。

## Registry 登记（新批在上 / newest first）

| crop id | date | glyph | books（library 卡） | verdict | href | keel 下个窗口 |
|---|---|---|---|---|---|---|
| `2026-japan-culture` | 2026-11-06 | 读日本·回归东方 JAPAN CULTURE | 特辑八册：[[jp-fenshen-新日本论]] · [[jp-momie-摩灭之赋]] · [[jp-wabisabi-日本侘寂]] · [[jp-shikike-日本色气]] · [[jp-hokyu-异国放浪记]] · [[jp-fuseiyobutanda-浮世与病榻]] · [[jp-mososha-妄想者手记]] ＋ 第二圈源头/对手（详见页内 24 书） | `gaps`（特辑 8 册 + 源头原典/英译/论日本对手共 24 书；色气实收篇目、川端/荷风版目、Onishi 英译书目待核，见页内缺口） | `read/japan-culture-books.html` | 2026-12 冬至 Winter solstice |
| `2026-writing-canon` | 2026-09-27 | 学术写作正典 WRITING CANON | [[wcs-elements-of-style]] · [[wcs-sense-of-style]] · [[wcs-they-say-i-say]] · [[wcs-on-being-a-scientist]] | `gaps`（wr_ref 23 本正典，仅 4 本有授权原书可通读；19 本待读，见页内缺口） | `read/writing-canon-books.html` | 2026-12 冬至 Winter solstice |
| `2026-penguin-europe` | 2026-09-25 | 企鹅欧洲史 PENGUIN EUROPE | [[pe-volume1-birth-classical]] · [[pe-volume2-inheritance-rome]] · [[pe-volume3-high-middle-ages]] · [[pe-volume4-renaissance-europe]] · [[pe-volume5-christendom-destroyed]] · [[pe-volume6-pursuit-glory]] · [[pe-volume7-pursuit-power]] · [[pe-volume8-hell-and-back]] · [[pe-volume9-global-age]] | `sufficient`（Vol.4 待出版；全套覆盖 1700BC–2017AD） | `read/penguin-europe-books.html` | 2026-12 冬至 Winter solstice |
| `2026-autumn` | 2026-09-23 | 秋分 Autumn | [[library/2026-mandel-exit-party]] · [[library/2026-vargas-une-unique-lueur]] · [[library/2026-lemaitre-belles-promesses]] · [[library/2026-pelicot-joie-de-vivre]] · [[library/2026-manda-kanoke-made]] | `gaps`（缺 AI 反思轴等 5 项，见 `readings/review_2026-09-23.md`） | `read/2026-09-books.html`（= 规范页名） | 2026-12 冬至 Winter solstice |

## Crops 各批（每批在 `docs/reading_ia/read/<crop>-books.html` 一页）

- **2026-japan-culture · 读日本·回归东方**（2026-11-06）：主题批，围绕北京联合「日本文化特辑（第一辑）八册」向两端梳理。三圈 24 书：核心特辑 8 册 / 环绕源头原典·英译通道·文化自述·论日本对手·文豪侧翼 / 参照指针。每书卡带「核心主张 + 情绪基调 + 可信度 ✓/◐/○」；三条读轴（思想史：黄遵宪→戴季陶→菊与刀→分身；美学：物哀→幽玄→粹→侘寂→阴翳→摩灭；文学：徒然草→荷风→漱石→芥川→川端）。判定 `gaps`（色气实收篇目、川端/荷风版目、Onishi 英译书目待核）。本批不建 library/ W1 卡。
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