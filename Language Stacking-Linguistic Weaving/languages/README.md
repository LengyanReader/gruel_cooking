---json
{
  "languages": [
    {
      "id": "ja", "glyph": "日本語", "name_zh": "日本語", "name_en": "Japanese",
      "iso": "ja · Japonic", "status": "active", "href": "ja/",
      "summary_zh": "汉字+假名 · 助词框定 · 以心传心",
      "summary_en": "kanji + kana · particle-framed · heart-to-heart"
    },
    {
      "id": "zh", "glyph": "中文", "name_zh": "中文", "name_en": "Chinese",
      "iso": "zh · Sino-Tibetan", "status": "planned",
      "summary_zh": "意合 · 声调 · 字孕义",
      "summary_en": "paratactic · tonal · meaning lives in the glyph"
    },
    {
      "id": "en", "glyph": "English", "name_zh": "英语", "name_en": "English",
      "iso": "en · Germanic", "status": "planned",
      "summary_zh": "名词化 · 双宾 · 时体",
      "summary_en": "nominalization · two objects · tense-aspect"
    },
    {
      "id": "fr", "glyph": "Français", "name_zh": "法语", "name_en": "French",
      "iso": "fr · Romance", "status": "planned",
      "summary_zh": "同音异形 · 联诵 · 心之理由",
      "summary_en": "homophones · liaison · the reasons of the heart"
    },
    {
      "id": "sa", "glyph": "संस्कृतम्", "name_zh": "梵语", "name_en": "Sanskrit",
      "iso": "sa · Indo-Aryan", "status": "planned",
      "summary_zh": "天城体 · sandhi · 语近数学",
      "summary_en": "Devanagari · sandhi · grammar as mathematics"
    },
    {
      "id": "la", "glyph": "Latina", "name_zh": "拉丁语", "name_en": "Latin",
      "iso": "la · Italic", "status": "planned",
      "summary_zh": "屈折完备 · 词序自由 · 格言浓缩",
      "summary_en": "full inflection · free order · condensed mottoes"
    },
    {
      "id": "de", "glyph": "Deutsch", "name_zh": "德语", "name_en": "German",
      "iso": "de · Germanic", "status": "planned",
      "summary_zh": "复合长词 · 句框 · 构式规整",
      "summary_en": "long compounds · sentence frame · orderly construction"
    },
    {
      "id": "sv", "glyph": "Svenska", "name_zh": "瑞典语", "name_en": "Swedish",
      "iso": "sv · North Germanic", "status": "planned",
      "summary_zh": "双性 · 词调 · 清音",
      "summary_en": "two genders · word tone · clear vowels"
    }
  ]
}
---
# 语种基础学习库 · Language Learning

<!-- zh -->
这是**语言叠织**下属的「各语种基础学习」知识库。每门语言一个子目录（`ja/`、`fr/`……）：prose 固化知识以 markdown 存放（文字体系、发音要点、学习路径），结构化数据（音图、词表）以 JSON 存放于 `data/`。二者共同构成**单一来源**，网页由生成器统一产出——不硬编码、不复制。站点层级：学习库 → 语言 → 模块（如 日语 → 五十音）。
<!-- en -->
This is the per-language **Learning** knowledge base under Language Stacking. Each language lives in its own folder (ja/, fr/, …): consolidated knowledge as markdown (writing systems, pronunciation, learning path), structured datasets (sound charts, word lists) as JSON under data/. Together they form the single source of truth; the web pages are generated — no hardcoding, no duplication. Site hierarchy: Learning → Language → Module (e.g. Japanese → Gojūon).

## 铁律 / Iron Rules

<!-- zh -->
1. **单一来源**：prose 存 markdown，结构化数据存 JSON；网页一律由生成器产出。
2. **记 → 读 → 写**：语音先于文字，听见比看见先行。
3. **锚点织法**：月・水・心・和……与核心术语表互为镜像，一物多名，名为镜。
4. **审校防线**：AI 起草一律标注；正式语料前必须母语审校（绝不静默出错）。
5. **数据层**：sqlite 查询库随构建生成（索引 / 复习 / 检索）；neo4j 图谱（跨语概念织网，`export_neo4j.py` 导出 Cypher，`weave_query.py` 提供「一词万境」无服务器读路径）阶段二已验收。
<!-- en -->
1. Single source: prose in markdown, structured data in JSON; pages are generated.
2. Listen → read → write: sound before glyph.
3. Anchor weaving: moon, water, heart, harmony … mirror the core glossary; many names, one mirror.
4. Review shield: AI-drafted material is always marked; native review before it enters the formal corpus.
5. Data layer: sqlite query index is generated with the build (search / review / retrieval); the neo4j graph (cross-language concept weaving, exported as Cypher by export_neo4j.py, served read-only by weave_query.py's "one word, many worlds") is phase-two verified.

## 产出 / Outputs

| 生成物 | 位置 | 说明 |
| --- | --- | --- |
| 学习库页面 | `docs/language_stacking/learning/` | 由生成器从本目录 md/json 构建（hub / 语种 / 模块 / **织网库 glossary**）（提交 git） |
| sqlite 索引 | `data/learning.db` | 注册表 + 模块 + 音图(chart_cells，含拨音ん) + 词表(vocab) + **织网库(concepts/concept_terms/scripts/threads)**，随构建同步（不入 git） |
| neo4j 图谱 | `data/neo4j_load.cypher` | 阶段二跨语概念织网的 Cypher 导入脚本（`export_neo4j.py` 产出，不入 git）；schema 见 `docs/neo4j_schema.md` |
| Core Glossary | `data/core_glossary.json` | 附录 D 概念 × 八语术语表第一批校准源（12 概念 × 8 语 + scripts + 织线），词位标 `review pending` |

## 织网库查询 / Weave Query（一词万境）

```bash
python "Language Stacking-Linguistic Weaving/web/weave_query.py" list            # 全部权威概念（含 probe 标记）
python "Language Stacking-Linguistic Weaving/web/weave_query.py" concept water    # 一词万境：八语词位 + 挂接词条 + 织线
python "Language Stacking-Linguistic Weaving/web/weave_query.py" concept water --cypher   # 等同的 neo4j 查询
python "Language Stacking-Linguistic Weaving/web/weave_query.py" script           # 文字体系 × 语言
python "Language Stacking-Linguistic Weaving/web/weave_query.py" thread           # 词源/借词织线
python "Language Stacking-Linguistic Weaving/web/weave_query.py" sound ja き      # 音图邻居
```

## 构建与测试 / Build & Test

运行构建（测试环境 `conda activate hy_py312`，仅依赖 `markdown` 包，可 `pip install -r web/requirements.txt`）：

```bash
conda activate hy_py312
python "Language Stacking-Linguistic Weaving/web/build_learning.py"          # 生成静态页
python "Language Stacking-Linguistic Weaving/web/build_learning.py" --validate  # 知识源校验
python "Language Stacking-Linguistic Weaving/web/build_learning.py" --db        # sqlite 全量索引
python "Language Stacking-Linguistic Weaving/web/build_learning.py" --check     # 源校验+产物校验(含陈旧产物)
python "Language Stacking-Linguistic Weaving/web/export_neo4j.py"            # neo4j 阶段二 Cypher 导出
```

测试套件（`web/tests/`，pytest）：

```bash
python -m pytest "Language Stacking-Linguistic Weaving/web/tests" -q
```

一键验收（Windows 主机，含 [1/4]校验+构建+索引 [2/4]Cypher 导出 [3/4]pytest [4/4]汇总）：

```powershell
powershell -ExecutionPolicy Bypass -File "Language Stacking-Linguistic Weaving/web/run_tests.ps1"
```

CI：`.github/workflows/learning-ci.yml` 在 `Language Stacking-Linguistic Weaving/**` 或 `docs/language_stacking/**` 变更时跑同一套校验，并强制**改源即重建提交产物**（页面与源不一致则失败）。

**纪律**：新建语种/模块 = ① 注册表/README frontmatter 登记 → ② 写 `{lang}/*.md` prose 与 `data/{lang}/*.json` → ③ 跑 `--validate --db --check` + pytest；**绝不直接编辑 `docs/language_stacking/learning/` 产物**。