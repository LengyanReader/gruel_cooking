import sqlite3
import sys

sys.path.insert(0, ".")
conn = sqlite3.connect("data/living_heritage.db")
conn.row_factory = sqlite3.Row

fails = []
def check(desc, ok):
    if ok:
        print(f"  [PASS] {desc}")
    else:
        print(f"  [FAIL] {desc}")
        fails.append(desc)

def full_key(key):
    row = conn.execute("SELECT en, zh FROM bilingual_text WHERE key=?", (key,)).fetchone()
    return bool(row and row["en"] and row["zh"])

print("== HARD ASSERTIONS ==")
check("四大廊道齐备", conn.execute("SELECT COUNT(*) FROM corridors").fetchone()[0] == 4)
for c in ["grand_canal", "gotland", "southern_oland", "linkoping"]:
    check(f"廊道存在且双语齐备: {c}", full_key(f"corridor.{c}.title"))

n_sites = conn.execute("SELECT COUNT(*) FROM heritage_sites").fetchone()[0]
n_scholars = conn.execute("SELECT COUNT(*) FROM scholars").fetchone()[0]
n_pubs = conn.execute("SELECT COUNT(*) FROM publications").fetchone()[0]
n_obs = conn.execute("SELECT COUNT(*) FROM field_observations").fetchone()[0]
check("学者 >= 5 且每名有双语名与机构",
      n_scholars >= 5 and all(
          full_key(r["name_key"]) and r["institution"]
          for r in conn.execute("SELECT name_key, institution FROM scholars").fetchall()))
check("文献库非空且每篇双语标题+来源级别合法",
      n_pubs > 0 and all(
          full_key(r["title_key"]) and r["source_level"] in ("A", "B", "C", "D")
          for r in conn.execute("SELECT title_key, source_level FROM publications").fetchall()))
check("每篇文献有 tags",
      all((r["tags"] or "").strip() for r in conn.execute("SELECT tags FROM publications").fetchall()))
check("田野观察非空且每条约记双语",
      n_obs > 0 and all(
          full_key(r["title_key"]) and full_key(r["notes_key"])
          for r in conn.execute("SELECT title_key, notes_key FROM field_observations").fetchall()))
check("每条观察挂接有效站点",
      all(
          conn.execute("SELECT 1 FROM heritage_sites WHERE id=?", (r["site_id"],)).fetchone()
          for r in conn.execute("SELECT site_id FROM field_observations").fetchall()
          if r["site_id"]))
check("无占位/待核标记残留",
      not any(
          v and (("[待核]" in v) or ("UNVERIFIED" in v) or ("to be verified" in v.lower()))
          for v in [row["en"] for row in conn.execute("SELECT en FROM bilingual_text").fetchall()]
      ) and not any(
          v and ("[待核]" in v)
          for v in [row["zh"] for row in conn.execute("SELECT zh FROM bilingual_text").fetchall()]
      ))

n_rel_site = conn.execute("SELECT COUNT(*) FROM relations WHERE relation='belongs_to'").fetchone()[0]
n_rel_obs = conn.execute("SELECT COUNT(*) FROM relations WHERE relation='involves' AND source_type='observation'").fetchone()[0]
n_rel_pub = conn.execute("SELECT COUNT(*) FROM relations WHERE relation='involves' AND source_type='publication'").fetchone()[0]
n_rel_auth = conn.execute("SELECT COUNT(*) FROM relations WHERE relation='authored'").fetchone()[0]
check(f"每站点都有 belongs_to 边 ({n_rel_site}/{n_sites})", n_rel_site == n_sites)
check(f"每条观察都有 involves→site 边 ({n_rel_obs}/{n_obs})", n_rel_obs == n_obs)
check("存在 authored 学者→文献 边", n_rel_auth > 0)
check("存在 involves 文献→廊道 边", n_rel_pub >= n_pubs)

print("== INFO ==")
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