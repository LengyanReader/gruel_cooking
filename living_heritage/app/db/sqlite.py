"""
SQLite connection and schema management.
No ORM — raw sqlite3 for transparency and zero coupling.
"""
import sqlite3
from pathlib import Path
from app.config import SQLITE_PATH

_schema_sql = """
CREATE TABLE IF NOT EXISTS bilingual_text (
    id          INTEGER PRIMARY KEY,
    key         TEXT    NOT NULL UNIQUE,
    en          TEXT,
    zh          TEXT,
    created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
    updated_at  TEXT    NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_bt_key ON bilingual_text(key);

CREATE TABLE IF NOT EXISTS pages (
    id          INTEGER PRIMARY KEY,
    slug        TEXT    NOT NULL UNIQUE,
    title_key   TEXT    NOT NULL,
    template    TEXT    NOT NULL,
    nav_key     TEXT,
    sort_order  INTEGER NOT NULL DEFAULT 0,
    is_published INTEGER NOT NULL DEFAULT 1,
    meta_json   TEXT,
    created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
    updated_at  TEXT    NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS page_sections (
    id              INTEGER PRIMARY KEY,
    page_id         INTEGER NOT NULL REFERENCES pages(id) ON DELETE CASCADE,
    section_key     TEXT    NOT NULL,
    title_key       TEXT,
    body_key        TEXT,
    content_type    TEXT    NOT NULL DEFAULT 'richtext',
    sort_order      INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS heritage_sites (
    id              INTEGER PRIMARY KEY,
    name_key        TEXT    NOT NULL UNIQUE,
    description_key TEXT,
    corridor_slug   TEXT    NOT NULL,
    latitude        REAL,
    longitude       REAL,
    heritage_type   TEXT,
    year_established TEXT,
    unesco_status   TEXT,
    photo_url       TEXT,
    created_at      TEXT    NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_hs_corridor ON heritage_sites(corridor_slug);

CREATE TABLE IF NOT EXISTS scholars (
    id              INTEGER PRIMARY KEY,
    name_key        TEXT    NOT NULL UNIQUE,
    bio_key         TEXT,
    institution     TEXT,
    specialization  TEXT,
    photo_url       TEXT,
    website_url     TEXT,
    corridor_slugs  TEXT,
    works_json      TEXT,
    traits_json     TEXT,
    created_at      TEXT    NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS field_observations (
    id              INTEGER PRIMARY KEY,
    site_id         INTEGER REFERENCES heritage_sites(id) ON DELETE SET NULL,
    scholar_id      INTEGER REFERENCES scholars(id) ON DELETE SET NULL,
    date_observed   TEXT,
    title_key       TEXT,
    notes_key       TEXT,
    observation_type TEXT,
    tags            TEXT,
    photos          TEXT,
    created_at      TEXT    NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_fo_site ON field_observations(site_id);

CREATE TABLE IF NOT EXISTS corridors (
    id          INTEGER PRIMARY KEY,
    slug        TEXT    NOT NULL UNIQUE,
    title_key   TEXT,
    intro_key   TEXT,
    detail_key  TEXT,
    region      TEXT,
    sort_order  INTEGER NOT NULL DEFAULT 0,
    created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_cor_sort ON corridors(sort_order);

CREATE TABLE IF NOT EXISTS relations (
    id          INTEGER PRIMARY KEY,
    source_type TEXT    NOT NULL,
    source_id   INTEGER NOT NULL,
    relation    TEXT    NOT NULL,
    target_type TEXT    NOT NULL,
    target_id   INTEGER NOT NULL,
    weight      REAL,
    note        TEXT,
    created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_rel_source ON relations(source_type, source_id);
CREATE INDEX IF NOT EXISTS idx_rel_target ON relations(target_type, target_id);

CREATE TABLE IF NOT EXISTS publications (
    id              INTEGER PRIMARY KEY,
    title_key       TEXT    NOT NULL,
    abstract_key    TEXT,
    authors         TEXT,
    publication_type TEXT,
    year            INTEGER,
    doi             TEXT,
    url             TEXT,
    pdf_url         TEXT,
    tags            TEXT,
    corridor_slugs  TEXT,
    created_at      TEXT    NOT NULL DEFAULT (datetime('now'))
);
"""


def get_db() -> sqlite3.Connection:
    """Get a synchronous SQLite connection (sqlite3 is already fast for reads)."""
    Path(SQLITE_PATH).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(SQLITE_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    """Create tables if they don't exist, and migrate older DBs."""
    conn = get_db()
    conn.executescript(_schema_sql)
    _migrate(conn)
    conn.close()
    print(f"SQLite initialized: {SQLITE_PATH}")


def _migrate(conn):
    """Add columns introduced after the initial schema (no-op on fresh DBs)."""
    columns = {r[1] for r in conn.execute("PRAGMA table_info(scholars)").fetchall()}
    if "works_json" not in columns:
        conn.execute("ALTER TABLE scholars ADD COLUMN works_json TEXT")
    if "traits_json" not in columns:
        conn.execute("ALTER TABLE scholars ADD COLUMN traits_json TEXT")
    page_cols = {r[1] for r in conn.execute("PRAGMA table_info(pages)").fetchall()}
    if "nav_key" not in page_cols:
        conn.execute("ALTER TABLE pages ADD COLUMN nav_key TEXT")
    conn.commit()
