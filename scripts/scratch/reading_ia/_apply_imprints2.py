# -*- coding: utf-8 -*-
"""Batch 2 of verified imprint data (accessed 2026-11-11).

Sources:
  - UC Press product page  : https://www.ucpress.edu/books/the-pierogi-problem/paper
  - U Minnesota Press page : /book-division/books/arts-of-living-on-a-damaged-planet
  - Crossref               : 10.5406/illinois/9780252037528.001.0001 (Jockers)
                             10.7208/chicago/9780226612973.001.0001 (Underwood)
"""
import io
import json

PATH = 'Reading_IA/web/data/books.json'
ACC = '2026-11-11'

DATA = {
    'parasecoli-pierogi-problem': {
        'pubdate': '2025-08',
        'pubdate_en': '2025-08 (University of California Press)',
        'pages': '260',
        'isbn': '9780520399068',
        'publines_zh': 'University of California Press · 2025-08 · 平装 ISBN 9780520399068 · 260 页 · 丛书 California Studies in Food and Culture',
        'publines_en': 'University of California Press · 2025-08 · paper ISBN 9780520399068 · 260 pp · series California Studies in Food and Culture',
        'baseline_conf': '✓ 版本、ISBN 与页数核实（UC Press 产品页，%s）' % ACC,
        'baseline_conf_en': '✓ edition, ISBN and pages verified (UC Press product page, %s)' % ACC,
        'ledger': [
            ('《The Pierogi Problem》2025 年 8 月由 University of California Press 出版，平装 260 页，属 “California Studies in Food and Culture” 丛书；合著者含 Agata Bachórz',
             'The Pierogi Problem was published by the University of California Press in August 2025, 260 pp. in paper, in the “California Studies in Food and Culture” series; co-authors include Agata Bachórz',
             'UC Press 产品页 https://www.ucpress.edu/books/the-pierogi-problem/paper',
             'UC Press product page https://www.ucpress.edu/books/the-pierogi-problem/paper'),
        ],
        'drop': ['ISBN、页数与目录'],
        'add_unverified': [
            ('目录与各章标题（ISBN/页数已核）', 'contents and chapter titles (ISBN/pages now verified)', '◐'),
        ],
    },
    'tsing-arts-living': {
        'pubdate': '2017-05-30',
        'pubdate_en': '2017-05-30 (University of Minnesota Press; some sources cite 2016)',
        'pages': '368',
        'isbn': '9781517902377',
        'publines_zh': 'University of Minnesota Press · 2017-05-30（部分文献引作 2016）· 平装 ISBN 9781517902377 · 368 页 · e-ISBN 9781452954493',
        'publines_en': 'University of Minnesota Press · 2017-05-30 (some sources cite 2016) · paper ISBN 9781517902377 · 368 pp · e-ISBN 9781452954493',
        'baseline_conf': '✓ 出版日、ISBN 与页数核实（U Minnesota Press 产品页，%s）' % ACC,
        'baseline_conf_en': '✓ date, ISBN and pages verified (U Minnesota Press product page, %s)' % ACC,
        'ledger': [
            ('《Arts of Living on a Damaged Planet》出版社页记 2017 年 5 月 30 日出版，平装 368 页，ISBN 9781517902377（电子版 9781452954493）',
             'The publisher page gives 30 May 2017 for Arts of Living on a Damaged Planet, 368 pp. in paper, ISBN 9781517902377 (e-book 9781452954493)',
             'U Minnesota Press 产品页 https://www.upress.umn.edu/book-division/books/arts-of-living-on-a-damaged-planet',
             'U Minnesota Press product page https://www.upress.umn.edu/book-division/books/arts-of-living-on-a-damaged-planet'),
        ],
        'drop': [],
        'add_unverified': [
            ('各篇（ghosts/monsters 两组）的完整篇目与页码', 'full list of contributions (ghosts/monsters) with page numbers', '◐'),
        ],
    },
    'jockers-macroanalysis': {
        'pubdate': '2013-04',
        'pubdate_en': '2013-04 (University of Illinois Press)',
        'pages': '—',
        'isbn': '9780252037528 · 9780252094767',
        'publines_zh': 'University of Illinois Press · 2013-04 · ISBN 9780252037528（纸本）/ 9780252094767（电子版）· 页数待核 · DOI 10.5406/illinois/9780252037528.001.0001',
        'publines_en': 'University of Illinois Press · 2013-04 · ISBN 9780252037528 (print) / 9780252094767 (e-book) · pages pending · DOI 10.5406/illinois/9780252037528.001.0001',
        'baseline_conf': '◐ 出版年、出版社与两枚 ISBN 经 Crossref（%s）；装帧对应与页数待核' % ACC,
        'baseline_conf_en': '◐ year, publisher and two ISBNs via Crossref (%s); format mapping and pages pending' % ACC,
        'ledger': [
            ('《Macroanalysis》2013 年 4 月由 University of Illinois Press 出版，注册 ISBN 为 9780252037528 与 9780252094767，DOI 10.5406/illinois/9780252037528.001.0001',
             'Macroanalysis was published by the University of Illinois Press in April 2013; registered ISBNs are 9780252037528 and 9780252094767, DOI 10.5406/illinois/9780252037528.001.0001',
             'Crossref 10.5406/illinois/9780252037528.001.0001',
             'Crossref 10.5406/illinois/9780252037528.001.0001'),
        ],
        'drop': ['ISBN/页数与目录'],
        'add_unverified': [
            ('页数、装帧对应与目录（ISBN 已核）', 'page count, format mapping and contents (ISBNs verified)', '◐'),
        ],
    },
    'underwood-distant-horizons': {
        'pubdate': '2019',
        'pubdate_en': '2019 (University of Chicago Press)',
        'pages': '—',
        'isbn': '9780226612836 · 9780226612669 · 9780226612973',
        'publines_zh': 'University of Chicago Press · 2019 · ISBN 9780226612836 / 9780226612669 / 9780226612973（三种装帧未分辨）· 页数待核 · DOI 10.7208/chicago/9780226612973.001.0001',
        'publines_en': 'University of Chicago Press · 2019 · ISBN 9780226612836 / 9780226612669 / 9780226612973 (formats not distinguished) · pages pending · DOI 10.7208/chicago/9780226612973.001.0001',
        'baseline_conf': '◐ 出版年、出版社与三枚 ISBN 经 Crossref（%s）；装帧对应与页数待核' % ACC,
        'baseline_conf_en': '◐ year, publisher and three ISBNs via Crossref (%s); format mapping and pages pending' % ACC,
        'ledger': [
            ('《Distant Horizons》2019 年由 University of Chicago Press 出版，注册 ISBN 为 9780226612836、9780226612669 与 9780226612973，DOI 10.7208/chicago/9780226612973.001.0001',
             'Distant Horizons was published by the University of Chicago Press in 2019; registered ISBNs are 9780226612836, 9780226612669 and 9780226612973, DOI 10.7208/chicago/9780226612973.001.0001',
             'Crossref 10.7208/chicago/9780226612973.001.0001',
             'Crossref 10.7208/chicago/9780226612973.001.0001'),
        ],
        'drop': ['ISBN/页数与目录'],
        'add_unverified': [
            ('页数、装帧对应与目录（ISBN 已核）', 'page count, format mapping and contents (ISBNs verified)', '◐'),
        ],
    },
}

raw = io.open(PATH, encoding='utf-8').read()
doc = json.loads(raw)
by = {b['id']: b for b in doc['books']}

for bid, spec in DATA.items():
    b = by.get(bid)
    if b is None:
        raise SystemExit('missing book: ' + bid)
    for k in ('pubdate', 'pubdate_en', 'pages', 'isbn', 'publines_zh', 'publines_en',
              'baseline_conf', 'baseline_conf_en'):
        b[k] = spec[k]
    ledger = b.get('fact_ledger') or []
    b['fact_ledger'] = ledger
    have = {e.get('claim') for e in ledger}
    for zh, en, s_zh, s_en in spec['ledger']:
        if zh not in have:
            ledger.append({'claim': zh, 'claim_en': en, 'source': s_zh, 'source_en': s_en, 'conf': '✓'})
    unv = [u for u in (b.get('unverified') or []) if u.get('item') not in spec['drop']]
    for item, item_en, conf in spec['add_unverified']:
        unv.append({'item': item, 'item_en': item_en, 'conf': conf})
    b['unverified'] = unv
    print('updated', bid)

io.open(PATH, 'w', encoding='utf-8', newline='\n').write(
    json.dumps(doc, ensure_ascii=False, indent=2) + '\n')
print('written')
