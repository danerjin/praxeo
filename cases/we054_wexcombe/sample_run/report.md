# Thin-slice run: Wexcombe Airport Night Curfew and Slot Order

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T05:51:44+00:00
Prediction log sha256 (frozen before the outcome card was opened): `bf932ec930670282…`

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
| `contested_otherwise(k1)` | other | 0.75 | Without the measure, the question it settles would still be contested by the same groups. |
| `binding(k2)` | binding | 0.85 | The cap holds the quantity below what would otherwise be traded. |
| `enforced(k2)` | enforcement | 0.90 | The cap is enforced. |
| `evasion(k2)` | enforcement | 0.15 | Some trade takes place beyond the cap without being caught. |
| `can_organize(k2)` | other | 0.85 | The holders of the rights can organize to lobby at a cost below their stake. |
| `expected_to_last(k2)` | expectations | 0.70 | Holders and buyers of the rights expect the restriction to last. |
| `values_differ(k2)` | other | 0.80 | Holders' costs or values differ. |
| `trade_cheap(k2)` | mobility | 0.75 | Rights can be sold or leased at low cost. |
| `allocation_known(k2)` | expectations | 0.80 | Actors know the allocation rule during the base period. |
| `contested_otherwise(k2)` | other | 0.75 | Without the measure, the question it settles would still be contested by the same groups. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | airlines.history | asset_value | increase | short+ | B | EN-6, SB-4 | {binding(k2), enforced(k2), expected_to_last(k2)} | yes |
| C-2 | airlines.history | asset_value [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |
| C-3 | airlines.history | capital_stock_target | decrease | long | B | EN-6, EN-13 | {binding(k2), enforced(k2), trade_cheap(k2), values_differ(k2)} | yes |
| C-4 | airlines.history | informal_activity | increase | short+ | B | EN-6, RS-3 | {binding(k2), enforced(k2), evasion(k2)} | no |
| C-5 | airlines.history | investment_target [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |
| C-6 | airlines.history | lobbying_effort | increase | medium+ | B | EN-6, RS-7 | {binding(k2), can_organize(k2), enforced(k2)} | yes |
| C-7 | airlines.history | lobbying_effort (policy_field) | ambiguous | medium+ | B | EN-6, RS-7 | {binding(k2), can_organize(k2), contested_otherwise(k2), enforced(k2)} | yes |
| C-8 | airlines.history | net_price_received | increase | short+ | B | EN-6 | {binding(k2), enforced(k2)} | yes |
| C-9 | airlines.history | number_of_sellers | decrease | medium+ | B | EN-6, EN-13 | {binding(k2), enforced(k2), trade_cheap(k2), values_differ(k2)} | yes |
| C-10 | airlines.history | quantity_supplied | increase | medium+ | B | EN-6, EN-13 | {binding(k2), enforced(k2), trade_cheap(k2), values_differ(k2)} | yes |
| C-11 | airlines.history | quantity_traded | decrease | short+ | B | EN-6 | {binding(k2), enforced(k2)} | yes |
| C-12 | airlines.history | quantity_traded [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |
| C-13 | airlines.history | resources_available_other_uses [announcement window] | decrease | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |
| C-14 | airlines.history | right_lease_price | increase | medium+ | B | EN-6, EN-13 | {binding(k2), enforced(k2), trade_cheap(k2), values_differ(k2)} | yes |
| C-15 | airlines.prospective | entry_rate [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |
| C-16 | officials.enforcement | enforcement_cost | increase | short+ | B | EN-6, OC-3 | {binding(k2), enforced(k2)} | yes |
| C-17 | travelers.wxi | disputes_settled_outside_courts | increase | short+ | B | EN-6, RS-3 | {binding(k2), enforced(k2), evasion(k2)} | no |
| C-18 | travelers.wxi | price_paid | increase | short+ | B | EN-6 | {binding(k2), enforced(k2)} | yes |
| C-19 | travelers.wxi | quality_information | decrease | short+ | B | EN-6, RS-3 | {binding(k2), enforced(k2), evasion(k2)} | no |
| C-20 | travelers.wxi | quantity_traded | decrease | short+ | B | EN-6 | {binding(k2), enforced(k2)} | yes |
| C-21 | travelers.wxi | resources_available_other_uses | decrease | short+ | B | EN-6 | {binding(k2), enforced(k2)} | yes |
| C-22 | travelers.wxi | search_cost | increase | short+ | B | EN-6, RS-3 | {binding(k2), enforced(k2), evasion(k2)} | no |
| C-23 | workers.wxi | employment or hours_worked | at_least_one_decrease | medium+ | B | EN-6, EN-13 | {binding(k2), enforced(k2), trade_cheap(k2), values_differ(k2)} | yes |
| C-24 | workers.wxi | employment or hours_worked [announcement window] | at_least_one_increase | short | B | CR-10, EN-12 | {allocation_known(k2)} | yes |

## Explanations

- C-1. Compared with no Wexcombe Airport Night Curfew and Slot Order, asset value for airlines.history rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Holders and buyers of the rights expect the restriction to last (p = 0.70). Reported.
- C-2. Compared with no Wexcombe Airport Night Curfew and Slot Order, asset value for airlines.history rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-3. Compared with no Wexcombe Airport Night Curfew and Slot Order, capital stock target for airlines.history falls in the long run (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Rights can be sold or leased at low cost (p = 0.75); Holders' costs or values differ (p = 0.80). Reported.
- C-4. Compared with no Wexcombe Airport Night Curfew and Slot Order, informal activity for airlines.history rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Some trade takes place beyond the cap without being caught (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-5. Compared with no Wexcombe Airport Night Curfew and Slot Order, investment target for airlines.history rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-6. Compared with no Wexcombe Airport Night Curfew and Slot Order, lobbying effort for airlines.history rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The holders of the rights can organize to lobby at a cost below their stake (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-7. Compared with no Wexcombe Airport Night Curfew and Slot Order, lobbying effort (policy field) for airlines.history may move either way from the medium run onward (tier B, invisible). Why: EN-6: EN-6; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The holders of the rights can organize to lobby at a cost below their stake (p = 0.85); Without the measure, the question it settles would still be contested by the same groups (p = 0.75); The cap is enforced (p = 0.90). Reported.
- C-8. Compared with no Wexcombe Airport Night Curfew and Slot Order, net price received for airlines.history rises from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-9. Compared with no Wexcombe Airport Night Curfew and Slot Order, number of sellers for airlines.history falls from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Rights can be sold or leased at low cost (p = 0.75); Holders' costs or values differ (p = 0.80). Reported.
- C-10. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity supplied for airlines.history rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Rights can be sold or leased at low cost (p = 0.75); Holders' costs or values differ (p = 0.80). Reported.
- C-11. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity traded for airlines.history falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-12. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity traded for airlines.history rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-13. Compared with no Wexcombe Airport Night Curfew and Slot Order, resources available other uses for airlines.history falls in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-14. Compared with no Wexcombe Airport Night Curfew and Slot Order, right lease price for airlines.history rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Rights can be sold or leased at low cost (p = 0.75); Holders' costs or values differ (p = 0.80). Reported.
- C-15. Compared with no Wexcombe Airport Night Curfew and Slot Order, entry rate for airlines.prospective rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-16. Compared with no Wexcombe Airport Night Curfew and Slot Order, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-17. Compared with no Wexcombe Airport Night Curfew and Slot Order, disputes settled outside courts for travelers.wxi rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Some trade takes place beyond the cap without being caught (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-18. Compared with no Wexcombe Airport Night Curfew and Slot Order, price paid for travelers.wxi rises from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-19. Compared with no Wexcombe Airport Night Curfew and Slot Order, quality information for travelers.wxi falls from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Some trade takes place beyond the cap without being caught (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-20. Compared with no Wexcombe Airport Night Curfew and Slot Order, quantity traded for travelers.wxi falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-21. Compared with no Wexcombe Airport Night Curfew and Slot Order, resources available other uses for travelers.wxi falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90). Reported.
- C-22. Compared with no Wexcombe Airport Night Curfew and Slot Order, search cost for travelers.wxi rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Some trade takes place beyond the cap without being caught (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-23. Compared with no Wexcombe Airport Night Curfew and Slot Order, employment or hours worked for workers.wxi falls for at least one of them from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.85); The cap is enforced (p = 0.90); Rights can be sold or leased at low cost (p = 0.75); Holders' costs or values differ (p = 0.80). Reported.
- C-24. Compared with no Wexcombe Airport Night Curfew and Slot Order, employment or hours worked for workers.wxi rises for at least one of them in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
