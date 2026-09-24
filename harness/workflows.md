# Workflows · Repo-wide 公共流程

Shared, env-wide loops with the exact commands. Domain-specific loops live in each domain's harness (registered in `harness/README.md`). All Python runs happen in **`conda activate hy_py312`**.

本文件只收**跨域公共**流程；域专属流程在各域 harness（见注册表）。

## W-GEN · Build & sync any generator 构建与源出同步

Pattern shared by every pillar that ships a static site: **source (markdown/JSON) → generator → `docs/` mirror → CI-verified `git diff --exit-code`**.

1. Edit source material (markdown/JSON), never the generated `docs/` output by hand.
2. Run the domain's generator (per-domain exact command lives in that domain's harness):
   - **Language Stacking**: `python "Language Stacking-Linguistic Weaving/web/build_learning.py" --validate --db --check`
   - **living_heritage**: `python scripts/build_static_site.py` (from `living_heritage/`, env `LH_SITE_OUT` set)
   - **Reading & IA**: `python Reading_IA/web/build_reading.py`
3. Verify: run the domain's checks (HTML / links / seed-verify / pytest).
4. Commit **source + generated mirror together**; CI enforces `git diff --exit-code -- <docs path>` so the mirror is always in sync.

## W-ENV · Environment 环境

- Python: `conda activate hy_py312` (repo-wide, per `harness/principles.md` §III.14).
- Preview locally: `python -m http.server 8080 --directory docs` → `http://localhost:8080/<pillar>/`.
- Bilingual by default (§II.12).

## W-PRE · Hygiene before any commit 提交前卫生

Run the spirit of `_final_ok.ps1` (triggered the moment a commit is requested):
1. `git status --short` — only intended files staged.
2. Junk scan: no `_tmp_*`, `extract_classes*`, `.bak`, stray output files.
3. Secrets scan on staged diff: `BEGIN … PRIVATE KEY`, `ghp_…`, `AKIA…`, API keys.
4. `git diff --cached --name-only` review.
5. Never write secrets into notes or data files (`.env` stays out).
6. Ask before committing/pushing/PR — per `harness/principles.md` §III.19.

## W-EVO · The harness evolves itself 装备自我演化

The most proactive loop in the repo: the harness does not wait to be told it is stale. Whenever any evolution signal fires (see `harness/evolution.md`), or monthly, run:

```powershell
python harness/audit.py --strict   # scans EVERY harness layer; S-signals reported
```

1. **Audit** — report which signal fired (S1 promote / S2 register / S3 deepen / S4 fission / S5 archive / S6 consolidate).
2. **Mutate** — apply the minimal mutation from `evolution.md`'s taxonomy, at the layer that owns it.
3. **Re-audit** — rerun until `audit clean`.
4. **Journal** — append one row to `harness/evolution.md` Journal (date · layer · mutation · signal).
5. **Human sign-off** — structural mutations carry an *AI proposed → human reviewed* marker (§I.6) before they are declared effective.

Wire `audit.py` into `_final_ok.ps1` so every commit hygiene pass also checks harness health.

## W-CAP · Session recap loop 每次工作后的复盘沉淀

Every session — no matter how small — ends by **catching what it taught, then routing it into the harness**. The harness grows only if we harvest; this loop is how "经验/方法/原则/反思" stop being tribal knowledge and become the operating manual.

1. **Collect 收集**（工作收尾时，2 分钟）：回答三问——
   - 这轮做成了什么以前没有的方法/原则/技巧？→ 候选 **Consolidate(S6)**
   - 哪个现有 harness 流程被**绕过**或**不够用**（重复了第二次就要记）？→ 候选 **Deepen(S3)**
   - 哪条规则失效 / 哪条该上浮为全仓库？→ 候选 **Promote(S1)** / **Archive(S5)**
2. **Route 分派**：按 `evolution.md` 变异谱系，把每条发现落到**拥有它的那层**（域内 → 域 harness；跨域 → 根 `harness/`；技能 → `skills.md`；规则 → `principles.md`）。域专属能力别 fork 进根文件，根规则别复制进域文件。
3. **Mutate 变异**：最小必要变更（一次 ≤1–3 条）；双语两侧同改（§II.12）；编号稳定（S 信号 / W- 编号不乱）。
4. **Journal 登记**:在 `harness/evolution.md` Journal 加一行（日期 · 层 · 变异 · 触发信号），域级变更同时写进该域 harness 的 Self-evolution 段。
5. **Verify 核验**：`python harness/audit.py --strict` 通过后，这次会话才算真正闭环。

> 复盘本身就是一条 workflow（本文件已注册为 W-CAP）；它不在已有循环里"夹带"，而是每轮工作的显式收尾步骤。结构性变异仍须人工复核（S6/§I.6）。

---

## Registry 各域工作流注册表

| Domain 板块 | Where 位置 | Loops 流程 |
|---|---|---|
| `Reading_IA/` | `Reading_IA/docs/workflows.md` | W1 阅读录入 · W2 书单核验 · W3 思潮之形 · W4 站点同步 |
| `Language Stacking-Linguistic Weaving/` | `README.md` §99 + `Language Stacking-Linguistic Weaving/web/README.md` | 构建/校验/导出 neo4j / pytest |
| `living_heritage/` | `living_heritage/docs/workflows.md` | LH-W1 录入 · W2 灌库校验 · W3 构建同步 · W4 e2e · W5 图谱 · W6 部署 |
| `math_clarification/` | `math_clarification/docs/workflows.md` | MC-W1 条目 · W2 机器验证 · W3 分层 · W4 索引 · W5 叙事 · W6 查看器 |
| `core/ · heaven_climate/ · economics_cross_culture/` | `README.md` | 尚无独立流程（内容驱动） |

> Extensibility 拓展规则：新的单域流程 → 写进该域 harness 并在上表加一行；新的跨域流程 → 作为 `W-` 加在本文件，或按 `evolution.md` 晋升/加深/拓展。