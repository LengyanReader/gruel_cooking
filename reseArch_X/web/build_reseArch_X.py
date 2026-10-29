"""Build the reseArch_X dashboard page.

Reads the module's Markdown sources of truth —
  reseArch_X/scholars/*.md
  reseArch_X/opportunities/*/*.md
  reseArch_X/mvp/MVP-*.md
  reseArch_X/indexes/dialogue_map.md
  reseArch_X/scan_log/*.md
— extracts each yaml-in-fence record with a small hand-rolled parser
(the schema uses bare `?` markers and unquoted `: ` inside list items,
both of which trip standard YAML), then renders `docs/reseArch_X/index.html`
from `template.html` with a JSON payload injected in-place.

Run:
    python -X utf8 reseArch_X/web/build_reseArch_X.py

Determinism: no clock is embedded. Every date in the output is either an
`asof` stamped in a source file or derived from a scan_log filename.
"""

from __future__ import annotations
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent                 # reseArch_X/
REPO = BASE.parent                 # gruel_cooking/
OUT = REPO / "docs" / "reseArch_X" / "index.html"
TEMPLATE = HERE / "template.html"

# ----------------------------------------------------------- yaml mini-parse --
# A line-based parser tuned to reseArch_X's schema. Handles:
#   key: scalar            (with optional trailing "# comment")
#   key:                   followed by "  - item" block sequence
#   key: {a: 1, b: ?, c: 3} flow mapping (bare "?" and unquoted scalars OK)
#   - {mark: ✔, asof: ...} sequence of flow mappings
# Anything more complex is out of scope — if a source needs it, fix the source.

FENCE = re.compile(r"```yaml\s*\n(.*?)\n```", re.DOTALL)
TOP_KEY = re.compile(r"^([A-Za-z_][\w]*):\s*(.*)$")
SEQ_ITEM = re.compile(r"^\s+-\s+(.*)$")


def strip_inline_comment(s: str) -> str:
    """Remove a trailing `# ...` comment when preceded by whitespace.
    Keeps `#` inside a URL fragment (which is not preceded by whitespace)."""
    return re.sub(r"\s+#.*$", "", s).rstrip()


def split_flow(s: str) -> list[str]:
    """Split a flow-mapping body by top-level commas."""
    parts, buf, depth = [], "", 0
    for ch in s:
        if ch in "{[":
            depth += 1
        elif ch in "}]":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(buf)
            buf = ""
        else:
            buf += ch
    if buf.strip():
        parts.append(buf)
    return [p.strip() for p in parts if p.strip() != ""]


def parse_scalar(s: str):
    s = s.strip()
    if s in ("?", "''", '""'):
        return s.strip("'\"")
    if s.startswith("{") and s.endswith("}"):
        return parse_flow_map(s)
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        return [parse_scalar(p) for p in split_flow(inner)] if inner else []
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    return s


def parse_flow_map(s: str) -> dict:
    assert s.startswith("{") and s.endswith("}")
    inner = s[1:-1].strip()
    out: dict = {}
    if not inner:
        return out
    for part in split_flow(inner):
        if ":" in part:
            k, v = part.split(":", 1)
            out[k.strip()] = parse_scalar(v.strip())
    return out


def parse_yaml_block(text: str) -> dict:
    """Parse the reseArch_X yaml-in-fence body into a dict."""
    result: dict = {}
    lines = text.split("\n")
    i = 0
    n = len(lines)
    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        m = TOP_KEY.match(line)
        if not m or raw.startswith(" "):
            # skip any stray line we can't interpret
            i += 1
            continue
        key, rest = m.group(1), strip_inline_comment(m.group(2))
        if rest == "":
            # block sequence (or empty string)
            items = []
            j = i + 1
            while j < n:
                nxt = lines[j]
                if not nxt.strip():
                    j += 1
                    continue
                sm = SEQ_ITEM.match(nxt)
                if sm:
                    items.append(parse_scalar(sm.group(1)))
                    j += 1
                else:
                    break
            result[key] = items if items else ""
            i = j
        else:
            result[key] = parse_scalar(rest)
            i += 1
    return result


# --------------------------------------------------------------- file loaders --


def load_records(dir_path: Path) -> list[dict]:
    out = []
    if not dir_path.exists():
        return out
    for p in sorted(dir_path.glob("*.md")):
        if p.name.startswith("_") or p.name == "README.md":
            continue
        text = p.read_text(encoding="utf-8")
        m = FENCE.search(text)
        if not m:
            continue
        try:
            rec = parse_yaml_block(m.group(1))
        except Exception as e:  # pragma: no cover — debugging aid
            print(f"[warn] parse fail {p.name}: {e}")
            continue
        rec["_slug"] = p.stem
        rec["_file"] = p.relative_to(REPO).as_posix()
        # capture 正文 tail (markdown under "## 正文")
        body = text[m.end():]
        body = re.sub(r"^\s*##\s*正文\s*", "", body)
        rec["_body"] = body.strip()
        out.append(rec)
    return out


def load_opportunities() -> list[dict]:
    out = []
    root = BASE / "opportunities"
    for sub in ("phd", "ra", "postdoc", "professor"):
        out.extend(load_records(root / sub))
    return out


def load_dialogue_map() -> dict:
    """Return {'rows': [...], 'sort_logic': '...'} parsed from dialogue_map.md."""
    p = BASE / "indexes" / "dialogue_map.md"
    if not p.exists():
        return {"rows": [], "sort_logic": ""}
    text = p.read_text(encoding="utf-8")
    rows = []
    for line in text.split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or cells[0] in ("人 / 节点", "") or set(cells[0]) <= set("-: "):
            continue
        rows.append({
            "who": cells[0].replace("**", "").strip(),
            "file": cells[1].strip("`"),
            "work": cells[2],
            "mvp": cells[3],
            "hook": cells[4],
            "status": cells[5],
        })
    sort_m = re.search(r"##\s*排序逻辑.*", text, re.DOTALL)
    sort_logic = sort_m.group(0).strip() if sort_m else ""
    return {"rows": rows, "sort_logic": sort_logic}


def load_mvp_roster() -> list[dict]:
    """Parse the MVP roster table from mvp/README.md, and merge per-MVP files."""
    p = BASE / "mvp" / "README.md"
    rows = []
    if p.exists():
        for line in p.read_text(encoding="utf-8").split("\n"):
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4 or cells[0] in ("编号", "") or set(cells[0]) <= set("-: "):
                continue
            rows.append({
                "id": cells[0],
                "target": cells[1],
                "summary": cells[2],
                "status": cells[3],
            })
    # enrich with any per-MVP files present
    for f in sorted((BASE / "mvp").glob("MVP-*.md")):
        m = FENCE.search(f.read_text(encoding="utf-8"))
        if not m:
            continue
        rec = parse_yaml_block(m.group(1))
        rid = rec.get("id") or f.stem.split("-").pop(0)
        for r in rows:
            if r["id"].startswith(rid) or rid in r["id"]:
                r["file"] = f.relative_to(REPO).as_posix()
                if rec.get("status"):
                    r["status"] = rec["status"]
    return rows


def load_scan_logs() -> list[dict]:
    out = []
    d = BASE / "scan_log"
    for p in sorted(d.glob("*.md")):
        if p.name == "README.md":
            continue
        m = re.match(r"(\d{8})-(v[\w.]+)-([\w-]+)", p.stem)
        if not m:
            continue
        date, wave, slug = m.groups()
        iso = f"{date[:4]}-{date[4:6]}-{date[6:]}"
        text = p.read_text(encoding="utf-8")
        title_m = re.match(r"#\s*(.+)", text)
        title = title_m.group(1).strip() if title_m else p.stem
        # pull first "触发" paragraph as summary
        trig_m = re.search(r"\*\*触发\*\*：(.+?)(?=\n\n|\n\*\*)", text, re.DOTALL)
        summary = trig_m.group(1).replace("\n", " ").strip()[:220] if trig_m else ""
        out.append({"date": iso, "wave": wave, "slug": slug,
                    "title": title, "summary": summary,
                    "file": p.relative_to(REPO).as_posix()})
    return sorted(out, key=lambda r: r["date"], reverse=True)


# ----------------------------------------------------------------- axis map --
# The nine user-declared axes. Kept here (not in source .md) because tags are
# curation judgments, not authored facts. Re-run build after editing.

AXES = [
    ("AI 与数据科学",       "ai_ds",     "AI/ML 方法本身 · 数据基础设施 · 计算社科"),
    ("AI × 人文交叉",        "ai_hum",    "LLM 时代人文批评 · 媒介理论 · 数字民主"),
    ("可持续发展",           "sus",       "人类世 ·  pluriverse · 韧性 · 跨文明经济"),
    ("数字人文",             "dh",        "批评性 DH · 远读 · Graphesis · 数据可视化"),
    ("文化遗产",             "herit",     "活态遗产 · 遗产 AI 可见性 · 走廊与场"),
    ("美食",                 "food",      "食物人类学 · 慢食 · 烹饪文化"),
    ("旅游",                 "tour",      "流动 · 廊道旅游 · Heritage × Tourism"),
    ("人生修行",             "cultiv",    "沉思科学 · 冥想训练实证 · 社会情绪神经"),
    ("良好生活",             "goodlife",  "幸福可训练性 · 共同生活 · 生活设计"),
]

SCHOLAR_AXES = {
    "manovich-lev":       ["dh", "ai_hum", "ai_ds"],
    "sheller-mimi":       ["ai_hum", "sus", "herit", "tour"],
    "behrendt-frauke":    ["ai_hum", "sus", "ai_ds", "tour"],
    "oberbichler-sarah":  ["dh", "herit", "ai_hum"],
    "davidson-richard":   ["cultiv", "goodlife", "ai_ds"],
    "moretti-franco":     ["dh", "ai_hum"],
    "salganik-matthew":   ["ai_ds", "ai_hum"],
    "norstrom-asa":       ["sus"],
    "chun-wendy":         ["ai_hum", "ai_ds", "sus", "dh"],
    "tsing-anna":         ["sus", "herit", "cultiv", "goodlife", "food", "tour"],
    "escobar-arturo":     ["sus", "herit", "ai_hum"],
    "singer-tania":       ["cultiv", "goodlife"],
    "drucker-johanna":    ["dh", "herit"],
    "dignum-virginia":    ["ai_ds", "ai_hum"],
}

OPP_AXES = {
    "RX-phd-cambridge-cdh-202610":  ["dh", "ai_hum", "herit"],
    "RX-phd-oxford-oii-202610":     ["ai_ds", "ai_hum"],
    "RX-phd-ucl-sas-202610":        ["dh", "herit", "ai_hum"],
    "RX-phd-ucd-ai-heritage-202610":["herit", "ai_hum", "tour"],
    "RX-phd-stockholm-resilience-202610": ["sus"],
    "RX-phd-unisg-gastronomy-202610":      ["food", "sus", "tour"],
    "RX-phd-msca-heritour-202610":         ["herit", "tour", "dh"],
    "RX-phd-nyu-cds-202610":               ["ai_ds", "ai_hum"],
    "RX-phd-esrc-sw-dtc-202610":           ["dh", "herit", "ai_ds"],
}


# ---------------------------------------------------------------- assemble --


def build_dataset() -> dict:
    scholars = load_records(BASE / "scholars")
    opportunities = load_opportunities()
    dialogue = load_dialogue_map()
    mvp = load_mvp_roster()
    scans = load_scan_logs()

    # attach axes
    for s in scholars:
        s["axes"] = SCHOLAR_AXES.get(s["_slug"], [])
    for o in opportunities:
        o["axes"] = OPP_AXES.get(o["id"], OPP_AXES.get(o["_slug"], []))

    # derive latest asof seen across scholars
    asof_dates = []
    for s in scholars:
        for st in (s.get("stamps") or []):
            if isinstance(st, dict) and st.get("asof"):
                asof_dates.append(str(st["asof"]))
    latest_asof = max(asof_dates) if asof_dates else ""

    # axis coverage summary (count of scholars+opps per axis)
    axis_cov = []
    for zh, key, desc in AXES:
        n_sch = sum(1 for s in scholars if key in s.get("axes", []))
        n_opp = sum(1 for o in opportunities if key in o.get("axes", []))
        axis_cov.append({"zh": zh, "key": key, "desc": desc,
                         "scholars": n_sch, "opportunities": n_opp})

    # counts
    counts = {
        "scholars": len(scholars),
        "卓越开明": sum(1 for s in scholars if s.get("tier") == "卓越开明"),
        "有潜力": sum(1 for s in scholars if s.get("tier") == "有潜力"),
        "opportunities": len(opportunities),
        "mvp_total": len(mvp),
        "mvp_built": sum(1 for m in mvp if str(m.get("status", "")).lower() == "built"),
        "scans": len(scans),
        "dialogue_rows": len(dialogue["rows"]),
    }

    return {
        "latest_asof": latest_asof,
        "counts": counts,
        "axes_meta": [{"zh": zh, "key": k, "desc": d} for zh, k, d in AXES],
        "axis_coverage": axis_cov,
        "scholars": scholars,
        "opportunities": opportunities,
        "dialogue_map": dialogue,
        "mvp": mvp,
        "scan_logs": scans,
    }


# ------------------------------------------------------------------- render --


def render(data: dict) -> str:
    tpl = TEMPLATE.read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False)
    # escape "</script>" inside JSON strings for safety
    payload = payload.replace("</", "<\\/")
    if "__DATA_JSON__" not in tpl:
        raise RuntimeError("template.html missing __DATA_JSON__ placeholder")
    html = tpl.replace("__DATA_JSON__", payload)
    return html


def main():
    data = build_dataset()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    html = render(data)
    OUT.write_text(html, encoding="utf-8", newline="\n")
    print(f"[ok] wrote {OUT.relative_to(REPO).as_posix()} "
          f"({len(html):,} chars) · "
          f"scholars={data['counts']['scholars']} · "
          f"opportunities={data['counts']['opportunities']} · "
          f"scans={data['counts']['scans']}")


if __name__ == "__main__":
    main()
