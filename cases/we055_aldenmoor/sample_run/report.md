# Thin-slice run: Aldenmoor Home Inspector Licensing Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-18T21:12:07+00:00
Prediction log sha256 (frozen before the outcome card was opened): `201d7b691d138275…`

## Policy record

- Rule-maker: the Aldenmoor legislature; enacted 3 June 2026, effective 1 July 2027 for new entrants; 1 January 2028 for all inspectors.
- Stated aim: none stated
- k1: licensing_requirement on home_inspection in aldenmoor; binds inspectors, protects None. Source: "Anyone inspecting a home for pay in Aldenmoor must hold a license: 120 hours of approved training, a state exam, $300,000 of insurance and $250 a year."
- Unclear U1: K4 forbids an agent to "direct, steer or require" a client to use a particular inspector. Readings: U1-a: the provision forbids only requiring or conditioning (making a transaction depend on the inspector); an agent may still name or recommend inspectors when asked, as now. / U1-b: naming a particular inspector is "steering"; an agent may give a client only the Board's public list of licensed inspectors.
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.90 | The requirement goes beyond what some current or would-be sellers already meet. |
| `enforced(k1)` | enforcement | 0.70 | The requirement is enforced often enough that many sellers comply or stop. |
| `some_qualify(k1)` | alternative_uses | 0.75 | Some current sellers or new entrants obtain the license. |
| `evasion(k1)` | enforcement | 0.70 | Some sellers keep selling without a license and are not caught. |
| `buyer_substitutes(k1)` | substitutability | 0.60 | Some buyers have a feasible substitute for the licensed service. |
| `tests_valued_quality(k1)` | other | 0.65 | The license tests something buyers value but cannot easily judge. |
| `can_organize(k1)` | other | 0.85 | The license holders can organize to lobby at a cost below their stake. |
| `training_common(k1)` | other | 0.20 | The required training was already commonly taken before the requirement. |
| `contested_otherwise(k1)` | other | 0.70 | Without the measure, the question it settles would still be contested by the same groups. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.current | price_paid | increase | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-2 | buyers.current | quality_information | increase | short+ | B | EN-1, EN-11 | {binding(k1), enforced(k1), tests_valued_quality(k1)} | yes |
| C-3 | buyers.current | quantity_substitute | increase | short+ | B | EN-1, RS-1 | {binding(k1), buyer_substitutes(k1), enforced(k1)} | yes |
| C-4 | buyers.current | quantity_traded | decrease | short+ | B | EN-1, OC-4 | {binding(k1), enforced(k1)} | yes |
| C-5 | buyers.current | resources_available_other_uses | decrease | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-6 | buyers.unlicensed | disputes_settled_outside_courts | increase | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-7 | buyers.unlicensed | quality_information | decrease | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-8 | buyers.unlicensed | search_cost | increase | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-9 | inspectors | compliance_cost | increase | short+ | B | EN-1, CR-8 | {binding(k1), enforced(k1), some_qualify(k1)} | yes |
| C-10 | inspectors | employment | decrease | short+ | B | EN-1, EN-3 | {binding(k1), enforced(k1)} | yes |
| C-11 | inspectors | entry_rate | decrease | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-12 | inspectors | informal_activity | increase | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-13 | inspectors | number_of_sellers | decrease | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-14 | inspectors | quantity_traded | decrease | short+ | B | EN-1, OC-4 | {binding(k1), enforced(k1)} | yes |
| C-15 | inspectors | share_of_sellers_licensed | increase | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-16 | inspectors.licensed | lobbying_effort | increase | medium+ | B | EN-1, EN-2, EN-5, RS-7 | {binding(k1), can_organize(k1), enforced(k1)} | yes |
| C-17 | inspectors.licensed | lobbying_effort (policy_field) | ambiguous | medium+ | B | EN-1, EN-2, EN-5, RS-7 | {binding(k1), can_organize(k1), contested_otherwise(k1), enforced(k1)} | yes |
| C-18 | inspectors.licensed | net_price_received | increase | short+ | B | EN-1, EN-2 | {binding(k1), enforced(k1)} | yes |
| C-19 | officials.enforcement | enforcement_cost | increase | short+ | B | EN-1, OC-3 | {binding(k1), enforced(k1)} | yes |
| C-20 | training_schools | quantity_demanded | increase | short+ | B | EN-1, CR-8 | {binding(k1), enforced(k1), some_qualify(k1)} | yes |

## Explanations

- C-1. Compared with no Aldenmoor Home Inspector Licensing Act, price paid for buyers.current rises from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-2. Compared with no Aldenmoor Home Inspector Licensing Act, quality information for buyers.current rises from the short run onward (tier B, visible). Why: EN-1: EN-1; EN-11: EN-11. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); The license tests something buyers value but cannot easily judge (p = 0.65). Reported.
- C-3. Compared with no Aldenmoor Home Inspector Licensing Act, quantity substitute for buyers.current rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-1: when a good becomes dearer, buyers turn to substitutes. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); Some buyers have a feasible substitute for the licensed service (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-4. Compared with no Aldenmoor Home Inspector Licensing Act, quantity traded for buyers.current falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-4: exchanges that no longer happen are lost to both sides. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-5. Compared with no Aldenmoor Home Inspector Licensing Act, resources available other uses for buyers.current falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-6. Compared with no Aldenmoor Home Inspector Licensing Act, disputes settled outside courts for buyers.unlicensed rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.70). Reported.
- C-7. Compared with no Aldenmoor Home Inspector Licensing Act, quality information for buyers.unlicensed falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.70). Reported.
- C-8. Compared with no Aldenmoor Home Inspector Licensing Act, search cost for buyers.unlicensed rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.70). Reported.
- C-9. Compared with no Aldenmoor Home Inspector Licensing Act, compliance cost for inspectors rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some current sellers or new entrants obtain the license (p = 0.75). Reported.
- C-10. Compared with no Aldenmoor Home Inspector Licensing Act, employment for inspectors falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; EN-3: EN-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-11. Compared with no Aldenmoor Home Inspector Licensing Act, entry rate for inspectors falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-12. Compared with no Aldenmoor Home Inspector Licensing Act, informal activity for inspectors rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.70). Reported.
- C-13. Compared with no Aldenmoor Home Inspector Licensing Act, number of sellers for inspectors falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-14. Compared with no Aldenmoor Home Inspector Licensing Act, quantity traded for inspectors falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-4: exchanges that no longer happen are lost to both sides. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-15. Compared with no Aldenmoor Home Inspector Licensing Act, share of sellers licensed for inspectors rises from the short run onward (tier B, visible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-16. Compared with no Aldenmoor Home Inspector Licensing Act, lobbying effort for inspectors.licensed rises from the medium run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2; EN-5: EN-5; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The license holders can organize to lobby at a cost below their stake (p = 0.85); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-17. Compared with no Aldenmoor Home Inspector Licensing Act, lobbying effort (policy field) for inspectors.licensed may move either way from the medium run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2; EN-5: EN-5; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The license holders can organize to lobby at a cost below their stake (p = 0.85); Without the measure, the question it settles would still be contested by the same groups (p = 0.70); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-18. Compared with no Aldenmoor Home Inspector Licensing Act, net price received for inspectors.licensed rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-19. Compared with no Aldenmoor Home Inspector Licensing Act, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-20. Compared with no Aldenmoor Home Inspector Licensing Act, quantity demanded for training_schools rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some current sellers or new entrants obtain the license (p = 0.75). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
