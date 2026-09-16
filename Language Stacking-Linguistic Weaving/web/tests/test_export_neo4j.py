# -*- coding: utf-8 -*-
"""neo4j 阶段二导出器 test_export_neo4j 的测试。"""
import os

import export_neo4j as ex

import build_learning as bl


def _tmp_db(tmp_path):
    """以真实源生成临时 learning.db，返回 db 路径与预期计数。"""
    registry, _ = bl.load_registry()
    meta, _ = bl.parse_frontmatter(bl.read(os.path.join(bl.LANG, "ja", "README.md")))
    db_path = str(tmp_path / "learning.db")
    bl.sync_sqlite(registry, {"ja": meta.get("modules", [])}, db_path=db_path)
    return db_path


def test_cypher_escape():
    assert ex.cypher_escape('He said "hi" \\ ok') == 'He said \\"hi\\" \\\\ ok'


def test_concept_key_normalization():
    assert ex.concept_key("Rain!") == "rain"
    assert ex.concept_key("Every-day Life") == "everyday life"
    assert ex.concept_key("???") == ""


def test_export_cypher_counts(tmp_path):
    db_path = _tmp_db(tmp_path)
    text = ex.export_cypher(db_path)
    counts, rels = ex.summarize(text)

    assert counts["Language"] == 8
    assert counts["Module"] == 4
    assert counts["Sound"] == 51
    assert counts["Word"] == 46
    assert counts["Term"] == 96          # 12 概念 × 8 语
    assert counts["Script"] == 4
    assert counts["Root"] == 3
    # 12 校准概念 + (46 学习库语义 key − 5 已覆盖) 探针
    assert counts["Concept"] == 53
    assert text.count("SET k.probe=false") == 12
    assert text.count("SET k.probe=true") == 41
    assert rels["HAS_MODULE"] == 4
    assert rels["HAS_SOUND"] == 51
    assert rels["HAS_WORD"] == 46
    assert rels["WRITES_IN"] == 9
    assert rels["EXPRESSES"] == 96 + 46  # Term + Word
    assert rels["DERIVES_FROM"] == 7
    assert rels["LOANED_TO"] == 2
    assert rels["TRANSLATES"] == 0


def test_export_cypher_deterministic(tmp_path):
    db_path = _tmp_db(tmp_path)
    assert ex.export_cypher(db_path) == ex.export_cypher(db_path)


def test_export_cypher_idempotent_merge(tmp_path):
    db_path = _tmp_db(tmp_path)
    text = ex.export_cypher(db_path)
    # 每条 MERGE 提供唯一主键，且带 SET —— 可重复导入不产生重复节点
    assert "MERGE (w:Word {lang:" in text
    assert "w.meaning_en=\"" in text
    assert "CREATE " not in text.replace("CREATE INDEX", "")


def test_export_cypher_special_sound(tmp_path):
    db_path = _tmp_db(tmp_path)
    text = ex.export_cypher(db_path)
    # を particle 单元 (wa 行 col 4)
    assert 'row: "わ", col: 4}' in text
    assert 's.note="particle"' in text
    # 特殊音节与拨音ん
    assert 's.roma="shi"' in text
    assert 's.roma="chi"' in text
    assert 's.roma="tsu"' in text
    assert 's.roma="fu"' in text
    assert 'row: "n", col: 0}' in text