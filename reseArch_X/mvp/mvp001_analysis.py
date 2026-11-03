#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MVP-001 v0 · Manovich「AI-as-culture / 媒体积累」在跨文明发现源语料上的压测.

数据仪器（M3.10 声明）:
  主张 = 「本仓发现源登记层中, 机器不可见性(bot-gating)的分布随语言圈而异」
  仪器 = 对版本化 SSOT(discovery_atlas/sources/*.json, 237 条)的**精确穷举计算**,
         结果完全由脚本重算可复现; 描述统计, 不做抽样推断(登记层 ≠ 随机样本,
         选择过程 = 建档者的注意力, 见 notebook 诚实边界)。
输入(全为本仓真实数据, 无外采):
  discovery_atlas/sources/{books,art,music,film,science}.json   # 标本 A: 机器面向的发现源登记层
  Reading_IA/readings/{library,authors,relations}/               # 标本 B: 手工深耕层(仅计数, 作对照语境)
输出:
  mvp001_data.json   # 全部计算表 + 溯源(输入文件/生成时间/分组定义)
  mvp001_fig1.svg    # 主图: (A) domain×layer 矩阵  (B) 各语言圈 bot-gated% 与 qid%
运行: python -I reseArch_X/mvp/mvp001_analysis.py   (仓库根; 纯标准库)
"""
import json
import glob
import collections
import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent          # reseArch_X/mvp/
REPO = HERE.parents[1]                          # gruel_cooking/
SRC = REPO / "discovery_atlas" / "sources"
LIB = REPO / "Reading_IA" / "readings"

# ---- 分组定义(分析性切分, v0; notebook 中披露) --------------------------------
# WEST_LANG: 全球性平台(global; 50 条中 33 条 langs 含 en、余多为 MULTI, 见 data JSON 的
# global_langs_note)+ 欧洲语言圈。he(2 条)不计入西组(文明归属有争议, 如实归入其他组)。
WEST_LANG = {"en", "global", "fr", "de", "it", "es", "nl", "pl"}
MIN_N = 3  # 单圈样本低于此值不进 per-circle 图表(表格仍给全量)

LAYERS = ["discovery", "criticism", "publishing", "infrastructure", "access"]
DOMAINS = ["books", "art", "music", "film", "science"]


def load_specimen_a():
    rows = []
    for f in sorted(SRC.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for s in d.get("sources", []):
            rows.append({
                "id": s.get("id", ""),
                "name": s.get("name", ""),
                "domain": s.get("domain", f.stem),
                "layer": s.get("layer", ""),
                "circle": s.get("circle", ""),
                "status": s.get("status", ""),
                "langs": s.get("langs", []),
                "qid": bool(s.get("wikidata_qid")),
                "src_file": f.name,
            })
    return rows


def main():
    a = load_specimen_a()
    n = len(a)

    # -- 标本 B: 手工深耕层计数(仅规模对照, 不做深算) -------------------------
    b = {
        "library_cards": len([p for p in (LIB / "library").glob("*.md")
                              if p.name not in ("README.md", "_template.md")]),
        "authors": len([p for p in (LIB / "authors").glob("*.md")
                        if p.name not in ("README.md", "_template.md")]),
        "relations_files": len([p for p in (LIB / "relations").glob("*.md")
                                if p.name != "README.md"]),
    }

    # -- 基础分布 -------------------------------------------------------------
    by_domain = collections.Counter(r["domain"] for r in a)
    by_layer = collections.Counter(r["layer"] for r in a)
    by_circle = collections.Counter(r["circle"] for r in a)
    by_status = collections.Counter(r["status"] for r in a)

    dom_layer = {d0: {l: sum(1 for r in a if r["domain"] == d0 and r["layer"] == l)
                      for l in LAYERS} for d0 in DOMAINS}

    global_langs = collections.Counter(
        "en_listed" if ("en" in (r["langs"] or [])) else
        ("multi" if any(str(x).lower() == "multi" for x in (r["langs"] or [])) else
         ("other" if r["langs"] else "empty"))
        for r in a if r["circle"] == "global")

    # -- 可见性探针: 两组对比 + 单圈明细 --------------------------------------
    def probe(sub):
        k = len(sub)
        return {
            "n": k,
            "share": round(k / n, 4),
            "bot_gated": sum(1 for r in sub if r["status"] == "bot-gated"),
            "active": sum(1 for r in sub if r["status"] == "active"),
            "qid": sum(1 for r in sub if r["qid"]),
        }

    west = [r for r in a if r["circle"] in WEST_LANG]
    other = [r for r in a if r["circle"] not in WEST_LANG]

    def rate(p, key):
        return round(p[key] / p["n"], 4) if p["n"] else None

    west_p, other_p = probe(west), probe(other)
    group_contrast = {
        "group_def": {
            "west_lang": sorted(WEST_LANG),
            "other": "其余全部语言圈(含 he 2 条——文明归属有争议, 如实归入其他组)",
            "note": "分析性切分(v0), 非语料自带; global 圈的语言构成见 global_langs_note",
        },
        "west_lang": {**west_p, "bot_gated_rate": rate(west_p, "bot_gated"),
                      "qid_rate": rate(west_p, "qid"),
                      "active_rate": rate(west_p, "active")},
        "other": {**other_p, "bot_gated_rate": rate(other_p, "bot_gated"),
                  "qid_rate": rate(other_p, "qid"),
                  "active_rate": rate(other_p, "active")},
    }

    per_circle = {}
    for c0, k in by_circle.most_common():
        sub = [r for r in a if r["circle"] == c0]
        p = probe(sub)
        per_circle[c0] = {**p, "bot_gated_rate": rate(p, "bot_gated"),
                          "qid_rate": rate(p, "qid"),
                          "active_rate": rate(p, "active"),
                          "in_fig": k >= MIN_N}

    # -- 落盘 -----------------------------------------------------------------
    data = {
        "generated_at": datetime.date.today().isoformat(),
        "script": "reseArch_X/mvp/mvp001_analysis.py",
        "instrument": "exact enumeration over versioned SSOT; descriptive only (no sampling inference)",
        "inputs": {"specimen_a": sorted(p.name for p in SRC.glob("*.json")),
                   "specimen_b_counts": b},
        "totals": {"n_sources": n, "by_domain": dict(by_domain),
                   "by_layer": dict(by_layer), "by_status": dict(by_status),
                   "by_circle": dict(by_circle)},
        "domain_x_layer": dom_layer,
        "global_langs_note": dict(global_langs),
        "group_contrast": group_contrast,
        "per_circle": per_circle,
        "fig_min_n": MIN_N,
    }
    (HERE / "mvp001_data.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    write_svg(data)
    print("OK n=%d -> mvp001_data.json, mvp001_fig1.svg" % n)
    print("west  : n=%(n)d bot_gated_rate=%(bot_gated_rate)s qid_rate=%(qid_rate)s" % group_contrast["west_lang"])
    print("other : n=%(n)d bot_gated_rate=%(bot_gated_rate)s qid_rate=%(qid_rate)s" % group_contrast["other"])


# ---- SVG 主图(代码声明、可 diff; M4.15: 图注随图走) ---------------------------
INK, SOFT, FAINT = "#1a1a1a", "#555", "#d8d4cc"


def write_svg(d):
    W, H = 980, 560
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, PingFang SC, Microsoft YaHei, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="#faf8f4"/>',
         f'<text x="24" y="34" font-size="19" font-weight="bold" fill="{INK}">MVP-001 · 对机器可见性探针 / Machine-visibility probes</text>',
         f'<text x="24" y="54" font-size="12" fill="{SOFT}">discovery_atlas 登记层 n={d["totals"]["n_sources"]}（2026-11 精确穷举; bot-gated=对爬虫关闭, qid=已解析进 Wikidata 机器层）</text>']

    # (A) domain × layer 矩阵
    o.append(f'<text x="24" y="88" font-size="14" font-weight="bold" fill="{INK}">A · 域 × 层（条目数）</text>')
    x0, y0, cw, ch = 90, 100, 108, 40
    mx = max(v for row in d["domain_x_layer"].values() for v in row.values()) or 1
    o.append(f'<text x="{x0 - 8}" y="{y0 + 26}" font-size="11" fill="{SOFT}" text-anchor="end">域＼层</text>')
    for j, l in enumerate(LAYERS):
        o.append(f'<text x="{x0 + j * cw + cw / 2}" y="{y0 + 14}" font-size="11" fill="{SOFT}" text-anchor="middle">{l}</text>')
    for i, d0 in enumerate(DOMAINS):
        yy = y0 + 24 + i * ch
        o.append(f'<text x="{x0 - 8}" y="{yy + 24}" font-size="12" fill="{INK}" text-anchor="end">{d0}</text>')
        for j, l in enumerate(LAYERS):
            v = d["domain_x_layer"][d0][l]
            t = (v / mx) * 0.82
            o.append(f'<rect x="{x0 + j * cw + 2}" y="{yy + 2}" width="{cw - 4}" height="{ch - 4}" rx="3" fill="#3d5a80" fill-opacity="{t:.2f}"/>')
            if v:
                o.append(f'<text x="{x0 + j * cw + cw / 2}" y="{yy + 26}" font-size="12" fill="{INK if t < 0.55 else "#fff"}" text-anchor="middle">{v}</text>')

    # (B) per-circle bot-gated% (n>=MIN_N)
    o.append(f'<text x="560" y="88" font-size="14" font-weight="bold" fill="{INK}">B · bot-gated%（按语言圈, n≥{d["fig_min_n"]}）</text>')
    rows_fig = sorted((v for v in d["per_circle"].values() if v["in_fig"]),
                      key=lambda v: -(v["bot_gated_rate"] or 0))
    bx, by, bw, bh, gap = 700, 102, 190, 21, 5.5
    o.append(f'<line x1="{bx}" y1="{by - 4}" x2="{bx}" y2="{by + len(rows_fig) * (bh + gap)}" stroke="{FAINT}"/>')
    for i, v in enumerate(rows_fig):
        yy = by + i * (bh + gap)
        w = (v["bot_gated_rate"] or 0) * bw
        circle = next(k for k, p in d["per_circle"].items() if p is v)
        o.append(f'<text x="{bx - 8}" y="{yy + 15}" font-size="12" fill="{INK}" text-anchor="end">{circle}</text>')
        o.append(f'<rect x="{bx}" y="{yy}" width="{w:.1f}" height="{bh - 6}" rx="2" fill="#a4443b"/>')
        o.append(f'<text x="{bx + w + 6:.1f}" y="{yy + 15}" font-size="11" fill="{SOFT}">{v["bot_gated_rate"]:.0%}（{v["bot_gated"]}/{v["n"]}）</text>')

    gy = by + len(rows_fig) * (bh + gap) + 24
    wp, op_ = d["group_contrast"]["west_lang"], d["group_contrast"]["other"]
    o.append(f'<text x="560" y="{gy}" font-size="12" fill="{INK}" font-weight="bold">两组对照（分析性切分, 定义见 data JSON）</text>')
    o.append(f'<text x="560" y="{gy + 20}" font-size="12" fill="{SOFT}">西组 west_lang: n={wp["n"]}, bot-gated {wp["bot_gated_rate"]:.1%}, qid {wp["qid_rate"]:.1%}</text>')
    o.append(f'<text x="560" y="{gy + 38}" font-size="12" fill="{SOFT}">其他组 other: n={op_["n"]}, bot-gated {op_["bot_gated_rate"]:.1%}, qid {op_["qid_rate"]:.1%}</text>')
    o.append(f'<text x="24" y="{H - 18}" font-size="11" fill="{SOFT}">图注: 登记 = 建档者手工所收发现源（选择性层, 非世界分布）; 读法与边界见 reseArch_X/mvp/MVP-001-notebook.md</text>')
    o.append("</svg>")
    (HERE / "mvp001_fig1.svg").write_text("\n".join(o) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
