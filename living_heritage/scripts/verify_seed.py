import sqlite3
import sys

sys.path.insert(0, ".")
conn = sqlite3.connect("data/living_heritage.db")
conn.row_factory = sqlite3.Row

for t in ["bilingual_text", "pages", "page_sections", "heritage_sites", "scholars", "corridors", "relations", "publications", "field_observations"]:
    n = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"{t}: {n}")

print("--- corridor titles ---")
rows = conn.execute(
    "SELECT key, en, zh FROM bilingual_text WHERE key LIKE 'corridor.%' AND key LIKE '%.title' ORDER BY key"
).fetchall()
for k in rows:
    d = dict(k)
    print(f"{d['key']} | {d['en']} | {d['zh']}")

print("--- sites ---")
rows = conn.execute("SELECT name_key FROM heritage_sites ORDER BY corridor_slug").fetchall()
for k in rows:
    print(dict(k)["name_key"])

print("--- scholars ---")
rows = conn.execute("SELECT name_key, institution FROM scholars").fetchall()
for k in rows:
    d = dict(k)
    print(f"{d['name_key']} | {d['institution']}")

print("--- nav resolves ---")
for locale in ("en", "zh"):
    r = conn.execute("SELECT en, zh FROM bilingual_text WHERE key='nav.home'").fetchone()
    d = dict(r)
    print(f"{locale}: nav.home -> {d.get(locale)}")

print("--- relations ---")
rows = conn.execute(
    "SELECT source_type, relation, target_type, COUNT(*) n FROM relations GROUP BY source_type, relation, target_type"
).fetchall()
for k in rows:
    print(dict(k))

print("--- pages nav_order ---")
rows = conn.execute("SELECT slug, nav_key, sort_order, is_published FROM pages ORDER BY sort_order").fetchall()
for k in rows:
    print(dict(k))

print("--- publications ---")
rows = conn.execute("SELECT title_key, source_level, year, authors FROM publications ORDER BY year DESC").fetchall()
for k in rows:
    d = dict(k)
    print(f"{d['title_key']} | [{d['source_level']}] | {d['year']} | {d['authors']}")

print("--- observations ---")
rows = conn.execute(
    "SELECT fo.title_key, fo.source_level, fo.date_observed, hs.name_key FROM field_observations fo LEFT JOIN heritage_sites hs ON fo.site_id = hs.id ORDER BY fo.date_observed DESC"
).fetchall()
for k in rows:
    d = dict(k)
    print(f"{d['title_key']} | [{d['source_level']}] | {d['date_observed']} | {d['name_key']}")

print("--- brand keys ---")
rows = conn.execute("SELECT key, en, zh FROM bilingual_text WHERE key LIKE 'brand.%' ORDER BY key").fetchall()
for k in rows:
    d = dict(k)
    print(f"{d['key']}: {d['en']} | {d['zh']}")

conn.close()