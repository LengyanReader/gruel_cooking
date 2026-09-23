# Part 1 · Readings 阅读知识管理

> **目的**：把「读过什么、谁写的、跟什么有关、通向哪里」全部显性化——既是笔记工具，也是可以回溯、检索、继续生长的知识网。
> Aims: make "what I read, who wrote it, what it relates to, where it leads" explicit — a note-taking tool that is also a retrievable, growing knowledge web.

---

## Concept 总体设计

The system is **card-based** (one file per entity) plus **explicit edges** (relations). Cards are plain Markdown, filed under one of five folders; relations live in `relations/` as a graph you can query by hand or with scripts.

系统采用**卡片制**（一实体一文件）+ **显式关系**（边）。卡片是纯 Markdown，分五类归档；关系存于 `relations/`，以图的形式可手工或用脚本查询。

### Layers 层次

```
library/  authors/  categories/        ← entities 实体 (cards)
          relations/                   ← edges 关系 (the graph)
notes/    extensions/                  ← activity 活动 (reading traces + leads)
```

**One rule of thumb 判据**：实体卡片回答「是什么」，关系文件回答「怎么连」，笔记回答「我读到了什么、想到了什么」，延伸回答「下一步读什么」。

---

## Card schemas 卡片格式

### Book card 书目卡片 — `library/<slug>.md`

Named by slug (`year-firstword`, e.g. `2026-herbert-platonic`). Front-matter-free; a check-sheet YAML-like block is fine. Keep the fields below.

| Field 字段 | Required | Note |
|---|---|---|
| `title` 书名 | ✓ | Original + Chinese title 原文名与中文名 |
| `author` 作者 | ✓ | Link to authors card 指向作者卡片 |
| `year` 出版年 | ✓ | Original publication year 原版年份 |
| `edition` 版本 | | Read edition, translator 所读版本与译者 |
| `lang_orig` 原语言 | | e.g. `en`, `de`, `zh`, `ja` |
| `category` 分类 | ✓ | One or more links to categories 指向分类 |
| `core_claims` 核心主张 | | 2–5 kernels in your own words 用自己的话写 2–5 条内核 |
| `method` 方法与体裁 | | treatise / essay / field note / fiction… 文体与方法 |
| `status` 状态 | | `unread / reading / done / re-reading / dnf` |
| `relation_stub` 关系线索 | | short hints of edges 关系的线索速写 |

### Author card 作者卡片 — `authors/<slug>.md`

| Field 字段 | Note |
|---|---|
| `name` 姓名 | Original + Chinese 原名与中文名 |
| `era` 时代 | birth–death / active period 生卒或活跃期 |
| `domain` 领域 | school, discipline 学派与学科 |
| `body_of_work` 主要作品 | linked titles 主要作品（链接书目） |
| `lineage` 师承与影响 | teachers, students, inheritors, critics 师承、后学、批评者 |
| `stance` 立场 | core commitments 核心立场与一贯关切 |
| `read_status` 阅读进度 | what you have actually read 实际读过什么 |
| `why_now` 为何此刻 | why this writer matters for the current moment 为何此刻重要 |

### Category card 分类 — `categories/<slug>.md`

A category = a persistent theme cluster (not a rigid library taxonomy). See `categories/README.md` for the taxonomy design.

分类 = 可持续的主题簇（而非僵硬的图书馆分类法）。设计见 `categories/README.md`。

---

## Note files 笔记 — `notes/`

- `notes/<book-slug>.md` — per-book reading note: highlights, margins, questions, disagreements, echoes (什么使我眼前一亮、什么我不同意、唤起了哪些旧读).
- Notes **never replace** the card; the card summarises, the note remembers the live reading process.

---

## Extensions 延伸 — `extensions/`

- `extensions/leads.md` — the open field: authors/books/questions you want to chase next, each with a one-line reason (why it might matter).
- `extensions/README.md` — method for scoring and pruning leads (cluster them; the moment is a pruning signal).

---

## Intake loop 录入流程

1. **Card first** 先建卡 — create book/author card while reading or right after DNF.
2. **Note when hot** 趁热记 — capture the live reaction in `notes/`.
3. **Wire edges** 连关系 — add rows to `relations/` graph files.
4. **Push extensions** 补延伸 — record at least one new lead per finished book.
5. **Prune by the moment** 借时事修剪 — use `moment/` signals to decide which leads to promote to the reading queue.