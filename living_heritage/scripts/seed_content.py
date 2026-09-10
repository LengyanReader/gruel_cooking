"""
Seed bilingual content into SQLite from JSON files.
Run: python scripts/seed_content.py
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.db.sqlite import get_db, init_db


def seed_bilingual_text(conn, en_data: dict, zh_data: dict, namespace: str = ""):
    """Insert bilingual text rows from en/zh dicts."""
    all_keys = set(en_data.keys()) | set(zh_data.keys())
    for key in all_keys:
        full_key = f"{namespace}.{key}" if namespace else key
        en_val = en_data.get(key, "")
        zh_val = zh_data.get(key, "")
        conn.execute(
            """INSERT OR REPLACE INTO bilingual_text (key, en, zh)
               VALUES (?, ?, ?)""",
            (full_key, en_val, zh_val)
        )
    conn.commit()


def seed_pages(conn, en_data: list, zh_data: list):
    """Seed pages and their sections."""
    zh_lookup = {p["slug"]: p for p in zh_data}
    for page in en_data:
        slug = page["slug"]
        conn.execute(
            """INSERT OR REPLACE INTO pages (slug, title_key, template, sort_order)
               VALUES (?, ?, ?, ?)""",
            (slug, page["title_key"], page["template"], page.get("sort_order", 0))
        )
        page_id = conn.execute("SELECT id FROM pages WHERE slug = ?", (slug,)).fetchone()[0]

        # Sections
        conn.execute("DELETE FROM page_sections WHERE page_id = ?", (page_id,))
        for i, section in enumerate(page.get("sections", [])):
            conn.execute(
                """INSERT INTO page_sections (page_id, section_key, title_key, body_key, sort_order)
                   VALUES (?, ?, ?, ?, ?)""",
                (page_id, section["key"], section.get("title_key"), section.get("body_key"), i)
            )
    conn.commit()


def seed_scholars(conn, en_data: list, zh_data: list):
    """Seed scholar records."""
    zh_lookup = {s["name_key"]: s for s in zh_data}
    for scholar in en_data:
        conn.execute(
            """INSERT OR REPLACE INTO scholars
               (name_key, bio_key, institution, specialization, website_url, corridor_slugs)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                scholar["name_key"],
                scholar.get("bio_key"),
                scholar.get("institution"),
                scholar.get("specialization"),
                scholar.get("website_url"),
                json.dumps(scholar.get("corridor_slugs", [])),
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


def seed_if_empty():
    """Seed only if the database has no content."""
    conn = get_db()
    count = conn.execute("SELECT COUNT(*) FROM bilingual_text").fetchone()[0]
    if count > 0:
        conn.close()
        return
    seed_all()
    conn.close()


def seed_all():
    """Full seed from data/seeds/ JSON files."""
    base = Path(__file__).parent.parent / "data" / "seeds"
    en_dir = base / "en"
    zh_dir = base / "zh"

    conn = get_db()

    # Bilingual text
    for filename in ["pages.json", "corridors.json", "scholars.json", "heritage_sites.json"]:
        en_file = en_dir / filename
        zh_file = zh_dir / filename
        if en_file.exists():
            en_data = json.loads(en_file.read_text(encoding="utf-8"))
            zh_data = json.loads(zh_file.read_text(encoding="utf-8")) if zh_file.exists() else {}
            seed_bilingual_text(conn, en_data, zh_data)

    # Pages
    en_pages = en_dir / "pages_structure.json"
    zh_pages = zh_dir / "pages_structure.json"
    if en_pages.exists():
        seed_pages(conn,
                   json.loads(en_pages.read_text(encoding="utf-8")),
                   json.loads(zh_pages.read_text(encoding="utf-8")) if zh_pages.exists() else [])

    # Scholars
    en_scholars = en_dir / "scholars.json"
    zh_scholars = zh_dir / "scholars.json"
    if en_scholars.exists():
        en_s = json.loads(en_scholars.read_text(encoding="utf-8"))
        zh_s = json.loads(zh_scholars.read_text(encoding="utf-8")) if zh_scholars.exists() else []
        # scholars.json has bilingual text mixed in, extract for text table
        text_data = {}
        for s in en_s:
            text_data[s["name_key"]] = s.get("name_en", "")
            if s.get("bio_key"):
                text_data[s["bio_key"]] = s.get("bio_en", "")
        zh_text = {}
        for s in zh_s:
            zh_text[s["name_key"]] = s.get("name_zh", "")
            if s.get("bio_key"):
                zh_text[s["bio_key"]] = s.get("bio_zh", "")
        seed_bilingual_text(conn, text_data, zh_text)
        seed_scholars(conn, en_s, zh_s)

    # Heritage sites
    en_sites = en_dir / "heritage_sites.json"
    zh_sites = zh_dir / "heritage_sites.json"
    if en_sites.exists():
        en_h = json.loads(en_sites.read_text(encoding="utf-8"))
        zh_h = json.loads(zh_sites.read_text(encoding="utf-8")) if zh_sites.exists() else []
        text_data = {}
        for s in en_h:
            text_data[s["name_key"]] = s.get("name_en", "")
            if s.get("description_key"):
                text_data[s["description_key"]] = s.get("description_en", "")
        zh_text = {}
        for s in zh_h:
            zh_text[s["name_key"]] = s.get("name_zh", "")
            if s.get("description_key"):
                zh_text[s["description_key"]] = s.get("description_zh", "")
        seed_bilingual_text(conn, text_data, zh_text)
        seed_heritage_sites(conn, en_h, zh_h)

    conn.close()
    print("Seed completed.")


if __name__ == "__main__":
    init_db()
    seed_all()
