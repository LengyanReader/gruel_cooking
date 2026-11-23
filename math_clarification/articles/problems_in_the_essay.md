# 文中的数学问题：一页看懂 / The problems in the essay: a one-page field guide

<!-- 姊妹页（companion page v3）：为长稿《各归各位：证明的归机器，理解的归人》（proofs_no_longer_scarce.md）中出现的全部数学问题做普通读者友好的深度导览。每卡八栏：一句话 / 譬喻 / 问的是什么 / 前提·背景 / 先修概念 / 逻辑与语言 / 为什么重要 / 现状。页首设「读卡之前：四个门槛」共享导读（词表、量词与渐近记号、逻辑门槛、譬喻的边界），承接语言学与逻辑学维度；各卡只写该题特需的部分，不重复。AI 起草、未经作者逐条复核（harness §I.6）；「现状」栏事实核于 2026-11-22（A1 依 T2 检索记录的已核实更正），方括号编号指向长稿文末来源表 [1]–[128]；标注「详见」处链接 math_clarification 既有条目（§II.9 单一来源）。双语逐段并列，英文侧与中文侧内容与精神对应。v3 每卡末增一幅几何示意 SVG（纯图形、无自然语言文字，图注承载文字；双语各一份）；图不是证明，图注标明其边界与不按比例之处。 -->

<!-- L0 -->

<!-- en -->

## Foreword

The essay this page accompanies tells a story about machines, proofs, and the people who check them — and the story walks through a crowd of specific mathematical problems: a Millennium Prize equation, an eighty-year-old combinatorial conjecture, a geometry question about seven-dimensional spheres, a counting problem about kisses in eleven dimensions. Most news coverage assumes you already know what these problems are. This page assumes you do not.

Each problem below gets eight fields: **in one line** (compressed), **analogy** (an everyday picture — with its boundary stated, because a compass is not a map), **what is asked**, **background** (who, when, out of what), **prerequisites** (the machinery the statement needs — what the zeta function *is*, what "smoothness" means), **logic and language** (the quantifier structure or logical form that makes the statement say what it says), **why it matters**, and **status** (as of 22 November 2026, with the essay's source numbers). Group A collects the problems that act in the essay's events; Group B collects those cited as background and evidence. Where the cookbook has a full entry, this page links rather than duplicates.

Every card closes with a schematic figure. The drawings carry geometry only — the shape of the question, never a proof and never a scale drawing; the caption says what the figure shows and where it stops. A diagram is a second compass, not a second map.

## Before the cards: four thresholds

**1 · Ten words.** A *conjecture* is a statement with strong evidence and no proof. A *theorem* has a proof. A *counterexample* is one instance that kills a universal claim. *Open* means no proof or disproof yet — it does **not** mean "we are unsure": on the law of excluded middle the statement is already one of true or false; we just do not know which. *Independent* is stronger than "unknown": it means someone **proved** that the accepted axioms can never decide it either way. *Existence* asks "is there at least one"; *uniqueness* asks "is there at most one" — two different questions that sound like one. *Smooth* means every order of derivative exists and is finite — loosely, the quantity has a definite value, rate, acceleration, and so on everywhere. A *singularity* is a point where the rules blow up: some quantity becomes infinite.

**2 · The language of mathematical sentences.** Two words do most of the work. "For **every** n" (∀) and "there **exists** an n" (∃) — swap them and you have a different claim. Erdős conjectured that for *every* n the unit-distance count stays near n; one *family* of counterexamples, existing for infinitely many n, killed it. Asymptotic notation is also grammar: n^(1+o(1)) means "grows like n, with a relative correction that fades as n grows"; O(n^(4/3)) means "never exceeds the shape n^(4/3) up to a constant". These are claims about the *shape of growth*, not exact values. And beware one deeper linguistic trap this essay itself discusses (§3.1, §3.5): mathematical words borrow body and space metaphors — "greater than", "contains", "approaches" — and a formal text keeps the logical form while discarding the intentions; that is why a formalized statement can be "checked" and still not be the sentence anyone meant.

**3 · The logic thresholds crossed.** One counterexample refutes a "for all" claim; no number of examples proves one. A lower bound is established by *building one object*; an upper bound by *excluding all better ones* — the two need opposite kinds of evidence. "Unproved" is not "disproven"; "independent" is not "unnoticed". And a claimed proof is a different status from an accepted one: released, checked, certified, understood — four rungs this essay keeps apart.

**4 · How to read an analogy.** Every analogy below is a compass, not a map: it points at the structure, and each card says where it breaks. That is not a decoration; it is the essay's own doctrine (§3.5): the medium is not the content, and the seam between them is where understanding lives.

<!-- zh -->

## 导读

本页所配套的那篇长文，讲的是机器、证明与核验者之间的故事——而故事里走过一群具体的数学问题：一道千禧年大奖难题、一个悬置八十年的组合猜想、一个关于七维球面的几何问题、一个数十一维空间里「接吻」的计数问题。绝大多数报道默认你早已知道这些问题是什么；本页默认你并不知道。

下面每个问题给八栏：**一句话**（压缩）、**譬喻**（日常画面——并写明边界，因为指南针不是地图）、**问的是什么**、**前提·背景**（谁、何时、出于什么）、**先修概念**（该题陈述所需的机器——zeta 函数到底是什么、「光滑」是什么意思）、**逻辑与语言**（使命题成为该命题的量词结构与逻辑形式）、**为什么重要**、**现状**（截至 2026 年 11 月 22 日，方括号为长文来源编号）。A 组收录文中事件里的「主角」问题；B 组收录论证援引的「背景板」问题。凡本册已有完整条目者，本页只链接、不重复。

每张卡末尾附一幅示意图。图只用几何承载问题的结构——是问题的形状，不是证明，也不按比例；图注写明它显示什么、在哪里停住。图是第二枚指南针，不是第二张地图。

## 读卡之前：四个门槛

**一、十个词。**「猜想」（conjecture）：证据很强、尚无证明。「定理」（theorem）：已有证明。「反例」（counterexample）：一个实例，杀掉一条全称主张。「未解」（open）：还没有证明或否证——**不等于**「我们拿不准」：按排中律，它此刻已经非真即假，只是我们不知道是哪个。「独立」（independent）比「不知道」强得多：有人**证明了**，公认的公理永远判不了它，两边都对不上。「存在性」（existence）问「至少有一个吗」；「唯一性」（uniqueness）问「至多有一个吗」——两个听起来像一个问题的问题。「光滑」（smooth）：每一阶导数都存在且有限——粗略说，这个量处处有确定的值、变化率、加速度……。「奇点」（singularity）：规则在此炸掉——某个量变成无穷。

**二、数学语句的语言学。**两个词承担了大部分工作。「对**每个** n」（∀）与「**存在**一个 n」（∃）——一换，命题就换了一条。Erdős 猜的是「对每个 n，单位距离对数都压在 n 附近」；而否证只需要一族反例在无穷多个 n 上突破它。渐近记号也是语法：n^(1+o(1)) 说的是「像 n 那样增长，相对修正随 n 增大而消失」；O(n^(4/3)) 说的是「不超过 n^(4/3) 这个形状（差个常数倍）」——它们谈的是增长的**形状**，不是精确值。还有一个更深的语言陷阱，正是本文自己讨论的（§3.1、§3.5）：数学词汇借自身体与空间的隐喻——「大于」「包含」「靠近」；形式文本保留逻辑形式、丢掉意图——所以一份「被核验过」的形式陈述，完全可能不是任何人想说过的那句话。

**三、跨过的逻辑门槛。**一个反例可以否证「对所有」式的主张；再多例子也证不出它。下界靠**造出一个对象**；上界靠**排除一切更好的可能**——两种相反的证据形态。「未证明」不是「被否证」；「独立」不是「没人注意」。还有：**被主张的证明**与**被接受的证明**是两种状态——已发布、已核验、已认证、已被理解，本文把四级分开。

**四、譬喻怎么读。**下面每个譬喻都是指南针，不是地图：它指向结构，每张卡都写明它在何处失效。这不是装饰，而是本文自己的学说（§3.5）：媒介不等于内容，两者的缝隙正是理解安身之处。

<!-- L1 -->

<!-- en -->

## Group A · The actors

### A1 · Navier–Stokes existence and smoothness

- **In one line**: do the equations of fluid flow always behave, or can they blow up?
- **Analogy**: a weather forecast run forever. The equations are the rulebook for "filming" a fluid — wind at every point, at every instant. "Existence and smoothness" says the film never jams: every pixel keeps a finite value, forever. A *blow-up* is a frame where one pixel's speed becomes infinite — the film stops. *Boundary*: real air is molecules; the equations are an idealization, so a singularity could mean the idealization (not the weather) breaks — and deciding which is exactly the point of the problem.
- **What is asked**: in three dimensions, do solutions exist for all time and remain smooth — or can they develop singularities?
- **Background**: Navier (1822) and Stokes (1845) wrote the equations of viscous fluids; the question carries one of the seven Clay Millennium Prizes (2000).
- **Prerequisites**: a *partial differential equation* is a rule linking a quantity to its own rates of change across space and time. *Solutions* are the fields obeying it. *Smoothness* here means all derivatives stay finite; *existence* and *uniqueness* are separate questions the Clay statement asks together. A *forcing term* f is an external push (a fan under the fluid); "unforced" means f = 0, the physically primary case.
- **Logic and language**: the problem is a disjunction — prove smoothness forever, *or* exhibit one singularity; either answer wins. That is why a "blow-up proof" would settle it negatively.
- **Why it matters**: the essay's central case (§1.7, §2.2) — September 2026 compressed a technical truth, a commercial race, an authorship dispute and a priority quarrel into one week [1,5,6].
- **Status (22 Nov 2026)**: the Clay page still labels the problem Active [4]. OpenAI's 8 September claim — a machine blow-up proof for statements "C/D", Lean-checked but with a forcing term [1] — was found by a Cambridge team not to match its own natural-language text [118]; the method did not obviously extend to the unforced case [5]. On 20 November, Alpöge and Buckmaster announced an *unforced* Navier–Stokes blow-up proof with a Lean formalization (~600,000 lines, public) — though the repository states the formalization contains no data and the interval-arithmetic *certificate* is not yet released [120,121]. A Lean artifact for a *forced* Euler blow-up (credited to Claude under Alpöge's guidance, Anthropic) is public; an *unforced* Euler proof attributed to three authors could not be verified against primary sources and is treated as unverified here. No prize has been claimed.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Smooth flow for all time, versus a finite-time blow-up">
<title>Smooth flow for all time, versus a finite-time blow-up</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="20" y="40" width="190" height="120" rx="6" fill="#FFFDF9" stroke="#EBDCC4"/>
<line x1="40" y1="62" x2="178" y2="62" stroke="#407CB0" stroke-width="1.5"/>
<polygon points="188,62 178,58 178,66" fill="#407CB0"/>
<line x1="40" y1="86" x2="178" y2="86" stroke="#407CB0" stroke-width="1.5"/>
<polygon points="188,86 178,82 178,90" fill="#407CB0"/>
<line x1="40" y1="110" x2="178" y2="110" stroke="#407CB0" stroke-width="1.5"/>
<polygon points="188,110 178,106 178,114" fill="#407CB0"/>
<line x1="40" y1="134" x2="178" y2="134" stroke="#407CB0" stroke-width="1.5"/>
<polygon points="188,134 178,130 178,138" fill="#407CB0"/>
<text x="115" y="182" text-anchor="middle" font-size="13" fill="#6B5F4F">∀ t</text>
<line x1="300" y1="160" x2="492" y2="160" stroke="#6B5F4F"/>
<line x1="300" y1="160" x2="300" y2="40" stroke="#6B5F4F"/>
<line x1="470" y1="160" x2="470" y2="48" stroke="#A4553F" stroke-dasharray="4 4"/>
<path d="M300 152 C 360 148, 430 120, 466 58" fill="none" stroke="#C9852F" stroke-width="2.2"/>
<text x="470" y="40" text-anchor="middle" font-size="14" fill="#A4553F">∞</text>
<text x="476" y="176" text-anchor="middle" font-size="12" fill="#A4553F">T*</text>
<text x="290" y="50" text-anchor="end" font-size="12" fill="#6B5F4F">‖u(t)‖</text>
<text x="496" y="164" text-anchor="end" font-size="12" fill="#6B5F4F">t</text>
</g>
</svg>
<figcaption><b>Fig. A1</b> · Schematic: smooth flow (left) and a finite-time blow-up (right). The curve shows shape only, not scale.</figcaption>
</figure>

### A2 · The Erdős unit distance conjecture (1946)

- **In one line**: among n points in the plane, how many pairs can be exactly distance 1 apart?
- **Analogy**: a playground with n pegs — how many pairs of pegs can sit exactly one meter apart? Erdős's neat grid (like a city street plan) gives many pairs, and he bet that was essentially the best anyone could do. In 2026 someone found a cleverer arrangement of "streets" — not a grid at all, but one built with number theory — with visibly more pairs. *Boundary*: the real construction is invisible in the plane intuition; it lives in algebraic number fields.
- **What is asked**: is the maximum number of unit distances among n plane points sub-polynomially more than n?
- **Background**: Paul Erdős, 1946; his grid construction gives about n^(1+c/log log n) pairs, and he conjectured u(n) ≤ n^(1+o(1)).
- **Prerequisites**: u(n) is a *maximum* over all arrangements. The growth shapes n^(1+o(1)) and n^(1+ε) are grammar (threshold 2 above).
- **Logic and language**: the conjecture is a *for-all* statement (for every n, the count stays near n); the disproof is *existential* — one family of configurations, working for infinitely many n, with a fixed ε > 0. One family kills the whole conjecture.
- **Why it matters**: in May 2026 it became the first core-field conjecture disproved by an AI system — §1.5's "act three" [19,20].
- **Status (22 Nov 2026)**: disproved. Alon, Bloom, Gowers and others published a human-verified digest of the OpenAI-generated counterexample (u(n) ≥ n^(1+ε) infinitely often); Sawin made the exponent explicit at n^1.014; the classical upper bound O(n^(4/3)) is untouched [19,20]. Full entry: [Erdős Unit Distance](../famous_problems/erdos_unit_distance.md).

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A five by five grid of unit distances, and growth shapes n, n^1.014, n^4/3">
<title>A five by five grid of unit distances, and growth shapes n, n^1.014, n^4/3</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<line x1="40" y1="50" x2="40" y2="170" stroke="#EBDCC4"/>
<line x1="40" y1="50" x2="160" y2="50" stroke="#EBDCC4"/>
<line x1="70" y1="50" x2="70" y2="170" stroke="#EBDCC4"/>
<line x1="40" y1="80" x2="160" y2="80" stroke="#EBDCC4"/>
<line x1="100" y1="50" x2="100" y2="170" stroke="#EBDCC4"/>
<line x1="40" y1="110" x2="160" y2="110" stroke="#EBDCC4"/>
<line x1="130" y1="50" x2="130" y2="170" stroke="#EBDCC4"/>
<line x1="40" y1="140" x2="160" y2="140" stroke="#EBDCC4"/>
<line x1="160" y1="50" x2="160" y2="170" stroke="#EBDCC4"/>
<line x1="40" y1="170" x2="160" y2="170" stroke="#EBDCC4"/>
<circle cx="40" cy="50" r="2.6" fill="#332C23"/>
<circle cx="40" cy="80" r="2.6" fill="#332C23"/>
<circle cx="40" cy="110" r="2.6" fill="#332C23"/>
<circle cx="40" cy="140" r="2.6" fill="#332C23"/>
<circle cx="40" cy="170" r="2.6" fill="#332C23"/>
<circle cx="70" cy="50" r="2.6" fill="#332C23"/>
<circle cx="70" cy="80" r="2.6" fill="#332C23"/>
<circle cx="70" cy="110" r="2.6" fill="#332C23"/>
<circle cx="70" cy="140" r="2.6" fill="#332C23"/>
<circle cx="70" cy="170" r="2.6" fill="#332C23"/>
<circle cx="100" cy="50" r="2.6" fill="#332C23"/>
<circle cx="100" cy="80" r="2.6" fill="#332C23"/>
<circle cx="100" cy="110" r="2.6" fill="#332C23"/>
<circle cx="100" cy="140" r="2.6" fill="#332C23"/>
<circle cx="100" cy="170" r="2.6" fill="#332C23"/>
<circle cx="130" cy="50" r="2.6" fill="#332C23"/>
<circle cx="130" cy="80" r="2.6" fill="#332C23"/>
<circle cx="130" cy="110" r="2.6" fill="#332C23"/>
<circle cx="130" cy="140" r="2.6" fill="#332C23"/>
<circle cx="130" cy="170" r="2.6" fill="#332C23"/>
<circle cx="160" cy="50" r="2.6" fill="#332C23"/>
<circle cx="160" cy="80" r="2.6" fill="#332C23"/>
<circle cx="160" cy="110" r="2.6" fill="#332C23"/>
<circle cx="160" cy="140" r="2.6" fill="#332C23"/>
<circle cx="160" cy="170" r="2.6" fill="#332C23"/>
<text x="100" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">n = 25 → 40</text>
<line x1="262" y1="170" x2="502" y2="170" stroke="#6B5F4F"/>
<line x1="262" y1="170" x2="262" y2="35" stroke="#6B5F4F"/>
<path d="M272 152 C 340 122, 430 82, 496 42" fill="none" stroke="#407CB0" stroke-dasharray="5 4"/>
<path d="M272 154 C 350 132, 440 96, 496 62" fill="none" stroke="#E8A855" stroke-width="2.2"/>
<path d="M272 156 C 350 140, 440 112, 496 80" fill="none" stroke="#6B5F4F" stroke-dasharray="2 4"/>
<line x1="278" y1="40" x2="298" y2="40" stroke="#407CB0" stroke-dasharray="5 4"/>
<text x="304" y="44" text-anchor="start" font-size="10" fill="#407CB0">n^4/3</text>
<line x1="278" y1="58" x2="298" y2="58" stroke="#E8A855" stroke-width="2.2"/>
<text x="304" y="62" text-anchor="start" font-size="10" fill="#C9852F">n^1.014</text>
<line x1="278" y1="76" x2="298" y2="76" stroke="#6B5F4F" stroke-dasharray="2 4"/>
<text x="304" y="80" text-anchor="start" font-size="10" fill="#6B5F4F">n</text>
<text x="502" y="164" text-anchor="end" font-size="12" fill="#6B5F4F">n</text>
<text x="258" y="44" text-anchor="end" font-size="12" fill="#6B5F4F">u(n)</text>
</g>
</svg>
<figcaption><b>Fig. A2</b> · Schematic: a 5×5 grid (n = 25, 40 unit pairs) and the three growth shapes — n, n^1.014, n^4/3.</figcaption>
</figure>

### A3 · Fermat's Last Theorem — and its formalization

- **In one line**: x^n + y^n = z^n has no positive integer solutions for n ≥ 3 — and in 2026 a machine wrote out the entire proof in a language a computer can check.
- **Analogy**: integer-sided cubes. Two cubes' volumes never make a third cube: 3³ + 4³ is not anyone's cube. What makes the statement delicious is the near-miss one floor down: 3² + 4² = 5² — squares *do* work (Pythagoras). Fermat's rule begins exactly where Pythagoras ends. *Boundary*: the analogy shows what is asked, none of why it is hard — the proof runs through elliptic curves and modular forms, territory no cube picture reaches.
- **What is asked** (2026 version): can Wiles's proof be re-derived from Lean's three standard axioms alone, with no human trust anywhere in the chain?
- **Background**: conjectured by Fermat around 1637; proved by Wiles (with Taylor) in 1994–95 after 358 years. Full entry: [Fermat's Last Theorem](../famous_problems/fermat_last_theorem.md).
- **Prerequisites**: "formalization" means transcribing the proof into a formal language (Lean) so a *kernel* — a tiny, trusted checker — verifies each step's type correctness. "Mathlib" is the community's formal library; "five times its size" is a volume claim, not a difficulty claim.
- **Logic and language**: the theorem is a for-all statement over infinitely many n — no computer search can settle it; that is why 358 years of special cases added up to nothing.
- **Why it matters**: §1.8 uses it as the extreme specimen of the verification bottleneck — an artifact no human can read end-to-end [25,26].
- **Status (22 Nov 2026)**: Anthropic announced (4 September) a complete Lean formalization: about 13 million lines, roughly 29,500 intermediate lemmas, eleven days of largely autonomous work, kernel-checked and confirmed to match Mathlib's statement; Buzzard reviewed it and called it an extraordinary autoformalization achievement that adds nothing mathematically new [25,26].

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Squares 3-4-5 add up; cubes 3 and 4 do not add up to a cube">
<title>Squares 3-4-5 add up; cubes 3 and 4 do not add up to a cube</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="26" y="80" width="48" height="48" fill="#F7EFE2" stroke="#C9852F"/>
<text x="50.0" y="144" text-anchor="middle" font-size="12" fill="#6B5F4F">3²</text>
<rect x="94" y="64" width="64" height="64" fill="#F7EFE2" stroke="#C9852F"/>
<text x="126.0" y="144" text-anchor="middle" font-size="12" fill="#6B5F4F">4²</text>
<rect x="186" y="48" width="80" height="80" fill="#F7EFE2" stroke="#C9852F"/>
<text x="226.0" y="144" text-anchor="middle" font-size="12" fill="#6B5F4F">5²</text>
<text x="82" y="96" text-anchor="middle" font-size="16" fill="#6B5F4F">+</text>
<text x="172" y="96" text-anchor="middle" font-size="16" fill="#6B5F4F">=</text>
<text x="300" y="86" text-anchor="start" font-size="12" fill="#332C23">3³ + 4³ = 91</text>
<text x="300" y="116" text-anchor="start" font-size="12" fill="#332C23">5³ = 125</text>
<text x="300" y="152" text-anchor="start" font-size="14" fill="#A4553F">91 ≠ 125</text>
</g>
</svg>
<figcaption><b>Fig. A3</b> · Schematic: squares add up (3² + 4² = 5²); cubes do not (3³ + 4³ = 91 ≠ 125).</figcaption>
</figure>

### A4 · The Riemann Hypothesis

- **In one line**: do all the "interesting" zeros of the zeta function sit on one straight line?
- **Analogy**: the zeta function is a transducer for the primes — plug in the messy, scattered primes, and it outputs one smooth wave whose "heartbeat nodes" (its zeros) govern how evenly the primes are spread. RH says every node lies on one baseline; equivalently, the primes' irregularity is pinned at the smallest size number theory allows. *Boundary*: the wave picture is a sketch of the encoding, not a derivation; the actual equivalence runs through an explicit error term.
- **What is asked**: do all nontrivial zeros of ζ(s) have real part exactly 1/2?
- **Background**: Bernhard Riemann, 1859; one of the seven Millennium Prizes, and the most famous open problem in mathematics.
- **Prerequisites (the zeta function, plainly)**: ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s + … — a dampening sum that converges when s has real part greater than 1. Euler's miracle: the same sum factors into one small factor per prime, ζ(s) = ∏ over primes p of 1/(1 − 1/p^s) — the primes are *encoded* in it. The sum's natural home runs out at real part 1; "analytic continuation" extends the same function beyond it by a uniquely-determined other formula — note the linguistic point: one name, ζ(s), is defined by different formulas on different regions, stitched together by uniqueness; the function is not its formula. The *zeros* are the inputs s where ζ(s) = 0: "trivial" ones at negative even numbers, "nontrivial" ones inside the strip 0 < real part < 1. RH says all nontrivial ones sit exactly on the middle line, real part = 1/2; the *quasi-RH* result in this essay's postscript confines them to the strip 1/8 ≤ real part ≤ 7/8 — a sliver, far short of the line [115]. What rides on it: the zero positions control the error term in counting primes — RH would pin the primes' irregularity at roughly the √x scale.
- **Logic and language**: the hypothesis is a for-all statement over infinitely many zeros; a single zero off the line refutes it. "Quasi-RH" is not a weakened RH in the logical sense — it is a *different, weaker confinement*, proved for all zeros at once.
- **Why it matters**: §6.4 used "will AI prove the Riemann hypothesis" as the question to look past; November 2026 answered a version of it in an unexpected way [93,120,122].
- **Status (22 Nov 2026)**: a proof was announced on 20 November by Levent Alpöge, produced with an internal AI model (press names Claude; Tao's wording says "an internal AI model" — both recorded [120,123]); it exists as a ~17-million-line Lean artifact, and on 21 November the Lean community certified by four stated criteria that "both the statement and the proof of the Riemann Hypothesis are correct" [122]. Earlier in the window, the quasi-RH result from the October release was digested and largely confirmed by human analysts within two weeks [115]. The Association for Human Mathematics objected that no human can responsibly claim to understand such a document [124]. Machine-verified; community-certified; human understanding in progress.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Critical strip, critical line at real part one half, quasi-Riemann band">
<title>Critical strip, critical line at real part one half, quasi-Riemann band</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="250" y="30" width="55" height="148" fill="#F7EFE2"/>
<rect x="256.9" y="30" width="41.2" height="148" fill="#FBE9C8"/>
<line x1="20" y1="110" x2="500" y2="110" stroke="#6B5F4F"/>
<line x1="250" y1="190" x2="250" y2="22" stroke="#6B5F4F"/>
<line x1="277.5" y1="190" x2="277.5" y2="22" stroke="#C9852F" stroke-width="2" stroke-dasharray="6 3"/>
<circle cx="277.5" cy="76.1" r="3.2" fill="#A4553F"/>
<circle cx="277.5" cy="59.6" r="3.2" fill="#A4553F"/>
<circle cx="277.5" cy="50.0" r="3.2" fill="#A4553F"/>
<circle cx="277.5" cy="143.9" r="3.2" fill="#A4553F"/>
<circle cx="277.5" cy="160.4" r="3.2" fill="#A4553F"/>
<circle cx="277.5" cy="170.0" r="3.2" fill="#A4553F"/>
<circle cx="140" cy="110" r="3.2" fill="#6B5F4F"/>
<circle cx="30" cy="110" r="3.2" fill="#6B5F4F"/>
<text x="283.5" y="20" text-anchor="start" font-size="12" fill="#C9852F">Re = 1/2</text>
<text x="256.875" y="194" text-anchor="middle" font-size="10" fill="#9A8D7A">1/8</text>
<text x="298.125" y="194" text-anchor="middle" font-size="10" fill="#9A8D7A">7/8</text>
<text x="140" y="126" text-anchor="middle" font-size="10" fill="#6B5F4F">−2</text>
<text x="30" y="126" text-anchor="middle" font-size="10" fill="#6B5F4F">−4</text>
<text x="309" y="126" text-anchor="start" font-size="10" fill="#6B5F4F">1</text>
<text x="246" y="126" text-anchor="end" font-size="10" fill="#6B5F4F">0</text>
<text x="287.5" y="80.088" text-anchor="start" font-size="10" fill="#A4553F">14.13i</text>
<text x="500" y="126" text-anchor="end" font-size="12" fill="#9A8D7A">Re(s)</text>
<text x="244" y="34" text-anchor="end" font-size="12" fill="#9A8D7A">Im(s)</text>
</g>
</svg>
<figcaption><b>Fig. A4</b> · Schematic: the critical strip 0 < Re < 1, the line Re = 1/2 with its first zeros, the trivial zeros at −2 and −4, and the quasi-RH band 1/8–7/8.</figcaption>
</figure>

### A5 · The Unique Games Conjecture (2002)

- **In one line**: is a certain "guess the labels" problem nearly as hard to approximately solve as it is to solve exactly?
- **Analogy**: seat a network of feuding guests at two tables so that no feuding pair shares a table — sometimes impossible to do perfectly. The conjecture says: for one family of such networks, even letting a *tiny* fraction of feuds through costs just as much as solving the whole thing. It is the "no discount" conjecture: the second-best answer is no cheaper than the best. *Boundary*: the real statement is about labeled constraints and approximation ratios, not tables; the analogy drops the quantitative spine.
- **What is asked**: for constraint systems with a small fraction of violations allowed, is finding a labeling satisfying most constraints computationally intractable?
- **Background**: Subhash Khot, 2002; if true, it locks in optimal "hardness of approximation" results for many classical problems (Max Cut among them).
- **Prerequisites**: an *approximation ratio* is the guaranteed quality of a fast method relative to the perfect one; hardness of approximation proves no fast method can beat a stated ratio.
- **Logic and language**: a conjecture *about difficulty* — its content is a universal statement over all efficient algorithms ("no algorithm ever does better than…"), which is why proofs in this area are rare and refutations would be algorithms.
- **Why it matters**: the 6 October release claimed a proof of it among its 372 families — the most consequential single claim in the batch (§xi of the postscript) [93].
- **Status (22 Nov 2026)**: released claim, not an accepted theorem. Dana Moshkovitz has spent weeks on the proof with Khot, Håstad and Minzer (and the GPT-6 Astra model), confronting what she calls a totally alien new error-correcting code; the effort was presented at the Simons Institute; no full verification has been declared [119].

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="An odd cycle that cannot be two-coloured, and the no-discount axis">
<title>An odd cycle that cannot be two-coloured, and the no-discount axis</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<line x1="120.0" y1="45.0" x2="172.3" y2="83.0" stroke="#EBDCC4" stroke-width="1.4"/>
<line x1="172.3" y1="83.0" x2="152.3" y2="144.5" stroke="#EBDCC4" stroke-width="1.4"/>
<line x1="152.3" y1="144.5" x2="87.7" y2="144.5" stroke="#EBDCC4" stroke-width="1.4"/>
<line x1="87.7" y1="144.5" x2="67.7" y2="83.0" stroke="#EBDCC4" stroke-width="1.4"/>
<line x1="67.7" y1="83.0" x2="120.0" y2="45.0" stroke="#A4553F" stroke-width="2" stroke-dasharray="4 4"/>
<circle cx="120.0" cy="45.0" r="7" fill="#E8A855" stroke="#FFFDF9"/>
<circle cx="172.3" cy="83.0" r="7" fill="#407CB0" stroke="#FFFDF9"/>
<circle cx="152.3" cy="144.5" r="7" fill="#E8A855" stroke="#FFFDF9"/>
<circle cx="87.7" cy="144.5" r="7" fill="#407CB0" stroke="#FFFDF9"/>
<circle cx="67.7" cy="83.0" r="7" fill="#E8A855" stroke="#FFFDF9"/>
<text x="120" y="188" text-anchor="middle" font-size="12" fill="#6B5F4F">C₅</text>
<line x1="250" y1="130" x2="500" y2="130" stroke="#6B5F4F"/>
<line x1="480" y1="120" x2="480" y2="140" stroke="#6B5F4F"/>
<line x1="440" y1="120" x2="440" y2="140" stroke="#A4553F"/>
<text x="480" y="156" text-anchor="middle" font-size="10" fill="#6B5F4F">1</text>
<text x="440" y="156" text-anchor="middle" font-size="10" fill="#A4553F">1−ε</text>
<line x1="440" y1="96" x2="480" y2="96" stroke="#A4553F" stroke-dasharray="3 3"/>
<text x="460" y="88" text-anchor="middle" font-size="14" fill="#A4553F">≈</text>
<text x="250" y="146" text-anchor="start" font-size="10" fill="#6B5F4F">0</text>
<text x="375" y="60" text-anchor="start" font-size="12" fill="#332C23" font-weight="600">UGC</text>
</g>
</svg>
<figcaption><b>Fig. A5</b> · Schematic: an odd cycle cannot be two-coloured — one constraint must break; the axis shows the conjecture's 'no discount' claim.</figcaption>
</figure>

### A6 · The Jacobian conjecture (1939)

- **In one line**: if a polynomial map has a constant nonzero Jacobian, must it have a polynomial inverse?
- **Analogy**: a "polynomial machine" transforms input vectors to output vectors. The Jacobian determinant measures, at each point, how much the machine locally stretches or squashes area; *constant nonzero* means it never flattens anything, anywhere. The conjecture asks: must such a machine come with another polynomial machine that undoes it? In 2026: no, in three dimensions and above — there are machines that squash nothing yet tangle their outputs so that no polynomial can untangle them. *Boundary*: the paper-sheet picture ("locally unfolded everywhere, so globally unfoldable?") carries the flavor; the actual obstruction is algebraic, not geometric.
- **What is asked**: for which dimensions n does a polynomial map C^n → C^n with constant nonzero Jacobian determinant necessarily admit a polynomial inverse?
- **Background**: Ott-Heinrich Keller, 1939; trivial in one dimension, open in two for nearly a century.
- **Prerequisites**: a *polynomial map* is a machine built from additions and multiplications of coordinates; the *Jacobian determinant* is the local stretching factor, computed from the machine's first derivatives.
- **Logic and language**: local-versus-global is the hinge — "invertible at every point" (analytic fact) is weaker than "has a polynomial inverse" (global algebraic fact); the conjecture asks whether the first forces the second, and the counterexamples show it does not, dimension by dimension.
- **Why it matters**: §2.1 lists its July 2026 counterexample among the machine-proof dramas preceding the Fields medalists' letter [1,19,30].
- **Status (22 Nov 2026)**: false for n ≥ 3. Levent Alpöge announced a three-variable counterexample on 19 July 2026, found with the help of an AI model; Tao wrote a public digestion the next day [106]; Gao generalized to every dimension greater than two, with all identities verified in exact rational arithmetic [107]; Buzzard's group saw the counterexample Lean-checked within days [108]. n = 2 remains open.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A shear with constant Jacobian, and a tangle with no polynomial inverse">
<title>A shear with constant Jacobian, and a tangle with no polynomial inverse</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="40" y="60" width="120" height="120" fill="#FFFDF9" stroke="#9A8D7A"/>
<line x1="40" y1="60" x2="40" y2="180" stroke="#EBDCC4"/>
<line x1="40" y1="60" x2="160" y2="60" stroke="#EBDCC4"/>
<line x1="70" y1="60" x2="70" y2="180" stroke="#EBDCC4"/>
<line x1="40" y1="90" x2="160" y2="90" stroke="#EBDCC4"/>
<line x1="100" y1="60" x2="100" y2="180" stroke="#EBDCC4"/>
<line x1="40" y1="120" x2="160" y2="120" stroke="#EBDCC4"/>
<line x1="130" y1="60" x2="130" y2="180" stroke="#EBDCC4"/>
<line x1="40" y1="150" x2="160" y2="150" stroke="#EBDCC4"/>
<line x1="160" y1="60" x2="160" y2="180" stroke="#EBDCC4"/>
<line x1="40" y1="180" x2="160" y2="180" stroke="#EBDCC4"/>
<line x1="220" y1="90.0" x2="220" y2="210.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="250" y1="79.5" x2="250" y2="199.5" stroke="#C9852F" stroke-width="1.4"/>
<line x1="280" y1="69.0" x2="280" y2="189.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="310" y1="58.5" x2="310" y2="178.5" stroke="#C9852F" stroke-width="1.4"/>
<line x1="340" y1="48.0" x2="340" y2="168.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="220" y1="90" x2="340" y2="48.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="220" y1="120" x2="340" y2="78.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="220" y1="150" x2="340" y2="108.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="220" y1="180" x2="340" y2="138.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="220" y1="210" x2="340" y2="168.0" stroke="#C9852F" stroke-width="1.4"/>
<text x="110" y="196" text-anchor="middle" font-size="12" fill="#332C23">det J = 1</text>
<text x="340" y="196" text-anchor="middle" font-size="12" fill="#332C23">n ≥ 3</text>
<path d="M330 70 C 390 30, 470 90, 410 130 C 360 165, 300 110, 350 80" fill="none" stroke="#407CB0" stroke-width="2"/>
<path d="M350 80 C 400 60, 440 120, 390 140" fill="none" stroke="#A4553F" stroke-width="2"/>
</g>
</svg>
<figcaption><b>Fig. A6</b> · Schematic: a shear with constant Jacobian (equal cell areas) and a tangle that no polynomial untangles.</figcaption>
</figure>

### A7 · Positive sectional curvature on all smooth 7-spheres

- **In one line**: can every exotic seven-dimensional sphere be given a geometry where all directions curve positively?
- **Analogy**: an orange peel curves outward everywhere; a saddle curves one way and then the other. "Positive sectional curvature" means *every* two-dimensional slice bends orange-like. The seven-sphere carries 28 legal ways to install calculus on the same topology — 28 differently "wired" twins; the theorem claims each twin can be given an all-orange geometry. *Boundary*: "wiring" (smooth structure) has no everyday picture; the twins are indistinguishable by touch and differ in which functions count as differentiable.
- **What is asked**: construct, for each of the 28 oriented diffeomorphism classes of smooth homotopy 7-spheres, a metric of strictly positive sectional curvature.
- **Background**: John Milnor, 1956, discovered the exotic smooth structures; the curvature question became a long-standing test of how topology constrains geometry.
- **Prerequisites**: a *manifold* is a space that looks like flat space in small patches; a *smooth structure* is a choice of which patches knit together differentiably; *sectional curvature* reads the bending of each two-dimensional slice.
- **Logic and language**: "all 28 classes" is a for-all claim — one class with a proven obstruction would refute it; the proof method (gluing two positively curved disks) makes a construction for each, so the claim is witnessed constructively.
- **Why it matters**: the essay's postscript §iv records it as a boundary case — with its AI acknowledgment visible from version one [82,83].
- **Status (22 Nov 2026)**: claimed in a preprint (24 September) by Yang-Hui He, Ziran Liu and Shing-Tung Yau, gluing two positively curved 7-disks with matching boundary metrics; the paper's acknowledgment thanks ChatGPT and Claude (present in v1) [82,83]. Follow-up work extends the technique; no community verdict either way.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Two positively curved discs glued along the boundary, and twenty-eight smooth structures">
<title>Two positively curved discs glued along the boundary, and twenty-eight smooth structures</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<path d="M70 110 A 60 60 0 0 1 190 110" fill="none" stroke="#C9852F" stroke-width="2"/>
<path d="M70 110 A 60 60 0 0 0 190 110" fill="none" stroke="#407CB0" stroke-width="2"/>
<line x1="70" y1="110" x2="190" y2="110" stroke="#A4553F" stroke-dasharray="4 4"/>
<line x1="95" y1="78" x2="95" y2="59" stroke="#C9852F" stroke-width="1.3"/>
<polygon points="95,57 92,65 98,65" fill="#C9852F"/>
<line x1="130" y1="66" x2="130" y2="46" stroke="#C9852F" stroke-width="1.3"/>
<polygon points="130,44 127,52 133,52" fill="#C9852F"/>
<line x1="165" y1="78" x2="165" y2="59" stroke="#C9852F" stroke-width="1.3"/>
<polygon points="165,57 162,65 168,65" fill="#C9852F"/>
<line x1="95" y1="142" x2="95" y2="161" stroke="#407CB0" stroke-width="1.3"/>
<polygon points="95,163 92,155 98,155" fill="#407CB0"/>
<line x1="130" y1="154" x2="130" y2="174" stroke="#407CB0" stroke-width="1.3"/>
<polygon points="130,176 127,168 133,168" fill="#407CB0"/>
<line x1="165" y1="142" x2="165" y2="161" stroke="#407CB0" stroke-width="1.3"/>
<polygon points="165,163 162,155 168,155" fill="#407CB0"/>
<text x="130" y="100" text-anchor="middle" font-size="11" fill="#332C23">D⁷ ∪ D⁷</text>
<circle cx="320" cy="66" r="5" fill="#E8A855"/>
<circle cx="320" cy="92" r="5" fill="#407CB0"/>
<circle cx="320" cy="118" r="5" fill="#E8A855"/>
<circle cx="320" cy="144" r="5" fill="#407CB0"/>
<circle cx="346" cy="66" r="5" fill="#407CB0"/>
<circle cx="346" cy="92" r="5" fill="#E8A855"/>
<circle cx="346" cy="118" r="5" fill="#407CB0"/>
<circle cx="346" cy="144" r="5" fill="#E8A855"/>
<circle cx="372" cy="66" r="5" fill="#E8A855"/>
<circle cx="372" cy="92" r="5" fill="#407CB0"/>
<circle cx="372" cy="118" r="5" fill="#E8A855"/>
<circle cx="372" cy="144" r="5" fill="#407CB0"/>
<circle cx="398" cy="66" r="5" fill="#407CB0"/>
<circle cx="398" cy="92" r="5" fill="#E8A855"/>
<circle cx="398" cy="118" r="5" fill="#407CB0"/>
<circle cx="398" cy="144" r="5" fill="#E8A855"/>
<circle cx="424" cy="66" r="5" fill="#E8A855"/>
<circle cx="424" cy="92" r="5" fill="#407CB0"/>
<circle cx="424" cy="118" r="5" fill="#E8A855"/>
<circle cx="424" cy="144" r="5" fill="#407CB0"/>
<circle cx="450" cy="66" r="5" fill="#407CB0"/>
<circle cx="450" cy="92" r="5" fill="#E8A855"/>
<circle cx="450" cy="118" r="5" fill="#407CB0"/>
<circle cx="450" cy="144" r="5" fill="#E8A855"/>
<circle cx="476" cy="66" r="5" fill="#E8A855"/>
<circle cx="476" cy="92" r="5" fill="#407CB0"/>
<circle cx="476" cy="118" r="5" fill="#E8A855"/>
<circle cx="476" cy="144" r="5" fill="#407CB0"/>
<text x="398" y="186" text-anchor="middle" font-size="12" fill="#6B5F4F">28</text>
</g>
</svg>
<figcaption><b>Fig. A7</b> · Schematic: two positively curved discs glued along a matching boundary; the 28 smooth structures of the 7-sphere.</figcaption>
</figure>

### A8 · Matrix multiplication, 4×4 complex: 49 to 48

- **In one line**: how many scalar multiplications are needed to multiply two 4×4 complex matrices?
- **Analogy**: a cooking challenge — multiply two grids of numbers using as few single-number "stirs" as possible. The textbook recipe uses 64 stirs; Strassen (1969) found one with 49; AlphaEvolve found one with 48. One stir saved is compounded enormously when the recipe is scaled up to giant grids. *Boundary*: the real object is a *tensor rank* — the shortest decomposition of the multiplication operator into rank-one pieces — and the analogy says nothing about why 48 is hard to beat.
- **What is asked**: find the smallest known number of scalar multiplications for the 4×4 complex case.
- **Background**: Strassen's 1969 algorithm founded algebraic complexity theory; the record stood for 56 years.
- **Prerequisites**: *tensor rank* counts the minimal number of simple (rank-one) building blocks needed to assemble the multiplication tensor; it is the coordinate-free version of "stirs".
- **Logic and language**: an upper bound is witnessed by an algorithm (build it); a matching lower bound would require excluding all better ones — the record 48 is the best *known* algorithm, not a proven minimum. The logical asymmetry of threshold 3, in the wild.
- **Why it matters**: §1.4 uses it as the emblem of results at the compute-verify end [16].
- **Status (22 Nov 2026)**: 48 (DeepMind's AlphaEvolve, May 2025) still the record; a follow-up re-derives it with rational coefficients only.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Three four by four grids, and bars for 64, 49, 48 scalar multiplications">
<title>Three four by four grids, and bars for 64, 49, 48 scalar multiplications</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="30" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="30" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="30" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="30" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="42" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="42" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="42" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="42" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="54" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="54" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="54" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="54" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="66" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="66" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="66" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="66" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<text x="54" y="60" text-anchor="middle" font-size="12" fill="#332C23" font-weight="600">A</text>
<rect x="120" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="120" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="120" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="120" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="132" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="132" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="132" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="132" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="144" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="144" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="144" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="144" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="156" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="156" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="156" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="156" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<text x="144" y="60" text-anchor="middle" font-size="12" fill="#332C23" font-weight="600">B</text>
<rect x="215" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="215" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="215" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="215" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="227" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="227" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="227" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="227" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="239" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="239" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="239" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="239" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="251" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="251" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="251" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="251" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<text x="239" y="60" text-anchor="middle" font-size="12" fill="#332C23" font-weight="600">C</text>
<text x="108" y="100" text-anchor="middle" font-size="16" fill="#6B5F4F">×</text>
<text x="200" y="100" text-anchor="middle" font-size="16" fill="#6B5F4F">=</text>
<rect x="300" y="70" width="166" height="18" rx="4" fill="#E8A855" opacity=".85"/>
<text x="474.4" y="84" text-anchor="start" font-size="12" fill="#332C23">64</text>
<rect x="300" y="110" width="127" height="18" rx="4" fill="#E8A855" opacity=".85"/>
<text x="435.4" y="124" text-anchor="start" font-size="12" fill="#332C23">49</text>
<rect x="300" y="150" width="124" height="18" rx="4" fill="#C9852F" opacity=".85"/>
<text x="432.8" y="164" text-anchor="start" font-size="12" fill="#332C23">48</text>
<text x="300" y="190" text-anchor="start" font-size="10" fill="#9A8D7A">n×n, n = 4</text>
</g>
</svg>
<figcaption><b>Fig. A8</b> · Schematic: multiplying two 4×4 matrices, and the record count 64 → 49 → 48.</figcaption>
</figure>

### A9 · The kissing number in eleven dimensions

- **In one line**: how many unit spheres can touch a central unit sphere at once, in 11-dimensional space?
- **Analogy**: oranges stacked in a fruit shop: around one central orange, twelve others can touch it (the number Newton and Gregory argued over). In eleven dimensions the "oranges" are 11-dimensional spheres, and we can only bracket the count: at least 593, at most 868. *Boundary*: high-dimensional spheres are not picturable; the analogy carries the counting question, none of the geometry that bounds it.
- **What is asked**: determine the maximum number of non-overlapping unit spheres touching a central one in R^11.
- **Background**: exact values are known only in dimensions 1, 2, 3, 4, 8 and 24 — in dimension 24, 196,560, a number that still stuns.
- **Prerequisites**: "dimension" here is the number of independent directions; a unit sphere is the set of points at distance exactly 1 from a center; "touching" means the distance between centers is exactly 2.
- **Logic and language**: a lower bound comes from one construction (593 — build it); the upper bound 868 comes from an exclusion argument (no arrangement beats it). Two opposite evidence shapes again.
- **Why it matters**: §1.4 pairs it with matrix multiplication as a mechanically checkable record [16].
- **Status (22 Nov 2026)**: 593–868; exact value unknown. A later paper claims 604; not yet reflected in standard references, unverified for this page [16].

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Six unit circles around a central one, and known kissing numbers by dimension">
<title>Six unit circles around a central one, and known kissing numbers by dimension</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<circle cx="120" cy="100" r="28" fill="#F7EFE2" stroke="#C9852F" stroke-width="2"/>
<circle cx="176.0" cy="100.0" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="148.0" cy="148.5" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="92.0" cy="148.5" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="64.0" cy="100.0" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="92.0" cy="51.5" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="148.0" cy="51.5" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<text x="120" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">d = 2</text>
<rect x="412" y="52" width="44" height="58" rx="6" fill="#FBE9C8" stroke="#C9852F" stroke-dasharray="4 3"/>
<text x="235" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">1</text>
<text x="235" y="96" text-anchor="middle" font-size="10" fill="#332C23">2</text>
<text x="272" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">2</text>
<text x="272" y="96" text-anchor="middle" font-size="10" fill="#332C23">6</text>
<text x="309" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">3</text>
<text x="309" y="96" text-anchor="middle" font-size="10" fill="#332C23">12</text>
<text x="346" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">4</text>
<text x="346" y="96" text-anchor="middle" font-size="10" fill="#332C23">24</text>
<text x="390" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">8</text>
<text x="390" y="96" text-anchor="middle" font-size="10" fill="#332C23">240</text>
<text x="434" y="70" text-anchor="middle" font-size="10" fill="#A4553F">11</text>
<text x="434" y="96" text-anchor="middle" font-size="9" fill="#A4553F">593–868</text>
<text x="478" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">24</text>
<text x="478" y="96" text-anchor="middle" font-size="10" fill="#332C23">196560</text>
<text x="200" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">d</text>
</g>
</svg>
<figcaption><b>Fig. A9</b> · Schematic: six unit circles around a central one (2-D), and the known kissing numbers — dimension 11 is still a bracket.</figcaption>
</figure>

### A10 · Nine-loop hexagon amplitudes (and a single-minus aside)

- **In one line**: compute a fearsomely complex scattering amplitude in the toy model of quantum field theory — nine quantum loops deep.
- **Analogy**: a scattering amplitude is nature's receipt for a particle collision — the probability printout. "Nine loops" means the receipt has nine nested layers of corrections, each layer summing over virtual particles. The *bootstrap* method is the jigsaw played backwards: instead of computing forward, you nail down so many consistency conditions (symmetries, limits) that the answer is forced. *Boundary*: the receipt picture hides why nine loops was a frontier — the expressions explode combinatorially.
- **What is asked**: compute the nine-loop hexagon amplitude (aside: decide whether a certain one-minus gluon tree amplitude is nonzero).
- **Background**: planar N=4 super Yang–Mills is the "hydrogen atom" of field theory; the eight-loop record was set by Lance Dixon and Andy Liu in 2023.
- **Prerequisites**: a *tree amplitude* is the no-virtual-particle-loops case; "single-minus" names the helicity configuration; the *form factor* is a cousin quantity used as an independent route.
- **Logic and language**: the aside's statement — "these amplitudes are nonzero" — is an existence claim witnessed by an explicit formula; the 2026 preprint reports the formula first conjectured by GPT-5.2 Pro, then proved by an OpenAI internal model [23].
- **Why it matters**: §1.7 reads the two 2026 physics cases as live specimens of machine-executed-recipe versus machine-proposed-conjecture [23,24].
- **Status (22 Nov 2026)**: Anthropic announced (25 September) Claude computing the nine-loop amplitude, validated independently by Dixon over roughly two weeks; a CAS team led by Song He obtained most of the result concurrently, using GPT-6 for part of the constraints [24].

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A hexagon amplitude with nine loops, and the eight to nine loop record">
<title>A hexagon amplitude with nine loops, and the eight to nine loop record</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<polygon points="185.0,100.0 157.5,147.6 102.5,147.6 75.0,100.0 102.5,52.4 157.5,52.4" fill="none" stroke="#C9852F" stroke-width="2"/>
<line x1="185.0" y1="100.0" x2="211.0" y2="100.0" stroke="#407CB0" stroke-width="1.6"/>
<line x1="157.5" y1="147.6" x2="170.5" y2="170.1" stroke="#407CB0" stroke-width="1.6"/>
<line x1="102.5" y1="147.6" x2="89.5" y2="170.1" stroke="#407CB0" stroke-width="1.6"/>
<line x1="75.0" y1="100.0" x2="49.0" y2="100.0" stroke="#407CB0" stroke-width="1.6"/>
<line x1="102.5" y1="52.4" x2="89.5" y2="29.9" stroke="#407CB0" stroke-width="1.6"/>
<line x1="157.5" y1="52.4" x2="170.5" y2="29.9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="105" cy="80" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="105" cy="100" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="105" cy="120" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="130" cy="80" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="130" cy="100" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="130" cy="120" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="155" cy="80" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="155" cy="100" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="155" cy="120" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<text x="130" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">L = 9</text>
<rect x="300" y="76" width="144" height="18" rx="4" fill="#E8A855" opacity=".85"/>
<text x="300" y="70" text-anchor="start" font-size="11" fill="#332C23">8 · 2023</text>
<rect x="300" y="122" width="162" height="18" rx="4" fill="#C9852F" opacity=".85"/>
<text x="300" y="116" text-anchor="start" font-size="11" fill="#332C23">9 · 2026</text>
</g>
</svg>
<figcaption><b>Fig. A10</b> · Schematic: a hexagon amplitude with nine loops, and the 8 → 9 loop record.</figcaption>
</figure>

### A11 · First Proof: ten research-level questions

- **In one line**: can a machine solve problems its own examiners care about?
- **Analogy**: not an olympiad with polished puzzles, but a plumber summoned to the examiner's own house — ten real leaks from eleven researchers' actual work. *Boundary*: the analogy misses the point that the leaks were *chosen*; the challenge's design (and the missing evaluation protocol) is the real story.
- **What is asked**: how many of the ten can machine-generated answers settle — and who can tell?
- **Background**: a 2026 challenge organized by eleven research mathematicians, deliberately not contest problems, not benchmarks written to be solved.
- **Prerequisites**: none beyond the essay's §1.1 framework — the challenge's crux is institutional: who grades, under what protocol.
- **Logic and language**: "research-level" is not a well-defined class; the challenge makes it concrete by construction — ten named questions, each with an owner who knows what an answer would have to do.
- **Why it matters**: §1.6 and §6.4 use it as the cleanest statement of the verification bottleneck [22].
- **Status (22 Nov 2026)**: the generation half stands; the evaluation half remains unfinished public business, and the organizers concede no protocol yet exists for measuring autonomous problem-posing [22].

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Ten research questions, a machine answer, and an open evaluation gate">
<title>Ten research questions, a machine answer, and an open evaluation gate</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="24" y="44" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="49" y="59" text-anchor="middle" font-size="10" fill="#6B5F4F">1</text>
<rect x="82" y="44" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="107" y="59" text-anchor="middle" font-size="10" fill="#6B5F4F">6</text>
<rect x="24" y="72" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="49" y="87" text-anchor="middle" font-size="10" fill="#6B5F4F">2</text>
<rect x="82" y="72" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="107" y="87" text-anchor="middle" font-size="10" fill="#6B5F4F">7</text>
<rect x="24" y="100" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="49" y="115" text-anchor="middle" font-size="10" fill="#6B5F4F">3</text>
<rect x="82" y="100" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="107" y="115" text-anchor="middle" font-size="10" fill="#6B5F4F">8</text>
<rect x="24" y="128" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="49" y="143" text-anchor="middle" font-size="10" fill="#6B5F4F">4</text>
<rect x="82" y="128" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="107" y="143" text-anchor="middle" font-size="10" fill="#6B5F4F">9</text>
<rect x="24" y="156" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="49" y="171" text-anchor="middle" font-size="10" fill="#6B5F4F">5</text>
<rect x="82" y="156" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="107" y="171" text-anchor="middle" font-size="10" fill="#6B5F4F">10</text>
<text x="76" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">10</text>
<line x1="146" y1="100" x2="182" y2="100" stroke="#6B5F4F" stroke-width="1.6"/>
<polygon points="190,100 180,96 180,104" fill="#6B5F4F"/>
<rect x="196" y="70" width="86" height="60" rx="8" fill="#F7EFE2" stroke="#C9852F"/>
<text x="239" y="105" text-anchor="middle" font-size="12" fill="#332C23" font-weight="600">AI</text>
<line x1="288" y1="100" x2="322" y2="100" stroke="#6B5F4F" stroke-width="1.6"/>
<polygon points="330,100 320,96 320,104" fill="#6B5F4F"/>
<rect x="336" y="66" width="120" height="68" rx="8" fill="#FBE9C8" stroke="#A4553F" stroke-dasharray="5 4"/>
<text x="396" y="106" text-anchor="middle" font-size="22" fill="#A4553F">?</text>
<text x="396" y="84" text-anchor="middle" font-size="10" fill="#A4553F">0 / 10</text>
</g>
</svg>
<figcaption><b>Fig. A11</b> · Schematic: ten questions, a machine answer, and the missing evaluation protocol.</figcaption>
</figure>

## Group B · The background

### B1 · Gödel's incompleteness theorems (1931)

- **In one line**: any consistent system rich enough for arithmetic contains true statements it cannot prove — and cannot certify its own consistency.
- **Analogy**: a court system in which some cases can only be settled by a higher court — and no court, including the supreme one, can rule on its own impartiality within its own rules. *Boundary and the common misreading*: Gödel did not show mathematics is unreliable, nor that some truths are forever unknowable; he showed *self-certification* has a bound — every given rulebook leaves cases it cannot decide, and the proof is a construction, not a mysticism.
- **What is asked** (answered): are there mechanical limits to formal proof? Yes — §3.3 leans on it against "mathematics as ultimate ground", §5.4 on Penrose's contested use of it [42,43,44].
- **Prerequisites**: a *formal system* is a rulebook plus a proof-checking procedure; *consistent* means no contradiction is derivable; *arithmetically rich* means it can express statements about whole numbers.
- **Logic and language**: the proof encodes a self-referential sentence — "this statement is not provable here" — inside arithmetic; the linguistic machinery (Gödel numbering) is what lets a rulebook talk about itself.
- **Status**: settled mathematics; the philosophical arguments built on it remain contested.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A formal system containing a true statement it cannot prove">
<title>A formal system containing a true statement it cannot prove</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="24" y="40" width="220" height="120" rx="10" fill="#FFFDF9" stroke="#6B5F4F" stroke-width="1.6"/>
<text x="40" y="62" text-anchor="start" font-size="12" fill="#332C23" font-weight="600">S</text>
<line x1="46" y1="82" x2="150" y2="82" stroke="#EBDCC4" stroke-width="2"/>
<line x1="46" y1="98" x2="150" y2="98" stroke="#EBDCC4" stroke-width="2"/>
<line x1="46" y1="114" x2="150" y2="114" stroke="#EBDCC4" stroke-width="2"/>
<line x1="46" y1="130" x2="150" y2="130" stroke="#EBDCC4" stroke-width="2"/>
<rect x="160" y="86" width="56" height="34" rx="6" fill="#FBE9C8" stroke="#C9852F"/>
<text x="188" y="108" text-anchor="middle" font-size="12" fill="#332C23" font-weight="600">G</text>
<path d="M216 96 C 250 70, 250 128, 216 110" fill="none" stroke="#A4553F" stroke-dasharray="4 3"/>
<line x1="244" y1="100" x2="300" y2="100" stroke="#A4553F" stroke-dasharray="4 3"/>
<polygon points="308,100 298,96 298,104" fill="#A4553F"/>
<text x="318" y="96" text-anchor="start" font-size="12" fill="#A4553F">S ⊬ G</text>
<text x="318" y="124" text-anchor="start" font-size="12" fill="#A4553F">S ⊬ Con(S)</text>
<text x="318" y="152" text-anchor="start" font-size="11" fill="#6B5F4F">G ⊨ ⊤</text>
</g>
</svg>
<figcaption><b>Fig. B1</b> · Schematic: inside the system S there is a true sentence G it cannot prove, and it cannot prove its own consistency.</figcaption>
</figure>

### B2 · The halting problem (1936)

- **In one line**: no algorithm can decide, for every program and input, whether the program eventually stops.
- **Analogy**: imagine a universal spoiler program that predicts, for every film, whether it ends. Feed it a film built to end exactly when the spoiler says it will not — contradiction. The film is a program fed its own description. *Boundary*: the paradox is airtight as logic; it says nothing about any particular program, most of which are easy to analyze.
- **What is asked** (answered): is there a universal mechanical decision procedure for this well-defined question? No [48].
- **Logic and language**: the proof is diagonal — one constructed counterexample against a universal claim; the same for-all/existential shape as threshold 3.
- **Why it matters**: with Gödel, it closes the "formalization can exhaust mathematics" hope — §3.5 and §5.4 [48].
- **Status**: settled; the boundary between decidable and undecidable remains an active map.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A halting decider fed its own description, and the contradiction">
<title>A halting decider fed its own description, and the contradiction</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="70" y="66" width="96" height="68" rx="10" fill="#FFFDF9" stroke="#6B5F4F" stroke-width="1.6"/>
<text x="118" y="106" text-anchor="middle" font-size="20" fill="#332C23" font-weight="600">H</text>
<line x1="24" y1="100" x2="62" y2="100" stroke="#6B5F4F" stroke-width="1.6"/>
<polygon points="70,100 60,96 60,104" fill="#6B5F4F"/>
<text x="44" y="90" text-anchor="middle" font-size="11" fill="#6B5F4F">⟨H,H⟩</text>
<line x1="166" y1="88" x2="216" y2="72" stroke="#6B5F4F" stroke-width="1.6"/>
<polygon points="224,70 213,68 216,76" fill="#6B5F4F"/>
<text x="236" y="70" text-anchor="start" font-size="16" fill="#6B5F4F">↓</text>
<line x1="166" y1="112" x2="216" y2="128" stroke="#6B5F4F" stroke-width="1.6"/>
<polygon points="224,130 213,132 216,124" fill="#6B5F4F"/>
<text x="236" y="136" text-anchor="start" font-size="16" fill="#6B5F4F">∞</text>
<path d="M270 140 C 320 190, 20 190, 44 118" fill="none" stroke="#A4553F" stroke-width="1.6" stroke-dasharray="5 4"/>
<text x="160" y="186" text-anchor="middle" font-size="18" fill="#A4553F">⊥</text>
</g>
</svg>
<figcaption><b>Fig. B2</b> · Schematic: the halting decider fed its own description — either output contradicts the other.</figcaption>
</figure>

### B3 · The continuum hypothesis

- **In one line**: is there a size of infinity strictly between the integers' and the continuum's?
- **Analogy**: an infinite hotel whose floors are sizes of infinity: the integers occupy one floor, the real-number continuum a much higher one. CH asks whether any habitable floor lies strictly between. Cohen's result: the building code (the axioms) licenses blueprints with the floor and without it — neither blueprint contradicts the code. *Boundary*: sizes of infinity are not floors of one tower; the hierarchy is subtler than a building.
- **What is asked** (answered): Cantor, 1878; Gödel (1940) showed it cannot be disproved from the axioms; Cohen (1963) that it cannot be proved — independent.
- **Logic and language**: "independent" here is a theorem *about the logic*, proved by constructing two model universes, one where CH holds and one where it fails [45].
- **Why it matters**: §3.3 uses it to show even the most foundational branch has axiomatic choices not uniquely forced.
- **Status**: settled as independence; adopting CH is a stance, not a fact.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A gap between aleph-null and the continuum, and two consistent models">
<title>A gap between aleph-null and the continuum, and two consistent models</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<line x1="110" y1="176" x2="110" y2="36" stroke="#6B5F4F" stroke-width="1.6"/>
<line x1="92" y1="168" x2="128" y2="168" stroke="#6B5F4F" stroke-width="1.6"/>
<line x1="92" y1="48" x2="128" y2="48" stroke="#6B5F4F" stroke-width="1.6"/>
<line x1="92" y1="108" x2="128" y2="108" stroke="#A4553F" stroke-dasharray="4 4"/>
<text x="84" y="172" text-anchor="end" font-size="12" fill="#332C23">ℵ₀</text>
<text x="84" y="52" text-anchor="end" font-size="12" fill="#332C23">2^ℵ₀</text>
<text x="84" y="112" text-anchor="end" font-size="16" fill="#A4553F">?</text>
<text x="110" y="30" text-anchor="middle" font-size="12" fill="#A4553F">CH</text>
<rect x="240" y="62" width="96" height="54" rx="8" fill="#FFFDF9" stroke="#6B5F4F"/>
<text x="288" y="86" text-anchor="middle" font-size="12" fill="#332C23">CH</text>
<text x="288" y="106" text-anchor="middle" font-size="12" fill="#6B5F4F">✓</text>
<rect x="356" y="62" width="96" height="54" rx="8" fill="#FFFDF9" stroke="#6B5F4F"/>
<text x="404" y="86" text-anchor="middle" font-size="12" fill="#332C23">¬CH</text>
<text x="404" y="106" text-anchor="middle" font-size="12" fill="#6B5F4F">✓</text>
<text x="346" y="146" text-anchor="middle" font-size="11" fill="#9A8D7A">ZFC</text>
</g>
</svg>
<figcaption><b>Fig. B3</b> · Schematic: the gap between ℵ₀ and 2^ℵ₀; both CH and ¬CH are consistent with the axioms.</figcaption>
</figure>

### B4 · Russell's paradox (1901)

- **In one line**: the set of all sets that do not contain themselves — contains itself or not?
- **Analogy**: the village barber who shaves exactly those who do not shave themselves: who shaves the barber? Or the catalogue of all catalogues that do not list themselves. Either answer breaks the rule that defined it. *Boundary*: the barber has a trivial escape (nobody shaves him); the set version has none, because the definition, not the person, is broken — the escape is to rebuild the rules.
- **What is asked** (answered): Russell's letter to Frege punctured naive set theory; type theory and axiomatic set theory rebuilt the ground.
- **Logic and language**: a self-reference defect in a definition — the linguistic side of threshold 2: a grammatical sentence can be semantically bankrupt.
- **Why it matters**: §3.1 uses it to mark logicism's failure — logic is mathematics' grammar, not its ground [36].
- **Status**: resolved; the lesson is a fixture of foundations.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="The set of all sets that do not contain themselves, and its contradiction">
<title>The set of all sets that do not contain themselves, and its contradiction</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<circle cx="120" cy="100" r="50" fill="#F7EFE2" stroke="#C9852F" stroke-width="1.8"/>
<text x="120" y="106" text-anchor="middle" font-size="18" fill="#332C23" font-weight="600">R</text>
<path d="M148 66 C 190 40, 210 96, 160 110" fill="none" stroke="#A4553F" stroke-width="1.6"/>
<polygon points="154,108 166,108 160,118" fill="#A4553F"/>
<text x="196" y="60" text-anchor="middle" font-size="12" fill="#A4553F">R ∈ R ?</text>
<text x="262" y="78" text-anchor="start" font-size="12" fill="#332C23">R ∈ R ⇒ R ∉ R</text>
<text x="262" y="104" text-anchor="start" font-size="12" fill="#332C23">R ∉ R ⇒ R ∈ R</text>
<text x="262" y="140" text-anchor="start" font-size="20" fill="#A4553F">⊥</text>
</g>
</svg>
<figcaption><b>Fig. B4</b> · Schematic: the set of all sets that do not contain themselves — either answer breaks the definition.</figcaption>
</figure>

### B5 · The Kepler conjecture

- **In one line**: the grocer's stacking of cannonballs is the densest way to pack equal spheres.
- **Analogy**: the fruit stall. Kepler guessed it in 1611; the stallholders' practice was ahead of the theorem for four centuries. *Boundary*: the conjecture is about *infinite* space and *all* conceivable packings — not just the neat ones a stall can show; that universality is what made the proof take 400 years and, finally, a computer.
- **What is asked** (answered): Thomas Hales announced a proof in 1998; referees "99% certain"; the machine-checked Flyspeck proof was completed 2014, published 2017.
- **Prerequisites**: *packing density* is the fraction of space occupied, maximized over all arrangements.
- **Why it matters**: §5.3 cites the verification labor as the price tag for professional verification — labor still among the discipline's worst paid [66].
- **Status**: proved, machine-checked; historically the first major theorem certified this way.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Hexagonal close packing cross-section and the proof timeline">
<title>Hexagonal close packing cross-section and the proof timeline</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<circle cx="130" cy="100" r="26" fill="#F7EFE2" stroke="#C9852F" stroke-width="1.8"/>
<circle cx="182.0" cy="100.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<circle cx="156.0" cy="145.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<circle cx="104.0" cy="145.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<circle cx="78.0" cy="100.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<circle cx="104.0" cy="55.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<circle cx="156.0" cy="55.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<polygon points="156,115 130,130 104,115 104,85 130,70 156,85" fill="none" stroke="#A4553F" stroke-dasharray="4 3"/>
<text x="130" y="190" text-anchor="middle" font-size="12" fill="#332C23">π / (3√2) ≈ 0.7405</text>
<line x1="270" y1="100" x2="500" y2="100" stroke="#EBDCC4"/>
<circle cx="300" cy="100" r="4" fill="#C9852F"/>
<text x="300" y="124" text-anchor="middle" font-size="10" fill="#6B5F4F">1611</text>
<circle cx="380" cy="100" r="4" fill="#C9852F"/>
<text x="380" y="124" text-anchor="middle" font-size="10" fill="#6B5F4F">1998</text>
<circle cx="460" cy="100" r="4" fill="#C9852F"/>
<text x="460" y="124" text-anchor="middle" font-size="10" fill="#6B5F4F">2014</text>
</g>
</svg>
<figcaption><b>Fig. B5</b> · Schematic: the hexagonal cross-section of the densest packing, density π/(3√2) ≈ 0.7405, and the proof timeline.</figcaption>
</figure>

### B6 · The Robbins problem

- **In one line**: do three simple equations about a boolean operation capture all of boolean algebra?
- **Analogy**: can three tent-poles hold up the whole dome of switching logic? The poles look too few — that was the fun, and the difficulty: sixty years of hands failed to prove either the poles suffice or that they do not. In 1996 William McCune's automated prover EQP found the proof. *Boundary*: the dome picture suggests size; the actual difficulty was finding the right intermediate lemma — a search, which is exactly what machines are good at.
- **What is asked** (answered): Herbert Robbins, 1933; settled by EQP in 1996 [65].
- **Logic and language**: an equivalence claim — "these axioms define exactly boolean algebra" — requires two proofs: everything boolean follows from the three, and the three hold in boolean algebra.
- **Why it matters**: §5.3 cites it in the lineage of machines absorbing the checking and the executing, humans moving on.
- **Status**: proved by machine — the precedent the AI-mathematics wave extends one layer up.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Three axiom poles holding up the dome of Boolean algebra">
<title>Three axiom poles holding up the dome of Boolean algebra</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<path d="M70 92 Q 160 34 250 92" fill="none" stroke="#C9852F" stroke-width="2"/>
<line x1="100" y1="150" x2="100" y2="76" stroke="#6B5F4F" stroke-width="2.4"/>
<text x="100" y="168" text-anchor="middle" font-size="10" fill="#6B5F4F">A1</text>
<line x1="160" y1="150" x2="160" y2="63" stroke="#6B5F4F" stroke-width="2.4"/>
<text x="160" y="168" text-anchor="middle" font-size="10" fill="#6B5F4F">A2</text>
<line x1="220" y1="150" x2="220" y2="76" stroke="#6B5F4F" stroke-width="2.4"/>
<text x="220" y="168" text-anchor="middle" font-size="10" fill="#6B5F4F">A3</text>
<text x="160" y="58" text-anchor="middle" font-size="12" fill="#332C23">B</text>
<text x="40" y="168" text-anchor="start" font-size="10" fill="#9A8D7A">1933</text>
<text x="280" y="168" text-anchor="start" font-size="10" fill="#9A8D7A">1996</text>
<line x1="24" y1="150" x2="300" y2="150" stroke="#EBDCC4"/>
</g>
</svg>
<figcaption><b>Fig. B6</b> · Schematic: three axiom poles holding up the dome of Boolean algebra.</figcaption>
</figure>

### B7 · Bounded gaps between primes (and Chen's theorem)

- **In one line**: how small a gap between consecutive primes occurs infinitely often?
- **Analogy**: primes as buses that stop at unpredictable times. Zhang proved (2014): there is *some* finite interval — his was 70 million — inside which two buses stop together, infinitely often. The Polymath project and Maynard shrank the interval to 246; by August 2026 it stands at 240 (Stadlmann, arXiv:2608.31126). The twin-prime conjecture is the same claim with interval 2 — still open. Chen's theorem (1973) is a neighboring triumph: every large even number is a prime plus a product of at most two primes ("1+2"). *Boundary*: "infinitely often" is about the whole infinite line, not any stretch you can walk.
- **What is asked**: the smallest H₁ such that infinitely many prime pairs differ by at most H₁.
- **Prerequisites**: "infinitely often" is the quantifier shape — not "there are many", but "no matter how far out you go, they keep happening".
- **Why it matters**: §4.2 and §6.2 cite the lineage as sieve methods and additive combinatorics alive [57,58,72]. Related entry: [Goldbach & twin primes](../famous_problems/goldbach_and_twin_primes.md).
- **Status (22 Nov 2026)**: record 240 (Stadlmann); twin primes open.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Primes on a line, a twin gap of two, and a bounded gap of 240">
<title>Primes on a line, a twin gap of two, and a bounded gap of 240</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<line x1="20" y1="110" x2="500" y2="110" stroke="#6B5F4F"/>
<line x1="30" y1="104" x2="30" y2="116" stroke="#6B5F4F"/>
<text x="30" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">2</text>
<line x1="75" y1="104" x2="75" y2="116" stroke="#6B5F4F"/>
<text x="75" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">3</text>
<line x1="120" y1="104" x2="120" y2="116" stroke="#6B5F4F"/>
<text x="120" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">5</text>
<line x1="165" y1="104" x2="165" y2="116" stroke="#6B5F4F"/>
<text x="165" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">7</text>
<line x1="210" y1="104" x2="210" y2="116" stroke="#6B5F4F"/>
<text x="210" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">11</text>
<line x1="255" y1="104" x2="255" y2="116" stroke="#6B5F4F"/>
<text x="255" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">13</text>
<line x1="300" y1="104" x2="300" y2="116" stroke="#6B5F4F"/>
<text x="300" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">17</text>
<line x1="345" y1="104" x2="345" y2="116" stroke="#6B5F4F"/>
<text x="345" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">19</text>
<line x1="390" y1="104" x2="390" y2="116" stroke="#6B5F4F"/>
<text x="390" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">23</text>
<line x1="435" y1="104" x2="435" y2="116" stroke="#6B5F4F"/>
<text x="435" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">29</text>
<line x1="480" y1="104" x2="480" y2="116" stroke="#6B5F4F"/>
<text x="480" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">31</text>
<path d="M210 96 L210 88 L255 88 L255 96" fill="none" stroke="#A4553F"/>
<text x="232" y="80" text-anchor="middle" font-size="10" fill="#A4553F">2</text>
<path d="M300 62 L300 52 L480 52 L480 62" fill="none" stroke="#C9852F" stroke-dasharray="4 3"/>
<text x="390" y="44" text-anchor="middle" font-size="12" fill="#C9852F">≤ 240</text>
<text x="390" y="176" text-anchor="middle" font-size="14" fill="#9A8D7A">∞</text>
</g>
</svg>
<figcaption><b>Fig. B7</b> · Schematic: primes on a line; a twin gap of 2 and the bounded gap of 240, which occurs infinitely often.</figcaption>
</figure>

### B8 · The Weil conjectures

- **In one line**: count solutions of polynomial equations over finite fields, and find deep topology hiding in the arithmetic.
- **Analogy**: counting chess positions on a finite board, over and over, for growing board sizes — and discovering that the counts' *rhythm* is governed by hidden "holes and handles" of a shape you never see. Weil conjectured the rhythm follows a zeta-like function with Riemann-hypothesis-flavored regularity; Deligne proved the hardest part in 1974. *Boundary*: the "hidden shape" is an algebraic variety, not a board; the analogy is why people call the result "topology speaking through arithmetic".
- **What is asked** (answered): André Weil, 1949; Deligne proved the last and hardest part (a Riemann hypothesis over finite fields) in 1974 [56].
- **Prerequisites**: a *finite field* is arithmetic with a fixed alphabet size where every operation wraps around (clock arithmetic generalized); the *zeta function of a variety* is the generating device that encodes the counts for every board size at once — a geometric cousin of A4's ζ.
- **Why it matters**: §4.2 cites Deligne's proof as the landmark of arithmetic geometry, the territory around the Langlands program.
- **Status**: proved; its descendants (geometric Langlands) remain among the deepest active territories.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Point counts over finite fields and a torus with its Betti numbers">
<title>Point counts over finite fields and a torus with its Betti numbers</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<circle cx="40" cy="60" r="3" fill="#EBDCC4"/>
<circle cx="40" cy="86" r="3" fill="#EBDCC4"/>
<circle cx="40" cy="112" r="3" fill="#EBDCC4"/>
<circle cx="40" cy="138" r="3" fill="#EBDCC4"/>
<circle cx="40" cy="164" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="60" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="86" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="112" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="138" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="164" r="3" fill="#EBDCC4"/>
<circle cx="92" cy="60" r="3" fill="#EBDCC4"/>
<circle cx="92" cy="86" r="3" fill="#EBDCC4"/>
<circle cx="92" cy="112" r="3" fill="#EBDCC4"/>
<circle cx="92" cy="138" r="3" fill="#EBDCC4"/>
<circle cx="92" cy="164" r="3" fill="#EBDCC4"/>
<circle cx="118" cy="60" r="3" fill="#EBDCC4"/>
<circle cx="118" cy="86" r="3" fill="#EBDCC4"/>
<circle cx="118" cy="112" r="3" fill="#EBDCC4"/>
<circle cx="118" cy="138" r="3" fill="#EBDCC4"/>
<circle cx="118" cy="164" r="3" fill="#EBDCC4"/>
<circle cx="144" cy="60" r="3" fill="#EBDCC4"/>
<circle cx="144" cy="86" r="3" fill="#EBDCC4"/>
<circle cx="144" cy="112" r="3" fill="#EBDCC4"/>
<circle cx="144" cy="138" r="3" fill="#EBDCC4"/>
<circle cx="144" cy="164" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="86" r="5" fill="#C9852F"/>
<circle cx="118" cy="86" r="5" fill="#C9852F"/>
<circle cx="66" cy="138" r="5" fill="#C9852F"/>
<circle cx="144" cy="164" r="5" fill="#C9852F"/>
<text x="90" y="196" text-anchor="middle" font-size="12" fill="#332C23">N₁ N₂ …</text>
<ellipse cx="360" cy="104" rx="86" ry="46" fill="none" stroke="#407CB0" stroke-width="2"/>
<ellipse cx="360" cy="104" rx="30" ry="14" fill="none" stroke="#407CB0" stroke-width="2"/>
<text x="360" y="176" text-anchor="middle" font-size="11" fill="#332C23">b: 1 · 2 · 1</text>
<text x="360" y="40" text-anchor="middle" font-size="12" fill="#C9852F">Z(V, t)</text>
</g>
</svg>
<figcaption><b>Fig. B8</b> · Schematic: point counts over finite fields feeding a zeta function; the shape's holes (Betti numbers) govern the rhythm.</figcaption>
</figure>

### B9 · Pi, Liu Hui and Zu Chongzhi

- **In one line**: how precisely can the circle's ratio be computed — and by which method?
- **Analogy**: fence a circle with straight fences: a hexagon, then a 12-gon, then 24 — Liu Hui's "cut-circle" method, each cut hugging the roundness closer. Zu Chongzhi (5th century) pushed to 355/113: on the Earth's circumference, the error is under eleven meters. Europe reached that precision a millennium later. *Boundary*: the fence picture shows *upper and lower* bounds closing in; the deeper point of §5.5 is methodological — the same truth, reached by an algorithmic path with different ideas about what counts as a solution.
- **What is asked** (answered): π is irrational and transcendental; the historiographical question — which traditions, which methods — is the essay's [50,69].
- **Why it matters**: §5.5 cites the Chinese tradition as an algorithmic, constructive path — different in what warrants a solution, not in what is true.
- **Status**: computed to trillions of digits; the essay's historiographical point stands.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Inscribed and circumscribed hexagons closing on the circle">
<title>Inscribed and circumscribed hexagons closing on the circle</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<circle cx="140" cy="100" r="60" fill="none" stroke="#6B5F4F" stroke-width="2"/>
<polygon points="200.0,100.0 170.0,152.0 110.0,152.0 80.0,100.0 110.0,48.0 170.0,48.0" fill="none" stroke="#407CB0" stroke-dasharray="5 4"/>
<polygon points="200.0,134.6 140.0,169.3 80.0,134.6 80.0,65.4 140.0,30.7 200.0,65.4" fill="none" stroke="#C9852F" stroke-dasharray="2 4"/>
<text x="140" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">n = 6</text>
<text x="280" y="74" text-anchor="start" font-size="11" fill="#332C23">3.14159265…</text>
<text x="280" y="100" text-anchor="start" font-size="11" fill="#C9852F">355/113</text>
<text x="280" y="126" text-anchor="start" font-size="11" fill="#6B5F4F">= 3.14159292…</text>
</g>
</svg>
<figcaption><b>Fig. B9</b> · Schematic: inscribed and circumscribed hexagons closing on the circle; 355/113 as the classical bound.</figcaption>
</figure>

### B10 · The Kerala school's infinite series

- **In one line**: power series for sine, cosine and π — laid down in India centuries before Newton and Leibniz.
- **Analogy**: a recipe that builds a rounded shape from infinitely many simple strips — the "recipe" is the series; the Kerala school (Madhava and successors, 14th–16th centuries) wrote down recipes for sine, cosine and π long before Europe's, but did not assemble them into the general-purpose machine later called calculus. *Boundary*: the recipe picture must not suggest the results were "the same but earlier" in institutional terms — §5.5's point is precisely that the machine and the recipes are different achievements.
- **What is asked** (answered): historically established; the essay uses it against the "modern Western mathematics = mathematics as such" equation [50,70].
- **Logic and language**: an infinite series is a claim with a limit in it — "the partial sums approach…"; the linguistic care (approach to what, at what speed) is exactly the grammar threshold 2 teaches.
- **Why it matters**: §5.5 cites Kerala as evidence that the same mathematics can grow in more than one institutional shape.
- **Status**: historically established.

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Sine and its successive partial sums from the power series">
<title>Sine and its successive partial sums from the power series</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<line x1="40" y1="110" x2="480" y2="110" stroke="#EBDCC4"/>
<line x1="260" y1="40" x2="260" y2="180" stroke="#EBDCC4"/>
<polyline points="60.0,267.1 66.7,261.8 73.3,256.6 80.0,251.4 86.7,246.1 93.3,240.9 100.0,235.7 106.7,230.4 113.3,225.2 120.0,220.0 126.7,214.7 133.3,209.5 140.0,204.2 146.7,199.0 153.3,193.8 160.0,188.5 166.7,183.3 173.3,178.1 180.0,172.8 186.7,167.6 193.3,162.4 200.0,157.1 206.7,151.9 213.3,146.7 220.0,141.4 226.7,136.2 233.3,130.9 240.0,125.7 246.7,120.5 253.3,115.2 260.0,110.0 266.7,104.8 273.3,99.5 280.0,94.3 286.7,89.1 293.3,83.8 300.0,78.6 306.7,73.3 313.3,68.1 320.0,62.9 326.7,57.6 333.3,52.4 340.0,47.2 346.7,41.9 353.3,36.7 360.0,31.5 366.7,26.2 373.3,21.0 380.0,15.8 386.7,10.5 393.3,5.3 400.0,0.0 406.7,-5.2 413.3,-10.4 420.0,-15.7 426.7,-20.9 433.3,-26.1 440.0,-31.4 446.7,-36.6 453.3,-41.8 460.0,-47.1" fill="none" stroke="#6B5F4F" stroke-width="1.2" stroke-dasharray="2 5"/>
<polyline points="60.0,8.7 66.7,28.4 73.3,46.5 80.0,63.0 86.7,77.9 93.3,91.4 100.0,103.4 106.7,114.0 113.3,123.3 120.0,131.3 126.7,138.2 133.3,143.8 140.0,148.4 146.7,152.0 153.3,154.6 160.0,156.2 166.7,157.0 173.3,157.0 180.0,156.3 186.7,154.9 193.3,152.8 200.0,150.1 206.7,147.0 213.3,143.4 220.0,139.3 226.7,135.0 233.3,130.3 240.0,125.4 246.7,120.4 253.3,115.2 260.0,110.0 266.7,104.8 273.3,99.6 280.0,94.6 286.7,89.7 293.3,85.0 300.0,80.7 306.7,76.6 313.3,73.0 320.0,69.9 326.7,67.2 333.3,65.1 340.0,63.7 346.7,63.0 353.3,63.0 360.0,63.8 366.7,65.4 373.3,68.0 380.0,71.6 386.7,76.2 393.3,81.8 400.0,88.7 406.7,96.7 413.3,106.0 420.0,116.6 426.7,128.6 433.3,142.1 440.0,157.0 446.7,173.5 453.3,191.6 460.0,211.3" fill="none" stroke="#407CB0" stroke-width="1.6" stroke-dasharray="5 4"/>
<polyline points="60.0,136.2 66.7,136.1 73.3,136.8 80.0,138.3 86.7,140.3 93.3,142.6 100.0,145.2 106.7,147.8 113.3,150.3 120.0,152.8 126.7,155.0 133.3,156.8 140.0,158.4 146.7,159.4 153.3,160.1 160.0,160.2 166.7,159.9 173.3,159.0 180.0,157.6 186.7,155.7 193.3,153.3 200.0,150.5 206.7,147.2 213.3,143.5 220.0,139.4 226.7,135.0 233.3,130.3 240.0,125.5 246.7,120.4 253.3,115.2 260.0,110.0 266.7,104.8 273.3,99.6 280.0,94.5 286.7,89.7 293.3,85.0 300.0,80.6 306.7,76.5 313.3,72.8 320.0,69.5 326.7,66.7 333.3,64.3 340.0,62.4 346.7,61.0 353.3,60.1 360.0,59.8 366.7,59.9 373.3,60.6 380.0,61.6 386.7,63.2 393.3,65.0 400.0,67.2 406.7,69.7 413.3,72.2 420.0,74.8 426.7,77.4 433.3,79.7 440.0,81.7 446.7,83.2 453.3,83.9 460.0,83.8" fill="none" stroke="#C9852F" stroke-width="1.6" stroke-dasharray="8 3 2 3"/>
<polyline points="60.0,110.0 66.7,115.2 73.3,120.4 80.0,125.5 86.7,130.3 93.3,135.0 100.0,139.4 106.7,143.5 113.3,147.2 120.0,150.5 126.7,153.3 133.3,155.7 140.0,157.6 146.7,158.9 153.3,159.7 160.0,160.0 166.7,159.7 173.3,158.9 180.0,157.6 186.7,155.7 193.3,153.3 200.0,150.5 206.7,147.2 213.3,143.5 220.0,139.4 226.7,135.0 233.3,130.3 240.0,125.5 246.7,120.4 253.3,115.2 260.0,110.0 266.7,104.8 273.3,99.6 280.0,94.5 286.7,89.7 293.3,85.0 300.0,80.6 306.7,76.5 313.3,72.8 320.0,69.5 326.7,66.7 333.3,64.3 340.0,62.4 346.7,61.1 353.3,60.3 360.0,60.0 366.7,60.3 373.3,61.1 380.0,62.4 386.7,64.3 393.3,66.7 400.0,69.5 406.7,72.8 413.3,76.5 420.0,80.6 426.7,85.0 433.3,89.7 440.0,94.5 446.7,99.6 453.3,104.8 460.0,110.0" fill="none" stroke="#332C23" stroke-width="2"/>
<text x="140" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">−π</text>
<text x="380" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">π</text>
<text x="470" y="32" text-anchor="end" font-size="10" fill="#C9852F">x − x³/3! + x⁵/5! …</text>
</g>
</svg>
<figcaption><b>Fig. B10</b> · Schematic: sin x and its successive partial sums — each added term hugs the curve closer.</figcaption>
</figure>

<!-- zh -->

## A 组 · 事件的主角

### A1 · 纳维–斯托克斯：存在性与光滑性

- **一句话**：描述流体运动的方程，是否永远规规矩矩——还是会在有限时间内「爆炸」？
- **譬喻**：一场永远放得下去的天气预报。方程是给流体「拍电影」的规则手册——每个位置、每个时刻的风速都要听它的；「存在且光滑」就是说这部电影永不卡带：每一帧、每个格点的值都有限。*blow-up*（爆掉）就是某一帧里某个格点的速度变成无穷——电影停机。**边界**：真实的空气是分子，方程是宏观理想化；所以奇点既可能揭示理想化（而非天气本身）的失灵——判定到底是哪种，恰恰就是这个问题的意义所在。
- **问的是什么**：三维情形，解是否对所有时间都存在且保持光滑——还是会产生奇点？
- **前提·背景**：纳维（1822）与斯托克斯（1845）写下黏性流体的运动方程；该问题携带七个千禧年大奖难题之一（2000）。
- **先修概念**：**偏微分方程**是一条把「量」与其在空间、时间上的变化率绑在一起的规则；**解**就是服从规则的场。这里的**光滑**指各阶导数都保持有限；**存在性**与**唯一性**是两个不同的问题，克雷的表述把它们一并问。**外力项 f** 是外加的推力（流体下装一台风扇）；「无外力」即 f = 0，物理上最原初的情形。
- **逻辑与语言**：这个问题是一个**析取式**——要么证明永远光滑，**要么**展示一个奇点，任一答案都算解决。所以「blow-up 证明」会以否定方式解决它。
- **为什么重要**：全文的中心案件（§1.7、§2.2）——2026 年 9 月的一纸宣布，把技术真相、商业竞争、署名纠纷、优先权公案压缩进同一周 [1,5,6]。
- **现状（2026-11-22）**：克雷官网仍标 Active [4]。OpenAI 9 月 8 日的主张——就克雷表述的 C/D 陈述给出机器 blow-up 证明，经 Lean 核验但带外力项 [1]——被剑桥团队发现与其自然语言文本对不上 [118]；该方法未见推广到无外力情形 [5]。11 月 20 日，Alpöge–Buckmaster 宣布**无外力** NS blow-up 证明，Lean 形式化约 60 万行、已公开——但仓库自述形式化不含数据、区间算术**证书尚未放出** [120,121]。另有一份**带光滑外力**的 Euler blow-up Lean 制品公开（署名 Anthropic，Claude 在 Alpöge 指导下写出）；所谓三人合著的「无外力 Euler」未获一手来源，此处按未核实处理。奖金至今无人申领。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Smooth flow for all time, versus a finite-time blow-up">
<title>Smooth flow for all time, versus a finite-time blow-up</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="20" y="40" width="190" height="120" rx="6" fill="#FFFDF9" stroke="#EBDCC4"/>
<line x1="40" y1="62" x2="178" y2="62" stroke="#407CB0" stroke-width="1.5"/>
<polygon points="188,62 178,58 178,66" fill="#407CB0"/>
<line x1="40" y1="86" x2="178" y2="86" stroke="#407CB0" stroke-width="1.5"/>
<polygon points="188,86 178,82 178,90" fill="#407CB0"/>
<line x1="40" y1="110" x2="178" y2="110" stroke="#407CB0" stroke-width="1.5"/>
<polygon points="188,110 178,106 178,114" fill="#407CB0"/>
<line x1="40" y1="134" x2="178" y2="134" stroke="#407CB0" stroke-width="1.5"/>
<polygon points="188,134 178,130 178,138" fill="#407CB0"/>
<text x="115" y="182" text-anchor="middle" font-size="13" fill="#6B5F4F">∀ t</text>
<line x1="300" y1="160" x2="492" y2="160" stroke="#6B5F4F"/>
<line x1="300" y1="160" x2="300" y2="40" stroke="#6B5F4F"/>
<line x1="470" y1="160" x2="470" y2="48" stroke="#A4553F" stroke-dasharray="4 4"/>
<path d="M300 152 C 360 148, 430 120, 466 58" fill="none" stroke="#C9852F" stroke-width="2.2"/>
<text x="470" y="40" text-anchor="middle" font-size="14" fill="#A4553F">∞</text>
<text x="476" y="176" text-anchor="middle" font-size="12" fill="#A4553F">T*</text>
<text x="290" y="50" text-anchor="end" font-size="12" fill="#6B5F4F">‖u(t)‖</text>
<text x="496" y="164" text-anchor="end" font-size="12" fill="#6B5F4F">t</text>
</g>
</svg>
<figcaption><b>图 A1</b> · 示意：光滑流（左）与有限时间爆破（右）。曲线只示形状，不按比例。</figcaption>
</figure>

### A2 · Erdős 单位距离猜想（1946）

- **一句话**：平面上的 n 个点，最多能有多少对恰好相距 1？
- **譬喻**：操场上插 n 根钉子——多少对恰好相距一米？Erdős 的整齐方格网（像城市街道）给出很多对，他赌这基本就是极限。2026 年，有人用数论搭出一种「不像街道」的更聪明的布局，对数明显更多。**边界**：那个真实构造在平面直觉里是看不见的，它住在代数数域里。
- **问的是什么**：n 个平面点之间的单位距离对数，是否只比 n 多出亚多项式的一点点？
- **前提·背景**：Erdős，1946；其网格构造给出约 n^(1+c/log log n) 对，并猜想 u(n) ≤ n^(1+o(1))。
- **先修概念**：u(n) 是**对所有摆法的最大值**。n^(1+o(1)) 与 n^(1+ε) 的增长形状是语法（见门槛二）。
- **逻辑与语言**：猜想是**全称**命题（对每个 n 都压在 n 附近）；否证是**存在性**的——一族反例，在无穷多个 n 上成立，带一个固定的 ε > 0。一族反例，杀掉整条猜想。
- **为什么重要**：2026 年 5 月，它成为第一个被 AI 系统证伪的核心领域猜想——§1.5 的「第三幕」[19,20]。
- **现状（2026-11-22）**：已证伪。Alon、Bloom、Gowers 等九人发表了 OpenAI 生成反例的人类核验版（u(n) ≥ n^(1+ε) 无穷多次成立）；萨温把指数显式化到 n^1.014；经典上界 O(n^(4/3)) 纹丝未动 [19,20]。完整条目详见 [Erdős 单位距离](../famous_problems/erdos_unit_distance.md)。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A five by five grid of unit distances, and growth shapes n, n^1.014, n^4/3">
<title>A five by five grid of unit distances, and growth shapes n, n^1.014, n^4/3</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<line x1="40" y1="50" x2="40" y2="170" stroke="#EBDCC4"/>
<line x1="40" y1="50" x2="160" y2="50" stroke="#EBDCC4"/>
<line x1="70" y1="50" x2="70" y2="170" stroke="#EBDCC4"/>
<line x1="40" y1="80" x2="160" y2="80" stroke="#EBDCC4"/>
<line x1="100" y1="50" x2="100" y2="170" stroke="#EBDCC4"/>
<line x1="40" y1="110" x2="160" y2="110" stroke="#EBDCC4"/>
<line x1="130" y1="50" x2="130" y2="170" stroke="#EBDCC4"/>
<line x1="40" y1="140" x2="160" y2="140" stroke="#EBDCC4"/>
<line x1="160" y1="50" x2="160" y2="170" stroke="#EBDCC4"/>
<line x1="40" y1="170" x2="160" y2="170" stroke="#EBDCC4"/>
<circle cx="40" cy="50" r="2.6" fill="#332C23"/>
<circle cx="40" cy="80" r="2.6" fill="#332C23"/>
<circle cx="40" cy="110" r="2.6" fill="#332C23"/>
<circle cx="40" cy="140" r="2.6" fill="#332C23"/>
<circle cx="40" cy="170" r="2.6" fill="#332C23"/>
<circle cx="70" cy="50" r="2.6" fill="#332C23"/>
<circle cx="70" cy="80" r="2.6" fill="#332C23"/>
<circle cx="70" cy="110" r="2.6" fill="#332C23"/>
<circle cx="70" cy="140" r="2.6" fill="#332C23"/>
<circle cx="70" cy="170" r="2.6" fill="#332C23"/>
<circle cx="100" cy="50" r="2.6" fill="#332C23"/>
<circle cx="100" cy="80" r="2.6" fill="#332C23"/>
<circle cx="100" cy="110" r="2.6" fill="#332C23"/>
<circle cx="100" cy="140" r="2.6" fill="#332C23"/>
<circle cx="100" cy="170" r="2.6" fill="#332C23"/>
<circle cx="130" cy="50" r="2.6" fill="#332C23"/>
<circle cx="130" cy="80" r="2.6" fill="#332C23"/>
<circle cx="130" cy="110" r="2.6" fill="#332C23"/>
<circle cx="130" cy="140" r="2.6" fill="#332C23"/>
<circle cx="130" cy="170" r="2.6" fill="#332C23"/>
<circle cx="160" cy="50" r="2.6" fill="#332C23"/>
<circle cx="160" cy="80" r="2.6" fill="#332C23"/>
<circle cx="160" cy="110" r="2.6" fill="#332C23"/>
<circle cx="160" cy="140" r="2.6" fill="#332C23"/>
<circle cx="160" cy="170" r="2.6" fill="#332C23"/>
<text x="100" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">n = 25 → 40</text>
<line x1="262" y1="170" x2="502" y2="170" stroke="#6B5F4F"/>
<line x1="262" y1="170" x2="262" y2="35" stroke="#6B5F4F"/>
<path d="M272 152 C 340 122, 430 82, 496 42" fill="none" stroke="#407CB0" stroke-dasharray="5 4"/>
<path d="M272 154 C 350 132, 440 96, 496 62" fill="none" stroke="#E8A855" stroke-width="2.2"/>
<path d="M272 156 C 350 140, 440 112, 496 80" fill="none" stroke="#6B5F4F" stroke-dasharray="2 4"/>
<line x1="278" y1="40" x2="298" y2="40" stroke="#407CB0" stroke-dasharray="5 4"/>
<text x="304" y="44" text-anchor="start" font-size="10" fill="#407CB0">n^4/3</text>
<line x1="278" y1="58" x2="298" y2="58" stroke="#E8A855" stroke-width="2.2"/>
<text x="304" y="62" text-anchor="start" font-size="10" fill="#C9852F">n^1.014</text>
<line x1="278" y1="76" x2="298" y2="76" stroke="#6B5F4F" stroke-dasharray="2 4"/>
<text x="304" y="80" text-anchor="start" font-size="10" fill="#6B5F4F">n</text>
<text x="502" y="164" text-anchor="end" font-size="12" fill="#6B5F4F">n</text>
<text x="258" y="44" text-anchor="end" font-size="12" fill="#6B5F4F">u(n)</text>
</g>
</svg>
<figcaption><b>图 A2</b> · 示意：5×5 网格（n = 25，40 对单位距离）与三种增长形状——n、n^1.014、n^4/3。</figcaption>
</figure>

### A3 · 费马大定理——与它的形式化

- **一句话**：x^n + y^n = z^n 在 n ≥ 3 时没有正整数解——2026 年，机器把整个证明写成了计算机能逐行检查的语言。
- **譬喻**：整数边的立方体。两个立方体的体积之和，永远拼不出第三个立方体：3³ + 4³ 不是任何整数的立方。妙处在楼下那层「差一点」：3² + 4² = 5²——平方可以（勾股定理）；费马的规则恰从勾股的终点开始。**边界**：譬喻说清了问的是什么，丝毫没说为什么难——证明穿过椭圆曲线与模形式，立方体的画面到不了那里。
- **问的是什么**（2026 年版本）：能否只从 Lean 的三条标准公理出发重新推出怀尔斯的证明——链条中不剩任何一处需要人的信任？
- **前提·背景**：费马约 1637 年留下猜想；358 年后由怀尔斯（与泰勒）于 1994–95 年证明。完整条目详见 [费马大定理](../famous_problems/fermat_last_theorem.md)。
- **先修概念**：「形式化」指把证明转写成形式语言（Lean），由一个极小、被信任的**内核**逐项检查每一步的类型正确性。「Mathlib」是共同体的形式库；「超过它五倍」是体量陈述，不是难度陈述。
- **逻辑与语言**：定理是对无穷多个 n 的全称命题——任何计算机搜索都判不了它；这正是 358 年的特例累积最终一无所获的原因。
- **为什么重要**：§1.8 以它作为核验瓶颈的极端标本——一份没有任何人能通读的制品 [25,26]。
- **现状（2026-11-22）**：Anthropic 9 月 4 日宣布完整 Lean 形式化：约 1300 万行、约 29500 个中间定理、近自主工作十一天，经内核核验并确认与 Mathlib 的陈述一致；巴扎德审阅后称之为非凡的自动形式化成就，但数学上不增添任何新知识 [25,26]。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Squares 3-4-5 add up; cubes 3 and 4 do not add up to a cube">
<title>Squares 3-4-5 add up; cubes 3 and 4 do not add up to a cube</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="26" y="80" width="48" height="48" fill="#F7EFE2" stroke="#C9852F"/>
<text x="50.0" y="144" text-anchor="middle" font-size="12" fill="#6B5F4F">3²</text>
<rect x="94" y="64" width="64" height="64" fill="#F7EFE2" stroke="#C9852F"/>
<text x="126.0" y="144" text-anchor="middle" font-size="12" fill="#6B5F4F">4²</text>
<rect x="186" y="48" width="80" height="80" fill="#F7EFE2" stroke="#C9852F"/>
<text x="226.0" y="144" text-anchor="middle" font-size="12" fill="#6B5F4F">5²</text>
<text x="82" y="96" text-anchor="middle" font-size="16" fill="#6B5F4F">+</text>
<text x="172" y="96" text-anchor="middle" font-size="16" fill="#6B5F4F">=</text>
<text x="300" y="86" text-anchor="start" font-size="12" fill="#332C23">3³ + 4³ = 91</text>
<text x="300" y="116" text-anchor="start" font-size="12" fill="#332C23">5³ = 125</text>
<text x="300" y="152" text-anchor="start" font-size="14" fill="#A4553F">91 ≠ 125</text>
</g>
</svg>
<figcaption><b>图 A3</b> · 示意：平方能拼（3² + 4² = 5²）；立方不能（3³ + 4³ = 91 ≠ 125）。</figcaption>
</figure>

### A4 · 黎曼假设

- **一句话**：zeta 函数所有「有意思」的零点，是否都落在一条直线上？
- **譬喻**：zeta 函数是素数的换能器——把散乱不规的素数接入，它输出一条光滑波形，波上的「心跳节点」（零点）支配着素数分布得多均匀。RH 说：所有节点都落在同一条基准线上；换个说法：素数的涨落被钉死在数论允许的最小尺寸。**边界**：波形画面是编码方式的示意，不是推导；真正的等价要走一条显式的误差项。
- **问的是什么**：ζ(s) 的所有非平凡零点，实部是否恰为 1/2？
- **前提·背景**：黎曼，1859；千禧年难题之一，数学最著名的未解问题。
- **先修概念（zeta 函数，平白版）**：ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s + …——一个带阻尼的级数，当 s 的实部大于 1 时收敛。欧拉的奇迹：同一个和可以按素数分解——每个素数贡献一个因子 1/(1 − 1/p^s)——素数被**编码**进去了。级数在实部 1 处用尽天然的住址；「解析延拓」用另一个唯一确定的公式把同一个函数延到界外——注意这里的语言学要点：同一个名字 ζ(s) 在不同区域由不同公式定义、靠唯一性缝合；**函数不是它的公式**。**零点**是使 ζ(s) = 0 的输入 s：「平凡」零点在负偶数处；「非平凡」零点在 0 < 实部 < 1 的带子里。RH 说它们全部恰在正中线 real part = 1/2；本文后记里的 **quasi-RH** 结果把它们压进 1/8 ≤ 实部 ≤ 7/8 的竖条——一窄条，远不及那条线 [115]。利害所在：零点的位置支配素数计数的误差项——RH 将把素数的不均匀性钉在约 √x 的量级。
- **逻辑与语言**：假设是对无穷多个零点的全称命题；线外一个零点即否证之。「quasi-RH」在逻辑上不是「弱化的 RH」——它是一条**不同且更弱的围栏**，且对全体零点一次证明。
- **为什么重要**：§6.4 曾以「AI 会不会证明黎曼猜想」作为该被绕开的问法；2026 年 11 月，这个问题以一种谁也没料到的方式被回答了一版 [93,120,122]。
- **现状（2026-11-22）**：11 月 20 日，Alpöge 宣布黎曼假设的证明，出自一个内部 AI 模型（媒体点名 Claude；Tao 原文说「一个内部 AI 模型」——两说照录 [120,123]）；证明以约 1700 万行的 Lean 制品存在，11 月 21 日 Lean 社区按四项明示判据认证「黎曼假设的陈述与证明均属正确」[122]。更早，10 月发布中的 quasi-RH 结果在两周内被人类分析学家消化并大体确认 [115]。人类数学协会则反对：无人能有理由声称理解这样一份文件 [124]。机器已核验；共同体已认证；人类理解进行中。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Critical strip, critical line at real part one half, quasi-Riemann band">
<title>Critical strip, critical line at real part one half, quasi-Riemann band</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="250" y="30" width="55" height="148" fill="#F7EFE2"/>
<rect x="256.9" y="30" width="41.2" height="148" fill="#FBE9C8"/>
<line x1="20" y1="110" x2="500" y2="110" stroke="#6B5F4F"/>
<line x1="250" y1="190" x2="250" y2="22" stroke="#6B5F4F"/>
<line x1="277.5" y1="190" x2="277.5" y2="22" stroke="#C9852F" stroke-width="2" stroke-dasharray="6 3"/>
<circle cx="277.5" cy="76.1" r="3.2" fill="#A4553F"/>
<circle cx="277.5" cy="59.6" r="3.2" fill="#A4553F"/>
<circle cx="277.5" cy="50.0" r="3.2" fill="#A4553F"/>
<circle cx="277.5" cy="143.9" r="3.2" fill="#A4553F"/>
<circle cx="277.5" cy="160.4" r="3.2" fill="#A4553F"/>
<circle cx="277.5" cy="170.0" r="3.2" fill="#A4553F"/>
<circle cx="140" cy="110" r="3.2" fill="#6B5F4F"/>
<circle cx="30" cy="110" r="3.2" fill="#6B5F4F"/>
<text x="283.5" y="20" text-anchor="start" font-size="12" fill="#C9852F">Re = 1/2</text>
<text x="256.875" y="194" text-anchor="middle" font-size="10" fill="#9A8D7A">1/8</text>
<text x="298.125" y="194" text-anchor="middle" font-size="10" fill="#9A8D7A">7/8</text>
<text x="140" y="126" text-anchor="middle" font-size="10" fill="#6B5F4F">−2</text>
<text x="30" y="126" text-anchor="middle" font-size="10" fill="#6B5F4F">−4</text>
<text x="309" y="126" text-anchor="start" font-size="10" fill="#6B5F4F">1</text>
<text x="246" y="126" text-anchor="end" font-size="10" fill="#6B5F4F">0</text>
<text x="287.5" y="80.088" text-anchor="start" font-size="10" fill="#A4553F">14.13i</text>
<text x="500" y="126" text-anchor="end" font-size="12" fill="#9A8D7A">Re(s)</text>
<text x="244" y="34" text-anchor="end" font-size="12" fill="#9A8D7A">Im(s)</text>
</g>
</svg>
<figcaption><b>图 A4</b> · 示意：临界带 0 < Re < 1、Re = 1/2 上的最初几个零点、−2 与 −4 处的平凡零点，以及 quasi-RH 的 1/8–7/8 竖条。</figcaption>
</figure>

### A5 · 唯一游戏猜想（2002）

- **一句话**：某个「猜标签」问题，近似求解是否几乎和精确求解一样难？
- **譬喻**：把一张积怨网里的宾客分到两桌，让每对冤家不同桌——有时做不到全对。猜想断言：对某一族这样的网，哪怕放过**一小撮**冤家，代价也与全解一样大。它是「无折扣」猜想：次优答案并不比最优答案便宜。**边界**：真实陈述关于带标签的约束与近似比，不是桌子；譬喻丢掉了定量的脊柱。
- **问的是什么**：允许少量违反的约束系统里，找到满足大多数约束的标签，是否计算上不可行？
- **前提·背景**：Khot，2002；若为真，则一大批经典问题（Max Cut 等）的最优「难以近似比」被锁定。
- **先修概念**：**近似比**是快速方法相对完美解的保证质量；「难以近似」证明没有快速方法能好过某个定死的比值。
- **逻辑与语言**：这是一条**关于困难的猜想**——内容是对一切高效算法的全称陈述（「没有任何算法能好过……」），所以这一领域里证明稀少，而否证将是一个算法。
- **为什么重要**：10 月 6 日发布宣称其 372 个家族中包含 UGC 的证明——整批发布中分量最重的一条主张（后记 §xi）[93]。
- **现状（2026-11-22）**：已发布的主张，未被接受的定理。Moshkovitz 已在这份证明上花数周，与 Khot、Håstad、Minzer 协作并借助 GPT-6 Astra，面对一个她称为「全然陌生的全新纠错码」；相关努力已在 Simons Institute 报告；完整核验尚未宣布 [119]。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="An odd cycle that cannot be two-coloured, and the no-discount axis">
<title>An odd cycle that cannot be two-coloured, and the no-discount axis</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<line x1="120.0" y1="45.0" x2="172.3" y2="83.0" stroke="#EBDCC4" stroke-width="1.4"/>
<line x1="172.3" y1="83.0" x2="152.3" y2="144.5" stroke="#EBDCC4" stroke-width="1.4"/>
<line x1="152.3" y1="144.5" x2="87.7" y2="144.5" stroke="#EBDCC4" stroke-width="1.4"/>
<line x1="87.7" y1="144.5" x2="67.7" y2="83.0" stroke="#EBDCC4" stroke-width="1.4"/>
<line x1="67.7" y1="83.0" x2="120.0" y2="45.0" stroke="#A4553F" stroke-width="2" stroke-dasharray="4 4"/>
<circle cx="120.0" cy="45.0" r="7" fill="#E8A855" stroke="#FFFDF9"/>
<circle cx="172.3" cy="83.0" r="7" fill="#407CB0" stroke="#FFFDF9"/>
<circle cx="152.3" cy="144.5" r="7" fill="#E8A855" stroke="#FFFDF9"/>
<circle cx="87.7" cy="144.5" r="7" fill="#407CB0" stroke="#FFFDF9"/>
<circle cx="67.7" cy="83.0" r="7" fill="#E8A855" stroke="#FFFDF9"/>
<text x="120" y="188" text-anchor="middle" font-size="12" fill="#6B5F4F">C₅</text>
<line x1="250" y1="130" x2="500" y2="130" stroke="#6B5F4F"/>
<line x1="480" y1="120" x2="480" y2="140" stroke="#6B5F4F"/>
<line x1="440" y1="120" x2="440" y2="140" stroke="#A4553F"/>
<text x="480" y="156" text-anchor="middle" font-size="10" fill="#6B5F4F">1</text>
<text x="440" y="156" text-anchor="middle" font-size="10" fill="#A4553F">1−ε</text>
<line x1="440" y1="96" x2="480" y2="96" stroke="#A4553F" stroke-dasharray="3 3"/>
<text x="460" y="88" text-anchor="middle" font-size="14" fill="#A4553F">≈</text>
<text x="250" y="146" text-anchor="start" font-size="10" fill="#6B5F4F">0</text>
<text x="375" y="60" text-anchor="start" font-size="12" fill="#332C23" font-weight="600">UGC</text>
</g>
</svg>
<figcaption><b>图 A5</b> · 示意：奇圈无法二染色——必有一条约束被违反；右轴示猜想的「无折扣」主张。</figcaption>
</figure>

### A6 · 雅可比猜想（1939）

- **一句话**：多项式映射若雅可比行列式恒为非零常数，它是否必有多项式逆映射？
- **譬喻**：一台「多项式机器」把输入向量变成输出向量。雅可比行列式度量机器在每一点局部拉伸或压扁面积的程度；**恒为非零常数**即它处处不压扁任何东西。猜想问：这样的机器是否必配一台多项式机器把输出还原？2026 年的答案是：三维及以上——不。存在什么都不压扁、却把输出绕得没有任何多项式能解开 Its 机器。**边界**：「一张纸处处没被压扁，是否必能完美摊平」的画面有那个味道；真正的障碍是代数的，不是几何的。
- **问的是什么**：对哪些维数 n，雅可比行列式恒为非零常数的多项式映射 C^n → C^n 必有多项式逆？
- **前提·背景**：Keller，1939；一维平凡成立，二维悬置近百年。
- **先修概念**：**多项式映射**是用坐标的加法与乘法搭成的机器；**雅可比行列式**是由机器的一阶导数算出的局部拉伸因子。
- **逻辑与语言**：局部对全局是铰链——「每一点都可逆」（分析事实）弱于「有多项式逆」（全局代数事实）；猜想问前者是否强制后者，反例逐维给出「不强制」。
- **为什么重要**：§2.1 把它 2026 年 7 月的反例列为菲尔兹奖得主联名信之前机器证明大戏的一幕 [1,19,30]。
- **现状（2026-11-22）**：n ≥ 3 为假。Alpöge 2026 年 7 月 19 日宣布三维反例（AI 模型助力找到）；Tao 次日发布公开的「消化」[106]；Gao 推广到一切大于二的维数，所有恒等式经精确有理数算术验证 [107]；巴扎德的团队在宣布数日内即看到反例被 Lean 机检 [108]。n = 2 仍未解。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A shear with constant Jacobian, and a tangle with no polynomial inverse">
<title>A shear with constant Jacobian, and a tangle with no polynomial inverse</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="40" y="60" width="120" height="120" fill="#FFFDF9" stroke="#9A8D7A"/>
<line x1="40" y1="60" x2="40" y2="180" stroke="#EBDCC4"/>
<line x1="40" y1="60" x2="160" y2="60" stroke="#EBDCC4"/>
<line x1="70" y1="60" x2="70" y2="180" stroke="#EBDCC4"/>
<line x1="40" y1="90" x2="160" y2="90" stroke="#EBDCC4"/>
<line x1="100" y1="60" x2="100" y2="180" stroke="#EBDCC4"/>
<line x1="40" y1="120" x2="160" y2="120" stroke="#EBDCC4"/>
<line x1="130" y1="60" x2="130" y2="180" stroke="#EBDCC4"/>
<line x1="40" y1="150" x2="160" y2="150" stroke="#EBDCC4"/>
<line x1="160" y1="60" x2="160" y2="180" stroke="#EBDCC4"/>
<line x1="40" y1="180" x2="160" y2="180" stroke="#EBDCC4"/>
<line x1="220" y1="90.0" x2="220" y2="210.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="250" y1="79.5" x2="250" y2="199.5" stroke="#C9852F" stroke-width="1.4"/>
<line x1="280" y1="69.0" x2="280" y2="189.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="310" y1="58.5" x2="310" y2="178.5" stroke="#C9852F" stroke-width="1.4"/>
<line x1="340" y1="48.0" x2="340" y2="168.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="220" y1="90" x2="340" y2="48.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="220" y1="120" x2="340" y2="78.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="220" y1="150" x2="340" y2="108.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="220" y1="180" x2="340" y2="138.0" stroke="#C9852F" stroke-width="1.4"/>
<line x1="220" y1="210" x2="340" y2="168.0" stroke="#C9852F" stroke-width="1.4"/>
<text x="110" y="196" text-anchor="middle" font-size="12" fill="#332C23">det J = 1</text>
<text x="340" y="196" text-anchor="middle" font-size="12" fill="#332C23">n ≥ 3</text>
<path d="M330 70 C 390 30, 470 90, 410 130 C 360 165, 300 110, 350 80" fill="none" stroke="#407CB0" stroke-width="2"/>
<path d="M350 80 C 400 60, 440 120, 390 140" fill="none" stroke="#A4553F" stroke-width="2"/>
</g>
</svg>
<figcaption><b>图 A6</b> · 示意：雅可比恒定的剪切（每格面积不变），以及没有多项式能解开的缠绕。</figcaption>
</figure>

### A7 · 全部光滑七维球面上的正截面曲率

- **一句话**：每一种「怪异」的七维球面，能否都被赋予一个处处正弯曲的几何？
- **譬喻**：橘子皮处处向外鼓；马鞍面这边鼓、那边塌。「正截面曲率」指**每一片**二维截面都像橘子。七维球面带着 28 种在同一拓扑上安装微积分的合法方式——28 颗「接线不同」的孪生球；这条定理说：每一颗都能配一副全橘子式的几何。**边界**：「接线」（光滑结构）没有日常画面；孪生球摸上去无法区分，差别在于哪些函数算「可微」。
- **问的是什么**：为光滑同伦七维球面的全部 28 个定向微分同胚类，各构造一个严格正截面曲率的度量。
- **前提·背景**：米尔诺 1956 年发现怪异光滑结构；曲率问题成为「拓扑如何约束几何」的长久试金石。
- **先修概念**：**流形**是每一小片都像平直空间的空间；**光滑结构**是「哪些小片以可微方式缝合」的一种选择；**截面曲率**读出每一片二维截面的弯曲方向。
- **逻辑与语言**：「全部 28 类」是全称断言——任何一类若被证明存在障碍即否证之；其证明方法（以两块正曲率圆盘粘合）是对每一类的构造，故主张是构造性见证的。
- **为什么重要**：后记 §iv 把它记作边界案例——AI 致谢自 v1 起就在 [82,83]。
- **现状（2026-11-22）**：何杨辉、刘子然与丘成桐 9 月 24 日在预印本中宣称已构造（以边界度量相容的两个正曲率七维圆盘粘合）；论文致谢 ChatGPT 与 Claude（v1 即有）[82,83]。后续工作正在延伸该技术；共同体尚无裁定。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Two positively curved discs glued along the boundary, and twenty-eight smooth structures">
<title>Two positively curved discs glued along the boundary, and twenty-eight smooth structures</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<path d="M70 110 A 60 60 0 0 1 190 110" fill="none" stroke="#C9852F" stroke-width="2"/>
<path d="M70 110 A 60 60 0 0 0 190 110" fill="none" stroke="#407CB0" stroke-width="2"/>
<line x1="70" y1="110" x2="190" y2="110" stroke="#A4553F" stroke-dasharray="4 4"/>
<line x1="95" y1="78" x2="95" y2="59" stroke="#C9852F" stroke-width="1.3"/>
<polygon points="95,57 92,65 98,65" fill="#C9852F"/>
<line x1="130" y1="66" x2="130" y2="46" stroke="#C9852F" stroke-width="1.3"/>
<polygon points="130,44 127,52 133,52" fill="#C9852F"/>
<line x1="165" y1="78" x2="165" y2="59" stroke="#C9852F" stroke-width="1.3"/>
<polygon points="165,57 162,65 168,65" fill="#C9852F"/>
<line x1="95" y1="142" x2="95" y2="161" stroke="#407CB0" stroke-width="1.3"/>
<polygon points="95,163 92,155 98,155" fill="#407CB0"/>
<line x1="130" y1="154" x2="130" y2="174" stroke="#407CB0" stroke-width="1.3"/>
<polygon points="130,176 127,168 133,168" fill="#407CB0"/>
<line x1="165" y1="142" x2="165" y2="161" stroke="#407CB0" stroke-width="1.3"/>
<polygon points="165,163 162,155 168,155" fill="#407CB0"/>
<text x="130" y="100" text-anchor="middle" font-size="11" fill="#332C23">D⁷ ∪ D⁷</text>
<circle cx="320" cy="66" r="5" fill="#E8A855"/>
<circle cx="320" cy="92" r="5" fill="#407CB0"/>
<circle cx="320" cy="118" r="5" fill="#E8A855"/>
<circle cx="320" cy="144" r="5" fill="#407CB0"/>
<circle cx="346" cy="66" r="5" fill="#407CB0"/>
<circle cx="346" cy="92" r="5" fill="#E8A855"/>
<circle cx="346" cy="118" r="5" fill="#407CB0"/>
<circle cx="346" cy="144" r="5" fill="#E8A855"/>
<circle cx="372" cy="66" r="5" fill="#E8A855"/>
<circle cx="372" cy="92" r="5" fill="#407CB0"/>
<circle cx="372" cy="118" r="5" fill="#E8A855"/>
<circle cx="372" cy="144" r="5" fill="#407CB0"/>
<circle cx="398" cy="66" r="5" fill="#407CB0"/>
<circle cx="398" cy="92" r="5" fill="#E8A855"/>
<circle cx="398" cy="118" r="5" fill="#407CB0"/>
<circle cx="398" cy="144" r="5" fill="#E8A855"/>
<circle cx="424" cy="66" r="5" fill="#E8A855"/>
<circle cx="424" cy="92" r="5" fill="#407CB0"/>
<circle cx="424" cy="118" r="5" fill="#E8A855"/>
<circle cx="424" cy="144" r="5" fill="#407CB0"/>
<circle cx="450" cy="66" r="5" fill="#407CB0"/>
<circle cx="450" cy="92" r="5" fill="#E8A855"/>
<circle cx="450" cy="118" r="5" fill="#407CB0"/>
<circle cx="450" cy="144" r="5" fill="#E8A855"/>
<circle cx="476" cy="66" r="5" fill="#E8A855"/>
<circle cx="476" cy="92" r="5" fill="#407CB0"/>
<circle cx="476" cy="118" r="5" fill="#E8A855"/>
<circle cx="476" cy="144" r="5" fill="#407CB0"/>
<text x="398" y="186" text-anchor="middle" font-size="12" fill="#6B5F4F">28</text>
</g>
</svg>
<figcaption><b>图 A7</b> · 示意：两个正曲率圆盘沿相容边界粘合；七维球面的 28 种光滑结构。</figcaption>
</figure>

### A8 · 四阶复矩阵乘法：49 到 48

- **一句话**：乘两个 4×4 复矩阵，最少需要几次标量乘法？
- **譬喻**：一场烹饪挑战——把两片数字网格相乘，尽量少用「单次搅拌」。教科书配方用 64 次搅拌；斯特拉森（1969）找到 49 次的；AlphaEvolve 找到 48 次的。省下一次搅拌，在放大到巨大网格的锅里复利放大。**边界**：真实的对象是**张量秩**——把乘法算子分解成最少的秩一零件——譬喻说不出 48 为什么难被击败。
- **问的是什么**：找到 4×4 复矩阵情形已知最少的标量乘法次数。
- **前提·背景**：斯特拉森 1969 年的算法开创了代数复杂度理论；纪录保持了五十六年。
- **先修概念**：**张量秩**数的是装配乘法张量所需最少的简单（秩一）积木数；它是「搅拌次数」的无坐标版本。
- **逻辑与语言**：上界由算法见证（造出来即可）；配套的下界要求排除一切更好的可能——纪录 48 是已知最好的**算法**，不是已证的最小值。门槛三的逻辑不对称，野生标本。
- **为什么重要**：§1.4 以 AlphaEvolve 的 48 作为「计算-核验」一端成果的标志 [16]。
- **现状（2026-11-22）**：48（DeepMind AlphaEvolve，2025 年 5 月）仍为纪录；后续工作把它以纯有理数系数重新导出。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Three four by four grids, and bars for 64, 49, 48 scalar multiplications">
<title>Three four by four grids, and bars for 64, 49, 48 scalar multiplications</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="30" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="30" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="30" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="30" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="42" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="42" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="42" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="42" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="54" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="54" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="54" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="54" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="66" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="66" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="66" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="66" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<text x="54" y="60" text-anchor="middle" font-size="12" fill="#332C23" font-weight="600">A</text>
<rect x="120" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="120" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="120" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="120" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="132" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="132" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="132" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="132" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="144" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="144" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="144" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="144" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="156" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="156" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="156" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="156" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<text x="144" y="60" text-anchor="middle" font-size="12" fill="#332C23" font-weight="600">B</text>
<rect x="215" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="215" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="215" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="215" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="227" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="227" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="227" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="227" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="239" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="239" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="239" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="239" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="251" y="70" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="251" y="82" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="251" y="94" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<rect x="251" y="106" width="12" height="12" fill="#F7EFE2" stroke="#EBDCC4"/>
<text x="239" y="60" text-anchor="middle" font-size="12" fill="#332C23" font-weight="600">C</text>
<text x="108" y="100" text-anchor="middle" font-size="16" fill="#6B5F4F">×</text>
<text x="200" y="100" text-anchor="middle" font-size="16" fill="#6B5F4F">=</text>
<rect x="300" y="70" width="166" height="18" rx="4" fill="#E8A855" opacity=".85"/>
<text x="474.4" y="84" text-anchor="start" font-size="12" fill="#332C23">64</text>
<rect x="300" y="110" width="127" height="18" rx="4" fill="#E8A855" opacity=".85"/>
<text x="435.4" y="124" text-anchor="start" font-size="12" fill="#332C23">49</text>
<rect x="300" y="150" width="124" height="18" rx="4" fill="#C9852F" opacity=".85"/>
<text x="432.8" y="164" text-anchor="start" font-size="12" fill="#332C23">48</text>
<text x="300" y="190" text-anchor="start" font-size="10" fill="#9A8D7A">n×n, n = 4</text>
</g>
</svg>
<figcaption><b>图 A8</b> · 示意：两个 4×4 矩阵相乘，以及 64 → 49 → 48 的纪录。</figcaption>
</figure>

### A9 · 十一维的接吻数

- **一句话**：在十一维空间里，多少个单位球可以同时贴住中央那个单位球？
- **譬喻**：水果店的橙子堆：围绕一个中央橙子，最多 12 个橙子同时贴住它（牛顿与格雷戈里争过的数）。十一维的「橙子」是十一维球，我们只能给计数划出区间：至少 593，至多 868。**边界**：高维球无法画；譬喻带得走计数之问，带不走约束它的几何。
- **问的是什么**：确定 R^11 中互不重叠的单位球同时贴住中央单位球的最大个数。
- **前提·背景**：精确值仅在一、二、三、四、八、二十四维已知——二十四维是 196,560，至今令人咋舌的数。
- **先修概念**：这里的**维数**是独立方向的个数；单位球是与中心距离恰为 1 的点的集合；「贴住」指点间距恰为 2。
- **逻辑与语言**：下界来自一个构造（593——造出来）；上界 868 来自排除论证（没有摆法能更好）。又是两种相反的证据形态。
- **为什么重要**：§1.4 把它与矩阵乘法并举，作为可机械核验的纪录 [16]。
- **现状（2026-11-22）**：593–868；精确值未知。后有论文主张 604；标准参考尚未采信，本页亦按未核验处理 [16]。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Six unit circles around a central one, and known kissing numbers by dimension">
<title>Six unit circles around a central one, and known kissing numbers by dimension</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<circle cx="120" cy="100" r="28" fill="#F7EFE2" stroke="#C9852F" stroke-width="2"/>
<circle cx="176.0" cy="100.0" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="148.0" cy="148.5" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="92.0" cy="148.5" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="64.0" cy="100.0" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="92.0" cy="51.5" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="148.0" cy="51.5" r="28" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.6"/>
<text x="120" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">d = 2</text>
<rect x="412" y="52" width="44" height="58" rx="6" fill="#FBE9C8" stroke="#C9852F" stroke-dasharray="4 3"/>
<text x="235" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">1</text>
<text x="235" y="96" text-anchor="middle" font-size="10" fill="#332C23">2</text>
<text x="272" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">2</text>
<text x="272" y="96" text-anchor="middle" font-size="10" fill="#332C23">6</text>
<text x="309" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">3</text>
<text x="309" y="96" text-anchor="middle" font-size="10" fill="#332C23">12</text>
<text x="346" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">4</text>
<text x="346" y="96" text-anchor="middle" font-size="10" fill="#332C23">24</text>
<text x="390" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">8</text>
<text x="390" y="96" text-anchor="middle" font-size="10" fill="#332C23">240</text>
<text x="434" y="70" text-anchor="middle" font-size="10" fill="#A4553F">11</text>
<text x="434" y="96" text-anchor="middle" font-size="9" fill="#A4553F">593–868</text>
<text x="478" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">24</text>
<text x="478" y="96" text-anchor="middle" font-size="10" fill="#332C23">196560</text>
<text x="200" y="70" text-anchor="middle" font-size="10" fill="#9A8D7A">d</text>
</g>
</svg>
<figcaption><b>图 A9</b> · 示意：二维中六个单位圆贴住中央圆；各维已知接吻数——十一维仍是一个区间。</figcaption>
</figure>

### A10 · 九圈六边形振幅（附一个「单负」旁注）

- **一句话**：在量子场论的「玩具模型」里，算出一个深达九个量子圈的、复杂得可怕的散射振幅。
- **譬喻**：散射振幅是自然界给一次粒子对撞开出的**收据**——概率的打印单。「九圈」是说收据上有九层嵌套的修正，每一层都对虚拟粒子求和。**自举**法是倒着玩的拼图：不是正向计算，而是钉下足够多的一致性条件（对称性、极限），让答案被逼出来。**边界**：收据画面藏住了九圈为何是前沿——表达式按组合方式爆炸。
- **问的是什么**：算出九圈六边形振幅（旁注：判定某个单负胶子树级振幅是否非零）。
- **前提·背景**：平面 N=4 超杨–米尔斯是场论的「氢原子」；八圈纪录是 2023 年 Dixon 与刘洋所立。
- **先修概念**：**树级振幅**是不含虚拟粒子圈的情形；「单负」指螺旋度组态；**形状因子**是一个表亲量，用作独立路径。
- **逻辑与语言**：旁注的陈述——「这些振幅非零」——是由显式公式见证的**存在性**主张；2026 年预印本报告该公式先由 GPT-5.2 Pro 猜想、再由 OpenAI 内部模型证明 [23]。
- **为什么重要**：§1.7 把 2026 年理论物理的两案读作「机器执行配方」与「机器提出猜想」的现场标本 [23,24]。
- **现状（2026-11-22）**：Anthropic 9 月 25 日宣布 Claude 算出九圈振幅，Dixon 花约两周独立核验；何颂领衔的中科院团队同期得到大部分结果，部分约束用了 GPT-6 [24]。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A hexagon amplitude with nine loops, and the eight to nine loop record">
<title>A hexagon amplitude with nine loops, and the eight to nine loop record</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<polygon points="185.0,100.0 157.5,147.6 102.5,147.6 75.0,100.0 102.5,52.4 157.5,52.4" fill="none" stroke="#C9852F" stroke-width="2"/>
<line x1="185.0" y1="100.0" x2="211.0" y2="100.0" stroke="#407CB0" stroke-width="1.6"/>
<line x1="157.5" y1="147.6" x2="170.5" y2="170.1" stroke="#407CB0" stroke-width="1.6"/>
<line x1="102.5" y1="147.6" x2="89.5" y2="170.1" stroke="#407CB0" stroke-width="1.6"/>
<line x1="75.0" y1="100.0" x2="49.0" y2="100.0" stroke="#407CB0" stroke-width="1.6"/>
<line x1="102.5" y1="52.4" x2="89.5" y2="29.9" stroke="#407CB0" stroke-width="1.6"/>
<line x1="157.5" y1="52.4" x2="170.5" y2="29.9" stroke="#407CB0" stroke-width="1.6"/>
<circle cx="105" cy="80" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="105" cy="100" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="105" cy="120" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="130" cy="80" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="130" cy="100" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="130" cy="120" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="155" cy="80" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="155" cy="100" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<circle cx="155" cy="120" r="7" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.3"/>
<text x="130" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">L = 9</text>
<rect x="300" y="76" width="144" height="18" rx="4" fill="#E8A855" opacity=".85"/>
<text x="300" y="70" text-anchor="start" font-size="11" fill="#332C23">8 · 2023</text>
<rect x="300" y="122" width="162" height="18" rx="4" fill="#C9852F" opacity=".85"/>
<text x="300" y="116" text-anchor="start" font-size="11" fill="#332C23">9 · 2026</text>
</g>
</svg>
<figcaption><b>图 A10</b> · 示意：带九个圈的六边形振幅，以及 8 → 9 圈的纪录。</figcaption>
</figure>

### A11 · First Proof：十道研究级问题

- **一句话**：机器能否解出它的考官们自己真心关心的问题？
- **譬喻**：不是打磨好的奥数谜题，而是把水管工请到自己家——十处真实的水管漏水，来自十一位研究者各自的研究。**边界**：譬喻漏了关键：漏点是**挑出来的**；挑战的设计（以及评估协议的缺失）才是真正的主戏。
- **问的是什么**：十题之中，机器生成的解答能确立几道——以及谁能判定？
- **前提·背景**：2026 年由十一位研究数学家组织的挑战，刻意不是竞赛题，不是为「可解」而设计的基准题。
- **先修概念**：出 §1.1 框架之外无需更多——挑战的关键在制度：谁评、按什么协议。
- **逻辑与语言**：「研究级」不是一个良定义的类；挑战用构造把它具体化——十道具名的问题，每道都有一个知道「答案必须做到什么」的主人。
- **为什么重要**：§1.6 与 §6.4 以它作为核验瓶颈最干净的表达 [22]。
- **现状（2026-11-22）**：生成的一半已经成立；评估的一半仍是未了的公案，组织者自己承认，测度「自主提出问题」的实验方法尚不存在 [22]。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Ten research questions, a machine answer, and an open evaluation gate">
<title>Ten research questions, a machine answer, and an open evaluation gate</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="24" y="44" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="49" y="59" text-anchor="middle" font-size="10" fill="#6B5F4F">1</text>
<rect x="82" y="44" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="107" y="59" text-anchor="middle" font-size="10" fill="#6B5F4F">6</text>
<rect x="24" y="72" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="49" y="87" text-anchor="middle" font-size="10" fill="#6B5F4F">2</text>
<rect x="82" y="72" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="107" y="87" text-anchor="middle" font-size="10" fill="#6B5F4F">7</text>
<rect x="24" y="100" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="49" y="115" text-anchor="middle" font-size="10" fill="#6B5F4F">3</text>
<rect x="82" y="100" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="107" y="115" text-anchor="middle" font-size="10" fill="#6B5F4F">8</text>
<rect x="24" y="128" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="49" y="143" text-anchor="middle" font-size="10" fill="#6B5F4F">4</text>
<rect x="82" y="128" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="107" y="143" text-anchor="middle" font-size="10" fill="#6B5F4F">9</text>
<rect x="24" y="156" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="49" y="171" text-anchor="middle" font-size="10" fill="#6B5F4F">5</text>
<rect x="82" y="156" width="50" height="22" rx="5" fill="#FFFDF9" stroke="#EBDCC4"/>
<text x="107" y="171" text-anchor="middle" font-size="10" fill="#6B5F4F">10</text>
<text x="76" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">10</text>
<line x1="146" y1="100" x2="182" y2="100" stroke="#6B5F4F" stroke-width="1.6"/>
<polygon points="190,100 180,96 180,104" fill="#6B5F4F"/>
<rect x="196" y="70" width="86" height="60" rx="8" fill="#F7EFE2" stroke="#C9852F"/>
<text x="239" y="105" text-anchor="middle" font-size="12" fill="#332C23" font-weight="600">AI</text>
<line x1="288" y1="100" x2="322" y2="100" stroke="#6B5F4F" stroke-width="1.6"/>
<polygon points="330,100 320,96 320,104" fill="#6B5F4F"/>
<rect x="336" y="66" width="120" height="68" rx="8" fill="#FBE9C8" stroke="#A4553F" stroke-dasharray="5 4"/>
<text x="396" y="106" text-anchor="middle" font-size="22" fill="#A4553F">?</text>
<text x="396" y="84" text-anchor="middle" font-size="10" fill="#A4553F">0 / 10</text>
</g>
</svg>
<figcaption><b>图 A11</b> · 示意：十道题、机器作答，以及缺失的评估协议。</figcaption>
</figure>

## B 组 · 论证的背景板

### B1 · 哥德尔不完备定理（1931）

- **一句话**：任何足够丰富、一致的形式系统，必有它自己证不出的真命题——而且它无法在内部证明自己的一致性。
- **譬喻**：一套法院系统，其中有些案子只能由更高的法院裁决——而包括最高法院在内的任何法院，都无法在其自身规则之内裁定自己的公正。**边界与常见误读**：哥德尔没有证明数学不可靠，也没有证明有些真理永远不可知；他证明的是**自证有界**——任何给定的规则手册都留有它判不了的案子，而且这是构造性证明，不是神秘主义。
- **问的是什么**（已有答案）：形式证明有没有机械边界？有——§3.3 反「数学是终极根据」、§5.4 论彭罗斯争议性援引时都倚重它 [42,43,44]。
- **先修概念**：**形式系统**是规则手册加一套证明检查程序；**一致**指推不出矛盾；**算术上足够丰富**指它能表达关于自然数的陈述。
- **逻辑与语言**：证明把一句自指的话——「本语句在此不可证」——编码进算术；**哥德尔编号**这套语言学机器，正是让规则手册能谈论自己的办法。
- **现状**：已成定论的数学；建立在它之上的哲学论证仍在争论。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A formal system containing a true statement it cannot prove">
<title>A formal system containing a true statement it cannot prove</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="24" y="40" width="220" height="120" rx="10" fill="#FFFDF9" stroke="#6B5F4F" stroke-width="1.6"/>
<text x="40" y="62" text-anchor="start" font-size="12" fill="#332C23" font-weight="600">S</text>
<line x1="46" y1="82" x2="150" y2="82" stroke="#EBDCC4" stroke-width="2"/>
<line x1="46" y1="98" x2="150" y2="98" stroke="#EBDCC4" stroke-width="2"/>
<line x1="46" y1="114" x2="150" y2="114" stroke="#EBDCC4" stroke-width="2"/>
<line x1="46" y1="130" x2="150" y2="130" stroke="#EBDCC4" stroke-width="2"/>
<rect x="160" y="86" width="56" height="34" rx="6" fill="#FBE9C8" stroke="#C9852F"/>
<text x="188" y="108" text-anchor="middle" font-size="12" fill="#332C23" font-weight="600">G</text>
<path d="M216 96 C 250 70, 250 128, 216 110" fill="none" stroke="#A4553F" stroke-dasharray="4 3"/>
<line x1="244" y1="100" x2="300" y2="100" stroke="#A4553F" stroke-dasharray="4 3"/>
<polygon points="308,100 298,96 298,104" fill="#A4553F"/>
<text x="318" y="96" text-anchor="start" font-size="12" fill="#A4553F">S ⊬ G</text>
<text x="318" y="124" text-anchor="start" font-size="12" fill="#A4553F">S ⊬ Con(S)</text>
<text x="318" y="152" text-anchor="start" font-size="11" fill="#6B5F4F">G ⊨ ⊤</text>
</g>
</svg>
<figcaption><b>图 B1</b> · 示意：系统 S 内部有一句它证不出的真语句 G，它也证不出自身的一致性。</figcaption>
</figure>

### B2 · 停机问题（1936）

- **一句话**：没有任何算法能对每个程序与输入判定它是否终将停机。
- **譬喻**：设想一个万能「剧透程序」，能对每部电影预言它是否放得完。给它喂一部「恰在剧透说不会结束时才结束」的电影——矛盾。这部电影就是喂了自己描述的程序。**边界**：悖论作为逻辑无懈可击；它对任何具体程序什么都没说，绝大多数程序都容易分析。
- **问的是什么**（已有答案）：对这道界定明确的问题，存在普适的机械判定程序吗？不存在 [48]。
- **逻辑与语言**：证明是**对角线**式的——针对全称主张构造一个反例；与门槛三的全称/存在形态同款。
- **为什么重要**：与哥德尔一道，合上「形式化能够穷尽数学」的希望——§3.5 与 §5.4 [48]。
- **现状**：已定论；可判定与不可判定的边界仍是一张活地图。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A halting decider fed its own description, and the contradiction">
<title>A halting decider fed its own description, and the contradiction</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<rect x="70" y="66" width="96" height="68" rx="10" fill="#FFFDF9" stroke="#6B5F4F" stroke-width="1.6"/>
<text x="118" y="106" text-anchor="middle" font-size="20" fill="#332C23" font-weight="600">H</text>
<line x1="24" y1="100" x2="62" y2="100" stroke="#6B5F4F" stroke-width="1.6"/>
<polygon points="70,100 60,96 60,104" fill="#6B5F4F"/>
<text x="44" y="90" text-anchor="middle" font-size="11" fill="#6B5F4F">⟨H,H⟩</text>
<line x1="166" y1="88" x2="216" y2="72" stroke="#6B5F4F" stroke-width="1.6"/>
<polygon points="224,70 213,68 216,76" fill="#6B5F4F"/>
<text x="236" y="70" text-anchor="start" font-size="16" fill="#6B5F4F">↓</text>
<line x1="166" y1="112" x2="216" y2="128" stroke="#6B5F4F" stroke-width="1.6"/>
<polygon points="224,130 213,132 216,124" fill="#6B5F4F"/>
<text x="236" y="136" text-anchor="start" font-size="16" fill="#6B5F4F">∞</text>
<path d="M270 140 C 320 190, 20 190, 44 118" fill="none" stroke="#A4553F" stroke-width="1.6" stroke-dasharray="5 4"/>
<text x="160" y="186" text-anchor="middle" font-size="18" fill="#A4553F">⊥</text>
</g>
</svg>
<figcaption><b>图 B2</b> · 示意：停机判定器被喂进自己的描述——两种输出互相矛盾。</figcaption>
</figure>

### B3 · 连续统假设

- **一句话**：整数与连续统之间，还有没有别的大小？
- **譬喻**：一座楼层即一种无穷大小的旅馆：整数住一层，实数连续统住在高得多的一层。CH 问：两者之间是否还有可以入住的夹层？科恩的结果：建筑规范（公理）同时许可「有夹层」与「无夹层」两种图纸，都不违规。**边界**：无穷的大小不是一座塔的楼层；层级比楼房微妙。
- **问的是什么**（已有答案）：康托尔，1878；哥德尔（1940）证明它不能从公理否证；科恩（1963）证明它也不能由此证出——**独立**。
- **逻辑与语言**：这里的「独立」是一条**关于逻辑本身的定理**——通过构造两个模型宇宙证明：一个 CH 成立，一个 CH 不成立 [45]。
- **为什么重要**：§3.3 以科恩的结果说明：连最基础的分支，其公理选择也不是唯一被迫的。
- **现状**：「独立」已成定论；采纳 CH 是立场，不是事实。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="A gap between aleph-null and the continuum, and two consistent models">
<title>A gap between aleph-null and the continuum, and two consistent models</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<line x1="110" y1="176" x2="110" y2="36" stroke="#6B5F4F" stroke-width="1.6"/>
<line x1="92" y1="168" x2="128" y2="168" stroke="#6B5F4F" stroke-width="1.6"/>
<line x1="92" y1="48" x2="128" y2="48" stroke="#6B5F4F" stroke-width="1.6"/>
<line x1="92" y1="108" x2="128" y2="108" stroke="#A4553F" stroke-dasharray="4 4"/>
<text x="84" y="172" text-anchor="end" font-size="12" fill="#332C23">ℵ₀</text>
<text x="84" y="52" text-anchor="end" font-size="12" fill="#332C23">2^ℵ₀</text>
<text x="84" y="112" text-anchor="end" font-size="16" fill="#A4553F">?</text>
<text x="110" y="30" text-anchor="middle" font-size="12" fill="#A4553F">CH</text>
<rect x="240" y="62" width="96" height="54" rx="8" fill="#FFFDF9" stroke="#6B5F4F"/>
<text x="288" y="86" text-anchor="middle" font-size="12" fill="#332C23">CH</text>
<text x="288" y="106" text-anchor="middle" font-size="12" fill="#6B5F4F">✓</text>
<rect x="356" y="62" width="96" height="54" rx="8" fill="#FFFDF9" stroke="#6B5F4F"/>
<text x="404" y="86" text-anchor="middle" font-size="12" fill="#332C23">¬CH</text>
<text x="404" y="106" text-anchor="middle" font-size="12" fill="#6B5F4F">✓</text>
<text x="346" y="146" text-anchor="middle" font-size="11" fill="#9A8D7A">ZFC</text>
</g>
</svg>
<figcaption><b>图 B3</b> · 示意：ℵ₀ 与 2^ℵ₀ 之间的空档；CH 与 ¬CH 都与公理相容。</figcaption>
</figure>

### B4 · 罗素悖论（1901）

- **一句话**：「所有不包含自身的集合组成的集合」——它包含自己吗？
- **譬喻**：村庄理发师「只给不自己刮脸的人刮脸」——谁给理发师刮脸？或「所有不收录自身的目录」的总目录。任一答案都违反定义它的规则。**边界**：理发师有平凡的出路（没人给他刮）；集合版本没有，因为碎掉的是定义本身而非某个人——出路是重建规则。
- **问的是什么**（已有答案）：罗素致弗雷格的信凿穿朴素集合论；类型论与公理化集合论重建了地基。
- **逻辑与语言**：定义里的**自指**缺陷——门槛二的语言学面：一句合语法的句子可能在语义上破产。
- **为什么重要**：§3.1 以它标记逻辑主义的失败——逻辑是数学的语法，不是数学的地基 [36]。
- **现状**：已解决；教训已成为基础理论的常识。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="The set of all sets that do not contain themselves, and its contradiction">
<title>The set of all sets that do not contain themselves, and its contradiction</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<circle cx="120" cy="100" r="50" fill="#F7EFE2" stroke="#C9852F" stroke-width="1.8"/>
<text x="120" y="106" text-anchor="middle" font-size="18" fill="#332C23" font-weight="600">R</text>
<path d="M148 66 C 190 40, 210 96, 160 110" fill="none" stroke="#A4553F" stroke-width="1.6"/>
<polygon points="154,108 166,108 160,118" fill="#A4553F"/>
<text x="196" y="60" text-anchor="middle" font-size="12" fill="#A4553F">R ∈ R ?</text>
<text x="262" y="78" text-anchor="start" font-size="12" fill="#332C23">R ∈ R ⇒ R ∉ R</text>
<text x="262" y="104" text-anchor="start" font-size="12" fill="#332C23">R ∉ R ⇒ R ∈ R</text>
<text x="262" y="140" text-anchor="start" font-size="20" fill="#A4553F">⊥</text>
</g>
</svg>
<figcaption><b>图 B4</b> · 示意：所有不含自身的集合之集——任一答案都破坏定义。</figcaption>
</figure>

### B5 · 开普勒猜想

- **一句话**：杂货店堆橙子的方式，就是等球堆得最密的方式。
- **譬喻**：水果摊。开普勒 1611 年猜到它；摊贩的实践比定理领先了四个世纪。**边界**：猜想说的是**无穷空间**与**一切可以设想的摆法**——不只是摊子能摆出的整齐那几种；这种普遍性正是它花了四百年、最后要靠计算机的原因。
- **问的是什么**（已有答案）：黑尔斯 1998 年宣布证明；审稿人「99% 确信」；机器核验的 Flyspeck 证明 2014 年完成、2017 年发表。
- **先修概念**：**堆积密度**是空间被占据的比例，对所有摆法取最大。
- **为什么重要**：§5.3 以多年的核验劳动为「核验应当付酬」的价码——这类劳动至今是学科里报酬最低的一档 [66]。
- **现状**：已证明、已机器核验；历史上第一个以此方式认证的重大定理。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Hexagonal close packing cross-section and the proof timeline">
<title>Hexagonal close packing cross-section and the proof timeline</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<circle cx="130" cy="100" r="26" fill="#F7EFE2" stroke="#C9852F" stroke-width="1.8"/>
<circle cx="182.0" cy="100.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<circle cx="156.0" cy="145.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<circle cx="104.0" cy="145.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<circle cx="78.0" cy="100.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<circle cx="104.0" cy="55.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<circle cx="156.0" cy="55.0" r="26" fill="#FFFDF9" stroke="#407CB0" stroke-width="1.4"/>
<polygon points="156,115 130,130 104,115 104,85 130,70 156,85" fill="none" stroke="#A4553F" stroke-dasharray="4 3"/>
<text x="130" y="190" text-anchor="middle" font-size="12" fill="#332C23">π / (3√2) ≈ 0.7405</text>
<line x1="270" y1="100" x2="500" y2="100" stroke="#EBDCC4"/>
<circle cx="300" cy="100" r="4" fill="#C9852F"/>
<text x="300" y="124" text-anchor="middle" font-size="10" fill="#6B5F4F">1611</text>
<circle cx="380" cy="100" r="4" fill="#C9852F"/>
<text x="380" y="124" text-anchor="middle" font-size="10" fill="#6B5F4F">1998</text>
<circle cx="460" cy="100" r="4" fill="#C9852F"/>
<text x="460" y="124" text-anchor="middle" font-size="10" fill="#6B5F4F">2014</text>
</g>
</svg>
<figcaption><b>图 B5</b> · 示意：最密堆积的六边形截面，密度 π/(3√2) ≈ 0.7405；右侧为证明时间线。</figcaption>
</figure>

### B6 · 罗宾斯问题

- **一句话**：三条关于一个布尔运算的简单等式，能否穷尽全部布尔代数？
- **譬喻**：三根帐篷柱能否撑起开关逻辑的整个穹顶？柱子看上去太少——这正是趣味与困难所在：六十年间，人手既证不出「三柱够用」，也证不出「三柱不够」。1996 年，麦库恩的自动证明器 EQP 找到了证明。**边界**：穹顶画面暗示体量；真正的困难是找到那条关键的中介引理——一次搜索，恰是机器擅长的事。
- **问的是什么**（已有答案）：罗宾斯，1933；EQP 于 1996 年解决 [65]。
- **逻辑与语言**：一条**等价**主张——「这三条公理恰好定义布尔代数」——需要两个方向的证明：布尔代数的一切可由三条推出，且三条在布尔代数中成立。
- **为什么重要**：§5.3 把它列在「机器接手检查与执行、人相应转移阵地」的谱系里。
- **现状**：已被机器证明——AI 数学浪潮正是把这个先例又推高一层。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Three axiom poles holding up the dome of Boolean algebra">
<title>Three axiom poles holding up the dome of Boolean algebra</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<path d="M70 92 Q 160 34 250 92" fill="none" stroke="#C9852F" stroke-width="2"/>
<line x1="100" y1="150" x2="100" y2="76" stroke="#6B5F4F" stroke-width="2.4"/>
<text x="100" y="168" text-anchor="middle" font-size="10" fill="#6B5F4F">A1</text>
<line x1="160" y1="150" x2="160" y2="63" stroke="#6B5F4F" stroke-width="2.4"/>
<text x="160" y="168" text-anchor="middle" font-size="10" fill="#6B5F4F">A2</text>
<line x1="220" y1="150" x2="220" y2="76" stroke="#6B5F4F" stroke-width="2.4"/>
<text x="220" y="168" text-anchor="middle" font-size="10" fill="#6B5F4F">A3</text>
<text x="160" y="58" text-anchor="middle" font-size="12" fill="#332C23">B</text>
<text x="40" y="168" text-anchor="start" font-size="10" fill="#9A8D7A">1933</text>
<text x="280" y="168" text-anchor="start" font-size="10" fill="#9A8D7A">1996</text>
<line x1="24" y1="150" x2="300" y2="150" stroke="#EBDCC4"/>
</g>
</svg>
<figcaption><b>图 B6</b> · 示意：三根公理柱撑起布尔代数的穹顶。</figcaption>
</figure>

### B7 · 素数有界间隙（与陈景润定理）

- **一句话**：相邻素数的间隙，最小能多小——而且无穷多次出现？
- **譬喻**：素数像到站时刻不定的公交车。张益唐证明（2014）：存在某个有限区间——他的是七千万——其中两班车几乎同时进站，且这样的事**无穷多次**发生。Polymath 项目与梅纳德把区间缩到 246；截至 2026 年 8 月，纪录是 240（Stadlmann, arXiv:2608.31126）。孪生素数猜想是把区间换成 2 的同一主张——仍未解。陈景润定理（1973）是相邻的丰碑：每个大偶数都是一个素数加至多两个素数之积（「1+2」）。**边界**：「无穷多次」说的是整条无穷直线，不是你走得到的任何一段。
- **问的是什么**：最小的 H₁，使无穷多对素数的差不超过 H₁。
- **先修概念**：「无穷多次」的量词形状——不是「有很多」，而是「无论走到多远，它们还在发生」。
- **为什么重要**：§4.2 与 §6.2 以这一谱系说明筛法与加法组合学的活力 [57,58,72]。相关条目详见 [哥德巴赫与孪生素数](../famous_problems/goldbach_and_twin_primes.md)。
- **现状（2026-11-22）**：纪录 240（Stadlmann）；孪生素数仍未解。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Primes on a line, a twin gap of two, and a bounded gap of 240">
<title>Primes on a line, a twin gap of two, and a bounded gap of 240</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<line x1="20" y1="110" x2="500" y2="110" stroke="#6B5F4F"/>
<line x1="30" y1="104" x2="30" y2="116" stroke="#6B5F4F"/>
<text x="30" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">2</text>
<line x1="75" y1="104" x2="75" y2="116" stroke="#6B5F4F"/>
<text x="75" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">3</text>
<line x1="120" y1="104" x2="120" y2="116" stroke="#6B5F4F"/>
<text x="120" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">5</text>
<line x1="165" y1="104" x2="165" y2="116" stroke="#6B5F4F"/>
<text x="165" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">7</text>
<line x1="210" y1="104" x2="210" y2="116" stroke="#6B5F4F"/>
<text x="210" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">11</text>
<line x1="255" y1="104" x2="255" y2="116" stroke="#6B5F4F"/>
<text x="255" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">13</text>
<line x1="300" y1="104" x2="300" y2="116" stroke="#6B5F4F"/>
<text x="300" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">17</text>
<line x1="345" y1="104" x2="345" y2="116" stroke="#6B5F4F"/>
<text x="345" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">19</text>
<line x1="390" y1="104" x2="390" y2="116" stroke="#6B5F4F"/>
<text x="390" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">23</text>
<line x1="435" y1="104" x2="435" y2="116" stroke="#6B5F4F"/>
<text x="435" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">29</text>
<line x1="480" y1="104" x2="480" y2="116" stroke="#6B5F4F"/>
<text x="480" y="136" text-anchor="middle" font-size="10" fill="#6B5F4F">31</text>
<path d="M210 96 L210 88 L255 88 L255 96" fill="none" stroke="#A4553F"/>
<text x="232" y="80" text-anchor="middle" font-size="10" fill="#A4553F">2</text>
<path d="M300 62 L300 52 L480 52 L480 62" fill="none" stroke="#C9852F" stroke-dasharray="4 3"/>
<text x="390" y="44" text-anchor="middle" font-size="12" fill="#C9852F">≤ 240</text>
<text x="390" y="176" text-anchor="middle" font-size="14" fill="#9A8D7A">∞</text>
</g>
</svg>
<figcaption><b>图 B7</b> · 示意：素数排成一线；孪生间隙 2 与有界间隙 240（后者无穷多次出现）。</figcaption>
</figure>

### B8 · 韦尔猜想

- **一句话**：数有限域上多项式方程的解，并在算术深处找到拓扑。
- **譬喻**：在一块有限棋盘上反反复复数棋局，棋盘越来越大——然后发现，计数的**节律**竟由一个你从未见过的形状的「孔与柄」支配。韦尔猜想：节律遵循一条 zeta 型函数、带着黎曼假设式的规整；德利涅 1974 年证明最难的那部分。**边界**：「隐藏的形状」是代数簇，不是棋盘；这个譬喻解释了为什么人们说这个结果是「拓扑借算术之口说话」。
- **问的是什么**（已有答案）：韦尔，1949；德利涅证明最后也最难的部分（有限域上的黎曼假设）于 1974 [56]。
- **先修概念**：**有限域**是字母表大小固定、一切运算到点回卷的算术（钟表算术的推广）；**簇的 zeta 函数**是一次性编码所有棋盘尺寸计数的生成装置——A4 那个 ζ 的几何亲戚。
- **为什么重要**：§4.2 以德利涅的证明作为算术几何的里程碑——朗兰兹纲领周边那片疆域的界碑。
- **现状**：已证明；其后裔（几何朗兰兹）仍是数学最深处的活疆域。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Point counts over finite fields and a torus with its Betti numbers">
<title>Point counts over finite fields and a torus with its Betti numbers</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<circle cx="40" cy="60" r="3" fill="#EBDCC4"/>
<circle cx="40" cy="86" r="3" fill="#EBDCC4"/>
<circle cx="40" cy="112" r="3" fill="#EBDCC4"/>
<circle cx="40" cy="138" r="3" fill="#EBDCC4"/>
<circle cx="40" cy="164" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="60" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="86" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="112" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="138" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="164" r="3" fill="#EBDCC4"/>
<circle cx="92" cy="60" r="3" fill="#EBDCC4"/>
<circle cx="92" cy="86" r="3" fill="#EBDCC4"/>
<circle cx="92" cy="112" r="3" fill="#EBDCC4"/>
<circle cx="92" cy="138" r="3" fill="#EBDCC4"/>
<circle cx="92" cy="164" r="3" fill="#EBDCC4"/>
<circle cx="118" cy="60" r="3" fill="#EBDCC4"/>
<circle cx="118" cy="86" r="3" fill="#EBDCC4"/>
<circle cx="118" cy="112" r="3" fill="#EBDCC4"/>
<circle cx="118" cy="138" r="3" fill="#EBDCC4"/>
<circle cx="118" cy="164" r="3" fill="#EBDCC4"/>
<circle cx="144" cy="60" r="3" fill="#EBDCC4"/>
<circle cx="144" cy="86" r="3" fill="#EBDCC4"/>
<circle cx="144" cy="112" r="3" fill="#EBDCC4"/>
<circle cx="144" cy="138" r="3" fill="#EBDCC4"/>
<circle cx="144" cy="164" r="3" fill="#EBDCC4"/>
<circle cx="66" cy="86" r="5" fill="#C9852F"/>
<circle cx="118" cy="86" r="5" fill="#C9852F"/>
<circle cx="66" cy="138" r="5" fill="#C9852F"/>
<circle cx="144" cy="164" r="5" fill="#C9852F"/>
<text x="90" y="196" text-anchor="middle" font-size="12" fill="#332C23">N₁ N₂ …</text>
<ellipse cx="360" cy="104" rx="86" ry="46" fill="none" stroke="#407CB0" stroke-width="2"/>
<ellipse cx="360" cy="104" rx="30" ry="14" fill="none" stroke="#407CB0" stroke-width="2"/>
<text x="360" y="176" text-anchor="middle" font-size="11" fill="#332C23">b: 1 · 2 · 1</text>
<text x="360" y="40" text-anchor="middle" font-size="12" fill="#C9852F">Z(V, t)</text>
</g>
</svg>
<figcaption><b>图 B8</b> · 示意：有限域上的点计数汇入 zeta 函数；形状的孔（贝蒂数）支配节律。</figcaption>
</figure>

### B9 · 圆周率：刘徽与祖冲之

- **一句话**：圆的比率能算到多精——以及用什么方法算？
- **譬喻**：用直的栅栏围出一个圆：六边形，再十二边形，再二十四——刘徽的「割圆术」，每割一次就更贴一点圆的圆润。祖冲之（五世纪）推到密率 355/113：按地球周长算，误差不足十一米。欧洲得到同样的精度要再等一千年。**边界**：栅栏画面展示的是**上下界合拢**；§5.5 更深的要点在方法——同一个真理，由一条算法性路径抵达，而对「什么算一份解答」的想法不同。
- **问的是什么**（已有答案）：π 是无理数也是超越数；史学之问——哪些传统、哪些方法——才是本文的 [50,69]。
- **为什么重要**：§5.5 以中国传统为「算法性、构造性路径」的证据——差别在什么使一份解答算数，不在什么为真。
- **现状**：数值上已算至万亿位；文章的史学论点依旧成立。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Inscribed and circumscribed hexagons closing on the circle">
<title>Inscribed and circumscribed hexagons closing on the circle</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<circle cx="140" cy="100" r="60" fill="none" stroke="#6B5F4F" stroke-width="2"/>
<polygon points="200.0,100.0 170.0,152.0 110.0,152.0 80.0,100.0 110.0,48.0 170.0,48.0" fill="none" stroke="#407CB0" stroke-dasharray="5 4"/>
<polygon points="200.0,134.6 140.0,169.3 80.0,134.6 80.0,65.4 140.0,30.7 200.0,65.4" fill="none" stroke="#C9852F" stroke-dasharray="2 4"/>
<text x="140" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">n = 6</text>
<text x="280" y="74" text-anchor="start" font-size="11" fill="#332C23">3.14159265…</text>
<text x="280" y="100" text-anchor="start" font-size="11" fill="#C9852F">355/113</text>
<text x="280" y="126" text-anchor="start" font-size="11" fill="#6B5F4F">= 3.14159292…</text>
</g>
</svg>
<figcaption><b>图 B9</b> · 示意：内接与外切六边形向圆合拢；355/113 为经典界。</figcaption>
</figure>

### B10 · 喀拉拉学派的无穷级数

- **一句话**：正弦、余弦与 π 的幂级数——在牛顿与莱布尼茨之前的几个世纪，已在印度写成。
- **譬喻**：一份用无穷多条简单「窄条」拼出圆润形状的配方——「配方」就是级数；喀拉拉学派（马达瓦及其后继者，十四至十六世纪）在欧洲之前很久就写下了正弦、余弦与 π 的配方，但没有把它们装配成后来叫作微积分的那台通用机器。**边界**：配方画面不可暗示「结果相同、只是更早」的制度判断——§5.5 的要点恰是：机器与配方是两种不同的成就。
- **问的是什么**（已有答案）：史学上已成定论；文章用它对抗「现代西方数学＝数学本身」的等式 [50,70]。
- **逻辑与语言**：无穷级数是带极限的主张——「部分和逼近……」；逼近什么、以多快的速度——这正是门槛二所教的那种语法细心。
- **为什么重要**：§5.5 以喀拉拉为证据：同一种数学可以在不止一种建制形态下生长。
- **现状**：史学上已成定论。

<figure class="fig">
<svg viewBox="0 0 520 200" role="img" aria-label="Sine and its successive partial sums from the power series">
<title>Sine and its successive partial sums from the power series</title>
<g font-family="Inter, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif" font-size="12" fill="#6B5F4F">
<line x1="40" y1="110" x2="480" y2="110" stroke="#EBDCC4"/>
<line x1="260" y1="40" x2="260" y2="180" stroke="#EBDCC4"/>
<polyline points="60.0,267.1 66.7,261.8 73.3,256.6 80.0,251.4 86.7,246.1 93.3,240.9 100.0,235.7 106.7,230.4 113.3,225.2 120.0,220.0 126.7,214.7 133.3,209.5 140.0,204.2 146.7,199.0 153.3,193.8 160.0,188.5 166.7,183.3 173.3,178.1 180.0,172.8 186.7,167.6 193.3,162.4 200.0,157.1 206.7,151.9 213.3,146.7 220.0,141.4 226.7,136.2 233.3,130.9 240.0,125.7 246.7,120.5 253.3,115.2 260.0,110.0 266.7,104.8 273.3,99.5 280.0,94.3 286.7,89.1 293.3,83.8 300.0,78.6 306.7,73.3 313.3,68.1 320.0,62.9 326.7,57.6 333.3,52.4 340.0,47.2 346.7,41.9 353.3,36.7 360.0,31.5 366.7,26.2 373.3,21.0 380.0,15.8 386.7,10.5 393.3,5.3 400.0,0.0 406.7,-5.2 413.3,-10.4 420.0,-15.7 426.7,-20.9 433.3,-26.1 440.0,-31.4 446.7,-36.6 453.3,-41.8 460.0,-47.1" fill="none" stroke="#6B5F4F" stroke-width="1.2" stroke-dasharray="2 5"/>
<polyline points="60.0,8.7 66.7,28.4 73.3,46.5 80.0,63.0 86.7,77.9 93.3,91.4 100.0,103.4 106.7,114.0 113.3,123.3 120.0,131.3 126.7,138.2 133.3,143.8 140.0,148.4 146.7,152.0 153.3,154.6 160.0,156.2 166.7,157.0 173.3,157.0 180.0,156.3 186.7,154.9 193.3,152.8 200.0,150.1 206.7,147.0 213.3,143.4 220.0,139.3 226.7,135.0 233.3,130.3 240.0,125.4 246.7,120.4 253.3,115.2 260.0,110.0 266.7,104.8 273.3,99.6 280.0,94.6 286.7,89.7 293.3,85.0 300.0,80.7 306.7,76.6 313.3,73.0 320.0,69.9 326.7,67.2 333.3,65.1 340.0,63.7 346.7,63.0 353.3,63.0 360.0,63.8 366.7,65.4 373.3,68.0 380.0,71.6 386.7,76.2 393.3,81.8 400.0,88.7 406.7,96.7 413.3,106.0 420.0,116.6 426.7,128.6 433.3,142.1 440.0,157.0 446.7,173.5 453.3,191.6 460.0,211.3" fill="none" stroke="#407CB0" stroke-width="1.6" stroke-dasharray="5 4"/>
<polyline points="60.0,136.2 66.7,136.1 73.3,136.8 80.0,138.3 86.7,140.3 93.3,142.6 100.0,145.2 106.7,147.8 113.3,150.3 120.0,152.8 126.7,155.0 133.3,156.8 140.0,158.4 146.7,159.4 153.3,160.1 160.0,160.2 166.7,159.9 173.3,159.0 180.0,157.6 186.7,155.7 193.3,153.3 200.0,150.5 206.7,147.2 213.3,143.5 220.0,139.4 226.7,135.0 233.3,130.3 240.0,125.5 246.7,120.4 253.3,115.2 260.0,110.0 266.7,104.8 273.3,99.6 280.0,94.5 286.7,89.7 293.3,85.0 300.0,80.6 306.7,76.5 313.3,72.8 320.0,69.5 326.7,66.7 333.3,64.3 340.0,62.4 346.7,61.0 353.3,60.1 360.0,59.8 366.7,59.9 373.3,60.6 380.0,61.6 386.7,63.2 393.3,65.0 400.0,67.2 406.7,69.7 413.3,72.2 420.0,74.8 426.7,77.4 433.3,79.7 440.0,81.7 446.7,83.2 453.3,83.9 460.0,83.8" fill="none" stroke="#C9852F" stroke-width="1.6" stroke-dasharray="8 3 2 3"/>
<polyline points="60.0,110.0 66.7,115.2 73.3,120.4 80.0,125.5 86.7,130.3 93.3,135.0 100.0,139.4 106.7,143.5 113.3,147.2 120.0,150.5 126.7,153.3 133.3,155.7 140.0,157.6 146.7,158.9 153.3,159.7 160.0,160.0 166.7,159.7 173.3,158.9 180.0,157.6 186.7,155.7 193.3,153.3 200.0,150.5 206.7,147.2 213.3,143.5 220.0,139.4 226.7,135.0 233.3,130.3 240.0,125.5 246.7,120.4 253.3,115.2 260.0,110.0 266.7,104.8 273.3,99.6 280.0,94.5 286.7,89.7 293.3,85.0 300.0,80.6 306.7,76.5 313.3,72.8 320.0,69.5 326.7,66.7 333.3,64.3 340.0,62.4 346.7,61.1 353.3,60.3 360.0,60.0 366.7,60.3 373.3,61.1 380.0,62.4 386.7,64.3 393.3,66.7 400.0,69.5 406.7,72.8 413.3,76.5 420.0,80.6 426.7,85.0 433.3,89.7 440.0,94.5 446.7,99.6 453.3,104.8 460.0,110.0" fill="none" stroke="#332C23" stroke-width="2"/>
<text x="140" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">−π</text>
<text x="380" y="190" text-anchor="middle" font-size="12" fill="#6B5F4F">π</text>
<text x="470" y="32" text-anchor="end" font-size="10" fill="#C9852F">x − x³/3! + x⁵/5! …</text>
</g>
</svg>
<figcaption><b>图 B10</b> · 示意：sin x 与其逐次部分和——每添一项，就更贴曲线一点。</figcaption>
</figure>

<!-- L1-end -->

<!-- 新来源备注：B7 的 Stadlmann 引用以行内署名给出（长稿来源表之外，不占编号）；其余方括号编号一律指向 proofs_no_longer_scarce.md 文末来源表。A1 现状栏曾依另一会话 T2 检索记录更正；2026-11-23 无外力 Euler 归属经一手核实落定（长稿新增 [130]），本页与长稿一致。 -->
