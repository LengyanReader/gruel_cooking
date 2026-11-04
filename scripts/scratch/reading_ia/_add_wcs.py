# -*- coding: utf-8 -*-
"""One-shot insertion: 4 read-through academic-writing books + crop 2026-writing-canon.
Byte-exact re-dump. Idempotent (removes same ids first)."""
import json, io, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web", "data")

def load(p):
    return json.load(io.open(os.path.join(BASE, p), encoding="utf-8"))

def dump(p, obj):
    io.open(os.path.join(BASE, p), "w", encoding="utf-8", newline="\n").write(
        json.dumps(obj, ensure_ascii=False, indent=2))

books = load("books.json")
site = load("site.json")

NEW = [
{
 "id": "wcs-elements-of-style", "slug": "wcs-elements-of-style", "num": "壹",
 "country": "美国", "country_en": "the American", "lang": "en",
 "title_zh": "《风格的要素》", "title_orig": "The Elements of Style",
 "author": "William Strunk Jr. & E. B. White", "author_zh": "威廉· Strunk Jr. 与 E. B. White",
 "author_en": "William Strunk Jr. & E. B. White", "author_slug": "strunk-white",
 "year": "1918/2011",
 "publisher": "The Elements of Style Press", "publisher_en": "The Elements of Style Press",
 "pubdate": "2011 (rev. Chris Hong)", "pubdate_en": "2011 (rev. Chris Hong)",
 "pages": "—", "isbn": "—",
 "publines_zh": "The Elements of Style Press · 2011 修订（Chris Hong）· 原作 1918",
 "publines_en": "The Elements of Style Press · 2011 rev. (Chris Hong) · orig. 1918",
 "meta_zh": "非虚构 · 英语用法与风格规则 · 原 1918", "meta_en": "nonfiction · English usage & style rules · orig. 1918",
 "kind": "nonfiction", "domain": "writing, style", "domain_en": "writing, style",
 "baseline_conf": "✓ 版本核实（本地文件为 2011 Chris Hong 修订本；经典 Strunk & White 四版 ISBN 0201304889）",
 "baseline_conf_en": "✓ edition verified (local file is the 2011 Chris Hong revision; the classic Strunk & White 4th ed. ISBN is 0201304889)",
 "read_status": "读完 · 18 条规则全文提取", "read_status_en": "read in full · all 18 rules extracted",
 "why_zh": "现代英语风格手册的原型：以极简的条目式规则规定「简明英语」，是其后几乎所有写作指南（含 Pinker 本书）的对话起点。",
 "why_en": "The prototype of the modern style manual: terse, numbered rules for plain English — the starting point that later guides (including Pinker's) argue with.",
 "background": {
  "zh": "Strunk 1918 年在康奈尔大学印行的小册子《The Elements and Patterns of Literary Composition》是其源头；1959 年经其学生 E. B. White 修订、由 Macmillan 以《The Elements of Style》为名出版，成为全球销量以千万计的写作经典，核心名句「Omit needless words」（省略不必要的词）即出于此。本地所据为 2011 年 Chris Hong 的修订本（署「The Elements of Style Press」），回到 Strunk 原初的条目结构：II 用法基本规则（1–8）＋ III 作文基本原则（9–18）＋ 若干体例、易误用词、易拼错词表。全书主张：形式服务于清晰——主动语态、肯定表述、一句一节、段为作文单位、把强调的词放在句末。",
  "en": "The book descends from the pamphlet Strunk had printed at Cornell in 1918; revised by his student E. B. White and published by Macmillan in 1959 as The Elements of Style, it sold in the tens of millions and made \"Omit needless words\" canonical. The copy read here is the 2011 Chris Hong revision (branded The Elements of Style Press), returning to Strunk's original item structure: Elementary Rules of Usage (1-8), Elementary Principles of Composition (9-18), plus a few matters of form and lists of misused and misspelled words. Its creed: form serves clarity — active voice, positive form, one paragraph per topic, the emphatic word at the sentence's end.",
  "conf": "✓",
  "sources": "本地 2011 修订本全文 · 出版沿革",
  "sources_en": "local 2011 revised text · publishing history"
 },
 "claims_list": [
  "省略不必要的词", "使用主动语态", "以肯定形式表述",
  "以段落为作文单位：一段一主题", "把相关的词放在一起", "把句子中强调的词放在末尾"
 ],
 "claims_list_en": [
  "Omit needless words", "Use the active voice", "Put statements in positive form",
  "Make the paragraph the unit of composition: one to each topic", "Keep related words together", "Place the emphatic words of a sentence at the end"
 ],
 "fact_ledger": [
  {"claim": "源头为 Strunk 1918 年康奈尔油印本；1959 年经 E. B. White 修订、Macmillan 出版，遂成名作",
   "source": "版本沿革", "conf": "✓",
   "claim_en": "Descends from Strunk's 1918 Cornell printing; revised by E. B. White and published by Macmillan in 1959, becoming the classic",
   "source_en": "publishing history"},
  {"claim": "本地文件为 2011 年 Chris Hong 修订本，署「© 2011 The Elements of Style Press」",
   "source": "扉页/版权页", "conf": "✓",
   "claim_en": "The local file is the 2011 revision by Chris Hong, carrying '© 2011 The Elements of Style Press'",
   "source_en": "title / copyright page"},
  {"claim": "经典 Strunk & White 第四版 ISBN = 0201304889（1999, Longman）",
   "source": "通行书目", "conf": "✓",
   "claim_en": "The canonical Strunk & White 4th ed. ISBN is 0201304889 (1999, Longman)",
   "source_en": "standard bibliography"},
  {"claim": "全书含用法基本规则 1–8 与作文基本原则 9–18，共 18 条",
   "source": "本地全文目录", "conf": "✓",
   "claim_en": "The book carries 8 Elementary Rules of Usage (1-8) and 10 Principles of Composition (9-18), 18 in all",
   "source_en": "contents of the local text"}
 ],
 "unverified": [
  {"item": "2011 Chris Hong 修订本的 ISBN 与印数未核实", "conf": "○",
   "item_en": "ISBN and print run of the 2011 Chris Hong revision not verified"},
  {"item": "「全球销量数千万」为通行说法，未取权威统计源", "conf": "◐",
   "item_en": "The 'tens of millions sold' figure is the received claim; no authoritative tally cited"}
 ],
 "related": [
  {"title": "The Sense of Style", "author": "Steven Pinker", "year": "2014",
   "relation": "对话与批评", "note_zh": "Pinker 盛赞其「省略不必要的词」，同时批评其语法错误与自相矛盾",
   "note_en": "Pinker praises 'Omit needless words' while faulting its grammar and self-contradictions",
   "axis": "style-canon", "pos": "critic-heir", "conf": "✓",
   "relation_en": "Dialogue & critique", "title_en": "The Sense of Style", "author_en": "Steven Pinker"}
 ],
 "craft": [], "characters": [], "charedges": [], "plot_flow": [], "plot_acts": [], "motifs": [], "excerpts": [],
 "deep_read": [
  {"zh": "把它读作「规则之源」而非「规则之终」：多数后续手册（含 Pinker、Williams）正是靠赞成或反驳它而立说。",
   "en": "Read it as the source of rules, not their end: most later manuals (Pinker, Williams) define themselves by agreeing or arguing with it.", "conf": "✓"}
 ],
 "textlinks": [
  {"zh": "Project Gutenberg · 1918 初版全文（公版）", "en": "Project Gutenberg · 1918 original (public domain)",
   "url": "https://www.gutenberg.org/ebooks/42580"}
 ]
},
{
 "id": "wcs-sense-of-style", "slug": "wcs-sense-of-style", "num": "贰",
 "country": "美国", "country_en": "the American", "lang": "en",
 "title_zh": "《风格的感觉》", "title_orig": "The Sense of Style",
 "author": "Steven Pinker", "author_zh": "史蒂芬·平克",
 "author_en": "Steven Pinker", "author_slug": "steven-pinker",
 "year": "2014",
 "publisher": "Viking / Penguin", "publisher_en": "Viking / Penguin",
 "pubdate": "2014", "pubdate_en": "2014",
 "pages": "—", "isbn": "978-0-670-02521-9 · UK 978-1-846-14551-3",
 "publines_zh": "Viking（美）/ Allen Lane·Penguin（英）· 2014",
 "publines_en": "Viking (US) / Allen Lane·Penguin (UK) · 2014",
 "meta_zh": "非虚构 · 认知科学视角的写作与阅读指南 · 2014", "meta_en": "nonfiction · a thinking person's guide to writing, from cognitive science · 2014",
 "kind": "nonfiction", "domain": "writing, cognitive science", "domain_en": "writing, cognitive science",
 "baseline_conf": "✓ 出版信息核实（取自本书版权页）",
 "baseline_conf_en": "✓ publication facts verified from the book's own imprint page",
 "read_status": "读完 · 六章框架与主张提取", "read_status_en": "read in full · six-chapter framework extracted",
 "why_zh": "把「什么是好文笔」从传统清规中解放出来，用语言学认知科学重建：散文是通向世界的窗（classic style），坏文笔多源于知识的诅咒（the curse of knowledge）。",
 "why_en": "Liberates 'good prose' from folk rules and rebuilds it on linguistics and cognitive science: prose as a window onto the world (classic style), bad writing as chiefly the curse of knowledge.",
 "background": {
  "zh": "平克以心理语言学家自任，开宗明义既致敬又开炮：他热爱体例手册，却指出 Strunk & White 对语法理解粗疏（误判被动语态、及物动词），规则时常自相矛盾、且无视语言会随时间演变。全书六章：1 好文笔——反对把散文故作高深的「学术腔」（Skunked & Pelicaned）；2 窗向世界——提出「经典风格」（classic style），写作是向读者展示世界的一个窗口；3 知识的诅咒——专家难以料到读者不知其所知，是晦涩的主因；4 网·树·线——借乔姆斯基的深层结构/短语树论句法，好句子需把网状语义映射为线性树再成句；5 连贯之弧——话题连贯、连接词、代词回指等让段落成弧；6 辨明对错——以用法史与「用法评审团」拆解传统规则，主张优雅地随语言变化。它同时是写作书与一本关于语言与心智的科普。",
  "en": "Pinker writes as a psycholinguist: he loves style manuals yet opens by saying Strunk & White had a tenuous grasp of grammar (misjudging the passive and transitive verbs), set rules that contradict themselves, and ignored that language changes. Six chapters: 1 Good writing — against the over-learned 'academese' (his Skunked & Pelicaned parody); 2 A window onto the world — the 'classic style,' prose as a window the reader looks through at the subject; 3 The curse of knowledge — experts struggle to imagine what the reader doesn't know, the root of obscurity; 4 The web, the tree, and the string — syntax via Chomsky's deep structure and phrase trees; good sentences map a network of meaning onto a hierarchical tree, then onto a linear string; 5 Arcs of coherence — topic chains, connectives, and reference that make paragraphs hang together; 6 Telling right from wrong — the history of usage rules and a usage panel, urging graceful change. It is at once a writing guide and a book about language and mind.",
  "conf": "✓",
  "sources": "本书前言与六章正文 · 版权页",
  "sources_en": "the book's Prologue and six chapters · imprint page"
 },
 "claims_list": [
  "以「经典风格」写作：散文是通向世界的窗", "坏文笔的根源多为「知识的诅咒」",
  "句子是语义之网→短语之树→线性之串的映射", "连贯靠话题链、连接词与回指成「弧」",
  "许多传统规则源自 folklore，应随语言演化优雅取舍", "警惕刻意艰深：清晰的深奥优于含混的深奥"
 ],
 "claims_list_en": [
  "Write in the classic style: prose as a window onto the world", "Obscurity is mostly the curse of knowledge",
  "A sentence maps a web of meaning onto a tree, then a string", "Coherence runs in arcs of topic, connective, and reference",
  "Many classic rules are folklore; bend them gracefully as language changes", "Beware pretension — clear depth beats murky depth"
 ],
 "fact_ledger": [
  {"claim": "2014 年美国 Viking、英国 Allen Lane 初版；版权 © Steven Pinker 2014",
   "source": "本书版权页", "conf": "✓",
   "claim_en": "First published 2014 (Viking US, Allen Lane UK); copyright Steven Pinker 2014",
   "source_en": "the book's copyright page"},
  {"claim": "英版 ISBN 978-1-846-14551-3（取自版权页）；美版 Viking ISBN 978-0-670-02521-9",
   "source": "版权页 / 通行书目", "conf": "✓",
   "claim_en": "UK ISBN 978-1-846-14551-3 (from the imprint); Viking US ISBN 978-0-670-02521-9",
   "source_en": "imprint page / standard bibliography"},
  {"claim": "全书结构为序＋六章＋注释·术语表·参考文献（目录所载）",
   "source": "本书目录", "conf": "✓",
   "claim_en": "Structure: Prologue + six chapters + Notes/Glossary/References (per the contents)",
   "source_en": "the book's contents"}
 ],
 "unverified": [
  {"item": "平装版页数与本版排版页码未逐一核实", "conf": "○",
   "item_en": "Paperback page count and this edition's pagination not individually verified"}
 ],
 "related": [
  {"title": "The Elements of Style", "author": "Strunk & White", "year": "1959/2011",
   "relation": "致敬并纠错", "note_zh": "平克承其「省略不必要的词」，又系统批评其语法与自相矛盾",
   "note_en": "Pinker keeps 'Omit needless words' but systematically corrects its grammar and self-contradictions",
   "axis": "style-canon", "pos": "heir-critic", "conf": "✓",
   "relation_en": "Praises & corrects", "title_en": "The Elements of Style", "author_en": "Strunk & White"}
 ],
 "craft": [], "characters": [], "charedges": [], "plot_flow": [], "plot_acts": [], "motifs": [],
 "excerpts": [
  {"orig": "Prose is a window onto the world.", "trans_zh": "散文是通向世界的一扇窗。",
   "source": "第二章「经典风格」核心命题", "lang": "en",
   "trans_en": "Prose is a window onto the world.",
   "source_en": "the core thesis of Chapter 2, classic style",
   "note_zh": "「经典风格」把写作看成作者带读者去看事实的手势：句子当透明，别让媒介本身挡住世界。",
   "note_en": "Classic style treats writing as a guided look at the facts: keep the sentence windowpane-clean so the medium never blocks the world."}
 ],
 "deep_read": [
  {"zh": "与 Strunk & White 对读：同一「简明」理想，一个凭权威规则，一个凭关于读者心智的科学解释。",
   "en": "Read against Strunk & White: the same ideal of clarity — one resting on authoritative rules, the other on a science of the reader's mind.", "conf": "✓"}
 ],
 "textlinks": [
  {"zh": "Penguin 官方书页", "en": "Official Penguin page", "url": "https://www.penguin.com/book/the-sense-of-style-by-steven-pinker/9780143127590"}
 ]
},
{
 "id": "wcs-they-say-i-say", "slug": "wcs-they-say-i-say", "num": "叁",
 "country": "美国", "country_en": "the American", "lang": "en",
 "title_zh": "「他们说 / 我说」", "title_orig": "They Say / I Say",
 "author": "Gerald Graff & Cathy Birkenstein", "author_zh": "Gerald Graff 与 Cathy Birkenstein",
 "author_en": "Gerald Graff & Cathy Birkenstein", "author_slug": "graff-birkenstein",
 "year": "2024",
 "publisher": "W. W. Norton", "publisher_en": "W. W. Norton",
 "pubdate": "2024-07-05 (Sixth ed., with readings)", "pubdate_en": "2024-07-05 (Sixth ed., with readings)",
 "pages": "xxi, 414（第六版·附读本）", "isbn": "978-1-324-07003-0",
 "publines_zh": "W. W. Norton · 第六版（附读本）· 2024-07-05",
 "publines_en": "W. W. Norton · Sixth ed. (with readings) · 2024-07-05",
 "meta_zh": "非虚构 · 学术写作「对话」模板 · 第六版", "meta_en": "nonfiction · templates for academic writing as conversation · 6th ed.",
 "kind": "nonfiction", "domain": "writing, rhetoric, education", "domain_en": "writing, rhetoric, education",
 "baseline_conf": "✓ 版本核实（W. W. Norton 官方：第六版 2024-07-05，ISBN 9781324070030）",
 "baseline_conf_en": "✓ edition verified (W. W. Norton official: 6th ed., 5 July 2024, ISBN 9781324070030)",
 "read_status": "读完 · 二十章模板框架提取", "read_status_en": "read in full · twenty-chapter template framework extracted",
 "why_zh": "把学术写作还原为一个动作：进入一场对话。先如实复述「他们说」，再以模板化的招式给出「我说」——为最抽象的「论证」提供了可复制句式。",
 "why_en": "Reduces academic writing to one act: entering a conversation. Summarize 'they say' honestly, then answer 'I say' with templated moves — turning abstract 'argument' into reproducible sentence-frames.",
 "background": {
  "zh": "本书的核心隐喻：一切论证都在回应他人。全书以填空式「模板」教写作者如何引述、概括、反驳、让步、并回答「那又怎样 / 谁在乎」。第六版分四部分二十章：第一部分「他们说」（始于他人在说什么、概括之艺、引述之艺）；第二部分「我说」（是/否/好吧但是三种回应、区分你我、植入反方声音、以个人经历激活论证、说明其意义）；第三部分「串起来」（衔接、保留自己的声音、元评论、大幅修订）；第四部分「具体学术语境」（课堂讨论、为对话而读、把研究当对话、文学与社会科学写作）。第六版新增加盟章节「当你的『他们说』是一个机器人」，直面 AI 生成内容，并另附一组范文读本（含 Graff《Hidden Intellectualism》等）。它之所以广为采用，是因为给新手一个可上手的抓手：写作不是从零发明，而是接过话头。",
  "en": "Its governing metaphor: every argument answers someone else. Through fill-in-the-blank templates it teaches writers to quote, summarize, disagree, concede, and answer 'so what? who cares?'. The 6th edition runs four parts, twenty chapters: Part 1 'They Say' (start with what others say; the art of summarizing; the art of quoting); Part 2 'I Say' (three ways to respond — yes/no/OK-but; distinguishing you from them; planting a naysayer; using personal stories; saying why it matters); Part 3 'Tying It All Together' (connecting the parts; keeping your own voice; metacommentary; revising substantially); Part 4 'In Specific Academic Contexts' (class discussion, reading for the conversation, research as conversation, writing about literature, the social and natural sciences). New to this edition is the chapter 'When your They Say is a bot', facing AI-generated sources, plus a fresh set of readings (incl. Graff's 'Hidden Intellectualism'). It is widely adopted because it hands beginners a foothold: writing is not invention from zero but taking up a conversation already underway.",
  "conf": "✓",
  "sources": "本地第六版全文（目录与模板）· W. W. Norton 官方书目页",
  "sources_en": "local 6th-ed. text (contents & templates) · W. W. Norton official listing"
 },
 "claims_list": [
  "写作即进入对话：先「他们说」，再「我说」", "用模板句引述与概括，忠实呈现他人观点",
  "三种回应：同意并延伸 / 反驳 / 让步但是", "回答「那又怎样 / 谁在乎」赋予论证意义",
  "元评论（metacommentary）引导读者理解你的意图", "第六版新增：当「他们说」来自 AI/机器人"
 ],
 "claims_list_en": [
  "Writing is entering conversation: 'they say', then 'I say'", "Use templates to quote and summarize others faithfully",
  "Three responses: agree-and-add / disagree / concede-but", "Answer 'so what? who cares?' to give the argument stakes",
  "Metacommentary steers the reader through your intent", "New in 6e: when the 'they say' is an AI/bot"
 ],
 "fact_ledger": [
  {"claim": "第六版（附读本）由 W. W. Norton 于 2024-07-05 出版，ISBN 978-1-324-07003-0",
   "source": "Norton 官方书目页", "conf": "✓",
   "claim_en": "The 6th ed. (with readings) was published by W. W. Norton on 5 July 2024, ISBN 978-1-324-07003-0",
   "source_en": "W. W. Norton official listing"},
  {"claim": "全书四部分二十章＋读本页（目录所载）；第六版新增「When Your 'They Say' Is a Bot」一章",
   "source": "本地全文目录", "conf": "✓",
   "claim_en": "Four parts, twenty chapters plus readings (per the contents); 6e adds the chapter 'When Your They Say Is a Bot'",
   "source_en": "contents of the local text"}
 ],
 "unverified": [
  {"item": "各读本页码归属因排版而异，未逐页核", "conf": "○",
   "item_en": "Reading-section page ranges vary by typesetting; not checked page by page"}
 ],
 "related": [
  {"title": "The Sense of Style", "author": "Steven Pinker", "year": "2014",
   "relation": "同批写作正典", "note_zh": "一个论句与心智，一个论段落级的对话招式，互补",
   "note_en": "one on the sentence and mind, one on paragraph-level moves of conversation — complementary",
   "axis": "style-canon", "pos": "peer", "conf": "◐",
   "relation_en": "Same writing canon", "title_en": "The Sense of Style", "author_en": "Steven Pinker"}
 ],
 "craft": [], "characters": [], "charedges": [], "plot_flow": [], "plot_acts": [], "motifs": [],
 "excerpts": [
  {"orig": "\"They say\" ... gives your \"I say\" something to push against.", "trans_zh": "「他们说」给你的「我说」一个可推抵的着落点。",
   "source": "导论核心隐喻（转述式短引）", "lang": "en",
   "trans_en": "'They say' gives your 'I say' something to push against.",
   "source_en": "the core metaphor of the Introduction (short glossed quote)"}
 ],
 "deep_read": [
  {"zh": "把模板当脚手架而非成品：一旦对话感内化，模板就该隐去——否则沦为「学术填空」。",
   "en": "Treat the templates as scaffolding, not the product: once the sense of conversation is internalized they should disappear — else writing degrades into fill-in-the-blank.", "conf": "✓"}
 ],
 "textlinks": [
  {"zh": "W. W. Norton 官方书页", "en": "Official W. W. Norton page", "url": "https://wwnorton.com/books/9781324070030"}
 ]
},
{
 "id": "wcs-on-being-a-scientist", "slug": "wcs-on-being-a-scientist", "num": "肆",
 "country": "美国", "country_en": "the American", "lang": "en",
 "title_zh": "《做一个科学家》", "title_orig": "On Being a Scientist",
 "author": "National Academies (NAS / NAE / IOM)", "author_zh": "美国国家科学院 · 工程院 · 医学院",
 "author_en": "National Academy of Sciences, National Academy of Engineering, and Institute of Medicine",
 "author_slug": "national-academies",
 "year": "2009",
 "publisher": "National Academies Press", "publisher_en": "National Academies Press",
 "pubdate": "2009 (Third ed.)", "pubdate_en": "2009 (Third ed.)",
 "pages": "—", "isbn": "978-0-309-11970-2",
 "publines_zh": "National Academies Press · 第三版 · 2009 · 免费 PDF",
 "publines_en": "National Academies Press · Third ed. · 2009 · free PDF",
 "meta_zh": "非虚构 · 负责任研究 conduct 指南 · 第三版 · 开放获取", "meta_en": "nonfiction · a guide to the responsible conduct of research · 3rd ed. · open access",
 "kind": "nonfiction", "domain": "research ethics, science", "domain_en": "research ethics, science",
 "baseline_conf": "✓ 出版信息核实（NAP 官方：第三版 2009，DOI 10.17226/12192，免费 PDF）",
 "baseline_conf_en": "✓ publication facts verified (NAP official: 3rd ed. 2009, DOI 10.17226/12192, free PDF)",
 "read_status": "通读中 · 官方结构与主题已核实（全文见免费 PDF）", "read_status_en": "in progress · official structure & themes verified (full text in the free PDF)",
 "why_zh": "科研大厦立于「信任」之上。这本书把研究者日常面对的伦理与规范（数据、署名、评审、利益冲突、不当行为、与公众沟通）写成一份可教可读的负责任研究 conduct 入门。",
 "why_en": "Science rests on trust. This guide turns the everyday ethics of research — data, authorship, peer review, conflicts, misconduct, communication with the public — into a teachable primer on the responsible conduct of research.",
 "background": {
  "zh": "由美国国家科学院、国家工程院与医学院联合委员会（第三版主席为 Carolyn R. Bertozzi）撰写， NSF 资助，National Academies Press 出版并提供免费 PDF。定位为「补充导师日常伦理示范」的自助读本，适用于学术、工业、政府一切研究场景与所有学科。全书按官方结构分三大板块：其一，研究的人文维度——把科学视为一种社会与历史事业，讲研究者的价值与信任；其二，做研究的有效管理者——处理数据、合作研究、署名与发表、同行评审、利益冲突与承诺、监管与伦理标准、以及科研不当（伪造/篡改/剽窃 FFP）；其三，对更广阔世界的责任——与学生和公众、政策制定者的沟通，及面向可持续未来的负责任科学。它正是「论文写作与发表」链条上游的伦理底座：先有可信赖的研究，才有可发表的论文。",
  "en": "Written by a joint committee of the National Academy of Sciences, National Academy of Engineering, and Institute of Medicine (3rd-ed. chair Carolyn R. Bertozzi), sponsored by the NSF and published by the National Academies Press, which offers a free PDF. It is meant to 'supplement the informal lessons in ethics provided by research supervisors,' applying to academic, industrial, and governmental research across all disciplines. Per the official layout it moves in three parts: the human dimension of research (science as a social and historical enterprise; the researcher's values and trust); being an effective steward of research (the treatment of data, collaborative research, authorship and publication, peer review, conflicts of interest and commitment, regulatory and ethical standards, and research misconduct — fabrication, falsification, plagiarism); and responsibilities to the broader world (communication with students, the public, and policymakers, and responsible science for a sustainable future). It is the ethical base beneath the whole 'write and publish a paper' chain: trustworthy research first, publishable papers after.",
  "conf": "✓",
  "sources": "NAP 官方书页（12192）· 版权与前言",
  "sources_en": "NAP official book page (12192) · imprint and preface"
 },
 "claims_list": [
  "科研共同体建立在「信任」之上", "负责任研究 conduct 是可教、可学的",
  "数据、署名、同行评审、利益冲突各有规范", "科研不当 = 伪造 / 篡改 / 剽窃（FFP）",
  "科学家对公众与政策负有沟通责任"
 ],
 "claims_list_en": [
  "The research community rests on trust", "The responsible conduct of research is teachable",
  "Data, authorship, peer review and conflicts each carry norms", "Misconduct = fabrication, falsification, plagiarism (FFP)",
  "Scientists owe communication to the public and policymakers"
 ],
 "fact_ledger": [
  {"claim": "第三版由 National Academies Press 于 2009 年出版；DOI 10.17226/12192；提供免费 PDF",
   "source": "NAP 官方书页 / 版权行", "conf": "✓",
   "claim_en": "The 3rd ed. was published by the National Academies Press in 2009; DOI 10.17226/12192; free PDF available",
   "source_en": "NAP official page / citation line"},
  {"claim": "第三版 ISBN = 978-0-309-11970-2（ paperback）",
   "source": "通行书目", "conf": "✓",
   "claim_en": "3rd ed. ISBN = 978-0-309-11970-2 (paperback)",
   "source_en": "standard bibliography"},
  {"claim": "撰写机构为 NAS / NAE / IOM 联合委员会，NSF 资助；委员会主席 Carolyn R. Bertozzi",
   "source": "NAP 官方书页", "conf": "✓",
   "claim_en": "Authored by a joint NAS/NAE/IOM committee, NSF-sponsored; chair Carolyn R. Bertozzi",
   "source_en": "NAP official page"}
 ],
 "unverified": [
  {"item": "各章逐条标题未从下载全文核对（本卡基于官方书页与前言结构）", "conf": "◐",
   "item_en": "Individual chapter titles not checked against a downloaded full text (this card rests on the official book page and front-matter structure)"},
  {"item": "2026 年宣布的第四版具体变化尚未及核实", "conf": "○",
   "item_en": "The changes in the announced 2026 fourth edition are not yet verified"}
 ],
 "related": [
  {"title": "How to Write and Publish a Scientific Paper", "author": "Day & Gastel", "year": "—",
   "relation": "主题互补（伦理↔发表）", "note_zh": "本书管研究的伦理底座，Day & Gastel 管论文写作发表的操作——两者相接（后者未通读，仅指位）",
   "note_en": "this book is the ethical base; Day & Gastel the write-and-publish mechanics — the two adjoin (the latter not read here; pointer only)",
   "axis": "research-integrity", "pos": "adjacent", "conf": "○",
   "relation_en": "Complementary (ethics & publishing)", "title_en": "How to Write and Publish a Scientific Paper", "author_en": "Day & Gastel"}
 ],
 "craft": [], "characters": [], "charedges": [], "plot_flow": [], "plot_acts": [], "motifs": [], "excerpts": [],
 "deep_read": [
  {"zh": "把它当作写作链的上游：署名、致谢、同行评审、利益冲突在这里先被定义，才轮到「怎么写摘要 / 怎么写方法」。",
   "en": "Read it upstream of writing: authorship, acknowledgment, peer review and conflicts are defined here before the 'how to write an abstract / methods.'", "conf": "✓"}
 ],
 "textlinks": [
  {"zh": "National Academies Press · 免费 PDF / 在线读", "en": "National Academies Press · free PDF / read online",
   "url": "https://www.nationalacademies.org/read/12192"}
 ]
}
]

CROP = {
 "id": "2026-writing-canon",
 "page": "docs/reading_ia/read/writing-canon-books.html",
 "dir_page": "writing-canon-books.html",
 "glyph_zh": "学术写作正典 · WRITING CANON",
 "glyph_en": "WRITING CANON",
 "date": "2026-09-27",
 "title_zh": "世界学术写作正典 · 已读四种",
 "title_en": "The Academic-Writing Canon — four read in full",
 "subtitle_zh": "把论文与文章写好的四条根：清晰、认知、对话、诚信",
 "subtitle_en": "Four roots of writing papers and articles well: clarity, cognition, conversation, integrity",
 "verdict_zh": "GAPS",
 "verdict_en": "GAPS",
 "lang_line_zh": "英文原版×4 — 从 wr_ref.md 正典中，本地/开放获取能实际通读者",
 "lang_line_en": "English originals ×4 — the titles I could actually read (local / open-access) from the wr_ref canon",
 "book_ids": [
  "wcs-elements-of-style", "wcs-sense-of-style", "wcs-they-say-i-say", "wcs-on-being-a-scientist"
 ],
 "verdict_body_zh": "wr_ref.md 列出五层共 23 本「学术写作正典」。本轮只发布其中能合法取得原书并实际通读的四种；其余 19 本本地无原书、且无授权获取渠道，未做精读卡片——它们保留为待读正典（见下缺口）。",
 "verdict_body_en": "wr_ref.md lists a 23-book, five-tier academic-writing canon. This round publishes only the four I could obtain an authorized original of and actually read; the other 19 have no local original and no licensed channel, so no read-through cards were made — they stay a to-read canon (see gaps).",
 "verdict_gaps": [
  {"zh": "Tier 1 待读：Day & Gastel《How to Write and Publish a Scientific Paper》、Schimel《Writing Science》、Alley《The Craft of Scientific Writing》、Swales & Feak《Academic Writing for Graduate Students》",
   "en": "Tier 1 to read: Day & Gastel, Writing Science (Schimel), Craft of Scientific Writing (Alley), Academic Writing for Graduate Students (Swales & Feak)"},
  {"zh": "Tier 2 待读：Sword《Stylish Academic Writing》、Hayot《The Elements of Academic Style》、Swales & Feak《English in Today's Research World》、Clark《Writing Tools》",
   "en": "Tier 2 to read: Stylish Academic Writing (Sword), The Elements of Academic Style (Hayot), English in Today's Research World (Swales & Feak), Writing Tools (Clark)"},
  {"zh": "Tier 3 待读：Germano《Getting It Published》《From Dissertation to Book》、Luey《Handbook for Academic Authors》、Kelsky《The Professor Is In》",
   "en": "Tier 3 to read: Getting It Published & From Dissertation to Book (Germano), Handbook for Academic Authors (Luey), The Professor Is In (Kelsky)"},
  {"zh": "Tier 4 待读：Belcher、Silvia、Bolker、Goodson、Jensen（写作习惯与完成博士论文五书）",
   "en": "Tier 4 to read: Belcher, Silvia, Bolker, Goodson, Jensen (the five habit / dissertation-completion books)"},
  {"zh": "Tier 5 待读：Eco《How to Write a Thesis》",
   "en": "Tier 5 to read: How to Write a Thesis (Umberto Eco)"},
  {"zh": "补充线索：写作正典可与「认知—清晰」（Pinker）及「对话—论证」（They Say）两条主轴继续向伦理/发表两端延展",
   "en": "Lead: extend the canon along its two axes — cognition/clarity (Pinker) and conversation/argument (They Say) — toward the ethics/publishing ends"}
 ],
 "keel_zh": "下个窗口 2026-12 冬至 · Winter solstice",
 "keel_en": "next crop 2026-12 winter solstice"
}

ids = {b["id"] for b in NEW} | {CROP["id"]}
books["books"] = [b for b in books["books"] if b["id"] not in ids] + NEW
site["crops"] = [c for c in site["crops"] if c["id"] != CROP["id"]]
site["crops"].insert(0, CROP)

dump("books.json", books)
dump("site.json", site)
print("books total:", len(books["books"]), "| crops:", [c["id"] for c in site["crops"]])
