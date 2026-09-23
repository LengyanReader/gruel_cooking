# 织桥设计 · Weave Bridge — Reading & IA ↔ Language Stacking

`2026-09-23` · 设计文档（design only，未实现）· 关联域：`Reading_IA/` ↔ `Language Stacking-Linguistic Weaving/`

> 目的：让两个域互相引用、彼此辅助——Reading_IA 的内容涉及多文化多语言，Language Stacking 是仓库里唯一的跨语概念权威。用**稳定概念 id** 做桥：书/作者/思潮档案引用概念（借词佐证阅读），概念获得作品侧证（活例赋形）。

---

## 1. 目标 Goals

1. **藏经者</>点灯人**：Reading_IA 的每张卡（书目/作者/思潮档案/简报）可以带 1–3 个语言叠织概念 id——同一心象，在别国语里怎么说，是阅读的旁注。
2. **反向回报**：Language Stacking 的概念获得「作品侧证」——当月读什么、此刻思潮映在哪个概念上，glossary 卡可见。
3. **安全落地**：不改两域的底层契约；设计分两档，P0 在 Reading 侧零风险先跑，P1 再动 LS 生成器（守其 CI 纪律）。

## 2. 桥的核心约定 The bridge contract

| 约定 | 内容 |
|---|---|
| 概念权威唯一 | 只引用 `languages/data/core_glossary.json` 中 `probe=false` 的**权威概念**（当前 12 个：water·水, moon·月, heart·心, time·时, sea·海, freedom·自由, tea·茶, silence·静, tree·树, wind·风, light·光, nature·自然）；`probe=true` 探针概念不得出现在正式卡上。 |
| 小且显式 | 每张卡 ≤3 条织线；每条一行「为何」。少而够用，超出即修剪（对齐 principles 9）。 |
| 双向可溯源 | 正向（卡→概念）在 `weave_ties.md`；反向（概念→卡）由同一文件兼任索引，或由 LS `refs` 显式落一份（P1）。 |
| 双语默认 | 织线「为何」与 chips 文案中英并列；引用 ONLY 原概念 id（不下叉语词位，词位只作文案参考）。 |
| 草拟必标注 | 织线由 AI 起草时标注；正式入库前人工复核（principles 6 / LS 铁律 4）。 |

## 3. 方向 A — Reading → LS（carrier → concept）

### 3.1 卡片新字段 `weave 织线`
书目卡/作者卡/思潮档案/简报模板追加：

```markdown
- **weave 织线**: `water` — 一点一滴之水，成了虚假的延命；水是咽喉也是开关
  `time` — 将「不健康寿命」压缩向零，即对时间主权的练习
```

约定：每条 = 概念 id（反引号）+ 破折号 + 一句中英皆可的「为何」（至少一语言）。id 必须存在于 `core_glossary.json` 权威集；写卡时用 `weave_query.py concept <key>` 可现查八语词位作旁注素材。

### 3.2 新边表 `readings/relations/weave_ties.md`
沿用既有边表格式，新增边型 `❋ weave-tie`（卡 ⇔ 概念）：

```markdown
## `❋` weave-tie 织线（book/category/theme ⇔ LS concept）

| from | to (concept id) | why 一句理由 | date | confidence |
|---|---|---|---|---|
| [[library/2026-manda-kanoke-made]] | `water` | 点滴=水作虚假延命；反写「生命之泉」 | 2026-09-23 | strong |
```

- 只放权威概念 id（`ls:concept:<key>` 亦可作链接写法）。
- `confidence` 沿用 ✓/○/◐ 简表；卡为本域事实、概念归属为判断，故一般为 `strong/medium`。
- 本表行数超 ~200 时并入生成图（同一阶段升级）。

### 3.3 网页呈现（P0 范围，Reading 侧）
- 书卡/作者卡/档案卡渲染「织线 ❋」chips，文案 `概念名（名）→ 八语怎么说`。
- 链接目标分两态：
  - 若 LS glossary 页已有概念锚点（P1 后）：`docs/language_stacking/learning/glossary/#<key>`
  - 未完成 P1 前：退化为整页 `docs/language_stacking/learning/glossary/`（无深链，不加假锚）。
- chips 旁可附该概念在本卡语言中的词位（如 Mandel=en `freedom/liberté/自由/jiyū/…`），只作文案，不作数据。

## 4. 方向 B — LS → Reading（concept → carrier）

### 4.1 P0 · 反向索引（零 LS 改动）
`weave_ties.md` 即反向索引：`directory_refs` 满足「概念的活例在哪」的查询。另在 Reading 侧存一份归属速查（本节 `## 6` 的表即其骨架），避免未来在 LS 侧重复维护。

### 4.2 P1 · LS 生成器增强（可选，守 CI）
目标：glossary 卡上可见「作品侧证」，且支持深链锚点。

**a) 数据** `core_glossary.json` 概念节点增可选字段：

```json
{ "id": "water",
  "refs": [
    {"kind": "reading", "id": "2026-manda-kanoke-made",
     "why_zh": "点滴=水作虚假延命", "why_en": "the drip as false life-support"}
  ] }
```

**b) 生成器** `web/build_learning.py`：
- `render_glossary_page()`：`wcard` 增 `id="<concept>"` 锚点（深链基础）。
- 渲染 `refs` 为「作品侧证 / read in」chips，链接到 `docs/reading_ia/…`。
- `validate_glossary()`：新增规则——`refs.kind` 合法、`id` 非空、（可选）指向的 Reading_IA 卡存在。

**c) 纪律**：改源后必须 `--validate --db --check` + `pytest` + 重建提交产物；CI（`learning-ci.yml`）强制源出同步。**不满足即不并库。**

## 5. 试点映射 Pilot mapping（2026-09-23 现有内容）

| 卡 | 概念 id | 为何 why |
|---|---|---|
| [[library/2026-mandel-exit-party]] | `freedom` | 两个美国：混乱共和国 vs 极权联合国——共和国的两种自由病 / two Americas, two failures of freedom |
| [[library/2026-vargas-une-unique-lueur]] | `light` | 「lueur」一束微光即谜面；Nerval 与白考尔形象的辉光 / a single glimmer as the enigma's engine |
| [[library/2026-lemaitre-belles-promesses]] | `time` | 1963–64 光荣年代的账单，时代的资产负债表 / the glory years' bill, time's ledger |
| [[library/2026-pelicot-joie-de-vivre]] | `heart` | joie de vivre：夺回主体之心，羞耻易边 / joy of living, the reclaimed heart |
| [[library/2026-manda-kanoke-made]] | `water` · `time` | 点滴=水作虚假延命；压缩不健康寿命 = 时间主权的练习 / the drip as false life-support; pressing unhealthy life toward zero |
| [[moment-series-year-2026]]（年度档案） | `sea` · `water` · `time` | 霍尔木兹咽喉·海水淡化·油污；秋分之「日中则昃」/ the throat of the sea, desalination, the equinox turning |

> 注：`nature`（Manda 的「自然死」）、`silence`（Lemaitre 的「沉默的共谋」、Vargas 的寂静）等为可替换候选，勿一次性堆砌；小且显式为上。

## 6. 治理与校验 Governance

1. 概念 id 白名单 = `core_glossary.json` 权威集（probe=false）；校验脚本可读该 JSON 对照（沿用 Reading_IA「以测为准」原则 16）。
2. 织线添加走 W1/W3 流程：卡建立时同步写 `weave_ties.md` 一行；carrier 进入 moment 档案时同步更新映射表。
3. 修剪：每月随 leads 修剪，概念与卡的对应超过 3 条即拆或弃。
4. 双语：chips 与「为何」至少一语言；引用词位需先用 `weave_query.py` 现查，不凭记忆。

## 7. 风险与未决 Open questions

1. **深链依赖 P1**：P0 阶段 glossary 无锚点，网页只能链整页；若想先有深链体验需提前 4.2-b。
2. **LS 侧 refs 审校**：`refs` 落在 LS 正式语料内，须过母语/人工审（LS 铁律 4），不能由本域单方面写死。
3. **跨域 diff 纪律**：P1 会同时触碰两个 `docs/` 产物，提交流须遵循两域各自的 hygiene（`_final_ok.ps1` 精神）。
4. **概念是否够用**：12 个权威概念对文学/思潮可能偏窄；后续可向 LS 提「转正探针概念」需求，而非在本域自造关键字（守住单一来源）。

---

*本文档是设计意向，非实现；落地顺序建议：P0（Reading 侧字段+边表+网页 chips）→ 用户验收 → P1（LS 生成器增强）。*
<!-- AI-drafted 草拟标注：2026-09-23 opencode；实现前需人工复核概念映射与「为何」文案。 -->