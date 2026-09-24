# Novel Lens · 小说/虚构透镜提示词

Load when: `kind = novel`（文学小说、科幻、推理、短篇集均可）。分层堆栈权威见 `../framework.md` §3.1。
**输出**：一张 `library/YYYY-slug.md` 卡片 → 可灌入 `web/data/books.json` 相应字段 → 生成器出书页。

---

## L1 · 出版与读态 Publication & status

- 版本信息（作者/译名/年份/ISBN/页数/出版社）逐项标 `✓`（一手目录）或 `◐`（二手引用）。
- `read_status` 必须诚实：未通读 → 情节转述一律 `◐`，绝不给单源摘要盖「已核」章。
- provenance 块：每条主张的来源 URL 并列。

## L2 · 骨架 Skeleton（结构无损）

- 按 Part / Act / chapter 分段；每段 1–2 行摘要 + **页码区间**（若能核）。
- **POV**：谁在看（一/三/全知；单/多视角）。
- **人称时态、叙事时序**：线性 / 倒叙 / 插叙 / 双线交叉 — 明说，别只写「双线」。

## L3 · 情节节点 Plot nodes（深度无损的发动机）

提取以**语义变化为边界**：风险、信息、关系、资源、决定、行动、读者理解发生变化时记一个节点；
同一动作链连续完成多个功能可记为 1 节点并在描述里说明。**用户理解的每一次移位 = 一个节点。**

每节点记录：
| 字段 | 说明 |
|---|---|
| 序号 | 严格时间顺序 |
| 类型 | 情绪/信息/冲突/转折/对话/氛围 |
| 描述 | 客观白描（禁止「揭开面纱」「命运转折」类空转套话） |
| 原文直引 | ≤300 字 |
| 情绪标记 | 类型 + 强度（-9..+9） |
| 涉及人物 | 全名 |

阈值：≥8 节点。不为凑数重复记录同一事件，也不按字数配额硬拆。

## L4 · 人物组 Character system（100% 覆盖）

- **有名人物全部提取**（id/name/group/role_zh/role_en/conf），一个都不落；出现即记，哪怕配角。
- 人物关系边 charedges：≥5 条，复用 `EDGE_KIND` 类别（mirror/parent/kin/romance/alliance/friend/colleague/cowrite/dialogue/evidence/witness/contrast/bond）。
- `conf`：关系可核（✓）还是暗示（◐）。

## L5 · 母题簇 Motif clusters（旧卡最大缺口）

这是过去详实度不足的头号病因：母题常被吞在「背景」里。
- 提名母题/意象/反复出现的物件**并命名**（如 counterlives、art-as-media、memory-repetition）。
- 每条带 ≥1 处**原文证例**（页码）。
- 已命名 → 提交 glossary；跨文本复用（≥2 典例）→ 晋升概念层原型簇（`categories/`）。

参考已落库范式（`web/data/books.json` → `motifs[]`，`web/build_reading.py` → `motif_block()`，例：exit-party 的「派对即门 / 国家的反生活」）：每条含 `name_zh/name_en` + `evid_zh/evid_en` 解析 + `orig` 原文引句 + `source` 可溯源 + `conf`。母题不等于主题——要「反复出现的意象/物件」，不是一句概括。

## L6 · 手法 Craft（从体验反推手法）

- 聚焦 / 陌生化 / 信息控制 / 对话节奏 / 时间碎片 / 细节选择……
- 每项写**「什么手法 → 制造什么读者体验」**（可复用动作），附原文示例；≥5 项。
- 禁写主观好评（「写得很好」）——只写机制。

## L7 · 意图 Intent

- 作者真正表达/暗示什么：用作者原话（采访/书内副文本）≥2 条引文支撑。
- reception 好坏都记：好的（Kirkus/Booklist…）与保留意见（plot unwieldy / 结尾失控）并列。

## L8 · 互文 Intertext & 关联边

- 对题(≡)/张力(↯)/延伸(→)/时事钩(◎) 各边入 `relations/`；≥3 边。
- 谱系：这本书在作者作品链里站第几位，与前作是什么继承/变奏（trace-lineage）。

## L9 · 精彩片段 Excerpts

- ≥3 段值得深读的原文片段：直引（≤300字）+ 双语译 + **note（为什么值得：手法?主题?信息?）**。

## L10 · 深读清单 Deep read

- ≥2 条「值得重新细读 X + 怎么读它」（可喂给读者的玩法，不只是书名）。

## L11 · 争议与未核 Disputes & unverified

- 未证实/单源/编辑红线的信息 → `unverified`，标 `◐/○`；绝不美化。

## L12 · 双语双写

- 所有面向读者的文字 zh/en 对照（内容对应优先，不逐字对齐）；原文必要时保留原语言。

---

## 完工自检（对应 `framework.md` §4 账本）

skeleton_parts≥3 · plot_nodes≥8 · characters全提取 · charedges≥5 · motif_clusters≥2 ·
craft_items≥5 · intent_quotes≥2 · excerpts≥3 · disagreements≥1 · 双语齐全。

缺哪补哪，补的是真实内容，不是放宽阈值。