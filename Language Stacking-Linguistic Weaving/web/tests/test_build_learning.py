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
    # 例句挂同款多声线朗读盘（浏览器 ja TTS，可逐句点读整句）
    assert 'class="kana-voices sent-voices"' in html
    assert html.count("sent-voices") == 46


LAYERS = {"古典", "经典", "现代", "流行", "重大文明事件"}


def test_vocab_layers_present_in_data():
    data = json.loads(bl.read(DATA_JA))
    for v in data["vocab"]:
        assert v.get("layer_zh") in LAYERS, f'{v["h"]} 缺 layer_zh'
        assert v.get("layer_en"), f'{v["h"]} 缺 layer_en'
    got = {v["layer_zh"] for v in data["vocab"]}
    assert got == LAYERS, f"五层未全出现: {got}"


def test_vocab_layer_badges_and_filter():
    data = json.loads(bl.read(DATA_JA))
    html = bl.vocab_html(data)
    # 每行带 data-layer 锚 + 徽章
    assert html.count('data-layer="') >= 46
    assert html.count('class="lyr-badge"') == 46 * 2  # 双语
    # 层筛选工具条：全部 + 五层
    assert 'class="layer-bar"' in html
    assert html.count('class="lyr-btn') == 6
    for L in LAYERS:
        assert f'data-layer="{L}"' in html
    # 分层列表头
    assert "分层 / Layer" in html


def test_cultural_rows_have_layer_and_anchor():
    data = json.loads(bl.read(DATA_JA))
    html = bl.cultural_html(data)
    assert html.count('data-layer="') >= 46
    assert 'class="layer-bar"' in html
    assert "分层 Layer" in html


def test_module_data_blocks_gojuon():
    module = {"id": "gojuon", "status": "ready"}
    blocks = bl.module_data_blocks("ja", module)
    # 螺旋六视图：引导 + 五旋（形/词/义/源/律）+ 回望收束（返回 HTML 字符串片段）
    assert len(blocks) == 6
    # 各旋视图块以 class 标识离弦：guide / shape / word / sense / root / law
    markers = ["spiral-guide", "ring-shape", "ring-word", "ring-sense", "ring-root", "ring-law"]
    for i, m in enumerate(markers):
        assert m in blocks[i], f"block[{i}] 应含 {m}"
    joint = "".join(blocks)
    # 形环 五十音表 + 词环 gloss + 义环 文化 + 源环 字源 + 律环 音律 + 收束
    assert "五十音" in joint and "か" in joint
    assert "gloss" in joint.lower() and "あめ" in joint
    assert "季語" in joint.lower() and "美学" in joint.lower() and "典故" in joint
    assert "pitch-svg" in joint and "最小对立对" in joint


def test_module_data_blocks_missing_json_empty():
    assert bl.module_data_blocks("ja", {"id": "kanji"}) == []


def test_four_ring_linkage_anchors():
    module = {"id": "gojuon", "status": "ready"}
    blocks = bl.module_data_blocks("ja", module)
    shape, word, sense, root = blocks[1], blocks[2], blocks[3], blocks[4]
    # 每盘行/格以假名 h 为联动锚
    assert shape.count('data-h="') >= 46          # 五十音格
    assert word.count('data-h="') >= 46           # 词环行 + 句朗读盘
    assert sense.count('data-h="') >= 46          # 义环行
    assert root.count('data-h="') >= 46           # 源环行
    # 同键跨盘：あ 在四盘均可定位
    for blk in (shape, word, sense, root):
        assert 'data-h="\u3042"' in blk, "四盘应共享 あ 锚"
    # 行级 data-h 落在 <tr> 上（词/义/源环）
    assert '<tr data-h="\u3042"' in word or '<tr data-h="\u3042"' in sense


def test_origin_rows_carry_anchor():
    data = json.loads(bl.read(DATA_JA))
    html = bl.origin_html(data)
    assert html.count('data-h="') >= 46
    assert '<tr data-h="\u3042"' in html


def test_kana_index_json_covers_all():
    data = json.loads(bl.read(DATA_JA))
    html = bl.kana_index_html(data)
    assert 'id="kana-index"' in html and 'type="application/json"' in html
    payload = html.split(">", 1)[1].rsplit("</script>", 1)[0]
    idx = json.loads(payload)
    assert idx["\u3042"].get("r") == "a"
    assert idx["\u3042"].get("kat")
    for v in data["vocab"]:
        d = idx.get(v["h"])
        assert d, f'{v["h"]} 缺聚合索引'
        assert d.get("sent") == v["sent"]
        assert d.get("kana") == v["kana"]
        assert d.get("layer_zh") == v["layer_zh"]


def test_vocab_and_cultural_word_play_buttons():
    data = json.loads(bl.read(DATA_JA))
    vh = bl.vocab_html(data)
    ch = bl.cultural_html(data)
    assert vh.count('class="word-play"') == 46
    assert ch.count('class="word-play"') == 46
    # 发音目标为词的假名读音（雨 → あめ）
    assert 'class="word-play" data-say="\u3042\u3081"' in vh


def test_modal_mandala_markup_and_js():
    html = bl.page("css/learning.css", "../../index.html", "Home",
                   "t", "lang-zh", "", "")
    # 聚合图弹窗骨架：中心 + 四枝 + 连线层
    assert 'id="kana-modal"' in html
    assert 'id="km-stage"' in html
    assert 'id="km-lines"' in html
    assert 'id="km-center"' in html
    assert html.count('data-sat="') >= 5
    for k in ("shape", "word", "sense", "root", "law"):
        assert f'data-sat="{k}"' in html
    # 弹窗逻辑：开启/关闭/连线/发音
    assert "openKanaModal" in html
    assert "closeKanaModal" in html
    assert "drawKmLines" in html
    assert "km-play" in html
    # 点击不再跳转（原 ringLink 自动滚动逻辑已移除），改为打开聚合图
    assert "r.bottom > window.innerHeight" not in html
    assert "window.openKanaModal(h)" in html


def test_page_js_voice_and_linkage():
    html = bl.page("css/learning.css", "../../index.html", "Home",
                   "t", "lang-zh", "", "")
    # 批A：全局声线下拉 + 本地声线优先 + 记忆 + 失败降级
    assert 'id="voice-picker"' in html
    assert "localService" in html
    assert "ls-jp-voice" in html
    assert "kanaVoiceScore" in html
    assert "onerror" in html                 # 失败自动换声线
    assert "speaking" in html                # 仅在播放中才 cancel
    # 单假名重复一次补时长；只念假名，不拼罗马音（拉丁字母会被读成外语）
    assert "text + '\u3001' + text" in html
    assert "'\u3001' + r" not in html
    # 批B：四盘联动 + 单旋聚焦 + Esc 退出
    assert "ringLink" in html
    assert "ring-hit" in html
    assert "ring-focus" in html
    assert "Escape" in html


# ── 第五旋·律 + 螺旋导图 + 媒体 ─────────────────────────────────
def test_mora_split_rules():
    assert bl.mora_split("おおさか") == ["お", "お", "さ", "か"]
    assert bl.mora_split("きって") == ["き", "っ", "て"]
    assert bl.mora_split("きゃ") == ["きゃ"]
    assert bl.mora_split("コーヒー") == ["コ", "ー", "ヒ", "ー"]
    assert len(bl.mora_split("きゃく")) == 2


def test_prosody_data_and_markup():
    data = json.loads(bl.read(DATA_JA))
    p = data["prosody"]
    assert len(p["accent_types"]) == 4
    assert [t["num"] for t in p["accent_types"]] == [0, 1, 2, 3]
    assert [t["seq"] for t in p["accent_types"]] == ["LHHH", "HLLL", "LHLL", "LHHL"]
    assert len(p["minimal_pairs"]) >= 4
    html = bl.prosody_html(data)
    assert html.count("pitch-svg") == 4
    assert 'id="pitch"' in html
    assert "最小对立对" in html and "特殊拍" in html
    # 音调最小对必须带出处（逐词音调不臆断）
    pitch_pairs = [m for m in p["minimal_pairs"] if m["kind"] == "pitch"]
    assert pitch_pairs and all(m.get("src") for m in pitch_pairs)


def test_prosody_in_ring_law_block():
    blocks = bl.module_data_blocks("ja", {"id": "gojuon", "status": "ready"})
    law = blocks[5]
    assert "ring-law" in law and "pitch-svg" in law
    assert "retro" in law              # 律旋回首内观
    assert "spiral-closure" in law     # 终点回望起点收束


def test_mindmap_tree_and_retro():
    data = json.loads(bl.read(DATA_JA))
    mm = bl.mindmap_html(data)
    assert 'id="mindmap"' in mm
    assert mm.count('class="mm-ring"') == 5
    assert mm.count('class="mm-trunk"') == 5
    assert "mm-leaf" in mm and 'data-h="\u3042"' in mm
    assert "mm-reverse" in mm and "mm-beats" in mm
    assert "mindmap" in bl.spiral_guide_html(data)
    # 回望面板：词/义/源/律 各指向上一旋
    for sid in ("word", "sense", "root", "law"):
        back = data["backrefs"][sid]["back"]
        assert f'href="#ring-{back}"' in bl.retro_html(sid, data)
    # shape 的回望写在收束里（终点回望起点）
    assert bl.retro_html("shape", data) == ""
    assert data["backrefs"]["shape"]["zh"] in bl.spiral_closure_html(data)


def test_media_embeds_and_links():
    data = json.loads(bl.read(DATA_JA))
    md = data["media"]
    assert md["video"]["id"]
    assert len(md["read"]) >= 6
    html = bl.media_html(data)
    assert "youtube-nocookie.com/embed/" in html
    assert "Special:FilePath/" in html
    assert html.count('class="read-card"') == len(md["read"])
    for r in md["read"]:
        assert r["url"].startswith("https://")


def test_page_js_beat_overlay_and_rate():
    html = bl.page("css/learning.css", "../../index.html", "Home", "t", "lang-zh", "", "")
    assert "moraSplit" in html
    assert "function beats(" in html
    assert "show-beats" in html
    assert "mm-reverse" in html
    assert "data-rate" in html


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