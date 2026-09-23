# 书单档案与更新设计 · Reading-list Archive & Update Protocol

`2026-09-23` · 已落地 D0（登记注册 + 档案页）；生成器待 Phase 1 · 关联：`readings/lists/`、`docs/reading_ia/read/`、`workflows.md`

> 问题：书单会**陆续添加**；文化趋势文章不应内嵌书单（已定规则，见 §7 R1）；需要一种可增长、可回溯、不破损的归档与更新方式。

---

## 1. 定义：什么是「书单」crop

一份书单 = 一个**带日期、被 W2 核验过**的读物批次，落入一个阅读窗口。

- 它的素材在 `library/` 卡（W1 产出）与 `review_*.md` 判定（W2 产出）；
- 它的**注册**在 `readings/lists/README.md`（唯一登记表，一窗一行）；
- 它的**镜像**是一页 web（`docs/reading_ia/read/<crop>-books.html`）+ 档案索引（`read/index.html`）。

> 书单是「素材层」，思潮文章是「合成层」。两层通过**指针**相接，不互相内嵌。

## 2. 数据流 Data flow

```
library/*.md  +  review_*.md        (W1 建卡 / W2 判定)
        │
        ▼
readings/lists/README.md            ← 书单登记注册 · 唯一注册表（一窗一行）
        │
        ├─► docs/reading_ia/read/<crop>-books.html   每批一页 · 永久文件名
        ├─► docs/reading_ia/read/index.html          档案索引 · 新批在上
        ├─► docs/reading_ia/index.html               着陆页「最新产出」卡
        └─► 思潮文章只放指针（链接 + 一句定位），永不全量内嵌清单
```

Phase 1（卡片积累后）：登记注册改 `---json---` frontmatter（同 Language Stacking `build_learning.py` 模式）；`web/build_reading.py` 从注册表 + library 卡生成 `read/` 全部页面与档案索引；`reading-ci.yml` 用 `git diff --exit-code -- docs/reading_ia/` 锁「源出同步」。清单见 §8。

## 3. 命名与身份 Naming & identity

| 项 | 约定 |
|---|---|
| crop id | `YYYY-<season>`，如 `2026-autumn`；一个阅读窗口至多一份书单。 |
| web 页名 | `read/<crop>-books.html`（当下定稿批 `2026-09-books.html` = `2026-autumn` 的规范页名）。 |
| 稳定性 | 页名定稿后**永不复用、不改名**——历史链接（着陆页 / 思潮文章 / 档案页 / 外部）永远有效。 |
| 注册行字段 | `crop id · date · glyph（秋分/春分…）· 所读图书（library 卡链接）· 判定 verdict · href · 下个窗口 keel` |

## 4. 档案页 `read/index.html` 结构

- **顶部**：板块定位——书单是素材层，思潮是合成层；「书单不入思潮之文」一句带过。
- **主体**：每批一张卡，新批在前。卡内含 glyph / 日期 / 书名列表（原文 + 语种）/ 判定 / 链接。
- **底部**：更新协议速查 + 校验门禁命令。

## 5. 更新协议 Update protocol

> **场景 A · 给已出版批补书**（同一窗口新读）：走 W1 建卡/补卡 → 把新书插入该批书单页 → 档案页若计数改变则同步 → 校验。

> **场景 B · 新批新书单**（最常见，如「冬至书单」）：
> 1. W1 建卡（library/ + authors/ + relations/ + leads）。
> 2. W2 判定 → 摘要写进该批页面头部。
> 3. `readings/lists/README.md` 加一行（新批在上）。
> 4. 新建 `read/<crop>-books.html`（双语，风格沿用既有书单页）。
> 5. 档案页 `read/index.html` 顶部插入新批卡。
> 6. 着陆页「最新产出」换成新卡对（书单 + 关联思潮文章）。
> 7. 思潮文章若有涉及旧书单的指针 → 更新指到新批。
> 8. 校验全部 HTML。

> **场景 C · 修订**：改该批书单页 + 档案页对应描述 + 校验；若思潮文章引用其内容，同步改指。

## 6. 历史与增长 History & growth

- 书单页是**时间档案**，不删改批号；每页底部固定「下个窗口 keel」提示。
- 从 `extensions/leads.md` 升级进书单的书，写 `promoted` 注明（对齐 W3 step 5「回连」）。
- 失效应**标注**而非删除（历史完整，放眼 WHO 校验思维）：用 `~~划掉~~` + 注记。
- 一个批阅读角色的投影过期，把它留在档案里，让「下一批」把它覆盖——开阔胜过完备。

## 7. 铁律（新增）Iron rules

1. **R1 · 书单不入思潮之文**：思潮文章（`.md` 与 `.html`）只允许**指针**（链接 + 一句定位），绝不允许内嵌书单清单或逐本展开。已同步进 `Reading_IA/docs/workflows.md` W3。
2. **R2 · 一窗一书单**：一个阅读窗口至多一份书单。
3. **R3 · 文件名稳定**：crop 页名定稿后不复用、不改名。
4. **R4 · 单一来源 → 镜像**：注册表与 web 页对用户呈现一致；改源即改镜像、跑校验。

## 8. 未决与 Phase 1 清单 Open / Phase 1

- `web/reading_data.py`：解析 `readings/lists/` 注册表 + `library/` 卡 → 结构化记录。
- `web/build_reading.py`：生成 `read/index.html` + 每批书单页 + 着陆页「最新产出」（Jinja 式模板，双语 toggle）。
- `scripts/verify_reading.py`：硬断言——注册表行 ↔ 页文件一一对应、无孤儿链接、双语字段齐全。
- `reading-ci.yml`：python 3.12，跑 `--validate` + `git diff --exit-code -- docs/reading_ia/`。
- 每书一页（per-book / per-author）待卡片更多时按 `web/README.md` 原有计划另行生成，与书单页分层。

---

*本文档是设计 + D0 落地基线；落地清单已登记于 `readings/lists/README.md`。*
<!-- AI-drafted 草拟标注：2026-09-23 opencode；规则 R1–R4 已在本次会话生效，人工复核后入 harness（根目录 `../harness/`）。 -->