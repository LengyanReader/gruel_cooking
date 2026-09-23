# Reading & IA · Domain Harness 本域工作流

Domain-specific workflows & skills for **Reading & IA**. Repo-wide rules, skills and env live in the root **`../harness/`** (`principles.md`, `skills.md`, `workflows.md`). This file holds only what is Reading-IA-specific; it is registered in `../harness/README.md`.

仅收本域专属流程与技能；跨域规则在根目录 `../harness/`。

---

## Skills & Tools · domain-specific 本域专属技能

### B · Reading & Knowledge Management 阅读与知识管理

| Tool | Use when | Notes |
|---|---|---|
| **grep / glob** (built-in) | locate cards, find relations, audit completeness | `rg` for content, `glob` for files |
| **Task/general agent** | take a pile of materials and produce first-draft cards / briefs for review | AI drafting **must be marked** as AI-drafted (`../harness/principles.md` §I.6) |
| **skill-creator** | turn a repeated intake ritual into a reusable skill | Only after the ritual runs twice by hand |

### C · Shape of the Moment 思潮之形

| Tool / Skill | Use when | Notes |
|---|---|---|
| **websearch + webfetch** | daily/weekly signal sweep | Build a 7d sweep from 3+ independent outlets per claim |
| **research** skill | delegate "map this controversy in depth" | Returns a dated Markdown brief → fits straight into `moment/briefs/` |
| **perspective skills** (see `../harness/skills.md` E) | stress-test a thesis against a great mind | Optional thought-augmentation, never a fact source |

---

## Workflows 常设流程

### W1 · Reading intake 阅读录入

Trigger: 读完 / 放弃 / 计划一本书，或收集到一批读物。

1. Create the cards: `library/YYYY-slug.md`, `authors/<name>.md`, wire `categories/`.
2. Write the hot note in `readings/notes/<slug>.md` (quotes short, replies long, ≥1 echo).
3. Add edges to `relations/influences.md` / `book_graph.md` / `moment_ties.md` (one row each, with confidence).
4. Drop ≥1 lead into `extensions/leads.md` with tags (`anticipation / moment / cost`).
5. If the material came from a live topic, cross-file into `moment/` (below).

Checks 自检: every card has a one-line thesis; every finished book has ≥1 new lead.

### W2 · Completeness review of a reading list 书目供给的完备性核验

Trigger: user supplies a set of readings, asks 是否充分/深入/正确.

Procedure 流程:
1. **Retrieve 检索** — for each supplied reading, locate the actual work via websearch/webfetch (don't trust the label; find the edition, year, author, language).
2. **Verify 核验** — is the attribution correct? original language? publication year? (`citation-verification` skill if citations are involved)
3. **Map the field 摆布地图** — for the topic under review, note the *missing canonical corners*: the originators, the strongest current critics, the adjacent disciplines, the dissenting traditions. Answer: *which high-value works are absent?*
4. **Depth check 深度检查** — do the readings cover both sides of the axis (e.g. theory vs. application, West vs. non-West, mainstream vs. fringe)?
5. **Deliver 交付** — a short verdict: `sufficient / gaps / missing-corner` + a pruned "add these 3–5" shortlist, each with a one-line why, filed into `extensions/leads.md`.

### W3 · Develop the shape of the moment 思潮之形展开

Trigger: user provides materials for a time window (7d / 14d / 1m / 1y), or asks to extend existing material 在广度与深度上发展.

1. **Capture**: drop materials into `moment/briefs/YYYY-MM-DD-*.md` with provenance (source URLs) — *before* any reinterpretation.
2. **Verify inward 向内深度**: websearch/webfetch; mark `✓/◐/○/✗`; trace who said it first/loudest; find the older idea it mutates.
3. **Grow outward 向外广度**: contrasts (opposite camp), adjacencies (which fields get dragged in), geography (local vs. planetary), carriers (labs/presses/platforms).
4. **Synthesise**: write the window file `moment/series/<window>.md`; keep long-lived themes in `moment/themes/<theme>.md`; end each synthesis with 2–3 consequential questions.
5. **Wire back 回连**: promote leads into `readings/`, tag them `moment*`.

**R1（铁律）· 书单不入思潮之文**: 思潮文章（`.md`/`.html`）只放**指针**（链接 + 一句定位），绝不内嵌书单清单或逐本展开。书单本体在独立页 + `readings/lists/README.md` 注册表（协议见 `docs/reading_lists_design.md`）。

Cadence: 7d sweep weekly; fortnight consolidation; monthly structure review; annual arc.

### W4 · Site build & sync 站点构建与同步

- The reading-list pages + archive mirror the registry `readings/lists/README.md`: `docs/reading_ia/read/<crop>-books.html` (one page per crop) + `read/index.html` (archive, newest first) + per-book / per-author pages + authors knowledge graph.
- **Phase 1 (live)**: adopt the repo's iron rule — **single source → generated pages** (`web/build_reading.py` reading JSON, emitting `docs/reading_ia/`); regenerate with `python Reading_IA/web/build_reading.py`.
- After any change, validate all HTML: `python <check_html.py> <files...>` and `python <check_links.py>` (per `../harness/workflows.md` W-GEN).
- New crop = registry row + new page + archive card + landing "Latest" + essay pointers. Protocol: `docs/reading_lists_design.md`.

Preview locally 本地预览:
```powershell
conda activate hy_py312
python -m http.server 8080 --directory docs
# open http://localhost:8080/reading_ia/
```

---

## Cross-references 关联

- Repo-wide principles: `../harness/principles.md`（§I 信息 · §II 知识设计 · §III 编码）。
- Repo-wide env & tools: `../harness/skills.md`, `../harness/workflows.md`.
- Reading-list protocol internals: `docs/reading_lists_design.md`（R1–R4 铁律）。

## Self-evolution 自我演化

本域 harness 的演化入口见根目录 **`../harness/evolution.md`（W-EVO）**；本域专属信号：
- 新书单形态/新命名约定 → 更新 W2/W4 与 `docs/reading_lists_design.md`。
- 卡片/关系/分类类型膨胀但无流程覆盖 → 在此补一条 W- 循环（或晋升共享规则）。
- 生成器 `build_reading.py` 数据层变动 → 同步 W4。
- 本域技能段与 `../harness/skills.md` 出现重复 → **晋升**到根，本域只留指针。