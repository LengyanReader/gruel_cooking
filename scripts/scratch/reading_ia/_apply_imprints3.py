# -*- coding: utf-8 -*-
"""Batch 3: page counts from Crossref-indexed review citations (marked ◐),
plus DOI/ISBN additions for Knowing Where It Comes From.

Review sources (accessed 2026-11-11):
  salen   : 10.1162/dram.2007.51.1.183  (MIT Press Journals review, 688 pp.)
  juul    : 10.1177/1367549408091320    (European Journal of Cultural Studies, 255 pp.)
  mintz   : 10.1126/science.232.4746.111-a (Science, 274 pp., Viking 1985)
  gmt     : 10.1093/fmls/cql045         (Forum for Modern Language Studies, 119 pp.)
  distant : 10.3366/ccs.2013.0105       (Comparative Critical Studies, 244 pp.)
  bourgeois: 10.1080/08831157.2014.937234 (Romance Quarterly, 203 pp.);
             10.1080/00168890.2015.1065164 (Germanic Review, 224 pp. — conflict)
  mushroom: 10.1111/aman.12640? -> American Anthropologist 352 pp. vs
             American Ethnologist / Ethnobiology Letters / Green Letters 331 pp.
  encountering: Journal of Asian Studies 1995 review (ix + 290 pp.)
  knowing : 10.1353/book52838 (Project MUSE), ISBN 9781609385347
"""
import io
import json

PATH = 'Reading_IA/web/data/books.json'
ACC = '2026-11-11'

DATA = {
    'salen-zimmerman-rules-of-play': {
        'pages': '688',
        'publines_zh': 'MIT Press · 2003 · ISBN 9780262240451 · 688 页（据书评标示，◐）',
        'publines_en': 'MIT Press · 2003 · ISBN 9780262240451 · 688 pp (per review, ◐)',
        'baseline_conf': '✓ 版本核实（MIT Press 2003, ISBN 9780262240451）；页数 688 据 MIT Press 期刊书评（%s，◐）' % ACC,
        'baseline_conf_en': '✓ edition verified (MIT Press 2003, ISBN 9780262240451); 688 pp from an MIT Press journal review (%s, ◐)' % ACC,
        'ledger': [('《Rules of Play》2003 年 MIT Press 版共 688 页',
                    'The 2003 MIT Press edition of Rules of Play runs to 688 pages',
                    '书评, MIT Press Journals, 2007, DOI 10.1162/dram.2007.51.1.183',
                    'Review, MIT Press Journals, 2007, DOI 10.1162/dram.2007.51.1.183', '◐')],
        'drop': ['页数与版次'],
        'add_unverified': [('版次与印次（页数已据书评补）', 'edition and printing (pages now from a review)', '◐')],
    },
    'juul-half-real': {
        'pages': '255',
        'publines_zh': 'MIT Press · 2005 · ISBN 9780262101103 · 255 页（据书评标示，◐）',
        'publines_en': 'MIT Press · 2005 · ISBN 9780262101103 · 255 pp (per review, ◐)',
        'baseline_conf': '✓ 版本核实（MIT Press 2005, ISBN 9780262101103）；页数 255 据 European Journal of Cultural Studies 书评（%s，◐）' % ACC,
        'baseline_conf_en': '✓ edition verified (MIT Press 2005, ISBN 9780262101103); 255 pp from a review in the European Journal of Cultural Studies (%s, ◐)' % ACC,
        'ledger': [('《Half-Real》2005 年 MIT Press 版共 255 页',
                    'The 2005 MIT Press edition of Half-Real runs to 255 pages',
                    '书评, European Journal of Cultural Studies, 2008, DOI 10.1177/1367549408091320',
                    'Review, European Journal of Cultural Studies, 2008, DOI 10.1177/1367549408091320', '◐')],
        'drop': ['页数与版次'],
        'add_unverified': [('版次与印次（页数已据书评补）', 'edition and printing (pages now from a review)', '◐')],
    },
    'mintz-sweetness-power': {
        'pages': '274',
        'publines_zh': 'Viking · 1985 · 274 页（据书评标示，◐）· ISBN 待核',
        'publines_en': 'Viking · 1985 · 274 pp (per review, ◐) · ISBN pending',
        'baseline_conf': '◐ 出版年/出版社经来源核实；页数 274 据 Science 书评（%s，◐）；ISBN 待核' % ACC,
        'baseline_conf_en': '◐ year/publisher verified; 274 pp from a review in Science (%s, ◐); ISBN pending' % ACC,
        'ledger': [('《Sweetness and Power》1985 年 Viking 版共 274 页',
                    'The 1985 Viking edition of Sweetness and Power runs to 274 pages',
                    '书评, Science 232(4746), 1986, DOI 10.1126/science.232.4746.111-a',
                    'Review, Science 232(4746), 1986, DOI 10.1126/science.232.4746.111-a', '◐')],
        'drop': ['ISBN、页数与版次'],
        'add_unverified': [('ISBN 与版次（页数已据书评补）', 'ISBN and edition (pages now from a review)', '◐')],
    },
    'moretti-graphs-maps-trees': {
        'pages': '119',
        'publines_zh': 'Verso · 2005 · ISBN 9781844670260 · 119 页（据书评标示，◐）',
        'publines_en': 'Verso · 2005 · ISBN 9781844670260 · 119 pp (per review, ◐)',
        'baseline_conf': '✓ 版本核实（Verso 2005, ISBN 9781844670260）；页数 119 据 Forum for Modern Language Studies 书评（%s，◐）' % ACC,
        'baseline_conf_en': '✓ edition verified (Verso 2005, ISBN 9781844670260); 119 pp from a review in Forum for Modern Language Studies (%s, ◐)' % ACC,
        'ledger': [('《Graphs, Maps, Trees》Verso 2005 版共 119 页',
                    'The Verso 2005 edition of Graphs, Maps, Trees runs to 119 pages',
                    '书评, Forum for Modern Language Studies, 2006, DOI 10.1093/fmls/cql045',
                    'Review, Forum for Modern Language Studies, 2006, DOI 10.1093/fmls/cql045', '◐')],
        'drop': ['页数与具体印次'],
        'add_unverified': [('具体印次（页数已据书评补）', 'specific printing (pages now from a review)', '◐')],
    },
    'moretti-distant-reading': {
        'pages': '244',
        'publines_zh': 'Verso · 2013 · 平装 ISBN 9781781680841 · 244 页（据书评标示，◐）· 精装 9781781681121',
        'publines_en': 'Verso · 2013 · paper ISBN 9781781680841 · 244 pp (per review, ◐) · cloth 9781781681121',
        'baseline_conf': '✓ 版本核实（Verso 2013, ISBN 9781781680841）；页数 244 与精装 ISBN 据 Comparative Critical Studies 书评（%s，◐）' % ACC,
        'baseline_conf_en': '✓ edition verified (Verso 2013, ISBN 9781781680841); 244 pp and the cloth ISBN from a review in Comparative Critical Studies (%s, ◐)' % ACC,
        'ledger': [('《Distant Reading》Verso 2013 版共 244 页，平装 ISBN 9781781680841、精装 9781781681121',
                    'The Verso 2013 Distant Reading runs to 244 pages, paper ISBN 9781781680841 and cloth 9781781681121',
                    '书评, Comparative Critical Studies, 2013, DOI 10.3366/ccs.2013.0105',
                    'Review, Comparative Critical Studies, 2013, DOI 10.3366/ccs.2013.0105', '◐')],
        'drop': ['页数与所收篇目的完整清单'],
        'add_unverified': [('所收篇目的完整清单（页数已据书评补）', 'full contents (pages now from a review)', '◐')],
    },
    'moretti-bourgeois': {
        'pages': '203',
        'publines_zh': 'Verso · 2013 · ISBN 9781781680858 · 203 页（据书评标示；另有书评作 224 页，存疑）',
        'publines_en': 'Verso · 2013 · ISBN 9781781680858 · 203 pp (per one review; another gives 224 pp, unresolved)',
        'baseline_conf': '✓ 版本核实（Verso 2013, ISBN 9781781680858）；页数两处书评不一（203 / 224），暂记 203（%s，◐）' % ACC,
        'baseline_conf_en': '✓ edition verified (Verso 2013, ISBN 9781781680858); reviews disagree on length (203 vs 224 pp), 203 recorded pending check (%s, ◐)' % ACC,
        'ledger': [
            ('《The Bourgeois》Romance Quarterly 书评记 203 页',
             'A review in Romance Quarterly gives 203 pages for The Bourgeois',
             '书评, Romance Quarterly, 2014, DOI 10.1080/08831157.2014.937234',
             'Review, Romance Quarterly, 2014, DOI 10.1080/08831157.2014.937234', '◐'),
            ('《The Bourgeois》Germanic Review 书评记 224 页，与上条冲突',
             'A review in The Germanic Review gives 224 pages, conflicting with the above',
             '书评, The Germanic Review, 2015, DOI 10.1080/00168890.2015.1065164',
             'Review, The Germanic Review, 2015, DOI 10.1080/00168890.2015.1065164', '✗'),
        ],
        'drop': ['页数与关键词章节的完整清单'],
        'add_unverified': [('页数（两处书评不一）与关键词章节清单', 'page count (reviews disagree) and the keyword chapter list', '◐')],
    },
    'tsing-mushroom': {
        'pages': '331',
        'publines_zh': 'Princeton University Press · 2015 · 331 页（xii + 331，据多篇书评，◐）· ISBN 待核',
        'publines_en': 'Princeton University Press · 2015 · 331 pp (xii + 331, per several reviews, ◐) · ISBN pending',
        'baseline_conf': '◐ 出版社/年份经指南核实；页数 331 经多篇书评一致（American Ethnologist、Ethnobiology Letters、Green Letters，%s，◐）；ISBN 待核' % ACC,
        'baseline_conf_en': '◐ publisher/year via guide; 331 pp agreed by several reviews (American Ethnologist, Ethnobiology Letters, Green Letters, %s, ◐); ISBN pending' % ACC,
        'ledger': [
            ('《The Mushroom at the End of the World》Princeton 2015 版为 xii + 331 页',
             'The Princeton 2015 edition of The Mushroom at the End of the World is xii + 331 pages',
             '书评, American Ethnologist 2016; Ethnobiology Letters 2015; Green Letters 2017',
             'Reviews, American Ethnologist 2016; Ethnobiology Letters 2015; Green Letters 2017', '◐'),
            ('American Anthropologist 书评作 352 页，与多数书评的 331 页不一致',
             'A review in American Anthropologist gives 352 pages, inconsistent with the 331 pages reported elsewhere',
             '书评, American Anthropologist, 2016',
             'Review, American Anthropologist, 2016', '✗'),
        ],
        'drop': ['ISBN、页数与具体印次'],
        'add_unverified': [('ISBN 与具体印次（页数已据书评补）', 'ISBN and printing (pages now from reviews)', '◐')],
    },
    'escobar-encountering-development': {
        'pages': '290',
        'publines_zh': 'Princeton University Press · 1995（另有 2012 年新版附新序）· ix + 290 页（据书评，◐）· ISBN 待核',
        'publines_en': 'Princeton University Press · 1995 (2012 reissue with a new preface) · ix + 290 pp (per review, ◐) · ISBN pending',
        'baseline_conf': '◐ 出版社与年份经指南核实（1994/1995 并存）；页数 ix + 290 据 Journal of Asian Studies 书评（%s，◐）；ISBN 与版次待核' % ACC,
        'baseline_conf_en': '◐ publisher/year via guide (1994/1995 both appear); ix + 290 pp from a review in the Journal of Asian Studies (%s, ◐); ISBN and printing pending' % ACC,
        'ledger': [('《Encountering Development》Princeton 1995 版为 ix + 290 页',
                    'The Princeton 1995 edition of Encountering Development is ix + 290 pages',
                    '书评, The Journal of Asian Studies, 1995',
                    'Review, The Journal of Asian Studies, 1995', '◐')],
        'drop': [],
        'add_unverified': [('ISBN 与具体印次（页数已据书评补）', 'ISBN and printing (pages now from a review)', '◐')],
    },
    'parasecoli-knowing-where': {
        'publines_zh': 'University of Iowa Press · 2017 · ISBN 9781609385330（纸本）/ 9781609385347 · DOI 10.1353/book52838 · 页数待核',
        'publines_en': 'University of Iowa Press · 2017 · ISBN 9781609385330 (print) / 9781609385347 · DOI 10.1353/book52838 · pages pending',
        'baseline_conf': '◐ 2017 年 Iowa 版与两枚 ISBN 经 Crossref / Project MUSE 注册记录（%s）；装帧对应与页数待核' % ACC,
        'baseline_conf_en': '◐ 2017 Iowa edition and two ISBNs via Crossref / Project MUSE registration (%s); format mapping and pages pending' % ACC,
        'ledger': [('《Knowing Where It Comes From》2017 年由 University of Iowa Press 出版，注册 ISBN 9781609385347，DOI 10.1353/book52838',
                    'Knowing Where It Comes From was published by the University of Iowa Press in 2017; registered ISBN 9781609385347, DOI 10.1353/book52838',
                    'Crossref 10.1353/book52838',
                    'Crossref 10.1353/book52838', '◐')],
        'drop': ['ISBN/页数与目录'],
        'add_unverified': [('页数、装帧对应与目录（ISBN 已核）', 'page count, format mapping and contents (ISBNs verified)', '◐')],
    },
}

raw = io.open(PATH, encoding='utf-8').read()
doc = json.loads(raw)
by = {b['id']: b for b in doc['books']}

for bid, spec in DATA.items():
    b = by.get(bid)
    if b is None:
        raise SystemExit('missing book: ' + bid)
    for k in ('pages', 'publines_zh', 'publines_en', 'baseline_conf', 'baseline_conf_en'):
        if k in spec:
            b[k] = spec[k]
    ledger = b.get('fact_ledger') or []
    b['fact_ledger'] = ledger
    have = {e.get('claim') for e in ledger}
    for zh, en, s_zh, s_en, conf in spec['ledger']:
        if zh not in have:
            ledger.append({'claim': zh, 'claim_en': en, 'source': s_zh, 'source_en': s_en, 'conf': conf})
    unv = [u for u in (b.get('unverified') or []) if u.get('item') not in spec['drop']]
    for item, item_en, conf in spec['add_unverified']:
        unv.append({'item': item, 'item_en': item_en, 'conf': conf})
    b['unverified'] = unv
    print('updated', bid, '->', b['pages'])

io.open(PATH, 'w', encoding='utf-8', newline='\n').write(
    json.dumps(doc, ensure_ascii=False, indent=2) + '\n')
print('written')
