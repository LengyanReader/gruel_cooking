#!/usr/bin/env python3
"""Render Figure 1 of the Comment draft from its own §B dataset.

Design intent (harness MC-W2 / R-D): the figure is *derived*, not hand-typed.
The eleven coded events and the five verification-question marks are parsed
straight out of the ```csv block in ../comment_draft.md, so the picture cannot
drift from the specification it illustrates. The script then re-computes the two
headline tallies quoted in the body (1/6 machine-or-hybrid vs 3/5 community) from
that same data and asserts them; it adds no facts and changes none.

Run:  python checks/figure1.py     (from the submission/ folder, or anywhere)
Out:  ../figure1.png  and  ../figure1.pdf   (vector PDF for print submission)

AI-drafted, unreviewed (harness §I.6). A rendering of the parent paper's own
coding, for pitching only; the numbers remain the parent's, selected through
publicity, descriptive only (Fisher exact P ~= 0.24 on a table this small).
"""

import io
import re
import sys
from pathlib import Path

import pandas as pd
import matplotlib

matplotlib.use("Agg")  # headless: no display needed to write PNG/PDF
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
DRAFT = HERE.parent / "comment_draft.md"
OUT_PNG = HERE.parent / "figure1.png"
OUT_PDF = HERE.parent / "figure1.pdf"

# regime -> staircase level (x order is handled by sorting)
LEVEL = {"MG": 0, "HG": 1, "CG": 2, "na": 2}
TIER_LABEL = {0: "machine-graded", 1: "hybrid-graded", 2: "community-graded"}

# short tick labels: house style keeps em-dashes out, so event names are tagged
# compactly; the authoritative wording stays in the draft's own CSV.
TAG = {
    1: "IMO'24\nG&M + Lean",
    2: "IMO'25\ncoordinators",
    3: "IMO'25\nself-selected",
    4: "o3 / FrontierMath\nsubset 75.7%",
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
    """Parse the ```csv block in the draft's §B into a DataFrame."""
    text = DRAFT.read_text(encoding="utf-8")
    m = re.search(r"```csv\n(.*?)\n```", text, re.S)
    if not m:
        sys.exit("ERROR: no ```csv block found in comment_draft.md (figure is derived, not invented)")
    df = pd.read_csv(io.StringIO(m.group(1)))
    df["regime"] = df["regime"].str.strip()
    return df.sort_values("id").reset_index(drop=True)


def check_tallies(df):
    """Recompute the two body tallies from the data; fail loudly on mismatch."""
    mh = df[df["regime"].isin(["MG", "HG"])]
    comm = df[df["regime"].isin(["CG", "na"])]  # parent grouping: 'na' sits in community denominator
    mh_dispute = int(mh["dispute"].sum())
    comm_dispute = int(comm["dispute"].sum())
    n_mh, n_comm = len(mh), len(comm)
    print(f"machine-or-hybrid graded: {mh_dispute}/{n_mh}  events have a recorded public dispute")
    print(f"community graded (+ n/a): {comm_dispute}/{n_comm} events have a recorded public dispute")
    ok = (mh_dispute, n_mh, comm_dispute, n_comm) == (1, 6, 3, 5)
    if not ok:
        sys.exit(f"ERROR: tallies do not reproduce the body's 1/6 and 3/5 -> got {mh_dispute}/{n_mh}, {comm_dispute}/{n_comm}")
    print("PASS: figure tallies reproduce the body (1/6 and 3/5); no facts added")
    return mh_dispute, n_mh, comm_dispute, n_comm


def draw(df):
    # order columns by staircase level, then id -> a left-to-right rise
    df = df.assign(_lvl=df["regime"].map(LEVEL)).sort_values(["_lvl", "id"]).reset_index(drop=True)
    xs = range(len(df))

    fig = plt.figure(figsize=(9.4, 6.0), dpi=150)
    gs = fig.add_gridspec(2, 1, height_ratios=[3, 1.7], hspace=0.32)

    # ---- top: the regime staircase ----------------------------------------
    ax = fig.add_subplot(gs[0])
    for lvl in (0, 1, 2):
        band = df[df["_lvl"] == lvl]
        if band.empty:
            continue
        x0, x1 = band.index.min() - 0.5, band.index.max() + 0.5
        ax.add_patch(Rectangle((x0, lvl - 0.42), x1 - x0, 0.84,
                               color=["#eef3fb", "#eaf4ee", "#f7f0e6"][lvl], zorder=0))
        ax.text((x0 + x1) / 2, lvl + 0.5, TIER_LABEL[lvl],
                ha="center", va="bottom", fontsize=9, style="italic", color="#444")

    for _, r in df.iterrows():
        disputed = int(r["dispute"]) == 1
        ax.plot(r.name, r["_lvl"], marker="o", markersize=13,
                markerfacecolor="#c62828" if disputed else "white",
                markeredgecolor="#c62828" if disputed else "#555",
                markeredgewidth=1.6, zorder=3)

    ax.set_xlim(-0.6, len(df) - 0.4)
    ax.set_ylim(-0.7, 2.9)
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels([])
    ax.set_xticks(list(xs))
    ax.set_xticklabels([TAG[i] for i in df["id"]], fontsize=6.6, rotation=45, ha="right")
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.set_ylabel("certification regime", fontsize=9)

    # rate captions
    mh_idx = df.index[df["regime"].isin(["MG", "HG"])]
    comm_idx = df.index[df["regime"].isin(["CG", "na"])]
    ax.set_title("Dispute lands where grading is human: 1/6 machine-or-hybrid vs 3/5 community",
                 fontsize=10.5, pad=12, weight="bold")

    legend = [
        Line2D([], [], marker="o", color="w", markerfacecolor="#c62828", markeredgecolor="#c62828",
               markersize=11, label="public dispute recorded"),
        Line2D([], [], marker="o", color="w", markerfacecolor="white", markeredgecolor="#555",
               markersize=11, label="no public dispute"),
    ]
    ax.legend(handles=legend, loc="upper left", fontsize=8, frameon=False)

    # ---- bottom: verification-question heat-strip -------------------------
    ax2 = fig.add_subplot(gs[1], sharex=ax)
    grid = df[Q_COLS].values  # events x questions
    for xi in range(len(df)):
        for yi in range(len(Q_COLS)):
            mark = str(grid[xi, yi]).strip()
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
    # light separators between regimes
    for lvl in (0, 1, 2):
        band = df[df["_lvl"] == lvl]
        if not band.empty:
            ax2.axvline(band.index.min() - 0.5, color="#bbb", lw=0.8)
    ax2.axvline(len(df) - 0.5, color="#bbb", lw=0.8)

    fig.text(0.5, 0.015,
             "n = 11 publicly recorded 2024-2026 certification events, selected through publicity; "
             "Fisher exact P \u2248 0.24 (descriptive, not a frequency). Data: comment_draft.md §B (parent coding).",
             ha="center", fontsize=6.6, color="#555")

    fig.savefig(OUT_PNG, bbox_inches="tight")
    fig.savefig(OUT_PDF, bbox_inches="tight")
    print(f"wrote {OUT_PNG}")
    print(f"wrote {OUT_PDF}")


if __name__ == "__main__":
    events = load_events()
    check_tallies(events)
    draw(events)
    print("ALL SELF-CHECKS PASSED")
