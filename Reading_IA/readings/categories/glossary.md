# glossary.md 术语架 · Term Registry

Single source for **term-level** knowledge across the whole reading domain — literature, theory, philosophy, mathematics, science, social science, media. Generator: `web/build_reading.py` → `docs/reading_ia/glossary.html`.

术语级记录的唯一来源，覆盖跨学科；生成器产出 `glossary.html`。

## Format 格式

每一条一个 `## 术语` 小节，字段如下（en / zh / def_zh / def_en 必填）：

```markdown
### <term-slug> · <中文名>
- **mode**: concept | tradition | archetype | practice   模式：概念 / 传统 / 原型 / 方法
- **domain**: <领域轴 tag>（`categories/README.md`）
- **cluster**: [[categories/<slug>]] 隶属概念簇或原型簇
- **def_zh**: 一句话定义（中文）
- **def_en**: One-line definition (English)
- **epitome**: 典例（作品/作者/文本，含年份）——原型必填 ≥2 例
- **source**: 出处 / 来源与把握 ✓◐○✗
- **links**: 相关 [[library/...]] · [[authors/...]] · [[moment/themes/...]]
```

---

## counterlife · 反生活
- **mode**: archetype
- **domain**: literature
- **cluster**: [[categories/mirror-double]]
- **def_zh**: 未曾活过的那种生活；人如此，国家亦然——「国家的反生活」是本项目的核心观察工具。
- **def_en**: The life you did not live; just as individuals have counterlives, so do states — the project's core lens.
- **epitome**: Emily St. John Mandel《Exit Party》(2026) —— A/B 两面皆国家的反生活；Philip Roth《The Plot Against America》(2004) 反事实极权美国
- **epitome_en**: Mandel, Exit Party (2026) — both A/B sides are national counterlives; Roth, The Plot Against America (2004), a counterfactual totalitarian America
- **source**: Mandel 访谈（irishtimes.com · lithub.com 2026-09）✓
- **source_en**: Mandel interviews (irishtimes.com · lithub.com, Sep 2026) ✓
- **links**: [[library/2026-mandel-exit-party]] · [[authors/mandel]]

## mirror-double · 双身与镜像
- **mode**: archetype
- **domain**: theory / literature
- **cluster**: [[categories/mirror-double]]
- **def_zh**: 人物、国家或文本的镜像分裂与互认；以重复句、对应人物缝合两面——超越解谜，读作「同一焦虑的两种结局」。
- **def_en**: Mirror-selves sutured by repeated sentences; read as twin outcomes of one anxiety, not a puzzle.
- **epitome**: Exit Party 的 Ari/Ibari 与双卡里姆；China Miéville《The City & The City》(2009)；Naomi Klein《Doppelganger》(2023)
- **epitome_en**: Exit Party's Ari/Ibari and the two Karims; China Miéville, The City & The City (2009); Naomi Klein, Doppelganger (2023)
- **source**: Mandel 自述（lithub.com ✓）；Klein 对照 ◐
- **source_en**: Mandel's own account (lithub.com ✓); Klein in comparison ◐
- **links**: [[categories/mirror-double]] · [[library/2026-mandel-exit-party]]

## aftermath-narrative · 余波叙事
- **mode**: archetype
- **domain**: literature
- **cluster**: [[categories/aftermath]]
- **def_zh**: 聚焦灾难**之后**而非灾难本身的叙事——余波重于现场，希望与照护藏在废墟里。
- **def_en**: Narrative of the aftermath, not the disaster — what follows matters more than the event.
- **epitome**: Mandel《Station Eleven》(2014) 与《Exit Party》；《The Leftovers》后启示录剧集
- **epitome_en**: Mandel, Station Eleven (2014) and Exit Party; The Leftovers, the post-apocalyptic series
- **source**: Mandel: "I am interested in its aftermath."（lithub.com ✓）；Perrotta 剧集对照 ✓
- **source_en**: Mandel: "I am interested in its aftermath." (lithub.com ✓); Perrotta's series in comparison ✓
- **links**: [[library/2026-mandel-exit-party]]

## aestheticized-violence · 图像化暴力
- **mode**: archetype
- **domain**: theory / literature
- **cluster**: [[categories/aestheticized-violence]]
- **def_zh**: 暴力被「排演」成美学构图——凶手以文学/影像为世界观，受害者被酿成偶像化身；罪案由此成为谜面本身。
- **def_en**: Violence staged as an aesthetic code — the killer's lens is literature and film, the victim composed into an icon.
- **epitome**: Fred Vargas《Une unique lueur》(2026) 银莲花女尸 + Bacall/Bogart 构图；J.G. Ballard 式「图像即罪行」
- **epitome_en**: Vargas, Une unique lueur (2026) — anemone, the staged corpse in a Bacall/Bogart composition; J.G. Ballard's "image-as-crime"
- **source**: Vargas 书评（lemonde 系 ◐）；Ballard 对照 ◐
- **source_en**: Vargas reviews (Le Monde press ◐); Ballard in comparison ◐
- **links**: [[library/2026-vargas-une-unique-lueur]] · [[authors/vargas]]

## intertext-vault · 互文宝匣
- **mode**: tradition
- **domain**: theory
- **cluster**: [[categories/language-meaning]]
- **def_zh**: 以一首诗 / 一幅画 / 一部电影为全书的互文枢纽，标题即答案的一半——文本在文本之网中获得意义。
- **def_en**: One quoted artifact (a poem, a painting, a film) as the intertextual hinge; meaning lives in the network of texts.
- **epitome**: Vargas 取 Nerval《El Desdichado》(1853)「一束唯一的光」为书名与谜面；Mandel《Swan Dive》画作串起全篇
- **epitome_en**: Vargas takes Nerval's El Desdichado (1853), "one unique light", as title and riddle; Mandel's painting Swan Dive threads the whole book
- **source**: Vargas 官方出版信息 + 书评 ✓◐；Nerval 原诗 ✓
- **source_en**: Vargas official publication info + reviews ✓◐; Nerval's poem ✓
- **links**: [[categories/language-meaning]] · [[library/2026-vargas-une-unique-lueur]]

## memory-repetition · 记忆与复诵
- **mode**: concept
- **domain**: philosophy / literature
- **cluster**: [[categories/language-meaning]]
- **def_zh**: 人物的反复重述、行走、绕圈——记忆不被记住，而被迫上演；复诵既是创伤机制，也是解谜钥匙。
- **def_en**: Characters who repeat, walk, circle; memory is performed, not recalled — repetition is both trauma and key.
- **epitome**: Vargas Adamsberg 系列；普鲁斯特式非自愿记忆传统
- **epitome_en**: Vargas's Adamsberg cycle; the Proustian tradition of involuntary memory
- **source**: Vargas 书评 ◐
- **source_en**: Vargas reviews ◐
- **links**: [[library/2026-vargas-une-unique-lueur]]

## witness-aesthetics · 见证美学
- **mode**: tradition
- **domain**: history / literature
- **cluster**: [[categories/aftermath]] · 见证文学
- **cluster_en**: aftermath · witness literature
- **def_zh**: 亲历者把第一人称夺回自己手中——口述史 × 文学转写的传统；「若无人见证，你的过去就开始像虚构」。
- **def_en**: The survivor reclaims the first person — oral history × literary transcription; un-witnessed, the past feels fictional.
- **epitome**: Gisèle Pelicot & Judith Perrignon《Et la joie de vivre》(2026)；Primo Levi 见证文学线；Marceline Loridan-Ivens
- **epitome_en**: Gisèle Pelicot & Judith Perrignon, Et la joie de vivre (2026); Primo Levi's testimonial-literature line; Marceline Loridan-Ivens
- **source**: 出版信息 ✓；关系表 ✓
- **source_en**: publication record ✓; relations table ✓
- **links**: [[library/2026-pelicot-joie-de-vivre]] · [[authors/perrignon]]

## testimonial-co-write · 证言转写合著
- **mode**: practice
- **domain**: history / social-science
- **cluster**: [[categories/aftermath]]
- **def_zh**: 经历者口述、作家转写成形——合著把声音还给本人，作家的手艺是透明的容器。
- **def_en**: The survivor speaks, a writer shapes it into form — the writer's craft is a transparent vessel.
- **epitome**: Pelicot × Perrignon《Et la joie de vivre》(2026)；Perrignon × Loridan-Ivens《Et tu n'es pas revenu》(2015)
- **epitome_en**: Pelicot × Perrignon, Et la joie de vivre (2026); Perrignon × Loridan-Ivens, Et tu n'es pas revenu (2015)
- **source**: relations.json cowrites ✓
- **source_en**: relations.json cowrites ✓
- **links**: [[authors/perrignon]] · [[authors/pelicot]]

## good-death · 善终与生死观
- **mode**: tradition
- **domain**: medicine-health
- **cluster**: [[categories/cosmos-place]] · 生死观话语场
- **cluster_en**: cosmos-place · the life-and-death discourse
- **def_zh**: 从「延命」到「尊厳」的范式——在宅安宁医疗与死亡素养是文明史的病历。
- **def_en**: From prolonging life to preserving dignity — home palliative care as a case-file of civilisation.
- **epitome**: 萬田緑平《棺桶まで歩こう》(2026)；柏木哲夫 ホスピス缓和ケア谱系；青柳幸利 8000步/日实证线
- **epitome_en**: Manda Ryōhei, Funeoke made arukō ("Let's walk to the coffin"); Kashiwagi Tetsuo's hospice palliative-care lineage; Aoyuki Yukitoshi's 8,000-steps/day evidence line
- **source**: 出版信息 ✓；对谈 2026-02-11 ✓
- **source_en**: publication record ✓; dialogue 2026-02-11 ✓
- **links**: [[library/2026-manda-kanoke-made]] · [[authors/manda]]

## template · 占位示例
- **mode**: concept
- **domain**: cross-disciplinary
- **cluster**: （待定）
- **cluster_en**: (to be set)
- **def_zh**: 占位模板——新术语随手复制本小节填写。
- **def_en**: placeholder template — copy this section to register a new term.
- **epitome**: —
- **epitome_en**: —
- **source**: —
- **source_en**: —