# lists/ 书单登记注册 · Reading-list registry

A reading list (`书单`) is a dated, W2-verified crop of books bound to one reading window. The registry below is the **single source of truth** for which crops exist; the web mirror lives in `docs/reading_ia/read/` (one page per crop + `index.html` archive). Design & update protocol: `docs/reading_lists_design.md`.

书单 = 一个带日期、经 W2 核验的读物批次，绑在一个阅读窗口上。本表是书单的**唯一注册表**；web 镜像在 `docs/reading_ia/read/`（每批一页 + 档案索引 `index.html`）。设计与更新协议见 `docs/reading_lists_design.md`。

**铁律 R1**：书单不入思潮之文——思潮文章只放指针（链接+一句定位），不内嵌清单。**R3**：页名定稿后不复用、不改名。

## Registry 登记（新批在上 / newest first）

| crop id | date | glyph | books（library 卡） | verdict | href | keel 下个窗口 |
|---|---|---|---|---|---|---|
| `2026-autumn` | 2026-09-23 | 秋分 Autumn | [[library/2026-mandel-exit-party]] · [[library/2026-vargas-une-unique-lueur]] · [[library/2026-lemaitre-belles-promesses]] · [[library/2026-pelicot-joie-de-vivre]] · [[library/2026-manda-kanoke-made]] | `gaps`（缺 AI 反思轴等 5 项，见 `readings/review_2026-09-23.md`） | `read/2026-09-books.html`（= 规范页名） | 2026-12 冬至 Winter solstice |

## Crops 各批（每批在 `docs/reading_ia/read/<crop>-books.html` 一页）

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