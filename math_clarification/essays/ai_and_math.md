# 数学的危机，还是数学家的危机？——AI 时代关于数学的七问 / A Crisis of Mathematics — or of the Mathematicians? Seven Questions in the Age of AI

<!-- L1 -->
<!-- en -->
## Contents — Seven Questions, One Essay

Each chapter asks one question, and answers it in a sentence you can carry away. The answers stack: each later chapter stands on the ones before it.

1. **先前的事物与它们的核验 / The things done before** — what the machines actually accomplished in these years, and how it was certified. The scandal-free rungs are the ones a machine itself graded; the scandals live one floor up, where a human community must judge meaning.
2. **诸声 / The voices** — five voices in one room, agreed about the results, quarrelsome about the worth of the work itself; a syllogism runs behind all five, and its minor premise is the dishonest part.
3. **数学是一种语言 / Mathematics is a language** — signifier and signified; exactness is a property of the drawing, not of the drawn; verification certifies the grammar, never the object.
4. **数学家是谁 / Who, then, are the mathematicians?** — a ladder, not a kind of person; untie the knot and the job description appears, and it was never "be brilliant."
5. **形式化之后的分工 / The division of labor after formalization** — machines propose, construct, verify, check; humans choose the goal, judge importance, digest, hold the community's standards. Every dialect of exact speech is mathematics, and the machine is reading them all.
6. **开创性问题之争 / The dispute about groundbreaking problems** — a breakthrough moves the border, not the frontier; the machine has broken walls inside given languages, and so has almost every human giant. Ramanujan's unposed questions.
7. **相融而不言其名 / Containment, without the vocabulary** — in plain words: nothing stands alone; the tool is part of the mountain; mathematics is for the human who wants it true.

A note on sources follows the seventh chapter.
<!-- zh -->
## 目录 · 核心要点

七问，一条主线。每一章问一个问题，并给出一句可以带走的话；答案彼此叠加，后一章踏着前一章。

1. **先前的事物与它们的核验** —— 这些年里机器究竟做成了什么，又是怎么被认证的。从不出事的那几级楼梯，是机器自己当判官的那些；丑闻都住在上一步，那里需要人类共同体去判断意义。
2. **诸声** —— 一个房间五派共立，对成果并无分歧，争的是劳作本身的价值；他们身后有一段三段论，小前提便是那不老实的一处。
3. **数学是一种语言** —— 能指与所指；精确属于图画，不属于被画之物；核验认证的是语法，从来不是对象本身。
4. **数学家是谁** —— 一架梯子，而非一种人；解开了结，职位描述便现形，而它从来不是「要聪明」。
5. **形式化之后的分工** —— 机器提案、构造、核验、检查；人类选择目标、判别重要、消化、守住共同体的标准。精确言说的每一门方言都是数学，而机器此刻正在把它们全部读着。
6. **开创性问题之争** —— 突破移动的是边界，不是前线；机器在给定的语言里击破过墙，而几乎每一位人类巨人也只是如此。还有拉马努金那些未经规训的问题。
7. **相融而不言其名** —— 用平实到人人都懂的话说：没有什么是独自成立的；工具是山的一部分；数学为那个愿它成真的人而在。

第七章之后，附一篇来源与考证。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
For thirty years the story has been told as a siege. Deep Blue outpaced Kasparov in 1997; AlphaGo crossed the summit of board games in 2016; from 2024 the machines reached olympiad mathematics, and in 2026 an eighty-year-old conjecture came open like a door — in that same September a Millennium problem was pronounced "apparently" settled and its authorship fought over in public. Each time the fortress was declared the last true fortress of the human mind; each time the wall was climbed. This is not a book for the victory lap or the funeral dirge. It puts, instead, two quieter questions: what exactly has been achieved, and whether the crisis everyone keeps naming has been named correctly. The title is the argument in miniature. Whether mathematics is in crisis is not at all clear; that mathematicians are in crisis has become very clear indeed.
<!-- zh -->
三十年来，这个故事被讲成一场围城。1997年深蓝越过卡斯帕罗夫，赢下国际象棋；2016年AlphaGo翻过世界棋类之巅；自2024年，机器抵达奥林匹克数学；2026年，一道静立八十年的猜想应声而开——同一年九月，一道千禧年问题被宣布「貌似」已解决，其署名在公众面前被争夺。每一次，那座堡垒都被宣称为人类心智最后的真堡垒；每一次，墙都被人翻了过去。本文不为庆功鼓掌，也不为时代送终。它只问一对更安静的问题：究竟成就了什么；人人都在命名的那个危机，是不是叫错了名字。题目就是论点的缩影：数学是否在危机之中，全然不清楚；数学家是否在危机之中，已清楚得不能再清楚。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第一章 · 先前的事物与它们的核验：机器做成了什么，核验得如何？ / The Things Done Before, and How Well They Were Proved

The chessboard and the Go board belong to this chapter because they set the atmosphere. They were clean victories over *closed* games — games with a fully written rulebook, no outside reference, a referee able to decide every position. A century of game theory had already shown that such games are search-problems in disguise; what AlphaGo added was the proof that the search could be made fast enough to beat human pattern-recognition on its own terrain. Mathematics is not, at first glance, such a game — and that discrepancy, more than any single result, is what this essay is trying to hold still. Does the arc from chess to Go to mathematics run straight, or does it bend exactly where the rules run out?

### Five questions, and a staircase

Put five questions to the period's loudest mathematics results — was the claim honestly stated, can anyone reproduce it, did independent experts certify it, was failure disclosed as freely as success, and did the machine *find* in the literature an answer that was already there, or *make* one that had not existed — and the results form a staircase rather than a row.

### The cleanest case on record

At the 2024 International Mathematical Olympiad, Google DeepMind's AlphaProof and AlphaGeometry 2 solved four of six problems at silver-medal level, including the hardest problem of the year, which only five human contestants had cracked. The scoring belonged to two academics, Timothy Gowers and Joseph Myers; the machine's own solutions ran through a formal checker, Lean. This is the cleanest case on record: a public contest, independent judges, machine-checkable output. It was mathematics done the way its own doctrine longs to do it. The open question was whether the doctrine would survive contact with the other results.

### The medal changes color

The next summer the medal changed color, and with it the meaning of the frame. At IMO 2025 two systems — the advanced "Deep Think" generation of Google's Gemini and a model from OpenAI — both reported gold-standard scores, 35 of 42, five of six problems. Then the two laboratories answered the same verification question differently. DeepMind put its outcome before the IMO's official coordinators, graded under the same rules as the students'; OpenAI had its work read by three former olympiad medalists of its own choosing, and announced the score during the closing ceremony, before the next working day. A "gentlemen's agreement" — that laboratories would wait for independent grading and for the students' moment — was invoked on one side and, pointedly, not observed on the other. On the same problem Google's proof was judged readable by one referee while OpenAI's was barely readable by another, and former olympians kept noticing that machine proofs were, correct or not, always suspiciously fluent. Even the route split the laboratories: OpenAI deliberately skipped Lean, betting that a natural-language proof carries across to more domains, trading machine-checkability for portability.

### How a number is framed

The OpenAI model announced in December 2024 looks from a distance like the same achievement, and from close up like something else. o3 took 25.2% on Epoch AI's FrontierMath, a private benchmark of hundreds of hard problems built by more than sixty mathematicians; a second, higher figure — reported by OpenAI against a "chosen" subset of the problems — then became the headline, and the builders pushed back. Epoch AI stated plainly that it had not run OpenAI's evaluation. How a number is framed, it turns out, is part of the result. The scandal that followed — *Fortune*'s headline is politely called "manipulative and disgraceful" — had a buried coda that matters more than the feud: when Epoch issued a corrected benchmark v2 in June 2026, the revision fixed errors in **42 percent of the original problems**. The benchmark was partly wrong; the model was partly framed; only a public, self-correcting institution could reveal either. That single fact makes the whole feud worth replaying.

### The case that changed the mood

Then came the case that changed the mood. On May 20, 2026, OpenAI announced that one of its models had disproved Erdős's unit-distance conjecture — a landmark open problem since 1946. Nine mathematicians, among them the Fields medalist Timothy Gowers, wrote the verification paper that digested the machine's construction into a proof a human could teach; Will Sawin sharpened the exponent to $\delta = 0.014$. The bounds now read $n^{1.014} \leq u(n) \leq n^{4/3}$, and the gap is wider, not narrower, than it has ever been. Nothing about the world's ability to float on its own foundations failed here; the profession's machinery worked as designed — proposed by a machine, judged by specialists, sharpened by a community. This is the case that made "collaboration" sound like a description instead of a slogan. These pages keep their own record of the result and its proof narrative.

### The bottleneck is checking, not solving

Harvard's "First Proof" experiment ran on a different axis, and produced the more uncomfortable lesson. Ten unpublished research lemmas, prepared by Lauren Williams and her co-authors, were offered as a challenge; the assembled AIs solved at least six of ten. The news was not that they ran, but that *the human reviewers then struggled to verify the machine's proofs* — the bottleneck was not solving but checking, and checking is the profession's oldest, least-paid, most essential act. A second batch has since been registered behind a nonprofit foundation.

### The silent rung, graded by a machine

A result that caused no scandal at all belongs on the staircase too, because its silence is the tell. Google DeepMind's AlphaEvolve found a new algorithm that multiplies 4×4 complex matrices in 48 scalar multiplications, shaving one off the 49 of Strassen's 1969 method after fifty-six years; fed some fifty open problems in analysis, geometry, combinatorics, and number theory, it re-derived roughly seventy percent of the known optima and genuinely advanced about a fifth of the rest, improving an upper bound for the kissing number in dimension eleven. Nobody quarrelled over any of it, precisely because the grader was a machine: how many multiplications an algorithm uses leaves no room for spin. The scandals live one floor up, where a human community must judge meaning — and on the pure machine-checkable strata, on the evidence, no scandal has yet been produced.

### The loop closes, with a machine for a judge

The newest standard, announced in September 2026, closes the loop in a way that would have been unimaginable a decade ago. Epoch AI's "FrontierMath Erdős" takes sixty-eight of Erdős's still-open problems, states each one in the Lean proof assistant, and gives every model the same \$300 budget to prove or disprove it on its own. Best score: GPT-6 Astra at 3%. Everyone else: zero. The grader is a machine, so there is no framing to spin and no subset to choose. The Bad Old Days of the benchmark wars are, for one slender slice of mathematics, over.

### And then it reopened, on the top rung

And then, just as the loop was closing, it reopened. In September 2026 OpenAI announced that an internal system had produced a finite-time singularity construction for the three-dimensional Navier–Stokes equations — a Millennium Prize problem — complete with a manuscript and a Lean formalization: roughly ten thousand cooperating agents, some 130 billion output tokens, an effort of days, a construction powered by a smooth external *forcing* term. Three things are separately true of the episode, and keeping them apart is the whole lesson. First, within its formal statement the argument may be valid — reports say Lean checked it. Second, that statement falls inside an admissible branch of the Clay formulation, so the prize's own text may already count it as a settlement. Third, mathematicians still regard the unforced blow-up — the question the field actually cares about — as open, and *Scientific American* reports a new argument that the OpenAI method cannot be extended to it. The Clay Institute's own wording climbs only to "apparently settled," while its slow machinery — publication in a qualifying venue, two years in the literature, general acceptance by the global community — remains in force, and the official page still pins the problem as active. The fight was never about whether the proof is true. It is about which sentence the proof is proof of, who wrote it first, and who has the authority to say so in public. That is the top rung of the staircase, and it is not a mathematical argument at all.

### Read the staircase honestly

Read the staircase honestly: AlphaProof's clean contest victory does not prove it is smarter than o3, only that its work could be certified cheaply; Erdős's disproof did not prove the machine had understood anything, only that its construction could be turned into an argument by nine of the world's careful readers. What collapses across these years is not the competence of the machines. What collapses is the industry's way of speaking — the difference between a score and a fact, an announcement and a proof. The mathematics is fine. The claim-making is not — and on the top rung the claim-making has stopped being a laboratory matter and become an institutional one.
<!-- zh -->
## 第一章 · 先前的事物与它们的核验：机器做成了什么，核验得如何？

棋盘与围棋盘之所以属于这一章，是因为它们规定了气氛。那是对*封闭*游戏的干净胜利——规则书写完备、无可外援、判官能对任何局面作出裁决。一个世纪的博弈论早已表明此类游戏无非是伪装的搜索问题；AlphaGo 真正贡献的，是证明搜索可以快得足以在人类模式识别的领地上战胜人类。乍看之下，数学并不是这样的游戏——而这一落差，比任何单项结果都更是本文试图按住不放的东西。从象棋到围棋再到数学的这条弧线，是笔直延伸的，还是在规则用尽之处恰好拐了弯？

### 五个问题，一座台阶

把同样的五个问题——表述是否诚实、能否复现、是否经独立专家认证、失败是否与成功一样被披露、机器究竟是从文献里*找到*了本就存在的答案，还是*造*出了此前不存在的答案——依次放到这些年最响亮的数学成果上，它们排不成一排，而砌成了一座台阶。

### 记录里最干净的一例

在 2024 年国际数学奥林匹克上，Google DeepMind 的 AlphaProof 与 AlphaGeometry 2 以银牌水平解出六题中的四题，其中包括当年最难、全场仅五名人类选手解出的那道题。评分归两位学者——Timothy Gowers 与 Joseph Myers；机器自身的解答通过了形式化检查器 Lean。这是记录里最干净的一例：公开竞赛、独立判官、可机器检查的输出。它是数学按自己教义最渴望的方式做成的一次。开放的问题在于，这条教义在其余成果的冲击下还能不能存活。

### 奖牌变了颜色

第二年夏天奖牌变了颜色，随之而变的还有那层框架的含义。在 2025 年 IMO 上，两套系统——谷歌 Gemini 的换代「Deep Think」与 OpenAI 的一个模型——都报出金牌水准：35/42，六题解五。接下来两家实验室对同一个核验问题给出了不同答案。DeepMind 把成果呈交 IMO 官方协调员，按与参赛学生完全相同的规则评阅；OpenAI 则请三位自己圈定的前奥赛奖牌得主读稿，并在闭幕式进行当中、下一个工作日到来之前就宣布了分数。一边有人援引「君子协定」——各实验室应等待独立核验成绩、让学生的荣光先行——另一边则毫不避讳地无视它。同一道题，谷歌版的证明被一位评审判为可读，OpenAI 版则近乎不可读；更有前奥赛选手反复注意到，机器证明无论对错，总是一副异常流畅的样子——这流畅本身就该被警惕。连路线都把两家劈开：OpenAI 特意不用 Lean，赌的是自然语言证明更能迁往别的领域，以机器可验证性换可迁移性。

### 一个数字的包装

2024 年 12 月公布的 OpenAI 模型，远看像同一成就，近看是另一回事。o3 在 Epoch AI 的 FrontierMath 上取得 25.2%——那是一个由六十余位数学家建造的私有题库，数百道硬题；随后，第二个更高的数字——OpenAI 在题库"经挑选"的子集上自报的成绩——成了头条，建题者随即回击。Epoch AI 明确声明：OpenAI 的评测并非他们所跑。原来一个数字怎么包装，本身就是结果的一部分。接踵而至的丑闻——*Fortune* 的标题客气地叫做"操纵、可耻"——底下埋着一则比争吵更重要的尾声：2026 年 6 月 Epoch 发布修正版 v2，修复了原始题库**百分之四十二的题目的错误**。题库部分出错，模型部分被包装，而只有公开、自我纠错的机构才能让二者同时浮出水面。单凭这一件事实，整场争吵就值得重放一遍。

### 改变气氛的那一桩

接着是改变气氛的那一桩。2026 年 5 月 20 日，OpenAI 宣布其模型推翻了 Erdős 单位距离猜想——一个自 1946 年以来的里程碑式开放问题。九位数学家（其中包括菲尔兹奖得主 Gowers）写下核验论文，把机器的构造消化成人类能教的证明；Will Sawin 把指数精化为 $\delta = 0.014$。现在的界是 $n^{1.014} \leq u(n) \leq n^{4/3}$，而空白比过去任何时候都更宽。世界赖以漂浮的自洽基础没有任何一处在这里失灵；职业的机器按设计运转——由机器提出、由专家裁决、由共同体精化。正是这一桩，让"合作"听起来像描述而非口号。本篇为这一结果及其证明叙事各留一份记录。

### 瓶颈在核验，不在解题

哈佛的 "First Proof" 实验跑在另一条轴上，给出了更不舒服的一课。Lauren Williams 与她的合作者备下十个未发表的研究引理设擂；众 AI 合计解出至少十个中的六个。新闻不是它们解出来了，而是*人类审稿人随后很难核验机器证明*——瓶颈不在解题，而在核验，而核验是这个职业最古老、最廉价、也最要命的动作。第二批引理此后已在某非营利基金会名下备案。

### 机器当判官的那安静的一级

台阶上还有一级从未惹起丑闻的成果，它的安静本身就是线索。Google DeepMind 的 AlphaEvolve 找到一套新的 4×4 复矩阵乘法算法，只要 48 次标量乘法，把斯特拉森 1969 年方法保持了五十六年的 49 次纪录削掉一次；把分析、几何、组合、数论上的五十余个开放问题喂给它，约七成被它重新推演到已知最优，另有约两成真的取得进展——其中包括把十一维「接吻数」问题的上界改善了一点。没有人为此争执，恰恰因为阅卷的是机器：一个算法用几次乘法，没有任何口径可包装。丑闻都住在上一步台阶，那里需要一个人类共同体去判断意义——而纯粹的机器可核验层，按现有证据，从不产出丑闻。

### 循环合拢，以机器为判官

最新标准在 2026 年 9 月登场，以一种十年前的想象力所不及的方式把循环闭上。Epoch AI 的 "FrontierMath Erdős" 挑出 68 道至今未解的 Erdős 问题，把每一道在 Lean 证明助手中写成陈述，并给每个模型以相同的 \$300 预算令其独立证明或证伪。最高分：GPT-6 Astra 的 3%。其余全部为零。阅卷者是机器，于是没有口径可包装，没有子集可挑选。基准战争那段坏日子，在数学的这细细一格上，宣告结束。

### 而它又在最高一级重新打开

而就在循环行将闭合之际，它重新打开了。2026 年 9 月，OpenAI 宣布其内部系统为三维 Navier–Stokes 方程——一道千禧年大奖问题——构造出有限时间奇点的证明，附上手稿与一份 Lean 形式化：约一万个协同智能体、约 1300 亿输出词元、持续数日的工作、由光滑外部*强迫项*驱动的构造。关于这一事件，有三件事可以分别成立，把它们分毫不混便是全部功课。其一，就它的形式陈述而言，论证可能成立——据报已通过 Lean 检查。其二，该陈述落在 Clay 公式化的一个可容许分支之内，故奖项文本本身或许已经可以把它算作一次解决。其三，数学家依然视无强迫项的爆破——那个领域真正在乎的问题——为未解，《科学美国人》并报道了一项新论证，称 OpenAI 的方法无法推广到无强迫项情形。克雷研究所自己的措辞只爬到「貌似已解决」，而其缓慢的机器——在合格刊物发表、文献滞留两年、为全球数学共同体普遍接受——依然在运转，官网页上仍把问题标为进行中。这场争执从来不是证明是否为真。它是那句证明究竟是哪个句子的证明、谁先写下它、以及谁有权当众宣布它。这是台阶的最高一级，而它根本不是数学论证。

### 诚实读这座台阶

诚实读这座台阶：AlphaProof 的干净竞赛胜利，证明不了它比 o3 更聪明，只证明它的活能被廉价地认证；Erdős 的反例，证明不了机器理解了任何东西，只证明它的构造能被九位最谨慎的读者改写为论证。这些年里崩塌的不是机器的本事。崩塌的是业界说话的方式——分数与事实之间、公告与证明之间的那道分别。数学安然无恙。说话的方式病了——而到了最高一级台阶，说话的方式已不再只是实验室的事，成了建制的事。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第二章 · 诸声：争的不是机器，是劳作的价值 / The Voices in the Room

Where one community should stand, five stand, and their quarrel is not about machinery. It is about what mathematics is *for*: the worth of the calling, the weight of a single person's labor, whether a thing done by a machine still counts as the thing being done.

### The integrationists

The integrationists read chess, Go, and mathematics as one long game, and the machine as its natural next player. Terence Tao's lecture essay for the 2026 International Congress of Mathematicians, "Mathematics in the age of AI," argues from what he calls a Working Hypothesis — a strong form of the "AI Capability Conjecture": that AI tools will soon carry out a reasonable share of research-level mathematics at reasonable quality and cost. If the bet holds, he warns, the bottleneck shifts from talent to *verification* — proofs arriving faster than they can be checked, checked proofs faster than they can be read, readable proofs faster than referees can be found. Kevin Buzzard carries the same confidence into code, running a long campaign to formalize Fermat's Last Theorem in Lean so that "checked by machine" becomes an ordinary sentence in working mathematics.

### The institutionalists

The institutionalists answer with rules rather than visions. The Leiden Declaration of June 2, 2026 — drafted by sixteen researchers from fifteen universities, endorsed by the International Mathematical Union, signed in its opening months by more than four thousand individual mathematicians, amplified by a *Nature* editorial — enumerates five threats: arguments that are plausible but unreliable; authorship dissolving into black boxes; dependence on proprietary tools dividing the profession into haves and have-nots; press offices overhyping raw results; and the slow thinning of what "understanding" still means. Peter Scholze, among its featured endorsers, drew the line that matters: the goal of mathematical research is *human* understanding, and mathematics can thrive only inside a community of human mathematicians. Notice, too, what the declaration does not ask for. No ban. Only disclosure, standards, authorship — a refusal to let outsiders' hype decide what counts as true.

### The fatalists

The fatalists run the trajectory's logic to its end. Jacob Tsimerman is reported to hold the dark version as a creed: AI will destroy the field, and perhaps the world, and mathematicians will have no choice but to use it all the same. The position has an internal coherence worth respecting. If the tools improve without limit and refusing them is professional suicide, then progress is ruin, and the only open question is whether the field goes down with style.

### The resisters

The resisters make the case for the other side with genuine force. Max Weinreich's essay "The crisis of AI-generated mathematics" argues for total opposition: AI is an anti-intellectual technology; it short-circuits understanding, devalues knowledge, and will tempt the best to abstain merely to prove their worth to one another. Patrick Massot has spoken of mathematics being "bombed" by AI. Inside the fierceness sits a quiet truth: if checking a flood of machine proofs is thankless and boring, then the prestige economy — which pays for *discovery*, not *checking* — now punishes exactly the labor that keeps mathematics honest. The resisters are right about the incentive; they may be wrong that the incentive cannot change.

### The moderates

The moderates, least quoted and perhaps most reliable, draw the line the later chapters will test. Bruce Schneier and Kasra Rafi write that today's AIs are strong at searching and recombining existing ideas, weak at building deep new theory, and, for now, nowhere near a practiced researcher. Michael Harris, in *Knowledge Collapse* and in the *Boston Review*, reminds the profession that mathematics has been, in his phrase, one of the last unalienated labors — a free creative art — and asks, quietly, what of that dignity survives automation.

### A voice outside the camps

One more voice belongs in the room, and it belongs to none of the five camps. Tristan Buckmaster is the mathematician who, with Levent Alpöge, proved the forced Euler blow-up in August 2026 and found himself inside the September machinery. He reports that OpenAI, proposing a joint announcement, offered to publish the forced Navier–Stokes result under his name alone — setting aside his co-author for reasons of competition — and answered his threat to go public with something close to a career warning; OpenAI denies the account flatly. Whatever the merits, the type is new: a working researcher whose results moved at corporate speed, whose authorship became a bargaining chip. He holds no position in the debate about AI and mathematics; he is the debate. Two readings of the story stand available at once, and the discipline — rarely practiced — is to hold both: an accusation may be true even though it serves the accuser, a triumph may be real even though it serves the company. Motive and content are not the same kind of evidence; the first tells you who stands to gain, the second what happened.

### The syllogism behind the five voices

Watch the syllogism running behind all five voices, the doomer's engine: *Go is a game; mathematics is also a game; therefore AI will solve mathematics.* Harris quotes it in *Knowledge Collapse* because it is the whole dispute in three lines. The minor premise — mathematics is a game — is doing all the work, and dishonestly: it holds only for the formalized slice of mathematics, a fact everyone in the room knows. None of the five camps doubts the *results*. The disproof stands; the Lean towers grow. What they dispute is the value of the activity itself — and there is the tell. A crisis of mathematics would show up in the content: theorems collapsing, truths decaying. Nothing is collapsing. What is being renegotiated is employment, authority, prestige, the meaning of a working day, the dignity of the judge. The crisis, if there is one, is a crisis of the mathematicians. Tao himself has named it — in the ICM lecture this essay keeps returning to — a stress-test of a largely implicit framework of mathematical values and practices, social rather than foundational: the shape of the last century's foundations crisis, except that this time what must be made explicit is the working arrangement, not the axioms.
<!-- zh -->
## 第二章 · 诸声：争的不是机器，是劳作的价值

本应是一个共同体的地方，如今立着五派，争执的却不是机器。他们争的是数学*做什么用*：这门行当值几钱，一个人的劳作重几两，一件事由机器去做，还算不算数。

### 整合派

整合派把象棋、围棋、数学读成一盘长棋，视机器为它天然的下一手。陶哲轩为 2026 年国际数学家大会撰写的演讲《Mathematics in the age of AI》以一个"工作假说"立论，实为"AI 能力猜想"的强形式：AI 工具很快将以合理的质量与成本，承担相当一部分科研级数学。赌注若成，他警告说，瓶颈便从天赋转往*核验*——证明来得比人检查得还快，检查过的证明来得比人读得还快，可读的证明来得比找到审稿人还快。Kevin Buzzard 把同样的信心落实在代码里，领衔一场长期的战役，要在 Lean 中形式化费马大定理，好让"机器已核验"变成数学日常里一句平平常常的话。

### 建制派

建制派以规范作答，而不是以愿景。《莱顿宣言》由十六位来自十五所大学的研究者起草，于 2026 年 6 月 2 日发布，获国际数学联盟背书，最早几个月里便有四千多位数学家个人签署，还得到《自然》社论的呼应。它点数出五重威胁：貌似可信却不可靠的机器论证；作者权化入黑箱；对专有工具的依赖把职业劈成有与无；新闻办公室把生结果炒作成定论；以及"理解"一词的含义在慢慢变薄。列在显著推荐人中的 Peter Scholze 划出那条要紧的界线：数学研究的目标是*人的*理解，数学只能在人类数学家的共同体中兴旺。还要留神宣言*没有*要求的东西。没有禁令。只有披露、规范、作者权——拒绝让外行的腔调决定什么才算真。

### 末日派

末日派把轨迹的逻辑推到尽头。据传 Jacob Tsimerman 以信条持有那暗色版本：AI 会毁掉这个领域，也许毁掉世界，而数学家无论多么不情愿，都别无选择，只能用。这套立场有一种值得敬重的自洽：若工具永无止境地精进，而拒绝使用等于职业自杀，那么进步就是末日，唯一还开放的问题，只剩下这个领域以何种风度倒下。

### 抵制派

抵制派为另一侧拿出了真正的力量。Max Weinreich 的《The crisis of AI-generated mathematics》主张彻底抵制：AI 是反智的技术，它短路理解、贬低知识，还会诱使最好的数学家彼此罢手，只为证明自己不屑与机器为伍。Patrick Massot 说数学正被 AI"轰炸"。凶猛底下藏着一句安静的实话：若核验海量机器证明既无回报又无聊，那么声望经济——它付钱给*发现*，不付钱给*核验*——如今惩罚的，恰恰是让数学保持诚实的那桩劳动。抵制派对激励的洞察没有错；"这激励改不了"的悲观，倒未必对。

### 温和派

温和派被引证得最少，也许最可靠，他们划出的那条线，正是本文后几章要检验的。Bruce Schneier 与 Kasra Rafi 写道：今日的 AI 强于搜索、重组既有的观念，弱于建造深刻而持久的新理论；目下还远不能比肩一位有经验的研究型数学家。Michael Harris 在《Knowledge Collapse》与《波士顿评论》里提醒职业界：按他自己的说法，数学向来是"所剩无几的未异化劳动"之一——一种自由创造的艺术——然后安静地问一句：自动化之下，这份尊严还剩下什么。

### 五派之外的声音

房间里还坐着一种声音，它不属于五派中的任何一派。Tristan Buckmaster 于 2026 年 8 月与 Levent Alpöge 合力证明受迫欧拉方程爆破，随后被卷进九月那架机器；他声称，OpenAI 提议联合宣布时，曾提出把受迫 Navier–Stokes 的研究成果单独署在他名下，以竞争为由撇下他的合作者；他威胁要公开此事时，又收到了近似职业前程的暗示性警告。OpenAI 断然否认。无论孰是孰非，这是一个新的类型：一位普通研究者的成果以企业速度流动，署名成了筹码。他没有关于"AI 与数学"的"立场"；他就是这场争执。这桩事同时容得下两种读法，而两者并置这门功夫很少有人练：指控可以因为对控告者有利而依然为真，胜利可以因为对公司有利而依然实至名归。动机与内容不是同一种证据——前者告诉你谁有得可图，后者告诉你发生了什么。

### 五派身后的三段论

现在来看五派身后轰隆转动的三段论，末日派的引擎：*围棋是博弈；数学也是博弈；因此 AI 将解出数学。* 哈里斯在《Knowledge Collapse》里引用它，因为它就是整场争执的三行压缩。小前提——数学是博弈——扛着全部重量，而且扛得不老实：它只对数学被形式化的那一格成立，这一点房间里人人都知道。五派没有一派怀疑*成果是真的*。反例立得住；Lean 的高塔还在长高。他们争的是活动本身的价值。线索就在这里。数学的危机应当显形于内容——定理崩塌、真理朽坏。没有任何东西在崩塌。被重新谈判的，是就业、权威、声望、一个工作日的意义、判官的体面。如果说有危机，那是数学家的危机。陶本人在本文屡屡回到的那场 ICM 演讲里，把它称为对一套隐而未宣的数学价值与实践框架的考验——一场社会的考验，而非基础的考验；形状仍与上一个世纪那场基础危机相似，只是这一次必须被摆到明处的是运作的安排，而非公理。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第三章 · 数学是一种语言：精确，对谁而言？ / Mathematics Is a Language: Exact, for Whom?

Every crisis in this conversation turns on one confusion, nameable in three words: signifier and signified. Mathematics is a language — a system of signs, of 能指 — in which we draw, exactly, what we want to say; and a language is never the thing it speaks of. The map is not the territory; the score is not the music; the watermark of a proof is not the pattern it proves. When the machines arrived, much of the panic came from quietly forgetting this — treating the language as the object, as if formalizing the proof of a theorem touched the truth it states. It does not. The grammar can be flawless and the world unchanged. And if the clause "we draw, exactly, what we want to say" slipped past unnoticed, read it twice: it hides the question this chapter must answer — what the "exactly" means, and to whom.

### The arbitrary tie, the portable language

Saussure saw why the confusion is built into every language. No necessity ties a signifier to its signified: "tree," Baum, arbre carry the same weight in their languages, and nothing about the wood demands any of them. The tie is arbitrary; the *structure* the signs evoke is not. When mathematics says "group," the word is a tag for an arrangement of operations, and the arrangement does not care which tag we chose. That is why mathematics can be re-described as it is: the language is portable, the necessity it carries is not. Human mathematicians spend careers shuffling signifiers — number systems, definitions, categories — because the signified, the structure, is what survives the shuffle. Poincaré compressed the whole lesson into one sentence: mathematics is "the art of giving the same name to different things." The names survive; the necessity travels with the structure, not with the noun.

### The disproof as a change of language

Read the unit-distance disproof through this lens and it turns almost eerie. The machine found no new facts about dots on a plane; it swapped one signifier for a richer one. A geometry expressed for eighty years in Gaussian integers, whose symmetries are finite, came to be drawn in algebraic number fields, whose symmetries are inexhaustible. The signified stayed off-stage the whole time; what changed was the language of the drawing, and the answer simply became visible. Whoever controls the re-description controls the deepest work in mathematics — and the machine has just shown it can re-describe.

### The language works without certification

None of this makes mathematics arbitrary, and none of it makes it a first cause. It is not what the universe is *made of*; it is the most exact language yet found for relations that hold necessarily, whatever name we give them. Kant called such truths synthetic a priori — they add to knowledge, yet hold independently of experience. Formalism answered from the opposite shore: truth is consistency in a game of symbols. Gödel's incompleteness theorems pushed a wall through that game in 1931: any sufficiently strong consistent system states truths it can neither prove nor refute, and cannot certify its own consistency. Turing's halting problem drove in a second wall — some precisely posed questions admit no algorithm at all — and Cohen showed the axiomatic ground itself can be rebuilt in incompatible ways. Then something undramatic happened: mathematics went on working, on what Tao calls "naive" foundations, and prospered. A foundations crisis that once seemed fatal ended in resignation, and the field did not mind. The oldest lesson may be that the language works whether or not we can certify it.

### Exact for whom?

Consider then, honestly, the "exactly" in "we draw, exactly, what we want to say." Who feels a mathematical statement to be 分毫不差? The field's reflexive answer — "anyone who can read it" — already gives the game away. The exactness is felt by whoever has mastered the dialect; it is a property of the reader's relation to the code, not of the code's relation to the world. The puzzle is that this felt exactness is both genuine and empty: genuine, because within the calculus the claim is not trusted but *enforced* — the derivation either follows the rules or it does not; empty, because that enforcement is entirely internal. Proof assistants certify the exactness of the drawing, since they check every stroke against the grammar — and the grammar, not the object, is all they see. A proof that is formally certified may nonetheless be a proof of the wrong sentence: the Navier–Stokes construction this essay began with is, on the reports, exactly a proof — formally checked, apparently valid — and yet the community's question, the unforced blow-up, remains open. The formalization was faithful; the formalization could not be faithful *to anything beyond itself*. This is why completeness is the deeper problem beneath exactness. Within a chosen language a theorem is as complete as its axioms make it; Gödel's wall is precisely the theorem that no sufficiently strong language can be complete about everything it can state. But a second incompleteness, quieter, matters more here: the incompleteness of the *characterization* — the fact that any re-description captures some relations and discards others, so the signified when we call it "unit distances" is not identical with the signified when the machine calls it "algebraic integers." What felt complete in 1946 — "we have said exactly what we mean about the unit-distance problem" — was not complete; it was exact in the only sense the field had yet found. That difference runs through everything below: exactness is a property of the sign-system; completeness is a relation between the sign-system and the thing it points at — and no grammar has authority over that relation.

### The limits of checking

Two consequences follow for everything claimed in these years. First, verification — Lean checks, expert read-throughs — stays in the signifier: it certifies that the translation was faithful, that the signs were shuffled lawfully. It cannot certify that the signified was worth attending to. Lean's own documentation states the limit in one sentence: checking whether a theorem has a valid proof and determining what the theorem *means* are distinct tasks, and the kernel settles only the first. Second, the freedom to change the language is at once mathematics' deepest liberty and its most human act — no formal system decides which re-description deserves the next twenty years. That judgment, which language will let the truth show itself, is not theorem-shaped, and it is not yet machine-shaped.
<!-- zh -->
## 第三章 · 数学是一种语言：精确，对谁而言？

这场对话里的每个危机，最终都落回同一个混淆，三个字说清：能指与所指。数学是一种语言——一套符号、一层能指——我们用它把想说之物*分毫不差*地画下；而语言从不等于它所言说的东西。地图不是领土；乐谱不是音乐；证明的水印，不是它所证的范式。机器到来时，恐慌的一大部分，来自悄悄忘掉这件事：把语言当成了对象，好像把定理的证明形式化了，就等于触到了它所陈述的真理。并不是。语法可以完美无缺，世界纹丝不动。可那句「把想说之物分毫不差地画下」若没经审视便滑了过去，就该回头再看一眼——它藏着的，正是本章必须回答的问题：画得「分毫不差」，究竟*分毫不差*在何处，又*对谁而言*？

### 任意的联结，可搬运的语言

索绪尔明白这种混淆为何内建于一切语言。能指并不被必然性系于所指："树"、tree、arbre 在各语言里背着同一重量，而木头的任何脾性都不要求其中任一个。符号与对象的联结是任意的；符号所唤醒的*结构*却绝不是。数学说"群"时，它只是一个符号，代表某种运算的布局；布局并不在乎我们拣了哪个符号。正因如此，数学才得以被这样重新刻画：语言是可搬运的，它所负载的必然性不是。人类数学家以毕生来回倒腾能指——换数系、换定义、换范畴——因为所指，那结构，才是倒腾之后幸存下来的东西。彭加莱把整一课压进一句话：数学是"给不同的事物以同一名字的艺术"。名字幸存下来，而必然性随结构而行，不随名词而行。

### 反例就是一次换语言

以此透镜读单位距离反例，几乎骇人。机器并没有发现关于平面上点的什么新事实；它只是用一个更富饶的能指换下原来的一个。被表达了八十年的单位距离几何——用高斯整数的语言，其对称性有限——转而画进代数数域的语言，其对称性取之不竭。所指全程在后台；变的是问题被描绘所用的语言，答案因此变得可见。谁掌握重新刻画，谁就在做数学里最深的活——而机器刚刚证明，它会重新刻画。

### 语言不必先被认证才能用

这一切既不使数学变任意，也不使它成第一因。它不是宇宙*由之构成*的东西；它是有史以来对"必然成立的关系"最精确的言说语言，无论我们给它罩上什么名词。康德把这类真理叫先天综合判断——增长知识，却又独立于经验而成立。形式主义传统在对岸作答：真理即符号博弈的自洽。哥德尔 1931 年的不完备定理向这场博弈立起一堵墙：任何足够强的自洽体系，都陈述着它既不能证也不能否的真理，也无法认证自身的自洽。图灵的停机问题立起第二堵——有些界定清楚的问题，原则上不存在任何算法——科恩又证明，公理地基本身可以被重建为互不相容的样子。然后，一件毫无戏剧性的事发生了：数学只在陶所说的"朴素基础"上继续运转，并且兴旺。一度看似致命的基础危机，以认输收场，而领域并不在意。它最老的教训也许是：语言能不能用，并不需要先认证语言。

### 分毫不差，对谁而言？

那么，且诚实看看「画得分毫不差」的那个"分毫不差"。谁会觉得一段数学陈述分毫不差？这个领域脱口而出的答案是"凡是会读它的人"；这答案已经先泄了题。分毫不差的感觉属于那个掌握了方言的人。它是读者与代码之间关系的性质，不是代码与世界之间关系的性质。费解之处在于：这份感觉既真切，又空洞。真切，因为在演算内部，这个声称不是被*信任*，而是被*强制执行*：推导要么合规则，要么不合。空洞，因为那强制执行全然在系统之内。证明辅助程序认证的是画的精确，它把每一笔都照语法检查一遍；而语法，不是对象，是它唯一见到的东西。一份经过形式化认证的证明，仍可能是对*错误句子*的证明。本文开头的 Navier–Stokes 构造，按报告，确乎是"一份证明"，被形式化检查，据称有效；而共同体的那个问题，无强迫项的爆破，依旧未解。形式化是忠实的；可形式化只能忠实于*它自身之外的存在*。这正是完整性比精确性更深的缘故。在一种被选定的语言内部，定理的完整程度与公理相当；哥德尔的墙，恰恰是说没有任何足够强的语言能对其一切陈述保持完备。但这里更要紧的，是第二重更安静的不可完备：*刻画*的不可完备。任何重新刻画都擒获一些关系、抛掷另一些；当我们叫它"单位距离"时的所指，与机器叫它"代数整数"时的所指，并不相同。1946 年觉得"关于单位距离问题，我们已把想说的说尽"，其实并不完整；它只是在那个时代所找到的、唯一的意义上精确。两义之别贯穿本章之后的一切：精确是符号系统的性质；完整是符号系统与它所指之物*之间*关系的性质，而任何语法对此关系都无权威。

### 核验的边界

对这些年的一切宣称，由此推出两条后果。其一，核验——Lean 检查、专家通读——停留在能指层面：它认证翻译是忠实的、符号的倒腾合乎法度。它认证不了所指是否值得关注。Lean 的官方文档用一句话说出这个限度：检查一个定理有没有有效证明，与断定这个定理*意味着什么*，是不同的任务，而内核只解决前者。其二，更换语言之自由，既是数学最深的自由，也是它最属人的动作——没有形式系统会决定哪一次重新刻画值得付出下一个二十年。那个判断，哪一种语言会让真理现身，不是定理的形状，也还不是机器的形状。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第四章 · 数学家是谁：一架梯子，而非一种人 / Who, Then, Are the Mathematicians? A Ladder, Not a Kind of Person

The word "mathematician" names a ladder, not a kind of person, and the public muddles the rungs on purpose, because each rung flatters. At the bottom stands the solver — the timed olympiad student, pattern-matching under the clock, the image that fronts every article about clever people. Above her, the researcher, proving things nobody has proved, most of it small, most of it by extension. Above that, the theory-builder, assembling results into an edifice — a Weil, a Grothendieck. At the top, the field-founder, who announces that the whole conversation should change: Descartes, Newton, Gauss. To mistake the first rung for the fourth — as the press and the hype cycle do constantly — is like concluding that because the fastest runner is athletic, she would make the best architect. The confusion costs real currency: attention.

### What the top does all day

What the top of the ladder does all day has changed within one generation: paper and ink, then verifying at a keyboard, then — since 2026 — deciding when to let a machine propose and when to demand a proof a human can carry. The prestige economy strains under the change. Joel David Hamkins has written of despairing at an ocean of slop overwhelming the journals; Daniel Litt warns of "pollution of the commons by AI-generated nonsense." The scarcity is not correctness; it is attention, and the attention-keepers are unpaid.

### Why "mathematician" became nearly the same word as "brilliant"

Why, outside the profession, has "mathematician" become nearly the same word as "brilliant"? Five forces, none of them about aptitude. *History* manufactured the cult of the solitary genius — Gauss, Erdős — a storyteller's invention that flattens decades of communal labor into a single flash. *Psychology* trains intuition and rigor as separate muscles and markets them as one gift; people fluent in both are rarer than the stereotype admits. *Gatekeeping* — the olympiad system, the ritual of formalization — decides early and cheaply whom the profession treats as promising; a filter built for speed and neatness, not depth. *Information asymmetry* hides the process: outsiders see the finished proof, inevitable and clean, never the two years of dead ends that made the residue look effortless. *Cognitive bias* does the rest — survivorship bias, only winners visible; halo effect, one brilliant theorem licensing everything adjacent. The psychology is measurable, not ornamental: meta-analyses spanning well over a hundred studies and close to a million participants find a real, reproducible drag of anxiety on mathematical performance. The same society now scandalized by a benchmark's cherry-picked subset has been running that exact inflation on human beings for three centuries; the machine merely returns the compliment. The cult's mirror face does at least as much quiet damage: the crowd concludes, without evidence, that whoever stumbles at mathematics lacks intelligence.

### The job description

Untie the knot and the job description appears, and it was never "be brilliant." It is: carry the community's standards, extend what nothing else has extended, and at the top — with one's whole judgment, skin in the game — decide what the community should work on next. These are categories of labor, not of grade. The tragedy of the moment is that this is precisely what the profession has stopped being able to say aloud. The panic comes from identifying mathematics with the score: if the machines score, what remains of the humans? The honest answer — everything that judges, teaches, and cares — sounds sentimental and is simply true.
<!-- zh -->
## 第四章 · 数学家是谁：一架梯子，而非一种人

"数学家"一词命名着一架梯子，而非一种人；公众故意把梯级搅浑，因为每一级都让人受用。底层站着解题者——计时赛场上的奥赛学生，在倒计时下做模式匹配——每一篇谈"聪明人"的文章都拿他做门面。其上，研究者，证明无人证过之物，多数很小，多数靠延伸。再上，理论建造者，把结果砌成一座建筑——一个 Weil，一个 Grothendieck。顶端，领域开创者，他宣布整场对话都该换——笛卡尔、牛顿、高斯。把第一级混作第四级——媒体与造神周期乐此不疲——好比因为跑得最快的短跑选手有运动天赋，就断定她是最佳建筑师。这混淆本身要花掉真正的通货：注意力。

### 顶端的人一天天做什么

梯子顶端的人一天天究竟在做什么，一代人之内就变了样：先是纸墨，再是键盘上的核验，然后——2026 年以来——是决定何时让机器提案、何时索要一份人带得走的证明。声望经济在这变化中承压。Joel David Hamkins 写他对着淹没了期刊系统的垃圾之海绝望；Daniel Litt 警告"AI 生成的垃圾污染公地"。稀缺的不是正确性，是注意力；而看护注意力的人，没有薪水。

### 为什么「数学家」几乎成了「才华横溢」的同义词

而在职业之外，"数学家"为什么几乎成了"才华横溢"的同义词？五股力量，无一关乎天赋。*历史*制造了孤胆天才的崇拜——高斯、埃尔德什——那是小说家的发明，把数十年的共同体劳作压扁成一道闪光。*心理*把直觉与严格各自练成两块肌肉，再当作一样天赋出卖；两者皆流利者，远比刻板印象以为的稀少。*守门*——奥赛体系、形式化的仪式——很早就地界定了职业将把谁当作可造之材；而这过滤器为速度与整洁而建，不是为深度。*信息不对称*藏起全部过程：外人只见成品证明——利落、无可逃——永不见那两年死胡同，正是死胡同让残渣显得毫不费力。*认知偏差*收走剩下的：幸存者偏差，只有赢家可见；光环效应，一条漂亮定理给一切邻近之物盖章。这心理可测，并非装饰：横跨一百余项研究、近百万被试的元分析，检出真实而可复现的"焦虑拖低数学表现"的印记。如今为基准精选子集而震惊的那个社会，三百年来对人类跑着同一场通货膨胀；机器不过是以其人之道、还施彼身。这崇拜还有一面镜子，造成的安静伤害至少同样大：人群不假证据便断定，在此道上一碰即退的人，缺乏智力。

### 职位描述

解开这结，职位描述便现形，而它从来不是"要聪明"。它是：承托共同体的标准；延伸无人能延伸之处；并在最高处，以全部的判断与身家性命，决定共同体接下来该做什么。这些是劳动的分类，不是分数的等级。此刻的悲剧在于，这恰是这个职业再也说不出口的东西。恐慌源于把数学等同于分数：如果机器会得分，人类还剩什么？诚实的答案——一切判断、教授与在乎的东西——听来煽情，却只是真话。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第五章 · 形式化之后的分工：机器做什么，人做什么 / The Division of Labor After Formalization: Who Does What

Set the relations down plainly, since everything else in this chapter hangs on them: *quantifiable* ⊂ *computable* ⊂ *formalizable* ⊂ *mathematics*. Logic is special — the skeleton of every formal system and, at the same time, one of mathematics' own objects, studied mathematically by proof theory. The point is the nesting, not the labels. Everything a machine has "solved" lives inside the formalizable stratum. The Erdős disproof lives there — that is why it could be certified — and so did every move of chess and of Go. The games trajectory and the mathematics trajectory overlap on this stratum, and no further.

### What carries across, and what does not

Here, then, is the honest measure of the run from chess to Go to mathematics. What carries across is the *rule-governed core*: a domain whose correctness can be checked without appeal to context. Chess is fully checked; Go nearly; the formalizable slice of mathematics fully, in principle. That is why the same search technique keeps advancing from one fortress to the next. What does not carry across is everything around that core — the choice of which game to study, the judgment of which move is *important* rather than merely legal, the decision that this conjecture and not that one deserves the next decade. No referee can certify importance, because importance is not a position on a board. The trajectory runs straight exactly until the rules run out; then it bends. Bent is not broken. And the layer where it bends is untouched by any reward signal: nothing in a search space says which conjecture deserves the next decade; reinforcement can grade a proof but cannot manufacture the asking.

### Indifference to the obvious

In the formalizable stratum the machine's advantage is no longer speed. It is indifference to the obvious — the willingness to try a language a human expert has long since learned to call irrelevant. Humans knew the right picture of the unit-distance problem; famously, that picture was the cage. The machine, unbothered, tried another number system and walked out. On bounded, checkable, searchable tasks, larger-than-human search now beats individual human search, full stop. First Proof adds the unsettling corollary: the machine can outrun not only the solver but the *verifier*, producing arguments before human referees can judge them.

### The division writes itself

The division of labor then writes itself, which is why the panic is aimed so badly. Machines propose, construct, formalize, check. Humans choose the goal, choose the language, judge importance, hold the community's standards, and — in Tao's word — *digest*: turn verified results into something a mathematician can carry in her head. Every bottleneck both camps predict — proofs outrunning verification, verification outrunning write-ups, write-ups outrunning referees — makes the human half scarcer, not less needed. Attention is finite; the machine manufactures supply, not demand. The person who converts machine output into understanding is not being automated away; she is being promoted. Concretely: future mathematicians will sort into formalization architects, auditors of machine proofs, and interpreters who translate machine output back into the community's ordinary language — three jobs this decade keeps producing.

### Five gates

Tao's lecture essay breaks the single goal "solve a problem" into a chain of fully five: solve, verify, explain, accept, and, last, absorb into the field's definitive theory — a stage he calls canonicalization, the slowest of all. The chain answers a sharp question the debate keeps papering over: *which stage is machine-accessible, and which is not?* By this essay's record, the first is now machine-accessible within the formalizable stratum; the second is machine-accessible by construction, since that is what the kernel is; the third, explanation, is the frontier — machines can write the words, and the words now routinely fail to teach; the fourth and fifth, acceptance and canonicalization, are *constituted by* the human community and cannot be executed on its behalf. Five gates; on present evidence the machine has passed two and a half, and the decisive ones stand at the end, in the hands of the species, by definition.

### The correction the conversation skips

One correction belongs in this chapter before it ends — the correction the whole conversation tends to skip. "Western mathematics," the axiomatic, formal, set-theoretic tradition, is one dialect of saying precisely, not the language itself. The Chinese algorithmic tradition — *The Nine Chapters*, celestial-source algebra (天元术), the Yang Hui / Jia Xian triangle — is mathematics of the first rank; it *computed* what the axiomatic style later *proved*. The point that conclusion resists is not rejoinder but scale. The same story runs to every corner of the record: the Kerala school computed the power series for π and the sine in the order of two centuries before the European calculus — on the question of transmission, scholars remain split, but that is the only part of the claim in dispute. The arithmetic we call Arabic numerals is Indian, decimal place value in full working order attested in Brahmagupta's *Brahmasphuṭasiddhānta* of 628, and it is from a ninth-century Baghdad mathematician's name — al-Khwārizmī, author of *Kitāb al-jabr* — that the word *algebra* descends; "algorithm," of all words, is his Latinized name (Algoritmi). The sexagesimal arithmetic of the old Babylonians, in positional use by the second millennium BCE, still keeps the sixty-minute hour and the 360-degree circle. The Maya wrote a positional zero, dot-one, bar-five, shell-nought, on vigesimal place, at Chiapa de Corzo by 36 BCE — the oldest date on record for a zero written in place, independent of the Old World's. The Inka administered an empire on quipus, decimal positional knot-records of astonishing bookkeeping reach — how far the cords also carry language is the question that still divides specialists. Nearly every world this essay glances at invented mathematics on its own grounds, and the dialect that now calls itself "modern mathematics" grew, by tribute and conquest both, out of the same many-roots tree. When the 2026 machine broke Erdős's conjecture with levers — unit groups, algebraic number fields — inherited from that older arithmetic earth, it was reading every dialect at once, not one. Wisdom has no nationality; the shame is that the conversation has.
<!-- zh -->
## 第五章 · 形式化之后的分工：机器做什么，人做什么

先把诸关系摆平，因为本章其余的一切都要挂在它们上面：*可量化* ⊂ *可计算* ⊂ *可形式化* ⊂ *数学*。逻辑是特殊的——它是每个形式系统的骨架，同时又是数学自己的对象之一，由证明论以数学的方式研究。要点在于嵌套本身，而非标签。凡机器"解出"的一切，都住在可形式化的那一层。Erdős 反例住在那里——所以它才可能被认证——象棋与围棋的每一步也都住在那里。博弈轨迹与数学轨迹，在这层相叠，且仅在此相叠。

### 搬得过界的，与搬不过界的

那么，从象棋到围棋再到数学的这条轨迹，诚实度量如下。能搬过界的，是*受规则支配的内核*：一个正确性无需援引语境即可判定的疆域。象棋全可判；围棋近乎全可判；数学可形式化的一格，原则上全可判。这就是为什么同一套搜索技法能一座堡垒接一座堡垒地前进。搬不过界的，是内核周围的一切——研究哪一局棋的选择、判哪一手*重要*而非仅仅合法、决定这一道猜想而非那一道应当赢得下一个十年。没有判官能认证重要性，因为重要性不是棋盘上的一个位置。轨迹笔直延伸，恰好到规则用尽之处；然后它拐弯。拐弯不等于断裂。而拐弯的那一层，没有任何奖励信号触达：搜索空间里没有哪一处写着哪道猜想配得上下一个十年——强化学习能给证明打分，却造不出那个提问。

### 对「显而易见」的无感

在可形式化的一层，机器的优势已不是速度。是对"显而易见"的无感——乐于尝试一种人类专家早已学会称之为无关的语言。人类知道单位距离问题的正确画面；众所周知，那画面就是笼子。机器不受打扰，试了另一个数系，便走了出去。在有界、可检、可搜的任务上，超出单人的搜索如今稳胜单人的搜索。First Proof 追加了一条令人不安的推论：机器非但跑赢解题者，还跑赢*核验者*——在人类判官来得及裁决之前，就端出论证。

### 分工自行写就

分工于是自行写就，这正是当下恐慌为何错失靶心。机器负责提案、构造、形式化、检查。人类选择目标、选择语言、判别重要性、守住共同体的标准，并且——用陶的话——*消化*：把被验证的结果，变成数学家装得进脑子的形状。乐观派与末日派共同预测的每一个瓶颈——证明跑赢核验、核验跑赢书写、书写跑赢审稿——都只会让人类那一半更稀缺，而非更可有可无。注意力是有限的；机器制造供给，不制造需求。把机器输出转译成理解的那个人，并没有被自动化掉；她被升职了。甚至可以写得更具体：未来的数学家将分化为形式化建筑师、机器证明的审计者、以及把机器输出再译回共同体日常语言的阐释者——正是这十年的事件在不断产出的三份工。

### 五道关口

陶的演讲文章把"解一道题"这一个目标拆成一串五道关口：解出、核验、解释、接受，最后被编入这个领域的定论——他称之为正典化，最慢的一关。这一串，回答的是当前争论一直含糊其辞的那个尖锐问题：*哪一关对机器开放，哪一关不对？* 按本文的记录：第一关，在可形式化的一层，现已对机器开放；第二关，按构造即对机器开放——那正是内核存在的意义；第三关"解释"是前沿——机器写得出话，而那些话如今照例教不会人；第四、第五关"接受"与"正典化"，*由*人类共同体*构成*，无人能代为执行。五道关口，就现有证据，机器已过两道半，决定性的关隘在末尾——握在人类物种手里，这是定义使然。

### 整场对话跳过的更正

本章结束前还需放上一条更正，而它是整场对话惯常跳过的那条更正。"西方数学"——公理化、形式化、集合论的传统——只是"精确言说"的一种方言，而非语言本身。中国算法传统——《九章算术》、天元术、杨辉/贾宪三角——是一流数学；它*计算*出了公理化风格后来才*证明*的东西。这条结论抵抗的，不是反驳，而是体量。同一套故事写到记录的每一角：喀拉拉学派计算 π 与正弦的幂级数，比欧洲微积分早约两个世纪——至于是否传入欧洲，学者至今两派分立，但那只是这一句里唯一被争议的部分。我们称之为"阿拉伯数字"的算术，实为印度发明，628 年婆罗摩笈多的《婆罗摩修正历数书》中十进制位值已完整运转；"代数"一词来自九世纪巴格达一位数学家的书名——《还原与对消之书》，作者花拉子米；"算法（algorithm）"——这个词本身——就是他名字的拉丁化拼写。古巴比伦的六十进制位值算术，公元前两千纪已在用，如今仍守着六十分钟、六十秒、三百六十度。玛雅人写位置零：点为一、横为五、贝壳为零，二十进制位值，恰帕·德·科尔索量尺历碑最早刻于公元前 36 年——这是记录里最早的、独立于旧大陆的"写在位置上的零"。印加人用奇普治理一整个帝国：十进制位值的结绳账目，簿记之广大得惊人——这些绳结在多大程度上也能承载语言，正是至今仍让专家分裂的问题。这篇随感所瞥见的几乎每个世界，都曾在自己的土地上发明数学；如今自称"现代数学"的方言，正是从同一棵多根的树上，靠进贡与征服兼有地长出来的。当 2026 年那部机器用它撬开 Erdős 猜想的杠杆——单位群、代数数域——来自那片更古老的算术大地时，它一次读的是每一门方言，不是某一家。智慧没有国籍；难为情的是，这场对话有。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第六章 · 开创性问题之争：机器提得出大问题吗？ / The Dispute About Groundbreaking Problems: Can the Machine Pose One?

"Groundbreaking" has to mean more than "hard." A theorem advances a frontier; a breakthrough moves the border itself — a new definition, a new language, a field turning toward a new object. Descartes' coordinates made geometry algebra and algebra geometry. Newton's and Leibniz's calculus gave change itself a syntax. Gauss rebuilt number theory until "law" meant "pattern with a proof." The common thread is the re-description of Chapter 3, run at the scale of a whole discipline.

### Where the machine stands

By that standard, where does the machine stand? On the public record it has shown the *cross-language* half of the act, not yet the *language-building* half. The unit-distance disproof is a first-rate theorem — a paradoxical family of counterexamples, a long leap from number theory into geometry — but it resolves a question mathematicians had posed, in a dialect, algebraic number theory, that already existed. Schneier and Rafi's distinction still holds: strong at recombination, unproven at theory-building. Nothing in the record yet shows an AI constructing a genuinely new system of concepts — the way category theory was new, the way sheaf theory was new. Read the games trajectory precisely and it predicts this: it advances steadily inside a given rule-system; it has not yet been seen founding one.

### Wall-breaking: Zhang and the parity barrier

One refinement stands between this claim and the honest counterexample, and it must be stated so the counterexample keeps its full force. "World-creation" is not the only kind of boundary-crossing that deserves the name breakthrough; there is also the defeat of a *wall* that older human efforts could not pass, and that defeat, too, can be historic. Zhang's 2013 theorem — infinitely many prime pairs within a bounded gap, first shown below seventy million — was universally received as a breakthrough of the first order, and it was won entirely inside an existing language: the sieve and its friends, methods nearly a century old. The theorem did not invent a new framework; it found that the old framework still had headroom nobody had seen. The parity barrier of sieve theory, however, then closes that headroom: sieve methods are structurally blind to the difference between a prime and a product of two primes — the arithmetic of parity — which is why the method has never resolved the twin-prime gap of exactly two nor Goldbach's "1+1," and why Chen's celebrated result — every sufficiently large even number is the sum of a prime and a number that is prime or a product of two primes — has stood since 1973, the sieve unable to strip away its last "or a product of two primes." The lesson cuts both ways. On one side, "not yet language-building" is a real and honest limit, not a rhetorical bias — the machine's defeats of unit distances and of the forced Navier–Stokes case sit on the same shelf as Zhang's: spectacular *wall-breaking* inside given frameworks. On the other side, wall-breaking of that caliber has, throughout the twentieth and twenty-first centuries, been the normal and sufficient condition for the greatest fame in mathematics. If the standard is "who merely recombines the old language," almost every human giant is convicted alongside the machine; if the standard is "who moves a border," Zhang was a border-mover. The parity barrier is the precise name for the thing the old language cannot do — and no advocate of the greatness of Zhang, and no critic of the machine, has produced a formalism showing which of the two is closer to the barrier's edge.

### The ladder confusion, repeated

Here the anti-AI argument commits its own version of the ladder confusion. It sets the bar at "groundbreaking problems" as though that were a mathematician's ordinary output, when the honest fact is that hardly anyone ever poses one. Hilbert's twenty-three problems redirected a century, and the list is now a monument nobody works in whole; even the specialist who commands a single problem family is rarer than the polymath myth allows. Erdős spent a career *distributing* problems — more than twelve hundred remain catalogued in the modern Erdős problems database, 562 of them now solved — and became, largely by that generosity, the most famous mathematician of his day. Most published mathematics is consolidation: extending, cleaning, sharpening a frame someone else built. If "AI cannot pose groundbreaking problems" is the test, it prunes almost all humans too. Posing deep questions is rarer than the myth admits, distributed wildly unequally, and not obviously a formal skill — which places the slogan "tools can never pose deep questions" in the same category as the older "machines can never think": a bet dressed as a law.

### Ramanujan's unposed questions

No one better defeats that slogan than the man who never received a degree. Srinivasa Ramanujan, a clerk in the Accounts Department of the Port Trust Office at Madras on a salary of twenty pounds a year, had lost his scholarship, failed his First Arts examination, and quit college by the time he wrote to G. H. Hardy in Cambridge in the winter of 1912–13. The letter ran to nine pages of mathematics; it carried "the enunciations of a hundred or more mathematical theorems," with no proofs, and it closed: "Requesting to be excused for the trouble I give you. I remain, Dear Sir, Yours truly, S. Ramanujan." Hardy, who had expected a crank, later wrote of his first reading, "They defeated me completely. I had never seen anything in the least like them before"; the formulas, he added, "must be true because, if they were not true, no one would have had the imagination to invent them." Ramanujan asked questions nobody else had asked — about partitions, about the divisors of tau, about mock theta functions — and he posed them without the apparatus a trained mathematician would have used to formalize them. The rare false ones among them were still worth more than most people's true ones, because they pointed at structures nobody had yet seen. The mock theta functions, from his deathbed letter of 12 January 1920, stayed unexplained for eighty-two years, until Sander Zwegers's Utrecht thesis (2002) revealed them as the holomorphic parts of harmonic weak Maass forms of weight half. The tau conjecture of 1916 waited fifty-eight years for Deligne's proof of 1974 — a proof that had to travel through the full Weil conjectures to arrive — and so unlikely was the landing that Deligne's Fields Medal (1978) was, in part, a medal for a question another man had dared to ask. Berndt's count puts more than three thousand two hundred theorems in the notebooks, almost all conjectured without proof; of the set, a half-dozen are known to be wrong. The point is that a man without the apparatus posed questions the language of the day could not even state cleanly, and then walked away; the profession spent the better part of a century translating those questions into its own terms. That is a form of thinking the modern rhetoric of problem-solving has quietly forgotten: the unposed problem, held in a head without words long enough that the words catch up. If "groundbreaking" means "posing what has never been posed," Ramanujan did it more completely than almost any machine, and his verification lag was measured in decades, not because of sloppiness but because the questions ran so far ahead of the answers that the community had to grow a language in which to answer them. The honest reply to the machine is thus not "machines can never pose deep questions"; it is "machines have not yet posed one — and neither have most humans."

The shape repeats a generation later on the other side of the world. Hua Luogeng, the son of a shopkeeper in Jiangsu who could not finish middle school, taught himself mathematics between errands and a long illness; he too never held a degree, his first being honorary. His short 1930 note in the Shanghai journal *Science*, showing that a celebrated 1926 attempt to solve the quintic was fundamentally flawed, brought him to the attention of Xiong Qinglai, who recruited him to Tsinghua — where he began as a clerk — and later to Hardy's Cambridge. Brilliance has never waited for the school; the school, at its best, comes looking.

### The historical interlude

The historical interlude belongs here because it defeats the strongest form of the disbelief. Descartes, Newton, Leibniz, Gauss were not narrowly "pure mathematicians"; they were polymaths — philosophy, physics, mechanics, astronomy, geodesy, metaphysics as one fabric. Their breakthroughs were cross-domain intuitions: secularizing the mystical, algebraizing the geometric, timing the falling. If what AI does is just recombination, then so has been every breakthrough worth the name; recombination *across* domains is the engine of the history they all wrote. The 2026 disproof is precisely a polymath's move — number theory imported into geometry — the first the public has watched a machine make. Its engine was a novel recombination of tools long in existence, the Golod–Shafarevich constructions the verifiers traced the argument to; and this matters because "creativity as recombination across domains" is not the insult critics sometimes take it for. It is the faithful description of how Newton and Leibniz themselves moved. The honest reservation is therefore not "machines can only recombine." It is "machines have not yet shown judgment about which future is worth building" — and in the noise of the present, neither, here, do many of the humans holding the microphone.

### The deepest act

The deepest act in the profession — deciding that this, not that, matters — is a social judgment about value, exercised by a community over time. AI will flood the docket with filings; it will not, on today's evidence, decide the case. What 2026 proved is that the *border-moving* problem is answerable by search, once the language is given. What remains is choosing the language — and the lesson of the unit-distance problem's eighty years is that no referee, human or machine, can certify which choice was *important* until long after the fact. Importance is a verdict of history, not of proof. And "groundbreaking" is not a binary act of creation from nothing but a continuous spectrum, at the celebrated, inhabited end of which no public record yet shows a machine's footprint.
<!-- zh -->
## 第六章 · 开创性问题之争：机器提得出大问题吗？

"开创性"必须意味着不止"困难"。定理推进界线；突破移动界线本身——一个新定义、一门新语言、一个转向新对象的领域。笛卡尔的坐标，让几何成为代数、代数成为几何。牛顿与莱布尼茨的微积分，为"变化"本身造出一句语法。高斯重构数论，直到"定律"意味着"有证明的模式"。共同线索，是第三章的"重新刻画"，以一门学科的规模来运行。

### 机器站在何处

按此标准，机器站在何处？就公开记录而言，它展示了那动作的*跨语言*一半，尚未展示*造语言*那一半。单位距离反例是一流定理——一组悖论式反例族，一次从数论跃入几何的奇崛长跳——但它解决的问题，是数学家提出来的，用的是早已存在的方言：代数数域论。Schneier 与 Rafi 的区分依然成立：重组为强，建理论未证。记录里还找不到任何迹象表明 AI 构造了一门真正新的概念体系——那种范畴论之新、层论之新。把博弈轨迹读得精确些，它预言的就是这一点：在给定的规则系统内部稳步前进；开宗立派，至今未见。

### 破壁：张益唐与奇偶性障碍

在这条主张与诚实的反例之间，还隔着一重必须说破的精化，好让反例保留全部力量。"创世"并不是唯一够格称为突破的越界；与之并立的，还有对*墙*的击破：旧日人力未能越过的一座墙，这一击本身也可以是历史性的。张益唐 2013 年的定理便是如此：存在无穷多对间隔有界的素数，最初的界是七千万。这份成果被公认为头等突破，而它完全是在既有语言内部取得的：筛法及其家族，一套近百年历史的方法。它没有发明新框架，只是发现旧框架里还有无人看见的余裕。然而筛法的奇偶性障碍随即封住了这道余裕：筛法在结构上分不清"素数"与"两素数之积"，这正是奇偶性，故此方法从未解出恰等于二的孪生素数间隔，也从未解出哥德巴赫的"1+1"。陈景润的著名结果，一切充分大的偶数皆为"一个素数加一个素数或两素数之积"，自 1973 年起便站在那里，筛法始终无法剥去最后那个"或两素数之积"。这教训是双刃的。一面，"尚未造语言"是真实而诚实的限度，不是修辞偏见；机器击破单位距离、击破受迫 Navier–Stokes 两案，与张益唐属于同一层货架，都是在给定框架内部改写纪录的*破壁*。另一面，破壁到那个份上，在整个二十与二十一世纪，向来就是数学界最高声望的常规而充分的条件。若以"谁不过是在重组旧语言"为标准，几乎每一位人类巨人都会与机器一道被定罪；若以"谁移动了边界"为标准，张益唐移动了边界。奇偶性障碍，是那个旧语言做不到之事的精确名字。无论是为张益唐的伟大辩护的人，还是机器的批评者，都没有产出任何形式化，能证明两者之中谁更靠近这道障碍的边缘。

### 梯级混淆，再度上演

反 AI 的论证在此犯下它自己版本的梯级混淆。它把标杆设在"开创性问题"，仿佛那是数学家的常规产出——而诚实的事实是，几乎没有任何一位数学家提出过。希尔伯特的二十三个问题重新定向了一个世纪，如今这清单是一座没人能在整体上工作的丰碑；连只懂单个问题家族的行家，也比全能天才神话所承认的更稀少。埃尔德什以毕生*分发*问题——现代 Erdős 问题库至今录得一千二百余道，其中五百六十二道已解——大体上就凭这份慷慨，成了他那个时代最著名的数学家。已发表数学的多数是巩固：延伸、清洗、磨利别人搭好的框架。倘若"AI 提不出开创性问题"是考题，那它也淘汰了几乎所有人类。提出深刻问题，比神话承认的更罕见，分配得极端不均，也显然不是一项形式化技能——这把"工具永远提不出深刻问题"的口号，归入"机器永远不能思考"的旧口号同一个类：一个穿上法律外衣的赌注。

### 拉马努金没有提出的问题

没有人比这位没有学位的人更能击败那句口号。斯里尼瓦瑟·拉马努金，马德拉斯港务局会计处的文员，年薪二十英镑，丢了奖学金、没通过学士考试、退了学，在 1912 年冬写信给剑桥的 G. H. 哈代。信是九页数学；上面载着"一百或更多条数学定理的陈述"，一条证明都没有，结尾写道："请原谅我给你添的麻烦。我仍是你真诚的 S. Ramanujan。"哈代原本只当是疯子来信，后来却写道："它们彻底击垮了我。我从未见过与它们有丝毫相似的东西"；那些公式，他补了一句，"必然是真的，因为如果它们是假的，没有人会有那样的想象力去发明它们"。拉马努金问了别人没问过的问题——关于整数分拆、关于 tau 函数的因子、关于 mock theta 函数——而提出它们时，他没有一位受过训练的数学家本该有的形式化装备。其中极少数是错的，但那几个错的，也比多数人对的更有价值，因为它们指向了当时无人看见的结构。mock theta 函数，出自他 1920 年 1 月 12 日的临终信，八十余年无人能解，直到 2002 年桑德·泽格斯的乌得勒支博士论文，揭示它们是半权调和弱 Maass 形式的全纯部分。tau 猜想提出于 1916 年，等了五十八年，才等来德利涅 1974 年的证明——那是一场必须穿过整套 Weil 猜想的降落——而这项猜想是如此难以落地，德利涅 1978 年的菲尔兹奖，一半是颁发给另一个敢于提问之人的问题。贝尔恩特的清点说，笔记里躺着三千二百余条定理，几乎全部是无证明的猜想；其中约六条已知是错的。要害在于：一个没有装备的人提出了当时语言根本无法干净陈述的问题，然后转身走了；这个职业随后花去大半个世纪，把那些问题翻译进自己的语言。这是现代"解题"修辞悄悄遗忘的一种思考方式：那个尚未被提出的问题，先在头脑里无言地存着，久到语言终于赶上它。倘若"开创性"意味着"提出从未被提出过的东西"，拉马努金达到的程度超过几乎任何一部机器，而他的核验滞后是以几十年计的，不是因为草率，而是因为问题远跑在答案前面，共同体不得不先长出一门回答它们的语言。因此对机器诚实的回答不是"机器永远提不出深刻问题"，而是"机器至今一个也未提出——而大多数人同样没有"。

一代之后，世界的另一头重复了同样的形状。华罗庚，江苏小店主之子，连中学都没读完，靠算账和一场长病之间的自修学会了数学；他同样从未持有学位，第一个学位是名誉的。1930 年他在上海《科学》上那篇短文，指出一篇名噪一时的 1926 年五次方程"解答"根本站不住脚，由此吸引了熊庆来，把他招进清华——他初到是当职员——后来又去了哈代的剑桥。才华从来不等学校；好的学校，好在会找来。

### 历史插曲

历史插曲之所以属于本章，是因为它击败了怀疑的最强版本。笛卡尔、牛顿、莱布尼茨、高斯都不是狭隘的"纯数学家"；他们是多面手——哲学、物理、力学、天文、测地、形而上学，同一匹织物。他们的突破是跨域直觉：把神秘学世俗化、把几何代数化、为下落计时。若说"AI 所做无非重组"，那么古往今来配得上引用的突破，无一不是重组；*跨域*重组，正是他们共同写下的那部历史的引擎。而 2026 年的反例，恰恰就是标准的多面手动作——把数论引进几何——这是公众第一次眼看着一部机器做出来。它的引擎，是对早已存在的深刻工具的一次新颖重组：核验者把它追溯到 Golod–Shafarevich 构造。这里要紧的，是"跨域重组即创造"并非反对者有时以为的那种贬损，而是对牛顿、莱布尼茨如何运思的如实描述。因此，老实的保留意见不是"机器只会重组"，而是"机器尚未展现对'哪个未来值得造'的判断"——而眼下这片噪声里，握着麦克风的人类，许多也未必具备这个判断。

### 最深的动作

这个职业里最深的动作——判定这一件而非那一件要紧——是一种关于价值的社群判断，由共同体在时间里行使。AI 会往案头塞满诉状；按今天的证据，它不会判案。2026 年证明的是：*移动边界*的问题，只要语言给定，搜索即可作答。剩下的，是选择语言——而单位距离问题过去八十年的教训是：没有任何判官，无论人或机器，能在时过境迁之前认证哪一次选择*重要*。重要性是历史的判决，不是证明的判决。而"开创性"，从来不是"从无到有"的非此即彼，而是一条连续谱；它的著名一端、有人居住着的那一端，在任何公开记录里，都还见不到机器的足迹。
<!-- L1-end -->

---

<!-- L1 -->
<!-- en -->
## 第七章 · 相融而不言其名：用平实的话说，还是一场危机吗？ / Containment, Without the Vocabulary: In Plain Words, Is It Still a Crisis?

### The plainest truth

Say it in words plain enough for anyone, purged of every borrowed term: nothing stands alone; everything holds everything else up; the tool is part of the mountain. The score is not the music, and the music is not the score; neither exists without the other. No school's vocabulary, no incantations — only the plainest truth there is, a truth that has been available for two thousand years and has never been less urgent than it is now.

### Connected in practice, not in poetry

All of it is connected in practice, not in poetry. The 2026 disproof needed a number system nobody had connected to the geometry; the benchmarks needed sixty mathematicians; the formalizers needed a century of Lean; the models needed the canon the profession had spent generations building. Remove any strand and the story snaps. Gowers and his eight co-authors did not "beautify a machine's output"; they did half the mathematics, in the oldest sense — turning an unheard claim into something teachable, checkable, alive. Neither party wrote the result alone. The result *was* the meeting. That is not a metaphor; it is a description of the working week.

### The verbs collapse

The sharp nouns — "solve," "understand," "author," "replace" — keep collapsing the moment the relation moves. The machine solved what no human, for eighty years, could; the verification paper made it understood; nobody owns the verb that spans both. Water is not fighting the river for being wetter here than there. A tool that extends a mathematician's reach is not distinguishable, in the life of that mathematician, from a theorem that extends everyone's reach: both are simply more mathematics. The logic that insists "the machine did it and the human did not" is the same logic that would insist the hammer built the house.

### The fear of redundancy was a category error

The fear of redundancy dissolves the same way, because it was a category error from the start. It assumes a zero-sum shelf of roles and a fixed stock of dignity. Look longer and dignity is found in the movement: the referee who makes the slop readable, the teacher who keeps the pattern alive in another person's mind, the one who at the table says *this, not that*. Every predicted bottleneck makes these more needed, not less. Redundancy confuses the number of people with the amount of care. A river is not half-empty for being deep in one bend and shallow in another; the water is the whole river at every point.

### The banks hold, and the water runs

And what is the fitting reply to the honest fear — "will I still be needed?" Not reassurance. It is the oldest partition of labor we have: the banks do not worry whether the water needs them; they hold, and the water runs. A river without banks is a flood; a river without water is a ditch. The profession's job is to stay the bank — to judge, to teach, to keep the standard that says what may be called true — and to let the water move. Mathematics is not endangered by the machine. It is being asked, for the first time in living memory, what it is *for*; and the honest answer has not changed in two thousand years: it is for the human who meets a pattern, wants it true, and wants to understand why. The machine can hand that human more patterns than any century before. What it cannot do is take the wanting.
<!-- zh -->
## 第七章 · 相融而不言其名：用平实的话说，还是一场危机吗？

### 最直白的真话

用平实到人人都懂的话说：没有什么是独自成立的；一切都托举着别的一切；工具本身是山的一部分。乐谱不是音乐，音乐也不是乐谱；二者缺其一，便都不存在。不提学派的名字，不念任何咒语——只要那最直白的真话；它已备在那里两千年，而此刻，它从未如此要紧。

### 连在实践里，而非连在诗意里

一切都在实践里相连，而非在诗意里相连。2026 年的反例需要一个无人把它连到几何上的数系；基准需要六十位数学家；形式化者需要一个世纪的 Lean；模型需要这个职业几代人垒起来的正典。抽掉任何一股，故事就断。Gowers 与其八位共同作者并不是在"美化机器的输出"；他们做了数学的一半，以最古老的意义——把一句从未听过的断言变成可教、可检、活着的东西。没有哪一方独自写下结果。结果*就是*那场相遇。这不是比喻；这是对一个工作周的描述。

### 动词纷纷塌缩

那些锋利的词——"解出"、"理解"、"作者"、"取代"——每逢关系移动便纷纷塌缩。机器解出了人类八十年未能解出的东西；核验论文使它被理解；横跨两者的动词无人认领。水不会因为此处在彼处更湿，就与河流搏斗。一件延伸数学家臂膀的工具，在数学家的生命里，同一个延伸了所有人臂膀的定理无从区分：二者都只是更多的数学。"是机器做的、不是人做的"这套逻辑，与"是锤子盖的、不是工匠盖的"同一路货。

### 对冗余的恐惧，是范畴错误

对冗余的恐惧同样化解，因为它从一开始就是范畴错误。它预设一块零和的角色货架、一份固定的尊严存量。看得更久些，尊严在*流动*里：让垃圾之海变得可读的审稿人、把范式活着放进别人脑中的师者、在桌边说"要这一件不要那一件"的判官。每一个被预言的瓶颈都只会让他们更被需要，而非更冗余。冗余把人数错当成了用心。一条河不会因为某一弯深、某一湾浅就算半空；水在每个点都是整条河。

### 岸守着，水自流过

至于那个诚实的恐惧——"我还会被需要吗？"——恰当的回应不是安慰。是那份我们最古老的分工：岸从不担心水需不需要它；它守着，水自流过。没有两岸的河是洪水；没有水的河是沟。职业的职责是继续做岸——判断、教授、守住"什么可被称作真"的标准——并让水流。数学并不因机器而受损。在活人的记性所及范围内，它第一次被问"数学是做什么用的"；诚实的答案两千年来未变：为那个遇见范式、愿它成真、又想知道它为何真的人。机器能递到那个人手中的范式，比此前任何世纪都多。它拿不走那份"愿"。
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
- **一手 — Tao on AI and mathematics:** Tao, T. (2026). "Mathematics in the age of AI." arXiv:2608.16753. <https://arxiv.org/abs/2608.16753> (ICM 2026 lecture essay. The five-stage pipeline — solve, verify, explain, accept, canonicalize — is his iterated Goals 6.1–6.5 in §6 "A case study: problem solving"; the "framework of mathematical values and practices" phrasing is from the abstract.)
- **一手 — Zhang's bounded gaps theorem:** Zhang, Y. (2014). "Bounded gaps between primes." *Annals of Mathematics* 179(3), 1121–1174. DOI 10.4007/annals.2014.179.3.7. <https://annals.math.princeton.edu/2014/179-3/p07> (gap < 7×10⁷, infinitely many prime pairs).
- **学界共识·解读 — the parity barrier:** Green, B. (2014). "Bounded gaps between primes." arXiv:1402.4849. <https://arxiv.org/abs/1402.4849> — colloquium notes on Zhang's work; the sieve/parity reading (sieve blind to the parity of the number of prime factors; twin-prime and Goldbach "1+1" out of its reach; Chen's 1973 "1+2" as the method's practical limit) is the standard interpretive account, flagged here as 学界共识·解读.
- **一手 — Chen's theorem:** Chen, J.-R. (1973). "On the representation of a larger even integer as the sum of a prime and the product of at most two primes." *Scientia Sinica* 16, 157–176. (No stable link; full citation given; result cited as 一手 statement of the theorem, with the interpretation above flagged separately.)
- **一手 — the Erdős problems database:** 1,217 problems as maintained at <https://erdosproblems.com/>; 562 (46%) listed as solved as checked 2026-09-23.
- **权威版本 — Poincaré's maxim:** Poincaré, H. *Science and Method* (1908), Part I, Ch. 2, "The Future of Mathematics," p. 31 — "mathematics is the art of giving the same name to different things" (the phrase used in 第三章). English translation commonly cited via *The Foundations of Science* (Halsted trans.), 1913/1921.
- **一手 — the total-resistance argument:** Weinreich, M. (2026). "The crisis of AI-generated mathematics." arXiv:2608.02859. <https://arxiv.org/abs/2608.02859>
- **一手 — the Leiden Declaration:** "Leiden Declaration on Artificial Intelligence and Mathematics" (2026-06-02), sixteen researchers, fifteen universities. DOI 10.5281/zenodo.20302944. <https://leidendeclaration.ai/> · Institutional endorsements: IMU, ICARM, Mathlib Initiative; featured endorsements incl. Peter Scholze and Terence Tao; 4,181 signatories as of 2026-09-23. IMU endorsement circular: <https://www.mathunion.org/fileadmin/documents/2026-06/IMU_AO_CL_8_2026.pdf> · *Nature* editorial (2026-06-18): <https://www.nature.com/articles/d41586-026-01881-2> · Report: Leiden University news (2026-06-02). <https://www.universiteitleiden.nl/en/news/2026/06/leiden-declaration-warns-ai-is-challenging-the-core-values-of-mathematics>
- **学界共识·解读 — Harris:** Harris, M. (2026). "Knowledge Collapse." *Boston Review*, Summer 2026. <https://www.bostonreview.net/articles/knowledge-collapse/> (Essay; the chess/Go/math syllogism is quoted from it — interpretive.)
- **权威版本 — the moderate view:** Schneier, B., Rafi, K. (2026-08-25). "No, AI Doesn't Mean the End of Mathematics—at Least Not Yet." *The Guardian*, via <https://www.schneier.com/essays/archives/2026/08/no-ai-doesnt-mean-the-end-of-mathematics-at-least-not-yet.html> (Opinion/commentary — flagged.)
- **存疑 — First Proof (Harvard):** a challenge of ten unpublished lemmas (Lauren Williams and co-authors); AI solved ≥6/10; a second batch is registered behind a nonprofit. Reported on Harvard Mathematics pages and in 2026 coverage; no stable institutional link verified at writing — the precise figures are 存疑 pending primary records.
- **存疑 — secondary reports:** Tsimerman's reported fatalism and the Cheng–Liu–Gao double-discovery experiment are cited *as reported in* arXiv:2608.02859 and press coverage; not verified at a single primary source.
- **一手 — Navier–Stokes (claimed):** OpenAI (2026-09-08), "On the Navier–Stokes Millennium Prize Problem." <https://openai.com/index/navier-stokes-solution/> · Clay Mathematics Institute (2026-09-11), "Navier-Stokes Announcement," problem "apparently" settled, evaluation deliberately unhurried: <https://www.claymath.org/news/navier-stokes-announcement/> · Clay Millennium Prize rules (qualifying-venue publication, two years in the literature, general acceptance): <https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf> · *Scientific American* (2026-09-21), "Did OpenAI solve the wrong Navier-Stokes problem?" — the unforced/forced distinction; interpretive journalism, flagged.
- **存疑 — the September attribution dispute:** Buckmaster's reported account — an offer to publish the forced Navier–Stokes result under his name alone, excluding Alpöge for competitive reasons, and a career-adjacent warning — with OpenAI's flat denial; contested, no adjudicated record at writing.
- **存疑 — AlphaEvolve (2025-26):** the 48-multiplication 4×4 complex matrix algorithm breaking Strassen's 49 after fifty-six years; ~70% rediscovery and genuine progress on a fifth of the rest (including an improved kissing-number bound in dimension 11) across some fifty open problems. As reported by DeepMind and 2025-26 coverage; figures 存疑 pending a fully verified primary record.
- **存疑 — IMO 2025 specifics:** both labs' gold-standard 35/42 (five of six); DeepMind's grading by official IMO coordinators vs. OpenAI's three self-selected former medalists; the "gentlemen's agreement" side of the exchange. DeepMind's page is 一手; OpenAI-side particulars are secondary as reported.
- **一手 — Lean's own limit:** Lean Language Reference, "Validating Proofs" — the kernel checks proof terms; what the statement *means* is expressly a separate task. <https://lean-lang.org/doc/reference/latest/ValidatingProofs/>
- **学界共识·解读 — mathematics anxiety:** Caviola et al., *Educational Psychology Review* (2022), meta-analysis aggregated across 177 studies / 900,000+ participants: <https://link.springer.com/article/10.1007/s10648-021-09618-5> · Namkung, Peng & Lin, meta-analytic investigation (84 samples): <https://pmc.ncbi.nlm.nih.gov/articles/PMC6692457/> (quantitative reviews — 解读性; stereotype-threat mechanisms are complex and are not overstated here).
- **一手 — in-repo cross-check:** the disproof's formal entry <../famous_problems/erdos_unit_distance.md> and its proof narrative <../proof_narratives/erdos_unit_distance.md> state the same results with their own sources.
- **interpretive — Saussure (signifier/signified) and Kant (synthetic a priori):** standard textbook accounts of *Course in General Linguistics* (1916) and the *Critique of Pure Reason* (1781/1787) — the chapter reads them as common intellectual property, not as claims in dispute.
- **一手 — Ramanujan's first letter to Hardy (16 Jan 1913):** full transcript with the "I beg to introduce myself to you as a clerk in the Accounts Department of the Port Trust Office at Madras on a salary of only £20 per annum" opening and the "Requesting to be excused for the trouble I give you" close — IMSc transcript: <https://www.imsc.res.in/~rao/ramanujan/newnow/hardyletterindex.htm>; collected in Berndt, B. & Rankin, R. (1995), *Ramanujan: Letters and Commentary*, AMS/LMS. The "nine pages" and "(a) hundred or more mathematical theorems" descriptions: MacTutor, "G. H. Hardy and the aesthetics of Mathematics": <https://mathshistory.st-andrews.ac.uk/Extras/Hardy_aesthetics/>.
- **一手 — Hardy on the first reading:** Hardy, G. H. (1937), "The Indian Mathematician Ramanujan," *Amer. Math. Monthly* 44, 137–155 — "They defeated me completely... They must be true because, if they were not true, no one would have had the imagination to invent them"; "a mathematician of the highest class." (JSTOR 2301659.)
- **一手 — Ramanujan's life dates and no-degree path:** MacTutor biography <https://mathshistory.st-andrews.ac.uk/Biographies/Ramanujan/>; Britannica entry; Cambridge BA by Research (16 Mar 1916) per Cambridge records.
- **一手 — mock theta functions / deathbed letter (12 Jan 1920) / Zwegers 2002:** S. Zwegers (2002), *Mock Theta Functions* (Utrecht PhD thesis), arXiv:0807.4834 (2008); letter transcript at IMSc; "harmonic weak Maass forms of weight half" per Zwegers and Griffin–Ono–Rolen, *PNAS* 110 (2013).
- **一手 — tau conjecture and Deligne:** Ramanujan (1916), the τ-function conjecture; proved in Deligne (1974), *La conjecture de Weil I*, Publ. IHÉS 43, 273–307; Deligne's Fields Medal in 1978 (paper date 1974) per IMU Fields Medal pages <https://www.mathunion.org/>.
- **一手 — notebook theorem counts / handful of errors:** Berndt's count of "more than 3200 results" (a half-dozen incorrect) cited in R. P. Schneider (2012), "Uncovering Ramanujan's 'Lost' Notebook," arXiv:1208.2694; incorrect claims (lost notebook p. 336) analyzed in Berndt, Dixit, Roy & Zaharescu (2016), arXiv:1608.03670.
- **一手 — Hua Loo-Keng (self-taught, no degree, 1930 quintic correction, recruited by Xiong Qinglai):** NAS Biographical Memoirs, "Loo-Keng Hua" <https://www.nasonline.org/publications/biographical-memoirs/memoir-pdfs/hua-loo-keng.pdf>; MacTutor biographies of Hua and Xiong Qinglai; obituary, *Acta Arithmetica* LI (1988) (his 1929 first paper and 1930 correction of the 1926 quintic claim are listed in the bibliographies).
- **权威版本 — cross-civilizational mathematics (Kerala, China, Islam, Maya):** J. Stillwell / V. J. Katz (ed.) (2007), *The Mathematics of Egypt, Mesopotamia, China, India, and Islam: A Sourcebook*, Princeton UP — "mathematics has always been a worldwide activity"; G. G. Joseph, *The Crest of the Peacock: Non-European Roots of Mathematics*, 3rd ed. (2011), the polycentric corrective (its Kerala-transmission thesis is the minority view; flagged separately). Kerala: Katz Sourcebook + MacTutor "Kerala mathematics"; transmission contested per Plofker's review in *Aestimatio* 4 (2013).
- **一手 / 权威版本 — specific dialect claims:** Brahmagupta's 628 rules for zero as number in *Brahmasphuṭasiddhānta* (MacTutor; Plofker 2009); al-Khwārizmī (c. 780–850), *Kitāb al-jabr*, and "algebra"/"algorithm" ← "Algoritmi" (LOC item 2021666184; Britannica); Babylonian sexagesimal in Old Babylonian period thus base-60 minute/degree (MacTutor "Babylonian numerals"); Maya positional zero at Chiapa de Corzo 36 BCE and Tres Zapotes 31 BCE (Britannica; AAS "Nik — The Zero in Vigesimal Maya Mathematics," 2021); Inka quipu as decimal positional knot-records (L. Locke, 1923 — foundational decode; U. G. Urton, *Signs of the Inka Khipu*, 2003, and F. Salomon, *The Cord Keepers*, 2004 for the contested narrative-language reading).
- **一手 — Gowers on Ramanujan's asking (framework for 第六章):** W. T. Gowers (2013), "The work of Pierre Deligne," Abel Prize biography — "It took extraordinary insight for Ramanujan to ask his conjecture about the τ function: the probable truth of that statement was a brilliant observation."
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
- **一手 — 陶哲轩论 AI 与数学：** Tao, T.（2026）《Mathematics in the age of AI》。arXiv:2608.16753。<https://arxiv.org/abs/2608.16753>（ICM 2026 演讲文章。五道关口——解出、核验、解释、接受、正典化——出自其§6「A case study: problem solving」中迭代出来的目标 6.1–6.5；「数学价值与实践的框架」一语出自摘要。）
- **一手 — 张益唐有界间隔定理：** Zhang, Y.（2014）《Bounded gaps between primes》，*Annals of Mathematics* 179(3)，1121–1174。DOI 10.4007/annals.2014.179.3.7。<https://annals.math.princeton.edu/2014/179-3/p07>（无穷多素数对、间隔小于 7×10⁷。）
- **学界共识·解读 — 奇偶性障碍：** Green, B.（2014）《Bounded gaps between primes》。arXiv:1402.4849。<https://arxiv.org/abs/1402.4849>——张益唐工作的演讲笔记；「筛法对素因子个数的奇偶性失明；孪生素数与哥德巴赫'1+1'非筛法所及；陈景润 1973 年'1+2'即其实际极限」是标准解读，此处按学界共识·解读标注。
- **一手 — 陈氏定理：** Chen, J.-R.（1973）《On the representation of a larger even integer as the sum of a prime and the product of at most two primes》，*Scientia Sinica* 16，157–176。（无稳定链接，按家规给全书目；定理本身按一手引用，上述解读另行标注。）
- **一手 — Erdős 问题库：** 截至 2026-09-23 校验，<https://erdosproblems.com/> 收录 1,217 道，其中 562 道（46%）标记为已解。
- **权威版本 — 彭加莱的名言：** Poincaré, H.《Science and Method》（1908），第一部分第二章「数学的未来」，第 31 页——「数学是给不同的事物以同一名字的艺术」（即第三章所用之语）。通行英译见《The Foundations of Science》（Halsted 译），1913/1921。
- **一手 — 彻底抵制论：** Weinreich, M.（2026）《The crisis of AI-generated mathematics》。arXiv:2608.02859。<https://arxiv.org/abs/2608.02859>
- **一手 — 莱顿宣言：**「Leiden Declaration on Artificial Intelligence and Mathematics」（2026-06-02），十六位研究者 / 十五所大学。DOI 10.5281/zenodo.20302944。<https://leidendeclaration.ai/> · 机构背书：IMU、ICARM、Mathlib 倡议；盛赞署名含 Peter Scholze 与陶哲轩；截至 2026-09-23 共 4,181 名签署人。IMU 背书通告：<https://www.mathunion.org/fileadmin/documents/2026-06/IMU_AO_CL_8_2026.pdf> · 《自然》社论（2026-06-18）：<https://www.nature.com/articles/d41586-026-01881-2> · 报道：莱顿大学新闻（2026-06-02）。<https://www.universiteitleiden.nl/en/news/2026/06/leiden-declaration-warns-ai-is-challenging-the-core-values-of-mathematics>
- **学界共识·解读 — 哈里斯：** Harris, M.（2026）《Knowledge Collapse》，*Boston Review* 夏季刊。<https://www.bostonreview.net/articles/knowledge-collapse/>（论说文；"象棋/围棋/数学"三段论系引自此文——解读性。）
- **权威版本 — 温和有据的观点：** Schneier, B., Rafi, K.（2026-08-25）《No, AI Doesn't Mean the End of Mathematics—at Least Not Yet》，*The Guardian*，转自 <https://www.schneier.com/essays/archives/2026/08/no-ai-doesnt-mean-the-end-of-mathematics-at-least-not-yet.html>（观点/评论——已标注。）
- **存疑 — First Proof（哈佛）：** 十个未发表引理设擂（Lauren Williams 及其合作者）；AI 合计解出 ≥6/10；第二批已在非营利机构名下备案。见哈佛数学系页面及 2026 年报道；成稿时未核到稳定的机构主链接——具体数字按存疑处理。
- **存疑 — 二手报道：** Tsimerman 的末日言论与 Cheng–Liu–Gao"双重发现"实验，均系转引自 arXiv:2608.02859 及媒体报道，未核到单一一手源。
- **一手 — Navier–Stokes（待议）：** OpenAI（2026-09-08）《On the Navier–Stokes Millennium Prize Problem》。<https://openai.com/index/navier-stokes-solution/> · 克雷数学研究所（2026-09-11）《Navier–Stokes Announcement》，称问题「貌似」已解决、评审刻意从缓：<https://www.claymath.org/news/navier-stokes-announcement/> · Clay 千禧年奖项规则（合格刊物发表、文献滞留两年、共同体普遍接受）：<https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf> · 《科学美国人》（2026-09-21）《Did OpenAI solve the wrong Navier-Stokes problem?》——无强迫项/受迫项之分；评述性新闻，已标注。
- **存疑 — 九月署名纠纷：** Buckmaster 报道的陈述——提出将受迫 Navier–Stokes 成果单独署于其名下、以竞争为由排除 Alpöge、并以近乎职业威胁回应公开施压——与 OpenAI 的全面否认；双方说法均未裁决，成稿时无定案记录。
- **存疑 — AlphaEvolve（2025–26）：** 以 48 次标量乘法完成 4×4 复矩阵乘法、刷新斯特拉森 1969 年方法保持了五十六年的 49 次纪录；约七成重新推导至已知最优、其余约两成实质进展（含十一维「接吻数」上界的改善），涉及五十余个开放问题。据 DeepMind 及 2025–26 年报道转述；具体数字待一手记录核实，按存疑处理。
- **存疑 — IMO 2025 之细节：** 两家实验室金牌级 35/42（六题解五）；DeepMind 经 IMO 官方协调员评阅 vs. OpenAI 自选三位前奖牌得主；以及互换中的「君子协定」一面。DeepMind 页面为一手；OpenAI 侧细节系转述。
- **一手 — Lean 自身的边界：** Lean Language Reference《Validating Proofs》——内核检查证明项；陈述*意味着什么*明确是另一项任务。<https://lean-lang.org/doc/reference/latest/ValidatingProofs/>
- **学界共识·解读 — 数学焦虑：** Caviola 等，*Educational Psychology Review*（2022），荟萃 177 项研究 / 90 余万被试：<https://link.springer.com/article/10.1007/s10648-021-09618-5> · Namkung、Peng 与 Lin 的元分析（84 个样本）：<https://pmc.ncbi.nlm.nih.gov/articles/PMC6692457/>（量化综述——解读性；刻板印象威胁之机制复杂，此处不作夸大。）
- **一手 — 本仓内部对表：** 反例的形式化条目 <../famous_problems/erdos_unit_distance.md> 与证明叙事 <../proof_narratives/erdos_unit_distance.md>，以各自来源陈述同一结果。
- **解读 — 索绪尔（能指/所指）与康德（先天综合）：** 依《普通语言学教程》（1916）与《纯粹理性批判》（1781/1787）的标准教材表述——本章视之为公共智识财产，非争议主张。
- **一手 — 拉马努金 1913 年 1 月 16 日致哈代的第一封信：** 全文转录，含开篇"I beg to introduce myself to you as a clerk in the Accounts Department of the Port Trust Office at Madras on a salary of only £20 per annum"与落款"Requesting to be excused for the trouble I give you"——IMSc 转录页：<https://www.imsc.res.in/~rao/ramanujan/newnow/hardyletterindex.htm>；亦收于 Berndt, B. 与 Rankin, R.（1995）《Ramanujan: Letters and Commentary》，AMS/LMS。"九页"与"一百或更多条定理的陈述"之描述：MacTutor《G. H. Hardy and the aesthetics of Mathematics》：<https://mathshistory.st-andrews.ac.uk/Extras/Hardy_aesthetics/>。
- **一手 — 哈代读信时的反应：** Hardy, G. H.（1937）《The Indian Mathematician Ramanujan》，*Amer. Math. Monthly* 44，137–155——"它们彻底击垮了我……它们必然是真的，因为如果它们是假的，没有人会有那样的想象力去发明它们"；"最高等级数学家的（手笔）"。（JSTOR 2301659。）
- **一手 — 拉马努金生平与无学位之路：** MacTutor 传记 <https://mathshistory.st-andrews.ac.uk/Biographies/Ramanujan/>；《不列颠百科全书》词条；剑桥"研究学士"（1916-03-16，据剑桥档案）。
- **一手 — mock theta 函数/临终信（1920-01-12）/策韦尔斯 2002：** S. Zwegers（2002）《Mock Theta Functions》（乌得勒支博士论文），arXiv:0807.4834（2008）；信件转录见 IMSc；"半权调和弱 Maass 形式"之说见 Zwegers 及 Griffin–Ono–Rolen《PNAS》110（2013）。
- **一手 — tau 猜想与德利涅：** Ramanujan（1916）提出 τ 函数猜想；Deligne（1974）《La conjecture de Weil I》，Publ. IHÉS 43，273–307 证明；德利涅于 1978 年获菲尔兹奖（论文 1974 年、奖 1978 年），见 IMU 菲尔兹奖页 <https://www.mathunion.org/>。
- **一手 — 笔记定理计数/少数错项：** 贝尔恩特计数"三千二百余条"（其中约六条错误），见 R. P. Schneider（2012）《Uncovering Ramanujan's "Lost" Notebook》，arXiv:1208.2694；错例（遗失笔记第 336 页）分析见 Berndt, Dixit, Roy & Zaharescu（2016），arXiv:1608.03670。
- **一手 — 华罗庚（自学成才、无学位、1930 年纠正五次方程论文、熊庆来举荐）：** NAS 传记《Loo-Keng Hua》<https://www.nasonline.org/publications/biographical-memoirs/memoir-pdfs/hua-loo-keng.pdf>；MacTutor 华罗庚与熊庆来传记；《Acta Arithmetica》LI（1988）讣告（其 1929 年首篇论文与 1930 年对 1926 年五次方程声称的更正均见书目）。
- **权威版本 — 跨文明数学（喀拉拉、中国、伊斯兰、玛雅）：** V. J. Katz 主编（2007）《The Mathematics of Egypt, Mesopotamia, China, India, and Islam: A Sourcebook》，Princeton UP——"数学向来是遍布世界的活动"；G. G. Joseph《The Crest of the Peacock: Non-European Roots of Mathematics》第 3 版（2011），多元中心论的纠正之作（其喀拉拉西传论属少数派，另行标注）。喀拉拉：Katz 源典 + MacTutor《Kerala mathematics》；西传之争议依 Plofker 评于《Aestimatio》4（2013）。
- **一手 / 权威版本 — 各方言的具体主张：** 婆罗摩笈多 628 年《婆罗摩修正历数书》论零作为数的运算（MacTutor；Plofker 2009）；花拉子米（约 780–850）《还原与对消之书》，"代数""算法"二词均出之（LOC item 2021666184；《不列颠百科全书》）；古巴比伦六十进制位值及六十分钟、六十秒、三百六十度（MacTutor《Babylonian numerals》）；玛雅位置零，恰帕·德·科尔索 公元前 36 年、特雷斯·萨波特斯 公元前 31 年（《不列颠百科全书》；AAS《Nik — The Zero in Vigesimal Maya Mathematics》，2021）；印加奇普作为十进制位值结绳账目（L. Locke，1923 年奠基性解读；其是否兼载叙事之说有争议，见 U. G. Urton《Signs of the Inka Khipu》，2003；F. Salomon《The Cord Keepers》，2004）。
- **一手 — 高尔斯评拉马努金之"提问"（作第六章框架）：** W. T. Gowers（2013）《The work of Pierre Deligne》，Abel 奖传记——"拉马努金竟敢就 τ 函数提出他的猜想，需非常人之洞察：该论断大概为真，本身便是天才的观察。"
<!-- L5-end -->