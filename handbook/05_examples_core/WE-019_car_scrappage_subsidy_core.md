# WE-019 / Core-only re-run: Temporary car scrappage rebate

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

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

CR-1 operations: 1 remove an option, 2 add an option, 3 change what an option brings, 4 transfer means.

| Component | Rothbard type | Binding? (assumption ID) | Core rules | CR-1 operations, by actor class |
|---|---|---|---|---|
| K1 | binary (a transfer from the state, conditional on a purchase) | Yes: many owners value the rebate above their car (A-2) | CR-1, CR-4, CR-6, CR-7b, CR-9, CR-10a | Owners of eligible cars: 3 and 4 (V$4,000 attached to scrap-and-buy). Dealers: 3 (claims paperwork). Fleets and owners without an eligible car: none directly (felt through CR-9). |
| K2 | condition of K1 (prohibits reuse of the car and its parts) | Yes for every rebate car | CR-1, CR-8a, CR-9, CR-10b | Rebate takers: 1 (selling or keeping the old car). Dismantlers: 1 (parts resale from these cars) and 4 (V$150 fee). |
| K3 | binary (borrowing, later taxes) | Yes | CR-1, CR-8 | Future taxpayers: 4. Lenders: the bonds add an option (2) that draws savings from other uses. |
| K4 | enforcement | Checks are routine; fake scrapping not reported (A-11) | CR-1, CR-8c | Claimants and dismantlers: 3 (clawback and fines). |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| buyers.rebate | Owners of eligible old cars who take the rebate | Scrap-and-buy now brings V$4,000 (3, 4); their old car must be crushed (1). |
| owners of eligible old cars | All 1.1 million owners of cars 12+ years old registered before 15 March | Same option offered; most may not take it. |
| buyers.new_cars, buyers.non_rebate | All private new-car buyers; fleets and buyers without an eligible car | Non-rebate buyers: no direct change; same models, possibly dearer (CR-9). |
| importers and dealers (sellers.current) | Sell eligible and non-eligible new models | Paperwork (3); demand moves in time and between models (CR-9). |
| sellers.substitutes (non-eligible new models) | Same sellers, other models | Demand moves to eligible models (CR-9). |
| owners of non-scrapped older cars, buyers.used_cars | Used-car market | No direct change; the stock of older cars shrinks (CR-9). |
| dismantlers | Licensed dismantlers | More cars, fee, no parts from these cars (1, 4). |
| sellers.complements (repair garages, parts, fuel) | Goods used with cars | No direct change; fleet changes (CR-9). |
| borrowers.private | Other borrowers in Vestria's capital market | No direct change; compete with the bonds for savings (CR-7a, CR-8a). |
| taxpayers (future), officials.enforcement | Repay bonds; administer | Transfer (4); new duties. |
| neighboring_jurisdictions | No scheme; source of imported used cars | No direct change; used-car imports may rise (CR-9). |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | buyers.rebate (owners of eligible old cars who take the rebate) | price_paid (eligible new cars, net of the rebate) | decrease | short | CR-1 op. 3 and 4 (V$4,000 attached to the option scrap-and-buy); CR-12b resolved by A-1 against C-13 | A-1 |
| C-2 | buyers.rebate (owners of eligible old cars who take the rebate) | quantity_traded (eligible new cars, 1 July to 31 December) | increase | short | CR-4b (x: keep the old car, y: scrap it and buy an eligible new car), for owners who rank the rebate above their car's value and the cost of buying sooner | A-1, A-2 |
| C-3 | dismantlers | quantity_traded (eligible old cars delivered for scrapping) | increase | short | CR-1 op. 1 (K2: rebate cars must be crushed, parts not resold); CR-9 (input_to: each rebate sale delivers a car) | A-2 |
| C-4 | importers and dealers (sellers.current) | compliance_cost | increase | short | CR-1 op. 3 (claims, invoice deduction, checks of registration and certificates); CR-8c |  |

## 5. Responses

CR-4 for each pair of options:

- **Owners of eligible cars.** (x: keep the car, y: scrap and buy) (C-2); (x: buy a non-eligible model, y: buy an eligible one) (C-8); for failing cars, (x: let it fail, y: repair it to qualify) (C-10). Because the rebate is a fixed amount from a fixed budget, if claims exceed 120,000 they are rationed by arrival (CR-6) (C-9).
- **All new-car buyers, timing.** CR-10a with (x: buy now, y: later): purchases wait from March to July (C-5); purchases are pulled into the window and missing from the following year (C-6); over the window and the following three years, only additional purchases remain (C-7).
- **Importers and dealers.** (x: accept expiry, y: lobby) (C-11). Their stock is fixed for the window by earlier orders (A-7), so they cannot add supply; their response is in price (section 6).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | buyers.new_cars (all private buyers) | quantity_traded (new cars, 15 March to 30 June) | decrease | short | CR-10a; CR-4b (x: buy now, y: wait for 1 July and the rebate) | A-5 |
| C-6 | buyers.new_cars (all private buyers) | quantity_traded (new cars, the year after the window) | decrease | medium | CR-10a (purchases moved into the window are not repeated after it); arithmetic | A-3, A-20 |
| C-7 | buyers.new_cars (all private buyers) | quantity_traded (new cars, window plus the following three years) | increase | long | Arithmetic: purchases moved in time cancel over the period (CR-10a), additional purchases do not (CR-4b, x: keep the old car or buy used, y: buy new) | A-19, A-20 |
| C-8 | sellers.substitutes (non-eligible new models) | quantity_traded (non-eligible new models, window) | decrease | short | CR-4b (x: non-eligible model, y: eligible model with the rebate) | A-12 |
| C-9 | owners of eligible old cars | allocation_by_non_price_criteria (rebates) | increase | short | CR-6 (rebates are offered at a fixed amount from a fixed budget, so when claims exceed 120,000 they go first come, first served; pressure moves to timing and to dealer relationships); CR-10a (claims rush to early in the window) | A-6 |
| C-10 | owners of eligible old cars (failing roadworthiness) | quantity_complement (repairs and inspections on cars about to be scrapped) | increase | short | CR-4b (x: scrap or keep a failing car without the rebate, y: repair it to obtain the certificate and the rebate) | A-8 |
| C-11 | importers and dealers (sellers.current) | lobbying_effort | increase | medium | CR-4b (x: accept expiry, y: lobby for extension or repetition), stronger in the post-window dip | A-9 |

## 6. Second-order effects

Depth limit 4; prune diffuse bystander effects after depth 3. Relations used: eligible models sold to rebate and non-rebate buyers: same market, other segment; scrapped and remaining older cars: same market, other segment (used cars); used cars at home and abroad: across_border, weak (25% duty, A-13); repairs, parts and fuel: complements of cars in use (A-17); dismantled cars: input_to used parts; government bonds and private borrowing: same market for loanable savings.

Chains:
1. K1 (1) demand for eligible models rises with stock fixed (2) the pre-rebate price rises, so part of the rebate goes to sellers and non-rebate buyers pay more (C-13, C-15, C-14, C-12) (3).
2. K1 and K2 (1) scrapping removes older cars (2) values and prices of remaining older cars rise (C-17, C-18) (3) fewer used-car purchases, more imports, more repair of existing cars (C-19, C-20, C-21).
3. K2 (1) cars crushed with their parts (2) fewer used parts later (C-22) (3) parts prices: opposing chains (C-23).
4. K1 (1) newer cars replace older ones (2) less fuel used (C-24).
5. K3 (1) bonds (2) savings withdrawn from other borrowers (C-25). Diffuse beyond this; stopped at depth 2 of the funding chain.
6. K1 (1) purchases pulled forward (2) post-window dip in sales and prices (C-6, C-16) (3) lobbying for a repeat (C-11).

Component interactions: K2 removes the option of selling the old car, so the rebate's value to an owner is V$4,000 less the car's value, and the stock of used cars shrinks by every rebate; K1's registration-date condition (before 15 March) closes the option of buying old cars to qualify after the announcement; K3 funds K1 by borrowing, so its cost falls on future taxpayers and on present borrowers.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | buyers.non_rebate (fleets, buyers without an eligible car) | price_paid (eligible new models) | increase | short | CR-6 first paragraph (planned purchases of eligible models rise against stock fixed for the window); CR-7b (the benefit settles on the side with fewer alternatives, here the sellers); CR-9 | same_market_other_segment (eligible models, non-rebate buyers) | A-7, A-16 |
| C-13 | buyers.rebate (owners of eligible old cars who take the rebate) | price_paid (eligible new cars, before the rebate) | increase | short | CR-6 first paragraph; CR-7b with the premise that sellers have fewer alternatives in the window | same market | A-7, A-16 |
| C-14 | importers and dealers (sellers.current) | subsidy_share_received | increase | short | CR-7b (the benefit of a subsidy settles on the side with fewer alternatives: sellers whose stock is fixed by earlier import orders) | same market | A-7, A-16 |
| C-15 | importers and dealers (sellers.current) | net_price_received (eligible models) | increase | short | CR-6 first paragraph; CR-7b | same market | A-7, A-16 |
| C-16 | importers and dealers (sellers.current) | net_price_received (new cars, the year after the window) | decrease | medium | CR-6 first paragraph (planned purchases fall in the dip, C-6) | same market | A-3, A-20 |
| C-17 | owners of non-scrapped older cars | asset_value (older used cars) | increase | short | CR-7c (an expected lasting fall in the stock of older cars raises their value when it becomes expected, from March); CR-9 | same_market_other_segment (scrapped and remaining older cars) | A-4, A-13 |
| C-18 | buyers.used_cars | price_paid (older used cars) | increase | medium | CR-6 first paragraph (the scrapped cars leave the stock the used market draws on); CR-9 | same_market_other_segment | A-4, A-13 |
| C-19 | buyers.used_cars | quantity_traded (older used cars) | decrease | medium | CR-4c after C-18; fewer cars available | same_market_other_segment | A-4, A-13 |
| C-20 | buyers.used_cars | cross_border_purchases (imported used cars) | increase | medium | CR-4b (x: domestic used car, y: imported used car despite the 25% duty), after C-18 | across_border (used cars abroad, weak because of duty and inspection) | A-4, A-N2 |
| C-21 | sellers.complements (repair garages) | quantity_complement (repair work on older cars) | ambiguous | medium | (-) CR-9, LW-10 (fewer older cars in use, so less repair work on them); (+) CR-4b (x: buy a dearer used car, y: repair the existing one); CR-12b | complement (repairs and older cars) | A-4, A-14, A-17 |
| C-22 | sellers.complements (used parts for older models) | quantity_supplied (used parts for older models) | decrease | long | CR-10b (cars that would later have reached dismantlers and yielded parts are crushed now, K2); CR-8a | input_to (dismantled cars to used parts) | A-4, A-17 |
| C-23 | buyers of parts for older models | price_complement (parts for older models) | ambiguous | long | (+) CR-6 first paragraph, less used-parts supply (C-22); (-) CR-9, fewer older cars needing parts; CR-12b | complement (parts and older cars) | A-4, A-17 |
| C-24 | sellers.complements (fuel sellers) | quantity_complement (fuel) | decrease | long | CR-9, LW-10 (demand for fuel follows the fuel used by the fleet; replacement cars use less per km) | complement (fuel and cars) | A-4, A-18, A-N3 |
| C-25 | borrowers.private (domestic capital market) | resources_available_other_uses | decrease | medium | CR-8a (savings lent to the government through K3's bonds are withdrawn from other borrowers); CR-7a | same market (loanable savings) | A-N1 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| buyers.rebate, price_paid (net of rebate), short | Pre-rebate price rises (CR-6, CR-7b with A-16) | V$4,000 deducted (CR-1 op. 4) | A-1: sellers do not capture the whole rebate. CR-7b with A-16 says only that sellers capture part, so A-1 is an empirical premise, not a derived dominance | decrease |
| sellers.complements (repair garages), quantity_complement (repairs on older cars), medium | Used-car buyers repair instead (CR-4b) | Fewer older cars (CR-9) | None | ambiguous (CR-12b) |
| buyers of parts, price_complement (parts for older models), long | Less used-parts supply (CR-6) | Fewer older cars needing parts (CR-9) | None | ambiguous (CR-12b) |
| buyers.new_cars, quantity_traded, by window | Window: rebate | Before July: waiting; year after: pulled-forward purchases missing | Not netted: separate windows, each signed against the counterfactual | short (Mar to Jun): decrease; short (window): increase; medium: decrease; window plus three years: increase |

No other key is reached by opposing chains. The rebate counted as a gain to buyers and sellers is matched by future taxpayers' outlay (C-26); the rise in older cars' value is matched by used-car buyers' outlay (C-29) (CR-8 symmetry). Different variables are not netted (CR-12c).

## 8. Time structure

- **Announcement to start (CR-10a).** The scheme was announced on 15 March and starts on 1 July, so new-car purchases are held back for three and a half months (C-5). The registration-date rule stops owners from buying old cars to qualify during this period.
- **Window.** Claims rush early in the window if the budget may run out (A-6) (C-9). Sellers' stock is fixed for the window by import lead times of three to five months (A-7), which is why part of the rebate goes to them in the short run.
- **After the window.** Pulled-forward purchases leave a dip (A-3, A-20) (C-6), with lower seller prices (C-16). If buyers expected a repeat (A-15, p 0.35), the dip would be deeper and longer; not reported.
- **Durable stock (CR-10b).** Each scrapped car's remaining years of service are lost for good; the shortage of older cars and of their used parts persists for as long as those cars would have run (A-4: retirement at about 18 years against eligibility at 12). The fuel saving also lasts for that period.
- **Funding.** The cost falls on taxpayers over ten years of bond service; the crowding of other borrowers falls in the year of issue.

## 9. Opportunity costs

CR-3 and CR-8. The rebate is a transfer (CR-8b): every V$4,000 received is V$4,000 (plus interest) paid later by taxpayers. The scrapped cars' remaining service is used up (CR-8a). Rebate buyers' own spending is moved in time, signed per window.

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-26 | taxpayers (future) | resources_available_other_uses | decrease | Future public spending or lower taxes | CR-8a, CR-8b (rebates, handling fees, administration and interest are repaid from general revenue over 10 years; every rebate counted as a gain is matched here) |
| C-27 | officials.enforcement (vehicle registry) | enforcement_cost | increase | Staff time and funds for other public uses | CR-8c; K4 |
| C-28 | sellers.current (owners who would have sold older cars) | quantity_supplied (older used cars) | decrease | The years of driving the scrapped cars would still have given | CR-8a (the remaining service of each scrapped car is destroyed rather than used by its owner or a later buyer) |
| C-29 | buyers.used_cars | resources_available_other_uses | decrease | Other spending by buyers of used cars | CR-8b (the gain to owners of older cars in C-17 is the matching outlay of their buyers); CR-3a |
| C-30 | buyers.rebate (owners of eligible old cars who take the rebate) | resources_available_other_uses (in the window) | decrease | Other spending in the window | CR-10a and CR-8d (spending on a car is moved into the window or added, net of the rebate) |
| C-31 | buyers.rebate (owners of eligible old cars who take the rebate) | resources_available_other_uses (in the years they would have bought) | increase | None: means freed for other uses later | CR-10a (the purchase they would have made later is not made) |

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Sellers do not capture the whole rebate by raising transaction prices, so the net price to rebate buyers falls. | other | 0.85 | Dealer discounting before the scheme; number of competing brands; rebate shown on the invoice; transaction-price surveys. | Net price to rebate buyers unchanged. |
| A-2 | Many owners of eligible cars value the rebate above their car and the cost of buying sooner. | other | 0.9 | Value distribution of 12-year-old cars against V$4,000; surveys of replacement plans. | Little take-up. |
| A-3 | Many window buyers would have bought a new car within the next few years anyway. | expectations | 0.85 | Age profile and replacement patterns of buyers; buyer surveys. | No post-window dip. |
| A-4 | The scrapped cars would otherwise have stayed in use for some years. | durability | 0.85 | Roadworthiness requirement; average age at retirement (about 18 years) against the 12-year eligibility age. | No used-car, parts or fuel chains. |
| A-5 | Buyers knew of the scheme from March and could delay purchases. | expectations | 0.85 | Publicity of the budget statement; dealer reports of deferred orders. | No pre-window dip. |
| A-6 | Demand for rebates exceeds 120,000 at some point in the window. | other | 0.6 | 1.1 million eligible cars; take-up in comparable schemes. | No rationing. |
| A-7 | The supply of eligible models cannot grow much within six months. | other | 0.7 | Importer allocations; shipping lead times of three to five months; dealer stock levels. | Sellers capture little. |
| A-8 | Some owners of failing cars can get a roadworthiness certificate for less than the rebate is worth to them. | other | 0.6 | Inspection pass rates; repair costs for common failures. | No pre-scrap repairs. |
| A-9 | Importers and dealers can organize to lobby at low cost. | other | 0.85 | Existing importers' association. | No lobbying. |
| A-10 | Importers can recertify model variants below 5.0 L/100 km within the window. | other | 0.3 | Certification lead times. | Below cut-off; not used. |
| A-11 | Dismantlers fake scrapping on a meaningful scale. | enforcement | 0.25 | Registry deregistration checks; audit frequency; penalties. | Below cut-off; not used. |
| A-12 | Some rebate buyers would otherwise have bought a non-eligible new model. | substitutability | 0.7 | Model mix of buyers who replace 12-year-old cars. | No model shift. |
| A-13 | Used-car imports cannot quickly replace the scrapped cars. | mobility | 0.75 | 25% duty; inspection cost; past import volumes. | Used prices barely rise. |
| A-14 | Repairing an existing old car is a feasible alternative to replacing it for some used-car buyers. | substitutability | 0.8 | Garage density; repair costs against used-car prices. | Repairs decrease. |
| A-15 | Buyers expect the scheme to be repeated. | expectations | 0.35 | Government statements; lobbying strength; history of repeat schemes in the region. | Below cut-off; not used. |
| A-16 | In the window, sellers of eligible models have clearly fewer alternatives than rebate buyers: their stock is fixed by earlier import orders, while rebate buyers can wait, keep their old car or choose a non-eligible model. | substitutability | 0.65 | Importer allocations and lead times; dealer stocks at the start of the window; share of eligible owners who did not take part in comparable schemes. | Sellers' share is ambiguous. |
| A-17 | Repairs, parts and fuel are complements in use of cars, and repairs and parts for older models have few uses other than in older cars. | substitutability | 0.85 | Model-specific parts; garages' share of work on older cars. | No complement chains. |
| A-18 | The scrapped cars used materially more fuel per km than the new cars that replace them. | other | 0.9 | Certified consumption of cars 12 or more years old against the 5.0 L/100 km eligibility limit. | No fuel chain. |
| A-19 | Some window purchases are additional: some rebate buyers would not have bought a new car within three years of the window (they would have kept their car or bought a used one). | other | 0.8 | Share of owners of 12-year-old cars who buy new; buyer surveys in comparable schemes. | Total over the period unchanged. |
| A-20 | The dips consist only of purchases moved into the window: buyers do not delay later purchases to wait for a repeat scheme (the opposite of A-15). | expectations | 0.65 | Government statements; history of repeat schemes in the region. | Post-window dip deeper; total ambiguous. |
| A-N1 | The bonds are bought largely with savings that would otherwise have been lent to other borrowers in Vestria. | revenue_use | 0.6 | Share of government bonds held by domestic savers and banks; foreign holdings of Vestrian bonds. | C-25 vanishes (the cost falls instead on foreign lenders' other uses). |
| A-N2 | Some buyers of older used cars are at the margin between a domestic used car and an imported one, so a rise in domestic prices brings some imports despite the duty. | mobility | 0.6 | Past import volumes and their response to used-car prices; duty and inspection cost against price differences. | C-20 vanishes. |
| A-N3 | Rebate buyers drive their new cars about as far as they drove the cars they scrapped. | other | 0.7 | Odometer records at scrapping and first service; travel surveys. | C-24 becomes ambiguous. |

**Not reported** (an assumption below 0.5):
- Importers recertify variants to qualify: `reclassification` increase (A-10, p 0.3).
- Fake scrapping, with parts resold: `informal_activity` increase among dismantlers (A-11, p 0.25).
- Buyers expect a repeat and delay later purchases: deeper `quantity_traded` decrease after the window and more `lobbying_effort` (A-15, p 0.35).

## 11. Report

**The policy:** Private buyers who scrap a drivable car aged 12 or more, registered to them since before 15 March, get V$4,000 off an eligible new car (5.0 L/100 km or less) bought between 1 July and 31 December, up to 120,000 rebates, first come, first served. The old car must be crushed without resale of parts. The scheme is funded by bonds repaid over ten years.

**Visible consequences:** Rebate buyers pay less, net (C-1), and buy more eligible new cars in the window (C-2); dismantlers crush more cars (C-3); new-car sales stall between March and July (C-5); the registry spends on administration (C-27).

**Invisible consequences:**
- *Sellers and other buyers:* with stock fixed for the window, part of the rebate goes to importers and dealers through higher pre-rebate prices (C-13, C-15, C-14), and fleets and other non-rebate buyers of eligible models pay more (C-12); sales of non-eligible models fall (C-8); claims are rationed by arrival if the budget runs out (C-9).
- *After the window:* new-car sales and seller prices dip (C-6, C-16); importers lobby for more (C-11); over the window and three years, total new-car sales are higher only by additional purchases (C-7).
- *Used-car market:* owners of remaining older cars gain value from March (C-17); used-car buyers pay more and buy fewer older cars (C-18, C-19, C-29), and some import (C-20); the scrapped cars' remaining years of use are lost (C-28).
- *Complements:* owners repair failing cars to qualify (C-10); fewer used parts for older models come to market later (C-22); less fuel is sold (C-24).
- *Funding:* future taxpayers repay the bonds (C-26); present borrowers face competition for savings (C-25); rebate buyers' own spending moves into the window (C-30, C-31).

**Ambiguous effects:** Repair work on older cars (fewer older cars against buyers who repair instead of buying) (C-21); prices of parts for older models (less supply against less demand) (C-23).

**Key conditions:** Many owners value the rebate above their car (A-2, 0.9); sellers do not capture all of it (A-1, 0.85) though they capture part because their stock is fixed (A-7, 0.7; A-16, 0.65); scrapped cars would have stayed in use (A-4, 0.85); purchases are pulled forward (A-3, 0.85) without waiting for a repeat (A-20, 0.65). Three new premises: bonds draw on domestic savings (A-N1, 0.6), some used-car buyers can import (A-N2, 0.6), and replacement cars are driven about as far (A-N3, 0.7).

**What this analysis cannot say:** how large any change is; whether the extra sales, the fuel saving or the gains to sellers outweigh the costs to taxpayers, used-car buyers and borrowers; whether the policy is good. Environmental and safety effects of newer cars and of scrapping are out of scope for version 1 and are not analyzed here.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.rebate (owners of eligible old cars who take the rebate) | price_paid (eligible new cars, net of the rebate) | decrease | short | visible | B | CR-1 op. 3 and 4 (V$4,000 attached to the option scrap-and-buy); CR-12b resolved by A-1 against C-13 | A-1 |
| C-2 | buyers.rebate (owners of eligible old cars who take the rebate) | quantity_traded (eligible new cars, 1 July to 31 December) | increase | short | visible | B | CR-4b (x: keep the old car, y: scrap it and buy an eligible new car), for owners who rank the rebate above their car's value and the cost of buying sooner | A-1, A-2 |
| C-3 | dismantlers | quantity_traded (eligible old cars delivered for scrapping) | increase | short | visible | B | CR-1 op. 1 (K2: rebate cars must be crushed, parts not resold); CR-9 (input_to: each rebate sale delivers a car) | A-2 |
| C-4 | importers and dealers (sellers.current) | compliance_cost | increase | short | invisible | A | CR-1 op. 3 (claims, invoice deduction, checks of registration and certificates); CR-8c |  |
| C-5 | buyers.new_cars (all private buyers) | quantity_traded (new cars, 15 March to 30 June) | decrease | short | visible | B | CR-10a; CR-4b (x: buy now, y: wait for 1 July and the rebate) | A-5 |
| C-6 | buyers.new_cars (all private buyers) | quantity_traded (new cars, the year after the window) | decrease | medium | invisible | B | CR-10a (purchases moved into the window are not repeated after it); arithmetic | A-3, A-20 |
| C-7 | buyers.new_cars (all private buyers) | quantity_traded (new cars, window plus the following three years) | increase | long | invisible | B | Arithmetic: purchases moved in time cancel over the period (CR-10a), additional purchases do not (CR-4b, x: keep the old car or buy used, y: buy new) | A-19, A-20 |
| C-8 | sellers.substitutes (non-eligible new models) | quantity_traded (non-eligible new models, window) | decrease | short | invisible | B | CR-4b (x: non-eligible model, y: eligible model with the rebate) | A-12 |
| C-9 | owners of eligible old cars | allocation_by_non_price_criteria (rebates) | increase | short | invisible | B | CR-6 (rebates are offered at a fixed amount from a fixed budget, so when claims exceed 120,000 they go first come, first served; pressure moves to timing and to dealer relationships); CR-10a (claims rush to early in the window) | A-6 |
| C-10 | owners of eligible old cars (failing roadworthiness) | quantity_complement (repairs and inspections on cars about to be scrapped) | increase | short | invisible | B | CR-4b (x: scrap or keep a failing car without the rebate, y: repair it to obtain the certificate and the rebate) | A-8 |
| C-11 | importers and dealers (sellers.current) | lobbying_effort | increase | medium | invisible | B | CR-4b (x: accept expiry, y: lobby for extension or repetition), stronger in the post-window dip | A-9 |
| C-12 | buyers.non_rebate (fleets, buyers without an eligible car) | price_paid (eligible new models) | increase | short | invisible | B | CR-6 first paragraph (planned purchases of eligible models rise against stock fixed for the window); CR-7b (the benefit settles on the side with fewer alternatives, here the sellers); CR-9 | A-7, A-16 |
| C-13 | buyers.rebate (owners of eligible old cars who take the rebate) | price_paid (eligible new cars, before the rebate) | increase | short | invisible | B | CR-6 first paragraph; CR-7b with the premise that sellers have fewer alternatives in the window | A-7, A-16 |
| C-14 | importers and dealers (sellers.current) | subsidy_share_received | increase | short | invisible | B | CR-7b (the benefit of a subsidy settles on the side with fewer alternatives: sellers whose stock is fixed by earlier import orders) | A-7, A-16 |
| C-15 | importers and dealers (sellers.current) | net_price_received (eligible models) | increase | short | invisible | B | CR-6 first paragraph; CR-7b | A-7, A-16 |
| C-16 | importers and dealers (sellers.current) | net_price_received (new cars, the year after the window) | decrease | medium | invisible | B | CR-6 first paragraph (planned purchases fall in the dip, C-6) | A-3, A-20 |
| C-17 | owners of non-scrapped older cars | asset_value (older used cars) | increase | short | invisible | B | CR-7c (an expected lasting fall in the stock of older cars raises their value when it becomes expected, from March); CR-9 | A-4, A-13 |
| C-18 | buyers.used_cars | price_paid (older used cars) | increase | medium | invisible | B | CR-6 first paragraph (the scrapped cars leave the stock the used market draws on); CR-9 | A-4, A-13 |
| C-19 | buyers.used_cars | quantity_traded (older used cars) | decrease | medium | invisible | B | CR-4c after C-18; fewer cars available | A-4, A-13 |
| C-20 | buyers.used_cars | cross_border_purchases (imported used cars) | increase | medium | invisible | B | CR-4b (x: domestic used car, y: imported used car despite the 25% duty), after C-18 | A-4, A-N2 |
| C-21 | sellers.complements (repair garages) | quantity_complement (repair work on older cars) | ambiguous | medium | invisible | B | (-) CR-9, LW-10 (fewer older cars in use, so less repair work on them); (+) CR-4b (x: buy a dearer used car, y: repair the existing one); CR-12b | A-4, A-14, A-17 |
| C-22 | sellers.complements (used parts for older models) | quantity_supplied (used parts for older models) | decrease | long | invisible | B | CR-10b (cars that would later have reached dismantlers and yielded parts are crushed now, K2); CR-8a | A-4, A-17 |
| C-23 | buyers of parts for older models | price_complement (parts for older models) | ambiguous | long | invisible | B | (+) CR-6 first paragraph, less used-parts supply (C-22); (-) CR-9, fewer older cars needing parts; CR-12b | A-4, A-17 |
| C-24 | sellers.complements (fuel sellers) | quantity_complement (fuel) | decrease | long | invisible | B | CR-9, LW-10 (demand for fuel follows the fuel used by the fleet; replacement cars use less per km) | A-4, A-18, A-N3 |
| C-25 | borrowers.private (domestic capital market) | resources_available_other_uses | decrease | medium | invisible | B | CR-8a (savings lent to the government through K3's bonds are withdrawn from other borrowers); CR-7a | A-N1 |
| C-26 | taxpayers (future) | resources_available_other_uses | decrease | long | invisible | A | CR-8a, CR-8b (rebates, handling fees, administration and interest are repaid from general revenue over 10 years; every rebate counted as a gain is matched here) |  |
| C-27 | officials.enforcement (vehicle registry) | enforcement_cost | increase | short | visible | A | CR-8c; K4 |  |
| C-28 | sellers.current (owners who would have sold older cars) | quantity_supplied (older used cars) | decrease | medium | invisible | B | CR-8a (the remaining service of each scrapped car is destroyed rather than used by its owner or a later buyer) | A-4 |
| C-29 | buyers.used_cars | resources_available_other_uses | decrease | medium | invisible | B | CR-8b (the gain to owners of older cars in C-17 is the matching outlay of their buyers); CR-3a | A-4, A-13 |
| C-30 | buyers.rebate (owners of eligible old cars who take the rebate) | resources_available_other_uses (in the window) | decrease | short | invisible | B | CR-10a and CR-8d (spending on a car is moved into the window or added, net of the rebate) | A-3, A-19 |
| C-31 | buyers.rebate (owners of eligible old cars who take the rebate) | resources_available_other_uses (in the years they would have bought) | increase | medium | invisible | B | CR-10a (the purchase they would have made later is not made) | A-3 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, LW-10 and arithmetic.

**(b) New premises.**
- A-N1 (bonds draw on domestic savings, p 0.6): CR-8a says the borrowed means are withdrawn from another use, but who would otherwise have used them, domestic borrowers or foreign ones, is the empirical `revenue_use` question CR-8 names; none of the case assumptions answers it.
- A-N2 (some used-car buyers can import, p 0.6): A-13 says imports cannot *quickly* replace the scrapped cars; CR-4b's margin premise that some buyers do switch to imports is not among the case assumptions.
- A-N3 (replacement cars driven about as far, p 0.7): A-18 is per km; the fuel chain needs a premise about distance driven, because a newer car could be driven more.

**(c) Unclear core rules.**
- CR-6 for a capped, first-come subsidy: CR-6 is stated for a market price prevented from moving. A fixed rebate amount from a fixed budget is a price held fixed only in a stretched sense (the "good" is the rebate, offered at zero); applying CR-6's displaced-pressure margins to it (C-9) is a reading of the rule.
- CR-7b and CR-12b on incidence: CR-7b says the benefit settles on the side with fewer alternatives, which, with A-16, gives a direction for the sellers' share, but not whether the net price to rebate buyers still falls. That needed A-1, an empirical premise. The core rules do not say whether a CR-7b premise counts as a "dominance" premise under CR-12b or only as a direction for one side.
- CR-10a and the timing-shift convention: the rule licenses "rushes before deadlines" but gives no guide to how windows should be cut when the announcement, start and end dates all differ; the windows used here (15 March to 30 June, the window, the year after, the window plus three years) are the analyst's choice.
