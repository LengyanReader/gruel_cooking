# 文中的数学问题：一页看懂 / The problems in the essay: a one-page field guide

<!-- 姊妹页（companion page）：为长稿《各归各位：证明的归机器，理解的归人》（proofs_no_longer_scarce.md）中出现的全部数学问题做一页普通读者友好的导览。每题五栏：一句话 / 前提·背景 / 问的是什么 / 为什么重要 / 现状。AI 起草、未经作者逐条复核（harness §I.6）；「现状」栏事实均核于 2026-11-22，方括号编号指向该长稿文末来源表（[1]–[128]），标注「详见」处链接 math_clarification 内既有条目（§II.9 单一来源：概念正文不在本页重复）。双语逐段并列，英文侧与中文侧内容与精神对应。 -->

<!-- en -->

## Foreword

The essay this page accompanies tells a story about machines, proofs, and the people who check them — and the story walks through a crowd of specific mathematical problems: a Millennium Prize equation, an eighty-year-old combinatorial conjecture, a geometry question about seven-dimensional spheres, a counting problem about kisses in eleven dimensions. Most news coverage assumes you already know what these problems are. This page assumes you do not.

Each problem below gets five fields: **in one line** (the problem compressed), **background** (who asked it, when, and out of what), **what is asked** (the question stated as plainly as precision allows), **why it matters** (what hangs on it, and where it appears in the essay), and **status** (where things stand as of 22 November 2026, with the essay's source numbers in brackets). Group A collects the problems that are actors in the essay's events; Group B collects the ones cited as background and evidence in its arguments. Where the cookbook already has a full entry for a problem, this page links to it rather than duplicating it.

<!-- zh -->

## 导读

本页所配套的那篇长文，讲的是机器、证明与核验者之间的故事——而故事里走过一群具体的数学问题：一道千禧年大奖难题、一个悬置八十年的组合猜想、一个关于七维球面的几何问题、一个数十一维空间里「接吻」的计数问题。绝大多数报道默认你早已知道这些问题是什么；本页默认你并不知道。

下面每个问题给五栏：**一句话**（问题压缩成一行）、**前提·背景**（谁、何时、出于什么提出）、**问的是什么**（在精确允许的范围内说得最平白）、**为什么重要**（利害何在、它在文章中何处出场）、**现状**（截至 2026 年 11 月 22 日的进展，方括号为长文来源编号）。A 组收录的是文中事件里的「主角」问题；B 组收录的是文中论证援引的「背景板」问题。凡本册（math_clarification）已有完整条目者，本页只链接、不重复。

<!-- L1 -->

<!-- en -->

## Group A · The actors

### A1 · Navier–Stokes existence and smoothness

- **In one line**: do the equations of fluid flow always behave, or can they blow up?
- **Background**: Claude-Louis Navier (1822) and George Stokes (1845) wrote down the equations governing viscous fluids — the water in a pipe, the air over a wing. Whether every smooth flow described by them stays smooth forever, or develops a singularity (infinite velocity) in finite time, has been open for over a century and carries one of the seven Clay Millennium Prizes (2000).
- **What is asked**: in three dimensions, do solutions exist for all time and remain smooth — or can they develop singularities?
- **Why it matters**: it is the essay's central case (§1.7, §2.2) — a September 2026 announcement compressed a technical truth, a commercial race, an authorship dispute and a priority quarrel into one week [1,5,6].
- **Status (22 Nov 2026)**: the Clay page still labels the problem Active [4]. OpenAI's 8 September claim — a machine blow-up proof for statements "C/D" of Clay's formulation, Lean-checked but with a forcing term [1] — was found by a Cambridge team not to match its own natural-language text [118]; the method did not obviously extend to the unforced case [5]. On 20 November, unforced blow-up proofs for 3D Euler (Alpöge, Buckmaster, Coiculescu) and 3D Navier–Stokes (Alpöge, Buckmaster) were announced, with Lean formalizations in public repositories [120,121]. No prize has been claimed.

### A2 · The Erdős unit distance conjecture (1946)

- **In one line**: among n points in the plane, how many pairs can be exactly distance 1 apart?
- **Background**: Paul Erdős asked in 1946; his grid construction gives about n^(1+c/log log n) unit distances, and he conjectured that is essentially the whole truth: u(n) ≤ n^(1+o(1)).
- **What is asked**: is the maximum number of unit distances among n plane points sub-polynomially more than n?
- **Why it matters**: in May 2026 it became the first core-field conjecture disproved by an AI system — the essay's "act three" (§1.5) and its sharpest case of machine-proposed, human-digested mathematics [19,20].
- **Status (22 Nov 2026)**: disproved. Alon, Bloom, Gowers and others published a human-verified digest of the OpenAI-generated counterexample (u(n) ≥ n^(1+ε) infinitely often); Sawin made the exponent explicit at n^1.014; the classical upper bound O(n^(4/3)) is untouched [19,20]. Full entry: [Erdős Unit Distance](../famous_problems/erdos_unit_distance.md).

### A3 · Fermat's Last Theorem — and its formalization

- **In one line**: x^n + y^n = z^n has no positive integer solutions for n ≥ 3 — and in 2026 a machine wrote out the entire proof in a language a computer can check.
- **Background**: conjectured by Fermat around 1637 in a margin too narrow for his proof; proved by Andrew Wiles (with Richard Taylor) in 1994–95 after 358 years. Full entry: [Fermat's Last Theorem](../fermat_last_theorem.md).
- **What is asked** (2026 version): can Wiles's proof be re-derived from Lean's three standard axioms alone, with no human trust anywhere in the chain?
- **Why it matters**: the essay's §1.8 uses it as the extreme specimen of the verification bottleneck — an artifact no human can read end-to-end [25,26].
- **Status (22 Nov 2026)**: Anthropic announced (4 September) a complete Lean formalization: about 13 million lines, roughly 29,500 intermediate lemmas, eleven days of largely autonomous work, checked by the Lean kernel and confirmed to match Mathlib's statement of the theorem; Kevin Buzzard reviewed it and called it an extraordinary autoformalization achievement that adds nothing mathematically new [25,26].

### A4 · The Riemann Hypothesis

- **In one line**: do all the "interesting" zeros of the zeta function sit on one straight line?
- **Background**: Bernhard Riemann (1859) noticed that the error term in the prime-counting theorem is governed by the zeros of his zeta function; he conjectured they all lie on the line Re(s) = 1/2. It is the most famous open problem in mathematics and one of the seven Millennium Prizes.
- **What is asked**: do all nontrivial zeros of ζ(s) have real part exactly 1/2?
- **Why it matters**: the essay's §6.4 uses "will AI prove the Riemann hypothesis" as the question to look past; November 2026 answered a version of it in an unexpected way [93,120,122].
- **Status (22 Nov 2026)**: a proof was announced on 20 November by Levent Alpöge, produced with an internal AI model (press names Claude; Tao's wording says "an internal AI model" — both recorded [120,123]); it exists as a ~17-million-line Lean artifact, and on 21 November the Lean community certified by four stated criteria that "both the statement and the proof of the Riemann Hypothesis are correct" [122]. Earlier in the window, a "quasi-RH" result (zeros off the line confined to 1/8 < Re(s) < 7/8) from the October release was digested and largely confirmed by human analysts within two weeks [115]. The Association for Human Mathematics objected that no human can responsibly claim to understand such a document [124]. Machine-verified; community-certified; human understanding in progress.

### A5 · The Unique Games Conjecture (2002)

- **In one line**: is a certain "guess the labels" problem nearly as hard to approximately solve as it is to solve exactly?
- **Background**: posed by Subhash Khot in 2002. If true, it implies that many approximation problems (Max Cut among them) are provably hard to approximate — it has become the hinge of theoretical computer science's hardness program.
- **What is asked**: for constraint systems with a small fraction of violations allowed, is finding a labeling satisfying most constraints computationally intractable?
- **Why it matters**: the 6 October release claimed a proof of it among its 372 families — the most consequential single claim in the batch (§xi of the postscript) [93].
- **Status (22 Nov 2026)**: released claim, not an accepted theorem. Dana Moshkovitz has spent weeks on the proof with Khot, Håstad and Minzer (and the GPT-6 Astra model), confronting what she calls a totally alien new error-correcting code; the effort was presented at the Simons Institute; no full verification has been declared [119].

### A6 · The Jacobian conjecture (1939)

- **In one line**: if a polynomial map has a constant nonzero Jacobian, must it have a polynomial inverse?
- **Background**: asked by Ott-Heinrich Keller in 1939; trivially true in one dimension, open in two for nearly a century, with false "proofs" accumulating on both sides.
- **What is asked**: for which dimensions n does a polynomial map C^n → C^n with constant nonzero Jacobian determinant necessarily admit a polynomial inverse?
- **Why it matters**: the essay's §2.1 lists its July 2026 counterexample as one of the machine-proof dramas preceding the Fields medalists' letter [1,19,30].
- **Status (22 Nov 2026)**: false for n ≥ 3. Levent Alpöge announced a three-variable counterexample on 19 July 2026, found with the help of an AI model; Tao wrote a public digestion of it the next day [106]; Gao generalized counterexamples to every dimension greater than two, with all identities verified in exact rational arithmetic [107]; Buzzard's group saw the counterexample Lean-checked within days of its announcement [108]. n = 2 remains open.

### A7 · Positive sectional curvature on all smooth 7-spheres

- **In one line**: can every exotic seven-dimensional sphere be given a geometry where all directions curve positively?
- **Background**: in 1956 John Milnor discovered the 7-sphere carries 28 distinct smooth structures — same topology, different differentiable calculus. Whether every one admits a Riemannian metric of strictly positive sectional curvature (all two-dimensional slices bend the same way, like a sphere and unlike a saddle) was a long-standing test case for how topology constrains geometry.
- **What is asked**: construct, for each of the 28 oriented diffeomorphism classes of smooth homotopy 7-spheres, a metric of strictly positive sectional curvature.
- **Why it matters**: the essay's postscript (§iv) records it as a boundary case — inside the essay's period, with its AI acknowledgment surfacing late [82,83].
- **Status (22 Nov 2026)**: claimed in a preprint (24 September) by Yang-Hui He, Ziran Liu and Shing-Tung Yau, gluing two positively curved 7-disks with matching boundary metrics; the paper acknowledges suggestions from GPT and Claude [82,83]. Follow-up work extends the technique; no community verdict either way.

### A8 · Matrix multiplication, 4×4 complex: 49 to 48

- **In one line**: how many scalar multiplications are needed to multiply two 4×4 complex matrices?
- **Background**: Volker Strassen's 1969 algorithm did it in 49 multiplications, beating the textbook 64 and founding algebraic complexity theory; his record stood for 56 years.
- **What is asked**: find the smallest known number of scalar multiplications for the 4×4 complex case — each reduction compounds across every larger matrix product.
- **Why it matters**: the essay's §1.4 uses AlphaEvolve's 48 as the emblem of results at the compute-verify end, where no expert judgment is needed [16].
- **Status (22 Nov 2026)**: 48, found by DeepMind's AlphaEvolve (May 2025), still the record; a follow-up line re-derives it with rational coefficients only. Note the fine print: 48 is the best known algorithm (an upper bound), not a proven minimum for the tensor rank.

### A9 · The kissing number in eleven dimensions

- **In one line**: how many unit spheres can touch a central unit sphere at once, in 11-dimensional space?
- **Background**: the "kissing number" is ancient in 3 dimensions (13, famously argued by Newton and Gregory); exact values are known only in dimensions 1, 2, 3, 4, 8 and 24.
- **What is asked**: determine the maximum number of non-overlapping unit spheres touching a central one in R^11.
- **Why it matters**: the essay's §1.4 pairs it with matrix multiplication as a mechanically checkable record [16].
- **Status (22 Nov 2026)**: lower bound 593 (AlphaEvolve, May 2025, replacing 592), upper bound 868; exact value unknown. A later paper claims 604; it is not yet reflected in standard references and is unverified for this page's purposes [16].

### A10 · Nine-loop hexagon amplitudes (and a single-minus aside)

- **In one line**: compute a fearsomely complex scattering amplitude in the toy model of quantum field theory — nine quantum loops deep.
- **Background**: planar N=4 super Yang–Mills is the "hydrogen atom" of modern field theory; its six-particle "hexagon" amplitudes at loop order L grow astronomically complex. The previous record, eight loops, was set by Lance Dixon and Andy Liu in 2023, by the "bootstrap" method — imposing consistency conditions until the answer is forced.
- **What is asked**: compute the nine-loop hexagon amplitude (and in the aside, decide whether a certain one-minus gluon tree amplitude is nonzero at all).
- **Why it matters**: the essay's §1.7 reads the two 2026 physics cases as live specimens of machine-executed-recipe versus machine-proposed-conjecture [23,24].
- **Status (22 Nov 2026)**: Anthropic announced (25 September) Claude computing the nine-loop amplitude, validated independently by Dixon over roughly two weeks; a CAS team led by Song He obtained most of the result concurrently, using GPT-6 for part of the constraints [24]. In the aside, a 2026 preprint reports the single-minus gluon tree amplitude formula first conjectured by GPT-5.2 Pro and then proved by an OpenAI internal model [23].

### A11 · First Proof: ten research-level questions

- **In one line**: can a machine solve problems its own examiners care about?
- **Background**: a 2026 challenge organized by eleven research mathematicians, posing ten questions that arose in their own research — deliberately not contest problems, not benchmarks written to be solved.
- **What is asked**: how many of the ten can machine-generated answers settle — and who can tell?
- **Why it matters**: the essay's §1.6 and §6.4 use it as the cleanest statement of the verification bottleneck: the reported difficulty was in evaluation, not generation [22].
- **Status (22 Nov 2026)**: the generation half stands; the evaluation half remains unfinished public business, and the organizers concede no protocol yet exists for measuring autonomous problem-posing [22].

## Group B · The background

### B1 · Gödel's incompleteness theorems (1931)

- **In one line**: any consistent system rich enough for arithmetic contains true statements it cannot prove — and cannot certify its own consistency.
- **Background**: Kurt Gödel, reacting to Hilbert's program of securing all of mathematics on formal foundations.
- **What is asked** (answered): are there mechanical limits to formal proof? Yes — the essay leans on this twice (§3.3 against "mathematics as ultimate ground", §5.4 on Penrose's contested use of it) [42,43,44].
- **Status**: settled mathematics; the philosophical arguments built on it remain contested.

### B2 · The halting problem (1936)

- **In one line**: no algorithm can decide, for every program and input, whether the program eventually stops.
- **Background**: Alan Turing, in the paper that defined computation itself.
- **What is asked** (answered): is there a universal mechanical decision procedure for this well-defined question? No [48].
- **Why it matters**: with Gödel, it closes the "formalization can exhaust mathematics" hope — the essay's §3.5 and §5.4 [48].

### B3 · The continuum hypothesis

- **In one line**: is there a size of infinity strictly between the integers' and the continuum's?
- **Background**: Georg Cantor, 1878. Gödel (1940) showed it cannot be disproved from the standard axioms; Paul Cohen (1963) showed it cannot be proved from them either — it is independent.
- **Why it matters**: the essay's §3.3 uses Cohen's result to show even the most foundational branch has axiomatic choices not uniquely forced [45].
- **Status**: settled as independence; which axiom to adopt remains a live stance, not a fact.

### B4 · Russell's paradox (1901)

- **In one line**: the set of all sets that do not contain themselves — contains itself or not?
- **Background**: Bertrand Russell's letter to Gottlob Frege, puncturing naive set theory at its foundation.
- **Why it matters**: the essay's §3.1 uses it to mark logicism's failure — the lesson being that logic is mathematics' grammar, not its ground [36].
- **Status**: resolved by type theory and axiomatic set theory; the lesson is now a fixture of foundations.

### B5 · The Kepler conjecture

- **In one line**: the grocer's stacking of cannonballs is the densest way to pack equal spheres.
- **Background**: Johannes Kepler, 1611. Thomas Hales announced a proof in 1998; referees "99% certain" but not certain; a machine-checked formal proof (Flyspeck) was completed in 2014 and published 2017.
- **Why it matters**: the essay's §5.3 cites the years of verification labor as the price tag for professional verification — labor still among the discipline's worst paid [66].
- **Status**: proved, machine-checked; historically the first major theorem certified this way.

### B6 · The Robbins problem

- **In one line**: do three simple equations about a boolean operation capture all of boolean algebra?
- **Background**: Herbert Robbins posed it in 1933; it resisted hand proof for over sixty years until William McCune's automated theorem prover EQP settled it in 1996.
- **Why it matters**: the essay's §5.3 cites it in the lineage of machines absorbing the checking and the executing, humans moving on [65].
- **Status**: proved by machine — the precedent the AI-mathematics wave extends one layer up.

### B7 · Bounded gaps between primes (and Chen's theorem)

- **In one line**: how small a gap between consecutive primes occurs infinitely often?
- **Background**: Yitang Zhang (2014) proved some gap below 70 million occurs infinitely often — the first finite bound — launching the Polymath8 project (246) and James Maynard's independent breakthrough. Chen Jingrun (1973) had proved every large even number is a prime plus a product of at most two primes ("1+2").
- **Why it matters**: the essay's §4.2 and §6.2 cite the lineage as additive combinatorics alive and well — and as an example of a stock of questions curated across generations [57,58,72].
- **Status (22 Nov 2026)**: the record unconditional bound is now 240 (Stadlmann, August 2026) [129]. The twin-prime conjecture (gap 2) remains open. Related entry: [Goldbach & twin primes](../famous_problems/goldbach_and_twin_primes.md).

### B8 · The Weil conjectures

- **In one line**: count solutions of polynomial equations over finite fields, and find deep topology hiding in the arithmetic.
- **Background**: André Weil, 1949, conjectured a zeta function for varieties over finite fields with the flavour of the Riemann hypothesis; Pierre Deligne proved the last and hardest part in 1974.
- **Why it matters**: the essay's §4.2 cites Deligne's proof as the landmark of arithmetic geometry, the territory around the Langlands program [56].
- **Status**: proved (Deligne 1974); its descendants — including the geometric Langlands program — remain among the deepest active territories in mathematics.

### B9 · Pi, Liu Hui and Zu Chongzhi

- **In one line**: how precisely can the circle's ratio be computed — and by which method?
- **Background**: Liu Hui (263 AD) computed π by inscribed polygons with a cut-and-augment algorithm; Zu Chongzhi (5th century) gave 355/113, correct to six decimals — a result Europe reached only after another millennium.
- **Why it matters**: the essay's §5.5 cites the Chinese tradition as an algorithmic, constructive path to the same truths — different in what counts as a solution, not in what is true [50,69].
- **Status**: settled numerically to trillions of digits; historiographically the essay's point stands: content may be necessary, form never was.

### B10 · The Kerala school's infinite series

- **In one line**: power series for sine, cosine and π — laid down in India centuries before Newton and Leibniz.
- **Background**: Madhava of Sangamagrama and successors (14th–16th centuries) derived series expansions equivalent to those later named for European mathematicians, without building the systematic calculus framework.
- **Why it matters**: the essay's §5.5 cites Kerala as evidence that the same mathematics can grow in more than one institutional shape [50,70].
- **Status**: historically established; the essay uses it against the "modern Western mathematics = mathematics as such" equation.

<!-- zh -->

## A 组 · 事件的主角

### A1 · 纳维–斯托克斯：存在性与光滑性

- **一句话**：描述流体运动的方程，是否永远规规矩矩——还是会在有限时间内「爆炸」？
- **前提·背景**：纳维（1822）与斯托克斯（1845）写下黏性流体的运动方程——水管里的水、机翼上的空气都由它描述。方程的光滑解是否永远光滑，还是会在有限时间内产生奇点（速度无穷大），悬置超过一个世纪，是七个千禧年大奖难题之一（2000）。
- **问的是什么**：三维情形，解是否对所有时间都存在且保持光滑——还是会产生奇点？
- **为什么重要**：它是全文的中心案件（§1.7、§2.2）——2026 年 9 月的一纸宣布，把一个技术真相、一场商业竞争、一次署名纠纷、一桩优先权公案压缩进了同一周 [1,5,6]。
- **现状（2026-11-22）**：克雷官网仍标 Active [4]。OpenAI 9 月 8 日的主张——就克雷表述的 C/D 陈述给出机器 blow-up 证明，经 Lean 核验但带一个外力项 [1]——被剑桥团队发现与其自然语言文本对不上 [118]；该方法未见推广到无外力情形 [5]。11 月 20 日，无外力三维 Euler（Alpöge、Buckmaster、Coiculescu）与无外力三维 Navier–Stokes（Alpöge、Buckmaster）的 blow-up 证明宣布，Lean 形式化存于公开仓库 [120,121]。奖金至今无人申领。

### A2 · Erdős 单位距离猜想（1946）

- **一句话**：平面上的 n 个点，最多能有多少对恰好相距 1？
- **前提·背景**：Erdős 1946 年提出；他的网格构造给出约 n^(1+c/log log n) 对，并猜想这已是全部真相：u(n) ≤ n^(1+o(1))。
- **问的是什么**：n 个平面点之间的单位距离对数，是否只比 n 多出亚多项式的一点点？
- **为什么重要**：2026 年 5 月，它成为第一个被 AI 系统证伪的核心领域猜想——全文 §1.5 的「第三幕」，也是机器提出、人类消化这一模式最锋利的样本 [19,20]。
- **现状（2026-11-22）**：已证伪。Alon、Bloom、Gowers 等九人发表了 OpenAI 生成反例的人类核验版（u(n) ≥ n^(1+ε) 无穷多次成立）；萨温把指数显式化到 n^1.014；经典上界 O(n^(4/3)) 纹丝未动 [19,20]。完整条目详见 [Erdős 单位距离](../famous_problems/erdos_unit_distance.md)。

### A3 · 费马大定理——与它的形式化

- **一句话**：x^n + y^n = z^n 在 n ≥ 3 时没有正整数解——2026 年，机器把整个证明写成了计算机能逐行检查的语言。
- **前提·背景**：费马约 1637 年在页边留下因「太窄写不下」而失传的证明；358 年后由怀尔斯（与泰勒）于 1994–95 年证明。完整条目详见 [费马大定理](../famous_problems/fermat_last_theorem.md)。
- **问的是什么**（2026 年版本）：能否只从 Lean 的三条标准公理出发重新推出怀尔斯的证明——链条中不剩任何一处需要人的信任？
- **为什么重要**：全文 §1.8 以它作为核验瓶颈的极端标本——一份没有任何人能通读的制品 [25,26]。
- **现状（2026-11-22）**：Anthropic 9 月 4 日宣布完整 Lean 形式化：约 1300 万行、约 29500 个中间定理、近自主工作十一天，经 Lean 内核核验、并确认与 Mathlib 的陈述一致；巴扎德审阅后称之为非凡的自动形式化成就，但数学上不增添任何新知识 [25,26]。

### A4 · 黎曼假设

- **一句话**：zeta 函数所有「有意思」的零点，是否都落在一条直线上？
- **前提·背景**：黎曼（1859）发现素数计数定理的误差由其 zeta 函数的零点支配，猜想这些零点全部位于实部 1/2 的直线上。它是数学最著名的未解问题，千禧年难题之一。
- **问的是什么**：ζ(s) 的所有非平凡零点，实部是否恰为 1/2？
- **为什么重要**：§6.4 曾以「AI 会不会证明黎曼猜想」作为该被绕开的问法；2026 年 11 月，这个问题以一种谁也没料到的方式被回答了一版 [93,120,122]。
- **现状（2026-11-22）**：11 月 20 日，Alpöge 宣布黎曼假设的证明，出自一个内部 AI 模型（媒体点名 Claude；Tao 原文说「一个内部 AI 模型」——两说照录 [120,123]）；证明以约 1700 万行的 Lean 制品存在，11 月 21 日 Lean 社区按四项明示判据认证「黎曼假设的陈述与证明均属正确」[122]。更早，10 月发布中的「quasi-RH」结果（临界线外的零点必落在 1/8 < Re(s) < 7/8 竖条内）在两周内被人类分析学家消化并大体确认 [115]。人类数学协会则反对：无人能有理由声称理解这样一份文件 [124]。机器已核验；共同体已认证；人类理解进行中。

### A5 · 唯一游戏猜想（2002）

- **一句话**：某个「猜标签」问题，近似求解是否几乎和精确求解一样难？
- **前提·背景**：Khot 2002 年提出。若为真，则一大批近似问题（Max Cut 等）可证难以近似——它已成为理论计算机科学困难性纲领的枢纽。
- **问的是什么**：允许少量违反的约束系统里，找到满足大多数约束的标签，是否计算上不可行？
- **为什么重要**：10 月 6 日发布宣称其 372 个家族中包含 UGC 的证明——整批发布中分量最重的一条主张（后记 §xi）[93]。
- **现状（2026-11-22）**：已发布的主张，未被接受的定理。Moshkovitz 已在这份证明上花数周，与 Khot、Håstad、Minzer 协作并借助 GPT-6 Astra，面对一个她称为「全然陌生的全新纠错码」；相关努力已在 Simons Institute 报告；完整核验尚未宣布 [119]。

### A6 · 雅可比猜想（1939）

- **一句话**：多项式映射若雅可比行列式恒为非零常数，它是否必有多项式逆映射？
- **前提·背景**：Keller 1939 年提出；一维平凡成立，二维悬置近百年，双方「证明」的沉船残骸堆积如山。
- **问的是什么**：对哪些维数 n，雅可比行列式恒为非零常数的多项式映射 C^n → C^n 必有多项式逆？
- **为什么重要**：§2.1 把它 2026 年 7 月的反例列为菲尔兹奖得主联名信之前机器证明大戏的一幕 [1,19,30]。
- **现状（2026-11-22）**：n ≥ 3 为假。Alpöge 2026 年 7 月 19 日宣布三维反例（AI 模型助力找到）；Tao 次日发布公开的「消化」[106]；Gao 推广到一切大于二的维数，所有恒等式经精确有理数算术验证 [107]；巴扎德的团队在宣布数日内即看到反例被 Lean 机检 [108]。n = 2 仍未解。

### A7 · 全部光滑七维球面上的正截面曲率

- **一句话**：每一种「怪异」的七维球面，能否都被赋予一个处处正弯曲的几何？
- **前提·背景**：1956 年米尔诺发现七维球面携带 28 种不同的光滑结构——拓扑相同，微积分法则不同。每一种是否都容许严格正截面曲率的黎曼度量（所有二维截面都同向弯曲，像球面而不像马鞍），是拓扑如何约束几何的长久试金石。
- **问的是什么**：为光滑同伦七维球面的全部 28 个定向微分同胚类，各构造一个严格正截面曲率的度量。
- **为什么重要**：后记 §iv 把它记作边界案例——论文落在正文时段之内，致谢细节落在时段之外 [82,83]。
- **现状（2026-11-22）**：何杨辉、刘子然与丘成桐 9 月 24 日在预印本中宣称已构造（以边界度量相容的两个正曲率七维圆盘粘合）；论文致谢 GPT 与 Claude 提出的建议 [82,83]。后续工作正在延伸该技术；共同体尚无裁定。

### A8 · 四阶复矩阵乘法：49 到 48

- **一句话**：乘两个 4×4 复矩阵，最少需要几次标量乘法？
- **前提·背景**：斯特拉森 1969 年的算法用 49 次，击败教科书的 64 次，开创了代数复杂度理论；这个纪录保持了五十六年。
- **问的是什么**：找到 4×4 复矩阵情形已知最少的标量乘法次数——每一次缩减都会在更大的矩阵乘积上复利放大。
- **为什么重要**：§1.4 以 AlphaEvolve 的 48 作为「计算-核验」一端成果的标志——那里不需要任何专家判断 [16]。
- **现状（2026-11-22）**：48（DeepMind AlphaEvolve，2025 年 5 月）仍为纪录；后续工作把它以纯有理数系数重新导出。小字须读：48 是已知最好算法（上界），不是已证的最小张量秩。

### A9 · 十一维的接吻数

- **一句话**：在十一维空间里，多少个单位球可以同时贴住中央那个单位球？
- **前提·背景**：「接吻数」在三维古已有之（牛顿与格雷戈里争论的 13）；精确值仅在一、二、三、四、八、二十四维已知。
- **问的是什么**：确定 R^11 中互不重叠的单位球同时贴住中央单位球的最大个数。
- **为什么重要**：§1.4 把它与矩阵乘法并举，作为可机械核验的纪录 [16]。
- **现状（2026-11-22）**：下界 593（AlphaEvolve，2025 年 5 月，自 592 提升），上界 868；精确值未知。后有论文主张 604；标准参考尚未采信，本页亦按未核验处理 [16]。

### A10 · 九圈六边形振幅（附一个「单负」旁注）

- **一句话**：在量子场论的「玩具模型」里，算出一个深达九个量子圈的、复杂得可怕的散射振幅。
- **前提·背景**：平面 N=4 超杨–米尔斯理论是现代场论的「氢原子」；其六粒子「六边形」振幅随圈数 L 天文级增长。原纪录为 2023 年 Dixon 与刘洋的八圈，用的是「自举」法——不断施加一致性条件，直到答案被逼出来。
- **问的是什么**：算出九圈六边形振幅（旁注：判定某个单负胶子树级振幅是否非零）。
- **为什么重要**：§1.7 把 2026 年理论物理的两案读作「机器执行配方」与「机器提出猜想」的现场标本 [23,24]。
- **现状（2026-11-22）**：Anthropic 9 月 25 日宣布 Claude 算出九圈振幅，Dixon 花约两周独立核验；何颂领衔的中科院团队同期得到大部分结果，部分约束用了 GPT-6 [24]。旁注中，一篇 2026 年预印本报告单负胶子树级振幅公式先由 GPT-5.2 Pro 猜想、再由 OpenAI 内部模型证明 [23]。

### A11 · First Proof：十道研究级问题

- **一句话**：机器能否解出它的考官们自己真心关心的问题？
- **前提·背景**：2026 年由十一位研究数学家组织的挑战，十道题全部取自出题人自己的研究——刻意不是竞赛题，不是为「可解」而设计的基准题。
- **问的是什么**：十题之中，机器生成的解答能确立几道——以及谁能判定？
- **为什么重要**：§1.6 与 §6.4 以它作为核验瓶颈最干净的表达：报告的困难在评估，不在生成 [22]。
- **现状（2026-11-22）**：生成的一半已经成立；评估的一半仍是未了的公案，组织者自己承认，测度「自主提出问题」的实验方法尚不存在 [22]。

## B 组 · 论证的背景板

### B1 · 哥德尔不完备定理（1931）

- **一句话**：任何足够丰富、一致的形式系统，必有它自己证不出的真命题——而且它无法在内部证明自己的一致性。
- **前提·背景**：哥德尔，针对希尔伯特「把全部数学安放在形式地基上」的纲领。
- **问的是什么**（已有答案）：形式证明有没有机械边界？有——全文两处倚重它（§3.3 反对「数学是终极根据」，§5.4 论彭罗斯对它的争议性援引）[42,43,44]。
- **现状**：已成定论的数学；建立在它之上的哲学论证仍在争论。

### B2 · 停机问题（1936）

- **一句话**：没有任何算法能对每个程序与输入判定它是否终将停机。
- **前提·背景**：图灵，在那篇定义了「计算」本身的论文里。
- **问的是什么**（已有答案）：对这道界定明确的问题，存在普适的机械判定程序吗？不存在 [48]。
- **为什么重要**：与哥德尔一道，合上了「形式化能够穷尽数学」的希望——§3.5 与 §5.4 [48]。

### B3 · 连续统假设

- **一句话**：整数与连续统之间，还有没有别的大小？
- **前提·背景**：康托尔，1878。哥德尔（1940）证明它不能从标准公理否证；科恩（1963）证明它也不能由此证出——它是独立的。
- **为什么重要**：§3.3 以科恩的结果说明：连最基础的分支，其公理选择也不是唯一被迫的 [45]。
- **现状**：「独立」已成定论；采纳哪套公理是立场，不是事实。

### B4 · 罗素悖论（1901）

- **一句话**：「所有不包含自身的集合组成的集合」——它包含自己吗？
- **前提·背景**：罗素致弗雷格的信，在朴素集合论的地基上凿出一个洞。
- **为什么重要**：§3.1 以它标记逻辑主义的失败——教训是逻辑是数学的语法，不是数学的地基 [36]。
- **现状**：由类型论与公理化集合论解决；教训已成为基础理论的常识。

### B5 · 开普勒猜想

- **一句话**：杂货店堆橙子的方式，就是等球堆得最密的方式。
- **前提·背景**：开普勒，1611。黑尔斯 1998 年宣布证明；审稿人「99% 确信」但不敢断言；机器核验的形式证明（Flyspeck）2014 年完成、2017 年发表。
- **为什么重要**：§5.3 以多年的核验劳动为「核验应当付酬」的价码——这类劳动至今是学科里报酬最低的一档 [66]。
- **现状**：已证明、已机器核验；历史上第一个以此方式认证的重大定理。

### B6 · 罗宾斯问题

- **一句话**：三条关于一个布尔运算的简单等式，能否穷尽全部布尔代数？
- **前提·背景**：罗宾斯 1933 年提出；人手六十余年攻而不克，1996 年被麦库恩的自动定理证明器 EQP 解决。
- **为什么重要**：§5.3 把它列在「机器接手检查与执行、人相应转移阵地」的谱系里 [65]。
- **现状**：已被机器证明——AI 数学浪潮正是把这个先例又推高一层。

### B7 · 素数有界间隙（与陈景润定理）

- **一句话**：相邻素数的间隙，最小能多小——而且无穷多次出现？
- **前提·背景**：张益唐（2014）证明存在某个小于七千万的间隙无穷多次出现——第一个有限界——引出 Polymath8 项目（246）与梅纳德独立的突破。陈景润（1973）证明每个大偶数都是素数加至多两个素数之积（「1+2」）。
- **为什么重要**：§4.2 与 §6.2 以这一谱系说明加法组合学的活力——以及世代筛选的问题存量如何供给研究 [57,58,72]。
- **现状（2026-11-22）**：无条件纪录现为 240（Stadlmann，2026 年 8 月）[129]。孪生素数猜想（间隙 2）仍未解。相关条目详见 [哥德巴赫与孪生素数](../famous_problems/goldbach_and_twin_primes.md)。

### B8 · 韦尔猜想

- **一句话**：数有限域上多项式方程的解，并在算术深处找到拓扑。
- **前提·背景**：韦尔 1949 年猜想有限域上代数簇的 zeta 函数具有黎曼假设的风味；德利涅 1974 年证明最后也最难的部分。
- **为什么重要**：§4.2 以德利涅的证明作为算术几何的里程碑——朗兰兹纲领周边那片疆域的界碑 [56]。
- **现状**：已证明（1974）；其后裔（几何朗兰兹等）仍是数学最深处的活疆域。

### B9 · 圆周率：刘徽与祖冲之

- **一句话**：圆的比率能算到多精——以及用什么方法算？
- **前提·背景**：刘徽（公元 263 年）以割补术用内接多边形逼近；祖冲之（五世纪）给出密率 355/113，精确到小数六位——欧洲得到同精度结果要再等一千年。
- **为什么重要**：§5.5 以中国传统为「算法性、构造性路径」的证据——差别在什么使一份解答算数，不在什么为真 [50,69]。
- **现状**：数值上已算至万亿位；史学上本页的论点依旧成立：内容或许必然，形式从来不是。

### B10 · 喀拉拉学派的无穷级数

- **一句话**：正弦、余弦与 π 的幂级数——在牛顿与莱布尼茨之前的几个世纪，已在印度写成。
- **前提·背景**：桑伽马格拉的马达瓦及其后继者（十四至十六世纪）得到与后来欧洲同名结果等价的级数展开，但没有发展出系统化的微积分框架。
- **为什么重要**：§5.5 以喀拉拉为证据：同一种数学可以在不止一种建制形态下生长 [50,70]。
- **现状**：史学上已成定论；文章用它对抗「现代西方数学＝数学本身」的等式。

<!-- L1-end -->

<!-- 新来源备注：本页 [129] 为长稿来源表之外新增（Stadlmann, Bounded gaps between primes, arXiv:2608.31126, 2026, https://arxiv.org/abs/2608.31126, accessed 22 November 2026, 一手（预印本））；其余方括号编号一律指向 proofs_no_longer_scarce.md 文末来源表。 -->
