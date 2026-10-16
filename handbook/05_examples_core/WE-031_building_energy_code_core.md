# WE-031 / Analysis: Westmere Residential Energy Performance Act (a building energy code that tightens each year)

Analyst: core-only re-run (Handbook 0.7)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Westmere Residential Energy Performance Act.** Westmere is a state of about 6 million people and about 2.4 million homes. About 40,000 new homes are permitted each year: 32,000 single-family homes and townhouses and 8,000 units in apartment buildings of three stories or fewer. The Halden metropolitan area, with about a quarter of the state's new building, straddles the line with Brennick, which has no comparable code. Manufactured homes built to the national standard are sold throughout the state. Performance is measured by the Design Energy Index (DEI): modeled annual site energy per square foot of conditioned floor area, computed from plans with state-approved software and checked on completion by a certified third-party rater. Without any code, the median DEI of new homes has fallen about 1.5% a year for ten years.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Westmere. Just outside: the Brennick side of the Halden metro area (no comparable code); manufactured homes under the national standard; buildings of four or more stories under the unchanged commercial code. | "The Halden metropolitan area ... straddles the state line with the neighboring state of Brennick, which has no comparable code." |
| Announced / enacted / effective / expires | Announced 3 February Year 0 (bill introduced with the governor's support and a sponsoring majority); enacted 15 June Year 0; first standard 1 January Year 1; tightens each 1 January to Year 10, then fixed until the legislature acts; no expiry. | "The bill was introduced on 3 February of Year 0 ... enacted on 15 June of Year 0. The first standard takes effect on 1 January of Year 1." |
| Enforcement (who, penalties, resources) | Local building departments (no permit without a DEI report; no certificate of occupancy without a rater's certificate), funded by permit fees fixed by local ordinance; State Energy Office certifies raters and audits 2% of certificates, funded by a new general-fund appropriation; builder fine up to $5,000 per home; rater decertification. Raters are hired and paid by builders. | K3. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Performance standard | `prohibition` of new homes whose DEI exceeds a maximum (the ontology has no `standard` type for a building; `product_standard` is for goods sold) | New residential buildings of three stories or fewer, including rebuilds after demolition | Builders and owners who apply for a building permit | Year 1 maximum: DEI met by 90% of the Year −2 sample (about 1.10 M0, M0 = that sample's median). Year n maximum = Year 1 × (1 − 0.04 (n − 1)); 64% of Year 1 (about 0.70 M0) in Year 10, then fixed. Size adjustment "by rule" not yet made (U1). | Renovations and alterations; additions of 50% or less of conditioned floor area; manufactured homes; buildings of four or more stories. |
| K2 Vesting | Timing rule | K1 | Permit applicants | A home must meet the standard in force on the date a complete application is filed; a permit lapses if construction has not begun within 12 months. | — |
| K3 Verification and enforcement | Enforcement | K1 | Building departments, raters, Energy Office | DEI report with the application; rater's certificate for the certificate of occupancy; 2% audits; fines; decertification; rater certification takes about six months. | — |

Existing rules (unchanged in the counterfactual): the utilities' Efficient New Homes rebate ($1,500 to the builder per home whose DEI is at least 15% below "the applicable state energy code or, where there is none, the program baseline" M0; paid from a fixed annual efficiency budget in electricity rates); local permit fees fixed by ordinance; about 70 raters rating new homes, capacity about 35,000 homes a year.

Counterfactual law: no state residential energy code; the rebate threshold stays at 0.85 M0; median DEI keeps falling about 1.5% a year (A-3).

Arithmetic on the record (used below): the rebate threshold under the Act is 0.85 × the code maximum: 0.935 M0 in Year 1, 0.898 M0 in Year 2, 0.860 M0 in Year 3 (all looser than 0.85 M0), 0.823 M0 in Year 4 (tighter), about 0.60 M0 in Year 10. Without the Act the median DEI would be about 0.96 M0 in Year 1 and about 0.83 M0 in Year 10 (1.5% a year from Year −2).

Horizons used throughout: **short** = Year 0 (from announcement) to Year 3, when the standard binds on few designs; **medium** = Years 4 to 9, when it binds on a growing share; **long** = Year 10 onward, when the maximum is fixed and the stock of homes adjusts.

Unclear provisions:
- **U1** (from the record): the size adjustment. U1-a: no adjustment beyond the per-square-foot measure. U1-b: for homes above 2,500 square feet, the maximum applies to total modeled energy as if the home were 2,500 square feet. No probabilities; one sign per reading.
- **U2** (added by this analysis; flagged): which code the rebate's "applicable state energy code" means for a vested home: U2-a, the code in force on the filing date (for a home filed in Year 0, none, so the program baseline 0.85 M0); U2-b, the code in force when the rebate is claimed at completion. The record does not say. It matters only for the timing of filings around 1 January of Year 1 (C-9, C-10).

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
|---|---|---|---|---|
| K1 Performance standard | triangular (prohibits the sale or building of a class of home between builder and buyer) | Short: on a few percent of designs (A-4); medium and long: on a growing, then large share (A-1, resting on A-3) | 1 (option "build a home with DEI above the maximum" removed, dated each 1 January); 3 (design and equipment costs attached to the option "build a home"); 2 (exempt forms stay open: renovation, small additions, manufactured, four stories) | CR-2, CR-3a, CR-4, CR-5a, CR-5c, CR-6, CR-7, CR-9, CR-10, CR-12 |
| K2 Vesting | timing rule on K1 | Yes, whenever the next step binds (A-9) | 3 (filing before each 1 January keeps the looser maximum; a 12-month start deadline attaches to it) | CR-4 (x: file after, y: file before), CR-10a, CR-12h |
| K3 Verification | triangular (requires a purchase of a rating) and binary (state spends) | Yes (A-2) | 3 (DEI report and rater's certificate attached to "get a permit" and "occupy"); 1 (occupancy removed without a certificate); 4 (general-fund money transferred to the audit unit); 3 (fine and decertification risk attached to false reports) | CR-1, CR-4 (x: comply, y: rate leniently), CR-6, CR-7, CR-8b, CR-8c |
| Rebate (existing rule, made to depend on K1) | binary (utility-rate funds given to builders) | Its threshold moves with K1 (A-19) | 3 (the payment attached to "build below the threshold" moves: looser in Years 1–3, tighter from Year 4) | CR-4, CR-5c, CR-7b, CR-8b, CR-8d |

K1 is a prohibition; its cost works through CR-1 op 3 for every home that must change design to comply. K2 changes when the prohibition applies to a given home, so it is a pure timing provision. K1 also changes who qualifies for an existing subsidy (the rebate), which is the main interaction between components.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| builders.site_built | Build the 32,000 houses and 8,000 low-rise apartment units a year | Op 1 on designs above the maximum (dated); op 3: DEI report, rater, design changes; op 3: the rebate threshold moves. |
| builders.small | Builders of fewer than 20 homes a year | Same, with a fixed cost per plan (software, training) spread over few homes (A-8). |
| builders.filing_near_a_step | Builders with homes they can file before a 1 January step and start within 12 months | Op 3 via K2: filing before the step keeps the looser maximum. |
| builders.presale_fixed_price | Builders who sold homes at a fixed price before filing | Through a `contract` relation: the price is fixed while the cost of a later step is not. |
| developers.low_rise_apartments | Build apartments of three stories or fewer | As builders.site_built; four-story reclassification needs A-26 (p 0.35, not reported). |
| buyers.new_homes | Buyers of new site-built homes in Westmere (later occupants) | Through CR-9 (exchange): prices, sizes and designs offered change; homes they would have bought may be prohibited (CR-5a). |
| buyers.new_homes.halden | New-home buyers in the Halden metro | Can buy across the line (A-13). |
| tenants.prospective | Renters of new and existing low-rise apartments | Through CR-9 (homes input_to rental service). |
| owners.buildable_lots | Owners of lots zoned for homes (specific means, A-21) | Through CR-9 (land input_to new homes) and CR-7c: expected yield changes from announcement. |
| owners.existing_homes | Owners and sellers of existing homes | Through CR-9 (substitute). Also: option "renovate instead of rebuild" left open (op 2 relative to the covered rebuild). |
| buyers.existing_homes | Buyers of existing homes | Through CR-9 (substitute): compete with buyers diverted from new homes. |
| sellers.manufactured_homes | Sellers of homes built to the national standard (exempt) | Through CR-9 (substitute). |
| builders.brennick | Builders on the Brennick side of Halden | Through CR-9 (across_border substitute). |
| raters.certified | The ~70 raters of new homes | Through CR-9 (input_to): a rating is now needed for every home (A-2). |
| raters.prospective | People in related trades (existing-home auditors) who can certify | CR-4 (x: stay, y: certify and enter). |
| buyers.existing_home_audits | Owners who buy energy audits of existing homes | Through CR-9: compete for the same auditor labor. |
| sellers.efficiency_products | Makers and installers of insulation, windows, heat pumps | Through CR-9 (input_to): more product per home. |
| input_suppliers.general_construction | Suppliers of lumber, framing, site work | Through CR-9 (input_to): fewer homes. |
| workers.residential_construction | Construction labor | Through CR-9 (input_to): fewer homes, more work per home. |
| buyers.commercial_construction | Buyers of commercial and four-story building work | Through CR-9 (same means): builders move capital and labor there (A-7). |
| officials.building_departments | Review permits; issue certificates of occupancy | Op 3: new review and checking duties; budget fixed by fee ordinance (A-10). |
| applicants.building_permits | Everyone who needs a permit from the same departments, including renovators and commercial builders | Through CR-6 (public supply at a fixed fee): share the departments' fixed review staff. |
| officials.energy_office | Certifies raters; audits; makes the U1 rule | Op 4: new appropriation; tasks. |
| taxpayers | Fund the general-fund appropriation | Op 4 (CR-8b: someone pays). |
| utilities.rebate_program | Pay the Efficient New Homes rebate | Its threshold is tied to the code (A-19). |
| electricity_customers | Fund the efficiency budget through rates; some receive other efficiency programs | Through CR-8b and CR-8d (the fixed budget). |
| utilities | Sell energy to occupants of new homes | Through CR-9 (exchange): occupants' spending changes (A-24). |

Relations followed: `exchange` (every buyer–seller pair above), `input_to` (land, ratings, efficiency products, general inputs, labor), `substitute` (existing, manufactured, Brennick homes; renovation for rebuild), `across_border` (Halden), `contract` (fixed-price presale contracts, C-27; the rebate as a standing offer), `same_market_other_segment` (other permit applicants; low-rise apartments and houses). `currency`: not followed, since all actors are within one currency area and the policy does not change trade with other countries in a way the case premises cover. `shared_facility` and `proximity`: the only links are through energy use and neighborhood effects, which are out of scope for version 1 (energy use is not analyzed, A-24). `gift`: none found.

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | builders.site_built | specification_level (modeled energy performance of new homes) | increase | short; medium; long | CR-1 op 1, CR-2, CR-4b | A-1, A-2, A-4 |
| C-2 | builders.site_built | compliance_cost | increase | short; medium; long | CR-1 op 3, CR-8c | A-2 |
| C-3 | buyers.new_homes | price_paid (new site-built homes) | ambiguous | short | CR-12b over two chains | A-2, A-4, A-6, A-19 |
| C-4 | buyers.new_homes | price_paid (new site-built homes) | increase | medium; long | CR-1 op 3, CR-6, CR-5c, CR-7b | A-1, A-5, A-6 |
| C-5 | officials.energy_office | enforcement_cost | increase | short; medium; long | CR-1 op 4, CR-8c | none |
| C-6 | officials.building_departments | enforcement_cost | increase | short; medium; long | CR-1 op 3, CR-8c | A-2 |

## 5. Responses

CR-4 applied to every pair of options each class has (substitute, quality or terms, evade, relocate, reclassify, exit, lobby, timing, entry); CR-5 and CR-6 in each market; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-7 | builders.site_built, buyers.new_homes | quantity_traded (new site-built homes in Westmere) | ambiguous | short | CR-12b | A-2, A-4, A-19 |
| C-8 | builders.site_built, buyers.new_homes | quantity_traded (new site-built homes in Westmere) | decrease | medium; long | CR-4b, CR-5a, CR-7a | A-1, A-5, A-7 |
| C-9 | builders.filing_near_a_step | quantity_traded (permit applications, 15 June to 31 December of Year 0) | U2-a: ambiguous; U2-b: increase | short (Year 0 window) | CR-10a, CR-4 (x: file in Year 1, y: file in Year 0), CR-12h | A-2, A-9, A-19 |
| C-10 | builders.filing_near_a_step | quantity_traded (permit applications, first months of Year 1) | U2-a: ambiguous; U2-b: decrease | short (Year 1 window) | CR-10a, CR-4, CR-12h | A-2, A-9, A-19 |
| C-11 | builders.filing_near_a_step | quantity_traded (permit applications, last months of each of Years 1 to 9) | increase | short; medium (each pre-step window) | CR-10a, CR-4 (x: file after the step, y: before), CR-12h | A-1, A-9 |
| C-12 | builders.filing_near_a_step | quantity_traded (permit applications, first months of each of Years 2 to 10) | decrease | short; medium (each post-step window) | CR-10a, CR-4, CR-12h | A-1, A-9 |
| C-13 | applicants.building_permits | wait_time (permit review) | increase | short | CR-6 (public supply at a fixed fee), CR-1 op 3, CR-9 | A-2, A-9, A-10 |
| C-14 | builders.site_built | wait_time (certificates of occupancy) | increase | short | CR-6, CR-9 (ratings input_to occupancy) | A-2, A-14, A-N3 |
| C-15 | raters.certified | quantity_traded (new-home ratings) | increase | short; medium; long | CR-1 op 1 and op 3, CR-9, LW-10 | A-2, A-N3 |
| C-16 | raters.certified | net_price_received (rating fees) | increase | short | CR-6, CR-7b | A-2, A-14, A-N3 |
| C-17 | raters.prospective | entry_rate | increase | short; medium | CR-4 (x: stay in present work, y: certify and enter), CR-7a | A-2, A-15, A-N3 |
| C-18 | raters.certified | asset_value (certifications and rating firms) | increase | short (from enactment) | CR-7c, CR-10c | A-2, A-14, A-N3 |
| C-19 | raters.certified, builders.site_built | legal_breach (lenient or false ratings) | increase | medium; long | CR-4 (x: build and rate to the standard, y: lenient rating), CR-5c | A-1, A-16 |
| C-20 | owners.existing_homes | reclassification (renovations and additions of 50% or less in place of rebuilds and larger additions) | increase | medium; long | CR-4 (x: covered form, y: exempt form), CR-1 op 2 | A-1, A-11 |
| C-21 | builders.small | number_of_sellers | decrease | short; medium | CR-4 (fixed costs per item; lumpy cost), CR-4b | A-2, A-8 |
| C-22 | builders.small | variety (house plans offered) | decrease | short; medium | CR-4 (fixed costs per item: x: offer the plan, y: drop it) | A-2, A-8 |
| C-23 | buyers.new_homes | unit_size (floor area of new homes near or above 2,500 sq ft) | U1-a: increase; U1-b: decrease | medium; long | CR-4c, CR-4 (x: smaller home, y: larger home) | A-1, A-N4 |
| C-24 | builders.site_built | lobbying_effort (to pause or slow the schedule; for reading U1-a) | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-10a, CR-8c | A-1, A-17 |
| C-25 | sellers.efficiency_products | lobbying_effort (to keep the schedule, extend it past Year 10; for reading U1-b) | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-8c | A-18, A-22 |
| C-26 | buyers.new_homes.halden | cross_border_purchases (new homes on the Brennick side) | increase | medium; long | CR-4 (x: buy here, y: buy there), CR-7a | A-1, A-13 |
| C-27 | builders.presale_fixed_price | tax_share_borne (relative to their buyers, on homes sold before a step and filed after it) | increase | short; medium | CR-6 (existing contracts count as regulated), CR-5c | A-1, A-N6 |
| C-28 | developers.low_rise_apartments | quantity_supplied (new rental units in buildings of three stories or fewer) | decrease | medium; long | CR-4b, CR-7a | A-1, A-5, A-23 |
| C-29 | builders.site_built | net_price_received (per new home, including the rebate) | increase | short | CR-6, CR-5c, CR-7b | A-2, A-4, A-6, A-19 |

Responses checked and not reported: evasion by building without a permit or occupying without a certificate (A-2 says departments do not issue them; no premise on unpermitted building); moving low-rise apartments to four stories (A-26, p 0.35); fines collected (needs a premise that audits detect the lenient ratings of C-19, which no case assumption states).

## 6. Second-order effects

Depth limit 4. Chains to buyers of the goods produced with commercial construction, and to employers of construction workers' households, are pruned at depth 3 as diffuse.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-30 | owners.buildable_lots | asset_value | decrease | short (from 3 February Year 0, more at enactment) | CR-7c, CR-10c, CR-9, CR-12b, CR-12e | land input_to new homes (close) | A-1, A-6, A-20, A-21, A-N5 |
| C-31 | owners.buildable_lots | tax_share_borne (relative to builders) | increase | medium; long | CR-7b | land input_to new homes (close) | A-1, A-7, A-21 |
| C-32 | owners.existing_homes | asset_value (existing homes) | increase | short (from announcement) | CR-9, CR-7c, CR-10c | existing homes substitute for new homes (partial) | A-1, A-6, A-7, A-20 |
| C-33 | buyers.existing_homes | price_substitute (existing homes) | increase | medium; long | CR-9, CR-6 | existing homes substitute for new homes (partial) | A-1, A-6, A-7 |
| C-34 | sellers.manufactured_homes | price_substitute, quantity_substitute (manufactured homes) | at_least_one_increase | medium; long | CR-9, CR-6 | manufactured homes substitute for new site-built homes (partial) | A-1, A-12 |
| C-35 | builders.brennick | price_substitute, quantity_substitute (new homes on the Brennick side of Halden) | at_least_one_increase | medium; long | CR-9, CR-6, CR-7a | across_border (close in Halden) | A-1, A-13 |
| C-36 | tenants.prospective | price_paid (rents, low-rise apartments) | increase | medium; long | CR-9, CR-6 | new low-rise units input_to rental housing; same_market_other_segment with existing units | A-1, A-5, A-23 |
| C-37 | sellers.efficiency_products | quantity_traded (efficiency products for new homes) | increase | short; medium; long | CR-9, LW-10 | efficiency products input_to new homes (close) | A-1, A-4, A-22 |
| C-38 | sellers.efficiency_products | asset_value | increase | short (from announcement) | CR-7c, CR-10c | as above | A-1, A-20, A-22 |
| C-39 | input_suppliers.general_construction | quantity_traded (lumber, framing, site work for new homes) | decrease | medium; long | CR-9, LW-10 | general inputs input_to new homes (close) | A-1, A-5, A-7 |
| C-40 | workers.residential_construction | employment | ambiguous | medium; long | CR-12b | labor input_to new homes (close) | A-1, A-7, A-22 |
| C-41 | buyers.existing_home_audits | price_paid (energy audits of existing homes) | increase | short | CR-9, CR-7a | auditor labor input_to both audits and new-home ratings (close) | A-2, A-14, A-15 |
| C-42 | utilities.rebate_program (payer); builders.site_built (recipient) | subsidy_outlay (Efficient New Homes rebate) | increase | short | CR-4, CR-8b, arithmetic on the thresholds | rebate as a standing offer (contract) | A-19, A-N1 |
| C-43 | utilities.rebate_program; builders.site_built | subsidy_outlay (Efficient New Homes rebate) | ambiguous | medium | CR-12b | as above | A-1, A-19 |
| C-44 | utilities.rebate_program; builders.site_built | subsidy_outlay (Efficient New Homes rebate) | decrease | long | CR-4, CR-8b, arithmetic on the thresholds | as above | A-3, A-19, A-N2 |
| C-45 | electricity_customers or recipients of other efficiency programs | resources_available_other_uses | at_least_one_decrease | short | CR-8b, CR-8d | efficiency budget funded in rates | A-19, A-N1 |
| C-46 | electricity_customers or recipients of other efficiency programs | resources_available_other_uses | at_least_one_increase | long | CR-8b, CR-8d | as above | A-3, A-19, A-N2 |
| C-47 | taxpayers or recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | CR-8b, CR-8a | general fund | none |
| C-48 | buyers.new_homes (occupants) | resources_available_other_uses | ambiguous | medium; long | CR-12b | exchange (home purchase); exchange (energy bought) | A-1, A-5, A-6, A-24 |
| C-49 | utilities | quantity_traded (energy sales to occupants of new homes, by value) | decrease | medium; long | CR-8b, CR-9 | exchange (energy sold to occupants) | A-1, A-24 |
| C-50 | buyers.prospective (all Westmere households) | capital_stock_target (housing stock in Westmere) | decrease | long | CR-10b, CR-8a | stock of homes built from the yearly flow | A-1, A-5, A-7 |
| C-51 | buyers.commercial_construction | price_paid (−), quantity_traded (+) (commercial and four-story building work) | at_least_one_as_stated | medium; long | CR-7a, CR-9, CR-6 | builders' capital and labor movable between segments (partial) | A-1, A-7 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| buyers.new_homes, price_paid, short | Compliance cost on every home (rating, report: A-2) and design changes on the few binding designs (A-4), passed in part (CR-6, CR-7b, A-6) | Looser rebate threshold in Years 1–3 (0.935 to 0.860 M0 against 0.85 M0): more homes earn $1,500, part passed to buyers (CR-5c, CR-7b, A-19) | None | ambiguous (C-3) |
| buyers.new_homes, price_paid, medium; long | Compliance cost on a growing share of homes (A-1, A-5); long: fewer rebates (A-N2), so less is passed to buyers | Rebate chain in the medium run has no sign of its own (C-43) | None needed in the long run (both chains +). Medium: the only signed chain is (+); see Gaps (b) | increase (C-4) |
| builders.site_built + buyers.new_homes, quantity_traded, short | Looser rebate threshold makes building qualifying homes more rewarding (CR-4, A-19) | Binding designs prohibited and compliance cost on every home (CR-4b, CR-5a, A-2, A-4) | None | ambiguous (C-7) |
| builders.site_built + buyers.new_homes, quantity_traded, medium; long | — | Standard binds on a growing share (A-1, A-5); long: fewer rebates (A-N2) | — | decrease (C-8) |
| builders.filing_near_a_step, applications in Year 0 window | Avoid K1 and K3 by filing before Year 1 (A-2, A-9) | U2-a only: a home filed in Year 0 is measured against the 0.85 M0 baseline rather than the looser 0.935 M0 Year 1 threshold, so builders of homes near the threshold wait (A-19) | None | U2-a: ambiguous; U2-b: increase (C-9); mirror for Year 1 window (C-10) |
| builders.site_built, net_price_received, short | Compliance cost passed in part (CR-6, A-6); more homes earn the rebate (A-19) | — | — | increase (C-29) |
| owners.buildable_lots, asset_value | Rebate looser in Years 1–3 raises yields for three years (A-19) | Standard binds from Year 4 for good, on every home (A-1); fewer rebates later (A-N2) | A-N5 (empirical premise, p 0.75): the permanent cost outweighs the three-year rebate gain in present value | decrease (C-30) |
| utilities.rebate_program, subsidy_outlay, medium | Compliance pushes homes down toward the threshold (CR-4) | Threshold tighter than counterfactual from Year 4; fewer homes built (C-8) | None | ambiguous (C-43) |
| workers.residential_construction, employment, medium; long | More labor per home for efficiency work (A-22) | Fewer homes (C-8, A-7) | None | ambiguous (C-40) |
| buyers.new_homes, resources_available_other_uses, medium; long | Lower energy spending each year (A-24) | Higher price kept paying through the mortgage (CR-3 note: they keep buying, so they pay more; A-6) | None | ambiguous (C-48) |
| electricity_customers group, resources_available_other_uses | short (C-45, decrease) | long (C-46, increase) | Different horizons: not combined (CR-12g) | short at_least_one_decrease; long at_least_one_increase |
| raters.certified, net_price_received | short: fixed capacity (A-14) | medium: entry (C-17) brings fees back toward cost | Different horizons; no sign claimed after the short run | increase (short) only (C-16) |

No chains cancel exactly by construction (CR-12f). Different variables are never netted (CR-12c): a higher price of new homes (C-4) and lower energy spending (C-48 chain) remain separate.

## 8. Time structure

- **Announcement (3 February to 15 June Year 0) and enactment.** The bill was expected to pass (A-20). Asset values move when the change becomes expected (CR-7c, CR-10c): buildable lots fall (C-30), existing homes rise (C-32), efficiency product makers rise (C-38), raters' certifications rise from enactment (C-18). Each is captured or borne by whoever held the asset then, partly as the probability of passage rose between February and June.
- **Rush before Year 1 and before each step (K2).** Vesting at filing makes "file before 1 January" a better option than "file after" whenever the next step binds (CR-10a; CR-4). Signed per window (CR-12h): applications rise in the months before each step and fall in the months after (C-9 to C-12); the 12-month start rule limits how far filings can be brought forward. The bunching raises permit review queues before each step (C-13) while staff is fixed (A-10, first two years). For Year 0 the sign depends on U2.
- **Growing bind.** The maximum falls 4% of the Year 1 value a year against a counterfactual 1.5% a year (A-3), so the share of homes it binds on grows from a few percent (A-4) to most by Year 10 (A-1). Consequences that depend on binding (C-8, C-20, C-26, C-28, C-34, C-35, C-36) are therefore signed from the medium horizon, and grow through it.
- **Rebate threshold path.** Looser than the counterfactual in Years 1–3, tighter from Year 4 (arithmetic in section 1). Its effects change sign across horizons (C-42 to C-46) and are kept separate (CR-12g).
- **Rater capacity.** Fixed in the short run (A-14: six-month certification); entry from related trades follows (C-17, A-15), so fees (C-16) and waits (C-14) are signed for the short run only.
- **Durability and persistence (CR-10b).** Homes last decades. The shortfall in homes built each year accumulates into a smaller housing stock (C-50), which persists even if the schedule were later paused, since homes not built are not recovered and the stock changes only through new building. Homes built to the standard keep their specification (C-1) and their occupants' lower energy spending (A-24) for their life. The fall in lot values (C-30) is a one-time capitalization: later buyers of lots pay the lower price and earn a normal return (CR-7c). The maximum stays fixed after Year 10 "until the legislature acts", so long-horizon consequences rest on A-20 continuing; lobbying on both sides (C-24, C-25) bears on whether it does.
- **U1 rulemaking.** Until the Energy Office makes the size rule, builders act under uncertainty between U1-a and U1-b; C-23 is signed per reading.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-2 | builders.site_built | compliance_cost | increase | Modeling, rating and design work that would have served other ends of builders and their buyers | CR-1 op 3, CR-8c |
| C-5 | officials.energy_office | enforcement_cost | increase | Staff and money for audits and certification | CR-1 op 4, CR-8c |
| C-6 | officials.building_departments | enforcement_cost | increase | Review time taken from other permit work (C-13) | CR-1 op 3, CR-8c |
| C-8 | builders.site_built, buyers.new_homes | quantity_traded (new site-built homes in Westmere) | decrease | Exchanges each party expected to gain from (CR-5a) | CR-5a, CR-4b |
| C-13 | applicants.building_permits | wait_time (permit review) | increase | Time of every applicant, including renovators and commercial builders | CR-6, CR-8c |
| C-24 | builders.site_built | lobbying_effort | increase | Association staff and money | CR-4, CR-8c |
| C-25 | sellers.efficiency_products | lobbying_effort | increase | Trade-group staff and money | CR-4, CR-8c |
| C-39 | input_suppliers.general_construction | quantity_traded | decrease | Sales of inputs for homes not built | CR-9, LW-10 |
| C-41 | buyers.existing_home_audits | price_paid (energy audits of existing homes) | increase | Audits of existing homes made dearer as auditors move to rating new homes | CR-9, CR-7a, CR-8a |
| C-45 | electricity_customers or recipients of other efficiency programs | resources_available_other_uses | at_least_one_decrease | Short run: the extra rebate paid from a fixed budget in rates | CR-8b, CR-8d |
| C-47 | taxpayers or recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | The audit unit's appropriation | CR-8b, CR-8a |

Both sides of every transfer (CR-8b): the rebate (payers C-45/C-46; recipients C-42 to C-44, with part passed to buyers in C-3); rater fees (builders' compliance cost C-2; raters' receipts C-15, C-16); the appropriation (taxpayers C-47; Energy Office C-5); occupants' energy spending (occupants C-48; utilities C-49); revaluations (lot owners lose at announcement, C-30, later lot buyers do not; existing-home owners gain, C-32, later buyers of existing homes pay more, C-33).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The schedule outpaces the counterfactual improvement, so that from about Year 4 a material share of the homes that would have been built would not meet the standard. | binding | 0.8 | Energy Office projections; 4% a year schedule against the 1.5% a year trend; spread of DEI in the reference sample. | These consequences fail or lose this chain: C-1 (medium; long), C-4, C-8, C-11, C-12, C-19, C-20, C-23, C-24, C-26, C-27, C-28, C-30 to C-40, C-43, C-48, C-49, C-50, C-51. |
| A-2 | Building departments do not issue permits without a DEI report, nor certificates of occupancy without a rater's certificate. | enforcement | 0.9 | K3; department procedures. | These consequences fail or lose this chain: C-1, C-2, C-3, C-6, C-7, C-9, C-10, C-13 to C-18, C-21, C-22, C-29, C-41. |
| A-3 | Without the Act, the median DEI of new homes would keep falling by about 1.5% a year (with the rebate at its program baseline). | other | 0.7 | Ten years of Energy Office data; falling heat pump prices. | A-1 rests on it; and C-44, C-46. |
| A-4 | The Year 1 standard binds on some designs (a few percent of homes). | binding | 0.7 | The 90th-percentile rule; Year −2 sample; the trend since. | These consequences fail or lose this chain: C-1 (short), C-3, C-7, C-29, C-37 (short). |
| A-5 | Once binding, the cost of meeting the standard is a material part of the cost of building a home. | other | 0.75 | Builders' cost estimates; the Energy Office's cost study. | These consequences fail or lose this chain: C-4, C-8, C-28, C-36, C-39, C-48, C-50. |
| A-6 | New-home buyers have imperfect substitutes, so they bear part of the cost and lot owners do not bear all of it. | substitutability | 0.75 | Differences between new and existing homes; share of buyers who want only new homes. | These consequences fail or lose this chain: C-3, C-4, C-29, C-30, C-32, C-33, C-48. |
| A-7 | Buyers have substitutes for new site-built homes in the state (existing homes, manufactured homes, homes across the state line), and builders can move some capital and labor to other work. | substitutability | 0.8 | Market shares; builders active in Brennick and in commercial work. | These consequences fail or lose this chain: C-8, C-31, C-32, C-33, C-39, C-40, C-50, C-51. |
| A-8 | The fixed cost of compliance per plan is material for builders of fewer than 20 homes a year. | other | 0.65 | Software and training costs; number of plans small builders use. | These consequences fail or lose this chain: C-21, C-22. |
| A-9 | Builders can file complete applications ahead of each step and start within 12 months. | expectations | 0.85 | Lot inventories; practice before earlier code changes in other states. | These consequences fail or lose this chain: C-9 to C-13. |
| A-10 | Building departments' review staff is fixed in the short run, because fees are fixed by ordinance and are not raised within two years. | revenue_use | 0.6 | Fee ordinances; council calendars. | These consequences fail or lose this chain: C-13. |
| A-11 | The renovation exemption can be used for projects that would otherwise be rebuilds or large additions. | other | 0.7 | The exemption's wording; how departments define "renovation". | These consequences fail or lose this chain: C-20. |
| A-12 | Manufactured homes are a usable substitute for some new-home buyers. | substitutability | 0.6 | Share of manufactured homes in rural new housing; zoning for them. | These consequences fail or lose this chain: C-34. |
| A-13 | Builders and buyers in the Halden metro area can move new building across the state line. | mobility | 0.6 | Commuting patterns; land on the Brennick side; builders in both states. | These consequences fail or lose this chain: C-26, C-35. |
| A-14 | Rater capacity cannot grow much within the first two years (six-month certification; about 70 active raters for new homes). | other | 0.7 | Energy Office certification records. | These consequences fail or lose this chain: C-14, C-16, C-18, C-41. |
| A-15 | Rater certification is open, and some people in related trades take it up. | alternative_uses | 0.8 | Course capacity; number of existing-home auditors. | These consequences fail or lose this chain: C-17, C-41. |
| A-16 | Lenient or false ratings occur on a meaningful scale, given that builders hire raters and 2% are audited. | enforcement | 0.55 | Audit findings in states with similar systems. | These consequences fail or lose this chain: C-19. |
| A-17 | Builders' associations can organize to lobby at a cost below their stake. | other | 0.9 | The state home builders' association; its testimony on the bill. | These consequences fail or lose this chain: C-24. |
| A-18 | Makers and installers of efficiency products can organize to lobby. | other | 0.7 | Trade groups for insulation, windows and heat pumps. | These consequences fail or lose this chain: C-25. |
| A-19 | The Utility Commission keeps the rebate rule tied to "the applicable state energy code", and the program pays all qualifying homes. | other | 0.7 | Commission orders; program budget use in recent years. | These consequences fail or lose this chain: C-3, C-4 (long, second chain), C-7, C-9 and C-10 (U2-a chain), C-29, C-42 to C-46. |
| A-20 | Buyers of homes and land expect the schedule to be carried out, not paused. | expectations | 0.7 | Legislative majorities; governor's support; history of code rollbacks elsewhere. | These consequences fail or lose this chain: C-30, C-32, C-38. |
| A-21 | Buildable lots have few uses other than new homes (zoning, services). | alternative_uses | 0.75 | Zoning maps; lots held by builders. | These consequences fail or lose this chain: C-30, C-31. |
| A-22 | Spending on efficiency products per new home rises proportionally more than the number of new homes falls. | other | 0.6 | Cost studies of each step; projected fall in building. | These consequences fail or lose this chain: C-25, C-37, C-38, C-40. |
| A-23 | Apartments of three stories or fewer are a material share of new rental units. | other | 0.6 | Permit data: 8,000 of 40,000 new homes a year. | These consequences fail or lose this chain: C-28, C-36. |
| A-24 | Occupants of a home meeting the standard spend less on energy each year than they would have in the home they would otherwise have bought (spending only; energy use is not analyzed). | other | 0.75 | Utility billing data for homes of different DEI. | These consequences fail or lose this chain: C-48, C-49. |
| A-25 | The Energy Office's audit unit is funded by a new general-fund appropriation, as K3 says, not by cuts elsewhere. | revenue_use | 0.6 | Budget bill. | No consequence fails; it decides which members of the C-47 group pay (taxpayers rather than recipients of other spending). |
| A-26 | Builders move small apartment projects to four stories to fall under the commercial code. | other | 0.35 | Height limits in local zoning. | Not reported (see below). |
| A-N1 | In Years 1–3 the rise in the share of new homes that qualify for the rebate (threshold 0.935 to 0.860 M0 instead of 0.85 M0) is larger than the fall in the number of homes built. | other | 0.7 | NEW. Year 1 threshold lies near the counterfactual median (about 0.96 M0, by A-3), so a large share of homes crosses it; the standard binds on only a few percent of homes in the short run (A-4). | These consequences fail or lose this chain: C-42, C-45. |
| A-N2 | From Year 10, fewer homes qualify for the rebate than in the counterfactual: the threshold is about 0.60 M0, while the counterfactual 0.85 M0 threshold is met by most homes (median about 0.83 M0), and builders meeting a binding maximum build close to it. | other | 0.6 | NEW. Arithmetic on the schedule and trend (A-3); builders choose the least-cost compliant design (CR-2), so few beat the code by 15% without a reason beyond the rebate. | These consequences fail or lose this chain: C-44, C-46; the long-run second chain of C-4. |
| A-N3 | Without the Act, only part of new homes would be rated (those seeking the rebate or sold on a rating); every home needs a rating under the Act. | other | 0.8 | NEW. Rater capacity about 35,000 against 40,000 permits a year; the rebate is the main reason to buy a rating without a code. | These consequences fail or lose this chain: C-14 to C-18. |
| A-N4 | Under a per-square-foot index, a larger home meets a given maximum at lower cost per square foot, because loads that do not grow with floor area (water heating, appliances) are spread over more of it. | other | 0.65 | NEW. Structure of modeled-energy software; DEI spread by home size in the reference sample. | These consequences fail or lose this chain: C-23 (U1-a sign only). |
| A-N5 | For lot owners, the expected cost of the standard from Year 4 on (permanent, on every home) outweighs the extra rebate in Years 1–3 (temporary, $1,500 on part of the homes) in present value. | other | 0.75 | NEW. Dominance premise under CR-12e: schedule to Year 10 with no expiry; rebate figures; A-5. | These consequences fail or lose this chain: C-30. |
| A-N6 | Some new homes are sold on fixed-price contracts signed before the permit application is filed, and some of those applications fall after a step. | other | 0.6 | NEW. Presale practice of production builders; the 12-month start rule limits filing ahead (A-9). | These consequences fail or lose this chain: C-27. |

**Not reported** (an assumption below 0.5, or a premise missing):
- Small apartment projects moved to four stories to fall under the commercial code (CR-4, x: covered form, y: exempt form): needs A-26 (p 0.35).
- Fines collected by the Energy Office from audited builders (CR-8b): needs a premise that the 2% audits detect lenient ratings, which no assumption states.
- Lower DEI ratings conveying information to buyers (CR-11c): needs premises on what buyers believed before and which way they move (CR-11 clarification); none is given, and buyers could already ask for ratings without the Act.

### Final check before the report

1. **Uncombined chains.** Every (class, variable, horizon) reached by more than one chain is in section 7. Opposing chains found: price_paid short (C-3), quantity_traded short (C-7), Year 0 filings under U2-a (C-9, C-10), rebate outlay medium (C-43), construction employment (C-40), occupants' resources (C-48), lot values (resolved by A-N5). The rebate chains from section 8 were checked against C-4, C-8, C-29 and C-30.
2. **Group signs.** Used where only "at least one" is licensed: substitute markets where price or quantity moves (C-34, C-35), commercial construction (C-51), budget payers (C-45 to C-47).
3. **Baseline.** Every sign is against Westmere without the Act, with the rebate at 0.85 M0 and the 1.5% trend (A-3); e.g. C-1 is "better specification than would have been built", not than in Year 0.
4. **Worse off is not poorer.** `resources_available_other_uses` is signed only for payers who cannot avoid the sum (taxpayers, ratepayers) and left ambiguous for occupants (C-48). Buyers priced out of new homes are worse off (CR-3a) but no resources sign is given for them.
5. **Timing shifts.** Filings are signed per window (C-9 to C-12); permit queues are recorded where the bunching affects waiting (C-13).
6. **Both sides of every transfer.** See the paragraph after section 9.
7. **Every class, every core rule.** For each class in section 3: CR-4 over every pair of options (substitute, quality, evade, relocate, reclassify, exit, lobby, timing, entry); CR-6 where a price or quantity is held (permit fees: C-13; rater capacity: C-14, C-16; existing contracts: C-27); CR-7 including capitalization (lots, existing homes, efficiency makers, raters: C-30, C-32, C-38, C-18; incidence: C-31); CR-9 along every relation listed in section 3; CR-8 for every use of means (C-2, C-5, C-6, C-24, C-25, C-45 to C-47); CR-10 for vesting, announcement and stock (C-9 to C-12, C-50); CR-11 checked and not used (no premise). Checked and found nothing reportable: renters of existing homes beyond low-rise apartments (no premise linking them); utilities' other sales (energy use not analyzed).
8. **Unstated premises.** Added A-N1 to A-N6 and U2; "can organize" is A-17 and A-18; "some at the margin" rests on A-1, A-4, A-7, A-11, A-12, A-13, A-15.

## 11. Report

**The policy:** From 1 January of Year 1, Westmere prohibits new homes of three stories or fewer whose modeled energy use per square foot exceeds a maximum. The maximum starts at a level 90% of recently permitted homes met and falls by 4% of that value each year to 64% of it in Year 10, then stays fixed. A home must meet the maximum in force when its complete permit application is filed, and must start within 12 months. Every new home needs a modeled energy report to get a permit and a third-party rater's certificate to be occupied. Renovations, small additions, manufactured homes and buildings of four stories or more are exempt. An existing utility rebate for homes 15% better than "the applicable code" is now measured against the new code.

**Visible consequences:** New homes are built to a higher energy specification than they would have been (C-1), at higher compliance cost to builders (C-2). From Year 4, new homes cost buyers more than they would have (C-4). The Energy Office and building departments spend more on administration (C-5, C-6).

**Invisible consequences:**
- *Builders and buyers of new homes:* Fewer new homes are built and bought from Year 4 (C-8), and the housing stock is smaller in the long run (C-50). Builders file applications in a rush before each 1 January step and hold back after it (C-11, C-12). Small builders leave or offer fewer plans (C-21, C-22). Builders with fixed-price presales bear the cost of a step that falls before filing (C-27). Fewer low-rise rental units are built and rents rise (C-28, C-36). Builders receive more per home in the first three years, including rebates (C-29).
- *Land and other homes:* Owners of buildable lots lose value from the bill's introduction (C-30) and bear more of the burden than builders (C-31). Owners of existing homes gain value (C-32); buyers of existing homes pay more (C-33). Sales of manufactured homes and of new homes on the Brennick side rise, in price or number (C-34, C-35), and Halden buyers cross the line (C-26). More owners renovate instead of rebuilding (C-20).
- *Raters:* More ratings are bought (C-15); in the first years fees rise and certificates take longer (C-16, C-14); raters' certifications gain value (C-18); new raters enter from related trades (C-17), which makes existing-home energy audits dearer (C-41). Lenient ratings become more common as the standard tightens (C-19).
- *Suppliers and workers:* Makers of efficiency products sell more and gain value (C-37, C-38); suppliers of general building inputs sell less (C-39). Commercial building work becomes cheaper or more plentiful as builders move to it (C-51).
- *Permits and budgets:* Every permit applicant, including renovators and commercial builders, waits longer for review in the first years (C-13). The rebate program pays out more in Years 1–3 and less from Year 10 (C-42, C-44), so ratepayers or other efficiency programs have less, then more (C-45, C-46). Taxpayers or recipients of other spending fund the audit unit (C-47). Utilities sell less energy by value to occupants of new homes (C-49).
- *Lobbying:* Builders lobby to slow the schedule and for the narrower size rule; efficiency product makers lobby to keep and extend it (C-24, C-25).

**Ambiguous effects:**
- New-home prices and the number of homes built in Years 1–3 (C-3, C-7): compliance costs push prices up and building down; the looser rebate threshold pushes the other way. Decided by the size of the rating cost and the few binding designs against the extra rebates.
- Filings in Year 0 (C-9, C-10): under reading U2-a the rebate baseline in Year 0 pushes some builders to wait for Year 1.
- Rebate outlay in Years 4–9 (C-43); construction employment (C-40): fewer homes against more work per home; occupants' money for other uses (C-48): higher home prices against lower energy bills.
- Floor area of large homes (C-23): larger under U1-a, smaller under U1-b.

**Key conditions:** The schedule outpaces the trend (A-1, 0.8) and compliance cost is material (A-5, 0.75): most medium- and long-run signs rest on them. Enforcement at permit and occupancy (A-2, 0.9). The rebate stays tied to the code (A-19, 0.7). Expectations that the schedule will be carried out (A-20, 0.7) drive the announcement revaluations. Lenient ratings (A-16, 0.55) are the least certain reported premise. Six premises were added (A-N1 to A-N6), and one unclear provision (U2).

**What this analysis cannot say:** How large any effect is; whether new-home prices rise or fall in the first three years; whether occupants end up with more or less to spend; whether the policy is good. Energy use, emissions, health and safety are out of scope for version 1; the analysis says nothing about whether homes use less energy, only about spending (A-24).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | builders.site_built | specification_level (modeled energy performance of new homes) | increase | short; medium; long | visible | B | CR-1 (op 1: designs above the maximum removed, from each 1 January; enforced at permit and occupancy, A-2); CR-2 (builders choose among the designs still open); CR-4b (those whose designs bind switch to compliant ones: a few in the short run, A-4; a growing share later, A-1) | A-1, A-2, A-4 |
| C-2 | builders.site_built | compliance_cost | increase | short; medium; long | visible | B | CR-1 (op 3: DEI report and rater's certificate attached to every permit and occupancy, A-2; design changes for binding homes); CR-8c (resources spent complying are used up) | A-2 |
| C-3 | buyers.new_homes | price_paid (new site-built homes) | ambiguous | short | invisible | B | CR-12b: (+) CR-1 op 3 and CR-6 (compliance cost on every home and design changes on binding ones, A-2, A-4, reduce supply at each price; part borne by buyers, CR-7b, A-6); (−) CR-5c and CR-7b (rebate threshold looser in Years 1–3 by arithmetic, A-19: more homes earn $1,500, part passed to buyers). No dominance premise | A-2, A-4, A-6, A-19 |
| C-4 | buyers.new_homes | price_paid (new site-built homes) | increase | medium; long | visible | B | CR-1 op 3 (cost of meeting a binding maximum, A-1, A-5); CR-6 (less offered at each price moves the price toward a higher clearing level); CR-5c; CR-7b (buyers have imperfect substitutes and bear part, A-6). Long: second chain, fewer rebates passed to buyers (CR-5c, A-19, A-N2) | A-1, A-5, A-6 |
| C-5 | officials.energy_office | enforcement_cost | increase | short; medium; long | visible | A | CR-1 (op 4: a new appropriation for audits and certification); CR-8c (resources spent administering and enforcing are used up) | none |
| C-6 | officials.building_departments | enforcement_cost | increase | short; medium; long | invisible | B | CR-1 (op 3: review of DEI reports and rater certificates, A-2); CR-8c | A-2 |
| C-7 | builders.site_built, buyers.new_homes | quantity_traded (new site-built homes in Westmere) | ambiguous | short | invisible | B | CR-12b: (−) CR-4b and CR-5a (binding designs prohibited, A-4; compliance cost on every home, A-2); (+) CR-4 (x: build a home that misses the rebate, y: build one that earns it; the looser threshold makes building more rewarding, A-19). No dominance premise | A-2, A-4, A-19 |
| C-8 | builders.site_built, buyers.new_homes | quantity_traded (new site-built homes in Westmere) | decrease | medium; long | invisible | B | CR-4b (buyers for whom a new home was ranked narrowly above an existing, manufactured or Brennick home switch, A-7; builders move capital to other work, CR-7a); CR-5a (exchanges that would have happened are prevented) given a material cost (A-5) on a growing share (A-1) | A-1, A-5, A-7 |
| C-9 | builders.filing_near_a_step | quantity_traded (permit applications, 15 June to 31 December of Year 0) | U2-a: ambiguous; U2-b: increase | short (Year 0 window) | invisible | B | CR-10a and CR-4 (x: file in Year 1 under K1 and K3, y: file in Year 0 and vest free of them; A-2, A-9); CR-12h (signed per window). U2-a adds an opposing chain: a Year 0 filing is measured against the 0.85 M0 baseline, tighter than the 0.935 M0 Year 1 threshold, so builders of homes between the two wait (CR-4, A-19); CR-12b | A-2, A-9, A-19 |
| C-10 | builders.filing_near_a_step | quantity_traded (permit applications, first months of Year 1) | U2-a: ambiguous; U2-b: decrease | short (Year 1 window) | invisible | B | Mirror of C-9: filings brought forward leave fewer for the months after (CR-10a, CR-4, CR-12h); U2-a adds the opposing rebate chain (CR-12b) | A-2, A-9, A-19 |
| C-11 | builders.filing_near_a_step | quantity_traded (permit applications, last months of each of Years 1 to 9) | increase | short; medium (each pre-step window) | invisible | B | CR-10a and CR-4 (x: file after 1 January under the tighter maximum, y: file before and vest; A-9, A-1); CR-12h. Under U2-a the rebate threshold also favors filing earlier, so no opposing chain | A-1, A-9 |
| C-12 | builders.filing_near_a_step | quantity_traded (permit applications, first months of each of Years 2 to 10) | decrease | short; medium (each post-step window) | invisible | B | Mirror of C-11 (CR-10a, CR-4, CR-12h) | A-1, A-9 |
| C-13 | applicants.building_permits | wait_time (permit review) | increase | short | invisible | B | CR-1 op 3 (each application now needs DEI review, A-2); CR-6 (public supply: fees fixed by ordinance and staff fixed, A-10, so added review and the pre-step bunching, A-9, are rationed by waiting); CR-9 (renovation and commercial applicants share the same staff) | A-2, A-9, A-10 |
| C-14 | builders.site_built | wait_time (certificates of occupancy) | increase | short | invisible | B | CR-9 (ratings input_to occupancy); CR-6 (demand for ratings, A-2, A-N3, exceeds the 35,000 capacity, which cannot grow quickly, A-14; where fees do not clear at once, the gap is closed by waiting) | A-2, A-14, A-N3 |
| C-15 | raters.certified | quantity_traded (new-home ratings) | increase | short; medium; long | invisible | B | CR-1 (op 1 and op 3: occupancy requires a rating, A-2); CR-9 and LW-10 (demand for ratings follows the requirement; only part of homes were rated without it, A-N3) | A-2, A-N3 |
| C-16 | raters.certified | net_price_received (rating fees) | increase | short | invisible | B | CR-6 (more demand at fixed capacity, A-14, moves fees toward a higher clearing level); CR-7b (the gain settles on the means that cannot move quickly: certified raters) | A-2, A-14, A-N3 |
| C-17 | raters.prospective | entry_rate | increase | short; medium | invisible | B | CR-4 (x: stay in present work, y: certify; y improved by higher fees and demand, C-16, A-N3); CR-7a (labor moves to the higher yield, A-15) | A-2, A-15, A-N3 |
| C-18 | raters.certified | asset_value (certifications and rating firms) | increase | short (from enactment) | invisible | B | CR-10c and CR-7c (expected higher yields, C-15, C-16, are captured by holders when they become expected; limited by expected entry, A-14) | A-2, A-14, A-N3 |
| C-19 | raters.certified, builders.site_built | legal_breach (lenient or false ratings) | increase | medium; long | invisible | B | CR-4 (x: build and rate to the standard, y: lenient rating; the cost of x rises as the standard binds, A-1, while audits cover 2%, so y gains; CR-4a: none move the other way); CR-5c (builders choose and pay raters, so the terms they accept include leniency, A-16) | A-1, A-16 |
| C-20 | owners.existing_homes | reclassification (renovations and additions of 50% or less in place of rebuilds and larger additions) | increase | medium; long | invisible | B | CR-1 op 2 (exempt forms stay open); CR-4 (x: covered rebuild or large addition, y: exempt renovation; x made worse as the standard binds, A-1, A-11) | A-1, A-11 |
| C-21 | builders.small | number_of_sellers | decrease | short; medium | invisible | B | CR-4 (fixed cost per item: software, training and modeling per plan are a lumpy cost, A-8; every small builder for whom it reverses "build here" over "other work" exits); CR-4b | A-2, A-8 |
| C-22 | builders.small | variety (house plans offered) | decrease | short; medium | invisible | B | CR-4 (fixed costs per item: x: keep offering a plan, y: drop it; each plan now needs modeling, A-2, A-8) | A-2, A-8 |
| C-23 | buyers.new_homes | unit_size (floor area of new homes near or above 2,500 sq ft) | U1-a: increase; U1-b: decrease | medium; long | invisible | B | U1-a: CR-4 (x: smaller home, y: larger home; a per-square-foot maximum is cheaper to meet per square foot in a larger home, A-N4, so y improves relative to x); U1-b: CR-4c (above 2,500 sq ft each added square foot must be met within a fixed total, so its cost rises and the last square foot, valued least, is given up); both need a binding standard (A-1) | A-1, A-N4 |
| C-24 | builders.site_built | lobbying_effort (to pause or slow the schedule; for reading U1-a) | increase | short; medium; long | invisible | B | CR-4 (x: accept the schedule, y: lobby; the stake grows as it binds, A-1, and the association can organize, A-17); CR-10a (the dated steps make lobbying before each one worth more); CR-8c | A-1, A-17 |
| C-25 | sellers.efficiency_products | lobbying_effort (to keep the schedule, extend it past Year 10; for reading U1-b) | increase | short; medium; long | invisible | B | CR-4 (x: accept, y: lobby; their sales depend on the schedule, A-22, and they can organize, A-18); CR-8c | A-18, A-22 |
| C-26 | buyers.new_homes.halden | cross_border_purchases (new homes on the Brennick side) | increase | medium; long | invisible | B | CR-4 (x: buy a new home in Westmere, y: across the line; x made dearer, A-1; CR-4a: none move the other way); CR-7a (builders move building to the yield across the line, A-13) | A-1, A-13 |
| C-27 | builders.presale_fixed_price | tax_share_borne (relative to their buyers, on homes sold before a step and filed after it) | increase | short; medium | invisible | B | CR-9 (contract relation: a fixed-price presale); CR-6 (terms fixed by existing contracts count as regulated while they last, so the cost of the step cannot be passed on); CR-5c | A-1, A-N6 |
| C-28 | developers.low_rise_apartments | quantity_supplied (new rental units in buildings of three stories or fewer) | decrease | medium; long | invisible | B | CR-4b (x: build a low-rise project here, y: other uses of the capital; x made dearer, A-1, A-5); CR-7a; material share of rental supply (A-23) | A-1, A-5, A-23 |
| C-29 | builders.site_built | net_price_received (per new home, including the rebate) | increase | short | invisible | B | CR-6 and CR-5c (compliance cost reduces supply, so the price paid rises in part, A-2, A-4, A-6); CR-7b (builders keep part of the extra rebates from the looser threshold, A-19); both chains point up (CR-12a) | A-2, A-4, A-6, A-19 |
| C-30 | owners.buildable_lots | asset_value | decrease | short (from 3 February Year 0, more at enactment) | invisible | B | CR-9 (land input_to new homes); CR-7c and CR-10c (the lower expected yield of lots, which have few other uses, A-21, and are only partly shielded by buyers, A-6, is borne by owners when the schedule becomes expected, A-20, A-1); CR-12b and CR-12e: the temporary rebate gain in Years 1–3 is outweighed by the lasting cost (A-N5) | A-1, A-6, A-20, A-21, A-N5 |
| C-31 | owners.buildable_lots | tax_share_borne (relative to builders) | increase | medium; long | invisible | B | CR-7b (lots have few other uses, A-21, while builders can move capital and labor, A-7; the side with clearly worse alternatives bears more), once the standard binds (A-1) | A-1, A-7, A-21 |
| C-32 | owners.existing_homes | asset_value (existing homes) | increase | short (from announcement) | invisible | B | CR-9 (substitute: buyers diverted from new homes, A-7, A-6); CR-7c and CR-10c (the expected rise in demand, A-1, is capitalized when it becomes expected, A-20) | A-1, A-6, A-7, A-20 |
| C-33 | buyers.existing_homes | price_substitute (existing homes) | increase | medium; long | invisible | B | CR-9 (substitute, A-7); CR-6 (more demand for a fixed stock moves the price to a higher clearing level), once the standard binds (A-1, A-6) | A-1, A-6, A-7 |
| C-34 | sellers.manufactured_homes | price_substitute, quantity_substitute (manufactured homes) | at_least_one_increase | medium; long | invisible | B | CR-4b (some buyers switch, A-12, A-1); CR-9 (substitute); CR-6 (the added demand is met by price or quantity, which one needs a premise) | A-1, A-12 |
| C-35 | builders.brennick | price_substitute, quantity_substitute (new homes on the Brennick side of Halden) | at_least_one_increase | medium; long | invisible | B | CR-9 (across_border); CR-6; CR-7a (building moves across the line, A-13, A-1) | A-1, A-13 |
| C-36 | tenants.prospective | price_paid (rents, low-rise apartments) | increase | medium; long | invisible | B | CR-9 (new low-rise units input_to rental housing; existing units same_market_other_segment); CR-6 (fewer units at each rent, C-28, move rents to a higher clearing level; A-1, A-5, A-23) | A-1, A-5, A-23 |
| C-37 | sellers.efficiency_products | quantity_traded (efficiency products for new homes) | increase | short; medium; long | invisible | B | CR-9 and LW-10 (demand for inputs follows the specification required, C-1; A-4 short, A-1 later); spending per home rises more than homes fall (A-22) | A-1, A-4, A-22 |
| C-38 | sellers.efficiency_products | asset_value | increase | short (from announcement) | invisible | B | CR-7c and CR-10c (expected higher sales, C-37, are capitalized when expected, A-20) | A-1, A-20, A-22 |
| C-39 | input_suppliers.general_construction | quantity_traded (lumber, framing, site work for new homes) | decrease | medium; long | invisible | B | CR-9 and LW-10 (demand for inputs follows the number of homes built, C-8; A-1, A-5, A-7) | A-1, A-5, A-7 |
| C-40 | workers.residential_construction | employment | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-9, LW-10 (more work per home on efficiency features, A-22); (−) CR-9, LW-10 (fewer homes, C-8, A-1, A-7). No dominance premise | A-1, A-7, A-22 |
| C-41 | buyers.existing_home_audits | price_paid (energy audits of existing homes) | increase | short | invisible | B | CR-9 (auditor labor input_to both audits and new-home ratings); CR-7a (auditors move to the higher-paid rating work, A-15, while capacity is short, A-14, A-2, so yields in audits are pulled up) | A-2, A-14, A-15 |
| C-42 | utilities.rebate_program (payer); builders.site_built (recipient) | subsidy_outlay (Efficient New Homes rebate) | increase | short | invisible | B | Arithmetic: threshold 0.935 to 0.860 M0 in Years 1–3 against 0.85 M0 (A-19); CR-4 (builders build to earn it); more qualifying homes outweigh fewer homes (A-N1); CR-8b (outlay paid by the program is received by builders) | A-19, A-N1 |
| C-43 | utilities.rebate_program; builders.site_built | subsidy_outlay (Efficient New Homes rebate) | ambiguous | medium | invisible | B | CR-12b: (+) homes pushed down toward the threshold by the binding standard (CR-4, A-1); (−) threshold tighter than 0.85 M0 from Year 4 and fewer homes (C-8). No dominance premise | A-1, A-19 |
| C-44 | utilities.rebate_program; builders.site_built | subsidy_outlay (Efficient New Homes rebate) | decrease | long | invisible | B | Arithmetic: threshold about 0.60 M0 against 0.85 M0, which most homes would meet without the Act (A-3); CR-2 (builders build close to a binding maximum); A-N2; CR-8b | A-3, A-19, A-N2 |
| C-45 | electricity_customers or recipients of other efficiency programs | resources_available_other_uses | at_least_one_decrease | short | invisible | B | CR-8b (the extra outlay, C-42, is taken from the efficiency budget in rates); CR-8d (the budget is fixed, so either other efficiency spending or ratepayers' returns are smaller) | A-19, A-N1 |
| C-46 | electricity_customers or recipients of other efficiency programs | resources_available_other_uses | at_least_one_increase | long | invisible | B | Mirror of C-45 for the lower outlay (C-44); CR-8b, CR-8d | A-3, A-19, A-N2 |
| C-47 | taxpayers or recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | invisible | A | CR-8b (the audit unit's appropriation is paid by someone); CR-8a; which members pay is decided by A-25 | none |
| C-48 | buyers.new_homes (occupants) | resources_available_other_uses | ambiguous | medium; long | invisible | B | CR-12b: (−) CR-3 note (they keep buying and pay the higher price, C-4, A-1, A-5, A-6); (+) lower energy spending each year (A-24). Different variables are not netted, but both are this variable. No dominance premise | A-1, A-5, A-6, A-24 |
| C-49 | utilities | quantity_traded (energy sales to occupants of new homes, by value) | decrease | medium; long | invisible | B | CR-8b (occupants' lower energy spending, A-24, is a lower receipt for the sellers); CR-9 (exchange) | A-1, A-24 |
| C-50 | buyers.prospective (all Westmere households) | capital_stock_target (housing stock in Westmere) | decrease | long | invisible | B | CR-10b (the stock changes only through the flow of new building, which is lower each year, C-8, and the shortfall persists); CR-8a | A-1, A-5, A-7 |
| C-51 | buyers.commercial_construction | price_paid (−), quantity_traded (+) (commercial and four-story building work) | at_least_one_as_stated | medium; long | invisible | B | CR-7a (builders move capital and labor to commercial work, A-7, as residential yields fall, A-1); CR-9; CR-6 (more offered at each price moves price down or quantity up) | A-1, A-7 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-031-C1: Rebate threshold arithmetic as a dominance premise. CR-12e lists "arithmetic on the case's figures" as a way to settle a sign, but the share of homes qualifying for the rebate under each threshold depends on the distribution of DEI, not on the case's figures alone; it needed empirical premises (A-N1, A-N2). No calculus gap, but the boundary between arithmetic and premise is not drawn by the rules.
- GAP-031-C2: Ambiguous chain feeding another consequence. C-4 (medium) combines a signed chain (+) with a chain whose own sign is ambiguous (the rebate outlay, C-43). CR-12b covers two signed chains pushing in opposite directions; it does not say whether a chain of unknown direction makes the combination ambiguous. Treated here as not opposing.

**(b) Core-rule wording that was hard to apply.**
- CR-1 op 1 vs op 3 for a performance standard: a maximum removes some designs (op 1) but its effect on most builders is a higher cost of the option "build a home" (op 3). CR-1's recording note covers multiple operations but not how to choose between them for a continuous standard.
- CR-12h and K2 vesting: the per-window signs work, but a window's sign can depend on a separate reading (U2), which the normal form handles only by per-reading signs within a window.
- CR-7b with three or more parties (lot owners, builders, buyers): A-6 says buyers bear part but gives no ranking against lot owners, so only the lot-owner/builder pair could be ranked (C-31).
- CR-11c: the rater's certificate is plainly information, but with no premise on buyers' prior beliefs it yields nothing; the rule correctly withholds a sign, but the analyst cannot record that a disclosure effect exists unsigned.
- CR-6 "public supply" clarification fit the building departments (fees fixed, staff fixed) only by analogy, since the departments are not the rule-maker of K1.

**(c) Vocabulary missing from the ontology.**
- d1: no instrument type for a building performance standard on producers (the record already notes this); `product_standard` is defined for goods sold.
- No variable for permit applications or filings as distinct from homes traded; `quantity_traded` was used with a named market.
- No variable for a seller's revenue (C-49 used `quantity_traded ... by value`).
- No actor-class or relation for a standing subsidy offer whose terms are tied to another rule (the rebate tied to "the applicable code"); recorded as `contract`.
- No field for persistence outside repeals; durability notes were put in section 8.
- No variable for the specification gap (how far homes beat the standard), which the rebate depends on (A-N2).
