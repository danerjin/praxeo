# Thin-slice run: Lanvik App-Based Work Act 2027

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-21T17:02:57+00:00
Prediction log sha256 (frozen before the outcome card was opened): `352189f405032b83…`

## Policy record

- Rule-maker: the Lanvik legislature; enacted 15 March 2027, effective 1 October 2027.
- Stated aim: none stated
- k1: mandated_contract_term on app_based_work in lanvik_app_work; binds platforms, protects None. Source: "An app-based worker is an employee of the network company unless the company proves that (a) the worker is free from its control and direction in performing the work, (b) the work is outside the usual course of its business, and (c) the worker is customarily engaged in an independently established trade."
- k2: price_floor on engaged_time in lanvik_app_work; binds platforms, protects drivers.employee. Source: "An employee shall be paid at least the state minimum wage for all engaged time."
- k5: mandate_with_charge on app_based_work in lanvik_app_work; binds platforms, protects drivers.contractor. Source: "A network company may elect to offer its app-based workers in Lanvik a contractor agreement; an election applies to all its Lanvik workers."
- Unclear U1: Is time logged in and waiting time "during which the worker is required by the network company to remain available"? Readings: U1-a: no. A worker may log off at will, so only time on a trip, and any shift a company schedules, is engaged time / U1-b: yes. The apps reduce the priority of workers who decline requests, so all logged-in time is engaged time
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.95 | The term was absent from some contracts, so the mandate binds for them. |
| `enforced(k1)` | enforcement | 0.80 | Most bound providers comply. |
| `wages_sticky(k1)` | other | 0.60 | The other money terms are fixed in the short run. |
| `wages_adjust(k1)` | other | 0.75 | The wage can adjust over the medium run. |
| `worth_less(k1)` | other | 0.55 | The term is worth less to the marginal recipient than it costs the provider. |
| `alternatives_worse(k1)` | mobility | 0.30 | The recipients' alternatives are worse than the providers'. |
| `valued_on_earnings(k1)` | expectations | 0.70 | The providers' businesses are valued on expected earnings. |
| `can_organize(k1)` | other | 0.90 | The bound providers can organize to lobby. |
| `recipients_organize(k1)` | other | 0.90 | The recipients can organize to lobby. |
| `floor_binds(k1)` | binding | 0.90 | A floor holds some recipients' wage. |
| `can_screen(k1)` | other | 0.70 | Providers can tell which applicants will cost more under the term. |
| `rivals_bound(k1)` | other | 0.80 | Most of the providers' rivals are bound too. |
| `compete_with_bound(k1)` | substitutability | 0.75 | The unbound firms compete with the bound providers. |
| `reshaping_pays(k1)` | other | 0.50 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |
| `staying_small_pays(k1)` | other | 0.50 | Some firms near the threshold value staying below it more than an extra hire. |
| `binding(k2)` | binding | 0.90 | The floor binds for an identifiable group of sellers. |
| `enforced(k2)` | enforcement | 0.80 | Most bound buyers comply with the floor. |
| `cost_not_offset(k2)` | substitutability | 0.80 | The floor raises buyers' cost per unit; it is not fully offset. |
| `evasion(k2)` | enforcement | 0.65 | Some trade below the floor goes undetected. |
| `can_organize(k2)` | other | 0.90 | The bound buyers can organize to lobby. |
| `sellers_organize(k2)` | other | 0.90 | The sellers the floor raises can organize to lobby. |
| `margins(k2)` | other | 0.90 | Buyers can adjust at least one margin. |
| `rivals_bound(k2)` | other | 0.80 | Most of the bound buyers' rivals face the same floor. |
| `expected_to_last(k2)` | expectations | 0.70 | Investors expect the measure to stay in force for at least its stated term. |
| `binding(k5)` | binding | 0.75 | The term was absent from some contracts, so the mandate binds for them. |
| `enforced(k5)` | enforcement | 0.90 | Most bound providers comply. |
| `can_organize(k5)` | other | 0.90 | The bound providers can organize to lobby. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | drivers.contractor | reclassification | increase | medium+ | B | RS-5 | {binding(k1), enforced(k1), reshaping_pays(k1)} | yes |
| C-2 | drivers.employee | allocation_by_non_price_criteria | increase | medium+ | B | PC-17, RS-23 | {binding(k1), can_screen(k1), enforced(k1)} | yes |
| C-3 | drivers.employee | allocation_by_non_price_criteria or search_cost or wait_time | at_least_one_increase | short+ | B | PC-9, CR-6, PC-11 | {binding(k2), cost_not_offset(k2), enforced(k2)} | yes |
| C-4 | drivers.employee | employment or hours_worked or non_wage_compensation | at_least_one_decrease | short+ | B | PC-17, PC-10, CR-2, CR-6, PC-9 | {binding(k2), cost_not_offset(k2), enforced(k2), margins(k2)} or {binding(k1), enforced(k1), floor_binds(k1)} or {binding(k1), enforced(k1), wages_sticky(k1)} or {binding(k1), enforced(k1), worth_less(k1)} | yes |
| C-5 | drivers.employee | excess_supply | increase | short+ | B | PC-9, CR-6, PC-11 | {binding(k2), cost_not_offset(k2), enforced(k2)} | yes |
| C-6 | drivers.employee | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k1), recipients_organize(k1)} or {binding(k2), sellers_organize(k2)} | yes |
| C-7 | drivers.employee | non_wage_compensation | increase | short+ | B | PC-17 | {binding(k1), enforced(k1)} | yes |
| C-8 | drivers.employee | wage_rate | increase | short+ | B | PC-9 | {binding(k2), enforced(k2)} | yes |
| C-9 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |
| C-10 | owners.platforms | asset_value | decrease | short+ | B | PC-9, CR-6, SB-4 | {binding(k2), cost_not_offset(k2), enforced(k2), expected_to_last(k2)} | yes |
| C-11 | platforms | asset_value | decrease | short+ | B | PC-17, CR-7 | {binding(k1), enforced(k1), valued_on_earnings(k1), wages_sticky(k1)} | yes |
| C-12 | platforms | compliance_cost | increase | short+ | A | OC-2 | {} | yes |
| C-13 | platforms | informal_activity | increase | short+ | B | RS-3 | {binding(k2), evasion(k2)} | yes |
| C-14 | platforms | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k5), can_organize(k5)} or {binding(k1), can_organize(k1)} or {binding(k2), can_organize(k2)} | yes |
| C-15 | platforms | price_paid | increase | short+ | B | PC-17, CR-12, CR-6 | {binding(k1), enforced(k1), wages_sticky(k1)} or {binding(k1), enforced(k1), worth_less(k1)} | yes |
| C-16 | platforms | reclassification | increase | medium+ | B | RS-5 | {binding(k1), enforced(k1), reshaping_pays(k1)} | yes |
| C-17 | platforms | resources_available_other_uses | decrease | short+ | B | PC-17, CR-7 | {binding(k1), enforced(k1), wages_sticky(k1)} | yes |
| C-18 | platforms | return_on_capital | decrease | short+ | B | PC-17, CR-7, PC-9, CR-6 | {binding(k1), enforced(k1), wages_sticky(k1)} or {binding(k2), cost_not_offset(k2), enforced(k2)} | yes |
| C-19 | riders | price_paid | increase | short+ | B | PC-17, CR-12, CR-6, RS-14, PC-9 | {binding(k2), cost_not_offset(k2), enforced(k2), rivals_bound(k2)} or {binding(k1), enforced(k1), rivals_bound(k1), wages_sticky(k1)} or {binding(k1), enforced(k1), rivals_bound(k1), worth_less(k1)} | yes |
| C-20 | riders | quantity_traded | decrease | short+ | B | PC-17, CR-12, CR-6, RS-14 | {binding(k1), enforced(k1), rivals_bound(k1), wages_sticky(k1)} or {binding(k1), enforced(k1), rivals_bound(k1), worth_less(k1)} | yes |
| C-21 | sellers.small_platform | asset_value | increase | short+ | B | PC-17, CR-7 | {binding(k1), compete_with_bound(k1), enforced(k1), valued_on_earnings(k1), wages_sticky(k1)} | yes |
| C-22 | sellers.small_platform | number_of_sellers | increase | medium+ | B | RS-17 | {binding(k1), staying_small_pays(k1)} | yes |
| C-23 | sellers.small_platform | quantity_supplied | increase | medium+ | B | PC-17, CR-12, CR-2, CR-9 | {binding(k1), compete_with_bound(k1), enforced(k1), worth_less(k1)} | yes |
| C-24 | sellers.substitutes | asset_value | increase | short+ | B | PC-17, CR-7 | {binding(k1), compete_with_bound(k1), enforced(k1), valued_on_earnings(k1), wages_sticky(k1)} | yes |
| C-25 | sellers.substitutes | quantity_supplied | increase | medium+ | B | PC-17, CR-12, CR-2, CR-9 | {binding(k1), compete_with_bound(k1), enforced(k1), worth_less(k1)} | yes |
| C-26 | taxpayers or recipients.other_spending or taxpayers.future | resources_available_other_uses | at_least_one_decrease | short+ | A | OC-1 | {} | yes |

## Explanations

- C-1. Compared with no Lanvik App-Based Work Act 2027, reclassification for drivers.contractor rises from the medium run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); Most bound providers comply (p = 0.80); Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.50). Reported.
- C-2. Compared with no Lanvik App-Based Work Act 2027, allocation by non price criteria for drivers.employee rises from the medium run onward (tier B, invisible). Why: PC-17: PC-17; RS-23: RS-23. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); Providers can tell which applicants will cost more under the term (p = 0.70); Most bound providers comply (p = 0.80). Reported.
- C-3. Compared with no Lanvik App-Based Work Act 2027, allocation by non price criteria or search cost or wait time for drivers.employee rises for at least one of them from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; PC-11: PC-11. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.80). Reported.
- C-4. Compared with no Lanvik App-Based Work Act 2027, employment or hours worked or non wage compensation for drivers.employee falls for at least one of them from the short run onward (tier B, invisible). Why: PC-17: PC-17; PC-10: PC-10; CR-2: CR-2; CR-6: sellers facing fewer buyers than they planned for cut their price; PC-9: PC-9. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); Most bound providers comply (p = 0.80); A floor holds some recipients' wage (p = 0.90). It also follows under 3 other minimal assumption set(s). Reported.
- C-5. Compared with no Lanvik App-Based Work Act 2027, excess supply for drivers.employee rises from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; PC-11: PC-11. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.80). Reported.
- C-6. Compared with no Lanvik App-Based Work Act 2027, lobbying effort for drivers.employee rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); The recipients can organize to lobby (p = 0.90). It also follows under 1 other minimal assumption set(s). Reported.
- C-7. Compared with no Lanvik App-Based Work Act 2027, non wage compensation for drivers.employee rises from the short run onward (tier B, visible). Why: PC-17: PC-17. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); Most bound providers comply (p = 0.80). Reported.
- C-8. Compared with no Lanvik App-Based Work Act 2027, wage rate for drivers.employee rises from the short run onward (tier B, visible). Why: PC-9: PC-9. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); Most bound buyers comply with the floor (p = 0.80). Reported.
- C-9. Compared with no Lanvik App-Based Work Act 2027, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-10. Compared with no Lanvik App-Based Work Act 2027, asset value for owners.platforms falls from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.80); Investors expect the measure to stay in force for at least its stated term (p = 0.70). Reported.
- C-11. Compared with no Lanvik App-Based Work Act 2027, asset value for platforms falls from the short run onward (tier B, invisible). Why: PC-17: PC-17; CR-7: CR-7. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); Most bound providers comply (p = 0.80); The providers' businesses are valued on expected earnings (p = 0.70); The other money terms are fixed in the short run (p = 0.60). Reported.
- C-12. Compared with no Lanvik App-Based Work Act 2027, compliance cost for platforms rises from the short run onward (tier A, invisible). Why: OC-2: OC-2. This holds if: no assumption. Reported.
- C-13. Compared with no Lanvik App-Based Work Act 2027, informal activity for platforms rises from the short run onward (tier B, invisible). Why: RS-3: RS-3. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); Some trade below the floor goes undetected (p = 0.65). Reported.
- C-14. Compared with no Lanvik App-Based Work Act 2027, lobbying effort for platforms rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); The bound providers can organize to lobby (p = 0.90). It also follows under 2 other minimal assumption set(s). Reported.
- C-15. Compared with no Lanvik App-Based Work Act 2027, price paid for platforms rises from the short run onward (tier B, visible). Why: PC-17: PC-17; CR-12: CR-12; CR-6: sellers facing fewer buyers than they planned for cut their price. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); Most bound providers comply (p = 0.80); The other money terms are fixed in the short run (p = 0.60). It also follows under 1 other minimal assumption set(s). Reported.
- C-16. Compared with no Lanvik App-Based Work Act 2027, reclassification for platforms rises from the medium run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); Most bound providers comply (p = 0.80); Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.50). Reported.
- C-17. Compared with no Lanvik App-Based Work Act 2027, resources available other uses for platforms falls from the short run onward (tier B, invisible). Why: PC-17: PC-17; CR-7: CR-7. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); Most bound providers comply (p = 0.80); The other money terms are fixed in the short run (p = 0.60). Reported.
- C-18. Compared with no Lanvik App-Based Work Act 2027, return on capital for platforms falls from the short run onward (tier B, invisible). Why: PC-17: PC-17; CR-7: CR-7; PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.80). It also follows under 1 other minimal assumption set(s). Reported.
- C-19. Compared with no Lanvik App-Based Work Act 2027, price paid for riders rises from the short run onward (tier B, invisible). Why: PC-17: PC-17; CR-12: CR-12; CR-6: sellers facing fewer buyers than they planned for cut their price; RS-14: a dearer input is passed down to the output: its price rises where competitors face the same cost, and its sellers sell less where competitors are exempt; PC-9: PC-9. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.80); Most of the bound buyers' rivals face the same floor (p = 0.80). It also follows under 2 other minimal assumption set(s). Reported.
- C-20. Compared with no Lanvik App-Based Work Act 2027, quantity traded for riders falls from the short run onward (tier B, invisible). Why: PC-17: PC-17; CR-12: CR-12; CR-6: sellers facing fewer buyers than they planned for cut their price; RS-14: a dearer input is passed down to the output: its price rises where competitors face the same cost, and its sellers sell less where competitors are exempt. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); Most bound providers comply (p = 0.80); Most of the providers' rivals are bound too (p = 0.80); The other money terms are fixed in the short run (p = 0.60). It also follows under 1 other minimal assumption set(s). Reported.
- C-21. Compared with no Lanvik App-Based Work Act 2027, asset value for sellers.small_platform rises from the short run onward (tier B, invisible). Why: PC-17: PC-17; CR-7: CR-7. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); The unbound firms compete with the bound providers (p = 0.75); Most bound providers comply (p = 0.80); The providers' businesses are valued on expected earnings (p = 0.70); The other money terms are fixed in the short run (p = 0.60). Reported.
- C-22. Compared with no Lanvik App-Based Work Act 2027, number of sellers for sellers.small_platform rises from the medium run onward (tier B, invisible). Why: RS-17: RS-17. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); Some firms near the threshold value staying below it more than an extra hire (p = 0.50). Reported.
- C-23. Compared with no Lanvik App-Based Work Act 2027, quantity supplied for sellers.small_platform rises from the medium run onward (tier B, invisible). Why: PC-17: PC-17; CR-12: CR-12; CR-2: CR-2; CR-9: an owner who leaves the rental market ends the leases of those who live in the building. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); The unbound firms compete with the bound providers (p = 0.75); Most bound providers comply (p = 0.80); The term is worth less to the marginal recipient than it costs the provider (p = 0.55). Reported.
- C-24. Compared with no Lanvik App-Based Work Act 2027, asset value for sellers.substitutes rises from the short run onward (tier B, invisible). Why: PC-17: PC-17; CR-7: CR-7. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); The unbound firms compete with the bound providers (p = 0.75); Most bound providers comply (p = 0.80); The providers' businesses are valued on expected earnings (p = 0.70); The other money terms are fixed in the short run (p = 0.60). Reported.
- C-25. Compared with no Lanvik App-Based Work Act 2027, quantity supplied for sellers.substitutes rises from the medium run onward (tier B, invisible). Why: PC-17: PC-17; CR-12: CR-12; CR-2: CR-2; CR-9: an owner who leaves the rental market ends the leases of those who live in the building. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.95); The unbound firms compete with the bound providers (p = 0.75); Most bound providers comply (p = 0.80); The term is worth less to the marginal recipient than it costs the provider (p = 0.55). Reported.
- C-26. Compared with no Lanvik App-Based Work Act 2027, resources available other uses for taxpayers or recipients.other_spending or taxpayers.future falls for at least one of them from the short run onward (tier A, invisible). Why: OC-1: what the payers give up is what they would otherwise have bought. This holds if: no assumption. Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
