# WE-031 Building energy code that tightens each year

Analyst: draft (Handbook 0.6)  |  Rule catalog version: 0.6  |  Status: awaiting expert review

A stylized policy in a fictional state. Many places have building energy codes; this one is not modeled on any of them. It is a gap-probing example. It tests a requirement that barely binds when it starts and binds more each year (TS-3; CR-1 with an operation that is nearly empty at the start), a counterfactual in which the market was already improving (`02_ontology.md`, 2.5; `06_gaps.md`, Q11), builders at the margin of compliance, the existing stock of homes as an exempt substitute (RS-16; CR-7c), an existing rebate program tied to the code, limited inspection capacity, and permits pulled before each step (RS-8). The catalog has no instrument type or pattern for a product standard, so most steps are derived from the core rules. **Energy use and environmental effects (emissions, air quality, climate) are out of scope for version 1 and are not analyzed.** Household energy bills enter only as spending, through `resources_available_other_uses`, because the vocabulary has no variable for spending on energy. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Westmere Residential Energy Performance Act.** Westmere is a state of about 6 million people with about 2.4 million homes. About 40,000 new homes are permitted each year: 32,000 single-family homes and townhouses and 8,000 units in apartment buildings of three stories or fewer. The Halden metropolitan area, with about a quarter of the state's new building, straddles the state line with the neighboring state of Brennick, which has no comparable code. Manufactured homes built to the national manufactured-housing standard are sold throughout the state.

The measure of performance is the **Design Energy Index (DEI)**: the modeled annual site energy of a home per square foot of conditioned floor area, computed from its plans with state-approved software and checked on completion by a certified third-party energy rater (an air-leakage test and a duct test). The State Energy Office's records show that the median DEI of new homes has fallen by about 1.5% a year for ten years without any state code, as heat pumps became cheaper, buyers asked for efficient homes, and the utilities' rebate program (below) paid for homes that beat its baseline.

The bill was introduced on 3 February of Year 0, with the governor's support and a majority sponsoring it. It was enacted on 15 June of Year 0. The first standard takes effect on 1 January of Year 1.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Performance standard | `prohibition` of new homes whose DEI exceeds a maximum (the ontology has no `standard` type; see Gaps found, d1) | New residential buildings of three stories or fewer above grade, including homes rebuilt after demolition | Builders and owners who apply for a building permit | Year 1 maximum: the DEI met by 90% of a sample of 2,000 homes permitted in Year −2, which the Act calls "current typical practice" (about 10% above that sample's median, M0). On 1 January of each later year the maximum falls by 4% of the Year 1 value: Year n maximum = Year 1 × (1 − 0.04 (n − 1)). In Year 10 it is 64% of the Year 1 value; it then stays fixed until the legislature acts. "The Energy Office shall by rule adjust the index for dwelling size." No such rule has been made (U1). | Renovations and alterations of existing homes. Additions that enlarge a home's conditioned floor area by 50% or less. Manufactured homes built to the national standard. Buildings of four or more stories (covered by the commercial code, unchanged). |
| K2 Vesting | Timing rule | K1 | Permit applicants | A home must meet the standard in force on the date a complete permit application is filed. A permit lapses if construction has not begun within 12 months. | — |
| K3 Verification and enforcement | Enforcement | K1 | Local building departments; certified raters; State Energy Office | A permit application must include a DEI report from approved software. A certificate of occupancy requires a rater's certificate. Raters are certified by the Energy Office (a course and exam, about six months) and are hired and paid by builders. The Energy Office audits 2% of certificates. Penalties: a builder fine of up to $5,000 per home; rater decertification. Local building departments are funded by permit fees set by local ordinance. The Energy Office's audit unit is funded by a new general-fund appropriation. | — |

Existing rules, which stay in place in the counterfactual:
- The utilities' **Efficient New Homes rebate**, set by the Utility Commission and paid from a fixed annual efficiency budget in electricity rates: $1,500 to the builder for each new home whose DEI is at least 15% below "the applicable state energy code or, where there is none, the program baseline" (M0, the median of the same Year −2 sample). In the counterfactual the threshold stays at 0.85 M0. Under the Act it becomes 15% below the code, so it is looser than the counterfactual threshold until the code falls below M0, in Year 4, and tighter after that.
- Local permit fees, fixed by ordinance; a change needs a vote of each county or city council.
- About 140 certified raters work in the state; about 70 of them rate new homes, a capacity of about 35,000 homes a year at current staffing.

Projected binding, from the Energy Office's projection of the counterfactual trend (A-3): the Year 1 maximum would be met by about 97% of the homes that would be built in Year 1 without the Act; by about three quarters in Year 4, about half in Year 6, and almost none by Year 10. The schedule tightens by about 4% of the Year 1 value a year, against a counterfactual improvement of about 1.5% a year, so the standard binds on more homes each year (TS-3).

Unclear provisions: **U1**, the size adjustment. The Act requires one but does not say what it is, and the record supports two readings. Reading U1-a: no adjustment beyond the per-square-foot measure. Builders' comments on the draft rule ask for this, and the Energy Office's first draft rule proposes it. Reading U1-b: for homes above 2,500 square feet, the maximum applies to the home's total modeled energy as if it were 2,500 square feet. The bill's sponsor described this in the floor debate as the purpose of the adjustment. Readings get no probability; C-12 reports one sign for each.

Renovation: exempt, as the Act states. That choice is the Act's, not the analyst's; the analysis follows its consequences (C-10, C-11).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1, as a ban on designs | Triangular: forbids exchanges between builders and buyers of new homes whose DEI exceeds the maximum | Barely in Year 1 (A-4: a few percent of homes); more each year; on a material share from about Year 4 (A-1) | CR-1 (op 1), CR-4, CR-5a, CR-7, TS-3, RS-1, RS-4, RS-5, RS-16, OC-4 |
| K1 and K3, as paperwork | Triangular in form; attaches a cost (modeling, rating, review) to every new home, whether or not its design changes | Yes, from Year 1, on every permit (A-2) | CR-1 (op 3), OC-2, CR-8c |
| K2 | A timing rule: makes the date of the application decide which standard applies | Yes, before each step (A-9) | RS-8, CR-10a |
| K3, enforcement | Binary: local building departments within fixed fee budgets (A-10); the Energy Office's audit unit from a new appropriation (A-25) | Yes | OC-3 (both funding cases) |
| Existing rule: rebate threshold | Binary: a payment from ratepayers' efficiency budget to builders, whose threshold the Act moves | Looser than the counterfactual threshold in Years 1 to 3, tighter from Year 4 (A-19) | CR-1 (op 3, by way of the existing rule) |

**CR-1 with an operation that is nearly empty at the start.** In Year 1, K1 removes the option of building designs that about 97% of builders would not have chosen anyway. For them, the removal changes nothing they would do (CR-3b: the option they chose is still open). It binds only for builders whose designs would have just missed the standard. But K1 and K3 attach paperwork to every permit from the first day (operation 3), and the schedule of later removals is known from the enactment. The future steps change present choices through expectations (CR-10a): land and home prices move at the enactment (C-21, C-23), and permits are pulled before each step (C-7). The table above records the operations year by year: op 3 for all builders from Year 1; op 1 for a growing share. See Gaps found, b1.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `builders` (`sellers.current`) | Home builders, from production builders to firms building a few homes a year | Every permit needs a DEI report and a rater's certificate; designs above the maximum are forbidden, for a growing share each year. |
| `builders.small` | Firms building fewer than 20 homes a year | Fixed costs of modeling, training and redesign are spread over few homes. |
| `buyers.new_homes` (`buyers.current`, `buyers.prospective`) | Buyers of new homes | The designs they would have chosen are, more and more, not built. |
| `owners.existing_homes` (`factor_owners.specific`) | Owners of the 2.4 million existing homes, which are exempt | Their homes compete with new homes that cost more. |
| `buyers.existing_homes` (`buyers.substitutes`) | Buyers of existing homes | Some new-home buyers turn to existing homes. |
| `homeowners.renovating` | Owners who would rebuild, enlarge or renovate | Renovation is exempt; rebuilding and large additions are not. |
| `owners.buildable_lots` (`factor_owners.specific`) | Owners of land zoned and serviced for new homes | Builders' expected return on new homes falls. |
| `renters` | Tenants, including in new apartments of three stories or fewer | Fewer new rental units are built. |
| `raters` (`intermediaries`) | Certified energy raters | Every new home now needs a rating. |
| `input_suppliers.efficiency` | Makers and installers of insulation, windows, heat pumps and air sealing | More of their products per new home. |
| `input_suppliers.other` | Sellers of lumber, framing, finishing and other inputs to new homes | Fewer new homes. |
| `workers.residential_construction` | People who build new homes | More work per home; fewer homes. |
| `sellers.substitutes` (manufactured homes) | Sellers of manufactured homes, which are exempt | New site-built homes cost more. |
| `neighboring_jurisdictions` | Builders and buyers on the Brennick side of the Halden metro area | No code there. |
| `applicants.permits` | Everyone who needs a permit from a local building department, including for renovations and commercial work | The same reviewers now also review DEI reports. |
| `officials.enforcement` | Local building departments and the Energy Office's audit unit | New review and audit work. |
| `taxpayers` | Funders of the Energy Office's new appropriation | Pay for audits. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `builders` | `compliance_cost` (energy modeling, rater testing, plan review of the DEI report) | increase | short to long | CR-1, OC-2, CR-8c | A-2 |
| C-2 | `builders` | `quality_per_unit` (energy specification of new homes, against the counterfactual trend) | increase | short (few homes) to long (most homes) | CR-1, CR-4, TS-3 | A-4 (short); A-1, A-3 (medium–long) |
| C-3 | `officials.enforcement` | `enforcement_cost` (DEI report review; audits) | increase | short | OC-3 | none |

The visible effects are that new homes must meet a stricter specification (C-2) and that builders bear new paperwork (C-1). Both are measured against the counterfactual, in which the specification of new homes was already improving by about 1.5% a year (A-3). A report comparing new homes in Year 5 with those in Year 0 would credit the Act with the whole improvement. The method credits it only with the part beyond the trend: almost nothing in Year 1 (A-4), and more each year as the schedule pulls ahead of the trend (A-1; TS-3).

C-1 binds at once and on every builder, including those whose designs already comply: modeling, rating and review are attached to every permit (CR-1, op 3), and the resources they use serve no other end of those who spend them (CR-8c; OC-2). It is Tier B only because it needs A-2 (permits and certificates are actually withheld without the reports).

`quality_per_unit` is the nearest variable for a mandated specification. It does not imply that buyers value the added features at their cost: buyers who would have chosen a less efficient design revealed that they ranked it higher (CR-2). See Gaps found, d2.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `buyers.new_homes` | `price_paid` (new homes) | increase | medium to long | RS-14, RS-16, CR-7b | A-1, A-5, A-6 |
| C-5 | `builders` | `quantity_supplied` (new homes, including rebuilds after demolition) | decrease | medium to long | RS-14, RS-6, CR-4 | A-1, A-5, A-7 |
| C-6 | `builders.small` | `number_of_sellers` | decrease | medium to long | CR-4, RS-6 | A-2, A-8 |
| C-7 | `builders` | `quantity_traded` (permit applications, October to December before each step) | increase | short | RS-8, CR-10a | A-9 |
| C-8 | `builders` | `quantity_traded` (permit applications, January to March after each step) | decrease | short | RS-8 | A-9 |
| C-9 | `applicants.permits` | `wait_time` (plan review, rating and certificate of occupancy) | increase | short to medium | OC-3, CR-8a, CR-6, RS-8 | A-10 or A-14; A-9 |
| C-10 | `homeowners.renovating` | `reclassification` (projects kept as exempt renovations or as additions of 50% or less) | increase | medium to long | RS-5 | A-1, A-11 |
| C-11 | `homeowners.renovating` | `quantity_substitute` (renovations and additions of existing homes) | increase | medium to long | RS-1, RS-16, CR-4 | A-1, A-11 |
| C-12 | `buyers.new_homes` | `unit_size` (floor area per new home) | U1-a: increase; U1-b: decrease | medium to long | CR-4c, CR-1 | A-1 |
| C-13 | `buyers.new_homes` | `quantity_substitute` (manufactured homes) | increase | medium to long | RS-1 | A-1, A-12 |
| C-14 | `neighboring_jurisdictions` | `quantity_supplied` (new homes on the Brennick side of the Halden metro area) | increase | medium to long | RS-4 | A-1, A-13 |
| C-15 | `builders` | `price_paid` (energy rating services) | increase | short | CR-6, CR-9 | A-14 |
| C-16 | `raters` | `entry_rate` | increase | short to medium | CR-4, CR-7a | A-15 |
| C-17 | `builders`, `raters` | `informal_activity` (homes certified as meeting the standard that do not) | increase | medium to long | RS-3 | A-1, A-16 |
| C-18 | `builders` | `lobbying_effort` (pause the schedule; U1-a size rule) | increase | short to medium | RS-7 | A-17 |
| C-19 | `input_suppliers.efficiency` | `lobbying_effort` (keep the schedule) | increase | medium | RS-7 | A-18 |
| C-20 | `builders` | `net_price_received` (utility rebates per home, Years 1 to 3) | increase | short to medium | CR-1 | A-19 |
| C-32 | `builders` | `net_price_received` (utility rebates per home, Years 4 to 10) | decrease | medium to long | CR-1 | A-19 |

**Builders at the margin of compliance.** In Year 1, the few builders whose usual designs would just miss the maximum choose the cheapest change that brings them under it: better air sealing, a larger heat pump, different windows (CR-4b: they bear the change or switch designs). Builders well under the maximum change nothing but their paperwork. Each year a new band of designs crosses the line, so in every year there is a margin of builders who first meet the standard, and the cost per home of meeting it rises as the cheapest changes are used up. Fixed costs of compliance (modeling software, training, redesigning a plan) are lumpy: by CR-4's note on lumpy costs, a builder of a few homes a year bears them over few homes, so some small builders leave new construction or are bought by larger ones (C-6, A-8). This starts with the paperwork in Year 1 and grows as redesigns are needed.

C-4 and C-5. Once the standard binds on a material share of homes (A-1), meeting it costs more per home (A-5). The cost of an input to new homes rises for every builder in the state, but new homes compete with exempt substitutes: existing homes, manufactured homes and new homes across the state line. RS-14 says the quantity effect then dominates for the builders in the state: fewer new homes are built (C-5). Fewer new homes means more buyers seek existing homes, and their price rises (RS-16; C-22). That in turn lets new-home prices rise, since new and existing homes are close substitutes. Both chains push new-home prices up (C-4). The burden is shared three ways, between buyers, builders and owners of buildable lots (CR-7b). Builders' capital and labor can move to other work, so their return is brought back into line (CR-7a), and the lasting loss settles on buyers, who have imperfect substitutes (A-6), and on lot owners, whose land has few other uses (C-23, A-21). The case supplies no premise to rank these shares, so only each side's price is signed.

C-7 and C-8 are a timing shift, recorded per window (`02_ontology.md`, 2.5; RS-8). K2 vests the standard in force on the date of a complete application, and a permit lasts 12 months, so builders file for lots they will start within a year in the last quarter before each step. Applications rise in October to December (C-7) and fall in January to March (C-8), against the counterfactual in which they are spread over the year. The shift grows each year as the gap between consecutive standards begins to bind on more homes. The bunching raises waiting at building departments and raters in the fourth quarter (C-9, one of its two chains).

C-9. Two independent chains with the same sign reach `wait_time` (CR-12d). (i) Building departments must now review DEI reports with the same staff, because fees are fixed by ordinance (A-10), and raters' capacity cannot grow quickly (A-14). Unpriced capacity is rationed by queue (CR-6). (ii) The fourth-quarter bunching (A-9) adds to the queue at the end of each year. Every applicant waits longer, including those seeking renovation and commercial permits, who are not bound by the Act at all. This is OC-3's fixed-budget case: the cost of reviewing DEI reports falls in part on other applicants (CR-8a; C-31).

C-10 and C-11. Renovation is exempt, and so are additions of 50% or less. A homeowner who would have demolished and rebuilt can instead renovate the existing structure, or rebuild in stages that each count as an addition of 50% or less (RS-5, A-11). Buyers who would have bought a new home renovate an existing one instead (RS-1, RS-16). Rebuilds after demolition fall (part of C-5) and the existing stock is kept in use longer.

C-12 depends on U1. The DEI is per square foot. Some energy loads (water heating, appliances) do not grow with floor area, so a larger home has a lower DEI for the same features. Under U1-a, adding floor area is one way to meet the standard, and the cost of the last square foot is lower relative to other ways of complying, so homes are built larger (CR-4c, applied to square feet). Under U1-b, homes above 2,500 square feet must meet a fixed total, so each square foot above that line makes compliance harder, and homes near the line are built smaller (CR-4c; CR-1, op 3 on the larger option). The text, not the analyst, decides between them.

C-13 and C-14: manufactured homes and homes across the state line are exempt substitutes (RS-1, A-12; RS-4, A-13).

C-15 and C-16. Every new home now needs a rating, against about 35,000 ratings a year of capacity among raters who rate new homes. In the first years the price of ratings rises (CR-6, CR-9; A-14), and new raters certify (CR-4, CR-7a; A-15). In the medium run, entry may bring the price back; demand stays higher than it would have been, so the medium-run price is not signed.

C-17. Raters are hired and paid by the builders whose homes they rate, and 2% of certificates are audited. A rater who passes homes that fail keeps clients; one who fails them loses clients (CR-4 for the rater: x, rate strictly; y, rate leniently). As the standard binds on more homes, the gain to builders from a lenient rating rises (RS-3; A-16, p = 0.55).

C-18 and C-19: RS-7, with each group's ability to organize stated (A-17, A-18). The schedule depends on the legislature not pausing it, and the size rule on the Energy Office's rulemaking: both are concentrated stakes in a political decision.

C-20 and C-32 follow from an existing rule that the Act moves. The rebate threshold is "15% below the applicable state energy code". In Years 1 to 3, the code is looser than the program baseline it replaces (1.10, 1.056 and 1.012 times M0), so the rebate threshold is looser than it would have been. More homes qualify, and builders receive more in rebates per home than they would have (C-20). From Year 4 the code is stricter than M0, and the threshold tightens every year, while in the counterfactual it stays fixed and more homes beat it each year as the trend continues. Builders receive less (C-32). Two horizons, two consequences; they are not combined (CR-12g). Which operation CR-1 records depends on the counterfactual law, here the program baseline that applies when there is no code. This also shows that part of the counterfactual trend (A-3) was driven by a rule the Act itself changes. A-3 is stated for the trend without the Act, with the rebate at its counterfactual threshold.

Not reported:
- Builders shifting small apartment projects to four stories, to fall under the unchanged commercial code (RS-5). Zoning limits heights in most of the state; A-26 is below the cut-off (p = 0.35).
- Permits pulled years ahead of construction: K2's 12-month lapse limits the shift to the year before each step.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-21 | `owners.existing_homes` | `asset_value` (existing homes) | increase | short (from enactment, June of Year 0) to long | CR-7c, CR-10c, RS-16 | existing and new homes: `substitute`, close | A-1, A-7, A-20 |
| C-22 | `buyers.existing_homes` | `price_substitute` (existing homes) | increase | medium to long | RS-16 | as C-21 | A-1, A-7 |
| C-23 | `owners.buildable_lots` | `asset_value` (lots zoned and serviced for new homes) | decrease | short (from enactment) to long | CR-7b, CR-7c, CR-10c | lots: `input_to` new homes | A-1, A-20, A-21 |
| C-24 | `input_suppliers.efficiency` | `quantity_demanded` (insulation, windows, heat pumps, air sealing for new homes) | increase | medium to long | CR-9, CR-12b | these products: `input_to` new homes | A-1, A-22 |
| C-25 | `input_suppliers.other` | `quantity_demanded` (lumber, framing, finishing for new homes) | decrease | medium to long | CR-9 | these inputs: `input_to` new homes | A-1, A-5, A-7 |
| C-26 | `workers.residential_construction` | `employment`, `hours_worked` | ambiguous | medium to long | CR-9, CR-12b | labor: `input_to` new homes | A-1, A-5, A-7 |
| C-27 | `renters` | `price_paid` (rents) | increase | long | RS-16, CR-9 | new and existing rental units: `same_market_other_segment`, close | A-1, A-7, A-23 |
| C-28 | `buyers.new_homes` | `resources_available_other_uses` | ambiguous | long | DM-3, CR-12b | new homes and energy: `complement` | A-1, A-24 |

C-21. Existing homes are exempt and durable, and they compete with new homes. The Act raises the cost of the new homes they compete with along a schedule known from the enactment. Existing homes' expected yield rises, as rents or as the value of living in them, for the years the steps bind, and their price rises when that becomes expected (CR-7c, CR-10c). That happens in June of Year 0, before the standard binds on almost anyone. A policy whose present operation is nearly empty thus has most of its effect on asset prices at once (A-20: the schedule is believed). Owners at the enactment gain. Later buyers pay the higher price (C-22); by CR-8b, each seller's gain is that buyer's outlay. C-23 is the mirror for buildable lots: the expected return to building on them falls, and their price falls when that becomes expected (CR-7b: the immobile factor bears part; CR-7c).

C-24: two chains reach the makers of efficiency products: more of their products per new home (+), fewer new homes (−). They push in opposite directions (CR-12b). A-22 (p = 0.6) states that spending on these products per home rises proportionally more than the number of homes falls, an empirical dominance premise (CR-12e). C-25: other inputs face only the (−) chain. C-26: work per home rises and the number of homes falls; there is no dominance premise, so the sign is ambiguous (section 7).

C-27. Apartments of three stories or fewer are covered (A-23). Fewer of them are built, and renters bid for existing units instead (RS-16 through the rental segment, CR-9). Depth 3: code, new rental units, existing rents.

C-28 is the only place household energy bills enter. A buyer of a new home that meets the standard pays more for it (C-4), once, through the price or mortgage; occupants of the home then spend less on energy each year than they would have in the home they would otherwise have bought (A-24, a premise about spending only). The two chains push the same variable in opposite directions, one as a one-time cost and one as a stream (DM-3): `ambiguous` by design. Buyers whose chosen design was still allowed are unaffected, apart from the paperwork cost passed on. Buyers whose chosen design was forbidden had revealed that they ranked it above the more efficient one at its price (CR-2), so by their own ranking they are worse off (CR-3a), whatever their later bills.

Depth. C-22, C-27 and C-28 are at depth 3. The spending of renters and buyers who pay more is not followed into named markets (CR-4, "A change in means alone"; Q19). Effects of lower energy sales on electricity rates (PC-15) are not traced: they would rest on energy use, which is out of scope.

Second-order checks:
- **RS-9 (bundled trips):** no change in where people shop. Not applicable.
- **RS-10 (informal trade):** lenient certification (C-17) happens inside the legal market, under false papers; buyers cannot tell, but RS-10's search and dispute effects are not claimed.
- **RS-11 (lock-in):** no benefit is tied to a place. Owners of existing homes gain in value, but nothing is forfeited by moving. Not applicable.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `buyers.new_homes`, `price_paid` (new homes), medium to long | Cost of meeting the standard (RS-14); existing homes dearer (RS-16, C-22). | None that reverses it. Lot owners and builders bear part, which lowers the size of the rise, not its sign. | — | **increase** (C-4). |
| `buyers.existing_homes`, `price_substitute`, medium to long | Fewer new homes (C-5); buyers turn to existing homes. | Responses to the higher price add substitutes: renovations and additions (C-11), manufactured homes (C-13), homes across the state line (C-14). | CR-12e, by logic: these responses are caused by the higher price of housing in the state. They cannot bring it below the counterfactual, or they would stop. | **increase** (C-22), and so C-21. |
| `input_suppliers.efficiency`, `quantity_demanded`, medium to long | More of these products per home. | Fewer homes (C-5). | A-22 (empirical, p = 0.6) | **increase** (C-24). If A-22 failed, ambiguous. |
| `workers.residential_construction`, `employment`, `hours_worked`, medium to long | More work per home (added features, testing). | Fewer homes (C-5). | None | **ambiguous** (C-26). Decided by how labor-intensive the added features are against how many fewer homes are built. |
| `buyers.new_homes`, `resources_available_other_uses`, long | Lower spending on energy each year (A-24). | Higher price paid once, through the purchase or mortgage (C-4). | DM-3 | **ambiguous** by design (C-28). |
| `builders`, `net_price_received` (rebates), by window | Years 1 to 3: looser threshold (C-20). | Years 4 to 10: tighter threshold (C-32). | Different horizons and windows (CR-12g) | **increase** in Years 1 to 3; **decrease** in Years 4 to 10. Not combined. |
| `builders`, `price_paid` (ratings), medium | Every home must be rated. | Entry of raters (C-16). | None | **Not reported** for the medium run; **increase** in the short run (C-15). |
| `builders`, `return_on_capital`, long | — | — | CR-7a | **Not signed.** Builders' capital and labor can move to other work, so their return is brought back into line with other uses; the lasting effect settles on lot owners and buyers (C-23, C-4). |
| `buyers.new_homes`, `unit_size`, medium to long | U1-a: compliance by adding floor area. | U1-b: a fixed total above 2,500 square feet. | — | **U1-a: increase; U1-b: decrease** (C-12). |

## 8. Time structure

- **Announcement and enactment (February to June of Year 0).** The schedule is known for all ten years. Existing homes gain value and buildable lots lose value as passage becomes likely and then certain (C-21, C-23), although the standard binds on almost no one yet.
- **Year 1.** The standard binds on about 3% of homes (A-4). The paperwork binds on all of them (C-1), and the rater bottleneck appears (C-15, C-9). New raters begin certifying (C-16). Rebates are easier to earn than they would have been (C-20). The first fourth-quarter rush, in late Year 0, is small, because the Year 1 standard binds on few homes.
- **Years 2 to 5.** Each step binds on a further band of designs. Builders at the margin redesign; small builders leave (C-6). The fourth-quarter rush and first-quarter dip grow each year (C-7, C-8). From Year 4 the code is stricter than the rebate's old baseline, and rebates fall (C-32).
- **Years 6 to 10.** The standard binds on half or more of the homes that would have been built. New-home prices and quantities move away from the counterfactual (C-4, C-5); renovation, manufactured homes and building across the state line take up part of the demand (C-11, C-13, C-14); lenient rating becomes more tempting (C-17).
- **After Year 10.** The maximum stays at its Year 10 level. The counterfactual trend keeps improving at about 1.5% a year, so the standard binds on fewer homes each year after Year 10, and would stop binding decades later (TS-3 in reverse), unless actors expect the legislature to set a new schedule (TS-2), in which case land and home prices move again when that becomes expected.
- **Durability.** Homes last 60 years or more, so the stock responds slowly (CR-10b; TS-1). A shortfall of new homes accumulates year by year; it does not reverse when the steps stop, because homes not built in Years 4 to 10 are not built later at the old cost.
- **Counterfactual.** Every sign is against Westmere without the Act, in which the median specification of new homes improves about 1.5% a year (A-3) and the rebate stays at its program baseline. Signs are never against Year 0.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-1 | `builders` | `compliance_cost` | increase | Modeling, rating and review for every new home, including the 97% of Year 1 homes whose design does not change. | OC-2, CR-8c |
| C-29 | `buyers.new_homes`, `builders` | `quantity_traded` (homes below the standard that would have been built and bought) | decrease | Exchanges that the ban forbids: both the buyer and the builder lose the gain each expected from them. | OC-4, CR-5a |
| C-30 | `taxpayers` | `resources_available_other_uses` | decrease | The Energy Office's new appropriation for audits (A-25). | OC-3, OC-1 |
| C-31 | `officials.enforcement` | `enforcement_cost` (other inspection and review work at local building departments) | decrease | With fees fixed (A-10), staff time on DEI reports is taken from other reviews and inspections; those whom that work served bear it, partly as waiting (C-9). | OC-3, CR-8a |
| C-3 | `officials.enforcement` | `enforcement_cost` (DEI review; audits) | increase | Staff time on the Act. | OC-3 |
| C-25 | `input_suppliers.other` | `quantity_demanded` | decrease | Lumber, framing and finishing for homes that are not built. | CR-9 |

Here, unlike in WE-030, OC-4 applies: the Act forbids the sale of homes above the maximum, so exchanges that both parties would have made do not happen (CR-5a). C-29 is Tier B because it rests on A-1 (that such homes would have been built).

The resources that go into the added features of compliant homes are not counted as an opportunity cost apart from C-4: the buyer pays for them in the price, and they buy something (the specification), whatever the buyer's own valuation of it.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The schedule outpaces the counterfactual improvement, so that from about Year 4 a material share of the homes that would have been built would not meet the standard. | binding | 0.8 | Energy Office projections; the 4% a year schedule against the 1.5% a year trend; spread of DEI in the reference sample. | Most medium- and long-run consequences (C-4 to C-6, C-10 to C-14, C-17, C-21 to C-29) lapse or shrink. |
| A-2 | Building departments do not issue permits without a DEI report, nor certificates of occupancy without a rater's certificate. | enforcement | 0.9 | K3; department procedures. | C-1 and C-6 weaken. |
| A-3 | Without the Act, the median DEI of new homes would keep falling by about 1.5% a year (with the rebate at its program baseline). | other | 0.7 | Ten years of Energy Office data; falling heat pump prices. | If the trend is faster, the Act binds later and less (A-1 weakens); if slower, sooner and more. |
| A-4 | The Year 1 standard binds on some designs (a few percent of homes). | binding | 0.7 | The 90th-percentile rule; Year −2 sample; the trend since. | C-2's short-run claim not reported. |
| A-5 | Once binding, the cost of meeting the standard is a material part of the cost of building a home. | other | 0.75 | Builders' cost estimates for features at each step; the Energy Office's cost study. | C-4, C-5, C-25, C-26 weaken. |
| A-6 | New-home buyers have imperfect substitutes, so they bear part of the cost and lot owners do not bear all of it. | substitutability | 0.75 | Differences between new and existing homes (age, location, layout); share of buyers who want only new homes. | C-4 not reported; C-23 grows. |
| A-7 | Buyers have substitutes for new site-built homes in the state (existing homes, manufactured homes, homes across the state line), and builders can move some capital and labor to other work. | substitutability | 0.8 | Market shares; builders active in Brennick and in commercial work. | C-5, C-21, C-22, C-25 to C-27 weaken; more of the cost falls on buyers as price. |
| A-8 | The fixed cost of compliance per plan is material for builders of fewer than 20 homes a year. | other | 0.65 | Software and training costs; number of plans small builders use. | C-6 not reported. |
| A-9 | Builders can file complete applications ahead of each step and start within 12 months. | expectations | 0.85 | Lot inventories; practice before earlier code changes in other states. | C-7, C-8 and chain (ii) of C-9 not reported. |
| A-10 | Building departments' review staff is fixed in the short run, because fees are fixed by ordinance and are not raised within two years. | revenue_use | 0.6 | Fee ordinances; council calendars. | Chain (i) of C-9 rests on A-14 alone; C-31 not reported; OC-3's first case then applies to fee payers. |
| A-11 | The renovation exemption can be used for projects that would otherwise be rebuilds or large additions. | other | 0.7 | The exemption's wording; how departments define "renovation". | C-10, C-11 not reported. |
| A-12 | Manufactured homes are a usable substitute for some new-home buyers. | substitutability | 0.6 | Share of manufactured homes in rural new housing; zoning for them. | C-13 not reported. |
| A-13 | Builders and buyers in the Halden metro area can move new building across the state line. | mobility | 0.6 | Commuting patterns; land on the Brennick side; builders operating in both states. | C-14 not reported. |
| A-14 | Rater capacity cannot grow much within the first two years (six-month certification; about 70 active raters for new homes). | other | 0.7 | Energy Office certification records. | C-15 not reported; chain (i) of C-9 rests on A-10 alone. |
| A-15 | Rater certification is open, and some people in related trades take it up. | alternative_uses | 0.8 | Course capacity; number of existing-home auditors. | C-16 not reported. |
| A-16 | Lenient or false ratings occur on a meaningful scale, given that builders hire raters and 2% are audited. | enforcement | 0.55 | Audit findings in states with similar systems. | C-17 not reported. |
| A-17 | Builders' associations can organize to lobby at a cost below their stake (RS-7's premise). | other | 0.9 | The state home builders' association; its testimony on the bill. | C-18 not reported. |
| A-18 | Makers and installers of efficiency products can organize to lobby. | other | 0.7 | Trade groups for insulation, windows and heat pumps. | C-19 not reported. |
| A-19 | The Utility Commission keeps the rebate rule tied to "the applicable state energy code", and the program pays all qualifying homes. | other | 0.7 | Commission orders; program budget use in recent years. | C-20 and C-32 not reported. |
| A-20 | Buyers of homes and land expect the schedule to be carried out, not paused. | expectations | 0.7 | Legislative majorities; governor's support; history of code rollbacks elsewhere. | C-21 and C-23 shrink (they do not reverse while the schedule has some chance of being carried out). |
| A-21 | Buildable lots have few uses other than new homes (zoning, services). | alternative_uses | 0.75 | Zoning maps; lots held by builders. | C-23 not reported; more of the cost falls on buyers. |
| A-22 | Spending on efficiency products per new home rises proportionally more than the number of new homes falls. | other | 0.6 | Cost studies of each step; projected fall in building. | C-24 becomes ambiguous. |
| A-23 | Apartments of three stories or fewer are a material share of new rental units. | other | 0.6 | Permit data: 8,000 of 40,000 new homes a year. | C-27 not reported. |
| A-24 | Occupants of a home meeting the standard spend less on energy each year than they would have in the home they would otherwise have bought. (A premise about spending only; energy use is not analyzed.) | other | 0.75 | Utility billing data for homes of different DEI. | The (+) chain in C-28 fails; C-28 becomes a decrease. |
| A-25 | The Energy Office's audit unit is funded by a new general-fund appropriation, as K3 says, not by cuts elsewhere. | revenue_use | 0.6 | Budget bill. | C-30 not reported; other Energy Office work falls instead. |
| A-26 | Builders move small apartment projects to four stories to fall under the commercial code. | other | 0.35 | Height limits in local zoning. | Below cut-off; not reported. |

**Final check before the report** (`03_workflow.md`).
1. *Uncombined chains.* Section 7 combines every class and variable reached by two chains: new and existing home prices, efficiency inputs (with A-22), construction labor (ambiguous), buyers' means (DM-3), rebates (by window), rating prices (short only). Builders' return is not signed (CR-7a).
2. *Group signs.* Construction labor is recorded as a group, ambiguous. RS-6's labor group is not claimed separately for builders.
3. *Baseline.* Every sign is against the counterfactual trend (A-3), not against Year 0. The rebate is signed against its counterfactual threshold, not against the code.
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for taxpayers (an appropriation) and, as ambiguous, for new-home buyers. Buyers whose design was forbidden are worse off by their own ranking (CR-3a), which is not signed as less money.
5. *Timing shifts.* Permit applications are signed per window (C-7, C-8). Rebates are split by window (C-20, C-32).
6. *Both sides of transfers.* Existing-home owners' gain is buyers' outlay (C-21, C-22). Rebates come from a fixed efficiency budget, so more (or less) for new-home builders means less (or more) for the program's other uses within it; those uses are not named in the record and are not signed.
7. *Every class, every core rule.* CR-7c applied to existing homes and lots (C-21, C-23); CR-6 to ratings and review capacity; enforcement costs and their funding (C-3, C-30, C-31).
8. *Unstated premises.* Lobbying (A-17, A-18), the margin for each substitute (A-7, A-11 to A-13), the trend (A-3) and the spending premise for energy bills (A-24) are in the table.

## 11. Report

**The policy.** Westmere requires new homes of up to three stories to meet a maximum modeled energy use per square foot. The first maximum, in Year 1, is met by about 90% of homes built two years earlier; it falls by 4% of that level each year for ten years. Each home needs a modeled report with its permit and a rater's test before occupancy. Renovations, small additions, manufactured homes and taller buildings are exempt.

**Visible consequences.** New homes are built to a stricter specification than they would have been: barely so in Year 1, much more so by Year 10 (C-2). Builders bear modeling, testing and review costs on every home from Year 1 (C-1). Local building departments and the Energy Office take on review and audit work (C-3).

**Invisible consequences.**
- *Buyers of new homes* pay more for them once the standard binds widely (C-4), and fewer new homes are built (C-5). Exchanges of homes below the standard that buyers and builders would have made do not happen (C-29). Buyers turn to existing homes, renovation, manufactured homes and homes across the state line in Brennick (C-11, C-13, C-14).
- *Owners of existing homes* gain in value from the enactment, before the code binds on almost anyone (C-21); later buyers of existing homes pay more (C-22). *Owners of buildable lots* lose value from the enactment (C-23). *Renters* pay more in the long run (C-27).
- *Builders* file permits in the last quarter before each step and fewer in the first quarter after (C-7, C-8). *Small builders* leave new construction (C-6). *Homeowners* shape projects to stay renovations rather than rebuilds (C-10).
- *Everyone needing a permit*, including for renovations and commercial work, waits longer (C-9), as building departments with fixed budgets spend staff time on the new reviews (C-31). Ratings cost more at first (C-15) and new raters enter (C-16). Some homes are certified that do not meet the standard (C-17).
- *Builders* receive more in utility rebates than they would have in Years 1 to 3, and less from Year 4 (C-20, C-32).
- *Makers of efficiency products* sell more for new homes (C-24); *sellers of other building inputs* sell less (C-25). Builders lobby to pause the schedule, and makers of efficiency products to keep it (C-18, C-19). Taxpayers fund the audit unit (C-30).

**Ambiguous effects.** Whether new homes are built larger or smaller depends on the size rule the Energy Office adopts (C-12: larger under U1-a, smaller under U1-b). Whether employment or hours in residential construction rise or fall (C-26). Whether buyers of code-built homes have more or less to spend on other things, once the higher price is set against lower spending on energy (C-28, DM-3).

**Key conditions.** Almost everything after Year 3 rests on the schedule pulling ahead of the improvement that would have happened anyway (A-1, p = 0.8; A-3, p = 0.7). The asset-price effects at enactment rest on the schedule being believed (A-20, p = 0.7). Waiting at building departments rests on fixed fee budgets (A-10, p = 0.6) or rater capacity (A-14, p = 0.7). The Act's size rule, not this analysis, decides C-12.

**What this analysis cannot say.** How large any effect is, including how many fewer homes are built and how the cost is split between buyers and lot owners; whether the specification buyers get is worth its cost to them; energy use and environmental effects (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | builders | compliance_cost | increase | short–long | visible | B | CR-1, OC-2, CR-8c | A-2 |
| C-2 | builders | quality_per_unit (energy specification) | increase | short–long | visible | B | CR-1, CR-4, TS-3 | A-4, A-1, A-3 |
| C-3 | officials.enforcement | enforcement_cost (DEI review, audits) | increase | short | invisible | A | OC-3 | none |
| C-4 | buyers.new_homes | price_paid (new homes) | increase | medium–long | visible | B | RS-14, RS-16, CR-7b | A-1, A-5, A-6 |
| C-5 | builders | quantity_supplied (new homes) | decrease | medium–long | invisible | B | RS-14, RS-6, CR-4 | A-1, A-5, A-7 |
| C-6 | builders.small | number_of_sellers | decrease | medium–long | invisible | B | CR-4, RS-6 | A-2, A-8 |
| C-7 | builders | quantity_traded (permit applications, Oct–Dec before each step) | increase | short | invisible | B | RS-8, CR-10a | A-9 |
| C-8 | builders | quantity_traded (permit applications, Jan–Mar after each step) | decrease | short | invisible | B | RS-8 | A-9 |
| C-9 | applicants.permits | wait_time | increase | short–medium | invisible | B | OC-3, CR-8a, CR-6, RS-8; CR-12d | A-10 or A-14; A-9 |
| C-10 | homeowners.renovating | reclassification | increase | medium–long | invisible | B | RS-5 | A-1, A-11 |
| C-11 | homeowners.renovating | quantity_substitute (renovations, additions) | increase | medium–long | invisible | B | RS-1, RS-16, CR-4 | A-1, A-11 |
| C-12 | buyers.new_homes | unit_size | U1-a: increase; U1-b: decrease | medium–long | invisible | B | CR-4c, CR-1 | A-1 |
| C-13 | buyers.new_homes | quantity_substitute (manufactured homes) | increase | medium–long | invisible | B | RS-1 | A-1, A-12 |
| C-14 | neighboring_jurisdictions | quantity_supplied (new homes, Brennick side) | increase | medium–long | invisible | B | RS-4 | A-1, A-13 |
| C-15 | builders | price_paid (energy ratings) | increase | short | invisible | B | CR-6, CR-9 | A-14 |
| C-16 | raters | entry_rate | increase | short–medium | invisible | B | CR-4, CR-7a | A-15 |
| C-17 | builders, raters | informal_activity (false certification) | increase | medium–long | invisible | B | RS-3 | A-1, A-16 |
| C-18 | builders | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-17 |
| C-19 | input_suppliers.efficiency | lobbying_effort | increase | medium | invisible | B | RS-7 | A-18 |
| C-20 | builders | net_price_received (utility rebates, Years 1–3) | increase | short–medium | invisible | B | CR-1 | A-19 |
| C-21 | owners.existing_homes | asset_value | increase | short–long | invisible | B | CR-7c, CR-10c, RS-16 | A-1, A-7, A-20 |
| C-22 | buyers.existing_homes | price_substitute (existing homes) | increase | medium–long | invisible | B | RS-16; CR-12e | A-1, A-7 |
| C-23 | owners.buildable_lots | asset_value | decrease | short–long | invisible | B | CR-7b, CR-7c, CR-10c | A-1, A-20, A-21 |
| C-24 | input_suppliers.efficiency | quantity_demanded | increase | medium–long | invisible | B | CR-9, CR-12b | A-1, A-22 |
| C-25 | input_suppliers.other | quantity_demanded | decrease | medium–long | invisible | B | CR-9 | A-1, A-5, A-7 |
| C-26 | workers.residential_construction | employment, hours_worked | ambiguous | medium–long | invisible | B | CR-9, CR-12b | A-1, A-5, A-7 |
| C-27 | renters | price_paid (rents) | increase | long | invisible | B | RS-16, CR-9 | A-1, A-7, A-23 |
| C-28 | buyers.new_homes | resources_available_other_uses | ambiguous | long | invisible | B | DM-3, CR-12b | A-1, A-24 |
| C-29 | buyers.new_homes, builders | quantity_traded (homes below the standard) | decrease | medium–long | invisible | B | OC-4, CR-5a | A-1 |
| C-30 | taxpayers | resources_available_other_uses | decrease | short | invisible | B | OC-3, OC-1 | A-25 |
| C-31 | officials.enforcement | enforcement_cost (other inspection work) | decrease | short–medium | invisible | B | OC-3, CR-8a | A-10 |
| C-32 | builders | net_price_received (utility rebates, Years 4–10) | decrease | medium–long | invisible | B | CR-1 | A-19 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from a pattern or from CR-1 to CR-12. The hardest steps (a nearly empty operation with a scheduled future one, the counterfactual trend, the existing stock as an exempt substitute) all came from CR-1, CR-4, CR-7 and CR-10.

**(b) Unclear core rules.**
1. *CR-1 and scheduled operations.* CR-1 lists what a policy does to an actor's present situation. A removal scheduled for Year 6 does nothing to a Year 1 builder's options, yet it moves land and home prices at the enactment (C-21, C-23). The move is licensed by CR-10a and CR-7c, but CR-1's "Recording" note does not say to record operations that are scheduled, with their dates, as part of the representation. Here they were recorded year by year in section 2. Proposed addition to CR-1: "Record each operation with the date from which it applies; an operation scheduled for a later date acts on present choices through expectations (CR-10a)." The note should also say that removing an option nobody would choose is an operation with no present effect on that actor (CR-3b), so that the analyst does not mistake it for a binding one.
2. *TS-3's derivation.* TS-3 is derived from CR-6: a fixed parameter binds when the clearing price moves past it. For a product standard, there is no clearing price to move. What moves is the spread of designs actors would choose, relative to the standard. Binding is then a matter of CR-1 (which actors' chosen options are removed) and CR-4 over actors with different designs. TS-3 was cited here for its conclusion; its derivation should add "or, for a standard on a good's specification, CR-1 and CR-4 over the spread of actors' choices".
3. *The counterfactual trend (`02_ontology.md`, 2.5; Q11).* The draft's default that a trend is part of the counterfactual worked here, but two points were unclear. (i) Part of the trend was driven by an existing rule (the rebate) whose threshold the Act itself moves. The trend must be projected under the counterfactual law, as 2.1 implies for existing rules, but neither 2.5 nor Q11 says so. (ii) The binding assumption (A-1) depends entirely on the projected trend (A-3), yet the assumption types have no place for a trend, and nothing says how the two should be linked when one is the premise of the other.
4. *Recurring timing windows (CR-12h; 2.5).* CR-12h covers a policy that raises an activity in every window while moving some of it. Here permits move from the first quarter to the fourth before each of ten steps, while building falls overall. Signing each window of each year would give twenty consequences. They were recorded as two consequences with recurring window qualifiers ("October to December before each step"). 2.5 should say whether that is allowed.
5. *CR-12e and dominance by logic.* As in WE-030, the existing-home price (section 7) combines a (+) chain with (−) chains that are responses to it. CR-12e lists empirical premises, accounting identities and arithmetic; "a response cannot reverse the change that causes it" fits none of them clearly.

**(c) Missing patterns.**
1. *EN-12 Minimum standard on new units of a durable good, with the existing stock exempt* (proposed). If a policy forbids the sale of new units of a durable good below a specification, and the existing stock is exempt, then: `quantity_traded` of units below the standard decreases (CR-5a); `compliance_cost` increases for all sellers of new units; `price_paid` for new units increases and `quantity_supplied` decreases once it binds; `price_substitute` and `asset_value` of existing units increase from the time the binding becomes expected; `asset_value` of factors specific to new units (land) decreases; the existing stock is kept in use longer and renovated more. Derivation: CR-1 (op 1 on designs, op 3 on paperwork), CR-4, CR-5a, CR-7b, CR-7c with CR-10c, CR-9 and RS-16. The same structure recurs for vehicle and appliance standards with exempt used goods.
2. *TS-10 Scheduled tightening* (proposed). If a standard, cap or rate tightens on a fixed, announced schedule faster than the counterfactual trend, then: it binds on more actors each year (TS-3); asset prices capitalize the whole expected path at announcement (CR-7c, CR-10c), while present operations are nearly empty; actions that vest the current standard bunch before each step (RS-8), signed per window; after the last step, the trend erodes the binding unless a new schedule is expected (TS-2). Derivation: CR-1, CR-4 over the spread of choices, CR-10a, CR-7c.
3. *RS-17 Normalized standards shift the normalizing attribute* (proposed; the ID collides with WE-030's proposal and would need renumbering). If a standard is stated per unit of an attribute the seller or buyer chooses (per square foot, per seat, per vehicle footprint), then the attribute increases among units bound by the standard, wherever adding it lowers the measured value more cheaply than other ways of complying. Derivation: CR-4c applied to the attribute (the standard lowers the relative cost of the last unit of the attribute) with CR-1. Used for C-12 under U1-a.
4. *EN-13 Verification by agents the regulated party hires* (proposed). If compliance is certified by private verifiers chosen and paid by those they verify, with audits below some rate, then lenient certification increases as the standard binds more. Derivation: CR-4 for the verifier (x: strict, y: lenient; the client relationship is part of what each option brings) with CR-1 for the audit risk. Used for C-17.

**(d) Vocabulary.**
1. *No instrument type for a standard.* 2.3 has no `standard` (a minimum specification for a good, or a performance requirement). K1 had to be recorded as a `prohibition` of designs above the maximum, which says how it works but not what it is, and points to EN patterns written for bans on whole goods. Proposed: `product_standard`, triangular, with the rule family left to the patterns proposed above.
2. *No neutral variable for a mandated specification.* `quality_per_unit` (C-2) implies that buyers value the change; for a mandated feature some buyers value it below its cost (CR-2). Proposed: `specification_level` (the level of a stated attribute per unit, without implying value).
3. *No variable for spending on a good.* The task allowed energy bills only as spending; the ontology records price and quantity separately, and energy quantity is out of scope. The only route was `resources_available_other_uses` (C-28), which merges the house price and energy spending into one ambiguous sign. Proposed: `spending` (price times quantity bought by an actor class, for a named good).
4. *No variable for the retirement of a durable stock.* That existing homes are demolished less and kept in use longer had no variable; it was folded into C-5 and C-11. Proposed: `stock_retirement_rate`.
5. *No assumption type for a counterfactual trend.* A-3 had to be typed `other`. Proposed: `counterfactual_trend`, with a required link to the binding assumptions that rest on it.
