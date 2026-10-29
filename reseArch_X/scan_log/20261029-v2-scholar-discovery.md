# 20261029 · v2 学者深化（第三轮检索台账）

**触发**：用户再聚焦——重点是「能否发现优秀卓越开明的学者，再看有无机会合作或受教」。故本轮不动 MVP 数据工程，专攻**学者发现**，并把「受教(mentorship)」升为一级正当结果（README 第〇节 + schema `mode` 字段）。

**query 集**（WebSearch，验「当年在做什么 + 眼界开放的可证行为」）：
1. Tania Singer social neuroscience contemplative 2025
2. Arturo Escobar pluriverse designs sustainability anthropology
3. Anna Tsing mushroom end of world arts sciences
4. Wendy Hui Kyong Chun SFU machine learning humanities climate
5. Johanna Drucker digital humanities UCLA graphesis
6. Virginia Dignum responsible AI Umeå 2025

**命中 → 新档案（均 ✔ 当年/代表作出处）**：
| 学者 | 机构（✔ asof 2026-10-29） | 关键 current_work | 落档 |
|---|---|---|---|
| Wendy Hui Kyong Chun | SFU Canada 150 Chair / Digital Democracies Inst | 2026 剑桥 CDH 讲座「LLM & Returns of Critical Theory」；hypo-real+气候 | `scholars/chun-wendy.md` |
| Anna Tsing | UC Santa Cruz | Mushroom(2015,引~6886)/Arts of Noticing | `scholars/tsing-anna.md` |
| Arturo Escobar | UNC Chapel Hill（当期身份 ◇） | Designs for the Pluriverse(引~7281)/autonomous design | `scholars/escobar-arturo.md` |
| Tania Singer | 前马普社会神经科学；ReConnect（现机构 ◇） | ReSource 九月纵向冥想研究；2025 NYAS 综述 | `scholars/singer-tania.md` |
| Johanna Drucker | UCLA Information Studies | Graphesis；批评性 DH；DH Coursebook 二版 | `scholars/drucker-johanna.md` |
| Virginia Dignum | Umeå · Professor of Responsible AI | AI Policy Lab；value-sensitive；AI4People 伦理框架 | `scholars/dignum-virginia.md` |

**登记**：`indexes/dialogue_map.md` 增此六行并重排（Chun 为本轮头名）；README 第〇节 outcome 改「合作 或 受教」；scholar schema 加 `mode: 合作|受教|两者`。
**学者库现状**：16 张（v1 复用 academic_research 6 + v1.5 新增 Behrendt/Oberbichler 2 + 本轮 6 + Manovich/Sheller 已重写）。

**核实/存疑**：无撤回。Tsing/Escobar/Singer 的**当期身份/招生通道**标 ◇（资深或已离建制的机构未逐条落页），仅其**代表作与工作**为 ✔。
**空手而归（下轮）**：
- 美食/旅游轴尚缺「可受教的青年学者」强锚（现有均偏资深或框架层）。
- 「受教」需各人**近 5 年指导学生谱系/毕业去向**——本轮只及工作，未展开组级档案（下一轮专做）。
- Wikidata QID 新六人未回填（待与 discovery_atlas resolve 流程统一做）。
