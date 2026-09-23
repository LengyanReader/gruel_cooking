# web/ 站点构建

Where the `docs/reading_ia/` mirror comes from. Bilingual, consistent with the site design language (warm paper, LXGW WenKai + Inter, zh/en toggle).

`docs/reading_ia/` 镜像站的来源。双语，与站点设计语言一致（暖纸、LXGW WenKai + Inter、中英切换）。

## Current 当前

Generator is **live**: JSON data layer (single source) → `web/build_reading.py` → `docs/reading_ia/`.

生成器已运作：JSON 数据层（唯一源）→ `web/build_reading.py` → `docs/reading_ia/`。

- Data (single source 单一数据源): `web/data/site.json`（站点元信息/书单批次）、`web/data/books.json`（每书完整档案）、`web/data/authors.json`（作者档案）、`web/data/relations.json`（作者边，镜像 `readings/relations/influences.md`）。
- Generator 生成器: `web/build_reading.py` — reads JSON, emits bilingual pages with inline SVG diagrams (plot flow / character relations), lang-toggle CSS/JS (storage key `zhzz-reading-lang`), confidence marks ✓/◐/○/✗.
- Outputs 输出: 每书一页 `docs/reading_ia/read/books/<slug>.html`；本批书单 `docs/reading_ia/read/<crop>-books.html`；档案 `docs/reading_ia/read/index.html`；作者图谱 `docs/reading_ia/authors/index.html`。
- Landing page `docs/reading_ia/index.html` and moment `docs/reading_ia/moment/year-2026.html` are handcrafted (not yet driven by the generator); keep in sync with `Reading_IA/README.md` when structures change.

着陆页 `docs/reading_ia/index.html` 与 moment 页 `docs/reading_ia/moment/year-2026.html` 仍为手工静态页（不在生成器范围内）；结构变动时与 `Reading_IA/README.md` 保持同步。

## Build 构建

```
conda activate hy_py312
python Reading_IA/web/build_reading.py            # validate JSON then write docs/reading_ia/
python Reading_IA/web/build_reading.py --validate # JSON + data sanity only
```

## Rules 规则

- Single source (JSON) → generated pages; no hardcoding in HTML.
- Every fact carries a confidence mark; plot-level claims stay ◐/○ until the book is actually read.
- AI-drafted content is marked until human-reviewed.
- Run both `check_html.py <files>` and `check_links.py docs/reading_ia` after any change.
- Nothing is committed to git without explicit request.