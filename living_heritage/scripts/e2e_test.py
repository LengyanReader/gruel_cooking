import re
import os
import sys
import http.cookiejar
import urllib.request
import urllib.error

sys.path.insert(0, ".")

PORT = os.getenv("LH_PORT", "8000")
BASE_URL = os.getenv("LH_BASE_URL", "").rstrip("/")
BASE = f"http://127.0.0.1:{PORT}"

FAILS = []


def check(label, ok, extra=""):
    print(("PASS " if ok else "FAIL ") + label + ((" [" + str(extra) + "]") if extra else ""))
    if not ok:
        FAILS.append(label)


def get(path):
    with op.open(BASE + path) as r:
        return r.read().decode("utf-8")


def get_en(path):
    with urllib.request.urlopen(BASE + path) as r:
        return r.read().decode("utf-8")


cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

op.open(urllib.request.Request(f"{BASE}/locale/zh", data=b"", method="POST"))
b = get("/")

m = re.search(r'nav-brand[^>]*>\s*<a[^>]*>(.*?)</a>', b, re.S)
print("brand:", m.group(1).strip())

m = re.search(r"hero-title[^>]*>(.*?)<", b)
print("hero:", m.group(1))

m = re.search(r'class="nav-links".*?href="/"[^>]*>(.*?)<', b, re.S)
print("nav.home label:", m.group(1))

check("has zh text", "\u6587\u5316" in b)
check("has new slogan \u5468\u4e88\u6148\u821f", "\u5468\u4e88\u6148\u821f" in b)
check("has footer \u5468\u6e21\u4e07\u6d32", "\u5468\u6e21\u4e07\u6d32" in b)
check("brand nav-sub (zh)", "\u6d3b\u6001\u6587\u5316\u5eca\u9053" in b)
check("brand kicker (zh)",
      "\u5468\u4e88\u6148\u821f\u3001\u5468\u6e21\u4e07\u6d32\u3001\u559d\u7ca5\u6696\u80c3" in b
      or "\u5468\u4e88\u6148\u821f\uff0c\u5468\u6e21\u4e07\u6d32\uff0c\u559d\u7ca5\u6696\u80c3" in b)
check("brand footer identity (zh)", "\u5468\u821f\u6d32\u7ca5 \u00b7 \u6d3b\u6001\u6587\u5316\u5eca\u9053" in b)

raw = get_en("/")
check("en brand kicker", "the bark, the isles, the gruel" in raw)
check("en brand nav-sub", "\u5468\u821f\u6d32\u7ca5" in raw)
check("en footer zhou_line", "the bark, the isles, the gruel" in raw)

mc = get("/css/main.css")
check("css has --gold", "--gold" in mc, ("len", len(mc)))
check("js served", len(get("/js/locale.js")) > 0)

# zh variants across pages — anchors per page: corridor-name string is only
# expected where corridors are actually listed/grouped
for p, anchor in [
    ("/corridors", "\u5317\u4eac\u5927\u8fd0\u6cb3"),  # corridor list includes the grand canal
    ("/scholars", "\u7406\u8bba\u661f\u5ea7"),          # scholars intro block title
    ("/graph", "\u77e5\u8bc6\u56fe\u8c31"),            # graph page marker
    ("/literature", "\u7efc\u8ff0\u5373\u524d\u884c"),  # literature intro title
    ("/methodology", "\u8ba9\u7530\u91ce\u6539\u53d8\u7814\u7a76\u8005"),  # field section title
    ("/fieldwork", "\u5317\u4eac\u5927\u8fd0\u6cb3"),   # fieldwork corridor group header
]:
    body = get(p)
    check(p + " anchor", anchor in body, ("len", len(body)))

pb = get("/publications")
check("publications has \u7814\u7a76\u8d44\u6599\u5e93", "\u7814\u7a76\u8d44\u6599\u5e93" in pb)
check("publications lvl-a chip", "lvl-a" in pb)
check("publications source_level A", "[A]" in pb)
check("publications verified Gillette", "Gillette" in pb)

gb = get("/graph")
check("graph has \u77e5\u8bc6\u56fe\u8c31", "\u77e5\u8bc6\u56fe\u8c31" in gb)
check("graph belongs_to", "belongs_to" in gb)
check("graph studies", "studies" in gb)

lb = get("/literature")
check("literature has \u54c1\u5473", "\u54c1\u5473" in lb)
check("literature has \u54f2\u5b66", "\u54f2\u5b66" in lb)
check("literature has \u4ee3\u8868\u4f5c\u54c1", "\u4ee3\u8868\u4f5c\u54c1" in lb)
check("literature has \u524d\u63d0", "\u524d\u63d0" in lb)
check("literature portrait grid", "portrait-grid" in lb)
check("literature dim-flow", "dim-flow" in lb)

elen = get_en("/literature")
check("en literature ok", "Literature Review" in elen and "taste" in elen and "premises" in elen)

check("pubs filter bar", "filter-pill" in pb)
fc = get("/publications?corridor=grand_canal")
check("pubs corridor=grand_canal keeps \u74f7\u5668\u4e4b\u90fd", "\u74f7\u5668\u4e4b\u90fd" in fc)
check("pubs corridor=grand_canal excludes \u6ce2\u7684\u5c3c\u4e9a\u6e7e", "\u6ce2\u7684\u5c3c\u4e9a\u6e7e" not in fc)
fl = get("/publications?level=A")
check("pubs level=A has \u74f7\u5668\u4e4b\u90fd", "\u74f7\u5668\u4e4b\u90fd" in fl)

check("fieldwork grouped (\u7ec4\u6807\u9898-\u5317\u4eac\u5927\u8fd0\u6cb3)", "\u5317\u4eac\u5927\u8fd0\u6cb3" in get("/fieldwork"))

ld = get("/literature?view=dimensions")
check("literature dimensions tabs", "lit-tab" in ld)
check("dimensions \u6309\u5185\u5bb9\u7ef4\u5ea6\u5bfc\u89c8", "\u6309\u5185\u5bb9\u7ef4\u5ea6\u5bfc\u89c8" in ld)
check("dimensions \u5eca\u9053\u4e0e\u79fb\u52a8", "\u5eca\u9053\u4e0e\u79fb\u52a8" in ld)
check("dimensions \u98df\u7269\u5eca\u9053", "\u98df\u7269\u5eca\u9053" in ld)
check("dimensions \u65b9\u6cd5\u8bba", "\u65b9\u6cd5\u8bba" in ld)

check("graph relations authored", "authored" in gb)
check("graph relations involves", "involves" in gb)
check("graph related literature", "\u76f8\u5173\u6587\u732e" in gb)

# SEO / OG meta
check("seo og:site_name", 'property="og:site_name"' in b)
check("seo og:title", 'property="og:title"' in b)
check("seo twitter:card", 'name="twitter:card"' in b)
check("seo canonical", '<link rel="canonical"' in b)
check("seo meta description", 'name="description"' in b)
check("favicon link", 'rel="icon"' in b)

# og/twitter image behaviour depends on LH_BASE_URL opt-in
if BASE_URL:
    check("og:image absolute (base_url set)", f'content="{BASE_URL}/img/og-cover.jpg"' in b)
    check("twitter:image absolute (base_url set)", f'content="{BASE_URL}/img/og-cover.jpg"' in b)
else:
    check("og:image suppressed w/o base_url", 'property="og:image"' not in b)
    check("twitter:image suppressed w/o base_url", 'name="twitter:image"' not in b)

# static og placeholder asset is always served
with urllib.request.urlopen(BASE + "/img/og-cover.jpg") as r:
    ogbytes = r.read()
check("og-cover.jpg served 200", r.status == 200 and len(ogbytes) > 1000, ("bytes", len(ogbytes)))

# styled bilingual 404 (en by default)
try:
    with urllib.request.urlopen(BASE + "/no-such-page") as r:
        check("404 page ok (unexpected 200)", False, r.status)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    check("404 status", e.code == 404)
    check("404 styled title", "Page not found" in body)
    check("404 back link", "Back to the shore" in body)

print()
if FAILS:
    print("FAILS (%d): %s" % (len(FAILS), "; ".join(FAILS)))
    sys.exit(1)
print("ALL CHECKS PASSED")