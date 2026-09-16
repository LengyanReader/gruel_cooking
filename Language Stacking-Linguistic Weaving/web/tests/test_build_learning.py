# -*- coding: utf-8 -*-
"""学习库生成器 build_learning.py 的单元/集成测试。

测试环境: conda activate hy_py312（含 markdown）。
运行:     python -m pytest "Language Stacking-Linguistic Weaving/web/tests" -q
"""
import json
import os
import sqlite3

import pytest

import build_learning as bl

DATA_JA = os.path.join(bl.DATA, "ja", "gojuon.json")


# ── frontmatter / md 工具 ──────────────────────────────────────
def test_parse_frontmatter_ok():
    meta, body = bl.parse_frontmatter('---json\n{"a": 1}\n---\n# 正文\n')
    assert meta == {"a": 1}
    assert body.strip() == "# 正文"


def test_parse_frontmatter_none():
    meta, body = bl.parse_frontmatter("# 无 frontmatter\n")
    assert meta is None
    assert body.startswith("# ")


def test_parse_frontmatter_malformed_json():
    with pytest.raises(ValueError):
        bl.parse_frontmatter('---json\n{"a":\n---\nbody')


def test_strip_h1_removes_first_only():
    out = bl.strip_h1("# H1\n\n## H2\n")
    assert "# H2" in out and "# H1" not in out


def test_render_prose_bilingual_blocks():
    md = ("# t\n\n前言\n\n<!-- zh -->\n中文段落\n\n<!-- en -->\nEnglish para\n")
    html = bl.render_prose(bl.strip_h1(md))
    assert '<div data-bit="zh">' in html
    assert '<div data-bit="en">' in html
    assert "中文段落" in html and "English para" in html
    # 无标记的共享段应双份（zh+en）
    assert html.count("前言") == 2


def test_render_prose_no_markers_doubled():
    html = bl.render_prose("只有一个段落")
    assert html.count('<div data-bit="zh">') == 1
    assert html.count('<div data-bit="en">') == 1


# ── 音图渲染（真数据不变式）──────────────────────────────────
def test_kana_table_structure():
    data = json.loads(bl.read(DATA_JA))
    html = bl.kana_table_html(data)
    assert "kana-table" in html
    # 10 行 + ん 行
    assert html.count("rowname") == 11
    # 46 个假名单元 = 45 普通 + 1 particle(を)；void 5 个
    assert html.count("kana-cell\"") + html.count("kana-cell particle") == 46
    assert html.count("kana-cell void") == 5
    # 特殊音节（古音拼写残留）
    for roma in ("shi", "chi", "tsu", "fu"):
        assert f'>{roma}<' in html
    # を = particle
    assert 'particle' in html


def test_derived_chips():
    data = json.loads(bl.read(DATA_JA))
    html = bl.derived_html(data)
    assert html.count("dname") == 4
    assert "浊音" in html and "拗音" in html


def test_kana_table_speak_and_tips():
    data = json.loads(bl.read(DATA_JA))
    html = bl.kana_table_html(data)
    # 点击假名念假名本身（日语 TTS 念假名 = 单音节连读），不念罗马音
    assert "kanaSpeak(" in html
    assert 'onclick="kanaSpeak(\'\u3042\')" data-h="\u3042" data-r="a"' in html
    # pron 指南以双语 tooltip 呈现
    assert "kana-tip" in html
    assert "类似" in html and "open vowel" in html
    # 每个非 void 格有发音人比对照（可点击的 voice 按钮容器）
    assert html.count("kana-voices") == 46
    # particle 格仍带 particle 类
    assert 'kana-cell particle" onclick="kanaSpeak(' in html
    assert 'data-h="\u3092" data-r="o"' in html
    # void 格空
    assert 'kana-cell void"' in html
    assert "kanaSpeak" not in html.split("kana-cell void")[1].split("<span>")[0]


def test_vocab_rows():
    data = json.loads(bl.read(DATA_JA))
    html = bl.vocab_html(data)
    assert len(data["vocab"]) == 46
    assert html.count('<td class="kc">') == 46
    assert 'lang="ja"' in html
    assert "雨" in html and "あめ" in html


def test_module_data_blocks_gojuon():
    module = {"id": "gojuon", "status": "ready"}
    blocks = bl.module_data_blocks("ja", module)
    # 螺旋五视图：引导 + 四旋（形/词/义/源）+ 回望收束（返回 HTML 字符串片段）
    assert len(blocks) == 5
    # 各旋视图块以 class 标识离弦：guide / shape / word / sense / root
    markers = ["spiral-guide", "ring-shape", "ring-word", "ring-sense", "ring-root"]
    for i, m in enumerate(markers):
        assert m in blocks[i], f"block[{i}] 应含 {m}"
    joint = "".join(blocks)
    # 形环 五十音表 + 词环 gloss + 义环 文化 + 源环 字源 + 收束
    assert "五十音" in joint and "か" in joint
    assert "gloss" in joint.lower() and "あめ" in joint
    assert "季語" in joint.lower() and "美学" in joint.lower() and "典故" in joint


def test_module_data_blocks_missing_json_empty():
    assert bl.module_data_blocks("ja", {"id": "kanji"}) == []


# ── 校验 ───────────────────────────────────────────────────────
def test_validate_sources_clean():
    assert bl.validate_sources() == []


def test_validate_md_bilingual_imbalance(tmp_path):
    p = tmp_path / "a.md"
    p.write_text("# H1\n\n<!-- zh -->\n中文\n", encoding="utf-8")
    errs = []
    bl.validate_md_bilingual(str(p), errs, "x", "m")
    assert any("双语标记不平衡" in e for e in errs)


def test_validate_module_json_missing_fields(tmp_path):
    bad = {"vocab": [{"h": "a"}]}
    p = tmp_path / "m.json"
    p.write_text(json.dumps(bad, ensure_ascii=False), encoding="utf-8")
    errs = []
    bl.validate_module_json(str(p), errs, "x", "m")
    assert any("缺字段" in e for e in errs)


def test_validate_module_json_unknown_kind(tmp_path):
    good = {"meta": {"kind": "no-such-view"}, "vocab": []}
    p = tmp_path / "m.json"
    p.write_text(json.dumps(good, ensure_ascii=False), encoding="utf-8")
    errs = []
    bl.validate_module_json(str(p), errs, "x", "m")
    assert any("未注册渲染视图" in e for e in errs)


def test_validate_module_json_void_cell_no_extra_keys(tmp_path):
    good = {"chart": {"rows": [{"row": "や", "cells": [{"void": True, "h": "x"}]}]}}
    p = tmp_path / "m.json"
    p.write_text(json.dumps(good, ensure_ascii=False), encoding="utf-8")
    errs = []
    bl.validate_module_json(str(p), errs, "x", "m")
    assert any("多余键" in e for e in errs)


# ── registry / 页面组装（真数据）──────────────────────────────
def test_registry_has_ja_active():
    registry, _ = bl.load_registry()
    ja = next(x for x in registry["languages"] if x.get("status") == "active")
    assert ja["id"] == "ja"
    assert ja["href"] == "ja/"


def test_lcard_statuses():
    ready = {"id": "a", "glyph": "A", "name_zh": "a", "name_en": "a", "iso": "x",
             "summary_zh": "s", "summary_en": "s", "status": "active", "href": "a/"}
    planned = {**ready, "status": "planned", "href": None}
    assert 'card card-ready' in bl.lcard(ready)
    assert 'href="a/"' in bl.lcard(ready)
    assert 'card card-planned' in bl.lcard(planned)
    assert 'href="#future"' in bl.lcard(planned)


def test_mcard_ready_vs_planned():
    ready = {"id": "g", "href": "g.html", "status": "ready",
             "name_zh": "五十音", "name_en": "Gojūon",
             "desc_zh": "d", "desc_en": "d"}
    planned = {**ready, "status": "planned", "href": "#future"}
    assert 'card card-ready' in bl.mcard(ready)
    assert 'aria-disabled' in bl.mcard(planned)


def test_build_pages_expected_tree():
    pages = bl.build()
    registry, _ = bl.load_registry()
    active = [x for x in registry["languages"] if x.get("status") == "active"]
    # hub + 每 active 语索引 + 每 ready 模块页
    assert bl.OUT + os.sep + "index.html" in pages
    for entry in active:
        lang_idx = os.path.join(bl.OUT, entry["id"], "index.html")
        assert lang_idx in pages
    assert os.path.join(bl.OUT, "ja", "gojuon.html") in pages


def test_build_deterministic():
    a, b = bl.build(), bl.build()
    assert set(a) == set(b)
    for path in a:
        assert a[path] == b[path]


# ── sqlite 索引 ───────────────────────────────────────────────
def test_sync_sqlite_full(tmp_path):
    registry, _ = bl.load_registry()
    meta, _ = bl.parse_frontmatter(
        bl.read(os.path.join(bl.LANG, "ja", "README.md")))
    db_path = str(tmp_path / "learning.db")
    bl.sync_sqlite(registry, {"ja": meta.get("modules", [])}, db_path=db_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    assert cur.execute("SELECT COUNT(*) FROM languages").fetchone()[0] == len(registry["languages"])
    assert cur.execute("SELECT COUNT(*) FROM vocab").fetchone()[0] == 46
    assert cur.execute("SELECT COUNT(*) FROM chart_cells").fetchone()[0] == 51
    rows = cur.execute("SELECT DISTINCT roma FROM chart_cells WHERE roma IN"
                       " ('shi','chi','tsu','fu','n')").fetchall()
    assert {r[0] for r in rows} == {"shi", "chi", "tsu", "fu", "n"}
    note = cur.execute("SELECT note FROM chart_cells WHERE h='を'").fetchone()
    assert note and note[0] == "particle"
    # 幂等：重复同步不产生重复行
    bl.sync_sqlite(registry, {"ja": meta.get("modules", [])}, db_path=db_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    assert cur.execute("SELECT COUNT(*) FROM vocab").fetchone()[0] == 46
    con.close()