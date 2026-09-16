# -*- coding: utf-8 -*-
"""Core Glossary 织网库：校验、sqlite 同步、页面渲染、weave_query 读路径。"""
import os
import sqlite3

import pytest

import build_learning as bl


def _tmp_db(tmp_path):
    registry, _ = bl.load_registry()
    meta, _ = bl.parse_frontmatter(bl.read(os.path.join(bl.LANG, "ja", "README.md")))
    db_path = str(tmp_path / "learning.db")
    bl.sync_sqlite(registry, {"ja": meta.get("modules", [])}, db_path=db_path)
    return db_path


# ── 校验 ───────────────────────────────────────────────────────
def test_validate_glossary_clean():
    assert bl.validate_glossary() == []


def test_validate_glossary_missing_terms(tmp_path, monkeypatch):
    bad = {"languages": ["zh", "en"], "concepts": [
        {"id": "dup", "name_zh": "a", "name_en": "a",
         "terms": {"zh": {"word": "x", "roma": "x"}}},
        {"id": "dup", "name_zh": "b", "name_en": "b", "terms": {"zh": {"word": "y"}}},
    ], "scripts": [], "threads": []}
    p = tmp_path / "core_glossary.json"
    p.write_text(bl.json.dumps(bad, ensure_ascii=False), encoding="utf-8")
    monkeypatch.setattr(bl, "GLOSSARY_JSON", str(p))
    errs = bl.validate_glossary()
    assert any("缺语种词位: ['en']" in e for e in errs)
    assert any("id 重复" in e for e in errs)
    assert any("缺 roma 键" in e for e in errs)
    assert any("meta.review" in e for e in errs)


# ── sqlite ─────────────────────────────────────────────────────
def test_sync_glossary_counts(tmp_path):
    db_path = _tmp_db(tmp_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    assert cur.execute("SELECT COUNT(*) FROM concepts").fetchone()[0] == 12
    assert cur.execute("SELECT COUNT(*) FROM concept_terms").fetchone()[0] == 96
    assert cur.execute("SELECT COUNT(*) FROM scripts").fetchone()[0] == 4
    assert cur.execute("SELECT COUNT(*) FROM threads").fetchone()[0] == 9
    # 每概念 8 语，probe 默认 0（权威）
    n_terms = cur.execute(
        "SELECT COUNT(*) FROM concept_terms GROUP BY concept").fetchall()
    assert {r[0] for r in n_terms} == {8}
    assert cur.execute("SELECT SUM(probe) FROM concepts").fetchone()[0] == 0
    con.close()


# ── 页面 ───────────────────────────────────────────────────────
def test_build_includes_glossary_page():
    pages = bl.build()
    idx = os.path.join(bl.OUT, "glossary", "index.html")
    assert idx in pages
    assert '<section class="wgrid">' in pages[idx]
    assert "review pending" in pages[idx]
    hub = pages[os.path.join(bl.OUT, "index.html")]
    assert 'href="glossary/"' in hub


def test_render_glossary_page_content():
    html = bl.render_glossary_page()
    assert html.count("wcard") == 12
    # 概念 id 与八语词位齐备（water）
    assert '<span class="wid">water</span>' in html
    assert "mizu" in html and "水" in html
    # 织线（water 卡以人读谱系注展示：water ← PIE *wédor）
    assert "w\u00e9dor" in html
    # 审校纪律：词位不得静默当审校过
    assert "review pending" in html


# ── weave_query 读路径 ─────────────────────────────────────────
def test_weave_concept_water(tmp_path, capsys):
    db_path = _tmp_db(tmp_path)
    import weave_query as wq
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    wq.cmd_concept(con, "water")
    out = capsys.readouterr().out
    assert "### 水" in out and "[water]" in out
    for word in ("水", "water", "eau", "aqua", "jala", "Wasser", "vatten"):
        assert word in out
    assert "root:pie-wedor" in out    # 织线
    assert "みず" in out             # 挂接学习库词条（ja 五十音 水）
    con.close()


def test_weave_concept_unknown(tmp_path, capsys):
    db_path = _tmp_db(tmp_path)
    import weave_query as wq
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    with pytest.raises(SystemExit):
        wq.cmd_concept(con, "no-such-concept")
    con.close()


def test_weave_sound_neighbours(tmp_path, capsys):
    db_path = _tmp_db(tmp_path)
    import weave_query as wq
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    wq.cmd_sound(con, "ja", "き")
    out = capsys.readouterr().out
    assert "き" in out and "か" in out and "こ" in out   # 同行 か行
    assert "い" in out and "し" in out and "り" in out   # 同列 i 段
    con.close()


def test_weave_list_and_thread(tmp_path, capsys):
    db_path = _tmp_db(tmp_path)
    import weave_query as wq
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    wq.cmd_list(con)
    out = capsys.readouterr().out
    assert "water" in out and "nature" in out and "probe" in out
    wq.cmd_thread(con)
    out = capsys.readouterr().out
    assert out.count("->") == 9
    assert "借渡" in out
    con.close()