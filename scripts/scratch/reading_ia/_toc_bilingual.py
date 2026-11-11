import json, io, collections

p = 'Reading_IA/web/data/books.json'
data = json.load(io.open(p, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
books = {b['id']: b for b in data['books']}

EN = {
    'moretti-graphs-maps-trees': [
        [("图表", "Graphs")],
        [("地图", "Maps")],
        [("树", "Trees")],
    ],
    'tsing-mushroom': [
        [("导论：世界末日的菌菇", "Introduction")],
        [("注意的艺术", "Arts of Noticing"),
         ("污染作为协作", "Contamination as Collaboration"),
         ("尺度的一些问题", "Some Problems with Scale")],
        [("在边缘劳作", "Working the Edge"),
         ("开放的车票，开放的问题", "Open Ticket, Open Question"),
         ("价格是什么？", "What Is a Price?")],
        [("森林的生命", "The Life of the Forest"),
         ("公共领域的泥泞", "Mud in the Public Domain"),
         ("拾荒式积累", "Salvage Accumulation")],
        [("菌菇的馈赠", "Mushroom Gifts"),
         ("菌菇热潮", "Mushroom Boom"),
         ("最后一口？", "Last Bite?")],
        [("当下的废墟", "The Ruins of the Present"),
         ("生活的艺术", "Arts of Living")],
    ],
    'escobar-encountering-development': [
        [("导论：发展与现代性的人类学", "Introduction: Development and the Anthropology of Modernity")],
        [("贫困的问题化：三个世界与发展故事", "The Problematization of Poverty: The Tale of Three Worlds and Development"),
         ("经济学与发展的空间：增长与资本的故事", "Economics and the Space of Development: Tales of Growth and Capital"),
         ("权力的散布：粮食与饥饿的故事", "The Dispersion of Power: Tales of Food and Hunger")],
        [("第三世界的建构与解构", "The Making and Unmaking of the Third World"),
         ("结论：想象一个后发展时代", "Conclusion: Imagining a Postdevelopment Era")],
    ],
}

for bid, groups in EN.items():
    t = books[bid]['toc']
    assert len(t['groups']) == len(groups), (bid, len(t['groups']), len(groups))
    for g, pairs in zip(t['groups'], groups):
        assert len(g['items']) == len(pairs), (bid, g['items'], pairs)
        g['items'] = [collections.OrderedDict([("zh", zh), ("en", en)]) for zh, en in pairs]

books['moretti-bourgeois']['background']['en'] = books['moretti-bourgeois']['background']['en'].replace(
    'keywords supply conceptual线索, prose supplies the formal landing',
    'keywords supply conceptual threads, prose supplies the formal landing')

io.open(p, 'w', encoding='utf-8', newline='\n').write(
    json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print('books.json toc items localised')
