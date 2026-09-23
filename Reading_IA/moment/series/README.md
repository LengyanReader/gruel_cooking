# series/ 滚动窗口综述

Cumulative syntheses by time window. Each file synthesises **everything beneath it**: a year file includes the year's months, a month file includes its fortnights.

按时间窗累积的综合。每个文件统合**其下的一切**：年文件涵盖年内各月，月文件涵盖其两周。

## Windows 窗口

| File 文件 | Covers 涵盖 |
|---|---|
| `week-YYYY-MM-DD.md` | last 7 days 最近 7 天 |
| `fortnight-YYYY-MM-DD.md` | last 14 days 最近 14 天 |
| `month-YYYY-MM.md` | last month 最近 1 月 |
| `year-YYYY.md` | the year 最近 1 年 |

## Structure 结构

```markdown
# <window> 窗口 · 思潮之形
`YYYY-MM-DD` · covers: 7d / 14d / 1m / 1y

## 出现的信号 Signals that surfaced
- <signal> — 出处 provenance: brief/URL · confidence 把握

## 上升 / 退场 / 反转 Rising · Falling · Reversing

## 摩擦点 Friction points
（两股思潮相撞处，通常在转折点附近）

## 与阅读的连接 Reading ties
- [[themes/…]] · [[readings/library/…]] · leads promoted 被升级的线索
- **R1 书单不入思潮之文**：此处只放指针（链接+一句定位）；书单本体在独立页 `docs/reading_ia/read/<crop>-books.html`，登记于 `readings/lists/README.md`。

## 结转问题 Questions carried forward
```

## Registry 登记

| Window | File | Status |
|---|---|---|
| 1y · 2026 | `year-2026.md` | published · 2026-09-23 秋分节点档案（Autumn-equinox balance dossier）· 书单为指针（清单在同名 read/ 页） |
| *(2026-…)* | | active |