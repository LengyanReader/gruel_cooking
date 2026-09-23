# Workflows 常设流程

Recurring loops with the exact commands. All Python runs happen in **`conda activate hy_py312`**.

## W1 · Reading intake 阅读录入

Trigger: 读完 / 放弃 / 计划一本书，或收集到一批读物。

1. Create the cards: `library/YYYY-slug.md`, `authors/<name>.md`, wire `categories/`.
2. Write the hot note in `readings/notes/<slug>.md` (quotes short, replies long, ≥1 echo).
3. Add edges to `relations/influences.md` / `book_graph.md` / `moment_ties.md` (one row each, with confidence).
4. Drop ≥1 lead into `extensions/leads.md` with tags (`anticipation / moment / cost`).
5. If the material came from a live topic, cross-file into `moment/` (below).

Checks 自检：every card has a one-line thesis; every finished book has ≥1 new lead.

## W2 · Completeness review of a reading list 书目供给的完备性核验

Trigger: user supplies a set of readings, asks 是否充分/深入/正确.

Procedure 流程:
1. **Retrieve 检索** — for each supplied reading, locate the actual work via websearch/webfetch (don't trust the label; find the edition, year, author, language).
2. **Verify 核验** — is the attribution correct? original language? publication year? (`citation-verification` skill if citations are involved)
3. **Map the field 摆布地图** — for the topic under review, note the *missing canonical corners*: the originators, the strongest current critics, the adjacent disciplines, the dissenting traditions. Answer: *which high-value works are absent?*
4. **Depth check 深度检查** — do the readings cover both sides of the axis (e.g. theory vs. application, West vs. non-West, mainstream vs. fringe)?
5. **Deliver 交付** — a short verdict: `sufficient / gaps / missing-corner` + a pruned "add these 3–5" shortlist, each with a one-line why, filed into `extensions/leads.md`.

## W3 · Develop the shape of the moment 思潮之形展开

Trigger: user provides materials for a time window (7d / 14d / 1m / 1y), or asks to extend existing material 在广度与深度上发展.

1. **Capture**: drop materials into `moment/briefs/YYYY-MM-DD-*.md` with provenance (source URLs) — *before* any reinterpretation.
2. **Verify inward 向内深度**: websearch/webfetch; mark `✓/◐/○/✗`; trace who said it first/loudest; find the older idea it mutates.
3. **Grow outward 向外广度**: contrasts (opposite camp), adjacencies (which fields get dragged in), geography (local vs. planetary), carriers (labs/presses/platforms).
4. **Synthesise**: write the window file `series/<window>.md`; keep long-lived themes in `themes/<theme>.md`; end each synthesis with 2–3 consequential questions.
5. **Wire back 回连**: promote leads into `readings/`, tag them `moment*`.

**R1（铁律）· 书单不入思潮之文**：思潮文章（`.md`/`.html`）只放**指针**（链接 + 一句定位），绝不内嵌书单清单或逐本展开。书单本体在独立页 + `readings/lists/README.md` 注册表（协议见 `docs/reading_lists_design.md`）。

Cadence: 7d sweep weekly; fortnight consolidation; monthly structure review; annual arc.

## W4 · Site build & sync 站点构建与同步

Phase 0 (now): the landing page `docs/reading_ia/index.html` is handcrafted and bilingual; edit it directly, keep it in sync with `Reading_IA/README.md`. The reading-list pages + archive mirror the registry `readings/lists/README.md`: `docs/reading_ia/read/<crop>-books.html` (one page per crop) + `read/index.html` (archive, newest first). New crop = registry row + new page + archive card + landing "Latest" + essay pointers, then validate all HTML (`check_html.py`). Protocol: `docs/reading_lists_design.md`.

Phase 1 (when cards accumulate): adopt the repo's iron rule — **single source → generated pages** (`web/build_reading.py` reading markdown/JSON, emitting `docs/reading_ia/`), then add a GitHub Actions check `git diff --exit-code -- docs/reading_ia/` exactly like `.github/workflows/learning-ci.yml`.

Preview locally 本地预览:
```powershell
conda activate hy_py312
python -m http.server 8080 --directory docs
# open http://localhost:8080/reading_ia/
```

## W5 · Hygiene before any commit 提交前卫生

Run the spirit of `_final_ok.ps1` (triggered the moment they ask to commit):
1. `git status --short` — only intended files staged.
2. Junk scan: no `_tmp_*`, `extract_classes*`, `.bak`, stray output files.
3. Secrets scan on staged diff: `BEGIN … PRIVATE KEY`, `ghp_…`, `AKIA…`, API keys.
4. `git diff --cached --name-only` review.
5. Never write secrets into notes or data files (`.env` stays out).