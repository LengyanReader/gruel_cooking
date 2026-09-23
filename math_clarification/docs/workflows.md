# math_clarification · Domain Harness 本域工作流

First-principles math, radical simplicity — one page per idea, visuals first, formulas second. This file holds the **math_clarification-specific** workflows & rules. Repo-wide principles, skills and env live in the root **`../harness/`**.

仅收本域专属流程与规则；跨域规则在根目录 `../harness/`。

## Domain 场景

| Loop 流程 | When 何时 · What 产出 |
|---|---|
| **MC-W1 · Add an entry 新增条目** | 新数学概念/名题 → 一个 md 文件（house style 九段式） |
| **MC-W2 · Machine-check 机器验证** | 可检查的命题 → Lean 4 钉扎前提 + 裁判小结论 |
| **MC-W3 · Render layer 渲染分层** | 条目加 L0–L5 / zh-en 标记，web 查看器分层渲染 |
| **MC-W4 · Index & link 登记与互链** | 条目 → 本域 README 索引 + 跨板块互链 |
| **MC-W5 · Proof narrative 证明叙事** | 把关键证明讲成故事（可选深化层） |
| **MC-W6 · Viewer run 本地查看器** | FastAPI 查看器按受众/语言渲染 |

All Python runs in `conda activate hy_py312`（Lean 编译用本机 `lean`；web 查看器历史约定 `conda activate ds_0708`,见 `web/README.md`）。本域强调 §II.8（一实体一卡）+ §II.9（小而显式）。

---

## MC-W1 · Add an entry 新增条目

1. 放置：`basics/<topic>.md`（基础）或 `famous_problems/<topic>.md`（名题）或 `proof_narratives/<topic>.md`（叙事）。
2. 结构：遵循 **house style 九段式**（`README.md` §House Style）：
   `一行为想 → 精确表述 → 譬喻直觉 → 前提与成立条件 → 一点数学 → 解题方向与历史 → 它出现在哪里（天/地/人）→ 常错处 → 来源`。
3. 声明条件：**前提/成立条件必须显式**——一个题不能精确表述，就没有开始；不能画出画面，就没有理解。
4. 每条目结尾补「Where it shows up」至少一处真实出现（通常指向本 cookbook 别处）。

## MC-W2 · Machine-check 机器验证

Trigger: 条目含可检查的命题（精确算术、数论小结论、可枚举结论）。

- 包内 `lean/core/*.lean`（只用内置库）：`cd math_clarification/lean/core && lean <File>.lean`——静默即通过。
- 需 Mathlib 的放 `lean/mathlib/*.lean`（lake 项目，可选档），如 √2 无理、0.999…=1。
- 对应表见 `lean/README.md` `What is stated & checked where`——**新条目可检查时，先在该表补一行**。
- 开放猜想**只声明不证明**，用 `sorry`，仅限这些文件。

## MC-W3 · Render layer 渲染分层

- 标记：`<!-- L{0..5} --> … <!-- L{0..5}-end -->` 切受众深度；`<!-- zh --> … <!-- zh-end -->` 切语言；双语块省略语言标记。
- 映射（`web/README.md`）：L0 一行想法 · L1 譬喻 · L2 表述+前提 · L3 数学+方向 · L4 机器验证+常错 · L5 出现处+来源。
- 标记可选——无标记的纯 md 仍然渲染（默认单段 L0 英文）；Erdős 条目是完整标记范本。

## MC-W4 · Index & link 登记与互链

1. 在所在文件夹 `README.md` 的索引加一行。
2. 其他板块引用数学概念时，互链回此条目（§II.13 单一来源：概念正文只在 `basics/`/`famous_problems/` 一处）。
3. 若条目同时是天/地/人板块的解释支撑，在「Where it shows up」写明位置。

## MC-W5 · Proof narrative 证明叙事（可选）

把证明改写为故事：谜题 → 失败的路 → 唯一关键想法 → 豁然。信条：**数学从不是难事**——感到难，是讲法失败不是读者失败。每篇对应一个条目的证明。

## MC-W6 · Viewer run 本地查看器

```bash
conda activate ds_0708          # 历史约定，见 web/README.md
cd math_clarification/web
uvicorn app:app --reload --port 18088   # 仅高端口可绑定
# http://127.0.0.1:18088/entry/famous_problems/erdos_unit_distance?level=L5&lang=dual
```

---

## Domain rules 本域铁律

R-A: **先精确后直觉**——表述（精确）与譬喻（直觉）是双核，缺一不算条目（§II.10 不同意：直觉与精确必须互相校准）。
R-B: **来源四级标注**——一手 / 权威版本 / 学界共识（解读性，必须标注）/ 存疑；传说类（费马页边注、希帕索斯、考拉兹口述）标 **legend**，绝不当作事实。
R-C: **宁缺毋滥**——无稳定链接（DOI/arXiv/机构数字化）就给完整书目引文并明说；不可验证的链接不如没有。
R-D: **可查则查**——能机器验证的命题必须过 Lean，并在条目末尾写一行 **Machine-checked**。

## Self-evolution 自我演化

本域 harness 的演化入口见根目录 **`../harness/evolution.md`（W-EVO）**；本域专属信号：
- 新增一种条目类型/渲染档位 → 在 MC-W1/MC-W3 与 `README.md` House Style 补对应段。
- 新 Lean 校验文件 → 更新 MC-W2 与 `lean/README.md` 对照表。
- house style 九段式出现歧义（不同条目写法分叉）→ 此处加重版描述，必要时抽出共享模板。
- 一条规则跨域复用 → **晋升**到根 harness，本域只留指针。