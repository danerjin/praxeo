# math-augmented-praxeo

A separate, minimal mathematical annex to the praxeological analyser. **It is not praxeology.** It lives in its own folder so that nothing in `handbook/` or `praxeo/` depends on it. Nothing in the main analysis may cite it as a reason for a sign.

**Start with `SURVEY.md`.** It goes through the main mathematical methods economists use and sorts each one: adopted, adopted as a bound only, usable as an input only, or excluded, with the reason.

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
   | **M0** | Nothing beyond its inputs: identities and arithmetic. | Equation of exchange and the Fisher relation. Inflation tax, debt dynamics, sectoral balances. Present value and capitalization, price paths, stock-flow arithmetic. Little's law, expected penalties, quota rents. |
   | **M1** | Local linearity only: for small changes, %ΔQ = elasticity × %ΔP, with elasticities given as ranges. No fitted curve, no functional form. | Supply and demand intersection. Ceiling shortage and floor surplus. Tax and subsidy incidence, exchanges forgone, the tariff. Spending change, cost pass-through (as a bound), tax revenue with base response. |
   | M2 and above | Functional forms, estimated systems, general equilibrium. | **Excluded.** Too many assumptions for what they add here. |
   | Excluded at any rung | Money measures of welfare: consumer and producer surplus, deadweight loss in money, welfare cost-benefit. | They add up ordinal value across persons. The annex counts the exchanges forgone instead. |

4. **M1 says when it is strained.** Above a 15% price gap, a constant elasticity is a strong assumption, and the result carries a warning to treat it as indicative only.
5. **Signs inside M1 come from praxeology.** Downward-sloping demand and non-negative supply response are the laws of demand and supply (LW-3, LW-4). A demand elasticity above zero is rejected, not used.

## How the annex relates to the core rules

**1. The core rules constrain the mathematics, never the reverse.**
- Directions come from the core rules and the laws. Downward-sloping demand and a non-negative supply response are LW-3 and LW-4; a demand elasticity above zero is rejected, not used. The annex sizes those directions and derives none.
- Methods are excluded exactly where they conflict with the core rules:
  - Keynesian multipliers contradict CR-8: means taken by a tax come from other uses.
  - Surplus and deadweight loss in money contradict the ordinal value behind CR-2 and CR-3.
  - Monopoly and game models replace CR-4's ordinal margin with an assumed model of how people decide.
- A range with the opposite sign to the praxeological consequence is reported as *contradicts*. It means an input range is wrong or a praxeological premise failed. The annex never resolves it by changing the sign.

**2. Where each part attaches.**

| Core rule | What the core rule decides | What the annex can add |
|---|---|---|
| CR-3, CR-8 (cost; conservation of means) | Who bears a loss; that means taken come from other uses | How much: inflation tax, debt dynamics, sectoral balances |
| CR-4 (response at the margin) | Direction of every switch; the means exception is `ambiguous` without a premise | `spending_change` (whether spending on the good rises or falls); `expected_penalty` (evidence for an enforcement premise) |
| CR-5 (exchange) | Exchanges that no longer happen (CR-5a) | `quantity_under_wedge`: how many, counted, never valued |
| CR-6 (price formation, displaced pressure) | Shortage, surplus, and pressure moved to other margins | Shortage, surplus, equilibrium shift, tax and subsidy incidence, wait times (Little's law) |
| CR-7 (equalization across uses; CR-7c) | Resources move; asset values change when the policy is expected | Present value, capitalized loss, quota and licence values |
| CR-9 (propagation) | The chain to linked markets | Cost pass-through (a bound); imports as use minus domestic output |
| CR-10 (time) | Timing per window | Price-gap paths (when a cap starts to bind), stock-flow (how fast a durable stock shrinks), doubling times |
| CR-12 (composition) | Opposing chains combine to `ambiguous` unless arithmetic or a premise settles them | See point 3 |

CR-1, CR-2 and CR-11 (what a policy can do to an actor, choice, knowledge) have no counterpart here, and should not have one.

**3. CR-12 is the one point of contact, and it is guarded.** CR-12e (0.8) already allows opposing chains to be combined by arithmetic where the case gives the figures, and by a premise otherwise. The annex respects that line:
- **M0 on the case's own figures may settle.** `bridge.settle_by_arithmetic` lets an M0 result settle a CR-12 comparison only when every input it used comes from the case record (`from_case: true`). That is the arithmetic CR-12e already allows, done in code.
- **M1, or any result on illustrative or outside ranges, can only be evidence.** `bridge.premise_evidence` proposes a probability for the dominance premise, with its source:
  - one range wholly larger than the other gives 0.9 or 0.1;
  - overlapping ranges give no change.

  It never writes the probability. A decider (LLM, human or Jev) must accept it, and the source is logged. `settle_by_arithmetic` raises `GuardError` if it is given such a result.

Without this guard, an elasticity guess could decide a sign through the back door.

**4. Two labels, never merged.** A consequence keeps its tier (A, B, J, C), which says how its sign was derived. An annex result carries a rung (M0, M1), which says what its size assumes. A Tier A sign with an M1 size is Tier A for its sign; the size is only as good as its ranges.

**5. One-way dependency, checked.** `bridge.annex_pass` reads a frozen `prediction.json` from `praxeo`. For each reported consequence whose variable has a handler, it attaches a range, its rung, the sign check and the source of every input. It verifies that the prediction is unchanged and raises `GuardError` if not. Nothing in `praxeo/` or `handbook/` imports the annex.

```
python3 -m praxeo cases/sf_1994 --out runs/sf
python3 math-augmented-praxeo/annex_run.py runs/sf/prediction.json math-augmented-praxeo/examples/sf_1994/annex_inputs.json runs/sf
```

`examples/sf_1994/annex.md` is the result for the committed sample run. Both attachments agree with their signs: the covered stock's quantity supplied, and sitting tenants' rent against the market path. All ranges but the horizon are illustrative.

## The equation of exchange

M V = P Y is used as an **identity** (rung M0). In growth factors it holds exactly: (1 + p) = (1 + m)(1 + v) / (1 + y). The identity is close to a priori: it restates that spending equals spending. The *quantity theory* goes further and assumes that velocity and real output do not respond to money. That claim is empirical, so here it enters only as ranges the analyst supplies for v and y.

Mises rejected the equation as an explanation (*Theory of Money and Credit*, Part II ch. 8; *Human Action* ch. XVII §4). P is an average, and new money reaches some people first. So individual prices rise at different times and by different amounts, and relative prices and wealth shift along the way (Cantillon effects). The annex therefore bounds the average only. Who gains and who loses stays a praxeological chain.

## Modules

| Module | Rung | Contents |
|---|---|---|
| `mathpraxeo/interval.py` | — | Interval arithmetic and corner evaluation for monotone functions. |
| `mathpraxeo/result.py` | — | `Result` (range, rung, assumptions, note) and `check_sign`. |
| `mathpraxeo/exchange.py` | M0 | Price-level change from m, v and y, and the implied v from observed m, p and y. |
| `mathpraxeo/identities.py` | M0 | Little's law (wait time), expected penalty, inflation tax, Fisher relation, debt dynamics, stock-flow, sectoral balances, doubling time. |
| `mathpraxeo/capital.py` | M0 | Gap path between a capped and a market price, the gap as a share of the market price, the capitalized loss, and the present value of a yearly amount (for license, quota and tax values). |
| `mathpraxeo/statics.py` | M1 (quota rent: M0) | Supply and demand intersection; ceiling shortage, floor surplus, quantity supplied under a held-down price; tax and subsidy incidence; exchanges forgone; tariff; quota rent; spending change; cost pass-through bound; tax revenue with base response. |
| `mathpraxeo/report.py` | — | Renders an annex table with the sign check for each consequence. |
| `mathpraxeo/bridge.py` | — | The annex pass over a `praxeo` prediction, with its guards: `annex_pass`, `premise_evidence`, `settle_by_arithmetic`, `GuardError`. |
| `annex_run.py` | — | Command line for the annex pass. |

## Examples

**The elasticities, shares, rates and durations in both examples are illustrative ranges, not estimates.**

- **`examples/we001_annex.py`** (WE-001, Riverton rent freeze) sizes three consequences: the year-3 shortage, the year-10 fall in quantity supplied, and the fall in building values at announcement. All three ranges agree with the praxeological signs. Two are flagged as strained, because the gaps grow large.
- **`examples/we013_annex.py`** (WE-013, Halvern steel tariff of 25%) sizes six consequences. Five agree with their signs:
  - the domestic steel price;
  - domestic output;
  - imports;
  - steel bought;
  - revenue short of the static projection.

  The sixth, construction prices, is *indeterminate*, because a pass-through bound includes zero. That is correct: the sign comes from the praxeological chain, and the annex only bounds its size.

## Run

```
python3 -m pytest math-augmented-praxeo/tests
python3 math-augmented-praxeo/examples/we001_annex.py
```

## Status and next steps

- This is a folder on the working branch, not a separate branch. A separate branch can be cut from it if wanted.
- The annex pass has handlers for `quantity_supplied`, `excess_demand` and the insiders' `price_paid`. More handlers (asset values, tariff consequences, wait times) follow the same pattern.
- Premise evidence is computed but not yet offered to a decider in the `praxeo` run; that needs a step where the decider sees the proposal and accepts or rejects it, logged.
- Bounds not yet built (see `SURVEY.md`): the black-market price under a ceiling, the Hotelling rule, rent-seeking dissipation, covered interest parity.
