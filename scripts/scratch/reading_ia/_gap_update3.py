# -*- coding: utf-8 -*-
"""Refresh crop gap text after the imprint round."""
import io
import json

PATH = 'Reading_IA/web/data/site.json'
s = json.load(io.open(PATH, encoding='utf-8'))
crops = {c['id']: c for c in s['crops']}

ts = crops['2026-tsing-escobar']
ts['verdict_gaps'] = [
    {'zh': '多数书未通读；解读限于书目、指南与二手来源。',
     'en': 'Most books are unread; interpretation rests on bibliography, guide and secondary sources.'},
    {'zh': '书目事实部分核实：15 部中页数 8 部（4 部经出版社产品页、3 部据书评、1 部为期刊文章）、ISBN 5 部；Princeton 五部、西语原版与数字项目因产品页 403 或未见权威页，仍留 —。',
     'en': 'Bibliographic facts partly verified: pages for 8 of 15 titles (4 from publisher pages, 3 from reviews, 1 journal article) and ISBNs for 5; the five Princeton titles, the Spanish-language editions and the digital project remain — because product pages return 403 or no authoritative page was found.'},
    {'zh': '《Arts of Living on a Damaged Planet》出版社页记 2017-05-30（部分文献作 2016）；本档两说并存，未强行统一。',
     'en': 'The publisher page dates Arts of Living on a Damaged Planet to 2017-05-30 (some sources say 2016); both are recorded rather than forced into one.'},
    {'zh': 'Feral Atlas 是数字项目，不是纸质书；阅读依赖网络。',
     'en': 'Feral Atlas is a digital project, not a print book; reading depends on the network.'},
    {'zh': 'Escobar 的 58 条 Goodreads 条目经去重/筛选为 ~15 核心作；筛选标准见指南。',
     'en': "Escobar's 58 Goodreads entries were deduplicated/curated to ~15 core works; criteria in the guide."},
    {'zh': 'Goodreads 评分与评价数随时间变动，只作参考。',
     'en': 'Goodreads ratings and counts change over time; reference only.'},
]
ts['lang_line_zh'] = '英/西/法/葡 × 15 — 核心书目经 Goodreads 作者页、指南与出版社页/书评核对；未见全文者标 ◐/○'
ts['lang_line_en'] = 'English / Spanish / French / Portuguese × 15 — core facts checked against Goodreads author pages, the guide, and publisher pages/reviews; unread items marked ◐/○'
ts['verdict_body_zh'] = ('两作者十五书：Tsing 的边缘/摩擦/多物种/人类世，Escobar 的发展批判/领地/多元宇宙/关联性。'
                         '七组共享主题（发展批判、多元宇宙、关联性、领地、社会运动/自主设计、翻译、方法论）作为读轴；'
                         '书目事实已部分回出版社页与书评核对（页数 8 部、ISBN 5 部）；未见全文者一律 ◐/○。')
ts['verdict_body_en'] = ("Fifteen dossiers: Tsing's margin/friction/multispecies/Anthropocene and Escobar's development critique/"
                         'territory/pluriverse/relationality. Seven shared themes (development critique, pluriverse, relationality, '
                         'territory, movements/autonomous design, translation, method) serve as axes; bibliographic facts are now partly '
                         'checked against publisher pages and reviews (pages for 8 titles, ISBNs for 5); unread items marked ◐/○.')

gm = crops['2026-games-play-culture']
gm['verdict_gaps'] = [
    {'zh': '页数 12/20 已补：6 部经出版社产品页（Parasecoli 两书、Rusch、Appadurai、Gobet 两书），6 部据书评标示（Salen & Zimmerman 688、Juul 255、Mintz 274、Moretti 三书 119/244/203）；ISBN 19/20，仅 Mintz 缺。',
     'en': 'Pages supplied for 12 of 20: six from publisher pages (two Parasecoli titles, Rusch, Appadurai, two Gobet titles) and six from review citations (Salen & Zimmerman 688, Juul 255, Mintz 274, three Moretti titles at 119/244/203); ISBNs 19 of 20, only Mintz missing.'},
    {'zh': '目录只对 6 部给出（Moretti 两书、Salen & Zimmerman、Mintz、Appadurai、Gobet 普及版），且注明「未逐页核对」；其余 14 部未列目录。',
     'en': "Contents are given for only six titles (two Moretti books, Salen & Zimmerman, Mintz, Appadurai, the Gobet primer), each flagged 'not checked page by page'; the other fourteen have no table of contents."},
    {'zh': '20/20 均已补「章节读法卡」（plot_acts），但多为论旨重构（标 ◐），不是逐章摘要。',
     'en': 'All twenty dossiers now carry chapter-level reading cards (plot_acts), but most are reconstructed arguments marked ◐ rather than chapter-by-chapter summaries.'},
    {'zh': '本轮网络部分恢复：Duke、Columbia、Minnesota、UC Press、T&F 产品页可取；Princeton、MIT、Bloomsbury、Penguin 与 Verso 产品页仍 403/429，相关书目事实未能核实。',
     'en': 'The network partly recovered this round: Duke, Columbia, Minnesota, UC Press and T&F product pages were reachable; Princeton, MIT, Bloomsbury, Penguin and Verso product pages still return 403/429, so those facts remain unchecked.'},
    {'zh': '多数书未通读；相邻作品（Jockers/Underwood/Salen & Zimmerman/Bogost/Juul/Mintz/Appadurai/de Groot）用于语境，不替代四家核心。',
     'en': 'Most books are unread; adjacent works (Jockers, Underwood, Salen & Zimmerman, Bogost, Juul, Mintz, Appadurai, de Groot) supply context and do not replace the four core scholars.'},
]
gm['lang_line_zh'] = '英/意/瑞/丹 × 20 — 书目事实部分经出版社产品页与书评核对；未见全文者标 ◐/○'
gm['lang_line_en'] = 'English / Italian / Swedish / Danish × 20 — bibliographic facts partly checked against publisher pages and review citations; unread items marked ◐/○'
gm['verdict_body_zh'] = ('四圈二十书：尺度（Moretti 四书 + Jockers/Underwood）、意义（Rusch + Salen & Zimmerman/Bogost/Juul）、'
                         '身份（Parasecoli 四书 + Mintz/Appadurai）、专长（Gobet 三书 + de Groot）。'
                         '书目事实已部分回出版社页与书评核对（页数 12 部、ISBN 19 部）；未见全文者一律 ◐/○；'
                         '相邻作品是语境，不是核心。')
gm['verdict_body_en'] = ('Four rings, twenty dossiers: scale (four Moretti titles plus Jockers/Underwood), meaning (Rusch plus '
                         'Salen & Zimmerman/Bogost/Juul), identity (four Parasecoli titles plus Mintz/Appadurai), expertise (three Gobet '
                         'titles plus de Groot). Bibliographic facts are now partly checked against publisher pages and reviews (pages for '
                         '12 titles, ISBNs for 19); unread items marked ◐/○; adjacent works are context, not core.')

io.open(PATH, 'w', encoding='utf-8', newline='\n').write(
    json.dumps(s, ensure_ascii=False, indent=2) + '\n')
print('site.json updated')
