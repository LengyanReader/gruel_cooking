"""Power of the census study's primary test — exact enumeration.

Companion to ../census_protocol.md §6. The protocol's endpoint is a one-sided
Fisher exact test comparing the dispute rate of community-graded events (stratum C)
with machine-graded events (stratum M), equal stratum sizes, alpha = 0.025, target
power 0.80.

Method (no normal approximation): the two dispute counts are independent binomials
X ~ Bin(n, pM) and Y ~ Bin(n, pC). For each pair (x, y) the one-sided p-value is the
hypergeometric tail P(X <= x | margins), i.e. `hypergeom.cdf(x, 2n, x+y, n)`; the
power at n is the binomial-weighted mass of the pairs whose p-value is <= alpha. n is
raised from 5 until that mass reaches the target. Exact size, exact power; the test is
discrete, so achieved power jumps past the target rather than landing on it.

Run:  conda activate hy_py312 && python power_fisher.py
Deps: scipy only (stdlib math for the binomials).
"""

from math import comb

from scipy.stats import hypergeom

ALPHA = 0.025   # one-sided, fixed in the protocol
TARGET = 0.80   # power, fixed in the protocol
N_MAX = 400     # give up beyond this per-stratum n and report None


def fisher_exact_power(n: int, pC: float, pM: float, alpha: float = ALPHA) -> float:
    """Rejection probability of the one-sided Fisher test at stratum size n."""
    rej = 0.0
    for x in range(n + 1):                       # disputes in stratum M
        px = comb(n, x) * pM**x * (1 - pM) ** (n - x)
        if px == 0.0:
            continue
        for y in range(n + 1):                   # disputes in stratum C
            pval = hypergeom.cdf(x, 2 * n, x + y, n)
            if pval <= alpha:
                rej += px * comb(n, y) * pC**y * (1 - pC) ** (n - y)
    return rej


def n_for_power(pC: float, pM: float, alpha: float = ALPHA, target: float = TARGET):
    """Smallest per-stratum n reaching `target` power, and the power achieved there."""
    for n in range(5, N_MAX + 1):
        pw = fisher_exact_power(n, pC, pM, alpha)
        if pw >= target:
            return n, pw
    return None, None


# pM = 0 exactly is degenerate for a binomial; 1e-9 is the numerical stand-in for
# "the machine stratum never produces a dispute", which is prediction P1 verbatim.
ZERO = 1e-9

SCENARIOS = [
    (0.60, 0.05), (0.60, ZERO),
    (0.40, 0.05), (0.40, ZERO),
    (0.30, 0.05), (0.30, ZERO),
    (0.20, 0.05), (0.20, ZERO),
    (0.15, ZERO), (0.10, ZERO),
]

if __name__ == "__main__":
    print(f"one-sided Fisher exact test, alpha={ALPHA}, target power={TARGET}")
    print(" rate_C   rate_M    n/stratum   achieved power")
    for pC, pM in SCENARIOS:
        n, pw = n_for_power(pC, pM)
        shown = "0.00" if pM == ZERO else f"{pM:.2f}"
        cell = f"{pw:.3f}" if pw else ">400"
        print(f"  {pC:.2f}    {shown:>4}   {str(n):>6}      {cell}")
