# web — FastAPI Viewer (Web 展示层)

Renders the math_clarification entries as layered, language-selectable pages. The same Markdown files stay the source of truth; this layer crops the depth for any audience.

## Run it

```bash
conda activate ds_0708
cd math_clarification/web
uvicorn app:app --reload --port 18088
```

Then open:

- Home / 首页: `http://127.0.0.1:18088/`
- An entry: `http://127.0.0.1:18088/entry/famous_problems/erdos_unit_distance`

> Note: on this Windows environment only high ports (e.g. 18088) bind successfully.

## Query parameters

### Level (crop depth by audience)
`?level=L0` … `?level=L5` — keep only sections up to that level.

| Level | Audience | Content |
|-------|----------|---------|
| L0 | everyone | **The idea in a line** (一行想法) |
| L1 | general readers | **Intuition / 譬喻** |
| L2 | students | **Precise statement + Premises** (精确表述·前提) |
| L3 | specialists | **A little math + Directions** (解题方向) |
| L4 | researchers | **Machine-checked + What people get wrong** |
| L5 | deep readers | **Where it shows up + Sources** (参考文献) |

### Language
`?lang=en` English-only · `?lang=zh` Chinese-only · `?lang=dual` bilingual (default).

### Markdown source format
Entries use inline markers the parser reads:

```markdown
<!-- L1 -->        opens an L1 section
<!-- en -->        opens an English block
...content...
<!-- L1-end -->    closes the level (and resets to English)
```

Binary content blocks are wrapped with `<!-- zh -->` … `<!-- zh-end -->` (dual blocks omit the language marker).

## JSON API

`GET /api/entry/{category}/{slug}?level=L5&lang=dual` returns the sections as JSON for other tools.

## Extending

- Add an entry as one Markdown file in `basics/` or `famous_problems/`; it appears on the home page automatically.
- The level/language markers are optional: a plain Markdown file without markers still renders (as a single L0 English section).

## App structure

- `app.py` — FastAPI routes (`/`, `/entry/...`, `/api/entry/...`)
- `parser.py` — Markdown parsing, level cropping, language filtering
- `templates/` — `base.html`, `home.html`, `entry.html` (Jinja2)
- `static/style.css` — styling; KaTeX renders math via CDN
