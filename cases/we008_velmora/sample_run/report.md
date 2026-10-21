# Thin-slice run: Velmora Dairy Stabilization Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-21T17:02:22+00:00
Prediction log sha256 (frozen before the outcome card was opened): `d674769278ca4c5d…`

## Policy record

- Rule-maker: the Velmora legislature; enacted June of Year 0, effective January 1, Year 1.
- Stated aim: none stated
- k1: price_floor on raw_milk in velmora; binds plants.commodity, protects None. Source: "Raw milk produced on farms registered in Velmora must be bought at a price of at least $21.00 per cwt by any plant located in Velmora that buys it."
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.80 | The floor binds for an identifiable group of sellers. |
| `enforced(k1)` | enforcement | 0.85 | Most bound buyers comply with the floor. |
| `cost_not_offset(k1)` | substitutability | 0.80 | The floor raises buyers' cost per unit; it is not fully offset. |
| `evasion(k1)` | enforcement | 0.55 | Some trade below the floor goes undetected. |
| `can_organize(k1)` | other | 0.70 | The bound buyers can organize to lobby. |
| `sellers_organize(k1)` | other | 0.70 | The sellers the floor raises can organize to lobby. |
| `rivals_bound(k1)` | other | 0.15 | Most of the bound buyers' rivals face the same floor. |
| `reshaping_pays(k1)` | other | 0.55 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |
| `expected_ahead(k1)` | expectations | 0.80 | Investors expected the floor before it took effect. |
| `expected_to_last(k1)` | expectations | 0.65 | Investors expect the measure to stay in force for at least its stated term. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | consumers | price_paid | increase | short+ | B | PC-9, CR-6, RS-14 | {binding(k1), cost_not_offset(k1), enforced(k1), rivals_bound(k1)} | no |
| C-2 | factor_owners.specific | asset_value | decrease | short+ | B | PC-9, CR-6, SB-4 | {binding(k1), cost_not_offset(k1), enforced(k1), expected_to_last(k1)} | yes |
| C-3 | farmers.velmora | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k1), sellers_organize(k1)} | yes |
| C-4 | farmers.velmora | net_price_received | increase | short+ | B | PC-9 | {binding(k1), enforced(k1)} | yes |
| C-5 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |
| C-6 | officials.enforcement | inventory_held | increase | short+ | B | PC-9, SB-9 | {binding(k1), cost_not_offset(k1), enforced(k1)} | yes |
| C-7 | officials.enforcement | subsidy_outlay | increase | short+ | B | PC-9, SB-9 | {binding(k1), cost_not_offset(k1), enforced(k1)} | yes |
| C-8 | plants.commodity | compliance_cost | increase | short+ | A | OC-2 | {} | yes |
| C-9 | plants.commodity | informal_activity | increase | short+ | B | RS-3 | {binding(k1), evasion(k1)} | yes |
| C-10 | plants.commodity | investment_target | decrease | short+ | B | TS-2 | {binding(k1), cost_not_offset(k1), enforced(k1), expected_ahead(k1)} | yes |
| C-11 | plants.commodity | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k1), can_organize(k1)} | yes |
| C-12 | plants.commodity | price_paid | increase | short+ | B | PC-9 | {binding(k1), enforced(k1)} | yes |
| C-13 | plants.commodity | reclassification | increase | short+ | B | RS-5 | {binding(k1), enforced(k1), reshaping_pays(k1)} | yes |
| C-14 | taxpayers or recipients.other_spending | resources_available_other_uses | at_least_one_decrease | short+ | B | OC-1, PC-9, SB-9 | {} | yes |

## Explanations

- C-1. Compared with no Velmora Dairy Stabilization Act, price paid for consumers rises from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; RS-14: a dearer input is passed down to the output: its price rises where competitors face the same cost, and its sellers sell less where competitors are exempt. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.85); Most of the bound buyers' rivals face the same floor (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-2. Compared with no Velmora Dairy Stabilization Act, asset value for factor_owners.specific falls from the short run onward (tier B, invisible). Why: PC-9: PC-9; CR-6: sellers facing fewer buyers than they planned for cut their price; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.85); Investors expect the measure to stay in force for at least its stated term (p = 0.65). Reported.
- C-3. Compared with no Velmora Dairy Stabilization Act, lobbying effort for farmers.velmora rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); The sellers the floor raises can organize to lobby (p = 0.70). Reported.
- C-4. Compared with no Velmora Dairy Stabilization Act, net price received for farmers.velmora rises from the short run onward (tier B, visible). Why: PC-9: PC-9. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); Most bound buyers comply with the floor (p = 0.85). Reported.
- C-5. Compared with no Velmora Dairy Stabilization Act, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-6. Compared with no Velmora Dairy Stabilization Act, inventory held for officials.enforcement rises from the short run onward (tier B, invisible). Why: PC-9: PC-9; SB-9: SB-9. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.85). Reported.
- C-7. Compared with no Velmora Dairy Stabilization Act, subsidy outlay for officials.enforcement rises from the short run onward (tier B, invisible). Why: PC-9: PC-9; SB-9: SB-9. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.85). Reported.
- C-8. Compared with no Velmora Dairy Stabilization Act, compliance cost for plants.commodity rises from the short run onward (tier A, invisible). Why: OC-2: OC-2. This holds if: no assumption. Reported.
- C-9. Compared with no Velmora Dairy Stabilization Act, informal activity for plants.commodity rises from the short run onward (tier B, invisible). Why: RS-3: RS-3. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); Some trade below the floor goes undetected (p = 0.55). Reported.
- C-10. Compared with no Velmora Dairy Stabilization Act, investment target for plants.commodity falls from the short run onward (tier B, invisible). Why: TS-2: TS-2. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); The floor raises buyers' cost per unit; it is not fully offset (p = 0.80); Most bound buyers comply with the floor (p = 0.85); Investors expected the floor before it took effect (p = 0.80). Reported.
- C-11. Compared with no Velmora Dairy Stabilization Act, lobbying effort for plants.commodity rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); The bound buyers can organize to lobby (p = 0.70). Reported.
- C-12. Compared with no Velmora Dairy Stabilization Act, price paid for plants.commodity rises from the short run onward (tier B, visible). Why: PC-9: PC-9. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); Most bound buyers comply with the floor (p = 0.85). Reported.
- C-13. Compared with no Velmora Dairy Stabilization Act, reclassification for plants.commodity rises from the short run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: The floor binds for an identifiable group of sellers (p = 0.80); Most bound buyers comply with the floor (p = 0.85); Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.55). Reported.
- C-14. Compared with no Velmora Dairy Stabilization Act, resources available other uses for taxpayers or recipients.other_spending falls for at least one of them from the short run onward (tier B, invisible). Why: OC-1: what the payers give up is what they would otherwise have bought; PC-9: PC-9; SB-9: SB-9. This holds if: no assumption. Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
