# 数学的危机，还是数学家的危机？——AI 时代关于数学的七问 / A Crisis of Mathematics — or of the Mathematicians? Seven Questions in the Age of AI

<!-- L1 -->
<!-- en -->
For thirty years the story has been told as a siege. In 1997 Deep Blue stepped past Kasparov at chess; in 2016 AlphaGo crossed the summit of the world's board games; from 2024 the machines arrived at olympiad mathematics, and in 2026 a conjecture that had stood for eighty years came open like a door. Each time the fortress was declared the last true fortress of the human mind; each time the wall was climbed. This essay refuses both the victory lap and the funeral dirge. It asks, instead, a quieter pair of questions — what exactly has been achieved, and whether the crisis everyone keeps naming has been named correctly. The title is the argument in miniature: whether mathematics is in crisis is not at all clear. That mathematicians are has become very clear indeed.
<!-- zh -->
三十年来，这个故事被讲成一场围城。1997年深蓝越过卡斯帕罗夫执掌的国际象棋；2016年AlphaGo翻过世界棋类之巅；从2024年起，机器抵达奥林匹克数学；2026年，一道静立八十年的猜想应声而开。每一次，那座堡垒都被宣称为人类心智最后的真堡垒；每一次，墙都被人翻了过去。这篇文章拒用庆功的掌声，也拒用出殡的哀歌。它只问一对更安静的问题——究竟成就了什么；人人都在命名的那个危机，是不是叫错了名字。标题就是论点缩小到极致的形：数学是否在危机之中，全然不清楚；数学家正处在危机之中，已经清楚得不能再清楚。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第一章 · 先前的事物与它们的核验 / The Things Done Before, and How Well They Were Proved

The chessboard and the Go board belong to this chapter because they set the atmosphere. They were clean victories over *closed* games — games with a fully written rulebook, no outside reference, a referee able to decide every position. A century of game theory had already shown that such games are search-problems in disguise; what AlphaGo added was the proof that the search could be made fast enough to beat human pattern-recognition on its own terrain. Mathematics is not, at first glance, such a game — and that discrepancy, more than any single result, is what this essay is trying to hold still. Does the arc from chess to Go to mathematics run straight, or does it bend exactly where the rules run out?

When the same four questions — was the claim honestly stated, can anyone reproduce it, did independent experts certify it, was failure disclosed — are put to the period's five loudest mathematics results, they form a staircase rather than a row.

At the 2024 International Mathematical Olympiad, Google DeepMind's AlphaProof and AlphaGeometry 2 solved four of six problems at silver-medal level, including the hardest problem of the year, which only five human contestants had cracked. The scoring belonged to two academics, Timothy Gowers and Joseph Myers; the machine's own solutions ran through a formal checker, Lean. This is the cleanest case on record: a public contest, independent judges, machine-checkable output. It was mathematics done the way its own doctrine longs to do it. The open question was whether the doctrine would survive contact with the other results.

The OpenAI model announced in December 2024 looks from a distance like the same achievement, and from close up like something else. o3 took 25.2% on Epoch AI's FrontierMath, a private benchmark of hundreds of hard problems built by more than sixty mathematicians; a second, higher figure — reported by OpenAI against a "chosen" subset of the problems — then became the headline, and the builders pushed back. Epoch AI stated plainly that it had not run OpenAI's evaluation. How a number is framed, it turns out, is part of the result. The scandal that followed — *Fortune*'s headline is politely called "manipulative and disgraceful" — had a buried coda that matters more than the feud: when Epoch issued a corrected benchmark v2 in June 2026, the revision fixed errors in **42 percent of the original problems**. The benchmark was partly wrong; the model was partly framed; only a public, self-correcting institution could reveal either. That is the single most instructive fact in the episode.

Then came the case that changed the mood. On May 20, 2026, OpenAI announced that one of its models had disproved Erdős's unit-distance conjecture — a landmark open problem since 1946. Nine mathematicians, among them the Fields medalist Timothy Gowers, wrote the verification paper that digested the machine's construction into a proof a human could teach; Will Sawin sharpened the exponent to $\delta = 0.014$. The bounds now read $n^{1.014} \leq u(n) \leq n^{4/3}$, and the gap is wider, not narrower, than it has ever been. Nothing about the world's ability to float on its own foundations failed here; the profession's machinery worked as designed — proposed by a machine, judged by specialists, sharpened by a community. This is the case that made "collaboration" sound like a description instead of a slogan. This cookbook keeps its own record of the result and its proof narrative.

Harvard's "First Proof" experiment ran on a different axis, and produced the more uncomfortable lesson. Ten unpublished research lemmas, prepared by Lauren Williams and her co-authors, were offered as a challenge; the assembled AIs solved at least six of ten. The news was not that they ran, but that *the human reviewers then struggled to verify the machine's proofs* — the bottleneck was not solving but checking, and checking is the profession's oldest, least-paid, most essential act. A second batch has since been registered behind a nonprofit foundation.

The newest standard, announced in September 2026, closes the loop in a way that would have been unimaginable a decade ago. Epoch AI's "FrontierMath Erdős" takes sixty-eight of Erdős's still-open problems, states each one in the Lean proof assistant, and gives every model the same \$300 budget to prove or disprove it on its own. Best score: GPT-6 Astra at 3%. Everyone else: zero. The grader is a machine, so there is no framing to spin and no subset to choose. The Bad Old Days of the benchmark wars are, for one slender slice of mathematics, over.

Read the staircase honestly: AlphaProof's clean contest victory does not prove it is smarter than o3, only that its work could be certified cheaply; Erdős's disproof did not prove the machine had understood anything, only that its construction could be turned into an argument by nine of the world's careful readers. What collapses across these years is not the competence of the machines. What collapses is the industry's way of speaking — the difference between a score and a fact, an announcement and a proof. The mathematics is fine. The claim-making is not.
<!-- zh -->
## 第一章 · 先前的事物与它们的核验

棋盘与围棋盘之所以属于这一章，是因为它们规定了气氛。那是对*封闭*游戏的干净胜利——规则书写完备、无可外援、判官能对任何局局面作出裁决。一个世纪的博弈论早已表明此类游戏无非是伪装的搜索问题；AlphaGo 真正贡献的，是证明搜索可以快得足以在人类模式识别的领地上战胜人类。乍看之下，数学并不是这样的游戏——而这一落差，比任何单项结果都更是本文试图按住不放的东西。从象棋到围棋再到数学的这条弧线，是笔直延伸的，还是在规则用尽之处恰好拐了弯？

把同样的四个问题——表述是否诚实、能否复现、是否经独立专家认证、失败是否与成功一样被披露——依次放到这一时期的五件最响亮的数学成果上，它们排不成一排，而砌成了一座台阶。

在 2024 年国际数学奥林匹克上，Google DeepMind 的 AlphaProof 与 AlphaGeometry 2 以银牌水平解出六题中的四题，其中包括当年最难、全场仅五名人类选手解出的那道题。评分归两位学者——Timothy Gowers 与 Joseph Myers；机器自身的解答通过了形式化检查器 Lean。这是记录里最干净的一例：公开竞赛、独立判官、可机器检查的输出。它是数学按自己教义最渴望的方式做成的一次。开放的问题在于，这条教义在其余成果的冲击下还能不能存活。

2024 年 12 月公布的 OpenAI 模型，远看像同一成就，近看是另一回事。o3 在 Epoch AI 的 FrontierMath 上取得 25.2%——那是一个由六十余位数学家建造的私有题库，数百道硬题；随后，第二个更高的数字——OpenAI 在题库"经挑选"的子集上自报的成绩——成了头条，建题者随即回击。Epoch AI 明确声明：OpenAI 的评测并非他们所跑。原来一个数字怎么包装，本身就是结果的一部分。接踵而至的丑闻——*Fortune* 的标题客气地叫做"操纵、可耻"——底下埋着一则比争吵更重要的尾声：2026 年 6 月 Epoch 发布修正版 v2，修复了原始题库**百分之四十二的题目的错误**。题库部分出错，模型部分被包装，而只有公开、自我纠错的机构才能让二者同时浮出水面。这是整桩事里最富教益的一则事实。

接着是改变气氛的那一桩。2026 年 5 月 20 日，OpenAI 宣布其模型推翻了 Erdős 单位距离猜想——一个自 1946 年以来的里程碑式开放问题。九位数学家（其中包括菲尔兹奖得主 Gowers）写下核验论文，把机器的构造消化成人类能教的证明；Will Sawin 把指数精化为 $\delta = 0.014$。现在的界是 $n^{1.014} \leq u(n) \leq n^{4/3}$，而空白比过去任何时候都更宽。世界赖以漂浮的自洽基础没有任何一处在这里失灵；职业的机器按设计运转——由机器提出、由专家裁决、由共同体精化。正是这一桩，让"合作"听起来像描述而非口号。本 cookbook 为这一结果与它的证明叙事各自留了一份记录。

哈佛的 "First Proof" 实验跑在另一条轴上，给出了更不舒服的一课。Lauren Williams 与她的合作者备下十个未发表的研究引理设擂；众 AI 合计解出至少十个中的六个。新闻不是它们解出来了，而是*人类审稿人随后很难核验机器证明*——瓶颈不在解题，而在核验，而核验是这个职业最古老、最廉价、也最要命的动作。第二批引理此后已在某非营利基金会名下备案。

最新标准在 2026 年 9 月登场，以一种十年前的想象力所不及的方式把循环闭上。Epoch AI 的 "FrontierMath Erdős" 挑出 68 道至今未解的 Erdős 问题，把每一道在 Lean 证明助手中写成陈述，并给每个模型以相同的 \$300 预算令其独立证明或证伪。最高分：GPT-6 Astra 的 3%。其余全部为零。阅卷者是机器，于是没有口径可包装，没有子集可挑选。基准战争那段坏日子，在数学的这细细一格上，宣告结束。

诚实读这座台阶：AlphaProof 的干净竞赛胜利，证明不了它比 o3 更聪明，只证明它的活能被廉价地认证；Erdős 的反例，证明不了机器理解了任何东西，只证明它的构造能被九位最谨慎的读者改写为论证。这些年里崩塌的不是机器的本事。崩塌的是业界说话的方式——分数与事实之间、公告与证明之间的那道分别。数学安然无恙。说话的方式病了。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第二章 · 诸声 / The Voices in the Room

Where there should be one community there are now five, and they are not disagreeing about mechanics. They are disagreeing about what mathematics is *for* — about the value of the activity, about whose work matters, about whether the thing being done, if done by a machine, is still being done.

The integrationists place their faith in the trajectory of chess, Go, mathematics read as one long game and see the machines as the natural next players. Terence Tao's lecture essay for the 2026 International Congress of Mathematicians, "Mathematics in the age of AI," argues from what he calls a Working Hypothesis — a strong version of the "AI Capability Conjecture," namely that AI tools will soon carry out a reasonable fraction of research-level mathematics at reasonable quality and cost. On that bet the bottleneck shifts, he warns, from talent to *verification*: machine proofs will arrive faster than they can be checked, checked proofs faster than they can be read, readable proofs faster than volunteers can referee them. Kevin Buzzard works the same confidence at the level of code, leading a long campaign to formalize Fermat's Last Theorem in Lean precisely so that "checked by machine" becomes an ordinary sentence in the daily life of mathematics.

The institutionalists answer with rules rather than visions. The Leiden Declaration of June 2, 2026 — sixteen researchers from fifteen universities, endorsed by the International Mathematical Union, the American Mathematical Society, and an editorial in *Nature* — counts five threats: plausible but unreliable machine arguments; authorship dissolving; dependence on proprietary tools splitting the profession into haves and have-nots; the overhyping of results by press offices; and the slow erosion of what "understanding" could mean. Peter Scholze, endorsing it, drew the line that matters: the goal of mathematical research is *human* understanding, and mathematics can survive only inside a community of human researchers. Notice what the declaration does *not* ask for. No ban. Disclosure, norms, authorship. A refusal to let the hype of outsiders decide what is true.

The fatalists take the trajectory's logic to the end. Jacob Tsimerman is reported to hold the dark version as a creed: AI will destroy the field and perhaps the world, and mathematicians will have no choice but to use it regardless. There is an internal coherence here that deserves respect; if tools improve forever and refusing them is professional suicide, then progress is doom, and the only open question is whether the field goes down with style.

The resisters make the case for the other side with real force. Max Weinreich's essay "The crisis of AI-generated mathematics" argues for total opposition: AI is an anti-intellectual technology, it short-circuits understanding, devalues knowledge, and will tempt the best mathematicians into abstaining just to keep proving their worth to one another. Patrick Massot has spoken of mathematics being "bombed" by AI. Inside the fierceness is a quiet truth: if checking a flood of machine proofs is thankless and boring, then the profession's prestige economy — which pays for *discovery*, not for *checking* — now punishes exactly the labor that keeps mathematics honest. The resisters are right about the incentive; they may be wrong to think the incentive cannot change.

The moderates, least quoted and perhaps most reliable, draw the line that the later chapters of this essay will test. Bruce Schneier and Kasra Rafi write that today's AIs are strong at searching and recombining existing ideas and weak at building deep, sustained new theory, and that in the short run they remain nowhere near an experienced research mathematician. Michael Harris, in his book *Knowledge Collapse* and in the *Boston Review*, reminds the profession that mathematics was, in Poincaré's phrase, a "free creative art" — one of the last unalienated labors — and asks, quietly, what survives of that dignity under automation.

Now watch the syllogism run behind all five voices, the doomer's engine: *Go is a game; mathematics is also a game; therefore AI will solve mathematics.* Harris quotes it in *Knowledge Collapse* because it is the whole dispute in three lines. The minor premise — mathematics is a game — is doing all the work, and it is doing it dishonestly: it is true only of the formalized slice of mathematics, and everyone in the room knows it. None of the five camps doubts that the *results* are real. The disproof stands; the Lean towers grow. Their disagreement is over the value of the activity itself. And that is the tell. A crisis of mathematics would show up in the content — in theorems collapsing, in truths decaying. Nothing is collapsing. What is renegotiated is employment, authority, prestige, the meaning of a working day, the dignity of the judge. The crisis, if there is one, is a crisis of the mathematicians.
<!-- zh -->
## 第二章 · 诸声

本应是一个共同体的地方，如今有五派，而他们争执的不是机械。他们争执的是数学*做什么用*——这项活动的价值、谁的劳动要紧、一件事如果由机器去做还做不做得算树。

整合派把信念押在"象棋、围棋、数学是一盘长棋"的轨迹上，视机器为自然的下一手。陶哲轩为 2026 年国际数学家大会写的演讲文章《Mathematics in the age of AI》以一个"工作假说"立论——即"AI 能力猜想"的强版本：AI 工具很快将以合理的质量与成本完成相当比例的科研级数学。基于这一赌注，他警告瓶颈将从天赋转移到*核验*：机器证明会比被检查更快地涌来，被检查的证明会比被阅读更快，可读的证明会比志愿审稿人更快。Kevin Buzzard 把同一信心落实在代码层：他领衔长程战役，要在 Lean 中形式化费马大定理，恰是为了让"机器已核验"成为数学日常中一句普通的话。

建制派以规范而非愿景作答。《莱顿宣言》（2026 年 6 月 2 日，十五所大学的十六位研究者，获国际数学联盟、美国数学会与《自然》社论背书）点数出五重威胁：可信但不可靠的机器论证；作者权瓦解；对专有工具的依赖把职业劈成有与无的两半；新闻办公室对成果的过度炒作；以及"理解"一词的含义被缓慢侵蚀。Peter Scholze 在背书时划出要命的界线：数学研究的目标是*人的*理解，数学只能在人类研究者的共同体中存活。注意宣言*没有*要求什么。没有禁令。披露、规范、作者权。拒绝让外行的炒作决定什么为真。

末日派把那条轨迹的逻辑推到尽头。据传 Jacob Tsimerman 以信条持有暗色版本：AI 会毁掉这个领域，也许毁掉世界，而数学家无论何等不情愿都别无选择只能用。这里有一种值得敬重的自洽：如果工具永远精进、拒绝即职业自杀，那么进步即末日，唯一开放的问题只剩这个领域以何种风度倒下。

抵制派为另一侧提出了真正有力的论据。Max Weinreich 的文章《The crisis of AI-generated mathematics》主张彻底抵制：AI 是反智的技术，短路理解、贬低知识，还会诱使最好的数学家罢手不用，只为彼此证明价值。Patrick Massot 则称数学正被 AI "轰炸"。凶猛内部藏着一句安静的实话：如果核验海量机器证明既无回报又无聊，那么职业的声望经济——它付钱给*发现*而非*核验*——如今恰好惩罚那个让数学保持诚实的动作。抵制派对激励的洞察是对的；"这激励改变不了"的悲观，则未必对。

温和派被引最少，也许最可靠，他们划出的界线正是本文后几章要检验的。Bruce Schneier 与 Kasra Rafi 写道：今日之 AI 强于搜索与重组既有观念，弱于建造深刻而持续的新理论；短期内，他们仍远不及一位有经验的研究型数学家。Michael Harris 在《Knowledge Collapse》与《波士顿评论》中提醒职业界：按庞加莱的话，数学曾是"自由创造的艺术"——所剩无几的未异化劳动之一——并安静地问：自动化之下，这尊严还剩什么。

现在看那条在三段论后面转动的、末日派的引擎：*围棋是博弈；数学也是博弈；因此 AI 将解出数学。* 哈里斯在《Knowledge Collapse》里引用它，因为它是整场争执的三行压缩。小前提——数学是博弈——扛着全部重担，而它扛得不诚实：它只对数学被形式化的那一格成立，而房间里所有人都知道。五派没有一派怀疑*成果是真的*。反例立得住；Lean 的高塔在长高。他们争执的是活动本身的价值。而这就是线索。数学的危机应当显形于内容——定理崩塌、真理朽坏。没有东西在崩塌。被重谈的是就业、权威、声望、一个工作日的意义、判官的尊严。如果说有危机，那是数学家的危机。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第三章 · 数学是一种语言 / Mathematics Is a Language

Every crisis in this conversation comes back to one confusion, and it can be named in three words: the signifier and the signified. Mathematics is a language — a system of signs, of 能指, in which we draw whatever we want to say exactly; and a language is never the thing it speaks of. The map is not the territory; the score is not the music; the watermark of a proof is not the pattern it proves. When the machines arrived, much of the panic came from quietly forgetting this: from treating the language as if it were the object, as if formalizing the proof of a theorem were the same as touching the truth it states. It is not. The grammar can be perfect and the world unchanged.

Saussure understood why this confusion is built into every language. The signifier is not fixed to the signified by any necessity: "tree" and Baum and arbre all carry the same weight across languages, and nothing about the wood demands any of them. The link between sign and object is arbitrary — but the *structure* that the signs recreate is not arbitrary at all. When mathematics says "group" it is only a symbol for a certain arrangement of operations; the arrangement itself does not depend on which symbol we chose. This is why mathematics can be re-described the way it is: because the language is portable, the necessity it encodes is not. Human mathematicians spend careers shuffling signifiers — changing the number system, the definition, the category — because the signified, the structure, is what survives the shuffle.

Read the unit-distance disproof through this lens and it becomes almost eerie. The machine did not discover new facts about dots on a plane; it replaced one signifier with a richer one. It took the geometry of unit distances — expressed for eighty years in the language of Gaussian integers, whose symmetries are finite — and re-expressed it in the language of algebraic number fields, whose symmetries are inexhaustible. The signified was off-stage the whole time; what changed was the language in which the question was drawn, and the answer simply became visible. Whoever controls the re-description, the chapter's lesson runs, controls the deepest work in mathematics — and the machine has just shown it can re-describe.

None of this makes mathematics arbitrary, and none of it makes it a first cause. Mathematics is not the thing the universe is *made of*; it is the most exact language yet found for speaking about relations that hold necessarily, whatever noun we paint them with. Kant called such truths synthetic a priori — they add to our knowledge, yet hold independently of experience. The formalist tradition answered from the other shore: truth is consistency in a game of symbols. Gödel's incompleteness theorems in 1931 put a wall through that game — any sufficiently strong consistent system states truths it can neither prove nor refute, and cannot certify its own consistency. And then something undramatic happened: mathematics simply went on working, on what Tao calls "naive" foundations, and prospered. The foundation crisis that had once seemed fatal ended in resignation, and the field did not mind. Its oldest lesson may be that the language works whether or not we can certify the language.

Two consequences follow for everything claimed in these years. First, verification — Lean checks, expert read-throughs — is a matter of the signifier: it certifies that the translation is faithful, that the signs were shuffled lawfully. It cannot certify that the signified was worth attending to. Second, the freedom to change the language is both mathematics' deepest liberty and its most human act: no formal system decides which re-description is worth the next twenty years. That judgment — which language will let the truth show itself — is not theorem-shaped, and it is not machine-shaped either. Not yet.
<!-- zh -->
## 第三章 · 数学是一种语言

这场对话里的每个危机，最终都能回落到一个混淆上，三个字足以命名：能指与所指。数学是一种语言——一套符号、一层能指，我们用它把想说之物画得分毫不差；而语言从不等于它所言说之物。地图不是领土；乐谱不是音乐；证明的水印不是它所证的范式。机器到来时，恐慌的一大部分来自悄悄忘掉这件事：把语言当成了对象，好像把定理的证明形式化了，就等于触到了它所陈述的真理。并非如此。语法可以完美无缺，而世界纹丝不动。

索绪尔明白这种混淆为何内建于一切语言。能指并不受必然性捆绑于所指："树"与 tree 与 arbre 在各语言里负着同一重量，而木头的任何性质都不要求其中任一个。符号与对象之间的联结是任意的——但符号所再造的*结构*却绝非任意。数学说"群"时，它只是某个运算布局的符号；这布局本身并不取决于我们选了哪个符号。正因如此，数学得以如此被重新刻画：因为语言是可搬运的，它所编码的必然性不是。人类数学家以毕生来回倒腾能指——换数系、换定义、换范畴——因为所指，那结构，才是倒腾之后幸存下来的东西。

以此透镜读单位距离反例，几乎骇人。机器并非发现了关于平面上点的什么新事实；它只是用一个更富饶的能指替换了原来的。那道单位距离几何被表达了八十年——用的是高斯整数的语言，其对称性有限——如今它被重新表达进代数数域的语言，其对称性取之不竭。所指全程都在后台；变的是描绘这个问题所用的语言，而答案由此变得可见。谁掌握重新刻画，这一章的教训就落到哪里——谁就在做数学里最深的活；而机器刚刚证明，它会重新刻画。

这一切既不使数学变得任意，也不使它成为第一因。数学不是宇宙*由之构成*的东西；它是有史以来对"必然成立的关系"做言说的最精确语言，无论我们用什么名词去涂它们。康德把这类真理称为先天综合判断——它们增长知识，却又独立于经验而成立。形式主义传统从对岸回应：真理即符号博弈的自洽。哥德尔 1931 年的不完备定理在这博弈中立起一堵墙——任何足够强的自洽体系都陈述着它既不能证也不能否的真理，且无法认证自身的自洽。然后发生了一件毫无戏剧性的事：数学只在"朴素基础"上继续运转——按陶的话——并且兴旺。一度看似致命的基础危机，以认输收场，而领域并不在意。它最老的教训也许是：语言能用与否，无需认证语言本身。

对这些年的一切宣称，由此推出两条后果。其一，核验——Lean 检查、专家通读——是能指层面的事：它认证翻译是忠实的、符号的倒腾合乎法度。它认证不了所指是否值得关注。其二，更换语言之自由，既是数学最深的自由，也是它最属人的动作：没有形式系统会决定哪一次重新刻画值得付出下一个二十年。那个判断——哪一种语言会让真理现身——不是定理的形状，也还不是机器的形状。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第四章 · 数学家是谁 / Who, Then, Are the Mathematicians?

The word "mathematician" names a ladder, not a kind, and the public confuses the rungs deliberately because the ladder is flattering. At the bottom stands the solver — the olympiad student, timed, pattern-matching under a clock; the image that dominates every article about "smart people." Above her the researcher, proving things nobody has proved, mostly small, mostly by extension. Above that the theory-builder, assembling results into architecture — a Weil, a Grothendieck. At the top the field-founder, who says the whole conversation should change: Descartes, Newton, Gauss. Confusing the first rung for the fourth — as the press and the hype cycle do constantly — is like deciding that because the fastest sprinter is athletic, she is the best architect. Attention is the only currency that gets no discount for this.

What the top of the ladder actually does all day has changed within a single generation: from paper and ink, to verifying at a keyboard, to — since 2026 — deciding when to let a machine propose and when to demand a proof a human can carry. The prestige economy strains under the change. Joel David Hamkins has written of despairing at an ocean of slop overwhelming the journals; Daniel Litt warns of "pollution of the commons by AI-generated nonsense." The scarcity is not correctness; it is attention, and the attention-keepers are unpaid.

And why, outside the profession, is "mathematician" nearly the same word as "brilliant"? Five forces, none of them about aptitude. *History* has manufactured the cult of the solitary genius — Gauss, Erdős — a storyteller's invention that flattens decades of communal effort into a single flash. *Psychology* trains intuition and rigor as separate muscles and markets them as one gift; people fluent in both are rarer than the stereotype admits. *Gatekeeping* — the olympiad system, the ritual of formalization — decides early and cheaply whom the profession will treat as promising, and it is a filter built for speed and neatness, not for depth. *Information asymmetry* hides all the process: outsiders see the finished proof, inevitable and clean, never the two years of dead ends that made the residue look effortless. *Cognitive bias* does the rest — survivorship bias (only the winners are visible), halo effect (one brilliant theorem licenses everything adjacent). The society that is now scandalized by a benchmark's cherry-picked subset has been running that exact inflation on human beings for three centuries. The machine merely returns the compliment.

Unlace the knot and the job description becomes visible, and it was never "be brilliant." It is: carry the community's standards, extend what nothing else has extended, and at the top decide — in the fullest sense of deciding, with one's whole judgment and skin in the game — what the community should work on next. Those are labor categories, not grade scores. The tragedy of the present moment is that this is exactly what the profession stopped being able to say out loud. The panic comes from identifying mathematics with the grade: if the machines score, what is left of the humans? The honest answer — everything that judges, teaches, and cares — sounds sentimental and is simply true.
<!-- zh -->
## 第四章 · 数学家是谁

"数学家"一词命名着一架梯子，而非一种人；公众刻意混淆梯级，因为梯子讨人喜欢。底层站着解题者——计时赛场上的奥赛学生，在倒计时下做模式匹配；每一篇谈"聪明人"的文章都以他做门面。其上是研究者，证明无人证过之物，多数很小，多数靠延伸。再上是理论建造者，把结果装配成建筑——一个 Weil，一个 Grothendieck。顶端是领域开创者，他说：整场对话都该换了——笛卡尔、牛顿、高斯。把第一级混作第四级——媒体与造神周期乐此不疲——好比因为最快的短跑运动员有运动天赋，就认定她是最佳建筑师。唯一不打折的通货是注意力。

梯子顶端的人一天天到底在做什么，在一代人之内变了形：从纸墨，到键盘上的核验，再到——2026 年以来——决定何时让机器提案、何时索要人类能带走的证明。声望经济在变化中承压。Joel David Hamkins 写他对着淹没期刊系统的垃圾之海绝望；Daniel Litt 警告"AI 生成的垃圾污染公地"。稀缺的不是正确性，是注意力，而看护注意力的人没有薪水。

而在职业之外，"数学家"为什么几乎成了"才华横溢"的同义词？五股力量，无一关乎天赋。*历史*制造了孤胆天才崇拜——高斯、埃尔德什——那是小说家的发明，把数十年的共同体劳作压扁成一道闪光。*心理*把直觉与严格各自练成两块肌肉，再作为一样天赋出卖；两者皆流利者远比刻板印象以为的稀少。*守门*——奥赛体系、形式化的仪式——在很早、很便宜的地方决定职业将把谁当作可造之材，而这过滤器为速度与整洁而建，不是为深度。*信息不对称*藏起了全部过程：外人只见成品证明——无可逃避、干净利落——永不见那两年死胡同，是它们让残渣显得毫不费力。*认知偏差*接管了剩下的——幸存者偏差（只有赢家可见）、光环效应（一条漂亮定理给一切邻近之物盖章）。那个如今为基准挑选子集而震惊的社会，三百年来一直对人类跑着同一场通货膨胀。机器不过是以其人之道还施其人之身。

解开这结，职位描述便现形，而它从来不是"要聪明"。它是：承托共同体的标准、延伸无人能延伸之处、并且——在最高处，以全部的判断与身家性命来"决定"——决定共同体接下来该做什么。这些是劳动的分类，不是分数的等级。此刻的悲剧是，这恰是这个职业不再能说出口的东西。恐慌源于把数学等同于分数：如果机器会得分，人类还剩下什么？诚实的答案是——一切判断、教授与在乎的东西——听来煽情，却只是真话。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第五章 · 形式化之后的分工 / The Division of Labor After Formalization

Set down the relations plainly, because everything else in this chapter hangs on them: *quantifiable* ⊂ *computable* ⊂ *formalizable* ⊂ *mathematics*. Logic is special — it is the skeleton of every formal system and at the same time one of mathematics' own objects, studied mathematically by proof theory. The point is the nesting, not the labels. Everything a machine has "solved" lives inside the formalizable stratum. The Erdős disproof lives there — that is why it could be certified. So did every move of chess and Go. The games trajectory and the mathematics trajectory overlap exactly on this stratum, no further.

Here, then, is the honest measure of the trajectory from chess to Go to mathematics. What carries across is the *rule-governed core*: a domain whose correctness can be checked without appeal to context. Chess is fully checked; Go nearly; the formalizable slice of mathematics is fully checked in principle. That is why the same search-technique keeps advancing from one fortress to the next. What does not carry across is everything around that core — the choice of which game to study, the judgment of which move is *important* rather than merely legal, the decision that this conjecture and not that one should receive the next decade. No referee can certify importance, because importance is not a position on a board. The trajectory runs straight precisely until the rules run out; then it bends. Bent is not broken.

In the formalizable stratum the machine's advantage is no longer speed. It is indifference to the obvious — the willingness to try a language a human expert has long since learned to call irrelevant. Humans knew the right picture of the unit-distance problem; famously, the picture was the cage. The machine, unbothered, tried another number system and walked out. On bounded, checkable, searchable tasks, larger-than-human search now beats individual human search — period. First Proof adds the unsettling corollary: the machine can outrun not only the solver but the *verifier*, producing arguments before human referees can judge them.

The division of labor then writes itself, which is why the current panic is so ill-targeted. Machines: propose, construct, formalize, and check. Humans: choose the goal, choose the language, judge importance, keep the community's standards, and — in Tao's word — *digest*: turn verified results into something a mathematician can carry in her head. Every bottleneck the optimists and fatalists both predict — proofs outrunning verification, verification outrunning write-ups, write-ups outrunning referees — makes the human half more scarce, not less. Attention is finite; the machine manufactures supply, not demand. The human being who converts machine output into understanding is not being automated away. She is being promoted.

One correction belongs in this chapter before it ends, and it is the correction the whole conversation tends to skip. "Western mathematics," the axiomatic, formal, set-theoretic tradition, is one dialect of saying precisely — not the language itself. The Chinese algorithmic tradition — *The Nine Chapters*, celestial-source algebra (天元术), the Yang Hui / Jia Xian triangle — is mathematics of the first rank; it *computed* what the axiomatic style later *proved*. "Modern mathematics can stand for all mathematics" is a statement of institutional reach, not of content. The 2026 disproof is a happy reminder that the levers that broke Erdős's conjecture — unit groups, algebraic number fields — were built by an arithmetic tradition older than the modern-foundations fashion. Wisdom is not Western; the machines have been reading every dialect at once.
<!-- zh -->
## 第五章 · 形式化之后的分工

先把诸关系摆平，因为本章其余一切都要挂在它们上面：*可量化* ⊂ *可计算* ⊂ *可形式化* ⊂ *数学*。逻辑是特殊的——它是每个形式系统的骨架，同时又是数学自身的对象之一，由证明论以数学方式研究。关键在于嵌套本身，而非标签。凡机器"解出"的一切，都住在可形式化的那一层。Erdős 反例住在那里——所以它才可能被认证。象棋与围棋的每一步也都住在那里。博弈轨迹与数学轨迹，恰好、且仅在，在这层相叠。

那么，从象棋到围棋再到数学的这条轨迹，诚实度量如下。能搬过界的，是*受规则支配的内核*：一个正确性无需援引语境即可判定的疆域。象棋全可判；围棋近乎全可判；数学可形式化的一格，原则上全可判。这就是为什么同一套搜索技法能一座堡垒接一座堡垒前进。搬不过界的，是内核周围的一切——研究哪一局棋的选择、判哪一手*重要*而非仅仅合法、决定这一道猜想而非那一道应当赢得下一个十年。没有判官能认证重要性，因为重要性不是棋盘上的一个位置。轨迹笔直延伸，严格直到规则用尽之处；然后它拐弯。拐弯不等于断裂。

在可形式化的一层，机器的优势已不是速度。是对"显而易见"的无感——乐于尝试人类专家早已学会称之为无关的语言。人类知道单位距离问题的正确画面；众所周知，那画面就是笼子。机器不受打扰，试了另一个数系，便走了出去。在有界、可检、可搜的任务上，超越单人的搜索如今战胜单人的搜索——没有例外。First Proof 追加了令人不安的推论：机器不但跑赢解题者，还跑赢*核验者*——在人类判官能够裁决之前，就产出论证。

分工于是自行写就，这正是当下恐慌为何错失靶心。机器：提案、构造、形式化、检查。人类：选择目标、选择语言、判别重要性、守住共同体的标准、并且——用陶的话——*消化*：把被验证的结果，变成数学家能装进脑子带走的形状。乐观派与末日派共同预测的每一个瓶颈——证明跑赢核验、核验跑赢书写、书写跑赢审稿——都只会让人类那一半更稀缺，而非更冗余。注意力是有限的；机器制造供给，不制造需求。那个把机器输出转译成理解的人，并没有被自动化掉。她被升职了。

本章结束前还需放上一条更正，而它是整场对话惯常跳过的更正。"西方数学"——公理化、形式化、集合论的传统——只是"精确言说"的一种方言，而非语言本身。中国算法传统——《九章算术》、天元术、杨辉/贾宪三角——是一流数学；它*计算*出了公理化风格后来才*证明*的东西。"现代数学可以代表全部数学"谈的是制度版图，不是内容版图。2026 年的反例是个愉快的提醒：撬开 Erdős 猜想的杠杆——单位群、代数数域——出自一个比现代基础时尚更古老的算术传统。智慧没有国籍；机器正在同时读着每一门方言。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第六章 · 开创性问题之争 / The Dispute About Groundbreaking Problems

"Groundbreaking" must mean more than "hard." A theorem advances a frontier; a breakthrough moves the border itself — a new definition, a new language, a field turned toward a new object. Descartes' coordinates made geometry algebra and algebra geometry. Newton's and Leibniz's calculus gave change itself a syntax. Gauss rebuilt number theory so that "law" meant "pattern with a proof." The common thread is the re-description of Chapter 3 performed at the scale of a discipline.

By that standard, where does the machine stand? On the public record, it has shown the *cross-language* half of the act and not yet the *language-building* half. The unit-distance disproof is a first-rate theorem — a paradoxical counterexample family, an exotic leap from number theory into geometry — but it resolves a question mathematicians had posed, in a dialect (algebraic number theory) that already existed. Schneier and Rafi's distinction still holds: strong at recombination, unproven at theory-building. Nothing in the record yet shows an AI constructing a genuinely new system of concepts — the way category theory was new, the way sheaf theory was new. The games trajectory, read precisely, predicts this: it advances steadily inside a given rule-system; it has not yet been seen founding one.

And here the anti-AI argument commits its own version of the ladder confusion. It sets the bar at "groundbreaking problems" as if that were the normal output of a mathematician — when the honest fact is that hardly any mathematician ever poses one. Hilbert's twenty-three problems redirected a century, and the hundred mathematicians who understand his list is a generous estimate. Erdős spent a career *distributing* roughly fifteen hundred problems and became, largely by that generosity, the most famous mathematician of his day. Most published mathematics is consolidation — extending, cleaning, sharpening a frame someone else built. If "AI cannot pose groundbreaking problems" is the test, it is a test that prunes almost all humans too. Posing deep questions is rarer than the myth admits, it is distributed wildly unequally, and it is not obviously a formal skill — which puts the slogan "tools can never do it" in exactly the category of the older slogan "tools can never do it": a bet dressed as a law.

The historical interlude belongs in this chapter because it defeats the strongest version of the disbelief. Descartes, Newton, Leibniz, Gauss were not narrowly "pure mathematicians"; they were polymaths — philosophy, physics, mechanics, astronomy, geodesy, metaphysics as one fabric. Their breakthroughs were cross-domain intuitions: secularizing the mystical, algebraizing the geometric, timing the falling. If "what AI does is just recombination," then so has been every breakthrough worth the name; recombination *across* domains is the engine of the history they all wrote. And the 2026 disproof is precisely a polymath-style move — number theory imported into geometry — the first the public has watched a machine make. The honest reservation is therefore not "machines can only recombine." It is "machines have not yet shown judgment about which future is worth building" — and neither, in the noise of the present, are many of the humans holding the microphone.

The deepest act in the profession — deciding that this, not that, matters — is a social judgment about value, exercised by a community over time. AI will flood the docket with filings; it will not, on today's evidence, decide the case. What 2026 proved is that the *border-moving* problem is answerable by search once the language is given. What remains is selecting the language — and the lesson of the last eighty years of the unit-distance problem is that no referee, human or machine, can certify which selection was *important* until long after the fact. Importance is a verdict of history, not a verdict of proof.
<!-- zh -->
## 第六章 · 开创性问题之争

"开创性"必须意味着不止"困难"。定理推进边界；突破移动边界本身——一个新定义、一门新语言、一个转向新对象的领域。笛卡尔的坐标让几何成为代数、代数成为几何。牛顿与莱布尼茨的微积分为"变化"本身造了一句语法。高斯重构数论，使"定律"意味着"有证明的模式"。共同线索，是第三章的"重新刻画"，以**学科**的规模实施。

按此标准，机器站在何处？就公开记录而言，它展示了那动作的*跨语言*一半，尚未展示*造语言*一半。单位距离反例是一流定理——一组悖论式反例族，一次从数论跃进几何的奇崛跳跃——但它所解决的问题，是数学家提出来的，用的是已存在的方言（代数数域论）。Schneier 与 Rafi 的区分依然成立：重组为强，建理论未证。记录里还没有任何东西表明 AI 构造了一门真正新的概念体系——那种范畴论之新、层论之新。博弈轨迹若读得精确，恰预言此点：它在给定的规则系统内部稳步前进；开宗立派，至今未见。

而反 AI 的论证在此犯下它自己版本的梯级混淆。它把标杆设在"开创性问题"，仿佛那是数学家的常规产出——而诚实的事实是，几乎没有任何数学家提出过。希尔伯特的二十三个问题重新定向了一个世纪，而能读懂他那张清单的百来位数学家，已是慷慨的估计。埃尔德什以毕生*分发*约一千五百个问题，并且大体上凭这份慷慨，成了他那个时代最著名的数学家。已发表数学的多数是巩固——延伸、清洗、磨利别人搭好的框架。倘若"AI 提不出开创性问题"是考题，那它是一道同样淘汰了几乎所有人类的考题。提出深刻问题，比神话所承认的更罕见、分配得极端不均、且显然不是一项形式化技能——这把"工具永远做不到"的标语，归入旧标语"工具永远做不到"的同一类：一个穿上法律外衣的赌注。

历史插曲之所以属于本章，是因为它击败了怀疑的最强版本。笛卡尔、牛顿、莱布尼茨、高斯都不是狭隘的"纯数学家"；他们是多面手——哲学、物理、力学、天文、测地、形而上学，同一匹织物。他们的突破是跨域直觉：把神秘学世俗化、把几何代数化、为下落计时。若说"AI 所做无非重组"，那么古往今来值得引用的突破，无一不是重组；*跨域*重组*正是他们共同书写的那部历史的引擎。而 2026 年的反例恰是标准的多面手动作——把数论引进几何——这是公众第一次眼看着一部机器做出来。因此，老实的保留意见不是"机器只会重组"，而是"机器尚未展现'哪个未来值得造'的判断"——而眼下这噪声里，握着麦克风的人类，许多也未必有这个判断。

这个职业里最深的动作——判定这一件而非那一件要紧——是一种关于价值的社群判断，由共同体在时间里行使。AI 会往案头塞满诉状；按今天的证据，它不会判案。2026 年证明的是：*移动边界*的问题，一旦语言给定，搜索即可作答。剩下的，是选择语言——而单位距离问题过去八十年的教训是，没有任何判官，无论人或机器，能在时过境迁之前认证哪一次选择*重要*。重要性是历史的判决，不是证明的判决。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第七章 · 相融而不言其名 / Containment, Without the Vocabulary

Say it in words cheap enough for anyone, purged of every borrowed term: nothing stands alone; everything holds everything else up; the tool is part of the mountain. The score is not the music, but the music is not the score either, and neither exists without the other. No school names, no incantations — just the plainest available truth, which has been available for two thousand years and has never been less urgent than it is now.

All of it is connected in practice, not in poetry. The 2026 disproof needed a number system nobody had connected to the geometry; the benchmarks needed sixty mathematicians; the formalizers needed a century of Lean; the models needed the canon the profession had spent generations building. Remove any strand and the story snaps. Gowers and his eight co-authors did not "beautify a machine's output"; they did half the mathematics, in the oldest sense — turning an unheard claim into something teachable, checkable, alive. Neither party wrote the result alone. The result *was* the meeting. That is not a metaphor; it is a description of the working week.

The sharp nouns — "solve," "understand," "author," "replace" — keep collapsing the moment the relation moves. The machine solved what no human, for eighty years, could; the verification paper made it understood; nobody owns the verb that spans both. Water is not fighting the river for being wetter here than there. A tool that extends a mathematician's reach is not distinguishable, in the life of that mathematician, from a theorem that extends everyone's reach: both are simply more mathematics. The logic that insists "the machine did it and the human did not" is the same logic that would insist the hammer built the house.

The fear of redundancy dissolves the same way, because it was a category error from the start. It assumes a zero-sum shelf of roles and a fixed stock of dignity. Look longer and dignity is found in the movement: the referee who makes the slop readable, the teacher who keeps the pattern alive in another person's mind, the one who at the table says *this, not that*. Every predicted bottleneck makes these more needed, not less. Redundancy confuses the number of people with the amount of care. A river is not half-empty for being deep in one bend and shallow in another; the water is the whole river at every point.

And what is the fitting reply to the honest fear — "will I still be needed?" The fitting reply is not reassurance. It is the oldest partition of labor we have: the banks do not worry whether the water needs them; they hold, and the water runs. A river without banks is a flood; a river without water is a ditch. The profession's job is to stay the bank — to judge, to teach, to keep the standard that says what may be called true — and to let the water move. Mathematics is not endangered by the machine. It is being asked, for the first time in living memory, what it is *for*; and the honest answer has not changed in two thousand years: it is for the human who meets a pattern, wants it true, and wants to understand why. The machine can hand that human more patterns than any century before. What it cannot do is take the wanting.
<!-- zh -->
## 第七章 · 相融而不言其名

用便宜到人人都懂的话说，洗尽一切借来的词：没有什么是独自成立的；一切都托举着别的一切；工具本身是山的一部分。乐谱不是音乐，但音乐也不是乐谱，二者缺其一便都不存在。不提学派名字，不念任何咒语——只要那最直白的真话；它已备在那里两千年，而此刻它从未如此要紧。

一切都在实践里相连，而非在诗意里相连。2026 年的反例需要一个无人把它连到几何上的数系；基准需要六十位数学家；形式化者需要一个世纪的 Lean；模型需要这个职业几代人垒起来的正典。抽掉任何一股，故事就断。Gowers 与其八位共同作者并不是在"美化机器的输出"；他们做了数学的一半，以最古老的意义——把一句从未听过的断言变成可教、可检、活着的东西。没有哪一方独自写下结果。结果*就是*那场相遇。这不是比喻；这是对一个工作周的描述。

那些锋利的词——"解出"、"理解"、"作者"、"取代"——每逢关系移动便纷纷塌缩。机器解出了人类八十年未能解出的东西；核验论文使它被理解；横跨两者的动词无人认领。水不会因为此处在彼处更湿，就与河流搏斗。一件延伸数学家臂膀的工具，在数学家的生命里，同一个延伸了所有人臂膀的定理无从区分：二者都只是更多的数学。"是机器做的、不是人做的"这套逻辑，与"是锤子盖的、不是工匠盖的"同一路货。

对冗余的恐惧同样化解，因为它从一开始就是范畴错误。它预设一块零和的角色货架、一份固定的尊严存量。看得更久些，尊严在*流动*里：让垃圾之海变得可读的审稿人、把范式活着放进别人脑中的师者、在桌边说"要这一件不要那一件"的判官。每一个被预言的瓶颈都只会让他们更被需要，而非更冗余。冗余把人数错当成了用心。一条河不会因为某一弯深、某一湾浅就算半空；水在每个点都是整条河。

至于那个诚实的恐惧——"我还会被需要吗？"——恰当的回应不是安慰。是那份我们最古老的分工：岸从不担心水需不需要它；它守着，水自流过。没有两岸的河是洪水；没有水的河是沟。职业的职责是继续做岸——判断、教授、守住"什么可被称作真"的标准——并让水流。数学并不因机器而受损。它在这个世纪第一次被问"数学是做什么用的"；诚实的答案两千年来未变：为那个遇见范式、愿它成真、又想知道它为何真的。机器能递给这位人的范式，比此前任何世纪都多。它拿不走那份"愿"。
<!-- L1-end -->

---

<!-- L5 -->
<!-- en -->
## A Note on Sources (来源与考证)

Reliability tiers per the house rules: 一手 (primary) · 权威版本 (authoritative edition/translation) · 学界共识·解读 (consensus/interpretive — flagged) · 存疑 (contested). Stable links are given where they exist; where a claim lives only in secondary reports, the citation names the report.

- **一手 — the Erdős disproof (machine-generated):** OpenAI (2026-05-20), "An OpenAI model has disproved a central conjecture in discrete geometry." <https://openai.com/index/model-disproves-discrete-geometry-conjecture/>
- **一手 — human verification paper:** Alon, N., Bloom, T. F., Gowers, W. T., Litt, D., Sawin, W., Shankar, A., Tsimerman, J., Wang, V., Wood, M. M. (2026). "Remarks on the disproof of the unit distance conjecture." arXiv:2605.20695. <https://arxiv.org/abs/2605.20695>
- **一手 — exponent refinement:** Sawin, W. (2026). "An explicit lower bound for the unit distance problem." arXiv:2605.20579. <https://arxiv.org/abs/2605.20579>
- **一手 — prior upper bound:** Spencer, J., Szemerédi, E., Trotter, W. T. (1984). "Unit distances in the Euclidean plane." *Graph Theory and Combinatorics* (Cambridge), 293–303. (No stable link; full citation given.)
- **一手 — AlphaProof / AlphaGeometry 2 at IMO 2024:** Google DeepMind (2024), "AI achieves silver-medal standard solving International Mathematical Olympiad problems," deepmind.google blog. (Publisher page; the score was independently credited to T. Gowers & J. Myers.)
- **一手 — FrontierMath and its v2 correction:** Epoch AI (2024). "FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI." arXiv:2411.04872. <https://arxiv.org/abs/2411.04872>; v2 release note (2026-06-12), which fixed errors in 42% of problems: <https://epoch.ai/benchmarks/frontiermath-tier-4-v1>
- **权威版本 — the o3/FrontierMath framing dispute:** Meyer, D. (2025-01-21). "'Manipulative and disgraceful': OpenAI's critics seize on math benchmarking scandal." *Fortune*. <https://fortune.com/2025/01/21/eye-on-ai-openai-o3-math-benchmark-frontiermath-epoch-altman-trump-biden> (Interpretive journalism — flagged; "75.7% on a chosen subset; Epoch not involved in the eval" is 学界共识 among critics, not a settled fact.)
- **一手 — open-problem benchmark with Lean built in:** Adamczewski, T., Bloom, T. F. (2026). "FrontierMath Erdős." Epoch AI. <https://epoch.ai/files/frontiermath-erdos.pdf>
- **一手 — Tao on AI and mathematics:** Tao, T. (2026). "Mathematics in the age of AI." arXiv:2608.16753. <https://arxiv.org/abs/2608.16753> (ICM 2026 lecture essay.)
- **一手 — the total-resistance argument:** Weinreich, M. (2026). "The crisis of AI-generated mathematics." arXiv:2608.02859. <https://arxiv.org/abs/2608.02859>
- **一手 — the Leiden Declaration:** "Leiden Declaration on Artificial Intelligence and Mathematics" (2026-06-02), sixteen researchers, fifteen universities. DOI 10.5281/zenodo.20302944. <https://leidendeclaration.ai/> · IMU endorsement circular: <https://www.mathunion.org/fileadmin/documents/2026-06/IMU_AO_CL_8_2026.pdf> · *Nature* editorial (2026-06-18): <https://www.nature.com/articles/d41586-026-01881-2> · Report: Leiden University news (2026-06-02). <https://www.universiteitleiden.nl/en/news/2026/06/leiden-declaration-warns-ai-is-challenging-the-core-values-of-mathematics>
- **学界共识·解读 — Harris:** Harris, M. (2026). "Knowledge Collapse." *Boston Review*, Summer 2026. <https://www.bostonreview.net/articles/knowledge-collapse/> (Essay; the chess/Go/math syllogism is quoted from it — interpretive.)
- **权威版本 — the moderate view:** Schneier, B., Rafi, K. (2026-08-25). "No, AI Doesn't Mean the End of Mathematics—at Least Not Yet." *The Guardian*, via <https://www.schneier.com/essays/archives/2026/08/no-ai-doesnt-mean-the-end-of-mathematics-at-least-not-yet.html> (Opinion/commentary — flagged.)
- **存疑 — First Proof (Harvard):** a challenge of ten unpublished lemmas (Lauren Williams and co-authors); AI solved ≥6/10; a second batch is registered behind a nonprofit. Reported on Harvard Mathematics pages and in 2026 coverage; no stable institutional link verified at writing — the precise figures are 存疑 pending primary records.
- **存疑 — secondary reports:** Tsimerman's reported fatalism and the Cheng–Liu–Gao double-discovery experiment are cited *as reported in* arXiv:2608.02859 and press coverage; not verified at a single primary source.
- **一手 — in-repo cross-check:** the disproof's formal entry <../famous_problems/erdos_unit_distance.md> and its proof narrative <../proof_narratives/erdos_unit_distance.md> state the same results with their own sources.
- **interpretive — Saussure (signifier/signified) and Kant (synthetic a priori):** standard textbook accounts of *Course in General Linguistics* (1916) and the *Critique of Pure Reason* (1781/1787) — the chapter reads them as common intellectual property, not as claims in dispute.
<!-- zh -->
## 来源与考证

信度分级按家规：一手 · 权威版本 · 学界共识·解读（须标注）· 存疑（有争议）。有稳定链接者给出；仅存于二手报道者，注明该报道。

- **一手 — Erdős 反例（机器生成）：** OpenAI（2026-05-20）《An OpenAI model has disproved a central conjecture in discrete geometry》。<https://openai.com/index/model-disproves-discrete-geometry-conjecture/>
- **一手 — 人类核验论文：** Alon, N., Bloom, T. F., Gowers, W. T., Litt, D., Sawin, W., Shankar, A., Tsimerman, J., Wang, V., Wood, M. M.（2026）《Remarks on the disproof of the unit distance conjecture》。arXiv:2605.20695。<https://arxiv.org/abs/2605.20695>
- **一手 — 指数精化：** Sawin, W.（2026）《An explicit lower bound for the unit distance problem》。arXiv:2605.20579。<https://arxiv.org/abs/2605.20579>
- **一手 — 既有上界：** Spencer, J., Szemerédi, E., Trotter, W. T.（1984）《Unit distances in the Euclidean plane》，*Graph Theory and Combinatorics*（Cambridge），293–303。（无稳定链接，按家规给全书目。）
- **一手 — AlphaProof / AlphaGeometry 2 于 IMO 2024：** Google DeepMind（2024）《AI achieves silver-medal standard solving International Mathematical Olympiad problems》，deepmind.google 博客。（机构页；评分独立归功于 T. Gowers 与 J. Myers。）
- **一手 — FrontierMath 基准及 v2 修正：** Epoch AI（2024）《FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI》。arXiv:2411.04872。<https://arxiv.org/abs/2411.04872>；v2 发布说明（2026-06-12，修复 42% 题目的错误）：<https://epoch.ai/benchmarks/frontiermath-tier-4-v1>
- **权威版本 — o3/FrontierMath 口径之争：** Meyer, D.（2025-01-21）《'Manipulative and disgraceful': OpenAI's critics seize on math benchmarking scandal》，*Fortune*。<https://fortune.com/2025/01/21/eye-on-ai-openai-o3-math-benchmark-frontiermath-epoch-altman-trump-biden>（评述性新闻——已标注；"75.7% 来自'精选子集'，Epoch 未参与评测"是批评方共识，非定论。）
- **一手 — 内置 Lean 的开放问题基准：** Adamczewski, T., Bloom, T. F.（2026）《FrontierMath Erdős》，Epoch AI。<https://epoch.ai/files/frontiermath-erdos.pdf>
- **一手 — 陶哲轩论 AI 与数学：** Tao, T.（2026）《Mathematics in the age of AI》。arXiv:2608.16753。<https://arxiv.org/abs/2608.16753>（ICM 2026 演讲文章。）
- **一手 — 彻底抵制论：** Weinreich, M.（2026）《The crisis of AI-generated mathematics》。arXiv:2608.02859。<https://arxiv.org/abs/2608.02859>
- **一手 — 莱顿宣言：**「Leiden Declaration on Artificial Intelligence and Mathematics」（2026-06-02），十六位研究者 / 十五所大学。DOI 10.5281/zenodo.20302944。<https://leidendeclaration.ai/> · IMU 背书通告：<https://www.mathunion.org/fileadmin/documents/2026-06/IMU_AO_CL_8_2026.pdf> · 《自然》社论（2026-06-18）：<https://www.nature.com/articles/d41586-026-01881-2> · 报道：莱顿大学新闻（2026-06-02）。<https://www.universiteitleiden.nl/en/news/2026/06/leiden-declaration-warns-ai-is-challenging-the-core-values-of-mathematics>
- **学界共识·解读 — 哈里斯：** Harris, M.（2026）《Knowledge Collapse》，*Boston Review* 夏季刊。<https://www.bostonreview.net/articles/knowledge-collapse/>（论说文；"象棋/围棋/数学"三段论系引自此文——解读性。）
- **权威版本 — 温和有据的观点：** Schneier, B., Rafi, K.（2026-08-25）《No, AI Doesn't Mean the End of Mathematics—at Least Not Yet》，*The Guardian*，转自 <https://www.schneier.com/essays/archives/2026/08/no-ai-doesnt-mean-the-end-of-mathematics-at-least-not-yet.html>（观点/评论——已标注。）
- **存疑 — First Proof（哈佛）：** 十个未发表引理设擂（Lauren Williams 及其合作者）；AI 合计解出 ≥6/10；第二批已在非营利机构名下备案。见哈佛数学系页面及 2026 年报道；成稿时未核到稳定的机构主链接——具体数字按存疑处理。
- **存疑 — 二手报道：** Tsimerman 的末日言论与 Cheng–Liu–Gao"双重发现"实验，均系转引自 arXiv:2608.02859 及媒体报道，未核到单一一手源。
- **一手 — 本仓内部对表：** 反例的形式化条目 <../famous_problems/erdos_unit_distance.md> 与证明叙事 <../proof_narratives/erdos_unit_distance.md>，以各自来源陈述同一结果。
- **解读 — 索绪尔（能指/所指）与康德（先天综合）：** 依《普通语言学教程》（1916）与《纯粹理性批判》（1781/1787）的标准教材表述——本章视之为公共智识财产，非争议主张。
<!-- L5-end -->