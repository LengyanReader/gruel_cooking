# -*- coding: utf-8 -*-
"""extract_corpus.py — persistent Layer-1 corpus extractor for Reading & IA.

Purpose
-------
Turn a whole book file (EPUB or PDF) into a stable, re-runnable *intermediate*:
one JSON per book holding every spine document's clean text, heading tree and
objective metrics. This is the missing tooling that lets the semantic passes
(brief / claims / quotes in ``books.json``) be grounded in the COMPLETE source
text rather than a partial read.

The extractor does NOT decide what a chapter "means" — it only surfaces the
material at full fidelity. The five-lossless-guarantee synthesis (see
``framework.md``) is a separate, human/agent reading step on top of this file.

Copyright / IP discipline
-------------------------
The full text it extracts is written to ``web/data/corpus/`` which is
**gitignored**: raw book text is a local working artefact for reading only, it
is never committed. Only downstream *summaries* reach ``books.json``. Where a
brief cites evidence it cites short spans, consistent with framework.md §5.

Usage
-----
    # one file, explicit id
    python -X utf8 extract_corpus.py --source "C:\\path\\book.epub" --id pe-volume7-pursuit-power

    # whole Penguin shelf, auto-mapped to the known volume ids
    python -X utf8 extract_corpus.py --penguin-dir "C:\\Docs_Here\\newReading\\企鹅欧洲"

    # all ids already in books.json, resolving source by title match in a dir
    python -X utf8 extract_corpus.py --from-books books.json --dir "C:\\Docs_Here\\newReading\\企鹅欧洲"

Output: web/data/corpus/<book_id>.json  (+ prints a per-chapter metric table)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from collections import OrderedDict

# --- optional, gracefully-degrading third-party readers -----------------------
try:
    import ebooklib as _ebooklib_root  # type: ignore
    from ebooklib import epub as _epub  # type: ignore
    HAVE_EPUBLIB = True
except Exception as exc:  # pragma: no cover
    _ebooklib_root = None
    HAVE_EPUBLIB = False
    _EPUBLIB_ERR = exc

# ITEM_DOCUMENT is an int (9) exposed on the top-level ebooklib package in
# current releases; older/alternate layouts put it on ebooklib.epub or
# ebooklib.constants. Resolve defensively so the type filter actually matches.
_ITEM_DOCUMENT = None
if HAVE_EPUBLIB:
    for _src in (_ebooklib_root, _epub):
        _v = getattr(_src, "ITEM_DOCUMENT", None)
        if _v is not None:
            _ITEM_DOCUMENT = _v
            break
    if _ITEM_DOCUMENT is None:
        try:
            from ebooklib import constants as _c  # type: ignore
            _ITEM_DOCUMENT = getattr(_c, "ITEM_DOCUMENT", 9)
        except Exception:  # noqa: BLE001
            _ITEM_DOCUMENT = 9


def _is_document(item) -> bool:
    """True if an EPUB manifest item is a readable (x)html document."""
    try:
        if item.get_type() == _ITEM_DOCUMENT:
            return True
    except Exception:  # noqa: BLE001
        pass
    try:
        return isinstance(item, _epub.EpubHtml)
    except Exception:  # noqa: BLE001
        return False

try:
    import pymupdf as _fitz  # type: ignore
except Exception:  # noqa: BLE001
    try:
        import fitz as _fitz  # type: ignore  # legacy module name
    except Exception as exc:  # pragma: no cover
        _fitz = None
        _FITZ_ERR = exc

try:
    from bs4 import BeautifulSoup  # type: ignore
    HAVE_BS4 = True
except Exception as exc:  # pragma: no cover
    HAVE_BS4 = False
    _BS4_ERR = exc

try:
    import trafilatura  # type: ignore
    HAVE_TRAFI = True
except Exception:  # noqa: BLE001
    trafilatura = None  # type: ignore
    HAVE_TRAFI = False

# textstat needs the NLTK cmudict resource which the sandboxed proxy can block;
# treat every call as optional so the harness never hard-depends on it.
try:
    import textstat as _textstat  # type: ignore
    HAVE_TEXTSTAT = True
except Exception:  # noqa: BLE001
    _textstat = None  # type: ignore
    HAVE_TEXTSTAT = False


# --------------------------------------------------------------------------- #
# text utilities
# --------------------------------------------------------------------------- #
_WS_RE = re.compile(r"[ \t\r\f\v]+")
_SENT_RE = re.compile(r"[^.!?…]+[.!?…]+|[^.!?…]+$")


def _clean_text(s: str) -> str:
    if not s:
        return ""
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\u00ad", "")  # soft hyphen
    s = s.replace("\u200b", "").replace("\ufeff", "")  # zero-width / BOM
    s = _WS_RE.sub(" ", s)
    # collapse >2 consecutive newlines to a double newline
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def _word_count(s: str) -> int:
    return len(re.findall(r"\w+", s, flags=re.UNICODE))


def _sentence_count(s: str) -> int:
    return len([m for m in _SENT_RE.findall(s) if _word_count(m)])


def _readability_or_none(s: str) -> dict:
    """Best-effort readability; empty dict if textstat/cmudict unavailable."""
    if not HAVE_TEXTSTAT or not s.strip():
        return {}
    try:
        return {
            "flesch_reading_ease": round(_textstat.flesch_reading_ease(s), 1),
            "flesch_kincaid_grade": round(_textstat.flesch_kincaid_grade(s), 1),
        }
    except Exception:  # noqa: BLE001  # missing cmudict etc.
        return {}


def _headings_from_soup(soup) -> list:
    heads = []
    for tag in soup.find_all(re.compile(r"^h[1-6]$")):
        txt = _clean_text(tag.get_text(" "))
        if txt:
            heads.append({"level": int(tag.name[1]), "text": txt})
    return heads


def _paras_from_soup(soup) -> list:
    """Main narrative paragraphs: <p> and <div> that behave like blocks."""
    body = soup.find("body") or soup
    out = []
    for el in body.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "li"]):
        txt = _clean_text(el.get_text(" "))
        if txt:
            out.append(txt)
    return out


# --------------------------------------------------------------------------- #
# EPUB reader
# --------------------------------------------------------------------------- #
def read_epub(path: str) -> dict:
    if not HAVE_EPUBLIB:
        raise RuntimeError(f"ebooklib unavailable: {_EPUBLIB_ERR}")
    book = _epub.read_epub(path, options={"ignore_ncx": False})

    # ---- TOC (navMap) for human titles keyed by content href ----------------
    toc_by_href = {}

    def _walk(toc_items):
        for it in toc_items:
            href = getattr(it, "href", None)
            title = _clean_text(getattr(it, "title", "") or "")
            if href:
                key = href.split("#", 1)[0]
                if key and key not in toc_by_href and title:
                    toc_by_href[key] = title
            subs = getattr(it, "children", None)
            if subs:
                _walk(subs)

    _walk(book.toc)

    # ---- manifest lookup ----------------------------------------------------
    manifest = {}
    for item in book.get_items():
        manifest[item.get_id()] = item

    # ---- spine order --------------------------------------------------------
    spine_ids = [idref for idref, _ in book.spine]
    chapters = []
    for i, sid in enumerate(spine_ids):
        item = manifest.get(sid)
        if item is None:
            continue
        if not _is_document(item):
            continue
        href = item.get_name()
        raw = item.get_content()
        try:
            html = raw.decode("utf-8", "replace") if isinstance(raw, (bytes, bytearray)) else str(raw)
        except Exception:  # noqa: BLE001
            html = ""
        text = ""
        heads = []
        paras = []
        if HAVE_BS4 and html:
            soup = BeautifulSoup(html, "html.parser")
            for junk in soup(["script", "style"]):
                junk.decompose()
            heads = _headings_from_soup(soup)
            paras = _paras_from_soup(soup)
            body = soup.find("body") or soup
            text = _clean_text(body.get_text("\n"))
        elif html:
            text = _clean_text(re.sub(r"<[^>]+>", " ", html))
        if not text.strip():
            continue  # skip empty cover/blank spine docs
        chapters.append({
            "index": len(chapters),
            "spine_id": sid,
            "href": href,
            "toc_title": toc_by_href.get(href, ""),
            "headings": heads,
            "paras": paras,
            "char_count": len(text),
            "word_count": _word_count(text),
            "sentence_count": _sentence_count(text),
            "text": text,
        })

    meta = {}
    for key in ("title", "language", "identifier"):
        vals = book.get_metadata("DC", key) if hasattr(book, "get_metadata") else []
        if vals:
            meta[key] = _clean_text(vals[0][0].get_text()) if hasattr(vals[0][0], "get_text") else str(vals[0][1].get("text", ""))
    return {
        "format": "epub",
        "source_path": os.path.abspath(path),
        "meta": meta,
        "toc_hrefs": len(toc_by_href),
        "chapters": chapters,
    }


# --------------------------------------------------------------------------- #
# PDF reader
# --------------------------------------------------------------------------- #
def read_pdf(path: str) -> dict:
    if _fitz is None:
        raise RuntimeError(f"PyMuPDF unavailable: {_FITZ_ERR}")
    doc = _fitz.open(path)
    toc = doc.get_toc(simple=True)  # [[level, title, page1based], ...]
    # bucket toc titles by 1-based start page
    title_by_page = {}
    for level, title, page in toc:
        title_by_page.setdefault(int(page), (int(level), _clean_text(title)))

    chapters = []
    for pno in range(doc.page_count):
        page = doc.load_page(pno)
        raw = page.get_text("text")
        text = _clean_text(raw)
        if not text:
            continue
        _, htitle = title_by_page.get(pno + 1, (None, ""))
        chapters.append({
            "index": len(chapters),
            "page": pno + 1,
            "toc_title": htitle,
            "char_count": len(text),
            "word_count": _word_count(text),
            "sentence_count": _sentence_count(text),
            "text": text,
            "paras": [ln for ln in text.split("\n") if ln.strip()],
            "headings": ([{"level": 1, "text": htitle}] if htitle else []),
        })
    out = {
        "format": "pdf",
        "source_path": os.path.abspath(path),
        "meta": {"title": _clean_text((doc.metadata or {}).get("title", ""))},
        "toc_entries": len(toc),
        "chapters": chapters,
    }
    doc.close()
    return out


def _wrap_single(path: str, text: str, fmt: str, title: str) -> dict:
    """Wrap an already-clean text blob into a single-chapter Corpus IR."""
    return {"format": fmt, "source_path": os.path.abspath(path), "meta": {"title": title},
            "chapters": [{"index": 0, "href": os.path.basename(path), "toc_title": title,
                          "headings": [], "paras": [text], "char_count": len(text),
                          "word_count": _word_count(text), "sentence_count": _sentence_count(text),
                          "text": text}]}


def read_universal(path: str) -> dict:
    """Fallback front door for formats no structured adapter owns
    (docx/pptx/xlsx/zip/csv/...): markitdown -> Markdown -> light-split IR.
    Fidelity is 'flat' — the caller's registry decides if that is acceptable."""
    try:
        from markitdown import MarkItDown  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(f"markitdown unavailable for read_universal: {exc}")
    result = MarkItDown(enable_plugins=False).convert(path)
    md = getattr(result, "markdown", "") or ""
    # Split on top-level ATX headings so downstream sees chapter-like segments,
    # but never claim structured fidelity we did not extract.
    segments = re.split(r"(?m)^(#{1,2}) ", md)
    chapters, idx = [], 0
    if len(segments) <= 1:
        clean = _clean_text(md)
        return _wrap_single(path, clean, "universal", os.path.basename(path))
    for j in range(2, len(segments), 2):
        title = _clean_text(segments[j].splitlines()[0]) if segments[j] else ""
        body = _clean_text(segments[j + 1]) if j + 1 < len(segments) else ""
        if not body:
            continue
        chapters.append({"index": idx, "href": f"md#{idx}", "toc_title": title,
                         "headings": [{"level": 1, "text": title}] if title else [],
                         "paras": [ln for ln in body.splitlines() if ln.strip()],
                         "char_count": len(body), "word_count": _word_count(body),
                         "sentence_count": _sentence_count(body), "text": body})
        idx += 1
    if not chapters:
        clean = _clean_text(md)
        return _wrap_single(path, clean, "universal", os.path.basename(path))
    return {"format": "universal", "source_path": os.path.abspath(path),
            "meta": {"title": os.path.basename(path), "backend": "markitdown"},
            "chapters": chapters}


def read_any(path: str) -> dict:
    low = path.lower()
    if low.endswith(".epub"):
        return read_epub(path)
    if low.endswith(".pdf"):
        return read_pdf(path)
    if low.endswith((".htm", ".html", ".txt", ".md")):
        raw = open(path, encoding="utf-8", errors="replace").read()
        text = _clean_text(trafilatura.extract(raw) if (HAVE_TRAFI and low.endswith(".html")) else raw)
        return {"format": "text", "source_path": os.path.abspath(path), "meta": {},
                "chapters": [{"index": 0, "toc_title": os.path.basename(path),
                              "headings": [], "paras": [text], "char_count": len(text),
                              "word_count": _word_count(text), "sentence_count": _sentence_count(text),
                              "text": text}]}
    if low.endswith((".docx", ".pptx", ".xlsx", ".xls", ".zip", ".csv", ".xml", ".json")):
        return read_universal(path)
    raise ValueError(f"unsupported format: {path}")


# --------------------------------------------------------------------------- #
# metrics roll-up
# --------------------------------------------------------------------------- #
def summarize(data: dict) -> dict:
    ch = data.get("chapters", [])
    total_chars = sum(c.get("char_count", 0) for c in ch)
    total_words = sum(c.get("word_count", 0) for c in ch)
    return {
        "n_chapters": len(ch),
        "total_chars": total_chars,
        "total_words": total_words,
        "avg_chars_per_chapter": (total_chars // len(ch)) if ch else 0,
        "chapters_with_headings": sum(1 for c in ch if c.get("headings")),
    }


# --------------------------------------------------------------------------- #
# Penguin shelf auto-mapping
# --------------------------------------------------------------------------- #
# map a normalised keyword signature to the books.json id used across the repo
PENGUIN_ID_KEYS = OrderedDict([
    ("pe-volume1-birth-classical", ["birth of classical"]),
    ("pe-volume2-inheritance-rome", ["inheritance of rome"]),
    ("pe-volume3-high-middle-ages", ["high middle ages"]),
    ("pe-volume4-renaissance-europe", ["renaissance"]),
    ("pe-volume5-christendom-destroyed", ["christendom destroyed"]),
    ("pe-volume6-pursuit-glory", ["pursuit of glory"]),
    ("pe-volume7-pursuit-power", ["pursuit of power"]),
    ("pe-volume8-hell-and-back", ["to hell and back", "hell and back"]),
    ("pe-volume9-global-age", ["global age"]),
])


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def match_penguin_id(filename: str):
    n = _norm(filename)
    for bid, keys in PENGUIN_ID_KEYS.items():
        if any(_norm(k) in n for k in keys):
            return bid
    return None


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _write_corpus(data: dict, book_id: str, out_dir: str) -> str:
    os.makedirs(out_dir, exist_ok=True)
    data["book_id"] = book_id
    data["summary"] = summarize(data)
    dest = os.path.join(out_dir, f"{book_id}.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    return dest


def _print_table(dest: str, data: dict):
    s = data["summary"]
    print(f"\n== {data['book_id']}  [{data['format']}] -> {dest}")
    print(f"   chapters={s['n_chapters']} chars={s['total_chars']:,} "
          f"words={s['total_words']:,} avg/chapter={s['avg_chars_per_chapter']:,}")
    shown = 0
    for c in data["chapters"]:
        title = c.get("toc_title") or (c.get("headings") or [{}])[0].get("text", "") or c.get("href", "")
        if not title:
            title = f"(ch {c['index']})"
        print(f"   [{c['index']:>3}] {c.get('char_count', 0):>7,} ch  {title[:60]}")
        shown += 1
        if shown >= 40:
            print(f"   … {s['n_chapters'] - 40} more chapters")
            break


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Extract a book file into a per-book corpus JSON.")
    ap.add_argument("--source", help="single EPUB/PDF/HTML file to extract")
    ap.add_argument("--id", dest="book_id", help="book id (used with --source)")
    ap.add_argument("--penguin-dir", help="directory of Penguin volumes to auto-map and extract")
    ap.add_argument("--out", default=None, help="output dir (default: <repo>/Reading_IA/web/data/corpus)")
    ap.add_argument("--no-text", action="store_true", help="omit full text field (metrics + headings only)")
    args = ap.parse_args(argv)

    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.abspath(os.path.join(here, "..", "..", ".."))
    out_dir = args.out or os.path.join(repo, "Reading_IA", "web", "data", "corpus")

    jobs = []
    if args.source:
        bid = args.book_id or match_penguin_id(os.path.basename(args.source)) or \
            _norm(os.path.splitext(os.path.basename(args.source))[0])[:48]
        jobs.append((args.source, bid))
    if args.penguin_dir:
        for fn in sorted(os.listdir(args.penguin_dir)):
            if not fn.lower().endswith((".epub", ".pdf")):
                continue
            full = os.path.join(args.penguin_dir, fn)
            bid = match_penguin_id(fn)
            if not bid:
                print(f"skip (unmapped): {fn}")
                continue
            jobs.append((full, bid))

    if not jobs:
        ap.error("nothing to do — pass --source ... --id ... or --penguin-dir ...")

    wrote = 0
    for src, bid in jobs:
        try:
            data = read_any(src)
        except Exception as exc:  # noqa: BLE001
            print(f"!! {bid}: extract failed: {exc}", file=sys.stderr)
            continue
        if args.no_text:
            for c in data["chapters"]:
                c.pop("text", None)
        dest = _write_corpus(data, bid, out_dir)
        _print_table(dest, data)
        wrote += 1
    print(f"\nextracted {wrote} book(s) -> {out_dir}")
    print("NOTE: corpus/ is a gitignored local working artefact (raw book text).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
