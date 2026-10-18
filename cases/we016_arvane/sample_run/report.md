# Thin-slice run: Arvane Interior Design Practice Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-18T20:58:43+00:00
Prediction log sha256 (frozen before the outcome card was opened): `62b446df23584f6b…`

## Policy record

- Rule-maker: the Arvane legislature; enacted ten months before the effective date, effective ten months after enactment.
- Stated aim: none stated
- k1: licensing_requirement on interior_design in arvane; binds designers, protects None. Source: "Anyone who offers interior design for pay in Arvane, and any firm that employs them, must hold a license."
- Unclear U1: Whether choosing furnishings, finishes and colors without any space planning ("styling") is covered. Readings: U1-a: covered (the definition lists "selection of interior finishes and furnishings") / U1-b: not covered (only space planning, or styling done with it, is covered)
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.90 | The requirement goes beyond what some current or would-be sellers already meet. |
| `enforced(k1)` | enforcement | 0.70 | The requirement is enforced often enough that many sellers comply or stop. |
| `some_qualify(k1)` | alternative_uses | 0.85 | Some current sellers or new entrants obtain the license. |
| `evasion(k1)` | enforcement | 0.80 | Some sellers keep selling without a license and are not caught. |
| `buyer_substitutes(k1)` | substitutability | 0.85 | Some buyers have a feasible substitute for the licensed service. |
| `tests_valued_quality(k1)` | other | 0.75 | The license tests something buyers value but cannot easily judge. |
| `can_organize(k1)` | other | 0.80 | The license holders can organize to lobby at a cost below their stake. |
| `enforcement_budget_raised(k1)` | revenue_use | 0.85 | The administering agency's budget is raised to cover the new work, so taxpayers fund it. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | clients | disputes_settled_outside_courts | increase | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-2 | clients | price_paid | increase | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-3 | clients | quality_information | ambiguous | short+ | B | EN-1, EN-11, RS-3 | {binding(k1), enforced(k1), evasion(k1)} or {binding(k1), enforced(k1), tests_valued_quality(k1)} | yes |
| C-4 | clients | quantity_substitute | increase | short+ | B | EN-1, RS-1 | {binding(k1), buyer_substitutes(k1), enforced(k1)} | yes |
| C-5 | clients | quantity_traded | decrease | short+ | B | EN-1, OC-4 | {binding(k1), enforced(k1)} | yes |
| C-6 | clients | resources_available_other_uses | decrease | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-7 | clients | search_cost | increase | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-8 | designers | compliance_cost | increase | short+ | B | EN-1, CR-8 | {binding(k1), enforced(k1), some_qualify(k1)} | yes |
| C-9 | designers | employment | decrease | short+ | B | EN-1, EN-3 | {binding(k1), enforced(k1)} | yes |
| C-10 | designers | entry_rate | decrease | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-11 | designers | informal_activity | increase | short+ | B | EN-1, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-12 | designers | number_of_sellers | decrease | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-13 | designers | quantity_traded | decrease | short+ | B | EN-1, OC-4 | {binding(k1), enforced(k1)} | yes |
| C-14 | designers | share_of_sellers_licensed | increase | short+ | B | EN-1 | {binding(k1), enforced(k1)} | yes |
| C-15 | designers.grandfathered | lobbying_effort | increase | medium+ | B | EN-1, EN-2, EN-5, RS-7 | {binding(k1), can_organize(k1), enforced(k1)} | yes |
| C-16 | designers.grandfathered | net_price_received | increase | short+ | B | EN-1, EN-2 | {binding(k1), enforced(k1)} | yes |
| C-17 | officials.enforcement | enforcement_cost | increase | short+ | B | EN-1, OC-3 | {binding(k1), enforced(k1)} | yes |
| C-18 | schools.design | quantity_demanded | increase | short+ | B | EN-1, CR-8 | {binding(k1), enforced(k1), some_qualify(k1)} | yes |
| C-19 | taxpayers or recipients.other_spending or taxpayers.future | resources_available_other_uses | at_least_one_decrease | short+ | B | EN-1, OC-3, OC-1 | {binding(k1), enforced(k1), enforcement_budget_raised(k1)} | yes |

## Explanations

- C-1. Compared with no Arvane Interior Design Practice Act, disputes settled outside courts for clients rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.80). Reported.
- C-2. Compared with no Arvane Interior Design Practice Act, price paid for clients rises from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-3. Compared with no Arvane Interior Design Practice Act, quality information for clients may move either way from the short run onward (tier B, visible). Why: EN-1: EN-1; EN-11: EN-11; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.80). It also follows under 1 other minimal assumption set(s). Reported.
- C-4. Compared with no Arvane Interior Design Practice Act, quantity substitute for clients rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-1: when a good becomes dearer, buyers turn to substitutes. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); Some buyers have a feasible substitute for the licensed service (p = 0.85); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-5. Compared with no Arvane Interior Design Practice Act, quantity traded for clients falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-4: exchanges that no longer happen are lost to both sides. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-6. Compared with no Arvane Interior Design Practice Act, resources available other uses for clients falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-7. Compared with no Arvane Interior Design Practice Act, search cost for clients rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.80). Reported.
- C-8. Compared with no Arvane Interior Design Practice Act, compliance cost for designers rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some current sellers or new entrants obtain the license (p = 0.85). Reported.
- C-9. Compared with no Arvane Interior Design Practice Act, employment for designers falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; EN-3: EN-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-10. Compared with no Arvane Interior Design Practice Act, entry rate for designers falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-11. Compared with no Arvane Interior Design Practice Act, informal activity for designers rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some sellers keep selling without a license and are not caught (p = 0.80). Reported.
- C-12. Compared with no Arvane Interior Design Practice Act, number of sellers for designers falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-13. Compared with no Arvane Interior Design Practice Act, quantity traded for designers falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-4: exchanges that no longer happen are lost to both sides. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-14. Compared with no Arvane Interior Design Practice Act, share of sellers licensed for designers rises from the short run onward (tier B, visible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-15. Compared with no Arvane Interior Design Practice Act, lobbying effort for designers.grandfathered rises from the medium run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2; EN-5: EN-5; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The license holders can organize to lobby at a cost below their stake (p = 0.80); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-16. Compared with no Arvane Interior Design Practice Act, net price received for designers.grandfathered rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-17. Compared with no Arvane Interior Design Practice Act, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70). Reported.
- C-18. Compared with no Arvane Interior Design Practice Act, quantity demanded for schools.design rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); Some current sellers or new entrants obtain the license (p = 0.85). Reported.
- C-19. Compared with no Arvane Interior Design Practice Act, resources available other uses for taxpayers or recipients.other_spending or taxpayers.future falls for at least one of them from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers; OC-1: what the payers give up is what they would otherwise have bought. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.90); The requirement is enforced often enough that many sellers comply or stop (p = 0.70); The administering agency's budget is raised to cover the new work, so taxpayers fund it (p = 0.85). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
