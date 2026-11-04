# -*- coding: utf-8 -*-
import os, io, re, sys, zipfile
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_ex")
os.makedirs(OUT, exist_ok=True)

def dump_pdf(path, slug):
    import fitz
    doc = fitz.open(path)
    n = doc.page_count
    parts = []
    for i, pg in enumerate(doc):
        parts.append("\n===== PAGE %d =====\n" % (i + 1))
        parts.append(pg.get_text("text"))
    txt = "".join(parts)
    io.open(os.path.join(OUT, slug + ".txt"), "w", encoding="utf-8").write(txt)
    print(slug, "pages=", n, "chars=", len(txt))

def dump_epub(path, slug):
    import fitz
    doc = fitz.open(path)  # fitz opens epub too
    n = doc.page_count
    parts = []
    for i, pg in enumerate(doc):
        parts.append("\n===== SPINE %d =====\n" % (i + 1))
        parts.append(pg.get_text("text"))
    txt = "".join(parts)
    io.open(os.path.join(OUT, slug + ".txt"), "w", encoding="utf-8").write(txt)
    print(slug, "pages=", n, "chars=", len(txt))

R = r"C:\Docs_Here\newReading"
dump_pdf(os.path.join(R, "The Elements of Style, 2011 Revised Edition (William Strunk, Chris Hong) (Z-Library).pdf"), "elements-of-style")
dump_pdf(os.path.join(R, "The Sense of Style The Thinking Person\u2019s Guide to Writing in the 21st Century (Steven Pinker) (Z-Library).pdf"), "sense-of-style")
dump_epub(os.path.join(R, "They Say  I Say - The Moves That Matter in Academic Writing with Readings (Sixth Edition) (Gerald Graff, Cathy Birkenstein) (Z-Library).epub"), "they-say-i-say")
