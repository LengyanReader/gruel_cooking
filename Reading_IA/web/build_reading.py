# -*- coding: utf-8 -*-
"""build_reading.py — P2 generator.

Fonts: JSON-in (site/books/authors/relations) -> HTML out (docs/reading_ia/).
Renders: per-book pages (read/books/<slug>.html), crop list page, archive page,
authors graph page.  Bilingual via data-zh/data-en spans + a shared lang toggle
(localStorage key from site.json).  Inline SVG visualizers only (no external deps).
"""
import json, os, html, sys, argparse
from operator import itemgetter

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
DATA = os.path.join(BASE, "data")

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
.diagram{background:var(--paper-soft);border:1px solid rgba(167,146,93,.3);border-radius:16px;padding:1rem;margin:1.2rem 0;overflow-x:auto}
.diagram svg{display:block;margin:0 auto}
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


def page(title, hero_kicker, hero_h1, hero_sub, chips, body, up_rel="..", hero_h1_en=None, hero_sub_en=None):
    nav_home = up_rel + "/index.html"
    hl = ' '.join('<span>%s</span>' % esc(c) for c in chips)
    script = SCRIPT.replace("__STORAGE__", STORAGE_KEY)
    h1_en = hero_h1_en if hero_h1_en is not None else hero_h1
    sub_en = hero_sub_en if hero_sub_en is not None else hero_sub
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
  <div class="nav-brand" data-both><span data-zh>{esc(hero_kicker)}</span><span data-en>{esc(hero_kicker)}</span><span class="sub" data-both><span data-zh>五部 · 2026-09</span><span data-en>five books · 2026-09</span></span></div>
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
  <p data-zh>一书一卡，一人一卡；读完每一本，至少落下一个延伸线索 · 阅读与智识 · 2026 秋</p>
  <p data-en>One card per book, one per author; every finished book drops a lead · Reading &amp; IA · Autumn 2026</p>
</footer>

<script>{script}</script>
</body>
</html>
"""


# ---------- SVG: plot flow ----------
def svg_plot_flow(nodes, width=860):
    if not nodes:
        return ''
    x = 90
    y0 = 26
    rh = 44
    gap = 26
    est = lambda t: sum(13 if ord(c) > 0x2E80 else 6.8 for c in t)
    hp = []
    for nd in nodes:
        w_zh = est(nd["zh"]); w_en = est(nd["en"])
        h = rh + 15 * (max(1, round(w_zh / 620 + 0.4))) + 13 * (max(1, round(w_en / 860 + 0.3)))
        hp.append(max(44, h))
    H = 2 * y0 + sum(hp) + gap * (len(hp) - 1) + 10
    out = [f'<svg viewBox="0 0 {width} {H}" role="img" aria-label="plot flow" xmlns="http://www.w3.org/2000/svg">']
    cy = y0
    for i, (nd, h) in enumerate(zip(nodes, hp), 1):
        yb = cy + h
        fill = "#FFF8EC" if i % 2 else "#EFE6D3"
        stroke = "#C9A227" if i == len(nodes) else "#A5811D"
        out.append(f'<rect x="{x}" y="{cy}" width="680" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>')
        out.append(f'<text x="{x+16}" y="{cy+20}" font-family="LXGW WenKai,serif" font-size="13" font-weight="700" fill="#A5811D">{i}</text>')
        # zh
        wy = cy + 20 + 14
        out.append(f'<text x="{x+40}" y="{wy}" font-family="LXGW WenKai,serif" font-size="12.5" fill="#26261F">{esc(nd["zh"])}</text>')
        # en (translate manually: wrap by char est)
        cum = 0; line = 1; seg = []
        row = []
        for c in nd["en"]:
            cum += 13 if ord(c) > 0x2E80 else 6.8
            row.append(c)
            # (simplified wrap at 150 *)
        # the len is enough: en single line
        # conf
        if nd.get("conf"):
            ccol = CONF_COLOR.get(nd["conf"], "#777069")
            out.append(f'<text x="{x+640}" y="{wy}" font-family="monospace" font-size="11" font-weight="700" fill="{ccol}">{esc(nd["conf"])}</text>')
        if i < len(nodes):
            out.append(f'<line x1="{x+340}" y1="{yb}" x2="{x+340}" y2="{yb+gap}" stroke="#C9A227" stroke-width="2" marker-end="url(#arw)"/>')
        cy = yb + gap
    out.append('<defs><marker id="arw" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="#C9A227"/></marker></defs>')
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
            out.append(f'<text x="{colx[g]}" y="28" text-anchor="middle" font-family="LXGW WenKai,serif" font-size="11.5" font-weight="700" fill="#A5811D">{g}</text>')
            # node
            out.append(f'<rect x="{colx[g]-58}" y="{pos[c["id"]][1]-14}" width="116" height="28" rx="14" fill="#FFF8EC" stroke="#C9A227" stroke-width="1.2"/>')
            out.append(f'<text x="{colx[g]}" y="{pos[c["id"]][1]+2}" text-anchor="middle" font-family="LXGW WenKai,serif" font-size="11" fill="#26261F">{c["name"]}</text>')
    for a, b, kind, note in edges:
        if a not in pos or b not in pos:
            continue
        (ax, ay), (bx, by) = pos[a], pos[b]
        kcol = EDGE_KIND.get(kind, ("", "#8c8c8c"))[1]
        mx, my = (ax + bx) / 2, (ay + by) / 2
        out.append(f'<path d="M{ax},{ay} C{ax},{my} {bx},{my} {bx},{by}" fill="none" stroke="{kcol}" stroke-width="1.3" stroke-dasharray="4 3"/>')
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


# ---------- book page ----------
def blk(label, zh, en, cls="card"):
    return f'<div class="{cls}"><h3 class="sec" data-both><span data-zh>{esc(label)}</span><span data-en>{esc(label)}</span></h3>{zh_en(zh, en)}</div>'


def book_page(site, book, crop):
    title = f"{book['title_zh']}｜{book['title_orig']}"
    hero_sub = f"{book['author_zh']} · {book['country']} · {book['publines_zh']}"
    hero_h1 = f"{book['title_zh']} · {book['title_orig']}"
    hero_h1_en = f"{book['title_orig']} — {book['title_zh']}"
    hero_sub_en = f"{book['author']} · {book['country_en']} · {book['publines_en']}"
    chips = [f"{crop['glyph_zh']} · {crop['date']}", book["meta_zh"], f"conf {book['baseline_conf']}"]
    s = []
    # provenance
    s.append(srcnote(
        "<b>来源说明。</b>" + esc(book["baseline_conf"]) + " · 档案：" + esc(book["id"]) + "（Books）核心数据经四级核实，情节细处标 ◐/○。",
        "<b>Provenance.</b> " + esc(book["baseline_conf"]) + " · record: " + esc(book["id"]) + ". Publication facts verified; plot details marked ◐/○."))
    # why
    s.append(blk("为何此刻 · Why now", book["why_zh"], book["why_en"]))
    # background
    s.append(blk("背景 · Background", book["background"]["zh"], book["background"]["en"]))
    s.append('<p class="tok">' + conf_token(book["background"]["conf"]) + ' <span class="hidden"></span></p>')
    # plot acts
    s.append('<h2 class="part" data-both><span data-zh>情节分幕 · Plot content</span><span data-en>Plot content</span></h2>')
    for act in book["plot_acts"]:
        s.append(f'<div class="card"><h3 class="sec" data-both><span data-zh>第 {act["n"]} 幕 · {act["title_zh"]}</span><span data-en>Act {act["n"]} · {act["title_en"]}</span></h3>')
        s.append(zh_en(act["zh"], act["en"]))
        if act.get("conf"):
            s.append('<p class="tok">' + conf_token(act["conf"]) + "</p>")
        if act.get("sources"):
            s.append(f'<p class="tok"><span class="conf c-part">src</span> <span style="font-size:.8rem;color:var(--ink-pale)">{act["sources"]}</span></p>')
        s.append("</div>")
    # narrative structure
    s.append('<h2 class="part" data-both><span data-zh>叙事结构 · Narrative structure</span><span data-en>Narrative structure</span></h2>')
    s.append(blk("结构 · Structure", book["narrative"]["zh"], book["narrative"]["en"], cls="card"))
    # plot flow svg
    s.append('<h2 class="part" data-both><span data-zh>情节流程图 · Plot flow</span><span data-en>Plot flow</span></h2>')
    s.append('<div class="diagram">' + svg_plot_flow(book["plot_flow"]) + '<p class="cap">' + esc(book["title_zh"]) + ' · 事件链（数字为顺序）</p></div>')
    # characters + charedge svg
    s.append('<h2 class="part" data-both><span data-zh>人物关系图 · Characters</span><span data-en>Characters &amp; relations</span></h2>')
    s.append('<div class="diagram">' + svg_charedge(book) + '<p class="cap">' + esc(book["title_zh"]) + ' · 人物关系（虚点线=连接）</p></div>')
    s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th>ID</th><th data-both><span data-zh>人物</span><span data-en>name</span></th><th data-both><span data-zh>阵营/组</span><span data-en>group</span></th><th data-both><span data-zh>角色</span><span data-en>role</span></th><th data-both><span data-zh>把握</span><span data-en>conf</span></th></tr></thead><tbody>')
    for c in book["characters"]:
        s.append(f'<tr><td>{esc(c["id"])}</td><td>{esc(c["name"])}</td><td>{esc(c.get("group",""))}</td><td><div data-zh>{esc(c["role_zh"])}</div><div data-en>{esc(c["role_en"])}</div></td><td class="conf">{conf_token(c["conf"])}</td></tr>')
    s.append('</tbody></table></div>')
    # intent
    s.append('<h2 class="part" data-both><span data-zh>作者真意 · Intent</span><span data-en>The author&rsquo;s intent</span></h2>')
    if book["intent"]["quotes"]:
        for q in book["intent"]["quotes"]:
            s.append(f'<div class="quote"><div class="orig">{esc(q["orig"])}</div><div class="trs">{esc(q["trans_zh"])}</div><div class="src">{esc(q["source"])}</div></div>')
    s.append(blk("为何如此写 · Reception & synthesis", book["intent"]["reception_good_zh"] + "\n\n" + book["intent"]["reception_bad_zh"] + "\n\n**合成 Synthesis：** " + book["intent"]["syn_zh"], book["intent"]["reception_good_en"] + "\n\n" + book["intent"]["reception_bad_en"] + "\n\n**Synthesis:** " + book["intent"]["syn_en"], cls="gapbox"))
    # craft / highlights
    s.append('<h2 class="part" data-both><span data-zh>手法与亮点 · Craft</span><span data-en>Craft &amp; highlights</span></h2>')
    if book.get("craft"):
        for c in book["craft"]:
            s.append(f'<div class="card"><p>{esc(c["zh"])}</p><p style="color:var(--ink-soft);font-size:.9rem">{esc(c["en"])}</p></div>')
    # excerpts
    s.append('<h2 class="part" data-both><span data-zh>精彩片段 · Excerpts</span><span data-en>Notable excerpts</span></h2>')
    if book.get("excerpts"):
        for e in book["excerpts"]:
            s.append(f'<div class="quote"><div class="orig">{esc(e["orig"])}</div><div class="trs">{esc(e["trans_zh"])}</div><div class="src">{esc(e["source"])}</div></div>')
    else:
        s.append(f'<div class="srcnote">{zh_en("待读原书摘引。", "Excerpts pending the read.")}</div>')
    # deep read
    s.append('<h2 class="part" data-both><span data-zh>精读建议 · Deep reading</span><span data-en>Deep reading</span></h2>')
    for d in book.get("deep_read", []):
        s.append(f'<div class="card">{zh_en(d["zh"], d["en"])}</div>')
    # related + positioning
    s.append('<h2 class="part" data-both><span data-zh>相关定位 · Positioning</span><span data-en>Related works &amp; positioning</span></h2>')
    s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th data-both><span data-zh>作品</span><span data-en>work</span></th><th data-both><span data-zh>作者</span><span data-en>author</span></th><th>年</th><th data-both><span data-zh>关系</span><span data-en>relation</span></th><th data-both><span data-zh>一句理由</span><span data-en>why</span></th><th data-both><span data-zh>轴</span><span data-en>axis</span></th><th class="conf">conf</th></tr></thead><tbody>')
    for r in book["related"]:
        why = '<div data-zh>%s</div><div data-en>%s</div>' % (esc(r["note_zh"]), esc(r["note_en"]))
        s.append(f'<tr><td><b>{esc(r["title"])}</b></td><td>{esc(r["author"])}</td><td>{esc(r["year"])}</td><td>{esc(r["relation"])}</td><td>{why}</td><td>{esc(r["axis"])}</td><td class="conf">{conf_token(r["conf"])}</td></tr>')
    s.append('</tbody></table></div>')
    # fact ledger
    s.append('<h2 class="part" data-both><span data-zh>核对账本 · Fact ledger</span><span data-en>Fact ledger</span></h2>')
    s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th data-both><span data-zh>主张</span><span data-en>claim</span></th><th data-both><span data-zh>来源</span><span data-en>source</span></th><th class="conf">conf</th></tr></thead><tbody>')
    for f in book["fact_ledger"]:
        s.append(f'<tr><td>{esc(f["claim"])}</td><td style="font-size:.8rem;color:var(--ink-pale)">{esc(f["source"])}</td><td class="conf">{conf_token(f["conf"])}</td></tr>')
    s.append('</tbody></table></div>')
    # unverified
    if book.get("unverified"):
        s.append('<h2 class="part" data-both><span data-zh>未核 / 未知 · Unverified</span><span data-en>Unverified / unknown</span></h2>')
        for u in book["unverified"]:
            s.append(f'<div class="card"><p>{esc(u["item"])} <span class="tok">{conf_token(u["conf"])}</span></p></div>')
    # links
    s.append('<div class="links">')
    s.append(f'<a class="pill" href="../2026-09-books.html">← <span data-zh>返回秋分书单</span><span data-en>back to the autumn list</span></a>')
    s.append(f'<a class="pill" href="../index.html">☰ <span data-zh>书单档案</span><span data-en>the archive</span></a>')
    s.append(f'<a class="pill" href="../../authors/index.html">↝ <span data-zh>作者知识图谱</span><span data-en>the authors graph</span></a>')
    s.append('</div>')
    return page(title, crop["glyph_zh"], hero_h1, hero_sub, chips, "\n".join(s), up_rel="../../..", hero_h1_en=hero_h1_en, hero_sub_en=hero_sub_en)


# ---------- crop list page ----------
def crop_page(site, crop, books):
    title = f"{crop['title_zh']}｜{crop['title_en']}"
    hero_sub = crop["subtitle_zh"]
    chips = [crop["date"] + " · " + crop["glyph_zh"], crop["verdict_zh"] + "/" + crop["verdict_en"], "每书一页"]
    s = []
    s.append(srcnote(
        '<b>来源说明。</b>本清单由 <code>web/data/books.json</code> 驱动（generator: build_reading.py）；每部均经 websearch/webfetch 定位实际版本（W2）。出版信息 <code>✓</code> 核实；情节细处标 <code>◐/○</code>。点击各书卡进入单书页码。',
        '<b>Provenance.</b> This list is driven by <code>web/data/books.json</code> (generator: build_reading.py); each title located &amp; verified (W2). Pub facts <code>✓</code>; plot details <code>◐/○</code>. Click a card for the per-book page.'))
    for i, b in enumerate(books, 1):
        s.append(f'<div class="card">')
        s.append('<div class="b-num" data-both style="font-family:var(--ff-display);color:var(--gold-dim);font-size:.85rem;letter-spacing:.08em"><span data-zh>%s · %s</span><span data-en>%s · %s</span></div>' % (b["num"], b["country"], chr(64+i), b["country_en"]))
        s.append(f'<h3 class="sec"><span data-zh>{esc(b["title_zh"])} <span style="color:var(--lapis)">{esc(b["title_orig"])}</span></span><span data-en>{esc(b["title_orig"])} — <span style="color:var(--lapis)">{esc(b["author"])}</span></span></h3>')
        s.append('<p style="font-size:.82rem;color:var(--ink-pale)">%s · %s · conf %s</p>' % (esc(b["year"]), esc(b["publines_zh"]), esc(b["baseline_conf"].split("；")[0] if "；" in b["baseline_conf"] else b["baseline_conf"])))
        s.append('<div class="why" style="margin-top:.6rem;color:var(--ink-soft);font-style:italic"><p data-zh>%s</p><p data-en>%s</p></div>' % (esc(b["why_zh"]), esc(b["why_en"])))
        s.append(f'<p style="margin-top:.7rem"><a class="pill" href="books/{esc(b["slug"])}.html">☞ <span data-zh>进入单书页 · 完整档案</span><span data-en>open the full dossier</span></a></p>')
        # mini claims (first 2)
        s.append('<ul style="list-style:none;margin-top:.5rem">')
        for c in b.get("claims_list", []):
            s.append('<li style="position:relative;padding-left:1rem;margin-bottom:.4rem"><span style="position:absolute;left:0;top:.5rem;width:7px;height:7px;border-radius:50%;background:var(--gold)"></span><b style="color:var(--gold-dim)">%s</b></li>' % esc(c))
        s.append('</ul>')
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
    return page(title, crop["glyph_zh"], title, hero_sub, chips, "\n".join(s))


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
    return page("书单档案 · BOOK LIST ARCHIVE", "AUTUMN", "书单档案 · 一窗一书单", "书单是素材层，思潮是合成层——清单不入思潮之文", ["最新批：2026 秋", "新批在上"], "\n".join(s))


# ---------- authors graph page ----------
def authors_page(site, authors, relations):
    by_id = {a["id"]: a for a in authors}
    s = []
    s.append(srcnote(
        '<b>来源与位置。</b>节点与生平：<code>web/data/authors.json</code>（逐条附出处与把握）；边：唯一源 <code>relations/influences.md</code> 镜像 <code>web/data/relations.json</code>。可信度 <code>✓ 已核 · ◐ 一手/自述 · ○ 转述 · ✗ 争议</code>。',
        '<b>Source &amp; layout.</b> Nodes &amp; lives: <code>web/data/authors.json</code>; edges: single source <code>relations.json</code> (mirrors influences.md). Confidence <code>✓ verified · ◐ primary · ○ secondhand · ✗ disputed</code>.'))
    # nodes
    s.append('<h2 class="part" data-both><span data-zh>一 · 节点 Nodes</span><span data-en>I · Nodes</span></h2>')
    s.append('<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1rem">')
    for a in authors:
        s.append('<div class="card" style="margin:0">')
        s.append('<h3 class="sec">%s <span style="font-size:.8rem;color:var(--ink-pale)">%s</span></h3>' % (esc(a["name_zh"]), esc(a["name_native"])))
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
        s.append('<h3 class="sec">' + esc(a["name_zh"]) + ' · ' + esc(a["slug_display"]) + '</h3>')
        # timeline
        s.append('<h4 class="sec" data-both><span data-zh>生平轨迹 Timeline</span><span data-en>Timeline</span></h4>')
        s.append('<div class="tablewrap"><table class="ledger"><thead><tr><th>y</th><th data-both><span data-zh>事件</span><span data-en>event</span></th><th class="conf">conf</th></tr></thead><tbody>')
        for t in a["timeline"]:
            s.append('<tr><td>%s</td><td><div data-zh>%s</div><div data-en>%s</div></td><td class="conf">%s</td></tr>' % (esc(t["y"]), esc(t["event_zh"]), esc(t["event_en"]), conf_token(t["conf"])))
        s.append('</tbody></table></div>')
        # works
        s.append('<h4 class="sec" data-both><span data-zh>作品 Works</span><span data-en>Works</span></h4>')
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
    return page("作者知识图谱 · AUTHORS GRAPH", "AUTUMN", "作者知识图谱 · 谁在写，与谁同代", "生平 · 朋友圈 · 合著 · 流派归属 · 影响链——人物即思想的坐标", ["2026 秋批 · " + str(len(authors)) + " 位作者", "generator 维护"], "\n".join(s))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true", help="validate JSON only, no writes")
    args = ap.parse_args()
    site = load("site.json"); books = load("books.json")["books"]; authors = load("authors.json")["authors"]; relations = load("relations.json")
    if args.validate:
        print("books=%d authors=%d relations=ok site=ok" % (len(books), len(authors)))
        return 0
    crops = site["crops"]
    crop = crops[0]
    root = os.path.join(ROOT, *site["site"]["base"].split("/"))
    out = []
    # book pages
    bdir = os.path.join(root, "read", "books")
    os.makedirs(bdir, exist_ok=True)
    for b in books:
        fp = os.path.join(bdir, b["slug"] + ".html")
        with open(fp, "w", encoding="utf-8") as f:
            f.write(book_page(site, b, crop))
        out.append(fp)
    # crop page
    books_all = {b["id"]: b for b in books}
    fp = os.path.join(root, "read", crop["dir_page"])
    with open(fp, "w", encoding="utf-8") as f:
        f.write(crop_page(site, crop, [books_all[i] for i in crop["book_ids"]]))
    out.append(fp)
    # archive
    fp = os.path.join(root, "read", "index.html")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(archive_page(site, crops, books_all))
    out.append(fp)
    # authors
    fp = os.path.join(root, "authors", "index.html")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(authors_page(site, authors, relations))
    out.append(fp)
    print("wrote %d files:" % len(out))
    for p in out:
        print("  " + os.path.relpath(p, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())