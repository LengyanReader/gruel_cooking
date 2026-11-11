import json, io, collections

p = 'Reading_IA/web/data/authors.json'
a = json.load(io.open(p, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
au = {x['id']: x for x in a['authors']}

ts = au['tsing']
ts['circle'] = [
    {
        "who": "Donna Haraway",
        "edge": "⇌",
        "why_zh": "同代对谈：多物种、共生（sympoiesis）与「与麻烦共处」的共同问题域",
        "why_en": "peer interlocutor on multispecies life, sympoiesis and staying with the trouble",
        "conf": "✓"
    },
    {
        "who": "Nils Bubandt / Elaine Gan / Heather Swanson",
        "edge": "✎",
        "why_zh": "Feral Atlas 合编者；「斑驳人类世」的共同作者",
        "why_en": "co-editors of Feral Atlas and co-authors of the patchy Anthropocene work",
        "conf": "✓"
    },
    {
        "who": "Matsutake Worlds Research Group",
        "edge": "✎",
        "why_zh": "松茸研究协作组：多人多地的民族志协作",
        "why_en": "the matsutake research collective; multi-sited collaborative ethnography",
        "conf": "✓"
    },
    {
        "who": "Shiho Satsuka / Michael Hathaway",
        "edge": "✎",
        "why_zh": "松茸追踪的合作研究者",
        "why_en": "collaborators in tracing matsutake worlds",
        "conf": "◐"
    },
    {
        "who": "UC Santa Cruz · 人类学系",
        "edge": "◎",
        "why_zh": "长期任教所在，多物种与人类世研究的据点",
        "why_en": "long-term institutional home for multispecies and Anthropocene work",
        "conf": "✓"
    }
]
ts['timeline'].append({
    "y": "2019",
    "event_zh": "与 Escobar 同被列为「后发展/多物种」一代的核心引用",
    "event_en": "read alongside Escobar as core references for post-development and multispecies work",
    "conf": "◐"
})
ts['works'].append({
    "y": "1993",
    "title": "In the Realm of the Diamond Queen",
    "title_en": "In the Realm of the Diamond Queen",
    "note_zh": "边陲、性别与国家的人类学",
    "note_en": "marginality, gender and the state",
    "conf": "✓"
})
ts['unverified'].append({
    "item": "《In the Realm of the Diamond Queen》出版社与页数、以及 Feral Atlas 的确切上线年份（2020/2022 两说）",
    "item_en": "publisher and pages of In the Realm of the Diamond Queen, and the exact launch year of Feral Atlas (2020 and 2022 both cited)",
    "conf": "◐"
})

es = au['escobar']
es['circle'] = [
    {
        "who": "Michal Osterweil / Kriti Sharma",
        "edge": "✎",
        "why_zh": "《Relationality》(2022) 合著者：社会运动理论与科学哲学",
        "why_en": "co-authors of Relationality (2022): social movement theory and philosophy of science",
        "conf": "◐"
    },
    {
        "who": "Marisol de la Cadena",
        "edge": "⇌",
        "why_zh": "同代对谈：政治本体论与「大地存在」",
        "why_en": "peer interlocutor on political ontology and earth beings",
        "conf": "✓"
    },
    {
        "who": "Ashish Kothari / Alberto Acosta / Gustavo Esteva",
        "edge": "⇌",
        "why_zh": "多元宇宙与后发展运动中的同行：Buen Vivir、生态斯瓦拉吉",
        "why_en": "allies in pluriverse and post-development movements: Buen Vivir, ecological swaraj",
        "conf": "◐"
    },
    {
        "who": "Grupo de Estudios Culturales · Universidad del Valle（Cali）",
        "edge": "◎",
        "why_zh": "早期学术据点：发展话语与哥伦比亚太平洋研究",
        "why_en": "early institutional base for development-discourse and Colombian Pacific research",
        "conf": "◐"
    },
    {
        "who": "UNC Chapel Hill · 人类学系",
        "edge": "◎",
        "why_zh": "长期任教所在（荣退）",
        "why_en": "long-term home department (now emeritus)",
        "conf": "✓"
    }
]
for ev in [
    ("2010", "《为后发展的一场明加》出版", "Una minga para el postdesarrollo"),
    ("2016", "《自主与设计》出版", "Autonomía y diseño"),
    ("2020", "《多元宇宙政治》出版", "Pluriversal Politics"),
    ("2022", "《关联性》合著出版", "Relationality (with Osterweil & Sharma)")
]:
    es['timeline'].append({"y": ev[0], "event_zh": ev[1], "event_en": ev[2], "conf": "◐"})
es['timeline'].sort(key=lambda x: x['y'])

for w in [
    ("2010", "Una minga para el postdesarrollo", "明加：后发展的实践原型"),
    ("2016", "Autonomía y diseño", "自主与设计：从设计人类学到自治"),
    ("2020", "Pluriversal Politics", "真实/可能：多元宇宙的政治"),
    ("2022", "Relationality", "关系本体论（合著）")
]:
    es['works'].append({
        "y": w[0], "title": w[1], "title_en": w[1],
        "note_zh": w[2], "note_en": w[2], "conf": "◐"
    })
es['works'].sort(key=lambda x: x['y'])
es['unverified'].append({
    "item": "《明加》《自主与设计》《多元宇宙政治》《关联性》的出版社、ISBN、页数与版次（本轮未能联网复核）",
    "item_en": "publishers, ISBNs, pages and printings of Una minga, Autonomía y diseño, Pluriversal Politics and Relationality (not re-checked online this round)",
    "conf": "◐"
})

io.open(p, 'w', encoding='utf-8', newline='\n').write(
    json.dumps(a, ensure_ascii=False, indent=2) + '\n')
print('authors.json updated')
