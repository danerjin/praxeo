# Survey: mathematical methods in economics, judged for the annex

This file goes through the main mathematical methods economists use. For each it says whether the method meets the annex's rules (README) and whether it is relevant to the handbook's patterns. A method qualifies when it meets three conditions:
- It needs no assumption beyond identities, arithmetic or local linearity with sourced elasticity ranges.
- It never has to decide a sign.
- It adds a size, a bound or a timing the praxeological chain lacks.

**Verdicts**
- **Adopt:** in the annex.
- **Bound:** adopted only as an upper or lower bound, never as a point estimate.
- **Input:** not a method of derivation; a legitimate source for the ranges the annex takes as inputs.
- **Exclude:** fails the rules, with the reason given.

**Rungs**
- **M0:** identities and arithmetic.
- **M1:** first-order, local, with elasticity ranges.

## 1. Accounting identities and arithmetic (M0)

| Method | Verdict | Assumes | Relevance | Module |
|---|---|---|---|---|
| Equation of exchange, MV = PY | Adopt, as an identity | Nothing; v and y enter as ranges | Monetary policies, budget deficits financed by money, the price level (TX-8, OC-8) | `exchange.price_level_change` |
| Quantity theory of money (v and y independent of M) | Input | That velocity and output do not respond to money: empirical | Same as above; enters only as narrow ranges for v and y | (ranges for `exchange`) |
| Fisher relation: (1+i) = (1+r)(1+π) | Adopt, as a definition | Nothing (ex post); expected inflation is an input | Real rates under interest caps and inflation; debt policies | `identities.real_rate` |
| Inflation tax on money balances | Adopt | Nothing beyond the inputs | Who loses when prices rise: holders of money. Pairs with Cantillon effects | `identities.inflation_tax` |
| Government budget constraint and debt dynamics | Adopt | Nothing; r, g and the primary balance are ranges | OC-8 (crowding out), OC-9 (debt-funded transfers), TX-9 | `identities.debt_path` |
| Sectoral balances: (S−I) + (T−G) + (M−X) = 0 | Adopt, as an identity | Nothing | Deficits and the currency link (TX-8, OC-8). The identity says nothing about which balance adjusts | `identities.sectoral_balance` |
| Balance of payments (current + capital account = 0) | Adopt, as an identity (same logic as sectoral balances) | Nothing | TX-8 (imports provide the means to buy exports or assets) | via `sectoral_balance` |
| Present value and capitalization | Adopt | A discount rate and an expected duration, as ranges | CR-7c, SB-4 (asset values), value of licenses and quotas (EN-), lasting taxes | `capital.capitalized_loss`, `capital.present_value` |
| Price-path arithmetic (caps, indexation, compounding) | Adopt | Growth rates as ranges | PC-1, TS-3, TS-10 (when a cap starts to bind; size of the gap) | `capital.cap_gap_path`, `identities.doubling_time` |
| Stock-flow accounting: K' = K(1−δ) + additions | Adopt | Depreciation and additions as ranges | TS-1, PC-5 (how fast a durable stock shrinks when building stops) | `identities.stock_path` |
| Little's law, L = λW (queueing) | Adopt | A stable queue | PC-2 (rationing by waiting), public supply at a set price (PC-19) | `identities.wait_time` |
| Expected value of a penalty | Adopt, to inform premises | Detection probability and penalty as ranges | Enforcement premises (A-2-type), RS-3, RS-20. Informs a premise; never decides it | `identities.expected_penalty` |
| Index numbers (CPI, deflators) | Input | The choice of basket | Converting nominal to real figures. Mises's critique applies (an average of incommensurable changes), so indices are inputs, never conclusions | — |
| Comparative advantage arithmetic (Ricardo) | Already praxeological | — | Mises's law of association (HA ch. VIII). The arithmetic illustrates a priori reasoning and adds nothing to it | — |
| Lerner symmetry (an import tax equals an export tax) | Already praxeological | Trade balanced over time | TX-8 already derives it through the currency link | — |

## 2. Partial equilibrium: supply and demand, first order (M1)

| Method | Verdict | Assumes | Relevance | Module |
|---|---|---|---|---|
| Supply and demand intersection; comparative statics of shifts | Adopt | Local linearity; elasticity ranges. Signs from LW-3 and LW-4 | Any policy that shifts demand or supply (subsidies to buyers, entry barriers, mandates) | `statics.equilibrium_shift` |
| Shortage under a ceiling | Adopt | As above | PC-1, PC-2 | `statics.ceiling_shortage` |
| Surplus under a floor (minimum wage) | Adopt | As above | PC-9, PC-10, PC-11 | `statics.floor_surplus` |
| Quantity supplied under a held-down price | Adopt | As above, with a horizon-specific supply elasticity | PC-5 | `statics.ceiling_quantity_supplied` |
| Tax incidence | Adopt | As above | TX-1, TX-2, TX-3; who bears a tax | `statics.tax_incidence` |
| Subsidy incidence | Adopt | As above | SB-1, SB-2, SB-8 | `statics.subsidy_incidence` |
| Quantity traded under a wedge (exchanges forgone) | Adopt, counted not valued | As above | CR-5a, TX-2, OC-2 (compliance cost as a wedge) | `statics.quantity_under_wedge` |
| Tariff: domestic price, output, use, imports | Adopt; pass-through as a range | As above; pass-through in [0, 1] | TX-7, TX-8, SB-10 | `statics.tariff` |
| Quota rent and license value | Adopt (M0 once the gap is known) | The price gap as a range | EN-1, EN-6, EN-12, EN-13 (value of a right) | `statics.quota_rent` + `capital.present_value` |
| Spending on a good after a price change, (1+ε)·%ΔP | Adopt | As above | CR-4's means exception (whether spending on the burdened good rises or falls); TX-6 | `statics.spending_change` |
| Cost pass-through up and down a chain | Bound: [0, cost share × input change] | Between no and full pass-through | RS-14, PC-12, TX-7 (steel users) | `statics.cost_pass_through` |
| Tax revenue with base response (the arithmetic behind the Laffer curve) | Adopt, first order; no claim about a revenue peak | Elasticity of the base to the net-of-tax rate, as a range | OC-1, TX-2, TX-9 (does revenue rise by less than the rate?) | `statics.revenue_change` |
| Cross-price effects (spillover to substitutes) | Adopt via `equilibrium_shift` | A demand shift in the substitute market = cross elasticity × price change | PC-8, RS-1, RS-4, RS-16 | `equilibrium_shift` with a = cross elasticity × %ΔP |
| Black-market price bounds | Bound | Under a ceiling, the illegal price lies between the ceiling and the clearing price plus the expected penalty per unit | PC-6, RS-3 | Not built; expressible with `expected_penalty` and `ceiling_shortage` |
| Hotelling rule (an exhaustible resource's price rises at the rate of interest) | Bound only | No-arbitrage over time, a known stock and known costs | Resource taxes and quotas (EN-, TX-12). Usable only as "the price path cannot rise much faster than r without inviting earlier extraction" | Not built |
| Rent-seeking dissipation (Tullock) | Bound: spending on lobbying ≤ the value of the rent to all bidders together | That bidders do not overpay in total, roughly | RS-7 (lobbying) | Not built; `present_value` gives the rent |

## 3. Valuation in money of gains and losses

| Method | Verdict | Why |
|---|---|---|
| Consumer and producer surplus; deadweight loss (Harberger triangle) in money | **Exclude** | It treats the area under a demand curve as a sum of value. Value is ordinal and cannot be added across persons or measured in money (LW-1, HA ch. II and XIV). The annex counts the exchanges forgone (`quantity_under_wedge`) and stops there. |
| Cost-benefit analysis with net present value of welfare | **Exclude** | Same reason, plus interpersonal comparison. Present value of *money flows* (taxes, rents, asset prices) is adopted; present value of *welfare* is not. |
| Compensating and equivalent variation | **Exclude** | Same: a money measure of utility. |
| Social welfare functions, optimal tax (Ramsey, Mirrlees) | **Exclude** | Normative, and they need a welfare function. Out of scope (the handbook's analysis is positive). |

## 4. Optimization, market structure and strategic models

| Method | Verdict | Why |
|---|---|---|
| Utility maximization with calculus (Lagrangians, indifference curves) | **Exclude** | Cardinal or differentiable utility. CR-4 already gives every direction these models are used for, from ordinal ranking alone. |
| Cost minimization and production functions (Cobb-Douglas, CES) | **Exclude** (functional forms) | Cost shares are adopted as *inputs* (`cost_pass_through`); the forms are not. |
| Perfect competition as a benchmark | **Exclude** | An imaginary state (Mises's evenly rotating economy) that never obtains. The annex works with changes, not with distance from an ideal. |
| Monopoly pricing, Lerner index, markups p = MC·ε/(ε+1) | **Exclude** | Needs a known demand curve and profit maximization at a point. Where a policy creates a single seller, the handbook's EN patterns give the direction. |
| Oligopoly models (Cournot, Bertrand, Stackelberg) | **Exclude** | Results depend on the model chosen, and each choice is an assumption about how rivals think. |
| Game theory: Nash equilibrium, mechanism design | **Exclude as computation; already praxeological where it is logic** | Dominant-strategy arguments (a prisoner's dilemma among sellers) are CR-4 applied to each actor. Equilibria that need common knowledge of payoffs are assumptions. |
| Search and matching models | **Exclude** | Functional forms for matching. Little's law (adopted) gives the waiting arithmetic without them. |
| Cobweb and hog-cycle models | **Exclude** | They assume a specific way of forming expectations. CR-10 handles timing. |

## 5. Macroeconomic and system models

| Method | Verdict | Why |
|---|---|---|
| Keynesian multipliers (spending multiplier, balanced-budget multiplier) | **Exclude** | They assume idle resources respond only to aggregate spending, and treat spending, not saving, as the source of income. That contradicts CR-8 (a tax-funded outlay is taken from other uses) and has no praxeological basis. |
| IS-LM, AD-AS, Phillips curve, Taylor rule | **Exclude** | Aggregate behavioral relations, estimated or assumed. They carry many assumptions and are contested. |
| DSGE and computable general equilibrium (CGE) models | **Exclude** | Hundreds of functional forms and calibrated parameters; they assume an equilibrium. They are the opposite of "few assumptions". |
| Input-output (Leontief) tables | **Exclude as a model; Input as data** | Fixed coefficients are an assumption. An input-output table's cost shares are adopted as *inputs* to `cost_pass_through`. |
| Growth accounting (Solow residual) | **Exclude** | A residual defined by a production function. |
| Ricardian equivalence | **Exclude** | A behavioral claim (people offset deficits by saving), empirical and disputed. The debt arithmetic is adopted (`debt_path`); the behavioral claim is not. |
| Purchasing power parity (absolute or relative) | **Input** | A long-run tendency, not an identity. Usable as a range for the exchange-rate response in TX-8, never as a law. |
| Covered interest parity | **Bound** | An arbitrage condition that holds closely in practice. Usable as a bound on forward exchange rates; rarely needed by the handbook. |

## 6. Statistical and empirical methods

| Method | Verdict | Why |
|---|---|---|
| Econometrics, regression, difference-in-differences, synthetic control | **Input** | They estimate elasticities and effects in past cases. They are the right source for the ranges the annex takes, and for outcome cards. They are not a way of deriving consequences. A cited estimate's confidence interval is a natural range. |
| Calibration and simulation | **Exclude** | Points chosen to fit, not ranges sourced. |
| Probability and expected value | **Adopt where it is arithmetic** | Expected penalties (above); the system's assumption probabilities (already in the method). |
| Forecasting from time series | **Input** | Counterfactual paths (the market rent without the policy) are inputs: a range, cited. |

## Summary

- **Adopted, in code (25 functions):**
  - M0, 14 functions: the equation of exchange and the velocity it implies; the Fisher relation; the inflation tax; debt dynamics; sectoral balances; present value, capitalized loss and price-path arithmetic; stock-flow arithmetic; doubling time; Little's law; expected penalty; quota rent.
  - M1, 11 functions: the supply and demand intersection; ceiling shortage, floor surplus and quantity supplied under a held-down price; tax and subsidy incidence; exchanges forgone; the tariff; spending change; cost pass-through (as a bound); tax revenue with base response.
- **Bounds only, not built yet:** black-market price, Hotelling, rent-seeking dissipation, covered interest parity.
- **Inputs, not methods:** econometric estimates, index numbers, input-output cost shares, purchasing power parity, forecasts.
- **Excluded:**
  - every money measure of welfare (surplus, deadweight loss in money, cost-benefit in welfare terms);
  - utility calculus and functional forms;
  - market-structure, oligopoly and equilibrium-game models;
  - Keynesian multipliers;
  - macro and general-equilibrium systems, growth accounting, Ricardian equivalence.
