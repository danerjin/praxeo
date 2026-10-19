# Thin-slice run: Westmere Residential Energy Performance Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T20:01:13+00:00
Prediction log sha256 (frozen before the outcome card was opened): `c626f5a9846b5df3…`

## Policy record

- Rule-maker: the Westmere legislature; enacted 15 June of Year 0, effective 1 January of Year 1.
- Stated aim: none stated
- k1: product_standard on new_homes in westmere_housing; binds builders, protects None. Source: "K1, the performance standard: new homes whose DEI exceeds a maximum may not be built."
- Unclear U1: The Act requires the Energy Office to adjust the index for dwelling size, but it does not say what the adjustment is. Readings: U1-a: no adjustment beyond the per-square-foot measure / U1-b: homes above 2,500 square feet are held to the maximum as if they were 2,500 square feet
- Unclear U2: The Act does not say which code the rebate's "applicable state energy code" means for a home vested under K2. Readings: U2-a: the code in force on the filing date / U2-b: the code in force when the rebate is claimed at completion
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.70 | The standard binds on some designs. |
| `enforced(k1)` | enforcement | 0.90 | Most makers comply. |
| `can_organize(k1)` | other | 0.90 | The makers can organize to lobby. |
| `stock_competes(k1)` | substitutability | 0.80 | Existing units compete with new ones. |
| `buyers_value_standard(k1)` | other | 0.30 | Buyers value the standard enough to prefer covered units. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | builders | compliance_cost | increase | short+ | B | EN-14 | {binding(k1), enforced(k1)} | yes |
| C-2 | builders | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k1), can_organize(k1)} | yes |
| C-3 | builders | quantity_supplied | decrease | medium+ | B | EN-14 | {binding(k1), enforced(k1)} | yes |
| C-4 | buyers.new_homes | price_paid | increase | short+ | B | EN-14 | {binding(k1), enforced(k1)} | yes |
| C-5 | buyers.new_homes | specification_level | increase | short+ | B | EN-14 | {binding(k1), enforced(k1)} | yes |
| C-6 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |
| C-7 | owners.existing_homes | asset_value | increase | medium+ | B | CR-7, EN-14 | {binding(k1), enforced(k1), stock_competes(k1)} | yes |
| C-8 | owners.existing_homes | stock_age | increase | long | B | CR-7, EN-14 | {binding(k1), enforced(k1), stock_competes(k1)} | yes |
| C-9 | taxpayers.current or recipients.other_spending or taxpayers.future | resources_available_other_uses | at_least_one_decrease | short+ | A | OC-1 | {} | yes |

## Explanations

- C-1. Compared with no Westmere Residential Energy Performance Act, compliance cost for builders rises from the short run onward (tier B, invisible). Why: EN-14: EN-14. This holds if: The standard binds on some designs (p = 0.70); Most makers comply (p = 0.90). Reported.
- C-2. Compared with no Westmere Residential Energy Performance Act, lobbying effort for builders rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The standard binds on some designs (p = 0.70); The makers can organize to lobby (p = 0.90). Reported.
- C-3. Compared with no Westmere Residential Energy Performance Act, quantity supplied for builders falls from the medium run onward (tier B, invisible). Why: EN-14: EN-14. This holds if: The standard binds on some designs (p = 0.70); Most makers comply (p = 0.90). Reported.
- C-4. Compared with no Westmere Residential Energy Performance Act, price paid for buyers.new_homes rises from the short run onward (tier B, invisible). Why: EN-14: EN-14. This holds if: The standard binds on some designs (p = 0.70); Most makers comply (p = 0.90). Reported.
- C-5. Compared with no Westmere Residential Energy Performance Act, specification level for buyers.new_homes rises from the short run onward (tier B, visible). Why: EN-14: EN-14. This holds if: The standard binds on some designs (p = 0.70); Most makers comply (p = 0.90). Reported.
- C-6. Compared with no Westmere Residential Energy Performance Act, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-7. Compared with no Westmere Residential Energy Performance Act, asset value for owners.existing_homes rises from the medium run onward (tier B, invisible). Why: CR-7: CR-7; EN-14: EN-14. This holds if: The standard binds on some designs (p = 0.70); Most makers comply (p = 0.90); Existing units compete with new ones (p = 0.80). Reported.
- C-8. Compared with no Westmere Residential Energy Performance Act, stock age for owners.existing_homes rises in the long run (tier B, invisible). Why: CR-7: CR-7; EN-14: EN-14. This holds if: The standard binds on some designs (p = 0.70); Most makers comply (p = 0.90); Existing units compete with new ones (p = 0.80). Reported.
- C-9. Compared with no Westmere Residential Energy Performance Act, resources available other uses for taxpayers.current or recipients.other_spending or taxpayers.future falls for at least one of them from the short run onward (tier A, invisible). Why: OC-1: what the payers give up is what they would otherwise have bought. This holds if: no assumption. Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
