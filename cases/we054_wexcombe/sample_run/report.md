# Thin-slice run: Wexcombe Airport Night Curfew and Slot Order

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T19:14:09+00:00
Prediction log sha256 (frozen before the outcome card was opened): `0d437e19bdd492d3…`

## Policy record

- Rule-maker: the Wexcombe Airport Authority board; enacted 15 September 2026, effective 31 October 2027.
- Stated aim: none stated
- k1: prohibition on night_movements in wxi; binds operators.night, protects neighbors.wxi. Source: "Curfew (K1), a prohibition of takeoffs and landings from 23:00 to 06:00."
- k2: quota on daytime_movements in wxi; binds airlines.history, protects None. Source: "Movements from 06:00 to 23:00 are capped at 380 a day (the summer 2025 scheduled number), binding all operators at WXI; the existing hourly limit of 34 stays."
- k3: rights_allocation on daytime_slots in wxi; binds officials.enforcement, protects airlines.history. Source: "Allocation by history (K3), a rights allocation."
- k5: rights_allocation on freed_slots in wxi; binds officials.enforcement, protects operators.night. Source: "Slots of a holder that ceases to operate at WXI, or that uses a slot on fewer than 80% of a season's days, return to the WAA and are reissued free, first to night operators (those with night movements in winter 2026/27) in proportion to their night movements, then to new entrants."
- Unclear U1: Late-running flights: whether a flight scheduled before 23:00 and delayed may operate until 00:00 as of right, or has no dispensation for ordinary delays. Readings: U1-a: a flight scheduled before 23:00 and delayed may land or take off until 00:00, as of right / U1-b: there is no dispensation for ordinary delays; after 23:00 only emergencies operate, and a late flight diverts (in practice to Pellham) or is cancelled
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `enforced(k1)` | enforcement | 0.90 | The legal sellers comply with the ban. |
| `demand_persists(k1)` | other | 0.70 | A meaningful share of buyers keep wanting the good after the ban. |
| `evasion(k1)` | enforcement | 0.10 | Enforcement is imperfect: many informal sales go undetected. |
| `enforcement_risk(k1)` | enforcement | 0.90 | Informal sellers face a real risk of punishment. |
| `no_other_use(k1)` | alternative_uses | 0.70 | The legal sellers cannot replace the banned good with other products for most of their business. |
| `buyer_substitutes(k1)` | substitutability | 0.70 | Legal substitutes are acceptable to some buyers. |
| `can_organize(k1)` | other | 0.85 | The former legal sellers can organize to seek repeal. |
| `buyers_organize(k1)` | other | 0.20 | The buyers have a concentrated stake and can organize for repeal. |
| `stockpile_ahead(k1)` | expectations | 0.05 | Buyers and importers can store the good and order ahead of the effective date. |
| `contested_otherwise(k1)` | other | 0.75 | The groups that gain from or are bound by the measure would have lobbied on the same question without it. |
| `binding(k2)` | binding | 0.85 | The cap holds the quantity below what would otherwise be traded. |
| `enforced(k2)` | enforcement | 0.90 | The cap is enforced. |
| `evasion(k2)` | enforcement | 0.15 | Some trade takes place beyond the cap without being caught. |
| `can_organize(k2)` | other | 0.85 | The holders of the rights can organize to lobby at a cost below their stake. |
| `expected_to_last(k2)` | expectations | 0.70 | Holders and buyers of the rights expect the restriction to last. |
| `values_differ(k2)` | other | 0.80 | Holders' costs or values differ. |
| `trade_cheap(k2)` | mobility | 0.75 | Rights can be sold or leased at low cost. |
| `allocation_known(k2)` | expectations | 0.80 | Actors know the allocation rule during the base period. |
| `contested_otherwise(k2)` | other | 0.40 | The groups that gain from or are bound by the measure would have lobbied on the same question without it. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | airlines.history | asset_value | increase | short+ | B | EN-6, SB-4 | {binding(k2), enforced(k2), expected_to_last(k2)} | yes |
| C-2 | airlines.history | asset_value [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |
| C-3 | airlines.history | capital_stock_target | decrease | long | B | EN-6, EN-13 | {binding(k2), enforced(k2), trade_cheap(k2), values_differ(k2)} | yes |
| C-4 | airlines.history | informal_activity | increase | short+ | B | EN-6, RS-3 | {binding(k2), enforced(k2), evasion(k2)} | no |
| C-5 | airlines.history | investment_target [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |
| C-6 | airlines.history | lobbying_effort | increase | medium+ | B | EN-6, RS-7 | {binding(k2), can_organize(k2), enforced(k2)} | yes |
| C-7 | airlines.history | lobbying_effort (policy_field) | ambiguous | medium+ | B | EN-6, RS-7 | {binding(k2), can_organize(k2), contested_otherwise(k2), enforced(k2)} | no |
| C-8 | airlines.history | net_price_received | increase | short+ | B | EN-6 | {binding(k2), enforced(k2)} | yes |
| C-9 | airlines.history | number_of_sellers | decrease | medium+ | B | EN-6, EN-13 | {binding(k2), enforced(k2), trade_cheap(k2), values_differ(k2)} | yes |
| C-10 | airlines.history | quantity_traded | decrease | short+ | B | EN-6 | {binding(k2), enforced(k2)} | yes |
| C-11 | airlines.history | quantity_traded [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |
| C-12 | airlines.history | resources_available_other_uses [announcement window] | decrease | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |
| C-13 | airlines.history | right_lease_price | increase | medium+ | B | EN-6, EN-13 | {binding(k2), enforced(k2), trade_cheap(k2), values_differ(k2)} | yes |
| C-14 | airlines.prospective | entry_rate [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |
| C-15 | buyers.current | disputes_settled_outside_courts | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-16 | buyers.current | lobbying_effort | increase | medium+ | B | RS-7 | {buyers_organize(k1)} | no |
| C-17 | buyers.current | price_paid | increase | short+ | B | EN-7, RS-3, CR-7 | {demand_persists(k1), enforced(k1), enforcement_risk(k1), evasion(k1)} | no |
| C-18 | buyers.current | quality_information | decrease | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-19 | buyers.current | quality_variability | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-20 | buyers.current | quantity_demanded | decrease | short+ | B | EN-7, RS-3, CR-7 | {demand_persists(k1), enforced(k1), enforcement_risk(k1), evasion(k1)} | no |
| C-21 | buyers.current | quantity_demanded [announcement window] | increase | short | B | RS-8 | {stockpile_ahead(k1)} | no |
| C-22 | buyers.current | quantity_substitute | increase | short+ | B | RS-1 | {buyer_substitutes(k1)} | yes |
| C-23 | buyers.current | quantity_traded | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-24 | buyers.current | search_cost | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-25 | officials.enforcement | enforcement_cost | increase | short+ | B | OC-3, EN-6 | {} | yes |
| C-26 | operators.night | asset_value | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | yes |
| C-27 | operators.night | employment | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | yes |
| C-28 | operators.night | lobbying_effort | increase | medium+ | B | RS-7 | {can_organize(k1)} | yes |
| C-29 | operators.night | lobbying_effort (policy_field) | ambiguous | medium+ | B | RS-7 | {can_organize(k1), contested_otherwise(k1)} | yes |
| C-30 | operators.night | number_of_sellers | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | yes |
| C-31 | operators.night | quantity_traded | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-32 | travelers.wxi | disputes_settled_outside_courts | increase | short+ | B | EN-6, RS-3 | {binding(k2), enforced(k2), evasion(k2)} | no |
| C-33 | travelers.wxi | price_paid | increase | short+ | B | EN-6 | {binding(k2), enforced(k2)} | yes |
| C-34 | travelers.wxi | quality_information | decrease | short+ | B | EN-6, RS-3 | {binding(k2), enforced(k2), evasion(k2)} | no |
| C-35 | travelers.wxi | quantity_traded | decrease | short+ | B | EN-6 | {binding(k2), enforced(k2)} | yes |
| C-36 | travelers.wxi | resources_available_other_uses | decrease | short+ | B | EN-6 | {binding(k2), enforced(k2)} | yes |
| C-37 | travelers.wxi | search_cost | increase | short+ | B | EN-6, RS-3 | {binding(k2), enforced(k2), evasion(k2)} | no |
| C-38 | workers.wxi | employment or hours_worked | at_least_one_decrease | medium+ | B | EN-6, EN-13 | {binding(k2), enforced(k2), trade_cheap(k2), values_differ(k2)} | yes |
| C-39 | workers.wxi | employment or hours_worked [announcement window] | at_least_one_increase | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |

## Explanations

- C-1. Compared with no Wexcombe Airport Night Curfew and Slot Order, asset value for airlines.history rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Holders and buyers of the rights expect the restriction to last (p = 0.70). Reported.
- C-2. Compared with no Wexcombe Airport Night Curfew and Slot Order, asset value for airlines.history rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-3. Compared with no Wexcombe Airport Night Curfew and Slot Order, capital stock target for airlines.history falls in the long run (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Rights can be sold or leased at low cost (p = 0.75); Holders' costs or values differ (p = 0.80). Reported.
- C-4. Compared with no Wexcombe Airport Night Curfew and Slot Order, informal activity for airlines.history rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Some trade takes place beyond the cap without being caught (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-5. Compared with no Wexcombe Airport Night Curfew and Slot Order, investment target for airlines.history rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-6. Compared with no Wexcombe Airport Night Curfew and Slot Order, lobbying effort for airlines.history rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The holders of the rights can organize to lobby at a cost below their stake (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-7. Compared with no Wexcombe Airport Night Curfew and Slot Order, lobbying effort (policy field) for airlines.history may move either way from the medium run onward (tier B, invisible). Why: EN-6: EN-6; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The holders of the rights can organize to lobby at a cost below their stake (p = 0.85); The groups that gain from or are bound by the measure would have lobbied on the same question without it (p = 0.40); The cap is enforced (p = 0.90). Not reported: an assumption is below the 0.5 cut-off.
- C-8. Compared with no Wexcombe Airport Night Curfew and Slot Order, net price received for airlines.history rises from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-9. Compared with no Wexcombe Airport Night Curfew and Slot Order, number of sellers for airlines.history falls from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Rights can be sold or leased at low cost (p = 0.75); Holders' costs or values differ (p = 0.80). Reported.
- C-10. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity traded for airlines.history falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-11. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity traded for airlines.history rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-12. Compared with no Wexcombe Airport Night Curfew and Slot Order, resources available other uses for airlines.history falls in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-13. Compared with no Wexcombe Airport Night Curfew and Slot Order, right lease price for airlines.history rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Rights can be sold or leased at low cost (p = 0.75); Holders' costs or values differ (p = 0.80). Reported.
- C-14. Compared with no Wexcombe Airport Night Curfew and Slot Order, entry rate for airlines.prospective rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-15. Compared with no Wexcombe Airport Night Curfew and Slot Order, disputes settled outside courts for buyers.current rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); The legal sellers comply with the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.10). Not reported: an assumption is below the 0.5 cut-off.
- C-16. Compared with no Wexcombe Airport Night Curfew and Slot Order, lobbying effort for buyers.current rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The buyers have a concentrated stake and can organize for repeal (p = 0.20). Not reported: an assumption is below the 0.5 cut-off.
- C-17. Compared with no Wexcombe Airport Night Curfew and Slot Order, price paid for buyers.current rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3; CR-7: CR-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); The legal sellers comply with the ban (p = 0.90); Informal sellers face a real risk of punishment (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.10). Not reported: an assumption is below the 0.5 cut-off.
- C-18. Compared with no Wexcombe Airport Night Curfew and Slot Order, quality information for buyers.current falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); The legal sellers comply with the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.10). Not reported: an assumption is below the 0.5 cut-off.
- C-19. Compared with no Wexcombe Airport Night Curfew and Slot Order, quality variability for buyers.current rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); The legal sellers comply with the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.10). Not reported: an assumption is below the 0.5 cut-off.
- C-20. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity demanded for buyers.current falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3; CR-7: CR-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); The legal sellers comply with the ban (p = 0.90); Informal sellers face a real risk of punishment (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.10). Not reported: an assumption is below the 0.5 cut-off.
- C-21. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity demanded for buyers.current rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: RS-8: a measure announced before it takes effect treats the same action differently by date, so actors move it toward the favourable window. This holds if: Buyers and importers can store the good and order ahead of the effective date (p = 0.05). Not reported: an assumption is below the 0.5 cut-off.
- C-22. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity substitute for buyers.current rises from the short run onward (tier B, invisible). Why: RS-1: when a good becomes dearer, buyers turn to substitutes. This holds if: Legal substitutes are acceptable to some buyers (p = 0.70). Reported.
- C-23. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity traded for buyers.current falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.90). Reported.
- C-24. Compared with no Wexcombe Airport Night Curfew and Slot Order, search cost for buyers.current rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); The legal sellers comply with the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.10). Not reported: an assumption is below the 0.5 cut-off.
- C-25. Compared with no Wexcombe Airport Night Curfew and Slot Order, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers; EN-6: EN-6. This holds if: no assumption. Reported.
- C-26. Compared with no Wexcombe Airport Night Curfew and Slot Order, asset value for operators.night falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.90); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.70). Reported.
- C-27. Compared with no Wexcombe Airport Night Curfew and Slot Order, employment for operators.night falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.90); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.70). Reported.
- C-28. Compared with no Wexcombe Airport Night Curfew and Slot Order, lobbying effort for operators.night rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The former legal sellers can organize to seek repeal (p = 0.85). Reported.
- C-29. Compared with no Wexcombe Airport Night Curfew and Slot Order, lobbying effort (policy field) for operators.night may move either way from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The former legal sellers can organize to seek repeal (p = 0.85); The groups that gain from or are bound by the measure would have lobbied on the same question without it (p = 0.75). Reported.
- C-30. Compared with no Wexcombe Airport Night Curfew and Slot Order, number of sellers for operators.night falls from the short run onward (tier B, visible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.90); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.70). Reported.
- C-31. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity traded for operators.night falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.90). Reported.
- C-32. Compared with no Wexcombe Airport Night Curfew and Slot Order, disputes settled outside courts for travelers.wxi rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Some trade takes place beyond the cap without being caught (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-33. Compared with no Wexcombe Airport Night Curfew and Slot Order, price paid for travelers.wxi rises from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-34. Compared with no Wexcombe Airport Night Curfew and Slot Order, quality information for travelers.wxi falls from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Some trade takes place beyond the cap without being caught (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-35. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity traded for travelers.wxi falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-36. Compared with no Wexcombe Airport Night Curfew and Slot Order, resources available other uses for travelers.wxi falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-37. Compared with no Wexcombe Airport Night Curfew and Slot Order, search cost for travelers.wxi rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Some trade takes place beyond the cap without being caught (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-38. Compared with no Wexcombe Airport Night Curfew and Slot Order, employment or hours worked for workers.wxi falls for at least one of them from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Rights can be sold or leased at low cost (p = 0.75); Holders' costs or values differ (p = 0.80). Reported.
- C-39. Compared with no Wexcombe Airport Night Curfew and Slot Order, employment or hours worked for workers.wxi rises for at least one of them in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
