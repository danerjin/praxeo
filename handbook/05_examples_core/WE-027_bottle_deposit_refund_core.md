# WE-027 / Analysis: Ten-cent deposit on beverage containers, refunded on return (Calder Beverage Container Recovery Act)

Analyst: core-only re-run (Handbook 0.7)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Calder Beverage Container Recovery Act.** Calder is a state of about 3.1 million people, in which about 2.2 billion covered containers are sold a year (about 700 per person). The neighboring state of Penhallow, to the east, has no deposit. About 600,000 Calder residents live in counties along the Penhallow line; four Calder towns are within 15 km of it, and Penhallow has large discount stores at two highway exits just across it. Regional bottlers and distributors serve both states from the same warehouses and print one label for the whole region. Most Calder municipalities run curbside recycling, and aluminum cans are the most valuable part of what they collect and sell.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | State of Calder. Penhallow (no deposit) to the east; its border stores are 10 to 15 minutes from the four Calder border towns. | §2 |
| Announced / enacted / effective / expires | Introduced 15 January 2027 as the governor's bill, with the majority leaders of both houses as sponsors (announced). Enacted 30 June 2027. Refund mark required on containers sold in Calder from 1 January 2028. Deposits charged and redemption begins 1 April 2028. No expiry. | §§3, 7, 11 |
| Enforcement (who, penalties, resources) | Department of Revenue (DoR): registration of distributors, monthly returns, audits of redemption points, eight investigators. Knowingly redeeming containers not sold in Calder: civil penalty of $100 per 100 containers; more than 10,000 containers in a year is a felony. DoR's administration and enforcement are paid from the Fund, up to 3% of deposits. | §§15, 16 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Deposit and refund | `deposit_refund` (2.3; the input records it as a `per_unit_tax` with a refund conditional on a later action) | Covered beverages in sealed glass, metal or plastic containers of 3 liters or less | Distributors pay 10 cents into the Beverage Container Fund on each container sold to a Calder retailer; retailers charge the buyer 10 cents a container, shown separately; any redemption point pays 10 cents for each empty bearing "CL 10¢". | 10 cents per container. | Milk and plant milks, wine, spirits, infant formula, containers over 3 liters, drinks served in open cups. |
| K2 Unredeemed deposits | Revenue rule | The Fund's balance | DoR | At each year-end, the balance after refunds, handling fees and DoR costs goes to the general fund. | None |
| K3 Handling fee | `per_unit_subsidy` | Redemption service | The Fund | 2 cents per container redeemed, paid weekly with the 10-cent refund. | None |
| K4 Return obligation | Forced exchange | Taking back empties | Retailers over 5,000 sq ft selling covered beverages | Must accept empties of the kinds and brands they sell, up to 250 containers per person per day. | Retailers with a licensed center open 40+ hours a week within one mile; smaller retailers. |
| K5 Licensed redemption centers | Permission | Operating a center | Any operator meeting site standards | $500 a year; no cap on numbers. Returned containers are picked up by the distributor that sold them, which owns and sells the material. | — |

Counterfactual law (CR-1 recording): no deposit, no refund, no fee, no return duty; empties are discarded, littered or put in curbside bins, and the material in curbside bins is collected and sold by municipal programs.

Unclear provisions:
- **U1.** Who pays if the Fund cannot cover refunds and handling fees (§14(c), §9). U1-a: distributors are assessed in proportion to containers sold. U1-b: the shortfall is met from the general fund. No probabilities.
- Not readings: whether pre-April and Penhallow containers bearing the mark are redeemed in practice. DoR has said redemption points will not be asked to tell them apart, so these are assumptions (A-9, A-10).
- Break-even of the Fund (arithmetic on the case's figures): surplus if *r* + *f* < 0.81, where *r* is the share of Calder-sold containers redeemed and *f* the containers redeemed with no deposit paid, as a share of containers sold.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Deposit and refund | binary (the Fund takes at purchase, gives at return) | Yes: charged on every covered container (A-1) | 3 (a charge attached to the option "buy a covered drink"); 3 (a payment attached to the option "return a marked empty", for anyone who holds one, including those who paid no deposit); 4 (for distributors, a sum paid per container sold, passed to retailers and buyers) | CR-3, CR-4, CR-5c, CR-6, CR-7, CR-8, CR-9, CR-10a, CR-10c, CR-11c |
| K2 Unredeemed deposits | binary (residual transfer to the state) | Yes in year 1 (A-3); no residual later if A-17 holds | 4 (means transferred from the Fund to the general fund); per reading U1-a: 4 (from distributors to the Fund), U1-b: 4 (from the general fund to the Fund) | CR-8b, CR-8d, CR-8 (residual claimants; payers from the general budget) |
| K3 Handling fee | binary (state gives) | Yes for each container redeemed (A-2) | 3 (a payment attached to the option "provide redemption service") | CR-4, CR-5c, CR-6, CR-7a |
| K4 Return obligation | triangular (forced exchange between retailers and returners) | Yes for large retailers without a nearby center (A-2, A-12) | 1 (the option "refuse empties" is removed); 3 (labor, space and fronted refunds attached to selling covered drinks; 2-cent fee attached to each return); 1 for returners above 250 a day at a store | CR-1, CR-4, CR-5b, CR-8c |
| K5 Centers and material | binary (permission with fee) and transfer of material | Yes: no cap, so the license creates no scarce asset | 2 (adds the option "operate a center"); 3 ($500 a year); 4 (material of returned containers transferred to the distributor) | CR-4, CR-7a, CR-7c, CR-8b |

CR-7c check on K5: because licenses are uncapped and cost $500, the license itself has no scarcity value and no capitalization is claimed for it.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| buyers.covered_drinks | All buyers of covered drinks in Calder | Op 3: 10-cent charge on each purchase; op 3: 10 cents on returning. Split by response (CR-1 clarification; A-6): |
| buyers.returning | Buyers who return their containers | Recover the 10 cents; spend time returning. |
| buyers.non_returning | Buyers who do not return (A-6) | Pay 10 cents per container with nothing back; the marginal ones switch to exempt drinks (A-4) or Penhallow (A-5). |
| buyers.border_counties | Calder residents near Penhallow | Penhallow purchases avoid the charge and, with A-9, can still be redeemed. |
| collectors | People who collect discarded containers | Op 3 adds a payment to collecting (A-7). |
| charities | Groups that run container drives | Through the gift relation (A-N4). |
| claimants.no_deposit | Holders of pre-April marked containers; people redeeming Penhallow containers | Op 3: 10 cents on returning a container on which no deposit was paid. |
| households.holding | Buyers of marked containers before 1 April 2028 | Op 3 from 1 April on empties they keep (A-10). |
| sellers.covered_drinks | Food service and bottlers | Can sell in exempt forms (open cups, over 3 liters). |
| retailers.calder | All Calder retailers of covered drinks | Op 3: must charge and record the deposit. |
| retailers.large | Retailers over 5,000 sq ft | Op 1 and 3 (K4); can escape K4 by a center within one mile. |
| retailers.calder_border | Retailers in the four border towns | Through CR-9 (across_border). |
| retailers.penhallow_border | Penhallow discount stores at the line | Through CR-9 (across_border; trip complements). |
| redemption_points | Centers and retailers that redeem | Op 3: 2-cent fee per container (K3). |
| redemption_centers.prospective | Would-be center operators | Op 2 (K5) and op 3 (K3, $500). |
| distributors | Registered distributors | Op 4/3: pay 10 cents per container into the Fund (passed on); registration, returns, pickup; receive material (K5). U1-a: assessment. |
| bottlers.regional | Regional bottlers with region-specific plant (A-18) | Through CR-9 (input_to covered drinks). |
| municipal_recycling_programs | Curbside programs | Through CR-9: returned containers are substitutes for curbside disposal (A-16). |
| municipal fee payers, service users, municipal taxpayers | Those who fund municipal programs | Through CR-8 (payers from a budget). |
| workers.calder_border_retail, workers.penhallow_border_retail, workers.redemption_centers | Labor in these activities | Through CR-9 (input_to). |
| beverage_container_fund | The Fund | Receives deposits; pays refunds, fees, DoR. |
| state.general_fund | residual_claimant | K2 residual; U1-b shortfall. |
| taxpayers, recipients_of_other_spending | Those whose taxes or spending the general budget sets | Through CR-8d and CR-8 (payers from the general budget). |
| officials.enforcement (DoR) | Administers and enforces | Op 4 (up to 3% of deposits); audits. |
| redeemers.non_calder_containers | Those who knowingly redeem containers not sold in Calder | Op 3: penalty risk attached to an option the Act forbids (detection low, A-9). |

## 4. Direct effect

CR-1 and CR-2: what K1 to K3 change first.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | buyers.covered_drinks | price_paid (including the deposit) | increase | short; medium; long | CR-1 op 3, CR-5c, CR-12e | A-1 |
| C-2 | buyers.non_returning | resources_available_other_uses | decrease | short; medium; long | CR-3 (note), CR-8a, CR-8b | A-1, A-19 |
| C-3 | beverage_container_fund | non_tax_receipts (deposits) | increase | short; medium; long | CR-1 op 4, CR-8b | A-1 |
| C-4 | beverage_container_fund | subsidy_outlay (refunds and handling fees) | increase | short; medium; long | CR-1 op 3, CR-8b | A-2 |
| C-5 | redemption_points | quantity_traded (redemption services) | increase | short; medium; long | CR-1 op 3, CR-4, CR-5 | A-2 |
| C-6 | state.general_fund | non_tax_receipts (K2 residual) | increase | short | CR-1 op 4, CR-8b, arithmetic | A-1, A-3 |

## 5. Responses

CR-4 for every pair of options each class has; CR-5 and CR-6 for the redemption service; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-7 | buyers.non_returning (marginal) | quantity_demanded (covered drinks bought in Calder) | decrease | short; medium; long | CR-4b, CR-4c | A-4 (chain 1); A-5 (chain 2) |
| C-8 | buyers.non_returning (marginal) | quantity_substitute (exempt drinks, tap water, fountain drinks) | increase | short; medium; long | CR-4b (x: covered drink, y: exempt alternative) | A-4 |
| C-9 | buyers.border_counties | cross_border_purchases (covered drinks in Penhallow) | increase | short; medium; long | CR-4 (x: buy in Calder, y: buy in Penhallow), CR-7a | A-5 |
| C-10 | buyers.returning | travel_time (trips to return containers) | increase | short; medium; long | CR-1 op 3, CR-4 (x: discard, y: return), CR-8c | A-2, A-6 |
| C-11 | buyers.returning, collectors | wait_time, travel_time | at_least_one_increase | short | CR-6 (fixed refund and fee; redemption capacity scarce in year 1) | A-3, A-2 |
| C-12 | collectors | earnings | increase | short; medium; long | CR-1 op 3, CR-3b, CR-4 (x: other use of time, y: collect) | A-7, A-8 |
| C-13 | collectors | hours_worked (collecting containers) | increase | short; medium; long | CR-4, CR-8a | A-7 |
| C-14 | sellers.covered_drinks | reclassification (drinks sold in open cups or containers over 3 liters) | increase | short; medium; long | CR-4 (x: covered form, y: exempt form) | A-N2 |
| C-15 | buyers.covered_drinks | quantity_traded (covered drinks, 1 January to 31 March 2028) | increase | short (Jan to Mar 2028; persistence n/a) | CR-10a, CR-4 (x: buy after 1 April with deposit, y: buy before without), CR-11c | A-10, A-11 |
| C-16 | buyers.covered_drinks | quantity_traded (covered drinks, April to June 2028) | decrease | short (Apr to Jun 2028) | CR-10a, CR-4b, CR-12a | A-11 (chain 1); A-4 (chain 2); A-5 (chain 3) |
| C-17 | households.holding | inventory_held (marked empties bought before 1 April 2028) | increase | short (Jan to Jun 2028; persistence n/a) | CR-10a, CR-11c, CR-4 (x: discard, y: keep for redemption) | A-10 |
| C-18 | retailers.calder | inventory_held (covered drinks, at 31 March 2028) | increase | short (persistence n/a) | CR-10a, CR-4 (x: buy stock after 1 April, y: before) | A-N1, A-11 |
| C-19 | distributors | compliance_cost | increase | short; medium; long | CR-1 op 3, CR-8c | A-2 |
| C-20 | retailers.calder | compliance_cost (charging, showing and remitting the deposit) | increase | short; medium; long | CR-1 op 3, CR-8c | A-1 |
| C-21 | retailers.large | compliance_cost (taking back empties, fronting refunds; gross of the 2-cent fee) | increase | short; medium; long | CR-1 op 1 and op 3, CR-5b, CR-8c | A-2 |
| C-22 | retailers.large | reclassification (use of the one-mile center exemption) | increase | medium; long | CR-4 (x: handle returns in store, y: arrange a nearby center) | A-12, A-13 |
| C-23 | redemption_centers.prospective | entry_rate | increase | short; medium | CR-1 op 2 and 3, CR-4 (x: stay out, y: enter), CR-7a | A-13, A-2 |
| C-24 | redeemers.non_calder_containers | legal_breach (redeeming containers not sold in Calder) | increase | short; medium; long | CR-1 (premises: unenforced prohibition is a risk), CR-4 (x: comply, y: violate) | A-9 |
| C-25 | officials.enforcement | enforcement_cost | increase | short; medium; long | CR-1 op 4, CR-8c | none |
| C-26 | distributors, retailers.large, redemption_centers | lobbying_effort | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-14 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Chains through `shared_facility` and `proximity` are Tier C notes below the table.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-27 | bottlers.regional | quantity_supplied (covered drinks for Calder) | decrease | short; medium; long | CR-9, LW-10 | bottling input_to covered drinks sold in Calder (close) | A-4 |
| C-28 | bottlers.regional | net_price_received | decrease | short; medium; long | CR-7b, CR-9 | as above | A-4, A-18 |
| C-29 | bottlers.regional | asset_value (region-specific plant) | decrease | short (from 2027); medium; long | CR-7c, CR-10c | as above | A-4, A-18 |
| C-30 | distributors | quantity_traded (recovered container material sold) | increase | short; medium; long | CR-1 op 4 (K5), CR-8b | returned containers substitute for curbside disposal (close) | A-2 |
| C-31 | distributors | return_on_capital | decrease | short; medium; long | CR-7b, CR-8c, CR-12e | distribution input_to covered drinks | A-N5, A-2 |
| C-32 | municipal_recycling_programs | quantity_traded (container material sold, chiefly aluminum) | decrease | short; medium; long | CR-9, CR-8b | returned containers substitute for curbside bins (close) | A-16, A-2 |
| C-33 | municipal fee payers, service users, municipal taxpayers | resources_available_other_uses | at_least_one_decrease | medium; long | CR-8b, CR-8 (payers from a budget), CR-12e | contract (residents and municipal program) | A-16, A-N3 |
| C-34 | retailers.calder | quantity_traded (covered drinks) | decrease | short; medium; long | CR-9, CR-5 | buyers of covered drinks (exchange); across_border to Penhallow | A-4 (chain 1); A-5 (chain 2) |
| C-35 | retailers.calder_border | quantity_traded (other groceries bought on the same trip) | decrease | short; medium; long | CR-9 | complement (trip) | A-5, A-15 |
| C-36 | retailers.penhallow_border | quantity_traded (covered drinks) | increase | short; medium; long | CR-9, CR-5 | across_border (close within 15 minutes) | A-5 |
| C-37 | retailers.penhallow_border | quantity_traded (other groceries bought on the same trip) | increase | short; medium; long | CR-9 | complement (trip) | A-5, A-15 |
| C-38 | workers.calder_border_retail | employment, hours_worked | at_least_one_decrease | short; medium | CR-9, LW-10 | labor input_to border retail | A-5, A-20 |
| C-39 | workers.penhallow_border_retail | employment, hours_worked | at_least_one_increase | short; medium | CR-9, LW-10 | labor input_to border retail | A-5, A-20 |
| C-40 | retailers.calder_border | asset_value (border-town store sites) | decrease | short (from 2027); medium; long | CR-7c, CR-10c | across_border | A-5 |
| C-41 | retailers.penhallow_border | asset_value (border store sites) | increase | short (from 2027); medium; long | CR-7c, CR-10c | across_border | A-5 |
| C-42 | claimants.no_deposit | resources_available_other_uses | increase | short; medium; long | CR-8b, CR-1 op 3 | across_border (Penhallow containers); same good earlier in time | A-10 (chain 1); A-9 (chain 2) |
| C-43 | beverage_container_fund | fund_balance (year-end, before transfer) | increase | short | CR-8b, arithmetic | - | A-1, A-3 |
| C-44 | beverage_container_fund | fund_balance (before the shortfall is met) | decrease | medium; long | CR-8b, arithmetic | - | A-17 |
| C-45 | state.general_fund | subsidy_outlay (meeting the Fund's shortfall) | U1-a: no_change; U1-b: increase | medium; long | CR-8b | - | A-17 |
| C-46 | taxpayers, recipients_of_other_spending | resources_available_other_uses | at_least_one_increase | short | CR-8b, CR-8d | - | A-1, A-3 |
| C-47 | taxpayers, recipients_of_other_spending | resources_available_other_uses | U1-a: no_change; U1-b: at_least_one_decrease | medium; long | CR-8b, CR-8 (payers from the general budget) | - | A-17 |
| C-48 | distributors | resources_available_other_uses | U1-a: decrease; U1-b: no_change | medium; long | CR-8b, CR-3c | - | A-17 |
| C-49 | buyers.covered_drinks | price_paid (shelf price excluding the deposit) | ambiguous | short; medium; long | CR-12b over chains below | distribution and bottling input_to covered drinks | A-N5, A-4, A-18 |
| C-50 | charities | resources_available_other_uses | increase | short; medium; long | CR-5 (gift), CR-8b | gift (buyers to charities) | A-N4 |
| C-51 | workers.redemption_centers | employment | increase | medium; long | CR-9, LW-10, CR-7a | labor input_to redemption service | A-13, A-2 |

Notes on relations followed:
- **Exchange**: buyers–retailers–distributors–bottlers (C-27 to C-31, C-34); returners–redemption points (C-5); material from redemption points to distributors (C-30).
- **Across border / trip complement**: C-9, C-35 to C-41.
- **Contract**: large retailers and center operators (C-22: a center near the store under a site or service agreement); residents and municipal programs (C-33). Distributors' supply contracts with retailers fix terms only while they last (CR-6 clarification); not signed separately.
- **Gift**: buyers give empties to charities (C-50).
- **Currency**: not applicable; Calder and Penhallow share a currency, so no exchange-rate link follows.
- **Shared facility (Tier C, not reported)**: collectors take containers from public bins and curbside bins set out by others; this changes what is left for municipal collection (same direction as C-32).
- **Proximity (Tier C, not reported)**: centers near large stores bring traffic and noise to neighbors; litter falls. These are safety or environmental effects with no variable in 2.4 and are out of scope.
- **Pruned**: further effects of lower bottler output on their suppliers and workers (depth 4, diffuse); further effects of the general fund's surplus on named spending (CR-4 "change in means alone": which uses needs a premise).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
| --- | --- | --- | --- | --- |
| buyers.covered_drinks, price_paid including deposit, all | 10-cent charge (CR-1 op 3); distributors' and retailers' added costs passed on in part (CR-7b, A-N5) | lower demand lowers the shelf price where plant is specific (CR-7b, A-18) | CR-12e: the fall in the shelf price is caused by the charge and cannot exceed it, since demand stops falling once the full price is back at its old level; also arithmetic (material receipts per container are a fraction of 10 cents) | increase (C-1) |
| buyers.covered_drinks, price_paid shelf price excluding deposit, all | net per-container cost to distributors and large retailers (A-N5), U1-a assessment (A-17) | lower demand with specific plant (A-4, A-18) | None stated | ambiguous (C-49) |
| bottlers.regional, net_price_received | - | lower demand (A-4, A-18); distributors' net cost passed back in part (A-N5) | Not needed: same direction | decrease (C-28) |
| distributors, return_on_capital | material receipts (C-30) | compliance and pickup costs (C-19); lower volume (C-34); U1-a assessment | A-N5 (empirical premise, CR-12e): costs at least as large as material receipts | decrease (C-31) |
| municipal programs' budget | lower collection and sorting volume saves some cost | lost material receipts (C-32) | A-N3 (empirical premise, CR-12e): the lost material earned more than its marginal handling cost | at_least_one_decrease for the group (C-33) |
| buyers.covered_drinks, quantity_traded, by window | Jan to Mar 2028: purchases brought forward (C-15) | Apr to Jun 2028: stocks drawn down and deposit (C-16); later: deposit (C-7) | Windows signed separately (CR-12h) | increase (Jan to Mar); decrease (Apr to Jun and after) |
| beverage_container_fund, fund_balance | short: r + f below 0.81 (A-3) | medium/long: r + f above 0.81 (A-17) | Different horizons not combined (CR-12g) | increase (short, C-43); decrease (medium; long, C-44) |
| taxpayers, resources_available_other_uses | short: residual received (C-46) | medium/long, U1-b: shortfall paid (C-47) | Different horizons | at_least_one_increase (short); per reading (medium; long) |
| retailers.large | 2-cent fee received (C-5) | handling costs (C-21) | Different variables, not netted (CR-12c) | separate consequences |
| retailers.calder, quantity_traded covered drinks | Jan to Mar 2028 forward buying (C-15, C-18) | substitution and cross-border (C-34) | Different windows | decrease outside Jan to Mar 2028 (C-34) |
| cross_border_purchases | non-returners avoid the charge (A-5); returners can buy without deposit and redeem (A-5, A-9) | - | Same direction | increase (C-9) |

CR-12f: no pair of provisions cancels exactly. The refund on containers with no deposit paid (f) is not an exact offset to anything; it is a transfer from the Fund to claimants (C-42), and C-4 and C-44 include it.

## 8. Time structure

- **Announcement (15 January 2027) and enactment (30 June 2027).** As passage becomes more likely, the expected lower yield on region-specific bottling plant (C-29) and on Calder border-town store sites (C-40), and the higher yield on Penhallow border sites (C-41), are capitalized, partly from January and fully from June 2027 (CR-7c, CR-10c). These losses and gains fall on those who own the assets then. Persistence: lasting while the Act stands.
- **Marked but no deposit (1 January to 31 March 2028).** Containers carry the mark from January but no deposit is charged until April; from April any marked container is redeemable (A-10; DoR's statement conveys this, CR-11c). Buyers bring purchases forward into the window (C-15) and keep the empties (C-17); retailers stock up before 1 April if they must charge the deposit on stock they bought without paying it (C-18, A-N1). Each window is signed against the counterfactual: purchases up in January to March, down in April to June (C-16). Persistence n/a: the window exists only at the transition. These redemptions are part of *f* and raise the Fund's year-1 outlays (C-4, C-42).
- **Year 1 (from 1 April 2028).** Redemption points are few (A-3): queues and travel for returners rise (C-11); r + f stays below 0.81, so the Fund has a surplus that goes to the general fund (C-6, C-43, C-46).
- **Medium and long run.** Centers enter (C-23, C-51) and large retailers move returns to nearby centers (C-22). Redemption rises; with Penhallow claims (A-9), r + f exceeds 0.81 (A-17) and the Fund runs short (C-44). Who pays depends on U1 (C-45, C-47, C-48). The surplus of year 1 and the shortfall later are separate consequences (CR-12g).
- **Durability.** Bottling plant is a durable stock specific to the region (A-18; CR-10b): output falls gradually, and the capital loss is borne at announcement (C-29). Curbside routes and equipment are fixed in the short run, which is why their cost does not fall with lost material (A-N3).
- **No expiry.** No end-date rush or post-program dip applies.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-2 | buyers.non_returning | resources_available_other_uses | decrease | Purchases forgone by those who keep buying and forfeit 10 cents a container | CR-3 (note), CR-8a, CR-8b |
| C-10 | buyers.returning | travel_time (trips to return containers) | increase | Time used to recover the deposit | CR-8c |
| C-11 | buyers.returning, collectors | wait_time, travel_time | at_least_one_increase | Time queuing or traveling to scarce redemption points in year 1 | CR-6, CR-8c |
| C-13 | collectors | hours_worked (collecting containers) | increase | Leisure, volunteering or lower-paid work given up (A-8) | CR-8a |
| C-19 | distributors | compliance_cost | increase | Registration, monthly returns, relabeling, pickup from redemption points | CR-8c |
| C-20 | retailers.calder | compliance_cost | increase | Till changes, receipts, remitting deposits | CR-8c |
| C-21 | retailers.large | compliance_cost | increase | Floor space, labor and working capital for returns | CR-8c |
| C-25 | officials.enforcement | enforcement_cost | increase | Up to 3% of deposits that would otherwise go to the general fund or reduce a shortfall | CR-8c |
| C-26 | distributors, retailers.large, redemption_centers | lobbying_effort | increase | Staff time and money spent on U1, the fee and the exemptions | CR-8c |
| C-27 | bottlers.regional | quantity_supplied | decrease | Drinks that buyers no longer buy in covered form | CR-8a |
| C-33 | municipal fee payers, service users, municipal taxpayers | resources_available_other_uses | at_least_one_decrease | Material receipts that had paid part of curbside service | CR-8b |
| C-38 | workers.calder_border_retail | employment, hours_worked | at_least_one_decrease | Work in Calder border stores | CR-9 |

CR-8b both sides: deposits paid by buyers (C-1, C-2) are received by the Fund (C-3); the Fund's refunds and fees (C-4) are received by returners, collectors, charities, no-deposit claimants (C-12, C-50, C-42) and redemption points (C-5); the residual goes to the general fund (C-6, C-46) or, later, a shortfall is paid by distributors or taxpayers (C-47, C-48); material moves from municipal programs (C-32) to distributors (C-30); DoR's costs are used up (C-25).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Retailers charge the deposit as required. | enforcement | 0.95 | It is shown on the receipt; distributors charge it to retailers. | C-1, C-2, C-3, C-6, C-20, C-43, C-46 fail. |
| A-2 | Some containers are returned by their buyers. | other | 0.95 | Return rates under deposits elsewhere; multipacks for home use. | C-4, C-5, C-10, C-11, C-19, C-21, C-23, C-30, C-31, C-32, C-51 fail. |
| A-3 | In the first year, redemption points are few and routines new, so r + f is below 0.81. | expectations | 0.75 | Time to license and open centers; start date. | C-6, C-11, C-43, C-46 fail. |
| A-4 | Buyers have exempt or untaxed alternatives they find acceptable. | substitutability | 0.85 | Exemption list. | C-8, C-27, C-28, C-29, C-49 fail; C-7, C-16, C-34 lose a chain. |
| A-5 | Enough border residents can shop in Penhallow, and some non-returners find 10 cents a container worth the trip. | mobility | 0.65 | 600,000 border-county residents; stores 10 to 15 minutes away; $2.40 on a 24-pack. | C-9, C-35 to C-41 fail; C-7, C-16, C-34 lose a chain. |
| A-6 | Buyers differ in what it costs them to return a container. | other | 0.95 | Consumption away from home; locations of redemption points. | C-10 fails; the split into returners and non-returners fails. |
| A-7 | Some buyers discard containers that others collect and redeem. | other | 0.95 | Collection elsewhere; public bins and events. | C-12, C-13 fail. |
| A-8 | For most collectors, the time spent collecting would otherwise have earned less money. | alternative_uses | 0.7 | Collectors elsewhere are mostly people with little paid work, and volunteers. | C-12 fails. |
| A-9 | Most Penhallow containers carry the Calder mark, redemption points cannot tell them apart, and detection is low enough that some people bring them in. | enforcement | 0.75 | Shared labels; DoR's statement; eight investigators. | C-24 fails; C-42 loses a chain. |
| A-10 | People learn that marked containers bought before April will be redeemable, and some hold them. | expectations | 0.7 | DoR's statement; press coverage. | C-15, C-17 fail; C-42 loses a chain. |
| A-11 | Covered drinks are storable, and some buyers can bring purchases forward by weeks. | other | 0.75 | Shelf life. | C-15, C-18 fail; C-16 loses a chain. |
| A-12 | For some large stores, arranging for a nearby center costs less than handling returns in the store. | other | 0.65 | Space and labor for returns; operators' interest in sites near large stores. | C-22 fails. |
| A-13 | At some sites, the 2-cent fee and volume cover a center's costs. | alternative_uses | 0.8 | Center costs elsewhere. | C-22, C-23, C-51 fail. |
| A-14 | Distributors, large retailers and center operators can organize at a cost below their stakes. | other | 0.8 | Existing associations; few distributors. | C-26 fails. |
| A-15 | Shoppers bundle drink purchases with other groceries. | other | 0.7 | Basket data. | C-35, C-37 fail. |
| A-16 | Many returned and collected containers would otherwise have gone into curbside bins. | other | 0.85 | Curbside participation. | C-32, C-33 fail. |
| A-17 | Once redemption points are established, r + f exceeds 0.81, so the Fund needs the shortfall rule. | other | 0.55 | 75% to 90% redemption elsewhere, plus no-deposit claims. | C-44, C-45, C-47, C-48 fail; the Fund keeps a surplus. |
| A-18 | Regional bottlers have plant specific to the region and sell mostly in Calder. | durability | 0.6 | Plant locations; sales shares. | C-28, C-29, C-49 fail. |
| A-19 | Most non-returning buyers keep buying covered drinks. | other | 0.9 | Consumption of covered drinks. | C-2 fails (CR-3 note). |
| A-20 | Sellers adjust staffing or hours to their sales. | alternative_uses | 0.75 | Part-time staff share. | C-38, C-39 fail. |
| A-21 | The state's revenue officials, preferring a larger surplus, slow the licensing of redemption centers. | other | 0.3 | No evidence either way. | Not reported (below 0.5). |
| A-22 | Municipal recycling programs make up lost material receipts by raising fees. | revenue_use | 0.45 | Programs could also cut service or draw general funds. | Not reported (below 0.5); C-33 is recorded as a group instead. |
| A-N1 | Retailers must charge buyers the deposit on every covered container sold from 1 April 2028, including stock they bought from distributors before that date without paying it, and distributors pay the Fund only on sales to retailers from 1 April. | other | 0.6 | NEW, flagged. The record says deposits are "charged" from 1 April and that distributors pay "on each container sold to a Calder retailer"; it says nothing about stock on hand. | C-18 fails. |
| A-N2 | Some sellers can offer covered drinks in exempt forms (open cups, containers over 3 liters) at little extra cost. | substitutability | 0.6 | NEW, flagged. Exemption list; fountain equipment is common in food service; large bottles exist. | C-14 fails. |
| A-N3 | The material lost from curbside bins earned municipal programs more than it cost them, at the margin, to collect and sort; routes run anyway. | other | 0.7 | NEW, flagged. Aluminum cans are the most valuable part of what programs sell (record); routes and trucks are fixed in the short run. | C-33 becomes ambiguous. |
| A-N4 | Some buyers give their empties to charities or schools that redeem them. | other | 0.8 | NEW, flagged. Container drives under deposits elsewhere; A-8's evidence mentions charity volunteers. | C-50 fails. |
| A-N5 | For distributors, the cost of registration, monthly returns, relabeling and picking up returned containers is at least as large as what they receive for the material. | other | 0.6 | NEW, flagged. Pickup from many dispersed points; glass and plastic of low value; aluminum valuable. Weak evidence. | C-31 becomes ambiguous; C-49 loses its (+) cost chain and becomes a decrease. |

**Not reported** (an assumption below 0.5):
- Slower licensing of centers by revenue officials who prefer a surplus (CR-4, x: license promptly, y: delay; needs A-21, p 0.3).
- Municipal fees rise to replace lost material receipts (needs A-22, p 0.45); recorded only as the group C-33.

### Final check before the report

1. **Uncombined chains.** Checked in section 7: the shelf price (C-49) is ambiguous; price including deposit (C-1) is signed by CR-12e; distributors' return (C-31) and the municipal group (C-33) are signed only with A-N5 and A-N3, flagged.
2. **Single signs for a group.** Queues and travel (C-11), border-retail labor (C-38, C-39), municipal payers (C-33) and taxpayers (C-46, C-47) are recorded as groups.
3. **Baseline.** Every sign is against Calder without the Act, where empties go to bins, litter or curbside. The Fund and general-fund signs are against no Fund at all.
4. **Worse off is not poorer.** Only non-returners who keep buying (A-19) are signed for resources_available_other_uses (C-2). Returners and buyers who switch are worse off by their own ranking (CR-3a) but no spending sign is claimed for them.
5. **Timing shifts.** January to March and April to June 2028 are signed per window (C-15, C-16); holding empties (C-17) is a new action, signed against zero.
6. **Both sides of every transfer.** Listed at the end of section 9.
7. **Every class, every core rule.** CR-7c checked for bottlers (C-29), border sites (C-40, C-41), licenses (none, uncapped) and distributors (not claimed: warehouses serve both states). CR-6 applied to the fixed refund and fee (C-11). CR-11c applied to DoR's statement (C-15, C-17). CR-9 followed along every relation type (section 6 notes).
8. **Unstated premises.** Five added premises (A-N1 to A-N5), each flagged.

## 11. Report

**The policy:** From 1 April 2028, every covered drink container sold in Calder carries a 10-cent deposit, paid by distributors into a state Fund and charged to buyers on the receipt. Anyone who brings back a container bearing the Calder mark gets 10 cents, and the redemption point gets a 2-cent fee from the Fund. Large stores must take back empties unless a licensed center is within a mile; anyone may open a center for $500 a year. Distributors collect and own the returned material. Whatever is left in the Fund each year goes to the general fund; who pays if the Fund runs short is unclear (U1).

**Visible consequences:** Buyers pay more at the till, including the deposit (C-1). The Fund collects deposits and pays out refunds and fees (C-3, C-4); redemption becomes a new trade (C-5). In the first year the Fund has a surplus that goes to the general fund (C-6).

**Invisible consequences:**
- *Buyers:* Those who do not return containers and keep buying have less for other things (C-2). Some switch to exempt drinks (C-7, C-8) or buy in Penhallow (C-9). Returners spend time doing it (C-10), and in the first year queue or travel further (C-11). Purchases are brought forward into January to March 2028, when containers are marked but carry no deposit, and empties are kept for later redemption (C-15, C-16, C-17).
- *Collectors and charities:* Collectors earn more and spend more hours collecting (C-12, C-13); charities that run container drives receive more (C-50). Holders of pre-April containers and people who redeem Penhallow containers receive 10 cents they never paid (C-42); the latter break the law (C-24).
- *Retailers:* All bear the cost of charging the deposit (C-20); large stores bear the cost of taking back empties (C-21) or arrange a nearby center (C-22). Retailers stock up before April (C-18). Calder stores sell fewer covered drinks (C-34); border-town stores also sell fewer other groceries, employ fewer people or hours, and are worth less, while Penhallow border stores gain the reverse (C-35 to C-41).
- *Producers:* Regional bottlers sell less, receive less per unit, and their region-specific plant loses value from the time the bill became likely (C-27, C-28, C-29). Distributors bear compliance and pickup costs (C-19), gain the material (C-30), and, if the costs exceed the material's value, earn less (C-31). Some drinks move into exempt forms (C-14).
- *Municipal recycling:* Programs sell less material, chiefly aluminum (C-32), so their fee payers, service users or taxpayers lose (C-33).
- *Centers and workers:* Centers open (C-23) and employ workers (C-51).
- *The state:* DoR spends on administration and enforcement (C-25); distributors, large retailers and center operators lobby (C-26). Once redemption is established, the Fund runs short (C-44): under U1-a distributors pay (C-48); under U1-b the general fund pays and taxpayers or recipients of other spending lose (C-45, C-47).

**Ambiguous effects:** The shelf price of covered drinks excluding the deposit (C-49). Distributors' and retailers' added costs push it up; lower demand, where bottling plant is specific, pushes it down. What would decide it: the cost per container of the deposit system against how much the fall in demand presses on bottlers.

**Key conditions:** That the first-year Fund runs a surplus (A-3, 0.75) and the established Fund runs short (A-17, 0.55) decide who gains from the residual and who pays the shortfall. Border mobility (A-5, 0.65) drives all the border effects; Penhallow containers being redeemable (A-9, 0.75) drives fraud and adds to the shortfall. Region-specific plant (A-18, 0.6) decides that bottlers bear part of the burden. Five premises were added (A-N1 to A-N5); A-N5 (0.6) and A-N3 (0.7) are dominance premises with weak evidence.

**What this analysis cannot say:** How large any effect is, the return rate, or whether the Fund's later shortfall is large. Whether the shelf price rises or falls. Who, among municipal payers, bears lost material receipts. Net welfare and whether the policy is good. Environmental effects (litter, recycling outcomes) and health and safety effects are out of scope in version 1 and are not analyzed.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | buyers.covered_drinks | price_paid (including the deposit) | increase | short; medium; long | visible | B | CR-1 (op 3: 10 cents attached to each purchase, shown on the receipt); CR-5c (the charge moves the range of terms); CR-12e (the induced fall in the shelf price cannot exceed the charge that causes it) | A-1 |
| C-2 | buyers.non_returning | resources_available_other_uses | decrease | short; medium; long | invisible | B | CR-3 (note: they keep buying, A-19, and forfeit 10 cents a container); CR-8a; CR-8b (what they forfeit is received by the Fund) | A-1, A-19 |
| C-3 | beverage_container_fund | non_tax_receipts (deposits) | increase | short; medium; long | visible | B | CR-1 (op 4: 10 cents per container paid in); CR-8b | A-1 |
| C-4 | beverage_container_fund | subsidy_outlay (refunds and handling fees) | increase | short; medium; long | visible | B | CR-1 (op 3: refund and fee attached to each return); CR-8b (paid to returners, collectors, claimants and redemption points) | A-2 |
| C-5 | redemption_points | quantity_traded (redemption services) | increase | short; medium; long | visible | B | CR-1 (op 3: 2-cent fee); CR-4 (x: no redemption, y: redeem); CR-5 (exchanges that do not exist without the Act) | A-2 |
| C-6 | state.general_fund | non_tax_receipts (K2 residual) | increase | short | visible | B | CR-1 (op 4: residual to the general fund); CR-8b; arithmetic: r + f below 0.81 gives a surplus | A-1, A-3 |
| C-7 | buyers.non_returning (marginal) | quantity_demanded (covered drinks bought in Calder) | decrease | short; medium; long | invisible | B | CR-4b (x: covered drink in Calder made worse by 10 cents; those ranking it narrowly above y switch); CR-4c (last unit given up first); independent chains (CR-12d): y = exempt alternative (A-4) or y = Penhallow purchase (A-5) | A-4 (chain 1); A-5 (chain 2) |
| C-8 | buyers.non_returning (marginal) | quantity_substitute (exempt drinks, tap water, fountain drinks) | increase | short; medium; long | invisible | B | CR-4b (x: covered, y: exempt; y now relatively better); CR-4a (none switch the other way) | A-4 |
| C-9 | buyers.border_counties | cross_border_purchases (covered drinks in Penhallow) | increase | short; medium; long | invisible | B | CR-4 (x: buy in Calder with deposit, y: buy in Penhallow without); CR-7a (purchases move until the gain no longer covers the trip) | A-5 |
| C-10 | buyers.returning | travel_time (trips to return containers) | increase | short; medium; long | invisible | B | CR-1 (op 3: 10 cents on return); CR-4 (x: discard, y: return; those whose return cost is below 10 cents return, A-6); CR-8c | A-2, A-6 |
| C-11 | buyers.returning, collectors | wait_time, travel_time | at_least_one_increase | short | invisible | B | CR-6 (refund and fee fixed by the Act; redemption capacity scarce in year 1, A-3; pressure goes to waiting or travel); CR-8c | A-3, A-2 |
| C-12 | collectors | earnings | increase | short; medium; long | invisible | B | CR-1 (op 3: discarded marked containers now bring 10 cents); CR-3b (an added option cannot make them worse off); CR-4 (x: other use of time, y: collect; A-8: the alternative earned less) | A-7, A-8 |
| C-13 | collectors | hours_worked (collecting containers) | increase | short; medium; long | invisible | B | CR-4 (y: collect made better); CR-8a (the time is withdrawn from leisure or other work) | A-7 |
| C-14 | sellers.covered_drinks | reclassification (drinks sold in open cups or containers over 3 liters) | increase | short; medium; long | invisible | B | CR-4 (x: covered form, y: exempt form; y relatively better since buyers avoid 10 cents); CR-4a | A-N2 |
| C-15 | buyers.covered_drinks | quantity_traded (covered drinks, 1 January to 31 March 2028) | increase | short (Jan to Mar 2028; persistence n/a) | invisible | B | CR-10a (a change expected in April alters choices now); CR-4 (x: buy after 1 April and pay the deposit, y: buy before, pay none, and redeem later); CR-11c (DoR's statement conveys that pre-April containers will be redeemable) | A-10, A-11 |
| C-16 | buyers.covered_drinks | quantity_traded (covered drinks, April to June 2028) | decrease | short (Apr to Jun 2028) | invisible | B | CR-10a (stocks bought forward are drawn down, A-11); CR-4b (the deposit, A-4 or A-5); CR-12a (same direction) | A-11 (chain 1); A-4 (chain 2); A-5 (chain 3) |
| C-17 | households.holding | inventory_held (marked empties bought before 1 April 2028) | increase | short (Jan to Jun 2028; persistence n/a) | invisible | B | CR-10a; CR-11c; CR-4 (x: discard or put in curbside bin, y: keep to redeem from April) | A-10 |
| C-18 | retailers.calder | inventory_held (covered drinks, at 31 March 2028) | increase | short (persistence n/a) | invisible | B | CR-10a; CR-4 (x: buy stock after 1 April and pay the deposit to the distributor, y: buy before and charge buyers the deposit anyway, A-N1); storability (A-11) | A-N1, A-11 |
| C-19 | distributors | compliance_cost | increase | short; medium; long | invisible | B | CR-1 (op 3: registration, monthly returns, the mark from January 2028, pickup of returned containers); CR-8c | A-2 |
| C-20 | retailers.calder | compliance_cost (charging, showing and remitting the deposit) | increase | short; medium; long | invisible | B | CR-1 (op 3: charge and show the deposit); CR-8c | A-1 |
| C-21 | retailers.large | compliance_cost (taking back empties, fronting refunds; gross of the 2-cent fee) | increase | short; medium; long | invisible | B | CR-1 (op 1: refusing empties removed; op 3: space, labor, sorting by distributor, refunds fronted until the weekly payment); CR-5b (a compelled exchange); CR-8c. Gross: the fee is recorded on the other side (C-5), not netted (CR-12c) | A-2 |
| C-22 | retailers.large | reclassification (use of the one-mile center exemption) | increase | medium; long | invisible | B | CR-4 (x: handle returns in store, y: arrange a center within one mile, by contract; y cheaper for some, A-12, and a center viable there, A-13) | A-12, A-13 |
| C-23 | redemption_centers.prospective | entry_rate | increase | short; medium | invisible | B | CR-1 (op 2: K5 permission; op 3: K3 fee); CR-4 (x: stay out, y: enter); CR-7a (entry until the fee and volume no longer cover costs at the margin) | A-13, A-2 |
| C-24 | redeemers.non_calder_containers | legal_breach (redeeming containers not sold in Calder) | increase | short; medium; long | invisible | B | CR-1 (premises: with detection low the prohibition attaches a risk, not a removal); CR-4 (x: comply, y: violate; the expected gain of 10 cents exceeds the expected penalty for some, A-9) | A-9 |
| C-25 | officials.enforcement | enforcement_cost | increase | short; medium; long | invisible | A | CR-1 (op 4: up to 3% of deposits to DoR); CR-8c | none |
| C-26 | distributors, retailers.large, redemption_centers | lobbying_effort | increase | short; medium | invisible | B | CR-4 (x: accept, y: lobby; distributors over U1 and the mark, large retailers over K4, centers over the fee); CR-8c | A-14 |
| C-27 | bottlers.regional | quantity_supplied (covered drinks for Calder) | decrease | short; medium; long | invisible | B | CR-9 and LW-10 (demand for bottling follows demand for covered drinks, C-7 chain 1; the Penhallow chain does not lower it, since the same bottlers serve Penhallow) | A-4 |
| C-28 | bottlers.regional | net_price_received | decrease | short; medium; long | invisible | B | CR-7b (with less demand, the side with fewer alternatives, region-specific plant, A-18, bears part); CR-9 | A-4, A-18 |
| C-29 | bottlers.regional | asset_value (region-specific plant) | decrease | short (from 2027); medium; long | invisible | B | CR-10c and CR-7c (lower expected yields, C-28, borne by owners when the Act becomes expected: partly from 15 January 2027, fully from 30 June 2027) | A-4, A-18 |
| C-30 | distributors | quantity_traded (recovered container material sold) | increase | short; medium; long | invisible | B | CR-1 (op 4: K5 gives distributors the material of returned containers); CR-8b (material that went to curbside programs or landfill now goes to them) | A-2 |
| C-31 | distributors | return_on_capital | decrease | short; medium; long | invisible | B | CR-12b with dominance premise A-N5 under CR-12e: (−) compliance and pickup (C-19) and lower volume (C-34), borne in part (CR-7b); (+) material receipts (C-30); A-N5: costs at least as large as material | A-N5, A-2 |
| C-32 | municipal_recycling_programs | quantity_traded (container material sold, chiefly aluminum) | decrease | short; medium; long | invisible | B | CR-9 (relation: returning a container is a substitute for putting it in the curbside bin; A-16); CR-8b (the material now goes to distributors, C-30) | A-16, A-2 |
| C-33 | municipal fee payers, service users, municipal taxpayers | resources_available_other_uses | at_least_one_decrease | medium; long | invisible | B | CR-8b (lost receipts are met by someone); CR-8 (payers from a budget: a group with at_least_one_decrease); CR-12e with A-N3 (lost receipts exceed saved handling cost) | A-16, A-N3 |
| C-34 | retailers.calder | quantity_traded (covered drinks) | decrease | short; medium; long | invisible | B | CR-9 and CR-5 (buyers buy less in Calder, C-7); independent chains: exempt alternatives (A-4), Penhallow (A-5) | A-4 (chain 1); A-5 (chain 2) |
| C-35 | retailers.calder_border | quantity_traded (other groceries bought on the same trip) | decrease | short; medium; long | invisible | B | CR-9 (relation: complement, trip; buyers who go to Penhallow for drinks buy groceries there, A-15) | A-5, A-15 |
| C-36 | retailers.penhallow_border | quantity_traded (covered drinks) | increase | short; medium; long | invisible | B | CR-9 (relation: across_border; C-9); CR-5 | A-5 |
| C-37 | retailers.penhallow_border | quantity_traded (other groceries bought on the same trip) | increase | short; medium; long | invisible | B | CR-9 (relation: complement, trip) | A-5, A-15 |
| C-38 | workers.calder_border_retail | employment, hours_worked | at_least_one_decrease | short; medium | invisible | B | CR-9 and LW-10 (demand for retail labor follows sales, C-34, C-35); A-20 | A-5, A-20 |
| C-39 | workers.penhallow_border_retail | employment, hours_worked | at_least_one_increase | short; medium | invisible | B | CR-9 and LW-10 (C-36, C-37); A-20 | A-5, A-20 |
| C-40 | retailers.calder_border | asset_value (border-town store sites) | decrease | short (from 2027); medium; long | invisible | B | CR-7c and CR-10c (lower expected sales at fixed sites, borne by owners as the Act becomes expected) | A-5 |
| C-41 | retailers.penhallow_border | asset_value (border store sites) | increase | short (from 2027); medium; long | invisible | B | CR-7c and CR-10c (higher expected sales at fixed sites, captured by owners as the Act becomes expected) | A-5 |
| C-42 | claimants.no_deposit | resources_available_other_uses | increase | short; medium; long | invisible | B | CR-1 (op 3: 10 cents on any marked container); CR-8b (paid by the Fund on containers with no deposit paid); independent chains: pre-April containers (A-10), Penhallow containers (A-9) | A-10 (chain 1); A-9 (chain 2) |
| C-43 | beverage_container_fund | fund_balance (year-end, before transfer) | increase | short | invisible | B | CR-8b; arithmetic: receipts 9.7 cents net of DoR per container sold exceed 12(r + f) when r + f is below 0.81 | A-1, A-3 |
| C-44 | beverage_container_fund | fund_balance (before the shortfall is met) | decrease | medium; long | invisible | B | CR-8b; arithmetic: 12(r + f) exceeds 9.7 when r + f is above 0.81; CR-8 (residual claimants: the residual can be negative) | A-17 |
| C-45 | state.general_fund | subsidy_outlay (meeting the Fund's shortfall) | U1-a: no_change; U1-b: increase | medium; long | invisible | B | CR-8b; per reading (CR-1 recording): U1-a distributors pay; U1-b the general fund pays | A-17 |
| C-46 | taxpayers, recipients_of_other_spending | resources_available_other_uses | at_least_one_increase | short | invisible | B | CR-8b and CR-8d (the residual frees general-budget money for lower taxes, other spending or less borrowing; which is not said) | A-1, A-3 |
| C-47 | taxpayers, recipients_of_other_spending | resources_available_other_uses | U1-a: no_change; U1-b: at_least_one_decrease | medium; long | invisible | B | CR-8b; CR-8 (payers from the general budget: a group); per reading | A-17 |
| C-48 | distributors | resources_available_other_uses | U1-a: decrease; U1-b: no_change | medium; long | invisible | B | CR-8b and CR-3c (U1-a: an assessment in proportion to containers sold, a sum they cannot avoid while they sell) | A-17 |
| C-49 | buyers.covered_drinks | price_paid (shelf price excluding the deposit) | ambiguous | short; medium; long | invisible | B | CR-12b: (+) CR-7b, net added cost per container to distributors and large retailers passed on in part (A-N5), and under U1-a an assessment per container (A-17); (−) CR-7b and CR-6, lower demand (A-4) presses the price down where plant is specific (A-18). No dominance premise | A-N5, A-4, A-18 |
| C-50 | charities | resources_available_other_uses | increase | short; medium; long | invisible | B | CR-5 (gift: givers rank giving above redeeming); CR-8b (redemption value received from the Fund) | A-N4 |
| C-51 | workers.redemption_centers | employment | increase | medium; long | invisible | B | CR-9 and LW-10 (labor input_to redemption service, C-23); CR-7a (labor moves in from other uses) | A-13, A-2 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-027-C1: A local program whose receipts fall (C-33). CR-8's clarification on "payers from the general budget" covers the state budget; it was applied by analogy to a municipal program funded by fees and local taxes. The analogy seems sound but the rule does not say it extends to any budget.
- GAP-027-C2: A fund that buys a service at a fixed fee from private sellers with no fixed quantity (K3). CR-6's "public supply" clarification covers a state that supplies a fixed quantity, not a state that buys at a fixed price. C-11 and C-23 used CR-6 (displaced pressure on buyers' side) and CR-7a (entry) together; no rule states this case directly.
- No other step lacked a rule. Everything else was derived from CR-1 to CR-12, LW-10 and arithmetic on the case's figures.

**(b) Core-rule wording that was hard to apply.**
- CR-12b and the clarification on chains that cannot be derived: a chain can be derived and still have no sign (distributors' net cost per container: compliance and pickup against material receipts). The rules say what to do with an underivable chain (Tier C note) and with opposing signed chains (ambiguous), but not with a derived chain of unknown sign. A-N5 was added to give it a sign; without A-N5, C-31 is ambiguous and C-49 changes.
- CR-7b with three parties and two markets: the regional bottlers serve both states, so cross-border shopping moves sales between their Calder and Penhallow customers without lowering their output. CR-7b ranks "each pair" but does not prompt for a party that sits on both sides of a border. Only the substitution chain (A-4) was used for bottlers.
- CR-5b on K4: "a compelled transfer that would not have taken place voluntarily" cannot be checked when the compensation (the 2-cent fee) did not exist before the policy. CR-2's clarification on absent exchanges applies, but whether large retailers lose net is left unsigned; only gross compliance cost (C-21) was reported.
- CR-1's clarification treats a deposit as op 3 on purchase. Here the refund is paid to whoever returns the container, not to the buyer, which makes it also an op 3 for collectors, charities and no-deposit claimants. The clarification's example (some return, some do not) does not mention that the refund attaches to the container rather than the buyer.
- CR-10a and the normal form for a window in which the policy is visible but not in force (marked containers without deposit, January to March 2028): the per-window signs (C-15, C-16) and the new action (C-17, signed against zero) both fit, but the rules do not say which applies when part of the action exists without the policy and part does not.

**(c) Vocabulary missing from the ontology.**
- No variable for a return or redemption rate (the share of containers returned), the central quantity of a deposit system; C-5 and C-10 stand in for it.
- No variable for material or by-product receipts of a seller (municipal material sales, distributors' material); `quantity_traded` with a named market was used, and `non_tax_receipts` covers only the state or a fund.
- No variable for the service level of a public program (curbside service cut), so the municipal response had to be a group over `resources_available_other_uses`.
- `subsidy_outlay` was stretched to cover the general fund's payment of a fund shortfall (C-45); a variable for transfers between public funds is missing.
- Actor classes not in 2.2: collectors, charities, claimants of refunds on goods on which no charge was paid, and municipal programs as residual buyers of discarded material.
- The input recorded K1 as having "no type in 2.3", but 2.3 lists `deposit_refund`; it was used here.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the core of the deposit case: a higher price at the till, fewer covered drinks bought from April and more exempt ones, cross-border buying, time spent returning containers, collectors' earnings, the January-to-March window (more purchases, marked empties held for April), compliance costs, centers entering and large stores using the one-mile exemption, lobbying, scrap moving from municipal programs to distributors, the capital loss on regional bottling plant, the non-returners' loss of means, a first-year surplus to the general fund, and a later shortfall whose payer depends on U1. No key is signed in opposite directions. The differences are of coverage and recording. The pattern version (catalog 0.6) recorded six derivable claims the core version left out: who among buyers bears the unclaimed deposits (`tax_share_borne`), the price of marked empties in Penhallow, Penhallow's lost aluminum, the Fund's surplus against a static projection, the float held from returning buyers, and the jobs lost where non-returners' forfeited deposits would have been spent. The core version went further down the exchange and asset relations (bottlers' output and net price, border retail labor and store sites, the taxpayers who receive the first-year residual, the no-deposit claimants' gain) and added five flagged premises, three of which carry consequences the pattern version could not reach (retailers stocking up before April, distributors' return, municipal payers). The one place where the pattern version is wrong rather than incomplete is its decision to leave sellers' net price unsigned: CR-7b already signs the direction, and the pattern version had the premise (A-18) it needed. Several pattern-version records are now superseded by 0.7 clarifications drawn from this very example (op 3 for a charge on an option, splitting classes by response, `non_tax_receipts`, `fund_balance`, `no_change`, payers from the general budget as a group); where they matter they are recorded as V, not as errors.

Counts: M 16, V 9, S 0, OP 17, OC 6.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | Core adds the CR-12e argument that the induced fall in the shelf price cannot exceed the charge, and all horizons. |
| C-2 | C-10, C-11 | V | | Pattern: `wait_time` for storing, carrying and queuing, against no deposit. Core: `travel_time` for all horizons (C-10) plus a year-1 group for queues and travel when redemption points are scarce (C-11, CR-6). Same claim, split by variable and horizon. |
| C-3 | C-6, C-43 | V | | Pattern records the swept surplus as `tax_revenue`; core uses `non_tax_receipts` (added in 0.7, as the pattern version's own vocabulary gap proposed) and records the Fund's year-end balance separately (C-43). Both rest on A-3 and the 0.81 break-even. |
| C-4 | C-7, C-16, C-34 | V | | Pattern signs all buyers from April, with two chains (full cost rises for every buyer, returners included; first-quarter stocks drawn down). Core signs marginal non-returners (C-7), the April-to-June window with the drawdown chain (C-16), and retailers' sales (C-34). Core is narrower than CR-4 allows: returners also face a higher full cost (the trip and the float), so the pattern's wider class is valid. Core's C-7 and C-34 are labeled "short; medium; long" without excluding January to March, where section 7 says the sign is reversed; a recording slip, not a sign difference. |
| C-5 | C-8 | M | | Core restricts the class to marginal non-returners; same sign and premise (A-4). |
| C-6 | C-9 | M | | Core also notes that returners can buy in Penhallow and still redeem (A-5, A-9), which strengthens the chain. |
| C-7 | none | OC | E | `tax_share_borne` increase for buyers with high return costs, relative to those with low ones. Derivable: CR-4 per container (a container is returned when 10 cents exceeds its owner's cost of returning it, A-6) with CR-8b; the variable is defined for subgroups in the same market. Core-version omission: the core split buyers by response, as the 0.7 clarification to CR-1 now asks, and used the same per-container comparison in C-10, but did not record who bears the unclaimed deposits. |
| C-8 | C-12 | M | | Both rest on A-7 and A-8. Core adds hours (C-13). |
| C-9 | C-24 | V | | Pattern: `informal_activity`; core: `legal_breach`. Same claim (CR-4, x: comply, y: violate; A-9). |
| C-10 | C-17 | M | | Core's class is households only; the pattern also names collectors. Same sign and premise (A-10). |
| C-11 | C-15 | M | | Core adds CR-11c (DoR's statement conveys that pre-April containers are redeemable). |
| C-12 | C-20, C-21 | V | | Split into all retailers (C-20) and large stores' take-back (C-21). Pattern: Tier A with no premise; core: Tier B (A-1, A-2). The take-back cost does depend on some containers being returned, so the core's tier is the more careful one. |
| C-13 | C-19 | M | | Tier A in the pattern, B in the core (A-2). Registration and monthly returns need no premise; only pickup does. |
| C-14 | C-22 | M | | Core horizon medium and long, with A-13 added (a center must be viable near the store). |
| C-15 | C-23 | M | | |
| C-16 | C-26 | M | | |
| C-17 | C-36, C-37 | V | | Pattern: all goods; core splits covered drinks (C-36) from other groceries on the same trip (C-37). |
| C-18 | C-35 | M | | |
| C-19 | none | OC | E | Holders of marked empties in Penhallow: `net_price_received` increase (CR-9 and CR-7a: the price of a marked empty there rises toward the Calder refund, net of transport and expected penalty; A-9). Core-version omission: the core recorded the redeemers' gain (C-42) and the breach (C-24) but not the price received by those who sell or give empties to them. |
| C-20 | C-32 | M | | |
| C-21 | C-30 | M | | |
| C-22 | none | OC | E | Penhallow recycling programs sell less aluminum (CR-9; marked cans move to Calder redemption points, A-9). Core-version omission: the core followed `across_border` for shoppers but not for empties. |
| C-23 | none | OC | E | `tax_revenue_vs_static_projection` decrease (a defined variable): claims by collectors on discarded containers, Penhallow containers and pre-April containers are all paid from the Fund (CR-8b, arithmetic; independent chains under CR-12d). Core-version omission: core C-4 and C-42 include these claims but no consequence compares the Fund with a static projection. |
| C-24 | C-44, C-45, C-47, C-48 | V | | Same claim (A-17), recorded per class and per reading in the core, with `no_change` where a reading gives none (added to 2.5 in 0.7; the pattern version noted its absence). One difference of content: under U1-b the pattern signs `taxpayers` decrease by TX-1 and OC-1, which presumes the shortfall is met by raising taxes; the 0.7 clarification to CR-8 ("payers from the general budget") gives only a group of taxpayers and recipients of other spending with `at_least_one_decrease`, as core C-47 records. The pattern version, written before that clarification, overclaims for taxpayers alone. |
| C-25 | C-29 | M | | Both date the loss from announcement (CR-7c, CR-10c; A-4, A-18). |
| C-26 | C-2 | M | | |
| C-27 | none | OC | E | Returning buyers' `resources_available_other_uses` decrease: deposits outstanding on containers bought and not yet returned are held by the Fund (CR-8b, LW-7). The core declined this in its final check ("no spending sign is claimed" for returners), but the CR-3 note's condition is met by returners who keep buying the burdened good, so the claim is derivable (CR-3 note, CR-8b, CR-10). Core-version error. The pattern version also hides a premise: it cites only A-2 (some containers are returned), while the claim needs returners to keep buying, the analogue of A-19 for non-returners. |
| C-28 | C-25 | M | | Both note the cost is paid from the Fund (OC-3 third case; CR-8c, CR-8d). |
| C-29 | C-51 | V | | Pattern: `employment`, `hours_worked` as a group, `at_least_one_increase` (OC-5). Core: `employment` increase alone. The core's single sign is defensible, since new centers start from no workers, so hours cannot substitute for jobs. |
| C-30 | none | OC | E | Sellers of what non-returning buyers would have bought: `employment`, `hours_worked`, `at_least_one_decrease` (CR-3 note with A-19, CR-8a, then CR-9 and LW-10 with A-20). This is the unseen side of core C-51 (Hazlitt's tailor). Core-version omission: it counted the jobs paid for by forfeited deposits but not the jobs their spending would have supported, although it did the analogous pair for border retail (C-38, C-39). |
| — (shelf price excluding the deposit, not signed) | C-49 | V | | Pattern leaves it unsigned (C-1 note); core records `ambiguous` with chains both ways. The core's (+) chain rests on its own premise A-N5 and on U1-a. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-3 | OP | J | The Fund's deposits received. The pattern version treated the Fund as a pass-through and recorded only its residual (C-3, C-23) and an accounting table in section 9. Recording choice. |
| C-4 | OP | J | The Fund's outlays on refunds and fees. As C-3. |
| C-5 | OP | E | Redemption services traded increase (CR-1 op 3, CR-4, CR-5; A-2). Pattern-version omission; implied by its C-15 and C-29 but not recorded. |
| C-13 | OP | E | Collectors' hours increase (CR-4, CR-8a; A-7). Pattern-version omission. |
| C-14 | OP | E | Sellers reshape drinks into exempt forms (open cups, containers over 3 liters) (CR-4, x: covered form, y: exempt form; A-N2). RS-5 applies to K1's exemption line; the pattern version cited RS-5 only for K4. Pattern-version omission, resting on a new premise. |
| C-18 | OP | A | Retailers stock up before 1 April 2028. Rests on A-N1 (p 0.6), a reading of the record on stock on hand that the pattern version did not make. Valid given the premise. |
| C-27 | OP | E | Regional bottlers supply less for Calder (CR-9, LW-10; A-4). The pattern version's C-25 rests on lower expected sales but records no quantity. Core correctly excludes the Penhallow chain, since the same bottlers serve both states. |
| C-28 | OP | P | Regional bottlers' `net_price_received` decrease (CR-7b, CR-9; A-4, A-18). The pattern version left sellers' net price unsigned in section 7 because "no premise compares buyers' and sellers' alternatives (CR-7b)". CR-7b (unchanged since 0.6) needs that comparison only to rank the shares; without it "only the direction of each side's price is signed", and the pattern version had the immobility premise (A-18) that makes bottlers bear part. Pattern-version error. |
| C-31 | OP | A | Distributors' return on capital decrease. Rests on the dominance premise A-N5 (p 0.6, weak evidence) under CR-12e. Without it the key is ambiguous, as the core says. The core's volume chain cites C-34 including its Penhallow chain, which by the core's own note on bottlers (distributors serve both states from the same warehouses) does not lower distributors' volume; the sign survives on the other chains. |
| C-33 | OP | A | Municipal fee payers, service users or taxpayers, `at_least_one_decrease`. The pattern version declined it because A-22 (fees rise) is below the cut-off. The core reached it by applying the 0.7 group clarification to CR-8 (which postdates the pattern version) by analogy to a municipal budget, plus A-N3. Different premises and a later rule; both versions agree that a specific payer cannot be named. |
| C-38 | OP | E | Calder border retail labor, `at_least_one_decrease` (CR-9, LW-10; A-5, A-20). Pattern-version omission (OC-5 or RS-6 would give it). |
| C-39 | OP | E | Penhallow border retail labor, `at_least_one_increase`. As C-38. |
| C-40 | OP | E | Calder border store sites lose value from 2027 (CR-7c, CR-10c; A-5). The pattern version's final check applied CR-7c to bottlers only. Pattern-version omission. |
| C-41 | OP | E | Penhallow border store sites gain value. As C-40. |
| C-42 | OP | E | No-deposit claimants (pre-April holders, Penhallow redeemers) gain means (CR-8b; A-9, A-10). The pattern version shows this transfer in its section 9 table but records no consequence for the recipients. Pattern-version omission. |
| C-46 | OP | E | Taxpayers and recipients of other spending, `at_least_one_increase` in year 1, from the residual (CR-8b, CR-8d). The pattern version recorded the state's receipt (C-3) but not who benefits from it. Pattern-version omission. |
| C-50 | OP | J | Charities' receipts through the gift relation (CR-5 gift clarification; A-N4). The pattern version folded charities and youth groups into collectors (C-8). Both defensible. |

### Findings

- **Pattern overclaims or hidden premises.** (1) C-24 under U1-b signs `taxpayers` decrease through TX-1 and OC-1, which presumes the shortfall is met by a tax rise; CR-8b gives only a group of taxpayers and recipients of other spending with `at_least_one_decrease`. The 0.7 clarification on payers from the general budget now says so; the pattern version predates it. (2) C-27 (returners' float) needs the premise that returners keep buying covered drinks; the pattern version cites only A-2. (3) C-12 and C-13 are given Tier A with no premise, but the take-back and pickup costs depend on some containers being returned (A-2).
- **Errors in the core version.** Omissions of derivable claims: who among buyers bears the unclaimed deposits (pattern C-7), the price of marked empties in Penhallow (C-19), Penhallow's lost aluminum (C-22), the Fund against a static projection (C-23), and the unseen jobs where forfeited deposits would have been spent (C-30), the missing half of its own C-51. Its decline of the returners' float (pattern C-27) misapplies the CR-3 note, whose condition is met by returners who keep buying. Smaller points: C-7 and C-34 carry "short; medium; long" without excluding the January-to-March window; C-31's volume chain uses the Penhallow chain that the core itself excluded for bottlers, who share warehouses with the distributors; C-3 and K1's distributor payment are recorded as CR-1 op 4, although the 0.7 clarification makes a charge paid per container sold op 3. C-7 also restricts the fall in demand to non-returners, though CR-4 gives it for returners too.
- **Errors in the pattern version.** Leaving sellers' net price unsigned (core C-28) misreads CR-7b, which signs each side's direction and needs a comparison of alternatives only to rank the shares. Omissions: the Fund's flows and the redemption trade (C-3 to C-5), collectors' hours (C-13), sellers' reshaping into exempt forms (C-14), bottlers' output (C-27), border retail labor and store sites (C-38 to C-41), the no-deposit claimants' gain (C-42) and the beneficiaries of the year-1 residual (C-46). Its op 2 for "returning the empty" and its single-row C-24 naming two classes are superseded by the 0.7 clarifications to CR-1 and the `no_change` value in 2.5, not errors under 0.6.
- **Limits of the core rules.** None produced a difference. Every pattern-version claim that the core version lacks is derivable from CR-1 to CR-12, and every core-only claim either is derivable or rests on a flagged premise. The core version's own notes stand: CR-6's public-supply clarification does not state the case of a fund buying a service at a fixed fee with no fixed quantity (GAP-027-C2); the CR-8 group clarification names only the general budget, not a municipal one (GAP-027-C1); CR-12 does not say what to do with a derived chain of unknown sign (distributors' net cost per container), which forced A-N5; and the CR-1 clarification on deposits does not say that the refund attaches to the container, not to the buyer, which is what makes collectors and no-deposit claimants recipients. Several 0.7 clarifications (CR-1 op 3 for charges and split by response, CR-8 residual claimants, RS-4's sentence on refunds drawing items across a boundary, RS-8's sentence on claims acquired before the charge) were drawn partly from the pattern version of this example, so the two versions are not fully independent tests of them.
