# Thin-slice run: Brennick Carryout Bag Ordinance

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-21T17:02:56+00:00
Prediction log sha256 (frozen before the outcome card was opened): `e78034e69313beb6…`

## Policy record

- Rule-maker: the Brennick city council; enacted nine months before the effective date, effective the effective date.
- Stated aim: none stated
- k1: prohibition on single_use_plastic_carryout_bags in brennick; binds retailers.brennick, protects None. Source: "From the effective date, all retailers in Brennick are prohibited from providing single-use plastic carryout bags (plastic bags with handles, thinner than 4 mil (0.1 mm)) at the point of sale."
- k2: price_floor on paper_carryout_bags in brennick; binds shoppers, protects shoppers.assistance. Source: "Recycled-paper carryout bags may be provided only for a charge of at least 10 cents a bag, kept by the retailer and shown on the receipt."
- Unclear U1: how a bag's design for 125 uses is verified Readings: U1-a: a maker's claim is accepted, since the ordinance sets no test
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `enforced(k1)` | enforcement | 0.85 | The legal sellers comply with the ban. |
| `demand_persists(k1)` | other | 0.20 | A meaningful share of buyers keep wanting the good after the ban. |
| `evasion(k1)` | enforcement | 0.60 | Enforcement is imperfect: many informal sales go undetected. |
| `enforcement_risk(k1)` | enforcement | 0.50 | Informal sellers face a real risk of punishment. |
| `no_other_use(k1)` | alternative_uses | 0.10 | The legal sellers cannot replace the banned good with other products for most of their business. |
| `buyer_substitutes(k1)` | substitutability | 0.95 | Legal substitutes are acceptable to some buyers. |
| `can_organize(k1)` | other | 0.70 | The former legal sellers can organize to seek repeal. |
| `buyers_organize(k1)` | other | 0.10 | The buyers have a concentrated stake and can organize for repeal. |
| `cross_border_feasible(k1)` | mobility | 0.55 | Enough buyers can easily buy across the boundary, where the tax does not apply. |
| `crossing_extra_trip(k1)` | mobility | 0.20 | Buying across the boundary takes trips the buyers would not otherwise make. |
| `reshaping_pays(k1)` | other | 0.60 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |
| `stockpile_ahead(k1)` | expectations | 0.70 | Buyers and importers can store the good and order ahead of the effective date. |
| `binding(k2)` | binding | 0.95 | The floor binds for an identifiable group of sellers. |
| `enforced(k2)` | enforcement | 0.85 | Most bound buyers comply with the floor. |
| `cost_not_offset(k2)` | substitutability | 0.85 | The floor raises buyers' cost per unit; it is not fully offset. |
| `evasion(k2)` | enforcement | 0.60 | Some trade below the floor goes undetected. |
| `can_organize(k2)` | other | 0.10 | The bound buyers can organize to lobby. |
| `sellers_organize(k2)` | other | 0.70 | The sellers the floor raises can organize to lobby. |
| `cross_border_feasible(k2)` | mobility | 0.55 | Some buyers of the output can easily buy across the boundary. |
| `substitute_exists(k2)` | alternative_uses | 0.95 | A substitute exists for what the floor makes dearer. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |
| C-2 | retailers.brennick | asset_value | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | no |
| C-3 | retailers.brennick | employment | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | no |
| C-4 | retailers.brennick | excess_supply | increase | short+ | B | PC-9, CR-6, PC-11 | {binding(k2), cost_not_offset(k2), enforced(k2)} | yes |
| C-5 | retailers.brennick | lobbying_effort | increase | medium+ | B | RS-7 | {can_organize(k1)} or {binding(k2), sellers_organize(k2)} | yes |
| C-6 | retailers.brennick | net_price_received | increase | short+ | B | PC-9 | {binding(k2), enforced(k2)} | yes |
| C-7 | retailers.brennick | number_of_sellers | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | no |
| C-8 | retailers.brennick | quantity_traded | decrease | short+ | B | EN-7, PC-9, CR-6 | {enforced(k1)} or {binding(k2), cost_not_offset(k2), enforced(k2)} | yes |
| C-9 | retailers.fallow_creek | quantity_traded | increase | short+ | B | RS-4 | {cross_border_feasible(k1)} | yes |
| C-10 | retailers.small | disputes_settled_outside_courts | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-11 | retailers.small | informal_activity | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-12 | retailers.small | reclassification | increase | short+ | B | RS-5 | {reshaping_pays(k1)} | yes |
| C-13 | sellers.substitutes | quantity_traded | increase | medium+ | B | PC-9, CR-6, RS-1 | {binding(k2), cost_not_offset(k2), enforced(k2), substitute_exists(k2)} | yes |
| C-14 | sellers.substitutes | reclassification | increase | short+ | B | RS-5 | {reshaping_pays(k1)} | yes |
| C-15 | shoppers | compliance_cost | increase | short+ | A | OC-2 | {} | yes |
| C-16 | shoppers | disputes_settled_outside_courts | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-17 | shoppers | informal_activity | increase | short+ | B | RS-3 | {binding(k2), evasion(k2)} | yes |
| C-18 | shoppers | lobbying_effort | increase | medium+ | B | RS-7 | {buyers_organize(k1)} or {binding(k2), can_organize(k2)} | no |
| C-19 | shoppers | price_paid | increase | short+ | B | EN-7, RS-3, CR-7, PC-9 | {binding(k2), enforced(k2)} or {demand_persists(k1), enforced(k1), enforcement_risk(k1), evasion(k1)} | yes |
| C-20 | shoppers | quality_information | decrease | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-21 | shoppers | quality_variability | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-22 | shoppers | quantity_demanded | decrease | short+ | B | EN-7, RS-3, CR-7 | {demand_persists(k1), enforced(k1), enforcement_risk(k1), evasion(k1)} | no |
| C-23 | shoppers | quantity_demanded [announcement window] | increase | short | B | RS-8 | {stockpile_ahead(k1)} | yes |
| C-24 | shoppers | quantity_substitute | increase | short+ | B | RS-1, PC-9, CR-6 | {buyer_substitutes(k1)} or {binding(k2), cost_not_offset(k2), enforced(k2), substitute_exists(k2)} | yes |
| C-25 | shoppers | quantity_traded | decrease | short+ | B | EN-7, PC-9, CR-6 | {enforced(k1)} or {binding(k2), cost_not_offset(k2), enforced(k2)} | yes |
| C-26 | shoppers | search_cost | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-27 | shoppers.edge | cross_border_purchases | increase | short+ | B | RS-4, PC-9, CR-6 | {cross_border_feasible(k1)} or {binding(k2), cost_not_offset(k2), cross_border_feasible(k2), enforced(k2)} | yes |
| C-28 | shoppers.edge | search_cost | increase | short+ | B | OC-2 | {cross_border_feasible(k1), crossing_extra_trip(k1)} | no |
| C-29 | taxpayers or recipients.other_spending or taxpayers.future | resources_available_other_uses | at_least_one_decrease | short+ | A | OC-1 | {} | yes |

## Explanations

- C-1. Compared with no Brennick Carryout Bag Ordinance, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-2. Compared with no Brennick Carryout Bag Ordinance, asset value for retailers.brennick falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.85); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.10). Not reported: an assumption is below the 0.5 cut-off.
- C-3. Compared with no Brennick Carryout Bag Ordinance, employment for retailers.brennick falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.85); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.10). Not reported: an assumption is below the 0.5 cut-off.
- C-4. Compared with no Brennick Carryout Bag Ordinance, excess supply for retailers.brennick rises from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; PC-11: PC-11. This holds if: The floor binds for an identifiable group of sellers (p = 0.95); The floor raises buyers' cost per unit; it is not fully offset (p = 0.85); Most bound buyers comply with the floor (p = 0.85). Reported.
- C-5. Compared with no Brennick Carryout Bag Ordinance, lobbying effort for retailers.brennick rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The former legal sellers can organize to seek repeal (p = 0.70). It also follows under 1 other minimal assumption set(s). Reported.
- C-6. Compared with no Brennick Carryout Bag Ordinance, net price received for retailers.brennick rises from the short run onward (tier B, visible). Why: PC-9: PC-9. This holds if: The floor binds for an identifiable group of sellers (p = 0.95); Most bound buyers comply with the floor (p = 0.85). Reported.
- C-7. Compared with no Brennick Carryout Bag Ordinance, number of sellers for retailers.brennick falls from the short run onward (tier B, visible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.85); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.10). Not reported: an assumption is below the 0.5 cut-off.
- C-8. Compared with no Brennick Carryout Bag Ordinance, quantity traded for retailers.brennick falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price. This holds if: The legal sellers comply with the ban (p = 0.85). It also follows under 1 other minimal assumption set(s). Reported.
- C-9. Compared with no Brennick Carryout Bag Ordinance, quantity traded for retailers.fallow_creek rises from the short run onward (tier B, invisible). Why: RS-4: shut-out buyers turn to uncovered units, which are close substitutes. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.55). Reported.
- C-10. Compared with no Brennick Carryout Bag Ordinance, disputes settled outside courts for retailers.small rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.20); The legal sellers comply with the ban (p = 0.85); Enforcement is imperfect: many informal sales go undetected (p = 0.60). Not reported: an assumption is below the 0.5 cut-off.
- C-11. Compared with no Brennick Carryout Bag Ordinance, informal activity for retailers.small rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.20); The legal sellers comply with the ban (p = 0.85); Enforcement is imperfect: many informal sales go undetected (p = 0.60). Not reported: an assumption is below the 0.5 cut-off.
- C-12. Compared with no Brennick Carryout Bag Ordinance, reclassification for retailers.small rises from the short run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.60). Reported.
- C-13. Compared with no Brennick Carryout Bag Ordinance, quantity traded for sellers.substitutes rises from the medium run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; RS-1: when a good becomes dearer, buyers turn to substitutes. This holds if: The floor binds for an identifiable group of sellers (p = 0.95); The floor raises buyers' cost per unit; it is not fully offset (p = 0.85); Most bound buyers comply with the floor (p = 0.85); A substitute exists for what the floor makes dearer (p = 0.95). Reported.
- C-14. Compared with no Brennick Carryout Bag Ordinance, reclassification for sellers.substitutes rises from the short run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.60). Reported.
- C-15. Compared with no Brennick Carryout Bag Ordinance, compliance cost for shoppers rises from the short run onward (tier A, invisible). Why: OC-2: OC-2. This holds if: no assumption. Reported.
- C-16. Compared with no Brennick Carryout Bag Ordinance, disputes settled outside courts for shoppers rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.20); The legal sellers comply with the ban (p = 0.85); Enforcement is imperfect: many informal sales go undetected (p = 0.60). Not reported: an assumption is below the 0.5 cut-off.
- C-17. Compared with no Brennick Carryout Bag Ordinance, informal activity for shoppers rises from the short run onward (tier B, invisible). Why: RS-3: RS-3. This holds if: The floor binds for an identifiable group of sellers (p = 0.95); Some trade below the floor goes undetected (p = 0.60). Reported.
- C-18. Compared with no Brennick Carryout Bag Ordinance, lobbying effort for shoppers rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The buyers have a concentrated stake and can organize for repeal (p = 0.10). It also follows under 1 other minimal assumption set(s). Not reported: an assumption is below the 0.5 cut-off.
- C-19. Compared with no Brennick Carryout Bag Ordinance, price paid for shoppers rises from the short run onward (tier B, visible). Why: EN-7: EN-7; RS-3: RS-3; CR-7: CR-7; PC-9: PC-9. This holds if: The floor binds for an identifiable group of sellers (p = 0.95); Most bound buyers comply with the floor (p = 0.85). It also follows under 1 other minimal assumption set(s). Reported.
- C-20. Compared with no Brennick Carryout Bag Ordinance, quality information for shoppers falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.20); The legal sellers comply with the ban (p = 0.85); Enforcement is imperfect: many informal sales go undetected (p = 0.60). Not reported: an assumption is below the 0.5 cut-off.
- C-21. Compared with no Brennick Carryout Bag Ordinance, quality variability for shoppers rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.20); The legal sellers comply with the ban (p = 0.85); Enforcement is imperfect: many informal sales go undetected (p = 0.60). Not reported: an assumption is below the 0.5 cut-off.
- C-22. Compared with no Brennick Carryout Bag Ordinance, quantity demanded for shoppers falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3; CR-7: CR-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.20); The legal sellers comply with the ban (p = 0.85); Informal sellers face a real risk of punishment (p = 0.50); Enforcement is imperfect: many informal sales go undetected (p = 0.60). Not reported: an assumption is below the 0.5 cut-off.
- C-23. Compared with no Brennick Carryout Bag Ordinance, quantity demanded for shoppers rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: RS-8: a measure announced before it takes effect treats the same action differently by date, so actors move it toward the favourable window. This holds if: Buyers and importers can store the good and order ahead of the effective date (p = 0.70). Reported.
- C-24. Compared with no Brennick Carryout Bag Ordinance, quantity substitute for shoppers rises from the short run onward (tier B, invisible). Why: RS-1: when a good becomes dearer, buyers turn to substitutes; PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price. This holds if: Legal substitutes are acceptable to some buyers (p = 0.95). It also follows under 1 other minimal assumption set(s). Reported.
- C-25. Compared with no Brennick Carryout Bag Ordinance, quantity traded for shoppers falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price. This holds if: The legal sellers comply with the ban (p = 0.85). It also follows under 1 other minimal assumption set(s). Reported.
- C-26. Compared with no Brennick Carryout Bag Ordinance, search cost for shoppers rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.20); The legal sellers comply with the ban (p = 0.85); Enforcement is imperfect: many informal sales go undetected (p = 0.60). Not reported: an assumption is below the 0.5 cut-off.
- C-27. Compared with no Brennick Carryout Bag Ordinance, cross border purchases for shoppers.edge rises from the short run onward (tier B, invisible). Why: RS-4: shut-out buyers turn to uncovered units, which are close substitutes; PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.55). It also follows under 1 other minimal assumption set(s). Reported.
- C-28. Compared with no Brennick Carryout Bag Ordinance, search cost for shoppers.edge rises from the short run onward (tier B, invisible). Why: OC-2: OC-2. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.55); Buying across the boundary takes trips the buyers would not otherwise make (p = 0.20). Not reported: an assumption is below the 0.5 cut-off.
- C-29. Compared with no Brennick Carryout Bag Ordinance, resources available other uses for taxpayers or recipients.other_spending or taxpayers.future falls for at least one of them from the short run onward (tier A, invisible). Why: OC-1: what the payers give up is what they would otherwise have bought. This holds if: no assumption. Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
