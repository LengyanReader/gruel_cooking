# 证明不再稀缺：AI 时代的数学边界与数学家之定位 / When proofs are no longer scarce: the boundaries of mathematics and the place of mathematicians in the age of AI

<!-- 长稿正式条目（论说体，house style 论点→论据→论证→反诘→来源）。AI 起草、未经作者逐条复核（harness §I.6）。双语逐段并列；英文侧与中文侧在内容与精神上对应，而非逐句对译（作者决定 2026-09-26）。来源标注四级（harness R-B）：一手 / 权威版本 / 学界共识·解读 / 存疑；【已审计】出自 essays/submission/citation_audit.md 语料，【待审】为待人工核验。L0 块为导读与目录（按受众层级裁剪：level=L0 只见导读）。 -->
<!-- en: Long-form entry (essayistic; house style claim → evidence → argument → counter-question → sources). AI-drafted and not yet verified item by item by the author (harness §I.6). The two languages run paragraph by paragraph in parallel: the English and the Chinese correspond in content and in spirit rather than word for word (author's decision, 2026-09-26). Sources are graded on four levels (harness R-B): primary / authoritative edition / scholarly consensus or interpretation / doubtful; 【已审计】marks material drawn from essays/submission/citation_audit.md, 【待审】marks what still needs manual verification. The L0 block is the foreword and contents, cropped by audience level (level=L0 shows the foreword only). -->

<!-- L0 -->

<!-- en -->

## Foreword and contents

This essay was written to slow a news cycle down. Between 2024 and 2026 the machine's report card changed every year, silver, gold, then a Millennium Prize problem, and every announcement drew astonishment or alarm while the arguments around it almost never concerned whether the calculation was right. The seven chapters below are a systematic cleaning, in one order, of the questions the news kept raising: what the events actually establish, what the voices reveal, what mathematics is, who mathematicians are, whether AI is really inferior, what "originative" means, and what, seen in the large, is happening to us. The running thesis: the visible disputes are not about whether machine derivations are valid but about framing, disclosure, attribution and admissibility, and the deeper question of the division between human and machine cannot be settled apart from the older questions of what mathematics is, who mathematicians are and who assigns meaning. Each chapter states its claim, argues it against evidence whose reliability is labelled, faces the strongest counter-argument, and closes with explicit credibility verdicts wherever events are at stake. The whole can be read front to back, or each chapter on its own; the tree below shows what is where.

- **1 · Events and credibility: a case-by-case audit**: five assessment dimensions and three certification settings, then the events graded one by one (IMO 2024 and 2025, the FrontierMath score, AlphaEvolve, the Erdős problems in three acts, First Proof, Navier-Stokes, and two physics cases, the single-minus gluon amplitude conjectured and proved, the nine-loop hexagon amplitude computed), closing in the diagnosis that the battlefield of credibility is not the derivation.
  - 1.1 A workable framework
  - 1.2 From silver to gold
  - 1.3 When numbers leave their conditions
  - 1.4 The mechanically checkable end
  - 1.5 The Erdős problems: a three-act play
  - 1.6 Generation is easy, verification is not
  - 1.7 A valid derivation, a contested claim
  - 1.8 The pattern, and its limits
- **2 · The voices, and whose crisis it is**: six voices (industry, rivals, careful scholars, institutions, grassroots, entangled participants) each read across four registers, argument, evidence, logic, and the position and motive behind it; then the crisis unpacked into four layers, truth, livelihood, trust and meaning; the verdict: a structural adjustment of mathematics as institution, not a crisis of mathematics as truth.
  - 2.1 The spectrum of voices
  - 2.2 A crisis of mathematics, or of mathematicians
- **3 · What mathematics is**: its place among logic, empirical science and natural language; the seven ontological positions and the AI-intuition each one carries; the question of an ultimate ground, answered by Gödel and Cohen; the four forces that shape it; its technical limits; and the few routes by which new questions and theories arise.
  - 3.1 Its place in the system of knowledge
  - 3.2 Seven ontological positions
  - 3.3 Is mathematics the ultimate ground of everything
  - 3.4 The four forces that shape mathematics
  - 3.5 The limits of mathematics
  - 3.6 Where new questions and new theories come from
- **4 · Who the mathematician is**: the spectrum of roles, birds, frogs, solvers, builders, synthesizers, expositors; what contemporary mathematicians actually work on, the Langlands programme, arithmetic geometry, PDE regularity and the newborn field of AI mathematics itself; and the four causes of the mathematics-equals-intelligence myth, answered by the anxiety evidence.
  - 4.1 Birds, frogs, and other roles
  - 4.2 What contemporary mathematicians do
  - 4.3 Why mathematics became a byword for intelligence
- **5 · Formalization, computation, and division: is AI really inferior to mathematicians**: the three layers of doing mathematics; the honest, still-open answer; the division of labour and the five institutional rules that support it; the vocabulary kept apart, rationality, formalization, computability, quantifiability, logic; and whether Western mathematics is the whole of mathematics.
  - 5.1 Three layers of mathematical activity
  - 5.2 An honest answer that remains open
  - 5.3 How the division of labour should evolve
  - 5.4 Rationality, formalization, computability, quantifiability and logic
  - 5.5 Is Western mathematics the whole of mathematics
- **6 · What counts as originative**: a checkable three-condition definition that makes originativity a relation between a question and a literature; why originative work is scarce and where its supply comes from; the multiple identities of Descartes, Newton, Leibniz, Gauss and their like; and a more productive way of asking the question about AI.
  - 6.1 Defining the term
  - 6.2 Scarcity and supply
  - 6.3 The multiple identities of the originators
  - 6.4 A more productive way of asking
- **7 · Summary and a view from above**: the threads gathered; Whitehead's process philosophy and Friston's free-energy principle as two nameable resources for a structure in which parts and whole constitute each other; and the warning that the concrete stakes of the moment are not dissolved by the wide view.
  - 7.1 Gathering the threads
  - 7.2 Process, prediction and mutual constitution
  - 7.3 Concrete stakes are not dissolved by the wide view

The 71 sources are numbered by first appearance at the end of the article, each carrying its reliability tier (primary / authoritative / scholarly consensus or interpretation / doubtful) and its audit status; entries marked 待审 are pending human verification.

<!-- zh -->

## 导读与目录

这篇文章想做一件事：把新闻的节奏放慢。2024 至 2026 年，机器的成绩单一年一换，银牌、金牌、千禧年难题，每一次宣布都引来一片惊叹或警惕，而围绕它的争论几乎从不落在「算得对不对」上。下面七章是对新闻不断抛出的一串问题的系统清理，顺序固定：这些事件究竟确立了什么，各种声音透露了什么，数学是什么，数学家是谁，AI 是不是真的不如人，「开创性」意味着什么，以及把这一切放到大处看，我们到底在经历什么。全文的核心命题是：可见的争执不关乎机器推导是否有效，而关乎框架、披露、归属与可入性；而人与机器如何分工这个更深的问题，无法脱离数学是什么、数学家是谁、意义由谁赋予这些更古老的追问被单独回答。每章先立论，再以标注了可靠程度的证据论证，正面回应最强的反驳，并在涉及事件处给出显式的信度判级。全文可以通读，也可以按章取读；下面的目录树标明各处所在。

- **1 · 事件与信度：一次逐案审计**：五维评估框架与三种核验情形，随后逐案判级这些事件（IMO 2024 与 2025、FrontierMath 分数、AlphaEvolve、Erdős 问题三幕、First Proof、纳维-斯托克斯，以及理论物理两案：单负胶子振幅的猜想与证明、九圈六边形振幅的计算），收束于一个诊断：信度的战场不在推导。
  - 1.1 一套可操作的评估框架
  - 1.2 从银牌到金牌
  - 1.3 数字脱离条件之后
  - 1.4 可机械核验的那一端
  - 1.5 Erdős 问题：一出三幕剧
  - 1.6 生成容易，核验难
  - 1.7 推导正确，主张受质疑
  - 1.8 小结：规律及其限度
- **2 · 众声喧哗与危机诊断**：六种声音（产业、竞争、审慎学者、建制、草根、被卷入当事人）各按论证、论据、逻辑，以及背后的立场与动机四个层面拆解；再把危机拆成真理、生计、信任、意义四个层次；结论：这不是数学作为真理的危机，而是数学界作为建制的结构性调适。
  - 2.1 众声的谱系
  - 2.2 是数学的危机，还是数学家的危机
- **3 · 数学是什么**：数学在逻辑、经验科学与自然语言之间的位置；七种本体论立场及各自携带的 AI 直觉；终极根据之问，由哥德尔与科恩作答；塑造数学的四种力量；技术性的边界；以及新问题与新理论诞生的少数几条路径。
  - 3.1 数学在知识体系中的位置
  - 3.2 七种本体论立场
  - 3.3 数学是万物的终极根据吗
  - 3.4 塑造数学的四种力量
  - 3.5 数学的边界
  - 3.6 新问题与新理论从何而来
- **4 · 数学家是何种人**：角色谱系，鸟、蛙、求解者、建构者、综合者、阐释者；当代数学家实际在忙什么：朗兰兹纲领、算术几何、PDE 正则性，以及新生的「AI 数学」本身；「数学=聪明」的四因拆解，与焦虑研究的实证回应。
  - 4.1 鸟、蛙与其他角色
  - 4.2 当代数学家在做什么
  - 4.3 数学何以成为「聪明」的代名词
- **5 · 形式化、可计算性与分工：AI 真的不如数学家吗**：「做数学」的三个层级；诚实而尚未定论的正面回答；人机分工与支撑它的五项制度规则；必须分开的概念词汇：理性、形式化、可计算、可量化、逻辑；以及西方数学是否是数学的全部。
  - 5.1 数学活动的三个层级
  - 5.2 一个尚无定论的正面回答
  - 5.3 分工应如何演化
  - 5.4 理性、形式化、可计算、可量化与逻辑
  - 5.5 西方数学是数学的全部吗
- **6 · 什么是「开创性」**：可核查的三条件定义，使开创性成为问题与文献之间的关系而非心智的属性；开创性工作为何稀缺、存量从何补给；以笛卡尔、牛顿、莱布尼茨、高斯为代表的开创者的多重身份；以及关于 AI 的一个更有生产力的问法。
  - 6.1 界定「开创性」
  - 6.2 开创性工作的稀缺与供给
  - 6.3 开创者的多重身份
  - 6.4 换一个更有生产力的问法
- **7 · 总结与统观**：收束全篇；怀特海过程哲学与弗里斯顿自由能原理为「整体与部分互相成就」的结构提供两个名字说得出口的思想资源；并提醒：此刻的具体利害不因整体视野而消解。
  - 7.1 收束
  - 7.2 统观：过程、预测与互相成就
  - 7.3 具体利害不因整体视野而消解

文末 71 条来源按首次出现编号，每条标注来源层级（一手 / 权威版本 / 学界共识·解读 / 存疑）与审计状态；标注【待审】者待人工核验。

<!-- L0-end -->

<!-- L1 -->

<!-- en -->

## Introduction

On 8 September 2026, OpenAI announced that an internal, unreleased model had solved the existence and smoothness problem for the Navier-Stokes equations, one of the seven Millennium Prize problems, open for nearly a century [1]. Three days later the Clay Mathematics Institute chose a telling word in reply: the problem was "apparently" settled, its evaluation procedure remained in force, and its website still labelled the problem "unsolved" [2,3,4]. Ten days further on, Scientific American asked whether OpenAI had solved the wrong problem [5]. In the same week a mathematician at New York University publicly accused the company of trying to exclude from the authorship his collaborator, who works at a competing firm [5]. A technical truth, a commercial race, an authorship dispute, and a priority quarrel echoing Newton against Leibniz were compressed into a single September.

The compression is the rhythm of the past two years. Silver in 2024, gold in 2025, a Millennium problem in 2026: the machine's report card changes every year, and each announcement stirs astonishment or alarm, while the disputes around it seldom touch whether the calculation was right. This essay wants to slow those news-cycle reflexes down and put the real questions on the table one at a time. There are seven of them. How much of each "breakthrough" deserves belief? Where do the voices raised in the mathematical community stand, and why? What is mathematics itself, and where does it sit in human knowledge? Who is the mathematician, and what do mathematicians do today? In formalizable settings, is the machine really inferior to the human? Does the word "originative" describe something only mathematicians can have? And what, seen in the large, is actually happening to us?

The essay attempts a systematic cleaning in that order, under a single rule: every claim follows its evidence, every piece of evidence carries a stated reliability, and every conclusion says under what conditions it would fail.

<!-- zh -->

## 引言

2026 年 9 月 8 日，OpenAI 宣布其内部一个未公开的模型解决了纳维-斯托克斯方程的存在性与光滑性问题，这是七个千禧年大奖难题之一，悬置近一个世纪 [1]。三天后，克雷数学研究所用了一个耐人寻味的词来回应：「似乎」已经解决，并强调评审程序照旧，官网上这道题仍标着「未解决」[2,3,4]。又过十天，《科学美国人》刊出质问：OpenAI 会不会解错了一道题 [5]？同一周里，一位纽约大学的数学家公开指控，对方曾试图把他在竞争对手公司任职的合作者从署名中剔除 [5]。一个技术真相、一场商业竞争、一次署名纠纷、一桩与牛顿和莱布尼茨之争遥相呼应的优先权公案，在同一个九月里被压缩到了一起。

这种压缩正是过去两年的节奏。2024 年银牌、2025 年金牌、2026 年千禧年难题，机器的成绩单一年一换；每一次宣布都激起一阵惊叹与警惕，而围绕每一张成绩单的争论，却几乎从不在「算得对不对」上。本文想做的，正是把这些新闻式的惊叹与警惕放慢下来，把争论背后的真问题一件一件摆到桌面上。这些真问题一共有七个：这些「突破」各自有几分可信？数学界里响起的各种声音，各自站在哪里、为什么？数学本身究竟是什么，它在人类知识里处在什么位置？数学家是怎样一种人，他们今天在忙什么？在可以形式化的场景里，机器真的不如人吗？所谓「开创性」，究竟是不是只有数学家才能拥有的东西？以及，把这一切放回一张更大的图景里看，我们到底在经历什么？

本文尝试按这个顺序做一次系统的清理。清理的原则只有一条：每一个论断都跟着证据走，每一处证据都标明它的可靠程度，而每一个结论，都一并说明它会在什么条件下失效。

<!-- L1-end -->

<!-- L1 -->

<!-- en -->

## 1 · Events and credibility: a case-by-case audit

### 1.1 A workable framework

"AI has solved a hard mathematical problem" cannot be assessed as a single sentence, because almost every such event is a compound of truth and half-truth. The stable method is to examine each event along five independent dimensions: autonomy, how much key prompting came from humans; verification independence, whether the judges are separate from the producers of the result; formalization status, whether a proof assistant such as Lean has checked it mechanically; transparency, whether prompts, reasoning traces and code are public and reproducible; and one question specific to mathematics, whether the system found an answer that already existed in the literature or generated an argument that did not exist before. The five dimensions are independent; any one of them flashing red changes the character of an announcement. Each event below closes with an explicit verdict stating where it deserves belief and where it must be discounted.

Verification independence can be refined further. Current practice gives three settings. A result is machine-checked when a proof assistant validates a formal artifact and no score can overrule the kernel's verdict; hybrid-graded when such an artifact exists but designated human judges still award the result and may decline it; and community-graded when acceptance depends on an unfixed body of people reading, citing, using or declaring the result admissible [6]. These are descriptions of practice, not a law discovered from a sample, and their use is diagnostic: a dispute can be filed against a derivation, against a formalization, or against the choice of problem, and the three kinds of dispute have different remedies.

Industry itself has begun to separate the autonomy of a result from its weight. In the paper introducing its research agent Aletheia, Google DeepMind proposes an autonomy scale for AI-generated mathematics, graded after the fashion of autonomous driving, and scores mathematical significance separately in five grades, from negligible to milestone [7]. "A highly autonomous triviality" and "a major result produced in deep collaboration" thereby land at opposite ends of the same scale.

<!-- zh -->

## 1 · 事件与信度：一次逐案审计

### 1.1 一套可操作的评估框架

「AI 解决了数学难题」这句话本身无法直接评估，因为这类事件几乎件件都是真假参半的复合体。比较稳妥的做法，是把每起事件放到五个相对独立的维度上分别考察：自主程度，人类给出了多少关键提示；验证独立性，评判者与结果生产方是否分离；形式化状态，是否经过 Lean 这类证明助手的机器检验；透明度，提示词、推理过程、代码是否公开可复现；以及一个专门针对数学研究的追问：这究竟是「找到」了文献里已有的解答，还是「生成」了此前不存在的论证。这五个维度互相独立，任何一个单独亮起红灯，都足以让一次宣布的性质改变。下文在每一个事件的末尾给出显式的信度判级，一句话说清它可信在何处、打折在何处。

验证独立性这一维还可以再细分。现有实践给出三种情形：机器核验，即证明助手验证了一份形式制品，内核的裁决无从推翻；混合核验，即形式制品存在，但指定的评审仍有权授予或拒收；共同体裁断，即接受与否取决于一群没有定编的人去读、去引、去用，或裁定该结果可入 [6]。这三种情形不是从样本里归纳出来的定律，而是对实践的描述；它们的用处在于诊断：一场争执可以针对推导提出，可以针对形式化提出，也可以针对问题的选择提出，而这三类争执需要不同的补救办法。

行业内部已经开始意识到，「自主程度」和「成果分量」必须分开评估。Google DeepMind 在介绍其数学研究智能体 Aletheia 的论文中，提议参照自动驾驶分级，为 AI 生成的数学成果建立「自主研究等级」，并把数学显著性单独分成从「可忽略」到「里程碑式突破」的五个等级 [7]；「高度自主的琐碎结果」与「深度协作的重大结果」因此落在同一条标尺的两端。

<!-- L1-end -->

<!-- L1 -->

<!-- en -->

### 1.2 From silver to gold

In July 2024, AlphaProof and AlphaGeometry 2 solved four of six problems at that year's International Mathematical Olympiad for 28 points, in the silver band, including the hardest problem of the year, which five human contestants completed. The solutions were marked by Fields medalist Timothy Gowers and Joseph Myers and checked in Lean; the peer-reviewed account appeared in Nature in 2026 [8,9]. Two qualifications belong beside the success: human mathematicians translated the problems into a formal language, and some searches ran for up to three days, so the system was not constrained by the four-and-a-half-hour limit that governed the human contestants [9]. Verdict: a genuine result under a stated protocol, high in autonomy and formality, but measured under conditions asymmetric to the human contest; it should be read as the system solving the formalized problems, not as the system sitting the Olympiad.

In July 2025 the picture turned dramatic. OpenAI and Google DeepMind announced almost simultaneously that their systems had reached gold standard at the following Olympiad, each solving five of six problems for 35 of 42 points. The two verification routes form a pair: OpenAI's solutions were assessed by three former medalists who were required to agree [10]; DeepMind's were graded by the official coordinators under the standard applied to human contestants [11]. The International Mathematical Union had asked laboratories to delay publication until after the closing ceremony; OpenAI's proofs appeared earlier, and whether that happened before or after the ceremony remains contested [10,11]. The dispute touched no mathematical content. It concerned the conditions under which the scores were produced. Verdict: the scores themselves are credible, but the worth of the word "gold" turns on verification independence, where the official-coordinator route is clearly stronger; the dispute was procedural, which is itself the point; there was nothing mathematical to contest. One further trade-off is worth recording: OpenAI deliberately declined formal verification this time and solved in natural language instead, on the ground that the resulting capability generalizes better; its gold may therefore be stronger on transferability and weaker on machine-checkability than that of the teams that stayed with the formal route (to be confirmed).

### 1.3 When numbers leave their conditions

Benchmark numbers need more care still, because a number can be true of one thing and quoted for another. In December 2024 OpenAI reported that o3 had solved 25.2% of FrontierMath, a benchmark written by more than sixty mathematicians and released as a preprint [12]. The 75.7% figure widely quoted in the same controversy came from o3's performance on the semi-private ARC-AGI evaluation under a reduced compute budget, and was not a FrontierMath subset score [13]. Both numbers were real, and the controversy arose from their being discussed as though they answered the same question [14]. Verdict: the clearest lesson of the whole record; a number detached from its conditions becomes a different claim, and the most damaging disputes can be about provenance rather than mathematics.

### 1.4 The mechanically checkable end

At the opposite pole sits AlphaEvolve, a coding agent guided by a language model, which in 2025 reported a decomposition of the multiplication of 4 by 4 complex matrices with tensor rank 48, against the rank 49 associated with Strassen's construction, a record standing since 1969, and an eleven-dimensional kissing-number lower bound improved from 592 to 593 [15]. Such results draw far less dispute than competition proofs or research conjectures, because they live at the compute-verify layer: how many multiplications an algorithm uses can be checked mechanically, without any expert's subjective judgement. Verdict: the numbers are objective and credible, but company material without independent certification; the case shows that the controversies AI mathematics provokes cluster not around whether the computation is right but around the zones where a community must judge as a whole.

### 1.5 The Erdős problems: a three-act play

The Erdős open-problem database ran through three acts in under a year, each demonstrating a distinct mode of credibility failure.

Act one, retrieval dressed up as solving. In October 2025 an OpenAI executive claimed on social media that GPT-5 had found solutions to ten previously "unsolved" Erdős problems; the database's maintainer, the mathematician Thomas Bloom, clarified that "unsolved" meant only that he personally knew of no published answer, and that the model had performed excellent literature retrieval (event detail to be confirmed, primary source to be supplied) [16]. Verdict: not fraud, but the packaging of a strong retrieval capacity as "independently solving open problems" is a conflation of two different kinds of thing, and costly once exposed.

Act two, the low-hanging fruit. In early 2026 Terence Tao endorsed a batch of Lean-formalized solutions to Erdős problems whose ideas a model had generated, while separating them sharply from the October episode: they were essentially autonomous and genuinely absent from the literature, yet they were low-hanging fruit, solvable by standard techniques and far from the genuine frontier (event detail to be confirmed) [17]. Tao also reminded the public that a problem unsolved for fifty years often means nobody seriously tried, rather than that people tried and failed for fifty years [17]. Verdict: an acknowledgement of real progress that refuses to inflate its meaning, the most instructive public formulation of the period.

Act three, verification by a distinguished cast. Around May 2026 OpenAI announced that an internal model had disproved the unit-distance conjecture of 1946; nine named mathematicians, including Gowers, then published a paper digesting the construction, and William Sawin separately supplied an explicit lower bound above the exponent in the model's version [18,19]. The new result did not pass in silence because a machine produced it; it passed because people with the relevant expertise read it, sharpened it and wrote the verification down [18]. The same period delivered a warning in the opposite direction: a paper on long-chain Lean autoformalization reported that, with the required algebraic number theory largely missing from Mathlib, an automated system "fabricated" the relevant number-theoretic objects, passed type-checking and CI with placeholder structures, and proved nothing real [20]. Verdict: "Lean-verified" is itself a claim to be interrogated; if key steps are fudged with placeholders, the seal can be hollow, and credibility assessment is never a one-time act.

### 1.6 Generation is easy, verification is not

The First Proof challenge posed ten research-level questions that had arisen in the work of Lauren Williams and collaborators; machine-generated answers were assessed through a process run by its organizers [21]. The public record does not support the confident numbers that circulated in secondary reporting, so this essay makes no claim about how many proofs were correct. The lesson of the episode lies exactly here: the difficulty reported was in evaluation rather than generation [17]. Verdict: as evidence of research-level mathematics, the episode establishes the generation half only; the evaluation half is still in progress, which is the pattern Tao identifies as a verification bottleneck.

### 1.7 A valid derivation, a contested claim

The 2026 Navier-Stokes announcement provides the clearest case of a derivation being correct and the claim being contested. OpenAI published a paper and a Lean formalization of a statement involving a smooth external forcing term, with the artifact public so that anyone can re-check it, and stated that it does not intend to claim the prize [1]. The Clay Mathematics Institute responded that the problem appeared to have been settled, kept its evaluation procedure in force, and continued to list the problem as active [2,4]; its prize rules require publication in a qualifying outlet, at least two years in the literature, and general acceptance by the global mathematics community [3]. A subsequent report argued that the method does not extend to the unforced case the problem asks about [5]. Verdict: the derivation was checked against a specified statement, and what remains open is whether that statement was the problem; formal verification makes the difference sharp, and sharpness is a form of protection.

The same questions are being posed live in theoretical physics, where the line between what a machine proposed and what a human certified is being drawn in public, in two cases. In the first, a 2026 preprint on single-minus gluon tree amplitudes states that its key formula was first conjectured by GPT-5.2 Pro and then proved by a new internal OpenAI model, with the authors reporting hand-checks against the Berends-Giele recursion and confirmation of the soft theorem, cyclicity, Kleiss–Kuijf and the decoupling identities [22]. The second concerns the nine-loop hexagon amplitude in planar N=4 super Yang-Mills theory: Anthropic reported computing it with the bootstrap method, and Lance Dixon, the holder of the previous record, then spent about two weeks validating the result independently, mostly by way of the form factor [23]. The drama had an almost unnoticed side-branch: He Song's team (He Song, Jirong Jing and Xiang Li) at the Institute of Theoretical Physics of the Chinese Academy of Sciences published a concurrent nine-loop result; according to Dixon, the team used GPT-6 to compute part of the constraints while the overall framework was built by humans [23]. Dixon, scooped first by a machine and then by a human-machine pair, joked about it and left a sentence that cuts to the heart of this essay: it is quite a triumph for a large language model to execute all the steps of the complicated recipe and organize the computational horsepower, but "the more soul-searching moments will come when large language models start to come up with new physical principles and insights before humans" [23]. Verdict: neither a preprint nor a company report is a certified result; the value of the cases is that they separate two capacities, a machine executing a recipe that humans specified, and a machine producing the conjecture a proof was then required for; and the nine-loop episode furnished one specimen of each capacity at once, a nearly unsupervised machine solve and a human-machine solve racing in the same arena.

### 1.8 The pattern, and its limits

Read across these cases and a pattern emerges. The disputes that reached the public did not, as a rule, allege that a derivation was formally invalid. They alleged that a problem had been misstated, that a number had been detached from its conditions, that a result had been announced before the community could assess it, or that credit had been assigned to the wrong people. The three settings of certification have corresponding failure modes: a machine-checked derivation fails when the formal statement is not the intended statement; a hybrid grade fails when the human judgement is undisclosed; a community grade fails when a claim enters circulation as established before the people qualified to assess it have done so. The remedies in each case are institutional. Two limits must be stated with the pattern. It describes a small and highly selected set of events, not a law discovered from them, and it is falsified as soon as a documented case appears in which a machine-checked derivation turns out to be wrong [20]. With those limits, the pattern still points to a diagnosis: the main battlefield of credibility is not the derivation but framing, disclosure, attribution and admissibility, which is exactly the ground on which the voices of the next chapter argue.

<!-- zh -->

### 1.2 从银牌到金牌

2024 年 7 月，AlphaProof 与 AlphaGeometry 2 组合在当年国际数学奥林匹克上解出六题中的四题，得 28 分，落在银牌区间，其中包括当年最难的一题，人类选手中仅五人完整做出。解答由菲尔兹奖得主高尔斯与约瑟夫·迈尔斯评阅，并经过 Lean 检查，同行评议的完整记录后来发表在《自然》上 [8,9]。两点限定必须与成绩并列：题目由人类数学家译入形式语言，部分搜索最长跑了三昼夜，系统不受人类选手四小时半赛制的约束 [9]。信度判级：这是一项在明示协议下取得的真实成果，高自主、高形式化，但评测条件与人类考生不对称；应当读作「系统解出了形式化后的题目」，而不是「系统参加了奥赛」。

2025 年 7 月，局面更戏剧化。OpenAI 与 Google DeepMind 几乎同日宣布各自系统达到金牌水准，同样解出六题中的五题、得 35 分。两条路线的验证方式构成一组对照：OpenAI 由三位前奖牌得主评审，评审须达成一致 [10]；DeepMind 则把解答提交给奥赛官方协调员，按人类考生的标准评阅 [11]。国际数学联盟事先要求各实验室把发表推迟到闭幕式之后；OpenAI 的解答出现得更早，是否赶在闭幕式前公布，各方说法不一 [10,11]。这场争执没有触及任何一份解答的数学内容，它争的是分数在什么条件下产生。信度判级：双方分数本身可信，但「金牌」一词的成色取决于验证的独立性，官方协调员路线在这一维上明显占优；争执是程序性的，这正说明数学内容上没有可争之处。尚有一层取舍不可不察：OpenAI 这次特意没有使用形式化验证，而是在自然语言层面直接求解，理由是这样得到的能力更具通用性、更容易迁移；这意味着它的金牌在「可迁移性」上可能占优，在「机器可验证性」上则弱于坚持形式化路线的对手（待审）。

### 1.3 数字脱离条件之后

基准分数需要比竞赛成绩更谨慎，因为一个数字可以属于一项评测，却被拿去说另一件事。2024 年 12 月，OpenAI 报告 o3 解决了 FrontierMath 的 25.2%，该基准由六十多位数学家参与编写、以预印本发布 [12]；同场争议中被广泛引用的 75.7%，是 o3 在缩减算力预算下参加 ARC-AGI 半私有评测的成绩，与 FrontierMath 无关 [13]。两个数字都是真的，风波起于它们被当作同一个问题的答案来讨论 [14]。信度判级：这是全文最清楚的一课，一个数字一旦脱离它成立的条件，就变成了另一项主张；最能伤及信誉的争执，可以完全不来自数学，而出自出处。

### 1.4 可机械核验的那一端

在另一个极端上，2025 年 Google DeepMind 的 AlphaEvolve 提供了一个验证摩擦几乎为零的对照样本：它发现了一种新的四阶复矩阵乘法算法，把标量乘法次数从斯特拉森 1969 年方法的 49 次降到 48 次，打破了一项保持了五十六年的纪录，还把十一维接吻数的下界从 592 推到 593 [15]。这类结果的争议远小于竞赛证明或研究性猜想，原因在于它落在「计算-验证」层面：一个算法用了多少次乘法，是可以不依赖任何专家主观判断、纯粹机械核验的。信度判级：自报数字可信且客观，但材料出自公司、未经独立认证；其意义在于提示我们，AI 数学能力引发的社会争议，往往不集中在「算得对不对」，而集中在需要共同体做整体判断的地带。

### 1.5 Erdős 问题：一出三幕剧

Erdős 未解问题数据库在不到一年里经历了三幕，每一幕各演示一种信度的失效方式。

第一幕，检索冒充解决。2025 年 10 月，OpenAI 一位高管在社交媒体上宣称，GPT-5 找到了十个此前「未解决」的 Erdős 问题的解答，随即引发轩然大波；数据库维护者、数学家托马斯·布洛姆出面澄清，所谓「未解决」只是他个人不知道已发表的解答，模型实际做的是一次出色的文献检索（事件细节待审，来源待补）[16]。信度判级：这不是欺诈，但把强大的检索能力包装成「独立解决未解之谜」，是把两类性质不同的事混为一谈；戳穿之后，对信誉的损害是实打实的。

第二幕，低垂的果实。2026 年初，陶哲轩认可了一批由模型生成思路、由另一系统完成 Lean 形式化的 Erdős 问题解答，但明确把它们与十月的风波区分开：这些解答基本是自主得出的，在文献里确实找不到；它们又是低垂的果实，可以用标准技巧解决，远非真正的前沿难题（具体事件待审）[17]。陶哲轩还提醒公众：一个问题「悬置五十年」，往往意味着没有人认真尝试过，而不是人类尝试并失败了五十年 [17]。信度判级：既承认真实进步、又拒绝夸大进步的意义，这是近两年所有公开表态里最值得学习的表述方式。

第三幕，豪华阵容的核验。2026 年 5 月前后，OpenAI 宣布其内部模型证伪了困扰数学家八十年的单位距离猜想；随后九位具名数学家，包括高尔斯，联署发表论文梳理这一构造，萨温另给出显式下界，其指数优于模型版本中的指数 [18,19]。新结果并非因为出自机器便悄然通过；它之所以通过，是因为一群具备相关专长的人读了它、把它打磨得更为精确、并写下核验 [18]。但同一时期还有一份反向的警示：一篇关于长程 Lean 自动形式化的论文报告，某次形式化尝试因底层代数数论工具在 Mathlib 中几乎完全缺失，自动化系统「伪造」了相关数论对象，用占位符蒙混过关，类型检查通过、CI 也通过，却没有证明任何真实内容 [20]。信度判级：「通过了 Lean 验证」这句话本身需要追问，验证的是什么？如果关键步骤靠占位符敷衍过去，「形式化验证」这块金字招牌就可能名不副实；信度评估从来不是一次性动作。

### 1.6 生成容易，核验难

First Proof 挑战给出十道研究层次的问题，都出自劳伦·威廉姆斯与合作者的真实研究；机器生成的解答由组织者主持的流程评估 [21]。公开记录不支持二手报道里流传的确定数字，因此本文不声称其中有多少证明正确。这一事件的教益正在于此：人们报告的困难在评估而不在生成 [17]。信度判级：作为「AI 能否做研究级数学」的证据，它目前只确立了一半，即生成的一半；评估的一半还在路上；这正是陶哲轩所称的核验瓶颈。

### 1.7 推导正确，主张受质疑

2026 年的纳维-斯托克斯公告提供了最清楚的例子：推导正确，主张却受质疑。OpenAI 公布了一篇论文及一份对应的 Lean 制品，其中形式化陈述含一个光滑的外加强迫项，形式化制品公开可查，使任何人有条件自行核验；公司并明确表示无意申领这笔百万美元奖金 [1]。克雷数学研究所回应「似乎」已解决，评估程序照旧，问题页仍标「未解决」[2,4]；其评奖规则要求发表、在文献中至少停留两年、并获得全球数学共同体的普遍接受 [3]。随后有报道认为，该方法并未推广到问题所问的无强迫情形 [5]。信度判级：推导是就一条明示陈述检查的，未决之处在于那条陈述是否就是所问的问题；形式化让这个差别变得清晰，而清晰本身是一种保护。

同一套问题正在理论物理中被实时提出，这里有两桩案子。第一桩：一篇 2026 年预印本说明，其关键公式先由 GPT-5.2 Pro 提出猜想，再由 OpenAI 一个未公开的新内部模型给出证明；作者报告已对照 Berends-Giele 递推逐项手检，并确认它满足软定理、循环性、Kleiss–Kuijf 与解耦恒等式 [22]。第二桩涉及平面 N=4 超杨-米尔斯理论中的九圈六边形振幅，Anthropic 报告用自举方法把它算出；此前纪录的保持者 Dixon 随后花了约两周独立核验，且主要经由形状因子路径验证 [23]。这出戏还有一个少有人注意的旁支：中国科学院理论物理研究所的何颂团队（何颂、景继荣、李想）几乎同期公布了九圈结果；据 Dixon 所述，该团队用 GPT-6 计算了部分约束条件，整体框架仍由人搭建 [23]。前后被机器与「人机合队」各抢发一次的 Dixon 自嘲之余，留下一句切中本文要害的话：机器执行人类设定的配方并组织计算已是巨大胜利，「但当大语言模型开始在人类之前提出新的物理学原理和洞察力时，那才是更触及灵魂的时刻」[23]。信度判级：预印本不是已认证的结果，公司报告也不是；这两个案例的贡献在于把两件事分得更清楚，机器执行人类指定的配方，与机器给出随后需要证明的猜想，是两种不同的能力；而九圈事件恰好一并给出了这两种能力的两个样本，几乎无人干预的机器独立求解，与人机合力的另一份求解，同场竞技。

### 1.8 小结：规律及其限度

把这一串案例并排看，会显出一种格局：引起公众关注的争执，通常并不指称某份推导在形式上无效，而是指问题被表述错了、数字脱离了成立条件、成果在共同体评估之前就已传开、或者功劳被记在错误的人名下。三种核验情形各有各的失效方式：机器核验在形式陈述不是意图中的陈述时失效，混合核验在人的判断没有公开时失效，共同体裁断在成果以既定事实的身份抢先传开时失效；三者的补救办法都在制度一侧。必须立即加上限定：这是一个规模极小、又经过高度筛选的事件集合，上述观察是对它的描述，而不是从它推出的定律；一旦出现一份有据可查的机器核验推导被证错的案例，该格局即被改写 [20]。带着这层限定，这一格局仍然应当认真对待，因为它指向一个诊断：信度问题的主要战场不在推导，而在框架、披露、归属与可入性。这一点，正好是下一章各路声音争论的底色。

<!-- L1-end -->

<!-- L1 -->

<!-- en -->

## 2 · The voices, and whose crisis it is

### 2.1 The spectrum of voices

The public record of 2024 to 2026 can be sorted into six voices, and each should be read across four registers at once: argument, evidence, logic, and the position and motive behind it. The first two decide whether the claim is right; the latter two decide how its weight should be measured.

The industry voice argues from benchmark scores to approaching general intelligence [1,10]. The argument is not necessarily false; much of the record in the previous chapter is real. But its expressed strength routinely runs beyond what the evidence supports, and the motive is not hidden: mathematics has long stood as the paradigm of objective truth, and conquering it persuades investors that a laboratory is on the road to superintelligence better than any other discipline would [14]. The criterion for reading this voice: the scores are real; the leap from scores to "general intelligence is near" exceeds the evidence. The rival voice, laboratories indicting each other over publication timing and priority [5,11], has a different lesson. A criticism can be entirely sound even when its motive is competitive; the two standard mistakes are to dismiss a substantive charge because the critic has an interest, and to accept it because the critic has a platform. An impure motive does not empty a claim of content.

The careful-scholar voice is defined by the ability to revise judgement as evidence arrives. Tao dismissed the October exaggerations without mercy and three months later endorsed genuinely autonomous results, always attaching the qualifying clause [17]; he has given the present situation a memorable name, "proof indigestion" (press-transmitted, to be confirmed). What such scholars guard is the credibility of collective judgement built up over generations, not the interest of any school or firm. Gowers himself warned the public against the opposite overcorrection: because the problems solved so far were the comparatively easy ones, it would be a mistake to conclude that Erdős's problems in general are mere leftovers nobody bothered with (to be confirmed against the co-signed paper) [18]. Two figures in this register deserve to have their backgrounds stated. David Bessis, trained as a mathematician and now a science writer, argues from his own experience that mathematical intuition is teachable and that the real difficulty is psychological rather than innate; readers weighing his voice must weigh both halves of that double identity [24]. And the formalizers are themselves divided: builders like Kevin Buzzard and Emily Riehl treat Lean and Mathlib as infrastructure for mathematics (to be confirmed), while Peter Scholze, in supporting the Leiden Declaration, insists that the goal of mathematics is human understanding rather than the mechanical generation of correct statements [25]. The same people who know formalization best stand on both sides of the question of what formalization serves.

The institutional voice speaks for the discipline as a going concern. The Leiden Declaration, endorsed by the International Mathematical Union, calls for disclosure, attribution and responsibility in AI-assisted mathematics [25,26]; the European Mathematical Society explicitly declined to endorse it, seeing opportunities as well as risks (EMS position to be confirmed). Its sharpest counterpart is the open letter signed by twenty-five Fields medalists on 11 September 2026, "A Severe Misalignment of AI in Mathematics", whose signatories include Tao, June Huh, Deligne and Scholze. Its programmatic sentence runs: solving problems is merely a tool and a proxy for the fundamental goal (conceptual understanding and insight); using famous problems as showcases for model capability is a severe misalignment. The letter grants that AI could strengthen and accelerate mathematical research and understanding, and asserts that the outcome "will largely be determined by the decisions of the humans who control this new technology" [27]. The letter's immediate context is the succession of machine-proof dramas within a few months: the unit-distance disproof in May, the Jacobian-conjecture counterexample in July, and the Navier-Stokes announcement of 8 September (Jacobian event to be confirmed; source to be supplied) [1,18]. What deserves attention is the letter's precision: its target is not the machine but the display logic that treats problem-solving as the whole of mathematics; one signatory, Smirnov, later used the excavator as his image, faster than the human hand, but capable of destroying precious artifacts (press-transmitted, to be confirmed) [27]. A companion essay, Jun-Yong Park's "Automation Without Understanding", argues that mathematical understanding is a form of infrastructure that cannot be reconstituted on demand, built over generations and weakened by budget cuts and shrinking pipelines at the very moment AI begins producing research-level mathematics, and that it should be treated as a strategic asset [28]. This is anxiety aimed at the long run: a community that can no longer verify, interpret and renew its own results is fragile over time, however many correct theorems it temporarily holds.

The grassroots voice, the anonymous discussants of the Erdős problems forum, asks the most technical questions: is this survivorship bias; can anyone run an experiment with failures reported as well as successes [16,29]? We see only the successful attempt, never knowing how many failures were never made public [29]. It represents no commercial interest and no institutional reputation, which is precisely why it is usually the quietest voice, and the easiest to drown out.

The entangled participant deserves a place of his own, because he is a distinct kind of speaker. Tristan Buckmaster is neither a laboratory spokesman nor a detached commentator. He pursued research at the traditional tempo of the mathematical community and was forced into hurried publication between two competing corporations [5]. According to the competing public accounts reported by Scientific American, Buckmaster and the Anthropic-employed mathematician Levent Alpöge had made the relevant progress by mid-August; the laboratory is said to have proposed that Buckmaster publish alone, excluding Alpöge on grounds of competition, with a response to his threat of publicity that resembled a hint about his career. OpenAI's research lead Bubeck denies the charge as "false and inflammatory" (both accounts press-transmitted; primary statements to be confirmed) [5]. This voice needs no further argument to show that something is changing; the speaker's situation is itself the evidence.

### 2.2 A crisis of mathematics, or of mathematicians

This deserves to be unpacked rather than voted on. Tao's 2026 International Congress report offers the sharpest frame: he sets aside the question of whether AI can do research mathematics, assumes the capacity will arrive, and asks instead what the goals and values of mathematical research are. He calls the situation "a crisis of mathematical value and practice", analogous to the foundational crisis of the early twentieth century, and is explicit that this one is social rather than foundational [17]. Unpacked, the distinction yields four layers. At the layer of truth, whether the Navier-Stokes equations develop singularities in finite time will not depend on whether the prover is human or machine; there is no crisis of mathematics in this sense. At the layer of livelihood, if the speed and cost of proof production change by orders of magnitude, the positions of the people who live by that skill are genuinely reshuffled; this is a real interest and must not be talked away by philosophy. At the layer of trust and institutions, priority, authorship and peer review were designed around a human rhythm, months to write a paper, weeks for referees to read it, a journal queue measured in half-years; the new rhythm is measured in hours, and a laboratory that can field tens of thousands of agents for dozens of hours on work that once took years, while competing commercially, strains the old machinery visibly [1]. The Navier-Stokes episode, with its mixture of rumour, rushing, accusation and denial, is the direct product of old institutions rubbing against the new speed [5]. At the layer of meaning and identity, mathematical research has never been only the production of correct answers; it is also the building of theories, the cultivation of a community and of the next generation, and the making of objects with aesthetic value, and these goals remain unmet when a machine supplies the answer, not because anyone is moving the goalposts but because no single goalpost ever defined the enterprise [17]. This is the deepest layer, and the one institutions can least repair.

The honest summary is therefore: not a crisis of mathematics as a body of truth, but a structural adjustment of mathematics as an institution, a livelihood, a trust mechanism and a practice of meaning, made acute because questions of truth, credit, livelihood and meaning, which could once be handled one at a time, have been compressed into the same weeks. The diagnosis has its own limit: it leaves the word "crisis" entirely on the side of the institution, which may be generous to its members and lenient to the institution itself. Testing it requires not more positions but the kind of clearing the next chapter performs on mathematics itself.

<!-- zh -->

## 2 · 众声喧哗与危机诊断

### 2.1 众声的谱系

把过去两年公开发声的各方按其位置归类，大致可以分出六种声音。评估每一种声音，都应当把它拆成四个层面分别审视：论证、论据、逻辑，以及其背后的立场与动机。前两者决定这话对不对，后两者决定这话的分量该如何称量。

产业鼓吹型。以各实验室的高管和研究负责人为代表，论证结构通常是「我们在公认的高难度基准上取得了突破性分数，这标志着通用智能正在临近」[1,10]。这个论证未必虚假，前章梳理的不少成果确实真实；但它表达的强度往往普遍超出证据所能支撑的范围。动机链条并不隐蔽：数学长期被视为「客观真理」的典范，攻克它，比攻克任何其他学科都更能说服投资人，自己正走在通向超级智能的路上 [14]。评估准则：分数是真的，从分数到「通用智能临近」的跳跃，超出证据。竞争攻讦型。以同行实验室之间的相互指摘为代表，表现为围绕 IMO 2025 发布节奏的隔空交锋，以及围绕纳维-斯托克斯优先权的正面冲突 [5,11]。这类声音的特点在于：批评即便出于竞争动机，指控内容本身也可能完全站得住脚。评估此类声音时最容易犯的谬误有两种：不能因为批评者别有用心就自动否定批评的实质，也不能因为批评者手握话语权就自动采信。动机不纯不等于言之无物。

审慎学者型。以陶哲轩、高尔斯这类身处共同体核心、又持续跟进 AI 进展的资深数学家为代表。这类声音最显著的特征是随证据调整判断的能力：陶哲轩在十月对夸大宣传毫不留情地否定，三个月后对真正自主、真正原创的结果给予明确肯定，并始终坚持在肯定之上附加限定 [17]。他甚至给眼下的局面起了一个传神的说法：「证明消化不良」（媒体转述，待核）。这类学者守护的，是那套需要长期积累才能建立起来的集体认知的可信度，而不是某个流派或机构的利益。高尔斯本人还特意提醒过舆论：不要因为此前那些「容易得多」的问题被机器解决，就反过来轻视 Erdős 问题的整体难度，那同样是一种矫枉过正（出处以联署论文为准，待核）[18]。这一类型中另有两位人物，其背景不可略去。一位是数学出身、转行科学写作的贝西斯，其论证以亲身经验为据，主张数学直觉是可教的、数学的困难主要在心理而不在天赋；这个背景本身要求读者在权衡他的声音时，把他「数学共同体内部出身、科学传播者立场」的双重身份一并计入 [24]。另一处分化尤须留意：巴扎德、里尔这类形式化倡导者把 Lean 与 Mathlib 视为数学的基础设施（待审），而肖尔策在支持《莱顿宣言》时强调的则是，数学的目标是人的理解，而不是机械地生成正确的陈述 [25]。同一批「懂形式化的人」，在「形式化服务于什么」上站到了两边。

建制/政策型。以《莱顿宣言》及其背书格局为典型：国际数学联盟予以背书，欧洲数学学会则明确拒绝背书，理由是不只看到风险，也看到机会（EMS 表态待审）[25,26]。这类声音的核心关切既不是「AI 能不能做数学」，也不是抢占话语权，而是数学共同体作为一种社会建制能否延续：培养体系是否还能培养出足够多能够理解、审核、教授、推进这些成果的人。同一类型的另一极，是二十五位菲尔兹奖得主于 2026 年 9 月 11 日发表的联名公开信《AI 在数学中的严重目标错位》，签署者包括陶哲轩、许埈珥、德利涅、肖尔策等。信中的纲领性判断是：解题只是达成根本目标（概念理解与洞察）的工具与代用指标；把名题当作模型能力的展示标尺，是「严重的错位」。信亦承认 AI 有「加强并加速数学研究与理解」的潜力，并断言其最终损益「将在很大程度上取决于掌控这项技术的人类的决定」[27]。这封信的直接语境，是数月之内接连上演的机器证明大戏：五月的单位距离反例、七月的雅可比猜想反例，以及 9 月 8 日的纳维-斯托克斯宣布（雅可比事件待审：来源待补）[1,18]。这封信的分寸感颇堪细读：它反对的不是机器，而是把解题当作数学全部目标的那套展示逻辑；签署者之一斯米尔诺夫事后以挖掘机为喻，说它快是快，却可能「毁坏珍贵的文物」（媒体转述，待核）[27]。另有一篇题为《没有理解的自动化》的论文，出自数学家 Jun-Yong Park 之手，把「数学理解能力」本身视为一种基础设施：平时无人在意，一旦缺失则处处塌方，其培养不可按需重建，因此应视同半导体一类的战略资产 [28]。这是面向长时段基础设施的忧虑，其逻辑基础是：一个不再有能力自我验证、自我更新的共同体，即便暂时拥有再多正确的定理，长期而言也是脆弱的。

草根方法论型。以 Erdős 问题论坛里那些追问「这到底是不是幸存者偏差」「能不能做一次提前公布、允许失败案例一并汇报的对照实验」的匿名讨论者为代表 [16,29]。这类声音技术含量最高、立场最中立，因为他们既不代表商业利益，也不承担机构声誉，纯粹从统计推断和实验设计的角度追问证据的分量：我们看到的永远是成功的那一次，而不知道背后有多少次失败从未被公开 [29]。遗憾的是，这类声音往往声量最小，最容易被淹没。

被卷入当事人型。布克马斯特应专辟一段，因为他是一种很独特的声音。他既不是实验室代言人，也不是纯粹的旁观评论者；他原本按照数学共同体的传统节奏推进研究，却因为身处两家巨头企业竞争夹缝而被迫仓促发表、卷入公开纠纷 [5]。据《科学美国人》报道的双方公开说法，布克马斯特与供职于 Anthropic 的数学家阿尔珀热早在 8 月中旬就已取得相关进展，对方曾提议由他一人单独署名，把阿尔珀热排除在外，理由竟是竞争关系；当他表示要公开时，得到的回应近似于职业前途的暗示性威胁。OpenAI 一方的研究负责人 Bubeck 则否认这一指控，斥之为「虚假且具煽动性」（两造说法均系媒体转述，一手声明待核）[5]。这一类型不需要额外的论证技巧来证明「有些东西正在被改变」，当事人的处境本身就是证据。

### 2.2 是数学的危机，还是数学家的危机

这是一个需要认真拆解、而不是简单选边的问题。陶哲轩在 2026 年 7 月国际数学家大会的报告里给出了一个极具启发性的框架：他刻意避开了「AI 到底能不能做研究级数学」这个争论最激烈的问题，转而假定这种能力终将到来，然后追问一个与此正交的问题：数学研究真正的目标和价值到底是什么。他用了相当罕见的沉重措辞，形容眼下是「一场关于数学价值与实践的危机」，并把它类比为二十世纪初那场促使数学家把隐含预设明确化的基础危机，并明确指出：这一次的危机性质是社会性的，而非基础性的 [17]。

把这个区分往下拆，至少可以看到四个层次。其一，真理层面。纳维-斯托克斯方程是否会在有限时间内产生奇点，这一问题的答案不会因为证明者是人还是机器而改变；数学命题的真假不依赖于发现者的身份。就此而言，不存在「数学的危机」。其二，职业与生计层面。如果证明的生产速度、生产成本发生数量级变化，依赖这一技能谋生、晋升、获得声望的具体的人，处境确实会被重新洗牌；这是实实在在的利害关系，不该被哲学思辨轻轻带过。其三，信任与制度层面。优先权认定、署名规范、同行评议这套运转了几个世纪的社会机制，是围绕人类研究节奏设计的：几个月写一篇论文，几位审稿人读上几周，期刊再排半年队；而新速度是几十个小时。当一家企业可以用上万个智能体在几十小时内完成过去需要数年积累的工作、又是一场激烈商业竞争的当事方时，原有的信任机制会显得力不从心 [1]。纳维-斯托克斯事件里那种混杂了传言、抢发、指控、否认的混乱局面，正是旧制度和新速度相互摩擦的直接产物 [5]。其四，意义与身份层面。陶哲轩特别强调，数学研究从来不只是「解出正确答案」这一件事，还包括发展新理论新技巧、理解世界、维系一个共同体、培养下一代数学家、积累可传承的知识、创造具有美学价值的作品；这些目标即便在机器给出正确解答之后依然没有得到满足，不是因为人在刻意移动球门，而是因为任何单一的球门本来就不足以概括数学这项事业的全部意义 [17]。这是最深的一层，也是最难用制度修补的一层。

因此，如果一定要用一句话回答「是数学的危机还是数学家的危机」，比较贴切的说法或许是：这不是数学作为一套真理的危机，而是数学界作为一套建制、一种谋生方式、一套信任机制、一种意义生产实践正在经历的结构性调适；这种调适之所以剧烈，正因它把真伪、归属、生计、意义这几个原本可以分开处理的问题，在极短时间内捆绑到了一起，让当事人来不及一层一层地厘清。当然，这个诊断本身也有它的限度：它把「危机」一词全部留给了建制，这可能对建制里的人过于慷慨，也可能对建制本身过于宽容；要检验它，需要的不是更多的立场，而是下一章那样对数学本身的一次清理。

<!-- L1-end -->

<!-- L1 -->

<!-- en -->

## 3 · What mathematics is

Before asking whether AI can do mathematics, it is worth asking what mathematics is, because the answer supplies the intuition behind every position in the debate.

### 3.1 Its place in the system of knowledge

Three relations fix the position of mathematics among its neighbours, and each must be stated head-on. Mathematics and logic: logicism attempted to reduce all of mathematics to pure logic, and the programme failed on Russell's paradox and kindred difficulties [30]; the lesson, often misread, is not that mathematics is logic but that logic is its grammar, not its ground; the question of which founds the other receives a more radical answer in Gödel, held over for now. Mathematics and the empirical sciences: Wigner marvelled at the "unreasonable effectiveness" of mathematics in the natural sciences [31], and the marvel is exact; Riemannian geometry, proposed half a century earlier, turned out to be the language general relativity needed, as if mathematics had stocked the vocabulary before physics asked for it. The resonance between physical and mathematical structure is real, but resonance is not one-way grounding; the sciences feed mathematics new problems and mathematics returns new languages, the two instruments calibrating each other, not a foundation with a building on it. Mathematics and natural language, the relation easiest to overlook: mathematical concepts borrow bodily metaphors wholesale, "greater than", "contains", "approaches", all spatial words, and the embodied-cognition tradition of Lakoff takes such projection as constitutive rather than incidental [30]. de Bruijn proved the same point from the other end with AUTOMATH: a large part of mathematical writing can be rearranged into a grammar a machine can parse, but the rearrangement preserves the logical form while discarding nearly everything else, what the notation suggests, which equivalent statement was treated as natural, why a hypothesis was unnecessary [32]. A formal text is a partial representation, and the part it omits is the part readers use to judge whether a problem has been posed well. The three relations together yield a picture: mathematics neither rules over logic, science and language nor bows beneath them; it sits at their junction, shaped by all three and constraining all three in return.

### 3.2 Seven ontological positions

About the nature of mathematics there are seven principal positions. Platonism treats mathematical objects as independent of mind and discovery as the mathematician's work; formalism treats mathematics as symbol manipulation under convention, with truth as derivability; logicism tried to reduce mathematics to logic; intuitionism and constructivism require objects to be constructed in the mind before they exist, and refuse the law of excluded middle its unconditional reign over the infinite; structuralism studies relations and structures themselves; embodied cognition roots concepts in bodily experience; and the social-historical view, of which Lakatos's Proofs and Refutations is the classic, holds that concepts and proof standards are themselves shaped in the dialectic of conjecture, counterexample and revised definition [30,33].

No single position persuades everyone, which already shows that the question has no settled answer. More important, each position carries its own intuition about AI: if mathematics is a territory awaiting discovery, then who or what discovers it is in principle irrelevant; if it is rooted in bodily experience, whether a bodiless system can understand mathematics becomes a harder question than whether it can produce correct answers. Most of the intuition-divergence in the AI debate has its source in this layer. The sketch is necessarily crude; every position has refined modern versions, but its purpose is a map of the intuitions, not a verdict on them.

### 3.3 Is mathematics the ultimate ground of everything

One extreme view promotes mathematics to the position of ultimate ground, what philosophy's old name calls the first cause: Tegmark's mathematical universe hypothesis claims that physical reality simply is a mathematical structure, with nothing more basic left to explain [34]. The lineage runs back to Pythagorean "all is number" and to Galileo's book of nature written in the language of mathematics.

But mathematics contains the strongest refutation of its own self-sufficiency, and it is a technical result rather than a philosophical one. Gödel's incompleteness theorems show that any consistent formal system rich enough to express elementary arithmetic contains true statements it can neither prove nor disprove, and that such a system cannot establish its own consistency; doing so requires a stronger metasystem, whose consistency in turn requires a still stronger one, in an open-ended ascent [35]; Lucas and Penrose built famous arguments on these theorems [36,37]. Cohen then proved the continuum hypothesis independent of the Zermelo-Fraenkel axioms, showing that even the most foundational-looking branch has axiomatic choices that are not uniquely forced [38]. If mathematics cannot supply itself with a closed, self-completing foundation, then "mathematics is the first cause" holds only in a localized sense, relative to some particular formal system, and cannot be promoted to a cosmological assertion. Mathematics resembles less a tower standing on a foundation that needs no foundation than a relational network without a single origin, in which every node is defined and warranted by other nodes, a figure to which the final chapter returns.

### 3.4 The four forces that shape mathematics

If mathematics is not self-grounding, what shapes it? Four forces at least. Logic, though Gödel showed deduction cannot exhaust mathematical truth. The applicability to physical reality, Wigner's effectiveness again [31]. Human cognition and bodily experience, which is why we speak of abstract relations in spatial vocabulary. And historical and cultural contingency, the most underestimated: Newton and Leibniz invented calculus independently, which suggests that certain structures emerge almost inevitably once external conditions are ready, yet the notation that surfaced carries the marks of its time and person; Leibniz's symbols survive, Newton's "fluxions" were abandoned by history [39,40]. Students today recognize only Leibniz's notation; the same calculus wore two faces, and one of them became "natural". The content of mathematics may carry necessity; its form was never uniquely destined.

### 3.5 The limits of mathematics

The limits are technical as well. Turing's proof that the halting problem is undecidable showed that some well-defined questions admit no algorithm that handles every input [41,42]. Together with Gödel's results, this ended the Hilbertian hope that formalization could exhaust mathematics: a formal system can neither prove its own consistency nor mechanically decide all questions. Formalization remains valuable, as Lean and Mathlib demonstrate daily [6], but it is an instrument and a facet of mathematical practice, not its whole definition. Between mathematical language and the structure mathematics means to grasp there is always a seam, and the seam is where intuition and aesthetic judgement live, the source of the mathematician's familiar feeling that a formally flawless proof can still fail to explain.

### 3.6 Where new questions and new theories come from

New theories have come into being along a small number of routes. Distillation from the concrete to the abstract, from millennia of land measurement to the Euclidean axioms, visible in the sourcebook Katz assembled from five traditions [43]. Analogy and generalization, from integers to rationals, reals and complexes, each step driven by asking what survives if some property is kept and another relaxed. Pressure from outside: physics demanding a language for continuous change [39], communication engineering begetting information theory, quantum mechanics begetting branches of functional analysis, and modern cryptography posing ever-new questions to number theory. And the dialectic of error and refutation that Lakatos reconstructed for Euler's polyhedron formula, in which the very concepts of vertex, face and polyhedron were redefined under the impact of counterexamples [33]. The conclusion common to these routes is that posing a good problem or a good theory was never an activity that pure deduction can exhaust; it depends on aesthetic judgement about what is interesting and on a sense of historical context. Pólya set the solving of a problem out as a cycle of understanding, planning, execution and checking [44], and Hadamard added that an attempt must be reorganized until it becomes readable [45], points the fifth and sixth chapters will need.

<!-- zh -->

## 3 · 数学是什么

在讨论「AI 能不能做数学」之前，更该先追问一个经常被绕过去的问题：我们所说的「数学」，到底是什么。这个问题不是书斋里的空转，因为它直接决定「AI 与数学」之争里每个立场的直觉来源。

### 3.1 数学在知识体系中的位置

要回答数学是什么，先回答它不在哪里、它与邻居的关系。至少有三层关系需要正面说清。

数学与逻辑。逻辑主义曾试图把全部数学还原为纯粹逻辑，这一宏大纲领因罗素悖论等困难而未能完全实现 [30]。但这个失败留下了一个常被误读的教训：数学不等于逻辑，却处处以逻辑为骨架；逻辑不是数学的地基，而是数学的语法。二者谁奠基谁的问题，在哥德尔那里会得到一个更彻底的回答，这里暂不展开。

数学与经验科学。物理学家维格纳曾感叹，数学在描述自然规律时展现出「不合理的有效性」[31]。这种有效性至今引人深思：黎曼几何在被提出半个多世纪之后，恰好成为广义相对论所需要的语言，好像数学在物理需要它之前就预先备好了词汇。它提示物理世界的结构与数学结构之间存在某种深刻的呼应，但呼应不等于单向奠基：经验科学不断向数学输送新问题，数学不断向经验科学返还新语言，二者更像一对互相校准的仪表，而不是地基与大厦。

数学与自然语言。这是最容易被忽略的一层。数学概念大量借用空间与身体的隐喻：「大于」「包含」「靠近」，这些词都源自方位经验；莱考夫一系的认知语言学家主张，数学概念根植于人类身体与感知运动经验中的隐喻投射 [30]。de Bruijn 的 AUTOMATH 计划从另一端证明了同一件事：数学书写中相当大的一部分可以重新安排为机器能解析的文法，但这种重新安排保留了论证的逻辑形式，舍弃了几乎所有其余内容，记号里隐含的意图、被认定为自然的表述、某个假设为何不必写出 [32]。形式文本只是数学文本的部分表示，而它略去的那部分，正是读者用来判断问题提得是否妥当的部分。

这三层关系合起来给出一幅图景：数学既不凌驾于逻辑、科学与语言之上，也不屈居于它们之下；它处在三者的交汇处，由三者共同塑形，又反过来约束三者。

### 3.2 七种本体论立场

关于数学的本性，哲学史上有七种主要立场。柏拉图主义认为数学对象独立于人类心智而客观存在，数学家的工作是发现而非发明；形式主义主张数学是依照约定规则操作符号的游戏，「真」只是「可从公理推出」的同义词；逻辑主义试图把数学还原为逻辑；直觉主义与构造主义认为数学对象只有在心智中被明确构造出来才算存在，拒绝排中律在无穷领域的无条件适用；结构主义主张数学研究的是关系与结构本身；具身认知视角主张数学概念根植于身体经验；社会建构与历史主义视角，以拉卡托斯的《证明与反驳》为代表，强调概念与证明标准本身是在「提出猜想、发现反例、修正定义」的历史辩证中被塑造出来的 [30,33]。

这七种立场彼此张力巨大，却没有一种能单独说服所有人；这本身就说明「数学是什么」远不是一个有共识答案的问题。更重要的是，每一种立场都对应着一种关于「AI 能不能做数学」的不同直觉：如果数学是等待发现的客观疆域，谁去发现、用什么工具发现，原则上并不重要；如果数学根植于身体经验，那么一个没有身体的系统能否真正「理解」数学，就成了一个远比「能否算出正确答案」更棘手的问题。AI 之争里各方的直觉分歧，大半可以在这一层找到源头。当然，这七种立场的速写必然失之于粗，每一种立场内部都有精细的现代版本；但速写的目的不是判决，而是标出直觉分歧的地图。

### 3.3 数学是万物的终极根据吗

有一种极端的看法把数学推上万物终极根据的位置，用哲学的旧名称说，即所谓「第一因」：物理学家泰格马克的「数学宇宙假说」主张，物理实在本身就是一个数学结构，除此之外再无更基础的东西需要被解释 [34]。这条线索可以上溯到毕达哥拉斯「万物皆数」的古老直觉，以及伽利略「自然这部大书是用数学语言写成的」著名论断。

但数学内部正藏着一个对这一自足性最有力的反驳，而且它来自数学自身最严格的技术性成果。哥德尔不完备定理表明：任何一个足够丰富、能表达基本算术的一致形式系统，必然存在在该系统内既不能证明、也不能证伪的真命题；更进一步，这样的系统甚至无法在内部证明自身的一致性，要证明它一致，必须诉诸更强的元系统，而那个元系统的一致性又需要更强的系统来担保，如此层层外推，没有尽头 [35]；卢卡斯与彭罗斯对哥德尔的著名援引另见 [36,37]。科恩其后证明连续统假设独立于策梅洛-弗兰克尔集合论公理系统，进一步说明即便集合论这样看似最基础的数学分支，其公理本身也存在并非唯一必然的选择空间 [38]。

把这个技术性事实推而广之：如果数学连给自己一个自洽、封闭、自我完成的基础都做不到，那么「数学是万物的终极根据」这一说法，大概只在非常在地化的、相对于某个具体形式系统的意义上成立，而不能推广为终极的宇宙论断言。数学更像一张没有单一起点、每个节点都依赖其他节点才能被定义和证成的关系网络，而不是一座建立在无需地基的地基之上的高塔。这个意象，留到第七章再做全面展开。

### 3.4 塑造数学的四种力量

如果数学不是自我担保的终极根据，那么是什么在为它划定边界、塑造它的走向？至少有四种力量在共同起作用。逻辑当然是其中之一，但哥德尔已经说明逻辑推演无法穷尽数学真理的全部。物理实在的可应用性是第二种强大的塑造力，维格纳的「不合理有效性」就是它的见证 [31]。人类认知与身体经验是第三种，我们借用空间词汇谈论抽象关系，绝非偶然。历史与文化偶然性是第四种，也最常被低估：牛顿与莱布尼茨各自独立发明微积分，说明某些结构一旦外部条件具备，就会以近乎必然的方式浮现；但它浮现出来的记号系统、表述方式、侧重点带着鲜明的时代与个人烙印，莱布尼茨的记号沿用至今，牛顿的「流数」说法早被历史淘汰 [39,40]。今天的学生只认识莱布尼茨的微积分符号，几乎没人知道牛顿的记号长什么样；同一个微积分，两副面孔，其中一副流传成了「自然」的样子。数学的内容或许有其必然性，但数学的形式从来不是唯一注定的。

### 3.5 数学的边界

除了哥德尔揭示的不完备性，图灵证明的停机问题不可判定性揭示了另一重边界：存在界定明确的问题，原则上不存在任何算法能对所有输入给出答案 [41,42]。这两项结果合在一起，构成对「形式化能够穷尽数学」这一希尔伯特式宏愿最沉重的打击：形式系统既无法证明自己的一致性，也无法机械地判定所有问题的可解性。这并不意味着形式化毫无价值，恰恰相反，Lean 与 Mathlib 这类工具的现实效用有目共睹 [6]。但它意味着，形式化终究只是数学实践的一种工具和一个侧面，而非数学的全部定义。数学的语言与数学真正想要把握的结构之间，始终存在缝隙；这道缝隙，正是数学直觉、审美判断得以安身立命之处，也是「证明在形式上无懈可击，却依然让人觉得没有真正说明白问题」这一数学家常有的感受的根源。

### 3.6 新问题与新理论从何而来

回顾数学史，新理论的诞生大体循着几条路径。其一，从具体到抽象的提炼：从测量土地的千年经验，到欧几里得的公理体系，卡茨的源典汇编了五个传统各自认为值得写下来的问题，看的就是这种提炼 [43]。其二，类比与推广：从整数到有理数、实数、复数，每一步都靠「如果保留某些性质、放松另一些性质会怎样」的类比式追问推动。其三，外部问题的倒逼：物理学对连续变化的描述催生微积分 [39]，通信工程催生信息论，量子力学催生泛函分析的若干分支，现代密码学对数论提出的新问题更是层出不穷。其四，错误与反驳的辩证：拉卡托斯细致重构了欧拉多面体公式在反例冲击下被一步步修正、其中「顶点」「面」「多面体」等概念本身也被重新定义的历史 [33]。

这几条路径共同指向一个结论：提出一个好问题或一套好理论，从来不是单纯的逻辑推演能够穷尽的活动，它高度依赖对「什么是有趣的」「什么方向可能有回报」的审美判断和历史语境感。波利亚把解决数学问题写成理解、拟定、执行、检验的循环，阿达玛则补上相关的一点：尝试必须重新组织，直到它变得可读 [44,45]。这一点在第五、第六两章会被反复用到。

<!-- L1-end -->

<!-- L1 -->

<!-- en -->

## 4 · Who the mathematician is

### 4.1 Birds, frogs, and other roles

The mathematician is not one kind of person, and the debate regularly forgets this. Dyson's famous image divides mathematicians into birds, who survey wide territory from above in search of unifying pictures, and frogs, who dig into the mud of a specific problem [46]. A second axis separates the competition solver, who cracks hard problems inside an existing framework; the paradigm builder in Grothendieck's manner, who erects a new conceptual language in which previously unrelated problems suddenly make sense together; the synthesizer, who unifies scattered results; and the expositor, who transmits hard mathematics to the next generation. Gowers's distinction between theory-building and problem-solving is the canonical statement of the same observation inside the discipline [47]. The profession is also stratified institutionally: a small apex of figures with enormous standing, a large middle of teaching researchers, and a substantial population of mathematically trained people in industry, finance, cryptography and machine learning. The stratification is not a reproach; it is a reminder that "the mathematician" of this debate has never been a homogeneous person.

### 4.2 What contemporary mathematicians do

The visible surface of contemporary research is extreme specialization; two professors in the same department may not be able to read each other's papers; overlaid by a few grand programmes that seek unity across subfields. The Langlands programme is the most famous: it conjectures deep correspondences between number theory, representation theory and harmonic analysis, has drawn the strongest minds for decades, and its non-abelian form is the heart of arithmetic geometry, seen by many as a "unified field theory" blueprint for mathematics, with modular forms as the shared language bridging the two shores [48]. Around it lie the great contemporary territories of moduli spaces, p-adic geometry and arithmetic algebraic geometry, of which Deligne's proof of the Weil conjectures is the landmark [49]. On the analytic side sit the regularity theory of nonlinear partial differential equations and the Navier-Stokes problem itself [1]. Additive combinatorics remains alive in the lineage of Zhang's bounded gaps between primes and Chen's theorem [50,51]. And in the last two years a new branch has begun growing in place: AI mathematics has become an object of mathematics itself, with formalization, benchmark design and verification methodology all live research topics [6,21,29]. The daily work of the contemporary mathematician is far more varied than the stereotype of solitary thought at a blackboard; collaboration, cross-disciplinary exchange and working with computational tools have long been the norm.

### 4.3 Why mathematics became a byword for intelligence

The social binding of mathematics to intelligence and talent deserves dissection, because it is the first mental habit to break before the sixth chapter can ask who is capable of originative work. Historically, mathematics has long served as the sorting instrument of education systems, from the imperial examination's arithmetic to the post-Sputnik investment in science, so that mathematical marks became a proxy for general intelligence and even national competitiveness, and this institutional use in turn shaped the public intuition about the link. Psychologically, mathematics has right and wrong answers where the humanities allow many readings, and this hardness makes the skill look solid and unforgeable, lending it a special cognitive authority. Cognitively, survivorship bias does heavy work: the public remembers Ramanujan and Gauss, not the countless researchers of equal effort and lesser luck [52]; the halo effect spreads mathematical skill into presumed general wisdom, as if solving equations conferred competence in statecraft, investment and everything in life; and information asymmetry amplifies the mystique, since most people cannot judge the truth or weight of a mathematical claim, and the gap breeds awe rather than assessment. Socially, in many East Asian societies, competition mathematics has long been coupled to advancement and social mobility, loading mathematical ability with social capital far beyond the discipline itself (an interpretive observation; the literature to be supplied). The empirical record supplies the underside of the myth: a meta-analysis of 177 studies and more than 900,000 students found mathematics anxiety negatively associated with achievement and tightly related to other forms of anxiety [53], and a second meta-analysis confirmed the robust negative association [54]. Mathematical performance is not a pure reading of abstract reasoning; it is the joint product of prior education, familiarity, working memory, confidence, anxiety, cultural expectation and task format. These factors together produce a nearly essentialist myth of the "mathematical brain", as if the ability were an inborn gift of a few rather than a skill that responds strongly to training. One counterweight against overstatement: mathematical ability is real and valuable, and individual differences are real; the error lies not in acknowledging difference but in smuggling a specialized skill into the general currency of personhood and wisdom.

<!-- zh -->

## 4 · 数学家是何种人

### 4.1 鸟、蛙与其他角色

数学家不是一种人，而这场争论经常忘记这一点。物理学家戴森有一个广为流传的比喻：数学家可以分为「鸟」与「蛙」，鸟从高处俯瞰辽阔疆域，寻找连接不同领域的统一图景；蛙深入具体问题的泥土，在细节中掘进 [46]。这个比喻之外还可以从另一个维度区分：有的数学家擅长在已有框架内解决高难度具体问题，即竞赛型、问题求解型；有的擅长搭建全新概念框架，让一大批此前互不相干的问题突然可以在同一种语言下被重新理解，即格罗滕迪克式的范式建构型；有的擅长把分散结果整合成连贯体系，即综合型；有的致力于把艰深的数学清晰传授给下一代，即阐释型、教育型。高尔斯关于理论建构与问题解决两种文化的著名区分，是这一观察在数学内部的正式说法 [47]。

在建制层面，数学家群体同样高度分层：少数处于金字塔尖、享有极高声望的领军人物；大量在高校和研究机构从事教学与研究的普通学者；还有相当一部分在工业界从事应用性工作的数学训练者，金融、密码学、机器学习里都有他们。这个分层本身并不丢人，它只是提醒我们，本章与第六章要讨论的「数学家」从来不是一个同质的人群。

### 4.2 当代数学家在做什么

当代数学研究的一个鲜明特征是高度专业化与碎片化，数学分支细化到即便同一个数学系的两位教授，彼此的研究内容也可能很难互相看懂细节。与之并存，也有一些跨越众多子领域、致力于寻找统一图景的宏大纲领。朗兰兹纲领是最著名的例子：它猜想数论与表示论、调和分析之间存在深刻的对应关系，几十年来持续吸引着最顶尖的头脑，其非阿贝尔版本至今是算术几何的核心，被不少人视为当代数学的「统一场论」蓝图；横跨两岸的桥梁，模形式，本身就成了数论与几何共享的语言 [48]。与它毗邻的，是围绕模空间、p-进几何、算术代数几何展开的大片当代工作，德利涅对韦尔猜想的证明正是这片疆域的里程碑 [49]。在分析一侧，非线性偏微分方程的正则性问题、纳维-斯托克斯方程本身，占据了另一个中心 [1]。加法组合学因为张益唐的有界素数间隙与陈景润定理的谱系而持续活跃 [50,51]。而最近两年，一个新的分支正在原地生长：AI 数学本身成了数学的对象，形式化、基准设计、核验方法论都是活的研究题目 [6,21,29]。

可以说，当代数学家的日常工作远比公众想象中「独自在黑板前苦思冥想」的刻板印象多元：协作、跨学科交流、与计算工具共同工作，早已是常态。

### 4.3 数学何以成为「聪明」的代名词

数学与「智力」「天赋」之间那种近乎本能的社会联想，应当拆解一下背后的成因，因为它是第六章重新审视「谁能提出开创性理论」时，必须首先破除的思维定式。

历史成因上，数学长期在教育体系中扮演筛选与分层的角色，从科举时代的算学到冷战「卫星危机」后对理工科的举国投入，数学成绩一直被当作衡量整体智力甚至国家竞争力的代理指标，这种制度化用法反过来塑造了公众对数学与智力关系的直觉。心理成因上，数学问题通常有明确对错，不像人文议题容许多元阐释，这种「非黑即白」的确定性让数学能力显得格外坚实、难以伪装，从而被赋予一种特殊的认知权威。认知偏差层面，幸存者偏差起了很大作用：公众记住的永远是拉马努金、高斯这类天才叙事，却看不到无数付出同等努力而未能突破的普通研究者 [52]；光环效应让人们不假思索地把数学能力泛化为「聪明」甚至整体性的品格优越，好像解得出方程的人自然懂得治国、投资与生活的一切道理；信息不对称进一步放大迷思，绝大多数人根本没有能力评判一项数学声明的真伪或分量，这种能力上的巨大落差，反而催生了一种反向的敬畏甚至神秘化倾向。社会成因上，在许多东亚社会，数学竞赛成绩长期与升学、阶层流动挂钩，数学能力因而被赋予了远超学科本身的社会资本含义（此系解读性观察，具体文献待补）。

实证研究为这一迷思的破除提供了底座。一项涵盖 177 项研究、逾九十万名学生的元分析发现，数学焦虑与成绩负相关，并与其他形式的焦虑紧密相关 [53]；另一项元分析同样确认了这一稳健的负相关 [54]。数学成绩不是一个纯粹的「抽象推理能力读数」，它是先前教育、熟悉度、工作记忆、信心、焦虑、文化期待与题型共同作用的产物。这些因素叠加在一起，共同催生了一种近乎本质主义的「数学脑」迷思，好像数学能力是少数人与生俱来、不可习得的天赋，而非一种高度依赖训练投入、可以后天大幅提升的技能。反诘一句以免过头：数学能力是真实的、可贵的，个体差异也是真实的；错不在承认差异，而在把一种专项能力偷换成人格与智慧的统称。

<!-- L1-end -->

<!-- L1 -->

<!-- en -->

## 5 · Formalization, computation, and division: is AI really inferior to mathematicians

### 5.1 Three layers of mathematical activity

"Does AI fall short of mathematicians?" is unanswerable until "doing mathematics" is decomposed. Three layers at least. Mechanical computation, numerical work and symbolic simplification, were conceded to machines long ago with calculators and computer algebra. Proof search inside a given formal system, the search for a path through a large but bounded space toward a stated goal, is a structured search problem, exactly the terrain on which reinforcement learning and large compute are strongest, and the recent progress of systems like AlphaProof sits largely here [8]. And the posing of problems themselves, judging what is worth asking, which direction has promise, what structure a conjecture hides, a layer that depends on aesthetic intuition, historical context and cross-domain association, for which no clean objective function yet exists as a reinforcement signal.

The industry's own data appear to echo the layering: in Aletheia's two-axis scheme of autonomy and significance, higher autonomy tends to come with lower mathematical significance, and the results that matter still cluster in the human-machine collaborations rather than the fully autonomous cases [7]. The pattern is preliminary and awaits more data, but it fits the three layers.

### 5.2 An honest answer that remains open

So, on the sharp question: in rationally analyzable, formalizable settings, is AI really inferior to mathematicians at proposing, thinking about and solving mathematical problems? In all honesty, the evidence so far supports no categorical verdict in either direction. On the proof-search layer, the speed of progress has surprised even senior mathematicians who thought such things a decade away: gold-standard Olympiad performance and some research-level results arrived within a remarkably short window [8,10,18,21]. On the other side, nearly every result acknowledged as significant, from the unit-distance disproof to the Navier-Stokes breakthrough, became a mathematical achievement only through deep human involvement in checking, digesting and contextualizing it [1,18]. A proof becomes knowledge only when a community capable of digesting, simplifying and verifying it takes it in; until then it is a correct symbol sequence and nothing more.

The more precise statement is therefore: in the relatively narrow but increasingly central subdomain of clearly specified goals with mechanically checkable correctness, AI already executes at a level comparable to the best humans and often faster; in the wider layer of deciding what is worth doing and what counts as important, for which no agreed metric yet exists, human experts still play an irreplaceable role. Whether that role is temporarily or in principle irreplaceable, nobody can say with confidence, and every categorical claim, "AI will never truly create" or "human mathematicians will soon be obsolete", runs beyond the evidence. The answer satisfies neither side: the partisans of "AI has won" find it too cautious and the partisans of "machines never understand" find it too generous; it is precisely this honesty, leaving both uncomfortable, that is its only virtue.

### 5.3 How the division of labour should evolve

Short of a final answer, the practical arrangements have a standing reference: the history of the calculator and the computer algebra system. The tools did not make mathematicians unemployed; they took over tedious computation and freed attention for conceptual construction and problem choice. The lineage runs further back, through Wang's programme, Robinson's resolution calculus, Newell and Simon's symbol search, AUTOMATH, McCune's solution of the Robbins problem and Hales's verification of the Kepler conjecture: machines have been absorbing the checking and the executing, and humans have been moving on [32,55,56,57,58,59]. AI extends the same pattern one layer up, taking on much of the proof search and the heavy routine labour of formalization.

The workable arrangements are already visible: humans set direction and make the aesthetic call that something is worth digging into; AI runs large, intensive searches and formalizations within that direction; humans read the candidates, decide whether they matter and connect to existing theory; AI absorbs the literature review and lemma work that used to consume graduate students, freeing scarce senior attention for the layers that need intuition and judgement. Such arrangements have already occurred in practice: a research problem is decomposed into components, the components requiring routine execution of known technique are handed to a model, and the human concentrates on the part requiring high-level creative reasoning, a workflow Tao has described and practised [17].

The institutional half of the division is equally indispensable. Five rules, stated here because they are the other half of any division of labour: laboratories should disclose every attempt symmetrically, including the failures and the zeros, because a record of successes alone writes survivorship bias into history [12,14]; certifiers should be designated before results are announced, so that the grader and the graded have no chance to collude [10,11]; admissibility should be registered separately from derivation, stating explicitly which proposition was established and whether it was the problem asked [3]; verification should be paid as professional labour; the multi-year work of Hales's team on the Kepler conjecture is its price tag, and the labour remains among the lowest-paid in the discipline [59]; and evaluation should be kept separate from generation, because generation is a search problem while evaluation is a problem of reading, translating, checking and contextualizing, and a benchmark that mixes the two measures the wrong thing [12,29]. Each rule is cheap to state and expensive to run, and the expense falls on people with no stake in any particular score; that is why the arrangement is not self-enforcing, and why a rule not written down before an announcement tends not to survive the announcement.

### 5.4 Rationality, formalization, computability, quantifiability and logic

The vocabulary of the debate needs separating as well. Rationality is not formalization: formal logic is one part of rationality, which also includes choosing what to measure, deciding which variables matter, recognizing analogies, deciding what counts as evidence, appraising relevance and allocating attention, activities that can be rational without reducing to a finite proof calculus. Computability is not tractability: the Church-Turing thesis ties intuitive effective procedures to Turing computability, but "computable" does not mean "feasible"; some functions are computable only with infeasible resources and some are uncomputable altogether [41,42]. The ladder formalizable, computable, tractable, searchable, discoverable in practice does not collapse: a theorem can have a short proof inside an enormous search space, and a statement can be decidable in principle and unreachable in computation.

Quantifiability deserves its own clause, because it is not the same as computability and its history is far shorter. Quantification, the conversion of qualitative judgement into numbers and measures, is a comparatively recent cognitive operation; the project of governing the world by turning it into numbers was assembled by modern states, science and industry together [60]. It brought mathematics and modern society enormous power, and a characteristic bias with it: a number gains authority by precision, and precision makes it portable; once portable, it travels without the conditions that made it meaningful. The 25.2% FrontierMath figure and the 75.7% ARC-AGI figure were both real, and the controversy arose from their being discussed as though they answered the same question [12,13,14]. That is the standard form of quantification bias: the number was not wrong; it was moved out of its context. Mathematics is both master and object of quantification; the first role nobody doubts, and the second has just been demonstrated by the AI industry itself.

Placed against the inner and outer faces of mathematics, the map becomes tidy: the intension of mathematics, definitions, axioms, deductions, invariants, is the home ground of formal systems and of AI's clearest advantage; the extension, scientific questions, physical reality, technological need, human purpose, places the criteria of evaluation beyond the reach of formal validity. Logic, formalization and computability are the skeleton on which mathematics can be mechanically verified; the flesh, aesthetic judgement, historical context, the intuition that something is worth studying, still lies outside the skeleton's coverage. Whether that state is permanent or merely reflects formalization not yet found is open. Penrose argued from Gödel that human mathematical understanding has a component no formal system can simulate; the argument has been widely criticized; most of the logic and computer science communities hold that its use of Gödel is mistaken, but the controversy itself shows that whether human mathematical intuition is computation remains unsettled [37]. History offers an optimistic precedent: Kolmogorov axiomatized "probability", a fuzzy pre-formal notion, and Turing formalized "effective procedure", a pre-formal intuition, and both turned vagueness into an exact discipline [41,61]. The seam between the pre-formal and the formal that looks impassable today has been crossed repeatedly; but every crossing changed the problem itself rather than abolishing intuition.

### 5.5 Is Western mathematics the whole of mathematics

Almost certainly not, and it is worth saying in what sense. The modern mathematics written into textbooks, with peer review and axiomatic deduction as its standard form, is largely the historical confluence of the Euclidean axiomatic tradition and the nineteenth- and twentieth-century European institutionalization of mathematics, later universalized through colonial history and global education, so that it is now easily mistaken for the only possible shape of the concept. The coexisting independent traditions were built on different emphases. Classical Chinese mathematics, above all the Nine Chapters, prized algorithm and practical computation, and the achievements of Liu Hui and Zu Chongzhi in pi and volume computation ran along a constructive, algorithmic path rather than an axiomatic one, Zu Chongzhi's close approximation of pi preceding the comparable European result by over a millennium [43,62]. Indian mathematics contributed the place-value system and the zero that reshaped the notation of mathematics itself, and the Kerala school derived results equivalent to infinite series expansions centuries before Newton and Leibniz, without developing a systematic calculus in the later European sense [43,63]. The scholars of the Islamic golden age systematized algebra and preserved and extended the Greek geometric heritage, and al-Khwarizmi's name survives in the word "algorithm" [43]. Martzloff and Plofker organize their histories around reasoning and structure, and around the decimal positional notation and an algebra conceived as a general method, showing that the differences lie less in content than in arrangement: which objects are treated as primitive, which notation is used, and above all what warrants a solution [62,63]. A computational procedure presented without axioms is not thereby an invalid proof; it is a different answer to the question of what makes a solution count. None of this denies the power of the modern paradigm, its unification and rigour are real; it denies only that modern mathematics is mathematics as such; a historical and local construction mistaken for universal necessity. There is a further irony: Wu Wen-tsun built his mechanical geometry theorem proving in the twentieth century explicitly on the algorithmic strand of the Chinese tradition [64]. A tradition pushed to the margin of the mainstream narrative proved its contemporaneity precisely in the age of machine proof. The detail plants a thread for the final chapter's wider view.

<!-- zh -->

## 5 · 形式化、可计算性与分工：AI 真的不如数学家吗

### 5.1 数学活动的三个层级

要回答「AI 是否不如数学家」，首先必须承认「做数学」不是一件单一的活动，至少可以拆成三个层级：机械计算，即数值运算、符号化简，这一层早在计算器与计算机代数系统时代就被机器全面超越；在给定形式系统内搜索证明，即已知目标命题、在庞大但边界清晰的证明空间中寻找路径，这是结构化搜索问题，恰是强化学习与大规模算力最擅长的领域，AlphaProof 等系统近两年的进展主要在这一层 [8]；提出问题本身，即判断什么问题值得问、这个方向是否有前途、这个猜想背后可能隐藏怎样的结构，这一层高度依赖审美直觉、历史语境感与跨领域联想，目前没有清晰的目标函数可以做强化学习的奖励信号。

耐人寻味之处在于，行业内部的数据似乎也隐约印证着这个分层：Aletheia 的自主性与显著性二维评估体系呈现出「自主程度越高、成果的数学显著性反而越低」的倾向，真正意义重大的成果目前仍更多地出现在人类与 AI 紧密协作、而非 AI 完全自主的案例中 [7]。这只是初步的、有待更多数据检验的经验模式，但它恰好呼应上面的三层划分。

### 5.2 一个尚无定论的正面回答

那么回到那个尖锐的问题：在可以被理性分析、形式化处理的场景下，AI 提出、思考、解决数学问题的能力，难道真的不如数学家吗？平心而论，截至目前，证据不支持任何方向的斩钉截铁答案。一方面，在第二层上，AI 近两年展现的进步速度已经让许多此前认为「至少还要十年」的资深数学家感到意外：竞赛数学金牌水准、部分研究级问题的自主解决，都发生在极短的时间窗口内 [8,10,18,21]。另一方面，举凡真正被承认为「重大」的成果，从单位距离猜想的证伪到纳维-斯托克斯的突破，都是在人类专家的深度参与、审核、语境化解读之下才最终成型的，离开这层人类参与，这些结果甚至无法被恰当地「理解」为一项数学成就 [1,18]。一个证明只有被一个能够消化、简化、验证它的人类共同体所吸纳，才真正转化为知识，而不只是一段冰冷的、正确的符号序列。

所以更诚实的回答或许是：在「给定清晰目标、可机械验证正确性」这个相对狭窄却越来越关键的子领域里，AI 已经具备了与顶尖人类相当甚至更快的执行力；但在「决定什么值得做、什么才算真正重要」这个更宽泛、目前仍缺乏明确评价标准的层面上，人类专家依然扮演着不可替代的角色。而这个角色究竟是「暂时不可替代」还是「原则上不可替代」，目前没有人能给出有充分把握的答案；任何斩钉截铁的断言，无论「AI 永远无法真正创造」还是「人类数学家很快就会过时」，都超出了现有证据所能支撑的范围。这个回答注定让两边都不满意：主张「AI 已经赢了」的人嫌它保守，主张「机器永远不懂数学」的人嫌它暧昧；而这份让两边都不舒服的诚实，正是它目前唯一能声称的美德。

### 5.3 分工应如何演化

如果不追求终极答案，而是着眼于眼下务实的分工安排，历史上一个现成的参照系是计算器与计算机代数系统的普及史：这些工具没有让数学家失业，而是把他们从繁琐的手工计算中解放出来，把精力集中在概念构建和问题选择上。这条线的起点其实更早：从王浩的机械判定方案、罗宾逊的归结演算、纽厄尔与西蒙的符号搜索，到 AUTOMATH、麦库恩解决罗宾斯问题、黑尔斯完成开普勒猜想的核验，机器一直在接手「检查」与「执行」的工作，人则相应转移了阵地 [32,55,56,57,58,59]。AI 系统很可能延续这一模式，但把解放的层级再往上推一级：不仅解放机械计算，也开始承接相当一部分证明搜索与形式化的繁重底层劳动。

由此可以想见几种切实可行的分工模式：人类负责提出方向、给出「这个值得深挖」的审美判断，AI 负责在给定方向内做大规模、高强度的搜索与形式化；人类负责对 AI 产出的候选结果做语境化解读，判断它是否真正重要、能否与既有理论体系产生有意义的连接；AI 逐渐承担起本来需要大量博士生、博士后投入的文献综述与引理证明工作，让稀缺的顶尖人类精力流向真正需要直觉与判断的环节。这种分工早已在个别案例中真实发生过：把研究问题拆解为组件，把需要熟练执行既有技巧的组件交给模型完成，自己专注于需要高层次创造性推理的部分，陶哲轩在论 AI 时代的数学时描述并实践过这类工作流 [17]。

制度侧的配套同样缺一不可。这里把五条规则再列一遍，因为它们说的是分工的另一半：实验室应对称披露每一次尝试，包括失败与零分，因为只报告成功会把幸存者偏差写进历史 [12,14]；认证者应当在结果公布之前指定，让评阅者与作答者无从合谋 [10,11]；可入性应当与推导分别登记，明示「确立的是哪条命题、是不是所问的问题」[3]；核验应当作为专业劳动取得报酬，黑尔斯团队为开普勒猜想付出的多年专门劳动就是这份劳动的价码，而这类劳动至今是学科里报酬最低的一档 [59]；评估应当与生成分开，因为生成是搜索问题，评估是阅读、翻译、核查与置入语境的问题，把两者混在一份基准里，测的是错误的东西 [12,29]。这五条规则说出口都便宜，做起来都贵，而费用落在与任何具体分数都没有利害关系的人身上；这正是它们不会自我维持的原因，也是为什么不在宣布之前写下的规则往往撑不过宣布那一刻。

### 5.4 理性、形式化、可计算、可量化与逻辑

现在进入那组经常被混用的概念。理性不等于形式化：形式逻辑只是理性的一部分，理性还包括选择测什么、决定哪些变量要紧、识别类比、决定什么算证据、评估相关性、分配注意力；这些活动可以是理性的，却不能还原为有限的证明演算。可计算也不等于易解：丘奇-图灵论题把直观的「有效程序」与图灵可计算性联系了起来，但「可计算」并不意味着「实际算得动」，有些函数原则上可算却需要不可行的资源，有些则根本不可算 [41,42]。所以「形式化、可计算、易解、搜得到、实践中可发现」是一条不塌缩的阶梯：一个定理可以有很短的证明却有巨大的搜索空间；一条陈述可以原则上可判定却在计算上不可达。

「可量化」应当单独加以辨析，因为它和「可计算」不是一回事，而且它的历史短得多。量化，即把定性判断转成数值或度量，是一种相当晚近的认知操作；把世界变成数字来治理，是近代国家、科学与工业共同塑造出来的技艺 [60]。它给数学与现代社会带来巨大的力量，也带来一种特有的偏差：数字因为精确而获得权威，精确又使它便于转手；一旦便于转手，它便脱离使它有意义的条件。FrontierMath 的 25.2% 与 ARC-AGI 的 75.7% 都是真的，风波起于人们把二者当作在回答同一个问题 [12,13,14]。这就是量化偏差的标准形态：不是数字错了，而是数字被从语境里搬走了。数学本身既是量化的主人，也是量化的对象；前一个身份无人置疑，后一个身份则刚被 AI 行业自己演示了一遍。

把这些概念放回数学的内外两侧，会得到一张比较整齐的地图：数学的内涵，即定义、公理、推导、不变量，是形式系统的主场，也是 AI 优势最明显的地带；数学的外延，即科学问题、物理实在、技术需要、人的目的，则让评价标准超出形式有效性的射程。逻辑、形式化、可计算，构成了数学得以被机械核验的骨架；但数学的血肉，即审美判断、历史语境感、「这值得研究」的直觉，目前仍游离在这套骨架的覆盖范围之外。至于这种游离是永久性的，还是仅仅因为我们尚未找到合适的形式化方式，眼下依然是开放问题。彭罗斯曾借助哥德尔不完备定理论证，人类数学理解存在无法被任何形式系统完全模拟的成分；这一论证在逻辑学界与计算机科学界受到广泛质疑，主流观点认为它对哥德尔的援引存在误用。但这场争论本身正说明，人类数学直觉的本质究竟是不是一种计算，至今仍未解决 [37]。历史上有一个乐观的参照：柯尔莫哥洛夫把「概率」这个前形式的模糊概念公理化，图灵把「有效程序」这个前形式的直觉概念形式化，都曾让一片混沌变成精确的学科 [41,61]。这提示我们，前形式与形式之间那道今天看起来不可逾越的缝隙，在历史上曾被一次次跨过；但过去每一次跨过都改变了问题本身，而不是简单地消灭了直觉。

### 5.5 西方数学是数学的全部吗

这个问题的答案大体可以肯定是否定的，但应当说清「否定」在何种意义上成立。今天被写入教科书、以期刊同行评议与公理化演绎证明为标准形态的现代数学，很大程度上是欧几里得式公理演绎传统与十九、二十世纪欧洲数学建制历史性汇流的产物，后来又通过殖民历史与全球教育体系被普遍推广，以至于今天很容易把它误认为「数学」这个概念唯一可能的样貌。但历史上并存的多个独立数学传统，其侧重点与这套范式相当不同。中国古代数学以《九章算术》为代表，高度重视算法与实用计算，刘徽、祖冲之等人在圆周率、体积计算上的成就走的是构造性、算法化的路径，而非公理化演绎；祖冲之的密率领先欧洲同类结果上千年 [43,62]。印度数学不仅贡献了位值制与「零」这一改变整个数学记号系统的概念，喀拉拉学派更是在牛顿、莱布尼茨之前的几个世纪就得到了若干等价于无穷级数展开的结果，只是没有发展出后来欧洲意义上的系统化微积分框架 [43,63]。伊斯兰黄金时代的学者则在代数方法的系统化、以及对古希腊几何遗产的保存与拓展上做出关键贡献，花拉子米的名字至今仍留在「算法」（algorithm）这个词里 [43]。马茨洛夫与普洛芙克的史学著作，分别从推理方式与结构、从十进位值制与「作为一般方法的代数学」入手组织材料，说明差别不只在于内容，更在于安排：哪些对象被当作原始项、用哪一套记号、以及最要紧的，一份解答凭据什么而成立 [62,63]。

一个没有公理支撑的计算程序，并不因此就是无效的证明；它是对「什么使一份解答算数」的另一种回答。承认这一点，并不是要否定现代数学范式的强大威力，它确实展现出了空前的统一性与严谨性；而是要提醒：把现代数学等同于数学的全部，本身是把一种历史性、地方性的建构误认成了普遍必然。更有意味的是，二十世纪的吴文俊正是从中国传统数学的算法脉络里汲取灵感，做出了机械化的几何定理证明 [64]。一条被主流叙事边缘化的传统，在机器证明时代反而重新证明了自己的当代性。这个细节为第七章的整体视野埋下了一条引线。

<!-- L1-end -->

<!-- L1 -->

<!-- en -->

## 6 · What counts as originative

### 6.1 Defining the term

Some mathematicians hold that a machine cannot construct an originative theory or pose an originative problem. The claim cannot be assessed before the term is fixed, because as ordinarily used it is a compliment rather than a criterion. A checkable definition: a question or a line of work is originative relative to a field at a given time when three conditions hold. It is not derivable from what the field already had. Answering it changes what the field can do, not merely what it can say about what it could already do. And it was not already latent in the literature in a form a competent reader could have extracted. The third condition matters most, because it makes originativity a claim about the state of a literature rather than about the mind of an author. Two mathematicians can therefore be given the same credit, and a mathematician and a system the same verdict: what is assessed is a relation between a question and a body of work, so who is capable of it has no purchase until that relation is established. Measured by this standard, calculus for the description of physical change, analytic geometry for the junction of algebra and geometry, group theory for the characterization of symmetry, and category theory for the abstraction of structural relations themselves all belong to the class.

### 6.2 Scarcity and supply

It is also worth asking whether originative work is available to mathematicians in general. It is not, and the cases already discussed show why. The pool from which originative questions are drawn is not the set of all questions but a stock, filtered by what a field has already established and replenished from contact with something outside mathematics: measurement, instruments, administration, trade, craft. Bounded gaps between primes and Chen's theorem each redirected a decade of work, and Green's account of the parity barrier explained why a family of near-miss methods had stopped rather than proposing a new theorem [50,51,65]. Problem selection is itself a mathematical act, not the neutral input to a procedure; what each major tradition transmitted is a curated sequence of questions, and the criteria of curation are mathematical criteria [16,43]. A field with a narrow stock has a correspondingly narrow supply of originative questions.

### 6.3 The multiple identities of the originators

The names usually offered against the claim make a far longer list than a mere handful, and no exhaustive list is needed; take the most representative of them, and on inspection they support the opposite reading. The logical role of the examples deserves a sentence: they are not meant to establish, by enumeration, that originators are always boundary-crossers, which would be a hasty generalization; they are meant to falsify the universal claim that only mathematicians can be originative, and a universal claim falls to a few counterexamples. Descartes was first a philosopher pursuing a universal method for all knowledge, and analytic geometry was the by-product of his larger ambition of taming geometry with algebra; on the record, his 1616 degree from Poitiers was in law, he held no mathematics degree and no university post, joined the army of Maurice of Nassau at twenty-two in engineering duties, and his mathematics came largely from correspondence with Beeckman, his teacher rather than his peer [66]. Newton's calculus was born of the physical problem of motion, and in the first book of the Principia he names Wren, Hooke and Halley as having observed the same fact [39]; the time he spent on alchemy and biblical chronology was no less than his time on mathematics and physics (to be confirmed). Leibniz was at once philosopher, diplomat, historian and jurist, and his notation for the calculus was an offshoot of his lifelong project of a universal symbolic language for all human reasoning [40]; the notation still in use descends from that almost mystical scheme. Gauss, the most "pure" of the group, computed the orbit of Ceres as an astronomical problem, was led to the intrinsic geometry of surfaces by his participation in land surveying, studied geomagnetism with Weber, and, doctorate notwithstanding, never held a chair of mathematics; his appointment was as professor of astronomy and director of the Göttingen Observatory [67]. The later examples are just as dense: Riemann's geometric intuition was inseparable from his thinking about physical space; Poincaré was a pioneer of the psychology of mathematical creation, and his essay on the subconscious incubation of discovery remains a standard text on mathematical creativity [68]; von Neumann spanned mathematics, physics, economics and computer science; Turing's work interwove logic, morphogenesis and cryptanalysis [41]. The message of the list is consistent: originative breakthroughs rarely arise from strict observance of the discipline's boundary, and more often from its frontier zones with philosophy, physics, engineering and beyond. The necessary qualification: breadth alone is insufficient. Every one of these figures also possessed ferocious technical depth; Newton without his almost obsessive geometric rigour could not have written the Principia, and Grothendieck's abstraction was unthinkable without decades of training. The accurate statement is that originative work is produced at the junction of breadth and depth, not by either alone: pure technique without cross-domain vision makes incremental progress inside the paradigm, and cross-domain inspiration without technique cannot even state its ideas clearly.

### 6.4 A more productive way of asking

This finding reframes the question about AI. If the historical regularity is a junction of breadth and depth rather than ever-deeper drilling inside one narrow discipline, then the right comparison is not whether a narrow-domain system trained to solve competition problems and prove lemmas has creativity, but whether a wide-domain system trained across nearly the whole of human knowledge has in principle the structural potential for a Cartesian or Leibnizian synthesis. The question has no current answer, and it is closer to the heart of the matter than "will AI prove the Riemann hypothesis". It also carries an observation about the present: the AI results judged most important so far were achieved not by inventing new concepts from nothing but by novel combinations and transfers of existing deep tools [18], which is a real and underestimated form of creativity; much of Newton's and Leibniz's own work was likewise the synthesis and recombination of earlier scattered insights. Originativity may never have been a binary zero-to-one property but a continuous spectrum, with the great leaps at its extreme. That extreme still belongs to humans, but whether that is due to a mysterious property unique to humans and in principle beyond machines, or merely to the fact that present systems have not been granted exploration broad, deep and autonomous enough, the question is far from settled. The organizers of First Proof themselves concede that mathematics includes posing new questions and building frameworks, and that no concrete protocol yet exists for measuring whether a system does so autonomously [21]. The honest verdict is therefore not that "machines cannot be originative" is false, but that it is unestablished, and that the reason is institutional rather than mathematical.

<!-- zh -->

## 6 · 什么是「开创性」

### 6.1 界定「开创性」

有些数学家主张，机器不可能构建开创性的理论，也不可能提出开创性的问题。这项主张必须先固定术语才能评估，因为「开创」在日常用法中是赞美而不是判准。一个可核查的定义是这样的：一个问题或一条研究路线，相对于某一领域在某一时刻是开创性的，须同时满足三项条件。其一，它不能由该领域已有的成果推出；其二，对它的回答改变了该领域能做什么，而不只是改变了它对自身已有能力的说法；其三，它也不是早已潜伏在文献中、以至于有能力的读者本可提取出来的形式。第三项条件最要紧，因为它使开创性成为关于一份文献状态的断言，而不是关于作者心智的断言。两位数学家可以得到同样的评价，一位数学家与一个系统也可以得到同样的裁决：被评估的是一个问题与一批工作之间的关系，所以「谁有能力提出它」在这项关系确立之前无从置喙。

用这个标准回看数学史：微积分之于物理变化描述、解析几何之于代数与几何的贯通、群论之于对称性的刻画、范畴论之于结构关系本身的抽象化，都属于这一类。

### 6.2 开创性工作的稀缺与供给

还该追问一句：开创性的工作，是所有数学家都能做的吗？不能。开创性问题可行的池子并不是所有问题的集合，而是一批存量：由这个领域已经确立的东西筛选而成，并靠着与数学之外的某种东西接触来补充，测量、仪器、行政、贸易、手艺。素数间隙有界结果与陈景润定理各自改写了一个十年的方向，而格林对奇偶障碍的说明解释了一整类差一点奏效的方法为什么停了下来 [50,51,65]。问题选择本身是数学行为，不是程序的中性输入；每一种重要传统传下来的文献，都是一份经过筛选的问题序列，筛选的依据是数学标准 [16,43]。存量窄的领域，开创性问题的供给也相应地窄。

### 6.3 开创者的多重身份

反对者常举出一批名字来证明「只有数学家才能开创」。这份名单远不止寥寥数人，也无需穷举；取其中最有代表性的几位，细查之下，他们反而支持相反的读法。这里先须说清这一论证的逻辑角色：它不是要用几个例子归纳出「开创者必是跨界者」，那会是以偏概全；它要证伪的是「开创只属于数学家」这一全称命题，而证伪一个全称命题，几个反例就足够了。笛卡尔首先是一位哲学家，他毕生追求一种能够统摄全部知识的普遍方法论，解析几何的诞生是他试图用代数驯服几何这一更宏大哲学抱负的副产品；细看履历，他 1616 年在普瓦捷取得的是法学学位，既无数学学位，也从未拥有大学教职，二十二岁加入拿骚的军队，所任职务偏于工程，数学功夫主要来自与贝克曼的通信，在数学上后者是教他的人而非同伴 [66]。牛顿的微积分诞生于对物体运动这一物理问题的直接需要，他在《原理》第一卷中还点名雷恩、胡克与哈雷，说这三人都已观察到同一事实 [39]；而他耗费在炼金术研究与《圣经》年代学考证上的时间精力，丝毫不亚于他在数学与物理上的投入（待审）。莱布尼茨兼为哲学家、外交官、历史学家、法学家，他发明微积分记号，背后是他毕生追求一种能表达全部人类理性推理的「通用符号语言」这一更大规模的哲学工程 [40]；今天仍在使用的微积分符号系统，正是那个颇带神秘色彩的普遍语言构想的分支产物。高斯看似是最「纯粹」的数学家，但即便如此，他对谷神星轨道的计算是天文问题，对大地测量的参与直接催生了他关于曲面内蕴几何的开创性工作，与韦伯合作研究地磁，而且他虽有博士学位却从未取得数学教职，被任命的是天文学教授兼哥廷根天文台台长 [67]。稍晚的例子同样密集：黎曼的几何直觉与他对物理空间本质的思考密不可分；庞加莱本人就是科学哲学与数学创造心理学研究的先驱，他那篇关于数学发现中「潜意识酝酿」的经典论述至今仍是理解数学创造力的重要文献 [68]；冯·诺依曼横跨数学、物理、经济学与计算机科学；图灵的工作交织着数理逻辑、生物形态发生与密码学 [41]。

这份名单传递的信息相当一致：真正意义上的开创性突破，似乎极少诞生于对「数学」这一学科边界的严格恪守之中，而更多诞生于数学与哲学、物理、工程乃至神学等其他领域的交界地带。当然，这里必须加上一个重要限定，以免滑入另一种简单化：广博的跨领域视野本身并不足够，这些人物无一例外兼具极为扎实的技术功力。牛顿若没有严谨到近乎苛刻的几何论证能力，单凭物理直觉写不出《原理》；格罗滕迪克那种令人生畏的抽象建构能力，离开经年累月的技术训练同样无从谈起。更准确的表述应当是：开创性突破往往产生于广度与深度的交汇处，而非二者中的任何一者单独作用的结果。纯粹的技术专精而缺乏跨领域视野，大概率只能在既定范式内做增量式的推进；而缺乏扎实技术训练的跨界灵感，往往连表述清楚都做不到，更遑论严格证明。

### 6.4 换一个更有生产力的问法

这个发现恰好为「AI 能否提出开创性理论」提供了一个更有生产力的重新表述。如果开创性突破的历史规律确实是「广度与深度的交汇」，而不是「在数学这一狭窄学科内部越钻越深」，那么真正该追问的比较对象，就不应该是「一个专门被训练来解竞赛题、证引理的窄域 AI 系统是否具备创造力」，而应该是：一个在人类几乎全部知识上完成训练的广域系统，理论上是否具备某种在结构上类似于笛卡尔、莱布尼茨式跨领域综合能力的潜质？这是一个目前完全没有确定答案、但明显比「AI 会不会证明黎曼猜想」更接近问题本质的追问。

它亦提示一条现实的观察：至少就目前而言，那些被认为最重要的 AI 数学成果，并非靠「从头发明全新概念」取得，而是靠对既有深刻工具做出人类此前未曾设想过的新颖组合与迁移取得的 [18]。这本身也是一种真实的、不该被轻视的创造力形式；历史上牛顿与莱布尼茨本人的很多工作，追根溯源同样是综合、重组前人已有的零散洞见，而非纯粹的无中生有。或许「开创性」从来就不是一个非此即彼的「从零到一」式概念，而更像一个连续的谱系；人类历史上最伟大的那几次跃迁恰好发生在谱系的极端。这个极端目前依然只属于人类，但无论把它归因于「人类特有、机器原理上不可企及」的神秘属性，还是仅仅归因于「目前的 AI 系统尚未被赋予足够广阔、足够深入、足够长期自主的探索空间」，现有证据都远不足以定论。First Proof 的组织者自己就承认，数学研究包括提出新问题与发展框架，但目前缺少测量系统自主完成这一阶段的具体实验方法 [21]。诚实的裁决因此不是「机器不可能开创」为假，而是它尚未确立，且原因出在制度而非数学。

<!-- L1-end -->

<!-- L1 -->

<!-- en -->

## 7 · Summary and a view from above

### 7.1 Gathering the threads

Gathered together, the six chapters describe a single woven figure. In the Navier-Stokes episode a technical truth, a commercial race, an authorship dispute and a priority quarrel were compressed into the same September week [1,5]. Asked whether mathematics is the ultimate ground of everything, the discipline's own strictest theorems answered, almost against intuition, that it cannot supply itself with a closed foundation, and that every truth is warranted by something outside the system. Unwrapped from its packaging of genius, the mathematician turns out, at the moments of genuine origin, to be a person carrying several identities at once. And the question of whether AI falls short of mathematicians cannot be answered apart from the older questions of what mathematics is, where creativity comes from and who assigns meaning.

### 7.2 Process, prediction and mutual constitution

The threads point to one structure: Be it mathematics itself, the identity of the mathematician, or the categories of human and machine, nothing that is pushed to the bottom yields a core that can stand alone. The truth of a theorem depends on an open-ended chain of axiomatic choices and metasystem guarantees; the greatness of a mathematician depends on a world woven from philosophical puzzlement, physical observation and historical accident; and the question of whose achievement a proof is opens, on inspection, into employment, non-compete clauses, lineages of teachers and the unfinished conjectures of a previous generation. No node is an isolated cause; every node is at once the result of countless others and the condition of the next.

Two nameable intellectual resources describe this figure without dissolving into vague sentiment. Whitehead's process philosophy holds that reality is process rather than substance, that each entity becomes itself through its relations to everything in its environment, and that each moment of actual existence prehends and integrates the whole past world [69]. The active inference framework and free-energy principle of Friston propose that every activity of a cognitive system, from perception to action, is a continuous generative prediction of the world with the minimization of prediction error, and that the boundary between system and environment is not given in advance but is continually redrawn by the system's own generative model [70]. What is called understanding, on this account, is not a static mirror of external facts but the process of a system generating and revising its own model of the world; the boundary between model and world is under permanent renegotiation. The two resources, eight decades and two disciplines apart, point at the same structure: the whole is given before the parts, the parts gain identity inside the whole's relations, and the whole is continually reconstituted by the relations among the parts. Leibniz's monads gave the structure a poetic version three centuries ago: the monads have no windows, yet each mirrors the same universe [71].

Placed over the present debate, this structure dissolves the either-or of crisis versus breakthrough. A proof becomes knowledge because a community able to understand it digests, questions and teaches it; a mathematical tradition becomes visible in its particularity and its limits through comparison with other traditions; an "AI victory", inspected closely, is always carried by a multitude of earlier human works, by the reviewing eyes of human experts, even by earlier competition and cooperation among humans. Crisis and breakthrough are not two external, mutually exclusive entities but two sides of one unfolding web momentarily lit up: the same structure that carries the machine's advance also carries the institution's instability, which is why both are visible at once. The Fields medalists' letter in fact touches this structure at its close: whether AI strengthens or damages mathematics "will largely be determined by the decisions of the humans who control this new technology" [27]. Even the sharpest critics, that is, do not hand the outcome to the technology; they hand it back to people.

### 7.3 Concrete stakes are not dissolved by the wide view

One caution must be added immediately, against misusing this whole view: none of it makes the participants in the authorship dispute a jot less wronged [5], nor dissolves the anxiety of a doctoral student about a career. The concrete interests of the moment remain real and remain to be honoured, and the wide view must not be allowed to dissolve them. Its use lies elsewhere, in a steadier posture: no need to declare the dusk of a discipline because a machine computes faster, and no need to declare the dawn of an era because a score is impressive. Whether "crisis" or "breakthrough", what is happening is a node of this mutually constitutive web being lit up for a moment, while the web itself continues its silent expansion in every direction. Mathematics was never only calculation, never only proof, never only intuition, never only abstraction. It is an evolving system in which problems generate representations, representations generate theories, theories generate new problems, and communities keep building the tools that transform the cycle. AI is entering that cycle. The historical meaning of the moment therefore depends less on whether a machine can imitate the mathematician of yesterday than on whether people and machines together can weave the mathematics of tomorrow into a larger web.

<!-- zh -->

## 7 · 总结与统观

### 7.1 收束

把前六章收束在一起，会看到一张相互缠绕的图景。纳维-斯托克斯事件里，一个技术真相、一场商业竞争、一次署名纠纷、一桩优先权公案，几乎被压缩进了同一个九月的星期 [1,5]。数学被追问是不是万物的终极根据，答案却在数学内部最严格的定理那里得到一种近乎反直觉的回应：它连给自己一个自足封闭的地基都做不到，任何一条真理都要靠系统之外的东西来担保。数学家的形象被「聪明」「天才」层层包裹，而拆开层层包裹之后，那些真正被公认开创了新局面的人物，几乎无一不是同时背负好几重身份、数学家只是其中之一的人。至于「AI 是否不如数学家」这个看似该有斩钉截铁答案的问题，越往深处追问，越发现它无法脱离「数学究竟是什么」「创造性从何而来」「意义由谁赋予」这些更古老的追问而被单独回答。

### 7.2 统观：过程、预测与互相成就

这些线索反复指向同一件事：无论是数学本身、数学家这个身份，还是人类与机器这组看似泾渭分明的范畴，一旦真正被追问到底，都找不到一个可以孤立自存、无需依赖其他一切就能被完整定义的核心。数学的真假依存于一整套公理选择与元系统担保的无穷链条；数学家的伟大依存于他们身处的那个由哲学困惑、物理观测与历史机缘共同编织的世界；而「这次证明究竟算谁的功劳」这个看似该有清晰答案的问题，一旦深究，也会牵出雇佣关系、竞业限制、师承脉络、乃至上一代人留下的未竟猜想。没有一个节点是真正孤立的原因，每一个节点都兼为无数其他节点共同作用之下的结果，又反过来成为下一步进展的条件之一。

要精确地描述这种图景而不落入模糊的感叹，可以借助两个现成的、名字说得出口的思想资源。其一是怀特海的过程哲学：他主张实在是过程而非实体，任何存在物都因它与环境中其他存在物的关系而成为它自身，每一刻的实际存在都以自己的方式摄入并整合了整个过去的世界 [69]。其二是认知科学中的主动推理与自由能原理：弗里斯顿提出，认知系统的一切活动，从知觉到行动，都在持续地对世界做生成式的预测并最小化预测误差；系统与环境的边界不是先验划定的，而是由系统自己的生成模型不断重新刻画的 [70]。所谓「理解」，在这种框架下不是对外部事实的静态镜像，而是系统持续生成并修正它自己的世界模型的过程；模型与世界的边界，因此永远处在再协商之中。这两套思想相隔八十余年、分属哲学与神经科学，却指向同一个结构：整体先于部分而被给定，部分在整体的关系中才获得身份，而整体又由部分之间的关系持续地再构成。莱布尼茨的单子论早在三百年前就为这种结构给过一个诗意的版本：单子没有窗户，却各自映照着同一个宇宙 [71]。

把这个结构放回我们的主题，会看到一场关于「危机还是突破」的争论如何失去它的非此即彼性。一个证明因为被一整个能理解它的共同体消化、质疑、传授，才真正成为知识；一种数学传统因为与其他传统的比照，才显出自己的特殊性与局限；一次「AI 的胜利」，细看之下也总是由无数人类的既有工作、人类专家的审核之眼、甚至人类之间此前的竞争与合作共同托举而成。危机与突破从来不是彼此外在、非此即彼的两个实体，而是同一张不断展开的关系之网上暂时被照亮的两个侧面：正因为同一个结构既托举了机器的进展，也托举了建制的失稳，人们才同时看到了两样东西。二十五位菲尔兹奖得主的那封信，末尾其实已经触到了这个结构：AI 最终是增益还是损害数学，「将在很大程度上取决于掌控这项技术的人类的决定」[27]。换言之，连最激烈的批评者也不把结局交给技术本身，而是交还给人。

### 7.3 具体利害不因整体视野而消解

必须立刻补上一句，以防这种整体性的视野被误用：承认这种彼此成就、没有哪一方能单独宣称全部功劳或全部危机的处境，并不会让署名纠纷中的当事人少受一分委屈 [5]，也不会让某位数学博士生对自己职业前景的忧虑因此消散。那些具体的、此时此地的利害依然真实，依然应当被认真对待，不该被这样一种整体视野轻轻消解掉。整体视野的用处不在这里；它的用处在于提供一种更从容的姿态：不必因为机器算得比自己快就仓皇宣告一个学科的黄昏，也不必因为一次漂亮的分数就急着宣告一个时代的黎明。

因为无论「危机」还是「突破」，归根结底，都只是这张相互成就之网上暂时被照亮的某一个节点。而这张网本身，还在无声地向着四面八方继续展开。数学曾经不只是计算，不只是证明，不只是直觉，也不只是抽象；它是一个不断演化的系统，问题生成表示，表示生成理论，理论生成新问题，而共同体不断造出能够改变整个循环的工具。AI 正在进入这个循环。这个时刻的历史意义，因此并不取决于机器能否模仿昨天的数学家，而取决于人与机器能否一起，把明天的数学这张网，织得更大。

<!-- L1-end -->

<!-- L5 -->
<!-- en -->
## Sources

1. OpenAI. On the Navier–Stokes Millennium Prize Problem (8 September 2026). https://openai.com/index/navier-stokes-solution/【已审计·一手】
2. Clay Mathematics Institute. Navier–Stokes announcement (11 September 2026). https://www.claymath.org/news/navier-stokes-announcement/【已审计·一手】
3. Clay Mathematics Institute. Rules for the Millennium Prize Problems. https://www.claymath.org/millennium-problems/rules/【已审计·一手】
4. Clay Mathematics Institute. Navier–Stokes Equation. Millennium Prize Problem page, status label Active. https://www.claymath.org/millennium/navier-stokes-equation/【已审计·一手】
5. Howlett, J. Did OpenAI solve the wrong Navier–Stokes problem? *Scientific American* (21 September 2026). https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/【已审计·存疑（媒体转述）】
6. Lean documentation. Validating a Lean proof. https://lean-lang.org/doc/reference/latest/ValidatingProofs/【已审计·一手】
7. Feng et al. Towards Autonomous Mathematics Research. arXiv:2602.10177 (2026). https://arxiv.org/abs/2602.10177【待审·一手（预印本）】
8. Hubert, T. et al. Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature* **651**, 607–613 (2026). https://doi.org/10.1038/s41586-025-09833-y【已审计·权威版本】
9. Google DeepMind. AI achieves silver-medal standard solving International Mathematical Olympiad problems (25 July 2024). https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/【已审计·一手】
10. OpenAI. IMO 2025 proof repository (2025). https://github.com/aw31/openai-imo-2025-proofs【已审计·一手】
11. Google DeepMind. Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad (21 July 2025). https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/【已审计·一手】
12. Glazer, E. et al. FrontierMath: a benchmark for evaluating advanced mathematical reasoning in AI. arXiv:2411.04872 (2024). https://doi.org/10.48550/arXiv.2411.04872【已审计·一手（预印本）】
13. ARC Prize. o3 and the ARC-AGI benchmark (2025). https://arcprize.org/blog/oai-o3-pub-breakthrough【已审计·一手】
14. Meyer, D. 'Manipulative and disgraceful': OpenAI's critics seize on math benchmarking scandal. *Fortune* (21 January 2025). https://fortune.com/2025/01/21/eye-on-ai-openai-o3-math-benchmark-frontiermath-epoch-altman-trump-biden【已审计·存疑（媒体转述）】
15. Google DeepMind. AlphaEvolve: a Gemini-powered coding agent for designing advanced algorithms (14 May 2025). https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/【已审计·一手】
16. Erdős problems. Snapshot of 23 September 2026. https://web.archive.org/web/20260923/https://www.erdosproblems.com/【已审计·一手】
17. Tao, T. Mathematics in the age of AI. arXiv:2608.16753 (2026). https://doi.org/10.48550/arXiv.2608.16753【已审计·一手（预印本）】
18. Alon, N. et al. Remarks on the disproof of the unit distance conjecture. arXiv:2605.20695 (2026). https://doi.org/10.48550/arXiv.2605.20695【已审计·一手（预印本）】
19. Sawin, W. An explicit lower bound for the unit distance problem. arXiv:2605.20579 (2026). https://doi.org/10.48550/arXiv.2605.20579【已审计·一手（预印本）】
20. Automatic formalization benchmarks over long chains (placeholder-fabrication case). arXiv:2606.29493 (2026). https://arxiv.org/html/2606.29493v1【待审·一手（预印本）】
21. Williams, L. et al. First Proof. arXiv:2602.05192 (2026). https://doi.org/10.48550/arXiv.2602.05192【已审计·一手（预印本）】
22. Guevara, A., Lupsasca, A., Skinner, D., Strominger, A. & Weil, K. Single-minus gluon tree amplitudes are nonzero. arXiv:2602.12176 (2026). https://doi.org/10.48550/arXiv.2602.12176【已审计·一手（预印本）】
23. von Hippel, M. Claude computes a nine-loop amplitude in N=4 super-Yang-Mills. Anthropic (25 September 2026). https://www.anthropic.com/research/yes-claude-can-do-nine-loops【已审计·一手】
24. Bessis, D. *Mathematica: A Secret World of Intuition and Curiosity*. Yale University Press (2024).【待审·权威版本（论点属作者个人视角）】
25. The Leiden Declaration on Artificial Intelligence and Mathematics (2 June 2026). https://doi.org/10.5281/zenodo.20302944【已审计·一手】
26. International Mathematical Union. AO Circular Letter 8/2026: Leiden Declaration (2 June 2026). https://www.mathunion.org/fileadmin/documents/2026-06/IMU_AO_CL_8_2026.pdf【已审计·一手】
27. 25 Fields Medalists. A Severe Misalignment of AI in Mathematics (11 September 2026). mathandai.org.【待审·一手（网址待核）】
28. Park, J.-Y. Automation Without Understanding. arXiv:2607.06377 (2026). https://arxiv.org/abs/2607.06377【待审·一手（预印本）】
29. Adamczewski, T. & Bloom, T. F. FrontierMath Erdős. arXiv:2609.25050 (2026). https://doi.org/10.48550/arXiv.2609.25050【已审计·一手（预印本）】
30. Stanford Encyclopedia of Philosophy. Philosophy of Mathematics. https://plato.stanford.edu/entries/philosophy-mathematics/【待审·权威版本】
31. Wigner, E. The unreasonable effectiveness of mathematics in the natural sciences. *Commun. Pure Appl. Math.* **13**, 1–14 (1960).【待审·权威版本】
32. de Bruijn, N. G. The mathematical language AUTOMATH. In *Symposium on Automatic Demonstration*, 29–61 (Springer, 1970). https://doi.org/10.1007/BFb0060623【已审计·权威版本】
33. Lakatos, I. *Proofs and Refutations: The Logic of Mathematical Discovery*. Cambridge University Press (1976). https://doi.org/10.1017/CBO9781139171472【已审计·权威版本】
34. Tegmark, M. *Our Mathematical Universe: My Quest for the Ultimate Nature of Reality*. Knopf (2014).【待审·权威版本】
35. Stanford Encyclopedia of Philosophy. Gödel's Incompleteness Theorems. https://plato.stanford.edu/entries/goedel-incompleteness/【待审·权威版本】
36. Lucas, J. R. Minds, machines and Gödel. *Philosophy* **36**, 112–127 (1961). https://doi.org/10.1017/S0031819100057983【已审计·权威版本】
37. Penrose, R. *The Emperor's New Mind*. Oxford University Press (1989).【已审计·权威版本】
38. Cohen, P. J. The independence of the continuum hypothesis. *Proc. Natl Acad. Sci. USA* **50**, 1143–1148 (1963).【待审·权威版本】
39. Newton, I. *Philosophiæ Naturalis Principia Mathematica*, new translation by I. B. Cohen & A. Whitman (University of California Press, 1999).【已审计·权威版本】
40. Crippa, D. *The Impossibility of Squaring the Circle in the 17th Century: A Debate Among Gregory, Huygens and Leibniz*. Birkhäuser Cham (2019). https://doi.org/10.1007/978-3-030-01638-8【已审计·权威版本】
41. Turing, A. M. Computing machinery and intelligence. *Mind* **59**, 433–460 (1950). https://doi.org/10.1093/mind/lix.236.433【已审计·权威版本】
42. Stanford Encyclopedia of Philosophy. The Church–Turing Thesis. https://plato.stanford.edu/entries/church-turing/【待审·权威版本】
43. Katz, V. J. (ed.) *The Mathematics of Egypt, Mesopotamia, China, India, and Islam: A Sourcebook*. Princeton University Press (2007).【已审计·权威版本】
44. Pólya, G. *How to Solve It: A New Aspect of Mathematical Method*. Princeton University Press (1945).【已审计·权威版本】
45. Hadamard, J. *An Essay on the Psychology of Invention in the Mathematical Field*. Princeton University Press (1945).【已审计·权威版本】
46. Dyson, F. Birds and frogs. *Notices Amer. Math. Soc.* **56**, 212–223 (2009).【待审·权威版本】
47. Gowers, W. T. The two cultures of mathematics. In *Mathematics: Frontiers and Perspectives* (eds V. Milman & G. Schechtman), 65–78 (AMS, 2000).【已审计·权威版本】
48. Langlands, R. P. Letter to André Weil (1967).【待审·一手】
49. Deligne, P. La conjecture de Weil. I. *Publ. Math. IHÉS* **43**, 273–307 (1974). https://doi.org/10.1007/BF02684373【已审计·权威版本】
50. Zhang, Y. Bounded gaps between primes. *Ann. Math.* **179**, 1121–1174 (2014). https://doi.org/10.4007/annals.2014.179.3.7【已审计·权威版本】
51. Chen, J.-R. On the representation of integers as the sum of primes. *Scientia Sinica* **16**, 157–176 (1973). https://www.sciengine.com/doi/10.1360/ya1973-16-2-157【已审计·权威版本】
52. MacTutor History of Mathematics. Ramanujan biography. https://mathshistory.st-andrews.ac.uk/Biographies/Ramanujan/【已审计·权威版本】
53. Caviola, G. et al. Test anxiety effects, predictors, and correlates: a 30-year meta-analytic review. *Educ. Psychol. Rev.* **34**, 363–399 (2022). https://doi.org/10.1007/s10648-021-09618-5【已审计·权威版本】
54. Namkung, H., Peng, S. & Lin, R. A meta-analysis of mathematics anxiety. *Rev. Educ. Res.* **89**, 459–496 (2019). https://doi.org/10.3102/0034654319843494【已审计·权威版本】
55. Wang, H. The formalization of mathematics. *J. Symb. Log.* **19**, 241–266 (1954). https://doi.org/10.2307/2267732【已审计·权威版本】
56. Robinson, J. A. A machine-oriented logic based on the resolution principle. *J. ACM* **12**, 23–41 (1965). https://doi.org/10.1145/321250.321253【已审计·权威版本】
57. Newell, A. & Simon, H. A. Computer science as empirical inquiry: symbols and search. *Commun. ACM* **19**, 113–126 (1976). https://doi.org/10.1145/360018.360022【已审计·权威版本】
58. McCune, W. Solution of the Robbins problem. *J. Autom. Reason.* **19**, 263–276 (1997). https://doi.org/10.1023/A:1005843212881【已审计·权威版本】
59. Hales, T. et al. A formal proof of the Kepler conjecture. *Forum Math. Pi* **5**, e2 (2017). https://doi.org/10.1017/fmp.2017.1【已审计·权威版本】
60. Porter, T. M. *Trust in Numbers: The Pursuit of Objectivity in Science and Public Life*. Princeton University Press (1995).【待审·权威版本】
61. Kolmogorov, A. N. *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Springer (1933).【待审·权威版本】
62. Martzloff, J.-C. *A History of Chinese Mathematics*. Springer-Verlag (1997). https://doi.org/10.1007/978-3-540-33783-6【已审计·权威版本】
63. Plofker, K. *Mathematics in India*. Princeton University Press (2009). https://doi.org/10.1515/9781400834075【已审计·权威版本】
64. Wu, W.-T. On the decision problem and the mechanization of theorem-proving in elementary geometry. *Scientia Sinica* **21**, 159–172 (1978).【待审·权威版本】
65. Green, T. Notes on the parity barrier (2014). arXiv:1402.4849. https://doi.org/10.48550/arXiv.1402.4849【已审计·一手（预印本）】
66. Smith, K. Descartes' life and works. *Stanford Encyclopedia of Philosophy* (rev. 1 March 2023). https://plato.stanford.edu/entries/descartes-works/【已审计·权威版本】
67. Wittmann, A. D. Carl Friedrich Gauss and the Gauss Society: a brief overview. *History of Geo- and Space Sciences* **11**, 199–205 (2020). https://doi.org/10.5194/hgss-11-199-2020【已审计·权威版本】
68. Poincaré, H. L'invention mathématique. *Enseign. Math.* **10**, 357–371 (1908).【待审·权威版本】
69. Whitehead, A. N. *Process and Reality: An Essay in Cosmology*. Macmillan (1929).【待审·权威版本】
70. Friston, K. The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.* **11**, 127–138 (2010). https://doi.org/10.1038/nrn2787【待审·权威版本】
71. Leibniz, G. W. *Monadologie* (1714).【待审·权威版本】
<!-- zh -->
## 来源

1. OpenAI. On the Navier–Stokes Millennium Prize Problem (8 September 2026). https://openai.com/index/navier-stokes-solution/【已审计·一手】
2. Clay Mathematics Institute. Navier–Stokes announcement (11 September 2026). https://www.claymath.org/news/navier-stokes-announcement/【已审计·一手】
3. Clay Mathematics Institute. Rules for the Millennium Prize Problems. https://www.claymath.org/millennium-problems/rules/【已审计·一手】
4. Clay Mathematics Institute. Navier–Stokes Equation. Millennium Prize Problem page, status label Active. https://www.claymath.org/millennium/navier-stokes-equation/【已审计·一手】
5. Howlett, J. Did OpenAI solve the wrong Navier–Stokes problem? *Scientific American* (21 September 2026). https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/【已审计·存疑（媒体转述）】
6. Lean documentation. Validating a Lean proof. https://lean-lang.org/doc/reference/latest/ValidatingProofs/【已审计·一手】
7. Feng et al. Towards Autonomous Mathematics Research. arXiv:2602.10177 (2026). https://arxiv.org/abs/2602.10177【待审·一手（预印本）】
8. Hubert, T. et al. Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature* **651**, 607–613 (2026). https://doi.org/10.1038/s41586-025-09833-y【已审计·权威版本】
9. Google DeepMind. AI achieves silver-medal standard solving International Mathematical Olympiad problems (25 July 2024). https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/【已审计·一手】
10. OpenAI. IMO 2025 proof repository (2025). https://github.com/aw31/openai-imo-2025-proofs【已审计·一手】
11. Google DeepMind. Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad (21 July 2025). https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/【已审计·一手】
12. Glazer, E. et al. FrontierMath: a benchmark for evaluating advanced mathematical reasoning in AI. arXiv:2411.04872 (2024). https://doi.org/10.48550/arXiv.2411.04872【已审计·一手（预印本）】
13. ARC Prize. o3 and the ARC-AGI benchmark (2025). https://arcprize.org/blog/oai-o3-pub-breakthrough【已审计·一手】
14. Meyer, D. 'Manipulative and disgraceful': OpenAI's critics seize on math benchmarking scandal. *Fortune* (21 January 2025). https://fortune.com/2025/01/21/eye-on-ai-openai-o3-math-benchmark-frontiermath-epoch-altman-trump-biden【已审计·存疑（媒体转述）】
15. Google DeepMind. AlphaEvolve: a Gemini-powered coding agent for designing advanced algorithms (14 May 2025). https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/【已审计·一手】
16. Erdős problems. Snapshot of 23 September 2026. https://web.archive.org/web/20260923/https://www.erdosproblems.com/【已审计·一手】
17. Tao, T. Mathematics in the age of AI. arXiv:2608.16753 (2026). https://doi.org/10.48550/arXiv.2608.16753【已审计·一手（预印本）】
18. Alon, N. et al. Remarks on the disproof of the unit distance conjecture. arXiv:2605.20695 (2026). https://doi.org/10.48550/arXiv.2605.20695【已审计·一手（预印本）】
19. Sawin, W. An explicit lower bound for the unit distance problem. arXiv:2605.20579 (2026). https://doi.org/10.48550/arXiv.2605.20579【已审计·一手（预印本）】
20. Automatic formalization benchmarks over long chains (placeholder-fabrication case). arXiv:2606.29493 (2026). https://arxiv.org/html/2606.29493v1【待审·一手（预印本）】
21. Williams, L. et al. First Proof. arXiv:2602.05192 (2026). https://doi.org/10.48550/arXiv.2602.05192【已审计·一手（预印本）】
22. Guevara, A., Lupsasca, A., Skinner, D., Strominger, A. & Weil, K. Single-minus gluon tree amplitudes are nonzero. arXiv:2602.12176 (2026). https://doi.org/10.48550/arXiv.2602.12176【已审计·一手（预印本）】
23. von Hippel, M. Claude computes a nine-loop amplitude in N=4 super-Yang-Mills. Anthropic (25 September 2026). https://www.anthropic.com/research/yes-claude-can-do-nine-loops【已审计·一手】
24. Bessis, D. *Mathematica: A Secret World of Intuition and Curiosity*. Yale University Press (2024).【待审·权威版本（论点属作者个人视角）】
25. The Leiden Declaration on Artificial Intelligence and Mathematics (2 June 2026). https://doi.org/10.5281/zenodo.20302944【已审计·一手】
26. International Mathematical Union. AO Circular Letter 8/2026: Leiden Declaration (2 June 2026). https://www.mathunion.org/fileadmin/documents/2026-06/IMU_AO_CL_8_2026.pdf【已审计·一手】
27. 25 Fields Medalists. A Severe Misalignment of AI in Mathematics (11 September 2026). mathandai.org.【待审·一手（网址待核）】
28. Park, J.-Y. Automation Without Understanding. arXiv:2607.06377 (2026). https://arxiv.org/abs/2607.06377【待审·一手（预印本）】
29. Adamczewski, T. & Bloom, T. F. FrontierMath Erdős. arXiv:2609.25050 (2026). https://doi.org/10.48550/arXiv.2609.25050【已审计·一手（预印本）】
30. Stanford Encyclopedia of Philosophy. Philosophy of Mathematics. https://plato.stanford.edu/entries/philosophy-mathematics/【待审·权威版本】
31. Wigner, E. The unreasonable effectiveness of mathematics in the natural sciences. *Commun. Pure Appl. Math.* **13**, 1–14 (1960).【待审·权威版本】
32. de Bruijn, N. G. The mathematical language AUTOMATH. In *Symposium on Automatic Demonstration*, 29–61 (Springer, 1970). https://doi.org/10.1007/BFb0060623【已审计·权威版本】
33. Lakatos, I. *Proofs and Refutations: The Logic of Mathematical Discovery*. Cambridge University Press (1976). https://doi.org/10.1017/CBO9781139171472【已审计·权威版本】
34. Tegmark, M. *Our Mathematical Universe: My Quest for the Ultimate Nature of Reality*. Knopf (2014).【待审·权威版本】
35. Stanford Encyclopedia of Philosophy. Gödel's Incompleteness Theorems. https://plato.stanford.edu/entries/goedel-incompleteness/【待审·权威版本】
36. Lucas, J. R. Minds, machines and Gödel. *Philosophy* **36**, 112–127 (1961). https://doi.org/10.1017/S0031819100057983【已审计·权威版本】
37. Penrose, R. *The Emperor's New Mind*. Oxford University Press (1989).【已审计·权威版本】
38. Cohen, P. J. The independence of the continuum hypothesis. *Proc. Natl Acad. Sci. USA* **50**, 1143–1148 (1963).【待审·权威版本】
39. Newton, I. *Philosophiæ Naturalis Principia Mathematica*, new translation by I. B. Cohen & A. Whitman (University of California Press, 1999).【已审计·权威版本】
40. Crippa, D. *The Impossibility of Squaring the Circle in the 17th Century: A Debate Among Gregory, Huygens and Leibniz*. Birkhäuser Cham (2019). https://doi.org/10.1007/978-3-030-01638-8【已审计·权威版本】
41. Turing, A. M. Computing machinery and intelligence. *Mind* **59**, 433–460 (1950). https://doi.org/10.1093/mind/lix.236.433【已审计·权威版本】
42. Stanford Encyclopedia of Philosophy. The Church–Turing Thesis. https://plato.stanford.edu/entries/church-turing/【待审·权威版本】
43. Katz, V. J. (ed.) *The Mathematics of Egypt, Mesopotamia, China, India, and Islam: A Sourcebook*. Princeton University Press (2007).【已审计·权威版本】
44. Pólya, G. *How to Solve It: A New Aspect of Mathematical Method*. Princeton University Press (1945).【已审计·权威版本】
45. Hadamard, J. *An Essay on the Psychology of Invention in the Mathematical Field*. Princeton University Press (1945).【已审计·权威版本】
46. Dyson, F. Birds and frogs. *Notices Amer. Math. Soc.* **56**, 212–223 (2009).【待审·权威版本】
47. Gowers, W. T. The two cultures of mathematics. In *Mathematics: Frontiers and Perspectives* (eds V. Milman & G. Schechtman), 65–78 (AMS, 2000).【已审计·权威版本】
48. Langlands, R. P. Letter to André Weil (1967).【待审·一手】
49. Deligne, P. La conjecture de Weil. I. *Publ. Math. IHÉS* **43**, 273–307 (1974). https://doi.org/10.1007/BF02684373【已审计·权威版本】
50. Zhang, Y. Bounded gaps between primes. *Ann. Math.* **179**, 1121–1174 (2014). https://doi.org/10.4007/annals.2014.179.3.7【已审计·权威版本】
51. Chen, J.-R. On the representation of integers as the sum of primes. *Scientia Sinica* **16**, 157–176 (1973). https://www.sciengine.com/doi/10.1360/ya1973-16-2-157【已审计·权威版本】
52. MacTutor History of Mathematics. Ramanujan biography. https://mathshistory.st-andrews.ac.uk/Biographies/Ramanujan/【已审计·权威版本】
53. Caviola, G. et al. Test anxiety effects, predictors, and correlates: a 30-year meta-analytic review. *Educ. Psychol. Rev.* **34**, 363–399 (2022). https://doi.org/10.1007/s10648-021-09618-5【已审计·权威版本】
54. Namkung, H., Peng, S. & Lin, R. A meta-analysis of mathematics anxiety. *Rev. Educ. Res.* **89**, 459–496 (2019). https://doi.org/10.3102/0034654319843494【已审计·权威版本】
55. Wang, H. The formalization of mathematics. *J. Symb. Log.* **19**, 241–266 (1954). https://doi.org/10.2307/2267732【已审计·权威版本】
56. Robinson, J. A. A machine-oriented logic based on the resolution principle. *J. ACM* **12**, 23–41 (1965). https://doi.org/10.1145/321250.321253【已审计·权威版本】
57. Newell, A. & Simon, H. A. Computer science as empirical inquiry: symbols and search. *Commun. ACM* **19**, 113–126 (1976). https://doi.org/10.1145/360018.360022【已审计·权威版本】
58. McCune, W. Solution of the Robbins problem. *J. Autom. Reason.* **19**, 263–276 (1997). https://doi.org/10.1023/A:1005843212881【已审计·权威版本】
59. Hales, T. et al. A formal proof of the Kepler conjecture. *Forum Math. Pi* **5**, e2 (2017). https://doi.org/10.1017/fmp.2017.1【已审计·权威版本】
60. Porter, T. M. *Trust in Numbers: The Pursuit of Objectivity in Science and Public Life*. Princeton University Press (1995).【待审·权威版本】
61. Kolmogorov, A. N. *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Springer (1933).【待审·权威版本】
62. Martzloff, J.-C. *A History of Chinese Mathematics*. Springer-Verlag (1997). https://doi.org/10.1007/978-3-540-33783-6【已审计·权威版本】
63. Plofker, K. *Mathematics in India*. Princeton University Press (2009). https://doi.org/10.1515/9781400834075【已审计·权威版本】
64. Wu, W.-T. On the decision problem and the mechanization of theorem-proving in elementary geometry. *Scientia Sinica* **21**, 159–172 (1978).【待审·权威版本】
65. Green, T. Notes on the parity barrier (2014). arXiv:1402.4849. https://doi.org/10.48550/arXiv.1402.4849【已审计·一手（预印本）】
66. Smith, K. Descartes' life and works. *Stanford Encyclopedia of Philosophy* (rev. 1 March 2023). https://plato.stanford.edu/entries/descartes-works/【已审计·权威版本】
67. Wittmann, A. D. Carl Friedrich Gauss and the Gauss Society: a brief overview. *History of Geo- and Space Sciences* **11**, 199–205 (2020). https://doi.org/10.5194/hgss-11-199-2020【已审计·权威版本】
68. Poincaré, H. L'invention mathématique. *Enseign. Math.* **10**, 357–371 (1908).【待审·权威版本】
69. Whitehead, A. N. *Process and Reality: An Essay in Cosmology*. Macmillan (1929).【待审·权威版本】
70. Friston, K. The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.* **11**, 127–138 (2010). https://doi.org/10.1038/nrn2787【待审·权威版本】
71. Leibniz, G. W. *Monadologie* (1714).【待审·权威版本】
<!-- L5-end -->
