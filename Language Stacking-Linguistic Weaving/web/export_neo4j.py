#!/usr/bin/env python3
"""Language Stacking: neo4j 阶段二导出器

读取 --db 生成的 sqlite 学习库索引(languages/data/learning.db),
导出可导入 neo4j 的 Cypher 文本(languages/data/neo4j_load.cypher)。

图谱模型(schema 文档: languages/docs/neo4j_schema.md):
  (:Language)-[:HAS_MODULE]->(:Module)-[:HAS_SOUND]->(:Sound)
             └-[HAS_MODULE]->(:Module)-[:HAS_WORD]->(:Word)-[:EXPRESSES]->(:Concept)
  (:Concept) <-[:EXPRESSES]-(:Term)     # 八语词位（Core Glossary，probe=false）
  (:Language)-[:WRITES_IN]->(:Script)
  (:Term|:Root)-[:DERIVES_FROM|:LOANED_TO|:TRANSLATES]->(:Term|:Root)   # 词源织线

概念权威：concepts 表 = Core Glossary（校准，probe=false）；
未落入权威表的学习库语义自动聚合为探针概念（probe=true，日志会列出待校准）。

幂等: 全部使用 MERGE + SET,可反复导入。每条语句包进 CALL { } IN TRANSACTIONS;
三个作用一座桥: ① cypher-shell 脚本模式作用域隔离(同名变量不冲突)
② 逐条独立提交 ③ 保留 MERGE 幂等语义。
用法:
  python "Language Stacking-Linguistic Weaving/web/build_learning.py" --db   # 先建 sqlite
  python "Language Stacking-Linguistic Weaving/web/export_neo4j.py" [--db-path PATH] [--out PATH] [--quiet]
  docker exec ls-neo4j cypher-shell -u neo4j -p <pass> -f /tmp/neo4j_load.cypher
"""
import argparse
import os
import re
import sqlite3
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOMAIN = os.path.join(REPO, "Language Stacking-Linguistic Weaving")
DB   = os.path.join(DOMAIN, "languages", "data", "learning.db")
OUT  = os.path.join(DOMAIN, "languages", "data", "neo4j_load.cypher")

RELID = {"derives_from": "DERIVES_FROM", "loaned_to": "LOANED_TO", "translates": "TRANSLATES"}


def cypher_escape(s):
    return str(s).replace("\\", "\\\\").replace('"', '\\"')


def concept_key(meaning_en):
    """meaning_en → 稳定探针 key(小写、去标点、压空格)。正式概念由 Glossary 校准。"""
    k = re.sub(r"[^a-z0-9 ]", "", meaning_en.lower())
    return re.sub(r"\s+", " ", k).strip()


def _rows(cur, sql):
    cur.execute(sql)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]


def cstmt(body):
    """把单条语句包装为 cypher-shell 独立作用域语句。

    neo4j 5 cypher-shell -f 脚本模式共享变量作用域，同名变量(如 l/m/w)会
    报 "Variable already declared"；每条包进 CALL { } IN TRANSACTIONS 即可。
    """
    return "CALL { %s } IN TRANSACTIONS;" % " ".join(body.split())


def export_cypher(db_path):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    languages = _rows(cur, "SELECT * FROM languages ORDER BY id")
    modules = _rows(cur, "SELECT * FROM modules ORDER BY lang, id")
    sounds = _rows(cur, "SELECT * FROM chart_cells ORDER BY lang, module, row, col")
    words = _rows(cur, "SELECT * FROM vocab ORDER BY lang, module, id")

    L = []
    L.append("// 语言叠织 · Language Stacking — neo4j 导入脚本")
    L.append(f"// 生成: {date.today().isoformat()} · export_neo4j.py · 从 learning.db 导出")
    L.append(f"// 规模: Language={len(languages)} Module={len(modules)} "
             f"Sound={len(sounds)} Word={len(words)}")
    L.append("")

    for l in languages:
        L.append(cstmt(f"MERGE (l:Language {{id: \"{cypher_escape(l['id'])}\"}})"
                       f" SET l.glyph=\"{cypher_escape(l['glyph'])}\", "
                       f"l.name_zh=\"{cypher_escape(l['name_zh'])}\", "
                       f"l.name_en=\"{cypher_escape(l['name_en'])}\", "
                       f"l.iso=\"{cypher_escape(l['iso'])}\", "
                       f"l.status=\"{cypher_escape(l['status'])}\""))

    for m in modules:
        L.append(cstmt(f"MERGE (m:Module {{lang: \"{cypher_escape(m['lang'])}\", "
                       f"id: \"{cypher_escape(m['id'])}\"}})"
                       f" SET m.name_zh=\"{cypher_escape(m['name_zh'])}\", "
                       f"m.name_en=\"{cypher_escape(m['name_en'])}\", "
                       f"m.status=\"{cypher_escape(m['status'])}\""))
        L.append(cstmt(f"MATCH (l:Language {{id: \"{cypher_escape(m['lang'])}\"}}), "
                       f"(m:Module {{lang: \"{cypher_escape(m['lang'])}\", id: \"{cypher_escape(m['id'])}\"}})"
                       f" MERGE (l)-[:HAS_MODULE]->(m)"))

    for snd in sounds:
        L.append(cstmt(f"MERGE (s:Sound {{lang: \"{cypher_escape(snd['lang'])}\", "
                       f"module: \"{cypher_escape(snd['module'])}\", "
                       f"row: \"{cypher_escape(snd['row'])}\", col: {snd['col']}}})"
                       f" SET s.hira=\"{cypher_escape(snd['h'])}\", "
                       f"s.kata=\"{cypher_escape(snd['kata'])}\", "
                       f"s.roma=\"{cypher_escape(snd['roma'])}\", "
                       f"s.note=\"{cypher_escape(snd['note'])}\""))
        L.append(cstmt(f"MATCH (m:Module {{lang: \"{cypher_escape(snd['lang'])}\", "
                       f"id: \"{cypher_escape(snd['module'])}\"}}), "
                       f"(s:Sound {{lang: \"{cypher_escape(snd['lang'])}\", "
                       f"module: \"{cypher_escape(snd['module'])}\", "
                       f"row: \"{cypher_escape(snd['row'])}\", col: {snd['col']}}})"
                       f" MERGE (m)-[:HAS_SOUND]->(s)"))

    for w in words:
        L.append(cstmt(f"MERGE (w:Word {{lang: \"{cypher_escape(w['lang'])}\", "
                       f"module: \"{cypher_escape(w['module'])}\", "
                       f"id: \"{cypher_escape(w['id'])}\"}})"
                       f" SET w.hira=\"{cypher_escape(w['hira'])}\", "
                       f"w.kata=\"{cypher_escape(w['kata'])}\", "
                       f"w.roma=\"{cypher_escape(w['roma'])}\", "
                       f"w.kanji=\"{cypher_escape(w['kanji'])}\", "
                       f"w.kana=\"{cypher_escape(w['kana'])}\", "
                       f"w.meaning_zh=\"{cypher_escape(w['meaning_zh'])}\", "
                       f"w.meaning_en=\"{cypher_escape(w['meaning_en'])}\""))
        L.append(cstmt(f"MATCH (m:Module {{lang: \"{cypher_escape(w['lang'])}\", "
                       f"id: \"{cypher_escape(w['module'])}\"}}), "
                       f"(w:Word {{lang: \"{cypher_escape(w['lang'])}\", "
                       f"module: \"{cypher_escape(w['module'])}\", "
                       f"id: \"{cypher_escape(w['id'])}\"}})"
                       f" MERGE (m)-[:HAS_WORD]->(w)"))

    # ── 织网库：Core Glossary 校准概念（权威，probe=false）──
    glossary = _rows(cur, "SELECT * FROM concepts ORDER BY id")
    gloss_ids = {c["id"] for c in glossary}
    for c in glossary:
        L.append(cstmt(f"MERGE (k:Concept {{key: \"{cypher_escape(c['id'])}\"}})"
                       f" SET k.probe=false, "
                       f"k.name_zh=\"{cypher_escape(c['name_zh'])}\", "
                       f"k.name_en=\"{cypher_escape(c['name_en'])}\""))

    # 探针概念：学习库词表里尚未校准的语义自动聚合（probe=true，待校准）
    used = set()
    for w in words:
        used.add(concept_key(w["meaning_en"]) or "unmapped")
    for key in sorted(used - gloss_ids):
        L.append(cstmt(f"MERGE (k:Concept {{key: \"{cypher_escape(key)}\"}})"
                       f" SET k.probe=true"))
    uncal = sorted(used - gloss_ids)
    if uncal:
        L.append(f"// 提示: {len(uncal)} 个探针概念待校准: {', '.join(uncal)}")

    # 八语词位 Term：(Term)-[:EXPRESSES]->(Concept)
    terms = _rows(cur, "SELECT * FROM concept_terms ORDER BY concept, lang")
    for t in terms:
        tkey = f"{t['lang']}:{t['concept']}"
        L.append(cstmt(f"MERGE (t:Term {{key: \"{cypher_escape(tkey)}\"}})"
                       f" SET t.lang=\"{cypher_escape(t['lang'])}\", "
                       f"t.concept=\"{cypher_escape(t['concept'])}\", "
                       f"t.word=\"{cypher_escape(t['word'])}\", "
                       f"t.roma=\"{cypher_escape(t['roma'])}\""))
        L.append(cstmt(f"MATCH (t:Term {{key: \"{cypher_escape(tkey)}\"}}), "
                       f"(k:Concept {{key: \"{cypher_escape(t['concept'])}\"}})"
                       f" MERGE (t)-[:EXPRESSES]->(k)"))

    # 学习库词条挂概念（命中权威概念的直接挂接）
    for w in words:
        key = concept_key(w["meaning_en"]) or "unmapped"
        L.append(cstmt(f"MATCH (w:Word {{lang: \"{cypher_escape(w['lang'])}\", "
                       f"module: \"{cypher_escape(w['module'])}\", id: \"{cypher_escape(w['id'])}\"}}), "
                       f"(k:Concept {{key: \"{cypher_escape(key)}\"}})"
                       f" MERGE (w)-[:EXPRESSES]->(k)"))

    # ── Script 节点 + (l:Language)-[:WRITES_IN]->(scr:Script) ──
    scripts = _rows(cur, "SELECT * FROM scripts ORDER BY id")
    for s in scripts:
        L.append(cstmt(f"MERGE (scr:Script {{id: \"{cypher_escape(s['id'])}\"}})"
                       f" SET scr.name_zh=\"{cypher_escape(s['name_zh'])}\", "
                       f"scr.name_en=\"{cypher_escape(s['name_en'])}\", "
                       f"scr.note_zh=\"{cypher_escape(s['note_zh'])}\", "
                       f"scr.note_en=\"{cypher_escape(s['note_en'])}\""))
        for lang_id in [x for x in s["langs"].split(",") if x]:
            L.append(cstmt(f"MATCH (l:Language {{id: \"{cypher_escape(lang_id)}\"}}), "
                           f"(scr:Script {{id: \"{cypher_escape(s['id'])}\"}})"
                           f" MERGE (l)-[:WRITES_IN]->(scr)"))

    # ── 织线：Root 节点 + (Term|Root)-[KIND]->(Term|Root) ──
    roots = set()
    threads = _rows(cur, "SELECT * FROM threads ORDER BY id")
    for t in threads:
        if t["to_ref"].startswith("root:"):
            roots.add(t["to_ref"].split(":", 1)[1])
    for rid in sorted(roots):
        L.append(cstmt(f"MERGE (r:Root {{id: \"{cypher_escape(rid)}\"}})"))
    for t in threads:
        rel = RELID[t["kind"]]
        from_ref = (f'(a:Term {{key: "{cypher_escape(t["from_ref"])}"}})'
                    if not t["from_ref"].startswith("root:")
                    else f'(a:Root {{id: "{cypher_escape(t["from_ref"].split(":", 1)[1])}"}})')
        to_ref = (f'(b:Term {{key: "{cypher_escape(t["to_ref"])}"}})'
                  if not t["to_ref"].startswith("root:")
                  else f'(b:Root {{id: "{cypher_escape(t["to_ref"].split(":", 1)[1])}"}})')
        L.append(cstmt(f"MATCH {from_ref}, {to_ref} "
                       f"MERGE (a)-[rel:{rel}]->(b) "
                       f"SET rel.note_zh=\"{cypher_escape(t['note_zh'])}\", "
                       f"rel.note_en=\"{cypher_escape(t['note_en'])}\""))

    L.append("")
    L.append("// 索引建议:")
    L.append("//   CREATE INDEX word_lang IF NOT EXISTS FOR (w:Word) ON (w.lang, w.module);")
    L.append("//   CREATE INDEX concept_key IF NOT EXISTS FOR (k:Concept) ON (k.key);")
    L.append("//   CREATE INDEX term_key IF NOT EXISTS FOR (t:Term) ON (t.key);")
    return "\n".join(L) + "\n"


def summarized_statements(text):
    """抽取被 CALL { ... } IN TRANSACTIONS; 包裹的语句体。"""
    return re.findall(r"CALL \{\s*(.*?)\s*\} IN TRANSACTIONS;", text, flags=re.S)


def summarize(text):
    stmts = summarized_statements(text)
    counts = {
        "Language": sum(1 for s in stmts if s.startswith("MERGE (l:Language {id:")),
        "Module": sum(1 for s in stmts if s.startswith("MERGE (m:Module {lang:")),
        "Sound": sum(1 for s in stmts if s.startswith("MERGE (s:Sound {lang:")),
        "Word": sum(1 for s in stmts if s.startswith("MERGE (w:Word {lang:")),
        "Term": sum(1 for s in stmts if s.startswith("MERGE (t:Term {key:")),
        "Concept": sum(1 for s in stmts if s.startswith("MERGE (k:Concept {key:")),
        "Script": sum(1 for s in stmts if s.startswith("MERGE (scr:Script {id:")),
        "Root": sum(1 for s in stmts if s.startswith("MERGE (r:Root {id:")),
    }
    rels = {
        "HAS_MODULE": sum(1 for s in stmts if s.endswith("MERGE (l)-[:HAS_MODULE]->(m)")),
        "HAS_SOUND": sum(1 for s in stmts if s.endswith("MERGE (m)-[:HAS_SOUND]->(s)")),
        "HAS_WORD": sum(1 for s in stmts if s.endswith("MERGE (m)-[:HAS_WORD]->(w)")),
        "WRITES_IN": sum(1 for s in stmts if s.endswith("MERGE (l)-[:WRITES_IN]->(scr)")),
        "EXPRESSES": sum(1 for s in stmts
                         if s.endswith("MERGE (t)-[:EXPRESSES]->(k)")
                         or s.endswith("MERGE (w)-[:EXPRESSES]->(k)")),
        "DERIVES_FROM": sum(1 for s in stmts if re.search(r"MERGE \(a\)-\[rel:DERIVES_FROM\]->\(b\)", s)),
        "LOANED_TO": sum(1 for s in stmts if re.search(r"MERGE \(a\)-\[rel:LOANED_TO\]->\(b\)", s)),
        "TRANSLATES": sum(1 for s in stmts if re.search(r"MERGE \(a\)-\[rel:TRANSLATES\]->\(b\)", s)),
    }
    return counts, rels


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db-path", default=DB)
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    if not os.path.exists(args.db_path):
        sys.exit(f"[export_neo4j] 缺 sqlite 索引: {args.db_path}  (先运行 build_learning.py --db)")

    text = export_cypher(args.db_path)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(text)

    counts, rels = summarize(text)
    if not args.quiet:
        print("[export_neo4j] 节点:", counts)
        print("              关系:", rels)
    print(f"[export_neo4j] 已导出 {len(text.splitlines())} 行 -> {args.out}")


if __name__ == "__main__":
    main()