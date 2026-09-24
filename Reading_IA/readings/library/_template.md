# Book card template v2 书目卡片模板 v2

Copy to `library/YYYY-slug.md`, fill both language fields. **Every factual claim carries a confidence mark** (`✓` verified / `◐` primary-claim / `○` secondary-source / `✗` disputed). Keep provenance links under 出处.

```markdown
## 书目卡片 · Book Card

- **title 书名**: Original 原文: *…*
  Chinese 中译: （暂译）
- **author 作者**: [[authors/<slug>]]（+ 合著者，如 [[authors/perrignon]]）
- **year 出版年**: （出版年-月-日 若有）ISBN / 页数 / 出版社
- **lang_orig 原语言** / **translator 译者 / edition 版本**:
- **kind 文本形态**: novel / essay / paper / memoir / testimony / film …（阅读不限于书）
- **domain 领域**: literature / theory / philosophy / history / social-science / mathematics / …（`categories/README.md` 领域轴，开放标签）
- **category 分类**: [[categories/<slug>]] × n
- **status 状态** / **date_read 阅读时间**:
- **award 奖项**（若获）: year · 奖名

> 出处 provenance: 供给源链接 + 各项把握标注（出版·版本 `✓`；情节·转述 `○/◐`）

### 全文骨架 Skeleton（全书结构与时间轴）
- Act/Part/systematic章节 1-2 行摘要，标注页码区间 if 可核。

### 关键概念 Key concepts（4–8 条）
- **术语/意象**: 一句话定义（页码）
- **…**

### 关键引语 Key quotes（短引，≤ 3 条择要）
> 「……」 — <zh>译</zh>（原文页码） `✓ 引原文` / `○ 转述`

### 论点与证据 Arguments & evidence（主张 ⇒ 证据/反证）
| 主张 | 书中证据 | 把握 |
|---|---|---|

### 陷阱与局限 Weak spots（作者的盲点；批评者怎么说）
- …

### 关联边 Edges（显式、可复核，对应 relations/ 行）
- `≡` 同题 → [[…]]（book_graph.md 行号）
- `↯` 张力 → [[…]]
- `◎` 时事钩 → moment/themes/…
- `→` 延伸 → extensions/leads.md…

### 延伸问题 Open questions（2–3，进 leads.md 候选）
- …

### 一句话 Why this book 为何读
…

---

## 提取账本 Extract Ledger（深度无损验账 · `../extraction/audit.py`）

分型堆栈（`../extraction/framework.md`）+ 对应透镜（`../extraction/prompts/<kind>.md`）逐层提取后，
如实填数字快照；阈值不达标=缺口，补真实内容而非放宽阈值。示例（按 kind 调整字段）：

```yaml
extract_ledger:
  kind: novel
  read_status: done
  skeleton_parts: 3
  plot_nodes: 9
  characters: 8
  charedges: 6
  motif_clusters: 4
  craft_items: 6
  intent_quotes: 2
  excerpts: 3
  disagreements: 1
  unverified_items: 2
  related_edges: 4
```

> L5 母题簇的内容宿地是 `../web/data/books.json` → `motifs[]`（`name_zh/name_en` + `evid_zh/evid_en` + `orig` 原文引句 + `source` + `conf`），渲染器为 `../web/build_reading.py` 的 `motif_block()`；卡里只需在账本如实计数。母题≠主题。参考已落库范例：`2026-mandel-exit-party`（派对即门、国家的反生活、见证公信……）。