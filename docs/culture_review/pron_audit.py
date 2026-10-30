# -*- coding: utf-8 -*-
"""Pronunciation audit for the zh read-aloud cues.

G2P the cue sentences with pypinyin (sentence mode), flag every polyphone
context, and group the output by word so a human can compare 期望读音 vs
默认读音. Reads _audio_sentences.json (the same cues build_audio.py renders).

    uv run --python 3.11 --with pypinyin python pron_audit.py > _pron_report.txt

Output sections:
  A. polyphone hits - char, its pinyin in this context, the phrase around it
  B. proper-noun / transliteration watchlist - curated terms from this issue
  C. digit/latin spans - places where TTS reads numbers/letters itself
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

from pypinyin import Style, pinyin, load_phrases_dict
from pypinyin.contrib.tone_convert import to_tone

HERE = Path(__file__).resolve().parent
DUMP = HERE / "_audio_sentences.json"

# chars whose reading depends on the word - the classic 多音字 set plus the
# ones this issue's text actually turns up (verified against 现代汉语词典)
POLYPHONES = set(
    "为长单朝宿没摩塞卡磨着了难盛数调处干场杆道都度乐剧少老好行相供帖"
    "片系旋压咽应与语扎涨中种转重得地率传还卡壳教任令似扫丧厦县背屏"
    "强悄切塞什适合瘦谈壳地圈圈和觉会"
)

# curated watchlist: proper nouns, transliterations, stage-art terms of this issue
WATCH = [
    "朝阳公园", "大歌剧院", "拉各斯", "内罗毕", "基贝拉", "釜山", "水立方",
    "国家游泳中心", "张艺谋", "吕其明", "红旗颂", "卡塔赫纳", "哈瓦那",
    "迈阿密", "阿拉伯小说国际奖", "布克", "凯西", " Said Khatibi", "长名单",
    "短名单", "新潮流", "单元", "展演季", "剧目", "唱作", "音乐剧", "咏剧",
    "话剧", "戏曲", "京剧", "昆曲", "皮黄", "西皮", "二黄",
    "拉各斯", "双年展", "艺文", "馆", "开幕", "启幕", "首演",
]

DIGIT_SPAN = re.compile(r"[0-9]+[·.–-][0-9]+|[0-9]+|《[^》]+》|[A-Za-z][A-Za-z0-9.'’&-]*")


def ctx(text, i, w=6):
    return text[max(0, i - w): i + w + 1]


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "-o":
        sys.stdout = open(sys.argv[2], "w", encoding="utf-8")
    data = json.loads(DUMP.read_text(encoding="utf-8"))
    rows = data["zh"]
    print("# pron_audit: %d zh cues, %d chars" % (len(rows), sum(len(r["text"]) for r in rows)))
    print()

    poly_counter = Counter()
    poly_hits = []
    watch_hits = []
    digit_hits = []

    seen_phrase = set()
    for r in rows:
        t = r["text"]
        py = pinyin(t, style=Style.TONE3, heteronym=True, errors=lambda x: list(x))
        flat = [p[0] for p in py]
        for i, ch in enumerate(t):
            if ch in POLYPHONES and re.match(r"[\u4e00-\u9fff]", ch):
                alts = pinyin(ch, style=Style.TONE3, heteronym=True)[0]
                if len(alts) > 1:
                    here = flat[i] if i < len(flat) else "?"
                    # only interesting when the context reading is one of several
                    phrase = ctx(t, i)
                    key = (ch, here, phrase)
                    if key not in seen_phrase:
                        seen_phrase.add(key)
                        poly_counter[(ch, here)] += 1
                        poly_hits.append((r["sec"], ch, here, sorted(alts), phrase))
        for w_ in WATCH:
            w2 = w_.strip()
            if w2 and w2 in t:
                i = t.find(w2)
                wp = pinyin(w2, style=Style.TONE)
                watch_hits.append((r["sec"], w2, "".join(x[0] for x in wp), ctx(t, i, 10)))
        for m in DIGIT_SPAN.finditer(t):
            digit_hits.append((r["sec"], m.group(0)))

    print("## A. polyphone contexts (char / G2P reading / all readings / context)")
    for sec, ch, here, alts, phrase in poly_hits:
        print("  [%s] %s -> %s  (alts %s)  …%s…" % (sec, ch, here, ",".join(alts), phrase))
    print()

    # the top-risk view: same char read differently in different contexts
    print("## A2. chars read multiple ways across the issue")
    by_char = {}
    for sec, ch, here, alts, phrase in poly_hits:
        by_char.setdefault(ch, set()).add(here)
    for ch, reads in sorted(by_char.items()):
        if len(reads) > 1:
            print("  %s: %s" % (ch, sorted(reads)))
    print()

    print("## B. watchlist terms (intended pinyin per pypinyin)")
    seen = set()
    for sec, w2, py, phrase in watch_hits:
        if (w2, py) not in seen:
            seen.add((w2, py))
            print("  %s = %s   …%s…" % (w2, py, phrase))
    print()

    print("## C. digit / latin / title spans the TTS reads on its own")
    seen = set()
    for sec, span in digit_hits:
        if span not in seen:
            seen.add(span)
            print("  [%s] %s" % (sec, span))


if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    main()
