#!/usr/bin/env python3
"""Language Stacking: 一词万境查询层（阶段二织网读路径）

不依赖 neo4j 服务器：直接在图数据模型上回答织网查询
（数据经由 build_learning.py --db 同步到 learning.db）。

子命令:
  list                     列出全部权威概念（Core Glossary）
  concept KEY [--cypher]   一词万境：概念 × 八语词位 + 挂接词条 + 织线；
                           --cypher 打印等同的 neo4j 查询
  script                   文字体系（language × WRITES_IN）
  thread                   词源/借词织线
  sound LANG REF           音图邻居（如: sound ja き → 行/列邻接）

用法:
  python "Language Stacking-Linguistic Weaving/web/weave_query.py" list
  python "Language Stacking-Linguistic Weaving/web/weave_query.py" concept water
  python "Language Stacking-Linguistic Weaving/web/weave_query.py" sound ja き
"""
import argparse
import os
import sqlite3
import sys

from export_neo4j import concept_key, cypher_escape

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOMAIN = os.path.join(REPO, "Language Stacking-Linguistic Weaving")
DB = os.path.join(DOMAIN, "languages", "data", "learning.db")

THREAD_KIND = {"derives_from": "沿根", "loaned_to": "借渡", "translates": "镜像"}


def con():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c


def find_concept(c, key):
    key = key.strip().lower()
    row = c.execute("SELECT * FROM concepts WHERE id=? OR name_zh=? OR lower(name_en)=?",
                    (key, key, key)).fetchone()
    if row is None:
        cands = [r["id"] for r in c.execute(
            "SELECT id FROM concepts ORDER BY id").fetchall()]
        sys.exit(f"[concept] 未找到概念 {key!r}；现有: {', '.join(cands)}")
    return row


def cmd_list(c, cypher=False):
    rows = c.execute(
        """SELECT co.id, co.name_zh, co.name_en, co.probe,
                  COUNT(DISTINCT ct.lang) AS langs
           FROM concepts co LEFT JOIN concept_terms ct ON ct.concept = co.id
           GROUP BY co.id ORDER BY co.id""").fetchall()
    print(f"{'id':<12} {'zh':<10} {'en':<12} 语种数  probe")
    for r in rows:
        print(f"{r['id']:<12} {r['name_zh']:<10} {r['name_en']:<12} "
              f"{r['langs']:<6} {r['probe']}")


def cmd_concept(c, key, cypher=False):
    if cypher:
        q = ("MATCH (c:Concept {key:$key})<-[:EXPRESSES]-(t:Term) "
             "RETURN t.lang, t.word, t.roma ORDER BY t.lang")
        print(f"// neo4j 一词万境（.key => \"{cypher_escape(key)}\"）")
        print(q)
        print()
        q2 = ("MATCH (c:Concept {key:$key})<-[:EXPRESSES]-(n) "
               "OPTIONAL MATCH (n)-[r:DERIVES_FROM|:LOANED_TO|:TRANSLATES]->(m) "
               "RETURN labels(n) AS kind, coalesce(n.word, n.hira) AS w, "
               "type(r) AS rel, coalesce(m.word, m.id) AS to_ ORDER BY w")
        print("// 挂接词条与织线")
        print(q2)
        return
    row = find_concept(c, key)
    cid = row["id"]
    terms = c.execute("SELECT * FROM concept_terms WHERE concept=? ORDER BY lang", (cid,)).fetchall()
    print(f"### {row['name_zh']} / {row['name_en']}  [{cid}]  probe={row['probe']}")
    print(f"{'lang':<4} {'term':<14} {'roma':<18}")
    for t in terms:
        print(f"{t['lang']:<4} {t['word']:<14} {t['roma']:<18}")
    # 挂接的学习库词条（ja vocab 等）
    hits = c.execute("SELECT * FROM vocab").fetchall()
    attached = [w for w in hits if (concept_key(w["meaning_en"]) or "unmapped") == cid]
    if attached:
        print(f"\n挂接学习库词条 ({len(attached)}):")
        for w in attached:
            print(f"  [{w['lang']}/{w['module']}] {w['hira']} · {w['kana']} —— {w['meaning_en']}")
    # 织线
    ths = c.execute("SELECT * FROM threads").fetchall()
    touched = [t for t in ths
               if t["from_ref"].endswith(":" + cid) or t["to_ref"].endswith(":" + cid)]
    if touched:
        print("\n织线:")
        for t in touched:
            kind = THREAD_KIND.get(t["kind"], t["kind"])
            print(f"  ({kind}) {t['from_ref']} → {t['to_ref']}  {t['note_zh']}")


def cmd_script(c):
    for s in c.execute("SELECT * FROM scripts ORDER BY id"):
        langs = s["langs"]
        print(f"[{s['id']}] {s['name_zh']} · {s['name_en']} — 语: {langs}")
        print(f"       {s['note_zh']}  |  {s['note_en']}")


def cmd_thread(c):
    for t in c.execute("SELECT * FROM threads ORDER BY id"):
        kind = THREAD_KIND.get(t["kind"], t["kind"])
        print(f"({kind:4s}) {t['from_ref']:<12} -> {t['to_ref']:<14}  {t['note_zh']}")


def cmd_sound(c, lang, ref):
    row = c.execute("SELECT * FROM chart_cells WHERE lang=? AND (h=? OR roma=?)",
                    (lang, ref, ref)).fetchone()
    if row is None:
        sys.exit(f"[sound] {lang} 无单元 {ref!r}")
    print(f"### {lang} · 单元 {row['h']}({row['kata']}) roma={row['roma']} note={row['note']!r} "
          f"@行{row['row']}列{row['col']}")
    rows = {r["row"]: r["col"] for r in c.execute(
        "SELECT row, col FROM chart_cells WHERE lang=?", (lang,))}
    cols = [r for r in set(rows.values())]
    # 同行邻居（列 ±1）
    mates = c.execute(
        "SELECT * FROM chart_cells WHERE lang=? AND row=? ORDER BY col", (lang, row["row"])).fetchall()
    print("同行:", " ".join(f"{m['h']}({m['roma']})" if not m["note"] else
                             f"{m['h']}[{m['note']}]" for m in mates))
    # 同列上下邻居（相邻行同 col）
    vertical = c.execute(
        "SELECT * FROM chart_cells WHERE lang=? AND col=? AND note != 'void' ORDER BY row",
        (lang, row["col"])).fetchall()
    print("同列:", " ".join(f"{v['h']}({v['roma']})" for v in vertical if v['h']))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sub", choices=["list", "concept", "script", "thread", "sound"])
    ap.add_argument("key", nargs="?")
    ap.add_argument("--lang", default="ja")
    ap.add_argument("--cypher", action="store_true")
    args = ap.parse_args()

    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    if not os.path.exists(DB):
        sys.exit(f"[weave] 缺 sqlite 索引: {DB}  (先运行 build_learning.py --db)")

    c = con()
    if args.sub == "list":
        cmd_list(c, args.cypher)
    elif args.sub == "concept":
        if not args.key:
            sys.exit("[concept] 需要概念 key，如: taste concept water")
        cmd_concept(c, args.key, args.cypher)
    elif args.sub == "script":
        cmd_script(c)
    elif args.sub == "thread":
        cmd_thread(c)
    elif args.sub == "sound":
        cmd_sound(c, args.lang, args.key or "き")


if __name__ == "__main__":
    main()