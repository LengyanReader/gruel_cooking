# MVP-001 notebook · 在跨文明发现源语料上压测 Manovich 的「媒体积累 / AI-as-culture」（v0）

> **状态**: v0 已建（2026-11-03）。可复现、纯本地、零外采。语气按规格不是「请收我」，而是：
> **「用您的方法跑了一份跨文明语料，发现 X 与您的假设有一处张力，请您指正。」**
> 目标学者: [`../scholars/manovich-lev.md`](../scholars/manovich-lev.md) · 规格: [`MVP-001-manovich-accumulation-on-corpus.md`](MVP-001-manovich-accumulation-on-corpus.md)

## 〇 · 运行方法（可复现）

```bash
python -I reseArch_X/mvp/mvp001_analysis.py    # 仓库根; 纯标准库, 秒级
```

产物：[`mvp001_data.json`](mvp001_data.json)（全部计算表 + 分组定义 + 溯源）、[`mvp001_fig1.svg`](mvp001_fig1.svg)（主图，代码生成可 diff）。输入为 `discovery_atlas/sources/*.json`（标本 A，n=237）与 `Reading_IA/readings/`（标本 B，仅计数）。

## 一 · 仪器声明（M3.10/M3.13）

- **主张**：本仓发现源登记层中，机器不可见性（bot-gating）的分布随语言圈而异。
- **仪器**：对版本化 SSOT（五域 JSON，237 条，逐条带 `verified`/`status`/`circle`/`wikidata_qid`）的**精确穷举计算**——脚本重算即复现，无采样、无估计量。
- **不做推断检验**：登记层 ≠ 随机样本（选择过程 = 建档者的注意力），p 值会伪装成抽样推断；故只报描述统计 + 明示选择偏差（M3.14：这是一次过滤，不是普查）。
- **探针定义**：`bot-gated` = 登记时实测对爬虫关闭（atlas 自家 verification pass 的观察）；`qid` = 实体已解析进 Wikidata 机器层。二者分别是「机器进得去的门」与「机器叫得出名字」的代理。

## 二 · 发现（v0）

| 组（分析性切分） | n | 占比 | bot-gated | qid 解析 | active |
|---|---|---|---|---|---|
| 西组（en+global+欧洲语言圈） | 185 | 78.1% | **55（29.7%）** | 146（78.9%） | 122（65.9%） |
| 其他组（zh/ja/ko/ar/fa/ru/tr/he/hi/afr/sea/pl） | 52 | 21.9% | **6（11.5%）** | 42（80.8%） | 44（84.6%） |

- **构成偏西**：登记层 78% 为西组——人类策展层的「西方中心」与预期一致。
- **不可见性反向**：对机器关门恰在西组更密（29.7% vs 11.5%）；单圈看，en 36%（39/107）、es 43%（3/7）、global 22%（11/50），而 **zh、ja、de、ar、fa、ru、afr 全为 0%**（各 n≥3）。非西组内的反例：zh-Hant 2/3（67%，n=3）。
- **机器可读性另一探针持平**：Wikidata 解析率两组相当（78.9% vs 80.8%）——「叫得出名字」无文明梯度，「进得去门」有。

## 三 · 可证伪问题与 v0 答案

**问**：在非西方语料上，「AI 使文化不可见」是否更强、还是反转？
**v0 答（张力，非定论）**：**反转迹象**——在本仓发现源层，机器不可见性集中于英文/西方圈。若「不可见」指机器对文化的读取，则数据显示：不可见性未必来自 AI 积累本身，而可能来自**积累中心对机器的拒绝**。

## 四 · 短文（≈500 字）

### 机器看不见谁？——一份跨文明发现源登记层的压测

马诺维奇与 Arielli 的《Artificial Aesthetics: Generative AI, Art and Visual Media》把生成 AI 放进媒体史：第七章「Separate and Reassemble: Generative AI and Media History」将其读作媒体积累的新层，第五章「Seven Arguments about AI Images and Generative Media」则论及生成媒体对文化可见性的重排。顺着这条线，我们把一个可证伪的问题交给本仓真实数据：在非西方语料上，「AI 使文化不可见」是否更强、还是反转？

语料是 discovery_atlas 的发现源登记层：237 条逐条人工核验的条目，横跨书/艺术/音乐/影像/科学五域、五个功能层，每条带语言圈、存活状态与 Wikidata QID。它不是世界的样本，而是「一位认真读者去哪里找文化」的完整账本——正因如此，它经得起一次诚实的描述性压测。

结果与预期相反。登记层构成偏西（西组 185 条，78%），但对机器关门恰在西组更密：29.7% 的源 bot-gated，其他语言圈仅 11.5%；en 圈 36%，而 zh、ja、de、ar、fa、ru、afr 全为 0%。另一探针 Wikidata 解析率则各圈持平（约 78–81%）。换言之：在「发现源」这一层，英语世界——恰是生成 AI 语料的中心——正更多地把门关上，若干非西方圈的门户反而对机器敞开。不可见性也许不来自 AI 的积累本身，而来自积累中心对机器的拒绝：「谁的门对机器关上」须按文明圈分别测量。

登记层小而偏（zh-Hant 2/3 即为圈内反例），v0 只求张力、不求定论；下一步以 Project Gutenberg 子集与更大登记层复测。

### Whom does the machine not see? — A stress test on a cross-civilizational registry of discovery sources

In *Artificial Aesthetics: Generative AI, Art and Visual Media*, Lev Manovich and Emanuele Arielli place generative AI inside media history: chapter 7, "Separate and Reassemble: Generative AI and Media History," reads it as a new layer of media accumulation, and chapter 5, "Seven Arguments about AI Images and Generative Media," takes up how generative media rearrange cultural visibility. Following that line, we hand a falsifiable question to real data from this repository: on non-Western corpora, is "AI makes culture invisible" stronger — or does it reverse?

The corpus is the discovery-source registry in `discovery_atlas`: 237 individually verified entries across five domains and five functional layers, each carrying a language circle, a liveness status, and a Wikidata QID. It is not a sample of the world but the complete ledger of "where a serious reader goes to find culture" — which is exactly why it survives an honest descriptive stress test.

The result runs against expectation. The registry skews Western (185 of 237 entries), yet machine-hostility concentrates there: 29.7% of Western-group sources are bot-gated against 11.5% in the other language circles; the English circle alone gates 36%, while zh, ja, de, ar, fa, ru and afr gate none. A second probe — Wikidata resolution — shows no civilizational gradient (78.9% vs 80.8%). In the discovery layer, in other words, the Anglosphere — the very center of generative-AI training data — is closing its doors to machines, while several non-Western circles keep them open. Invisibility may come not from AI accumulation itself but from the accumulation centers refusing the machine: "whose doors are closed to the machine" must be measured circle by circle.

The registry is small and curated (zh-Hant, 2 of 3 gated, is a counterexample within the non-Western group), so v0 claims a tension, not a verdict; a Project Gutenberg subset and a larger registry are the next instruments.

## 五 · 诚实边界（v0）

1. **登记层是手工策展的选择性层**：反映建档者的注意力（偏 en/global 面向），不反映世界分布；两 GROUP 对照是描述性的，无推断效力。
2. **`circle` 是语言圈**，不是文明圈本体（zh-Hant 3 条与 zh 14 条分列）；分组切分（西组含 global）是分析性的，定义与依据（global 50 条中 33 条 langs 含 en）写在 data JSON。
3. **`bot-gated` 系本仓 verification pass 的观察**（atlas 自家 gate.py/probe 流程），非第三方审计；`status` 有 pending 8 / contested 2 未计入二值探针。
4. **单圈 n 小**（多数 n<10）；比例差异 20.3pp 在 n=185/52 下的稳定性未经检验——这正是 v1 要做的（Gutenberg 外部基线 + 更大登记层）。
5. **标本 B（Reading_IA 手工深耕层）规模极小**（书卡 5、作者 6、关系档 3），仅作「人类可见深度 vs 机器层广度」的语境对照，未参与任何比例计算。

## 六 · Manovich 锚点（来源）

- 《Artificial Aesthetics: Generative AI, Art and Visual Media》，Lev Manovich & Emanuele Arielli——章节 2021–2024 逐章在线发布，合卷 PDF 2025-01-15，CC BY-NC-SA（✔ manovich.net/projects/artificial-aesthetics，访问 2026-11-03；Ch.5 2023-04-20、Ch.7 2024-03-27 日期同页核得）。
- 「When AI becomes culture」(2025)——「生成 AI 使文化对肉眼不可见」（✔ 沿 [`../scholars/manovich-lev.md`](../scholars/manovich-lev.md) current_work，档案 asof 2026-06-01；本 notebook 未另回源该篇原文）。
- 「Visual AI and Media Accumulation」（✔ 沿同上档案 current_work，2026-10-29）。
