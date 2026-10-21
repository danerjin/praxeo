# WE-027 Ten-cent deposit on beverage containers, refunded on return

Analyst: draft (Handbook 0.6, corrected under 0.8)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional state. It is a gap-probing example: one instrument takes money from every buyer and gives it back to whoever returns the container, so it is a tax for some actors, an interest-free loan for others and a source of income for third parties, depending on choices made after the purchase. None of WE-001 to WE-025 has an instrument whose direction of transfer depends on the actor's own later choice. The analysis tests CR-1 on such an instrument, CR-8 on the unredeemed residual and on payments made with no deposit behind them, a new option open to people who never bought the good, and cross-border claims. Environmental effects (litter, recycling rates, use of materials) are the stated purpose of deposit laws but are out of scope for version 1, which has no variables for them; this analysis covers only the variables in the controlled list. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Calder Beverage Container Recovery Act.** Calder is a state of about 3.1 million people, in which about 2.2 billion covered containers are sold a year (about 700 per person). The neighboring state of Penhallow, to the east, has no deposit. About 600,000 Calder residents live in counties along the Penhallow line; four Calder towns are within 15 km of it, and Penhallow has large discount stores at two highway exits just across it. Regional bottlers and distributors serve both states from the same warehouses, and print one label for the whole region. Most Calder municipalities run curbside recycling, and aluminum cans are the most valuable part of what they collect and sell.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | State of Calder. Penhallow (no deposit) to the east; its border stores are 10 to 15 minutes from the four Calder border towns. | §2 |
| Announced / enacted / effective / expires | Introduced 15 January 2027 as the governor's bill, with the majority leaders of both houses as sponsors (announced). Enacted 30 June 2027. Refund mark required on containers sold in Calder from 1 January 2028. Deposits charged and redemption begins 1 April 2028. No expiry. | §§3, 7, 11 |
| Enforcement (who, penalties, resources) | Department of Revenue (DoR): registration of distributors, monthly returns, audits of redemption points, eight investigators. Knowingly redeeming containers not sold in Calder: civil penalty of $100 per 100 containers; more than 10,000 containers in a year is a felony. DoR's administration and enforcement are paid from the Fund, up to 3% of deposits. | §§15, 16 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Deposit and refund | `deposit_refund` (section 2) | Covered beverages (soft drinks, water, beer, malt drinks, juice, sports and energy drinks) in sealed glass, metal or plastic containers of 3 liters or less | Distributors pay 10 cents into the Beverage Container Fund on each container sold to a Calder retailer; retailers must charge the buyer 10 cents a container, shown separately on the receipt; any redemption point pays 10 cents for each empty container bearing the mark "CL 10¢". | 10 cents per container. | Milk and plant milks, wine, spirits, infant formula, containers over 3 liters, drinks served in open cups. |
| K2 Unredeemed deposits | Revenue rule | The Fund's balance | DoR | At each year-end, the Fund's balance after refunds, handling fees and DoR costs goes to the general fund. | None |
| K3 Handling fee | `per_unit_subsidy` | Redemption service | The Fund | 2 cents per container redeemed, paid to the redemption point, with the 10-cent refund, weekly. | None |
| K4 Return obligation | Forced exchange (section 2) | Taking back empties | Retailers with more than 5,000 sq ft of floor space that sell covered beverages | Must accept empties of the kinds and brands they sell, up to 250 containers per person per day. | Retailers with a licensed redemption center open at least 40 hours a week within one mile. Smaller retailers. |
| K5 Licensed redemption centers | Permission | Operating a center | Any operator meeting site standards | $500 a year; no cap on numbers. Returned containers are picked up by the distributor that sold them, which owns and sells the material. | — |

Unclear provisions:
- **U1.** Who pays if the Fund cannot cover refunds and handling fees. §14(c): "Should the Fund be insufficient, the shortfall shall be met as provided by law." §9 says each distributor "is responsible for the refund value of containers it initiates", which suggests an assessment on distributors; no statute provides one, and the general fund could be drawn on instead. Reading U1-a: distributors are assessed in proportion to containers sold. Reading U1-b: the shortfall is met from the general fund. Readings get no probability.

**What the text decides.** §11 says that from 1 April 2028 a redemption point "shall pay the refund value on any empty covered container bearing the refund mark". It does not exclude containers sold before the deposit began (marked from 1 January 2028) or sold outside Calder with the regional label. DoR has said it will not ask redemption points to tell them apart, because they cannot. These are therefore treated as assumptions about practice (A-9, A-10), not readings.

**Break-even of the Fund (arithmetic on the case's figures).** Per container sold, the Fund receives 10 cents. It pays 12 cents (refund and handling fee) for each container redeemed, whether or not a deposit was paid on it, and up to 0.3 cents for DoR. Let *r* be the share of containers sold in Calder that are redeemed, and *f* the number of containers redeemed on which no deposit was paid (pre-April and Penhallow containers), as a share of containers sold. The Fund has a surplus if 12(*r* + *f*) < 9.7, that is, if *r* + *f* < 0.81.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary, in both directions: a forced payment to the Fund on every purchase, and a payment from the Fund to whoever returns the container. Per container, the net is a tax if no one returns it, a transfer from the buyer to a collector if someone else does, and an interest-free loan to the Fund if the buyer does. | Yes (A-1) | `deposit_refund` (candidate pattern; 2.3): CR-1, CR-4, CR-8. TX (TX-1, TX-5 apply; TX-2's wedge applies only in part, see section 4); RS |
| K2 | Binary: the state is the `residual_claimant`. | Yes | CR-8b (0.7: residual claimants) |
| K3 | Binary: a per-unit payment to redemption points, funded by the unredeemed deposits. | Yes | SB (SB-1's two sides through CR-8b); CR-6 (0.8: a public buyer at a fixed fee with no fixed quantity) |
| K4 | Triangular: forces large retailers to buy empties from the public at 10 cents (reimbursed, with the 2-cent fee). | Yes for stores without a center nearby | CR-1, CR-5b, RS-5 |
| K5 | Adds an option (CR-1 op 2); not restrictive. | — | CR-7 |

**CR-1 operations by actor class.** The counterfactual law has no deposit; empties have only scrap value (about 1 cent for a can at a scrap yard, nothing for most plastic). Under the 0.7 and 0.8 clarifications to CR-1, a charge paid only when an option is taken is operation 3, and a refund attached to the container rather than to the person is operation 3 on the option of returning it, for anyone who holds the container.

| Actor class | Operations |
|---|---|
| `buyers.calder` | Op 3 on buying a covered drink: a 10-cent payment is attached. Op 3 on returning the empty: 10 cents is attached to it. The operations are the same for every buyer; the classes `buyers.returning` and `buyers.non_returning` are split by response, per container (CR-1, 0.7). |
| `collectors` (anyone, including people who never buy covered drinks) | Op 3 on returning a marked container, which they hold once they collect it. |
| `holders_of_empties.penhallow` | Op 3 (a Calder redemption point will pay for marked containers), with a further op 3 attached: the risk of a penalty for knowingly redeeming them. |
| `retailers.calder` | Op 3 on selling covered drinks: collecting and showing deposits. Large stores without a center nearby: op 1 (refusing empties removed) and op 3 (taking back empties, K4). |
| `distributors` | Op 3 on selling to Calder retailers: 10 cents per container to the Fund (CR-1, 0.8), returns, pickup of empties. Op 4: the material of returned containers. U1-a only: op 3, an assessment in proportion to containers sold. |
| `redemption_centers` | Op 2: a new line of business (K5), with op 3: the 2-cent fee on each container redeemed. |
| `state_budget` (`residual_claimant`), taxpayers and recipients of other spending | Op 4: the state receives the Fund's surplus. U1-b only: the general budget funds a shortfall. |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `buyers.calder` | Everyone buying covered drinks in Calder | Pay 10 cents more per container at the till; may return it for 10 cents. |
| `buyers.returning`, `buyers.non_returning` | Buyers, for the containers they return and for those they do not | Per container: a loan repaid at the cost of the return trip, or a 10-cent charge. |
| `buyers.high_return_cost`, `buyers.low_return_cost` | Buyers whose cost of returning a container is high (drinks consumed away from home, small volumes, far from a redemption point, high value of time) or low | Who bears the tax part of K1. |
| `collectors` | People who collect discarded containers and redeem them: informal collectors, charities and youth groups running bottle drives | A new source of income. |
| `collectors.cross_border` | People who bring empties from Penhallow | A refund for containers on which no deposit was paid, at a legal risk. |
| `claimants.no_deposit` | Holders of marked containers bought before April 2028, and redeemers of Penhallow containers | Receive 10 cents on containers on which no deposit was paid. |
| `holders_of_empties.penhallow` | Penhallow households, bars and restaurants | Their empties gain a buyer. |
| `retailers.calder` (large, small, border) | Shops selling covered drinks | Compliance; large stores take back empties; border stores lose some customers. |
| `retailers.penhallow.border` (`neighboring_jurisdictions`) | Penhallow stores near the line | Gain some Calder customers. |
| Workers in border retail on each side | Labor in the border stores | Demand for their work moves with sales. |
| `sellers.covered_drinks` | Food service and bottlers | Can sell drinks in exempt forms. |
| `distributors` | Register, remit deposits, collect empties | Compliance; own returned material; U1-a: pay any shortfall. |
| `redemption_centers` | New licensed centers | Paid 2 cents a container. |
| `bottlers.regional` (`factor_owners.specific`) | Bottlers and brewers with plants specific to the region and most sales in Calder | Lower demand in Calder. |
| `sellers.substitutes` | Sellers of exempt drinks | More demand. |
| `recycling_programs.calder`, `recycling_programs.penhallow` | Municipal curbside programs | Lose the most valuable material. |
| Municipal fee payers, service users and municipal taxpayers | Those who fund Calder's recycling programs | Bear the programs' lost receipts. |
| `officials.revenue`, `state_budget`, taxpayers and recipients of other spending | DoR, the general fund and those whose taxes or spending the general budget sets | New administration; the residual; U1-b: shortfalls. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.calder` | `price_paid` (covered drinks, including the deposit, at the till) | increase | short | CR-1 op 3; arithmetic (the deposit is charged on top of the shelf price by law); CR-12e (any fall in the shelf price is caused by the charge and cannot exceed it) | A-1 |
| C-2 | `buyers.returning` | `wait_time` (time spent storing, sorting, carrying and queuing to return containers) | increase | short | CR-4, CR-8c, OC-2 | A-2 |
| C-3 | `state_budget` (`residual_claimant`) | `non_tax_receipts` (Fund surplus swept to the general fund; first year) | increase | short | CR-8b with K2 (0.7: residual claimants); CR-12e (arithmetic: *r* + *f* below 0.81 in the first year) | A-3 |

C-1 is the price at the till. The shelf price before the deposit is a separate consequence (C-44, `ambiguous`): lower demand presses it down where plant is specific (CR-7b), while per-container costs of distributors and large stores, and under U1-a an assessment per container, push it up. For buyers who return their containers the deposit is not a wedge at all, since it comes back.

C-2: compared with no deposit, a buyer who returns a container pays 10 cents and gets 10 cents back, so the time spent returning it is a cost with nothing to show for it against the counterfactual. Against not returning, it buys 10 cents. Both statements are true; the sign is against the counterfactual (2.5).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `buyers.calder` | `quantity_traded` (covered drinks in Calder; from 1 April 2028) | decrease | short | CR-4c (the full cost of a container rises for every buyer: 10 cents if not returned, the return trip and the wait for the refund if returned); CR-10a (stocks bought in the first quarter are drawn down, C-11) | A-4, A-11 |
| C-5 | `buyers.calder` | `quantity_substitute` (exempt drinks: milk, wine, spirits, fountain drinks, containers over 3 liters, home carbonation) | increase | short | RS-1 | A-4 |
| C-6 | `buyers.non_returning` near the border | `cross_border_purchases` (covered drinks bought in Penhallow) | increase | short | RS-4 | A-5 |
| C-7 | `buyers.high_return_cost` | `tax_share_borne` (relative to `buyers.low_return_cost`) | increase | short | CR-4 (a buyer returns a container when 10 cents exceeds their cost of returning it, so the containers not returned are those of buyers with high return costs); CR-8b | A-6 |
| C-8 | `collectors` | `earnings` (from redeeming containers others discard) | increase | short to medium | CR-1 op 3 (the refund attaches to the container), CR-3b; CR-4 (x: next-best use of the time, y: collecting); CR-7a (collecting spreads to wherever discarded containers are found) | A-7, A-8 |
| C-9 | `collectors.cross_border` | `legal_breach` (Penhallow containers redeemed in Calder) | increase | short to medium | RS-3, RS-4 (a payment inside the boundary draws items across it); CR-4 (x: comply, y: violate) | A-9 |
| C-10 | households and `collectors` | `inventory_held` (marked empty containers held unredeemed, 1 January to 31 March 2028) | increase | short | RS-8 (*Unless*: a claim acquired before the charge that funds it starts); CR-10a (a marked container will be worth 10 cents from April, with no deposit paid on it) | A-10 |
| C-11 | `buyers.calder` | `quantity_traded` (covered drinks in Calder; window 1 January to 31 March 2028) | increase | short | RS-8; CR-10a: buyers who expect not to return stock up before the deposit, and every marked container bought in the window is redeemable from April without a deposit having been paid | A-10, A-11 |
| C-12 | `retailers.calder` | `compliance_cost` (charging and showing deposits, records; for large stores, taking back, storing and counting empties) | increase | short | TX-5, CR-8c | A-1, A-2 |
| C-13 | `distributors` | `compliance_cost` (registration, monthly returns, labels, pickup of empties) | increase | short | TX-5, CR-8c | none |
| C-14 | `retailers.calder` (large) | `reclassification` (arranging for a licensed center within one mile, to fall under K4's exemption) | increase | short to medium | RS-5 | A-12 |
| C-15 | `redemption_centers` | `entry_rate` | increase | short | CR-1 op 2, CR-7 (resources move to the new use while its yield exceeds others) | A-13 |
| C-16 | `distributors`, `retailers.calder`, `redemption_centers` | `lobbying_effort` (distributors and retailers for repeal, a lower deposit or narrower coverage; centers for a higher handling fee; distributors for reading U1-b) | increase | medium | RS-7 | A-14 |
| C-31 | `redemption_centers` and large retailers (redemption points) | `quantity_traded` (redemption services) | increase | short to medium | CR-1 op 3 (the 2-cent fee), CR-4, CR-5 (exchanges that do not take place without the Act), CR-6 (0.8: a public buyer at a fixed fee; the quantity is set by sellers' response) | A-2 |
| C-32 | `collectors` | `hours_worked` (collecting containers) | increase | short to medium | CR-4 (y: collecting, made better), CR-8a (the time is withdrawn from leisure or other work) | A-7 |
| C-33 | `sellers.covered_drinks` | `reclassification` (drinks sold in open cups or containers over 3 liters) | increase | short to medium | RS-5 (K1's exemption line), CR-4 (x: covered form, y: exempt form) | A-24 |

C-4 and C-11 are the same activity in two windows, as 2.5 requires. In the first quarter of 2028, purchases rise against the counterfactual for two reasons that push the same way: buyers who do not expect to return containers stock up before the deposit (RS-8), and every container bought in that window carries the mark but no deposit, so it can be redeemed in April for 10 cents that no one paid in (RS-8's *Unless* clause, 0.7). From April, purchases fall: stocks bought in the first quarter are drawn down, and the deposit raises the full cost of every container for every buyer (C-4). Both chains of C-4 push down, so no combination is needed.

C-7 is the incidence of the tax part of K1. By CR-4, applied per container, a container is returned when its refund exceeds its owner's cost of returning it. The containers that are not returned, whose deposits are the tax, are therefore those of buyers for whom returning costs most: drinks consumed away from home, buyers far from a redemption point, buyers who value their time highly, and buyers of a single can. This is a statement about who bears the tax among buyers; how the burden of lower sales splits between buyers and sellers is in section 7.

C-8 and C-32: anyone may redeem a marked container, so collectors take up containers that buyers discard. For them the Act only adds to what an option brings (CR-3b). They spend more hours collecting (C-32); their money earnings rise if the time they spend collecting would otherwise have earned less money (A-8). Where a collector redeems a container that its buyer discarded, the buyer's 10 cents go to the collector instead of to the state (CR-8b, section 9).

C-9: most containers sold in Penhallow carry the Calder mark, and redemption points cannot tell them apart. For Penhallow empties, collecting and carrying them to a Calder redemption point yields 10 cents less transport and expected penalty, against about 1 cent at a scrap yard. CR-4 (x: comply, y: violate) gives the direction; A-9 is the premise that detection is low enough. The redemption itself takes place in the legal market, so the variable is `legal_breach`.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-17 | `retailers.penhallow.border` | `quantity_traded` (all goods) | increase | short | RS-4, RS-9 | Calder and Penhallow border stores: `across_border`, close for border residents | A-5, A-15 |
| C-18 | `retailers.calder` (border) | `quantity_traded` (other groceries bought on drink trips) | decrease | short | RS-9 | covered drinks and other groceries: `complement`, note `trip` | A-5, A-15 |
| C-19 | `holders_of_empties.penhallow` | `net_price_received` (empty containers bearing the mark) | increase | short to medium | CR-9, CR-7a (the price of a marked empty in Penhallow rises toward the Calder refund, net of transport and expected penalty) | marked empties in Penhallow and Calder: `across_border`, close | A-9 |
| C-20 | `recycling_programs.calder` | `quantity_traded` (aluminum and plastic scrap sold) | decrease | short to medium | CR-9; CR-4 (returned and collected containers no longer go into curbside bins) | containers and municipal scrap sales: `input_to` | A-16 |
| C-21 | `distributors` | `quantity_traded` (scrap from returned containers) | increase | short | CR-8b, CR-9 (K5: the material of returned containers is the distributors') | as C-20 | A-2 |
| C-22 | `recycling_programs.penhallow` | `quantity_traded` (aluminum scrap sold) | decrease | short to medium | CR-9 (marked cans move to Calder redemption points, C-9, C-19) | as C-19 | A-9 |
| C-23 | `officials.revenue`, `state_budget` | `tax_revenue_vs_static_projection` (Fund surplus against deposits sold times a projected non-return rate) | decrease | short | CR-8b with arithmetic; three independent chains, each enough (CR-12d): collectors redeem discarded containers (A-7); Penhallow containers are redeemed (A-9); pre-April containers are redeemed (A-10) | — | A-7 |
| C-24 | `distributors` | `resources_available_other_uses` (assessment for a Fund shortfall) | U1-a: decrease; U1-b: no_change | medium | CR-8b (refunds and fees beyond the Fund's receipts are paid by someone); U1-a: CR-1 op 3 (an assessment in proportion to containers sold) with the CR-3 note (a sum they cannot avoid while they sell); CR-8, 0.8 (contingent payers recorded per reading) | — | A-17 |
| C-25 | `bottlers.regional` | `asset_value` (plants and firms) | decrease | short | CR-7c, CR-10c (lower expected sales in Calder, C-4, from when the Act became expected) | — | A-4, A-18 |
| C-34 | `bottlers.regional` | `quantity_supplied` (covered drinks for Calder) | decrease | short to medium | CR-9 and LW-10 (demand for bottling follows demand for covered drinks through the exempt-drinks chain, C-4, C-5; the Penhallow chain does not lower it, since the same bottlers serve Penhallow) | covered drinks: `input_to` | A-4 |
| C-35 | `bottlers.regional` | `net_price_received` | decrease | short to medium | CR-7b (with lower demand, the side with fewer alternatives, region-specific plant, bears part; the direction is signed without a premise ranking the shares), CR-9 | as C-34 | A-4, A-18 |
| C-36 | Workers in Calder border retail | `employment`, `hours_worked` | at_least_one_decrease | short to medium | OC-5 (existing activity: group form), CR-9 and LW-10 (C-6, C-18) | labor `input_to` border retail | A-5, A-20 |
| C-37 | Workers in Penhallow border retail | `employment`, `hours_worked` | at_least_one_increase | short to medium | OC-5, CR-9 and LW-10 (C-17) | as C-36 | A-5, A-20 |
| C-38 | `retailers.calder` (border) | `asset_value` (border-town store sites) | decrease | short (from 2027) | CR-7c, CR-10c (lower expected sales at fixed sites, borne by owners as the Act becomes expected) | `across_border` | A-5 |
| C-39 | `retailers.penhallow.border` | `asset_value` (border store sites) | increase | short (from 2027) | CR-7c, CR-10c (higher expected sales at fixed sites, captured by owners as the Act becomes expected) | `across_border` | A-5 |
| C-40 | `claimants.no_deposit` | `resources_available_other_uses` | increase | short to medium | CR-1 op 3 (10 cents on any marked container), CR-8b (paid by the Fund on containers with no deposit paid); independent chains (CR-12d): pre-April containers (A-10), Penhallow containers (A-9) | — | A-9, A-10 |
| C-41 | taxpayers, recipients of other spending | `resources_available_other_uses` (first-year residual) | at_least_one_increase | short | CR-8b and CR-8d (the residual frees general-budget money for lower taxes, other spending or less borrowing; which is not said) | — | A-3 |
| C-42 | taxpayers, recipients of other spending | `resources_available_other_uses` (Fund shortfall) | U1-a: no_change; U1-b: at_least_one_decrease | medium | CR-8b; CR-8 (0.7: payers from the general budget are a group; 0.8: contingent payers per reading); OC-1 (Who pays) | — | A-17 |
| C-43 | `state_budget` | `subsidy_outlay` (meeting the Fund's shortfall) | U1-a: no_change; U1-b: increase | medium | CR-8b; CR-8, 0.8 (contingent payers per reading) | — | A-17 |
| C-44 | `buyers.calder` | `price_paid` (shelf price excluding the deposit) | ambiguous | short to medium | CR-12b: (−) CR-7b and CR-6 (lower demand presses the price down where plant is specific); (+) CR-7b (per-container costs of distributors and large stores, net of material and fees, passed on in part; under U1-a, an assessment per container); CR-12 (0.8, kind 2: the (+) chain's premise has p ≥ 0.5) | — | A-4, A-18, A-26 |
| C-45 | Municipal fee payers, service users, municipal taxpayers | `resources_available_other_uses` | at_least_one_decrease | medium | CR-8b (the programs' lost receipts are met by someone); OC-1 (0.8: payers from a budget are a group); CR-12e with A-25 (lost receipts exceed the handling cost saved) | containers and municipal scrap sales: `input_to` | A-16, A-25 |

C-20 and C-21 are two sides of one move (CR-8b, CR-9). Without the Act, cans and bottles went into curbside bins, and municipal programs sold the material; now the containers returned or collected are picked up by distributors, who sell it. What the programs lose in material, distributors gain. Who makes up the programs' lost receipts is a group (C-45): which member pays (higher fees, less service or general funds) needs a premise, and A-22 (fees rise, p = 0.45) is below the cut-off.

C-23: a static projection of the Fund multiplies deposits sold by a projected rate of non-return. Every container redeemed by a collector in place of its discarding buyer, every Penhallow container and every pre-April container is paid out of the Fund, so the surplus is below that projection. Each chain is enough on its own (CR-12d); A-7 (p = 0.95) is listed as the premise of the strongest.

C-24, C-42 and C-43: U1 decides *who* pays a shortfall. A-17 (p = 0.55) is the premise that *r* + *f* exceeds 0.81 once redemption points are established (break-even, section 1). Each class now has its own row, with `no_change` under the reading in which it does not pay (2.5). Under U1-b the payers are a group of taxpayers and recipients of other spending (`at_least_one_decrease`), not taxpayers alone (CR-8, 0.7; OC-1 and TX-1, 0.8).

C-34 and C-35: bottlers sell less for Calder and receive a lower net price. The cross-border chain (C-6) does not reduce their volume, because the same bottlers serve Penhallow. CR-7b signs the direction of each side's price. A comparison of alternatives is needed only to rank the shares, and none is claimed.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `buyers.calder`, `quantity_traded` (covered drinks), from April 2028, short | None | Full cost of every container rises (C-4); first-quarter stocks drawn down (C-11). | — | **decrease** (C-4). |
| `buyers.calder`, `quantity_traded`, first quarter 2028 | Stocking up before the deposit; containers bought then are redeemable without a deposit. | None | — | **increase** (C-11). |
| `buyers.calder`, `price_paid` including deposit, short | The 10-cent charge (CR-1 op 3). | Lower demand lowers the shelf price where plant is specific (CR-7b). | CR-12e: the fall in the shelf price is caused by the charge and cannot exceed it. | **increase** (C-1). |
| `buyers.calder`, `price_paid` (shelf price excluding deposit), short to medium | Per-container costs of distributors and large stores, net of material and fees, passed on in part (A-26); under U1-a, an assessment per container (A-17). | Lower demand with specific plant (A-4, A-18). | None | **ambiguous** (C-44). |
| `bottlers.regional`, `net_price_received`, short to medium | — | Lower demand (A-4, A-18). | Not needed. | **decrease** (C-35). |
| `state_budget`, `non_tax_receipts` (Fund surplus), short | Deposits on containers not yet returned while redemption points open (A-3). | Payments on containers with no deposit (C-23); handling fees; DoR costs. | Arithmetic: *r* + *f* below 0.81 in the first year (A-3, CR-12e). | **increase** (C-3). |
| `state_budget`, Fund position, medium | Deposits not redeemed. | Refunds, fees and claims with no deposit. | A-17 says *r* + *f* exceeds 0.81 (p = 0.55). | With a shortfall the general fund receives nothing. It pays under U1-b and not under U1-a (C-43, with `no_change` under U1-a). The payers are recorded per reading (C-24, C-42). |
| Municipal payers, `resources_available_other_uses`, medium | Lower collection and sorting volume saves some cost. | Lost material receipts (C-20). | A-25 (empirical premise, CR-12e): the lost material earned more than its marginal handling cost. | **at_least_one_decrease** for the group (C-45). |
| `buyers.non_returning`, `resources_available_other_uses`, short | — | Deposits not recovered on drinks they keep buying (C-26). | — | **decrease** (C-26). |
| `buyers.returning`, `resources_available_other_uses`, short | — | Deposits outstanding on containers not yet returned, on drinks they keep buying (C-27). | — | **decrease** (C-27). |
| `collectors`, `earnings`, short to medium | Refunds on discarded containers. | Next-best paid uses of the time given up (A-8). | A-8: collectors' next-best uses earn less money (empirical premise). | **increase** (C-8). |
| `redemption_centers`, labor, medium | New centers hire (C-29). | — | New activity: hours cannot substitute for jobs (OC-5, 0.8). | **increase** in `employment` (C-29). |

## 8. Time structure

- **Announcement to enactment (15 January to 30 June 2027).** Regional bottlers' values fall as passage becomes likely (C-25, CR-7c), and so do the values of Calder border store sites, while Penhallow border sites gain (C-38, C-39). Redemption-center operators look for sites, especially within a mile of large stores that want the K4 exemption (C-14, C-15).
- **Mark without deposit (1 January to 31 March 2028).** Purchases rise (C-11), and households and collectors hold marked empties for April (C-10). This is a transfer from the Fund to whoever holds them (C-23, C-40, CR-8b). It ends once pre-April containers have been redeemed: its persistence is limited to the window.
- **First year (from April 2028).** Purchases fall (C-4) as stocks are drawn down and the deposit applies. Redemption points open gradually, so redemption starts low, and the Fund has a surplus (C-3), which frees general-budget money (C-41). Collecting, including from Penhallow, grows as routes and contacts form (C-8, C-9, C-19, C-32). Returning containers becomes a routine for some households over months (TS-8), so the share of containers returned rises, and with it *r*.
- **Medium run.** *r* + *f* may pass the break-even of 0.81 (A-17), and the Fund may need the shortfall rule (C-24, C-42, C-43, U1). Lobbying over the handling fee and over U1 follows (C-16).
- **Expectations.** If Penhallow is expected to adopt its own deposit, cross-border collecting will be expected to be temporary, and investment in it (trucks, contacts) stays small.

## 9. Opportunity costs

**Where each deposit goes (CR-8b).** Every 10 cents paid in at the till ends up with one of four parties, and every refund is paid out of what others paid in.

| What happens to the container | Who pays | Who receives | Net |
|---|---|---|---|
| Returned by its buyer | Buyer (10 cents at the till) | Buyer (10 cents at return); redemption point (2 cents from the Fund) | An interest-free loan from the buyer to the Fund, plus the buyer's time (C-2, C-27). |
| Discarded, collected and returned by someone else | Buyer | Collector (10 cents); redemption point (2 cents) | A transfer from the buyer to the collector (C-8, C-26). |
| Not returned by anyone | Buyer | The Fund, and so the general fund (C-3, C-41) | A tax (C-26). |
| Marked but no deposit paid (Penhallow or pre-April) | The Fund: other buyers' unredeemed deposits, or, after a shortfall, distributors (U1-a) or a group of taxpayers and recipients of other spending (U1-b) (C-24, C-42) | Collector or holder (10 cents, C-40); redemption point (2 cents) | A transfer from the Fund (C-23). |

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-26 | `buyers.non_returning` | `resources_available_other_uses` | decrease | What they would have bought with the deposits they pay and do not recover, on drinks they keep buying. | TX-1, CR-8a, CR-3 |
| C-27 | `buyers.returning` | `resources_available_other_uses` | decrease | At any time, a returning buyer who keeps buying has deposits outstanding on containers bought and not yet returned; that money is held by the Fund. A present sum given up for the same sum later is a loss (LW-7). | CR-3 note, CR-8b, CR-10 |
| C-28 | `officials.revenue` | `enforcement_cost` | increase | Staff for registration, audits and investigation. Paid from the Fund (OC-3, third funding case), so it reduces the surplus swept to the general fund (CR-8d), not general taxpayers' means. | OC-3, CR-8c |
| C-29 | `redemption_centers` | `employment` | increase | Jobs paid from handling fees, which are paid from unredeemed deposits (CR-8b). Centers are a new activity, so `employment` alone is derivable (OC-5, 0.8). | OC-5 |
| C-30 | sellers of what non-returning buyers would have bought | `employment`, `hours_worked` | at_least_one_decrease | The jobs supported by the spending that went into deposits not recovered. | OC-5, OC-1 |

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Retailers charge the deposit as required. | enforcement | 0.95 | It is shown on the receipt; distributors charge it to retailers. | C-1 fails; C-12 loses its charging chain. |
| A-2 | Some containers are returned by their buyers. | other | 0.95 | Return rates under deposits elsewhere; many households buy in multipacks for home use. | C-2, C-21, C-27, C-31 fail; C-12 loses its take-back chain. |
| A-3 | In the first year, redemption points are few and routines new, so *r* + *f* is below 0.81. | expectations | 0.75 | Time to license and open centers; the Act's start date. | C-3, C-41 fail. |
| A-4 | Buyers have exempt or untaxed alternatives they find acceptable (exempt drinks, tap water, fountain drinks). | substitutability | 0.85 | Exemption list. | C-4 shrinks; C-5, C-25, C-34, C-35 fail; C-44 loses its (−) chain. |
| A-5 | Enough border residents can easily shop in Penhallow, and some who do not return containers find 10 cents a container worth the trip. | mobility | 0.65 | 600,000 residents of border counties; Penhallow stores 10 to 15 minutes away; 10 cents is $2.40 on a 24-pack. | C-6, C-17, C-18, C-36 to C-39 fail. |
| A-6 | Buyers differ in what it costs them to return a container (where they drink, distance to a redemption point, value of time, volume). | other | 0.95 | Consumption away from home; locations of redemption points. | C-7 fails. |
| A-7 | Some buyers discard containers that others then collect and redeem. | other | 0.95 | Collection under deposit systems elsewhere; public bins and events. | C-8, C-32, C-23's collector chain fail. |
| A-8 | For most collectors, the time spent collecting would otherwise have earned less money. | alternative_uses | 0.7 | Collectors elsewhere are mostly people with little paid work, and charity volunteers. | C-8 becomes ambiguous (section 7). |
| A-9 | Most containers sold in Penhallow carry the Calder mark, redemption points cannot tell them apart, and detection is low enough that some people bring them in. | enforcement | 0.75 | Shared regional labels; DoR's statement; eight investigators. | C-9, C-19, C-22 and the cross-border chains of C-23 and C-40 fail. |
| A-10 | People learn that marked containers bought before April will be redeemable, and some hold them. | expectations | 0.7 | DoR's public statement; press coverage. | C-10 fails; C-11 keeps only the stock-up chain (A-11); C-40 loses its pre-April chain. |
| A-11 | Covered drinks are storable, and some buyers can bring purchases forward by weeks. | other | 0.75 | Shelf life of canned and bottled drinks. | C-11's stock-up chain fails; C-4's drawdown chain fails. |
| A-12 | For some large stores, arranging for a nearby center costs less than handling returns in the store. | other | 0.65 | Space and labor needed for returns; center operators' interest in sites near large stores. | C-14 fails. |
| A-13 | At some sites, the 2-cent fee and volume cover a center's costs. | alternative_uses | 0.8 | Center costs under deposit systems elsewhere. | C-15, C-29 fail. |
| A-14 | Distributors, large retailers and center operators can organize at a cost below their stakes. | other | 0.8 | Existing beverage and grocery associations; few distributors. | C-16 not reported. |
| A-15 | Shoppers bundle drink purchases with other groceries. | other | 0.7 | Basket data. | C-17, C-18 weaken. |
| A-16 | Many returned and collected containers would otherwise have gone into curbside bins. | other | 0.85 | Curbside participation in Calder municipalities. | C-20, C-45 fail. |
| A-17 | Once redemption points are established, *r* + *f* exceeds 0.81, so the Fund needs the shortfall rule. | other | 0.55 | Redemption of 75% to 90% reported under 10-cent deposits elsewhere, plus claims with no deposit (A-9). | C-24, C-42, C-43 fail; the Fund keeps a surplus; C-44 loses its U1-a chain. |
| A-18 | Regional bottlers have plant specific to the region and sell mostly in Calder. | durability | 0.6 | Plant locations; sales shares. | C-25, C-35 fail; C-44 loses its (−) chain. |
| A-19 | Most non-returning buyers keep buying covered drinks. | other | 0.9 | Consumption of covered drinks. | C-26, C-30 weaken. |
| A-20 | Sellers adjust staffing or hours to their sales. | alternative_uses | 0.75 | Share of part-time staff in retail and services. | C-29, C-30, C-36, C-37 weaken. |
| A-21 | The state's revenue officials, preferring a larger surplus, slow the licensing of redemption centers. | other | 0.3 | No evidence either way; DoR has no stated target. | Below cut-off; not reported. |
| A-22 | Municipal recycling programs make up lost material receipts by raising fees. | revenue_use | 0.45 | Programs could also cut service or draw general funds. | Below cut-off; the payers are recorded only as a group (C-45). |
| A-23 | Most returning buyers keep buying covered drinks. | other | 0.9 | Consumption of covered drinks; multipacks for home use. | C-27 fails (CR-3 note). |
| A-24 | Some sellers can offer covered drinks in exempt forms (open cups, containers over 3 liters) at little extra cost. | substitutability | 0.6 | Exemption list; fountain equipment is common in food service; large bottles exist. | C-33 fails. |
| A-25 | The material lost from curbside bins earned municipal programs more than it cost them, at the margin, to collect and sort; routes run anyway. | other | 0.7 | Aluminum cans are the most valuable part of what programs sell; routes and trucks are fixed in the short run. | C-45 becomes ambiguous. |
| A-26 | For distributors and large stores, the added cost per container of handling deposits and returns exceeds what they receive for the material and in handling fees. | other | 0.6 | Pickup from many dispersed points; glass and plastic of low value; aluminum valuable. Weak evidence. | C-44's (+) chain rests on U1-a alone. |

C-29, C-30, C-36 and C-37 rest on A-20 as well as the assumptions of the chains that lead to them; they are listed in the consequence list.

**Final check (workflow).**
1. *Uncombined chains.* Drink purchases (two windows), the price at the till and the shelf price, bottlers' net price, the Fund's surplus (short and medium), municipal payers, collectors' earnings and redemption-center labor were combined in section 7.
2. *Group signs.* C-30 and C-36 to C-37 are employment-or-hours groups; C-29 is `employment` alone because centers are a new activity (OC-5, 0.8). C-41, C-42 and C-45 are groups over actor classes (CR-8; OC-1).
3. *Baseline.* Every sign is against no deposit. C-2 is a cost against that baseline even though returning a container "pays" against not returning it.
4. *Worse off is not poorer.* C-26 is signed only for non-returning buyers who keep buying (A-19); C-27 only for returning buyers who keep buying (A-23). Collectors are better off by their own ranking (CR-3b); their money earnings rise only on A-8.
5. *Timing shifts.* Purchases are signed per window (C-11, C-4); holding of marked empties (C-10) is limited to its window.
6. *Both sides of every transfer.* The table in section 9; C-20 and C-21 (scrap), with the programs' payers (C-45); C-3 and C-26 (unredeemed deposits), with the beneficiaries of the residual (C-41); C-23 and C-40 (claims with no deposit) with their payers (C-24, C-42, C-43); C-29 and C-30 (handling fees and forgone spending).
7. *Every actor class, every core rule.* CR-7c: regional bottlers (C-25) and border store sites (C-38, C-39); no transferable license is created (K5 is uncapped). CR-7b: bottlers' net price (C-35), the shelf price (C-44). CR-6: the price of empties in Penhallow (C-19); the Fund as a buyer of redemption services at a fixed fee (C-31). CR-9: Penhallow stores, border retail labor, bottlers, recycling programs on both sides. Enforcement and its funding: C-28.
8. *Unstated premises.* Lobbying (A-14); "some actors at the margin" (A-4, A-5, A-11, A-12, A-24); returners who keep buying (A-23); the dominance premises for collectors' earnings (A-8) and municipal payers (A-25); the break-even arithmetic for the Fund (A-3, A-17).

## 11. Report

**The policy.** From 1 April 2028, Calder adds 10 cents to the price of every covered drink container and pays 10 cents to whoever brings an empty to a redemption point. Redemption points also get 2 cents a container. Large stores must take back empties unless a licensed center is within a mile. Deposits that are never claimed go to the state's general fund. Containers must carry the refund mark from 1 January 2028, and any marked container is redeemable, wherever and whenever it was sold. Who pays if refunds exceed deposits is unclear (U1). Penhallow, next door, has no deposit, and its containers carry the same regional labels.

**Visible consequences.** Drinks cost 10 cents a container more at the till (C-1). Buyers who return containers get the money back, but spend time doing it (C-2). In the first year the state collects the deposits that are not claimed (C-3).

**Invisible consequences.**
- *Buyers* buy fewer covered drinks from April (C-4) and more exempt ones (C-5); some near the border buy in Penhallow (C-6). In the first quarter of 2028 they buy more, both to beat the deposit and because containers bought then can be redeemed without a deposit having been paid (C-11). The deposits that no one claims, which are the tax part of the Act, are paid by the buyers for whom returning a container costs most: drinks consumed away from home, buyers far from redemption points, buyers who value their time highly (C-7). Those buyers have less to spend on other things (C-26), and so, by a little, do buyers who return their containers and keep buying, since their deposits are held until they return them (C-27).
- *Collectors*, including people who never buy the drinks, spend more hours collecting (C-32) and earn money redeeming containers that others discard (C-8). Some bring containers from Penhallow (C-9), so empties there gain a price (C-19), and Penhallow's recycling programs lose cans (C-22). People hold marked empties in the first quarter of 2028 to redeem them in April (C-10). Those who redeem containers on which no deposit was paid gain (C-40).
- *Retailers, distributors and bottlers* bear compliance costs (C-12, C-13). Large stores arrange for centers nearby to avoid taking back empties themselves (C-14). Sellers offer more drinks in exempt forms (C-33). New redemption centers open (C-15), sell redemption services (C-31) and hire (C-29), paid from deposits that buyers did not reclaim. The sellers of what those buyers would otherwise have bought employ fewer people or hours (C-30). Penhallow border stores gain customers, store-site value and work (C-17, C-39, C-37). Calder border stores lose the groceries bought on those trips, along with store-site value and work (C-18, C-38, C-36). Regional bottlers supply less for Calder, receive less per unit and lose value (C-34, C-35, C-25). Distributors, retailers and center operators lobby over the Act and the handling fee (C-16).
- *Recycling programs* in Calder lose their most valuable material, which distributors now sell instead (C-20, C-21), and their fee payers, service users or municipal taxpayers bear the loss (C-45).
- *The state* collects less than a projection based on non-return would suggest, because collectors, Penhallow containers and pre-April containers all draw on the Fund (C-23). DoR's costs come out of the Fund (C-28). The first-year residual benefits taxpayers or recipients of other spending (C-41). If redemption and claims without deposits rise above 81% of containers sold (A-17, p = 0.55), the Fund runs short. Then either distributors pay the difference (U1-a, C-24) or the general fund pays it (U1-b, C-43), and in that case taxpayers or recipients of other spending bear it (C-42).

**Ambiguous effects.** Whether the shelf price before the deposit rises or falls (C-44). Whether the general fund gains from the Act once redemption points are established: it gains if the Fund keeps a surplus. If there is a shortfall, it receives nothing under U1-a and pays under U1-b (section 7).

**Key conditions.** Shared labels and weak detection (A-9, p = 0.75) drive the cross-border effects. The Fund's medium-run position turns on arithmetic (break-even at 81%) and on A-17 (p = 0.55), the weakest reported premise. The first-quarter windfall rests on DoR's decision not to separate pre-April containers (A-10).

**What this analysis cannot say.** How large any effect is, including how many containers are returned or brought in from Penhallow. Environmental effects (litter, recycling, materials), which are the Act's purpose and out of scope for version 1. Whether the time buyers spend returning containers is worth what the Act aims at. Whether the policy is a good idea.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.calder | price_paid (covered drinks, incl. deposit) | increase | short | visible | B | CR-1 op 3; arithmetic; CR-12e | A-1 |
| C-2 | buyers.returning | wait_time (returning containers) | increase | short | visible | B | CR-4, CR-8c, OC-2 | A-2 |
| C-3 | state_budget (residual_claimant) | non_tax_receipts (Fund surplus, first year) | increase | short | visible | B | CR-8b; CR-12e | A-3 |
| C-4 | buyers.calder | quantity_traded (covered drinks, from April 2028) | decrease | short | invisible | B | CR-4c, CR-10a | A-4, A-11 |
| C-5 | buyers.calder | quantity_substitute (exempt drinks) | increase | short | invisible | B | RS-1 | A-4 |
| C-6 | buyers.non_returning (border) | cross_border_purchases | increase | short | invisible | B | RS-4 | A-5 |
| C-7 | buyers.high_return_cost | tax_share_borne | increase | short | invisible | B | CR-4, CR-8b | A-6 |
| C-8 | collectors | earnings (from redemption) | increase | short–medium | invisible | B | CR-1 op 3, CR-3b, CR-4, CR-7a | A-7, A-8 |
| C-9 | collectors.cross_border | legal_breach (Penhallow containers redeemed) | increase | short–medium | invisible | B | RS-3, RS-4, CR-4 | A-9 |
| C-10 | households, collectors | inventory_held (marked empties, Jan–Mar 2028) | increase | short | invisible | B | RS-8, CR-10a | A-10 |
| C-11 | buyers.calder | quantity_traded (covered drinks, Jan–Mar 2028) | increase | short | invisible | B | RS-8, CR-10a | A-10, A-11 |
| C-12 | retailers.calder | compliance_cost | increase | short | invisible | B | TX-5, CR-8c; CR-12d | A-1, A-2 |
| C-13 | distributors | compliance_cost | increase | short | invisible | A | TX-5, CR-8c | none |
| C-14 | retailers.calder (large) | reclassification (center within one mile) | increase | short–medium | invisible | B | RS-5 | A-12 |
| C-15 | redemption_centers | entry_rate | increase | short | visible | B | CR-1 op 2, CR-7 | A-13 |
| C-16 | distributors, retailers.calder, redemption_centers | lobbying_effort | increase | medium | invisible | B | RS-7 | A-14 |
| C-17 | retailers.penhallow.border | quantity_traded (all goods) | increase | short | invisible | B | RS-4, RS-9 | A-5, A-15 |
| C-18 | retailers.calder (border) | quantity_traded (other groceries on drink trips) | decrease | short | invisible | B | RS-9 | A-5, A-15 |
| C-19 | holders_of_empties.penhallow | net_price_received (marked empties) | increase | short–medium | invisible | B | CR-9, CR-7a | A-9 |
| C-20 | recycling_programs.calder | quantity_traded (scrap sold) | decrease | short–medium | invisible | B | CR-9, CR-4 | A-16 |
| C-21 | distributors | quantity_traded (scrap from returned containers) | increase | short | invisible | B | CR-8b, CR-9 | A-2 |
| C-22 | recycling_programs.penhallow | quantity_traded (aluminum scrap sold) | decrease | short–medium | invisible | B | CR-9 | A-9 |
| C-23 | officials.revenue, state_budget | tax_revenue_vs_static_projection | decrease | short | invisible | B | CR-8b, arithmetic; CR-12d | A-7 |
| C-24 | distributors | resources_available_other_uses (shortfall assessment) | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-8b; U1-a: CR-1 op 3, CR-3 note; CR-8 | A-17 |
| C-25 | bottlers.regional | asset_value | decrease | short | invisible | B | CR-7c, CR-10c | A-4, A-18 |
| C-26 | buyers.non_returning | resources_available_other_uses | decrease | short | invisible | B | TX-1, CR-8a, CR-3 | A-19 |
| C-27 | buyers.returning | resources_available_other_uses | decrease | short | invisible | B | CR-3 note, CR-8b, CR-10, LW-7 | A-2, A-23 |
| C-28 | officials.revenue | enforcement_cost | increase | short | invisible | A | OC-3, CR-8c | none |
| C-29 | redemption_centers | employment | increase | medium | visible | B | OC-5 (new activity) | A-13, A-20 |
| C-30 | sellers (forgone purchases) | employment, hours_worked | at_least_one_decrease | medium | invisible | B | OC-5, OC-1 | A-19, A-20 |
| C-31 | redemption_centers, large retailers (redemption points) | quantity_traded (redemption services) | increase | short–medium | visible | B | CR-1 op 3, CR-4, CR-5, CR-6 | A-2 |
| C-32 | collectors | hours_worked (collecting) | increase | short–medium | invisible | B | CR-4, CR-8a | A-7 |
| C-33 | sellers.covered_drinks | reclassification (open cups, containers over 3 liters) | increase | short–medium | invisible | B | RS-5, CR-4 | A-24 |
| C-34 | bottlers.regional | quantity_supplied (covered drinks for Calder) | decrease | short–medium | invisible | B | CR-9, LW-10 | A-4 |
| C-35 | bottlers.regional | net_price_received | decrease | short–medium | invisible | B | CR-7b, CR-9 | A-4, A-18 |
| C-36 | workers, Calder border retail | employment, hours_worked | at_least_one_decrease | short–medium | invisible | B | OC-5, CR-9, LW-10 | A-5, A-20 |
| C-37 | workers, Penhallow border retail | employment, hours_worked | at_least_one_increase | short–medium | invisible | B | OC-5, CR-9, LW-10 | A-5, A-20 |
| C-38 | retailers.calder (border) | asset_value (store sites) | decrease | short | invisible | B | CR-7c, CR-10c | A-5 |
| C-39 | retailers.penhallow.border | asset_value (store sites) | increase | short | invisible | B | CR-7c, CR-10c | A-5 |
| C-40 | claimants.no_deposit | resources_available_other_uses | increase | short–medium | invisible | B | CR-1 op 3, CR-8b; CR-12d | A-9, A-10 |
| C-41 | taxpayers, recipients of other spending | resources_available_other_uses (first-year residual) | at_least_one_increase | short | invisible | B | CR-8b, CR-8d | A-3 |
| C-42 | taxpayers, recipients of other spending | resources_available_other_uses (Fund shortfall) | U1-a: no_change; U1-b: at_least_one_decrease | medium | invisible | B | CR-8b, CR-8, OC-1 | A-17 |
| C-43 | state_budget | subsidy_outlay (meeting the Fund's shortfall) | U1-a: no_change; U1-b: increase | medium | invisible | B | CR-8b, CR-8 | A-17 |
| C-44 | buyers.calder | price_paid (shelf price excluding the deposit) | ambiguous | short–medium | invisible | B | CR-7b, CR-6; CR-12b | A-4, A-18, A-26 |
| C-45 | municipal fee payers, service users, municipal taxpayers | resources_available_other_uses | at_least_one_decrease | medium | invisible | B | CR-8b, OC-1, CR-12e | A-16, A-25 |

## Corrections after the core-only comparison

Changed under catalog 0.8, after checking each comparison row against the core rules:
- **C-35 added (sellers' net price).** The 0.6 version left it unsigned and misread CR-7b. CR-7b signs each side's direction and needs a comparison of alternatives only to rank the shares. With A-18, bottlers' `net_price_received` decreases. C-44 now records the shelf price before the deposit as `ambiguous` instead of "not signed", following CR-12 (0.8, kind 2), with A-26.
- **C-24 split; C-42 and C-43 added.** Under U1-b the 0.6 version signed `taxpayers` decrease by TX-1 and OC-1. The payers from the general budget are a group (CR-8 0.7; OC-1 and TX-1 0.8). C-24 now covers distributors only (U1-a: decrease; U1-b: no_change). C-42 records the group per reading, with `at_least_one_decrease` under U1-b. C-43 records the general fund's outlay per reading.
- **C-3.** The variable is now `non_tax_receipts` (unredeemed deposits are not taxes). C-9 now uses `legal_breach`. K1 is now the instrument `deposit_refund`. The refund is now CR-1 operation 3 attached to the container (0.8), not operation 2.
- **C-29.** Now `employment` alone, because centers are a new activity (OC-5, 0.8).
- **C-27.** The premise A-23 (returning buyers keep buying) is now explicit; before, it was hidden.
- **C-12.** Now Tier B with A-1 and A-2. Charging depends on compliance, and take-back depends on returns.
- **Omissions added:** C-31 (redemption services), C-32 (collectors' hours), C-33 (exempt forms, A-24), C-34 (bottlers' output), C-36 and C-37 (border retail labor), C-38 and C-39 (border store sites), C-40 (no-deposit claimants), C-41 (beneficiaries of the first-year residual).
- **C-45 added (municipal payers as a group).** The comparison classed this core row A. 0.8 now settles the form: OC-1's group of payers from a budget means no single payer needs naming, which was the 0.6 reason for declining. The remaining premise, A-25, is drawn from the record.

Comparison conclusions rejected or not applied:
- **C-13 (Tier A): kept.** Distributors' registration and monthly returns are required whether or not any container is returned, so TX-5 gives Tier A for that chain alone (CR-12d).
- **Core C-3, C-4 and C-50 (Fund flows; charities through the gift relation): not applied.** These are J rows. The pattern version records the Fund through its residual and the section 9 table, and folds charities into collectors (C-8).
- **Core C-18 (retailers stock up before April) and C-31 (distributors' return on capital): not applied.** These are A rows resting on premises that the record does not decide (A-N1) or whose evidence is weak (A-N5 as a dominance premise), and 0.8 does not settle them.
- **Core C-2/C-10/C-11 split of returning time by variable and horizon: not applied.** These are V rows. C-2 covers the same claim.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or a pattern, including the conditional direction of the transfer (CR-1, CR-4 per container), the residual claimant (CR-8b), payments with no deposit behind them (CR-8b), the price of empties across the border (CR-7a) and the Fund's break-even (CR-12e, arithmetic).

**(b) Unclear core rules (wording that was hard to apply here).**
- *CR-1, operations 3 and 4* (closed in 0.7 and 0.8: a charge paid only when an option is taken is operation 3, and a refund attached to a thing is operation 3 on the option of returning it, for anyone who holds it).
- *CR-1, Recording: splitting a class* (closed in 0.7: where every member faces the same operation but responds differently, split the class by response).
- *CR-8b with a residual claimant* (closed in 0.7: CR-8's clarification on residual claimants, the actor class `residual_claimant` and the variable `fund_balance`).
- *OC-2 and CR-8c against two baselines.* Returning a container is time that "buys" 10 cents against not returning, and buys nothing against no deposit. CR-8c lists queuing "because of" a policy as used up; it was applied against the no-policy baseline (C-2), as 2.5 requires, but the wording of OC-2 ("buys nothing they value for its own sake") invites the other baseline. Still open.
- *2.5, readings* (closed in 0.7: `no_change` lets each class have its own row with a sign per reading; C-24, C-42, C-43).

**(c) Missing patterns (derived here, likely to recur).**
- *P-027-1 Refundable charge (deposit-refund).* If: a payment is attached to buying a good, and a refund of up to the same amount is paid to whoever later performs an act (returning it, completing a course, leaving a site clean), with the unclaimed balance kept by a named party. Then: (i) per unit, the charge ends as a tax where no one claims it, as a loan where the payer claims it, and as a transfer where a third party does (CR-1 op 3, CR-8b); (ii) the unclaimed part is borne by those for whom claiming costs most (CR-4, per unit) (`tax_share_borne`); (iii) the good's full cost rises for every buyer, including those who claim (CR-4c, LW-7); (iv) third parties enter to claim refunds others abandon, and the item acquires a market value of up to the refund less the cost of claiming (CR-1 op 3, CR-7a); (v) the residual claimant's receipt falls as claims rise and can turn negative, so its sign needs arithmetic on the case's figures (CR-8b, CR-12e), and its beneficiaries or payers from a general budget are a group (CR-8). Derivation: CR-1, CR-4, CR-7a, CR-8b, CR-12e. Recurs for bonds on returnable equipment, tenancy deposits set by law, deposits on batteries, tires and propane cylinders, and cleanup bonds. The instrument `deposit_refund` was added in 0.7; the pattern remains a candidate.
- *P-027-2 A claim payable inside a boundary draws claims from outside* (closed in 0.7: RS-4's sentence on payments that depend on an item crossing the boundary).
- *P-027-3 A claim that starts before the charge* (closed in 0.7: RS-8's *Unless* clause on claims acquired before the charge that funds them).

**(d) Vocabulary (what the ontology lacks).**
- *Instrument type* (closed in 0.7: `deposit_refund`). K4, an obligation to buy back empties, is a forced exchange with no instrument type (2.3's triangular types all prohibit, cap or mandate a contract term; none compels an exchange). Still open.
- *Signs* (closed in 0.7: `no_change`).
- *Variables.* (1) Unredeemed deposits (closed in 0.7: `non_tax_receipts`). (2) A fund's balance (closed in 0.7: `fund_balance`). (3) `earnings` is defined for a group's total money earnings; C-8 needed earnings from one source (collection), which the definition does not separate. Still open.
- *Actor classes.* Residual claimants (closed in 0.7: `residual_claimant`). The generic list in 2.2 still has no class for third parties who claim a payment created by the policy without being party to the taxed exchange (collectors, no-deposit claimants).
- *Relation types.* None missing: `input_to` (containers to recycling) and `across_border` (empties) sufficed.
