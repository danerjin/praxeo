# math-augmented-praxeo

A separate, minimal mathematical annex to the praxeological analyser. **It is not praxeology.** It lives in its own folder so that nothing in `handbook/` or `praxeo/` depends on it. Nothing in the main analysis may cite it as a reason for a sign.

## What it is for

The praxeological method gives directions and conditions: rents for sitting tenants fall, quantity supplied falls if owners have other uses for the buildings. It does not give sizes. The annex adds sizes and bounds to consequences the method has already signed, using as little mathematics and as few assumptions as possible.

## Rules

1. **It never sets or changes a sign.** Every result is checked against the praxeological sign (`check_sign`) and reported as one of:
   - *agrees*.
   - *indeterminate*: the range straddles zero, or the sign was `ambiguous`.
   - *contradicts*: an input range is wrong, or a praxeological premise failed. Report it; never resolve it here.
2. **Ranges, never points.** Every input is an interval the analyst must source, and every output is an interval. Arithmetic is interval arithmetic. Bounds come from the corners only where the function is monotone in each input, and each function says why it is.
3. **The fewest assumptions that do the job, on a ladder.** Each result states its rung and lists every assumption it took.

   | Rung | What it assumes | Examples here |
   |---|---|---|
   | **M0** | Nothing beyond its inputs: identities and arithmetic. | Equation of exchange as an identity. Gap between a capped and a market price path. Present value of that gap. |
   | **M1** | Local linearity only: for small changes, %ΔQ = elasticity × %ΔP, with elasticities given as ranges. No fitted curve, no functional form. | Shortage at a ceiling. Fall in quantity supplied. Tax incidence. |
   | M2 and above | Functional forms, estimated systems, general equilibrium. | **Excluded.** Too many assumptions for what they add here. |

4. **M1 says when it is strained.** Above a 15% price gap, a constant elasticity is a strong assumption, and the result carries a warning to treat it as indicative only.
5. **Signs inside M1 come from praxeology.** Downward-sloping demand and non-negative supply response are the laws of demand and supply (LW-3, LW-4). A demand elasticity above zero is rejected, not used.

## The equation of exchange

M V = P Y is used as an **identity** (rung M0). In growth factors it holds exactly: (1 + p) = (1 + m)(1 + v) / (1 + y). The identity is close to a priori: it restates that spending equals spending. The *quantity theory* goes further and assumes that velocity and real output do not respond to money. That claim is empirical, so here it enters only as ranges the analyst supplies for v and y.

Mises rejected the equation as an explanation (*Theory of Money and Credit*, Part II ch. 8; *Human Action* ch. XVII §4). P is an average, and new money reaches some people first. So individual prices rise at different times and by different amounts, and relative prices and wealth shift along the way (Cantillon effects). The annex therefore bounds the average only. Who gains and who loses stays a praxeological chain.

## Modules

| Module | Rung | Contents |
|---|---|---|
| `mathpraxeo/interval.py` | — | Interval arithmetic and corner evaluation for monotone functions. |
| `mathpraxeo/result.py` | — | `Result` (range, rung, assumptions, note) and `check_sign`. |
| `mathpraxeo/exchange.py` | M0 | Price-level change from m, v and y, and the implied v from observed m, p and y. |
| `mathpraxeo/capital.py` | M0 | Gap path between a capped and a market price, the gap as a share of the market price, and the capitalized loss (present value of the gaps over an expected duration). |
| `mathpraxeo/statics.py` | M1 | Shortage share at a ceiling, quantity supplied under a held-down price, and tax incidence. |

## Example

`examples/we001_annex.py` sizes three consequences of the handbook's WE-001 (Riverton rent freeze) and writes `examples/we001_annex.md`:
- the year-3 shortage;
- the year-10 fall in quantity supplied;
- the fall in building values at announcement.

All three ranges agree with the praxeological signs. Two are flagged as strained first-order results, because the gaps grow large. **The elasticities, discount rate and expected duration in it are illustrative ranges, not estimates.**

## Run

```
python3 -m pytest math-augmented-praxeo/tests
python3 math-augmented-praxeo/examples/we001_annex.py
```

## Status and next steps

- This is a folder on the working branch, not a separate branch. A separate branch can be cut from it if wanted.
- Not yet connected to `praxeo/`. The natural hook is an optional pass after the verifier: for each reported consequence whose variable has an annex function, attach a `Result` and its sign check, without touching the consequence.
- Candidates that would stay at M0 or M1:
  - deadweight loss as a range (M1);
  - burden of a budget-funded program per payer (M0);
  - sectoral balance identities for budget deficits (M0);
  - the arithmetic of compounding for inflation targets (M0).
