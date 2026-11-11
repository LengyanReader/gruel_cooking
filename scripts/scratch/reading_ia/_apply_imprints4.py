# -*- coding: utf-8 -*-
"""Batch 4: Diamond Queen pages (review) + Bogost e-ISBN/DOI (Crossref)."""
import io
import json

PATH = 'Reading_IA/web/data/books.json'
ACC = '2026-11-11'

DATA = {
    'tsing-diamond-queen': {
        'pages': '350',
        'publines_zh': 'Princeton University Press · 1993 · xvi + 350 页（据书评，◐）· ISBN 待核',
        'publines_en': 'Princeton University Press · 1993 · xvi + 350 pp (per review, ◐) · ISBN pending',
        'baseline_conf': '◐ 出版社与年份经指南核实；页数 xvi + 350 据 Journal of Asian Studies 书评（%s，◐）；ISBN 待核' % ACC,
        'baseline_conf_en': '◐ publisher/year via guide; xvi + 350 pp from a review in the Journal of Asian Studies (%s, ◐); ISBN pending' % ACC,
        'ledger': [('《In the Realm of the Diamond Queen》Princeton 1993 版为 xvi + 350 页',
                    'The Princeton 1993 edition of In the Realm of the Diamond Queen is xvi + 350 pages',
                    '书评, The Journal of Asian Studies, 1994',
                    'Review, The Journal of Asian Studies, 1994', '◐')],
        'drop': ['ISBN、页数与具体印次'],
        'add_unverified': [('ISBN 与具体印次（页数已据书评补）', 'ISBN and printing (pages now from a review)', '◐')],
    },
    'bogost-persuasive-games': {
        'publines_zh': 'MIT Press · 2007 · 精装 ISBN 9780262026147 · e-ISBN 9780262268912 · DOI 10.7551/mitpress/5334.001.0001 · 页数待核',
        'publines_en': 'MIT Press · 2007 · cloth ISBN 9780262026147 · e-ISBN 9780262268912 · DOI 10.7551/mitpress/5334.001.0001 · pages pending',
        'baseline_conf': '✓ 版本核实（MIT Press 2007, ISBN 9780262026147）；电子版 ISBN 与 DOI 经 Crossref（%s）；页数待核' % ACC,
        'baseline_conf_en': '✓ edition verified (MIT Press 2007, ISBN 9780262026147); e-ISBN and DOI via Crossref (%s); pages pending' % ACC,
        'ledger': [('《Persuasive Games》的 MIT Press 电子版 ISBN 为 9780262268912，DOI 10.7551/mitpress/5334.001.0001',
                    'The MIT Press e-book of Persuasive Games carries ISBN 9780262268912 and DOI 10.7551/mitpress/5334.001.0001',
                    'Crossref 10.7551/mitpress/5334.001.0001',
                    'Crossref 10.7551/mitpress/5334.001.0001', '✓')],
        'drop': [],
        'add_unverified': [],
    },
}

raw = io.open(PATH, encoding='utf-8').read()
doc = json.loads(raw)
by = {b['id']: b for b in doc['books']}
for bid, spec in DATA.items():
    b = by[bid]
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
    print('updated', bid)

io.open(PATH, 'w', encoding='utf-8', newline='\n').write(
    json.dumps(doc, ensure_ascii=False, indent=2) + '\n')
print('written')
