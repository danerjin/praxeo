# WE-019 Temporary car scrappage rebate

Analyst: draft (Handbook 0.2)  |  Rule catalog version: 0.2  |  Status: awaiting expert review

A stylized policy in a fictional country. It resembles the scrappage schemes many countries have run, but it is not any of them. The probabilities are illustrative; the evidence column says what a real analysis would cite. Environmental effects (emissions, air quality) are out of scope for version 1 and are not analyzed.

## 1. Policy record

**Vestria Fleet Renewal Rebate.** Vestria is a country of about 9 million people with no domestic car manufacturing: new cars are imported by about 30 brand importers and sold through some 600 franchised dealers. About 200,000 new cars are sold in a normal year, roughly 40% of them models that use 5.0 liters of fuel per 100 km or less. Of 4.5 million registered cars, about 1.1 million are 12 or more years old; a drivable car of that age typically sells for V$1,500 to V$5,000. Used cars can be imported, but they pay a 25% duty and a registration inspection, so the used-car market runs mostly on the domestic fleet. Neighboring countries have no scheme.

The government announced the rebate in its budget statement on 15 March. Parliament enacted it on 20 May. It applies to purchase contracts signed from 1 July to 31 December of the same year and then expires. Ministers have said there is no plan to repeat it, but have not ruled it out.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Rebate | `purchase_rebate` | New cars certified at 5.0 L/100 km or less, bought from a registered Vestrian dealer | Private buyers who scrap an eligible old car | V$4,000, paid by the Transport Ministry to the dealer and deducted on the invoice; one per buyer. The old car must be 12 or more years old, registered to the buyer continuously since before 15 March, and hold a current roadworthiness certificate (that is, drivable). Budget capped at V$480 million (120,000 rebates), first come, first served; the scheme closes early if the budget runs out. | Business and rental fleets; cars bought for export. |
| K2 Scrapping condition | Condition of K1 | The old car | Buyer and a licensed dismantler | The old car is delivered to a licensed dismantler, deregistered, and crushed within 30 days. Only scrap metal may be sold; no parts may be resold. Dismantlers receive a V$150 handling fee per car. | None |
| K3 Funding | Funding of K1, K2 and K4 | — | Treasury | Additional government bonds issued in the year, serviced and repaid from general revenue over 10 years. | — |
| K4 Administration | Enforcement | K1 and K2 | Transport Ministry vehicle registry | Checks registration history and roadworthiness certificates; confirms deregistration; audits dismantlers. Clawback of the rebate and fines for false claims. | — |

Unclear provisions: whether the scheme would be reopened if the budget ran out early. Treated as an expectation (A-15).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: a transfer from the state to buyers (and, through prices, possibly to sellers) | Yes for owners whose old car is worth less to them than the rebate (A-2) | SB, RS, TS |
| K2 | Binary: part of the exchange with the state; the state pays for the destruction of a usable good | Yes, by its text | SB-6, OC |
| K3 | Binary: borrowing now, taxes later | Yes | SB-1, TX-1, OC-1 |
| K4 | Binary: funded by taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `buyers.new_cars.scrapping` | Owners of eligible old cars who buy an eligible new car | New car V$4,000 cheaper if they give up a drivable old car, and only during the window. |
| `buyers.new_cars.other` | New-car buyers with no eligible car to scrap, including fleets | No rebate; compete with rebate buyers for the same models. |
| `sellers.new_cars` | Importers and dealers | Surge of demand for eligible models in a fixed window, then fewer buyers. |
| `owners.old_cars.keeping` | Owners of older cars who do not take part | Their cars become scarcer and more valuable. |
| `buyers.used_cars` | Households who buy older used cars, often first-time or lower-income car buyers | Fewer older cars for sale. |
| `repair_shops` (`sellers.complements`) | Independent garages that mostly service older cars | Fewer old cars to service; more owners keeping old cars longer. |
| `parts_suppliers` (`input_suppliers`) | Suppliers of parts for older models | Demand follows the repair shops. |
| `dismantlers` | Licensed scrap yards | More cars to crush; handling fee. |
| `sellers.fuel` (`sellers.complements`) | Fuel retailers | Fleet becomes more fuel-efficient. |
| `taxpayers`, `officials.enforcement` | Funders (now and over ten years) and the registry | Pay for the rebate and its administration. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.new_cars.scrapping` | `price_paid` (eligible new cars, net of rebate) | decrease | short | SB-2 | A-1, A-2 |
| C-2 | `sellers.new_cars` | `quantity_traded` (eligible new cars, during the window) | increase | short | SB-2, SB-6, RS-8 | A-2, A-3 |
| C-3 | `buyers.used_cars` | `quantity_substitute` (stock of drivable cars 12 or more years old) | decrease | short to medium | SB-6 | A-2, A-4 |
| C-4 | `dismantlers` | `quantity_traded` (cars received for scrapping) | increase | short | SB-6 | A-2 |

C-1 and C-2 are what the scheme's supporters point to: cheaper new cars and a sales boom. C-3 is also announced (the number of "old cars off the road"), so it is visible; what it does to used-car buyers is not (C-13).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | `buyers.new_cars.scrapping` | `quantity_traded` (eligible new cars, between announcement on 15 March and 1 July) | decrease | short | RS-8 | A-5 |
| C-6 | `sellers.new_cars` | `quantity_traded` (new cars, in the one to three years after the window) | decrease | short to medium | SB-6 | A-3 |
| C-7 | `buyers.new_cars.scrapping` | `wait_time` (race to claim before the budget runs out; delivery queues) | increase | short | LW-6, RS-8 | A-6 |
| C-8 | `sellers.new_cars` | `net_price_received` (eligible models; fewer discounts) | increase | short | SB-2, GAP-019-2 | A-7 |
| C-9 | `buyers.new_cars.other` | `price_paid` (eligible models, without a rebate) | increase | short | SB-2, GAP-019-2 | A-7 |
| C-10 | owners of old cars near the end of their life | `reclassification` (repairs made only to obtain a roadworthiness certificate and qualify) | increase | short | SB-5, RS-5 | A-8 |
| C-11 | `sellers.new_cars`, `dismantlers`, would-be rebate buyers | `lobbying_effort` (for an extension or a repeat) | increase | short to medium | RS-7, SB-5 | A-9 |
| C-12 | `sellers.new_cars` | `quantity_traded` (non-eligible new models, during the window) | decrease | short | RS-1, SB-3 | A-12 |

C-7: the rebate is a good handed out at a fixed price (zero) in a fixed quantity. If more owners want it than the budget allows, it is rationed by timing (LW-6): buyers rush to sign in July and August, and dealers with limited stock of eligible models build waiting lists.

C-8 and C-9: SB-2 says only that buyers pay less and/or sellers receive more. To say that sellers capture part of it, the analysis uses the logic of DM-1 (the side with fewer alternatives in the period gets more of the benefit; here, sellers whose stock of eligible models cannot grow within six months, A-7). DM-1 is written for taxes only, so these are Tier C (GAP-019-2). C-9 follows: people who buy the same models without scrapping a car pay more than they would have.

Not reported:
- Reclassification by importers (recertifying model variants to get under 5.0 L/100 km). The window is too short for new certification; A-10 is below the cut-off (p = 0.3). Importers can only change which certified models they ship, which is part of C-2 and C-12.
- Evasion through false scrapping (cars certified as crushed but resold or exported). Deregistration is checked against the registry and dismantlers are audited; A-11 is below the cut-off (p = 0.25).
- Relocation (RS-4): the rebate requires a Vestrian dealer, and Vestrians did not buy new cars abroad in meaningful numbers before the scheme. No chain to follow.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-13 | `buyers.used_cars` | `price_substitute` (cars 12 or more years old) | increase | short to medium | SB-6 | new and old cars: `substitute`, partial; old cars in Vestria and abroad: `across_border`, weak (duty) | A-4, A-13 |
| C-14 | `owners.old_cars.keeping` | `asset_value` (their older cars) | increase | short to medium | SB-6 | as C-13 | A-4, A-13 |
| C-15 | `buyers.used_cars` | `quantity_substitute` (repairs that keep their current car in service instead of replacing it) | increase | medium | RS-1 | repairing an old car and buying a used one: `substitute`, partial | A-4, A-13, A-14 |
| C-16 | `repair_shops` | `quantity_traded` (repairs of older cars) | see section 7 | medium | RS-1; GAP-019-1 | old cars and repairs: `complement`, close | A-4, A-14 |
| C-17 | `parts_suppliers` | `quantity_demanded` (parts for older models) | see section 7 | medium | GAP-019-1 | repairs and parts: `input_to`, close | A-4, A-14 |
| C-18 | `sellers.fuel` | `quantity_traded` (motor fuel) | see section 7 | medium | GAP-019-1 | cars and fuel: `complement`, close | A-2 |

C-17 is at depth 4 (rebate → scrapping → fewer old cars → fewer repairs → fewer parts), so the chain stops there. C-18 is at depth 3 and spreads over all fuel sellers, so it also stops there.

Second-order checks:
- **RS-9 (bundled trips).** No buyer changes where they buy the target good: rebate purchases were already made at Vestrian dealers. A new car does bring service visits back to the dealer during the warranty period, away from independent garages; that is a complement in use rather than a trip, and it is part of the minus chain in C-16.
- **RS-10 (informal trade).** No informal market is created unless scrapping is faked, which is not reported (A-11).
- **RS-11 (lock-in).** The rebate is not tied to a location and does not have to be repaid on moving. Not applicable.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `sellers.new_cars`, `quantity_traded` (eligible new cars, total from announcement to three years after the window), medium | Surge in the window (C-2), including some purchases that would never have happened without the rebate. | Purchases delayed from March to June (C-5); dip after the window as buyers who brought their purchase forward do not buy again (C-6). | None. The catalog has no rule for netting a timing shift against extra purchases. | **ambiguous**. If every purchase in the dips was simply moved into the window, the total over the period rises by the number of extra buyers; a rule saying so is proposed as GAP-019-3. Under catalog 0.2 the sign stays ambiguous. |
| `repair_shops`, `quantity_traded` (repairs of older cars), medium | Used-car buyers facing higher prices keep their own cars longer and repair them (C-15, RS-1, Tier B). In the run-up, borderline cars are repaired to qualify (C-10, short only). | 120,000 fewer old cars need servicing; new cars are serviced at dealers under warranty (complement in use; no rule, GAP-019-1, Tier C). | None | **ambiguous** (Tier C, the lowest tier in the chains). Decided by how many scrapped cars would have kept visiting independent garages compared with how much longer non-participants keep their cars. |
| `parts_suppliers`, `quantity_demanded` (parts for older models), medium | Follows the + chain of C-16. | Follows the − chain of C-16. | None | **ambiguous** (Tier C). |
| `sellers.fuel`, `quantity_traded` (motor fuel), medium | Lower fuel cost per km in the new cars leads some owners to drive more (LW-3 applied to driving; no rule links it to fuel sales, GAP-019-1). | The cars replaced used more fuel per km (complement in use, GAP-019-1). | None | **ambiguous** (Tier C). |
| Split of the rebate between `buyers.new_cars.scrapping` and `sellers.new_cars`, short | — | — | DM-1 logic, not in the catalog for subsidies (GAP-019-2) | **Not determined by catalog 0.2.** Both C-1 and C-8 can hold at once; they are not conflicting chains on one variable. With A-7, sellers receive part of the rebate in the window. |

## 8. Time structure

- **Before the window.** The scheme was public 3.5 months before it applied. Owners of eligible cars who planned to buy in that period wait for July (C-5), so dealers see a dip before the boom. The 15 March registration cut-off stops people from buying cheap old cars to scrap.
- **In the window.** If the budget would be exhausted before December (A-6), the six months shrink in practice: buyers race to sign early (C-7), and the price capture in C-8 is greatest then, when the stock of eligible models is fixed by import orders placed before the scheme (A-7). Importers can redirect later shipments toward eligible models, which weakens C-8 toward the end of the window.
- **After the window.** The dip (C-6) is spread over the period in which the pulled-forward buyers would otherwise have bought, mostly the next one to three years. Dealer staffing and importer allocations set for the boom are cut back in the dip.
- **Used cars.** The scrapped cars would have been retired over the following years anyway (A-4). The used-car price effect (C-13, C-14) is largest at once and fades as the missing cohort reaches the age at which it would have been scrapped. Used-car imports, slowed by duty, also add supply over time.
- **Funding.** The rebate is paid in the window but funded by bonds repaid over ten years (K3), so the cost to taxpayers (C-20) is medium to long while the gain is short.
- **Expectations.** If buyers come to expect a repeat scheme (TS-2), some delay purchases in later years to wait for it, deepening future dips. The lobbying in C-11 makes that more likely, but the government's stated position puts A-15 below the cut-off (p = 0.35), so the deeper later dip is not reported.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-19 | `officials.enforcement` | `enforcement_cost` | increase | Registry checks, dismantler audits and fee payments. | OC-3 |
| C-20 | `taxpayers` | `resources_available_other_uses` | decrease | What taxpayers would have bought with the taxes that repay V$480 million of bonds plus interest, the dismantler fees and the administration (C-19). | SB-1, TX-1, OC-1, OC-3 |
| C-21 | `buyers.used_cars` | `quantity_traded` (resales of the scrapped cars) | decrease | The sales in which the scrapped cars would later have passed to another owner. Both sides lose the gain each expected. | SB-6, OC-4 |

The destroyed cars are a usable capital good turned into scrap metal. For the owners who scrap them, the exchange with the state is voluntary and expected to be worth it (LW-5): the rebate is worth more to them than the car. The forgone use of the car does not disappear, however. It falls on the people who would have driven it later, recorded as fewer cars (C-3), higher prices (C-13) and resales that do not happen (C-21), and on the taxpayers who pay the rebate (C-20). Search and waiting are already recorded as C-7.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Sellers do not capture the whole rebate by raising transaction prices, so the net price to rebate buyers falls. | other | 0.85 | Dealer discounting before the scheme; number of competing brands; rebate shown on the invoice; transaction-price surveys. | C-1 fails; the whole rebate goes to sellers. |
| A-2 | Many owners of eligible cars value the rebate above their car and the cost of buying sooner. | other | 0.9 | Value distribution of 12-year-old cars against V$4,000; surveys of replacement plans. | C-1 to C-4 shrink; few cars are scrapped. |
| A-3 | Many window buyers would have bought a new car within the next few years anyway. | expectations | 0.85 | Age profile and replacement patterns of buyers; buyer surveys. | C-6 weakens; the surge is mostly extra purchases. |
| A-4 | The scrapped cars would otherwise have stayed in use for some years. | durability | 0.85 | Roadworthiness requirement; average age at retirement (about 18 years) against the 12-year eligibility age. | C-3, C-13 to C-17 and C-21 weaken or fail. |
| A-5 | Buyers knew of the scheme from March and could delay purchases. | expectations | 0.85 | Publicity of the budget statement; dealer reports of deferred orders. | C-5 not reported. |
| A-6 | Demand for rebates exceeds 120,000 at some point in the window. | other | 0.6 | 1.1 million eligible cars; take-up in comparable schemes. | C-7 shrinks to delivery delays only. |
| A-7 | The supply of eligible models cannot grow much within six months. | other | 0.7 | Importer allocations; shipping lead times of three to five months; dealer stock levels. | C-8 and C-9 weaken; buyers get more of the rebate. |
| A-8 | Some owners of failing cars can get a roadworthiness certificate for less than the rebate is worth to them. | other | 0.6 | Inspection pass rates; repair costs for common failures. | C-10 not reported. |
| A-9 | Importers and dealers can organize to lobby at low cost. | other | 0.85 | Existing importers' association. | C-11 weakens. |
| A-10 | Importers can recertify model variants below 5.0 L/100 km within the window. | other | 0.3 | Certification lead times. | Below cut-off; not reported. |
| A-11 | Dismantlers fake scrapping on a meaningful scale. | enforcement | 0.25 | Registry deregistration checks; audit frequency; penalties. | Below cut-off; not reported. |
| A-12 | Some rebate buyers would otherwise have bought a non-eligible new model. | substitutability | 0.7 | Model mix of buyers who replace 12-year-old cars. | C-12 weakens. |
| A-13 | Used-car imports cannot quickly replace the scrapped cars. | mobility | 0.75 | 25% duty; inspection cost; past import volumes. | C-13 to C-15 weaken. |
| A-14 | Repairing an existing old car is a feasible alternative to replacing it for some used-car buyers. | substitutability | 0.8 | Garage density; repair costs against used-car prices. | C-15 fails; C-16 becomes a decrease (Tier C). |
| A-15 | Buyers expect the scheme to be repeated. | expectations | 0.35 | Government statements; lobbying strength; history of repeat schemes in the region. | Below cut-off; the deeper later dip is not reported. |

## 11. Report

**The policy.** For six months, Vestria pays V$4,000 toward a new fuel-efficient car to private buyers who have a drivable car at least 12 years old crushed. The budget covers 120,000 rebates, first come, first served, and is borrowed and repaid from taxes over ten years.

**Visible consequences.** Rebate buyers pay less for new fuel-efficient cars (C-1), dealers sell more of them during the window (C-2), and many old cars leave the road (C-3, C-4).

**Invisible consequences.**
- *New-car buyers and sellers.* Sales dip between the announcement and the start (C-5) and again for one to three years after the window, as buyers who brought their purchase forward drop out of the market (C-6). If the budget looks likely to run out, buyers race to claim early (C-7). While the stock of eligible models is fixed, dealers give smaller discounts and keep part of the rebate (C-8); buyers of the same models who have no car to scrap pay more (C-9). These two are Tier C. Sales of non-eligible models fall during the window (C-12).
- *Used-car buyers*, often first-time or lower-income car buyers, face fewer older cars and higher prices for them (C-3, C-13); some resales that would have happened never do (C-21). More of them keep and repair their current car instead (C-15). Owners of older cars who do not take part find their cars worth more (C-14).
- *Owners of failing cars* repair them just enough to qualify (C-10).
- *Repair shops, parts suppliers and fuel sellers*: see ambiguous effects.
- *Importers, dealers and others* lobby for an extension or repeat (C-11).
- *Taxpayers* repay the borrowing and fund the registry's work over ten years (C-19, C-20).

**Ambiguous effects.** Whether total new-car sales over the whole period rise, once both dips are counted (rises if some window buyers are extra buyers and the dips are only moved purchases; the catalog cannot yet net them, GAP-019-3). Whether independent repair shops and parts suppliers do more or less work on older cars (fewer old cars against owners keeping theirs longer). Whether fuel sales fall (more efficient cars against more driving).

**Key conditions.** Most of the less obvious effects depend on the scrapped cars having had useful life left (A-4, p = 0.85) and on used-car imports being slow to replace them (A-13, p = 0.75). The early rush depends on demand outrunning the budget (A-6, p = 0.6). How much of the rebate dealers keep depends on how fast importers can bring in more eligible models (A-7, p = 0.7).

**What this analysis cannot say.** How large any effect is; whether the gains to rebate buyers and sellers outweigh the costs to used-car buyers and taxpayers; environmental effects (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.new_cars.scrapping | price_paid (eligible new cars, net) | decrease | short | visible | B | SB-2 | A-1, A-2 |
| C-2 | sellers.new_cars | quantity_traded (eligible, in window) | increase | short | visible | B | SB-2, SB-6, RS-8 | A-2, A-3 |
| C-3 | buyers.used_cars | quantity_substitute (stock of old cars) | decrease | short–medium | visible | B | SB-6 | A-2, A-4 |
| C-4 | dismantlers | quantity_traded (cars scrapped) | increase | short | invisible | B | SB-6 | A-2 |
| C-5 | buyers.new_cars.scrapping | quantity_traded (eligible, March to June) | decrease | short | invisible | B | RS-8 | A-5 |
| C-6 | sellers.new_cars | quantity_traded (after the window) | decrease | short–medium | invisible | B | SB-6 | A-3 |
| C-7 | buyers.new_cars.scrapping | wait_time | increase | short | invisible | B | LW-6, RS-8 | A-6 |
| C-8 | sellers.new_cars | net_price_received (eligible models) | increase | short | invisible | C | SB-2, GAP-019-2 | A-7 |
| C-9 | buyers.new_cars.other | price_paid (eligible models) | increase | short | invisible | C | SB-2, GAP-019-2 | A-7 |
| C-10 | owners of failing old cars | reclassification | increase | short | invisible | B | SB-5, RS-5 | A-8 |
| C-11 | sellers.new_cars, dismantlers, rebate buyers | lobbying_effort | increase | short–medium | invisible | B | RS-7, SB-5 | A-9 |
| C-12 | sellers.new_cars | quantity_traded (non-eligible models, in window) | decrease | short | invisible | B | RS-1, SB-3 | A-12 |
| C-13 | buyers.used_cars | price_substitute (old cars) | increase | short–medium | invisible | B | SB-6 | A-4, A-13 |
| C-14 | owners.old_cars.keeping | asset_value (old cars) | increase | short–medium | invisible | B | SB-6 | A-4, A-13 |
| C-15 | buyers.used_cars | quantity_substitute (repairs of own car) | increase | medium | invisible | B | SB-6, RS-1 | A-4, A-13, A-14 |
| C-16 | repair_shops | quantity_traded (repairs of old cars) | ambiguous | medium | invisible | C | C-15 vs GAP-019-1 | A-4, A-14 |
| C-17 | parts_suppliers | quantity_demanded (parts for old models) | ambiguous | medium | invisible | C | C-16, GAP-019-1 | A-4, A-14 |
| C-18 | sellers.fuel | quantity_traded (motor fuel) | ambiguous | medium | invisible | C | GAP-019-1 | A-2 |
| C-19 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-20 | taxpayers | resources_available_other_uses | decrease | medium–long | invisible | A | SB-1, TX-1, OC-1, OC-3 | none |
| C-21 | buyers.used_cars | quantity_traded (resales of scrapped cars) | decrease | medium | invisible | B | SB-6, OC-4 | A-4 |
| C-22 | sellers.new_cars | quantity_traded (eligible, cumulative to three years after) | ambiguous | medium | invisible | B | C-2 vs C-5, C-6; GAP-019-3 | A-2, A-3, A-5 |

## Gaps found

- **GAP-019-1. No rule for complements in use.** RS-9 covers goods bought on the same trip, but nothing covers goods used together (old cars and repairs, cars and fuel): when the stock or use of one good changes, demand for its complements in use changes in the same direction. Market relation type `complement` exists in 2.8, and the variables `price_complement` and `quantity_complement` exist, but no rule licenses the move. C-16 to C-18 use it, at Tier C. **Proposed fix:** a generic rule RS-12 "Complement spillover": if `quantity_traded` or the stock in use of a good changes, then `quantity_complement` (and, with fixed supply, `price_complement`) changes in the same direction for goods recorded as `complement` (not `trip`); assumes the complement relation is close and the complement has few other uses; Tier B; builds on LW-2.
- **GAP-019-2. DM-1 covers taxes only.** Who receives a subsidy (buyers through lower net prices, or sellers through higher prices received) follows the same logic as tax incidence: the side with fewer alternatives in the period gets the larger share. DM-1 is written for TX-2 only, and SB-2 leaves the split open. C-8 and C-9 use the move, at Tier C. **Proposed fix:** extend DM-1 to SB-2 ("If SB-2 applies and one side has clearly fewer alternatives, that side receives the larger part of the subsidy"), with the time note that supply alternatives grow over time.
- **GAP-019-3. No rule for netting a timing shift.** SB-6 predicts a surge and a dip, but the catalog cannot combine them into a sign for the total over a period that includes both. If the dips consist only of purchases moved into the window, and some window purchases are extra, the total rises; but this needs an assumption, and no DM rule exists. C-22 is left ambiguous. **Proposed fix:** a dominance rule DM-4 "Timing shifts net to zero": over a horizon long enough to include the dip, a temporary purchase subsidy raises the total quantity traded if some purchases are additional, given the assumption that the dip contains only moved purchases (type `expectations`; fails if, for example, the subsidy is expected to recur and buyers wait for it).
