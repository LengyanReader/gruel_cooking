# 20261122 · v18 弟子与圈层轮（用户指令：检索梳理潜在学者及其圈子与弟子）

**触发**：用户指令——继续检索梳理潜在学者、他们的圈子以及弟子。此即 DEBTS M-1「指导谱系」的开工轮。

## 一、schema 演进（先立契约再提取，M4.11）

- 新增 **`mentees`（弟子·门生谱系）** 字段：直系博士/门生与社群传习，各带 ✔ 与出处；纪律——「弟子」在学派成熟期常以**社群**而非学位形式出现（AII 教材共读即 Friston 弟子层的当代形态）。
- 接入成本为零：builder 的 `parse_yaml_block` 为通用解析（circle 先例），模板渲染新增 `MENTEES` 块；README schema 与 intake 规则同步。

## 二、命中 → 入档

| 项 | 内容（✔ 2026-11-22） | 落点 |
|---|---|---|
| 新档 | **Thomas Parr**（有潜力）——Friston 博士生→UCL Queen Square 博士后；《Active Inference》教科书共同执笔人（MIT Press 2022，与 Pezzulo/Friston）；该书即 AII Textbook Group 教材（九期共读）。医师+理论神经科学家双轨。**「Bristol」一说查无实据，不采**（M4.12） | `scholars/parr-thomas.md` |
| friston-karl | 补 `mentees`：Thomas Parr（✔）、AII Textbook Group（✔ 社群形态弟子层） | `scholars/friston-karl.md` |
| hui-yuk | 补 `circle` 师承：**Bernard Stiegler**（Goldsmiths 博士导师 ✔；Hui 自述「teacher and dear friend，2008 年结识」；2021 年主讲 Stiegler 纪念演讲 ✔）——法国技术哲学直系承灯者 | `scholars/hui-yuk.md` |
| 仪表盘 | 重建 scholars=61，mentees 渲染入卡，--check 绿 | `docs/reseArch_X/index.html` |

**谱系链现观**：Friston（立法）→ Parr/Pezzulo（执笔成书）→ AII 社群（逐章传习）→ 本仓（外行形式化附录）；Stiegler（已故）→ Hui（承灯）→ Research Network（建制）。

## 三、空手而归（下轮）

- Manovich Cultural Analytics Lab 门生名单：公开页名册不完整且来源不稳（Jay Chow/Damon Burrow 等待回 manovich.net/softwarestudies 归档页逐条核），本轮不采。
- 其余 58 位学者的 mentees/circle 待补（优先：dialogue_map 头排 Manovich/Tsing/Buzzard/Tao/Sawin）。
- Hui 的弟子辈（他自任导师的学生）未检——Erasmus 带生通道 ◇ 未开。
