import re
import sys

f = r"C:\DA_Practice\cookbooks\gruel_cooking\Language Stacking-Linguistic Weaving\web\build_learning.py"
s = open(f, encoding="utf-8").read()
names = ["spiral_guide_html", "cultural_html", "origin_html",
         "spiral_closure_html", "gojuon_views"]
for n in names:
    i = s.find("def " + n + "(")
    if i < 0:
        print(f"[MISS] {n}")
        continue
    j = s.find("\ndef ", i + 5)
    body = s[i : j if j > 0 else i + 5000]
    classes = sorted({c for m in re.findall(r'class="([^"]+)"', body) for c in m.split()})
    print(f"## {n}  ->  {' '.join(classes)}")
