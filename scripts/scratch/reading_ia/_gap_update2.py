import json, io, collections

p = 'Reading_IA/web/data/site.json'
s = json.load(io.open(p, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)

for c in s['crops']:
    if c['id'] != '2026-games-play-culture':
        continue
    c['verdict_body_zh'] = c['verdict_body_zh'].replace(
        '核心书目事实经出版社/作者页核对', '核心书目事实部分经出版社/作者页核对')
    c['verdict_body_en'] = c['verdict_body_en'].replace(
        'Core facts checked against publishers and author pages',
        'Core facts partly checked against publishers and author pages')
    c['lang_line_zh'] = '英/意/瑞/丹 × 20 — 书目事实部分经出版社/作者页/馆藏核对；未见全文者标 ◐/○'
    c['lang_line_en'] = ('English / Italian / Swedish / Danish × 20 — bibliographic facts partly checked '
                         'against publishers, author pages and catalogues; unread items marked ◐/○')

io.open(p, 'w', encoding='utf-8', newline='\n').write(
    json.dumps(s, ensure_ascii=False, indent=2) + '\n')
print('ok')
