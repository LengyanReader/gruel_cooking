import re, sys
sys.stdout.reconfigure(encoding="utf-8")
f = r"C:\DA_Practice\cookbooks\gruel_cooking\Language Stacking-Linguistic Weaving\web\build_learning.py"
s = open(f, encoding="utf-8").read()
parts = s.split("\n\n")
targets = ("spiral_guide_html", "kana_origin_line", "cultural_html", "origin_html",
           "spiral_closure_html", "gojuon_views", "derived_html")
for name in targets:
    i = s.find(f"def {name}(")
    if i < 0:
        print(f"MISSING {name}")
        continue
    j = s.find("\n\n\n", i)
    body = s[i:j if j > 0 else i + 4000]
    classes = re.findall(r'class="([a-zA-Z0-9_\- ]+)"', body)
    all_c = []
    for c in classes:
        all_c += c.split()
    uniq = sorted(set(all_c))
    print(f"== {name} ({len(uniq)} classes) ==")
    print(" ".join(uniq))
