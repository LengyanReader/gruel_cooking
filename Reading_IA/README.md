# 阅读与智识 · Reading & IA

**Reading & IA — Ideas & Awareness | 智识与觉察**

> 读何以成智慧？一书一师，一条思路一条河。留阅读之痕，察时代之形。
>
> *How does reading become intelligence? Each book a teacher, each thread a river. Keep the traces of reading; read the shape of the moment.*

---

## Two Parts 两大板块

### Part 1 · Readings, Writers, Extensions 阅读 · 作者 · 延伸

A personal **knowledge management system** for reading. One card per book, one card per author, a living taxonomy of categories, explicit relations between them, reading notes, and a growing map of *extensions* — clues and inspirations that open the mind and lead to the next book.

阅读的个人知识管理系统。一书一卡，一人一卡，活的分类体系，显式的书目—作者—主题关系，阅读笔记，以及不断生长的「延伸地图」——那些打开心智、通向下一本书的线索与灵感。

**Directory 目录:**

| Path 路径 | Purpose 用途 |
|---|---|
| `readings/library/` | Book records 书目卡片 |
| `readings/authors/` | Author / writer records with life-timeline & knowledge graph 作者卡片（生平轨迹 + 知识图谱） |
| `readings/categories/` | Taxonomy & themes 分类与主题体系 |
| `readings/relations/` | Edges: author→book→category, influences, inspirations 关系网络 |
| `readings/notes/` | Reading notes, quotes, reflections 读书笔记与随想 |
| `readings/extensions/` | Reading clues, mind-opening leads 延伸线索与灵感地图 |
| `readings/lists/` | Reading-list registry — one dated, W2-verified crop per window 书单登记注册（一窗一份，带日期、经核验） |

**Book lists 书单** · a reading list is the *material layer*; an essay is the *synthesis*. Every crop lives on its own page and the archive, never inside an essay (R1 — essays only carry pointers). Registry: `readings/lists/README.md` · protocol & design: `docs/reading_lists_design.md`.

书单是「素材层」，思潮之文是「合成层」。每份书单一批一页，档案在 `docs/reading_ia/read/`（索引 `index.html`）；思潮文章只放指针（R1），不内嵌清单。

### Part 2 · The Shape of the Moment 当下的形状 · 思潮之形

Tracking **cultural movements and thought trends** across time windows — 7 days, 14 days, 1 month, 1 year — that develop out of provided material in breadth and depth. Dated research briefs, rolling window syntheses, and persistent dossiers on themes that outlive any single week.

追踪一段时间内的文化运动与思潮演化——7 天、14 天、1 个月、1 年——从你提供的材料出发，向广度与深度发展。含日期的研究简报、滚动时间窗综述，以及跨越单周的持久主题档案。

**Directory 目录:**

| Path 路径 | Purpose 用途 |
|---|---|
| `moment/briefs/` | Dated research briefs on breaking topics 带日期的研究简报 |
| `moment/series/` | Rolling window syntheses (7d / 14d / 1m / 1y) 滚动窗口综述 |
| `moment/themes/` | Persistent movement & trend dossiers 持久思潮档案 |

### Support 支撑

| Path 路径 | Purpose 用途 |
|---|---|
| `docs/workflows.md` | Domain workflows 本域工作流（W1–W4 + 本域技能） |
| `web/` | Static site build plan & templates 静态站点构建计划 |

> Repo-wide rules, skills & tools live in the root **`../harness/`** (`principles.md`, `skills.md`, `workflows.md`) — shared across all pillars. 跨域规则、技能与工具在根目录 `../harness/`（全仓库共享）。

---

## Site Output 站点产出

The mirror lives at `docs/reading_ia/` and is linked from the site home `docs/index.html`:
- landing + domain pages `docs/reading_ia/index.html`
- book-list pages & archive `docs/reading_ia/read/` (one page per crop + `index.html`)
- authors knowledge graph `docs/reading_ia/authors/index.html` (nodes from `readings/authors/` + edges from `relations/influences.md`)

镜像站位于 `docs/reading_ia/`，并由站点首页 `docs/index.html` 链接进入；书单页与档案在 `docs/reading_ia/read/`，作者知识图谱（节点+朋友圈+流派+影响链）在 `docs/reading_ia/authors/`。

## Working Env 环境

- Python environment: `conda activate hy_py312`
- Languages: Chinese and English (bilingual by default)
- See `../harness/principles.md` for the repo-wide rules, and `docs/workflows.md` for this domain's workflows.