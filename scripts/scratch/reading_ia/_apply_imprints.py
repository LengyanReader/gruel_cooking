# -*- coding: utf-8 -*-
"""Write verified imprint data for 8 books back into books.json.

Sources (accessed 2026-11-11):
  - Columbia UP product page  : https://cup.columbia.edu/book/x/9780231202077
  - Duke UP product pages     : /territories-of-difference, /designs-for-the-pluriverse,
                                /pluriversal-politics
  - U Minnesota Press page    : /book-division/books/modernity-at-large
  - T&F product page (JSON-LD): 10.1201/9781315748986, 10.4324/9780203503638
  - Crossref                  : 10.1515/9783110800647 (degroot, 1978 De Gruyter ed.)
"""
import io
import json

PATH = 'Reading_IA/web/data/books.json'
ACC = '2026-11-11'

DATA = {
    'parasecoli-gastronativism': {
        'pubdate': '2022-07',
        'pubdate_en': '2022-07 (Columbia University Press)',
        'pages': '248',
        'isbn': '9780231202077',
        'publines_zh': 'Columbia University Press · 2022-07 · 平装 ISBN 9780231202077 · 248 页',
        'publines_en': 'Columbia University Press · 2022-07 · paper ISBN 9780231202077 · 248 pp',
        'baseline_conf': '✓ 版本、ISBN 与页数核实（Columbia UP 产品页，%s）' % ACC,
        'baseline_conf_en': '✓ edition, ISBN and pages verified (Columbia UP product page, %s)' % ACC,
        'ledger': [
            ('《Gastronativism》2022 年 7 月由 Columbia University Press 出版，平装 248 页',
             'Gastronativism was published by Columbia University Press in July 2022, 248 pp. in paper',
             'Columbia UP 产品页 https://cup.columbia.edu/book/x/9780231202077',
             'Columbia UP product page https://cup.columbia.edu/book/x/9780231202077'),
        ],
        'drop': ['页数与具体案例清单'],
        'add_unverified': [
            ('具体案例清单与各章标题', 'list of cases and chapter titles', '◐'),
        ],
    },
    'escobar-territories-difference': {
        'pubdate': '2008-11',
        'pubdate_en': '2008-11 (Duke University Press)',
        'pages': '456',
        'isbn': '9780822343271',
        'publines_zh': 'Duke University Press · 2008-11 · 平装 ISBN 9780822343271 · 456 页 · DOI 10.1215/9780822389439',
        'publines_en': 'Duke University Press · 2008-11 · paper ISBN 9780822343271 · 456 pp · DOI 10.1215/9780822389439',
        'baseline_conf': '✓ 版本、ISBN 与页数核实（Duke UP 产品页，%s）' % ACC,
        'baseline_conf_en': '✓ edition, ISBN and pages verified (Duke UP product page, %s)' % ACC,
        'ledger': [
            ('《Territories of Difference》2008 年 11 月由 Duke University Press 出版，平装 456 页，属 “New Ecologies for the Twenty-First Century” 丛书',
             'Territories of Difference was published by Duke University Press in November 2008, 456 pp., in the series “New Ecologies for the Twenty-First Century”',
             'Duke UP 产品页 https://dukeupress.edu/territories-of-difference',
             'Duke UP product page https://dukeupress.edu/territories-of-difference'),
        ],
        'drop': ['ISBN、页数与具体印次'],
        'add_unverified': [],
    },
    'escobar-designs-pluriverse': {
        'pubdate': '2018-03',
        'pubdate_en': '2018-03 (Duke University Press)',
        'pages': '312',
        'isbn': '9780822371052',
        'publines_zh': 'Duke University Press · 2018-03 · 平装 ISBN 9780822371052 · 312 页',
        'publines_en': 'Duke University Press · 2018-03 · paper ISBN 9780822371052 · 312 pp',
        'baseline_conf': '✓ 版本、ISBN 与页数核实（Duke UP 产品页，%s）' % ACC,
        'baseline_conf_en': '✓ edition, ISBN and pages verified (Duke UP product page, %s)' % ACC,
        'ledger': [
            ('《Designs for the Pluriverse》2018 年 3 月由 Duke University Press 出版，平装 312 页',
             'Designs for the Pluriverse was published by Duke University Press in March 2018, 312 pp. in paper',
             'Duke UP 产品页 https://dukeupress.edu/designs-for-the-pluriverse',
             'Duke UP product page https://dukeupress.edu/designs-for-the-pluriverse'),
        ],
        'drop': ['ISBN、页数与具体印次'],
        'add_unverified': [],
    },
    'escobar-pluriversal-politics': {
        'pubdate': '2020-04',
        'pubdate_en': '2020-04 (Duke University Press)',
        'pages': '232',
        'isbn': '9781478008460',
        'publines_zh': 'Duke University Press · 2020-04 · 平装 ISBN 9781478008460 · 232 页 · DOI 10.1215/9781478012108',
        'publines_en': 'Duke University Press · 2020-04 · paper ISBN 9781478008460 · 232 pp · DOI 10.1215/9781478012108',
        'baseline_conf': '✓ 版本、ISBN 与页数核实（Duke UP 产品页，%s）；译者与原篇出处待核' % ACC,
        'baseline_conf_en': '✓ edition, ISBN and pages verified (Duke UP product page, %s); translator and original venues pending' % ACC,
        'ledger': [
            ('《Pluriversal Politics》2020 年 4 月由 Duke University Press 出版，平装 232 页，属 “Latin America in Translation” 丛书',
             'Pluriversal Politics was published by Duke University Press in April 2020, 232 pp., in the “Latin America in Translation” series',
             'Duke UP 产品页 https://dukeupress.edu/pluriversal-politics',
             'Duke UP product page https://dukeupress.edu/pluriversal-politics'),
        ],
        'drop': ['ISBN、页数与译者'],
        'add_unverified': [
            ('译者与原篇出处（ISBN/页数已核）', 'translator and original venues (ISBN/pages now verified)', '◐'),
        ],
    },
    'appadurai-modernity-large': {
        'pubdate': '1996',
        'pubdate_en': '1996 (University of Minnesota Press)',
        'pages': '248',
        'isbn': '9780816627936',
        'publines_zh': 'University of Minnesota Press · 1996 · 平装 ISBN 9780816627936 · 248 页',
        'publines_en': 'University of Minnesota Press · 1996 · paper ISBN 9780816627936 · 248 pp',
        'baseline_conf': '✓ 版本、ISBN 与页数核实（U Minnesota Press 产品页，%s）' % ACC,
        'baseline_conf_en': '✓ edition, ISBN and pages verified (U Minnesota Press product page, %s)' % ACC,
        'ledger': [
            ('《Modernity at Large》1996 年由 University of Minnesota Press 出版，平装 248 页',
             'Modernity at Large was published by the University of Minnesota Press in 1996, 248 pp. in paper',
             'U Minnesota Press 产品页 https://www.upress.umn.edu/book-division/books/modernity-at-large',
             'U Minnesota Press product page https://www.upress.umn.edu/book-division/books/modernity-at-large'),
        ],
        'drop': ['ISBN、页数与版次'],
        'add_unverified': [
            ('具体印次与后续重印年份', 'specific printing and later reprint years', '◐'),
        ],
    },
    'rusch-making-deep-games': {
        'pubdate': '2017-01-12',
        'pubdate_en': '2017-01-12 (Routledge)',
        'pages': '228',
        'isbn': '9781315748986',
        'publines_zh': 'Routledge · 2017-01-12 · 电子版 ISBN 9781315748986 · 228 页 · DOI 10.1201/9781315748986',
        'publines_en': 'Routledge · 2017-01-12 · e-book ISBN 9781315748986 · 228 pp · DOI 10.1201/9781315748986',
        'baseline_conf': '✓ 出版日、页数与电子版 ISBN 核实（T&F 产品页 JSON-LD，%s）；平装 ISBN 待核' % ACC,
        'baseline_conf_en': '✓ date, pages and e-book ISBN verified (T&F product page JSON-LD, %s); paper ISBN pending' % ACC,
        'ledger': [
            ('《Making Deep Games》2017 年 1 月 12 日由 Routledge 出版，228 页，DOI 10.1201/9781315748986',
             'Making Deep Games was published by Routledge on 12 January 2017, 228 pp., DOI 10.1201/9781315748986',
             'T&F 产品页 https://www.taylorfrancis.com/books/mono/10.1201/9781315748986/making-deep-games-doris-rusch',
             'T&F product page https://www.taylorfrancis.com/books/mono/10.1201/9781315748986/making-deep-games-doris-rusch'),
        ],
        'drop': ['ISBN、页数与完整目录'],
        'add_unverified': [
            ('平装 ISBN 与完整目录（页数已核）', 'paper ISBN and full contents (pages now verified)', '◐'),
        ],
    },
    'gobet-moves-in-mind': {
        'pubdate': '2004-08-05',
        'pubdate_en': '2004-08-05 (Psychology Press)',
        'pages': '288',
        'isbn': '1841693367',
        'publines_zh': 'Psychology Press · 2004-08-05 · 平装 ISBN 1-84169-336-7 · 288 页 · e-ISBN 9780203503638',
        'publines_en': 'Psychology Press · 2004-08-05 · paper ISBN 1-84169-336-7 · 288 pp · e-ISBN 9780203503638',
        'baseline_conf': '✓ 出版日、页数与电子版 ISBN 核实（T&F 产品页 + Crossref，%s）' % ACC,
        'baseline_conf_en': '✓ date, pages and e-book ISBN verified (T&F product page + Crossref, %s)' % ACC,
        'ledger': [
            ('《Moves in Mind》2004 年 8 月 5 日由 Psychology Press 出版，288 页，DOI 10.4324/9780203503638',
             'Moves in Mind was published by Psychology Press on 5 August 2004, 288 pp., DOI 10.4324/9780203503638',
             'T&F 产品页 https://www.taylorfrancis.com/books/mono/10.4324/9780203503638/moves-mind-gobet-de-voogt-retschitzki',
             'T&F product page https://www.taylorfrancis.com/books/mono/10.4324/9780203503638/moves-mind-gobet-de-voogt-retschitzki'),
        ],
        'drop': ['页数与所比较游戏清单'],
        'add_unverified': [
            ('所比较游戏的完整清单（页数已核）', 'full list of games compared (pages now verified)', '◐'),
        ],
    },
    'degroot-thought-choice': {
        'pubdate': '1965',
        'pubdate_en': '1965 English trans. (Mouton); 1978 De Gruyter ed.',
        'pages': '—',
        'isbn': '9789027979148',
        'publines_zh': 'Mouton · 1965 英译（1946 荷兰文原版）· 1978 De Gruyter 版 ISBN 9789027979148 · DOI 10.1515/9783110800647 · 页数待核',
        'publines_en': 'Mouton · 1965 English trans. (Dutch original 1946) · 1978 De Gruyter ed. ISBN 9789027979148 · DOI 10.1515/9783110800647 · pages pending',
        'baseline_conf': '◐ 1965 英译沿革经 chessprogramming；1978 De Gruyter 版 ISBN/DOI 经 Crossref（%s）；页数待核' % ACC,
        'baseline_conf_en': '◐ 1965 translation history via chessprogramming; 1978 De Gruyter ISBN/DOI via Crossref (%s); pages pending' % ACC,
        'ledger': [
            ('1978 年 De Gruyter（Mouton）版《Thought and Choice in Chess》ISBN 为 9789027979148，DOI 10.1515/9783110800647',
             'The 1978 De Gruyter (Mouton) edition of Thought and Choice in Chess carries ISBN 9789027979148 and DOI 10.1515/9783110800647',
             'Crossref 10.1515/9783110800647',
             'Crossref 10.1515/9783110800647'),
        ],
        'drop': ['英译本 ISBN、页数与版次'],
        'add_unverified': [
            ('英译本页数，及 1965 初版与 1978 版次的关系', 'page count of the English translation, and the relation between the 1965 first printing and the 1978 edition', '◐'),
        ],
    },
}

raw = io.open(PATH, encoding='utf-8').read()
doc = json.loads(raw)
books = doc['books']
by_id = {b['id']: b for b in books}

changed = []
for bid, spec in DATA.items():
    b = by_id.get(bid)
    if b is None:
        raise SystemExit('missing book: ' + bid)
    for k in ('pubdate', 'pubdate_en', 'pages', 'isbn', 'publines_zh', 'publines_en',
              'baseline_conf', 'baseline_conf_en'):
        b[k] = spec[k]
    ledger = b.get('fact_ledger')
    if ledger is None:
        ledger = b['fact_ledger'] = []
    existing = {e.get('claim') for e in ledger}
    for zh, en, s_zh, s_en in spec['ledger']:
        if zh in existing:
            continue
        ledger.append({'claim': zh, 'claim_en': en,
                       'source': s_zh, 'source_en': s_en, 'conf': '✓'})
    unv = [u for u in (b.get('unverified') or []) if u.get('item') not in spec['drop']]
    for item, item_en, conf in spec['add_unverified']:
        unv.append({'item': item, 'item_en': item_en, 'conf': conf})
    b['unverified'] = unv
    changed.append(bid)

out = json.dumps(doc, ensure_ascii=False, indent=2) + '\n'
io.open(PATH, 'w', encoding='utf-8', newline='\n').write(out)
print('updated', len(changed))
for c in changed:
    print(' -', c)
