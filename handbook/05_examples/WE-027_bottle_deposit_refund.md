# WE-027 Ten-cent deposit on beverage containers, refunded on return

Analyst: draft (Handbook 0.6)  |  Rule catalog version: 0.6  |  Status: awaiting expert review

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
| K1 Deposit and refund | No type in 2.3; recorded as a `per_unit_tax` with a refund conditional on a later action (section 2) | Covered beverages (soft drinks, water, beer, malt drinks, juice, sports and energy drinks) in sealed glass, metal or plastic containers of 3 liters or less | Distributors pay 10 cents into the Beverage Container Fund on each container sold to a Calder retailer; retailers must charge the buyer 10 cents a container, shown separately on the receipt; any redemption point pays 10 cents for each empty container bearing the mark "CL 10¢". | 10 cents per container. | Milk and plant milks, wine, spirits, infant formula, containers over 3 liters, drinks served in open cups. |
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
| K1 | Binary, in both directions: a forced payment to the Fund on every purchase, and a payment from the Fund to whoever returns the container. Per container, the net is a tax if no one returns it, a transfer from the buyer to a collector if someone else does, and an interest-free loan to the Fund if the buyer does. | Yes (A-1) | TX (TX-1, TX-5 apply; TX-2's wedge applies only in part, see section 4); RS; derived from CR-1, CR-4, CR-8 |
| K2 | Binary: the state is the residual claimant. | Yes | CR-8b |
| K3 | Binary: a per-unit payment to redemption points, funded by the unredeemed deposits. | Yes | SB (SB-1's two sides through CR-8b) |
| K4 | Triangular: forces large retailers to buy empties from the public at 10 cents (reimbursed, with the 2-cent fee). | Yes for stores without a center nearby | CR-1, CR-5b, RS-5 |
| K5 | Adds an option (CR-1 op 2); not restrictive. | — | CR-7 |

**CR-1 operations by actor class.** The counterfactual law has no deposit; empties have only scrap value (about 1 cent for a can at a scrap yard, nothing for most plastic).

| Actor class | Operations |
|---|---|
| `buyers.calder` | Op 3 on buying a covered drink: a 10-cent payment is attached. Op 2: a new option, returning the empty for 10 cents. Whether, for a given container, the buyer ends up taxed or lending depends on which option they later choose. The operations are the same for every buyer; the classes `buyers.returning` and `buyers.non_returning` are defined by that later choice, per container, not per person (see Gaps found, (b)). |
| `collectors` (anyone, including people who never buy covered drinks) | Op 2: redeeming containers that others discard. |
| `holders_of_empties.penhallow` | In effect op 2 (a Calder redemption point will pay for marked containers), with op 3 attached: the risk of a penalty for knowingly redeeming them. |
| `retailers.calder` | Op 3: collecting and showing deposits. Large stores without a center nearby: op 3, taking back empties (K4). |
| `distributors` | Op 3: remitting deposits, filing returns, collecting empties. Op 2: selling the material from returned containers. U1-a only: op 4, assessment for a Fund shortfall. |
| `redemption_centers` | Op 2: a new line of business, paid by handling fees. |
| `state_budget`, `taxpayers` | Op 4: the state receives the Fund's surplus. U1-b only: taxpayers fund a shortfall. |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `buyers.calder` | Everyone buying covered drinks in Calder | Pay 10 cents more per container at the till; may return it for 10 cents. |
| `buyers.returning`, `buyers.non_returning` | Buyers, for the containers they return and for those they do not | Per container: a loan repaid at the cost of the return trip, or a 10-cent charge. |
| `buyers.high_return_cost`, `buyers.low_return_cost` | Buyers whose cost of returning a container is high (drinks consumed away from home, small volumes, far from a redemption point, high value of time) or low | Who bears the tax part of K1. |
| `collectors` | People who collect discarded containers and redeem them: informal collectors, charities and youth groups running bottle drives | A new source of income. |
| `collectors.cross_border` | People who bring empties from Penhallow | A refund for containers on which no deposit was paid, at a legal risk. |
| `holders_of_empties.penhallow` | Penhallow households, bars and restaurants | Their empties gain a buyer. |
| `retailers.calder` (large, small, border) | Shops selling covered drinks | Compliance; large stores take back empties; border stores lose some customers. |
| `retailers.penhallow.border` (`neighboring_jurisdictions`) | Penhallow stores near the line | Gain some Calder customers. |
| `distributors` | Register, remit deposits, collect empties | Compliance; own returned material; U1-a: pay any shortfall. |
| `redemption_centers` | New licensed centers | Paid 2 cents a container. |
| `bottlers.regional` (`factor_owners.specific`) | Bottlers and brewers with plants specific to the region and most sales in Calder | Lower demand in Calder. |
| `sellers.substitutes` | Sellers of exempt drinks | More demand. |
| `recycling_programs.calder`, `recycling_programs.penhallow` | Municipal curbside programs | Lose the most valuable material. |
| `officials.revenue`, `state_budget`, `taxpayers` | DoR, the general fund and its funders | New administration; the residual; U1-b: shortfalls. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.calder` | `price_paid` (covered drinks, including the deposit, at the till) | increase | short | CR-1 op 3; arithmetic (the deposit is charged on top of the shelf price by law) | A-1 |
| C-2 | `buyers.returning` | `wait_time` (time spent storing, sorting, carrying and queuing to return containers) | increase | short | CR-4, CR-8c, OC-2 | A-2 |
| C-3 | `state_budget` | `tax_revenue` (Fund surplus swept to the general fund; first year) | increase | short | CR-8b with K2; CR-12e (arithmetic: *r* + *f* below 0.81 in the first year) | A-3 |

C-1 is the price at the till. Whether the shelf price before the deposit falls (sellers absorbing part of it) is not signed: TX-2's wedge needs a comparison of alternatives that the case does not supply (CR-7b), and for buyers who return their containers the deposit is not a wedge at all, since it comes back.

C-2: compared with no deposit, a buyer who returns a container pays 10 cents and gets 10 cents back, so the time spent returning it is a cost with nothing to show for it against the counterfactual. Against not returning, it buys 10 cents. Both statements are true; the sign is against the counterfactual (2.5).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `buyers.calder` | `quantity_traded` (covered drinks in Calder; from 1 April 2028) | decrease | short | CR-4c (the full cost of a container rises for every buyer: 10 cents if not returned, the return trip and the wait for the refund if returned); CR-10a (stocks bought in the first quarter are drawn down, C-11) | A-4, A-11 |
| C-5 | `buyers.calder` | `quantity_substitute` (exempt drinks: milk, wine, spirits, fountain drinks, containers over 3 liters, home carbonation) | increase | short | RS-1 | A-4 |
| C-6 | `buyers.non_returning` near the border | `cross_border_purchases` (covered drinks bought in Penhallow) | increase | short | RS-4 | A-5 |
| C-7 | `buyers.high_return_cost` | `tax_share_borne` (relative to `buyers.low_return_cost`) | increase | short | CR-4 (a buyer returns a container when 10 cents exceeds their cost of returning it, so the containers not returned are those of buyers with high return costs); CR-8b | A-6 |
| C-8 | `collectors` | `earnings` (from redeeming containers others discard) | increase | short to medium | CR-1 op 2, CR-3b; CR-4 (x: next-best use of the time, y: collecting); CR-7a (collecting spreads to wherever discarded containers are found) | A-7, A-8 |
| C-9 | `collectors.cross_border` | `informal_activity` (Penhallow containers redeemed in Calder) | increase | short to medium | RS-3, RS-4; CR-4 (x: comply, y: violate) | A-9 |
| C-10 | households and `collectors` | `inventory_held` (marked empty containers held unredeemed, 1 January to 31 March 2028) | increase | short | CR-10a (a marked container will be worth 10 cents from April, with no deposit paid on it) | A-10 |
| C-11 | `buyers.calder` | `quantity_traded` (covered drinks in Calder; window 1 January to 31 March 2028) | increase | short | RS-8; CR-10a: buyers who expect not to return stock up before the deposit, and every marked container bought in the window is redeemable from April without a deposit having been paid | A-10, A-11 |
| C-12 | `retailers.calder` | `compliance_cost` (charging and showing deposits, records; for large stores, taking back, storing and counting empties) | increase | short | TX-5, CR-8c | none |
| C-13 | `distributors` | `compliance_cost` (registration, monthly returns, labels, pickup of empties) | increase | short | TX-5, CR-8c | none |
| C-14 | `retailers.calder` (large) | `reclassification` (arranging for a licensed center within one mile, to fall under K4's exemption) | increase | short to medium | RS-5 | A-12 |
| C-15 | `redemption_centers` | `entry_rate` | increase | short | CR-1 op 2, CR-7 (resources move to the new use while its yield exceeds others) | A-13 |
| C-16 | `distributors`, `retailers.calder`, `redemption_centers` | `lobbying_effort` (distributors and retailers for repeal, a lower deposit or narrower coverage; centers for a higher handling fee; distributors for reading U1-b) | increase | medium | RS-7 | A-14 |

C-4 and C-11 are the same activity in two windows, as 2.5 requires. In the first quarter of 2028, purchases rise against the counterfactual for two reasons that push the same way: buyers who do not expect to return containers stock up before the deposit (RS-8), and every container bought in that window carries the mark but no deposit, so it can be redeemed in April for 10 cents that no one paid in. From April, purchases fall: stocks bought in the first quarter are drawn down, and the deposit raises the full cost of every container for every buyer (C-4). Both chains of C-4 push down, so no combination is needed.

C-7 is the incidence of the tax part of K1. By CR-4, applied per container, a container is returned when its refund exceeds its owner's cost of returning it. The containers that are not returned, whose deposits are the tax, are therefore those of buyers for whom returning costs most: drinks consumed away from home, buyers far from a redemption point, buyers who value their time highly, and buyers of a single can. This is a statement about who bears the tax among buyers; it says nothing about how the burden splits between buyers and sellers (section 7).

C-8: anyone may redeem a marked container, so collectors take up containers that buyers discard. For them the Act only adds an option (CR-3b). Their money earnings rise if the time they spend collecting would otherwise have earned less money (A-8). Where a collector redeems a container that its buyer discarded, the buyer's 10 cents go to the collector instead of to the state (CR-8b, section 9).

C-9: most containers sold in Penhallow carry the Calder mark, and redemption points cannot tell them apart. For Penhallow empties, collecting and carrying them to a Calder redemption point yields 10 cents less transport and expected penalty, against about 1 cent at a scrap yard. CR-4 (x: comply, y: violate) gives the direction; A-9 is the premise that detection is low enough.

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
| C-24 | payers of a Fund shortfall: `distributors` under U1-a, `taxpayers` under U1-b | `resources_available_other_uses` | U1-a: decrease; U1-b: decrease | medium | CR-8b (refunds and fees beyond the Fund's receipts are paid by someone); U1-a: CR-1 op 4 on distributors; U1-b: TX-1, OC-1 | — | A-17 |
| C-25 | `bottlers.regional` | `asset_value` (plants and firms) | decrease | short | CR-7c, CR-10c (lower expected sales in Calder, C-4, from when the Act became expected) | — | A-4, A-18 |

C-20 and C-21 are two sides of one move (CR-8b, CR-9). Without the Act, cans and bottles went into curbside bins, and municipal programs sold the material; now the containers returned or collected are picked up by distributors, who sell it. What the programs lose in material, distributors gain. How the programs make up the lost receipts (higher fees, less service or general funds) needs a premise; A-22 (fees rise, p = 0.45) is below the cut-off, so no consequence is reported for it.

C-23: a static projection of the Fund multiplies deposits sold by a projected rate of non-return. Every container redeemed by a collector in place of its discarding buyer, every Penhallow container and every pre-April container is paid out of the Fund, so the surplus is below that projection. Each chain is enough on its own (CR-12d); A-7 (p = 0.95) is listed as the premise of the strongest.

C-24 depends on U1 for *who* pays, not for the sign: the reading changes the actor class. A-17 (p = 0.55) is the premise that *r* + *f* exceeds 0.81 once redemption points are established (break-even, section 1). 2.5 gives each reading its own sign but not its own actor class, so C-24 names both (Gaps found, (b)).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `buyers.calder`, `quantity_traded` (covered drinks), from April 2028, short | None | Full cost of every container rises (C-4); first-quarter stocks drawn down (C-11). | — | **decrease** (C-4). |
| `buyers.calder`, `quantity_traded`, first quarter 2028 | Stocking up before the deposit; containers bought then are redeemable without a deposit. | None | — | **increase** (C-11). |
| `state_budget`, `tax_revenue` (Fund surplus), short | Deposits on containers not yet returned while redemption points open (A-3). | Payments on containers with no deposit (C-23); handling fees; DoR costs. | Arithmetic: *r* + *f* below 0.81 in the first year (A-3, CR-12e). | **increase** (C-3). |
| `state_budget`, `tax_revenue` (Fund surplus), medium | Deposits not redeemed. | Refunds, fees and claims with no deposit. | A-17 says *r* + *f* exceeds 0.81 (p = 0.55). | **Not signed.** With a shortfall, the general fund receives nothing under U1-a (no change, for which the sign list has no value) and pays under U1-b (C-24). |
| Sellers of covered drinks, `net_price_received`, short | — | Lower quantity demanded (C-4) puts pressure on the shelf price before deposit. | No premise compares buyers' and sellers' alternatives (CR-7b). | **Not signed.** |
| `buyers.non_returning`, `resources_available_other_uses`, short | — | Deposits not recovered on drinks they keep buying (C-26). | — | **decrease** (C-26). |
| `collectors`, `earnings`, short to medium | Refunds on discarded containers. | Next-best paid uses of the time given up (A-8). | A-8: collectors' next-best uses earn less money (empirical premise). | **increase** (C-8). |

## 8. Time structure

- **Announcement to enactment (15 January to 30 June 2027).** Regional bottlers' values fall as passage becomes likely (C-25, CR-7c). Redemption-center operators look for sites, especially within a mile of large stores that want the K4 exemption (C-14, C-15).
- **Mark without deposit (1 January to 31 March 2028).** Purchases rise (C-11), and households and collectors hold marked empties for April (C-10). This is a transfer from the Fund to whoever holds them (C-23, CR-8b). It ends once pre-April containers have been redeemed: its persistence is limited to the window.
- **First year (from April 2028).** Purchases fall (C-4) as stocks are drawn down and the deposit applies. Redemption points open gradually, so redemption starts low, and the Fund has a surplus (C-3). Collecting, including from Penhallow, grows as routes and contacts form (C-8, C-9, C-19). Returning containers becomes a routine for some households over months (TS-8), so the share of containers returned rises, and with it *r*.
- **Medium run.** *r* + *f* may pass the break-even of 0.81 (A-17), and the Fund may need the shortfall rule (C-24, U1). Lobbying over the handling fee and over U1 follows (C-16).
- **Expectations.** If Penhallow is expected to adopt its own deposit, cross-border collecting will be expected to be temporary, and investment in it (trucks, contacts) stays small.

## 9. Opportunity costs

**Where each deposit goes (CR-8b).** Every 10 cents paid in at the till ends up with one of four parties, and every refund is paid out of what others paid in.

| What happens to the container | Who pays | Who receives | Net |
|---|---|---|---|
| Returned by its buyer | Buyer (10 cents at the till) | Buyer (10 cents at return); redemption point (2 cents from the Fund) | An interest-free loan from the buyer to the Fund, plus the buyer's time (C-2, C-27). |
| Discarded, collected and returned by someone else | Buyer | Collector (10 cents); redemption point (2 cents) | A transfer from the buyer to the collector (C-8, C-26). |
| Not returned by anyone | Buyer | The Fund, and so the general fund (C-3) | A tax (C-26). |
| Marked but no deposit paid (Penhallow or pre-April) | The Fund: other buyers' unredeemed deposits, or, after a shortfall, distributors or taxpayers (C-24) | Collector or holder (10 cents); redemption point (2 cents) | A transfer from the Fund (C-23). |

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-26 | `buyers.non_returning` | `resources_available_other_uses` | decrease | What they would have bought with the deposits they pay and do not recover, on drinks they keep buying. | TX-1, CR-8a, CR-3 |
| C-27 | `buyers.returning` | `resources_available_other_uses` | decrease | At any time, a returning buyer has deposits outstanding on containers bought and not yet returned; that money is held by the Fund. A present sum given up for the same sum later is a loss (LW-7). | CR-8b, CR-10 |
| C-28 | `officials.revenue` | `enforcement_cost` | increase | Staff for registration, audits and investigation. Paid from the Fund (OC-3, third funding case), so it reduces the surplus swept to the general fund (CR-8d), not general taxpayers' means. | OC-3, CR-8c |
| C-29 | `redemption_centers` | `employment`, `hours_worked` | at_least_one_increase | Jobs paid from handling fees, which are paid from unredeemed deposits (CR-8b). | OC-5 |
| C-30 | sellers of what non-returning buyers would have bought | `employment`, `hours_worked` | at_least_one_decrease | The jobs supported by the spending that went into deposits not recovered. | OC-5, OC-1 |

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Retailers charge the deposit as required. | enforcement | 0.95 | It is shown on the receipt; distributors charge it to retailers. | C-1 fails. |
| A-2 | Some containers are returned by their buyers. | other | 0.95 | Return rates under deposits elsewhere; many households buy in multipacks for home use. | C-2, C-21, C-27 fail. |
| A-3 | In the first year, redemption points are few and routines new, so *r* + *f* is below 0.81. | expectations | 0.75 | Time to license and open centers; the Act's start date. | C-3 fails. |
| A-4 | Buyers have exempt or untaxed alternatives they find acceptable (exempt drinks, tap water, fountain drinks). | substitutability | 0.85 | Exemption list. | C-4 shrinks; C-5, C-25 fail. |
| A-5 | Enough border residents can easily shop in Penhallow, and some who do not return containers find 10 cents a container worth the trip. | mobility | 0.65 | 600,000 residents of border counties; Penhallow stores 10 to 15 minutes away; 10 cents is $2.40 on a 24-pack. | C-6, C-17, C-18 fail. |
| A-6 | Buyers differ in what it costs them to return a container (where they drink, distance to a redemption point, value of time, volume). | other | 0.95 | Consumption away from home; locations of redemption points. | C-7 fails. |
| A-7 | Some buyers discard containers that others then collect and redeem. | other | 0.95 | Collection under deposit systems elsewhere; public bins and events. | C-8, C-23's collector chain fail. |
| A-8 | For most collectors, the time spent collecting would otherwise have earned less money. | alternative_uses | 0.7 | Collectors elsewhere are mostly people with little paid work, and charity volunteers. | C-8 becomes ambiguous (section 7). |
| A-9 | Most containers sold in Penhallow carry the Calder mark, redemption points cannot tell them apart, and detection is low enough that some people bring them in. | enforcement | 0.75 | Shared regional labels; DoR's statement; eight investigators. | C-9, C-19, C-22 and C-23's cross-border chain fail. |
| A-10 | People learn that marked containers bought before April will be redeemable, and some hold them. | expectations | 0.7 | DoR's public statement; press coverage. | C-10 fails; C-11 keeps only the stock-up chain (A-11). |
| A-11 | Covered drinks are storable, and some buyers can bring purchases forward by weeks. | other | 0.75 | Shelf life of canned and bottled drinks. | C-11's stock-up chain fails; C-4's drawdown chain fails. |
| A-12 | For some large stores, arranging for a nearby center costs less than handling returns in the store. | other | 0.65 | Space and labor needed for returns; center operators' interest in sites near large stores. | C-14 fails. |
| A-13 | At some sites, the 2-cent fee and volume cover a center's costs. | alternative_uses | 0.8 | Center costs under deposit systems elsewhere. | C-15, C-29 fail. |
| A-14 | Distributors, large retailers and center operators can organize at a cost below their stakes. | other | 0.8 | Existing beverage and grocery associations; few distributors. | C-16 not reported. |
| A-15 | Shoppers bundle drink purchases with other groceries. | other | 0.7 | Basket data. | C-17, C-18 weaken. |
| A-16 | Many returned and collected containers would otherwise have gone into curbside bins. | other | 0.85 | Curbside participation in Calder municipalities. | C-20 fails. |
| A-17 | Once redemption points are established, *r* + *f* exceeds 0.81, so the Fund needs the shortfall rule. | other | 0.55 | Redemption of 75% to 90% reported under 10-cent deposits elsewhere, plus claims with no deposit (A-9). | C-24 fails; the Fund keeps a surplus. |
| A-18 | Regional bottlers have plant specific to the region and sell mostly in Calder. | durability | 0.6 | Plant locations; sales shares. | C-25 fails. |
| A-19 | Most non-returning buyers keep buying covered drinks. | other | 0.9 | Consumption of covered drinks. | C-26, C-30 weaken. |
| A-20 | Sellers adjust staffing or hours to their sales. | alternative_uses | 0.75 | Share of part-time staff in retail and services. | C-29, C-30 weaken. |
| A-21 | The state's revenue officials, preferring a larger surplus, slow the licensing of redemption centers. | other | 0.3 | No evidence either way; DoR has no stated target. | Below cut-off; not reported. |
| A-22 | Municipal recycling programs make up lost material receipts by raising fees. | revenue_use | 0.45 | Programs could also cut service or draw general funds. | Below cut-off; not reported. |

C-29 and C-30 rest on A-20 as well as the assumptions of the chains that lead to them; they are listed in the consequence list.

**Final check (workflow).**
1. *Uncombined chains.* Drink purchases (two windows), the Fund's surplus (short and medium), collectors' earnings and sellers' net price were combined in section 7.
2. *Group signs.* C-29 and C-30 are employment-or-hours groups.
3. *Baseline.* Every sign is against no deposit. C-2 is a cost against that baseline even though returning a container "pays" against not returning it.
4. *Worse off is not poorer.* C-26 is signed only for buyers who keep buying (A-19); C-27 for returning buyers, who keep deposits outstanding. Collectors are better off by their own ranking (CR-3b); their money earnings rise only on A-8.
5. *Timing shifts.* Purchases are signed per window (C-11, C-4); holding of marked empties (C-10) is limited to its window.
6. *Both sides of every transfer.* The table in section 9; C-20 and C-21 (scrap); C-3 and C-26 (unredeemed deposits); C-23 and C-24 (claims with no deposit and their payers); C-29 and C-30 (handling fees and forgone spending).
7. *Every actor class, every core rule.* CR-7c: regional bottlers (C-25); no transferable license is created (K5 is uncapped). CR-6: the price of empties in Penhallow (C-19). CR-9: Penhallow stores, recycling programs on both sides. Enforcement and its funding: C-28.
8. *Unstated premises.* Lobbying (A-14); "some actors at the margin" (A-4, A-5, A-11, A-12); the dominance premise for collectors' earnings (A-8); the break-even arithmetic for the Fund (A-3, A-17).

## 11. Report

**The policy.** From 1 April 2028, Calder adds 10 cents to the price of every covered drink container and pays 10 cents to whoever brings an empty to a redemption point. Redemption points also get 2 cents a container. Large stores must take back empties unless a licensed center is within a mile. Deposits that are never claimed go to the state's general fund. Containers must carry the refund mark from 1 January 2028, and any marked container is redeemable, wherever and whenever it was sold. Who pays if refunds exceed deposits is unclear (U1). Penhallow, next door, has no deposit, and its containers carry the same regional labels.

**Visible consequences.** Drinks cost 10 cents a container more at the till (C-1). Buyers who return containers get the money back, but spend time doing it (C-2). In the first year the state collects the deposits that are not claimed (C-3).

**Invisible consequences.**
- *Buyers* buy fewer covered drinks from April (C-4) and more exempt ones (C-5); some near the border buy in Penhallow (C-6). In the first quarter of 2028 they buy more, both to beat the deposit and because containers bought then can be redeemed without a deposit having been paid (C-11). The deposits that no one claims, which are the tax part of the Act, are paid by the buyers for whom returning a container costs most: drinks consumed away from home, buyers far from redemption points, buyers who value their time highly (C-7). Those buyers have less to spend on other things (C-26), and so, by a little, do buyers who return their containers, since their deposits are held until they do (C-27).
- *Collectors*, including people who never buy the drinks, earn money redeeming containers that others discard (C-8). Some bring containers from Penhallow (C-9), so empties there gain a price (C-19), and Penhallow's recycling programs lose cans (C-22). People hold marked empties in the first quarter of 2028 to redeem them in April (C-10).
- *Retailers and distributors* bear compliance costs (C-12, C-13). Large stores arrange for centers nearby to avoid taking back empties themselves (C-14). New redemption centers open (C-15) and hire (C-29), paid from deposits that buyers did not reclaim, while the sellers of what those buyers would otherwise have bought employ fewer people or hours (C-30). Penhallow border stores gain customers and Calder border stores lose the groceries bought on those trips (C-17, C-18). Regional bottlers lose value (C-25). Distributors, retailers and center operators lobby over the Act and the handling fee (C-16).
- *Recycling programs* in Calder lose their most valuable material, which distributors now sell instead (C-20, C-21).
- *The state* collects less than a projection based on non-return would suggest, because collectors, Penhallow containers and pre-April containers all draw on the Fund (C-23). DoR's costs come out of the Fund (C-28). If redemption and claims without deposits rise above 81% of containers sold (A-17, p = 0.55), the Fund runs short, and either distributors (U1-a) or taxpayers (U1-b) pay the difference (C-24).

**Ambiguous effects.** Whether the general fund gains from the Act once redemption points are established is not signed: it gains if the Fund keeps a surplus, receives nothing under U1-a if it does not, and pays under U1-b (section 7). How the burden of lower sales splits between drink buyers and sellers is not signed (section 7).

**Key conditions.** Shared labels and weak detection (A-9, p = 0.75) drive the cross-border effects. The Fund's medium-run position turns on arithmetic (break-even at 81%) and on A-17 (p = 0.55), the weakest reported premise. The first-quarter windfall rests on DoR's decision not to separate pre-April containers (A-10).

**What this analysis cannot say.** How large any effect is, including how many containers are returned or brought in from Penhallow. Environmental effects (litter, recycling, materials), which are the Act's purpose and out of scope for version 1. Whether the time buyers spend returning containers is worth what the Act aims at. Whether the policy is a good idea.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.calder | price_paid (covered drinks, incl. deposit) | increase | short | visible | B | CR-1 op 3; arithmetic | A-1 |
| C-2 | buyers.returning | wait_time (returning containers) | increase | short | visible | B | CR-4, CR-8c, OC-2 | A-2 |
| C-3 | state_budget | tax_revenue (Fund surplus, first year) | increase | short | visible | B | CR-8b; CR-12e | A-3 |
| C-4 | buyers.calder | quantity_traded (covered drinks, from April 2028) | decrease | short | invisible | B | CR-4c, CR-10a | A-4, A-11 |
| C-5 | buyers.calder | quantity_substitute (exempt drinks) | increase | short | invisible | B | RS-1 | A-4 |
| C-6 | buyers.non_returning (border) | cross_border_purchases | increase | short | invisible | B | RS-4 | A-5 |
| C-7 | buyers.high_return_cost | tax_share_borne | increase | short | invisible | B | CR-4, CR-8b | A-6 |
| C-8 | collectors | earnings (from redemption) | increase | short–medium | invisible | B | CR-1 op 2, CR-3b, CR-4, CR-7a | A-7, A-8 |
| C-9 | collectors.cross_border | informal_activity (Penhallow containers redeemed) | increase | short–medium | invisible | B | RS-3, RS-4, CR-4 | A-9 |
| C-10 | households, collectors | inventory_held (marked empties, Jan–Mar 2028) | increase | short | invisible | B | CR-10a | A-10 |
| C-11 | buyers.calder | quantity_traded (covered drinks, Jan–Mar 2028) | increase | short | invisible | B | RS-8, CR-10a | A-10, A-11 |
| C-12 | retailers.calder | compliance_cost | increase | short | invisible | A | TX-5, CR-8c | none |
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
| C-24 | distributors (U1-a) / taxpayers (U1-b) | resources_available_other_uses | U1-a: decrease; U1-b: decrease | medium | invisible | B | CR-8b; U1-a: CR-1 op 4; U1-b: TX-1, OC-1 | A-17 |
| C-25 | bottlers.regional | asset_value | decrease | short | invisible | B | CR-7c, CR-10c | A-4, A-18 |
| C-26 | buyers.non_returning | resources_available_other_uses | decrease | short | invisible | B | TX-1, CR-8a, CR-3 | A-19 |
| C-27 | buyers.returning | resources_available_other_uses | decrease | short | invisible | B | CR-8b, CR-10, LW-7 | A-2 |
| C-28 | officials.revenue | enforcement_cost | increase | short | invisible | A | OC-3, CR-8c | none |
| C-29 | redemption_centers | employment, hours_worked | at_least_one_increase | medium | visible | B | OC-5 | A-13, A-20 |
| C-30 | sellers (forgone purchases) | employment, hours_worked | at_least_one_decrease | medium | invisible | B | OC-5, OC-1 | A-19, A-20 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or a pattern, including the conditional direction of the transfer (CR-1, CR-4 per container), the residual claimant (CR-8b), payments with no deposit behind them (CR-8b), the price of empties across the border (CR-7a) and the Fund's break-even (CR-12e, arithmetic).

**(b) Unclear core rules (wording that was hard to apply here).**
- *CR-1, operations 3 and 4.* CR-1 lists "a tax" as operation 4 (transferring means). A per-unit tax is in fact attached to an option (operation 3): it is paid only if the actor buys. With a deposit the difference matters, because whether the payment ends as a tax, a loan or a transfer to a collector depends on a later choice. This analysis recorded op 3 on buying and op 2 on returning. CR-1 could say that a payment conditional on a choice is operation 3, and keep operation 4 for unconditional transfers (a lump-sum tax, a grant).
- *CR-1, Recording: splitting a class.* CR-1 says to split an actor class where the operation differs within it. Here the operations are identical for every buyer; what differs is the response, and it differs per container rather than per person (most buyers return some containers and discard others). The classes `buyers.returning` and `buyers.non_returning` are therefore defined by a CR-4 response, and membership changes with the policy itself. CR-1 does not say whether response-defined classes are allowed, or that the unit of a class may be a transaction rather than an actor.
- *CR-8b with a residual claimant.* CR-8b says every transfer adds to the recipient exactly what it takes from the payer. With one 10-cent payment and four possible recipients (the buyer, a collector, the state, a claimant with no deposit), and a residual that can turn negative, the identity holds only for the Fund as a whole. CR-8 does not say how to record a residual claimant whose receipt is the remainder after others' choices; it was handled with an accounting table (section 9) and arithmetic (CR-12e).
- *OC-2 and CR-8c against two baselines.* Returning a container is time that "buys" 10 cents against not returning, and buys nothing against no deposit. CR-8c lists queuing "because of" a policy as used up; it was applied against the no-policy baseline (C-2), as 2.5 requires, but the wording of OC-2 ("buys nothing they value for its own sake") invites the other baseline.
- *2.5, readings.* U1 changes who pays (distributors or taxpayers), not the sign. The `reading` field gives one sign per reading but not one actor class per reading, so C-24 names both classes in one row.

**(c) Missing patterns (derived here, likely to recur).**
- *P-027-1 Refundable charge (deposit-refund).* If: a payment is attached to buying a good, and a refund of up to the same amount is paid to whoever later performs an act (returning it, completing a course, leaving a site clean), with the unclaimed balance kept by a named party. Then: (i) per unit, the charge ends as a tax where no one claims it, as a loan where the payer claims it, and as a transfer where a third party does (CR-1 op 3 and op 2, CR-8b); (ii) the unclaimed part is borne by those for whom claiming costs most (CR-4, per unit) (`tax_share_borne`); (iii) the good's full cost rises for every buyer, including those who claim (CR-4c, LW-7); (iv) third parties enter to claim refunds others abandon, and the item acquires a market value of up to the refund less the cost of claiming (CR-1 op 2, CR-7a); (v) the residual claimant's receipt falls as claims rise and can turn negative, so its sign needs arithmetic on the case's figures (CR-8b, CR-12e). Derivation: CR-1, CR-4, CR-7a, CR-8b, CR-12e. Recurs for bonds on returnable equipment, tenancy deposits set by law, deposits on batteries, tires and propane cylinders, and cleanup bonds.
- *P-027-2 A claim payable inside a boundary draws claims from outside.* If: a payment is made inside a jurisdiction for an item that can also be obtained outside it without the matching charge, and the payer cannot tell the items apart. Then: items move in to be claimed (`informal_activity` increase where it is illegal); their price outside rises toward the payment, net of transport and expected penalty (CR-7a); the payer's fund pays out with nothing paid in (CR-8b), so the fund falls short of a static projection; sellers of the item's other uses outside lose supply (CR-9). Derivation: CR-4 (x: comply, y: violate), CR-7a, CR-8b, CR-9. RS-4 covers buyers moving purchases out; this is its mirror, items moved in to claim a payment.
- *P-027-3 A claim that starts before the charge.* If: a payment for an item becomes claimable on a date, while the charge that funds it applies only from a later date or to items marked from an earlier one. Then: items acquired in the gap are held for the claim (`inventory_held` increase in the gap), purchases rise in the gap and fall after it (per window), and the fund pays claims with nothing paid in. Derivation: CR-10a, CR-8b, 2.5 timing shifts.

**(d) Vocabulary (what the ontology lacks).**
- *Instrument type.* 2.3 has no type for a charge refundable on a later act. Proposed: `deposit_refund` (binary, in both directions). K4, an obligation to buy back empties, is a forced exchange with no instrument type either (2.3's triangular types all prohibit or cap; none compels).
- *Signs.* The sign list has no value for "no change" or for "increase or no change". The medium-run receipt of the general fund (section 7) is non-negative under U1-a (a surplus, or nothing) and cannot be recorded. WE-026 met the same limit for a reading under which a chain does not arise.
- *Variables.* (1) Unredeemed deposits are not taxes, but the only receipt variable is `tax_revenue` (C-3, C-23); proposed `non_tax_receipts` (also needed for fines in WE-026). (2) No variable for a fund's balance or shortfall. (3) `earnings` is defined for a group's total money earnings; C-8 needed earnings from one source (collection), which the definition does not separate.
- *Actor classes.* The generic list in 2.2 has no class for third parties who claim a payment created by the policy without being party to the taxed exchange (collectors), and no class for residual claimants (the state as holder of unclaimed deposits).
- *Relation types.* None missing: `input_to` (containers to recycling) and `across_border` (empties) sufficed.
