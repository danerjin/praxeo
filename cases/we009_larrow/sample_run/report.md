# Thin-slice run: Larrow Fair Wage Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-21T17:26:53+00:00
Prediction log sha256 (frozen before the outcome card was opened): `0dba2bd63a6148d9…`

## Policy record

- Rule-maker: the Larrow legislature; enacted March of Year 1, effective January 1, Year 2.
- Stated aim: none stated
- k1: price_floor on adult_low_wage_labor in larrow; binds employers.low_wage, protects None. Source: "The adult minimum wage for employees aged 20 and over, paid by all employers in Larrow, is $12 an hour from January 1, Year 2 and $14 an hour from January 1, Year 3."
- k2: price_floor on youth_labor in larrow; binds employers.low_wage, protects None. Source: "Employers may pay employees under 20 at least 85% of the adult minimum: $10.20 in Year 2 and $11.90 in Year 3."
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.90 | The floor binds for an identifiable group of sellers. |
| `enforced(k1)` | enforcement | 0.75 | Most bound buyers comply with the floor. |
| `cost_not_offset(k1)` | substitutability | 0.80 | The floor raises buyers' cost per unit; it is not fully offset. |
| `evasion(k1)` | enforcement | 0.65 | Some trade below the floor goes undetected. |
| `can_organize(k1)` | other | 0.65 | The bound buyers can organize to lobby. |
| `sellers_organize(k1)` | other | 0.65 | The sellers the floor raises can organize to lobby. |
| `margins(k1)` | other | 0.90 | Buyers can adjust at least one margin. |
| `rivals_bound(k1)` | other | 0.80 | Most of the bound buyers' rivals face the same floor. |
| `cross_border_feasible(k1)` | mobility | 0.70 | Some buyers of the output can easily buy across the boundary. |
| `substitute_exists(k1)` | alternative_uses | 0.75 | A substitute exists for what the floor makes dearer. |
| `reshaping_pays(k1)` | other | 0.55 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |
| `expected_ahead(k1)` | expectations | 0.85 | Investors expected the floor before it took effect. |
| `expected_to_last(k1)` | expectations | 0.85 | Investors expect the measure to stay in force for at least its stated term. |
| `lower_tier_used(k1)` | other | 0.80 | A meaningful number of buyers use the lower floor. |
| `tiers_substitute(k1)` | substitutability | 0.80 | The two groups of sellers are substitutes. |
| `budget_fixed(k1)` | revenue_use | 0.60 | The agency's budget is not increased for the measure. |
| `binding(k2)` | binding | 0.80 | The floor binds for an identifiable group of sellers. |
| `enforced(k2)` | enforcement | 0.75 | Most bound buyers comply with the floor. |
| `cost_not_offset(k2)` | substitutability | 0.80 | The floor raises buyers' cost per unit; it is not fully offset. |
| `evasion(k2)` | enforcement | 0.65 | Some trade below the floor goes undetected. |
| `can_organize(k2)` | other | 0.65 | The bound buyers can organize to lobby. |
| `sellers_organize(k2)` | other | 0.65 | The sellers the floor raises can organize to lobby. |
| `margins(k2)` | other | 0.90 | Buyers can adjust at least one margin. |
| `budget_fixed(k2)` | revenue_use | 0.60 | The agency's budget is not increased for the measure. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | consumers | price_paid | increase | short+ | B | PC-9, CR-6, RS-14 | {binding(k1), cost_not_offset(k1), enforced(k1), rivals_bound(k1)} | yes |
| C-2 | consumers.border | cross_border_purchases | increase | short+ | B | PC-9, CR-6, RS-4 | {binding(k1), cost_not_offset(k1), cross_border_feasible(k1), enforced(k1)} | yes |
| C-3 | employers.low_wage | compliance_cost | increase | short+ | A | OC-2 | {} | yes |
| C-4 | employers.low_wage | informal_activity | increase | short+ | B | RS-3 | {binding(k1), evasion(k1)} or {binding(k2), evasion(k2)} | yes |
| C-5 | employers.low_wage | investment_target | decrease | short+ | B | TS-2 | {binding(k1), cost_not_offset(k1), enforced(k1), expected_ahead(k1)} | yes |
| C-6 | employers.low_wage | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k1), can_organize(k1)} or {binding(k2), can_organize(k2)} | yes |
| C-7 | employers.low_wage | quantity_substitute | increase | medium+ | B | PC-9, CR-6, RS-1 | {binding(k1), cost_not_offset(k1), enforced(k1), substitute_exists(k1)} | yes |
| C-8 | employers.low_wage | reclassification | increase | short+ | B | RS-5 | {binding(k1), enforced(k1), reshaping_pays(k1)} | yes |
| C-9 | employers.low_wage | return_on_capital | decrease | short+ | B | PC-9, CR-6, CR-7 | {binding(k2), cost_not_offset(k2), enforced(k2)} or {binding(k1), cost_not_offset(k1), enforced(k1)} | yes |
| C-10 | factor_owners.specific | asset_value | decrease | short+ | B | PC-9, CR-6, SB-4 | {binding(k1), cost_not_offset(k1), enforced(k1), expected_to_last(k1)} | yes |
| C-11 | input_suppliers | quantity_traded | increase | medium+ | B | PC-9, CR-6, RS-1 | {binding(k1), cost_not_offset(k1), enforced(k1), substitute_exists(k1)} | yes |
| C-12 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |
| C-13 | officials.enforcement | enforcement_cost (other_work) | decrease | short+ | B | OC-3 | {budget_fixed(k1)} or {budget_fixed(k2)} | yes |
| C-14 | workers.adult_low_wage | employment or hours_worked or non_wage_compensation | at_least_one_decrease | short+ | B | PC-9, CR-6, RS-1, PC-10 | {binding(k1), cost_not_offset(k1), enforced(k1), margins(k1)} or {binding(k1), cost_not_offset(k1), enforced(k1), lower_tier_used(k1), tiers_substitute(k1)} | yes |
| C-15 | workers.adult_low_wage | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k1), sellers_organize(k1)} | yes |
| C-16 | workers.adult_low_wage | wage_rate | increase | short+ | B | PC-9 | {binding(k1), enforced(k1)} | yes |
| C-17 | workers.prospective | allocation_by_non_price_criteria or search_cost or wait_time | at_least_one_increase | short+ | B | PC-9, CR-6, PC-11 | {binding(k1), cost_not_offset(k1), enforced(k1)} | yes |
| C-18 | workers.prospective | excess_supply | increase | short+ | B | PC-9, CR-6, PC-11 | {binding(k1), cost_not_offset(k1), enforced(k1)} | yes |
| C-19 | workers.youth | employment or hours_worked or non_wage_compensation | ambiguous | short+ | B | PC-9, CR-6, RS-1, PC-10 | {binding(k1), cost_not_offset(k1), enforced(k1), lower_tier_used(k1), tiers_substitute(k1)} or {binding(k2), cost_not_offset(k2), enforced(k2), margins(k2)} | yes |
| C-20 | workers.youth | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k2), sellers_organize(k2)} | yes |
| C-21 | workers.youth | wage_rate | increase | short+ | B | PC-9 | {binding(k2), enforced(k2)} | yes |

## Explanations

- C-1. Compared with no Larrow Fair Wage Act, price paid for consumers rises from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; RS-14: a dearer input is passed down to the output: its price rises where competitors face the same cost, and its sellers sell less where competitors are exempt. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.75); Most of the bound buyers' rivals face the same floor (p = 0.80). Reported.
- C-2. Compared with no Larrow Fair Wage Act, cross border purchases for consumers.border rises from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; RS-4: shut-out buyers turn to uncovered units, which are close substitutes. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Some buyers of the output can easily buy across the boundary (p = 0.70); Most bound buyers comply with the floor (p = 0.75). Reported.
- C-3. Compared with no Larrow Fair Wage Act, compliance cost for employers.low_wage rises from the short run onward (tier A, invisible). Why: OC-2: OC-2. This holds if: no assumption. Reported.
- C-4. Compared with no Larrow Fair Wage Act, informal activity for employers.low_wage rises from the short run onward (tier B, invisible). Why: RS-3: RS-3. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); Some trade below the floor goes undetected (p = 0.65). It also follows under 1 other minimal assumption set(s). Reported.
- C-5. Compared with no Larrow Fair Wage Act, investment target for employers.low_wage falls from the short run onward (tier B, invisible). Why: TS-2: TS-2. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.75); Investors expected the floor before it took effect (p = 0.85). Reported.
- C-6. Compared with no Larrow Fair Wage Act, lobbying effort for employers.low_wage rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The bound buyers can organize to lobby (p = 0.65). It also follows under 1 other minimal assumption set(s). Reported.
- C-7. Compared with no Larrow Fair Wage Act, quantity substitute for employers.low_wage rises from the medium run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; RS-1: when a good becomes dearer, buyers turn to substitutes. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.75); A substitute exists for what the floor makes dearer (p = 0.75). Reported.
- C-8. Compared with no Larrow Fair Wage Act, reclassification for employers.low_wage rises from the short run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); Most bound buyers comply with the floor (p = 0.75); Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.55). Reported.
- C-9. Compared with no Larrow Fair Wage Act, return on capital for employers.low_wage falls from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; CR-7: CR-7. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.75). It also follows under 1 other minimal assumption set(s). Reported.
- C-10. Compared with no Larrow Fair Wage Act, asset value for factor_owners.specific falls from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.75); Investors expect the measure to stay in force for at least its stated term (p = 0.85). Reported.
- C-11. Compared with no Larrow Fair Wage Act, quantity traded for input_suppliers rises from the medium run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; RS-1: when a good becomes dearer, buyers turn to substitutes. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.75); A substitute exists for what the floor makes dearer (p = 0.75). Reported.
- C-12. Compared with no Larrow Fair Wage Act, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-13. Compared with no Larrow Fair Wage Act, enforcement cost (other work) for officials.enforcement falls from the short run onward (tier B, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: The agency's budget is not increased for the measure (p = 0.60). It also follows under 1 other minimal assumption set(s). Reported.
- C-14. Compared with no Larrow Fair Wage Act, employment or hours worked or non wage compensation for workers.adult_low_wage falls for at least one of them from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; RS-1: when a good becomes dearer, buyers turn to substitutes; PC-10: PC-10. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.75); Buyers can adjust at least one margin (p = 0.90). It also follows under 1 other minimal assumption set(s). Reported.
- C-15. Compared with no Larrow Fair Wage Act, lobbying effort for workers.adult_low_wage rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The sellers the floor raises can organize to lobby (p = 0.65). Reported.
- C-16. Compared with no Larrow Fair Wage Act, wage rate for workers.adult_low_wage rises from the short run onward (tier B, visible). Why: PC-9: PC-9. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); Most bound buyers comply with the floor (p = 0.75). Reported.
- C-17. Compared with no Larrow Fair Wage Act, allocation by non price criteria or search cost or wait time for workers.prospective rises for at least one of them from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; PC-11: PC-11. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.75). Reported.
- C-18. Compared with no Larrow Fair Wage Act, excess supply for workers.prospective rises from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; PC-11: PC-11. This holds if: The floor binds for an identifiable group of sellers (p = 0.90); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.75). Reported.
- C-19. Compared with no Larrow Fair Wage Act, employment or hours worked or non wage compensation for workers.youth may move either way from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; RS-1: when a good becomes dearer, buyers turn to substitutes; PC-10: PC-10. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.75); Buyers can adjust at least one margin (p = 0.90). It also follows under 1 other minimal assumption set(s). Reported.
- C-20. Compared with no Larrow Fair Wage Act, lobbying effort for workers.youth rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); The sellers the floor raises can organize to lobby (p = 0.65). Reported.
- C-21. Compared with no Larrow Fair Wage Act, wage rate for workers.youth rises from the short run onward (tier B, visible). Why: PC-9: PC-9. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); Most bound buyers comply with the floor (p = 0.75). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
