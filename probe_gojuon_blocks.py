import sys, io, json, os

_sys = sys
out = r"C:\DA_Practice\cookbooks\gruel_cooking\probe_blocks_gojuon.json"
try:
    # import module_data_blocks 所在的模块
    sys.path.insert(0, r"C:\DA_Practice\cookbooks\gruel_cooking\Language Stacking-Linguistic Weaving\web")
    import build_learning as bl

    blocks = bl.module_data_blocks("ja", {"id": "gojuon", "status": "ready"})

    def summarize(b):
        # 取前 90 字符 + 存在的 spiral/ring id + class 标记
        head = b[:90]
        markers = {}
        for m in ["spiral-guide", "ring-shape", "ring-word", "ring-sense", "ring-root",
                  "kana-table", "gloss-table", "gloss-wrap", "culture", "cultural",
                  "origin", "spiral-closure", "spiral-guide", "closure"]:
            markers[m] = m in b
        return {"type": "str", "len": len(b), "head": head, "markers": markers}

    result = {"len_blocks": len(blocks), "all_str": all(isinstance(b, str) for b in blocks),
              "blocks": [summarize(b) for b in blocks]}
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print("PROBE_OK")
except Exception as e:
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump({"err": repr(e)}, f, ensure_ascii=False, indent=1)
    print("PROBE_ERR")
