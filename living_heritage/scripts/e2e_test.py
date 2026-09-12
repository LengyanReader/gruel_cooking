import re
import os
import sys
import http.cookiejar
import urllib.request

sys.path.insert(0, ".")

PORT = os.getenv("LH_PORT", "8000")
BASE = f"http://127.0.0.1:{PORT}"

cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

op.open(urllib.request.Request(f"{BASE}/locale/zh", data=b"", method="POST"))
r = op.open(f"{BASE}/")
b = r.read().decode("utf-8")

m = re.search(r'nav-brand[^>]*>\s*<a[^>]*>(.*?)</a>', b, re.S)
print("brand:", m.group(1).strip())

m = re.search(r"hero-title[^>]*>(.*?)<", b)
print("hero:", m.group(1))

m = re.search(r'class="nav-links".*?href="/"[^>]*>(.*?)<', b, re.S)
print("nav.home label:", m.group(1))

m = re.search(r'class="nav-links">(.*?)</ul>', b, re.S)
print("nav item count:", m.group(1).count("<li>") if m else -1)
print("has nav /graph:", '/graph' in b)

print("has zh text:", "\u6587\u5316" in b)
print("has new slogan \u5468\u4e88\u6148\u821f:", "\u5468\u4e88\u6148\u821f" in b)
print("has footer \u5468\u6e21\u4e07\u6d32:", "\u5468\u6e21\u4e07\u6d32" in b)

# brand consistency: nav-sub, hero kicker, footer all from brand.* keys
print("brand nav-sub (zh):", "\u6d3b\u6001\u6587\u5316\u5eca\u9053" in b)
print("brand kicker (zh):", "\u5468\u4e88\u6148\u821f\u3001\u5468\u6e21\u4e07\u6d32\u3001\u559d\u7ca5\u6696\u80c3" in b or "\u5468\u4e88\u6148\u821f\uff0c\u5468\u6e21\u4e07\u6d32\uff0c\u559d\u7ca5\u6696\u80c3" in b)
print("brand footer identity (zh):", "\u5468\u821f\u6d32\u7ca5 \u00b7 \u6d3b\u6001\u6587\u5316\u5eca\u9053" in b)

# en variant default locale: brand strings should match the en seed
raw = urllib.request.urlopen(f"{BASE}/").read().decode("utf-8")
print("en brand kicker:", "the bark, the isles, the gruel" in raw)
print("en brand nav-sub:", "\u5468\u821f\u6d32\u7ca5" in raw)
print("en footer zhou_line:", "the bark, the isles, the gruel" in raw)

# static asset check
r = urllib.request.urlopen(f"{BASE}/css/main.css")
mc = r.read().decode("utf-8")
print("css ok, len:", len(mc), "has --gold:", "--gold" in mc)
r = urllib.request.urlopen(f"{BASE}/js/locale.js")
print("js ok, len:", len(r.read()))

# zh variants across pages (reuse cookie opener)
for p in ["/corridors", "/scholars", "/graph", "/literature", "/methodology", "/fieldwork"]:
    b = op.open(f"{BASE}" + p).read().decode("utf-8")
    print(p, "len:", len(b), "has 北京大运河:", "\u5317\u4eac\u5927\u8fd0\u6cb3" in b)

# zh publications page specifics
pb = op.open(f"{BASE}/publications").read().decode("utf-8")
print("publications has 研究资料库:", "\u7814\u7a76\u8d44\u6599\u5e93" in pb,
      "| lvl-a chip:", "lvl-a" in pb,
      "| source_level A:", "[A]" in pb,
      "| verified Gillette:", "Gillette" in pb)

# zh graph page specifics
gb = op.open(f"{BASE}/graph").read().decode("utf-8")
print("graph has \u77e5\u8bc6\u56fe\u8c31:", "\u77e5\u8bc6\u56fe\u8c31" in gb,
      "| belongs_to:", "belongs_to" in gb, "| studies:", "studies" in gb)

# zh literature page specifics
lb = op.open(f"{BASE}/literature").read().decode("utf-8")
print("literature has 品味:", "\u54c1\u5473" in lb, "| 哲学:", "\u54f2\u5b66" in lb, "| 代表作品:", "代表作品" in lb, "| 前提:", "\u524d\u63d0" in lb)
print("literature has portrait grid:", 'portrait-grid' in lb, "| dim-flow:", 'dim-flow' in lb)

# en variant of literature page (fresh opener without zh cookie)
raw = urllib.request.urlopen(f"{BASE}/literature").read().decode("utf-8")
print("en literature ok:", "Literature Review" in raw and "taste" in raw and "premises" in raw)

# ── research library filters ──
print("pubs filter bar:", "filter-pill" in pb)
fc = op.open(f"{BASE}/publications?corridor=grand_canal").read().decode("utf-8")
print("pubs corridor=grand_canal keeps 瓷器之都:", "\u74f7\u5668\u4e4b\u90fd" in fc,
      "| excludes gotland-only 2026 (波的尼亚湾):", "\u6ce2\u7684\u5c3c\u4e9a\u6e7e" not in fc)
fl = op.open(f"{BASE}/publications?level=A").read().decode("utf-8")
print("pubs level=A has 瓷器之都:", "\u74f7\u5668\u4e4b\u90fd" in fl)

# ── fieldwork corridor grouping ──
print("fieldwork grouped (组标题-北京大运河):", "\u5317\u4eac\u5927\u8fd0\u6cb3" in op.open(f"{BASE}/fieldwork").read().decode("utf-8"))

# ── literature dimensions view ──
ld = op.open(f"{BASE}/literature?view=dimensions").read().decode("utf-8")
print("literature dimensions has tabs:", "lit-tab" in ld,
      "| 按内容维度导览:", "\u6309\u5185\u5bb9\u7ef4\u5ea6\u5bfc\u89c8" in ld,
      "| 廊道与移动:", "\u5eca\u9053\u4e0e\u79fb\u52a8" in ld,
      "| 食物廊道:", "\u98df\u7269\u5eca\u9053" in ld,
      "| 方法论:", "\u65b9\u6cd5\u8bba" in ld)

# ── knowledge graph edges on page ──
print("graph relations authored:", "authored" in gb, "| involves:", "involves" in gb,
      "| related literature:", "\u76f8\u5173\u6587\u732e" in gb)

# ── SEO / OG meta on public pages ──
print("seo og:site_name:", "property=\"og:site_name\"" in b,
      "| og:title:", "property=\"og:title\"" in b,
      "| twitter:card:", "name=\"twitter:card\"" in b,
      "| canonical:", '<link rel="canonical"' in b,
      "| meta description:", 'name="description"' in b)

# ── styled bilingual 404 (en by default) ──
try:
    r = urllib.request.urlopen(f"{BASE}/no-such-page")
    print("404 page ok (unexpected):", r.status)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print("404 status:", e.code, "| styled title:", "Page not found" in body,
          "| back link:", "Back to the shore" in body)