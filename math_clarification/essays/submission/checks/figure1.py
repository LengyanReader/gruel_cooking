#!/usr/bin/env python3
"""Re-render the WITHDRAWN Figure 1 from the frozen pilot coding.

This figure is no longer part of the manuscript. The Nature Review presents no
figure and no tally. This script is retained so the archive stays reproducible
and so the old picture can be regenerated for comparison with the new argument.

The data is read from ../figure1_data.csv, a verbatim transcription of the
pre-Review draft's CSV block. It is deliberately *not* corrected in place; see
../figure1_data_NOTES.md for the three defects that got it withdrawn:

  1. row 4 files 75.7% under FrontierMath. o3's FrontierMath score is 25.2%;
     75.7% is o3's ARC-AGI result. The tick label below is corrected because it
     is typed here, but the CSV keeps the historical error.
  2. the `na` regime is folded into the community denominator, which silently
     turns row 11's attribution quarrel into community-graded evidence.
  3. the Fisher exact P ~= 0.24 does not license a frequency claim from eleven
     events selected through publicity. The caption therefore reports no test.

The data layer is stdlib-only and always runs. Rendering needs matplotlib and is
skipped with instructions when it is absent.

Run:  python checks/figure1.py [--report-only]
Out:  ../figure1.png  and  ../figure1.pdf   (archive, not for submission)

AI-drafted, unreviewed. Withdrawn from the manuscript.
"""

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "figure1_data.csv"
OUT_PNG = HERE.parent / "figure1.png"
OUT_PDF = HERE.parent / "figure1.pdf"

# regime -> staircase level (x order is handled by sorting)
LEVEL = {"MG": 0, "HG": 1, "CG": 2, "na": 2}
TIER_LABEL = {0: "machine-graded", 1: "hybrid-graded", 2: "community-graded"}

# House style keeps dashes out, so event names are tagged compactly. These labels
# are typed here, not derived from the data, so the row-4 label is corrected:
# 25.2% is the FrontierMath score.
TAG = {
    1: "IMO'24\nG&M + Lean",
    2: "IMO'25\ncoordinators",
    3: "IMO'25\nself-selected",
    4: "o3 / FrontierMath\n25.2% full set",
    5: "FrontierMath v2\nbuilder fixes",
    6: "Unit-distance\n9 verifiers",
    7: "Harvard\nFirst Proof",
    8: "AlphaEvolve\n48 mults",
    9: "Erdos bench\n68 in Lean",
    10: "Navier-Stokes\nadmissibility",
    11: "Attribution\ndispute",
}

Q_COLS = [
    "q1_framing",
    "q2_reproducible",
    "q3_independent",
    "q4_symmetric_disclosure",
    "q5_found_or_made",
]
Q_ROWS = ["Q1 framing", "Q2 reproducible", "Q3 independent", "Q4 disclosure", "Q5 found/made"]
MARK_COLOR = {"+": "#2e7d32", "\u00b1": "#e0a800", "\u2212": "#c62828", "na": "#cfcfcf"}


def load_events():
    """Read the frozen coding table with the standard library only."""
    if not DATA.exists():
        sys.exit(f"ERROR: {DATA} not found (the archive data was deleted)")
    with DATA.open(newline="", encoding="utf-8") as fh:
        rows = [dict(r) for r in csv.DictReader(fh)]
    if not rows:
        sys.exit(f"ERROR: {DATA} has no rows")
    for r in rows:
        r["id"] = int(r["id"])
        r["dispute"] = int(r["dispute"])
        r["regime"] = (r["regime"] or "").strip()
    rows.sort(key=lambda r: r["id"])
    # sort by staircase level, then id, for the left-to-right rise
    rows.sort(key=lambda r: (LEVEL[r["regime"]], r["id"]))
    return rows


def report_history(rows):
    """Print the old arithmetic as history, with the defects named. Asserts nothing."""
    def count(pred):
        sel = [r for r in rows if pred(r)]
        return sum(r["dispute"] for r in sel), len(sel)

    print("ARCHIVE ONLY. The following numbers are NOT claims of the Review:")
    print("  machine-or-hybrid graded : %d/%d rows flagged as disputed"
          % count(lambda r: r["regime"] in ("MG", "HG")))
    print("  community graded          : %d/%d" % count(lambda r: r["regime"] == "CG"))
    print("  not applicable            : %d/%d   <- the old tally folded this row "
          "into the community denominator" % count(lambda r: r["regime"] == "na"))
    print("  the withdrawn headline was '1/6 vs 3/5'; the honest split is 1/6, 1/4 and 1/1")
    print("  no significance test is reported: n = 11, selected through publicity")


def draw(rows):
    try:
        import matplotlib
        matplotlib.use("Agg")  # headless: no display needed to write PNG/PDF
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle
        from matplotlib.lines import Line2D
    except ImportError:
        print("SKIP: rendering needs matplotlib (`pip install matplotlib`).")
        print("      The archive data check above ran regardless and needs no dependency.")
        return False

    n = len(rows)
    fig = plt.figure(figsize=(9.4, 6.4), dpi=150)
    gs = fig.add_gridspec(2, 1, height_ratios=[3, 1.7], hspace=0.32)

    # ---- top: the regime staircase ----------------------------------------
    ax = fig.add_subplot(gs[0])
    for lvl in (0, 1, 2):
        idx = [i for i, r in enumerate(rows) if LEVEL[r["regime"]] == lvl]
        if not idx:
            continue
        x0, x1 = min(idx) - 0.5, max(idx) + 0.5
        ax.add_patch(Rectangle((x0, lvl - 0.42), x1 - x0, 0.84,
                               color=["#eef3fb", "#eaf4ee", "#f7f0e6"][lvl], zorder=0))
        ax.text((x0 + x1) / 2, lvl + 0.5, TIER_LABEL[lvl],
                ha="center", va="bottom", fontsize=9, style="italic", color="#444")

    for i, r in enumerate(rows):
        disputed = r["dispute"] == 1
        ax.plot(i, LEVEL[r["regime"]], marker="o", markersize=13,
                markerfacecolor="#c62828" if disputed else "white",
                markeredgecolor="#c62828" if disputed else "#555",
                markeredgewidth=1.6, zorder=3)

    ax.set_xlim(-0.6, n - 0.4)
    ax.set_ylim(-0.7, 2.9)
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels([])
    ax.set_xticks(list(range(n)))
    ax.set_xticklabels([TAG[r["id"]] for r in rows], fontsize=6.6, rotation=45, ha="right")
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.set_ylabel("certification regime", fontsize=9)
    ax.set_title("WITHDRAWN pilot coding (n = 11): recorded disputes by grading regime",
                 fontsize=10.5, pad=26, weight="bold", color="#b71c1c")
    ax.text(0.5, 1.045, "not part of the Nature Review; see figure1_data_NOTES.md",
            transform=ax.transAxes, ha="center", fontsize=8, style="italic", color="#b71c1c")

    ax.legend(handles=[
        Line2D([], [], marker="o", color="w", markerfacecolor="#c62828",
               markeredgecolor="#c62828", markersize=11, label="public dispute recorded"),
        Line2D([], [], marker="o", color="w", markerfacecolor="white",
               markeredgecolor="#555", markersize=11, label="no public dispute"),
    ], loc="upper left", fontsize=8, frameon=False)

    # ---- bottom: verification-question heat-strip -------------------------
    ax2 = fig.add_subplot(gs[1], sharex=ax)
    for xi, r in enumerate(rows):
        for yi, col in enumerate(Q_COLS):
            mark = (r[col] or "").strip()
            ax2.add_patch(Rectangle((xi - 0.5, yi - 0.5), 1, 1,
                                    color=MARK_COLOR.get(mark, "#ffffff"), zorder=1))
            ax2.text(xi, yi, mark, ha="center", va="center", fontsize=8,
                     color="white" if mark in ("+", "\u2212") else "#333", zorder=2)
    ax2.set_ylim(-0.5, len(Q_COLS) - 0.5)
    ax2.set_yticks(range(len(Q_COLS)))
    ax2.set_yticklabels(Q_ROWS, fontsize=7)
    ax2.invert_yaxis()
    ax2.set_ylabel("verification\nquestions", fontsize=8)
    ax2.tick_params(axis="x", labelbottom=False)
    for spine in ax2.spines.values():
        spine.set_visible(False)
    for lvl in (0, 1, 2):
        idx = [i for i, r in enumerate(rows) if LEVEL[r["regime"]] == lvl]
        if idx:
            ax2.axvline(min(idx) - 0.5, color="#bbb", lw=0.8)
    ax2.axvline(n - 0.5, color="#bbb", lw=0.8)

    fig.text(0.5, 0.015,
             "Archive render of figure1_data.csv. Defects: 75.7% misfiled under FrontierMath "
             "(o3 scored 25.2% there; 75.7% is ARC-AGI); the na row is folded into the "
             "community denominator; cases were selected through publicity, so no rate or "
             "significance test is reported.",
             ha="center", fontsize=6.4, color="#555", wrap=True)

    fig.savefig(OUT_PNG, bbox_inches="tight")
    fig.savefig(OUT_PDF, bbox_inches="tight")
    print(f"wrote {OUT_PNG}")
    print(f"wrote {OUT_PDF}")
    return True


if __name__ == "__main__":
    events = load_events()
    report_history(events)
    if "--report-only" not in sys.argv:
        draw(events)
    print("ARCHIVE CHECK COMPLETE (withdrawn from the manuscript; no claims asserted)")
