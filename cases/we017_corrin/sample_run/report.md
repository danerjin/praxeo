# Thin-slice run: Corrin Lirva Control Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T18:49:52+00:00
Prediction log sha256 (frozen before the outcome card was opened): `23f7e174de738265…`

## Policy record

- Rule-maker: the Corrin legislature; enacted six months before the effective date, effective the effective date.
- Stated aim: none stated
- k1: prohibition on lirva in corrin; binds shops.lirva, protects None. Source: "From the effective date, making, selling, possessing for sale, importing and growing lirva, its active compound lirvine, and any product containing either are prohibited, except for licensed research."
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `enforced(k1)` | enforcement | 0.95 | The legal sellers comply with the ban. |
| `demand_persists(k1)` | other | 0.90 | A meaningful share of buyers keep wanting the good after the ban. |
| `evasion(k1)` | enforcement | 0.85 | Enforcement is imperfect: many informal sales go undetected. |
| `enforcement_risk(k1)` | enforcement | 0.80 | Informal sellers face a real risk of punishment. |
| `no_other_use(k1)` | alternative_uses | 0.85 | The legal sellers cannot replace the banned good with other products for most of their business. |
| `buyer_substitutes(k1)` | substitutability | 0.80 | Legal substitutes are acceptable to some buyers. |
| `can_organize(k1)` | other | 0.60 | The former sellers or the buyers can organize to seek repeal. |
| `cross_border_feasible(k1)` | mobility | 0.65 | Enough buyers can easily buy across the boundary, where the tax does not apply. |
| `reshaping_pays(k1)` | other | 0.60 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |
| `stockpile_ahead(k1)` | expectations | 0.75 | Buyers and importers can store the good and order ahead of the effective date. |
| `concentrate_easy(k1)` | other | 0.75 | A concentrated form can be made with simple means. |
| `records_checked(k1)` | other | 0.60 | Convictions are recorded and checked by employers. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | halvet.sellers | quantity_traded | increase | short+ | B | RS-4 | {cross_border_feasible(k1)} | yes |
| C-2 | importers.lirva | quantity_traded | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-3 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |
| C-4 | officials.enforcement | tax_revenue | decrease | short+ | B | EN-7, TX-10 | {enforced(k1)} | yes |
| C-5 | sellers.informal | disputes_settled_outside_courts | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-6 | sellers.informal | informal_activity | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-7 | sellers.informal | reclassification | increase | short+ | B | RS-5 | {reshaping_pays(k1)} | yes |
| C-8 | sellers.informal | share_concentrated_forms | increase | medium+ | B | EN-7, RS-3, EN-8 | {concentrate_easy(k1), demand_persists(k1), evasion(k1)} | yes |
| C-9 | sellers.substitutes | reclassification | increase | short+ | B | RS-5 | {reshaping_pays(k1)} | yes |
| C-10 | shops.lirva | asset_value | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | yes |
| C-11 | shops.lirva | employment | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | yes |
| C-12 | shops.lirva | inventory_held | decrease | short+ | B | EN-7, RS-8 | {enforced(k1)} | yes |
| C-13 | shops.lirva | lobbying_effort | increase | medium+ | B | RS-7 | {can_organize(k1)} | yes |
| C-14 | shops.lirva | number_of_sellers | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-15 | shops.lirva | quantity_traded | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-16 | shops.lirva | resources_available_other_uses | decrease | short+ | A | OC-1 | {} | yes |
| C-17 | taxpayers or recipients.other_spending or taxpayers.future | resources_available_other_uses | at_least_one_decrease | short+ | A | OC-1 | {} | yes |
| C-18 | users.convicted | employment | decrease | long | B | CR-7, EN-7, EN-10 | {demand_persists(k1), enforcement_risk(k1), records_checked(k1)} | yes |
| C-19 | users.current | lobbying_effort | increase | medium+ | B | RS-7 | {can_organize(k1)} | yes |
| C-20 | users.current | price_paid | increase | short+ | B | CR-7, EN-7 | {demand_persists(k1), enforcement_risk(k1)} | yes |
| C-21 | users.current | quantity_demanded | decrease | short+ | B | CR-7, EN-7 | {demand_persists(k1), enforcement_risk(k1)} | yes |
| C-22 | users.current | quantity_demanded [announcement window] | increase | short | B | RS-8 | {stockpile_ahead(k1)} | yes |
| C-23 | users.current | quantity_substitute | increase | short+ | B | RS-1 | {buyer_substitutes(k1)} | yes |
| C-24 | users.current | quantity_traded | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-25 | users.informal | disputes_settled_outside_courts | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-26 | users.informal | quality_information | decrease | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-27 | users.informal | quality_variability | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-28 | users.informal | search_cost | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-29 | users.mobile | cross_border_purchases | increase | short+ | B | RS-4 | {cross_border_feasible(k1)} | yes |
| C-30 | users.mobile | search_cost | increase | short+ | B | RS-4 | {cross_border_feasible(k1)} | yes |
| C-31 | users.prospective | quantity_demanded | decrease | long | B | CR-7, EN-7 | {demand_persists(k1), enforcement_risk(k1)} | yes |

## Explanations

- C-1. Compared with no Corrin Lirva Control Act, quantity traded for halvet.sellers rises from the short run onward (tier B, invisible). Why: RS-4: shut-out buyers turn to uncovered units, which are close substitutes. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.65). Reported.
- C-2. Compared with no Corrin Lirva Control Act, quantity traded for importers.lirva falls from the short run onward (tier B, invisible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.95). Reported.
- C-3. Compared with no Corrin Lirva Control Act, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-4. Compared with no Corrin Lirva Control Act, tax revenue for officials.enforcement falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; TX-10: TX-10. This holds if: The legal sellers comply with the ban (p = 0.95). Reported.
- C-5. Compared with no Corrin Lirva Control Act, disputes settled outside courts for sellers.informal rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.85). Reported.
- C-6. Compared with no Corrin Lirva Control Act, informal activity for sellers.informal rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.85). Reported.
- C-7. Compared with no Corrin Lirva Control Act, reclassification for sellers.informal rises from the short run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.60). Reported.
- C-8. Compared with no Corrin Lirva Control Act, share concentrated forms for sellers.informal rises from the medium run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3; EN-8: EN-8. This holds if: A concentrated form can be made with simple means (p = 0.75); A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.85). Reported.
- C-9. Compared with no Corrin Lirva Control Act, reclassification for sellers.substitutes rises from the short run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.60). Reported.
- C-10. Compared with no Corrin Lirva Control Act, asset value for shops.lirva falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.95); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.85). Reported.
- C-11. Compared with no Corrin Lirva Control Act, employment for shops.lirva falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.95); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.85). Reported.
- C-12. Compared with no Corrin Lirva Control Act, inventory held for shops.lirva falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-8: a measure announced before it takes effect treats the same action differently by date, so actors move it toward the favourable window. This holds if: The legal sellers comply with the ban (p = 0.95). Reported.
- C-13. Compared with no Corrin Lirva Control Act, lobbying effort for shops.lirva rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The former sellers or the buyers can organize to seek repeal (p = 0.60). Reported.
- C-14. Compared with no Corrin Lirva Control Act, number of sellers for shops.lirva falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.95). Reported.
- C-15. Compared with no Corrin Lirva Control Act, quantity traded for shops.lirva falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.95). Reported.
- C-16. Compared with no Corrin Lirva Control Act, resources available other uses for shops.lirva falls from the short run onward (tier A, invisible). Why: OC-1: what the payers give up is what they would otherwise have bought. This holds if: no assumption. Reported.
- C-17. Compared with no Corrin Lirva Control Act, resources available other uses for taxpayers or recipients.other_spending or taxpayers.future falls for at least one of them from the short run onward (tier A, invisible). Why: OC-1: what the payers give up is what they would otherwise have bought. This holds if: no assumption. Reported.
- C-18. Compared with no Corrin Lirva Control Act, employment for users.convicted falls in the long run (tier B, invisible). Why: CR-7: CR-7; EN-7: EN-7; EN-10: EN-10. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Informal sellers face a real risk of punishment (p = 0.80); Convictions are recorded and checked by employers (p = 0.60). Reported.
- C-19. Compared with no Corrin Lirva Control Act, lobbying effort for users.current rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The former sellers or the buyers can organize to seek repeal (p = 0.60). Reported.
- C-20. Compared with no Corrin Lirva Control Act, price paid for users.current rises from the short run onward (tier B, invisible). Why: CR-7: CR-7; EN-7: EN-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Informal sellers face a real risk of punishment (p = 0.80). Reported.
- C-21. Compared with no Corrin Lirva Control Act, quantity demanded for users.current falls from the short run onward (tier B, invisible). Why: CR-7: CR-7; EN-7: EN-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Informal sellers face a real risk of punishment (p = 0.80). Reported.
- C-22. Compared with no Corrin Lirva Control Act, quantity demanded for users.current rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: RS-8: a measure announced before it takes effect treats the same action differently by date, so actors move it toward the favourable window. This holds if: Buyers and importers can store the good and order ahead of the effective date (p = 0.75). Reported.
- C-23. Compared with no Corrin Lirva Control Act, quantity substitute for users.current rises from the short run onward (tier B, invisible). Why: RS-1: when a good becomes dearer, buyers turn to substitutes. This holds if: Legal substitutes are acceptable to some buyers (p = 0.80). Reported.
- C-24. Compared with no Corrin Lirva Control Act, quantity traded for users.current falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.95). Reported.
- C-25. Compared with no Corrin Lirva Control Act, disputes settled outside courts for users.informal rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.85). Reported.
- C-26. Compared with no Corrin Lirva Control Act, quality information for users.informal falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.85). Reported.
- C-27. Compared with no Corrin Lirva Control Act, quality variability for users.informal rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.85). Reported.
- C-28. Compared with no Corrin Lirva Control Act, search cost for users.informal rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Enforcement is imperfect: many informal sales go undetected (p = 0.85). Reported.
- C-29. Compared with no Corrin Lirva Control Act, cross border purchases for users.mobile rises from the short run onward (tier B, invisible). Why: RS-4: shut-out buyers turn to uncovered units, which are close substitutes. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.65). Reported.
- C-30. Compared with no Corrin Lirva Control Act, search cost for users.mobile rises from the short run onward (tier B, invisible). Why: RS-4: shut-out buyers turn to uncovered units, which are close substitutes. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.65). Reported.
- C-31. Compared with no Corrin Lirva Control Act, quantity demanded for users.prospective falls in the long run (tier B, invisible). Why: CR-7: CR-7; EN-7: EN-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.90); Informal sellers face a real risk of punishment (p = 0.80). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
