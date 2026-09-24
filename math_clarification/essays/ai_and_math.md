# 智慧与证明：AI 时代的数学七问 / Wisdom and Proof: Seven Questions on Mathematics in the Age of AI

<!-- L1 -->
<!-- en -->
**Abstract.** Between 2024 and 2026, artificial intelligence crossed from solving olympiad problems to tearing open a conjecture that had stood for eighty years, and the mathematical community responded — excitedly, angrily, and in manifesto form. This essay asks seven questions in order: what exactly was claimed and how well was it verified; who has spoken for and against, and with what arguments; what mathematics is; who mathematicians are; where the division of labor lands once proof can be formalized; whether an AI can pose a groundbreaking problem; and, at the close, what it would look like to accept this change without either panic or worship.
<!-- zh -->
**提要。** 在 2024 至 2026 年间，人工智能从解竞赛题跨越到撕裂一道尘封八十年的猜想，数学界的回应则热烈、愤怒，且频频以宣言形式出现。本文依次提出七问：究竟声称了什么、验证得有多严；谁在为其背书或反对、各自的论据何在；数学是什么；数学家是谁；一旦证明可以形式化，工作该如何分工；AI 能否提出开创性的问题；最后，放下恐慌与膜拜，去接受这一变化的成熟方式长什么样。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## Chapter 1 · The Claims and Their Verification (事件与核验)

**Claim.** "An AI solved a hard mathematics problem" is not one statement but five, with wildly different standards of proof attached. Rated on a single rubric — is the claim framed honestly, is it reproducible, is it checked by independent experts, are its failures disclosed — the announced results of 2024–2026 form a ladder, not a row.

Five events, one assessment frame. At the 2024 International Mathematical Olympiad, Google DeepMind's AlphaProof and AlphaGeometry 2 solved four of six problems at silver-medal level, including the hardest problem, which only five of the contest's human competitors cracked; the scoring was performed by two professors, Timothy Gowers and Joseph Myers, and AlphaProof's solutions were formally verified in the Lean proof assistant. This is the cleanest case on the list: an open contest, independent expert judging, machine-checkable output.

The OpenAI model announced in December 2024 landed differently. o3 scored 25.2% on Epoch AI's FrontierMath, a private benchmark of hundreds of hard problems authored by sixty-plus mathematicians — then the framing of the result came under fire. Epoch AI, which built the benchmark, stated it had not run the evaluation; OpenAI's higher number was achieved on a "chosen" subset, under a still-private protocol. Fortune summarized the ensuing fight as "Manipulative and disgraceful"; Epoch itself later released a corrected v2 in June 2026 that fixed errors in **42% of the problems** of the original set. That correction is the single most instructive fact in this chapter: the benchmark was partly wrong, the model was partly framed, and only a disciplined public process surfaced either.

The third event is the anchor of this cookbook. On May 20, 2026, OpenAI announced that one of its models had disproved Erdős's unit-distance conjecture, a landmark open problem of discrete geometry since 1946. Nine mathematicians — among them Fields medalist Timothy Gowers — wrote the verification paper (arXiv 2605.20695) that digested the construction; Will Sawin sharpened the exponent to $\delta = 0.014$ (arXiv 2605.20579); the problem's bound is now $n^{1.014} \leq u(n) \leq n^{4/3}$, with the gap wider than ever. The verification standard here is the highest yet seen: a peer-group of specialists read, sharpened, and made the machine's leap their own.

The Harvard "First Proof" project ran on a different axis. Ten unpublished research lemmas, authored by Lauren Williams and colleagues, were offered as a challenge; AI systems collectively solved at least six of ten. The striking finding was not that they ran, but that *human reviewers then struggled to verify the machine proofs* — the vetting bottleneck, not the solving, was the news. A second batch has since been registered behind a nonprofit foundation.

And the newest standard, announced in September 2026, closes the loop. Epoch AI's "FrontierMath Erdős" benchmark fixes 68 of Erdős's still-open problems, states each one in Lean, and gives every model the same budget of \$300 per problem to prove or disprove it autonomously. Best score: GPT-6 Astra at 3%. Everyone else: zero. This is the first benchmark where the verification is built into the task itself — you cannot spin the framing when the grader is a proof assistant.

The ladder, compressed. (i) *Open contest + independent experts + formal verification* (AlphaProof): the gold standard. (ii) *Private benchmark + private subset + contested framing* (o3/FrontierMath): the cautionary tale. (iii) *New result + specialist verification paper* (Erdős): the model that made partnership respectable. (iv) *Solveable but unverifiable* (First Proof): the open wound. (v) *Open conjectures, Lean-built-in, uniform budget* (FME): the emerging protocol.

**Pushback.** The ladder is a criterion of *process*, not *talent*: AlphaProof's clean result does not prove it is smarter than o3, only that its work was easier to certify. What collapses in reputational terms is not the models' competence but the industry's claim-making — when a company curates its own subset, it has moved from reporting a score to negotiating one.
<!-- zh -->
## 第一章 · 事件与核验

**论点。** "AI 解出了数学难题"不是一句话，而是五句话，各自带着天差地别的证明标准。用同一把尺子来量——表述是否诚实、是否可复现、是否经独立专家核验、是否如实披露失败——2024 至 2026 年间的公开成果摆成一把梯子，而非一排列队。

五件事，同一把评估尺。2024 年国际数学奥林匹克上，Google DeepMind 的 AlphaProof 与 AlphaGeometry 2 以银牌水平解出六题中的四题，其中包括全场只有五名人类选手解出的最难一题；评分由 Timothy Gowers 与 Joseph Myers 两位教授独立完成，AlphaProof 的解答在 Lean 证明助手中通过了机器核验。这是整张清单里最干净的一例：公开竞赛、独立专家裁决、可机器检查的输出。

2024 年 12 月公布的 OpenAI 模型则落在另一侧。o3 在 Epoch AI 的 FrontierMath 上拿到 25.2%——那是六十余位数学家建造的私有题库，数百道难题——随后，成绩的说法本身遭到围攻。建题的 Epoch AI 声明并未参与该次评测；OpenAI 更高的那个分数来自"经挑选"的子集与仍属私有的协议。*Fortune* 把这场争执概括为"操纵、可耻"；Epoch 自己在 2026 年 6 月发布修正版 v2，修复了原始题库中 **42% 的题目的错误**。这个修正堪称本章最具教益的事实：题库部分出错、模型部分被包装、而只有严格的公开程序才让两者浮出水面。

第三件事正是本 cookbook 的锚点。2026 年 5 月 20 日，OpenAI 宣布其模型推翻了 Erdős 单位距离猜想——一个自 1946 年以来困扰离散几何的里程碑式开放问题。九位数学家（其中包括菲尔兹奖得主 Gowers）写下核验论文（arXiv 2605.20695），"消化"了那份构造；Will Sawin 把指数精化到 $\delta = 0.014$（arXiv 2605.20579）；如今该问题的界是 $n^{1.014} \leq u(n) \leq n^{4/3}$，空白反而比过去更大。这里的核验标准是迄今最高的：一个专家群体读、精化、并把机器的跨越变成了自己的成果。

哈佛的 "First Proof" 项目跑在另一条轴上。Lauren Williams 与人合写的十个未发表研究引理被公开设擂；AI 系统合计解出至少十个中的六个。真正惊人的发现不是它们解出来了，而是*人类审稿人随后很难核验机器证明*——新闻是审稿瓶颈，而不是解题。第二批引理已在某非营利基金会名下登记。

而 2026 年 9 月公布的最新标准，把整个循环闭上了。Epoch AI 的 "FrontierMath Erdős" 基准挑出 68 道至今未解的 Erdős 问题，把每一道都用 Lean 写成陈述，并给每个模型同等预算（每题 \$300）自主证明或证伪。最高分：GPT-6 Astra 的 3%。其余全部为零。这是第一个把核验内置进任务本身的基准——当阅卷者是证明助理时，你没法再包装口径。

压缩成梯子：(i) *公开竞赛 + 独立专家 + 形式化核验*（AlphaProof）——黄金标准；(ii) *私有题库 + 私有子集 + 争议口径*（o3/FrontierMath）——警世之作；(iii) *新结果 + 专家核验论文*（Erdős 反例）——让"合作"变得体面的那个样例；(iv) *能解但难验*（First Proof）——未愈合的伤口；(v) *开放猜想 + 内置 Lean + 统一预算*（FME）——正在成型的范式。

**反诘。** 这把梯子量的是*流程*，不是*天赋*：AlphaProof 的干净成果并不能证明它比 o3 更聪明，只能证明它的活更容易被认证。在声誉上崩塌的不是模型的能耐，而是业界的话语方式——当一家公司自挑子集时，它已经从"报告成绩"滑向"商定成绩"。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## Chapter 2 · The Voices (众声)

**Claim.** The community has split into camps with coherent logics; the loudest disagreement is not about whether AI works, but about what mathematics is *for*. Read charitably, the answer to "is this a crisis of mathematics or of mathematicians?" is: of the mathematicians — of their institutions, their authority, their labor.

**The integrationists.** Terence Tao's ICM 2026 lecture essay, "Mathematics in the age of AI" (arXiv 2608.16753), argues from a "Working Hypothesis": a strong AI Capability Conjecture will soon hold — AI tools will do a reasonable fraction of research-level mathematics, at reasonable quality and cost. On that bet, he warns, the discipline's bottleneck moves: AI-generated proofs will accumulate faster than they can be verified, and verified proofs faster than they can be given readable write-ups, and readable write-ups will overwhelm volunteer peer review. Tao treats this as a call to make mathematics' goals explicit — do we optimize theorems, or understanding, or human training? Kevin Buzzard of Imperial College works the same side in code: he leads a long-project to formalize Fermat's Last Theorem in Lean, estimated at a hundred person-years, precisely to build the machinery that would let machines be checked.

**The institutionalists.** The Leiden Declaration (2 June 2026, DOI 10.5281/zenodo.20302944) was drafted by sixteen researchers from fifteen universities and endorsed by the International Mathematical Union, the AMS, and an editorial in *Nature*. Its five named threats are the most careful inventory yet: reliance on plausible but unreliable machine arguments; attribution and authorship dissolving; dependence on proprietary tools creating inequality between researchers; the overhyping of results by press releases; and the erosion of what "understanding" means. Peter Scholze, endorsing it, put the stake plainly: the goal of mathematical research is *human* understanding, and mathematics can only thrive inside a community of human researchers. Note what this camp does *not* demand: no ban. It asks for disclosure, norms, and authorship rules.

**The fatalists.** Jacob Tsimerman, Fields medalist, reportedly takes the darkest reading: AI will destroy the field, and perhaps the world — yet mathematicians have no choice but to use it. This is the doom position with the cleanest logic: if tools keep improving and refusing them means irrelevance, then progress itself is self-reinforcing doom; the only question is how gracefully the field erodes.

**The resisters.** Max Weinreich's essay "The crisis of AI-generated mathematics" (arXiv 2608.02859) argues for total opposition: AI is an "anti-intellectual technology" that short-circuits understanding, devalues knowledge, and tempts the best mathematicians to avoid it simply to keep demonstrating value to one another. Patrick Massot has spoken of AI "bombing" mathematics. The resistance has a real argument hiding inside its fierceness: if checking a flood of machine proofs is tedious, then the profession's prestige economy — which attaches worth to *discovering*, not *checking* — punishes exactly the labor that will keep mathematics honest.

**The moderates.** Bruce Schneier and Kasra Rafi, writing in *The Guardian*, draw the line that later chapters will test: AIs are strong at searching and recombining existing ideas, weak at building deep sustained new theory; in the short term they are nowhere near experienced academic mathematicians. Michael Harris, in *Boston Review*'s "Knowledge Collapse," reminds the field that mathematics was, in Henri Poincaré's phrase, a "free creative art" — one of the last unalienated labors — and asks what survives of that under automation.

**Crisis?** Each camp is coherent about its own premises. What none of them doubts is that the *results* are real — the disproof stands, the Lean towers grow. The dispute is about the value of the activity. That is the tell: a crisis is not of mathematics (its content, its problems, its truths — these are untouched), but of the mathematician — of employment, institutional authority, the meaning of one's day's work, and the dignity of judging what is worth proving. A question about *what mathematics is* has been forcibly re-opened.
<!-- zh -->
## 第二章 · 众声

**论点。** 数学界已分裂为若干立场严整的阵营；最激烈的争执不在"AI 能不能干"，而在"数学是做什么用的"。若放在最善意的解读下，"这是数学的危机，还是数学家的危机？"的答案是：数学家的——他们的制度、权威与劳动。

**整合派。** 陶哲轩在 ICM 2026 的演讲文章《Mathematics in the age of AI》（arXiv 2608.16753）以一个"工作假说"立论：AI 能力猜想的一个强版本即将成立——AI 工具将以合理的质量与成本完成相当比例的科研级数学。基于这一赌注，他警告学科的瓶颈将转移：AI 生成的证明会积累得比被验证还快，被验证的会比被写成可读文本还快，可读文本会淹没志愿审稿制。陶因此呼吁把数学的目标说清楚——我们优化的是定理、理解，还是人的训练？伦敦帝国理工的 Kevin Buzzard 以代码实践同一路线：他领衔"在 Lean 中形式化费马大定理"的长程项目，估计约百人年，目的正是建造让机器可被检查的机器。

**建制派。** 《莱顿宣言》（2026 年 6 月 2 日，DOI 10.5281/zenodo.20302944）由来自十五所大学的十六位研究者起草，获得国际数学联盟（IMU）、美国数学会（AMS）与《自然》社论背书。其点名的五重威胁是迄今最谨慎的清单：可信但不可靠的机器论证；署名与作者权瓦解；对专有工具的依赖造成研究者间不平等；新闻稿对成果的过度炒作；"理解"含义本身的侵蚀。Peter Scholze 在背书时把赌注说得干脆：数学研究的目标是*人的*理解，数学只能在人类研究者的共同体中繁荣。注意这个阵营没有要求什么：没有禁令。它要的是披露、规范与署名规则。

**末日派。** 菲尔兹奖得主 Jacob Tsimerman 据说持最黑暗的读法：AI 会毁掉这个领域，甚至毁掉世界——但数学家别无选择，只能用。这是逻辑最干净的末日立场：如果工具持续进步、拒绝它意味着边缘化，那么进步本身就是自我强化的毁灭；问题只剩数学以何种姿态溃退。

**抵制派。** Max Weinreich 的《The crisis of AI-generated mathematics》（arXiv 2608.02859）主张彻底抵制：AI 是"反智的技术"，短路理解、贬低知识，并诱使最好的数学家放弃 AI 只为彼此证明价值。Patrick Massot 则称 AI 在"轰炸"数学。抵制派火力凶猛之下藏着一个真实的论证：如果核验海量机器证明既枯燥又无荣耀，那么职业的声望经济——它把价值系于*发现*而非*核验*——恰好惩罚了让数学保持诚实的那个动作。

**温和派。** Bruce Schneier 与 Kasra Rafi 在《卫报》上划出的界线，正是后文要检验的：AI 强于搜索与重组既有观念，弱于建造深刻、持续的新理论；短期内远不及有经验的研究型数学家。Michael Harris 在《波士顿评论》的《Knowledge Collapse》里提醒数学界：按庞加莱的说法，数学曾是"自由创造的艺术"——所剩无几的未异化劳动之一——自动化之下还剩下什么。

**危机吗？** 各方在自己的前提内部都逻辑自洽。而没有任何一方怀疑*结果是真的*——反例立得住，Lean 的高塔在长高。争执在于这项活动的价值。这就是线索：危机的不是数学（其内容、问题、真理皆未受损），而是数学家——就业、机构权威、一日工作的意义、以及判断"什么值得证明"的尊严。一个关于"数学是什么"的问题被迫重新敞开。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## Chapter 3 · What Mathematics Is (数学为何物)

**Claim.** Mathematics is not the first cause of anything. It is a way of speaking about relations that hold necessarily — and precisely because it is a *way of speaking*, its edge is decided less by what is true than by what a community agrees is worth saying next.

**Not a first cause.** The universe does not run on equations the way a program runs on code; physics runs, and mathematics is the language in which physicists find the patterns legible. Calling mathematics the "first cause" mistakes the map for the territory, the grammar for the speech. What is genuinely prior about mathematics is the *mode*: the insistence that a claim may be examined purely by itself, stripped of context, and forced to justify its own necessity.

**Very well, what is it then?** The oldest and still most serviceable description is Kant's: mathematical truth is *synthetic a priori* — it extends what we know (it is not a tautology) yet holds with necessity, independent of experience. The formalist rejoinder (Hilbert's lineage) treats mathematics as a game of symbols under rules, answering the question "is it true?" with "it is consistent." Gödel's 1931 incompleteness theorems put a wall through that game: any sufficiently strong consistent system contains statements it can neither prove nor refute, and cannot prove its own consistency. Since then, as Tao's essay notes, mathematics has simply continued to work on "naive" foundations — the crisis that once ended at Hilbert's doorstep ended instead in resignation, and the field prospered anyway.

**The limits of expression.** Incompleteness and independence results (Cohen's 1963 proof that the continuum hypothesis can be neither proved nor refuted) draw the boundary of *formalized* mathematics. But there is a wider edge: no formal system decides which problems to work on, which symmetries are deep, what deserves the next decade. Those judgments are not theorem-shaped, yet they are mathematics' most consequential acts. Formality is mathematics' *backbone*, not its mind.

**How problems are made.** Problems are not found, they are constructed — and three moves recur. *Analogy* (draw a line from one domain to another), *generalization* (relax a hypothesis and ask what still holds), and *changing the language* (re-describe the object). The unit-distance disproof is a perfect specimen: the move was neither harder work in geometry nor a sharper lemma, but a swap of number system — from the Gaussian integers to number fields whose symmetries are inexhaustible. The conjecture fell because someone asked "what if the cage were made of glass?" The ethical conclusion for the chapters ahead: whoever (human or machine) controls the *re-description* is the one doing mathematics' deepest work.
<!-- zh -->
## 第三章 · 数学为何物

**论点。** 数学不是万物的第一因。它是对"必然成立的关系"的一种言说方式——正因为它是*一种言说方式*，它的边界与其说由"何为真"决定，不如说由"一个共同体同意接下来值得说什么"决定。

**不是第一因。** 宇宙不像程序跑代码那样按方程运行；物理学在运行，而数学是物理学家在其中看清模式的工具语言。把数学称为"第一因"，是把地图当成了领土，把语法当成了言说。数学中真正居于先前的是那种*方式*：坚持一个命题可以被抽离语境、单独审视、并为自身的必然性负责。

**那它到底是什么？** 最古老也仍最耐用的描述属于康德：数学真理是"先天综合判断"——它增长我们的知识（不是同义反复），却又必然有效、不依赖于经验。形式主义回应（希尔伯特一系）把数学当作符号在规则下的博弈，把"它为真吗"翻译成"它自洽吗"。哥德尔 1931 年不完备定理在博弈内部竖了一堵墙：任何足够强的自洽体系都含有其既不能证也不能否的命题，也无法证明自身的自洽。此后，如陶哲轩的文章所言，数学只靠在"朴素基础"上运行便继续繁荣——曾经终结于希尔伯特门口的基础危机，最终以"接受它"收场，而这个领域反而兴旺。

**表达的极限。** 不完备性与独立性结果（柯恩 1963 年证明连续统假设既不可证也不可否）划出了*形式化*数学的边界。但还有一条更宽的边缘：没有任何形式系统能决定该研究什么问题、哪些对称性深刻、什么值得再投入十年。这些判断并非定理形状，却正是数学最要紧的动作。形式性是数学的*脊梁*，而非其心智。

**问题是怎么来的。** 问题不是被找到的，而是被构造的——且万变不离三种动作。*类比*（从一域引线到另一域）、*推广*（放松一个假设，问结论还剩多少）、*换语言*（重新刻画对象）。单位距离反例是一具完美标本：那一跃既不是几何上加倍用功，也不是更锋利的引理，而是换数系——从高斯整数换到对称性取之不竭的数域。反例之所以倾覆，是因为有人问"如果笼子是玻璃做的呢？"这对后面各章的结论是：谁掌握*重新刻画*，谁就在做数学里最深的活。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## Chapter 4 · Who the Mathematicians Are (数学家是谁)

**Claim.** "Mathematician" is a ladder, not a kind: solver, researcher, theory-builder, field-founder. Most of the wedding of "mathematics" to "intelligence" is scaffolding — history, gatekeeping, asymmetric information, and a survivorship bias that only ever shows the winners.

**The ladder.** The olympiad solver — the tier that dominates the public image — is actually doing pattern-matching under a clock. The researcher proves things nobody has proved, mostly small, mostly by extension. The theory-builder assembles results into architecture (a Weil, a Grothendieck). The field-founder says *the whole conversation should change* — Descartes, Newton, Gauss. These are different crafts. Confusing tier one with tier four — as the popular press (and the AI hype cycle) constantly does — is like assuming the fastest sprinter is the best architect because both are athletic.

**What they actually do now.** The raw material of the day's work has changed within one generation: from paper-and-ink lemmas, to verifying on a keyboard, to — since 2026 — deciding when to let a machine propose and when to demand a readable human-scale proof. The prestige economy strains under this: checking is essential and thankless. Joel David Hamkins has written of "despairing at an ocean of slop overwhelming journal systems"; Daniel Litt of "pollution of the commons by AI-generated nonsense." The problem is not that proofs are wrong but that *attention* is the scarce good, and the referee is unpaid.

**Why "mathematics = intelligence"?** Five forces, none about aptitude itself. *History*: the cult of the solitary genius (Gauss, Erdős) is a post-Enlightenment storyteller's invention that flattens decades of communal labor into a single flash. *Psychology*: intuition and rigor are trained separately and marketed as a single gift; those fluent in both are rarer than the stereotype admits. *Gatekeeping*: olympiads and the formalization ritual decide, early and cheaply, whom the profession treats as promising — a filter optimized for speed and neat problem-solving, not for depth. *Information asymmetry*: outsiders see finished proofs, exquisite and inevitable; they never see the two-year stretch of dead ends, which makes the residue look effortless. *Cognitive bias*: survivorship bias (the silenced failures), the halo effect (one brilliant theorem licenses praise for everything adjacent) — the mind performs the same inflation on humans that we now accuse benchmarks of performing on models.

**Unbinding.** "Smart" was never the job description. The job is: carry the community's standards, extend what no one has extended, and — at the top — decide what the community should work on next. Those are labor categories, not grade scores.
<!-- zh -->
## 第四章 · 数学家是谁

**论点。** "数学家"是一架梯子而非一种人：解题者、研究者、理论建造者、领域开创者。"数学"与"聪明"之间的婚姻，大半是脚手架——历史叙事、守门仪式、信息不对称，以及一个只展示胜者的幸存者偏差。

**这架梯子。** 竞赛解题者——霸占公众形象的那一档——其实是在倒计时下做模式匹配。研究者证明前人未证之物，多数很小、多数靠延伸。理论建造者把结果装配成建筑（一个 Weil，一个 Grothendieck）。领域开创者说：*整场对话都该换了*——笛卡尔、牛顿、高斯。这是不同的手艺。把第一档混同于第四档——大众媒体与 AI 造神周期不断这么干——好比因为最快的短跑运动员也是运动员，就认定他是最好的建筑师。

**他们现在到底在做什么。** 一日工作的原材料在一代人内变了形：从纸墨引理，到键盘上的验证，再到——2026 年以来——决定何时让机器提案、何时索要一份可读的人类尺度证明。声望经济在此承压：核验必不可少却无人感恩。Joel David Hamkins 写他"对着淹没期刊系统的垃圾之海绝望"；Daniel Litt 谈"AI 生成的垃圾污染公地"。问题不在证明错了，而在*注意力*才是稀缺品，而审稿人没有工资。

**为什么"数学=聪明"？** 五股力量，无一关乎天赋本身。*历史*：孤胆天才崇拜（高斯、埃尔德什）是启蒙之后小说家式发明的叙事，把数十年的共同体劳作压扁成一道闪光。*心理*：直觉与严格分开训练、又当作一种天赋售卖；两者皆流利者远比刻板印象以为的稀少。*守门*：奥赛与形式化仪式在很早、很便宜的地方决定谁被视为可造之材——这套过滤器为速度和整洁解题而设计，不是为深度。*信息不对称*：外人只见成品证明——精致、无可逃避；他们从不见那两年的死胡同，于是残渣显得毫不费力。*认知偏差*：幸存者偏差（被湮灭的失败）、光环效应（一条漂亮定理给周边一切盖上合格戳）——大脑对人所做的通货膨胀，正是我们现在指控基准对模型所做的。

**解绑。** "聪明"从来不是职位描述。职位是：承托共同体的标准、延伸无人延伸之处、并且——在最顶端——决定共同体接下来该做什么。这是劳动的分类，不是分数的等级。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## Chapter 5 · Formalization and the Division of Labor (形式化与分工)

**Claim.** In the layer where proof becomes formalizable, an AI can already out-search any individual human. That settles less than it seems: the containment (logic ⊂ mathematics, formalization ⊂ mathematics, computation ⊂ formalization, quantifiability ⊂ computation) leaves mathematics' controlling decisions — goal, language, importance — outside the machine's reach. And the West is not the whole of mathematics.

**What contains what.** Write the inclusions plainly: *quantifiable* ⊂ *computable* ⊂ *formalizable* ⊂ *mathematics*. Logic deserves a double entry — it is mathematics' skeleton, the grammar of every formal system, and also one of mathematics' objects (proof theory studies logic mathematically). The core of the claim: everything a machine "solves" lives in the formalizable stratum, which is real, vast, and not the whole. The Erdős counterexample lives there — that is why it could be certified.

**Case for the machine.** In that stratum the machine's advantage is not speed of arithmetic but the *indifference to the obvious* — it will try languages a human expert has already learned to call irrelevant. Human mathematicians know the right picture; famously, the picture was the cage. AlphaProof matched olympiad elites; the Erdős model found an 80-year counterexample by switching number systems nobody connected to the problem; First Proof solved lemmas *before human referees could verify them*. On bounded, checkable, searchable tasks, larger-than-human search now beats individual human search, period.

**Case for the human.** Then the division writes itself. Machines: propose, construct, formalize, and run the first pass of checking — twenty drafts for every thought worth keeping. Humans: set the goal, choose the language, judge importance, keep the community's standards, and — Tao's word — "digest": turn verified results into something a mathematician can carry in her head. The verification bottleneck Tao names (proofs outrun verification, verification outruns write-ups, write-ups outrun referees) only tightens this: the scarcer the attention, the more valuable the human who converts machine output into understanding. This is why the resistance and the coherence of the institutionals both misfire slightly: the bottleneck favors *the human work*, not the machine work.

**Is Western mathematics all of mathematics?** No, and this matters more than the A-list hype suggests. Modern axiomatic mathematics — the Hilbert-lineage, formal, set-theoretic brand — is one dialect of "saying precisely," not the language itself. The Chinese algorithmic tradition (*The Nine Chapters*, celestial-source algebra 天元术, Yang Hui's / Jia Xian's triangle) is mathematics of the first rank — it computed what the axiomatic style later proved. "Modern mathematics can stand for all mathematics" is a statement of institutional reach, not of content. The 2026 disproof is a happy reminder: the levers that broke Erdős's conjecture (algebraic number theory, unit groups) come from an arithmetic tradition that predates and outlives the modern-foundations fashion.
<!-- zh -->
## 第五章 · 形式化与分工

**论点。** 在证明变得可以形式化的那一层，AI 的搜索能力已经超过任何个人。但这解决的远没有看上去多：那一串包含关系（逻辑 ⊂ 数学、形式化 ⊂ 数学、可计算 ⊂ 形式化、可量化 ⊂ 可计算）把数学的支配性决断——目标、语言、重要性——留在机器够不到的地方。且西方不是数学的全部。

**谁包含谁。** 把包含关系写直白：*可量化* ⊂ *可计算* ⊂ *可形式化* ⊂ *数学*。逻辑需记两笔——它是数学的骨架，每个形式系统的语法；同时又是数学的研究对象（证明论在数学地研究逻辑）。论断的核心是：机器"解出"的一切都住在可形式化的一层，这一层真实、广袤、却不是全体。Erdős 反例就住在那里——所以它才可能被认证。

**机器的一份。** 在那一层，机器的优势不是计算速度，而是*对"显而易见"无感*——它乐于尝试人类专家早已学会称之为无关的语言。人类数学家知道正确的画面；众所周知，那幅画面就是笼子。AlphaProof 追平奥赛精英；Erdős 模型靠切换无人联想过的问题相关数系找到八十年反例；First Proof 在*人类审稿人尚不能核验*前就解出了引理。在有界、可检、可搜的任务上，超越单人的搜索如今胜过单人的搜索，没有例外。

**人类的一份。** 分工于是自己写就。机器：提案、构造、形式化、跑第一遍核验——为每一条值得留下的思想造二十个草稿。人类：设定目标、选择语言、判别重要性、守住共同体的标准、并——用陶的话——"消化"：把被验证的结果变成数学家能装进脑子带走的东西。陶点出的核验瓶颈（证明跑赢验证、验证跑赢书写、书写跑赢审稿）只会让这一点更紧：注意力越稀缺，那个把机器输出转译成理解的人越值钱。这也解释了为什么抵制派与建制派的自我叙事都略失焦：瓶颈恰恰*有利于人的劳动*，而非机器的劳动。

**西方数学是数学的全部吗？** 不是，而且这一点比头条炒作更值得注意。现代公理化数学——希尔伯特一系、形式化、集合论品牌——只是"精确言说"的一种方言，而不是语言本身。中国算法传统（《九章算术》、天元术、杨辉/贾宪三角）是一流数学：它计算出了公理化风格后来才证明了的东西。"现代数学可以代表全部数学"说的是制度版图，而非内容版图。2026 年的反例是个愉快的提醒：撬开 Erdős 猜想的杠杆（代数数论、单位群）出自一个先于、并活过了现代基础时尚的算术传统。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## Chapter 6 · Groundbreaking Problems (开创性问题)

**Claim.** "Groundbreaking" should mean *changing the frame* — a new definition, a new language, a redirected field — not merely a hard theorem. By that standard, the AI has already crossed languages (what was invented in 2026) but has not yet built a new language system (what has not). And by that standard, most mathematicians never pose a groundbreaking problem either.

**Define the term.** A theorem advances the frontier; a *breakthrough* moves the border. Descartes' coordinates turned geometry into algebra and algebra into geometry. Newton's fluxions and Leibniz's calculus gave change itself a syntax. Gauss rebuilt number theory so that "law" meant "pattern with a proof." The common thread is the *re-description* from Chapter 3 performed at the scale of a discipline. Nothing in the public record yet shows an AI doing that. The 2026 disproof is a theorem of enormous reach — a new counterexample family, an exotic cross-domain leap — but it answers a question mathematicians posed, in a dialect (algebraic number theory) that already existed. Schneier and Rafi's distinction survives this test: strong at recombination, unproven at theory-building.

**Who can actually pose one?** The honest floor: hardly anyone. Hilbert's 23 problems redirected a century; Erdős spent a career distributing roughly 1,500 problems to a generation. The majority of published mathematics is consolidation — extending, cleaning, sharpening somebody else's frame. If "AI cannot pose groundbreaking problems" is the test, it is a test that prunes almost all humans too. Posing deep questions is rarer than the myth suggests, is distributed unequally, and is not obviously a *formal* skill — which makes the claim "agile tools cannot do it" belong to the same category as "agile tools can never do it," i.e., a bet, not a proof.

**The polymath interlude.** Descartes, Newton, Leibniz, Gauss were not narrowly "pure mathematicians"; they were polymaths — philosophies, physics, astronomy, geodesy, metaphysics, all of it one fabric. Their breakthroughs were *cross-domain intuition*: secularizing the mystical, algebraizing the geometric, timing the falling, enumerating the smooth. This cuts against the anti-AI reading twice. First, "what AI does is just recombination" misdescribes what breakthrough has ever been; recombination *across* domains *is* the historical engine. Second, the Erdős-AI did exactly that — crossed number theory into geometry — which is the first polymath-style move a machine has made in public mathematics. The honest reservation is not "machines can only recombine"; it is "machines have not yet shown *judgment about which shape of the future is worth building*."

**Who keeps the judge's chair?** The deepest act in the profession — deciding that this, not that, matters — is a social judgment about value, exercised by a community over time. AI will flood the court with filings; it will not, on today's evidence, decide the case. The 2026 lesson is that the *border-moving question* is answerable by search once the language is given. The *question-selection* remains the crown — and it, too, is a labor, not a gift.
<!-- zh -->
## 第六章 · 开创性问题

**论点。** "开创性"应当指*更换框架*——一个新定义、一门新语言、一个被重新定向的领域——而不只是一道硬定理。按这个标准，AI 已经做过跨语言（2026 年发明的那个动作），但尚未造出一门新语言体系（尚未发生的那件事）。而按这个标准，大多数数学家也没提出过开创性问题。

**先定义。** 定理推进边界；*突破*移动边界。笛卡尔的坐标把几何变成代数、把代数变成几何。牛顿的流数与莱布尼茨的微积分为"变化"本身造了一句语法。高斯重构数论，使"定律"意味着"有证明的模式"。共同线索是按第三章的"重新刻画"，在**学科**的尺度上实施。公开记录里还没有 AI 做到这一点的证据。2026 年的反例是跨度极大的定理——一个新反例族、一次奇异的跨域跳跃——但它回答的是数学家提出的问题，用的是既有的方言（代数数论）。Schneier 与 Rafi 的区分在此经受住了检验：重组为强，建理论未证。

**谁真有资格提出？** 老实说底限是：几乎没人。希尔伯特的 23 个问题重新定向了一整个世纪；埃尔德什以毕生散布约一千五百个问题给一代人。已发表数学的多数是巩固——延伸、清洗、磨利别人的框架。如果"AI 提不出开创性问题"是考题，那它是一道也淘汰几乎所有人类的考题。提出深刻问题比神话所言的更罕见、分配得更不均、且显然不是一种*形式化*技能——这让"敏捷工具做不到"沦入与"敏捷工具永远做不到"同类：是赌注，不是证明。

**多面手插曲。** 笛卡尔、牛顿、莱布尼茨、高斯都不是狭隘的"纯数学家"；他们是多面手——哲学、物理、天文、测地、形而上学，同一匹织物。他们的突破是*跨域直觉*：把神秘学世俗化、把几何代数化、给下落计时、为光滑计数。这双重地削弱反 AI 的读法。其一，"AI 所做无非重组"错误描述了突破自古以来的样子；*跨域*重组*本来就是历史引擎*。其二，Erdős-AI 干的正是这件事——把数论引进几何——这是机器在公众视野里打的第一个多面手式动作。老实的保留意见不是"机器只会重组"，而是"机器尚未展现*对'哪个未来值得造'的判断*"。

**谁坐法官席？** 这个职业里最深的动作——判定这一件、而非那一件要紧——是一种关于价值的社群判断，由共同体在时间里行使。AI 会往法院塞满诉状；按今天的证据，它不会判案。2026 年的教训是：*移动边界的问题*在语言给定后是搜索可以回答的；*选题*仍是王冠——而它也同样是劳动，不是馈赠。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## Chapter 7 · The View of Mutual Containment (圆融观照)

**Claim.** Without any borrowed vocabulary — no "interpenetration," no "web of causes," no school names at all — here is the oldest way to hold this change: nothing stands alone, everything holds everything else up, and the tool is part of the mountain. Seen so, the human–machine contest was never a contest; it was a river meeting its own banks.

**Everything is connected in practice, not in poetry.** The disproof of 2026 needed a number system nobody had connected to the geometry; the benchmarks needed sixty mathematicians; the formalizers needed a century of Lean; the models needed the canon that the profession had built. Take away any of these and the story dies. A machine's leap and a human's habit are not separate things fighting — they are two strands of the same rope, each holding the other's meaning. When Gowers and his eight co-authors sat down to turn the machine's construction into a proof humans could teach, neither party was the author of the result; the result was the meeting.

**No fixed labels survive.** "Solve" and "understand" looked like opposites until the machine solved what the human could not yet understand; after the verification paper, the human understood it, and the machine had done its half. The labels migrate as the relation shifts — which is how it should be read: as a moving relation, not a fixed ranking. A "tool" that extends a mathematician's reach is not an invader; it is indistinguishable, in the life of the mathematician, from a new theorem that extends the reach of everyone. Water does not fight the river for being wetter in one place.

**The fear of redundancy dissolves the same way.** Fear assumes a zero-sum shelf of roles with a fixed stock of dignity. But a deeper look finds dignity in the *movement*: the referee who makes the slop readable, the teacher who keeps the pattern alive in others' heads, the one who says "this, not that" — each only more needed as the machine makes everything faster. Redundancy is a fiction that confuses the number of people with the amount of care. A river is not half-empty for being deep in one bend and shallow in another; the water is the whole thing at every point.

**What the mature reaction looks like.** Neither panic (the field is not over; the gap grew, the discipline widened) nor worship (the tools did not do the thinking that picked the question). A river without banks is a flood; a river without water is a ditch. The bank's job is to stay bank — to judge, to teach, to keep the standard — and to let the water run. Mathematics is not endangered by the machine; it is being asked, first time in living memory, what it is *for*. The honest answer has not changed in two thousand years: it is for the human who, meeting a pattern, wants it true and wants to understand why. The machine can give that human more patterns than ever. It cannot take the wanting.
<!-- zh -->
## 第七章 · 圆融观照

**论点。** 不用任何借来的词汇——不说"相融""互为条件""网"，更不提任何学派的名字——这里有看待这场变化的最古方式：没有什么是独自成立的，一切都托举着别的一切，而工具本身是山的一部分。如此看去，人机之争从来不是之争；它是河水遇上了自己的两岸。

**一切在实践里相连，而非在诗意里相连。** 2026 年的反例需要一个没人把它连到几何上来的数系；基准需要六十位数学家；形式化者需要一个世纪的 Lean；模型需要这个职业亲手积累起来的正典。抽掉其中任何一环，故事就死。机器的跳跃与人的习惯并不是对立的两个东西在搏斗——它们是同一根绳的两股，互为意义。当 Gowers 与其八位共同作者坐下来，把机器的构造改写成人类能教、能带的证明时，没有哪一方是结果唯一的作者；结果就是这场相遇本身。

**没有固定标签幸存。** "解出"与"理解"曾看似对立，直到机器解出了人类尚不能理解之物；核验论文之后，人理解了它，而机器做完了它那一半。标签随关系的移动而迁移——这正是应有的读法：一个移动的关系，而非固定的排名。一件延伸数学家臂膀的"工具"不是入侵者；在数学家的生命里，它同一个延伸了所有人臂膀的新定理并无区别。水不会因为在此处更湿就与河流搏斗。

**对冗余的恐惧同样化解。** 恐惧预设角色是一块零和的货架，尊严的存量固定。但更深的视界在*流动*里看到尊严：让垃圾之海变得可读的审稿人、把范式存活着放进别人脑中的师者、说"要这一件不要那一件"的人——机器让一切加速时，他们只会更被需要。冗余是虚构，它把人数错当成了用心。一条河不会因为某一弯深、某一湾浅就算半空；水在每一个点都是整个河。

**成熟反应长什么样。** 不恐慌（领域没有终结；空白变大了，学科变宽了），也不膜拜（工具并没有做"选题"的那个思考）。没有两岸的河是洪水；没有水的河是沟。岸的职责就是继续做岸——判断、教导、守住标准——并让水去流。数学并不因机器而受损；它在这个世纪第一次被问"数学是做什么用的"。诚实的答案两千年来没变：为那个——遇到某种范式、愿它成真、并想弄明白何以如此的人。机器能给他的范式比以往任何时候都多。它拿不走那份"愿"。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## Conclusion (结语)

**Claim.** The seven questions collapse into one: what do humans keep for themselves when every answer can be computed? The answer this essay defends is neither the theorems (give them away) nor the praise (share it), but the *labors of the border* — choosing what matters, teaching it, and holding the standard by which anything is called true. The unit-distance disproof is the whole argument in miniature: the machine moved the border; humans kept the map. That is not a division of humiliation; it is almost a division of love.

So: is mathematics in crisis? No — mathematics was never healthier, never more open, never more genuinely in love with both its traditions. Are mathematicians? Their identity is being renegotiated in public, under hot light, and that is uncomfortable and entirely survivable. Do not ask whether the machine is the future. Ask who will do the judging, who will do the teaching, who will keep saying *this one matters*. The answer is available, and it has always been available: the human being, in community, doing quietly the work that no proof can certify.
<!-- zh -->
## 结语

**论点。** 七问坍缩成一问：当每一个答案都能被算出来时，人类为自己留下什么？本文辩护的答案既不是定理（交给机器）也不是赞颂（一起分），而是*边界的劳动*——选择什么要紧、把它教出去、并守住"任何东西被称作真"的那条标准。单位距离反例就是全部论证的微缩：机器移动了边界；人类守住了地图。这不是一份屈辱的分工，恰是一份近乎爱意的分工。

那么，数学在危机中吗？没有——数学从未更健康，更开放，从未如此真诚地同时爱着它的两条传统。数学家呢？他们的身份正在聚光灯下被公开重谈，这令人不适，却完全可以存活。不要问机器是否是未来。要问的是：谁来审判，谁来教导，谁继续说着*这一样要紧*。答案是现成的，而且一直现成：人，在共同体里，安静地做着没有任何证明能够认证的工作。
<!-- L1-end -->

---

<!-- L5 -->
<!-- en -->
## Sources (参考文献)

Reliability tiers per house rules: 一手 (primary) · 权威版本 (authoritative edition/translation) · 学界共识·解读 (consensus/interpretive — flagged) · 存疑 (contested). Stable links are given where they exist; where a claim lives only in a secondary report, the citation names the report.

- **一手 — Erdős unit distance disproof (AI-generated):** OpenAI (2026-05-20), "An OpenAI model has disproved a central conjecture in discrete geometry." <https://openai.com/index/model-disproves-discrete-geometry-conjecture/>
- **一手 — human verification of the disproof:** Alon, N., Bloom, T. F., Gowers, W. T., Litt, D., Sawin, W., Shankar, A., Tsimerman, J., Wang, V., Wood, M. M. (2026). "Remarks on the disproof of the unit distance conjecture." arXiv:2605.20695. <https://arxiv.org/abs/2605.20695>
- **一手 — exponent refinement:** Sawin, W. (2026). "An explicit lower bound for the unit distance problem." arXiv:2605.20579. <https://arxiv.org/abs/2605.20579>
- **一手 — prior upper bound:** Spencer, J., Szemerédi, E., Trotter, W. T. (1984). "Unit distances in the Euclidean plane." *Graph Theory and Combinatorics* (Cambridge), 293–303. (No stable link; full citation given.)
- **一手 — AlphaProof / AlphaGeometry 2 at IMO 2024:** Google DeepMind (2024), "AI achieves silver-medal standard solving International Mathematical Olympiad problems." deepmind.google blog. (Publisher page; the score was independently credited to T. Gowers & J. Myers.)
- **一手 — FrontierMath benchmark & v2 correction:** Epoch AI (2024). "FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI." arXiv:2411.04872. <https://arxiv.org/abs/2411.04872>; v2 release note (2026-06-12) fixing errors in 42% of problems: <https://epoch.ai/benchmarks/frontiermath-tier-4-v1>
- **权威版本 — o3/FrontierMath framing dispute:** Meyer, D. (2025-01-21). "'Manipulative and disgraceful': OpenAI's critics seize on math benchmarking scandal." *Fortune*. <https://fortune.com/2025/01/21/eye-on-ai-openai-o3-math-benchmark-frontiermath-epoch-altman-trump-biden> (Interpretive journalism — flagged; the "75.7% on a chosen subset / Epoch not involved in the eval" reading is 学界共识 among critics, not a settled fact.)
- **一手 — new open-problem benchmark with Lean built in:** Adamczewski, T., Bloom, T. F. (2026). "FrontierMath Erdős." Epoch AI. <https://epoch.ai/files/frontiermath-erdos.pdf>
- **一手 — Tao on AI and mathematics:** Tao, T. (2026). "Mathematics in the age of AI." arXiv:2608.16753. <https://arxiv.org/abs/2608.16753> (ICM 2026 lecture essay.)
- **一手 — total-resistance argument (mathematician's own essay):** Weinreich, M. (2026). "The crisis of AI-generated mathematics." arXiv:2608.02859. <https://arxiv.org/abs/2608.02859>
- **一手 — Leiden Declaration:** "Leiden Declaration on Artificial Intelligence and Mathematics" (2026-06-02), 16 researchers / 15 universities. DOI 10.5281/zenodo.20302944. <https://leidendeclaration.ai/> · IMU endorsement circular: <https://www.mathunion.org/fileadmin/documents/2026-06/IMU_AO_CL_8_2026.pdf> · *Nature* editorial (2026-06-18): <https://www.nature.com/articles/d41586-026-01881-2> · Report: Leiden University news (2026-06-02). <https://www.universiteitleiden.nl/en/news/2026/06/leiden-declaration-warns-ai-is-challenging-the-core-values-of-mathematics>
- **学界共识·解读 — Harris on knowledge collapse:** Harris, M. (2026). "Knowledge Collapse." *Boston Review*, Summer 2026. <https://www.bostonreview.net/articles/knowledge-collapse/> (Essay; interpretive.)
- **权威版本 — the competent-moderate view:** Schneier, B., Rafi, K. (2026-08-25). "No, AI Doesn't Mean the End of Mathematics—at Least Not Yet." *The Guardian*, via <https://www.schneier.com/essays/archives/2026/08/no-ai-doesnt-mean-the-end-of-mathematics-at-least-not-yet.html> (Opinion/commentary — flagged.)
- **存疑 — First Proof (Harvard):** challenge of ten unpublished lemmas (Lauren Williams and co-authors); AI solved ≥6/10; second batch registered behind a nonprofit. Reported at Harvard Mathematics pages and in coverage of 2026; no stable institutional link verified at writing — treat the precise figures as 存疑 pending primary records.
- **存疑 — secondary reports:** Tsimerman's reported fatalism and the Cheng–Liu–Gao double-discovery experiment are cited *as reported in* arXiv:2608.02859 and press coverage; not verified at their single primary source.
- **一手 — domain cross-check within this repo:** the disproof's formal entry <../famous_problems/erdos_unit_distance.md> and proof narrative <../proof_narratives/erdos_unit_distance.md> state the same results with their own sources.
<!-- zh -->
## 参考文献

信度分级按家规：一手 · 权威版本 · 学界共识·解读（须标注）· 存疑（有争议）。有稳定链接者给出；仅存于二手报道者，注明该报道。

- **一手 — Erdős 单位距离反例（AI 生成）：** OpenAI（2026-05-20）《An OpenAI model has disproved a central conjecture in discrete geometry》。<https://openai.com/index/model-disproves-discrete-geometry-conjecture/>
- **一手 — 反例的人类核验：** Alon, N., Bloom, T. F., Gowers, W. T., Litt, D., Sawin, W., Shankar, A., Tsimerman, J., Wang, V., Wood, M. M.（2026）《Remarks on the disproof of the unit distance conjecture》。arXiv:2605.20695。<https://arxiv.org/abs/2605.20695>
- **一手 — 指数精化：** Sawin, W.（2026）《An explicit lower bound for the unit distance problem》。arXiv:2605.20579。<https://arxiv.org/abs/2605.20579>
- **一手 — 既有上界：** Spencer, J., Szemerédi, E., Trotter, W. T.（1984）《Unit distances in the Euclidean plane》，*Graph Theory and Combinatorics*（Cambridge），293–303。（无稳定链接，按家规给全书目。）
- **一手 — AlphaProof / AlphaGeometry 2 于 IMO 2024：** Google DeepMind（2024）《AI achieves silver-medal standard solving International Mathematical Olympiad problems》，deepmind.google 博客。（机构页；评分独立归功于 T. Gowers 与 J. Myers。）
- **一手 — FrontierMath 基准及 v2 修正：** Epoch AI（2024）《FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI》。arXiv:2411.04872。<https://arxiv.org/abs/2411.04872>；v2 发布说明（2026-06-12，修复 42% 题目错误）：<https://epoch.ai/benchmarks/frontiermath-tier-4-v1>
- **权威版本 — o3/FrontierMath 口径之争：** Meyer, D.（2025-01-21）《'Manipulative and disgraceful': OpenAI's critics seize on math benchmarking scandal》，*Fortune*。<https://fortune.com/2025/01/21/eye-on-ai-openai-o3-math-benchmark-frontiermath-epoch-altman-trump-biden>（评述性新闻——已标注；"75.7% 来自'精选子集'、Epoch 未参与评测"是批评方共识，非定论。）
- **一手 — 内置 Lean 的开放问题基准：** Adamczewski, T., Bloom, T. F.（2026）《FrontierMath Erdős》，Epoch AI。<https://epoch.ai/files/frontiermath-erdos.pdf>
- **一手 — 陶哲轩论 AI 与数学：** Tao, T.（2026）《Mathematics in the age of AI》。arXiv:2608.16753。<https://arxiv.org/abs/2608.16753>（ICM 2026 演讲文章。）
- **一手 — 彻底抵制论（数学家本人的文章）：** Weinreich, M.（2026）《The crisis of AI-generated mathematics》。arXiv:2608.02859。<https://arxiv.org/abs/2608.02859>
- **一手 — 莱顿宣言：**「Leiden Declaration on Artificial Intelligence and Mathematics」（2026-06-02），16 位研究者 / 15 所大学。DOI 10.5281/zenodo.20302944。<https://leidendeclaration.ai/> · IMU 背书通告：<https://www.mathunion.org/fileadmin/documents/2026-06/IMU_AO_CL_8_2026.pdf> · 《自然》社论（2026-06-18）：<https://www.nature.com/articles/d41586-026-01881-2> · 报道：莱顿大学新闻（2026-06-02）。<https://www.universiteitleiden.nl/en/news/2026/06/leiden-declaration-warns-ai-is-challenging-the-core-values-of-mathematics>
- **学界共识·解读 — 哈里斯论知识坍缩：** Harris, M.（2026）《Knowledge Collapse》，*Boston Review* 夏季刊。<https://www.bostonreview.net/articles/knowledge-collapse/>（论说文，解读性。）
- **权威版本 — 温和有据的观点：** Schneier, B., Rafi, K.（2026-08-25）《No, AI Doesn't Mean the End of Mathematics—at Least Not Yet》，*The Guardian*，转自 <https://www.schneier.com/essays/archives/2026/08/no-ai-doesnt-mean-the-end-of-mathematics-at-least-not-yet.html>（观点/评论——已标注。）
- **存疑 — First Proof（哈佛）：** 十个未发表引理设擂（Lauren Williams 及其合作者）；AI 合计解出 ≥6/10；第二批已在非营利机构名下登记。见哈佛数学系页面及 2026 年报道；成稿时未核到稳定的机构主链接——具体数字按存疑处理。
- **存疑 — 二手报道：** Tsimerman 的末日言论与 Cheng–Liu–Gao"双重发现"实验，均系转引自 arXiv:2608.02859 及媒体报道，未核到单一一手源。
- **一手 — 本仓内部对表：** 反例的形式化条目 <../famous_problems/erdos_unit_distance.md> 与证明叙事 <../proof_narratives/erdos_unit_distance.md>，以各自来源陈述同一结果。
<!-- L5-end -->