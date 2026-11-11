# -*- coding: utf-8 -*-
"""Replace selected dossier fields in books.json from a JSON patch file.

Usage: python _apply_patch.py patch.json
Patch shape: { "<book-id>": { "<field>": <value>, ... }, ... }
Values replace the existing field wholesale. No appends.
"""
import json
import io
import os
import sys

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = os.path.join(BASE, "Reading_IA", "web", "data", "books.json")


def main():
    patch_path = sys.argv[1]
    with io.open(patch_path, encoding="utf-8") as f:
        patch = json.load(f)
    with io.open(P, encoding="utf-8", newline="") as f:
        raw = f.read()
    obj = json.loads(raw)
    byid = {b["id"]: b for b in obj["books"]}
    changed = []
    for bid, fields in patch.items():
        if bid not in byid:
            raise SystemExit("unknown book id: " + bid)
        b = byid[bid]
        for k, v in fields.items():
            if k not in b and k not in ("toc",):
                raise SystemExit("unknown field %s on %s" % (k, bid))
            b[k] = v
        changed.append(bid)
    with io.open(P, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(obj, ensure_ascii=False, indent=2))
        f.write("\n")
    print("patched %d books: %s" % (len(changed), ", ".join(changed)))


if __name__ == "__main__":
    main()
