# 20261104 · v12 学者档案介绍增维（八件套 schema 扩展 · 游戏线 9 档试跑）

**触发**：用户指令「另外，对每一个学者的介绍再增加一些维度，再详实和具体一下，在突出重点，要点的基础上」。经三问定档：新增维度选**八件套**、执行范围选**游戏线 9 档先试跑**、取证强度选**只用已核实料**。本轮为**schema 变更**（方法学，依 README §六记档），非新学者入库。

## 一、八件新维度（在既有 13 字段之上）

| 字段 | 义 | 落点 |
|---|---|---|
| `essence` | 一句话要点：为何值得连 + 最硬的已核实证据 | 渲染**置顶**，直接答「突出重点」 |
| `key_works` | 代表作清单（书名/文 + 年份 + 出版处） | 答「详实具体」，从已核实 current_work/trends 重抽 |
| `repo_anchors` | 与本仓的**具体文件/模块**接口（真实路径） | 把「接得住程度」落到可点开的文件 |
| `peer_bridges` | 与已入库学者的对话连线（同场/承接） | 网络视图，强化场景作品 |
| `why_now` | 时代抓手：让「此刻」成为时点的 2025-26 事件/出版物 | 把闸口「直面时代」逐人显影 |
| `entry_sequence` | 分层触达次序：公开作品→会议/机构→私信 | 从 `entry` 展开成可执行三步 |
| `feasibility` | 可达性·回信可行性/带宽（诚实，多标 ◐ 推断） | MVP 策略的现实约束层 |
| `open_questions` | 待追问的诚实缺口（归拢现有 ◇/◐） | 对话发起前的直补清单 |

**取证纪律**：全部八项**只从各档已 ✔/◐/◇ 内容重抽、拆分、结构化，不新增任何事实主张**。`repo_anchors` 逐条经 Glob 核实文件真实存在（避免 v9「场地意象」臆造覆辙，见 memory 8fc56d26）：MVP-004 圆桌、20261103 Book-of-Go 台账、`living_heritage/ref_canal_beijing_chronicle.md`、`contemplative science/ref_integrated.md`、`heaven_climate/README.md`、`economics_cross_culture/README.md`、`Reading_IA/engine/ingest.py`、`Language Stacking-Linguistic Weaving/languages/glossary.md` 全部命中。

## 二、试跑范围：游戏线 9 档

zhang-houquan · sicart-miguel · gobet-fernand · boellstorff-tom · sotamaa-olli · juul-jesper · liestol-gunnar · klein-richard · rusch-doris——这 9 档最新直采、字段内容最现成、且共用 `play` 轴可横向对照，作 schema 扩展的试点。验收后推广至其余 45 档（分波，每波过闸与取证纪律照旧）。

## 三、渲染与确定性

- `template.html`：新增 8 个字段的渲染块——`essence`（置顶高亮条 `.essence`）、`key_works/repo_anchors/entry_sequence/open_questions`（`.dim` 标签清单，repo_anchors 走等宽 `.mono`）、`peer_bridges`（`.tag.bridge` 胶囊）、`why_now/feasibility`（`.dim-line` 行内）。**中英双语标签齐**（isEn 分支），守双语 parity 铁律。
- `build_reseArch_X.py` **未改**：其 `load_records` 通用解析任意顶层 key，整份 dict 直入 JSON，故新字段自动进 payload，无需白名单。
- README §五 schema 补登八项（见本次同批提交）。
- 一处占位笔误（`${whyRealPlaceholder}`/`${whyReal}` 未定义变量）在模板内即时回修为 `${whatReal}${whyNow}`；rusch `peer_bridges`「瞑想」错字回正「冥想」；zhang key_works 一处引号嵌套 `「『…」` 回正。

## 四、下轮待办增量

- **推广至剩余 45 档**（v5–v7 及更早），按线分波；每档八件仍只从已核实料重抽，`repo_anchors` 必 Glob 核路径。
- 推广时同步补 `qid`（各档现均空）是否启用为新维度，待用户定。
- `feasibility` 全为 ◐ 推断——若某档真要发起对话，须以其当期实作（而非带宽揣测）复核该项。
