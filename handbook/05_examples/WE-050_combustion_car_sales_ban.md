# WE-050 Ban on sales of new combustion-engine cars from 2035

Analyst: draft (Handbook 0.9, held-out test)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized policy in a fictional country. It resembles the end-of-sale dates for combustion cars that several countries have announced, but it is not modeled on any one of them. It is part of a held-out test of catalog 0.9: the 0.9 changes were drawn from WE-036 to WE-045, and this case asks whether they work, as written, on a case they were not drawn from. It probes EN-14 (a standard on new units, with the stock exempt), TS-3's clause on product standards (where the counterfactual trend moves toward the standard anyway), RS-8's 0.9 clause on opposing timing chains (a rush by buyers before the deadline against sellers who withdraw models and pre-register stock), CR-7's 0.9 clause on persistence following the stock and CR-10b (the value of used combustion cars), CR-12's 0.9 clause on what the response argument gives (imports of used cars as a partial response), RS-16's 0.9 clause on costs attached to the substitute (a road charge on electric cars), and CR-6's 0.9 clause on splitting a shift between price and quantity. The unclear provision is whether a used car imported from abroad after 2035 counts as "new". Effects on emissions, air quality, health and safety are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Vessmark Clean Cars Act.** Vessmark is a country of about 9 million people with about 4.8 million registered passenger cars, of average age 10 years. Cars are scrapped at about 17 years on average, about 260,000 a year. Vessmark has no car assembly: every new car is imported by about 12 brand importers and sold through about 600 dealers. Vessmark buys about 0.4% of the world's new cars.

In 2025 about 280,000 new cars were sold: 196,000 (70%) with combustion engines only (petrol, diesel, conventional hybrids), 28,000 (10%) plug-in hybrids (PHEVs) and 56,000 (20%) battery-electric cars (BEVs). A typical new combustion compact costs about $30,000 and a comparable BEV about $36,000; the importers' association forecasts the gap at about $2,000 by 2035. Its forecast without new rules is that BEVs reach about 50% of new sales by 2035 and about 80% by 2045, the rest combustion and PHEVs. A five-year-old combustion compact sells for about $15,000.

About 650,000 used cars change hands a year. About 25,000 of them are imported used from Drevland, the larger neighbor to the south (about 3.5 million used-car sales a year), which has no ban and no announced date. Used cars are already imported at import parity: Vessmark's used prices for comparable cars sit about $1,800 above Drevland's, the cost of transport, the state's import roadworthiness inspection ($900) and registration. The inspection is done only at state test centers, whose capacity is about 40,000 cars a year.

Vessmark has about 2,100 fuel stations and 9,000 public chargers. Fuel excise is $0.70 a liter, about $600 a year for an average combustion car, and raises about $2.6 billion a year for the general budget. About 3,500 independent repair shops employ about 14,000 mechanics. Existing rules, in force on both paths: the fuel excise; the import inspection; a resident may drive a foreign-registered car in Vessmark for at most six months.

The bill was introduced on 3 March 2026, passed on 18 June 2026 by a large cross-party majority, and enacted on 30 June 2026. It has no expiry. Section 9 requires the Minister to report on "the readiness of the charging network" by 30 June 2031 and allows the Minister, by order, to postpone the dates in sections 3 and 4 by up to three years.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 End of sale (s. 3) | `product_standard` (a new passenger car must have no combustion engine) | First registration of new passenger cars | Vehicle Registry; importers and dealers | "From 1 January 2035 the Registry shall not register for the first time a new passenger car fitted with an internal combustion engine." Section 2: "'new passenger car' means a passenger car that has not previously been registered." | PHEVs, under K2. |
| K2 Plug-in hybrids (s. 4) | Dated exemption from K1 | New PHEVs with at least 50 km of electric range | as K1 | Exempt until 31 December 2037; banned from 1 January 2038. | — |
| K3 Existing cars (s. 5) | Saving clause | Cars registered before the dates | — | "Nothing in this Act affects the use, sale, transfer or re-registration of a car registered before the date in section 3 or 4." | — |
| K4 Enforcement (s. 7) | Enforcement | K1, K2 | Vehicle Registry | Registration refused; selling an unregistrable new car as new is an offence, fine $5,000. The Registry's budget is fixed by law; no new funds. | — |
| K5 Road charge (s. 8) | `lump_sum_tax` per car per year (operation 3 on owning a BEV) | Battery-electric passenger cars | Owners of BEVs | $250 a year from 1 January 2035, collected with the annual registration renewal; to the general budget. Stated purpose: "to replace fuel excise". | PHEVs (which pay fuel excise). |

Unclear provision:
- **U1, "not previously been registered" (s. 2).** The Act does not say registered where. Reading U1-a: previously registered in Vessmark. A car first registered in Vessmark after 2035 is "new" whatever its age, so used combustion cars imported from abroad can no longer be registered. Reading U1-b: previously registered anywhere. A used combustion car registered in Drevland can still be imported and registered after 2035, and so can a new one registered in Drevland first. The Registry has issued no rule and no court has ruled. Readings get no probability; where a sign depends on one, each reading's sign is reported.

**Figures.** On the forecast trend (A-1), counterfactual new combustion sales (excluding PHEVs) fall from about 196,000 in 2025 to about 110,000 in 2035 and about 40,000 in 2045; PHEVs stay near 25,000 a year. With the Act, combustion sales are zero from 2035 and PHEV sales zero from 2038. The combustion fleet (including PHEVs) is about 4.4 million in 2026. With the Act it falls to about 3.9 million in 2035, 2.9 million in 2040 and 1.7 million in 2045; on the counterfactual path it is about 3.9, 3.4 and 2.8 million. Most cars in the fleet in 2026 are scrapped by about 2043. Under U1-b, imports of used and nearly-new combustion cars can grow by at most about 15,000 a year above today's 25,000 until inspection capacity grows, against about 110,000 counterfactual buyers of new combustion cars a year in 2035.

The counterfactual is Vessmark without the Act: no end-of-sale date, no road charge, the BEV share rising on the forecast trend.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: forbids exchanges between importers or dealers and buyers of new combustion cars (CR-1, operation 1, dated 1 January 2035; before then it acts through expectations, CR-10a, while durable assets revalue at once, CR-7c; CR-1 0.7 on dated operations). The counterfactual law has no such rule. | Binds on the share of new cars that would still have combustion engines from 2035 (A-1); that share shrinks over time on the trend (TS-3, product standards). | EN-14, TS-3, CR-1, CR-4, CR-6 (0.9: splitting a shift), CR-7c, CR-7 (0.9: persistence), CR-10, RS-1, RS-4, RS-5, RS-8, RS-12, RS-16, OC-4 |
| K2 | Triangular, dated three years later | Binds on would-be PHEV buyers from 2038 (A-1). | RS-8, CR-12h, RS-1 |
| K3 | Keeps every option for the stock | — | EN-14 (stock exempt), CR-7c |
| K4 | Binary: enforcement from a fixed budget | Registration is near-perfect enforcement for cars registered in Vessmark (A-2). | OC-3 (0.9: fixed budget), CR-8c |
| K5 | Binary: a charge on owning a BEV, CR-1 operation 3 (paid only if one owns a BEV), operation 4 in effect for those who keep their car | Yes, from 2035 | TX-1, RS-16 (0.9: costs on the substitute), CR-3 (note), CR-8b, TX-10 |

A ban on combustion engines in new cars is classed as a `product_standard` rather than a `prohibition`: the good (a car) stays legal, existing units stay legal and tradable, and what is forbidden is new units below a specification (here a yes-or-no one: no combustion engine). That is EN-14's situation.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `buyers.new_combustion` | Those who would buy a new combustion car from 2035 | Option removed (CR-3a); may buy a BEV, a PHEV until 2037, a used car, keep their car, or buy in 2033 to 2034. |
| `buyers.new_phev` | Those who would buy a new PHEV from 2038 | Option removed from 2038. |
| `buyers.new_cars` | All buyers of new cars | The set of new cars is narrowed. |
| `buyers.used_combustion` | Buyers of used combustion cars | Face buyers displaced from new combustion cars. |
| `owners.combustion.2026` | Owners of combustion cars at enactment | Their cars are part of a stock that will no longer be added to. |
| `owners.combustion` | Owners of combustion cars at any date | Keep, repair, sell. |
| `owners.bev` | Owners of BEVs, existing and new | Pay $250 a year from 2035. |
| `owners.bev.existing` | Owners of BEVs at enactment | Used BEVs are a substitute for new combustion cars; the charge is capitalized. |
| `importers` | Brand importers | May not register new combustion cars from 2035; choose which models to certify and market before then. |
| `dealers` | Car dealers | May pre-register unsold combustion stock before the date. |
| `importers.used` | Importers of used cars from Drevland | Under U1-a, lose combustion imports from 2035; under U1-b, keep them. |
| `sellers.foreign` (Drevland used-car sellers) | Sell used cars to Vessmark | Vessmark demand is under 1% of their market. |
| `sellers.complements` (fuel retailers) | 2,100 fuel stations | Fewer combustion cars in use from 2035 on. |
| `sellers.complements` (charging) | Public charging operators | More BEVs in use. |
| `repair_shops` | Independent repairers and their 14,000 mechanics | Older combustion cars kept longer; fewer combustion cars later. |
| `fuel_station_workers` | Staff of fuel stations | Volume falls in the long run. |
| `officials.enforcement` | Vehicle Registry | New checks at first registration, from a fixed budget. |
| `taxpayers` (general budget) | Funders of, and recipients from, the general budget | Fuel excise falls; road charge arrives. |
| Interest groups | Dealers, fuel retailers, motoring clubs; BEV importers, charging firms | Stakes in the 2031 review. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.new_combustion`, `importers` | `quantity_traded` (new combustion cars first registered, from 2035) | decrease | medium to long (from 1 January 2035) | CR-1, EN-14, TS-3, OC-4, CR-5a | A-1, A-2, A-3 |
| C-2 | `buyers.new_phev`, `importers` | `quantity_traded` (new PHEVs first registered, from 2038) | decrease | medium to long (from 1 January 2038) | CR-1, EN-14, TS-3, OC-4 | A-1, A-2, A-3 |
| C-3 | `owners.bev` | `resources_available_other_uses` (the road charge) | decrease | medium to long (from 2035) | CR-1, TX-1, CR-3 (note), CR-8b | A-2 |
| C-4 | `taxpayers` (general budget) | `tax_revenue` (road charge) | increase | medium to long (from 2035) | TX-1, CR-8b | A-2 |

C-1 and C-2 are the Act's purpose. Against the counterfactual, where about 110,000 new combustion cars a year are sold in 2035 and fewer each year after, the number first registered is zero (A-1, A-2), and so are PHEVs from 2038. Each prevented sale is an exchange both sides expected to gain from (OC-4, CR-5a): buyers and importers and dealers lose those gains. C-1 holds only if the 2031 review does not postpone the date (A-3); if it does, every post-2035 sign moves three years later. C-3 and C-4 are the two sides of the road charge (CR-8b). Owners who keep a BEV pay it every year, so their means for other uses fall (CR-3, note).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | `buyers.new_combustion` | `quantity_substitute` (new BEVs registered) | increase | medium (2035 on) | RS-1, RS-16, CR-6 (0.9: splitting a shift), CR-12b, CR-12e (dominance, A-22) | A-1, A-3, A-5, A-22 |
| C-6 | `buyers.new_combustion` (those who buy a new BEV instead) | `price_paid` (purchase price of the new car bought) | increase | medium | EN-14, CR-4, CR-3a | A-1, A-23 |
| C-7 | `buyers.new_cars` | `quantity_traded` (all new cars) | decrease | medium | CR-4a, CR-12e (response argument), CR-12 (0.9: partial response, A-4) | A-1, A-3, A-4 |
| C-8 | `buyers.new_phev` | `quantity_traded` (new PHEVs, 2035 to 2037) | increase | short to medium (2035 to 2037) | RS-1, RS-8, CR-10a | A-1, A-3, A-25 |
| C-9 | `buyers.new_combustion` | `quantity_traded` (new combustion cars bought by final buyers, 2033 to 2034) | ambiguous | short (2033 to 2034) | RS-8 (0.9: opposing timing chains), CR-10a, CR-4, CR-12b | A-7, A-8, A-9, A-29 |
| C-10 | `importers` | `variety` (combustion models offered in Vessmark, 2031 to 2034) | decrease | short to medium (2031 to 2034) | CR-4 (0.7: fixed costs per item offered), CR-10a | A-3, A-8 |
| C-11 | `dealers` | `inventory_held` (combustion cars registered before 1 January 2035 and unsold on that date) | increase | short (end of 2034) | RS-8, RS-5, CR-10a, CR-12 (0.9: an activity that exists only under the policy) | A-3, A-9 |
| C-12 | `importers.used` | `quantity_traded` (used combustion cars imported, 2026 to 2034) | increase | short to medium | RS-4, CR-7a, CR-7c, CR-10a | A-3, A-11, A-20 |
| C-13 | `importers.used` | `quantity_traded` (used combustion cars imported, from 2035) | U1-a: decrease; U1-b: increase | medium | CR-1, RS-4, CR-7a, CR-12e | A-2, A-3, A-20 |
| C-14 | `importers.used` | `reclassification` (new combustion cars registered briefly in Drevland and imported as used, from 2035) | U1-a: no_change; U1-b: increase | medium | RS-5, CR-4 | A-21 |
| C-15 | `owners.combustion` | `maintenance_spending` (repairs to keep older combustion cars in use) | increase | medium (2035 to 2040) | EN-14, CR-10b, CR-4 | A-1, A-3, A-19 |
| C-16 | `owners.combustion` | `quantity_traded` (combustion cars scrapped, 2035 to 2040) | decrease | medium (2035 to 2040) | EN-14, CR-10b, CR-4, CR-12g | A-1, A-3, A-19 |
| C-17 | `owners.combustion` | `quantity_traded` (combustion cars scrapped, after 2040) | ambiguous | long | CR-10b, CR-12b, CR-12g | A-4, A-19 |
| C-18 | Dealers, fuel retailers, motoring clubs; BEV importers, charging firms | `lobbying_effort` (on postponement at the 2031 review) | increase | short to medium (2026 to 2031) | RS-7, CR-4 | A-15 |

**Where would-be buyers of new combustion cars go (C-5 to C-8).** The Act removes their chosen option (CR-3a). By CR-4 they take their next-best: a new BEV, a PHEV until 2037 (C-8; A-25), a used combustion car (C-20), a used BEV (C-23), or keeping their present car longer (C-15, C-16). Those who buy a BEV pay more for the car than for the combustion car they would have bought (C-6; A-23): EN-14's "new units cost more". This is the purchase price only; whether they spend more in total, given lower running costs, is not signed (CR-3, note). New BEVs registered rise (C-5): Vessmark is about 0.4% of the world market and importers have eight years' notice, so the shift in demand is met mainly by quantity (CR-6, 0.9: the split needs a premise on supply, A-5). The premise that supply cannot expand at once in 2035 (A-6) is below the cut-off, so no short-run price rise for new BEVs is signed; the price of new BEVs is not signed at all (see below). The road charge (K5) is an opposing chain on C-5: it makes a BEV dearer to own relative to a used combustion car, a PHEV, or keeping one's present car, so some who would have bought a BEV anyway do not (CR-4). Both chains are derived. The charge is $250 a year against about $600 of fuel excise a combustion car pays, and the ban removes the choice of about half of new-car buyers in 2035, so the ban chain dominates (A-22, empirical, p = 0.85).

**Total new cars (C-7).** Every new car a would-be combustion buyer now buys (a BEV or PHEV) was open to them without the Act, and they did not choose it then. By CR-4a no one who chose a BEV switches to buying more new cars because the combustion option was removed. So the moves to BEVs and PHEVs are a response that cannot raise total new-car purchases above the counterfactual (CR-12e, response argument). To report `decrease` rather than a decrease or no change, the response must be partial (CR-12, 0.9): some would-be combustion buyers rank a used car or keeping their car above a new BEV or PHEV (A-4).

**The rush before the deadline, and what opposes it (C-9 to C-11).** RS-8: a buyer who wants a new combustion car and would have bought in 2035 or 2036 can buy in 2033 or 2034 (A-7): purchases rise in the last window before the deadline. Two chains push the other way in the same window, and RS-8's 0.9 clause says to combine all of them. (i) Importers bear a fixed cost per model offered in Vessmark (certification, marketing, parts stocks), recovered over the years the model sells. From 2031 the remaining window is short, so some combustion models are not launched or are withdrawn early (C-10; CR-4, 0.7; A-8); some buyers of those models buy something that is not a new combustion car. (ii) Dealers may register unsold combustion cars before 1 January 2035 so that they remain sellable afterwards, as used cars (C-11; A-9). Sellers thus move earlier and buyers can move later: some buyers who would have bought new in late 2034 wait for pre-registered stock, which dealers must clear in 2035 below the new price (A-29). So for final buyers' purchases in 2033 to 2034 one chain is (+) and two are (−), each with p ≥ 0.5: `ambiguous` (C-9; CR-12b). Registered-but-unsold stock at the deadline exists only under the Act: `increase` (C-11; CR-12, 0.9). In 2035 and after, new combustion sales are zero (C-1), so the rush is not netted against a dip: the later window is C-1.

**Used imports (C-12 to C-14).** Imports already run at import parity (A-20): Vessmark's used price for a comparable car is Drevland's plus about $1,800. When Vessmark's used combustion prices rise (C-19, C-20), imports rise (CR-7a across the border; RS-4). Before 2035 this holds under both readings, because the premium on cars that will still be in use after 2035 is capitalized from 2026 (C-12). From 2035 the readings part. Under U1-a, a used car first registered in Vessmark after the date is "new", so combustion imports stop against about 25,000 a year on the counterfactual path: `decrease`. Under U1-b they continue and rise with the price gap: `increase` (C-13). Under U1-b a further route opens: a new combustion car registered for a day in Drevland is "previously registered" and can be imported and registered as used (C-14; RS-5; A-21). Under U1-a such a car is "new" and refused: `no_change` against the counterfactual, where no one does this. These signs are each against the counterfactual, not U1-a against U1-b.

**The stock kept longer (C-15 to C-17).** EN-14: the existing units are kept in use longer (CR-10b). A combustion car's value now exceeds the cost of repairing it in more cases (A-19), so owners repair rather than scrap: repair spending rises and scrapping falls in 2035 to 2040 (C-15, C-16). Scrapping happens with and without the Act, at different times, so it is signed per window (02_ontology.md, 2.5; CR-12g). After 2040 two chains meet: the retained cars are scrapped later (+), and fewer combustion cars were bought, so fewer reach scrapping age (−): `ambiguous` (C-17).

**Lobbying (C-18).** The 2031 review is a concentrated stake on both sides: dealers, fuel retailers and motoring clubs gain from postponement, BEV importers and charging operators from keeping the date (RS-7; A-15). Neither side lobbies on this question on the counterfactual path.

**Evasion.** Residents could keep a combustion car registered in Drevland; the six-month rule makes it an offence (A-14, p = 0.3, below the cut-off: noted, not reported).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-19 | `owners.combustion.2026` | `asset_value` (combustion cars held at enactment) | increase | short (from June 2026, more as the 2031 review passes) | EN-14, SB-4, CR-7c, CR-10c, CR-12e (dominance, A-11) | used and new combustion cars: `same_market_other_segment`, close | A-1, A-3, A-11 |
| C-20 | `buyers.used_combustion` | `price_paid` (used combustion cars, 2035 to 2040) | increase | medium | EN-14, RS-16, CR-6 (0.9: splitting a shift), CR-12e (response argument), CR-12 (0.9: partial response), CR-12e (dominance, A-11) | as C-19; Drevland used cars `across_border` | A-1, A-2, A-3, A-4, A-11, A-12 |
| C-21 | `owners.combustion` (who sell) | `net_price_received` (used combustion cars, 2035 to 2040) | increase | medium | CR-8b, OC-7 | as C-20 | A-1, A-2, A-3, A-4, A-11, A-12 |
| C-22 | `buyers.used_combustion` | `price_paid` (used combustion cars, after 2040) | ambiguous | long | CR-12b, CR-12 (0.8: kind 2), TS-3, CR-7 (0.9: persistence), RS-12 | fuel and repairs `complement` of combustion cars | A-1, A-10 |
| C-23 | `owners.bev.existing` | `asset_value` (BEVs held at enactment) | ambiguous | short (from June 2026) | RS-16 (0.9: costs on the substitute), CR-7c, CR-10c, CR-12b | used BEVs and new combustion cars: `substitute`, partial | A-2, A-3, A-27 |
| C-24 | `sellers.complements` (fuel retailers) | `quantity_complement` (fuel sold) | decrease | medium to long | RS-12, CR-9, CR-12e (dominance, A-16) | fuel `complement` of combustion cars | A-1, A-3, A-16 |
| C-25 | `sellers.complements` (fuel retailers) | `number_of_sellers` (fuel stations) | decrease | long | RS-12, CR-4 (0.8: a cost fixed per outlet) | as C-24 | A-1, A-3, A-16, A-17 |
| C-26 | `sellers.complements` (fuel retailers) | `asset_value` (fuel station businesses and sites) | decrease | short (from June 2026) | SB-4, CR-7c, CR-10c | as C-24 | A-1, A-3, A-16, A-17 |
| C-27 | `fuel_station_workers` | `employment`, `hours_worked` | at_least_one_decrease | long | RS-6, CR-9 | station labor `input_to` fuel retailing | A-16, A-17, A-18 |
| C-28 | `sellers.complements` (charging) | `quantity_complement` (public charging sold) | increase | medium | RS-12, CR-9 | charging `complement` of BEVs | A-5, A-22, A-24 |
| C-29 | `repair_shops` | `quantity_traded` (repairs of combustion cars, 2035 to 2040) | increase | medium | CR-9, RS-12, CR-12e (dominance, A-26) | repairs `complement` of combustion cars | A-19, A-26 |
| C-30 | `repair_shops` | `quantity_traded` (repairs of combustion cars, after 2040) | ambiguous | long | CR-9, RS-12, CR-12b | as C-29 | A-10, A-19 |
| C-31 | `owners.combustion` | `travel_time` (to refuel) | increase | long | RS-12, CR-9 | as C-24 | A-16, A-17 |
| C-32 | `taxpayers` (general budget) | `tax_revenue` (fuel excise) | decrease | medium to long | TX-10, CR-9 | as C-24 | A-1, A-3, A-16 |
| C-33 | `taxpayers` (general budget) | `tax_revenue` (fuel excise and road charge together) | ambiguous | medium | CR-12b, CR-12 (0.8: two items in one variable) | — | A-2, A-16 |

**Used combustion cars: the stock exempt (C-19 to C-21).** EN-14: existing units now face no competition from new combustion cars, so their value rises (CR-7c). The used market is where displaced buyers go (RS-16): after 2035 the stock of combustion cars can only shrink, so the shift in demand goes mainly to price (CR-6, 0.9: the supply of the stock is fixed in the period; the split is signed on that premise). Under U1-a nothing else can add to it; the only way to add units is the rush and pre-registration before the date (C-9, C-11), which are themselves responses to the premium and cannot remove it, since they stop once buying early costs as much as the premium is worth (CR-12e). Under U1-b imports respond (C-13, C-14). They cannot push Vessmark's used price below its no-Act level, since imports stop once the price gap is no more than the cost of importing (CR-12e). To report `increase` rather than an increase or no change, the response must be partial (CR-12, 0.9). Here that follows from the case's figures: inspection capacity allows about 15,000 more imports a year against about 110,000 displaced buyers a year, and A-12 (p = 0.6) says capacity is not expanded enough by 2040 to close the gap. So used prices rise in 2035 to 2040 under both readings (C-20), by less under U1-b. Sellers receive what buyers pay (C-21; CR-8b, OC-7).

Three chains oppose the rise. (i) Complements thin as the combustion fleet shrinks (fewer stations, scarcer combustion repair: C-25, C-31), lowering a combustion car's value in use (A-10, p = 0.6). The fleet with the Act is about 3.9 million in 2035 against 3.9 million counterfactual, and 2.9 against 3.4 million in 2040, so thinning is slight before 2040; A-11 (p = 0.7) states that for 2035 to 2040 the scarcity chain dominates. (ii) Owners may expect further restrictions on using combustion cars (A-13, p = 0.3): a chain the rules derive but whose premise falls below the cut-off, so the derived sign is reported and the chain recorded in section 10 (CR-12, 0.8, kind 2). (iii) The road charge makes BEVs dearer to own, which pushes buyers toward used combustion cars: same direction, (+).

**Cars held at enactment (C-19).** Their value rises from June 2026 for the yields they will bring after 2035 (CR-7c, CR-10c), part of the way at once and more as the 2031 review passes without postponement (CR-7c, probability clause; A-3). Most of these cars are scrapped by 2043, so the thinning after 2040 bears on a small tail of their yields (A-11). Buyers of combustion cars after enactment pay the capitalized price, so they neither gain nor lose from the Act as it stands (SB-4).

**After 2040 (C-22).** The scarcity chain continues while the stock gap lasts, and the thinning chain grows; both have premises with p ≥ 0.5, so the combined sign is `ambiguous` (CR-12b). The premium also follows the gap between the actual and counterfactual stock (CR-7, 0.9, read on this path; CR-10b): that gap grows to about 1.1 million cars in 2045 and then narrows as counterfactual combustion sales fall toward zero on the trend (TS-3, product standards: the share of designs the standard binds on shrinks). See section 8.

**Existing BEVs (C-23).** A used BEV is a substitute for a new combustion car for some displaced buyers (A-27), and the stock of used BEVs is fixed in the short run, so RS-16 gives a rise in their price. RS-16's 0.9 clause applies: the policy also attaches a cost to the substitute itself (the road charge, capitalized into BEVs' value from enactment, CR-7c). Two derived chains with p ≥ 0.5: `ambiguous` (CR-12b).

**New BEVs: price not signed.** RS-16 gives a price rise for the substitute only where its supply cannot expand at unchanged cost; with A-5 (world supply expands to Vessmark at world prices) that chain fails, and A-6 (p = 0.3) is below the cut-off. RS-16's 0.9 clause would make the road charge an opposing chain on sellers' net price; but sellers of new BEVs sell worldwide and have far better alternatives than Vessmark's buyers, so the charge is borne by buyers (CR-7b) and leaves sellers' price where it is. The charge appears instead as the opposing chain on quantity (C-5) and on owners' means (C-3). No price consequence is recorded (Gaps found, c2).

**Complements (C-24 to C-31).** RS-12: fuel is used with combustion cars. Vehicle-km in combustion cars fall with the combustion fleet; older cars use somewhat more fuel per km, but not enough to offset (A-16): fuel sold falls (C-24). A station's costs are mostly fixed per outlet (CR-4, 0.8), so as volume falls some close (C-25; A-17), drivers of combustion cars travel further to refuel (C-31), and staff or hours fall (C-27; A-18). The value of station businesses falls from enactment, as the lower expected volume is capitalized (C-26). Charging sales rise with BEVs (C-28). Repairs: the cars missing from the combustion fleet in 2035 to 2040 are new ones, which need few repairs, while the retained cars are old ones, which need many (A-26): combustion repairs rise in that window (C-29), with A-26 dominating the (−) chain from fewer cars. After 2040 both chains have weight: `ambiguous` (C-30).

**Tax (C-32, C-33).** Less fuel sold means less fuel excise (C-32; TX-10). The road charge brings new revenue (C-4). Two items of `tax_revenue` move in opposite directions; the total is `ambiguous` (C-33; CR-12, 0.8). Where the total falls, the shortfall is made up by a group of payers (OC-1, Who pays); since the total is not signed, no such group is recorded.

**Drevland.** Under U1-b, Vessmark's added import demand (at most about 15,000 cars a year, limited by inspection) is under 1% of Drevland's used market: the price effect there is negligible and noted, not recorded (as EN-6's wider-market clause). Under U1-a, Drevland sells about 25,000 fewer cars a year to Vessmark from 2035, also negligible in that market.

Stopping points: spending by fuel station workers and mechanics, landowners of closed stations (depth 3, diffuse); electricity generation (depth 3; out of scope as an environmental question where it concerns emissions).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `buyers.new_combustion`, `quantity_substitute` (new BEVs), medium | Displaced combustion buyers (RS-1, RS-16). | Road charge makes BEVs dearer to own (K5). | A-22 (empirical, on the case's figures) | **increase** (C-5) |
| `buyers.new_cars`, `quantity_traded` (all new cars), medium | Moves to BEVs and PHEVs (a response). | Combustion option removed. | CR-12e (response argument), partial with A-4 | **decrease** (C-7) |
| `buyers.new_combustion`, `quantity_traded` (final buyers), 2033 to 2034 | Rush before the date (A-7). | Models withdrawn (A-8); waiting for pre-registered stock (A-29). | None | **ambiguous** (C-9) |
| `buyers.used_combustion`, `price_paid`, 2035 to 2040 | Displaced buyers against a fixed stock; road charge on BEVs. | Imports under U1-b (a response); rush and pre-registration (responses); thinning of complements (A-10). | CR-12e for the responses, partial from the figures and A-12; A-11 for thinning. Expected further restrictions: A-13, below the cut-off (kind 2). | **increase** under both readings (C-20; C-21 for sellers) |
| `buyers.used_combustion`, `price_paid`, after 2040 | Stock gap. | Thinning (A-10). | None | **ambiguous** (C-22) |
| `owners.combustion.2026`, `asset_value`, short | Capitalized scarcity after 2035. | Capitalized thinning after 2040. | A-11 | **increase** (C-19) |
| `owners.bev.existing`, `asset_value`, short | Displaced buyers turn to used BEVs (A-27). | Road charge capitalized. | None | **ambiguous** (C-23) |
| `sellers.complements`, `quantity_complement` (fuel), medium to long | Older cars use more fuel per km. | Fewer combustion vehicle-km. | A-16 | **decrease** (C-24) |
| `repair_shops`, `quantity_traded`, 2035 to 2040 | Older cars kept longer. | Fewer combustion cars. | A-26 (the missing cars are new and need few repairs) | **increase** (C-29) |
| `repair_shops`, `quantity_traded`, after 2040 | As above. | As above. | None | **ambiguous** (C-30) |
| `owners.combustion`, `quantity_traded` (scrapped), 2035 to 2040 | — | Cars kept longer (A-19). | — | **decrease** (C-16) |
| `owners.combustion`, `quantity_traded` (scrapped), after 2040 | Retained cars scrapped later. | Fewer cars bought. | None | **ambiguous** (C-17) |
| `taxpayers`, `tax_revenue`, medium | Road charge (C-4). | Fuel excise (C-32). | None | **ambiguous** (C-33); each item recorded separately |
| `importers.used`, `quantity_traded` (used combustion imports), from 2035 | U1-b: price gap draws imports. | U1-a: imports refused. | — | U1-a: **decrease**; U1-b: **increase** (C-13) |

## 8. Time structure

Horizons for announcement effects are counted from June 2026; for effects of the ban, from 1 January 2035 (2038 for PHEVs).

- **June 2026 to June 2031: expectation and the review.** Combustion cars and fuel stations revalue at once, part of the way, since postponement is possible (C-19, C-23, C-26; CR-7c, probability clause). Lobbying on the review (C-18). Used imports rise with the capitalized premium (C-12).
- **2031 to 2034: models withdrawn.** As the remaining window shortens, importers launch fewer combustion models for Vessmark (C-10).
- **2033 to 2034: the rush and pre-registration.** Final buyers' purchases are ambiguous (C-9); dealers pre-register unsold stock in the last weeks (C-11), with its registration fees and carrying costs (C-34). Under U1-a, importers also bring used combustion cars in before the date so that they are "previously registered" (part of C-12).
- **2035 to 2037: the PHEV window.** Some displaced buyers buy PHEVs (C-8), and purchases bunch toward the end of 2037 before the second date. Without the Act these purchases would have happened in this window and later, so the bunching inside the window is a path note (CR-12h); C-8 and C-2 sign the windows against the counterfactual.
- **2035 to 2040: the stock premium.** Used combustion prices are above the counterfactual (C-20), cars are repaired and kept (C-15, C-16, C-29).
- **After 2040: thinning and convergence.** Stations close and repair thins (C-25, C-31); used prices and repairs become ambiguous (C-22, C-30). The share of new cars the ban binds on falls each year as the counterfactual trend moves toward BEVs (TS-3, product standards): about 110,000 cars in 2035, about 40,000 in 2045. Every consequence that depends on the size of the gap between the two paths (C-1, C-5, C-7, C-20) shrinks in the long run, without changing sign while A-1 holds.
- **Persistence, if the date were postponed or the Act repealed (CR-7, 0.9; CR-10b; TS-6).** The Act is not a repeal, so `persistence` is not recorded; but A-3 is not certain, and the 0.9 clause says what would follow. If the date were postponed in 2031, no stock would yet have changed except the models withdrawn (C-10): the capitalized premium on combustion cars would fall at once on whoever then holds them (SB-4), with nothing to persist. If the Act were repealed after 2035, the missing vintages (combustion cars not bought in the ban years) would not reappear: that part of the stock change persists. But the premium on used combustion cars depends less on that stock than on the absence of new combustion cars, which world supply can restore within months. So the premium would fall mostly at once, persisting only for young used cars of the missing vintages: partial at most, short-lived. Fuel stations closed after 2040 would reopen only where the restored volume exceeds the cost of reopening (TS-6).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-1 | `buyers.new_combustion`, `importers` | `quantity_traded` (new combustion cars, from 2035) | decrease | The exchanges the ban prevents, and each side's expected gain from them. | OC-4, CR-5a |
| C-34 | `dealers` | `compliance_cost` (registration fees, insurance and financing on pre-registered stock) | increase | Means spent only to keep stock sellable after the date. | CR-8c, OC-2 |
| C-35 | `officials.enforcement` (Registry) | `enforcement_cost` | increase | Staff time checking engine type and, under either reading, the registration history of imports. | OC-3, CR-8c |
| C-36 | Other users of the Registry | `wait_time` (registration and licensing services) (+), other Registry checks (−) | at_least_one_as_stated | The Registry's budget is fixed; the new checks come out of its other work. | OC-3 (0.9: fixed budget), CR-8a |
| C-37 | `importers.used` | `compliance_cost` (import inspections and foreign-registration checks, from 2035) | U1-a: decrease; U1-b: increase | Under U1-a, fewer used imports to inspect; under U1-b, more imports and the checks on brief foreign registrations. | CR-1, CR-8c |

The road charge (C-3) is a transfer, recorded on both sides (C-3, C-4). Pre-registration fees and import inspection fees are receipts to the state for work done, recorded only as the payers' compliance costs. Buyers who would have bought a new combustion car are worse off by their own ranking (CR-3a); that is not signed as less money for other uses, except for the road charge, which owners who keep a BEV must pay every year.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the Act, a material share of new cars sold from 2035 would have combustion engines (about 110,000 a year in 2035, 40,000 in 2045, plus about 25,000 PHEVs a year). | counterfactual_trend | 0.9 | Importers' association forecast; BEV price gap. | The ban binds on few buyers; C-1, C-2 and every consequence that follows shrink toward nothing. |
| A-2 | The Registry refuses first registration of new combustion cars and collects the road charge with renewals. | enforcement | 0.95 | Registration is required to drive legally; existing collection of renewal fees. | C-1, C-2 weaken; C-3, C-4 shrink. |
| A-3 | The 2035 and 2038 dates are not postponed at the 2031 review. | expectations | 0.7 | Cross-party majority; the review is limited to charging readiness. | Every post-2035 consequence moves three years later; the premium in C-19, C-23, C-26 is smaller and falls at postponement. |
| A-4 | Some would-be buyers of new combustion cars rank a used car or keeping their present car above a new BEV or PHEV. | substitutability | 0.85 | Price gap; rural drivers' range needs. | C-7 is a decrease or no change, not reported; the used-car chain of C-20 weakens. |
| A-5 | World supply of BEVs to Vessmark expands at about unchanged cost within the planning period. | alternative_uses | 0.8 | Vessmark buys 0.4% of world cars; eight years' notice. | The shift to BEVs splits into price as well as quantity; new BEV prices rise. |
| A-6 | In 2035, BEV supply to Vessmark cannot expand at once (allocations fixed). | other | 0.3 | Importers plan allocations years ahead. | Below the cut-off: no short-run price rise for new BEVs is reported. |
| A-7 | Buyers know the date, and some can bring the purchase of a new combustion car forward into 2033 to 2034. | expectations | 0.85 | Publicity; replacement cycles of 6 to 10 years. | C-9 loses its (+) chain and becomes a decrease. |
| A-8 | Importers stop offering some combustion models in Vessmark from 2031 rather than certify or market them for a short window, and some buyers of those models buy something other than a new combustion car. | other | 0.6 | Model cycles of 5 to 7 years; fixed certification and launch costs per market. | C-10 is not reported; C-9 loses a (−) chain. |
| A-9 | Dealers pre-register unsold combustion stock before 1 January 2035. | other | 0.8 | Dealers' practice before past rule changes. | C-11 and C-34 are not reported. |
| A-10 | After about 2040, as the combustion fleet falls well below its counterfactual size, stations close and combustion repair becomes scarcer, lowering a combustion car's value in use. | other | 0.6 | Fleet figures (2.9 against 3.4 million in 2040; 1.7 against 2.8 million in 2045); station volumes. | C-22 and C-30 become `increase`. |
| A-11 | For cars in the fleet at enactment, and for used prices in 2035 to 2040, the scarcity chain dominates the thinning chain. | other | 0.7 | Thinning slight before 2040 (fleet gap about 0.5 million); most 2026 cars scrapped by 2043. | C-19 and C-20 become `ambiguous`; C-12 loses its pre-2035 basis. |
| A-12 | Import inspection capacity is not expanded by 2040 enough for imports to close the gap between Vessmark's and Drevland's used combustion prices. | mobility | 0.6 | State test centers; no budget for expansion in the Act. | Under U1-b, C-20 holds only for the first years; later it is an increase or no change. |
| A-13 | Owners expect further restrictions on using combustion cars within their cars' lives. | expectations | 0.3 | No such proposals; the Act protects use (K3). | Below the cut-off. If true, a (−) chain on C-19 to C-22 (CR-12, 0.8, kind 2) and they become `ambiguous`. |
| A-14 | Residents evade the ban by keeping combustion cars registered in Drevland. | enforcement | 0.3 | Six-month rule; roadside checks of foreign plates. | Below the cut-off; if true, `legal_breach` increases. |
| A-15 | Dealers, fuel retailers and motoring clubs, and BEV importers and charging firms, can each organize at a cost below their stake in the review. | other | 0.85 | Existing trade associations. | C-18 is not reported. |
| A-16 | Vehicle-km in combustion cars fall with the combustion fleet; older cars' higher fuel use per km does not offset it. | other | 0.75 | Fuel economy by age; km driven by age. | C-24, C-25, C-27, C-31 and C-32 are not reported. |
| A-17 | Fuel stations' costs are largely fixed per outlet, and their sites have other uses. | other | 0.7 | Station accounts; volumes needed to break even. | C-25, C-27 and C-31 are not reported; C-26 smaller. |
| A-18 | Fuel retailers adjust staff or hours to volume. | alternative_uses | 0.7 | Staffing by volume. | C-27 is not reported. |
| A-19 | Some owners keep combustion cars longer, repairing them, because the car is now worth more than the repair. | other | 0.8 | Scrap decisions turn on repair cost against value. | C-15, C-16, C-29 are not reported. |
| A-20 | Used imports from Drevland are at import parity, and rise when Vessmark's used price rises. | mobility | 0.75 | 25,000 imports a year; the $1,800 gap. | C-12 and C-13 under U1-b are not reported. |
| A-21 | Under U1-b, registering a new combustion car briefly in Drevland and importing it costs less than the premium it earns in Vessmark for some importers. | other | 0.6 | Drevland registration about $500; transport and inspection $1,800. | C-14 under U1-b is not reported. |
| A-22 | The ban chain on new BEV registrations dominates the road-charge chain. | substitutability | 0.85 | The charge ($250 a year) is below a combustion car's fuel excise (about $600); the ban removes the choice of about half of new-car buyers. | C-5 becomes `ambiguous`; C-28 weakens. |
| A-23 | A new BEV costs more to buy in 2035 than the comparable combustion car. | other | 0.7 | Forecast gap of about $2,000. | C-6 is not reported. |
| A-24 | Public charging sales rise with the BEV fleet. | other | 0.8 | Share of charging done publicly. | C-28 is not reported. |
| A-25 | Some would-be buyers of combustion cars buy PHEVs in 2035 to 2037. | substitutability | 0.8 | PHEVs are closest to combustion cars in range and refueling. | C-8 is not reported. |
| A-26 | In 2035 to 2040, the old cars kept in use need more repair a year than the new combustion cars missing from the fleet would have. | other | 0.8 | Repair spending by car age. | C-29 becomes `ambiguous`. |
| A-27 | Some displaced buyers of new combustion cars buy used BEVs. | substitutability | 0.6 | Price of used BEVs against new ones. | C-23 loses its (+) chain and becomes `decrease`. |
| A-28 | The Registry's budget does not rise with the new checks. | revenue_use | 0.8 | K4: budget fixed by law; no appropriation. | C-36 is replaced by a charge on the general budget's payers. |
| A-29 | Dealers clear pre-registered stock in 2035 below the new price, and some buyers who would have bought new in late 2034 wait for it. | other | 0.55 | Discounts on pre-registered cars after past rule changes. | C-9 loses a (−) chain; its sign rests on A-8 against A-7, still `ambiguous`. |

**Final check before the report** (`03_workflow.md`).
1. *Uncombined chains.* Section 7 combines every key reached by opposing chains, including the timing chains of section 8 (C-9), the road charge against the substitute's quantity (C-5) and the imports against the used price (C-20). The rush adds to the stock only before the date and is combined in C-20 as a response.
2. *Group signs.* Station staff are a group (C-27); the Registry's fixed budget gives a mixed group (C-36).
3. *Baseline.* Every sign is against the no-Act path on the forecast trend (A-1), not against 2025. C-13, C-14 and C-37 are signed per reading against that path, not U1-a against U1-b. C-14 under U1-a is `no_change` because no one does this on the counterfactual path.
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for BEV owners, who keep paying the charge (C-3). Displaced buyers and buyers of used cars are worse off by their own ranking; that is not signed as less money.
5. *Timing shifts.* Purchases (C-9 against C-1), PHEVs (C-8 against C-2), scrapping (C-16, C-17), imports (C-12, C-13) and repairs (C-29, C-30) are signed per window. Bunching inside the PHEV window is a path note.
6. *Both sides of transfers.* Road charge (C-3, C-4); revaluation of used cars (C-20, C-21); fuel excise lost and the total (C-32, C-33).
7. *Every class, every core rule.* CR-7c applied to combustion cars, BEVs and fuel stations (C-19, C-23, C-26); CR-6 to new BEVs (quantity only) and used cars (price); CR-9 to fuel, charging and repairs; enforcement from a fixed budget (C-35, C-36).
8. *Unstated premises.* Lobbying (A-15), every margin (A-4, A-7, A-8, A-19, A-25, A-27), the trend (A-1), the review (A-3) and the dominance premises (A-11, A-16, A-22, A-26) are in the table.

## 11. Report

**The policy.** From 1 January 2035 Vessmark will not register new cars with combustion engines; plug-in hybrids may be registered until the end of 2037. Cars registered before then may be driven, sold and re-registered. From 2035 battery-electric cars pay a road charge of $250 a year. The Minister may postpone the dates by up to three years after a review in 2031. Whether a used car imported after 2035 counts as "new" is unclear.

**Visible consequences.** No new combustion cars are sold from 2035 and no new plug-in hybrids from 2038 (C-1, C-2). More new electric cars are sold (C-5). Electric-car owners pay the road charge (C-3), which the budget receives (C-4).

**Invisible consequences.**
- *Buyers.* Those who would have bought a new combustion car lose that option; those who buy an electric car instead pay more for the car (C-6), and fewer new cars are bought in total (C-7), as some keep their old car or buy a used one. Plug-in hybrid sales rise until 2037 (C-8).
- *Before the deadline.* Importers offer fewer combustion models from 2031 (C-10); dealers register unsold stock before the date (C-11, C-34). Whether final buyers buy more or fewer new combustion cars in 2033 to 2034 is ambiguous: some rush, others find their model gone or wait for pre-registered stock (C-9).
- *The existing stock.* Combustion cars held in 2026 gain value from enactment (C-19). From 2035 to 2040 used combustion cars cost more (C-20, C-21), under either reading of the import rule; cars are repaired and kept longer (C-15, C-29) and fewer are scrapped (C-16). Used imports rise before 2035 (C-12).
- *Imports, per reading.* If "registered" means registered in Vessmark (U1-a), used combustion imports stop from 2035 (C-13). If it means registered anywhere (U1-b), they rise, and new cars registered briefly in Drevland are imported as used (C-14); limited inspection capacity keeps the rise partial.
- *Fuel and repair.* Fuel sales (C-24) and the fuel excise (C-32) fall; fewer stations operate in the long run (C-25), their value falls from enactment (C-26), their staff or hours fall (C-27) and drivers travel further to refuel (C-31). Charging sales rise (C-28).
- *Administration.* The Registry's new checks (C-35) come out of its other work (C-36). Lobbying over the 2031 review (C-18).

**Ambiguous effects.** Final buyers' purchases of new combustion cars in 2033 to 2034 (C-9); used combustion prices and repair work after 2040, as scarcity meets a thinning fuel and repair network (C-22, C-30); scrapping after 2040 (C-17); the value of existing electric cars, which displaced buyers want but which carry the new charge (C-23); total road-user tax revenue (C-33).

**Key conditions.** That the date holds at the 2031 review (A-3, p = 0.7); the forecast trend (A-1); that world supply of electric cars expands to Vessmark (A-5); that inspection capacity stays limited, which keeps imports a partial response under U1-b (A-12, p = 0.6); that thinning of the fuel network stays slight before 2040 (A-11, p = 0.7).

**What this analysis cannot say.** How large any effect is; whether displaced buyers spend more or less in total on cars and fuel; whether the price of new electric cars moves; emissions, air quality and safety (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.new_combustion, importers | quantity_traded (new combustion cars, from 2035) | decrease | medium–long | visible | B | CR-1, EN-14, TS-3, OC-4, CR-5a | A-1, A-2, A-3 |
| C-2 | buyers.new_phev, importers | quantity_traded (new PHEVs, from 2038) | decrease | medium–long | visible | B | CR-1, EN-14, TS-3, OC-4 | A-1, A-2, A-3 |
| C-3 | owners.bev | resources_available_other_uses (road charge) | decrease | medium–long | visible | B | CR-1, TX-1, CR-3, CR-8b | A-2 |
| C-4 | taxpayers (general budget) | tax_revenue (road charge) | increase | medium–long | visible | B | TX-1, CR-8b | A-2 |
| C-5 | buyers.new_combustion | quantity_substitute (new BEVs) | increase | medium | visible | B | RS-1, RS-16, CR-6, CR-12b, CR-12e | A-1, A-3, A-5, A-22 |
| C-6 | buyers.new_combustion (who buy a BEV) | price_paid (car bought) | increase | medium | invisible | B | EN-14, CR-4, CR-3a | A-1, A-23 |
| C-7 | buyers.new_cars | quantity_traded (all new cars) | decrease | medium | invisible | B | CR-4a, CR-12e, CR-12 | A-1, A-3, A-4 |
| C-8 | buyers.new_phev | quantity_traded (new PHEVs, 2035–2037) | increase | short–medium | invisible | B | RS-1, RS-8, CR-10a | A-1, A-3, A-25 |
| C-9 | buyers.new_combustion | quantity_traded (final buyers, 2033–2034) | ambiguous | short | invisible | B | RS-8, CR-10a, CR-4, CR-12b | A-7, A-8, A-9, A-29 |
| C-10 | importers | variety (combustion models, 2031–2034) | decrease | short–medium | invisible | B | CR-4, CR-10a | A-3, A-8 |
| C-11 | dealers | inventory_held (pre-registered unsold combustion cars, 1 Jan 2035) | increase | short | invisible | B | RS-8, RS-5, CR-10a, CR-12 | A-3, A-9 |
| C-12 | importers.used | quantity_traded (used combustion imports, 2026–2034) | increase | short–medium | invisible | B | RS-4, CR-7a, CR-7c, CR-10a | A-3, A-11, A-20 |
| C-13 | importers.used | quantity_traded (used combustion imports, from 2035) | U1-a: decrease; U1-b: increase | medium | invisible | B | CR-1, RS-4, CR-7a, CR-12e | A-2, A-3, A-20 |
| C-14 | importers.used | reclassification (new cars registered in Drevland, imported as used) | U1-a: no_change; U1-b: increase | medium | invisible | B | RS-5, CR-4 | A-21 |
| C-15 | owners.combustion | maintenance_spending (older cars kept in use) | increase | medium | invisible | B | EN-14, CR-10b, CR-4 | A-1, A-3, A-19 |
| C-16 | owners.combustion | quantity_traded (cars scrapped, 2035–2040) | decrease | medium | invisible | B | EN-14, CR-10b, CR-4, CR-12g | A-1, A-3, A-19 |
| C-17 | owners.combustion | quantity_traded (cars scrapped, after 2040) | ambiguous | long | invisible | B | CR-10b, CR-12b, CR-12g | A-4, A-19 |
| C-18 | dealers, fuel retailers, motoring clubs; BEV importers, charging firms | lobbying_effort (2031 review) | increase | short–medium | invisible | B | RS-7, CR-4 | A-15 |
| C-19 | owners.combustion.2026 | asset_value (combustion cars held at enactment) | increase | short | invisible | B | EN-14, SB-4, CR-7c, CR-10c, CR-12e | A-1, A-3, A-11 |
| C-20 | buyers.used_combustion | price_paid (used combustion cars, 2035–2040) | increase | medium | invisible | B | EN-14, RS-16, CR-6, CR-12e, CR-12 | A-1, A-2, A-3, A-4, A-11, A-12 |
| C-21 | owners.combustion (sellers) | net_price_received (used combustion cars, 2035–2040) | increase | medium | invisible | B | CR-8b, OC-7 | A-1, A-2, A-3, A-4, A-11, A-12 |
| C-22 | buyers.used_combustion | price_paid (used combustion cars, after 2040) | ambiguous | long | invisible | B | CR-12b, TS-3, CR-7, RS-12 | A-1, A-10 |
| C-23 | owners.bev.existing | asset_value (BEVs held at enactment) | ambiguous | short | invisible | B | RS-16, CR-7c, CR-10c, CR-12b | A-2, A-3, A-27 |
| C-24 | sellers.complements (fuel retailers) | quantity_complement (fuel sold) | decrease | medium–long | invisible | B | RS-12, CR-9, CR-12e | A-1, A-3, A-16 |
| C-25 | sellers.complements (fuel retailers) | number_of_sellers (fuel stations) | decrease | long | invisible | B | RS-12, CR-4 | A-1, A-3, A-16, A-17 |
| C-26 | sellers.complements (fuel retailers) | asset_value (station businesses and sites) | decrease | short | invisible | B | SB-4, CR-7c, CR-10c | A-1, A-3, A-16, A-17 |
| C-27 | fuel_station_workers | employment, hours_worked | at_least_one_decrease | long | invisible | B | RS-6, CR-9 | A-16, A-17, A-18 |
| C-28 | sellers.complements (charging) | quantity_complement (public charging) | increase | medium | invisible | B | RS-12, CR-9 | A-5, A-22, A-24 |
| C-29 | repair_shops | quantity_traded (combustion repairs, 2035–2040) | increase | medium | invisible | B | CR-9, RS-12, CR-12e | A-19, A-26 |
| C-30 | repair_shops | quantity_traded (combustion repairs, after 2040) | ambiguous | long | invisible | B | CR-9, RS-12, CR-12b | A-10, A-19 |
| C-31 | owners.combustion | travel_time (to refuel) | increase | long | invisible | B | RS-12, CR-9 | A-16, A-17 |
| C-32 | taxpayers (general budget) | tax_revenue (fuel excise) | decrease | medium–long | invisible | B | TX-10, CR-9 | A-1, A-3, A-16 |
| C-33 | taxpayers (general budget) | tax_revenue (fuel excise and road charge) | ambiguous | medium | invisible | B | CR-12b, CR-12 | A-2, A-16 |
| C-34 | dealers | compliance_cost (pre-registration) | increase | short | invisible | B | CR-8c, OC-2 | A-9 |
| C-35 | officials.enforcement (Registry) | enforcement_cost | increase | short–long | invisible | B | OC-3, CR-8c | A-2 |
| C-36 | other users of the Registry | wait_time (registration services) (+), other Registry checks (−) | at_least_one_as_stated | short–long | invisible | B | OC-3, CR-8a | A-28 |
| C-37 | importers.used | compliance_cost (import inspections and checks, from 2035) | U1-a: decrease; U1-b: increase | medium | invisible | B | CR-1, CR-8c | A-20, A-21 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from a pattern or a core rule.

**(b) Unclear core rules.**
1. *CR-7, 0.9 (persistence follows the stock).* Written for repeals. Here it was needed twice outside a repeal: for the path of the used-car premium against a counterfactual trend that converges with the policy (C-22), and for the postponement or repeal scenarios the 2031 review makes possible (section 8). In the second use "the stock its value depends on" had to be read as the stock of substitutes, including new supply that can arrive at once. The premium on used combustion cars depends on the absence of new combustion cars, which world supply restores within months of a repeal, not on the missing vintages, which persist. Read literally, the clause would say the premium persists as long as the missing vintages do; that would be wrong here.
2. *CR-12, 0.9 (what the response argument gives).* Under U1-b the partial-response premise came from the case's figures (inspection capacity), as the clause allows. Under U1-a there is no import response at all, and the rise in used prices rests on CR-6's 0.9 split with a fixed stock, not on CR-12e. The clause does not say that where the response is closed off, the split premise does the work instead; it was applied that way.
3. *CR-1, 0.7 (dated operations).* The clause says "an option nobody currently chooses can be removed with no present effect on choices". Here the option removed in 2035 is chosen today by about 70% of buyers, and present choices do change (models withdrawn, rush, imports, lobbying). The clause covers this through CR-10a, but its example points the other way.

**(c) Missing or wrong patterns.**
1. *EN-14, applied as written, gave a conclusion that needed a dominance premise the pattern does not mention.* Its "existing units ... rise in value" omits the opposing chain that the shrinking stock brings on its own complements (RS-12: fuel stations close, repair thins). For cars and other durables that depend on a network, that chain is derived and has p ≥ 0.5 in the long run (A-10). With it, C-19 and C-20 hold only with A-11, and long-run used prices are `ambiguous` (C-22). EN-14 should say: where the exempt stock needs complements whose supply depends on the size of the stock, combine their thinning under CR-12b. Its "kept in use longer" also needs per-window signs for scrapping (C-16, C-17).
2. *RS-16, 0.9 (costs on the substitute), as written, names the wrong variable for this case.* It makes the cost an opposing chain on the substitute's net price to its sellers. With the substitute's supply elastic (A-5), the price chain fails (CR-6, 0.9), and the cost, an annual charge on owning the substitute rather than on its sale, is borne by buyers (CR-7b), so sellers' net price does not move. The charge opposed the substitute's quantity (C-5) instead, and the value of the existing stock of the substitute (C-23). The clause should say: combine the cost with whichever of the substitute's price or quantity the demand shift moves.
3. *TS-3 (product standards).* Worked; the binding share shrinks on the trend. It does not mention that the same convergence ends the premium on the exempt stock (EN-14), which is where the 0.9 persistence idea was needed (b1).
4. *Candidate "scheduled tightening faster than the trend"* (6.2e, from WE-031; CR-10c, CR-7c, CR-12h). Needed: two dated steps (2035 combustion, 2038 PHEVs) against a counterfactual trend toward BEVs (A-1). The derivation applied: the steps bind only on the gap between schedule and trend, the exempt stock is revalued at enactment, and bunching before the second step is a path note (CR-12h). The use is valid against the counterfactual: each window is signed against the no-Act trend (C-8 against C-2). Second use: promotes it.
5. *Candidate "fixed cost per item reduces variety"* (6.2e, WE-035). C-10 uses the same derivation (CR-4, 0.7: x: offer the model, y: drop it), but the policy adds no cost per item; it shortens the window over which an existing fixed cost is recovered. Possibly a second use in a wider form; not counted here, because the earlier invalid second use (WE-040) shows the experts should decide what counts.

**(d) Vocabulary.**
1. No variable for the age or scrapping rate of a durable stock; used `quantity_traded` (cars scrapped) and `maintenance_spending`.
2. No sign for "not signed" (the price of new BEVs), as found in the held-out test of 0.8.
3. `persistence` exists only for repeals; there is no field for how a consequence fades as a counterfactual trend converges with the policy (C-20 to C-22).
4. No way to record a difference between readings that is only one of size (the used-car premium is smaller under U1-b, C-20).

**(e) Test of 0.9.**
- *EN-14 (promoted in 0.9).* Needed interpretation: a yes-or-no ban on a type read as a product standard; its value conclusion for the stock needed a dominance premise against complement thinning (c1), and its "kept longer" needed per-window signs.
- *TS-3, product standards (the 0.8 clause EN-14 cites).* Worked as written: the share bound follows the trend (section 8).
- *RS-8, 0.9 (more timing chains; sellers and buyers moving in opposite directions).* Worked as written: buyers rush, sellers withdraw models and pre-register, buyers wait for pre-registered stock; the window is `ambiguous` (C-9), and pre-registered stock is an activity that exists only under the policy (C-11).
- *CR-7, 0.9 (persistence follows the stock) with CR-10b.* Needed interpretation: it is phrased for repeals, and "the stock" had to be read to include new supply that can return at once; read literally it would overstate persistence of the used-car premium after a repeal (b1).
- *CR-12, 0.9 (what the response argument gives).* Worked as written under U1-b (partial from the case's figures and A-12; C-20) and for total new-car sales (partial with A-4; C-7). Under U1-a the clause was not needed: there is no response, and CR-6's split carries the sign (b2).
- *RS-16, 0.9 (costs on the substitute).* Worked as written for used BEVs (C-23, `ambiguous`). Failed as written for new BEVs: it points at sellers' net price, which does not move when the substitute's supply is elastic and the cost is on ownership; the cost had to be combined with quantity instead (c2).
- *CR-6, 0.9 (splitting a shift).* Worked as written: new BEVs signed on quantity only (A-5), used combustion cars on price (fixed stock), the BEV short-run price not signed because its premise is below the cut-off (A-6).
- *OC-3, 0.9 (fixed budget).* Worked as written: a mixed group for the Registry's other work (C-36).
- *CR-12, 0.8 (kinds of opposing chain).* Worked as written for kind 2 below the cut-off (A-13 on C-19 to C-22) and kind 2 above it (A-10 on C-22).
- *Candidates from 6.2e.* "Scheduled tightening faster than the trend": needed, valid second use (c4). "Fixed cost per item reduces variety": a possible wider second use, not counted (c5).
