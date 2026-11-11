import json, io, collections, re

p = 'Reading_IA/web/data/books.json'
data = json.load(io.open(p, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
changed = 0


def walk(obj):
    global changed
    if isinstance(obj, str):
        if 'membership' in obj:
            return obj.replace('membership 的行政技术', '归属的行政技术')
        return obj
    if isinstance(obj, list):
        return [walk(x) for x in obj]
    if isinstance(obj, dict):
        return collections.OrderedDict((k, walk(v)) for k, v in obj.items())
    return obj


for i, b in enumerate(data['books']):
    before = json.dumps(b, ensure_ascii=False)
    data['books'][i] = walk(b)
    if json.dumps(data['books'][i], ensure_ascii=False) != before:
        changed += 1

io.open(p, 'w', encoding='utf-8', newline='\n').write(
    json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print('books touched:', changed)
