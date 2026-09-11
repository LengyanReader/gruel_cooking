"""
Seed SQLite from JSON files in data/seeds/.

This is the single seeding implementation (app layer). The scripts/ wrappers
and the --seed-if-empty bootstrap both delegate here.
Run directly: python -m app.seed
"""
import json
from pathlib import Path

from app.config import SEEDS_DIR
from app.db.sqlite import get_db, init_db
from app.services.graph import R_BELONGS_TO, R_STUDIES


def seed_bilingual_text(conn, en_data: dict, zh_data: dict):
    """Insert bilingual text rows from en/zh dicts."""
    all_keys = set(en_data.keys()) | set(zh_data.keys())
    for key in all_keys:
        en_val = en_data.get(key, "")
        zh_val = zh_data.get(key, "")
        conn.execute(
            """INSERT OR REPLACE INTO bilingual_text (key, en, zh)
               VALUES (?, ?, ?)""",
            (key, en_val, zh_val)
        )
    conn.commit()


def seed_pages(conn, en_data: list, zh_data: list):
    """Seed pages and their sections."""
    zh_lookup = {p["slug"]: p for p in zh_data}
    for page in en_data:
        slug = page["slug"]
        conn.execute(
            """INSERT OR REPLACE INTO pages (slug, title_key, template, nav_key, sort_order)
               VALUES (?, ?, ?, ?, ?)""",
            (slug, page["title_key"], page["template"], page.get("nav_key"), page.get("sort_order", 0))
        )
        page_id = conn.execute("SELECT id FROM pages WHERE slug = ?", (slug,)).fetchone()[0]

        conn.execute("DELETE FROM page_sections WHERE page_id = ?", (page_id,))
        for i, section in enumerate(page.get("sections", [])):
            conn.execute(
                """INSERT INTO page_sections (page_id, section_key, title_key, body_key, sort_order)
                   VALUES (?, ?, ?, ?, ?)""",
                (page_id, section["key"], section.get("title_key"), section.get("body_key"), i)
            )
    conn.commit()


def seed_corridors(conn, en_data: list):
    """Seed corridor records from corridors_structure.json."""
    for c in en_data:
        conn.execute(
            """INSERT OR REPLACE INTO corridors (slug, title_key, intro_key, detail_key, region, sort_order)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (c["slug"], c.get("title_key"), c.get("intro_key"), c.get("detail_key"),
             c.get("region"), c.get("sort_order", 0))
        )
    conn.commit()


def seed_scholars(conn, en_data: list, zh_data: list):
    """Seed scholar records."""
    for scholar in en_data:
        conn.execute(
            """INSERT OR REPLACE INTO scholars
               (name_key, bio_key, institution, specialization, website_url, corridor_slugs,
                works_json, traits_json)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                scholar["name_key"],
                scholar.get("bio_key"),
                scholar.get("institution"),
                scholar.get("specialization"),
                scholar.get("website_url"),
                json.dumps(scholar.get("corridor_slugs", []), ensure_ascii=False),
                json.dumps(scholar.get("works", []), ensure_ascii=False),
                json.dumps(scholar.get("traits", {}), ensure_ascii=False),
            )
        )
    conn.commit()


def seed_heritage_sites(conn, en_data: list, zh_data: list):
    """Seed heritage site records."""
    for site in en_data:
        conn.execute(
            """INSERT OR REPLACE INTO heritage_sites
               (name_key, description_key, corridor_slug, latitude, longitude,
                heritage_type, year_established, unesco_status)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                site["name_key"],
                site.get("description_key"),
                site["corridor_slug"],
                site.get("latitude"),
                site.get("longitude"),
                site.get("heritage_type"),
                site.get("year_established"),
                site.get("unesco_status"),
            )
        )
    conn.commit()


def seed_relations(conn):
    """Build the knowledge-graph edge table from normalized entity columns.

    site    -[belongs_to]-> corridor      (from heritage_sites.corridor_slug)
    scholar -[studies]---> corridor       (from scholars.corridor_slugs)
    """
    conn.execute("DELETE FROM relations")

    sites = conn.execute("SELECT id, corridor_slug FROM heritage_sites").fetchall()
    scol = {s["slug"]: s for s in conn.execute("SELECT slug, id FROM corridors").fetchall()}
    for site in sites:
        corr = scol.get(site["corridor_slug"])
        if corr:
            conn.execute(
                """INSERT INTO relations (source_type, source_id, relation, target_type, target_id)
                   VALUES ('site', ?, ?, 'corridor', ?)""",
                (site["id"], R_BELONGS_TO, corr["id"])
            )

    scholars = conn.execute("SELECT id, corridor_slugs FROM scholars").fetchall()
    for scholarly in scholars:
        slugs = json.loads(scholarly["corridor_slugs"] or "[]")
        for slug in slugs:
            corr = scol.get(slug)
            if corr:
                conn.execute(
                    """INSERT INTO relations (source_type, source_id, relation, target_type, target_id)
                       VALUES ('scholar', ?, ?, 'corridor', ?)""",
                    (scholarly["id"], R_STUDIES, corr["id"])
                )
    conn.commit()


def _seed_pair_dicts(conn, pairs: dict):
    """Seed {key: (en_val, zh_val)} into bilingual_text."""
    for key, (en_val, zh_val) in pairs.items():
        conn.execute(
            """INSERT OR REPLACE INTO bilingual_text (key, en, zh) VALUES (?, ?, ?)""",
            (key, en_val, zh_val)
        )
    conn.commit()


def _load(lang: str) -> dict[str, Path]:
    base = SEEDS_DIR / lang
    return {
        "ui_text": base / "ui_text.json",
        "pages": base / "pages.json",
        "corridors": base / "corridors.json",
        "pages_structure": base / "pages_structure.json",
        "corridors_structure": base / "corridors_structure.json",
        "scholars": base / "scholars.json",
        "heritage_sites": base / "heritage_sites.json",
    }


def seed_all():
    """Full seed from data/seeds/ JSON files."""
    conn = get_db()

    # Bilingual text: merge ui_text + pages + corridors per locale, then seed once
    en_merged, zh_merged = {}, {}
    for lang, target in (("en", en_merged), ("zh", zh_merged)):
        files = _load(lang)
        for fname in ("ui_text", "pages", "corridors"):
            p = files[fname]
            if p.exists():
                target.update(json.loads(p.read_text(encoding="utf-8")))
    seed_bilingual_text(conn, en_merged, zh_merged)

    en_files = _load("en")
    zh_files = _load("zh")
    if en_files["pages_structure"].exists():
        seed_pages(
            conn,
            json.loads(en_files["pages_structure"].read_text(encoding="utf-8")),
            json.loads(zh_files["pages_structure"].read_text(encoding="utf-8")) if zh_files["pages_structure"].exists() else [],
        )

    # Corridors
    if en_files["corridors_structure"].exists():
        seed_corridors(conn, json.loads(en_files["corridors_structure"].read_text(encoding="utf-8")))

    # Scholars (records + their bilingual text)
    if en_files["scholars"].exists():
        en_s = json.loads(en_files["scholars"].read_text(encoding="utf-8"))
        zh_s = json.loads(zh_files["scholars"].read_text(encoding="utf-8")) if zh_files["scholars"].exists() else []
        zmap = {s["name_key"]: s for s in zh_s}
        texts = {}
        for s in en_s:
            z = zmap.get(s["name_key"], {})
            texts[s["name_key"]] = (s.get("name_en", ""), z.get("name_zh", ""))
            if s.get("bio_key"):
                texts[s["bio_key"]] = (s.get("bio_en", ""), z.get("bio_zh", ""))
        _seed_pair_dicts(conn, texts)
        seed_scholars(conn, en_s, zh_s)

    # Heritage sites
    if en_files["heritage_sites"].exists():
        en_h = json.loads(en_files["heritage_sites"].read_text(encoding="utf-8"))
        zh_h = json.loads(zh_files["heritage_sites"].read_text(encoding="utf-8")) if zh_files["heritage_sites"].exists() else []
        zmap = {s["name_key"]: s for s in zh_h}
        texts = {}
        for s in en_h:
            z = zmap.get(s["name_key"], {})
            texts[s["name_key"]] = (s.get("name_en", ""), z.get("name_zh", ""))
            if s.get("description_key"):
                texts[s["description_key"]] = (s.get("description_en", ""), z.get("description_zh", ""))
        _seed_pair_dicts(conn, texts)
        seed_heritage_sites(conn, en_h, zh_h)

    # Knowledge-graph edges
    seed_relations(conn)

    conn.close()
    print("Seed completed.")


def seed_if_empty():
    """Seed only if the database has no content."""
    conn = get_db()
    count = conn.execute("SELECT COUNT(*) FROM bilingual_text").fetchone()[0]
    conn.close()
    if count > 0:
        return
    seed_all()


if __name__ == "__main__":
    init_db()
    seed_all()