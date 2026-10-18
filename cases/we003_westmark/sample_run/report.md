# Thin-slice run: Westmark State Cosmetology Act, amendment 7

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-18T20:53:36+00:00
Prediction log sha256 (frozen before the outcome card was opened): `ef644730f4ea9192…`

## Policy record

- Rule-maker: the Westmark legislature; enacted amendment 7, effective amendment 7.
- Stated aim: none stated
- k1: licensing_requirement on hair_braiding in westmark; binds braiders, protects None. Source: "Anyone who braids hair for pay, and any business that employs them, must hold a full cosmetology license: 1,500 hours at a licensed cosmetology school (typical tuition $12,000 to $18,000) and a state exam."
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.95 | The requirement goes beyond what some current or would-be sellers already meet. |
| `enforced(k1)` | enforcement | 0.70 | The requirement is enforced often enough that many sellers comply or stop. |
| `some_qualify(k1)` | alternative_uses | 0.80 | Some current sellers or new entrants obtain the license. |
| `evasion(k1)` | enforcement | 0.80 | Some sellers keep selling without a license and are not caught. |
| `buyer_substitutes(k1)` | substitutability | 0.75 | Some buyers have a feasible substitute for the licensed service. |
| `tests_valued_quality(k1)` | other | 0.15 | The license tests something buyers value but cannot easily judge. |
| `can_organize(k1)` | other | 0.70 | The license holders can organize to lobby at a cost below their stake. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | braiders | compliance_cost | increase | short+ | B | EN-1, CR-8 | {binding(k1), enforced(k1), some_qualify(k1)} | yes |
| C-2 | braiders | employment | decrease | short+ | B | EN-1, EN-3 | {binding(k1), enforced(k1)} | yes |
| C-3 | braiders | entry_rate | decrease | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-4 | braiders | informal_activity | increase | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-5 | braiders | number_of_sellers | decrease | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-6 | braiders | quantity_traded | decrease | short+ | B | EN-1, OC-4 | {binding(k1), enforced(k1)} | yes |
| C-7 | braiders | share_of_sellers_licensed | increase | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-8 | braiders.licensed | lobbying_effort | increase | medium+ | B | EN-1, EN-2, EN-5, RS-7 | {binding(k1), can_organize(k1), enforced(k1)} | yes |
| C-9 | braiders.licensed | net_price_received | increase | short+ | B | EN-1, EN-2 | {binding(k1), enforced(k1)} | yes |
| C-10 | customers.braiding | disputes_settled_outside_courts | increase | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-11 | customers.braiding | price_paid | increase | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-12 | customers.braiding | quality_information | decrease | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-13 | customers.braiding | quantity_substitute | increase | short+ | B | EN-1, RS-1 | {binding(k1), buyer_substitutes(k1), enforced(k1)} | yes |
| C-14 | customers.braiding | quantity_traded | decrease | short+ | B | EN-1, OC-4 | {binding(k1), enforced(k1)} | yes |
| C-15 | customers.braiding | resources_available_other_uses | decrease | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-16 | customers.braiding | search_cost | increase | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-17 | officials.enforcement | enforcement_cost | increase | short+ | B | EN-1, OC-3 | {binding(k1), enforced(k1)} | yes |
| C-18 | schools.cosmetology | quantity_demanded | increase | short+ | B | EN-1, CR-8 | {binding(k1), enforced(k1), some_qualify(k1)} | yes |

## Explanations

- C-1. Compared with no Westmark State Cosmetology Act, amendment 7, compliance cost for braiders rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some current sellers or new entrants obtain the license (p = 0.80). Reported.
- C-2. Compared with no Westmark State Cosmetology Act, amendment 7, employment for braiders falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; EN-3: EN-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-3. Compared with no Westmark State Cosmetology Act, amendment 7, entry rate for braiders falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-4. Compared with no Westmark State Cosmetology Act, amendment 7, informal activity for braiders rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.80). Reported.
- C-5. Compared with no Westmark State Cosmetology Act, amendment 7, number of sellers for braiders falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-6. Compared with no Westmark State Cosmetology Act, amendment 7, quantity traded for braiders falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-4: exchanges that no longer happen are lost to both sides. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-7. Compared with no Westmark State Cosmetology Act, amendment 7, share of sellers licensed for braiders rises from the short run onward (tier B, visible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-8. Compared with no Westmark State Cosmetology Act, amendment 7, lobbying effort for braiders.licensed rises from the medium run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2; EN-5: EN-5; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The license holders can organize to lobby at a cost below their stake (p = 0.70); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-9. Compared with no Westmark State Cosmetology Act, amendment 7, net price received for braiders.licensed rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-10. Compared with no Westmark State Cosmetology Act, amendment 7, disputes settled outside courts for customers.braiding rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.80). Reported.
- C-11. Compared with no Westmark State Cosmetology Act, amendment 7, price paid for customers.braiding rises from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-12. Compared with no Westmark State Cosmetology Act, amendment 7, quality information for customers.braiding falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.80). Reported.
- C-13. Compared with no Westmark State Cosmetology Act, amendment 7, quantity substitute for customers.braiding rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-1: when a good becomes dearer, buyers turn to substitutes. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); Some buyers have a feasible substitute for the licensed service (p = 0.75); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-14. Compared with no Westmark State Cosmetology Act, amendment 7, quantity traded for customers.braiding falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-4: exchanges that no longer happen are lost to both sides. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-15. Compared with no Westmark State Cosmetology Act, amendment 7, resources available other uses for customers.braiding falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-16. Compared with no Westmark State Cosmetology Act, amendment 7, search cost for customers.braiding rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.80). Reported.
- C-17. Compared with no Westmark State Cosmetology Act, amendment 7, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-18. Compared with no Westmark State Cosmetology Act, amendment 7, quantity demanded for schools.cosmetology rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.95); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some current sellers or new entrants obtain the license (p = 0.80). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
