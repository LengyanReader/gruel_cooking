# Principles & Rules · Repo-wide 全仓库原则与规则

Rules for information use, knowledge design, and coding — distilled from this repository's operating principles (root `README.md`), the Language Stacking iron rules, and habits established in earlier working sessions. **Every piece of work in every domain obeys these.**

本仓库所有板块的工作都必须遵守的规则——由本仓库运行原则、语言叠织"铁律"及既往会话习惯蒸馏而来。

---

## I. Information use 信息使用

1. **Sources before narrative 来源先于叙述。** Every reading card, brief, brief and dossier carries provenance. An unverifiable link is worse than none. (README operating principle 7)
2. **Mark reliability 永远标注可信度。** `✓ verified / ◐ company-claim / ○ unconfirmed / ✗ disputed`. Nothing enters a dossier unlabelled. "Company claims are claims, not results" — write the confidence next to the claim.
3. **Primary before press 一手先于转述。** Prefer the origin; press echo only to broaden, never to establish.
4. **Trace the genealogy 追溯谱系。** Every idea has an origin — record the chain of influence, including who misquoted it. (README principle 4)
5. **Date everything 一切带日期。** Briefs carry dates; window files carry windows; a claim without a date is a fish without water.
6. **AI-drafted = labelled 草拟必标注。** Anything drafted by an AI is marked as such; formal corpus entries pass a human review before they become "established" in the notes. (Language Stacking rule 4)
7. **No secrets in notes 笔记不藏密。** Personal notes and data files never hold keys, tokens, `.env` contents, or third-party copyrighted images without attribution.

## II. Knowledge design 知识设计

8. **One card per entity 一实体一卡。** No duplicate representations of the same entity; a re-read / re-visit updates the card, it does not fork it.
9. **Small and explicit 小而显式。** Few categories, few relation types, one line per edge. Complexity is allowed to *emerge*, never required at build time. (README principle 6)
10. **Disagreement counts 不同意即进步。** Every note seeks at least one point of disagreement and at least one echo — the map must show the counter-narrative.
11. **Mind-opening beats completeness 开阔胜过完备。** Extensions may stay unfinished; their job is to make adjacency visible.
12. **Bilingual by default 双语默认。** Chinese and English are co-primary. Cards carry both where possible; the site toggles between them. Unused language notes are welcome but never expunge the other.

## III. Coding & repository 编码与仓库

13. **Single source → generated pages 单一来源。** Prose in Markdown, structured data in JSON, web pages generated — no hardcoding, no copy-paste duplication. (Language Stacking rule 1)
14. **Environment is `hy_py312`。** All Python runs use `conda activate hy_py312`.
15. **Source ↔ output sync 源出同步。** When a generator exists, the static mirror under `docs/` is *rebuilt and committed together*; CI enforces `git diff --exit-code`. (repo CI convention: `learning-ci.yml`, `ci.yml`)
16. **Verify with tests 以测为准。** Assertions over vibes: a seed/verify script or pytest accompanies any data pipeline.
17. **Simple observable first 从可感处起。** Approach from a concrete phenomenon or a concrete text — not from abstraction. (README principle 1)
18. **Commit hygiene 提交卫生。** Stage only intended files; scan staged diff for junk (`_tmp_*`, `.bak`) and secrets; never add `.env`.
19. **Ask before surprising actions 先问再做。** Commits, pushes, and PRs happen only when explicitly requested. (repo convention)

---

## Domain-specific extensions 本域延伸

Domain-only rules belong in the domain's own harness (see `README.md` registry), not here. Keep this file shared and stable.
域专属规则见各域自身 harness（见 `README.md` 注册表）；本文件保持共享与稳定。