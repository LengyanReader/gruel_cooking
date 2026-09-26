# -*- coding: utf-8 -*-
"""Ground-truth EN-view leak check (HTMLParser edition).
Emulates `body.lang-en`: the CSS hides [data-zh] at ANY DOM depth (incl. nested
inside another [data-zh] or inside SVG), so we parse properly and skip every
[data-zh] subtree, plus the 中 side of the language toggle and class="quote-src"
(source-language quotations whose translation is given inline).
Remaining Hanzi = a real zh↔en parity leak. Japanese primary material (kana
present) is exempt: it is source language, not Chinese editorial text."""
import io, re, glob, html
from html.parser import HTMLParser

HAN = re.compile(r"[\u4e00-\u9fff]")
KANA = re.compile(r"[\u3040-\u30ff]")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}


class EnView(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_body = False
        self.stack = []          # open tags inside hidden subtrees
        self.hits = []           # (lineno, text)

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.in_body = True
        if not self.in_body or tag in VOID:
            return
        if self.stack:
            self.stack.append(tag)   # child of a hidden subtree
            return
        a = dict(attrs)
        if (tag in ("script", "style") or "data-zh" in a
                or (tag == "button" and a.get("data-lang") == "zh")
                or "quote-src" in (a.get("class") or "")):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_data(self, data):
        if self.in_body and not self.stack and HAN.search(data):
            ln, _ = self.getpos()
            self.hits.append((ln, data.strip()))


total = 0
rep = io.open("_leak_report.txt", "w", encoding="utf-8")
def emit(*a):
    line = " ".join(str(x) for x in a)
    print(line); rep.write(line + "\n")
for path in sorted(glob.glob("../docs/reading_ia/**/*.html", recursive=True)):
    src = io.open(path, encoding="utf-8").read()
    p = EnView()
    p.feed(src)
    # merge adjacent text runs into display lines, dedupe, exempt kana
    hits, seen = [], set()
    for ln, text in p.hits:
        for piece in text.splitlines():
            piece = piece.strip()
            if not piece or not HAN.search(piece) or KANA.search(piece):
                continue
            if piece in seen:
                continue
            seen.add(piece)
            hits.append((ln, piece))
    if hits:
        total += len(hits)
        emit("\n#### " + path + "  (" + str(len(hits)) + " hanzi lines in EN view)")
        for ln, h in hits:
            emit("    L%-5d %s" % (ln, h[:110]))
emit("\nTOTAL EN-VIEW HANZI LINES:", total)
rep.close()
