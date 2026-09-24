
Below is a research-ready structure followed by a complete draft. It treats **24 September 2026 as the cutoff date**, because the mathematics/AI story is changing rapidly and the September 2026 Navier–Stokes dispute is still unresolved.

## Proposed title

**When Machines Prove Mathematics: AI, Formal Verification, Mathematical Creativity, and the Changing Identity of the Mathematician**

### Central thesis

The recent AI-mathematics breakthroughs do not by themselves demonstrate the “end of mathematics” or the disappearance of mathematicians. They demonstrate something more precise and more consequential: a growing fraction of mathematical activity can be decomposed into stages—formal specification, search, deduction, verification, computation, exposition, and conceptual synthesis—that machines can perform at increasingly high levels. Yet these stages are not identical to one another. A mechanically checked proof certifies a formal statement relative to a formal system; it does not by itself settle whether the formal statement captured the intended problem, whether the result is conceptually explanatory, whether it is novel relative to the literature, or whether anyone understands why it matters. The emerging fault line is therefore less “human versus machine intelligence” than **verification versus interpretation, execution versus conception, and local proof production versus global theory formation**.

---

# I. Outline

### 1. AI Breakthroughs and Verification Rigor

1. Establish distinctions among:

   * competition performance;
   * formal theorem proving;
   * research-level proof attempts;
   * independently audited mathematical results.
2. Chronology:

   * AlphaGeometry, January 2024.
   * AlphaProof + AlphaGeometry 2 at IMO 2024.
   * AlphaProof methodology in *Nature*, 2025.
   * Gemini Deep Think at IMO 2025.
   * Harmonic’s Aristotle, 2025.
   * FirstProof Batch 1, February 2026.
   * Aletheia and FirstProof.
   * FirstProof Batch 2, June 2026.
   * Aletheia’s broader research experiments, 2026.
   * OpenAI Navier–Stokes, September 2026.
3. Separate:

   * correctness of proof object,
   * correctness of formalization,
   * correctness of informal argument,
   * novelty,
   * attribution,
   * acceptance by the mathematical community.
4. Evaluate each event without conflating these dimensions.

### 2. Debates Within the Mathematical Community

1. “AI can now do mathematics” position.
2. “AI can prove but not understand” position.
3. “The central issue is not capability but institutional practice” position.
4. Motivations and structural incentives:

   * research acceleration,
   * commercial signaling,
   * professional identity,
   * attribution,
   * epistemic standards.
5. Is this a crisis of mathematics?

   * not a crisis of mathematical validity;
   * potentially a crisis of professional division of labor, authorship, evaluation, and institutional authority.

### 3. Epistemological Essence and Limits of Mathematics

1. Mathematics as:

   * structure,
   * formal language,
   * proof practice,
   * conceptual construction,
   * human knowledge system.
2. “First cause” versus framework:

   * axioms,
   * semantics,
   * cognition,
   * language,
   * computational models,
   * social purposes.
3. Formal foundations:

   * formalism,
   * structuralism,
   * intuitionism,
   * Platonist perspectives.
4. Gödel, incompleteness, undecidability.
5. Church–Turing and computability.
6. Mathematical representation as selection and construction, not mere transcription.

### 4. Identity of Mathematicians and the Intelligence Myth

1. Analytic stages of mathematical development.
2. Different mathematical roles:

   * solver,
   * theorist,
   * formalizer,
   * computational experimenter,
   * synthesizer,
   * expositor,
   * field architect.
3. Contemporary research problems.
4. Why mathematics is culturally coupled to “intelligence.”
5. Historical genius narratives.
6. Social selection and information asymmetry.
7. Anxiety, stereotype, signaling, Matthew effects, and halo effects.
8. Why mathematical achievement should not be equated with generic “intelligence” or “wisdom.”

### 5. Formalization, Rationality, and AI–Human Division of Labor

1. What formalization can and cannot guarantee.
2. AI’s potential superiority in highly specified rational tasks.
3. Difference between:

   * decidability,
   * computability,
   * tractability,
   * proof search,
   * conceptual discovery.
4. Intrinsic versus extrinsic mathematics.
5. A proposed division of labor.
6. Limits of contemporary Western mathematical frameworks.
7. Global mathematical traditions and mathematical pluralism.

### 6. Groundbreaking Paradigms and Polymathic Breakthroughs

1. Define “groundbreaking.”
2. Distinguish difficult problem solving from paradigm creation.
3. Evidence from FirstProof: AI sometimes generates novel arguments, but experiments have not yet established autonomous theory invention at scale.
4. Why not every human mathematician formulates groundbreaking theories either.
5. Descartes, Newton, Leibniz, Gauss as boundary-crossing cases.
6. Specialization versus synthesis.

### 7. Synthesis and Meta-Reflection

1. Mathematics as a nested system:

   * object,
   * representation,
   * proof,
   * interpreter,
   * community,
   * tool,
   * purpose.
2. Human and AI capabilities as interpenetrating rather than simply opposed.
3. What remains distinct:

   * assigning purposes,
   * selecting significance,
   * maintaining epistemic responsibility.
4. Final synthesis.

---

# Complete Draft

## When Machines Prove Mathematics: AI, Formal Verification, Mathematical Creativity, and the Changing Identity of the Mathematician

### Introduction

The most important recent developments in artificial intelligence and mathematics are not merely spectacular demonstrations that machines can solve difficult equations. They are more disruptive than that. AI systems have begun to participate in several traditionally distinct layers of mathematical activity: solving difficult competition problems, constructing formal proofs, generating mathematical arguments, searching large spaces of possibilities, identifying useful lemmas, navigating literature, and—at least in carefully delimited cases—producing research-level results that experts judge to be correct.

The transition is visible across several milestones. In 2024, Google DeepMind's AlphaGeometry reached near-human-gold-medalist performance on a benchmark of Olympiad geometry problems, with every solution computer-verified. Later that year, AlphaProof combined with AlphaGeometry 2 solved four of six International Mathematical Olympiad (IMO) problems and scored 28/42, matching the silver-medal range, although AlphaProof required manual translation into Lean and in some cases days of computation. ([Google DeepMind][1]) In 2025, an advanced Gemini Deep Think system achieved 35/42 at IMO 2025 under official grading, a gold-medal-level score, while moving from the previous year's manually formalized pipeline toward end-to-end natural-language solutions. ([Google DeepMind][2]) Later in 2025, Harmonic announced Aristotle, an AI theorem-proving system combining informal reasoning, Lean proof search, and a geometry engine, with gold-medal-equivalent performance on the 2025 IMO problems. ([arXiv][3])

In 2026, the question changed again. FirstProof, an independent research-mathematics evaluation effort, posed unpublished, research-level problems drawn from the work of professional mathematicians. In its second, controlled batch, four AI systems generated 39 submissions that were reviewed by roughly 30 expert mathematicians; seven of the ten problems received at least one submission judged either essentially flawless or requiring only minor revisions. Yet the same experiment documented recurring hallucinated citations, false statements, incomplete arguments, and instances in which AI proved a weaker theorem rather than the theorem actually posed. ([1stproof][4])

Then, in September 2026, OpenAI announced an AI-generated solution to the Navier–Stokes Millennium Prize problem, accompanied by a Lean formalization. The announcement has generated a deeper controversy because the result appears to exploit an admissible but unusual branch of the Clay formulation involving a smooth external force. The Clay Mathematics Institute has acknowledged the apparent settlement while emphasizing that its deliberately slow evaluation procedure remains in force; its current Navier–Stokes page still labels the problem “Active,” while the prize rules require publication in a qualifying venue, two years of elapsed time, and general acceptance in the global mathematical community. ([OpenAI][5])

These episodes invite a seductive but misleading question: **Has AI become better at mathematics than mathematicians?**

That formulation is too coarse. The more interesting question is what, exactly, “doing mathematics” consists of. A proof can be correct while its formalization is semantically defective. A theorem can be true while its proof is unilluminating. A solution can be novel while lacking attribution. An AI can discover an argument without independently deciding that the associated theorem deserves to be studied. Conversely, humans can formulate important questions yet fail to solve them efficiently. The recent evidence therefore suggests not a binary contest but a decomposition of mathematics into partially separable activities.

The central claim of this essay is consequently that the present moment should be understood less as a crisis of mathematical truth than as a transformation of the **architecture of mathematical work**. AI is making increasingly visible the distinction between proof production and mathematical conception, between formal validity and semantic meaning, between search and significance, and between the production of results and the social processes by which a result becomes mathematics.

---

# 1. AI Breakthroughs and Verification Rigor

The first requirement for a serious assessment is methodological separation. It is no longer enough to ask whether “AI solved a math problem.” We must ask what was provided to the system, what the system actually did, how much human intervention occurred, what was independently checked, what was formally verified, whether the statement matched the intended problem, and whether the result has survived ordinary mathematical scrutiny.

A useful distinction is between six levels:

1. **Answer correctness** — the final numerical or symbolic answer is correct.
2. **Informal proof correctness** — the argument is judged valid by experts.
3. **Formal proof correctness** — a proof object is accepted by a trusted proof assistant.
4. **Statement alignment** — the formal theorem correctly expresses the intended informal problem.
5. **Research novelty** — the result or method is genuinely new relative to existing literature.
6. **Community validation** — independent mathematicians inspect and accept the result under ordinary scholarly norms.

These are not interchangeable.

### The chronology

| Event                                              | What happened                                                                                                | Verification regime                                                                             | Methodological assessment                                                                                                                                                                                        |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AlphaGeometry, Jan. 2024**                 | Solved 25/30 benchmark IMO geometry problems, approaching average human gold-medalist performance            | Computer-verified proofs; selected solutions assessed by Olympiad expert Evan Chen              | Strong evidence of domain-specific theorem proving; narrow domain, synthetic training data, and benchmark specialization limit generalization ([Google DeepMind][1])                                             |
| **AlphaProof + AlphaGeometry 2, IMO 2024**   | Solved 4/6 problems, 28/42, silver-medal range                                                               | Problems manually formalized; proofs checked in Lean; scored by Timothy Gowers and Joseph Myers | Strongly verified in the proof-checking sense, but competition conditions were not symmetric: two-to-three days of computation and manual formalization were required ([Google DeepMind][6])                     |
| **AlphaProof methodology, *Nature*, 2025** | Detailed publication of RL + Lean approach and IMO results                                                   | Formal proof within Lean; peer-reviewed publication                                             | Important because the system and methodology became independently inspectable through scholarly publication, while compute/time asymmetry remained significant ([Nature][7])                                     |
| **Gemini Deep Think, IMO 2025**              | 35/42, five of six problems solved perfectly                                                                 | Official IMO grading and certification; natural-language end-to-end generation within 4.5 hours | Strong evidence of general mathematical reasoning on competition problems; not equivalent to research-level autonomous theory construction ([Google DeepMind][2])                                                |
| **Aristotle, 2025**                          | Gold-medal-equivalent IMO performance using Lean, informal reasoning, and geometry components                | Formal verification is integral to system                                                       | Important technical advance; however, an industry preprint is not equivalent to independent research-community validation ([arXiv][3])                                                                           |
| **FirstProof Batch 1, Feb. 2026**            | AI systems attempted ten unpublished research-level problems                                                 | Informal expert/community evaluation                                                            | Significant frontier evidence, but methods were intentionally informal and not controlled; even OpenAI subsequently retracted confidence in one initially promising proof ([1stproof][8])                        |
| **Aletheia on FirstProof**                   | 6/10 problems reportedly solved under majority expert judgment, with no human intervention during generation | Expert evaluation after generation                                                              | Stronger evidence for autonomous research-level proof construction, but “correct” was interpreted as publishable after minor revisions, not formal proof or unconditional independent replication ([arXiv][9]) |
| **FirstProof Batch 2, June 2026**            | Four systems tested under controlled conditions; 39 solutions formally assessed                              | Each submission reviewed by 2–3 expert referees                                                | Probably the most informative current controlled evidence: genuine successes coexist with systematic citation, interpretation, and reasoning failures ([1stproof][4])                                            |
| **Aletheia research experiments, 2026**      | Claimed autonomous work across PhD-level problems, open Erdős questions, and research papers                | Expert/author-dependent evaluation rather than universal formal certification                   | Important frontier evidence, but autonomy, novelty, and field-wide significance remain heterogeneous and require case-by-case verification ([arXiv][10])                                                         |
| **OpenAI Navier–Stokes, Sept. 2026**        | Claimed finite-time blowup for forced 3D Navier–Stokes with Lean formalization                              | Company-published manuscript + Lean proof; CMI has not completed prize evaluation               | Formally serious and unusually transparent about a proof artifact, but semantic interpretation, novelty, attribution, and community acceptance remain under active dispute ([OpenAI][5])                         |

### AlphaProof and the first decisive shift

AlphaProof is especially important because it joined two previously separate traditions: machine learning and proof assistants. DeepMind's 2024 description explicitly contrasted natural-language systems, which may hallucinate plausible but incorrect reasoning, with Lean, where proof terms can be mechanically verified. AlphaProof learned to generate candidate statements, search for proofs, and reinforce successful formal proof trajectories. ([Google DeepMind][6])

But the methodological caveat is just as important as the achievement. At IMO 2024, the problems were **manually translated** into a formal language, and AlphaProof sometimes spent **two or three days** solving a single problem. The competition itself allowed human contestants only two four-and-a-half-hour sessions. ([Google DeepMind][6])

Thus “AlphaProof solved the IMO problem” is true in one sense and misleading in another. It solved the formalized problem using a highly capable computational pipeline. It did not perform the entire human task under identical temporal and representational conditions.

This distinction is not a criticism of the system. It is a lesson about measurement. A machine and a human are not necessarily being evaluated on the same task merely because the final theorem is the same.

### Gemini and the transition from theorem proving to reasoning

The 2025 Gemini Deep Think result changed the comparison. DeepMind reports that the system was officially graded by IMO coordinators using the same criteria applied to student solutions and achieved 35/42, solving five of six problems perfectly. Crucially, it operated from the official natural-language problem statements and produced mathematical proofs directly within the 4.5-hour contest time limit. ([Google DeepMind][2])

This is methodological evidence of a different quality from AlphaProof's 2024 result. It reduces two important sources of asymmetry: manual formalization and much longer inference time.

Nevertheless, it remains an **Olympiad benchmark**. Olympiad mathematics is unusually self-contained, deliberately posed, and bounded. Research mathematics typically requires literature search, historical awareness, abstraction, conjecture formation, problem reformulation, and deciding whether a result is interesting enough to pursue. The benchmark therefore establishes something narrower than “AI is now an autonomous mathematician.”

### FirstProof is the more revealing experiment

The FirstProof project is particularly valuable because it explicitly recognized the gap between competition-style mathematics and research mathematics. The organizers selected unpublished problems that had emerged naturally in professional mathematicians' research. Their own report says that mathematics involves not only solving questions but “asking new questions” and “developing frameworks to answer them.” They nevertheless restricted the benchmark to proof production because no sufficiently concrete experimental protocol for measuring autonomous conjecture generation or framework construction was yet available. ([1stproof][4])

That decision is methodologically important. It prevents a common category error: **we should not infer that success at producing proofs establishes success at inventing the research agenda those proofs inhabit.**

The second batch is even more informative. The organizers ran the tests themselves, restricted systems to public models or public-model harnesses, released costs and logs, and used approximately thirty expert referees. Each submission was evaluated by at least two mathematical experts. Seven of the ten problems received at least one submission judged essentially flawless or requiring only minor revisions. ([1stproof][4])

At the same time, the experiment exposed systematic failure modes. AI systems sometimes handled routine steps in painstaking detail while skipping the genuinely difficult step. They sometimes asserted that something followed by a “standard argument” when it did not. They produced unsupported or hallucinated citations. They occasionally proved a weaker theorem than the problem asked, or even attempted to prove a false statement. ([1stproof][4])

This is arguably more scientifically useful than a perfect benchmark score. It reveals the **topology of failure**.

One of the most striking results was Problem 5, where one system was judged essentially flawless by all three referees. The proof was considered correct and novel and used a different route from the human solution, including a stronger intermediate result. ([1stproof][4]) That is genuine evidence that contemporary AI can sometimes contribute mathematical arguments that are not merely reproductions of known human proof templates.

But the same experiment also found citation failures serious enough that a human submission using similar language without attribution would likely have been treated as unacceptable scholarship. ([1stproof][4]) The lesson is important: **proof competence and scholarly competence are different capabilities.**

---

# 2. The Navier–Stokes Episode: Formal Success, Semantic Dispute

The September 2026 OpenAI announcement is the most consequential case because it moves beyond benchmarks into a Millennium Prize problem. OpenAI reported that an internal system generated a finite-time blowup construction for three-dimensional incompressible Navier–Stokes equations and supplied both an informal manuscript and a Lean formalization. The effort reportedly used a large system of cooperating agents and was completed in several days. ([OpenAI][5])

At one level, this is an unusually rigorous AI claim. Lean's design makes an important distinction possible: the kernel checks proof terms, and dependencies can be inspected for axioms. Lean's own documentation explicitly warns, however, that verifying a theorem and determining what the theorem means are different tasks. A successful kernel check guarantees that the formal statement follows from the definitions, imported results, and axioms used; it does **not** itself guarantee that the formal statement corresponds to the intended informal theorem. ([Lean Language][11])

That distinction is central to the current Navier–Stokes debate.

The Clay formulation allows several alternatives, including forced cases. OpenAI argues that its construction satisfies one of the admissible forced alternatives, and the company's paper explicitly frames its result in those terms. ([OpenAI][5]) The Clay Institute itself has confirmed that the official formulation permits such an alternative and, on 11 September, described the problem as “apparently” settled while stressing that its prize process is deliberately unhurried. ([Clay Mathematics Institute][12])

The debate is therefore not simply “proof versus no proof.” It is partly about **what the original problem was intended to measure**.

Scientific American's 21 September report quotes mathematicians who regard the forced construction as mathematically within the Clay formulation but substantially different from the unforced blowup scenario that much of the field regards as the central scientific question. It also reports a new mathematical argument purporting to show that the OpenAI method cannot be extended to the unforced problem. ([Scientific American][13])

This creates an unusually instructive three-way distinction:

**First**, a result can be mathematically valid within a formal statement.

**Second**, that statement can be legitimately included within a prize's official wording.

**Third**, mathematicians can still regard a nearby, more structurally central question as unresolved.

Those three propositions are perfectly compatible.

The Clay prize rules make the institutional position especially clear. A qualifying solution must be published in a qualifying outlet, remain in the literature for at least two years, achieve general acceptance in the global mathematics community, and satisfactorily answer the official problem. The rules also state explicitly that only a complete mathematical solution to the official formulation is eligible. ([Clay Mathematics Institute][14]) As of 24 September 2026, the prize therefore has not been awarded, and the Clay site continues to list the Navier–Stokes problem as active. ([Clay Mathematics Institute][15])

The correct conclusion at this date is not “OpenAI solved Navier–Stokes” or “OpenAI did not solve Navier–Stokes.” It is:

> **OpenAI has produced a serious formalized claim that appears to settle an admissible branch of the Clay formulation, but the claim has not yet completed the mathematical, semantic, attribution, and institutional validation procedures required for recognition as a resolved Millennium Prize problem.**

That distinction is likely to become one of the most important lessons in AI-assisted mathematics.

---

# 3. Debates Within the Mathematical Community

The mathematical community is not divided cleanly into “pro-AI” and “anti-AI.” Its actual disagreement concerns which parts of mathematical value are being measured and which ought to count.

Three broad positions are visible.

## The capability position

The first position emphasizes demonstrated performance. From this perspective, repeated success across Olympiads, formal theorem proving, unpublished research problems, and increasingly open-ended research tasks is strong evidence that AI systems are acquiring capabilities that were previously regarded as distinctively mathematical.

There is good empirical support for the narrow version of this claim. AlphaProof proved difficult formal statements. Gemini reached gold-medal-level Olympiad performance. FirstProof systems sometimes generated proofs that experts judged correct and novel. ([Nature][7])

The strongest argument for this camp is methodological: **one should infer capabilities from successful performance rather than from philosophical intuitions about what machines “cannot” do.**

That argument is powerful. Human beings have repeatedly underestimated machine performance by assuming that particular styles of cognition are uniquely human. The Alpha series itself emerged from a similar history in games and scientific computation.

Yet capability claims have their own potential bias. Commercial AI companies have legitimate incentives to emphasize milestones that demonstrate technological progress. A benchmark can be selected because it is measurable, spectacular, reproducible, and useful for public communication. This does not make the result false, but it can shape the **selection of visible evidence**.

## The understanding position

The second position holds that proof production is not the whole of mathematics. Peter Scholze's endorsement of the Leiden Declaration expresses a strong version of this view, emphasizing that mathematical research is fundamentally a human communal activity oriented toward understanding. The Leiden Declaration itself argues for continued human responsibility, transparency, attribution, and disclosure in AI-assisted research. ([Leiden AI & Mathematics Declaration][16])

The strongest form of the argument is not that AI cannot prove theorems. The evidence now makes such a claim increasingly untenable. Rather, it is:

> **A mathematically valid proof is not identical to mathematical understanding.**

This is consistent with ordinary human mathematical practice. A proof may be correct yet unilluminating. It may be enormously long but conceptually weak. It may prove a theorem by a technically valid route that obscures why the theorem is true. Mathematics values not only truth but also structure, explanatory compression, reusable ideas, and conceptual transport across problems.

The danger in this position is that “understanding” can become a moving criterion that is applied selectively whenever machines succeed. If no operational definition is supplied, the claim becomes unfalsifiable: whenever a machine succeeds, its performance can be reclassified as “mere calculation.”

FirstProof provides a way out. It does not resolve philosophical questions about understanding, but it makes some relevant dimensions measurable. Its referees could distinguish correct novel arguments from hallucinated citations, weaker substitute theorems, and incomplete proofs. ([1stproof][4])

## The institutional position

A third position, exemplified by the Leiden Declaration and by Terence Tao's recent writings, shifts the question away from “Can AI do mathematics?” toward “How should mathematics operate if increasingly capable AI exists?”

Tao's 2026 ICM essay deliberately conditions on the possibility that AI will perform a substantial fraction of mathematical tasks and instead examines the goals and values of mathematical research. ([arXiv][17]) The Leiden Declaration similarly focuses on disclosure, attribution, responsibility, transparency, and publication norms. The International Mathematical Union endorsed the declaration, while the European Mathematical Society explicitly declined to endorse it, saying that it recognized the concerns but also wanted continued attention to AI's opportunities. ([Leiden AI & Mathematics Declaration][18])

This disagreement is revealing. The dispute is not simply over whether AI works. It is about **what the mathematical institution is for**.

Possible structural incentives exist on both sides. AI companies benefit from capability demonstrations, faster scientific progress, and evidence of technological differentiation. Academic mathematicians have strong incentives to protect norms of attribution, priority, reproducibility, interpretability, and professional responsibility. Institutions also need procedures for deciding who counts as an author, how AI-generated discoveries should be cited, who bears responsibility for errors, and how confidential research data should be handled.

These incentives need not imply bad faith. They are normal consequences of different institutional functions.

### Crisis of mathematics or crisis of the establishment?

The evidence favors a more precise diagnosis.

There is no evidence of a crisis in the sense that mathematical truth has suddenly become unstable. A theorem does not become false because an AI discovered it. Formal logic does not cease to function because the proof was machine-generated. Gödel's incompleteness theorems, computability theory, and ordinary proof semantics remain exactly as they were.

What is changing is the social organization around mathematics.

Questions about authorship become harder when a proof emerges from proprietary models.

Questions about originality become harder when training data are opaque.

Questions about expertise change when a person can produce hundreds of candidate arguments by querying a machine.

Questions about professional identity change when a mathematician's traditional skill—writing proofs—is partially automated.

This is better described as a **crisis of division of labor and epistemic governance** than a crisis of mathematics itself.

---

# 4. What Is Mathematics?

The deeper argument requires stepping back from the current technology.

Mathematics is often spoken of as though it were one thing: a body of truths. But mathematical practice contains several layers.

At the object level there are structures: numbers, spaces, functions, groups, categories, manifolds, graphs, equations.

At the representational level there are symbols, diagrams, definitions, coordinate systems, notation, algorithms and formal languages.

At the inferential level there are proofs and derivations.

At the conceptual level there are choices about which objects and relations deserve to be formalized.

At the epistemic level there are standards for what counts as evidence and understanding.

At the social level there are communities that decide which problems are interesting, which terminology is useful, and which results are worth publishing.

The current AI revolution is affecting these layers differently.

### Is mathematics a “first cause”?

The phrase “first cause” belongs to a metaphysical register rather than a mathematical one. Mathematics can be foundational **inside a formal system**, but that does not mean mathematics is the ultimate explanatory layer of reality or cognition.

Every formal mathematical system begins with a choice of language, primitives, axioms, inference rules, and interpretation. Structuralist accounts emphasize mathematical structures rather than individual objects; intuitionist approaches emphasize construction; formalist approaches emphasize formal derivation; other philosophical positions treat mathematical objects as in some sense independent of human minds. There is no single philosophical consensus that makes one of these perspectives definitive. ([Stanford Encyclopedia of Philosophy][19])

The important point for AI is that **mathematics always has a framework dimension**.

Before asking whether \(X\) can be proved, someone must decide what \(X\) is.

Before deciding what constitutes a solution, someone must specify which equivalence relation matters.

Before deciding which objects belong together, someone must choose a level of abstraction.

Mathematics therefore operates not merely by deduction but by **framing**.

### Gödel and the limits of formal completeness

Gödel's incompleteness theorems place a deep limit on any simple identification of mathematics with formal proof production. For sufficiently expressive, consistent, effectively axiomatized systems, there are statements that cannot be proved within the system even though they have determinate mathematical status in the intended interpretation. The second incompleteness theorem shows that such a system cannot, in an appropriate sense, prove its own consistency. ([Stanford Encyclopedia of Philosophy][20])

This does not mean that “AI cannot do mathematics.” That is a common overinterpretation.

Gödel shows something more subtle: **no single formal system captures all mathematical truth in a complete and internally self-certifying way**.

That leaves space for moving between formal systems, proving relative consistency, inventing new axioms, and constructing stronger frameworks.

Thus the frontier of mathematics cannot be identified simply with running a proof checker faster.

### Computability is not the same as solvability

The Church–Turing tradition similarly clarifies an important distinction. The Church–Turing thesis connects intuitive effective procedures with Turing computability, but “computable” does not mean “efficiently computable.” Some functions are computable but require infeasible resources; others are uncomputable altogether. ([Stanford Encyclopedia of Philosophy][21])

Mathematical AI sits inside this hierarchy:

**formalizable → computable → tractable → searchable → discoverable in practice**

These arrows do not collapse into one another.

A theorem may have a short proof but an enormous search space.

A statement may be decidable in principle but computationally inaccessible.

A proof may exist in a formal system while finding it requires enormous exploration.

An AI may solve such tasks not because it has escaped computational limits but because it has learned good heuristics for navigating enormous spaces.

This distinction is fundamental to rationality. Rational reasoning is not identical to exhaustive search. Much of mathematics consists of discovering a representation that makes the search tractable.

---

# 5. Formalization Is Powerful—but Formalization Is Not Meaning

The rise of Lean makes an important epistemological point unusually visible.

Lean's own documentation states that its kernel checks proof terms, but it explicitly distinguishes **“does the theorem have a valid proof?”** from **“what does the theorem statement mean?”** A successful check is meaningful only if the formal statement corresponds to the intended informal meaning and if the imported mathematical environment is trusted. ([Lean Language][22])

This is not a weakness of Lean. It is an unavoidable fact about formalization.

Suppose a natural-language problem says:

> “Find a structure with property \(P\).”

One still has to choose the precise definitions of “structure” and “property \(P\).”

The formal system then answers the question:

> “Does this precisely encoded proposition follow from these axioms?”

That is enormously valuable.

But the first question remains human—or at least semantic:

> “Was this the proposition we meant?”

The Navier–Stokes controversy demonstrates this perfectly. If a proof genuinely establishes a branch of the official Clay statement, then the formal result may be mathematically valid. Yet another question can remain: is that branch capturing the scientific phenomenon mathematicians had primarily intended to understand? The two questions are different.

Formalization thus creates a new division:

**syntax-level rigor** can be automated;

**semantic-level adequacy** cannot simply be assumed.

The same point appears in ordinary mathematics. A formal theorem can be correct and still be trivial, irrelevant, redundantly formulated, or conceptually uninteresting.

---

# 6. The Mathematician: What Is the Job?

There is no universally accepted official “tier system” for mathematicians beyond ordinary career structures, so the following is an analytic taxonomy of mathematical work rather than a professional credential hierarchy.

## Tier 1: The mathematical learner

The learner develops fluency with notation, definitions, standard proof techniques, examples, and problem-solving patterns. The central activity is acquiring the language and internal grammar of a field.

## Tier 2: The independent problem solver

At this stage, the mathematician can work on unfamiliar problems, combine known techniques, and navigate literature. The emphasis is still primarily on solving questions within existing conceptual frameworks.

## Tier 3: The specialist researcher

The specialist does not merely solve problems; they identify gaps in the field, develop lemmas, construct examples and counterexamples, and develop localized techniques that other researchers can reuse.

## Tier 4: The theory builder

The theory builder introduces definitions, invariants, frameworks, or organizing principles that change the way a class of problems can be attacked.

## Tier 5: The synthesizer or field architect

This person connects multiple subfields, imports concepts across disciplinary boundaries, or reorganizes existing knowledge into a larger structure.

## Tier 6: The paradigm-forming mathematician

This is the rarest category. The work does not merely solve a difficult problem but changes the questions that are considered natural, creates a new language, or produces a framework that reorganizes significant portions of the subject.

These levels are not mutually exclusive. A mathematician can be an extraordinary solver but not a theory builder; a conceptual architect can be weak at routine computation; a great formalizer may not be a great expositor.

That fact is important because the modern debate often implicitly treats “mathematician” as though it were one unitary skill.

It is not.

### What do modern mathematicians actually do?

Contemporary mathematical research commonly involves:

* proving conjectures;
* constructing counterexamples;
* inventing definitions;
* classifying structures;
* discovering invariants;
* simplifying existing theories;
* translating between fields;
* performing symbolic or numerical experiments;
* reading and synthesizing huge literatures;
* formalizing results;
* finding applications;
* developing computational tools.

AI is relevant to all of these, but at very different levels.

A theorem-prover primarily attacks deduction and proof search.

A literature agent attacks information retrieval and synthesis.

A symbolic engine attacks manipulation and computation.

A generative model attacks conjecture generation and candidate argument construction.

A human mathematician may still be the person deciding **which problem deserves any of these operations**.

---

# 7. Deconstructing the Intelligence Myth

Why does mathematics have such a strong cultural association with “intelligence”?

Part of the explanation is sociological rather than mathematical.

Mathematics is unusually useful for **sorting** people. School systems can assign scores, competitions can rank contestants, entrance exams can standardize performance, and technical careers can attach economic rewards to mathematical credentials. The result is a social feedback loop in which success at mathematical tasks becomes evidence of generalized intellectual worth.

A second factor is information asymmetry. Most people cannot directly inspect advanced mathematics. As a result, they are forced to infer the ability of mathematicians from prestige markers: elite university affiliations, awards, famous problems, abstruse notation, and media narratives about “genius.”

A third is the prestige effect associated with unusually selective mathematical competitions. The competition itself creates a visible hierarchy that can be mistaken for a hierarchy of general human worth.

A fourth is psychological.

Research on mathematics anxiety shows that anxiety and social context can materially affect mathematical performance. A large meta-analysis spanning 177 studies and more than 900,000 participants found significant relationships between anxiety and mathematics performance, with working memory and task characteristics playing important roles. ([Springer][23]) Another meta-analysis of 84 samples found a robust negative relationship between math anxiety and performance. ([PubMed Central (PMC)][24])

That matters because performance on a mathematical test is not a pure meter of abstract reasoning ability. It is a product of prior education, familiarity, working memory, confidence, anxiety, cultural expectations, and task format.

Stereotype effects provide another mechanism through which the cultural idea of mathematical “natural ability” can become self-reinforcing. The literature on mathematics anxiety and stereotype threat finds evidence that social expectations can affect performance, while also emphasizing that the precise causal mechanisms are complex and should not be overstated. ([Taylor & Francis Online][25])

There is also an institutional mechanism analogous to the Matthew effect in science. Research on scientific careers documents self-reinforcing patterns in which established scientists receive disproportionate recognition for subsequent achievements relative to less established researchers producing similar work. ([ScienceDirect][26])

In mathematical culture, the same general process can amplify the “genius” image.

Once a person is recognized as extraordinary, every future success is interpreted through that lens. The public sees the theorem, not the years of training, failed approaches, collaborators, informal conversations, literature searches, pedagogical support, or institutional resources that enabled it.

The cultural equation therefore becomes:

$$
\text{mathematical success}
\;\approx\;
\text{intelligence}
\;\approx\;
\text{wisdom}.
$$

That equation is unjustified.

Mathematical achievement is evidence of extraordinary competence in some dimensions of cognition and practice. It is not evidence that a person possesses superior judgment in every domain, nor that mathematical excellence is reducible to an underlying quantity called “intelligence.”

AI destabilizes this myth because it makes a formerly invisible fact impossible to ignore:

> A large part of mathematical performance consists of learnable procedures, representations, search strategies, symbolic transformations, and access to enormous informational resources.

Once machines become competent at those tasks, it becomes harder to treat successful mathematical performance as a transparent window into some singular human essence called intelligence.

---

# 8. Formalization, Rationality, and Whether AI Is “Inferior”

The strongest version of the human-superiority thesis says that because mathematics is rational, a machine can never truly replace the mathematician.

But this argument does not follow.

Suppose a problem is:

1. precisely specified;
2. formally expressible;
3. governed by explicit inference rules;
4. sufficiently computable;
5. judged primarily by correctness.

In such a problem class, there is no principled reason to assume that humans must remain superior.

Indeed, AI systems may have structural advantages:

* much larger memory;
* parallel search;
* persistence;
* precise symbolic manipulation;
* automatic checking;
* large-scale literature retrieval;
* rapid generation of variants;
* no fatigue.

The relevant question is not whether humans are “more intelligent,” but which cognitive architecture is better matched to the task.

This is already visible in chess, theorem proving, symbolic computation, numerical optimization, and formal verification.

The opposite claim is equally mistaken:

> “Because AI can formalize and prove things, it will automatically replace mathematicians.”

That fails because mathematical research is not equivalent to proof search.

There is a major difference between:

$$
\text{Given } P,\ \text{find a proof of } P
$$

and

$$
\text{What proposition } P\text{ should we investigate?}
$$

There is also a difference between:

$$
\text{Find a theorem satisfying constraints } C
$$

and

$$
\text{Discover a representation that makes an entire class of theorems intelligible.}
$$

The second task includes a problem-selection component.

### A better division of labor

A plausible future division is not “AI does calculations, humans do thinking.” That boundary is already obsolete.

A more realistic division is:

**AI**

* explores huge candidate spaces;
* proposes lemmas;
* searches proofs;
* formalizes statements;
* checks arguments;
* scans literature;
* generates counterexamples;
* runs large computational experiments;
* tests variants;
* maintains formal libraries.

**Humans**

* choose research goals;
* select definitions;
* determine which abstractions are useful;
* judge significance;
* establish attribution;
* interpret results;
* decide when a result changes the conceptual landscape;
* integrate mathematics with scientific, social, or philosophical purposes.

Yet this is not a rigid division. AI can increasingly contribute to goal formation, and humans increasingly depend on computational systems for discovery.

The emerging relationship is therefore better described as **iterative co-construction**.

---

# 9. Mathematics Is Not Exhausted by One Western Formal Framework

A discussion of AI and mathematics also needs to avoid another hidden assumption: that the contemporary Western formal tradition is identical to mathematics as such.

Modern mathematics has a powerful universal formal language, but the historical development of mathematical ideas has been global and culturally diverse.

The development of zero and the decimal place-value system, for example, involved Indian mathematics and later transmission through Islamic mathematical traditions into Europe. Chinese mathematics developed substantial traditions of algebra, geometry, interpolation, astronomy, and computation. Histories of Islamic mathematics show that the mathematical sciences were intertwined with mechanics, optics, astronomy, and instruments rather than conforming neatly to today's disciplinary boundaries. ([Maths History][27])

This matters conceptually.

Mathematics is not only what happens inside today's institutional category called “pure mathematics.” It also emerges from different practical pressures, representational choices, scientific problems, computational needs, philosophical commitments, and systems of education.

One should not therefore replace the older claim

> “Western mathematicians invented mathematics”

with the equally simplistic claim

> “Every mathematical tradition is simply another version of exactly the same thing.”

A more accurate formulation is that human cultures have developed different mathematical practices, some of which have been progressively translated into a highly interoperable modern formal language.

AI inherits that language disproportionately because today's training corpora and formal libraries are concentrated there.

Thus an AI trained on contemporary formal mathematics may become extraordinarily powerful **inside a particular mathematical regime** without thereby exhausting the space of possible mathematical cognition.

---

# 10. Can AI Formulate Groundbreaking Theories?

The statement “AI cannot formulate groundbreaking mathematics” is much too strong.

But the opposite statement—

> “Because AI can produce novel proofs, AI can therefore originate mathematical paradigms”—

is equally unsupported.

The first issue is definitional.

A “groundbreaking” mathematical result should not be defined merely by difficulty. A very difficult theorem can be conceptually routine. Conversely, an apparently modest theorem can introduce a definition or viewpoint that later reorganizes a field.

A useful working definition is:

> **A groundbreaking mathematical idea changes the space of problems that can naturally be asked, changes the representations in which those problems are studied, or unifies previously disconnected results under a reusable framework.**

On that definition, a groundbreaking contribution may be one of five things:

1. a new object;
2. a new invariant;
3. a new representation;
4. a new proof paradigm;
5. a new bridge between fields.

This makes the AI question harder—but also more empirical.

### What does the current evidence show?

FirstProof's organizers explicitly state that mathematical research includes asking new questions and developing frameworks, but that they currently lack a concrete experimental methodology for measuring autonomous AI performance at that stage. ([1stproof][4])

That means the scientific literature should resist claiming too much.

At the same time, FirstProof Batch 2 found that AI systems sometimes generated novel arguments differing from the human solutions, including a problem on stochastic PDEs where the AI proof was judged correct and novel. ([1stproof][4])

So the empirical position is:

**AI can already generate some novel mathematical arguments.**

**AI can sometimes solve previously unpublished research-level problems.**

**Current evidence is insufficient to conclude that AI has independently generated broad, field-defining mathematical paradigms at the level associated with the most transformative episodes of mathematical history.**

That is a much stronger and more defensible conclusion than either extreme.

---

# 11. Do All Human Mathematicians Formulate Groundbreaking Ideas?

Obviously not.

This point is often omitted from the AI debate because “the mathematician” is treated as though every human mathematician were a potential Gauss or Grothendieck.

Most mathematical research is not paradigm founding.

Most scientists are not Newton.

Most writers are not Shakespeare.

Most mathematicians do not invent new mathematical languages.

The profession depends precisely on the existence of a large population of competent researchers who extend, verify, simplify, specialize, connect, teach, formalize, generalize, and apply ideas developed by a smaller number of unusually generative thinkers.

That creates an important asymmetry.

If AI automates 70 percent of routine theorem proving, this does not mean “70 percent of mathematicians disappear” in any straightforward sense.

It may instead mean that the **composition of mathematical labor changes**.

The scarce activity could migrate upward:

$$
\text{proof execution}
\rightarrow
\text{proof design}
\rightarrow
\text{problem formulation}
\rightarrow
\text{framework selection}
\rightarrow
\text{significance judgment}.
$$

But even that should not be taken as inevitable. AI may eventually become strong at higher levels as well.

The correct approach is empirical: identify which tasks remain bottlenecks and redesign institutions around those bottlenecks.

---

# 12. Why Descartes, Newton, Leibniz, and Gauss Matter

The history of mathematics also undermines any simplistic assumption that paradigm-changing mathematics is always produced inside narrow disciplinary specialization.

Descartes combined philosophy with geometry and introduced the algebraic-geometric framework that became Cartesian geometry. ([Maths History][28]) Newton transformed mathematics through an interaction among calculus, mechanics, astronomy, and optics. ([Maths History][29]) Leibniz worked across mathematics, logic, philosophy, mechanical calculation, and the sciences, while developing the notation that became central to modern calculus. ([Maths History][30]) Gauss worked across number theory, analysis, differential geometry, geodesy, magnetism, astronomy, optics, and statistics. ([Maths History][31])

These examples should not be romanticized into a claim that polymathy is automatically superior to specialization.

Their importance is different.

They demonstrate that mathematics can undergo conceptual transformation at the **interfaces between domains**.

The modern institutional structure fragments these interfaces into departments, journals, specialties, conferences, and vocabularies. That organization has enormous advantages, because advanced mathematics is too large for any one person to master completely.

But it also creates a paradox.

The more mathematics specializes, the more valuable mechanisms for **cross-domain synthesis** may become.

AI could become particularly powerful here because it can maintain access to many mathematical dialects simultaneously.

A human specialist may know one neighborhood extraordinarily deeply.

An AI system may be able to retrieve the maps of a thousand neighborhoods and search for roads connecting them.

That does not guarantee that it knows which roads matter.

But it changes the economics of interdisciplinary discovery.

---

# 13. Rationality, Quantification, Computability, and the Intrinsic/Extrinsic Divide

The AI-mathematics debate is ultimately a debate about rationality itself.

One common assumption is:

$$
\text{rationality}
=
\text{formal logic}.
$$

That is too narrow.

Formal logic is one part of rationality.

So are:

* choosing what to measure;
* deciding which variables matter;
* selecting a model;
* identifying an analogy;
* deciding what counts as evidence;
* evaluating relevance;
* allocating attention.

These activities can be rational without being reducible to a finite proof calculus.

Similarly:

$$
\text{quantifiable} \neq \text{fully intelligible}.
$$

A model can measure something without explaining it.

A theorem can be true without telling us why the concept is important.

A proof assistant can verify a relation without deciding whether the relation deserves to occupy the center of a theory.

The distinction can be expressed through two dimensions.

### Intrinsic mathematics

This concerns internal relations:

* definitions;
* axioms;
* proofs;
* deductions;
* invariants;
* constructions;
* equivalences.

This is the territory in which AI and formal systems have the clearest advantage.

### Extrinsic mathematics

This concerns the relation of mathematics to:

* scientific problems;
* physical reality;
* technological needs;
* human purposes;
* aesthetics;
* institutions;
* history;
* education;
* conceptual significance.

AI can help here too, but the evaluation criteria become less reducible to formal validity.

The future of mathematical AI will therefore depend on whether systems can cross the boundary between these dimensions rather than merely becoming faster at the first.

---

# 14. What the Mathematical Profession Should Become

The most useful response to AI is not to defend every existing task equally. It is to distinguish what should be automated from what should be preserved, transformed, or made more valuable.

A future mathematician may spend less time manually checking routine algebra and more time designing the conceptual architecture of a proof.

A graduate student may learn Lean early, not as an alternative to mathematics but as one of the mathematical languages alongside ordinary notation.

Research groups may become mixed human-AI laboratories in which machines generate thousands of conjectures and humans decide which ten deserve attention.

Formal proof libraries may become the mathematical equivalent of modern software repositories: shared infrastructure that allows entire fields to build on machine-checked foundations.

This is already visible in the ecosystem around Lean, where the kernel provides a relatively small trusted core while automation generates proof terms checked by that core. Lean's documentation emphasizes precisely this architecture: sophisticated tactics may construct proofs, but the trusted kernel checks the resulting proof object. ([Lean Language][32])

The institutional consequence is substantial.

The mathematician of the future may need to be simultaneously:

* concept designer;
* AI orchestrator;
* formalization expert;
* literature navigator;
* proof auditor;
* model critic;
* interdisciplinary translator.

The profession would not become less mathematical.

It would become **more explicitly architectural**.

---

# 15. Meta-Reflective Synthesis: Toward a Mathematics of Mutual Containment

The deepest lesson of the AI transition may be that the usual distinctions—human versus machine, proof versus discovery, mathematics versus computation, intuition versus logic—are less independent than they first appear.

A mathematical theorem depends on a definition.

A definition depends on a conceptual distinction.

A conceptual distinction is motivated by a problem.

A problem emerges inside a historical and scientific context.

A proof is expressed through a language.

That language is implemented by a formal system.

The formal system is checked by software.

The software is built by people.

The people are shaped by institutions.

The institutions distribute attention, prestige, resources, and information.

The resulting mathematics then feeds back into the tools that generate the next mathematical questions.

There is therefore no clean boundary at which “pure mathematics” stops and “human context” begins.

Even a completely formal theorem lives within a network of meanings.

This does not reduce mathematics to sociology. Nor does it reduce mathematics to computation.

It means that different descriptions are simultaneously valid at different levels.

A theorem can be viewed as:

* a formal object;
* a proof object;
* a conceptual pattern;
* a piece of knowledge;
* a communication artifact;
* a component of a theory;
* a step in a research program.

AI is beginning to operate on many of these descriptions at once.

That is why its impact feels so profound.

The machine is not simply replacing a calculator.

It is entering a network of mutually dependent activities that humans previously experienced as one indivisible practice called “doing mathematics.”

The appropriate response is therefore neither to romanticize human intuition nor to declare the death of mathematical expertise.

The more coherent interpretation is that mathematics is revealing its own internal plurality.

Some mathematical labor is fundamentally formal and therefore increasingly automatable.

Some is computational and therefore naturally machine-amplified.

Some is exploratory and can increasingly be shared.

Some is interpretive.

Some is organizational.

Some concerns the selection of concepts.

Some concerns deciding what deserves to become part of collective knowledge.

No single one of these is identical with “mathematics.”

The future is consequently unlikely to be a simple replacement of mathematicians by machines. A more plausible trajectory is a restructuring in which humans and AI increasingly occupy overlapping portions of the mathematical process.

The decisive question will not be:

> **Which side is more intelligent?**

It will be:

> **Which configuration of humans, machines, formal systems, institutions, representations, and purposes produces mathematics that is both more reliable and more illuminating?**

That question changes the entire frame.

It moves the discussion away from competition over status and toward the architecture of knowledge.

A machine that proves a theorem is not thereby a human mathematician.

A human who understands a theorem is not thereby the sole source of its possibility.

A formal system is not the whole of meaning.

An intuition is not the opposite of rationality.

A mathematical culture is not separable from the tools through which it thinks.

And a new mathematical capability does not simply destroy an old one; it changes the environment in which that old capability acquires value.

The emerging mathematical order may therefore be understood as a system of **mutual containment**: each layer enters the others, constrains them, amplifies them, and acquires meaning through them. Formal proof depends on conceptual choice; conceptual choice depends on information; information depends on representation; representation depends on tools; tools depend on formal knowledge; formal knowledge depends on communities that recognize what is worth formalizing.

Nothing stands entirely outside the network.

From this perspective, the arrival of increasingly capable mathematical AI is not principally a story about the triumph of one kind of mind over another.

It is a revelation about mathematics itself.

Mathematics was never only calculation.

It was never only proof.

It was never only intuition.

It was never only abstraction.

It was a continually evolving system in which problems generate representations, representations generate theories, theories generate new problems, and communities develop tools capable of transforming the entire cycle.

AI is entering that cycle.

The historical significance of the moment will therefore depend less on whether a machine can imitate the mathematician of yesterday than on whether humans and machines together can enlarge the space of mathematics tomorrow.

---

# Selected Reference Base

### Recent AI and mathematics

1. **Google DeepMind.** “AlphaGeometry: An Olympiad-level AI system for geometry.” 17 January 2024. ([Google DeepMind][1])
2. **Google DeepMind.** “AI achieves silver-medal standard solving International Mathematical Olympiad problems.” 25 July 2024. ([Google DeepMind][6])
3. **Hubert et al.** “Olympiad-level formal mathematical reasoning with reinforcement learning.” *Nature* (2025). ([Nature][7])
4. **Google DeepMind.** “Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad.” 2025. ([Google DeepMind][2])
5. **Achim et al.** “Aristotle: IMO-level Automated Theorem Proving.” arXiv:2510.01346 (2025). ([arXiv][3])
6. **First Proof Project.** “First Proof” and “First Proof Second Batch.” 2026. ([1stproof][8])
7. **OpenAI.** “Our First Proof submissions.” 20 February 2026. ([OpenAI][33])
8. **Feng et al.** “Aletheia tackles FirstProof autonomously.” arXiv:2602.21201 (2026). ([arXiv][9])
9. **Feng et al.** “Towards Autonomous Mathematics Research.” arXiv:2602.10177 (2026). ([arXiv][10])
10. **OpenAI.** “On the Navier–Stokes Millennium Prize Problem.” 8 September 2026. ([OpenAI][5])
11. **Clay Mathematics Institute.** “Navier-Stokes Announcement.” 11 September 2026. ([Clay Mathematics Institute][12])
12. **Clay Mathematics Institute.** “Rules for the Millennium Prize Problems.” ([Clay Mathematics Institute][14])
13. **Scientific American.** “Did OpenAI solve the wrong Navier-Stokes problem?” 21 September 2026. ([Scientific American][13])

### Mathematics, formalization, and foundations

14. **Lean Language Reference.** Lean 4 documentation, especially “Validating Proofs” and “Axioms.” ([Lean Language][22])
15. **Stanford Encyclopedia of Philosophy.** “Philosophy of Mathematics.” ([Stanford Encyclopedia of Philosophy][19])
16. **Stanford Encyclopedia of Philosophy.** “Gödel’s Incompleteness Theorems.” ([Stanford Encyclopedia of Philosophy][20])
17. **Stanford Encyclopedia of Philosophy.** “The Church–Turing Thesis.” ([Stanford Encyclopedia of Philosophy][21])
18. **Stanford Encyclopedia of Philosophy.** “Structuralism in the Philosophy of Mathematics.” Revised 2025. ([Stanford Encyclopedia of Philosophy][34])
19. **Stanford Encyclopedia of Philosophy.** “Intuitionism in the Philosophy of Mathematics.” ([Stanford Encyclopedia of Philosophy][35])

### History, sociology, and psychology

20. **MacTutor History of Mathematics.** Biographies of Descartes, Newton, Leibniz, and Gauss. ([Maths History][28])
21. **Mathematical Association of America / history sources** on India, China, and Islamic mathematics. ([Maths History][27])
22. **Caviola et al.** “Math Performance and Academic Anxiety Forms…” *Educational Psychology Review* (2022). ([Springer][23])
23. **Namkung, Peng & Lin.** “The Relationship Between Math Anxiety and Math Performance: A Meta-Analytic Investigation.” ([PubMed Central (PMC)][24])
24. **Mertonian/Matthew-effect research** on recognition and scientific careers. ([ScienceDirect][26])
25. **Leiden Declaration on Artificial Intelligence and Mathematics**, 2026; endorsements and institutional responses from the IMU, LMS, and EMS. ([Leiden AI & Mathematics Declaration][18])
26. **Terence Tao.** “Mathematics in the age of AI.” arXiv:2608.16753 (2026). ([arXiv][17])

## A concise editorial assessment of the evidence

The evidence currently supports five propositions particularly well.

**First**, AI has crossed a genuine threshold from routine mathematical assistance to high-level theorem solving and, in selected cases, research-level proof construction. ([Google DeepMind][2])

**Second**, formal verification materially improves reliability, but formal verification does not eliminate semantic, bibliographic, or interpretive failure. Lean's own documentation makes this distinction explicit. ([Lean Language][22])

**Third**, contemporary AI systems can sometimes produce genuinely novel mathematical arguments, so “AI is merely copying known proofs” is no longer an adequate general description. FirstProof provides direct evidence of this. ([1stproof][4])

**Fourth**, there is not yet comparable evidence establishing broad autonomous paradigm formation—new mathematical languages, foundational frameworks, or durable shifts in what mathematicians regard as important questions. The most carefully designed evaluations explicitly identify this as an unmeasured dimension. ([1stproof][4])

**Fifth**, the most serious emerging challenge is institutional rather than logical: how authorship, attribution, verification, confidentiality, publication, responsibility, and mathematical understanding should operate when proof-producing systems are increasingly capable. The Leiden Declaration, FirstProof methodology, and the current Navier–Stokes controversy all point toward that problem from different directions. ([Leiden AI & Mathematics Declaration][16])

That is why the AI–mathematics transformation should be understood neither as the collapse of mathematics nor as a simple victory of machines. It is the beginning of a redefinition of what counts as a mathematical task, what counts as evidence, and what it means to participate in the production of mathematical knowledge.

[1]: https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/?utm_source=chatgpt.com
[2]: https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/?utm_source=chatgpt.com
[3]: https://arxiv.org/abs/2510.01346?utm_source=chatgpt.com
[4]: https://1stproof.org/assets/docs/report.pdf
[5]: https://openai.com/index/navier-stokes-solution/?utm_source=chatgpt.com
[6]: https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/?utm_source=chatgpt.com
[7]: https://www.nature.com/articles/s41586-025-09833-y?utm_source=chatgpt.com
[8]: https://1stproof.org/?utm_source=chatgpt.com
[9]: https://arxiv.org/abs/2602.21201?utm_source=chatgpt.com
[10]: https://arxiv.org/abs/2602.10177?utm_source=chatgpt.com
[11]: https://lean-lang.org/doc/reference/latest?utm_source=chatgpt.com
[12]: https://www.claymath.org/news/navier-stokes-announcement/?utm_source=chatgpt.com
[13]: https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/
[14]: https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf
[15]: https://www.claymath.org/millennium/navier-stokes-equation/
[16]: https://leidendeclaration.ai/?utm_source=chatgpt.com
[17]: https://arxiv.org/abs/2608.16753?utm_source=chatgpt.com
[18]: https://leidendeclaration.ai/about?utm_source=chatgpt.com
[19]: https://plato.stanford.edu/entries/philosophy-mathematics/?utm_source=chatgpt.com
[20]: https://plato.stanford.edu/entries/goedel-incompleteness/?utm_source=chatgpt.com
[21]: https://plato.stanford.edu/archives/sum2025/entries/church-turing/?utm_source=chatgpt.com
[22]: https://lean-lang.org/doc/reference/latest/ValidatingProofs/?utm_source=chatgpt.com
[23]: https://link.springer.com/article/10.1007/s10648-021-09618-5?utm_source=chatgpt.com
[24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6692457/?utm_source=chatgpt.com
[25]: https://www.tandfonline.com/doi/full/10.1080/14794802.2013.797744?utm_source=chatgpt.com
[26]: https://www.sciencedirect.com/science/article/pii/S1751157723000901?utm_source=chatgpt.com
[27]: https://mathshistory.st-andrews.ac.uk/HistTopics/Zero/?utm_source=chatgpt.com
[28]: https://mathshistory.st-andrews.ac.uk/Biographies/Descartes/?utm_source=chatgpt.com
[29]: https://mathshistory.st-andrews.ac.uk/Biographies/Newton/?utm_source=chatgpt.com
[30]: https://mathshistory.st-andrews.ac.uk/Biographies/Leibniz/?utm_source=chatgpt.com
[31]: https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/?utm_source=chatgpt.com
[32]: https://lean-lang.org/doc/reference/latest/Tactic-Proofs/?utm_source=chatgpt.com
[33]: https://openai.com/index/first-proof-submissions/?utm_source=chatgpt.com
[34]: https://plato.stanford.edu/entries/structuralism-mathematics/?utm_source=chatgpt.com
[35]: https://plato.stanford.edu/entries/intuitionism/?utm_source=chatgpt.com
