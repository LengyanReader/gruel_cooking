# Skills & Tools Catalog · Repo-wide 环境级技能与工具目录

How to *query, retrieve, and organise* the tools available in this environment. Grouped by the workflow each tool serves. Domain-only skills (e.g. reading & moment loops) live in the domain harnesses; this file covers the shared environment.

本环境可用"装备"的检索与组织说明。按工作流分组；域专属技能（如阅读/思潮流程）在对应板块的本域 harness 中。

---

## A · Researching & Fact-finding 检索与查证

| Tool / Skill 工具 | Use when 何时用 | Notes 备注 |
|---|---|---|
| **websearch** (built-in) | any live question about today / this week / this year | Set the year explicitly in queries (2026); `deep` mode for comprehensive sweeps, `fast` for quick facts |
| **webfetch** (built-in) | read a specific URL (paper, article, press) | Ask for `markdown`; prefer primary sources over press echo |
| **research** skill | "investigate X" — a background agent gathers findings into a Markdown file in the repo | Ideal for delegating leg-work on a trend before you write a brief |
| **academic-research-writer** skill | scholarly documents, literature reviews, IEEE-style references | Use when a dossier needs peer-reviewed grounding |
| **citation-verification** skill | before copying any citation into a dossier | Verifies references, surfaces fake/ghost citations |
| **find-skills** skill | "is there a skill for X?" — discover installable skills | First stop when you sense a gap in the harness |

**The source-confidence ritual 来源可信度仪式** — every claim entering any dossier or note must be marked `✓ verified / ◐ company-claim / ○ unconfirmed / ✗ disputed` (see `harness/principles.md` §I.2). **Non-negotiable in every domain.**

---

## B · Discovery 探索

| Tool / Skill | Use when | Notes |
|---|---|---|
| **grep / glob** (built-in) | locate files, find relations, audit completeness | `rg` for content, `glob` for files |
| **Task/general agent** | take a pile of materials and produce first-draft cards / briefs for review | AI drafting **must be marked** as AI-drafted (\(principles.md\) §I.6) |
| **skill-creator** | turn a repeated intake ritual into a reusable skill | Only after the ritual runs twice by hand |

---

## C · Site & Output Engineering 站点与产出

| Tool / Skill | Use when | Notes |
|---|---|---|
| **frontend-design** skill | designing a new page under `docs/` | Use the repo's design language (warm paper + LXGW WenKai + Inter, bilingual toggle) rather than templated defaults |
| **conda `hy_py312`** | any Python run | activation: `conda activate hy_py312` (or `conda run -n hy_py312 python …`) |
| **pwsh (bash tool)** | builds, git, checks | Prefer dedicated Read/Write/Edit/Grep tools over shell for file ops |
| **ai-image-generation / ai-video / ai-music / video-edit / image-to-video / remotion-best-practices** | media assets if needed | Not core to any domain; available wherever figures/audio are needed |

---

## D · Repo-native helpers 仓库自带

| Tool | Use when | Notes |
|---|---|---|
| `Language Stacking-Linguistic Weaving/web/build_learning.py` | reference for markdown/JSON → static pages generator | the "single source, generated pages" pattern — `--validate --db --check`, `git diff --exit-code` (see `learning-ci.yml`) |
| `living_heritage/scripts/` | reference patterns for seed+verify builds | `build_static_site.py`, `verify_seed.py`, `e2e_test.py` — the source→output sync pattern (see `ci.yml`) |
| `_final_ok.ps1` | pre-commit hygiene checklist | junk-file & secret scan habits (adapted into `harness/principles.md` §III.18) |

---

## E · Perspective skills 视角技能（思维顾问，可选）

Available: Karpathy, Musk, Feynman, Ilya, MrBeast, Munger, Naval, Paul Graham, Jobs, Sun Yuchen, Taleb, Trump, Zhang Yiming, Zhang Xuefeng. Each is a distilled thinking framework for **stress-testing** a thesis — Feynman to detect cargo-cult understanding, Taleb for tail-risk blind spots, Munger for incentive structures. Activate only when explicitly wanted; **never use a perspective skill as a fact source.** Per-domain analogues (if a domain nourishes one) are registered in that domain's harness.

---

## How to extend 如何拓展

1. A tool/skill serving **≥2 domains** → add a row here or in `harness/workflows.md`.
2. A workflow looping **only inside one domain** → write it in that domain's harness and register it in `harness/README.md`.
3. A brand-new skill gap → run **find-skills** first; create via **skill-creator** only after the ritual runs twice by hand.
个人或单域工具走本域 harness，不在本文件重复。