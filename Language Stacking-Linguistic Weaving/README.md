# 语言叠织 · Language Stacking & Linguistic Weaving

> **一意而万语，一镜而八澜。**
> *One meaning, a thousand tongues; one mirror, eight ripples.*

「语言叠织」是把同一个心象，用 **八种语言**——中文、English、Français、日本語、संस्कृतम्、Latina、Deutsch、Svenska——对照叠放、互为注释、织成一锦。它既是内容作品（视频 / 图文卡 / 网站），也是方法（结构化平行语料库 + 多模态流水线）。

**这条工程的灵魂：充分体现每一种语言的特色，及其背后的文明核心味道。** 一种语言绝不只是一只"译文的容器"，它是一套世界观，是一段文明的呼吸——汉字的礼乐与天人合一，英文的经验主义与契约精神，法文的启蒙与雄辩，日文的物哀与留白，梵文的圣言与内观，拉丁的罗马法与斯多葛，德文的观念论与秩序，瑞典文的北欧自然与适度。

*Language Stacking & Linguistic Weaving presents one *image of thought* in eight languages — Chinese, English, French, Japanese, Sanskrit, Latin, German, Swedish — stacked, woven, and mutually annotated. It is both a body of work (video / text-image cards / website) and a method (structured parallel corpus + multimodal pipeline).*

*The soul of this project: let each language show its own character, and the civilizational core it carries. A language is never just a container for translation — it is a worldview, the breathing of a civilization: the rites and harmony of Hanzi, English empiricism and contract, French Enlightenment and eloquence, Japanese mono-no-aware and restraint, Sanskrit as sacred utterance and inner science, Latin law and Stoic calm, German idealism and order, Swedish Nordic clarity and lagom.*

| 元信息 Meta | 值 Value |
|---|---|
| 状态 Status | v1.0 总体规划 Master Plan |
| 日期 Date | 2026-09-14 |
| 所属 Workspace | `gruel_cooking`（舟洲粥 · 六大支柱之「语」） |
| 文档语言 Doc language | 中文 Chinese + English（本文档双语） |
| 内容语言 Content languages | zh · en · fr · ja · sa · la · de · sv（+ 附录 C 扩展预案） |

---

## 目录 Table of Contents

1. [缘起与愿景 Vision](#1-缘起与愿景-vision)
2. [核心设计理念 Design DNA](#2-核心设计理念-design-dna)
3. [语言与文明矩阵 Language × Civilization Matrix](#3-语言与文明矩阵-language--civilization-matrix)
4. [主题矩阵 Theme Matrix](#4-主题矩阵-theme-matrix)
5. [选材与语料库 Corpus & Sourcing](#5-选材与语料库-corpus--sourcing)
6. [多模态总设计 Multimodal Master Design](#6-多模态总设计-multimodal-master-design)
7. [格式模板 Format Templates](#7-格式模板-format-templates)
8. [制作流水线 Production Pipeline](#8-制作流水线-production-pipeline)
9. [工具栈 Toolchain](#9-工具栈-toolchain)
10. [翻译方法论 Translation Doctrine](#10-翻译方法论-translation-doctrine)
11. [质量控制 QA](#11-质量控制-qa)
12. [发布与增长 Publish & Growth](#12-发布与增长-publish--growth)
13. [路线图 Roadmap](#13-路线图-roadmap)
14. [首批制作清单 First Deliverables](#14-首批制作清单-first-deliverables)
15. [目录结构与命名规范 Directory & Naming](#15-目录结构与命名规范-directory--naming)
16. [附录 A 数据模型 Data Model](#16-附录-a-数据模型-data-model)
17. [附录 B 8 语完整对照样例 Worked Sample](#17-附录-b8-语完整对照样例-worked-sample)
18. [附录 C 扩展语种预案 Expansion Playbook](#18-附录-c扩展语种预案-expansion-playbook)
19. [附录 D 概念 × 八语术语表 Core Glossary](#19-附录-d概念--八语术语表-core-glossary)

---

## 1. 缘起与愿景 Vision

**为什么做这个？** 同一个意思，不同语言有不同的"说话方式"——中文的凝练、英文的精确、法文的优雅、日文的留白、梵文的神圣、拉丁的庄严、德文的思辨、瑞典文的澄澈。把这些"说话方式"并置在一起，**语言本身就是风景，翻译本身就是创作**；而每一种语言背后站着一种文明的理由——这正是本工程最深的着力点。

*Why? The same meaning is *said differently* in every language — Chinese condensation, English precision, French elegance, Japanese ellipsis, Sanskrit sacrality, Latin solemnity, German speculation, Swedish clarity. When placed side by side, the languages themselves become the scenery; translation itself becomes the art — and behind every language stands the reason of a civilization.*

**目标 Goals：**
- 做出 **美观、准确、有呼吸感** 的多语对照视频与图文卡，让观众"看见语法的多样、听出语音的节奏、闻到文明的味道"。
  *Tasteful, accurate, breathable multilingual media — let viewers see the variety of grammar, hear the rhythm of speech, and sense the flavor of civilizations.*
- 建立 **可持续、可复用、可校验** 的内容管线：一处语料，多渠道输出。
  *A sustainable, reusable, verifiable pipeline — one corpus, many outputs.*
- 成为「舟洲粥」人文工程的第六支柱，与 first principles、跨文化经济、living_heritage（大运河 ↔ Gotland）互相滋养。瑞典语正是与 Gotland 案例天然咬合的一环。
  *Serve as the sixth pillar of the zhōuzhōuzhōu humanities project, cross-pollinating with first-principles, cross-culture economics, and living_heritage (Grand Canal ↔ Gotland); Swedish is the natural hinge to the Gotland case.*

**三条可行的并列原则 Principles：**
1. **同题多语** —— 一个心象，八面镜子（*one image of thought, eight mirrors*）。
2. **先准后美** —— 准确到可以教学，然后才谈美学（*accurate enough to teach, then beautiful*）。
3. **匠心颗粒度** —— 每个字（形）、每个音都是产品的一部分（*every glyph and every phoneme is part of the product*）。

---

## 2. 核心设计理念 Design DNA

三个动词定义全部创作：

| 支柱 Pillar | 含义 Meaning | 落到制作 Production |
|---|---|---|
| **叠 Stack** | 同一心象在 8 语中叠加并置：一套语法，一面镜子 | 同一句、同一画面基底，多语文本逐层浮现 |
| **织 Weave** | 语言互为注释：词源、直译、文化注疏缝合一体 | 三行对照（原文 / 译文 / 字面直译 + 注）；词源动画 |
| **照 Illuminate** | 每语一个"角色"、一种音色、一种色彩、一种文明气韵 | 语言×文明身份卡；发音即音色；字型即表情 |

**四条铁律 Iron Rules：**
1. **源先于叙事 Sources before narrative** —— 引用必标出处，公版与原创优先；绝不把未经审校的译文冒充权威。*Cite primary sources; prefer public-domain and original texts; never pass unreviewed translations off as authoritative.*
2. **一处语料，一切输出 One source of truth** —— 平行语料只存一份（JSON 三行对照），视频 / 卡图 / 网站都从它渲染，杜绝多渠道漂移。*Store each parallel text once; every output renders from it.*
3. **绝不静默出错 No silent errors** —— 每个字形（天城体连字、日文竖排、拉丁 macron）、每个发音，都在 QA 门内显式验证。*Every script rendering and every pronunciation passes an explicit QA gate.*
4. **宁少勿滥，宁缓勿错 Slow is smooth** —— 先出 5 条试片跑通全链，再放量。*Ship 5 pilots first, prove the chain, then scale.*---

## 3. 语言与文明矩阵 Language × Civilization Matrix

每种语言一张「身份卡」，全工程制作的**总辞典**：字体、颜色、音乐、口吻、以及它要传达的"文明核心味"都从这里取，保证整套内容风格统一、味道分明。每种语言永远是"它自己的方式"说同一个意思——绝不做成机器对称的"八栏同一行"。

*Each language has one Identity Card — the master dictionary of the whole project: font, color, music, tone, and the "civilizational core flavor" it must carry. Every language always says the same thing *its own way*; never a mechanically symmetric 8-column row.*

### 3.1 身份卡总表 Summary Table

| 语种 Language | ISO | 语系 Family | 文字 Script | 文明核心味 Civilizational DNA | 角色 Role | 主色 Palette |
|---|---|---|---|---|---|---|
| **中文** Chinese | zh | 汉藏 Sino-Tibetan | 汉字 Hanzi | 天人合一 · 礼乐 · 诗教 · 和 | 诗眼与原乡 | 墨黑 + 朱砂红 + 留白 |
| **English** | en | 印欧·日耳曼 Germanic | Latinate | 经验主义 · 契约 · 个体 · 自由 | 精确的音叉 | 藏青 + 骨白 |
| **Français** 法语 | fr | 罗曼 Romance | Latinate (+éèàçœ) | 启蒙 · 理性 · 雄辩 · esprit | 哲思的低语 | 薰衣草紫 + 暖金 |
| **日本語** | ja | 日语系 Japonic | 汉字 + 假名 | 物哀 · 幽玄 · 侘寂 · 无常 | 留白的一瞬 | 和纸米 + 樱粉 + 墨 |
| **संस्कृतम्** 梵文 | sa | 印欧·印度雅利安 Indo-Aryan | 天城体 Devanagari | 圣言 · 业与法 · 梵我一如 · 内观 | 根与咒 | 姜黄 + 朱砂 + 莲花金 |
| **Latina** 拉丁 | la | 意大利语族 Italic | Roman (+macrons) | 罗马法 · 修辞 · 斯多葛 · 永续 | 不朽的铭刻 | 石灰岩白 + 暗铜 |
| **Deutsch** 德语 | de | 日耳曼 Germanic | Latinate (+äöüß) | 观念论 · 秩序 · 修养 · 森林 | 思想的拱顶 | 板岩灰 + 冷钢蓝 |
| **Svenska** 瑞典语 | sv | 北日耳曼 Nordic | Latinate (+åäö) | 北欧自然 · 适度 · 高信任 · 光 | 北境的澄澈 | 湖蓝 + 桦木白 + 苔绿 |

> **语种扩编（2026-09）**：生产编队已由 8 语扩至 **32 语**（6 大洲 × 12 语系 × 26 文字形态），核心 8 语全量产出不变，新增 24 语按三档排产（A 全链 TTS／B 真声／C 词卡）。身份卡全集与选语原则（谱系/文字/类型学/文明/可行性五棱镜）见 **[LANGUAGES_LINGUISTIC_EXPANSION.md](LANGUAGES_LINGUISTIC_EXPANSION.md)**。

### 3.2 逐语身份卡 Identity Cards

每张卡包含：**文明核心味（灵魂）→ 语言特色（表情）→ 制作要点（皮相）**。*Each card: civilizational DNA (soul) → linguistic character (expression) → production notes (skin).*

---

#### 中文 zh —— 诗眼与原乡 *The Poetic Source*

**文明核心味 Civilizational DNA：**
- **天人合一**：人不是自然的主人，而是自然的一部分；山水、农时、节气都是道德与美学的教材。`气和万物的伦理亲缘`
- **礼乐文明**：以礼立序、以乐化人；艺术从来不只是审美，而是修身齐家的功夫。`rites as ethics, music as cultivation`
- **诗教传统**：诗言志、文载道；"不学诗，无以言"——语言承载着道德的重量。`poetry as the mother tongue of ethics`
- **以和为贵**：中庸、尚同、求同存异；"和而不同"几乎就是本工程的纲领。`harmony in diversity — the project's own charter`

**语言特色 Linguistic Character：**
- 汉字是**表意方块字**：字即词、形声会意并行；一个字就是一幅微型画、一段典故。`Hanzi is ideographic: each character is a micro-painting and a classical allusion.`
- **意合（paratactic）**：不靠时态和连接词，靠语序与语感；留白即意义。`Paratactic: meaning rides on word order and feel; the unsaid matters.`
- 古文高度凝练：四字一句即是宇宙（"上善若水""逝者如斯"）。`Classical Chinese compresses a cosmos into four characters.`
- 单音节 + 声调：发音本身就是音乐（平仄、对仗）。`Tonal and mono-syllabic: sound is already music (level/oblique, parallelism).`

**制作要点 Production Notes：**
- 字体：宋体 / 楷体 / 行书（书法感用楷、行，正文标题用宋）。*Fonts: Songti for headings, Kaiti/Xingshu for calligraphic feel.*
- 颜色：墨黑为主，朱砂红印章点睛，大面积留白。*Ink-black dominant, cinnabar seal accents, generous whitespace.*
- 音乐：古琴、琵琶、箫笛，山风与空谷。*Guqin, pipa, xiao/dizi; wind and hollow valleys.*
- 口吻：见字如面，四两拨千斤；读诗要"慢，再慢"。*Slow, weighty, restrained.*

**常用试读句 Try-lines：**
- 「海上生明月，天涯共此时。」（张九龄）
- 「上善若水。」（《道德经》八章）
- 「逝者如斯夫！不舍昼夜。」（《论语·子罕》）

---

#### English —— 精确的音叉 *The Tuning Fork of Precision*

**文明核心味 Civilizational DNA：**
- **经验主义与实用主义**：从培根、洛克到美式 pragmatism，"可检验、可证伪、就这么办"。`Empiricism and pragmatism: verifiable, workable, do it.`
- **契约与法治**：common law 传统，白纸黑字；语言追求"把话说死、不留歧义"。`Contract and rule of law: language aims to say things precisely, leaving no ambiguity.`
- **个体主义与言论自由**：我思我言我负责；"I contain multitudes"。`Individualism and free speech: I think, I speak, I am responsible.`
- **清教徒工作伦理**：时间即金钱，节俭而严肃。`Work ethic: time is money, frugality is virtue.`

**语言特色 Linguistic Character：**
- **时态与语气完整**：句子像一台齿轮严密的机器，主谓宾 + 逻辑连接词。`Fully inflected tenses and moods; sentences mesh like machinery.`
- **词汇层叠**：日耳曼土词（freedom）与拉丁借用词（liberty）并置，天然双声部。`Two-layered vocabulary: Germanic (freedom) + Latinate (liberty) — naturally duophonic.`
- **简洁直接**主张："Say what you mean"，修辞被压缩进节奏与停连。`Directness is doctrine; rhetoric hides in rhythm and pause.`
- **介词系统极度发达**：位置、方向、关系一旦定位即精确。`A hyper-developed preposition system: precision through placement.`

**制作要点 Production Notes：**
- 字体：EB Garamond / Georgia 人文衬线；英式用典时可用 Trajan 式罗马大写。*EB Garamond / Georgia; Roman caps for inscriptions.*
- 颜色：藏青沉稳，骨白衬底，一点文书红。*Deep navy, bone white, a touch of document red.*
- 音乐：钢弦民谣、钢琴、弦乐四重奏。*Steel-string folk, piano, string quartet.*
- 口吻：清晰、直接、少修饰但有力；句读间的停顿即表情。*Clear, direct, spare but strong.*

**常用试读句 Try-lines：**
- "Into the woods I go, to lose my mind and find my soul."（谚语 · 无单一定说者，归为口传）
- "The woods are lovely, dark and deep."（Robert Frost）
- "I contain multitudes."（Walt Whitman）

---

#### Français fr —— 哲思的低语 *Philosophy's Whisper*

**文明核心味 Civilizational DNA：**
- **启蒙与理性主义**：笛卡尔"我思故我在"，百科全书理想；理性之光要照亮一切。`Cartesian reason; the Encyclopédie's dream that reason illuminates everything.`
- **大革命的普遍主义**：自由、平等、博爱；语言承载普世价值宣言。`The universalist cry of the Revolution: liberté, égalité, fraternité.`
- **esprit（精神/机智）**：沙龙文化——交谈是艺术，雄辩是公民美德。`The esprit of the salon: conversation as art, eloquence as civic virtue.`
- **法兰西学院的纪律**：正字与法统，语言是国家气质。`The Académie française: orthography as national character.`

**语言特色 Linguistic Character：**
- **联诵（liaison）与节奏**：辅音在词间流动，"说"本身即音乐与礼仪。`Liaison: consonants flow between words; speech is music and courtesy.`
- **主语 + 严密动词变位**：性别、数、时、式一丝不苟；表达讲究层次。`Disciplined morphology: gender, number, tense, mood — layered nuance.`
- **介词与心态的细腻**：aimer à / aimer de / aimer —— 三种爱，三种滋味。`Fine-grained prepositions: three loves, three flavors.`
- **雄辩传统**：从布道到议会，讲辞要有起承转合。`Oratorical lineage: sermon to parliament, speeches are built.`

**制作要点 Production Notes：**
- 字体：Didot 式花体 + 人文衬线；斜体优雅。*Didot-styled display + humanist serif; graceful italics.*
- 颜色：薰衣草紫与暖金，法蓝点缀。*Lavender and warm gold, a touch of royal blue.*
- 音乐：chanson、手风琴、极简钢琴。*Chanson, accordion, minimal piano.*
- 口吻：优雅而不装饰过度；句子之间用停顿换呼吸。*Elegant, unhurried; pauses are breath.*

**常用试读句 Try-lines：**
- « Il n'y a pas de vent favorable pour celui qui ne sait pas où il va. »（常归于 Sénèque，实为谚语化转述——需注释其流传属性）
- « Cent fois sur le métier remettez votre ouvrage. »（Boileau, *L'Art poétique*）
- « Le cœur a ses raisons que la raison ne connaît point. »（Pascal, *Pensées*）

---

#### 日本語 ja —— 留白的一瞬 *The Held Breath*

**文明核心味 Civilizational DNA：**
- **物哀 mono no aware**：见花落而知哀，哀而不伤——对万物无常的深情。`Sorrow-seeing beauty: grief without bitterness, tenderness for impermanence.`
- **幽玄 yūgen**：言外之意，不可言说处的深度；"月见草荣る奥山"的暗昧之美。`Depth beyond words; the beauty of the unsaid and shadowed.`
- **侘寂 wabi-sabi**：残缺、朴素、时间的锈迹也是美。`Flaws, plainness, the patina of time are beauty.`
- **精进与一期一会**：无常推人把当下做到极致；每一次相逢都是一生一次。`Impermanence demands perfection of the moment; every meeting is once-in-a-lifetime.`
- **神道与自然百神**：一粒米、一座山皆有神；自然不是资源而是神明。`Shinto: rice and mountain are kami; nature is divine, not resource.*`

**语言特色 Linguistic Character：**
- **汉字 + 平假名 + 片假名三套系统**共织：表意（汉字）、表音（假名）、外来（片假名），一眼即见文明交汇。`Three scripts woven: kanji (meaning), hiragana (native phonetics), katakana (borrowed).`
- **竖排（縦書き）**曾是诗的默认方向——上下流淌如雨丝。`Vertical writing is the natural direction of poetry — falling like rain.*
- **助词框定关系**，主语常省：暧昧即是精确，"以心传心"。`Particles frame relations; subjects often vanish; ambiguity is precision.*
- **擬音語・擬態語**极丰富：きらきら、そっと、しっとり——声音即意象。`Rich onomatopoeia: sound is image.*
- **敬语体系**是伦理的地图：见语言便知人际的等高线。`Keigo maps ethics: the topography of human relations lives in speech.*`

**制作要点 Production Notes：**
- 字体：明朝体（Mincho）正文 + 教科書体/行书手写感；竖排优先。*Mincho for body, textbook/handwritten style for warmth; vertical preferred.*
- 颜色：和纸米底、樱粉与墨；留白是构图的主角。*Washi-paper cream, sakura pink, sumi ink; whitespace is the protagonist.*
- 音乐：尺八、筝、三味线、雨声。*Shakuhachi, koto, shamisen, rain.*
- 口吻：一字千钧的省略；淡如茶，深如井。*Economy of the unsaid: pale as tea, deep as a well.*

**常用试读句 Try-lines：**
- 「古池や 蛙飛びこむ 水の音」（松尾芭蕉）
- 「月やあらぬ 春や昔の 春ならぬ 我が身ひとつは もとの身にして」（在原業平）
- 「請はば これは来む日は 短し ただ去り行く 日々」（芥川风之译写——勿用，示范不可编造；真作见下）*（示范警示：勿未审而引）*

---

#### संस्कृतम् sa —— 根与咒 *The Root & The Incantation*

**文明核心味 Civilizational DNA：**
- **圣言观**：梵语被称为 devabhāṣā "天语"；吠陀是所闻（śruti），语言本身是神圣的。`Sanskrit as divine speech (devabhāṣā); the Vedas are "heard", and language itself is sacred.*`
- **业与法 dharma · karma**：因果相续、正法为道；生命是一场可自觉的长旅。`Karma and dharma: cause and consequence, conduct as path, life as a self-aware journey.*`
- **梵我一如 ātman = brahman**：奥义书的核心直觉——小我即大我，语言止处有真。`The Upaniṣadic intuition: ātman and brahman are one; where words end, truth begins.*`
- **内观科学**：瑜伽、禅那、四圣谛——把心当作可训练的对象，早于现代心理学两千年。`The inner science of yoga and dhyāna: the mind as a trainable object, millennia early.*`

**语言特色 Linguistic Character：**
- **天城体（Devanagari）**：字母即音节（abugida），音形结合；"字母是种子（bīja）"。`Devanagari is an abugida — each glyph is a syllable; letters are seeds (bīja).*`
- **沙达律 Sandhi**：词间连音如水汇流，句是流动的整体。`Sandhi: sounds flow together across word boundaries; the sentence is one stream.*`
- **复合词（samāsa）**可造出"世界级长词"，一部字典装进一个词。`Compounding (samāsa) can build telescoping super-words.*`
- **语法近于数学**：波你尼《八章书》被比作最早的生成文法。`Pāṇini's Aṣṭādhyāyī: often called the first generative grammar.*`
- **种子音**：ॐ（oṃ）、śāntiḥ（寂静）、hṛdaya（心）——每个都是微型冥想。`Seed-syllables: oṃ, śāntiḥ, hṛdaya — each is a mini-meditation.*`

**制作要点 Production Notes：**
- 字体：Noto Serif/Sans Devanagari；连字（conjuncts）必须经 HarfBuzz 级渲染验证。*Noto Serif/Sans Devanagari; conjunct shaping must be verified at HarfBuzz level.*
- 颜色：姜黄、朱砂、莲花金；曼陀罗元素作底。*Turmeric, cinnabar, lotus-gold; mandala motifs.*
- 音乐：维纳琴 vīṇā、颂钵、吠陀唱诵 Vedic chanting。*Vīṇā, singing bowls, Vedic chanting.*
- 发音路线（见 §6.2）：真人学者/唱诵者优先 → Indic TTS → 兜底为天城体字幕 + 罗马化朗读。*Voice path: scholars/reciters first → Indic TTS → fallback Devanagari subtitles + romanized reading.*
- 口吻：庄重而宁静；快则失其咒，慢则得其根。*Solemn and still; speed loses the mantra, slowness finds the root.*

**常用试读句 Try-lines：**
- ॐ शान्तिः शान्तिः शान्तिः (oṃ śāntiḥ śāntiḥ śāntiḥ)
- यदा हि नेन्द्रियार्थेषु न कर्मस्वनुषज्जते । सर्वसंकल्पसंन्यासी योगारूढस्तदोच्यते ॥（《薄伽梵歌》6.4）
- प्रकृति (prakṛti，自然/本性)——一个好词汇题：一处自然、两重文明。

---

#### Latina la —— 不朽的铭刻 *The Eternal Inscription*

**文明核心味 Civilizational DNA：**
- **罗马法与法治秩序**：契约、所有权、公法私法之辨；拉丁术语至今是法学的母语。`Roman law and rule-of-law order: contract, property, public vs private — Latin is still the mother tongue of jurisprudence.*`
- **修辞与公民共和**：西塞罗的演说是武器；公民争辩即政体。`Ciceronian oratory as civic weapon; debate is government.*`
- **斯多葛不动心**：Seneca、Marcus Aurelius——把命运当训练，把当下当全部。`Stoic apatheia: fate as training, this moment as everything.*`
- **永续的帝国记忆**：两千年欧洲知识界的 lingua franca；"ad astra per aspera"。`Two millennia as Europe's lingua franca; the imperial memory of permanence.*`

**语言特色 Linguistic Character：**
- **屈折完备，词序自由**：名词格、动词式把关系刻进词形，语序服务于修辞。`Rich inflection frees word order; case and mood carry the grammar, word order serves rhetoric.*`
- **格言密度极高**：carpe diem、memento mori、amor fati、veritas——一句即一国。`Maxim density is extreme: one line is a whole nation.*`
- **长短音节**（不来世尔格与六音步）：诗有可听的建筑。`Quantity (long/short syllables) and hexameter: poetry with audible architecture.*`
- **古典发音是可重构的**：Caesar 读作 Kaisar，"凯撒"才是真罗马音。`Classical pronunciation is reconstructable: Caesar = Kaisar — that is the true Roman sound.*`

**制作要点 Production Notes：**
- 字体：Cinzel / EB Garamond / Trajan；碑刻石感。*Cinzel / EB Garamond / Trajan; inscription-stone feel.*
- 颜色：石灰岩白与暗铜；军团红旗为点。*Limestone white and dark bronze; a fleck of legion red.*
- 音乐：管风琴、格里高利平咏、铜管号角。*Organ, Gregorian chant, brass fanfare.*
- 口吻：如凿如刻，一音一石；格言不解释，只说一遍。*Carved, lapidary; maxims are not explained, only uttered.*
- 发音：古典重构发音优先（长短音要明显）；espeak-ng `la` 兜底。*Reconstructed Classical pronunciation first; espeak-ng `la` as fallback.*

**常用试读句 Try-lines：**
- Carpe diem, quam minimum credula postero.（Horatius, *Carmina* 1.11）
- Memento mori.（传统格言，墓刻传统）
- Aqua maris, luna lucet super omnia.（*创作示范，须标注"自制拉丁句"——模型句不可冒充古典原文；正式语料将走审校*）

---

#### Deutsch de —— 思想的拱顶 *The Vault of Thought*

**文明核心味 Civilizational DNA：**
- **德意志观念论**：康德、黑格尔、叔本华——哲学以体系立世，"思想经得起施工"。`German idealism: philosophy as system; thought must withstand construction.*`
- **宗教改革与良心**：路德把《圣经》译成德语，个人与上帝直接对话。`The Reformation: Luther's Bible puts the individual face-to-face with God.*`
- **秩序与纪律 Ordnung**：工作伦理、逻辑的严格；守时与整洁是美德。`Order and discipline: punctuality, rigor, exactness as virtues.*`
- **Bildung（修养）传统与森林情结**：漫游（Wandern）、森林（Wald）与灵魂的私密对话——"Waldeinsamkeit"。`Bildung and the forest: wandering and woods as private dialogue of the soul.*`

**语言特色 Linguistic Character：**
- **复合词扣件机**：Weltanschauung（世界观）、Zeitgeist（时代精神）、Sehnsucht（深切的向往）——一个词是一门哲学。`Word-compounding as worldview: Weltanschauung, Zeitgeist, Sehnsucht — one word, one philosophy.*`
- **动词框定全句（Verbklammer）**：主句动词把整个思想"扣"在句尾，像拱顶闭合。`The verb bracket: the main verb closes the sentence like a vault keystone.*`
- **名词性极强**：思想的实体化，万事皆可名词化。`Heavy nominalization: everything can become a noun — thoughts as substance.*`
- **大小写/屈折/框式结构**：读德语像解读一座精密的时钟。`Capitalization, morphology, bracketing: reading German is reading a precision clock.*`

**制作要点 Production Notes：**
- 字体：衬线正文 + 现代怪异体（grotesk）标题；历史文本可植 Fraktur 点缀。*Serif body + grotesk display; Fraktur accent for historical pieces.*
- 颜色：板岩灰、冷钢蓝，一块暖木色。*Slate gray, cold steel blue, a panel of warm wood.*
- 音乐：Bach、Schubert 之 Lied、Brahms；长笛与低音。*Bach, Schubert Lieder, Brahms; flute and bass.*
- 口吻：精确到可施工，诗意藏在句法深处。*Precise enough to build; the poetry hides in syntax.*

**常用试读句 Try-lines：**
- »Wo aber Gefahr ist, wächst das Rettende auch.«（Friedrich Hölderlin, *Patmos*）
- »Alles Vergängliche ist nur ein Gleichnis.«（Goethe, *Faust II*）
- »Der Herbst ist ein zweiter Frühling, wo jedes Blatt eine Blume ist.«（Albert Camus 法语转述的德语谚语化——须标注出处属性；常用祝词句）

---

#### Svenska sv —— 北境的澄澈 *Northern Clarity*

**文明核心味 Civilizational DNA：**
- **与自然的亲密**：森林、湖泊、群岛是国民的客厅；allemansrätten（自然拥抱权）许人人入林采果。`Intimacy with nature: forest, lake, archipelago are the national living room; allemansrätten grants everyone access to the wild.*`
- **lagom——适度之道**："不多不少，恰如其分"，一套国民的伦理与美学。`Lagom: "just right, not too much" — national ethics and aesthetics.*`
- **高信任社会契约**：北欧福利与协商；语言谦和而免于暴力。`High-trust social contract; speech is civil and non-confrontational.*`
- **光明与暗夜**：冬日的漫漫长夜让人懂光，夏夜的午阳让人懂生。`Amid northern darkness one learns light; amid midnight sun one learns life.*`
- **社会性茶歇 fika**：咖啡与肉桂卷之间的平等交谈。`Fika: coffee, cinnamon buns, and egalitarian talk.*`

**语言特色 Linguistic Character：**
- **北日耳曼的澄澈**：紧凑的构词与浮音（melodiös），angänser 温和。`North Germanic clarity; tonal melodies; soft, civil cadence.*`
- **专有词汇的智慧**：lagom、fika、längtan（思念/渴想）、hemlängtan（乡愁——"家之渴"）。`Untranslatable jewels: lagom, fika, längtan, hemlängtan.*`
- **与英语同宗不同貌**：vatten/water、tid/time——看得见的亲缘。`Sibling of English with a different face: vatten/water, tid/time — visible kinship.*`
- **极简句法 + 表面礼貌**：直接但温文，疑问与命令都裹着礼貌。`Minimal syntax with surface politeness; requests wrapped in courtesy.*`

**制作要点 Production Notes：**
- 字体：人文衬线 + 简洁无衬线；北欧极简排版。*Humanist serif + clean sans; Nordic minimal layout.*
- 颜色：湖蓝、桦木白、苔绿；一刻极夜蓝。*Lake blue, birch white, moss green; a moment of deep-night blue.*
- 音乐：瑞典民谣、管风琴、海岸环境音（海鸥与浪）。*Swedish folk, organ, coastal ambience (gulls and waves).*
- 口吻：谦和、朴素、心向自然与光；"lagom"本的克制就是表达力。*Humble, plain, turned toward nature and light; lagom restraint is eloquence.*
- 特别呼应：与 `living_heritage` 的 **Gotland** 案例天然咬合——瑞典语是北欧之门的钥匙。*Hinge to the Gotland case in living_heritage.*

**常用试读句 Try-lines：**
- »Ja, visst gör det ont när knoppar brister.«（Karin Boye, *Hur långt kan elden nå?*）
- »Det enda som frälsar oss är att våga leva.«（口传/谚语化——须标注属性）（常用句仍须核源）
- »Stillheten är vårt enda hem.«（*创作示范*——自制句，须标注，正式语料走审校）

---

### 3.3 织的线索 Weaving Threads —— 语言间的互文

这些「织线」专门喂给 Format E（词源解密）和 Format B（深读）。

- **印欧大系（欧洲五语 + 梵语同源）**：*aqua/mare/cor/⟨心⟩* 一族——梵语 huādi（親）de、拉丁 mare、法 mer、德 Meer、英 mere、瑞典 hav/märke；以及 *sea/mare/Mer/hav* 这条"海"之词脉。`The Indo-European web: one root, eight dialects of the same story.`*
- **汉字圈**：中 ↔ 日——日月山水草木共享，词是文明的共同遗产（观字知史）。`Sinosphere: shared characters are a shared archive.*
- **对照最出戏的"镜象对" Mirror Pairs：**
  - 中文（意合、留白）↔ 拉丁（屈折、格言）——"一首诗 vs 一行碑"
  - 日语（暧昧的精确）↔ 法语（细腻的优雅）——"不说的 vs 会说的"
  - 梵语（圣言、复合词）↔ 德语（体系、复合词）——"神谕的 vs 工程的世界观"
  - 瑞典语（适度）↔ 英语（直接）——"lagom vs plain-spoken"

- **扩编织线（新增 24 语）**：复兴三姐妹 he·ga·mi（怎么把语言说回来）／文字的三种命运 ar·fa·tr（保留-改造-决裂）／同根两端 sa→hi／词根共享 ar·he（s-l-m）／借词回旋镖 es↔nah·gn→en／包罗性 we qu·tpi·id／证据性情态 qu／声调群 zh·th·vi·yo·yua／乌拉尔之镜 fi×sv／海洋贸易带 ar·sw·id·mi·tpi。全集见扩展蓝图 §4。

> **制作忠告**：身份卡决定"谁在说"，织线决定"他们说什么"。一期内容至少带一条织线，否则只是"八行译文"。

---

## 4. 主题矩阵 Theme Matrix

**五大主题，五大「织语」子系列。** 每个主题先定 12 个"心象"，逐期灌溉成片。主题之间有意识交叉（例：一棵树既是"自然"也是"文明的隐喻"）。

*Five themes, five sub-series. Each theme starts with ~12 "images of thought".*

| # | 主题 Theme | 中文名 | 英文名 | 心象种子 *Image seeds* | 代表声源 Voice |
|---|---|---|---|---|---|
| 1 | 大自然 | 织语·自然 | *Nature in Every Tongue* | 春、月、海、山、树、雪、光、星空、风、溪、节气、雨 | 田园与山海的影像 |
| 2 | 生命觉悟 | 织语·觉 | *Awakened Words* | 无常、当下、生死、觉知、放下、自由、静、初心、精进、回归 | 面容与光的特写 |
| 3 | 文化文明 | 织语·文明 | *Civilizations Whisper* | 语言起源、文字源流、经典、神话对比、哲学、桥梁 | 手写与古籍的文献影像 |
| 4 | 生活感悟 | 织语·渐悟 | *Notes on Living* | 时间、幸福、友谊、知足、热爱、孤独、勇气、简单 | 日常物的柔焦 |
| 5 | 日常生活 | 织语·日常 | *Everyday Songs* | 清晨、茶、散步、家常、相逢、劳作、一餐、睡眠、旅途 | 生活流与环境的实录 |

### 4.1 主题 × 子题展开（首期种子清单）

- **大自然 Nature**：《月照千川》（月）、《海之名词学》（海）、《春的八种说法》（春）、《一棵树的年轮》（树）、《雪落无声》（雪）、《光的迟到》（光）、《星图》（星空）、《风的踪迹》（风）、《山在那里》（山）、《流水不争先》（溪/水）、《节气之歌》（节气）、《一场雨的时间》（雨）。
- **生命觉悟 Awakening**：《无常的语法》（无常）、《当下即太》——正名（当下）、《生死的两行》（生死）、《觉》（觉知）、《放下》（放下）、《自由之词》（自由）、《静默三行》（静）、《初心》（初心）、《精进》（精进）、《归》（回归）、《向内》（内观）、《此身此世》（此刻）。
- **文化文明 Civilization**：《书同文》（文字）、《语言是什么时候出生的》（起源）、《神话对坐》（神话）、《经典的一句话》（经典）、《哲学的国界》（哲学）、《桥梁与驿道》（通道）、《冠冕与印章》（象征）、《文明的剪影》（物证）、《圣书与法典》（神圣文本）、《手迹》（手稿）、《地图上的语言》（语言地图）、《成语博物馆》（习语）。
- **生活感悟 Insights**：《时间之词》（时间）、《幸福的定义》（幸福）、《友谊五种》（友谊）、《知足常乐》（知足）、《热爱可抵漫长》（热爱）、《孤独的尊严》（孤独）、《勇气》（勇气）、《简单》（简单）、《选择与遗憾》（选择）、《中年之诗》（中年）、《老去与童年》（老与童）、《意义的重量》（意义）。
- **日常生活 Daily**：《清晨八国》（清晨）、《茶事》（茶）、《散步》（散步）、《家常味》（家常）、《相逢一刻》（相逢）、《劳作与休息》（劳作）、《一餐的光阴》（一餐）、《晚安八语》（睡眠）、《在旅途》（旅途）、《一场雨中的伞》（雨）、《fika与茶》（茶歇对照）、《灯下的书》（阅读）。

### 4.2 选题三问（每期必答）Selection Triad

1. **这个心象是否"一句即见全豹"？**（可浓缩成一个画面、一行大字、一条语音）
2. **八语对它是否"各有其说"且"殊途同归"？**（若八语只译得一样，则换题）
3. **能否带一条"织线"（词源/语法/文化互文）？**（见 §3.3）

---

## 5. 选材与语料库 Corpus & Sourcing

### 5.1 素材来源分级（按可靠性三档）

| 档 | 说明 | 示例 |
|---|---|---|
| **A 公版经典 Public-domain classics** | 版权过期，可自由引用、翻译 | 《道德经》《论语》、唐诗宋词、Shakespeare、Montaigne、Pascal、芭蕉、紫式部、Horace、Vergil、Seneca、Goethe、Rilke、Hölderlin、Karin Boye、Selma Lagerlöf、Tranströmer（其 2015 年后版权状态需逐本核验） |
| **B 原创自制 Original compositions** | 自己创作原文/译文，零版权风险 | 试句、现代译文、揭示"不可译"的创作对照 |
| **C 现代/受版权保护（谨慎）** | 只允许短引（fair use / 注明出处），绝不拿来当全文 | 现代诗人的名句、现代散文（阿斯特丽德·林格伦等）——只"引用一行 + 大段背景音与影像"，并明示来源 |

> **铁律**：A 类必须能够定位到"版本/篇目/卷章"；B 类必须在语料 JSON 中标注 `original: true`；C 类一律标注 `copyright:"short-quote"`，且不建设完整译文在公开渠道。*Rule: A must cite edition/work/chapter; B marked original; C limited to short quotes with attribution.*

### 5.2 每语基准语料池（A 类优先起步）

- **zh**：《道德经》《论语》《庄子》《诗经》、唐诗（李白/杜甫/王维/苏轼/张九龄）、宋词。
- **en**：Shakespeare 十四行诗、Emerson《自然》、Thoreau《瓦尔登湖》、Whitman《草叶集》、Frost、Dickinson。
- **fr**：Montaigne《随笔集》、La Fontaine《寓言诗》、Pascal《思想录》、Boileau《诗艺》、Hugo 诗、Baudelaire《恶之花》（公版）。
- **ja**：芭蕉俳句、一茶俳句、万葉集、古今和歌集、『源氏物語』。
- **sa**：Ṛgveda、Bhagavad Gītā、Yogasūtra、Dhammapada（法句经，巴利为主，梵文对应可注）、Upaniṣad 选篇。
- **la**：Cicero、Seneca、Vergil《埃涅阿斯纪》、Horace《歌集/书简》、Ovid《变形记》。
- **de**：Goethe《浮士德》、Hölderlin《帕特莫斯》、Rilke《杜伊诺哀歌》《秋》、Novalis、Nietzsche《查拉图斯特拉如是说》。
- **sv**：Karin Boye、Tomas Tranströmer、Selma Lagerlöf、Viktor Rydberg（《Tomten》）、Belle Wulff 等民谣/圣咏传统（逐本核版权）。

### 5.3 平行语料数据结构（JSON 三行对照，详见附录 A）

每个心象 = 一个 JSON 对象：`source`（原文+出处+性质）+ `translations[8]`（译文+字面直译+注）+ `linguistic_notes`（织线）+ `visual/audio`（制作参数）+ `status`（生命周期）。全部输出（视频/卡图/网站）都由它渲染。

### 5.4 词汇级语料：Glossary 术语表（见附录 D）

"水/月/心/时间/海/自由/茶/寂静/树/风"等核心概念，预先把八语对应词与直译建表，保证跨期一致。

---

## 6. 多模态总设计 Multimodal Master Design

**六重模态粽子结构**：文字(字形) × 声音(语音) × 影像(画面) × 字幕(信息层) × 时空(词源/地图/年代) × 交互(学习/切换)。每一期不必全上，但要明确"本期主打哪几层"。

*Six modality layers: text/script × sound/voice × visuals × captions × time/space (etymology, maps, eras) × interaction. Not every episode uses all six — but every episode states its layers.*

### 6.1 文字视觉层 Typography & Script

- **字体栈 Fonts**（免费、渲染可靠）：
  - 中文：Noto Serif CJK SC / Noto Sans CJK SC；书法感用楷体类（STKaiti 或开源 LXGW WenKai）。
  - 日文：Noto Serif JP / Noto Sans JP（竖排时用排版引擎支持 tate-chu-yoko）。
  - 天城体：Noto Serif/Sans Devanagari（必须经 HarfBuzz 验证连字：क्र स्त क्ष 等）。
  - 拉丁/罗曼/日耳曼（en/fr/la/de/sv）：EB Garamond（大段落）、Cinzel（拉丁碑刻感）、UnifrakturMaguntia（德语 Fraktur 点缀用）。
  - IPA 与音标：Noto Sans 系或系统字体即可。
- **文字动画原则**：叠(Stack) 时——原语大字为主体，逐行亮起并伴随读音；译语小字为辅；注疏以"脚注小纸条"出现。**永远保持原语的"字形主权"**：梵文亮天城、日文可以用竖排、拉丁保留 macron、德语保留 ß/äöü。
- **渲染技术**：字幕/卡图用 `libass + ffmpeg`（支持套路 claim；Devanagari shaping 用 HarfBuzz）或直接 `Pillow + uharfbuzz` 光栅化为无损图，避开编辑器字形渲染缺陷。
- **规则**：每屏文本 ≤ 90 字（含译注）；母语列永远最大字号；同屏颜色≤3（+1 安全色）。

### 6.2 声音层 Audio

- **语音矩阵 Voice Matrix**（先 TTS 起步，逐步补真人）：
  - zh / en / fr / ja / de / sv：**edge-tts** 高质量神经音色（如 zh-CN-Xiaoxiao；en-US-Jenny/Christopher；fr-FR-Denise/Remi；ja-JP-Nanami/Keita；de-DE-Katja/Conrad；sv-SE-Sofie/Mattias）。多音色轮换，让“同一语种也有表情”。
  - sa：**优先真人学者/唱诵者**（Vedic chanting 视频素材库可临时替）；其次 Indic TTS（Asha/AI4Bharat 系若可用）；兜底——天城体大字字幕 + 罗马化（IAST）朗读，并注明"此为工具音，梵读以真为尚"。
  - la：优先古典重构发音录音（长短音、c/k 读法）；兜底 `espeak-ng -v la`（质量一般，适短句）。
  - 全 TTS 输出要 **拼接调速**（±0–15%）以匹配画面呼吸；并用 pydub 统一响度（-16 LUFS）。
- **音乐身份 Music Identity**：沿用 §3.2 每语"音乐卡"；每期一主一辅，切换语言时音乐随之换色。初版可全部使用 **公有领域音乐**（古典录音年代久者或 CC0 素材）。
- **环境音 Ambient**：自然系（水声/鸟唱/风声/虫鸣）、日常系（茶沸/脚步/雨伞）——一句一景，音景即地点。
- **念诵 Chanting/读法规范**：每语给出"朗读谱"（重音、停连、浊化/联诵要点），存入 `04_audio/readings/`。

### 6.3 影像层 Visuals

- **素材三级**：① 免费优质素材库（Pexels/Pixabay/Unsplash，务必记录作者与许可）；② 自摄（旅行/日常顺手拍，统一横竖比）；③ AI 生成（SD/SDXL/FLUX + 每主题固定提示词模板）。
- **同题跨语图像一致性**：一个心象 = 一个画面基底（如"同一轮月、同一片水"），八语只是字幕/旁白的切换——**避免**八语各配八幅不同画面而失去"同镜"的张力。
- **AI 生图提示词模板**（存 `05_visual/prompts/`）：`[scene] + 电影感打光 + [主题色板] + 高反差低饱和 + 无文字`，并规定"生成图像不得含真实文字/商标/人脸泛化"。
- **生视频（可选进阶）**：Kling / Runway / Veo 等把静帧做成 3–6s 微动；先手工剪辑求稳。

### 6.4 字幕与信息层 Captions & Information

- **三轨字幕策略**（每期三选二）：
  1. **Hero 轨**：原语大字（当前在读的语言）——字形主权。
  2. **Gloss 轨**：中/英双解（面向全球观众，默认中—英二选）。
  3. **Note 轨**：织线注疏（词源/文化点），用"侧栏纸条"而非长文。
- **字体嵌入**：发布字幕必须内嵌字体或转语音图像；srt/ass 一律 UTF-8，特殊字符（梵文/日文竖排/长音符）经试渲染 QA。
- **无障碍**：永远有纯字幕版 + 语音版；关键注疏同时以文字出现（照顾静音观者）。

### 6.5 时空层 Time & Space（词源 · 地图 · 年代）

- **词源树动画 Etymology tree**：一个词跨语同根（印欧词族）/异根同义（汉字词族），用"根-枝-叶"或"河流支流"隐喻生长。
- **语言地图**：一个心象的词，在世界地图上点出分布与传播路线（梵语 → 印欧西行，汉字 → 东亚传播，瑞典语 ↔ 北欧语族）。
- **文明年代尺**：诗的诞生年代、作者的世纪、两个文明的"同时刻"（例：某唐诗与某拉丁诗同一年代对坐）。
- 素材：公版地图底图 + 手工绘制（避免版权）。

### 6.6 交互层 Interaction（网站与学习模式，Phase 4）

- **叠字阅读器**：网页上下键逐语切换竖排/横排；点击单词看 IPA + 直译 + 例句。
- **跟读模式**：语音逐字高亮，用户可跟读录音对比（语言学习侧）。
- **卡片翻面**：图文卡两面（正面原语大字 / 背面字面直译 + 注疏）。
- 聚合在 `gruel_cooking/docs`（GitHub Pages）作为视频索引 + 交互剧场。

---

## 7. 格式模板 Format Templates

**六种模板；现阶段以文字为主（网页、词卡、平行语料先行），视频统一 16:9 宽屏（供 YouTube 嵌入，制作方案另列规划）**，其余按路线图逐步解锁。每期选一种"主格式"，可附带衍生。

*Six templates; the current phase is text-first (web, word-cards, corpus), video output will be 16:9 widescreen for YouTube embedding (plan TBD). Each episode picks one "main format", optionally with derivatives.*

### 7.1 A 叠式短视频「一镜八澜」Stack Short —— 首推 Launch Format

- **时长**：30–60s（宽屏 16:9，适配 YouTube 嵌入）。
- **结构（分镜 beats）**：
  1. `0–3s` 钩子：一帧留白 + 中文原句大字（或英文）定格，环境音起。
  2. `3–45s` 逐语登场：每语约 4–6s，语音先、字幕随；语言切换时背景音乐与色带同步换"身份"。
  3. `45–60s` 合璧：八语同屏（叠成"语言格里"），一句注疏（织线）浮出；落款系列名 + 下期预告。
- **每条固定元素**：母语英雄字 / 语言身份色 / 一个织线注疏 / 片名与台标。
- **衍生**：同一心象切 1:1 封面 + 9:16 首帧。
- **制作清单**：见 §8 流水线，一条约 2–4 人日（含翻译与 QA）。

### 7.2 B 织式长视频「对读之辩」Weave Long —— 深读 Format

- **时长**：3–6min（横屏 16:9）。
- **结构**：开场心象（30s）→ 原文深读（1min，原文大字+朗读+逐句解说）→ 逐语对读（2–3min，每语 20–30s：语音+字形+词源/语法/文明味滴定）→ 合诵与总结（30s，八语合声剪辑）。
- **特色桥段**：「不可译实验室」——用 3 句话解释为什么某个词"翻不进去"（侘寂、lagom、Sehnsucht、śāntiḥ、memento mori……）。
- **来源**：由 2–3 条 A 型短视频的内容升级而来（一处语料，多条输出）。

### 7.3 C 每日一词「一词万境」Word of the Day Card —— 图文卡 Format

- **形态**：9:16 竖版图文卡（适合小红书/B站动态/公众号），每期 1 个概念词。
- **卡面结构**（自上而下）：大字原词（该语文字形）→ IPA 读音 → 拉丁转写（若适用）→ 一词直译 + 中英注释 → 出自哪条句子/哪本书 → 一张对应影像（一致图形）→ 底部"织线"（该词八语对照小行）。
- **音轨（可选）**：15–30s 音频（真人/TTS 朗读 + 一段环境音）。
- **内容节奏**：可日更或周更；先期词库见附录 D。

### 7.4 D 多语对读「同题异想」Parallel Reading —— 学习 Format

- **形态**：竖屏/横屏，逐行滚动。同一首诗/一段话，8 语逐行并列显示，一行一朗读，石刊式排版。
- **用途**：语言学习者 + 普通观众感知"语感节奏"。可做成长系列（如《道德经》一课 × 八语）。
- **关键**：每行附 IPA/直译脚注，且"读一行停一拍"——声音给呼吸，呼吸给理解。

### 7.5 E 词源解密「语之谱系」Etymology —— 知识 Format

- **形态**：1–2min 横屏/竖屏均可；核心是"词源树动画"。
- **例题**：《海之氏谱》——sea/mare/mer/Meer/hav/समुद्र；《心相通》——heart/cœur/cor/Herz/hjärta/हृदय/心；《时间之词》——time/temps/Zeit/tid/tempus/kāla/时。
- **结构**：一个词的八语分身 → 追根（印欧原根 *ḱerd- 等/汉字源流/假名与借词）→ 落地（各自文明如何用它）→ 出片点题："同源而殊途，殊途而同归。"
- **素材**：公版词源词典（如 EtymOnline 摘注须注名）、文献核对。

### 7.6 F 轮诵「七语八澜 · 合唱」Choir —— 节气/节日 Format

- **形态**：60–90s，同一文本（或同一主题各语一首微诗）逐语轮诵，最后八语交织（交叉淡化）合一收束；画面同一影像连续。
- **适用**：节庆（除夕、中秋、圣诞、新年）、世纪名句、史诗片段。
- **关键**：轮诵节奏按"诗律"而非等分；合颂段用音量与声道分层（左右耳流动）。

---

## 8. 制作流水线 Production Pipeline

**一条流水线管全部模板**。每期在 `06_production/` 下建一个工作目录，八步走完即出片。

*One pipeline for all templates; each episode gets a working directory under `06_production/`.*

| 步 Step | 名称 | 输入 → 产物 | 工具 | 质量门 Gate |
|---|---|---|---|---|
| 0 | 选题 Idea | 主题种子 → 一期卡片（选题三问） | 语料库浏览 + §4.2 | 三问全过 |
| 1 | 文本 Text | 期卡片 → 平行语料 JSON（source + 8 译文 + 注） | 编辑器 + 语料 schema | schema 校验通过 |
| 2 | 译审 Review | JSON → 审校签名（per-lang） | §10 方法论 + 双人矩阵 | 回环校验 ≤5% 漂移，母语确认 |
| 3 | 语音 Voice | JSON → 每语音频轨 + 朗读谱 | edge-tts / 真人 / espeak | 断句、长音、连读 QA |
| 4 | 视觉 Visual | 提示词/素材库 → 画面基底 + 卡图 | SD/FLUX + 素材库 | 无文字/无商标/许可记录 |
| 5 | 合成 Compose | 音频轨+画面+字幕 → 母带 | 剪映 / CapCut / DaVinci / AE | 韵律与画面对齐，字幕可读 |
| 6 | 质检 QA | 母带 → 待发布包 | §11 | 全项清单通过 |
| 7 | 发布 Publish | 待发布包 → 多平台 + 网站 | 各平台 + docs/ 脚本 | 标题/封面/标签齐 |

### 8.1 角色分工 Role Split（单人多角色亦可）

- 策划 Curator：选题、心象、织线、文明味把关。
- 译者 Translators：8 语译文起草；es 级审校由专项审校人完成。
- 审校 Reviewers：语言对（zh/en 母语；fr/ja/de/sv 母语或近母语；sa/la 古典语专家或受训者）。
- 声音 Voice Lead：录音/ TTS/SARS、朗读谱、音乐。
- 视觉 Visual Lead：素材、提示词、色板、封面。
- 剪辑 Edit Lead：合成、节奏、字幕。
- QA：逐项过清单。
- 运营 Ops：标题、简介、标签、日历、互动回复。

### 8.2 每期交付物 Deliverables per Episode

```
episode/slug/
├── idea.md            # 选题三问 + 心象描述
├── corpus.json        # 平行语料（正本）
├── review.md          # 审校记录（每语确认人 + 回环差异）
├── audio/             # 8 条朗读轨 + 音乐 + 环境音 + mix.wav
├── visual/            # 画面基底、卡图、封面、提示词记录
├── timeline.md        # 分镜表（Beat × 时序 × 字幕）
├── render/            # 母带 mp4 + 字幕文件（ass/srt）
└── publish/           # 各平台标题/简介/标签 + 缩略图
```

---

## 9. 工具栈 Toolchain

| 用途 Use | 首选 Primary | 备选/兜底 Fallback | 说明 |
|---|---|---|---|
| 文本语料 | JSON + Markdown | SQLITE（后期） | 正本只有 JSON，Markdown 是视图 |
| 语音 TTS | edge-tts | Coqui/XTTS、espeak-ng | sa→Indic TTS/真人；la→espeak-ng/真人 |
| 音频处理 | pydub + ffmpeg | Audacity | 响度 -16 LUFS、淡入淡出 |
| 图像 | FLUX/SDXL + Pexels 等 | 自摄、MJ | 记录许可；提示词模板化 |
| 生视频（可选） | Kling / Runway / Veo | — | 3–6s 微动；先用静帧求稳 |
| 视频合成 | 剪映 / CapCut | DaVinci Resolve / After Effects | 快片走剪映；大片走 AE |
| 自动化渲染 | ffmpeg + moviepy + Pillow | uharfbuzz+fonttools | 卡图/字幕/批量音频 |
| 字幕 | ass/srt（UTF-8） | libass | 天城体连字、竖排日文须 char 级 QA |
| 封面 | 模板 + 卡图 | 手动微调 | 统一版式 |
| 发布网页 | gruel_cooking/docs（GitHub Pages） | — | 视频索引 + 叠字阅读器 |

> **脚本仓库**：`08_tools/` 放可复用脚本（批量 TTS、卡图生成、词源树数据、字幕生成、响度归一）。所有脚本只读正本语料 JSON。

---

## 10. 翻译方法论 Translation Doctrine

翻译是这门工程的**一半本体**。要诀：让每种语言"以它自己的方式忠于原意"，而不是八份同一语的直译。

*Translation is half the project. Let each language be faithful *in its own way* — not eight literal versions of one voice.*

### 10.1 直译↔意译梯度 Literal↔Free Gradient

对同一句每组译文，标注其"忠诚坐标"：
- **L 直译 Literal**：逐词贴近，用于"字面直译 + 注"轨道（帮助观众看语法）。
- **G 通译 General**：自然流畅的目标语读法，用于 Hero 轨与正文。
- **P 诗译 Poetical / 复刻意象**：保留意象与节奏（如俳句的 5-7-5、格言的对仗），允许增词减字，但**必须注释"为诗而作"**。

> 例（「海上生明月，天涯共此时」张九龄）：G 通译为 *Over the sea a bright moon rises; we two share this moment across the world.*；L 直译为 *Sea(surface) up-bring bright moon; far-horizon together this-hour.*——两条轨道并存，观众同时看见"意思"与"语法"，这就是叠与织。

### 10.2 工作流 Workflow

1. **起草 Draft**：LLM 首译（提示词含：语种身份 → 忠实方向 → 韵律要求 → 防幻觉）；或人类译者。
2. **回环校验 Round-trip**：把译文再译回中文/英文，比对漂移≤5%（语义五要素：主体、事件、时间、趋向、情感缺一即返工）。
3. **母语审校 Native review**：一致性、自然度、文化得当（法语 liaisons、德语名词性、瑞典语情绪温度等）。
4. **古典语专审**：sa/la 由受训者逐词核格/式/数/性/时（可辅以工具：Perseus 词形、词源词典）；无把握者宁缺毋滥，退回"词汇+注"而非整句译文。
5. **注疏 Gloss**：每条译文附 `literal`（字面）+ `note`（文化注）。

### 10.3 不可译之美的处理 Handling the Untranslatable

- 保留原词 + 术语表：侘寂、lagom、śāntiḥ、memento mori、Sehnsucht——以"原词即阐释"对待。
- 加"译注纸条"：Why three words are needed to explain one.
- 编辑原则：**宁失一词，不失一义；宁留注释，不弃原文。** *Rather lose a word than a meaning; rather keep a gloss than drop the original.*

### 10.4 名词与正字规范 Orthography

- 中文：简化字为正体，必要时附繁体/拼音。
- 日文：现代假名 + 汉字；标读音（furigana）供非日语观众。
- 梵文：天城体为正体，括注 IAST 罗马转写（शान्तिः = śāntiḥ）。
- 拉丁：保留 macron（ā ē ī ō ū）与古典拼写（v 与 u 依规矩）。
- 德/瑞：保留 äöüß / åäö 完整字符。
- 全网统一正字表（存 `03_translation/glossary.md`）。

---

## 11. 质量控制 QA

**每次发布前，走通下面整张清单（任一失败即返工）。** *Every release clears this whole checklist or it ships back.*

### 11.1 字形与排版 Script & Layout
- [ ] 天城体连字渲染正确（क्र/स्त/क्ष/र्ग 等字形不被拆坏）；字体已内嵌。
- [ ] 日文竖排时假名/标点/长音（ー）方向正确；『』「」不翻边。
- [ ] 拉丁 macron 清晰可辨；德语 ß 与 ß 大小写、瑞典 åäö 不缺失。
- [ ] 每屏 ≤ 90 字；Hero 与原语主字 ≥ 背景对比（WCAG AA 优先）。
- [ ] 中文标点（「」、·）与西文标点（，. '）不混排出错。

### 11.2 语音与音乐 Audio
- [ ] 每语音频与字幕逐句对齐（允许 ±150ms）。
- [ ] 朗读谱执行：重音/停连/TTS 的断句位置人工复核一次。
- [ ] sa/la 兜底音已做音质补偿（降噪/减速）；长音节奏近诗律。
- [ ] 响度归一 -16 LUFS；人声 -3dB 于音乐；无爆音/齿音问题。

### 11.3 内容与版权 Content & Rights
- [ ] 引文有版本/篇目可查；版权档位写清（A/B/C）。
- [ ] 影像每帧许可记录齐全（素材作者/许可；AI 图无真人脸、无商标文字）。
- [ ] 译注无"编造出处"——口传/谚语/误归都显式标注"流传属性待核源"。
- [ ] 术语表一致（附录 D）——同一概念全期同词同译。

### 11.4 平台与体验 Platform UX
- [ ] 封面吸引且不误导（标题=内容）；缩略图无多余文字。
- [ ] 静音可读（字幕完整）；语音可懂（字幕不抢音）。
- [ ] 竖屏版无裁切（16:9 与 9:16 各审一次）。

---

## 12. 发布与增长 Publish & Growth

### 12.1 平台矩阵 Platform Matrix

| 平台 | 形态 | 用途 | 频率 |
|---|---|---|---|
| 抖音 / TikTok / Instagram Reels / YouTube Shorts | 竖屏 A/F 型 | 触达 + 完播率 | 周更 |
| Bilibili | 竖屏+横屏 | 中长 B/C/D 型 | 两周更 |
| 小红书 | 图文卡 C 型 | 收藏 + 讨论 | 日更/隔日 |
| YouTube 长频道 | 横屏 B/E 型 | 深度 + 播放列表 | 两周更 |
| GitHub Pages（docs/） | 网站索引 + 叠字阅读器 | 沉淀 + 学习 | 随更新 |

### 12.2 系列命名 Series Naming

- 母题：**Language Stacking · 语言叠织**（或保留英文原名贯名）。
- 五大子系列：织语·自然 / 织语·觉 / 织语·文明 / 织语·渐悟 / 织语·日常。
- 栏目：一词万境（C）、语之谱系（E）、七语八澜 · 轮诵（F）。
- 标题模板：`[心象]｜8 种语言说同一个意思`（短视频）；`古今诗栖处 · [作品] 八语对读`（长视频）；`一词万境#12 · lagom（适度）`（卡）。

### 12.3 每期发布包 Publish Kit

标题（≤25字）+ 副题 + 简介（含八语列表与织线一句）+ 标签集（主题/语种/栏目/平台）+ 封面 + 时间标签 + 系列口令（如 #语言叠织 #一镜八澜）。

### 12.4 内容日历 Content Calendar

按"月主题制"：每月一个主题（自然 → 觉 → 文明 → 渐悟 → 日常 轮转），每周一条主片 + 2–3 张卡。重大节庆（中秋/月圆=自然月之光，圣诞/新年=轮诵 F 型）固定卡位。

### 12.5 反馈回路 Feedback Loop

每篇评论区收集：① 观众最想看的语言组合；② 求助最多的"不可译词"；③ 长视频的跳看位置（复盘字幕/节奏）。全部回流选题库（`02_corpus/backlog.md`）。

---

## 13. 路线图 Roadmap

| 阶段 Phase | 时间 Time | 目标 Goal | 产物 Deliverables |
|---|---|---|---|
| **P0 地基** | 第 1–2 周 | 设计包 + 语料 schema + 工具脚本 | 本 README / 8 张身份卡 / 主题五卡 / JSON schema / TTS 与素材验证 |
| **P1 试片** | 第 3–6 周 | 5 条 16:9 宽屏 Pilot 跑通全链 | A 型×3 + C 型×1 + E 型×1（见 §14） |
| **P2 全 8 语链路** | 第 1–2 月 | 全部 8 语含 sa/la 语音策略落地 | 首条 B 型长视频 + 例行周更 |
| **P3 系列化** | 季度 | 5 主题 × 8 条 = 40 条主线 + 卡 100+ | 主题合集播放列表 + GitHub Pages 剧场 |
| **P4 交互** | 半年+ | 叠字阅读器 + 跟读模式 | 学习模式 + 投稿/共同翻译社区 |

---

## 14. 首批制作清单 First Deliverables（P1 试片）

| # | 类型 | 题目 | 心象 | 为何先做 |
|---|---|---|---|---|
| P1 | A 叠式短视频 | 《一镜八澜 · 月》 | 张九龄「海上生明月，天涯共此时」 | 全 8 语齐发力、人心所向 |
| P2 | A 叠式短视频 | 《海之名词学》 | 一"海"：水之一体，八语之名（织线：印欧词族 + 汉字） | E 型词源前置，双格式复用 |
| P3 | C 每日一词 | 一词万境 #1 · lagom | 瑞典语"适度" | 预热瑞典语 + 加拉"不可译"话题 |
| P4 | F 轮诵 | 七语八澜 · 冬 | 冬之微诗/寒夜短句（自制原文，免责安全） | 时节即流量 |
| P5 | E 词源解密 | 语之谱系 · 心 | heart/cœur/cor/Herz/hjärta/हृदय/心 同源与殊途 | 教育感最强，收藏率高 |

**P1 验收口径**：5 条全部过 §11 全清单；发布 14 天后复盘（完播、收藏、评论词云），据反馈微调选题池。

---

## 15. 目录结构与命名规范 Directory & Naming

### 15.1 目录总览

```
Language Stacking-Linguistic Weaving/
├── README.md                    ← 本计划（正本，双语）
├── 00_session/                  # 会话/灵感速记、选题池 backlog
├── 01_core_design/              # 身份卡、主题卡、字体/色板/音乐库索引、版式指南
├── 02_corpus/                   # 平行语料（JSON 正本） + Markdown 视图，按主题分
│   ├── nature/ awakening/ civilization/ insights/ daily/
│   ├── backlog.md               # 选题池
│   └── glossary.md              # 概念×八语术语表（附录 D 的正本）
├── 03_translation/              # 翻译工作流、审校记录、正字表、风格指南
├── 04_audio/                    # 朗读谱、voice lists、TTS 配置、音乐库索引、录制
├── 05_visual/                   # 素材索引、提示词库、色板、封面模板
├── 06_production/               # 每期工作目录（§8.2）
├── 07_publish/                  # 标题/简介/标签库、封面、发布记录、内容日历
├── 08_tools/                    # 可复用脚本：TTS/卡图/字幕/词源树/响度
├── 09_docs_web/                 # GitHub Pages 材料：影片索引 + 叠字阅读器
├── 10_archive/                  # 废弃草稿、旧版本
├── languages/                   # 学习库子站知识单一来源（md prose + frontmatter + data/ JSON + glossary + docs/），见 §15.4
└── web/                         # 学习库子站生成器 build_learning.py + export_neo4j.py 导出器 + weave_query.py 读路径 + tests/ + run_tests.ps1
```

### 15.2 命名规范 Naming Conventions

- **期号**：`{series}-{number}`，如 `nat-001`（自然）、`awa-001`（觉）、`civ-001`（文明）、`ins-001`（渐悟）、`day-001`（日常）、`wd-012`（一词）。
- **文件**：`{series-号}_{slug}_{lang}.md`，lang 用 ISO（en 文件即英文；zh 即中文；双语主文件用 `dual`）。
- **语料 JSON**：`corpus/{series-号}_{slug}.json`；每语字段见附录 A。
- **成片**：`06_production/{series-号}_{slug}/render/{type}_{series-号}_{slug}.mp4`。
- **审校签名**：`review.md` 顶部表格逐语登记人/日期/结论，未签名语言不得发布。

### 15.3 协作约定 Contribution Rules

- 每期必答选题三问（§4.2）后入池。
- 修改正本语料一律走"译审矩阵"（起草→回环→母语→签名），**禁止直接改 JSON 而不留审校记录**。
- 所有 AI 生成内容在 `idea.md`/`corpus.json` 中标注"AI-assisted"，且最终句由人类定稿。
- 尊重 A/B/C 版权档位，绝不把"自制句"混入经典引用。

### 15.4 学习库子站 Learning Sub-site（基础学习层）

「各语种基础学习」是独立于「心象语料」的知识层：**学习库 → 语言 → 模块** 三级子站，内嵌于主站 `docs/language_stacking/`（导航「学习库」）。

- **知识单一来源** `languages/`（本领域仓库内，git 可编辑）：
  - `languages/README.md` — hub 双语散文 + frontmatter 语种注册表（`status: active|planned`）
  - `languages/{lang}/README.md` — 该语基础 + frontmatter 模块清单（`status: ready|planned`）
  - `languages/{lang}/*.md` — 各模块知识 prose（`<!-- zh --> / <!-- en -->` 标记，遵循 kb 语态约定）
  - `languages/data/{lang}/*.json` — 结构化数据（音图矩阵、词表、provenance）
- **生成器** `web/build_learning.py`（标准库 + `markdown` 包）渲染静止页 → `docs/language_stacking/learning/`（hub、ja/、模块页、**织网库 glossary/** + 共享 `learning.css`）。不硬编码、不在页面复制内容；页面壳层 chrome 与语言切换沿用主站 `ls-lang` 约定。
- **数据层**：`--db` 同步 sqlite 查询索引 `languages/data/learning.db`（语种注册 + 模块 + 音图 chart_cells（含拨音ん）+ 词表 vocab + **织网库 concepts/concept_terms/scripts/threads**）；`web/export_neo4j.py` 从索引导出阶段二跨语概念织网的 Cypher 导入脚本 `languages/data/neo4j_load.cypher`（幂等 MERGE + `CALL { } IN TRANSACTIONS` 作用域封装，不入 git），schema 与查询样例见 `languages/docs/neo4j_schema.md`；`web/weave_query.py` 提供「一词万境」无服务器读路径（list/concept/script/thread/sound）。节点权威 `languages/data/core_glossary.json`（附录 D 概念 × 八语术语表第一批校准，12 概念 × 8 语 + scripts + 织线，词位标 review pending）。数据/模型遵守仓库 `.gitignore`（不入 git）。阶段二已用 Docker `neo4j:5-community` 实测导入 + 查询。
- **构建**（本地测试环境 `conda activate hy_py312`，`pip install -r web/requirements.txt`）：

```bash
python "Language Stacking-Linguistic Weaving/web/build_learning.py" --validate --db --check
python "Language Stacking-Linguistic Weaving/web/export_neo4j.py"
python -m pytest "Language Stacking-Linguistic Weaving/web/tests" -q
```

- **CI**：`.github/workflows/learning-ci.yml` 在 `Language Stacking-Linguistic Weaving/**` 或 `docs/language_stacking/**` 变更时跑同一套校验，并强制「改源即重建提交产物」——页面与源不一致则 CI 失败。

- **纪律**：新增/修改知识一律改 `languages/**` 源文件后重建，绝不直接编辑 `docs/language_stacking/learning/` 产物；AI 起草的例句标注「待母语审校」后才入正式语料。流程：登记 → 写 prose/data → `--validate --db --check` + pytest（一键验收见 `web/run_tests.ps1`）。

------

## 16. 附录 A 数据模型 Data Model

**正本语料 JSON schema（v1）**。一切输出的唯一事实源。

```jsonc
{
  "id": "nat-001",
  "slug": "one-moon-eight-ripples",
  "series": "nature",
  "format": ["stack", "card"],
  "image_of_thought": "同一轮月，照着所有说它的人。",
  "source": {
    "lang": "zh",
    "text": "海上生明月，天涯共此时。",
    "author": "张九龄",
    "work": "《望月怀远》",
    "era": "唐 开元年间",
    "rights": "A",
    "original": false
  },
  "translations": [
    {
      "lang": "en",
      "text": "Over the sea a bright moon rises; / we share this moment across the world.",
      "mode": "G",
      "literal": "on-sea [it] gives-birth bright moon; sky's-edge together this-hour.",
      "note": "生：'give birth to' 一日一意，月从海中'生'出。",
      "status": "drafted"
    }
  ],
  "linguistic_notes": [
    "月亮在印欧系各语多为阴性（luna/la lune/der Mond... der 阳性）、中文'月'无性——母语无性别的文明把月当作'会阴晴圆缺的物'。",
    "涯=水边天边；天涯=世界尽头——'天涯共此时'把空间压平成'此刻'。"
  ],
  "visual": {
    "palette": ["#101418", "#c5a253", "#e8e0cf"],
    "footage_tags": ["moon", "sea", "night"],
    "image_prompt": "a full moon over a calm night sea, ink-wash gradient, high contrast low saturation, no text"
  },
  "audio": {
    "voices": { "zh": "zh-CN-XiaoxiaoNeural", "en": "en-US-JennyNeural", "fr": "fr-FR-DeniseNeural",
                 "ja": "ja-JP-NanamiNeural", "sa": "scholar|fallback", "la": "scholar|espeak",
                 "de": "de-DE-KatjaNeural", "sv": "sv-SE-SofieNeural" },
    "music_identity": "guqin → folk piano → chanson → koto → vina/bowl → organ → lied → nordic folk",
    "ambient": ["sea waves", "night wind"]
  },
  "status": "draft | translated | reviewed | produced | published"
}
```

**指定字段**：`status` 生命周期五态；`translations[].status` 逐语状态（未审不署名）；`rights` 用 A/B/C 档；`mode` 用 L/G/P（§10.1）。**校验规则**：无 `source.text` 不出片；`translations` 至少含"当前 Hero 语 + 中/英双解"；`linguistic_notes` 至少 1 条（织线）。

---

## 17. 附录 B 8 语完整对照样例 Worked Sample

以下为**工作底稿（演示用）**：演示"叠 + 织 + 照"如何落到一页。**凡译文均须经 §10 审校后方可用于成片**；sa/la 正式稿由受训人员起草，此处仅展示"词汇 + 注"形态。

*Draft below is a demonstration of Stack + Weave. All translations must pass the §10 review before production; sa/la full renderings are drafted by trained reviewers — here we show the word+gloss form.*

### B.1 原句 Source
> **海上生明月，天涯共此时。** —— 张九龄《望月怀远》（唐）

### B.2 八语对照 Working Stack

| 语 Lang | 译文 Rendering | 字面直译 Literal / 注 Note |
|---|---|---|
| **en** | *Over the sea a bright moon rises; we share this moment across the world.* | lit. on-sea it-begets bright-moon; sky's-edge together this-hour — "生" = to give birth to |
| **fr** | *Au-dessus de la mer, une lune claire se lève ; nous partageons cet instant aux confins du monde.* | lit. above-of-the sea, a moon clear itself-raises; we share this instant at the limits of-the world |
| **ja** | 海の上に明月昇り、天涯にこの時を同じくす。 | lit. sea-gen.上に bright-moon rises; 天涯=世界の果て、時を同じく=同刻 |
| **sa** | （待专家起草 *pending specialist draft*）समुद्रे जायते प्रकाशा चन्द्रिका, संसारे जन्मान्तरसहस्रैः समा घटिका। | 词汇层：समुद्र samudra（海）、चन्द्र candra（月）、समां घटिकां samāṃ ghaṭikāṃ（共此时）——整句译由受训译员完成并审校 |
| **la** | (*carmen* by reviewer) *Clara luna super mare oritur; nos hoc idem momentum per totum orbem tenemus.* | lit. clear moon above the sea rises; we this same moment through the whole world hold — mare/mar/sea 词族直达印欧 |
| **de** | *Über dem Meer erhebt sich der lichte Mond; wir teilen diese Stunde bis ans Ende der Welt.* | lit. over the sea rises the bright moon; we share this hour to the end of the world |
| **sv** | *Över havet stiger den klara månen; vi delar denna stund vid världens ände.* | lit. over the sea rises the clear moon; we share this hour at the world's end — orden: hav/sea, måne/moon, stund/moment |

> **教学注 Teaching note**：注意这颗月亮的"语法性别"——la lune(法/阴)、der Mond(德/阳)、the moon(英/无)、月(中/无)、candra(梵/阳)——"语言孕育了我们看待世界的方式"。(*Note how each grammar genders the moon differently; language shapes how we see the world.*)

### B.3 生成示例 Format 映射
- **A 型**：B.2 即分镜表；语音按 voices 逐个登场（sa/la 以词汇+注轨处理）。
- **C 型卡**：用法语轨 + 月之影像 + 词族小图（luna/la lune/moon/måne/月）。
- **E 型**：词源族谱动画：印欧 *mē-／lūna 一族 vs 汉字节日之"月"（象形：月缺之形）。

---

## 18. 附录 C 扩展语种预案 Expansion Playbook

**生产编队已扩至 32 语**（详见 **[LANGUAGES_LINGUISTIC_EXPANSION.md](LANGUAGES_LINGUISTIC_EXPANSION.md)**：选语五原则、24 张新增身份卡、新织线、三档制作机制、术语表扩展样例）。本节保留**候选池**（Ready-List，排产候补）与转正条件：

| 候选语言 | ISO | 理由（一句话） | 优先度 |
|---|---|---|---|
| 意大利语 it | it | 拉丁的活体孩子（↔ la）；文艺复兴 | 高 |
| 葡萄牙语 pt | pt | 大航海、saudade；巴西的跨洋语 | 高 |
| 乌尔都语 ur | ur | 与印地同语法两文字——"一门语言两身世" | 高 |
| 巴利语 pi | pi | 佛说原典（↔ sa bo 织线） | 中 |
| 古希腊语 grc | grc | 荷马原文（↔ el 织线） | 中 |
| 匈牙利语 hu | hu | 乌拉尔另一极；元音和谐 + 18 格 | 中 |
| 立陶宛语 lt | lt | 最"古老"的活印欧语 | 中 |
| 冰岛语 is | is | 语言纯化主义 | 中 |
| 世界语 eo | eo | 人造语言的乌托邦 | 低 |
| 夏威夷语 haw | haw | 波利尼西亚复兴另一例（↔ mi） | 中 |
| 切罗基语 chr | chr | 唯一独立造的音节字（司奎亚 1821） | 中 |
| 祖鲁语 zu / 科萨语 xh | zu/xh | 非洲搭舌音 clicks 语音珍品 | 中 |
| 豪萨语 ha | ha | 亚非·乍得语支，西非贸易通用语 | 中 |
| 阿姆哈拉语 am | am | 吉兹字体系宝库；埃塞文明 | 中 |
| 因纽特语 iu | iu | 多式综合语极限样本 | 低 |
| 巴斯克语 eu | eu | 欧洲最古活遗存；无亲人的语言 | 中 |

**扩展流程（不变）**：新增语言即新增一张**身份卡**（§3 结构）→ 术语表追加 → 试一集 C 型词卡 → 评审 → 转正。**转正条件**：该语 ≥10 条术语 + 语音方案可行 + 有对应文明主题 + 词卡试跑通过。

---

## 19. 附录 D 概念 × 八语术语表 Core Glossary

**核心概念 → 八语对照**（全期一致性底表；完整版见 `02_corpus/glossary.md`）。

| 概念 Concept | zh | en | fr | ja | sa (IAST) | la | de | sv |
|---|---|---|---|---|---|---|---|---|
| 水 Water | 水 | water | eau | 水（みず） | jala जल | aqua | Wasser | vatten |
| 月 Moon | 月 | moon | lune | 月（つき） | candra चन्द्र | luna | Mond | måne |
| 心 Heart | 心 | heart | cœur | 心（こころ） | hṛdaya हृदय | cor | Herz | hjärta |
| 时间 Time | 时 | time | temps | 時（とき） | kāla काल | tempus | Zeit | tid |
| 海 Sea | 海 | sea | mer | 海（うみ） | samudra समुद्र | mare | Meer | hav |
| 自由 Freedom | 自由 | freedom | liberté | 自由（じゆう） | mokṣa/स्वतन्त्र | libertas | Freiheit | frihet |
| 茶 Tea | 茶 | tea | thé | 茶（ちゃ） | cāya चाय | (theria 借) | Tee | te |
| 寂静 Silence | 静 | silence | silence | 静けさ（しずけさ） | śāntiḥ शान्तिः | silentium | Stille | tystnad |
| 树 Tree | 树 | tree | arbre | 木（こ） | vṛkṣa वृक्ष | arbor | Baum | träd |
| 风 Wind | 风 | wind | vent | 風（かぜ） | vāta वात | ventus | Wind | vind |
| 光 Light | 光 | light | lumière | 光（ひかり） | jyoti ज्योति | lux | Licht | ljus |
| 自然 Nature | 自然 | nature | nature | 自然（しぜん） | prakṛti प्रकृति | natura | Natur | natur |

> 词汇本身即是故事：*prakṛti*（自然/本性与"造"同根）、*mundus* 与 *孟/明*、*Zeit* 与 *tid* 同属印欧 *dī-（分开）……每张表都能长出一条 E 型词源片。*Each row is a potential word-genealogy episode.*

---

## 结语 Afterword

语言叠织的最终产品，不是"八行译文"，而是**让观众在 45 秒里感到：同一个人类之心，被八种文明各自点亮了一次。** 用水、月、心做种子，用叠、织、照做方法，用音、形、像做颜料——慢慢织，慢慢亮。

*The final product is not "eight rows of translation" — it is the feeling, in forty-five seconds, that one human heart was lit once by eight civilizations. Seeds: water, moon, heart. Method: stack, weave, illuminate. Pigment: voice, glyph, image. Weave slowly, light gently.*

—— Language Stacking · Linguistic Weaving · 语言叠织（v1.0 总体规划，2026-09-14）
