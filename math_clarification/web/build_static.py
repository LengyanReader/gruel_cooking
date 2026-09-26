"""Build self-contained static HTML from the Markdown articles.

The FastAPI viewer in this folder is convenient while writing, but it needs a
running server. This script renders the same Markdown into standalone files
that open straight from disk (file://), so an article can be read, mailed or
archived without any dependency.

Design borrows the warm "dawn" palette and typography of
docs/living_heritage/css/main.css, re-tuned for long-form academic reading:
a serif body against sans headings, a measure capped for comfortable CJK
line lengths, a sticky chapter list, and a three-way language switch.

    python build_static.py              # export every article + index.html
    python build_static.py --slug NAME  # export one article
"""

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from parser import parse_entry, parse_markdown, extract_notes  # noqa: E402

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ARTICLES = BASE / "articles"
OUT = HERE / "static" / "articles"

# GitHub Pages publishes this repo from docs/, and docs/index.html already links
# to math_clarification/ -- a path that 404s until the pages land there. The
# pages are self-contained and only ever use sibling-relative links, so the same
# files are written flat into docs/math_clarification/ and go live as they are.
DOCS_SITE = BASE.parent / "docs" / "math_clarification"

# Articles that are still built and published (so their direct URL works), but are
# deliberately left out of the landing index so they cannot be reached by browsing
# the site — only via the link itself. Their pages also carry a noindex hint so
# they stay out of search results. Add a file's stem here to unlist it.
UNLISTED = {"proofs_no_longer_scarce"}

# ---------------------------------------------------------------- design ----

CSS = """
:root {
  --cream: #FFFBF5;
  --cream-deep: #F7EFE2;
  --paper: #FFFDF9;
  --gold: #F5C97E;
  --gold-soft: #FBE9C8;
  --amber: #E8A855;
  --amber-deep: #C9852F;
  --ink: #332C23;
  --ink-soft: #6B5F4F;
  --ink-faint: #9A8D7A;
  --sky-deep: #407CB0;
  --line: #EBDCC4;
  --line-soft: #F3E9D8;
  --measure: 42rem;
  --sans: "Inter", "Segoe UI", "PingFang SC", "Microsoft YaHei", system-ui, sans-serif;
  --serif: "Iowan Old Style", "Palatino Linotype", Georgia, "LXGW WenKai",
           "Songti SC", "Source Han Serif SC", "Noto Serif CJK SC", "SimSun", serif;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: calc(var(--bh, 0px) + 84px); }
body {
  margin: 0;
  padding-top: var(--bh, 0px);
  font-family: var(--serif);
  font-size: 17.5px;
  line-height: 1.85;
  color: var(--ink);
  background-color: var(--cream);
  background-image: radial-gradient(rgba(232, 168, 85, 0.055) 1px, transparent 1px);
  background-size: 26px 26px;
  -webkit-font-smoothing: antialiased;
}

/* ---------- bilingual text pairs ----------
   Dual mode shows both halves; lang-en and lang-zh each keep their own.
   `revert` restores the element's default display, so a pair can sit inside
   a span or a <p> without either one changing the surrounding layout. */
.p-zh, .p-en { display: revert; }
body.lang-en .p-zh { display: none !important; }
body.lang-zh .p-en { display: none !important; }

/* ---------- draft notice (pinned, floating) ---------- */
#draft {
  position: fixed; top: 0; left: 0; right: 0; z-index: 70;
  display: flex; align-items: center; justify-content: center; gap: 14px;
  padding: 9px 52px 9px 20px;
  font-family: var(--sans); font-size: .78rem; line-height: 1.5;
  color: #6B4A12; text-align: center;
  background: repeating-linear-gradient(135deg, #FBE9C8, #FBE9C8 12px, #F8E0B8 12px, #F8E0B8 24px);
  border-bottom: 1px solid var(--amber);
  box-shadow: 0 2px 10px rgba(58, 50, 40, .07);
}
#draft .flag {
  flex: none; font-size: .62rem; font-weight: 700; letter-spacing: .12em;
  text-transform: uppercase; color: #fff; background: var(--amber-deep);
  border-radius: 4px; padding: 2px 7px;
}
#draft .msg { min-width: 0; }
#draft .msg em { font-style: normal; font-weight: 600; }
#draft .dismiss {
  position: absolute; top: 50%; right: 10px; transform: translateY(-50%);
  width: 26px; height: 26px; padding: 0; cursor: pointer;
  font: inherit; font-size: 1.05rem; line-height: 1;
  color: var(--amber-deep); background: rgba(255, 255, 255, .6);
  border: 1px solid var(--amber); border-radius: 50%;
}
#draft .dismiss:hover { background: #fff; color: #8A4B12; }
#draft[hidden] { display: none; }

/* ---------- reading progress ---------- */
#progress {
  position: fixed; top: var(--bh, 0px); left: 0; height: 3px; width: 0;
  background: linear-gradient(90deg, var(--amber), var(--gold));
  z-index: 60; transition: width .1s linear;
}

/* ---------- top bar ---------- */
.topbar {
  position: sticky; top: 0; z-index: 50;
  display: flex; align-items: center; gap: 18px;
  padding: 12px 26px;
  background: rgba(255, 251, 245, 0.93);
  backdrop-filter: blur(9px);
  border-bottom: 1px solid var(--line);
}
.topbar .brand { display: flex; flex-direction: column; line-height: 1.25; min-width: 0; }
.topbar .brand a { color: var(--ink); font-weight: 600; font-size: .95rem;
                   text-decoration: none; font-family: var(--sans); }
.topbar .brand .zh { font-size: .74rem; color: var(--ink-faint); letter-spacing: .04em; }
.topbar .spacer { flex: 1; }
.topbar .langset { display: flex; gap: 6px; font-family: var(--sans); }
.langset { display: flex; gap: 6px; font-family: var(--sans); }
.langset button {
  font: inherit; font-size: .82rem; cursor: pointer; line-height: 1.4;
  padding: 5px 13px; border-radius: 999px;
  border: 1px solid var(--line); background: var(--cream); color: var(--ink-soft);
  transition: all .16s ease;
}
.langset button:hover { border-color: var(--amber); color: var(--ink); }
.langset button[aria-pressed="true"] {
  background: var(--amber); border-color: var(--amber); color: #fff; font-weight: 600;
}

/* ---------- share ---------- */
.share { display: flex; align-items: center; gap: 6px; font-family: var(--sans); }
.share button {
  font: inherit; font-size: .78rem; line-height: 1.4; cursor: pointer;
  padding: 5px 11px; border-radius: 999px; text-decoration: none;
  border: 1px solid var(--line); background: var(--cream); color: var(--ink-soft);
  transition: all .16s ease; white-space: nowrap;
}
.share button:hover { border-color: var(--amber); color: var(--ink); background: var(--cream-deep); }
.share button.done { background: var(--amber); border-color: var(--amber); color: #fff; }

/* ---------- signature ---------- */
.byline, .colophon {
  font-family: var(--sans); font-size: .74rem; color: var(--ink-faint);
}
.byline { margin-top: 14px; letter-spacing: .02em; }
.byline b { font-weight: 600; color: var(--ink-soft); }
.byline a, .colophon a { color: var(--sky-deep); text-decoration: none; }
.byline a:hover, .colophon a:hover { text-decoration: underline; }
/* publication / update dateline, declared as metadata in the source preamble */
.dateline { margin-top: 10px; font-family: var(--sans); font-size: .74rem; color: var(--ink-faint); letter-spacing: .02em; }
.dateline b { font-weight: 600; color: var(--ink-soft); font-variant-numeric: tabular-nums; }
.dateline .sep { margin: 0 10px; color: var(--line); }
.colophon {
  margin-top: 46px; padding-top: 20px; border-top: 1px solid var(--line-soft);
  display: flex; flex-wrap: wrap; gap: 6px 14px; justify-content: space-between;
}

/* ---------- shell ---------- */
.shell { display: grid; grid-template-columns: 262px minmax(0, 1fr); gap: 0; align-items: start; }
.toc {
  position: sticky; top: calc(var(--bh, 0px) + 62px); align-self: start;
  max-height: calc(100vh - var(--bh, 0px) - 62px); overflow-y: auto;
  padding: 30px 20px 60px 26px; border-right: 1px solid var(--line-soft);
}
.toc h2 {
  font-family: var(--sans); font-size: .72rem; font-weight: 600;
  letter-spacing: .16em; text-transform: uppercase;
  color: var(--ink-faint); margin: 0 0 14px;
}
.toc ol { list-style: none; margin: 0; padding: 0; counter-reset: c; }
.toc li { counter-increment: c; margin: 0 0 2px; }
.toc a {
  display: block; padding: 5px 10px; border-radius: 7px;
  font-family: var(--sans); font-size: .855rem; line-height: 1.45;
  color: var(--ink-soft); text-decoration: none;
  border-left: 2px solid transparent; transition: all .16s ease;
}
.toc a:hover { background: var(--cream-deep); color: var(--ink); }
.toc a.active {
  background: var(--gold-soft); color: var(--amber-deep);
  border-left-color: var(--amber); font-weight: 600;
}
.toc .lv { font-size: .95em; opacity: .55; margin-right: .4em; }

main { padding: 40px 56px 140px; min-width: 0; }
.doc { max-width: var(--measure); margin: 0 auto; }

/* ---------- title block ---------- */
.titleblock { border-bottom: 1px solid var(--line); padding-bottom: 26px; margin-bottom: 12px; }
.kicker {
          font-family: var(--sans); font-size: .72rem; font-weight: 600;
          letter-spacing: .18em; text-transform: uppercase; color: var(--amber-deep);
          margin: 0 0 14px;
        }
        .kicker { margin: 0 0 14px; }

.titleblock h1 {
  font-family: var(--sans); font-weight: 700; color: var(--ink);
  font-size: clamp(1.65rem, 3.4vw, 2.35rem); line-height: 1.32; margin: 0 0 10px;
  letter-spacing: -.005em;
}
.titleblock h1 .t-zh, .titleblock h1 .t-en { display: block; }
/* In dual mode the English title rides under the Chinese one; the lang-en and
   lang-zh modes each promote their own half to full heading size. */
.titleblock h1 .t-en {
  margin-top: .32em; font-size: .54em; font-weight: 500;
  color: var(--ink-soft); line-height: 1.44; letter-spacing: 0;
}
body.lang-en .titleblock h1 .t-zh { display: none; }
body.lang-en .titleblock h1 .t-en {
  margin-top: 0; font-size: 1em; font-weight: 700;
  color: var(--ink); line-height: 1.32; letter-spacing: -.005em;
}
body.lang-zh .titleblock h1 .t-en { display: none; }
.titleblock .sub {
  font-family: var(--sans); font-size: 1.02rem; color: var(--ink-soft);
  line-height: 1.6; margin: 0;
}
.titleblock .note {
          font-family: var(--sans); font-size: .78rem; line-height: 1.65;
          color: var(--ink-faint); margin: 16px 0 0; padding: 10px 14px;
          background: var(--cream-deep); border-left: 3px solid var(--line);
          border-radius: 0 8px 8px 0;
        }
        .titleblock .note .n-en { display: block; }
        .titleblock .note .n-en + .n-zh, .titleblock .note .n-zh + .n-en { margin-top: 8px; }
        body.lang-en .titleblock .note .n-zh,
        body.lang-zh .titleblock .note .n-en { display: none; }


/* ---------- units (one per source block) ---------- */
.unit { padding: 34px 0 10px; border-top: 1px solid var(--line-soft); }
.unit:first-of-type { border-top: none; }
.unit.is-src .lang-body ol { columns: 2; column-gap: 34px; font-size: .84rem; line-height: 1.62; }
.unit.is-src .lang-body li { break-inside: avoid; margin-bottom: 9px; }

.lang-block { position: relative; margin: 0 0 26px; }
.lang-chip {
  display: inline-block; font-family: var(--sans); font-size: .64rem; font-weight: 700;
  letter-spacing: .14em; color: var(--ink-faint);
  border: 1px solid var(--line); border-radius: 4px;
  padding: 1px 7px; margin-bottom: 12px; background: var(--paper);
}
.lang-zh { border-left: 3px solid var(--gold); padding-left: 20px; }

/* ---------- heading hierarchy ----------
   Chapters (h2) sit flush against the measure with a rule above; numbered
   sub-sections (h3/h4) step in by one level each, and their body copy follows
   them in, so the outline is readable at a glance. */
.lang-body .sub { margin: 0; }
.lang-body h2 {
  font-family: var(--sans); font-weight: 650; font-size: 1.32rem; line-height: 1.4;
  color: var(--ink); letter-spacing: -.003em;
  margin: 38px 0 8px; padding-top: 24px; border-top: 1px solid var(--line);
}
.lang-body .sub.d0 > h2:first-child,
.lang-body > h2:first-child { margin-top: 0; padding-top: 0; border-top: 0; }
.lang-body h3 {
  font-family: var(--sans); font-weight: 600; font-size: 1.06rem; line-height: 1.5;
  color: var(--amber-deep); margin: 28px 0 9px;
  padding-left: .8rem; border-left: 2px solid var(--gold);
}
.lang-body h4 {
  font-family: var(--sans); font-weight: 600; font-size: .97rem; color: var(--ink-soft);
  margin: 22px 0 7px; padding-left: .7rem; border-left: 2px solid var(--line);
}
.lang-body .sub.d1 { margin-left: 1.5rem; }
.lang-body .sub.d2 { margin-left: 1.5rem; }
.lang-body .sub.d2 > h4 { border-left-color: var(--line); }
.lang-body .sub > :first-child { margin-top: 0; }
.lang-body p { margin: 0 0 17px; }
.lang-zh .lang-body p { text-align: justify; text-justify: inter-ideograph; letter-spacing: .01em; }
.lang-body ul, .lang-body ol { margin: 0 0 18px; padding-left: 1.35em; }
.lang-body li { margin-bottom: 7px; }
.lang-body li > ul, .lang-body li > ol { margin-top: 7px; }
.lang-body strong { font-weight: 650; color: #241E17; }
.lang-body em { font-style: italic; }
.lang-body a { color: var(--sky-deep); text-underline-offset: 2px; }
.lang-body hr { border: 0; border-top: 1px solid var(--line); margin: 26px 0; }
.lang-body blockquote {
  margin: 0 0 18px; padding: 4px 0 4px 18px;
  border-left: 3px solid var(--line); color: var(--ink-soft); font-style: italic;
}
.lang-body code {
  font-family: "Cascadia Mono", Consolas, monospace; font-size: .88em;
  background: var(--cream-deep); padding: 1px 5px; border-radius: 4px;
}
.lang-body pre {
  background: var(--cream-deep); border: 1px solid var(--line);
  padding: 14px 16px; border-radius: 10px; overflow-x: auto; line-height: 1.55;
}
.lang-body pre code { background: none; padding: 0; }
.lang-body table { border-collapse: collapse; width: 100%; font-size: .9rem; margin: 0 0 18px; }
.lang-body th, .lang-body td { border: 1px solid var(--line); padding: 7px 10px; text-align: left; }
.lang-body th { background: var(--cream-deep); font-family: var(--sans); font-weight: 600; }

/* ---------- language modes ---------- */
body.lang-en .lang-zh { display: none; }
body.lang-zh .lang-en { display: none; }
body.lang-en .lang-chip, body.lang-zh .lang-chip { display: none; }
body.lang-zh .lang-body, body.lang-en .lang-body { text-align: left; }
body.lang-en .lang-block { border-left: none; padding-left: 0; }

/* ---------- index page ---------- */
.idx { max-width: 780px; margin: 0 auto; padding: 64px 26px 120px; }
.idx h1 { font-family: var(--sans); font-size: 2rem; margin: 0 0 6px; }
.idx .lede { color: var(--ink-soft); font-size: 1.02rem; margin: 0 0 34px; font-family: var(--sans); }
.idx article {
  background: var(--paper); border: 1px solid var(--line);
  border-radius: 14px; padding: 24px 26px; margin-bottom: 18px;
  box-shadow: 0 8px 24px rgba(58, 50, 40, .05);
}
.idx article h2 { font-family: var(--sans); font-size: 1.15rem; margin: 0 0 8px; line-height: 1.45; }
.idx article h2 a { color: var(--ink); text-decoration: none; }
.idx article h2 a:hover { color: var(--amber-deep); }
.idx article p { margin: 0 0 12px; font-size: .95rem; color: var(--ink-soft); }
.idx .meta { font-family: var(--sans); font-size: .78rem; color: var(--ink-faint); }
.idx .open {
  display: inline-block; font-family: var(--sans); font-size: .8rem; font-weight: 600;
  color: #fff; background: var(--amber); text-decoration: none;
  padding: 6px 16px; border-radius: 999px;
}
.idx .open:hover { background: var(--amber-deep); color: #fff; }

/* ---------- responsive ---------- */
@media (max-width: 1000px) {
  .shell { grid-template-columns: 1fr; }
  .toc {
    position: static; max-height: none; border-right: none;
    border-bottom: 1px solid var(--line-soft); padding: 20px 26px;
  }
  .toc ol { columns: 2; column-gap: 18px; }
  main { padding: 26px 26px 100px; }
  .unit.is-src .lang-body ol { columns: 1; }
}
@media (max-width: 620px) {
        body { font-size: 16.5px; }
        .toc ol { columns: 1; }
        .lang-zh { padding-left: 14px; }
        .topbar { flex-wrap: wrap; gap: 10px 14px; padding: 10px 18px; }
        #draft { font-size: .72rem; padding: 7px 40px 7px 14px; }
      }

      /* ---------- print ---------- */
      @media print {
        body { background: #fff; font-size: 11.5pt; line-height: 1.6; padding-top: 0; }
        #draft, #progress, .topbar, .toc, .lang-chip, .langset, .share { display: none !important; }
        .shell { display: block; }
        main { padding: 0; }
        .doc { max-width: none; }
        body.lang-en .lang-zh, body.lang-zh .lang-en { display: none; }
        .lang-block { break-inside: avoid; }
        .unit { border-top: 1px solid #ddd; }
        .colophon { border-top: 1px solid #ccc; }
      }
      """


JS = """
(function () {
  var body = document.body;
  // Scope the language choice per page: reading one essay in EN must not force
  // another essay to open in EN. Each document remembers its own selection, and a
  // page never chosen defaults to bilingual. An explicit ?lang= link still wins.
  var KEY = 'zh-article-lang:' + location.pathname;
  var DRAFT_KEY = 'zh-draft-dismissed';

  /* ---------- draft notice: measure, pin, remember dismissal ---------- */
  var draft = document.getElementById('draft');
  function syncBanner() {
    var h = (draft && !draft.hidden) ? draft.offsetHeight : 0;
    document.documentElement.style.setProperty('--bh', h + 'px');
  }
  if (draft) {
    try {
      if (localStorage.getItem(DRAFT_KEY) === '1') { draft.hidden = true; }
    } catch (e) { /* file:// may block */ }
    var dismiss = draft.querySelector('.dismiss');
    if (dismiss) {
      dismiss.addEventListener('click', function () {
        draft.hidden = true;
        try { localStorage.setItem(DRAFT_KEY, '1'); } catch (e) { /* ignore */ }
        syncBanner();
      });
    }
    syncBanner();
    window.addEventListener('resize', syncBanner);
  }

  /* ---------- share: copy the page link ---------- */
  var here = location.href;
  Array.prototype.forEach.call(document.querySelectorAll('.share [data-share]'), function (el) {
    if (el.getAttribute('data-share') === 'copy') {
      // Keep the bilingual markup intact: swapping textContent would delete the
      // .p-zh/.p-en spans and freeze the button in one language after one click.
      var rest = el.innerHTML;
      el.addEventListener('click', function () {
        function ok() {
          el.innerHTML = '<span class="p-zh">' + (el.getAttribute('data-done-zh') || '已复制')
            + '</span><span class="p-en">' + (el.getAttribute('data-done-en') || 'Copied')
            + '</span>';
          el.classList.add('done');
          setTimeout(function () {
            el.innerHTML = rest;
            el.classList.remove('done');
          }, 1600);
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(here).then(ok, fallback);
        } else { fallback(); }
        function fallback() {
          // file:// and older browsers block the async clipboard API
          var ta = document.createElement('textarea');
          ta.value = here;
          ta.setAttribute('readonly', '');
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          body.appendChild(ta);
          ta.select();
          try { document.execCommand('copy'); ok(); } catch (e) { /* give up */ }
          body.removeChild(ta);
        }
      });
    }
  });

  /* ---------- language ---------- */
  function setLang(mode) {
    body.classList.remove('lang-en', 'lang-zh', 'lang-dual');
    body.classList.add('lang-' + mode);
    Array.prototype.forEach.call(document.querySelectorAll('.langset button'), function (b) {
      b.setAttribute('aria-pressed', String(b.dataset.lang === mode));
    });
    var tz = body.getAttribute('data-title-zh');
    var te = body.getAttribute('data-title-en');
    if (tz && te) {
      document.title = mode === 'en' ? te : (mode === 'zh' ? tz : tz + ' / ' + te);
    }
    try { localStorage.setItem(KEY, mode); } catch (e) { /* file:// may block */ }
    if (history.replaceState) {
      history.replaceState(null, '', '?lang=' + mode);
    }
    spy();
  }

  Array.prototype.forEach.call(document.querySelectorAll('.langset button'), function (b) {
    b.addEventListener('click', function () { setLang(b.dataset.lang); });
  });

  var initial = 'dual';
  try {
    var saved = localStorage.getItem(KEY);
    if (saved) { initial = saved; }
  } catch (e) { /* ignore */ }
  var q = (location.search.match(/lang=(en|zh|dual)/) || [])[1];
  if (q) { initial = q; }
  setLang(initial);

  // reading progress
  var bar = document.getElementById('progress');
  function progress() {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
  }
  document.addEventListener('scroll', progress, { passive: true });
  progress();

  // scroll spy
  var links = {};
  Array.prototype.forEach.call(document.querySelectorAll('.toc a'), function (a) {
    links[a.getAttribute('href').slice(1)] = a;
  });
  var units = Array.prototype.slice.call(document.querySelectorAll('.unit'));
  var current = null;
  function spy() {
    var y = window.scrollY + 140, found = null;
    for (var i = 0; i < units.length; i++) {
      if (units[i].offsetTop <= y) { found = units[i].id; } else { break; }
    }
    if (found === current) { return; }
    current = found;
    Object.keys(links).forEach(function (k) { links[k].classList.remove('active'); });
    if (found && links[found]) { links[found].classList.add('active'); }
  }
  window.addEventListener('scroll', spy, { passive: true });
  spy();
})();
"""

PAGE = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">__ROBOTS__
<style>__CSS__</style>
</head>
<body class="lang-dual" data-title-zh="__TITLE_ZH__" data-title-en="__TITLE_EN__">
<div id="draft" role="note">
  <span class="flag"><span class="p-zh">草稿</span><span class="p-en">Draft</span></span>
  <span class="msg">
    <span class="p-zh"><em>本文仅为草稿，仅供参考</em>，恳请各位读者多多指正、批评指教；文中观点与疏漏之处，欢迎来信讨论。</span>
    <span class="p-en"><em>This is a working draft, for reference only.</em> Comments and corrections are warmly welcome — please get in touch.</span>
  </span>
  <button type="button" class="dismiss" aria-label="关闭声明 / Dismiss notice">&times;</button>
</div>
<div id="progress"></div>

<div class="topbar">
  <div class="brand">
    <a href="index.html">__NAVTITLE__</a>
    <span class="zh"><span class="p-zh">__NAVZH__</span><span class="p-en">__NAV_EN__</span></span>
  </div>
  <div class="spacer"></div>
  <div class="share">
    <button type="button" data-share="copy" data-done-zh="已复制" data-done-en="Copied"><span class="p-zh">复制链接</span><span class="p-en">Copy link</span></button>
  </div>
  <div class="langset" role="group" aria-label="Language / 语言">
    <button type="button" data-lang="en" aria-pressed="false">EN</button>
    <button type="button" data-lang="zh" aria-pressed="false">中</button>
    <button type="button" data-lang="dual" aria-pressed="true">双语</button>
  </div>
</div>

<div class="shell">
  <nav class="toc">
    <h2><span class="p-zh">目录</span><span class="p-en">Contents</span></h2>
    <ol>__TOC__</ol>
  </nav>
  <main>
    <div class="doc">
      <div class="titleblock">
        <p class="kicker"><span class="p-zh">__KICKER_ZH__</span><span class="p-en">__KICKER_EN__</span></p>
        <h1><span class="t-zh">__H1__</span><span class="t-en">__SUB__</span></h1>
        __NOTE__
        __DATES__
        <p class="byline">南予 <b>nanyu</b> &middot; <a href="mailto:nanyudong@gmail.com">nanyudong@gmail.com</a></p>
      </div>
      __BODY__
      <p class="colophon">
        <span>南予 <b>nanyu</b> &middot; <a href="mailto:nanyudong@gmail.com">nanyudong@gmail.com</a></span>
        <span><span class="p-zh">本文为草稿，仅供参考，欢迎批评指正</span><span class="p-en">A working draft, for reference only — corrections welcome</span></span>
      </p>
    </div>
  </main>
</div>

<script>__JS__</script>
</body>
</html>
"""

INDEX = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>__CSS__</style>
</head>
<body class="lang-dual" data-title-zh="__TITLE_ZH__" data-title-en="__TITLE_EN__">
<div class="topbar">
  <div class="brand">
    <a href="index.html">__NAVTITLE__</a>
    <span class="zh"><span class="p-zh">__NAVZH__</span><span class="p-en">__NAV_EN__</span></span>
  </div>
  <div class="spacer"></div>
  <div class="langset" role="group" aria-label="Language / 语言">
    <button type="button" data-lang="en" aria-pressed="false">EN</button>
    <button type="button" data-lang="zh" aria-pressed="false">中</button>
    <button type="button" data-lang="dual" aria-pressed="true">双语</button>
  </div>
</div>
<div class="idx">
  <h1><span class="p-zh">__TITLE_ZH__</span><span class="p-en">__TITLE_EN__</span></h1>
  <p class="lede"><span class="p-zh">__LEDE_ZH__</span><span class="p-en">__LEDE_EN__</span></p>
  __CARDS__
  <p class="colophon">
    <span>南予 <b>nanyu</b> &middot; <a href="mailto:nanyudong@gmail.com">nanyudong@gmail.com</a></span>
    <span><span class="p-zh">本文为草稿，仅供参考，欢迎批评指正</span><span class="p-en">A working draft, for reference only — corrections welcome</span></span>
  </p>
</div>
<script>__JS__</script>
</body>
</html>
"""


# ------------------------------------------------------------- utilities ----

LEVEL_OPEN = re.compile(r"^<!--\s*(L[0-5])\s*-->$")
LEVEL_CLOSE = re.compile(r"^<!--\s*L[0-5]-end\s*-->$")
LANG_OPEN = re.compile(r"^<!--\s*(zh|en|dual)\s*-->$")
LANG_CLOSE = re.compile(r"^<!--\s*(zh|en|dual)-end\s*-->$")
# Author-declared dates, kept in the source preamble so the build stays
# deterministic (no file mtimes, no clock): <!-- 发表 2026-09-26 19:38 · 更新 2026-09-26 22:15 -->
# The HH:MM time of day is optional; a bare date still works.
DATE_META = re.compile(
    r"^<!--\s*(?:发表|Published)\s*(\d{4}-\d{2}-\d{2}(?:\s+\d{2}:\d{2})?)\s*·\s*"
    r"(?:更新|Updated)\s*(\d{4}-\d{2}-\d{2}(?:\s+\d{2}:\d{2})?)\s*-->$")


def esc(s):
    return html.escape(s, quote=True)


def extract_dates(raw):
    """Pull the author-declared (published, updated) pair from the preamble.

    The metadata line may be written with either label set (发表/更新 or
    Published/Updated); both languages render from the one date pair.
    Returns None when no line is present, so an article without the
    comment renders exactly as before.
    """
    for line in raw.splitlines():
        m = DATE_META.match(line.strip())
        if m:
            return " ".join(m.group(1).split()), " ".join(m.group(2).split())
    return None


def strip_heading_ids(fragment):
    """TocExtension gives every CJK heading the same id; drop them, we link per unit."""
    return re.sub(r"(<h[2-4])\s+id=\"[^\"]*\"", r"\1", fragment)


def first_h2_text(fragment):
    """First heading of any rank, as plain text.

    Continuation blocks open straight into `### 1.2 ...` with no chapter `##`,
    so falling back through the ranks beats inventing a chapter number.
    """
    m = re.search(r"<h([2-4])[^>]*>(.*?)</h\1>", fragment, re.S)
    if not m:
        return ""
    return re.sub(r"<[^>]+>", "", m.group(2)).strip()


def to_html(markdown_text):
    """Convert one language chunk to HTML, reusing the viewer's converter setup."""
    if not markdown_text.strip():
        return ""
    return parse_markdown(markdown_text).sections[0][2]


def split_blocks(raw):
    """Split the source into per-block EN/ZH pairs.

    The level alone cannot delimit chapters: every chapter is an L1 block, so
    nine consecutive chapters all carry the same level and would collapse into
    one. A chapter boundary is an opening <!-- Ln --> marker, so that is what
    this walks. Returns (provenance, units) where each unit is
    {"level", "en", "zh"} holding raw Markdown.
    """
    provenance_lines = []
    units = []
    cur = None
    lang = None
    buf = []

    def flush():
        if cur is not None and lang and any(l.strip() for l in buf):
            if lang == "dual":
                cur["en"].extend(buf)
            else:
                cur.setdefault(lang, []).extend(buf)
        buf.clear()

    for line in raw.split("\n"):
        s = line.strip()
        if LEVEL_OPEN.match(s):
            flush()
            if cur is not None and (cur["en"] or cur["zh"]):
                units.append(cur)
            cur = {"level": LEVEL_OPEN.match(s).group(1), "en": [], "zh": []}
            lang = None
            continue
        if LEVEL_CLOSE.match(s):
            flush()
            continue
        if LANG_OPEN.match(s):
            flush()
            lang = LANG_OPEN.match(s).group(1)
            continue
        if LANG_CLOSE.match(s):
            flush()
            lang = None
            continue
        if cur is None:
            provenance_lines.append(line)
        else:
            buf.append(line)

    flush()
    if cur is not None and (cur["en"] or cur["zh"]):
        units.append(cur)
    provenance = "\n".join(provenance_lines).strip()
    return provenance, units


def group_units(entry):
    """Kept for callers that already hold a ParsedEntry; pairs by level run."""
    units = []
    cur = None
    for level, lang, frag in entry.sections:
        if cur is None or level != cur["level"]:
            if cur:
                units.append(cur)
            cur = {"level": level, "en": [], "zh": []}
        if lang in ("en", "dual"):
            cur["en"].append(frag)
        if lang in ("zh", "dual"):
            cur["zh"].append(frag)
    if cur:
        units.append(cur)
    return units


# ------------------------------------------------------------------ build ---

def build_article(md_path: Path) -> dict:
    raw = md_path.read_text(encoding="utf-8")
    entry = parse_entry(md_path)
    provenance, blocks = split_blocks(raw)
    del provenance  # the preamble is surfaced through extract_note() below

    title = entry.title
    if " / " in title:
        zh_title, en_title = title.split(" / ", 1)
    else:
        zh_title, en_title = title, title

    body, toc = [], []
    for i, b in enumerate(blocks):
        en_html = strip_heading_ids(to_html("\n".join(b["en"]))).strip()
        zh_html = strip_heading_ids(to_html("\n".join(b["zh"]))).strip()
        if not en_html and not zh_html:
            continue
        uid = "u%d" % i
        level = b["level"]

        label_en = first_h2_text(en_html) or ("Section %d" % (i + 1))
        label_zh = first_h2_text(zh_html) or label_en
        # The chapter label is a language pair too, so the contents list follows
        # the article instead of always reading "中文 / English".
        toc.append(
            '<li><a href="#%s"><span class="lv">%s</span>'
            '<span class="p-zh">%s</span><span class="p-en">%s</span></a></li>'
            % (uid, esc(level), esc(label_zh), esc(label_en))
        )

        cls = "unit is-src" if level == "L5" else "unit"
        parts = ['<section class="%s" id="%s">' % (cls, uid)]
        if en_html:
            parts.append(
                '<div class="lang-block lang-en"><span class="lang-chip">EN</span>'
                '<div class="lang-body">%s</div></div>' % en_html
            )
        if zh_html:
            parts.append(
                '<div class="lang-block lang-zh"><span class="lang-chip">中</span>'
                '<div class="lang-body">%s</div></div>' % zh_html
            )
        parts.append("</section>")
        body.append("\n".join(parts))

    # The house-style notes sit ahead of the first marker; keep them visible so the
    # drafting status travels with the rendered page, and switch them with the
    # article language.
    note_zh, note_en = extract_notes(raw)
    if note_zh or note_en:
        note = '<p class="note">'
        if note_zh:
            note += '<span class="n-zh">%s</span>' % esc(note_zh)
        if note_en:
            note += '<span class="n-en">%s</span>' % esc(note_en)
        note += '</p>'
    else:
        note = ""

    # Dateline below the byline: 发表 / Published and 更新 / Updated, each half
    # switching with the article language like every other bilingual label.
    dates = extract_dates(raw)
    if dates:
        pub, upd = dates
        dates_html = ('<p class="dateline">'
                      '<span class="p-zh">发表</span><span class="p-en">Published</span>'
                      ' <b>%s</b><span class="sep">·</span>'
                      '<span class="p-zh">更新</span><span class="p-en">Updated</span>'
                      ' <b>%s</b></p>' % (esc(pub), esc(upd)))
    else:
        dates_html = ""

    cjk = sum(1 for c in raw if "\u4e00" <= c <= "\u9fff")
    en_words = len(re.findall(
        r"[A-Za-z][A-Za-z'-]*",
        " ".join(re.sub(r"<[^>]+>", " ", "\n".join(b["en"])) for b in blocks)))

    if "当证明不再稀缺" in title:
        kicker_zh, kicker_en = "长稿 · 七章全景", "Long-form · Seven chapters"
    else:
        kicker_zh, kicker_en = "综述 · Review", "Review · Survey"
    robots_meta = (
        '\n<meta name="robots" content="noindex, nofollow">'
        if md_path.stem in UNLISTED else ""
    )
    page = (PAGE
            .replace("__CSS__", CSS)
            .replace("__ROBOTS__", robots_meta)
            .replace("__JS__", JS)
            .replace("__TOC__", "\n      ".join(toc))
            .replace("__NOTE__", '<p class="note">%s</p>' % note if note else "")
            .replace("__DATES__", dates_html)
            .replace("__BODY__", "\n".join(body))
            .replace("__KICKER_ZH__", esc(kicker_zh))
            .replace("__KICKER_EN__", esc(kicker_en))
            .replace("__H1__", esc(zh_title))
            .replace("__SUB__", esc(en_title))
            .replace("__TITLE__", esc(zh_title))
            .replace("__TITLE_ZH__", esc(zh_title))
            .replace("__TITLE_EN__", esc(en_title))
            .replace("__DESC__", esc(en_title))
            .replace("__NAVTITLE__", "Math Clarification")
            .replace("__NAVZH__", "数学释疑 · 文章")
            .replace("__NAV_EN__", "Math Clarification · Essays"))

    return {
        "slug": md_path.stem,
        "page": page,
        "zh_title": zh_title,
        "en_title": en_title,
        "units": len(toc),
        "cjk": cjk,
        "en_words": en_words,
    }


def build_once(slugs=None):
    targets = sorted(p for p in ARTICLES.glob("*.md") if p.name != "README.md")
    if slugs:
        targets = [p for p in targets if p.stem in slugs]
    if not targets:
        print("no articles found in %s" % ARTICLES)
        return None

    OUT.mkdir(parents=True, exist_ok=True)
    DOCS_SITE.mkdir(parents=True, exist_ok=True)
    built = []
    for md in targets:
        info = build_article(md)
        dest = OUT / (info["slug"] + ".html")
        dest.write_text(info["page"], encoding="utf-8")
        published = DOCS_SITE / dest.name
        published.write_text(info["page"], encoding="utf-8")
        info["path"] = dest
        info["published"] = published
        built.append(info)
        print("wrote %-34s %6.1f KB  units=%2d  en~%5d words  zh %5d chars"
              % (dest.name, dest.stat().st_size / 1024, info["units"],
                 info["en_words"], info["cjk"]))

    cards = []
    for info in built:
        if info["slug"] in UNLISTED:
            continue  # published, but not discoverable from the landing page
        cards.append(
            '<article>\n'
            '  <h2><a href="%s.html"><span class="p-zh">%s</span>'
            '<span class="p-en">%s</span></a></h2>\n'
            '  <p class="meta"><span class="p-zh">%d 节 · 英文约 %s 词 · 中文约 %s 字</span>'
            '<span class="p-en">%d sections · ~%s English words · ~%s Chinese characters</span></p>\n'
            '  <a class="open" href="%s.html">'
            '<span class="p-zh">打开</span><span class="p-en">Open</span></a>\n'
            '</article>'
            % (info["slug"], esc(info["zh_title"]), esc(info["en_title"]),
               info["units"], "{:,}".format(info["en_words"]),
               "{:,}".format(info["cjk"]),
               info["units"], "{:,}".format(info["en_words"]),
               "{:,}".format(info["cjk"]), info["slug"])
        )

    idx = (INDEX
           .replace("__CSS__", CSS)
           .replace("__JS__", JS)
           .replace("__CARDS__", "\n".join(cards))
           .replace("__LEDE_ZH__", "本地静态页,双击即可阅读,无需启动服务。中英对照可随时切换。")
           .replace("__LEDE_EN__", "A local static page — double-click to read, no server needed. "
                                   "Switch between Chinese and English at any time.")
           .replace("__NAVTITLE__", "Math Clarification")
           .replace("__NAVZH__", "数学释疑 · 文章")
           .replace("__NAV_EN__", "Math Clarification · Essays")
           .replace("__TITLE__", "数学释疑 · 文章 / Math Clarification")
           .replace("__TITLE_ZH__", "数学释疑 · 文章")
           .replace("__TITLE_EN__", "Math Clarification"))
    dest = OUT / "index.html"
    dest.write_text(idx, encoding="utf-8")
    # Publish the same landing into docs/math_clarification/ so the root site's
    # "Math Clarification" pillar (href="math_clarification/") resolves on Pages
    # and lists every article. Links are sibling-relative, so the copy is live as-is.
    (DOCS_SITE / "index.html").write_text(idx, encoding="utf-8")
    print("wrote %-34s %6.1f KB  (%d articles)  -> published to %s"
          % (dest.name, dest.stat().st_size / 1024, len(built), DOCS_SITE))
    return dest


def snapshot():
    """(path, mtime, size) for every source article, for change detection."""
    return {
        p.name: (p.stat().st_mtime_ns, p.stat().st_size)
        for p in ARTICLES.glob("*.md")
        if p.name != "README.md"
    }


def watch(slugs=None, interval=1.0):
    """Rebuild whenever a source .md changes, so a browser refresh is enough."""
    import time
    print("watching %s (Ctrl+C to stop)" % ARTICLES)
    last = None
    while True:
        now = snapshot()
        if now != last:
            stamp = time.strftime("%H:%M:%S")
            print("\n[%s] change detected, rebuilding..." % stamp)
            try:
                build_once(slugs)
            except Exception as exc:  # keep watching through a bad edit
                print("build failed: %s: %s" % (type(exc).__name__, exc))
            last = snapshot()
        time.sleep(interval)


def main():
    args = sys.argv[1:]
    slugs = []
    if "--slug" in args:
        slugs = [args[args.index("--slug") + 1]]

    if "--watch" in args or "-w" in args:
        try:
            watch(slugs)
        except KeyboardInterrupt:
            print("\nstopped")
        return 0

    dest = build_once(slugs)
    if dest is None:
        return 1
    print("\nopen: %s" % dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
