# Math core rules

The annex's counterpart to the handbook's core rules (`handbook/04a_core_rules.md`). The handbook derives its 106 patterns from twelve core rules. The annex derives every one of its functions and handlers from the seven rules below. Each function and handler carries a derivation line naming them: `@derives(...)` in the code, and `HANDLER_RULES` in `mathpraxeo/bridge.py`. A test checks that none is missing.

**These rules are not praxeology.** Each says what it takes as given and which praxeological core rule it is the quantitative counterpart of. None of them can produce a sign. Signs come only from the core rules. The math rules size what the core rules have already signed, or rank two magnitudes under the guard in MR-7.

## The admission test

> A method belongs in the annex if and only if it can be derived from MR-1 to MR-7, with every input a sourced range.

`SURVEY.md` judged each method one by one. The test turns those judgments into a rule. Every excluded method fails it at an identifiable point (see "Verdicts restated" below). A method proposed later is admitted by writing its derivation line, or excluded by naming the step no rule covers. This is the same discipline the handbook applies to a new pattern.

## Rungs

- **MR-1, MR-2, MR-3 are exact given their inputs.** They are identities, definitions and arithmetic, so their results are rung **M0**.
- **MR-4 and MR-5 assume a stable response over the change considered.** Their results are rung **M1**, and this is where the annex parts from Mises: there are no constant quantitative relations in human action.
- **MR-6 sets limits.** Its direction is praxeological: switching narrows a gap (CR-4, CR-7). How far the gap can stay open is a size, and it depends on switching costs given as ranges. Results that rest on it are **bounds**.
- **MR-7 governs how magnitudes may combine.** It is the annex's form of CR-12.

---

### MR-1 Ranges

**Statement.** Every quantity is a set of possible values: a closed interval given by its lowest and highest value. Operations carry sets to sets, and a result is the full set its inputs allow. A function monotone in each input separately reaches its extremes at the corners of the input box, so corner evaluation is exact for it. Where an input range includes a point at which the result is undetermined, the result is the full range of values it could take there. No conventional value is chosen ("no hidden splits").

**Exact or assumed.** Exact: it is interval arithmetic. The only assumption is that each input range contains the true value, which is the input's source's claim, not the annex's.

**Praxeological counterpart.** The method's rule that no premise stands without an estimate: an assumption gets a probability, and a quantity gets a range.

**Limits.** Corner evaluation is used only where monotonicity in each input has been checked. Otherwise a grid that includes the corners is used (`statics._extremes`), and the function says so.

**Used by.** Everything (`mathpraxeo/interval.py`). It is implied and not named in derivation lines.

### MR-2 Identities and conservation

**Statement.** Over a closed set of accounts, flows balance, and quantities defined as sums, differences or products of others equal them. Spending equals receipts (M V = P Y). Saving net of investment sums to zero across the private, government and foreign sectors. A stock changes by its inflows minus its outflows. Imports are domestic use minus domestic output. A queue's average length is its arrival rate times the average wait (Little's law). A right's yearly rent is the price gap times the quantity it covers. An expected cost is the probability times the amount.

**Exact or assumed.** Exact, by definition or by counting. The identity says nothing about which account moves when another changes: that is a causal question for the core rules.

**Praxeological counterpart.** CR-8 (conservation of means): means taken by a policy come from other uses. MR-2 does the counting; CR-8 says whose means.

**Limits.** An identity used as a theory is outside the annex. For example, the quantity *theory* of money, which says velocity and output do not respond to money, enters only as ranges for v and y. Aggregates such as the price level are averages; who gains and who loses stays a praxeological chain (Cantillon effects).

**Used by.**
- `exchange`: the price-level change and the implied velocity change.
- `identities`: wait time, expected penalty, inflation tax, sectoral balance; debt and stock paths (with MR-3).
- `statics`: quota rent; imports in the tariff; the accounting in spending and revenue changes.
- `bridge.dominance_evidence`: the counts behind each chain.

### MR-3 Compounding and discounting

**Statement.** A value growing at rate g for t periods is multiplied by (1 + g)^t. An amount due in t periods is worth 1 / (1 + r)^t of itself today, at discount rate r. Present values add over periods. The Fisher relation (1 + i) = (1 + r)(1 + π) defines the real rate.

**Exact or assumed.** Exact given the growth rates, the discount rate and the duration. All three are inputs, given as ranges.

**Praxeological counterpart.**
- CR-10 (time): when an effect appears and how it grows.
- CR-7c: a lasting change in income is priced into an asset when it becomes expected. MR-3 says by how much, given the buyers' discount rate and expected duration.
- Time preference (LW-7 in the foundations) is why the discount rate is positive, but the annex takes its size as an input.

**Limits.** The discount rate and expected duration are the buyers' (CR-7c). They are estimated as ranges, never derived.

**Used by.**
- `capital`: gap paths, gap shares, capitalized loss, present value.
- `identities`: real rate, doubling time; the debt and stock paths (with MR-2).
- Handlers for insiders' price, asset values and rights' values.
- Inside the bounds: Hotelling and the rent-seeking ceiling.

### MR-4 First-order response

**Statement.** For a small change in price, the proportional change in quantity demanded or supplied is the elasticity times the proportional change in price. The elasticity's **sign** comes from the laws: demand falls as price rises (LW-3), and supply does not fall (LW-4). A demand elasticity above zero is rejected. The elasticity's **size** is a sourced range for the market and horizon in question. Products of a price and a quantity (spending, revenue) change, to first order, by the sum of their proportional changes.

**Exact or assumed.** Assumed: the response is stable enough over the change for one elasticity range to describe it. This is the annex's first departure from praxeology. Mises held there are no constant relations in human action, so the range is history, not law. Results beyond a 15% price gap are flagged as strained.

**Praxeological counterpart.** CR-4 (response at the margin). CR-4 gives the direction and says that some actors are at the margin (the `substitutability`, `alternative_uses` and `mobility` premises). MR-4 sizes how many.

**Limits.** It is local only. It never decides CR-4's means exception (the direction of spending when the price of a heavily bought good changes); it can only size each side for the premise. It never values the exchanges forgone, only counts them.

**Used by.** In `statics`: ceiling shortage, quantity supplied under a held-down price, floor surplus, quantity under a wedge, spending change, revenue change, and the tariff's output and use. Handlers built on these, and the black-market upper limit.

### MR-5 Clearing as a tendency

**Statement.** When demand shifts by a share a and supply by a share b at the old price, the first-order price change that would remove the excess is (a − b) / (εs − εd). The matching quantity change is (εs·a − εd·b) / (εs − εd). A wedge (a tax or subsidy) between buyers' and sellers' prices splits between them in proportion to the opposite side's response. Buyers bear εs / (εs + |εd|) of it.

**Exact or assumed.** Assumed: MR-4's stable responses, and that the price moves toward clearing. It measures the size of a tendency, not a state the market reaches. Equilibrium is an imaginary construct in Mises (the evenly rotating economy): the annex uses where the curves would meet only to size the pressure.

**Praxeological counterpart.** CR-6 (price formation and displaced pressure): a price held off its clearing level displaces pressure to other margins. CR-6 also says which side bears a wedge, according to which side can move more. MR-5 says how much.

**Limits.** It never claims the market reaches the new point. If both responses can be zero, MR-1's no-hidden-splits rule applies: the share is anything from none to all.

**Used by.** `statics`: equilibrium shift, tax incidence, subsidy incidence. Handlers for the substitute's price and the tax and subsidy prices.

### MR-6 No arbitrage

**Statement.** Where actors can switch between two options (two markets, two times, two currencies, legal and illegal trade, owning and leasing a right), the difference in what the options yield cannot stay above the cost of switching. If it did, someone would gain by switching until it no longer did. So:
- prices and yields are bounded by each other plus switching costs;
- a pass-through lies between none and all;
- an illegal premium lies between what sellers must be paid for the risk and what buyers will pay;
- a resource is extracted sooner when its net price grows more slowly than the rate of interest;
- spending to win a privilege does not exceed its value.

**Exact or assumed.**
- The direction is praxeological: actors switch toward the option that yields more (CR-4), which equalizes yields across uses (CR-7).
- The bound's position depends on switching costs, penalties and rates, which are inputs given as ranges.
- That arbitrage has finished is not assumed: the bound says where the gap must end up, not when.

**Praxeological counterpart.** CR-7 (equalization across uses) and CR-4. MR-6 is the quantitative shadow of CR-7.

**Limits.** It gives bounds, not points. A bound that includes zero cannot confirm a sign, so the sign check reports *indeterminate*.

**Used by.**
- `bounds`: black-market premium, Hotelling gap, rent-seeking ceiling, covered interest parity.
- `statics`: cost pass-through; the tariff's pass-through range.
- Handlers for tariff prices, lease prices of rights, and the bounds.

### MR-7 Composition of magnitudes

**Statement.** Two opposing chains are ranked by size only when their ranges do not overlap. If they overlap, the comparison is undetermined. A ranking may *settle* a CR-12 comparison only when both sizes are rung M0 and every input comes from the case record. That is the arithmetic CR-12e (0.8) already allows. In every other case, the ranking is *evidence* for a dominance premise: the annex proposes a probability, and a decider decides. A sign is never set by MR-7.

**Exact or assumed.** Exact as a comparison of sets. The guard is a rule of method, not a mathematical fact: it keeps M1 assumptions from deciding a sign.

**Praxeological counterpart.** CR-12 (composition): opposing chains combine to `ambiguous` unless arithmetic or a premise settles them.

**Used by.** `bridge.premise_evidence`, `bridge.dominance_evidence`, `bridge.settle_by_arithmetic` (raises `GuardError` when the guard is breached), and `premise_step`.

---

## Derivation lines

**Functions.**

| Module | Function | Math rules |
|---|---|---|
| exchange | price_level_change, implied_velocity_change | MR-2 |
| identities | wait_time, expected_penalty, inflation_tax, sectoral_balance | MR-2 |
| identities | debt_path, stock_path | MR-2, MR-3 |
| identities | real_rate, doubling_time | MR-3 |
| capital | cap_gap_path, gap_share, capitalized_loss, present_value | MR-3 |
| statics | ceiling_shortage, ceiling_quantity_supplied, floor_surplus | MR-4 |
| statics | equilibrium_shift, tax_incidence, subsidy_incidence | MR-5 |
| statics | quantity_under_wedge | MR-4, MR-5 |
| statics | quota_rent | MR-2 |
| statics | spending_change, revenue_change | MR-2, MR-4 |
| statics | tariff | MR-2, MR-4, MR-6 |
| statics | cost_pass_through | MR-6 |
| bounds | black_market_premium | MR-4, MR-6 |
| bounds | hotelling_gap, rent_seeking_ceiling | MR-3, MR-6 |
| bounds | covered_interest_parity | MR-6 |
| bridge | premise_evidence, settle_by_arithmetic | MR-7 |
| bridge | dominance_evidence | MR-2, MR-7 |

**Handlers.** The derivation lines of the 27 handlers are in `HANDLER_RULES` (`mathpraxeo/bridge.py`). They use MR-2 to MR-6 only, and each of the five at least once. MR-7 is reserved for the CR-12 machinery. The annex pass's report shows each handler's rules beside its result.

## Verdicts restated

The verdicts of `SURVEY.md`, restated against the rules. "Admitted" gives the derivation line. "Fails at" names the step that no rule covers.

| Method | Verdict | Derivation, or where it fails |
|---|---|---|
| Equation of exchange; sectoral balances; balance of payments | Admitted | MR-2 |
| Quantity theory of money (as a theory) | Fails at: a behavioural claim (v and y do not respond to M) | Usable only as input ranges for v and y |
| Fisher relation; present value; capitalization; compounding | Admitted | MR-3 |
| Debt dynamics; stock-flow | Admitted | MR-2, MR-3 |
| Little's law; expected penalty; inflation tax; quota rent | Admitted | MR-2 |
| Supply and demand intersection; incidence | Admitted | MR-5 (with MR-4) |
| Shortage, surplus, quantity under a wedge, spending and revenue change | Admitted | MR-4 (with MR-2) |
| Tariff | Admitted | MR-2, MR-4, MR-6 |
| Cost pass-through; black-market premium; Hotelling; rent-seeking ceiling; covered interest parity | Admitted as bounds | MR-6 (with MR-3, MR-4) |
| Consumer and producer surplus; deadweight loss in money; welfare cost-benefit; compensating variation | Fails at: summing value across persons in money | No rule adds ordinal value. MR-4 counts the exchanges forgone instead |
| Utility maximization with calculus | Fails at: a cardinal or differentiable utility | CR-4 gives the directions without it |
| Production functions (Cobb-Douglas, CES) | Fails at: a functional form | Cost shares are admitted as inputs (MR-6 pass-through) |
| Perfect competition as a benchmark | Fails at: distance from a state that never obtains | MR-5 sizes tendencies from the actual position |
| Monopoly markup (Lerner) | Fails at: a known demand curve and an assumed goal (profit maximization at a point) | — |
| Oligopoly models; Nash equilibria needing common knowledge | Fails at: an assumed model of how rivals think | Dominant-strategy arguments are CR-4 already |
| Search and matching; cobweb models | Fails at: matching functions; an assumed way of forming expectations | Little's law (MR-2) gives waiting arithmetic |
| Keynesian multipliers | Fails at: a fixed spending propensity treated as a law, and spending as the source of income | Contradicts CR-8; MR-2's identities do not imply it |
| IS-LM, AD-AS, Phillips curve, Taylor rule | Fails at: aggregate behavioural relations | — |
| DSGE and CGE models | Fails at: functional forms and calibrated parameters | — |
| Input-output (Leontief) as a model | Fails at: fixed coefficients | Its cost shares are admitted as inputs |
| Growth accounting | Fails at: a production function residual | — |
| Ricardian equivalence | Fails at: a behavioural claim (people offset deficits by saving) | The debt arithmetic (MR-2, MR-3) is admitted |
| Purchasing power parity | Fails at: a long-run tendency stated as a law | Usable as an input range |
| Econometrics, forecasts, index numbers | Not methods of derivation | Sources for input ranges |
