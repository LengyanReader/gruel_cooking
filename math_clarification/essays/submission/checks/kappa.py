"""Cohen's kappa for the census study's coder-reliability gate — pure stdlib.

Companion to ../census_protocol.md §8. That gate requires each doubly-coded column
(regime, each of Q1..Q5, dispute, and the §3.2 novelty screen) to reach kappa >= 0.6
before it may enter the primary analysis; a column below threshold is reported
descriptively with its divergence list. This script is the arithmetic behind that
decision, so that the gate is machine-checked rather than asserted (MC-W2 / R-D).

Definition (unweighted Cohen's kappa for two coders over nominal categories):
    po = observed agreement = (sum of confusion-matrix diagonal) / N
    pe = chance agreement   = sum_k (row_k * col_k) / N**2
    kappa = (po - pe) / (1 - pe)
pe == 1 (a degenerate column coded to one category every time) leaves kappa
undefined; that case returns None and the column cannot pass the gate. The ordinal
regime column *could* use a weighted kappa, but §8 names plain Cohen's kappa, so this
file implements exactly what the protocol promises and no more.

Run:  python kappa.py            # self-tests the worked example, cross-checks sklearn
Deps: none required (stdlib). If scikit-learn happens to be installed, the __main__
block additionally cross-checks every example against sklearn.metrics.cohen_kappa_score.
"""

from collections import Counter


def kappa_from_pairs(pairs):
    """Cohen's kappa from an iterable of (coder1_label, coder2_label) pairs."""
    matrix = Counter(pairs)
    cats = sorted({label for pair in pairs for label in pair})
    n = sum(matrix.values())
    if n == 0:
        raise ValueError("no paired observations")
    diag = sum(matrix[(c, c)] for c in cats)
    po = diag / n
    row = {a: sum(matrix[(a, b)] for b in cats) for a in cats}
    col = {b: sum(matrix[(a, b)] for a in cats) for b in cats}
    pe = sum(row[c] * col[c] for c in cats) / (n * n)
    if pe == 1.0:
        return None                      # degenerate: kappa undefined
    return (po - pe) / (1 - pe)


def kappa_from_matrix(cat, counts):
    """Cohen's kappa from a square confusion matrix.

    `cat` lists categories; `counts[i][j]` = items coder1 put in cat[i] and coder2
    put in cat[j]. Same result as kappa_from_pairs over the expanded pair list.
    """
    pairs = []
    for i, a in enumerate(cat):
        for j, b in enumerate(cat):
            pairs += [(a, b)] * counts[i][j]
    return kappa_from_pairs(pairs)


def verdict(k, gate=0.6):
    """Reading of a kappa value against the protocol gate + Landis–Koch bands."""
    if k is None:
        return "undefined (degenerate column) — cannot enter primary analysis"
    band = ("poor" if k < 0 else "<0.20 slight" if k < 0.20 else
            "<0.40 fair" if k < 0.40 else "<0.60 moderate" if k < 0.60 else
            "<0.80 substantial" if k < 0.80 else "almost perfect")
    return f"{k:.4f}  [{band}]  -> {'PASS' if k >= gate else 'FAIL'} gate (>= {gate})"


# --- worked example, checkable by hand (see census_protocol.md §8) ---------------
# Two coders classify N=100 events; confusion matrix over {yes, no}:
#              coder2
#            yes   no
# coder1 yes  55   15
#        no   10   20
# po = (55+20)/100 = 0.75
# row totals (yes=70,no=30), col totals (yes=65,no=35)
# pe = (70*65 + 30*35)/100**2 = (4550 + 1050)/10000 = 0.56
# kappa = (0.75 - 0.56)/(1 - 0.56) = 0.19/0.44 = 0.431818...
WORKED_MATRIX = [["yes", "no"], [[55, 15], [10, 20]]]
WORKED_EXPECT = 0.19 / 0.44

if __name__ == "__main__":
    cat, counts = WORKED_MATRIX
    k = kappa_from_matrix(cat, counts)
    print(f"worked example (2x2, N=100): kappa = {k:.6f}   expected = {WORKED_EXPECT:.6f}")
    assert abs(k - WORKED_EXPECT) < 1e-12, "hand-check failed"
    print("verdict:", verdict(k))

    # perfect and chance baselines
    assert kappa_from_pairs([("a", "a"), ("b", "b")]) == 1.0
    print("perfect agreement kappa =", kappa_from_pairs([("a", "a"), ("b", "b")]))
    print("degenerate (all one category) ->", kappa_from_pairs([("a", "a"), ("a", "a")]))

    # optional cross-check against scikit-learn, if present
    try:
        from sklearn.metrics import cohen_kappa_score
        flat = []
        for i, a in enumerate(cat):
            for j, b in enumerate(cat):
                flat += [(a, b)] * counts[i][j]
        sk = cohen_kappa_score([p[0] for p in flat], [p[1] for p in flat])
        print(f"sklearn cross-check: {sk:.6f}  (matches: {abs(sk - k) < 1e-9})")
        assert abs(sk - k) < 1e-9
    except ImportError:
        print("sklearn not installed — hand-check above is the verification")
    print("ALL SELF-CHECKS PASSED")
