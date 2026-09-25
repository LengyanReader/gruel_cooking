# -*- coding: utf-8 -*-
"""build_reading.py — P2 generator.

Fonts: JSON-in (site/books/authors/relations) -> HTML out (docs/reading_ia/).
Renders: per-book pages (read/books/<slug>.html), crop list page, archive page,
authors graph page.  Bilingual via data-zh/data-en spans + a shared lang toggle
(localStorage key from site.json).  Inline SVG visualizers only (no external deps).
"""
import json, os, html, sys, argparse, math, re
from operator import itemgetter

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
DATA = os.path.join(BASE, "data")
ART_DIR = os.path.join(ROOT, "docs", "reading_ia", "art")


def cover_art(slug):
    """Local cover image file (art/covers/<slug>.jpg|png) or None."""
    for ext in ("jpg", "png"):
        p = os.path.join(ART_DIR, "covers", slug + "." + ext)
        if os.path.exists(p):
            return p
    return None


def author_art(slug):
    """Local author portrait (art/authors/<slug>.jpg/png) or None."""
    for ext in ("jpg", "png"):
        p = os.path.join(ART_DIR, "authors", slug + "." + ext)
        if os.path.exists(p):
            return p
    return None

CONF_COLOR = {"✓": "#3E7C5A", "◐": "#A5811D", "○": "#6C8AAF", "✗": "#B0413E"}
EDGE_KIND = {
    "mirror": ("双身 mirror", "#8C4A77"),
    "parent": ("亲子 parent", "#3E5C76"),
    "kin": ("亲属 kin", "#6C8AAF"),
    "romance": ("恋人 romance", "#C0556B"),
    "alliance": ("结盟 alliance", "#7A8F6E"),
    "friend": ("挚友 friend", "#C9A227"),
    "colleague": ("同组 colleague", "#A5811D"),
    "cowrite": ("合著 co-write", "#8C6A4A"),
    "dialogue": ("对谈 dialogue", "#C9A227"),
    "evidence": ("实证 evidence", "#7A8F6E"),
    "witness": ("旁观 witness", "#6C8AAF"),
    "contrast": ("对照 contrast", "#777069"),
    "bond": ("羁绊 bond", "#8C4A77"),
}

CSS = """/* shared Reading & IA toolkit */
:root {
  --ink-deep:#26261F; --ink-mid:#4E4B42; --ink-soft:#7C7568; --ink-pale:#A89F90;
  --paper:#F7F1E3; --paper-soft:#EFE6D3; --paper-deep:#E7DCC4;
  --gold:#C9A227; --gold-soft:#E3C457; --gold-dim:#A5811D;
  --lapis:#3E5C76; --lapis-soft:#6C8AAF; --sage:#7A8F6E;
  --cond:#3E7C5A; --lueur:#A5811D;
  --ff-display:"LXGW WenKai","Noto Serif SC",serif;
  --ff-body:"Inter","LXGW WenKai","Noto Sans SC",sans-serif;
  --shadow-md:0 6px 20px rgba(38,38,31,.08);
}
body.lang-zh [data-en]{display:none!important}
body.lang-en [data-zh]{display:none!important}
body.lang-en [data-both] span[data-en]{display:inline!important}
body.lang-en [data-both] span[data-zh]{display:none!important}
body.lang-zh [data-both] span[data-zh]{display:inline!important}
body.lang-zh [data-both] span[data-en]{display:none!important}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased}
body{font-family:var(--ff-body);color:var(--ink-deep);background:var(--paper);line-height:1.85;overflow-x:hidden}
a{color:var(--lapis);text-decoration:none;transition:color .25s}
a:hover{color:var(--gold)}
.nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:.7rem 2rem;display:flex;align-items:center;justify-content:space-between;background:rgba(247,241,227,.85);backdrop-filter:blur(20px) saturate(1.3);-webkit-backdrop-filter:blur(20px) saturate(1.3);border-bottom:1px solid rgba(167,146,93,.25)}
.nav.scrolled{background:rgba(247,241,227,.97);box-shadow:0 2px 16px rgba(38,38,31,.07)}
.nav-brand{font-family:var(--ff-display);font-weight:700;font-size:1.15rem;color:var(--ink-deep);letter-spacing:.05em}
.nav-brand .sub{font-size:.66em;color:var(--ink-pale);margin-left:.55em;font-weight:400;letter-spacing:.12em}
.nav-right{display:flex;align-items:center;gap:1rem}
.nav-home{color:var(--ink-soft);font-size:.8rem;font-weight:500;border:1px solid rgba(167,146,93,.4);border-radius:18px;padding:4px 13px}
.nav-home:hover{color:var(--gold);border-color:var(--gold)}
.lang-toggle{display:flex;border-radius:20px;overflow:hidden;border:1px solid rgba(167,146,93,.45);font-size:.8rem;font-weight:500;cursor:pointer;background:var(--paper-soft)}
.lang-toggle button{border:none;padding:5px 14px;cursor:pointer;font-family:var(--ff-body);font-size:.8rem;font-weight:500;transition:all .25s;color:var(--ink-soft);background:transparent}
.lang-toggle button.active{background:linear-gradient(135deg,var(--gold),var(--gold-soft));color:#fff}
.hero{position:relative;padding:7.5rem 2rem 3.4rem;text-align:center;color:#F3EDE0;
  background:radial-gradient(700px 360px at 20% 10%,rgba(201,162,39,.14),transparent 60%),
    linear-gradient(170deg,#20253A 0%,#2A3350 28%,#3E5C76 52%,#8C8A6C 76%,#C9B98F 90%,var(--paper) 100%)}
.hero .kicker{font-size:.85rem;letter-spacing:.3em;color:var(--gold-soft);font-weight:500;margin-bottom:1rem}
.hero h1{font-family:var(--ff-display);font-size:clamp(1.9rem,4.6vw,3rem);font-weight:700;color:#F7F1E3;letter-spacing:.06em;line-height:1.3;margin-bottom:.4rem}
.hero h1 .zh{font-size:.85em;display:block;margin-bottom:.3rem;color:#E9E2CE}
.hero .subtitle{font-family:var(--ff-display);font-size:clamp(.95rem,2vw,1.2rem);color:#D9E1EA;font-weight:300;letter-spacing:.12em}
.hero .metachip{display:inline-flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:1.2rem}
.hero .metachip span{font-size:.74rem;letter-spacing:.08em;color:#D9E1EA;border:1px solid rgba(217,225,234,.35);border-radius:20px;padding:4px 12px;background:rgba(30,34,48,.25)}
.article{max-width:960px;margin:0 auto;padding:3rem 2rem 3.4rem}
h2.part{font-family:var(--ff-display);font-size:clamp(1.5rem,3.2vw,2rem);font-weight:700;color:var(--ink-deep);letter-spacing:.04em;margin:3.4rem 0 .3rem;text-align:center}
h2.part::after{content:"";display:block;width:54px;height:2px;margin:.8rem auto 1.2rem;background:linear-gradient(90deg,transparent,var(--gold),transparent);border-radius:1px}
h3.sec{font-family:var(--ff-display);font-size:1.18rem;font-weight:700;color:var(--lapis);margin:2.2rem 0 .6rem;letter-spacing:.03em}
.srcnote{font-size:.84rem;color:var(--ink-soft);background:var(--paper-soft);border:1px solid rgba(167,146,93,.3);border-radius:12px;padding:.9rem 1.1rem;margin:1rem 0 1.8rem}
.srcnote code{font-family:"Inter",monospace;font-size:.78rem;color:var(--gold-dim)}
.readban{font-size:.84rem;color:#5A5E33;background:#ECEFD8;border:1px solid rgba(167,146,93,.35);border-left:4px solid var(--gold);border-radius:10px;padding:.7rem 1rem;margin:.6rem 0 1.4rem}
.card{background:var(--paper-soft);border:1px solid rgba(167,146,93,.3);border-radius:16px;padding:1.3rem 1.5rem;margin:1.1rem 0;box-shadow:var(--shadow-md);position:relative;overflow:hidden}
.card::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--gold-dim),var(--gold-soft));opacity:.85}
.ledger{width:100%;border-collapse:collapse;font-size:.86rem;background:var(--paper-soft);border:1px solid rgba(167,146,93,.3);border-radius:14px;overflow:hidden}
.ledger th,.ledger td{padding:.6rem .85rem;text-align:left;border-bottom:1px solid rgba(167,146,93,.22);vertical-align:top}
.ledger th{font-family:var(--ff-display);font-size:.8rem;font-weight:700;color:var(--gold-dim);background:var(--paper-deep);letter-spacing:.04em}
.ledger tr:last-child td{border-bottom:none}
.ledger td.conf{font-size:.78rem;white-space:nowrap}
.tablewrap{overflow-x:auto;margin:1rem 0 1.8rem;border-radius:14px}
.conf{font-family:"Inter",monospace;font-weight:700}
.conf.c-ok{color:var(--cond)} .conf.c-part{color:var(--lueur)}
.tok{margin-left:.35rem}
.quote{border-left:3px solid var(--gold-soft);background:var(--paper-soft);border-radius:0 10px 10px 0;padding:.7rem 1rem;margin:.7rem 0}
.quote .orig{font-style:italic;color:var(--ink-deep)}
.quote .trs{color:var(--ink-soft);font-size:.9rem;margin-top:.2rem}
.quote .src{color:var(--ink-pale);font-size:.76rem;margin-top:.25rem}
.exq{background:var(--paper-soft);border:1px solid rgba(167,146,93,.3);border-left:3px solid var(--lapis);border-radius:0 12px 12px 0;padding:.8rem 1.05rem;margin:.8rem 0}
.exq .orig{font-style:italic;color:var(--ink-deep);font-size:1.02rem;line-height:1.6}
.exq .lang{display:inline-block;font-size:.68rem;font-weight:700;letter-spacing:.06em;color:var(--ink-pale);border:1px solid rgba(167,146,93,.4);border-radius:8px;padding:.05rem .5rem;margin-left:.45rem;vertical-align:.18rem}
.exq .tr{color:var(--ink-soft);font-size:.9rem;margin-top:.3rem;line-height:1.55}
.exq .tr [data-en]{font-style:italic}
.exq .note{background:var(--paper-deep);border-radius:8px;padding:.5rem .7rem;margin-top:.45rem;font-size:.88rem;color:var(--ink-deep);line-height:1.6}
.exq .note::before{content:"✎ ";color:var(--lapis)}
.exq .src{color:var(--ink-pale);font-size:.76rem;margin-top:.3rem}
.exq .mname{font-weight:700;letter-spacing:.02em;color:var(--ink-deep);margin-bottom:.35rem}
.exq .mname [data-en]{font-weight:400;color:var(--ink-soft);font-style:italic}
.exq .mnote{background:var(--paper-deep);border-radius:8px;padding:.5rem .7rem;margin:.4rem 0;font-size:.88rem;color:var(--ink-deep);line-height:1.6}
.exq .mnote [data-en]{font-style:italic;color:var(--ink-soft)}
.diagram{background:var(--paper-soft);border:1px solid rgba(167,146,93,.3);border-radius:16px;padding:1rem;margin:1.2rem 0;overflow-x:auto}
.diagram svg{display:block;margin:0 auto;max-width:100%;height:auto}
.diagram .cap{font-size:.8rem;color:var(--ink-pale);text-align:center;margin-top:.5rem;letter-spacing:.06em}
.links{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:2.2rem 0 1rem}
.pill{display:inline-block;font-size:.85rem;font-weight:500;color:var(--ink-soft);border:1px solid rgba(167,146,93,.45);border-radius:22px;padding:7px 18px;background:var(--paper-soft);transition:all .25s}
.pill:hover{color:#fff;background:linear-gradient(135deg,var(--gold),var(--gold-dim));border-color:var(--gold)}
.footer{text-align:center;padding:2.6rem 2rem 2.2rem;color:var(--ink-pale);font-size:.875rem;border-top:1px solid rgba(167,146,93,.3);background:var(--paper)}
.gapbox{background:var(--paper-deep);border:1px solid rgba(167,146,93,.35);border-radius:16px;padding:1.4rem 1.6rem;margin:1.4rem 0}
.gapbox .v-line{font-family:var(--ff-display);font-size:1.12rem;font-weight:700;color:var(--ink-deep);margin-bottom:.5rem}
.gapbox .v-line .badge{display:inline-block;font-family:var(--ff-body);font-size:.74rem;font-weight:700;letter-spacing:.08em;background:linear-gradient(135deg,var(--gold),var(--gold-dim));color:#fff;border-radius:20px;padding:3px 12px;margin-right:.6rem;vertical-align:2px}
.gapbox ul{list-style:none}
.gapbox ul li{position:relative;padding-left:1.25rem;margin-bottom:.5rem;font-size:.93rem;color:var(--ink-mid)}
.gapbox ul li::before{content:"";position:absolute;left:0;top:.62rem;width:7px;height:7px;border-radius:50%;background:var(--lapis)}
/* Goodreads × Douban hybrid book card */
.bkcard{display:grid;grid-template-columns:126px 1fr;gap:1.15rem;background:linear-gradient(180deg,#FBF6EA,#F2EAD8);border:1px solid rgba(167,146,93,.35);border-radius:14px;padding:1.15rem 1.25rem;margin:1.3rem 0;box-shadow:0 4px 18px rgba(38,38,31,.08);position:relative;overflow:hidden}
.bkcard::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--gold-dim),var(--gold-soft));opacity:.9}
.bkcover{width:126px;align-self:start;filter:drop-shadow(0 6px 14px rgba(38,38,31,.25))}
.bkcover svg,.bkcover img{display:block;width:100%;height:auto;border-radius:6px}
.bkcover img{object-fit:cover}
.bkhead{display:flex;align-items:baseline;gap:.55rem;flex-wrap:wrap}
.bknum{font-family:var(--ff-display);font-size:.76rem;color:var(--gold-dim);letter-spacing:.14em}
.bktitle{font-family:var(--ff-display);font-size:1.28rem;font-weight:700;color:var(--ink-deep);line-height:1.35;margin:.1rem 0 .05rem}
.bktitle a{color:inherit}.bktitle a:hover{color:var(--gold)}
.bktitle .orig{color:var(--lapis);font-weight:400;font-size:.9em}
.bkauthor{font-size:.86rem;color:var(--ink-mid)}
.bkauthor a{color:var(--lapis)}
.aface{width:44px;height:44px;min-width:44px;border-radius:50%;object-fit:cover;border:2px solid rgba(201,162,39,.5);box-shadow:0 3px 9px rgba(38,38,31,.18)}
.aface.sm{width:30px;height:30px;min-width:30px;border-width:1.5px;box-shadow:none;vertical-align:middle;margin-right:.3rem}
.anode{display:flex;gap:.85rem;align-items:center}
.bkrate{display:flex;align-items:center;gap:.5rem;flex-wrap:wrap;margin:.4rem 0 .05rem}
.bkrate .score{font-family:var(--ff-display);font-weight:700;font-size:1.2rem;color:#C77E1F}
.bkrate .cnt{font-size:.74rem;color:var(--ink-pale)}
.bkrate .cnt .n{color:var(--ink-soft);font-weight:600}
.bkmeta{font-size:.79rem;color:var(--ink-soft);margin-top:.15rem}
.bktags{display:flex;gap:.4rem;flex-wrap:wrap;margin:.5rem 0 .1rem}
.tag{font-size:.7rem;border:1px solid rgba(167,146,93,.5);border-radius:10px;padding:1px 9px;color:var(--gold-dim);background:rgba(255,255,255,.55);letter-spacing:.03em}
.tag.pub{color:#fff;border-color:transparent;font-weight:600}
.tag.cn{font-weight:700;color:#fff;border-color:transparent}
.status{font-size:.7rem;font-weight:700;border-radius:9px;padding:2px 9px;letter-spacing:.05em}
.status.reading{background:#E4EFDD;color:#2F6B4A;border:1px solid #A9C6A0}
.status.unread{background:#F6EDE4;color:#96674A;border:1px solid #DCC3AC}
.status.half{background:#E7EDF5;color:#3E5C76;border:1px solid #A9BCD0}
.bkwhy{font-size:.9rem;color:var(--ink-soft);font-style:italic;margin:.4rem 0 .1rem}
.bkact{display:flex;gap:.55rem;flex-wrap:wrap;align-items:center;margin-top:.55rem}
.pill.sm{font-size:.77rem;padding:4px 14px}
.pill.ext::after{content:" ↗";font-size:.72em;opacity:.75}
.pill.on{color:#fff;background:linear-gradient(135deg,var(--gold),var(--gold-dim));border-color:var(--gold)}
/* glossary & methods chips */
.modechip{display:inline-block;font-size:.68rem;font-weight:700;letter-spacing:.06em;border-radius:20px;padding:2px 11px;color:#fff;background:#3E5C76;margin-right:.35rem}
.modechip.tradition{background:#8C4A77}
.modechip.archetype{background:#C9880F}
.modechip.practice{background:#7A8F6E}
.domchip{display:inline-block;font-size:.68rem;font-weight:500;letter-spacing:.05em;border-radius:20px;padding:2px 11px;color:#7C7568;border:1px solid rgba(167,146,93,.45);margin-right:.35rem}
.ref{display:inline-block;font-size:.72rem;font-weight:600;color:var(--gold-dim);background:var(--paper);border:1px dashed rgba(167,146,93,.5);border-radius:7px;padding:0 7px;margin:.1rem .2rem;vertical-align:1px}
.term-line{margin:.3rem 0;font-size:.9rem}
.term-line b{font-family:var(--ff-display);color:var(--ink-deep);font-weight:700}
.method-num{font-family:var(--ff-display);font-weight:700;color:#fff;background:linear-gradient(135deg,var(--gold),var(--gold-dim));border-radius:50%;width:26px;height:26px;display:inline-flex;align-items:center;justify-content:center;font-size:.78rem;margin-right:.5rem;vertical-align:2px}
.tl-list{display:flex;flex-direction:column;gap:.45rem;margin:.7rem 0 1.4rem}
.tl-list a{display:flex;justify-content:space-between;gap:1rem;align-items:baseline;font-size:.86rem;background:var(--paper-soft);border:1px solid rgba(167,146,93,.35);border-radius:11px;padding:.55rem .9rem;color:var(--lapis)}
.tl-list a:hover{border-color:var(--gold);color:var(--gold);background:#FFF8EC}
.tl-list a .dom{font-size:.72rem;color:var(--ink-pale);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:44%}
.pubviz{display:grid;gap:.55rem;margin:.8rem 0 1.6rem}
.pubviz .row{display:grid;grid-template-columns:150px 1fr;gap:.7rem;align-items:center;font-size:.83rem}
.pubviz .pname{display:flex;align-items:center;gap:.5rem;font-weight:600;color:var(--ink-deep);justify-content:flex-end;text-align:right}
.pubviz .dot{width:11px;height:11px;border-radius:3px;flex:none;box-shadow:0 1px 3px rgba(38,38,31,.25)}
.pubviz .bar{display:flex;gap:.5rem;align-items:center;min-height:24px}
.pubviz .blk{height:22px;border-radius:5px;box-shadow:inset 0 -6px 12px rgba(0,0,0,.12);position:relative;min-width:34px}
.pubviz .blk span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:.64rem;color:#fff;font-weight:700;text-shadow:0 1px 2px rgba(0,0,0,.4);white-space:nowrap;padding:0 4px;overflow:hidden}
.pubviz .cnt{font-size:.75rem;color:var(--ink-pale)}
@media (max-width:768px){.bkcard{grid-template-columns:92px 1fr;padding:.9rem;gap:.8rem}.bkcover{width:92px}.pubviz .row{grid-template-columns:110px 1fr}}
@media (max-width:768px){.nav{padding:.6rem 1rem}.hero{padding:6rem 1rem 2.6rem}.article{padding:2.4rem 1.1rem 3rem}}
"""

SCRIPT = """
const nav=document.getElementById('nav');
window.addEventListener('scroll',()=>{nav.classList.toggle('scrolled',window.scrollY>60)});
const toggle=document.getElementById('langToggle');
const buttons=toggle.querySelectorAll('button');
function setLang(lang){document.body.className='lang-'+lang;buttons.forEach(b=>b.classList.toggle('active',b.dataset.lang===lang));localStorage.setItem('__STORAGE__',lang);document.documentElement.lang=(lang==='zh')?'zh':'en';}
const saved=localStorage.getItem('__STORAGE__');
if(saved)setLang(saved);
buttons.forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));
"""

STORAGE_KEY = "zhzz-reading-lang"


def esc(s):
    return html.escape(str(s), quote=True)


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def load_md_sections(rel_path):
    """Parse a Markdown file of '## <title>' sections with '- **key**: value' bullets.
    Returns list of {title, items{key: value}} in file order.
    术语架/方法论源（单一来源 Markdown）→ 生成 HTML 页。"""
    path = os.path.join(ROOT, rel_path)
    sections = []
    if not os.path.exists(path):
        return sections
    cur = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("## "):
                title = line[3:].strip()
                if title.startswith("Format") or title.startswith("格式"):
                    cur = None
                    continue
                cur = {"title": title, "items": {}}
                sections.append(cur)
            elif cur is not None:
                m = re.match(r"^\s*-\s*\*\*([^*]+)\*\*:\s*(.*)$", line)
                if m:
                    key = m.group(1).replace("  ", " ").strip()
                    cur["items"][key] = m.group(2).strip()
    return sections


def wl(text):
    """Render [[...]] wikilinks as non-dangling reference chips (data-layer pointers)."""
    if not text:
        return ""
    out = []
    for part in re.split(r"(\[\[[^\]]+\]\])", text):
        if part.startswith("[[") and part.endswith("]]"):
            ref = part[2:-2].strip()
            slug = ref.split("/")[-1]
            out.append(f'<span class="ref">{esc(slug)}</span>')
        else:
            out.append(esc(part))
    return "".join(out)


def conf_mark(text):
    """Pull a trailing ✓◐○✗ confidence mark out of a source string for a colored chip."""
    m = re.search(r"([✓◐○✗])", text)
    if not m:
        return ""
    c = m.group(1)
    return '<span class="tok">' + conf_token(c) + "</span>"


# ---------- helpers ----------
def zh_en(zh, en, tag="div"):
    if tag == "span":
        return ('<span data-both><span data-zh>%s</span><span data-en>%s</span></span>') % (esc(zh), esc(en))
    return ('<div data-zh>%s</div><div data-en>%s</div>') % (esc(zh), esc(en))


def srcnote(zh, en):
    return '<div class="srcnote"><div data-zh>%s</div><div data-en>%s</div></div>' % (zh, en)


def conf_token(c):
    r = {"✓": "c-ok", "◐": "c-part", "○": "c-part", "✗": "c-bad"}.get(c, "c-part")
    return '<span class="conf %s">%s</span>' % (r, esc(c))


# ---------- hybrid card helpers (Goodreads × Douban) ----------
PUB_COLOR = {
    "Knopf": "#8C4A77", "HarperAvenue": "#6C8AAF", "Picador": "#7A8F6E",
    "Flammarion": "#3E5C76", "Calmann-Lévy": "#A5811D", "Calmann-Levy": "#A5811D",
    "幻冬舎新書": "#B0413E", "Gentosha": "#B0413E",
    "Allen Lane": "#1A3C5E", "Penguin": "#1A3C5E", "Viking": "#2D5A3F",
}
COUNTRY_COLOR = {"美国": "#3E5C76", "法国": "#1F3A63", "日本": "#B0413E", "英国": "#1A3C5E", "欧洲": "#4E4B42"}


def _esc_at(s):
    return s.replace("@", " at ")


def stars_svg(score, size=15, uid="r"):
    """5-star Goodreads/Douban-style rating row as inline SVG."""
    if not score:
        return ""
    w = size * 5 + 4 * 3
    out = [f'<svg viewBox="0 0 {w} {size}" width="{w}" height="{size}" role="img" aria-label="{score}/5" xmlns="http://www.w3.org/2000/svg">']
    star_d = "M7,0.6 L8.9,4.6 L13.2,5.2 L10.1,8.3 L10.8,12.6 L7,10.5 L3.2,12.6 L3.9,8.3 L0.8,5.2 L5.1,4.6 Z"
    for i in range(5):
        x = i * (size / 15 * 15 + 3) if False else i * (size + 3)
        frac = max(0.0, min(1.0, score - i))
        clip = f"{uid}{i}"
        out.append(f'<g transform="translate({x},0) scale({size/13:.4f})">')
        out.append(f'<path d="{star_d}" fill="#E4DAC4" stroke="#C9BFA6" stroke-width="0.6"/>')
        if frac >= 0.999:
            out.append(f'<path d="{star_d}" fill="#E8A317" stroke="#C9880F" stroke-width="0.6"/>')
        elif frac > 0.05:
            out.append(f'<defs><clipPath id="{clip}"><rect x="0" y="0" width="{13.2*frac:.2f}" height="14"/></clipPath></defs>')
            out.append(f'<path d="{star_d}" fill="#E8A317" stroke="#C9880F" stroke-width="0.6" clip-path="url(#{clip})"/>')
        out.append('</g>')
    out.append('</svg>')
    return "".join(out)


def rating_line(b, cls=""):
    """Goodreads-style score row: stars + score + counts (Douban). Bilingual."""
    r = b.get("rating") or {}
    gr = r.get("goodreads")
    if gr:
        score = gr.get("score")
        stars = stars_svg(score, uid="s" + b["slug"][:6]) if score else ""
        score_el = f'<span class="score">{score:.2f}</span>' if score else ""
        cnt_zh, cnt_en = [], []
        if gr.get("count"):
            n = f'{gr["count"]:,}'
            cnt_zh.append(f'<span class="n">{n}</span> 评分')
            cnt_en.append(f'<span class="n">{n}</span> ratings')
        if gr.get("reviews"):
            n = f'{gr["reviews"]:,}'
            cnt_zh.append(f'<span class="n">{n}</span> 评论')
            cnt_en.append(f'<span class="n">{n}</span> reviews')
        note_zh = r.get("note_zh", "")
        note_en = r.get("note_en", "")
        zh = stars + score_el + '<span class="cnt">' + " · ".join(cnt_zh) + '</span>'
        if note_zh:
            zh += f'<span class="cnt" style="color:var(--ink-pale)">{esc(note_zh)}</span>'
        en = stars + score_el + '<span class="cnt">' + " · ".join(cnt_en) + '</span>'
        if note_en:
            en += f'<span class="cnt" style="color:var(--ink-pale)">{esc(note_en)}</span>'
        return f'<div class="bkrate {cls}" data-both><span data-zh>{zh}</span><span data-en>{en}</span></div>'
    sales = r.get("sales")
    if sales:
        copies = sales.get("copies", "") or "—"
        copies = re.sub(r"(\d)(?=(\d{3})+(\+|$))", r"\1,", copies)
        note_zh = sales.get("note_zh", "")
        note_en = sales.get("note_en", "")
        zh = (f'<span class="score">{esc(copies)}</span><span class="cnt"> 部销量 · {esc(note_zh)}</span>'
              if note_zh else f'<span class="score">{esc(copies)}</span><span class="cnt"> 部销量</span>')
        en = (f'<span class="score">{esc(copies)}</span><span class="cnt"> copies sold · {esc(note_en)}</span>'
              if note_en else f'<span class="score">{esc(copies)}</span><span class="cnt"> copies sold</span>')
        return f'<div class="bkrate {cls}" data-both><span data-zh>{zh}</span><span data-en>{en}</span></div>'
    return ""


def read_chip(b):
    """Douban-style shelf state: 想读 / 在读 / 读过."""
    rs = b.get("read_status", "")
    if "通读中" in rs:
        zh, en, cls = "在读", "currently reading", "reading"
    elif "读完" in rs or "已读" in rs:
        zh, en, cls = "读过", "read", "reading"
    else:
        zh, en, cls = "想读 / 未通读", "want to read / not finished", "unread"
    return f'<span class="status {cls}" data-both><span data-zh>{esc(zh)}</span><span data-en>{esc(en)}</span></span>'


def pub_key(publisher):
    """Primary publisher name (first of a multi-territory line)."""
    return publisher.split(" · ")[0].split(" (")[0].strip()


def pub_color(name):
    for k, v in PUB_COLOR.items():
        if k.lower() in name.lower():
            return v
    return "#777069"


def svg_cover(b, w=126, h=178):
    """Inline SVG book cover: country-coded field, vertical title, author, imprint."""
    bg = COUNTRY_COLOR.get(b.get("country", ""), "#3E5C76")
    accent = pub_color(pub_key(b.get("publisher", "")))
    title = b["title_orig"]
    author = b["author"].split(" & ")[0].split(" ")[-1]
    imprint = pub_key(b.get("publisher", ""))
    num = b.get("num", "")
    # wrap title into short vertical lines
    words = title.split()
    lines, cur = [], ""
    for w_ in words:
        if len(cur) + len(w_) + (1 if cur else 0) <= 11:
            cur = (cur + " " + w_).strip()
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    if len(lines) > 4:
        lines = lines[:4]
        lines[-1] += "…"
    k = h / 178.0           # height scale for small covers
    cx = w / 2.0 + 4
    sf = lambda v: int(v * k * 100) / 100.0
    out = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="cover {esc(title)}">']
    out.append(f'<rect x="0" y="0" width="{w}" height="{h}" rx="5" fill="{bg}"/>')
    out.append(f'<rect x="0" y="0" width="9" height="{h}" fill="{accent}"/>')
    # inner frame
    out.append(f'<rect x="17" y="{sf(10)}" width="{w-30}" height="{h-sf(20)}" fill="none" stroke="rgba(255,255,255,.35)" stroke-width="1"/>')
    # num badge
    out.append(f'<text x="{w-16}" y="{sf(30)}" text-anchor="end" font-family="LXGW WenKai,serif" font-size="{sf(15)}" font-weight="700" fill="#E9D89B">{esc(num)}</text>')
    # title lines centered
    y0 = sf(52)
    ctx_fs = sf(15)
    for i, ln in enumerate(lines):
        out.append(f'<text x="{cx}" y="{y0+i*sf(20)}" text-anchor="middle" font-family="LXGW WenKai,serif" font-size="{ctx_fs}" font-weight="700" fill="#F7F1E3">{esc(ln)}</text>')
    yb = y0 + len(lines) * sf(20) + sf(6)
    out.append(f'<line x1="24" y1="{yb}" x2="{w-20}" y2="{yb}" stroke="rgba(233,216,155,.7)" stroke-width="1"/>')
    out.append(f'<text x="{cx}" y="{yb+sf(20)}" text-anchor="middle" font-family="Inter,sans-serif" font-size="{sf(9.5)}" fill="#D9E1EA">{esc(author)}</text>')
    out.append(f'<text x="{cx}" y="{yb+sf(36)}" text-anchor="middle" font-family="Inter,sans-serif" font-size="{sf(8)}" fill="rgba(217,225,234,.75)">{esc(imprint[:18])} · {esc(b.get("year",""))}</text>')
    # spine label at bottom
    out.append(f'<text x="{cx}" y="{h-sf(18)}" text-anchor="middle" font-family="Inter,sans-serif" font-size="{sf(7.5)}" letter-spacing="1.5" fill="rgba(247,241,227,.6)">{esc(b.get("lang","").upper())} · {esc(b.get("country",""))}</text>')
    out.append('</svg>')
    return "".join(out)


def pubviz_svg(books, width=760):
    """Publisher × books bar (Goodreads-like shelf visualization): one colored block per book, width ∝ pages."""
    groups = {}
    for b in books:
        k = pub_key(b.get("publisher", ""))
        groups.setdefault(k, []).append(b)
    rows = []
    maxp = 1
    for k, bs in groups.items():
        for b in bs:
            try:
                p = int(str(b.get("pages", "0")).split()[0])
            except Exception:
                p = 300
            maxp = max(maxp, p)
        rows.append((k, bs))
    html_out = ['<div class="pubviz">']
    for k, bs in rows:
        col = pub_color(k)
        blocks = []
        for b in bs:
            try:
                p = int(str(b.get("pages", "0")).split()[0])
            except Exception:
                p = 300
            wpx = max(34, int(150 + 330 * p / maxp))
            short = b["title_orig"][:16]
            blocks.append(f'<div class="blk" style="background:{col};width:{wpx}px" title="{esc(b["title_orig"])} · {p}pp"><span>{esc(short)}</span></div>')
        html_out.append(f'<div class="row"><div class="pname"><span class="dot" style="background:{col}"></span>{esc(k)}</div>'
                        f'<div class="bar">{"".join(blocks)}<span class="cnt">×{len(bs)}</span></div></div>')
    html_out.append('</div>')
    return "".join(html_out)


def access_route(dom):
    """Classify a link's route from its domain — metadata only, never content."""
    d = dom.lower()
    if any(s in d for s in ("penguinrandomhouse", "flammarion", "calmann", "gentosha", "gallimard", "actes-sud")):
        return ("官方出版页 · Official publisher", "✓")
    if any(s in d for s in ("overdrive", "libby", "biblio", "leslibraires")):
        return ("图书馆 · 借阅记录 Library", "◐")
    if any(s in d for s in ("goodreads", "bookmeter")):
        return ("读者平台 · Reader community", "◐")
    if any(s in d for s in ("npr", "today", "wfae", "irishtimes", "lithub", "theguardian", "elle", "lepoint", "liberation", "lefigaro", "letemps", "lacroix", "telegramme")):
        return ("媒体 · 授权转载 Media", "◐")
    return ("其他 · Other", "○")


def textlinks_block(b):
    """Access to the original — licensed previews & links only, no scraped content
    and no unlicensed mirrors. Each entry: bilingual label + route chip + conf."""
    tls = b.get("textlinks") or []
    if not tls:
        return ""
    rows = []
    for t in tls:
        dom = t["url"].split("/")[2]
        route, tconf = access_route(dom)
        ccol = CONF_COLOR.get(tconf, "#777069")
        rows.append(f'<a href="{esc(t["url"])}" target="_blank" rel="noopener">'
                    f'<span data-zh>{esc(t["zh"])}</span><span data-en>{esc(t["en"])}</span>'
                    f'<span class="dom">{esc(dom)} ↗</span>'
                    f'<span class="rtag" style="color:{ccol}">{esc(route)} · {tconf}</span></a>')
    note = ('本页仅收录官方预览 / 授权试读与图书馆记录等可核验出处，'
            '不提供未经授权的全文镜像。全文以正式出版与馆藏借阅为准。',
            'This page links only verifiable sources — official previews, licensed '
            'samples, and library/OverDrive records. No unlicensed full-text mirrors. '
            'The complete original is obtained via the published edition or library loan.')
    return ('<h3 class="sec" data-both><span data-zh>原文获取 · Accessing the original</span>'
            '<span data-en>Accessing the original</span></h3>'
            '<p class="tl-note">' + zh_en(note[0], note[1], "span") + '</p>'
            '<div class="tl-list">' + "".join(rows) + '</div>')


def page(title, hero_kicker, hero_h1, hero_sub, chips, body, up_rel="..", hero_h1_en=None, hero_sub_en=None, nav_sub_zh="", nav_sub_en=""):
    nav_home = up_rel + "/index.html"
    hl = ' '.join('<span>%s</span>' % esc(c) for c in chips)
    script = SCRIPT.replace("__STORAGE__", STORAGE_KEY)
    h1_en = hero_h1_en if hero_h1_en is not None else hero_h1
    sub_en = hero_sub_en if hero_sub_en is not None else hero_sub
    ns_zh = nav_sub_zh or ""
    ns_en = nav_sub_en or ns_zh
    return f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)} | 阅读与智识</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai:wght@300;400;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body class="lang-zh">

<nav class="nav" id="nav">
  <div class="nav-brand" data-both><span data-zh>{esc(hero_kicker)}</span><span data-en>{esc(hero_kicker)}</span><span class="sub" data-both><span data-zh>{esc(ns_zh)}</span><span data-en>{esc(ns_en)}</span></span></div>
  <div class="nav-right">
    <a class="nav-home" href="{nav_home}">
      <span data-zh>← 阅读与智识 首页</span><span data-en>← Reading &amp; IA</span>
    </a>
    <div class="lang-toggle" id="langToggle">
      <button class="active" data-lang="zh">中</button><button data-lang="en">EN</button>
    </div>
  </div>
</nav>

<section class="hero">
  <p class="kicker">READING &amp; IA — {esc(hero_kicker)}</p>
  <h1><span data-zh>{esc(hero_h1)}</span><span data-en>{esc(h1_en)}</span></h1>
  <div class="subtitle" data-both><span data-zh>{esc(hero_sub)}</span><span data-en>{esc(sub_en)}</span></div>
  <div class="metachip">{hl}</div>
</section>

<div class="article">
{body}
</div>

<footer class="footer">
  <p data-zh>一书一卡，一人一卡；读完每一本，至少落下一个延伸线索 · 阅读与智识</p>
  <p data-en>One card per book, one per author; every finished book drops a lead · Reading &amp; IA</p>
</footer>

<script>{script}</script>
</body>
</html>
"""


# ---------- SVG: plot flow ----------
def _cjk_w(t):
    return sum(13 if ord(c) > 0x2E80 else 6.8 for c in t)


def _wrap(t, maxw):
    if not t:
        return [""]
    lines = []
    cur = ""
    for c in t:
        if _cjk_w(cur) + _cjk_w(c) > maxw and cur:
            lines.append(cur)
            cur = c
        else:
            cur += c
    if cur:
        lines.append(cur)
    return lines if lines else [""]


def svg_plot_flow(nodes, width=860):
    if not nodes:
        return ''
    x = 72
    y0 = 26
    gap = 30
    box_w = 716
    txt_w = 560
    zh_lh = 17
    en_lh = 13
    boxes = []
    for nd in nodes:
        zl = _wrap(nd["zh"], txt_w)
        el = _wrap(nd["en"], txt_w)
        h = 26 + (len(zl) - 1) * zh_lh + 12 + (len(el) - 1) * en_lh + 14 + 12
        boxes.append((zl, el, h))
    H = 2 * y0 + sum(b[2] for b in boxes) + gap * (len(boxes) - 1) + 10
    out = [f'<svg viewBox="0 0 {width} {H}" role="img" aria-label="plot flow" xmlns="http://www.w3.org/2000/svg">']
    cy = y0
    for i, (nd, (zl, el, h)) in enumerate(zip(nodes, boxes), 1):
        yb = cy + h
        fill = "#FFF8EC" if i % 2 else "#EFE6D3"
        stroke = "#C9A227" if i == len(nodes) else "#A5811D"
        out.append(f'<rect x="{x}" y="{cy}" width="{box_w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.4"{' class="cn"' if i == len(nodes) else ''}/>')
        out.append(f'<text x="{x+16}" y="{cy+22}" font-family="LXGW WenKai,serif" font-size="14" font-weight="700" fill="#A5811D">{i}</text>')
        # zh
        ty = cy + 24
        for ln in zl:
            out.append(f'<text x="{x+40}" y="{ty}" font-family="LXGW WenKai,serif" font-size="12.5" fill="#26261F">{esc(ln)}</text>')
            ty += zh_lh
        ty += 4
        # en
        for ln in el:
            out.append(f'<text x="{x+40}" y="{ty}" font-family="Inter,sans-serif" font-size="11" fill="#7C7568" font-style="italic">{esc(ln)}</text>')
            ty += en_lh
        # conf
        if nd.get("conf"):
            ccol = CONF_COLOR.get(nd["conf"], "#777069")
            out.append(f'<text x="{x+box_w-14}" y="{cy+22}" text-anchor="end" font-family="monospace" font-size="11" font-weight="700" fill="{ccol}">{esc(nd["conf"])}</text>')
        if i < len(nodes):
            out.append(f'<line class="eflow" x1="{x+box_w/2}" y1="{yb}" x2="{x+box_w/2}" y2="{yb+gap}" stroke="#C9A227" stroke-width="2" marker-end="url(#arw)"/>')
        cy = yb + gap
    out.append('<defs><marker id="arw" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="#C9A227"/></marker>'
                '<style>@media (prefers-reduced-motion: no-preference){.eflow{animation:pfdraw 7s linear infinite}.cn{animation:pfpulse 4.2s ease-in-out infinite}}'
                '@keyframes pfdraw{to{stroke-dashoffset:-132}}@keyframes pfpulse{0%,100%{opacity:1}50%{opacity:.45}}'
                '@media print{.eflow,.cn{animation:none}}</style></defs>')
    out.append('</svg>')
    return "\n".join(out)


# ---------- SVG: character relationship ----------
def svg_charedge(book, width=900):
    chars = book.get("characters", [])
    edges = book.get("charedges", [])
    if not chars:
        return ''
    groups = []
    seen = []
    for c in chars:
        g = c.get("group", "?")
        if g not in seen:
            seen.append(g); groups.append(g)
    by_id = {c["id"]: c for c in chars}
    found = [(c["id"]) for c in chars]
    col_w = 210
    W = max(560, 90 + col_w * len(groups) + 40)
    rows = max(len([c for c in chars if c["group"] == g]) or 1 for g in groups)
    row_h = 62
    H = 40 + rows * row_h + 20
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="character relationship" xmlns="http://www.w3.org/2000/svg">']
    colx = {}
    for i, g in enumerate(groups):
        colx[g] = 60 + i * col_w / (len(groups)) * 1  # scale below
    # recompute with scaling to fit width
    step = (W - 120) / max(1, len(groups) - 1) if len(groups) > 1 else 0
    pos = {}
    for g, i in zip(groups, range(len(groups))):
        colx[g] = 80 + i * min(step, col_w)
    for g in groups:
        members = [c for c in chars if c["group"] == g]
        for j, c in enumerate(members):
            pos[c["id"]] = (colx[g], 46 + j * row_h)
            # group label
            out.append(f'<text x="{colx[g]}" y="28" text-anchor="middle" font-family="LXGW WenKai,serif" font-size="13.5" font-weight="700" fill="#A5811D">{g}</text>')
            # node
            out.append(f'<rect x="{colx[g]-62}" y="{pos[c["id"]][1]-16}" width="124" height="32" rx="16" fill="#FFF8EC" stroke="#C9A227" stroke-width="1.3"/>')
            out.append(f'<text x="{colx[g]}" y="{pos[c["id"]][1]+1}" text-anchor="middle" font-family="LXGW WenKai,serif" font-size="12.5" fill="#26261F">{c["name"]}</text>')
    for a, b, kind, note in edges:
        if a not in pos or b not in pos:
            continue
        (ax, ay), (bx, by) = pos[a], pos[b]
        klabel, kcol = EDGE_KIND.get(kind, (kind, "#8C8C8C"))
        dash = "4 3" if kind in ("witness", "dialogue", "contrast", "evidence", "colleague") else "1"
        my = (ay + by) / 2
        out.append(f'<path class="edge eflow" d="M{ax},{ay} C{ax},{my} {bx},{my} {bx},{by}" fill="none" stroke="{kcol}" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="{dash}" marker-end="url(#arwX)"/>')
        # bilingual edge-kind label at midpoint (small, low-contrast)
        lx, ly = (ax + bx) / 2, my - 7
        out.append(f'<text x="{lx}" y="{ly}" text-anchor="middle" font-family="LXGW WenKai,serif" font-size="9.5" fill="#8A8066">{esc(note)}</text>')
    # legend: kinds used in this book, bilingual
    used = []
    for a, b, kind, note in edges:
        if kind not in used:
            used.append(kind)
    if used:
        out.append('<g class="legend">')
        lx = 24
        ly0 = H - 14
        for i, kind in enumerate(used):
            klabel, kcol = EDGE_KIND.get(kind, (kind, "#8C8C8C"))
            if i % 6 == 0:
                lx = 24
                ly = ly0 - (i // 6) * 14
            if i > 0 and i % 6 == 0:
                lx = 24
            out.append(f'<rect x="{lx}" y="{ly-8}" width="9" height="3" rx="1.5" fill="{kcol}"/>')
            out.append(f'<text x="{lx+13}" y="{ly}" font-family="LXGW WenKai,serif" font-size="9.5" fill="#57524A">{esc(klabel)}</text>')
            lx += 30 + _cjk_w(klabel) + 8
        out.append('</g>')
    out.append('<defs><marker id="arwX" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="#C9A227"/></marker>'
                '<style>@media (prefers-reduced-motion: no-preference){.eflow{animation:pfdraw 7s linear infinite}.cn{animation:pfpulse 4.2s ease-in-out infinite}}'
                '@keyframes pfdraw{to{stroke-dashoffset:-132}}@keyframes pfpulse{0%,100%{opacity:1}50%{opacity:.45}}'
                '@media print{.eflow,.cn{animation:none}}</style></defs>')
    out.append('</svg>')
    return "\n".join(out)


# ---------- SVG: timeline ----------
def svg_timeline(flow_nodes, width=900):
    if not flow_nodes:
        return ''
    # if flow has date hints use them; else use n column
    H = 120
    n = len(flow_nodes)
    out = [f'<svg viewBox="0 0 {width} {H}" role="img" aria-label="flow timeline" xmlns="http://www.w3.org/2000/svg">']
    x0, x1 = 40, width - 40
    if n <= 1:
        return ''
    step = (x1 - x0) / (n - 1)
    out.append(f'<line x1="{x0}" y1="{H*0.5}" x2="{x1}" y2="{H*0.5}" stroke="#A5811D" stroke-width="1.2"/>')
    dates = [nd.get("zh", "")[:8] for nd in flow_nodes]
    for i, nd in enumerate(flow_nodes):
        cx = x0 + i * step
        top = i % 2 == 0
        cy = H * 0.5 - 16 if top else H * 0.5 + 16
        out.append(f'<circle cx="{cx}" cy="{H*0.5}" r="4" fill="#C9A227"/>')
        out.append(f'<text x="{cx}" y="{cy}" text-anchor="middle" font-family="LXGW WenKai,serif" font-size="9.5" fill="#7C7568">{i+1}</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------- SVG: works × years ----------
def svg_works_years(a, width=860):
    """Per-author works × years timeline: one spine, dots labeled with titles.
    The current-crop book is highlighted in gold with a ring."""
    ymin = None
    ys = []
    for w in a["works"]:
        y = w["y"]
        if y.isdigit():
            y = int(y)
        yy = (y if isinstance(y, int) else None)
        ys.append((w, y, yy))
    ints = [yy for (_, _, yy) in ys if yy is not None]
    if not ints:
        return ""
    ymin, ymax = min(ints), max(ints)
    if ymin > 1980:
        ymin = 1980
    year_w = (ymax - ymin) or 1
    H = 158
    x0, x1 = 52, width - 34
    out = [f'<svg viewBox="0 0 {width} {H}" role="img" aria-label="works over years" xmlns="http://www.w3.org/2000/svg">']
    base = H * 0.6
    out.append(f'<line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="#A5811D" stroke-width="1.2"/>')
    out.append(f'<text x="{x0-8}" y="{base+4}" text-anchor="end" font-family="Inter,sans-serif" font-size="10" fill="#7C7568">{ymin}</text>')
    out.append(f'<text x="{x1+4}" y="{base+4}" text-anchor="start" font-family="Inter,sans-serif" font-size="10" fill="#7C7568">{ymax}</text>')
    for t in range((ymin // 10) * 10 + 10, ymax, 10):
        if t <= ymin:
            continue
        tx = x0 + (t - ymin) / year_w * (x1 - x0)
        out.append(f'<line x1="{tx:.1f}" y1="{base-4}" x2="{tx:.1f}" y2="{base+4}" stroke="#C9BFA6" stroke-width="0.8"/>')
        out.append(f'<text x="{tx:.1f}" y="{base+18}" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#7C7568">{t}</text>')
    for i, (w, y, yy) in enumerate(reversed(ys)):
        if yy is None:
            continue
        k = (yy - ymin) / year_w
        cx = x0 + k * (x1 - x0)
        top = i % 2 == 0
        cy = base - 22 if top else base + 22
        is_crop = w.get("crop")
        fill = "#C9A227" if is_crop else "#6C8AAF"
        ring = 'stroke="#E9D89B" stroke-width="2"' if is_crop else ""
        out.append(f'<circle cx="{cx:.1f}" cy="{base}" r="{5.5 if is_crop else 4.5}" fill="{fill}" {ring}/>')
        out.append(f'<text x="{cx:.1f}" y="{cy:.1f}" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="{"#B08A2E" if is_crop else "#7C7568"}">{y}</text>')
        out.append(f'<text x="{cx:.1f}" y="{cy + (17 if top else -9):.1f}" text-anchor="middle" font-family="LXGW WenKai, serif" font-size="11.5" fill="{("#C9A227" if is_crop else "#4A4438")}">{esc(str(w["title"])[:20])}</text>')
        if is_crop:
            out.append(f'<text x="{cx:.1f}" y="{cy + (30 if top else -22):.1f}" text-anchor="middle" font-family="LXGW WenKai, serif" font-size="10" fill="#B08A2E">【本批书单】</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------- book page ----------
def blk(label, zh, en, cls="card"):
    return f'<div class="{cls}"><h3 class="sec" data-both><span data-zh>{esc(label)}</span><span data-en>{esc(label)}</span></h3>{zh_en(zh, en)}</div>'


LANG_LABEL = {"en": "EN · english", "fr": "FR · français", "ja": "JA · 日本語"}


def excerpt_block(e):
    lang = LANG_LABEL.get(e.get("lang", ""), "")
    bits = [f'<div class="exq">', f'<div class="orig">{esc(e["orig"])}' + (f'<span class="lang">{lang}</span>' if lang else '') + '</div>']
    trs = f'<div data-zh>{esc(e["trans_zh"])}</div>'
    if e.get("trans_en"):
        trs += f'<div data-en>{esc(e["trans_en"])}</div>'
    bits.append(f'<div class="tr">{trs}</div>')
    if e.get("note_zh") or e.get("note_en"):
        note = f'<div data-zh>{esc(e["note_zh"])}</div><div data-en>{esc(e["note_en"])}</div>'
        bits.append(f'<div class="note">{note}</div>')
    bits.append(f'<div class="src">{esc(e["source"])}</div></div>')
    return "\n".join(bits)


def motif_block(m):
    bits = [f'<div class="exq">',
            f'<div class="mname"><span data-zh>{esc(m["name_zh"])}</span><span data-en>{esc(m["name_en"])}</span></div>']
    if m.get("orig"):
        bits.append(f'<div class="orig">{esc(m["orig"])}</div>')
    bits.append(f'<div class="mnote">{zh_en(m["evid_zh"], m["evid_en"])}</div>')
    if m.get("source"):
        bits.append(f'<div class="src">{esc(m["source"])} · {conf_token(m.get("conf", "◐"))}</div>')
    bits.append('</div>')
    return "\n".join(bits)


def book_page(site, book, crop):
    title = f"{book['title_zh']}｜{book['title_orig']}"
    hero_sub = f"{book['author_zh']} · {book['country']} · {book['publines_zh']}"
    hero_h1 = f"{book['title_zh']} · {book['title_orig']}"
    hero_h1_en = f"{book['title_orig']} — {book['title_zh']}"
    hero_sub_en = f"{book['author']} · {book['country_en']} · {book['publines_en']}"
    chips = [f"{crop['glyph_zh']} · {crop['date']}", book["meta_zh"], f"conf {book['baseline_conf']}"]
    if book.get("kind"):
        chips.insert(2, f"kind·{book['kind']}")
    if book.get("domain"):
        chips.insert(3, book["domain"])
    is_hist = book.get("kind", "") in ("history", "nonfiction", "scholarship")
    s = []
    # provenance
    s.append(srcnote(
        "<b>来源说明。</b>" + esc(book["baseline_conf"]) + " · 档案：" + esc(book["id"]) + "（Books）核心数据经四级核实，情节细处标 ◐/○。",
        "<b>Provenance.</b> " + esc(book["baseline_conf"]) + " · record: " + esc(book["id"]) + ". Publication facts verified; plot details marked ◐/○."))
    # read status banner
    if book.get("read_status"):
        rs_en = book.get("read_status_en", book["read_status"])
        s.append('<div class="readban" data-both><span data-zh>%s</span><span data-en>%s</span></div>' % (
            esc(book["read_status"]), esc(rs_en)))
    # rating strip (Douban/Goodreads).
    rating_html = rating_line(book)
    if rating_html:
        cov = cover_art(book["slug"])
        cover_el = (f'<img src="../../art/covers/{esc(os.path.basename(cov))}" alt="{esc(book["title_orig"])}" style="width:88px;height:124px;object-fit:cover;border-radius:6px;box-shadow:0 4px 12px rgba(38,38,31,.2)" loading="lazy">'
                    if cov else svg_cover(book, 88, 124))
        aface = author_art(book["author_slug"])
        if aface:
            cover_el += f'<a href="../../authors/index.html#{esc(book["author_slug"])}" title="{esc(book["author"])}"><img src="../../art/authors/{esc(os.path.basename(aface))}" alt="{esc(book["author"])}" class="aface" loading="lazy"></a>'
        s.append('<div class="card" style="display:flex;align-items:center;gap:.9rem;flex-wrap:wrap;padding:.9rem 1.2rem">'
                 + cover_el + '<div>' + rating_html + read_chip(book) + '</div></div>')
    # why
    s.append(blk("为何此刻 · Why now", book["why_zh"], book["why_en"]))
    # original text / preview links (links only, no scraped content)
    tl = textlinks_block(book)
    if tl:
        s.append('<div class="card" id="textlinks">' + tl + '</div>')
    # background
    s.append(blk("背景 · Background", book["background"]["zh"], book["background"]["en"]))
    s.append('<p class="tok">' + conf_token(book["background"]["conf"]) + ' <span class="hidden"></span></p>')
    # plot acts / thematic periods
    acts_label = ("时段章节 · Periods &amp; chapters", "Periods &amp; chapters") if is_hist else ("情节分幕 · Plot content", "Plot content")
    s.append(f'<h2 class="part" data-both><span data-zh>{acts_label[0]}</span><span data-en>{acts_label[1]}</span></h2>')
    for act in book.get("plot_acts", []):
        act_head_zh = f'第 {act["n"]} 节 · {act["title_zh"]}' if is_hist else f'第 {act["n"]} 幕 · {act["title_zh"]}'
        act_head_en = f'Section {act["n"]} · {act["title_en"]}' if is_hist else f'Act {act["n"]} · {act["title_en"]}'
        s.append(f'<div class="card"><h3 class="sec" data-both><span data-zh>{act_head_zh}</span><span data-en>{act_head_en}</span></h3>')
        s.append(zh_en(act["zh"], act["en"]))
        if act.get("conf"):
            s.append('<p class="tok">' + conf_token(act["conf"]) + "</p>")
        if act.get("sources"):
            s.append(f'<p class="tok"><span class="conf c-part">src</span> <span style="font-size:.8rem;color:var(--ink-pale)">{act["sources"]}</span></p>')
        s.append("</div>")
    # narrative structure / analytical framework
    narr_label = ("论述框架 · Analytical framework", "Analytical framework") if is_hist else ("叙事结构 · Narrative structure", "Narrative structure")
    s.append(f'<h2 class="part" data-both><span data-zh>{narr_label[0]}</span><span data-en>{narr_label[1]}</span></h2>')
    s.append(blk("结构 · Structure", book["narrative"]["zh"], book["narrative"]["en"], cls="card"))
    # plot flow svg / chronological flow
    flow_label = ("时间线索引 · Chronological flow", "Chronological flow") if is_hist else ("情节流程图 · Plot flow", "Plot flow")
    s.append(f'<h2 class="part" data-both><span data-zh>{flow_label[0]}</span><span data-en>{flow_label[1]}</span></h2>')
    s.append('<div class="diagram">' + svg_plot_flow(book.get("plot_flow", [])) + '<p class="cap">' + zh_en(book["title_zh"] + " · 时段链（数字为顺序）" if is_hist else book["title_zh"] + " · 事件链（数字为顺序）", book["title_orig"] + " · the chronological chain" if is_hist else book["title_orig"] + " · the event chain (numbers = order)", "span") + '</p></div>')
    # characters + charedge svg / key figures
    if book.get("characters"):
        chars_label = ("关键人物 · Key Figures", "Key Figures") if is_hist else ("人物关系图 · Characters", "Characters &amp; relations")
        s.append(f'<h2 class="part" data-both><span data-zh>{chars_label[0]}</span><span data-en>{chars_label[1]}</span></h2>')
        s.append('<div class="diagram">' + svg_charedge(book) + '<p class="cap">' + zh_en(book["title_zh"] + " · 人物关系（虚点线=连接）", book["title_orig"] + " · character relations (dotted = link)", "span") + '</p></div>')
        s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th>ID</th><th data-both><span data-zh>人物</span><span data-en>name</span></th><th data-both><span data-zh>阵营/组</span><span data-en>group</span></th><th data-both><span data-zh>角色</span><span data-en>role</span></th><th data-both><span data-zh>把握</span><span data-en>conf</span></th></tr></thead><tbody>')
        for c in book["characters"]:
            s.append(f'<tr><td>{esc(c["id"])}</td><td>{esc(c["name"])}</td><td>{esc(c.get("group",""))}</td><td><div data-zh>{esc(c["role_zh"])}</div><div data-en>{esc(c["role_en"])}</div></td><td class="conf">{conf_token(c["conf"])}</td></tr>')
        s.append('</tbody></table></div>')
    # intent / thesis
    intent_label = ("核心论题 · Thesis" if is_hist else "作者真意 · Intent", "Thesis" if is_hist else "The author&rsquo;s intent")
    s.append(f'<h2 class="part" data-both><span data-zh>{intent_label[0]}</span><span data-en>{intent_label[1]}</span></h2>')
    if book["intent"].get("quotes"):
        for q in book["intent"]["quotes"]:
            s.append(f'<div class="quote"><div class="orig">{esc(q["orig"])}</div><div class="trs">{esc(q["trans_zh"])}</div><div class="src">{esc(q["source"])}</div></div>')
    s.append(blk("评价与合成 · Reception & synthesis", book["intent"]["reception_good_zh"] + "\n\n" + book["intent"]["reception_bad_zh"] + "\n\n**合成 Synthesis：** " + book["intent"]["syn_zh"], book["intent"]["reception_good_en"] + "\n\n" + book["intent"]["reception_bad_en"] + "\n\n**Synthesis:** " + book["intent"]["syn_en"], cls="gapbox"))
    # craft / highlights
    craft_label = ("史学方法 · Historiography", "Historiography") if is_hist else ("手法与亮点 · Craft", "Craft &amp; highlights")
    s.append(f'<h2 class="part" data-both><span data-zh>{craft_label[0]}</span><span data-en>{craft_label[1]}</span></h2>')
    if book.get("craft"):
        for c in book["craft"]:
            s.append(f'<div class="card"><p>{esc(c["zh"])}</p><p style="color:var(--ink-soft);font-size:.9rem">{esc(c["en"])}</p></div>')
    else:
        s.append(f'<div class="srcnote">{zh_en("待通读原书后补充。", "Craft notes come after the full read.")}</div>')
    # motifs（母题簇 / key themes）
    if book.get("motifs"):
        motif_label = ("核心主题 · Themes", "Themes") if is_hist else ("母题簇 · Motifs", "Motif clusters")
        s.append(f'<h2 class="part" data-both><span data-zh>{motif_label[0]}</span><span data-en>{motif_label[1]}</span></h2>')
        for m in book["motifs"]:
            s.append(motif_block(m))
    # excerpts
    if not is_hist:
        s.append('<h2 class="part" data-both><span data-zh>语言与文化 · 原意摘录</span><span data-en>Language &amp; culture — excerpts</span></h2>')
        if book.get("excerpts"):
            for e in book["excerpts"]:
                s.append(excerpt_block(e))
        else:
            s.append(f'<div class="srcnote">{zh_en("待读原书摘引。", "Excerpts pending the read.")}</div>')
    # deep read
    s.append('<h2 class="part" data-both><span data-zh>精读建议 · Deep reading</span><span data-en>Deep reading</span></h2>')
    for d in book.get("deep_read", []):
        s.append(f'<div class="card">{zh_en(d["zh"], d["en"])}</div>')
    # related + positioning
    s.append('<h2 class="part" data-both><span data-zh>相关定位 · Positioning</span><span data-en>Related works &amp; positioning</span></h2>')
    s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th data-both><span data-zh>作品</span><span data-en>work</span></th><th data-both><span data-zh>作者</span><span data-en>author</span></th><th>年</th><th data-both><span data-zh>关系</span><span data-en>relation</span></th><th data-both><span data-zh>一句理由</span><span data-en>why</span></th><th data-both><span data-zh>轴</span><span data-en>axis</span></th><th data-both><span data-zh>把握</span><span data-en>conf</span></th></tr></thead><tbody>')
    for r in book.get("related", []):
        why = '<div data-zh>%s</div><div data-en>%s</div>' % (esc(r["note_zh"]), esc(r["note_en"]))
        s.append(f'<tr><td><b>{esc(r["title"])}</b></td><td>{esc(r["author"])}</td><td>{esc(r["year"])}</td><td>{esc(r["relation"])}</td><td>{why}</td><td>{esc(r["axis"])}</td><td class="conf">{conf_token(r["conf"])}</td></tr>')
    s.append('</tbody></table></div>')
    # fact ledger
    s.append('<h2 class="part" data-both><span data-zh>核对账本 · Fact ledger</span><span data-en>Fact ledger</span></h2>')
    s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th data-both><span data-zh>主张</span><span data-en>claim</span></th><th data-both><span data-zh>来源</span><span data-en>source</span></th><th class="conf">conf</th></tr></thead><tbody>')
    for f in book.get("fact_ledger", []):
        s.append(f'<tr><td>{esc(f["claim"])}</td><td style="font-size:.8rem;color:var(--ink-pale)">{esc(f["source"])}</td><td class="conf">{conf_token(f["conf"])}</td></tr>')
    s.append('</tbody></table></div>')
    # unverified
    if book.get("unverified"):
        s.append('<h2 class="part" data-both><span data-zh>未核 / 未知 · Unverified</span><span data-en>Unverified / unknown</span></h2>')
        for u in book["unverified"]:
            s.append(f'<div class="card"><p>{esc(u["item"])} <span class="tok">{conf_token(u["conf"])}</span></p></div>')
    # links — dynamic back-link
    s.append('<div class="links">')
    s.append(f'<a class="pill" href="../{esc(crop["dir_page"])}">← <span data-zh>返回{esc(crop["glyph_zh"])}</span><span data-en>back to {esc(crop.get("glyph_en", crop["glyph_zh"]))}</span></a>')
    s.append(f'<a class="pill" href="../index.html">☰ <span data-zh>书单档案</span><span data-en>the archive</span></a>')
    s.append(f'<a class="pill" href="../../authors/index.html">↝ <span data-zh>作者知识图谱</span><span data-en>the authors graph</span></a>')
    s.append('</div>')
    nav_sub = f"{len(crop['book_ids'])} 部 · {crop['date'][:7]}"
    return page(title, crop["glyph_zh"], hero_h1, hero_sub, chips, "\n".join(s), up_rel="../../..", hero_h1_en=hero_h1_en, hero_sub_en=hero_sub_en, nav_sub_zh=nav_sub, nav_sub_en=nav_sub)


# ---------- crop list page ----------
def crop_page(site, crop, books):
    title = f"{crop['title_zh']}｜{crop['title_en']}"
    hero_sub = crop["subtitle_zh"]
    chips = [crop["date"] + " · " + crop["glyph_zh"], crop["verdict_zh"] + "/" + crop["verdict_en"], "每书一页"]
    s = []
    s.append(srcnote(
        '<b>来源说明。</b>本清单由 <code>web/data/books.json</code> 驱动（generator: build_reading.py）；每部均经 websearch/webfetch 定位实际版本（W2）。出版信息 <code>✓</code> 核实；情节细处标 <code>◐/○</code>。点击各书卡进入单书页码。',
        '<b>Provenance.</b> This list is driven by <code>web/data/books.json</code> (generator: build_reading.py); each title located &amp; verified (W2). Pub facts <code>✓</code>; plot details <code>◐/○</code>. Click a card for the per-book page.'))
    s.append(srcnote(
        '<b>书封与照片。</b>书封图取自各出版社/书店公开页（<code>docs/reading_ia/art/covers/</code>，仅本地引用）；作者照片取自 Wikimedia Commons 等公开来源，版权归原作者，个人笔记内引用。',
        '<b>Covers &amp; portraits.</b> Cover art referenced locally from publisher/bookseller pages (<code>art/covers/</code>); author photos from public sources (Wikimedia Commons etc.). All rights remain with their owners; cited here for a personal reading journal.'))
    for i, b in enumerate(books, 1):
        s.append('<article class="bkcard">')
        cov = cover_art(b["slug"])
        if cov:
            s.append(f'<a class="bkcover" href="books/{esc(b["slug"])}.html" aria-label="{esc(b["title_zh"])}"><img src="../art/covers/{esc(os.path.basename(cov))}" alt="{esc(b["title_orig"])}" loading="lazy"></a>')
        else:
            s.append(f'<a class="bkcover" href="books/{esc(b["slug"])}.html" aria-label="{esc(b["title_zh"])}">{svg_cover(b)}</a>')
        s.append('<div class="bkbody">')
        s.append('<div class="bkhead">'
                 '<span class="bknum" data-both><span data-zh>%s · %s</span><span data-en>%s · %s</span></span>'
                 '<span class="tag cn">%s</span></div>'
                 % (esc(b["num"]), esc(b["country"]), chr(64 + i), esc(b["country_en"]), esc(b.get("lang", "").upper())))
        s.append(f'<h3 class="bktitle"><a href="books/{esc(b["slug"])}.html"><span data-zh>{esc(b["title_zh"])}</span><span data-en>{esc(b["title_orig"])}</span> <span class="orig" data-both><span data-zh>{esc(b["title_orig"])}</span><span data-en>{esc(b["title_zh"])}</span></span></a></h3>')
        s.append(f'<div class="bkauthor"><a href="../authors/index.html#{esc(b["author_slug"])}" data-both><span data-zh>{esc(b["author_zh"])}</span><span data-en>{esc(b["author"])}</span></a>'
                 f' <span class="cnt" style="color:var(--ink-pale);font-size:.78rem">· {esc(b.get("author",""))}</span></div>')
        s.append(rating_line(b))
        # Douban-style publisher / date / pages / ISBN meta line
        s.append(f'<div class="bkmeta" data-both><span data-zh>{esc(b["publines_zh"])} · ISBN {esc(str(b.get("isbn","")).split(" · ")[0])}</span>'
                 f'<span data-en>{esc(b["publines_en"])} · ISBN {esc(str(b.get("isbn","")).split(" · ")[0])}</span></div>')
        # tags: series / meta / country / publisher chip
        s.append('<div class="bktags">')
        s.append(f'<span class="tag pub" style="background:{pub_color(pub_key(b.get("publisher","")))}">{esc(pub_key(b.get("publisher","")))}</span>')
        s.append(f'<span class="tag" data-both><span data-zh>{esc(b["country"])}</span><span data-en>{esc(b["country_en"])}</span></span>')
        s.append(f'<span class="tag" data-both><span data-zh>{esc(b.get("meta_zh",""))}</span><span data-en>{esc(b.get("meta_en",""))}</span></span>')
        if b.get("kind"):
            s.append(f'<span class="tag" data-both><span data-zh>kind · {esc(b["kind"])}</span><span data-en>{esc(b["kind"])}</span></span>')
        if b.get("domain"):
            s.append(f'<span class="tag" data-both><span data-zh>{esc(b["domain"])}</span><span data-en>{esc(b["domain"])}</span></span>')
        s.append(read_chip(b))
        s.append('</div>')
        # why (Goodreads blurb position)
        s.append(f'<div class="bkwhy"><p data-zh>{esc(b["why_zh"])}</p><p data-en>{esc(b["why_en"])}</p></div>')
        # claims strip (Douban short-review feel)
        claims = b.get("claims_list") or []
        if claims:
            s.append('<ul style="list-style:none;display:flex;flex-wrap:wrap;gap:.35rem .9rem;margin-top:.35rem">')
            for c in claims:
                s.append('<li style="font-size:.78rem;color:var(--gold-dim)">· %s</li>' % esc(c))
            s.append('</ul>')
        # actions: dossier + first original-text link inline (Goodreads action buttons row)
        s.append('<div class="bkact">')
        s.append(f'<a class="pill sm" href="books/{esc(b["slug"])}.html">☞ <span data-zh>进入单书页 · 完整档案</span><span data-en>open the full dossier</span></a>')
        tl = (b.get("textlinks") or [])
        if tl:
            s.append(f'<a class="pill sm ext" href="{esc(tl[0]["url"])}" target="_blank" rel="noopener"><span data-zh>原文试读 · {esc(tl[0]["zh"])}</span><span data-en>Original text · {esc(tl[0]["en"])}</span></a>')
            if len(tl) > 1:
                s.append(f'<a class="pill sm" href="books/{esc(b["slug"])}.html#textlinks"><span data-zh>全部原文链接 {len(tl)} 条 →</span><span data-en>all {len(tl)} source links →</span></a>')
        s.append('</div>')
        s.append('</div></article>')
    # publisher × books visualization (Goodreads-shelf style)
    s.append('<h2 class="part" data-both><span data-zh>出版社 × 书 · Publishers &amp; shelves</span><span data-en>Publishers &amp; shelves</span></h2>')
    s.append(srcnote(
        '<b>可视化说明。</b>每行一个出版社（色块=出版社色），块宽∝页数，块内为书名——出版方、篇幅与批次分布一图读完。',
        '<b>How to read.</b> One row per publisher (color = press); block width ∝ page count; titles inside — press, length and batch at a glance.'))
    s.append(pubviz_svg(books))
    # author × books mapping
    s.append('<h2 class="part" data-both><span data-zh>作者 × 书 · Authors mapping</span><span data-en>Authors mapping</span></h2>')
    s.append('<div class="pubviz">')
    seen_auth = {}
    for b in books:
        seen_auth.setdefault(b["author_slug"], []).append(b)
    for slug, bs in seen_auth.items():
        col = COUNTRY_COLOR.get(bs[0].get("country", ""), "#777069")
        links = " ".join(f'<a href="books/{esc(x["slug"])}.html" style="font-size:.78rem">{esc(x["title_orig"])}</a>' for x in bs)
        auth_zh = bs[0]["author_zh"]; auth_en = bs[0]["author"]
        s.append(f'<div class="row"><div class="pname"><span class="dot" style="background:{col}"></span>'
                 f'<a href="../authors/index.html#{esc(slug)}" data-both><span data-zh>{esc(auth_zh)}</span><span data-en>{esc(auth_en)}</span></a></div>'
                 f'<div class="bar" style="gap:.9rem">{links}</div></div>')
    s.append('</div>')
    # verdict
    s.append('<h2 class="part" data-both><span data-zh>完备性核验 · Completeness review</span><span data-en>Completeness review</span></h2>')
    s.append('<div class="gapbox"><div class="v-line"><span class="badge">判定 ' + esc(crop["verdict_zh"]) + '</span><span data-zh>' + esc(crop["verdict_body_zh"]) + '</span><span data-en>' + esc(crop["verdict_body_en"]) + '</span></div><ul>')
    for g in crop["verdict_gaps"]:
        s.append(f'<li data-zh>{esc(g["zh"])}</li><li data-en>{esc(g["en"])}</li>')
    s.append('</ul></div>')
    s.append('<div class="links">')
    s.append('<a class="pill" href="index.html">☰ <span data-zh>全部书单 · 档案</span><span data-en>all lists · archive</span></a>')
    s.append('<a class="pill" href="../moment/year-2026.html">↝ <span data-zh>读年度思潮：活着的此刻</span><span data-en>read the year</span></a>')
    s.append('<a class="pill" href="../index.html">↝ <span data-zh>返回板块首页</span><span data-en>back to the domain</span></a>')
    s.append('</div>')
    return page(title, crop["glyph_zh"], title, hero_sub, chips, "\n".join(s),
                nav_sub_zh=f"{len(crop['book_ids'])} 部 · {crop['date'][:7]}",
                nav_sub_en=f"{len(crop['book_ids'])} books · {crop['date'][:7]}")


# ---------- archive page ----------
def archive_page(site, crops, books_by_id):
    s = []
    s.append(srcnote(
        '<b>来源与位置。</b>注册表（唯一）：<code>readings/lists/README.md</code> · 设计协议：<code>docs/reading_lists_design.md</code> · 每批一页，文件定稿后不复用（R3）。档案由 generator 维护。',
        '<b>Source &amp; layout.</b> Registry (single source): <code>readings/lists/README.md</code> · protocol: <code>docs/reading_lists_design.md</code> · one page per crop; stable files (R3). Maintained by the generator.'))
    for crop in crops:
        books = [books_by_id[i] for i in crop["book_ids"] if i in books_by_id]
        lines = ''.join('<li data-zh>%s %s — %s（%s）</li><li data-en>%s — %s (%s)</li>' % (
            b["title_zh"], b["title_orig"], b["author_zh"], b["country"],
            b["title_orig"], b["author"], b["lang"]) for b in books)
        s.append(f'<div class="card"><h3 class="sec"><span data-zh>{esc(crop["glyph_zh"])} · {esc(crop["title_zh"])}</span><span data-en>{esc(crop["glyph_en"])} · {esc(crop["title_en"])}</span></h3>')
        s.append('<p style="font-size:.8rem;color:var(--ink-pale)">' + esc(crop["date"]) + ' · ' + esc(crop["lang_line_zh"]) + '</p>')
        s.append('<ul style="list-style:none;margin:.5rem 0">' + lines + '</ul>')
        s.append(f'<a class="pill" href="{esc(crop["dir_page"])}">☞ <span data-zh>打开本批书单</span><span data-en>open this list</span></a>')
        s.append('</div>')
    # next keel
    s.append('<div class="card" style="border-style:dashed"><h3 class="sec" data-both><span data-zh>下一批 · 待 W2 核验后登记</span><span data-en>next crop — registered after W2</span></h3><p style="font-size:.85rem;color:var(--ink-soft)">' + esc(site["keel"]) + '</p></div>')
    s.append('<div class="links"><a class="pill" href="../authors/index.html">↝ 作者知识图谱</a><a class="pill" href="../index.html">↝ 板块首页</a></div>')
    newest = crops[0] if crops else {"glyph_en": "CROPS", "glyph_zh": "书单", "date": ""}
    kicker = newest["glyph_en"].split("·")[-1].strip() or "CROPS"
    latest_chip = f"最新批：{newest['date'][:7]}" if newest.get("date") else "新批在上"
    return page("书单档案 · BOOK LIST ARCHIVE", kicker, "书单档案 · 一窗一书单", "书单是素材层，思潮是合成层——清单不入思潮之文", [latest_chip, "新批在上"], "\n".join(s),
                nav_sub_zh=f"{len(crops)} 批 · 档案", nav_sub_en=f"{len(crops)} crops · archive")


# ---------- authors graph page ----------
def authors_page(site, authors, relations):
    by_id = {a["id"]: a for a in authors}
    s = []
    s.append(srcnote(
        '<b>来源与位置。</b>节点与生平：<code>web/data/authors.json</code>（逐条附出处与把握）；边：唯一源 <code>relations/influences.md</code> 镜像 <code>web/data/relations.json</code>。可信度 <code>✓ 已核 · ◐ 一手/自述 · ○ 转述 · ✗ 争议</code>。',
        '<b>Source &amp; layout.</b> Nodes &amp; lives: <code>web/data/authors.json</code>; edges: single source <code>relations.json</code> (mirrors influences.md). Confidence <code>✓ verified · ◐ primary · ○ secondhand · ✗ disputed</code>.'))
    s.append(srcnote(
        '<b>照片。</b>作者照片取自公开来源（Wikimedia Commons 等），版权归原作者，仅个人笔记引用。',
        '<b>Portraits.</b> Photos from public sources (Wikimedia Commons &amp;c.), rights remain with the owners; cited for a personal journal.'))
    # nodes
    s.append('<h2 class="part" data-both><span data-zh>一 · 节点 Nodes</span><span data-en>I · Nodes</span></h2>')
    s.append('<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1rem">')
    for a in authors:
        s.append('<div class="card" style="margin:0">')
        face = author_art(a["id"])
        name_block = '<h3 class="sec">%s <span style="font-size:.8rem;color:var(--ink-pale)">%s</span></h3>' % (esc(a["name_zh"]), esc(a["name_native"]))
        if face:
            s.append(f'<div class="anode"><img src="../art/authors/{esc(os.path.basename(face))}" alt="{esc(a["name_en"])}" class="aface" loading="lazy"><div style="min-width:0">{name_block}</div></div>')
        else:
            s.append(name_block)
        s.append('<p style="font-size:.76rem;color:var(--gold-dim)">' + esc(a["born"]) + ' · ' + esc(a["native_lang"]) + '</p>')
        s.append('<p data-zh style="font-size:.9rem">' + esc(a["one_liner_zh"]) + '</p><p data-en style="font-size:.9rem">' + esc(a["one_liner_en"]) + '</p>')
        s.append('<div style="margin-top:.6rem"><span class="conf c-ok">' + esc(a["school_zh"]) + '</span></div>')
        s.append('</div>')
    s.append('</div>')
    # schools
    s.append('<h2 class="part" data-both><span data-zh>二 · 流派归属 Schools</span><span data-en>II · Schools</span></h2>')
    for row in relations["schools"]:
        a = by_id.get(row["author"])
        s.append(f'<div style="background:var(--paper-deep);border:1px solid rgba(167,146,93,.35);border-radius:16px;padding:1.1rem 1.4rem;margin-bottom:.8rem"><h3 class="sec" style="margin:0 0 .3rem">{esc(row["school_zh"])}</h3><p style="font-size:.88rem;color:var(--ink-mid)"><span data-zh>{esc(row["why_zh"]) + (" · 成员：" + esc(a["name_zh"]) if a else "")}</span><span data-en>{esc(row["why_en"]) + (" · members: " + esc(a["name_en"]) if a else "")}</span></p></div>')
    # circles
    s.append('<h2 class="part" data-both><span data-zh>三 · 朋友圈 · 合著 Circles &amp; Co-writes</span><span data-en>III · Circles &amp; Co-writes</span></h2>')
    s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th data-both><span data-zh>作者</span><span data-en>author</span></th><th>edge</th><th data-both><span data-zh>同代 · 合作者</span><span data-en>peer / collaborator</span></th><th data-both><span data-zh>一句理由</span><span data-en>why</span></th><th class="conf">conf</th></tr></thead><tbody>')
    for r in relations["circle"]:
        a = by_id.get(r["from"], {})
        nm = a.get("name_zh", r["from"])
        s.append(f'<tr><td>{esc(nm)}</td><td class="conf">{esc(r["arrow"])}</td><td>{esc(r["to"])}</td><td>{zh_en(r["why_zh"], r["why_en"], "span")}</td><td class="conf">{esc(r["conf"])}</td></tr>')
    for r in relations["cowrites"]:
        a = by_id.get(r["from"], {})
        nm = a.get("name_zh", r["from"])
        s.append(f'<tr><td>{esc(nm)}</td><td class="conf">✎</td><td>{esc(r["to"])}</td><td>{zh_en(r["why_zh"] + " · " + r["book"], r["why_en"] + " · " + r["book"], "span")}</td><td class="conf">{esc(r["conf"])}</td></tr>')
    s.append('</tbody></table></div>')
    # influences
    s.append('<h2 class="part" data-both><span data-zh>四 · 影响链 Influence</span><span data-en>IV · Influence</span></h2>')
    s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th data-both><span data-zh>源</span><span data-en>from</span></th><th>edge</th><th data-both><span data-zh>向</span><span data-en>to</span></th><th data-both><span data-zh>一句理由</span><span data-en>why</span></th><th class="conf">conf</th></tr></thead><tbody>')
    for r in relations["influences"]:
        def nm(key):
            return by_id[key]["name_zh"] if key in by_id else key
        s.append(f'<tr><td>{esc(nm(r["from"]))}</td><td class="conf">{esc(r["arrow"])}</td><td>{esc(nm(r["to"]))}</td><td>{zh_en(r["why_zh"], r["why_en"], "span")}</td><td class="conf">{esc(r["conf"])}</td></tr>')
    s.append('</tbody></table></div>')
    # per-author deep dossiers
    s.append('<h2 class="part" data-both><span data-zh>五 · 每位作者 Deep dossiers</span><span data-en>V · Per-author dossiers</span></h2>')
    for a in authors:
        s.append(f'<div class="card" id="{esc(a["id"])}">')
        face = author_art(a["id"])
        head = '<h3 class="sec">' + esc(a["name_zh"]) + ' · ' + esc(a["slug_display"]) + '</h3>'
        if face:
            s.append(f'<div class="anode"><img src="../art/authors/{esc(os.path.basename(face))}" alt="{esc(a["name_en"])}" class="aface" loading="lazy"><div style="min-width:0">{head}</div></div>')
        else:
            s.append(head)
        # timeline
        s.append('<h4 class="sec" data-both><span data-zh>生平轨迹 Timeline</span><span data-en>Timeline</span></h4>')
        s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th>y</th><th data-both><span data-zh>事件</span><span data-en>event</span></th><th class="conf">conf</th></tr></thead><tbody>')
        for t in a["timeline"]:
            s.append('<tr><td>%s</td><td><div data-zh>%s</div><div data-en>%s</div></td><td class="conf">%s</td></tr>' % (esc(t["y"]), esc(t["event_zh"]), esc(t["event_en"]), conf_token(t["conf"])))
        s.append('</tbody></table></div>')
        # works
        s.append('<h4 class="sec" data-both><span data-zh>作品 Works</span><span data-en>Works</span></h4>')
        tline = svg_works_years(a)
        if tline:
            s.append('<div class="diagram">' + tline + '<p class="cap">' + zh_en(a["name_zh"] + " · " + a["name_native"] + " 作品年表（金环 = 本批书单）", a["name_en"] + " works by year (gold ring = this batch)", "span") + '</p></div>')
        s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th>y</th><th>title</th><th data-both><span data-zh>备注</span><span data-en>note</span></th><th class="conf">conf</th></tr></thead><tbody>')
        for w in a["works"]:
            s.append('<tr><td>%s</td><td><b>%s</b></td><td><div data-zh>%s</div><div data-en>%s</div></td><td class="conf">%s</td></tr>' % (esc(w["y"]), esc(w["title"]), esc(w["note_zh"]), esc(w["note_en"]), conf_token(w["conf"])))
        s.append('</tbody></table></div>')
        # awards
        if a.get("awards"):
            s.append('<h4 class="sec" data-both><span data-zh>奖项 Awards</span><span data-en>Awards</span></h4>')
            s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th>y</th><th>award</th><th>note</th></tr></thead><tbody>')
            for aw in a["awards"]:
                s.append('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (esc(aw["y"]), esc(aw["award"]), esc(aw.get("note", ""))))
            s.append('</tbody></table></div>')
        # circle & influences per author
        if a.get("circle"):
            s.append('<h4 class="sec" data-both><span data-zh>朋友圈 Circle</span><span data-en>Circle</span></h4>')
            s.append('<ul style="list-style:none">')
            for c in a["circle"]:
                s.append('<li style="margin-bottom:.35rem">%s %s — <span style="color:var(--ink-soft)">%s</span> %s</li>' % (esc(c["who"]), esc(c["edge"]), zh_en(c["why_zh"], c["why_en"], "span"), conf_token(c["conf"])))
            s.append('</ul>')
        # stance
        s.append('<h4 class="sec" data-both><span data-zh>立场与一贯关切 Stance</span><span data-en>Stance</span></h4>')
        s.append(zh_en(a["stance_zh"], a["stance_en"]))
        # why now
        s.append('<h4 class="sec" data-both><span data-zh>为何此刻 Why now</span><span data-en>Why now</span></h4>')
        s.append(zh_en(a["why_now_zh"], a["why_now_en"]))
        # ledger
        s.append('<h4 class="sec" data-both><span data-zh>核对账本 Ledger</span><span data-en>Ledger</span></h4>')
        s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th data-both><span data-zh>主张</span><span data-en>claim</span></th><th data-both><span data-zh>来源</span><span data-en>source</span></th><th class="conf">conf</th></tr></thead><tbody>')
        for f in a["fact_ledger"]:
            s.append('<tr><td>%s</td><td style="font-size:.78rem;color:var(--ink-pale)">%s</td><td class="conf">%s</td></tr>' % (esc(f["claim"]), esc(f["source"]), conf_token(f["conf"])))
        s.append('</tbody></table></div>')
        if a.get("unverified"):
            s.append('<h4 class="sec" data-both><span data-zh>未核 Unverified</span><span data-en>Unverified</span></h4>')
            for u in a["unverified"]:
                s.append('<div style="font-size:.85rem;color:var(--ink-soft);margin-bottom:.25rem">%s %s</div>' % (esc(u["item"]), conf_token(u["conf"])))
        s.append('</div>')
    s.append('<div class="links"><a class="pill" href="../read/index.html">↝ 读书单档案</a><a class="pill" href="../index.html">↝ 板块首页</a></div>')
    return page("作者知识图谱 · AUTHORS GRAPH", "AUTHORS", "作者知识图谱 · 谁在写，与谁同代", "生平 · 朋友圈 · 合著 · 流派归属 · 影响链——人物即思想的坐标", ["全批 · " + str(len(authors)) + " 位作者", "generator 维护"], "\n".join(s),
                nav_sub_zh=str(len(authors)) + " 位作者", nav_sub_en=str(len(authors)) + " authors")


def glossary_page(site, entries):
    """Render readings/categories/glossary.md → docs/reading_ia/glossary.html."""
    s = []
    s.append(srcnote(
        '<b>单一来源。</b>术语架 = <code>readings/categories/glossary.md</code>（唯一源），由 <code>build_reading.py</code> 生成本页。新术语（文学/理论/哲学/数学/科学/社科/媒介）先落术语架，成熟后晋升为概念层原型簇。',
        '<b>Single source.</b> Terms live in <code>readings/categories/glossary.md</code>; this page is generated. New terms land here first; mature ones are promoted to concept-layer archetype clusters.'))
    s.append('<div class="links"><a class="pill" href="read/index.html">↝ <span data-zh>书目档案</span><span data-en>the library</span></a>'
             '<a class="pill" href="methods.html">↝ <span data-zh>方法论与透镜</span><span data-en>methods &amp; lenses</span></a>'
             '<a class="pill" href="index.html">↝ <span data-zh>板块首页</span><span data-en>the domain</span></a></div>')
    count = len(entries)
    for e in entries:
        it = e["items"]
        mode = it.get("mode", "concept")
        dom = it.get("domain", "")
        s.append('<div class="card" id="%s" style="margin-top:1.4rem">' % esc(e["title"].split(" ")[0]))
        en_sub = it.get("en", "")
        if en_sub:
            s.append('<h3 class="sec" style="margin-top:.2rem">%s <span style="font-size:.78rem;color:var(--ink-pale)">%s</span></h3>'
                     % (esc(e["title"]), esc(en_sub)))
        else:
            s.append('<h3 class="sec" style="margin-top:.2rem">%s</h3>' % esc(e["title"]))
        s.append(f'<div><span class="modechip {esc(mode)}">{esc(mode)}</span>'
                 f'<span class="domchip">{esc(dom)}</span>'
                 f'<span class="ref">cluster → {esc(it.get("cluster","").split("/")[-1].replace("]]",""))}</span></div>')
        s.append('<div class="term-line"><b>' + esc("定义 · ") + '</b>' + wl(it.get("def_zh", "")) + "</div>")
        s.append('<div class="term-line" style="color:var(--ink-soft)"><b>' + esc("en · ") + '</b>' + wl(it.get("def_en", "")) + "</div>")
        if it.get("epitome"):
            s.append('<div class="term-line" style="font-size:.85rem"><b>' + esc("典例 · epitome") + '</b> ' + wl(it.get("epitome")) + "</div>")
        if it.get("source"):
            s.append('<div class="term-line" style="font-size:.82rem;color:var(--ink-pale)"><b>' + esc("出处 · source") + '</b> ' + wl(it.get("source")) + "</div>")
        if it.get("links"):
            s.append('<div style="margin-top:.5rem">' + wl(it.get("links")) + "</div>")
        s.append("</div>")
    s.append('<div class="links"><a class="pill" href="methods.html">↝ <span data-zh>方法论</span><span data-en>methods</span></a>'
             '<a class="pill" href="read/index.html">↝ <span data-zh>读书</span><span data-en>the library</span></a></div>')
    return page("术语架 · TERM REGISTRY", "TERMS", "术语架 · 全领域的名字", "概念 · 传统 · 原型 · 方法——先命名，再理解", ["%d 条术语" % count, "跨学科"], "\n".join(s))


def methods_page(site, methods):
    """Render readings/methods/README.md → docs/reading_ia/methods.html."""
    s = []
    s.append(srcnote(
        '<b>单一来源。</b>方法论 = <code>readings/methods/README.md</code>（唯一源），由生成器产出本页。一法一卡；一种方法至少实践两次后才可入档（skill-creator 触发条件）。',
        '<b>Single source.</b> Methods live in <code>readings/methods/README.md</code>; this page is generated. A method earns a card only after working twice in practice.'))
    s.append('<div class="links"><a class="pill" href="glossary.html">↝ <span data-zh>术语架</span><span data-en>glossary</span></a>'
             '<a class="pill" href="read/index.html">↝ <span data-zh>书目档案</span><span data-en>the library</span></a>'
             '<a class="pill" href="index.html">↝ <span data-zh>板块首页</span><span data-en>the domain</span></a></div>')
    for i, m in enumerate(methods, 1):
        it = m["items"]
        s.append('<div class="card" id="%s">' % esc(m["title"].split(" ")[0]))
        s.append('<h3 class="sec" style="margin-top:.2rem"><span class="method-num">%d</span>%s <span style="font-size:.78rem;color:var(--ink-pale)">%s</span></h3>'
                 % (i, esc(m["title"]), esc(it.get("en", ""))))
        if it.get("applies"):
            s.append('<div class="term-line" style="font-size:.82rem"><b>' + esc("适用 · applies") + '</b> ' + wl(it.get("applies")) + "</div>")
        if it.get("why 为何"):
            s.append('<div class="term-line"><b>' + esc("为何 · why") + '</b> ' + wl(it.get("why 为何")) + "</div>")
        if it.get("how 怎么做"):
            s.append('<div class="term-line" style="color:var(--ink-soft)"><b>' + esc("怎么做 · how") + '</b><br>' + wl(it.get("how 怎么做")) + "</div>")
        if it.get("rule 关联"):
            s.append('<div class="term-line" style="font-size:.82rem;color:var(--gold-dim)"><b>' + esc("关联 · rule") + '</b> ' + wl(it.get("rule 关联")) + "</div>")
        s.append("</div>")
    s.append('<div class="links"><a class="pill" href="glossary.html">↝ <span data-zh>术语架</span><span data-en>glossary</span></a>'
             '<a class="pill" href="index.html">↝ <span data-zh>板块首页</span><span data-en>the domain</span></a></div>')
    return page("方法论与透镜 · METHODS & LENSES", "METHODS", "方法论与透镜 · 怎么读", "一手先于转述 · 追溯谱系 · 双身对读 · 原型猎袭 · 理论即透镜", ["%d 法" % len(methods), "practice i 义"], "\n".join(s))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true", help="validate JSON only, no writes")
    args = ap.parse_args()
    site = load("site.json"); books = load("books.json")["books"]; authors = load("authors.json")["authors"]; relations = load("relations.json")
    if args.validate:
        print("books=%d authors=%d relations=ok site=ok" % (len(books), len(authors)))
        return 0
    crops = site["crops"]
    root = os.path.join(ROOT, *site["site"]["base"].split("/"))
    out = []
    books_all = {b["id"]: b for b in books}
    # iterate all crops: book pages + crop page
    bdir = os.path.join(root, "read", "books")
    os.makedirs(bdir, exist_ok=True)
    for crop in crops:
        for b_id in crop["book_ids"]:
            b = books_all.get(b_id)
            if not b:
                continue
            fp = os.path.join(bdir, b["slug"] + ".html")
            with open(fp, "w", encoding="utf-8") as f:
                f.write(book_page(site, b, crop))
            out.append(fp)
        fp = os.path.join(root, "read", crop["dir_page"])
        with open(fp, "w", encoding="utf-8") as f:
            f.write(crop_page(site, crop, [books_all[i] for i in crop["book_ids"] if i in books_all]))
        out.append(fp)
    # archive
    fp = os.path.join(root, "read", "index.html")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(archive_page(site, crops, books_all))
    out.append(fp)
    # authors
    fp = os.path.join(root, "authors", "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(authors_page(site, authors, relations))
    out.append(fp)
    # glossary (single source: readings/categories/glossary.md)
    fp = os.path.join(root, "glossary.html")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(glossary_page(site, load_md_sections("Reading_IA/readings/categories/glossary.md")))
    out.append(fp)
    # methods (single source: readings/methods/README.md)
    fp = os.path.join(root, "methods.html")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(methods_page(site, load_md_sections("Reading_IA/readings/methods/README.md")))
    out.append(fp)
    print("wrote %d files:" % len(out))
    for p in out:
        print("  " + os.path.relpath(p, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())