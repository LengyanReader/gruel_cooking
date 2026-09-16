# neo4j 阶段二 —— 跨语概念图谱 Schema

> 目标：把「语言叠织」织成一张可查询的图——同一个概念如何被八语说、词与词如何同源/互借、就是图里的可达关系。阶段一从 sqlite 学习库索引导出；阶段二以附录 D Core Glossary（`core_glossary.json`）校准概念节点。**状态：阶段二是图模型已全部实现并在 neo4j 5 实测验收。**

## 1. 数据流

```
languages/** (单一来源)
   │  build_learning.py --db
   ▼
languages/data/learning.db (sqlite: languages/modules/chart_cells/vocab/concepts/concept_terms/scripts/threads)
   │  export_neo4j.py
   ▼
languages/data/neo4j_load.cypher   ──(docker cypher-shell -f )──►  neo4j
   │  weave_query.py (无服务器读路径，供日常快速查询/SQLite 兜底)
```

本地验收（已实测，Docker Desktop v29.6.2 / neo4j:5-community）：

```bash
docker run -d --name ls-neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/<pass> neo4j:5-community
docker cp "Language Stacking-Linguistic Weaving/languages/data/neo4j_load.cypher" ls-neo4j:/tmp/neo4j_load.cypher
docker exec ls-neo4j cypher-shell -u neo4j -p <pass> -f /tmp/neo4j_load.cypher
```

**语句封装**：每条语句包进 `CALL { ... } IN TRANSACTIONS;`（`cstmt` 生成）——三个作用一座桥：① neo4j 5 cypher-shell 脚本模式按文件共享变量作用域，同名变量（l/m/w…）会报 "Variable already declared"，封装后逐条独立作用域；② 逐条独立提交；③ 保留 MERGE 幂等语义。全部为 `MERGE + SET`，重复导入实测不产生重复节点。

## 2. 节点 Node Types

| Label | Merge 主键 | 属性 | 来源 | 数量(实测) |
|---|---|---|---|---|
| `Language` | `id` | glyph, name_zh, name_en, iso, status | registry | 8 |
| `Module` | `(lang, id)` | name_zh, name_en, status | `{lang}/README.md` modules | 4 |
| `Sound` | `(lang, module, row, col)` | hira, kata, roma, note(空/void/particle) | `data/{lang}/{m}.json` chart | 51 |
| `Word` | `(lang, module, id)` | hira, kata, roma, kanji, kana, meaning_zh, meaning_en | 同词表 | 46 |
| `Concept` | `key` | probe(true=自动聚合待校准, false=权威), name_zh, name_en | **Core Glossary（权威）** + meaning_en 探针 | 53（12 校准 + 41 探针） |
| `Term` | `key="<lang>:<concept>"` | lang, concept, word, roma | Core Glossary 八语词位 | 96（12 概念 × 8 语） |
| `Script` | `id` | name_zh, name_en, note_zh, note_en | Core Glossary scripts | 4 |
| `Root` | `id` | （词根节点，形如 pie-wedor） | Core Glossary threads 引用的 root:* | 3 |

## 3. 关系 Relationship Types

| 关系 | 起 → 止 | 语义 | 数量(实测) |
|---|---|---|---|
| `HAS_MODULE` | Language → Module | 这门语言有这个学习模块 | 4 |
| `HAS_SOUND` | Module → Sound | 模块的音图单元 | 51 |
| `HAS_WORD` | Module → Word | 模块的词条 | 46 |
| `EXPRESSES` | Term/Word → Concept | 词位/词条表达此概念——**跨语织网的枢纽** | 142（96+46） |
| `WRITES_IN` | Language → Script | 这门语言用此文字体系 | 9 |
| `DERIVES_FROM` | Term/Root → Term/Root | 词源同根/沿革 | 7 |
| `LOANED_TO` | Term → Term | 借词回旋镖 | 2 |
| `TRANSLATES` | Term ↔ Term | 镜像对（预留，当前无数据） | 0 |

## 4. 织网查询样例 Query Recipes

「同一个概念，八语怎么说」——**一词万境**（概念权威 Term）：

```cypher
MATCH (c:Concept {key:'water'})<-[:EXPRESSES]-(t:Term)
RETURN t.lang, t.word, t.roma ORDER BY t.lang;
```

「水」的词源织线（含词根）：

```cypher
MATCH (t:Term {concept:'water'})-[r:DERIVES_FROM]->(dest)
RETURN t.lang, t.word, type(r), coalesce(dest.id, dest.concept) AS target;
```

「茶」的借词回旋镖（汉字圈东传 + 海运西传）：

```cypher
MATCH (z:Term {key:'zh:tea'})-[r:LOANED_TO]->(t)
RETURN type(r), r.note_en, t.key;
```

「某个音的矩阵邻居」（五十音坐标系）:

```cypher
MATCH (s1:Sound {lang:'ja', row:'か'})--(:Module)--(s2:Sound)
RETURN s2.row, s2.col, s2.roma ORDER BY s2.row, s2.col;
```

命令行读路径（无需 neo4j 服务器，读 learning.db，实测）：

```bash
python "Language Stacking-Linguistic Weaving/web/weave_query.py" list
python "Language Stacking-Linguistic Weaving/web/weave_query.py" concept water
python "Language Stacking-Linguistic Weaving/web/weave_query.py" concept water --cypher
python "Language Stacking-Linguistic Weaving/web/weave_query.py" script
python "Language Stacking-Linguistic Weaving/web/weave_query.py" thread
python "Language Stacking-Linguistic Weaving/web/weave_query.py" sound ja き
```

## 5. 阶段二状态（已实现）

1. **概念收敛** ✅：Core Glossary 为权威，`probe=false`；学习库 meaning_en 语义未落入权威表的自动聚合为 `probe=true`（当前 41 个），导出器在文件头注释列出待校准列表，人工复核后进 `core_glossary.json` 即转为正式。
2. **词源织线** ✅：`Term/Root` 节点 + `DERIVES_FROM / LOANED_TO / TRANSLATES`（幂等 MERGE 带双语 note 属性）；织线数据在 `core_glossary.json` threads，向导出的机制为 sqlite `threads` 表。
3. **Script 节点** ✅：`Script`（Hanzi/Kana/Latin/Devanagari）+ `Language-[:WRITES_IN]->Script`，支撑「文字的三种命运」「借词回旋镖」专题查询。
4. **查询型学习交互** ✅：`weave_query.py` 提供「一词万境」推荐（同概念八语词 + 词源链）读路径。

> **纪律**：概念节点的权威在 Glossary，不在 meaning_en 探针；探针组只作线索，入正式语料必须人工核（对齐「绝不静默出错」铁律 3）。当前 12 概念 × 8 语词位全部标记 `review pending`，待母语审校后移除标记批量转正。