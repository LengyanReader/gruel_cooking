# relations/ 关系网络

The edges between cards. Keep it **small and explicit**: a handful of edge types, one row per edge. This is the graph you will re-read when building a reading path or writing a trend dossier.

卡片之间的边。保持**小而显式**：少量边类型，每边一行。你在规划阅读路径或撰写思潮档案时要重读的，正是这张图。

## Edge types 边的类型

| Type 类型 | Direction 方向 | Meaning 含义 |
|---|---|---|
| `⇒ influences` 影响 | author ⇒ author | A shaped B's thought 影响 |
| `⇐ inherits/continues` 继承 | author ⇒ author | B continues A's line 继承 |
| `↯ refutes/tensions` 反驳 | author ⇔ author | productive tension 反驳或张力 |
| `⊆ genre/method` 同法 | book ⇔ book | same method or genre lineage 同法 |
| `≡ concept-core` 同题 | book ⇔ category | book elaborates the cluster 同题 |
| `→ extends-to` 延伸 | book ⇒ category | book opens a new facet of the cluster 开辟新面向 |
| `◎ moment-tie` 时事钩 | book/category ⇔ moment/theme | the reading meets the present 与当下思潮相连 |
| `◎ circle` 同代·朋友圈 | author ⇔ person/author | same-generation peers, editors, collaborators 同代人 / 圈子 |
| `✎ co-write` 合著 | author ⇔ author | co-authored a text 共同署名 |
| `⌾ school` 流派归属 | author ⇒ school/movement | which school or movement the author belongs to 学派归属 |

## Files 文件组织

Prefer a few **edge-list files** over many tiny files:

- `influences.md` — author ⇒ author (rows: `from → to`, one-line reason)
- `book_graph.md` — book ⇒ category / book ⇔ book / book ⇒ extension
- `moment_ties.md` — readings ↔ `moment/themes/` cross-references

When the list grows past ~200 rows, promote to a scripted graph (SQLite or JSON under `web/` builds; see `web/README.md`).

```markdown
## Edge list 边表: <type>

| from | to | why 一句理由 | date 日期 | confidence 把握 |
|---|---|---|---|---|
| [[authors/herbert]] | [[authors/levi]] | 意识到「模式即尺度」 | 2026-09 | strong |
```