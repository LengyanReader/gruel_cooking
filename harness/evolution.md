# Evolution · 自我演化机制

How every layer of the harness **continually improves itself** — without waiting for a human to notice. The mechanism is the same at every layer (root harness + each domain harness): **a signal fires → an audit runs → a mutation applies → the journal records it**. Nothing here is a one-off; the point is that the harness is *alive*: it deepens, widens, and re-organizes as the repo does.

每一层 harness（根 harness + 各域 harness）用同一套机制自我演化：**信号触发 → 审查 → 变异 → 记入日志**。目标不是一次性完成，而是让 harness 像仓库一样持续生长。

## The engine 引擎

```
      signal ──► W-EVO review ──► audit (harness/audit.py) ──► mutation ──► journal
        ▲                                                        │
        └──────────────────── 下次 signal ───────────────────────┘
```

- **Trigger 触发**：任何信号发生（下节）即进入 W-EVO；多次信号合并为一次 review。
- **Audit 审校**：`python harness/audit.py` 自动扫描全部 harness 层的漂移（断链、漏注册、规则复制、编号漂移），输出报告 + 建议动作。
- **Mutation 变异**：按「变异谱系」施加最小必要变更。
- **Journal 日志**：每条变异在 `evolution.md` 日志段记一行（日期 · 层 · 变更 · 触发信号），**倒序，最新在上**。

## Signals 信号表（何时演化）

| Sig | Signal 信号 | Meaning 含义 | Default mutation 默认变异 |
|---|---|---|---|
| **S1** | 一条规则/流程在 **≥2 个域 harness** 中出现（audit 报「复制」） | 它其实跨域 | **Promote 晋升**到根 harness，域内只留指针 |
| **S2** | 一个新域长出重复流程（audit 报「未注册域」） | 域已激活 | **Register 登记**：建 `docs/workflows.md` + 注册表加行 |
| **S3** | 同一条 W- 循环被绕过第二次（人手动做了 harness 里已有的事） | 流程失配现实 | **Deepen 加深**：改写该循环直至与现实一致 |
| **S4** | 全新的工作方向反复出现却无归属 harness（audit 报「缺 harness」） | 域在分裂 | **Fission 裂变**：新开子 harness 或本域加层 |
| **S5** | 某规则长期零触发 / 域长期未注册活动 | 死规则 | **Archive 归档**：移入「休眠」注释或删除并记日志 |
| **S6** | 一次会话沉淀了新的、验证过的操作法（如 W3 催生新一步） | 经验成型 | **Consolidate 固化**：并入本域 harness 对应循环 |

## Mutation taxonomy 变异谱系

| Mutation 变异 | What 做什么 | Where 落在 | Example 示例 |
|---|---|---|---|
| **Promote 晋升** | 域规则 → 共享规则 | 根 `harness/` | B/C 技能段从 Reading_IA 役上移 |
| **Deepen 加深** | 现有循环内部细化/重写 | 所在域 harness | W2 增加「摆布地图」一步 |
| **Expand 拓展** | 新增文件/段/循环 | 所在层 | 新增 `LC-W` 或新域 harness |
| **Fission 裂变** | 一个大域拆出独立子 harness | 新开 `docs/workflows.md` | math 的 lean 层若独立成流程 |
| **Fuse 融合** | 两个瘦域并作一条循环 | 合并到一域 | core 与 heaven 若共享流程 |
| **Archive 归档** | 死规则休眠/删除并留档 | 所在层 + 日志 | S5 |
| **Promote+Strip 晋升+削枝** | 晋升同时删除域内副本 | 根 + 所有域 | S1 |

## Guardrails 护栏（自我演化不是无节制）

1. **最小变异**：一次 review 只做最必要的 1–3 个 mutation；宁可留待下次。
2. **可回滚**：每行日志标注触发信号与原因；变异后 `audit.py` 必须通过。
3. **双语保真**：变异不得删掉中英任何一侧（§II.12）。
4. **编号稳定**：已引用的规则/循环编号（W1、R4、MC-W2…）尽量保留，深化时不重新编号。
5. **人验后生效**：规则晋升/裂变等结构性变异，写「AI 提议 → 人工复核」标记（§I.6），确认后生效。

## Cadence 节奏

- **被动**：任何 S1–S6 信号发生即入列；每次把 audit.py 并进 `_final_ok.ps1` 前的卫生检查。
- **主动**：每月一次（或每新方向迭代一次）跑 `python harness/audit.py` + 一次 W-EVO 通读。
- **边界**：harness 永不为演化而演化——每一次变异都追一条真实信号。

---

## Journal 演化日志（latest first 最新在上）

| Date 日期 | Layer 层 | Mutation 变异 | Signal 信号 | Notes 备注 |
|---|---|---|---|---|
| 2026-09-24 | root → all | Engine：新增 `harness/audit.py`（自动审校器）+ W-EVO 公共循环（`harness/workflows.md`），并接入 `_final_ok.ps1` 步骤 6 | S6（机制需要可运行的审校引擎，而非纯文档） | 实测 S2 Register 信号可被真实触发；`--strict` 作门禁 |
| 2026-09-24 | living_heritage · math_clarification | Register：新建两域 harness（LH-W1…W6、MC-W1…W6），注册表 + 各域 harness 均含 Self-evolution 段；Reading_IA 也补上 Self-evolution 段（S6） | S2（living_heritage 已有 CI seed/verify/e2e；math 已有 house style + Lean + viewer，均无归属 harness） | 待人工复核（S6/§I.6） |
| 2026-09-24 | Reading_IA | Consolidate：本域 harness 收缩为 W1–W4 + 本域技能段，指向根 harness | S1（跨域规则已抽到根） | 待人工复核 |
| 2026-09-24 | root | Promote：`harness/` 从 Reading_IA 升格为全仓库操作手册（README/principles/skills/workflows）+ evolution 引擎 | S1/S2（跨域规则已存在：hy_py312、单一来源、提交卫生 ≥2 域在用） | 迁移 + 重构 + 引用更新 |