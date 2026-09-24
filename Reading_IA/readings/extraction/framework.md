# 内容提取框架 · Extraction Framework

**唯一权威** for Reading & IA intake. Decode a material into a card with full fidelity.
Five lossless guarantees (无损五维) apply to **every** kind; kind-specific lens stacks below.

本文件是 Reading & IA 内容提取的唯一权威。五种无损保证适用于一切读物类型；分型透镜堆栈见 §3。

> 溯源：方法学来自学术 close-reading 传统（Sinykin & Winant 2025 五步法）、网文拆解工业流水线
> （story-short-analyze 的语义边界节点 + 数值门槛）、记忆研究/叙事医学（Charon 2006、Gornick 2007）、
> 论证结构（CER: Claim-Evidence-Reasoning），逐条见文档末尾来源。
> 本框架是这些方法在**双语资料库/书目卡片**场景的落地，非照搬。

---

## 1 · 无损五维 Five Lossless Guarantees

| 维度 | 定义 | 失败信号 | 守门机制 |
|---|---|---|---|
| **信息无损** | 每个事实主张都能指到证据（原文/一手源） | 转述无出处、二手当一手 | 每条必带 source + conf（✓◐○✗）；fact/plot 分流 |
| **内容无损** | 关键段落保留原文引句（✓ 原文/✗ 直觉） | 只写概述不引原文 | 引句≤300字直引；双语互译对应；见 §4 |
| **深度无损** | 每个透镜层都做到阈值，不做表面概括 | 只写「plot」不写「novel 的 plot」 | 分型堆栈 + ledger 逐层验账，`audit.py` 挡接 |
| **结构无损** | 保留原文的叙事时序/论证顺序/章节骨架 | 时间线被摊平、论证被压缩成一句 | Skeleton(骨架) 层强制记录 Act/Part/chapter + POV + 时间线 |
| **证据无损** | 反驳/争议/失败也保留，不粉饰 | 一片叫好，反对意见缺失 | 每卡 ≥1 个 disagreement/echo（铁律 10）；详见 §7 |

守恒律：**提取 = 无损变换，不是有损压缩**。任何一句概括都必须能在 原文/证据 处复原。

---

## 2 · 分型路由 Kind Router

入卡第一问：这是哪种材料？**不同读物 → 不同透镜堆栈**，照搬别的类型的剧本是深度无损的头号杀手。

| kind | 判定 | 透镜 | 出厂档案（产物） |
|---|---|---|---|
| `novel` | 虚构叙事（长篇/短篇均可） | prompts/novel.md | 骨架+节点+人物网络+手法+母题+意图+引用 |
| `memoir` | 第一人称真实生活/证词 | prompts/memoir.md | 事件-情感双时间线+转折+证词伦理+回响 |
| `essay` | 论证/非虚构（社科医学科技） | prompts/essay.md | 论点+主张账本+证据/反证+数字复核+争议 |
| `generic` | 非以上（film/poetry/paper…） | prompts/generic.md | 骨架+关键概念+论点/证据+引句 |
| `unclear` | 混合/跨界 → 问「主导模态是什么」 | 取主模态 | 若真混判，双透镜并给主线 |

规则：一本书若同时是 memoir+essay（如《野兽与野兽》），取**主导模态**为 kind，其余模态作为
「副透镜」在骨架层之后追加，不摊平主线。

---

## 3 · 分型透镜堆栈 Lens Stacks

每一层都是**必做的提取动作**，不是可选项。各层阈值聚合进 §4 的 ledger，由 `audit.py` 验。

### 3.1 novel 小说（prompts/novel.md）

| # | 层 | 提取动作 | 阈值/形态 |
|---|---|---|---|
| L1 | 出版与读态 | 版本/ISBN/页码 ✓；read_status 诚实标注 | 全 metadata ✓ 级 |
| L2 | 骨架 Skeleton | 分 Part/Act/chapter，每段 1–2 行 + 页码区间；POV（谁在看）+ 人称时态 + 叙事时序（线性/倒叙/双线） | ≥3 段 |
| L3 | 情节节点 Plot nodes | 以**语义变化**为界：风险/信息/关系/资源/决定/读者理解变化点时记一个节点；不按字数配额拆 | ≥8 节点，每节点 情绪标记 -9..+9 |
| L4 | 人物组 Character system | 有名人物全部提取（100% 覆盖）：id/name/group/role + conf ✓ | 全人物；人物关系边 chaedgedges ≥5 |
| L5 | 母题簇 Motif clusters | 母题/意象/反复出现物 → 命名 + ≥1 处证例；符合 archetype-hunt 标准（跨文本复用）入 glossary | ≥2 条（此为旧卡最大缺口）。落库范式见 `web/data/books.json` → `motifs[]`（`name_zh/name_en` + `evid_zh/evid_en` + `orig` 原文引句 + `source` + `conf`；渲染 `web/build_reading.py` → `motif_block()`）。母题≠主题：要反复出现的意象/物件，不是一句概括（例：exit-party「派对即门 / 国家的反生活」）。 |
| L6 | 手法 Craft | POV/对话/时间/信息控制/细节：什么手法制造什么体验（可复用动作） | ≥5 项，每项带原文例 |
| L7 | 意图 Intent | 作者真正表达/暗示（引文支撑）；reception 好/坏都记 | 引文 ≥2 条引作者原话 |
| L8 | 互文 Intertext | 对题/同题/谱系边（relations/ 入账） | ≥3 边：对题/张力/延伸 |
| L9 | 精彩片段 Excerpts | 值得深读原文片段（直引 + 双语译）+ note（为什么值得） | ≥3 片段 |
| L10 | 深读清单 Deep read | things worth re-reading closely + 玩法（怎么读它） | ≥2 条 |
| L11 | 争议与未核 | 编辑上未证实/单源的情节 → unverified，标 ◐/○ | 非空即标注，不为凑数省略 |
| L12 | 双语双写 | 所有面向读者文字 zh/en 对照 | 双语默认铁律 |

### 3.2 memoir 回忆录/证词（prompts/memoir.md）

| # | 层 | 提取动作 | 阈值/形态 |
|---|---|---|---|
| M1 | 出版与读态 | 同 L1；**注意作者即叙述者** 的版权/版本差异 | metadata ✓ |
| M2 | 事件时间线 Event line | 可核实的事件/日期，按发生顺序；与叙述顺序分离 | 事件 ≥5（含年代） |
| M3 | 叙事时间线 Narrative line | 书中实际叙述顺序（倒叙/插叙/当下与回忆穿插） | 明确叙事结构 |
| M4 | 转折点 Turning points | 人生的关键转向/创伤点/决定点（**证词焦点**） | ≥3 |
| M5 | 证词伦理 Ethics | 作者怎么写他人（匿名/去标识/知情同意？）；「此处我改变了细节」类自述 | 记录策略 |
| M6 | 情感真实 Emotional truth | Gornick: situation（发生了什么）vs story（叙述者的解读）分开记 | 两列对照 |
| M7 | 回响 Echoes | 主题句的人际回声/读者回声/当下时事钩 | ≥1 echo（铁律 10） |
| M8 | 关键引语 | 直引本人原文 + 双语 | ≥3 引句 |
| M9 | 事实核验 Fact-check | 事件 vs 史料交叉；未核实标 ◐/○ 进 unverified | 记录差异 |
| M10 | 双语双写 | 同上 | 双语 |

### 3.3 essay 论说/非虚构（prompts/essay.md）

| # | 层 | 提取动作 | 阈值/形态 |
|---|---|---|---|
| E1 | 出版与读态 | 同 L1 | metadata ✓ |
| E2 | 论点 Thesis | 全书核心主张一句话（作者论断，不是要你赞同） | 1 句，引原文 |
| E3 | 论证链 Argument | 论点→子命题→证据（CER 结构），记录支持/反驳 | 主张账本 ≥5 条 |
| E4 | 数字复核 Numeric | 所有数字：单位/基期/出处三连（numeric-verification 方法） | 每个数字带出处 |
| E5 | 证据与反证 | 一手证据/二手转述分流；作者对反方怎么应答 | 每主张 证据≥1 |
| E6 | 概念与术语 | 关键概念入 glossary（一句定义 + 页码） | ≥4 条 |
| E7 | 争议/弱点 | 批评者怎么看、作者盲点 | 非空 |
| E8 | 关联边 | 同题/张力/延伸 | ≥2 边 |
| E9 | 双语双写 | 同上 | 双语 |

### 3.4 generic 通用（prompts/generic.md）

骨架(≥3) + 关键概念(≥4) + 论点/证据(≥3) + 引句(≥3) + 关联(≥2) + 双语。主模态不明时兜底。

---

## 4 · 无损账本 Lossless Ledger

每卡末尾的「提取账本」块 = 多层透镜的**可验数字快照**。`audit.py` 逐卡核对，任一不达标 → 卡片未完成。

```yaml
extract_ledger:
  kind: novel                   # 分型（模式必填）
  read_status: done             # done / reading / dnf …（决定哪些阈值适用）
  skeleton_parts: 3             # ≥3（骨架段数）
  plot_nodes: 9                 # ≥8 novel；≥5 memoir 事件；essay 用 claims
  claims: 0                     # essay ≥5；novel 强≥5 弱≥2
  characters: 8                 # novel：有名人物全提取
  charedges: 6                  # novel ≥5
  motif_clusters: 4             # novel ≥2
  craft_items: 6                # novel ≥5
  intent_quotes: 2              # novel ≥2 作者原话
  excerpts: 3                   # ≥3（novel 明文；其他 ≥2）
  quotes_original: 8            # 直引原文行数合计（受版权约束，≤300字/条）
  disagreements: 1              # 全类型 ≥1
  unverified_items: 2           # 允许 0，但只允许 all-✓ 时
  related_edges: 4              # ≥3 novel / ≥2 essay
```

阈值是**有损压缩防线**，不是字数比赛：`plot_nodes` 不给字数配额，按语义变化边界自然提取。
`audit.py` 输出每层达标/缺口，缺口=待补，不是删除。

---

## 5 · 引句守则 Quote Rules（内容无损的实现）

- 直引原文 ≤300 字/条；翻译逐条对应，宁可短而准，不译长而糊。
- `✓ 引原文`（有原文在手）与 `○ 转述`（只见二手摘要）**必须分标**。
- 版权整书/长段：不复制全文，只摘示片段 —— 「原文获取」面板提供正当获取通道。

---

## 6 · 与其他文件的关系

| 文件 | 关系 |
|---|---|
| `readings/library/_template.md` | v2 卡片模板；本框架是它的**提取协议**（怎么填到有深度） |
| `readings/methods/README.md` | 本框架在卡里引用既有方法卡（primary-verification、fact-vs-plot、numeric-verification、mirror-reading、archetype-hunt、trace-lineage） |
| `web/data/books.json` | 生成器的富数据源；L1–L12 直接映射到 books.json 字段（plot_acts、charedges、motif 等） |
| `docs/workflows.md` W1 | 实际执行入口 |

---

## 7 · 反方与回声 Disagreements (证据无损)

每卡至少一处 disagreement（铁律 10）：
- 书内：作者自己的矛盾/未答问题
- 书外：批评者的反对、后续研究反证、译介争议
记入 `read_status` 外，独立成节（`weak spots / unverified`），进 ledger 计 `disagreements`。

---

## 8 · 诚实边界 Honesty ceiling

- 没读完全文 → `read_status` 如实标注，情节标 `◐`（跟 fact-vs-plot 方法卡一致），别装。
- 一手源不可得 → 标 `◐/○` 进 `unverified`，比硬写一个「已核」强。
- **样本少是常态**：阈值不达时补真实内容，而不是放宽阈值凑数。

---

## 来源 Sources（检索于 2026-09）

- Sinykin & Winant, *Close Reading for the Twenty-First Century*, Princeton UP, 2025 —「scene setting → noticing → local claiming → regional argumentation → global theorizing」五步法，透镜堆栈的骨架。
- zenstory-ai, *story-short-analyze*（skills.sh，14.5K installs）— 语义边界情节节点、情感曲线、爆点六维、数值门槛（structure_counts）与 BLOCK 验收；L3/L6/L9 与 §4 账本直接借镜。
- Charon R., *Narrative Medicine: Honoring the Stories of Illness*, Oxford UP, 2006 — 见证/证词的 attention·representation·affiliation 三动；memoir 透镜底色。
- Gornick V., *The Situation and the Story*, 2001 — memoir 的 situation vs story 两列对照（M6）。
- Rosenbaum P., *Observational Studies* / *Design of Observational Studies*, Springer — 观察研究里的「可见偏差 vs 隐藏偏差」区分；essay E3/E5 与 fact/plot 分流的方法论远亲。
- Duke Writing Studio & Brandeis Close-Reading handbooks — prefread→markup→interpret→argue 的过程确认。