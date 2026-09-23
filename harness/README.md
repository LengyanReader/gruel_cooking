# harness/ 方法 · 技能 · 工具 · 规则

Repo-wide operating manual — Methods, Skills, Tools & Rules for the **whole 舟洲粥 repository**.

This folder is the **operating manual for every domain in this repo**: which tools exist, which skill to invoke when, the shared workflows (environment, build ↹ sync, commit hygiene), and the rules every piece of work must obey — regardless of which pillar it belongs to.

这里是**全仓库操作手册**：有哪些工具、何时调用哪个技能、公共工作流（环境 / 源出同步 / 提交卫生）如何运行、以及所有板块的工作必须遵守的规则。

## Layout 结构

| File 文件 | Content 内容 |
|---|---|
| `skills.md` | Environment-wide catalog of skills & tools 环境级技能与工具目录 |
| `workflows.md` | Shared workflows + per-domain registry 公共流程 + 各域工作流注册表 |
| `principles.md` | Repo-wide rules (information use · knowledge design · coding) 全仓库规则（信息 · 知识 · 编码） |
| `evolution.md` | Self-evolution mechanism 自我演化机制（信号 · 变异 · 日志） |
| `README.md` | this index 本索引 |

## Self-evolution 自我演化

Every harness layer carries a **self-evolution mechanism** — the capability to continuously audit itself, detect drift, and deepen/extend/promote rules without waiting for a human to notice. See **`evolution.md`** for the full loop (`W-EVO`), the signal table, and the dated journal. Each domain harness ends with its own *Self-evolution* section listing domain-specific signals (see `Reading_IA/docs/workflows.md`, `living_heritage/docs/workflows.md`, `math_clarification/docs/workflows.md`).

每一层 harness 都带自我演化机制——自动审校、察觉漂移、持续加深/拓展/晋升规则。完整循环（W-EVO）、信号表与日志见 `evolution.md`；各域 harness 末尾各有本域专属信号段。

## Domains & their own harnesses 板块及其本域 harness

Each domain owns its *domain-specific* workflows and skills inline (a domain-local workflows document under its own `docs/`, or a dedicated section in its own README), while this root folder holds what is **shared**. Register every active domain here with one row. **Extensibility rule 拓展规则**: a new rule/tool that serves more than one domain enters this folder; a domain-only loop lives in the domain and gets one row below — never fork the shared files into a domain.

| Domain 板块 | Domain harness 本域地点 |
|---|---|
| `Reading_IA/` | `Reading_IA/docs/workflows.md` — W1-W4 阅读录入 / 书单核验 / 思潮之形 / 站点同步 |
| `Language Stacking-Linguistic Weaving/` | `README.md` §15 法则 + §99 构建流程 |
| `living_heritage/` | `living_heritage/docs/workflows.md` — LH-W1…W6 录入 / 灌库校验 / 构建同步 / e2e / 图谱 / 部署 |
| `math_clarification/` | `math_clarification/docs/workflows.md` — MC-W1…W6 条目 / 机器验证 / 分层 / 索引 / 叙事 / 查看器 |
| `core/`, `heaven_climate/`, `economics_cross_culture/` | `README.md` per pillar 运行原则 |
| `contemplative science/`, `direction_refs/` | 引用/研究素材库，无独立工作流（未激活） |