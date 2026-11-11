import json, io, collections

p = 'Reading_IA/web/data/site.json'
s = json.load(io.open(p, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)

for c in s['crops']:
    if c['id'] != '2026-games-play-culture':
        continue
    c['verdict_gaps'] = [
        {
            "zh": "页数全部待核（仅 Gobet《The Psychology of Chess》记 140 页）；ISBN 已核 8 部，余 12 部为 —。",
            "en": "Page counts pending throughout (only Gobet's The Psychology of Chess records 140 pages); ISBN verified for 8 titles, with the other 12 left as —."
        },
        {
            "zh": "目录只对 6 部给出（Moretti 两书、Salen & Zimmerman、Mintz、Appadurai、Gobet 普及版），且注明「未逐页核对」；其余 14 部未列目录。",
            "en": "Contents are given for only six titles (two Moretti books, Salen & Zimmerman, Mintz, Appadurai, the Gobet primer), each flagged 'not checked page by page'; the other fourteen have no table of contents."
        },
        {
            "zh": "20/20 均已补「章节读法卡」（plot_acts），但多为论旨重构（标 ◐），不是逐章摘要。",
            "en": "All twenty dossiers now carry chapter-level reading cards (plot_acts), but most are reconstructed arguments marked ◐ rather than chapter-by-chapter summaries."
        },
        {
            "zh": "本轮网络不可用，未能回出版社/馆藏复核，故书目事实维持原标注；恢复联网后应补 ISBN/页数并升为 ✓。",
            "en": "The network was unavailable this round, so publisher and catalogue records could not be re-checked and existing confidence marks stand; once online, ISBNs and page counts should be filled in and raised to ✓."
        },
        {
            "zh": "多数书未通读；相邻作品（Jockers/Underwood/Salen & Zimmerman/Bogost/Juul/Mintz/Appadurai/de Groot）用于语境，不替代四家核心。",
            "en": "Most books are unread; adjacent works (Jockers, Underwood, Salen & Zimmerman, Bogost, Juul, Mintz, Appadurai, de Groot) supply context and do not replace the four core scholars."
        }
    ]
    c['verdict_body_zh'] = c['verdict_body_zh'].rstrip('。') + "；本轮补入二十张章节读法卡，书目事实仍标 ◐ 以待联网复核。"
    c['verdict_body_en'] = c['verdict_body_en'].rstrip('.') + "; this round added twenty chapter-level reading cards, with bibliographic facts still marked ◐ pending an online check."

io.open(p, 'w', encoding='utf-8', newline='\n').write(
    json.dumps(s, ensure_ascii=False, indent=2) + '\n')
print('site.json updated')
