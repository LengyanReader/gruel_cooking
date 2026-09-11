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