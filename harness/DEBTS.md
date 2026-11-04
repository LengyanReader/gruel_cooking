# harness/DEBTS.md · 溯源债总台账（Provenance Debt Ledger）

> **目的**：把散落在各档案里的 ◇/◐「待补」汇成一张可管理的队列，按对话优先级清偿（REVIEW-2026-11 P1-6）。
> **规则**：仅追加（append-only）；清偿一项就在「状态」列记 `✔ 已补 (日期)` 并把行移入文末「已清偿」；不删除历史行。每个条目须指向**具体档案与字段**，能被 grep 到。

**Opened:** 2026-11-04 · **维护者**: 各线会话 · **清偿动作**: 回源→改档案→在此行记状态

## 一、QID 回填（entity-resolution，M4.12）

| id | 项 | 涉及 | 状态 | 优先级 |
|---|---|---|---|---|
| Q-1 | 26 位学者 Wikidata QID 全体未回填（诚实留空），需统一 resolve 流程 | `reseArch_X/scholars/*.md` 字段 `qid` | 待办 | 中 |
| Q-2 | resolve 工具复用：`discovery_atlas/scripts/resolve_qid.py` 已有，迁移/包装即可 | discovery_atlas | 待办 | 中 |

## 二、一手直链待补（M4.16：悬空/转述/截断）

| id | 项 | 涉及 | 状态 | 优先级 |
|---|---|---|---|---|
| L-1 | 学院官网直链 + 新书《文化遗产智能计算》/数字演绎剧场一手页（现为权威媒体转述 ◐） | `scholars/wang-xiaoguang.md` | 待办 | 高 |
| L-2 | 8.8% 排放论文一手 DOI（Drivers of global tourism carbon emissions） | `scholars/gossling-stefan.md` | 待办 | 高 |
| L-3 | FAccT 2026 论文精确题名一手页（AI 儿童故事性别审计） | `scholars/walsh-melanie.md` | 待办 | 中 |
| L-4 | HKUST 当期职务核实（或明确撤除该线索） | `scholars/kenderdine-sarah.md` | 待办 | 低 |
| L-5 | LinkedIn 截断 URL 补全或替换（M4.16 悬空指针已登记） | `opportunities/phd/RX-phd-unisg-gastronomy-202610.md` sources | 待办 | 低 |
| L-6 | watchlist 三网络数字回源：UNVEIL 12 位 / UNCHANGE 15 位·9 beneficiary / RAISE 2026-05-28 | `RX-phd-msca-heritour-202610.md` 正文 | 待办 | 中 |
| L-7 | UCD SPIRE/Honohan 备选通道当期是否开设 | `RX-phd-ucd-ai-heritage-202610.md` 正文 | 待办 | 低 |
| L-8 | 「When AI becomes culture」(2025) 原文回源（现沿档案 2026-06-01 转录，notebook 未直核） | `scholars/manovich-lev.md` current_work + `mvp/MVP-001-notebook.md` §六 | 待办 | 中 |

## 三、指导谱系（「受教」一级结果的核证层）

| id | 项 | 涉及 | 状态 | 优先级 |
|---|---|---|---|---|
| M-1 | 26 位学者近 5 年指导谱系/毕业生去向（v2、v3 两轮均「空手而归」，下轮专做） | `reseArch_X/scholars/*.md` 字段 `risk`/`entry` | 待办 | 高 |

## 四、趋势/动向回源（trends_analysis 补强）

| id | 项 | 涉及 | 状态 | 优先级 |
|---|---|---|---|---|
| T-1 | manovich「合成媒体认识论/典型性度量」一手来源（2026-10 表述） | `scholars/manovich-lev.md` trends_analysis | 待办 | 中 |
| T-2 | escobar 近 6 个月动向（档案锚点止于 2018/2020 纲领） | `scholars/escobar-arturo.md` | 待办 | 低 |
| T-3 | singer 现机构/带生通道 | `scholars/singer-tania.md` | 待办 | 中 |
| T-4 | davidson/drucker 近 6 个月新事件（档案判读为「路线连续、未命中新事件」） | `scholars/davidson-richard.md` · `drucker-johanna.md` | 待办 | 低 |

## 五、会话残件处置（待用户决断）

| id | 项 | 涉及 | 状态 | 优先级 |
|---|---|---|---|---|
| X-1 | `math_clarification/docs/vc.md` 仅一行 opencode 会话 ID——入库/删除/保留，待用户 | 该文件（未跟踪） | 待用户 | 低 |

---

## 已清偿（archive）

| id | 项 | 清偿记录 |
|---|---|---|
| — | （暂无） | |
