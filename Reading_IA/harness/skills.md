# Skills & Tools Catalog 技能与工具目录

How to *query, retrieve, and organise* the harness available in this environment. Grouped by the workflow each tool serves.

本环境可用"装备"的检索与组织说明。按工作流分组。

---

## A · Reseaching & Fact-finding 检索与查证

| Tool / Skill 工具 | Use when 何时用 | Notes 备注 |
|---|---|---|
| **websearch** (built-in) | any live question about today / this week / this year | Set the year explicitly in queries (2026); `deep` mode for comprehensive sweeps, `fast` for quick facts |
| **webfetch** (built-in) | read a specific URL (paper, article, press) | Ask for `markdown`; prefer primary sources over press echo |
| **research** skill | "investigate X" — a background agent gathers findings into a Markdown file in the repo | Ideal for delegating leg-work on a trend before you write a brief |
| **academic-research-writer** skill | scholarly documents, literature reviews, IEEE-style references | Use when a theme dossier needs peer-reviewed grounding |
| **citation-verification** skill | before copying any citation into `readings/` or `moment/` | Verifies references, surfaces fake/ghost citations |
| **find-skills** skill | "is there a skill for X?" — discover installable skills | First stop when you sense a gap in the harness |

### The source-confidence ritual 来源可信度仪式
Every claim entering `moment/` or a reading note must be marked: `✓ verified / ◐ company-claim / ○ unconfirmed / ✗ disputed` (see `moment/README.md`). This mirrors the discipline used in `direction_refs/mostik-latent-bridge-brief.md` and is **non-negotiable** in this domain.

---

## B · Reading & Knowledge Management 阅读与知识管理

| Tool | Use when | Notes |
|---|---|---|
| **grep / glob** (built-in) | locate cards, find relations, audit completeness | `rg` for content, `glob` for files |
| **Task/general agent** | take a pile of your materials and produce first-draft cards / briefs for your review | AI drafting **must be marked** as AI-drafted (below) |
| **skill-creator** | if you want to turn a repeated intake ritual into a reusable skill | Only after the ritual runs twice by hand |

---

## C · Shape of the Moment 思潮之形

| Tool / Skill | Use when | Notes |
|---|---|---|
| **websearch + webfetch** | daily/weekly signal sweep | Build a 7d sweep from 3+ independent outlets per claim |
| **research** skill | delegate "map this controversy in depth" | Returns a dated Markdown brief → fits straight into `moment/briefs/` |
| **perspective skills** (see below) | stress-test a thesis against a great mind | Optional thought-augmentation, not fact-finding |

### Perspective skills 视角技能（思维顾问，可选）
Available: Karpathy, Musk, Feynman, Ilya, MrBeast, Munger, Naval, Paul Graham, Jobs, Sun Yuchen, Taleb, Trump, Zhang Yiming, Zhang Xuefeng. Each is a distilled thinking framework for **stress-testing** a thesis — for example: Feynman to detect cargo-cult understanding, Taleb for tail-risk blind spots, Munger for incentive structures. Activate only when explicitly wanted; never use a perspective skill as a fact source.

---

## D · Site & Output Engineering 站点与产出

| Tool / Skill | Use when | Notes |
|---|---|---|
| **frontend-design** skill | designing a new page for `docs/reading_ia/` | Use the repo's design language (warm paper + LXGW WenKai + Inter, bilingual toggle) rather than templated defaults |
| **conda `hy_py312`** | any Python run | activation: `conda activate hy_py312` (or `conda run -n hy_py312 python …`) |
| **pwsh (bash tool)** | builds, git, checks | Prefer dedicated Read/Write/Edit/Grep tools over shell for file ops |
| **ai-image-generation / ai-video / ai-music / video-edit / image-to-video / remotion-best-practices** | media assets if needed | Not core to this domain; available if the site ever needs figures/audio |

---

## E · Repo-native helpers 仓库自带

| Tool | Use when | Notes |
|---|---|---|
| `living_heritage/scripts/` | reference patterns for seed+verify builds | `build_static_site.py`, `verify_seed.py` — the source→output sync pattern |
| `Language Stacking…/web/build_learning.py` | reference for markdown/JSON → static pages generator | the "single source, generated pages" pattern we will follow in phase 1 (`web/README.md`) |
| `._final_ok.ps1` | pre-commit hygiene checklist | junk-file & secret scan habits (adapted into `principles.md`) |