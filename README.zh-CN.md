# 舟洲粥

**English [README](README.md) | 中文**

> **一叶小舟，渡万洲之远；一碗清粥，暖天地之心。**

---

## 项目概览

以最朴素的食材熬粥——用**第一性原理**解读天地人三域现象，不止于应用，更追问：这些"基本"原理为何成立？其边界何在？

粥是最简单的食物，用最根本的食材熬成。本项目追寻的是能解释复杂现象的最简内核。

---

## 仓库现状（2026-11）

> 诚实的分层，依据 [tasks/REVIEW-2026-11.md](tasks/REVIEW-2026-11.md)：三条活跃线、一条共享工具带、以及立项目的骨架区——各自标注真实状态。下表即模块状态总表（Pages 落地页渐次对齐此表）。

### 三条活跃线

**1. 文化月旦（[`docs/culture_review/`](docs/culture_review/)）**
双语月刊文化梳评——2026 年十月号已上线：十一栏、四声部预生成神经音频（44 轨，`verify_audio` 门禁）、词内注、选段朗读、仅追加的订正登记；每条主张回源（✔/◐/◇ + 访问日期）。

**2. 数学释疑（[`math_clarification/`](math_clarification/)）**
极简数学：一屏一题，先图后式（`basics/`、`famous_problems/`、Lean 4 机器验证 `lean/`、证明叙事 `proof_narratives/`），按受众等级（L0–L5）与语言（en/zh/dual）渲染。另有旗舰双语论说与三道门禁的投稿套件（`essays/`：`build_reader --check`、`refcheck`、`review_scope`——均已入 CI）。

**3. 科研侦察（[`academic_research/`](academic_research/) → [`reseArch_X/`](reseArch_X/)）**
「方向 × 势能 × 可介入性」的前沿侦察图及其机会层 [`reseArch_X/`](reseArch_X/)：**26 份开放学者档案**（只记可证行为，逐条溯源）、9 份 PhD 机会档案、5 轮可审计检索台账、只读调研面板（[`docs/reseArch_X/index.html`](docs/reseArch_X/index.html)）。**对话优先**：每位学者配一件小而真实的 MVP 话柄；申请退居次要。未经明确人工授权不对外联系。

### 工具带（横切）

| 工具 | 职能 | 状态 |
|---|---|---|
| [`discovery_atlas/`](discovery_atlas/) | 237 个发现源：5 域 × 5 层 × 文明圈；schema 门禁（CI）；离线站 + 星座图；支撑「机器可见性」研究（MVP-001） | 活跃 |
| [`Reading_IA/`](Reading_IA/) | 阅读语料与知识引擎（graph 构建/审计/导出，CI 门禁）；手工书卡层同步生长 | 成形 |
| [`living_heritage/`](living_heritage/) | 全栈运河应用（Docker、pytest CI、PythonAnywhere 部署）；田野实验室：北京大运河 × 哥特兰 | **暂停**（2026-09 起）——绑定 reseArch_X MVP-002 复活或显式降级 |
| [`Language Stacking-Linguistic Weaving/`](Language%20Stacking-Linguistic%20Weaving/) | 跨语词表/语料切面；build-test CI | 低频 |
| [`harness/`](harness/) | 全仓操作手册：方法、技能、工具、规则与工作流（W-GEN/W-ENV/W-PRE/W-EVO/W-CAP）、audit.py | 维护中 |
| `tasks/` | 会话协议（PLAN/PROGRESS）与 2026-11 全仓评估 | 维护中 |

### 骨架区（立项目的——承诺暂缓，如实标注）

| 区 | 路径 | 状态 |
|---|---|---|
| 第一性原理 · 元思考 | [`core/`](core/) | 骨架——仅 README 与工作方法 |
| 天文 · 天象 · 气候 | [`heaven_climate/`](heaven_climate/) | 骨架 |
| 跨文化经济学 | [`economics_cross_culture/`](economics_cross_culture/) | **喂料启动（2026-11-04）**——首个溯源案例见 [`cases/001-salt-and-iron-debate.md`](economics_cross_culture/cases/001-salt-and-iron-debate.md)；它是 reseArch_X 各 MVP 的语料（technodiversity × taste 等级对话话柄） |
| 沉思科学 | `contemplative science/` | 近空；学术覆盖移至 [`reseArch_X/scholars/`](reseArch_X/scholars/)（Davidson / Singer / Britton） |
| 方向参考 | `direction_refs/` | 有意仅本地（`.gitignore`） |

### 模块状态总表

| 模块 | 层 | 门禁 | CI（2026-11） | 最近提交 |
|---|---|---|---|---|
| docs/culture_review | 内容 | verify_audio | ✅ culture-review-ci | 2026-11-03 |
| math_clarification | 内容 | build_reader --check · refcheck · review_scope | ✅ math-ci | 2026-11-03 |
| reseArch_X | 内容 | build_reseArch_X --check | ✅ research-ci | 2026-11-04 |
| discovery_atlas | 工具 | gate.py | ✅ discovery-ci | 2026-11-04 |
| Reading_IA | 工具 | graph/corpus 审计（fabric） | ✅ reading-ci | 2026-09-27 |
| living_heritage | 工具 | pytest + verify_seed | ✅ ci | 2026-09-26 |
| Language Stacking | 工具 | build-test | ✅ learning-ci | 2026-09-17 |
| core / heaven_climate / economics | 内容 | — | — | 2026-09-08 |

---

## 目录结构

```
gruel_cooking/
├── README.md / README.zh-CN.md  # 双语说明（本文）
├── docs/                        # GitHub Pages：落地页 + 各模块站点
│   ├── index.html               #   落地页
│   ├── culture_review/          #   文化月旦（正刊 HTML + 音频资产）
│   ├── reseArch_X/              #   学者/机会调研面板
│   ├── math_clarification/      #   条目阅读器
│   ├── reading_ia/ · living_heritage/ · language_stacking/ · discovery_atlas/
├── math_clarification/          # 条目 + 论说 + 投稿机器 + web
├── reseArch_X/                  # scholars/ · opportunities/ · mvp/ · indexes/ · scan_log/ · web/
├── academic_research/           # 方向侦察图（喂给 reseArch_X）
├── discovery_atlas/             # sources/*.json（SSOT）· gate.py · scripts/
├── Reading_IA/                  # readings/ · moment/ · knowledge/ · engine/ · web/
├── living_heritage/             # app/ · data/ · scripts/（Docker；CI）
├── Language Stacking-Linguistic Weaving/  # languages/ · web/
├── core/ · heaven_climate/ · economics_cross_culture/   # 骨架区
├── harness/                     # 全仓手册 + audit.py
├── scripts/                     # 仓库级工具（scratch/ 收一次性脚本）
└── tasks/                       # PLAN · PROGRESS · REVIEW-2026-11
```

---

## 运行原则

1. **从可感处起**——一切追问始于一个可见的现象或一个具体的问题。
2. **化至最简**——用第一性原理找到能解释现象的最小模型。
3. **反问解释本身**——这个原理为何成立？预设了什么？在哪里失效？
4. **追溯谱系**——每个想法都有来历，记录影响的链条。
5. **跨界授粉**——经济学滋养气候学，气候学滋养天文学，让连接活着。
6. **以最朴素的食材**——复杂性从简单规则的交互中涌现，相信那碗粥。
7. **来源先于叙述**——引用一手文献，核实来源，标注可靠度（✔ 已核 / ◐ 部分 / ◇ 未核，附访问日期）。

---

## 如何参与

- 向三条活跃线供稿：月旦条目、数学条目、学者档案（schema 与溯源标记有门禁把关）。
- 改进工具带：每个生成器都有 `--check` 类门禁；提交前跑 [`scripts/check_all.py`](scripts/check_all.py)。
- 复活骨架区：喂一个真实的、带来源的案例；或在 issue 里提议冻结。

始终回答：**"这个现象最简单的解释版本是什么？"**
