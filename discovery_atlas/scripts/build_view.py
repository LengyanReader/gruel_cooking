#!/usr/bin/env python3
"""Discovery Atlas · static web view generator.

Reads sources/*.json (the verified registry) and emits a self-contained,
filterable, bilingual (zh/en) static site at docs/discovery_atlas/index.html.
No data is hardcoded here — the view is always regenerated from the registry,
so it can be re-run after any batch. Opens fully offline on double-click.

Usage (from module root):  python scripts/build_view.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent           # .../discovery_atlas
REPO = ROOT.parent                                       # .../gruel_cooking
OUT = REPO / "docs" / "discovery_atlas" / "index.html"

LAYERS = ["discovery", "criticism", "publishing", "infrastructure", "access"]
DOMAINS = ["books", "music", "film", "art"]


def load_entries():
    ents = []
    for f in sorted((ROOT / "sources"). glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        for e in data.get("sources", []):
            ents.append(e)
    return ents


def build():
    ents = load_entries()
    # keep only fields the view needs; shrink payload
    slim = []
    for e in ents:
        slim.append({
            "id": e.get("id", ""),
            "qid": e.get("wikidata_qid", ""),
            "domain": e.get("domain", ""),
            "layer": e.get("layer", ""),
            "circle": e.get("circle", ""),
            "name": e.get("name", ""),
            "url": e.get("url", ""),
            "langs": e.get("langs", []),
            "regions": e.get("regions", []),
            "kind": e.get("kind", ""),
            "why": e.get("why", ""),
            "not_for": e.get("not_for", ""),
            "verified": e.get("verified", ""),
            "status": e.get("status", ""),
            "note": e.get("note", ""),
        })
    circles = sorted({e["circle"] for e in slim})
    dom_counts = {d: sum(1 for e in slim if e["domain"] == d) for d in DOMAINS}
    qid_count = sum(1 for e in slim if e["qid"])
    live_count = sum(1 for e in slim if str(e["verified"]).startswith("\u2714"))
    payload = {
        "generated": "2026-10-27",
        "total": len(slim),
        "qid": qid_count,
        "live": live_count,
        "domains": dom_counts,
        "circles": circles,
        "entries": slim,
    }
    html = TEMPLATE.replace("__DATA__", json.dumps(payload, ensure_ascii=False))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT}  ·  {len(slim)} entries · {qid_count} QID · {live_count} live")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>发现星图 · Discovery Atlas</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai:wght@300;400;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --sky-deep:#4A90C2;--sky-mid:#7AB8D9;--sky-light:#A8D4EC;
  --warm-cream:#FFFBF5;--warm-soft:#FFF5E6;--warm-gold:#F5C97E;--warm-amber:#E8A855;
  --ink-deep:#3A3228;--ink-mid:#5C5248;--ink-soft:#8A7E72;--ink-pale:#B8AFA4;
  --accent-teal:#5BA3A3;--accent-coral:#D4836A;--accent-violet:#8B7BAA;--accent-sage:#7A9E7E;
  --ff-display:"LXGW WenKai","Noto Serif SC",serif;--ff-body:"Inter","LXGW WenKai","Noto Sans SC",sans-serif;
  --ff-zh:"LXGW WenKai","Noto Serif SC",serif;--shadow-md:0 6px 20px rgba(58,50,40,.07);--shadow-lg:0 12px 40px rgba(58,50,40,.09);
}
body.lang-zh [data-en]{display:none!important}
body.lang-en [data-zh]{display:none!important}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased}
body{font-family:var(--ff-body);color:var(--ink-deep);background:var(--warm-cream);line-height:1.7;overflow-x:hidden}
a{color:var(--accent-teal);text-decoration:none}a:hover{color:var(--sky-deep)}
.nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:.7rem 2rem;display:flex;align-items:center;justify-content:space-between;
  background:rgba(255,251,245,.75);backdrop-filter:blur(20px) saturate(1.3);border-bottom:1px solid rgba(228,220,208,.4)}
.nav-brand{font-family:var(--ff-display);font-weight:700;font-size:1.25rem;color:var(--ink-deep);letter-spacing:.04em}
.nav-brand .pinyin{font-size:.65em;color:var(--ink-soft);margin-left:.4em;font-weight:400}
.lang-toggle{display:flex;border-radius:20px;overflow:hidden;border:1px solid rgba(228,220,208,.6);background:var(--warm-cream);font-size:.8rem;font-weight:500;cursor:pointer}
.lang-toggle button{border:none;padding:5px 14px;cursor:pointer;font-family:var(--ff-body);font-size:.8rem;font-weight:500;color:var(--ink-soft);background:transparent;transition:.25s}
.lang-toggle button.active{background:linear-gradient(135deg,var(--warm-gold),var(--warm-amber));color:#fff}
.hero{padding:7rem 2rem 3rem;text-align:center;background:linear-gradient(170deg,#5A9ECF 0%,#7AB8D9 18%,#A8D4EC 38%,#D4E8F0 55%,#F0E4D0 74%,#FFFBF5 100%)}
.hero h1{font-family:var(--ff-display);font-size:clamp(2rem,5vw,3.2rem);font-weight:700;color:var(--ink-deep);letter-spacing:.05em;margin-bottom:.4rem}
.hero .sub{font-family:var(--ff-zh);font-size:1.05rem;color:var(--ink-mid);font-weight:300;letter-spacing:.06em;max-width:640px;margin:0 auto .4rem;line-height:1.9}
.hero .stat-row{display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:center;margin-top:1.5rem;font-size:.9rem;color:var(--ink-soft)}
.hero .stat-row b{font-family:var(--ff-display);font-size:1.4rem;color:var(--warm-amber);font-weight:700;margin-right:.25em}
.controls{max-width:1200px;margin:0 auto;padding:1.5rem 2rem .5rem;display:flex;flex-direction:column;gap:.8rem}
.ctrl-row{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem}
.ctrl-row .lbl{font-size:.78rem;color:var(--ink-pale);min-width:52px;letter-spacing:.04em}
.chip{border:1px solid rgba(228,220,208,.7);background:var(--warm-cream);color:var(--ink-soft);border-radius:99px;padding:4px 14px;font-size:.8rem;font-weight:500;cursor:pointer;transition:.2s;font-family:var(--ff-body)}
.chip:hover{border-color:var(--warm-gold);color:var(--ink-deep)}
.chip.active{background:linear-gradient(135deg,var(--warm-gold),var(--warm-amber));color:#fff;border-color:transparent}
select.chip{border-radius:10px}
.search{flex:1;min-width:200px;padding:8px 14px;border:1px solid rgba(228,220,208,.7);border-radius:12px;font-family:var(--ff-body);font-size:.9rem;background:var(--warm-cream);color:var(--ink-deep)}
.search:focus{outline:none;border-color:var(--warm-amber)}
.count-line{max-width:1200px;margin:0 auto;padding:0 2rem;font-size:.85rem;color:var(--ink-soft)}
.grid{max-width:1200px;margin:0 auto;padding:1.2rem 2rem 4rem;display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:1.4rem}
.card{background:var(--warm-cream);border:1px solid rgba(228,220,208,.55);border-radius:16px;padding:1.4rem 1.5rem;box-shadow:var(--shadow-md);position:relative;transition:transform .25s,box-shadow .25s;overflow:hidden}
.card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg)}
.card::before{content:"";position:absolute;top:0;left:0;right:0;height:3px}
.card[data-d="books"]::before{background:linear-gradient(90deg,var(--sky-mid),var(--sky-light))}
.card[data-d="music"]::before{background:linear-gradient(90deg,var(--accent-coral),#E8A890)}
.card[data-d="film"]::before{background:linear-gradient(90deg,var(--accent-violet),#AEA0CC)}
.card[data-d="art"]::before{background:linear-gradient(90deg,var(--accent-sage),#9CBEA0)}
.card h3{font-family:var(--ff-display);font-size:1.2rem;font-weight:700;color:var(--ink-deep);line-height:1.3;margin-bottom:.5rem}
.card h3 a{color:var(--ink-deep)}.card h3 a:hover{color:var(--accent-teal)}
.badges{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:.7rem}
.badge{display:inline-block;padding:2px 10px;border-radius:99px;font-size:.7rem;font-weight:600;background:var(--warm-soft);color:var(--ink-soft);border:1px solid rgba(228,220,208,.4)}
.badge.layer{background:#E8F4FA;color:#3F7290}
.badge.kind{background:#EDE8F4;color:#6A5A86}
.badge.circle{background:#E0F0E6;color:#4A7050}
.card .why{font-size:.9rem;color:var(--ink-mid);margin-bottom:.55rem;line-height:1.7}
.card .notfor{font-size:.82rem;color:var(--ink-pale);margin-bottom:.7rem;line-height:1.6}
.card .notfor b{color:var(--accent-coral);font-weight:600}
.card .foot{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.5rem;border-top:1px dashed rgba(228,220,208,.7);padding-top:.6rem;font-size:.75rem;color:var(--ink-pale)}
.vdot{display:inline-flex;align-items:center;gap:5px;font-weight:600}
.vdot.live{color:var(--accent-sage)}.vdot.gated{color:var(--warm-amber)}.vdot.pend{color:var(--accent-coral)}
.ext{display:inline-flex;align-items:center;gap:4px;color:var(--accent-teal)}
.meta-dim{opacity:.85}
.empty{grid-column:1/-1;text-align:center;color:var(--ink-pale);padding:3rem;font-family:var(--ff-zh)}
.footer{text-align:center;padding:2.5rem 2rem 3rem;color:var(--ink-pale);font-size:.82rem;border-top:1px solid rgba(228,220,208,.4)}
.footer .motto{font-family:var(--ff-zh);font-size:1.05rem;color:var(--ink-soft);margin-bottom:.3rem}
.footer .prov{max-width:640px;margin:.6rem auto 0;line-height:1.7}
@media(max-width:768px){.nav{padding:.6rem 1rem}.hero{padding-top:5.5rem}.grid{grid-template-columns:1fr;padding:1rem}.controls{padding:1rem}.ctrl-row .lbl{min-width:auto}}
</style>
</head>
<body class="lang-zh">
<nav class="nav">
  <div class="nav-brand"><span data-zh>发现星图</span><span data-en>Discovery Atlas</span><span class="pinyin">zh</span></div>
  <div class="lang-toggle" id="langToggle"><button class="active" data-lang="zh">中</button><button data-lang="en">EN</button></div>
</nav>
<section class="hero">
  <h1><span data-zh>发现星图 · 跨媒介发现源登记库</span><span data-en>Discovery Atlas · A registry of discovery sources</span></h1>
  <p class="sub"><span data-zh>书 · 乐 · 影 · 艺——按 五层 × 文明圈 归档的「去哪儿找好东西」的地图。每条均经实测探针与回源核实；<b>只登记信息，不代为获取</b>。</span><span data-en>Books · Music · Film · Art — a map of "where to find good things", filed across five layers and civilizational circles. Every entry is probe-tested and source-verified; the atlas only records information, never fetches on your behalf.</span></p>
  <div class="stat-row" id="statRow"></div>
</section>
<div class="controls">
  <div class="ctrl-row"><span class="lbl"><span data-zh>域</span><span data-en>Domain</span></span><span id="domChips"></span></div>
  <div class="ctrl-row"><span class="lbl"><span data-zh>层</span><span data-en>Layer</span></span><span id="layerChips"></span></div>
  <div class="ctrl-row"><span class="lbl"><span data-zh>圈</span><span data-en>Circle</span></span><select class="chip" id="circleSel"></select>
    <span class="lbl" style="margin-left:1rem"><span data-zh>核验</span><span data-en>Verified</span></span><span id="verChips"></span>
    <input class="search" id="search" placeholder="搜索 name / why…"></div>
</div>
<div class="count-line" id="countLine"></div>
<main class="grid" id="grid"></main>
<footer class="footer">
  <div class="motto"><span data-zh>来源先于叙述 · 只登记，不获取</span><span data-en>Sources before narrative · record only, never fetch</span></div>
  <div class="prov"><span data-zh>本页由 <code>scripts/build_view.py</code> 从 <code>sources/*.json</code> 生成，随批次可重跑。✔=本会话实测可达 · ○=正典域名未本次确认（403/429 反爬或网络待复测）。</span><span data-en>Generated by <code>scripts/build_view.py</code> from <code>sources/*.json</code>; re-run any time. &#10004; = reachable in-session &#183; &#9675; = canonical domain not confirmed this session (bot-gated or pending re-test).</span></div>
</footer>
<script>
const DATA = __DATA__;
const L_ZH={discovery:"发现",criticism:"批评",publishing:"出版",infrastructure:"基础设施",access:"获取"};
const L_EN={discovery:"Discovery",criticism:"Criticism",publishing:"Publishing",infrastructure:"Infrastructure",access:"Access"};
const D_ZH={books:"书",music:"乐",film:"影",art:"艺"};
const S_ZH={active:"可达","bot-gated":"反爬",pending:"待复测",moved:"已迁移",contested:"有争议"};
const state={domain:"",layer:"",circle:"",ver:"",q:""};
function el(t,c,h){const e=document.createElement(t);if(c)e.className=c;if(h!=null)e.innerHTML=h;return e;}
function verClass(e){if(String(e.verified).startsWith("\u2714"))return"live";if(e.status==="pending")return"pend";return"gated";}
function verGlyph(e){if(String(e.verified).startsWith("\u2714"))return"\u2714 "+e.verified.replace("\u2714","").trim();return"\u96cb";}
function buildChips(id,items,key){const box=document.getElementById(id);
  const all=el("button","chip active");all.innerHTML='<span data-zh>全部</span><span data-en>All</span>';
  all.onclick=()=>{state[key]="";setActive(box,all);render();};box.appendChild(all);
  items.forEach(it=>{const b=el("button","chip");
    b.innerHTML=key==="domain"?`<span data-zh>${D_ZH[it]}</span><span data-en>${it}</span>`:
      key==="layer"?`<span data-zh>${L_ZH[it]}</span><span data-en>${L_EN[it]}</span>`:it;
    b.onclick=()=>{state[key]=it;setActive(box,b);render();};box.appendChild(b);});}
function setActive(box,btn){box.querySelectorAll(".chip").forEach(c=>c.classList.remove("active"));btn.classList.add("active");}
function initStats(){const s=document.getElementById("statRow");
  s.innerHTML=`<span><b>${DATA.total}</b><span data-zh>条源</span><span data-en>sources</span></span>`+
    `<span><b>${DATA.qid}</b><span data-zh>维基数据主键</span><span data-en>Wikidata QIDs</span></span>`+
    `<span><b>${DATA.live}</b><span data-zh>实测可达</span><span data-en>probe-verified</span></span>`+
    `<span><b>${DATA.circles.length}</b><span data-zh>文明圈</span><span data-en>circles</span></span>`;}
function render(){const g=document.getElementById("grid");g.innerHTML="";
  const q=state.q.toLowerCase();
  const rows=DATA.entries.filter(e=>
    (!state.domain||e.domain===state.domain)&&(!state.layer||e.layer===state.layer)&&
    (!state.circle||e.circle===state.circle)&&
    (!state.ver||(state.ver==="live"?String(e.verified).startsWith("\u2714"):!String(e.verified).startsWith("\u2714")))&&
    (!q||((e.name+" "+e.why+" "+e.id+" "+e.kind).toLowerCase().includes(q))));
  rows.sort((a,b)=>a.domain.localeCompare(b.domain)||a.layer.localeCompare(b.layer)||a.circle.localeCompare(b.circle));
  document.getElementById("countLine").innerHTML=`<span data-zh>显示 <b>${rows.length}</b> / ${DATA.total} 条</span><span data-en>Showing <b>${rows.length}</b> of ${DATA.total}</span>`;
  if(!rows.length){g.appendChild(el("div","empty",'<span data-zh>无匹配条目</span><span data-en>No matching entries</span>'));return;}
  rows.forEach(e=>{const c=el("div","card");c.setAttribute("data-d",e.domain);
    const host=(e.url.match(/https?:\/\/([^\/]+)/)||[])[1]||e.url;
    const qidLink=e.qid?`<a class="ext" href="https://www.wikidata.org/wiki/${e.qid}" target="_blank" rel="noopener">${e.qid}&#8599;</a>`:"";
    c.innerHTML=`<h3><a href="${e.url}" target="_blank" rel="noopener">${e.name}</a></h3>`+
      `<div class="badges"><span class="badge layer">${document.body.classList.contains("lang-en")?L_EN[e.layer]:L_ZH[e.layer]}</span>`+
      `<span class="badge circle">${e.circle}</span><span class="badge kind">${e.kind}</span></div>`+
      `<p class="why">${e.why}</p><p class="notfor"><b>&#215;&nbsp;</b>${e.not_for}</p>`+
      `<div class="foot"><span class="vdot ${verClass(e)}">${verGlyph(e)} · ${document.body.classList.contains("lang-en")?e.status:(S_ZH[e.status]||e.status)}</span>`+
      `<span class="meta-dim">${host}${qidLink?" · "+qidLink:""}</span></div>`;
    g.appendChild(c);});}
function applyLang(){document.querySelectorAll(".badge.layer,.card .vdot").forEach(()=>{});render();}
document.addEventListener("DOMContentLoaded",()=>{
  initStats();
  buildChips("domChips",DATA.domains?Object.keys(DATA.domains):["books","music","film","art"],"domain");
  buildChips("layerChips",["discovery","criticism","publishing","infrastructure","access"],"layer");
  const cs=document.getElementById("circleSel");
  cs.innerHTML='<option value="">'+(document.body.classList.contains("lang-en")?"All circles":"全部圈")+'</option>'+
    DATA.circles.map(c=>`<option value="${c}">${c}</option>`).join("");
  cs.onchange=()=>{state.circle=cs.value;render();};
  const vb=document.getElementById("verChips");
  [["","<span data-zh>全部</span><span data-en>All</span>","all"],
   ["live","<span data-zh>\u2714 可达</span><span data-en>\u2714 live</span>","live"],
   ["gated","<span data-zh>\u96cb 待确认</span><span data-en>\u9675 pending</span>","gated"]].forEach(v=>{
    const b=el("button","chip"+(v[2]==="all"?" active":""));b.innerHTML=v[1];
    b.onclick=()=>{state.ver=v[0];vb.querySelectorAll(".chip").forEach(x=>x.classList.remove("active"));b.classList.add("active");render();};
    vb.appendChild(b);});
  document.getElementById("search").oninput=e=>{state.q=e.target.value;render();};
  const tg=document.getElementById("langToggle");
  tg.querySelectorAll("button").forEach(b=>b.onclick=()=>{document.body.className="lang-"+b.dataset.lang;
    tg.querySelectorAll("button").forEach(x=>x.classList.toggle("active",x===b));
    cs.innerHTML='<option value="">'+(b.dataset.lang==="en"?"All circles":"全部圈")+'</option>'+DATA.circles.map(c=>`<option value="${c}"${c===state.circle?" selected":""}>${c}</option>`).join("");
    render();});
  render();});
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
