# living_heritage · Domain Harness 本域工作流

Fieldwork-based, comparative, digitally-enabled cultural-corridor research. This file holds the **living_heritage-specific** workflows & rules. Repo-wide principles, skills and env live in the root **`../harness/`**.

仅收本域专属流程与规则；跨域规则在根目录 `../harness/`。

## Domain 场景

| Loop 流程 | When 何时 · What 产出 |
|---|---|
| **LH-W1 · Content intake 内容录入** | 田野笔记/口述/图像资料 → `data/` 结构化 + 页面 |
| **LH-W2 · Seed & verify 灌库与校验** | 改 `data/seeds/` → 重灌库 → 硬断言 |
| **LH-W3 · Site build & sync 站点构建与同步** | 源 → 静态镜像 `docs/living_heritage/`，CI 锁同步 |
| **LH-W4 · Local run & e2e 本地运行与端到端** | 起服务 → 自测 → e2e |
| **LH-W5 · Export graph 图谱导出** | SQLite → neo4j Cypher（`scripts/sync_neo4j.py`） |
| **LH-W6 · Deploy 部署** | PythonAnywhere 持久化上线（见 `DEPLOY_PYTHONANYWHERE.md`） |

All Python runs in `conda activate hy_py312`. DB 默认 `data/living_heritage.db`；测试/CI 用 `LH_SQLITE_PATH` 指到临时库，**跑任务前先确认不写脏生产库**。

---

## LH-W1 · Content intake 内容录入

1. 田野/文献素材按类型归档进 `data/`（结构随 `app/db/sqlite.py` 的 schema）。
2. 页面内容改模板/静态资源，**不改 DB 的展示生效**——展示由 `app` render。
3. 双语内容遵循 `app/services/locale.py` 约定；`data/seeds/` 更新后必须走 LH-W2。
4. 新增图片/静态资源放 `app/static/**`，本地与 WSGI 一致。

## LH-W2 · Seed & verify 灌库与校验

Trigger: `data/seeds/` 或 schema 变更、首次克隆、CI。

```powershell
conda activate hy_py312
cd living_heritage
python -m app.seed                    # 生成 data/living_heritage.db 并灌入种子
python scripts/verify_seed.py        # 硬断言：权威种子与 DB 一致
```

CI 镜像（`.github/workflows/ci.yml`）：`python -m app.seed` + `verify_seed.py`，用 `${{ runner.temp }}/lh-ci.db`。

## LH-W3 · Site build & sync 站点构建与同步

```powershell
cd living_heritage
$env:LH_BASE_URL = "https://lengyanreader.github.io/gruel_cooking/living_heritage"
$env:LH_SITE_OUT = "../docs/living_heritage"
python scripts/build_static_site.py   # 全站静态镜像
git diff --exit-code -- docs/living_heritage/   # 源出同步锁
```

R4/§III.15（单一来源 → 镜像）：**只改源，产物随源一起提交**；end 换人、换机器后先 `build_static_site.py` 再 diff。

## LH-W4 · Local run & e2e 本地运行与端到端

```powershell
cd living_heritage
python -m app.main                    # 或 ./start_server.ps1；访问 http://127.0.0.1:18080/
python scripts/e2e_test.py            # 自测：起服务 → 打页面 → 校验关键路由
```

注意：`app` 是纯 stdlib `http.server`，无客户端数据拉取；`LH_PORT` 可覆盖端口。

## LH-W5 · Export graph 图谱导出

当 `relations`/学者图谱变更：

```powershell
cd living_heritage
python scripts/sync_neo4j.py          # SQLite → Cypher（具体如 neo4j 导入参数，见脚本头）
```

## LH-W6 · Deploy 部署（PythonAnywhere）

手顺见 `DEPLOY_PYTHONANYWHERE.md`：clone → venv → `app.seed` → 配置 WSGI（`app/wsgi_app.py`，注入 `LH_ADMIN_TOKEN`/`LH_BASE_URL`）→ Reload。**每次更新代码**：`git pull` →（seeds 有变则 `app.seed`）→ Reload。免费版限 100 CPU 秒/天。

---

## Domain rules 本域铁律

R-A: **DB 写前先隔离**——`/admin`/编辑操作走 `LH_ADMIN_TOKEN`；本地/CI/生产用不同 DB 路径，绝不互写。
R-B: **镜像只生成**——`docs/living_heritage/**` 一律由 `build_static_site.py` 产生，禁止手改。
R-C: **e2e 门禁**——任何路由/模板变更必须过 `scripts/e2e_test.py` 才合入。

## Self-evolution 自我演化

本域 harness 的演化入口见根目录 **`../harness/evolution.md`（W-EVO）**；本域专属信号：
- 新内容形态（新增一种资料类型/新页面路由）→ 在此补一条 LH-W 循环。
- seed/verify 断言放宽或收紧 → 同步改 LH-W2 与 `verify_seed.py`。
- 部署环境变动（商用、换域名）→ 更新 LH-W6 与 `DEPLOY_PYTHONANYWHERE.md`。
- 一条规则跨域复用 → **晋升**到根 harness，本域只留指针。