# methods/ 方法论与透镜 · Methods & Lenses

Cross-disciplinary reading & thinking protocols: **how** to read, not just what. One card per method; the generator builds `docs/reading_ia/methods.html`. A method earns its place here only after it has worked in practice at least twice (see root `harness/skills.md` — skill-creator triggers).

跨学科读出与思考的**读法**——贵在「怎么读」，不只在「读什么」。一法一卡；生成器产出 `methods.html`。一种方法只有在实践中用过两次之后才可入档。

## Format 格式

```markdown
### <slug> · <中文名>
- **en**: <English name>
- **applies**: <适用领域/文本类型>
- **why 为何**: 一句话——它解决什么问题
- **how 怎么做**: 步骤 1..n（可核验、可重复）
- **rule 关联**: 对应本仓库铁律 / 原则
```

---

## kind-route · 分型透镜（extraction framework）
- **en**: Route kind, then read with the right lens
- **applies**: 一切阅读入档（novel / memoir / essay / generic）
- **why 为何**: 不同读物要不同的提取剧本——把小说当论证、把回忆录当小说，是深度无损的头号杀手。
- **how 怎么做**: 1) 按 `readings/extraction/framework.md` §2 定 kind；2) 加载 `readings/extraction/prompts/<kind>.md` 透镜堆栈；3) 逐层提取（骨架/节点/人物/母题/手法/意图…）；4) 卡尾填 `extract_ledger`；5) `py -X utf8 readings/extraction/audit.py` 验深度无损。
- **rule 关联**: 铁律 9「小而显式」· 铁律 2「立场必标」· 铁律 11「开阔胜过完备」——无损不等于无删，诚实标 ◐ 优于硬凑数。

## primary-verification · 一手先于转述
- **en**: Primary before press
- **applies**: 一切事实主张——新闻、传记、出版信息
- **why 为何**: 转述 = 噪声放大；只有一手源能终结复读机。这是全部档案可靠性的底座。
- **how 怎么做**: 1) 找到发声最早/最权威的一手源（原书、访谈记录、官方页、庭审记录）；2) 以一手为准写下主张；3) 转述源仅作交叉，标 `○`；4) 无法取到一手 → 标 `◐/○` 进「未核」而非硬写。
- **rule 关联**: 本书袋铁律 1「来源先于叙述」· 铁律 2「立场必标」（✓◐○✗）

## trace-lineage · 追溯谱系
- **en**: Trace the genealogy
- **applies**: 思想史、文艺理论、跨学科概念
- **why 为何**: 每个想法都有来历——记下影响之链，包括谁误读了它，才能看清「现在」由什么构成。
- **how 怎么做**: 1) 问「这个想法最早来自谁」；2) 沿影响边 `⇒/⇐` 画链；3) 标注误读/变形节点；4) 与 `relations/`、`categories/glossary.md` 互链。
- **rule 关联**: 铁律 3「追溯谱系」· 关系网络每边可复核

## mirror-reading · 双身对读
- **en**: Read as mirror, not as puzzle
- **applies**: 平行世界 / 双主角 / 反生活文本
- **why 为何**: 双面结构常被读成解谜题，而作者意在「同一焦虑的两种结局」——错读会丢掉全书主旨。
- **how 怎么做**: 1) 找出所有镜像句与镜像人物；2) 逐对问「这句/此人是谁的另一种结局」；3) 把两面当作一个硬币来读，而非两个宇宙。
- **rule 关联**: 概念层原型簇 `mirror-double` · deep_read 精读建议体例

## archetype-hunt · 原型猎袭
- **en**: Hunt the archetype
- **applies**: 文学、神话、文化研究、跨学科
- **why 为何**: 原型是「被多次照亮的簇」——在 ≥2 个文本/学科里认出同一模式，比任何一次单读都更接近深层结构。
- **how 怎么做**: 1) 读到一个强烈形象/母题时先命名（落 `glossary.md`）；2) 必须找到 ≥2 个典例（不同文本/学科）；3) 典例齐全 → 晋升为概念层原型簇 `categories/<slug>`；4) 只有 1 例 → 留在术语架。
- **rule 关联**: `categories/README.md` 放置裁定：原型显式命名入概念层

## theory-as-lens · 理论即透镜
- **en**: Theory as lens, never a cage
- **applies**: 文艺理论、哲学、社科理论阅读
- **why 为何**: 理论是工具不是神庙——它照亮书的一角，不绑架整本书。用理论拷问文本，也用文本校对理论。
- **how 怎么做**: 1) 每次只用一种视角（聚焦 / 陌生化 / 互文 ……）切入；2) 问「这个透镜照亮了什么、遮挡了什么」；3) 记下理论与文本相悖处——那才是进步点。
- **rule 关联**: 铁律 5「不同意即进步」· glossary 术语架

## fact-vs-plot · 事实与情节分流
- **en**: Separate facts from plot
- **applies**: 所有「书评/档案式」阅读，尤其出版前新书
- **why 为何**: 出版信息可四级核实，情节只有摘要可依——混为一谈等于给转述盖上「已核」章。
- **how 怎么做**: 1) 出版信息（版本/ISBN/页数/日期）→ `✓`；2) 情节梗概 → 按源数量与级别标 `◐/○`，标 `○/✗` 争议锚点；3) 全书的 `plot_acts` 与正文卡片强制分开标注。
- **rule 关联**: books.json `baseline_conf` · fact_ledger 核对账本

## numeric-verification · 数感复核
- **en**: Check the numbers
- **applies**: 社会科学、经济、医学、科技数据
- **why 为何**: 数字是转述里最易被改写的部分——一个「150 万+」需要单位、基期与出处三连。
- **how 怎么做**: 1) 还原数字原文语境（单位/基期/是谁说的）；2) 交叉 ≥2 源；3) 写进 fact_ledger 时带出处可点开；4) 无法复核的笼统数字 → 标 `○`。
- **rule 关联**: fact_ledger · 铁律 2「立场必标」

## window-layering · 窗口分层
- **en**: Layer the windows
- **applies**: 思潮与时间序列阅读（7d/14d/1m/1y）
- **why 为何**: 短期动静与长期结构是两种东西——分层后才不会把噪声当趋势。
- **how 怎么做**: 1) 7d 简报只记信号与峰值；2) 月度找结构位移；3) 年度拉弧线、问「十年之教」；4) 层层累积，年文件涵盖各月（不复制，只引用 + 指针）。
- **rule 关联**: 铁律 R1「书单不入思潮之文」· moment/series 生命周期