# Thin-slice run: Corvany Personal Data Residency Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T18:54:23+00:00
Prediction log sha256 (frozen before the outcome card was opened): `1fe5739f3a7ec33a…`

## Policy record

- Rule-maker: the Corvany legislature; enacted 1 July 2027, effective 1 January 2029.
- Stated aim: none stated
- k1: prohibition on cloud_hosting_abroad in corvany; binds sellers.foreign, protects None. Source: "Residency (K1): storing or processing personal data of Corvany residents outside Corvany is prohibited for each data controller that held such data on more than 50,000 residents on any day of the preceding calendar year."
- k3: licensing_requirement on data_center_hosting in corvany; binds sellers.substitutes, protects None. Source: "Facility certificate (K3): data centers in Corvany that host covered data need a license (a certificate) for the facility, which the facility operators must hold."
- Unclear U1: Encrypted backups abroad: Section 4(2) says "A copy made solely for security may be kept outside Corvany where the Office so allows by regulation." Readings: U1-a: encrypted backup copies may be kept abroad (the provision is read as permitting security copies, with the regulation setting only conditions) / U1-b: until the Office allows it by regulation, every copy, including backups, must be in Corvany
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `enforced(k1)` | enforcement | 0.85 | The legal sellers comply with the ban. |
| `demand_persists(k1)` | other | 0.95 | A meaningful share of buyers keep wanting the good after the ban. |
| `evasion(k1)` | enforcement | 0.70 | Enforcement is imperfect: many informal sales go undetected. |
| `enforcement_risk(k1)` | enforcement | 0.30 | Informal sellers face a real risk of punishment. |
| `no_other_use(k1)` | alternative_uses | 0.20 | The legal sellers cannot replace the banned good with other products for most of their business. |
| `buyer_substitutes(k1)` | substitutability | 0.85 | Legal substitutes are acceptable to some buyers. |
| `can_organize(k1)` | other | 0.85 | The former sellers or the buyers can organize to seek repeal. |
| `reshaping_pays(k1)` | other | 0.75 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |
| `stockpile_ahead(k1)` | expectations | 0.10 | Buyers and importers can store the good and order ahead of the effective date. |
| `binding(k3)` | binding | 0.60 | The requirement goes beyond what some current or would-be sellers already meet. |
| `enforced(k3)` | enforcement | 0.85 | The requirement is enforced often enough that many sellers comply or stop. |
| `some_qualify(k3)` | alternative_uses | 0.90 | Some current sellers or new entrants obtain the license. |
| `evasion(k3)` | enforcement | 0.20 | Some sellers keep selling without a license and are not caught. |
| `buyer_substitutes(k3)` | substitutability | 0.65 | Some buyers have a feasible substitute for the licensed service. |
| `tests_valued_quality(k3)` | other | 0.40 | The license tests something buyers value but cannot easily judge. |
| `can_organize(k3)` | other | 0.85 | The license holders can organize to lobby at a cost below their stake. |
| `enforcement_budget_raised(k3)` | revenue_use | 0.90 | The administering agency's budget is raised to cover the new work, so taxpayers fund it. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | firms.covered | disputes_settled_outside_courts | increase | short+ | B | EN-1, RS-3 | {binding(k3), enforced(k3), evasion(k3)} | no |
| C-2 | firms.covered | lobbying_effort | increase | medium+ | B | RS-7 | {can_organize(k1)} | yes |
| C-3 | firms.covered | price_paid | increase | short+ | B | CR-7, EN-7, EN-1 | {demand_persists(k1), enforcement_risk(k1)} or {binding(k3), enforced(k3)} | yes |
| C-4 | firms.covered | quality_information | ambiguous | short+ | B | EN-1, EN-11, RS-3 | {binding(k3), enforced(k3), evasion(k3)} or {binding(k3), enforced(k3), tests_valued_quality(k3)} | no |
| C-5 | firms.covered | quantity_demanded | decrease | short+ | B | CR-7, EN-7 | {demand_persists(k1), enforcement_risk(k1)} | no |
| C-6 | firms.covered | quantity_demanded [announcement window] | increase | short | B | RS-8 | {stockpile_ahead(k1)} | no |
| C-7 | firms.covered | quantity_substitute | increase | short+ | B | RS-1, EN-1 | {buyer_substitutes(k1)} or {binding(k3), buyer_substitutes(k3), enforced(k3)} | yes |
| C-8 | firms.covered | quantity_traded | decrease | short+ | B | EN-7, EN-1, OC-4 | {enforced(k1)} or {binding(k3), enforced(k3)} | yes |
| C-9 | firms.covered | resources_available_other_uses | decrease | short+ | B | EN-1 | {binding(k3), enforced(k3)} | yes |
| C-10 | firms.covered | search_cost | increase | short+ | B | EN-1, RS-3 | {binding(k3), enforced(k3), evasion(k3)} | no |
| C-11 | firms.near_threshold | reclassification | increase | short+ | B | RS-5 | {reshaping_pays(k1)} | yes |
| C-12 | officials.enforcement | enforcement_cost | increase | short+ | B | OC-3, EN-1 | {} | yes |
| C-13 | sellers.foreign | asset_value | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | no |
| C-14 | sellers.foreign | employment | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | no |
| C-15 | sellers.foreign | lobbying_effort | increase | medium+ | B | RS-7 | {can_organize(k1)} | yes |
| C-16 | sellers.foreign | number_of_sellers | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-17 | sellers.foreign | quantity_traded | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-18 | sellers.foreign.online | disputes_settled_outside_courts | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-19 | sellers.foreign.online | quality_information | decrease | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-20 | sellers.foreign.online | quality_variability | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-21 | sellers.foreign.online | search_cost | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-22 | sellers.substitutes | compliance_cost | increase | short+ | B | EN-1, CR-8 | {binding(k3), enforced(k3), some_qualify(k3)} | yes |
| C-23 | sellers.substitutes | employment | decrease | short+ | B | EN-1, EN-3 | {binding(k3), enforced(k3)} | yes |
| C-24 | sellers.substitutes | entry_rate | decrease | short+ | B | EN-1 | {binding(k3), enforced(k3)} | yes |
| C-25 | sellers.substitutes | informal_activity | increase | short+ | B | EN-1, RS-3 | {binding(k3), enforced(k3), evasion(k3)} | no |
| C-26 | sellers.substitutes | lobbying_effort | increase | medium+ | B | EN-1, EN-2, EN-5, RS-7 | {binding(k3), can_organize(k3), enforced(k3)} | yes |
| C-27 | sellers.substitutes | net_price_received | increase | short+ | B | EN-1, EN-2 | {binding(k3), enforced(k3)} | yes |
| C-28 | sellers.substitutes | number_of_sellers | decrease | short+ | B | EN-1 | {binding(k3), enforced(k3)} | yes |
| C-29 | sellers.substitutes | quantity_traded | decrease | short+ | B | EN-1, OC-4 | {binding(k3), enforced(k3)} | yes |
| C-30 | sellers.substitutes | share_of_sellers_licensed | increase | short+ | B | EN-1 | {binding(k3), enforced(k3)} | yes |
| C-31 | taxpayers or recipients.other_spending or taxpayers.future | resources_available_other_uses | at_least_one_decrease | short+ | B | OC-1, EN-1, OC-3 | {} | yes |

## Explanations

- C-1. Compared with no Corvany Personal Data Residency Act, disputes settled outside courts for firms.covered rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85); Some sellers keep selling without a license and are not caught (p = 0.20). Not reported: an assumption is below the 0.5 cut-off.
- C-2. Compared with no Corvany Personal Data Residency Act, lobbying effort for firms.covered rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The former sellers or the buyers can organize to seek repeal (p = 0.85). Reported.
- C-3. Compared with no Corvany Personal Data Residency Act, price paid for firms.covered rises from the short run onward (tier B, invisible). Why: CR-7: CR-7; EN-7: EN-7; EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). It also follows under 1 other minimal assumption set(s). Reported.
- C-4. Compared with no Corvany Personal Data Residency Act, quality information for firms.covered may move either way from the short run onward (tier B, visible). Why: EN-1: EN-1; EN-11: EN-11; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85); The license tests something buyers value but cannot easily judge (p = 0.40). It also follows under 1 other minimal assumption set(s). Not reported: an assumption is below the 0.5 cut-off.
- C-5. Compared with no Corvany Personal Data Residency Act, quantity demanded for firms.covered falls from the short run onward (tier B, invisible). Why: CR-7: CR-7; EN-7: EN-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.95); Informal sellers face a real risk of punishment (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-6. Compared with no Corvany Personal Data Residency Act, quantity demanded for firms.covered rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: RS-8: a measure announced before it takes effect treats the same action differently by date, so actors move it toward the favourable window. This holds if: Buyers and importers can store the good and order ahead of the effective date (p = 0.10). Not reported: an assumption is below the 0.5 cut-off.
- C-7. Compared with no Corvany Personal Data Residency Act, quantity substitute for firms.covered rises from the short run onward (tier B, invisible). Why: RS-1: when a good becomes dearer, buyers turn to substitutes; EN-1: EN-1. This holds if: Legal substitutes are acceptable to some buyers (p = 0.85). It also follows under 1 other minimal assumption set(s). Reported.
- C-8. Compared with no Corvany Personal Data Residency Act, quantity traded for firms.covered falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; EN-1: EN-1; OC-4: exchanges that no longer happen are lost to both sides. This holds if: The legal sellers comply with the ban (p = 0.85). It also follows under 1 other minimal assumption set(s). Reported.
- C-9. Compared with no Corvany Personal Data Residency Act, resources available other uses for firms.covered falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-10. Compared with no Corvany Personal Data Residency Act, search cost for firms.covered rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85); Some sellers keep selling without a license and are not caught (p = 0.20). Not reported: an assumption is below the 0.5 cut-off.
- C-11. Compared with no Corvany Personal Data Residency Act, reclassification for firms.near_threshold rises from the short run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.75). Reported.
- C-12. Compared with no Corvany Personal Data Residency Act, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers; EN-1: EN-1. This holds if: no assumption. Reported.
- C-13. Compared with no Corvany Personal Data Residency Act, asset value for sellers.foreign falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.85); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.20). Not reported: an assumption is below the 0.5 cut-off.
- C-14. Compared with no Corvany Personal Data Residency Act, employment for sellers.foreign falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.85); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.20). Not reported: an assumption is below the 0.5 cut-off.
- C-15. Compared with no Corvany Personal Data Residency Act, lobbying effort for sellers.foreign rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The former sellers or the buyers can organize to seek repeal (p = 0.85). Reported.
- C-16. Compared with no Corvany Personal Data Residency Act, number of sellers for sellers.foreign falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.85). Reported.
- C-17. Compared with no Corvany Personal Data Residency Act, quantity traded for sellers.foreign falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.85). Reported.
- C-18. Compared with no Corvany Personal Data Residency Act, disputes settled outside courts for sellers.foreign.online rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.70). Reported.
- C-19. Compared with no Corvany Personal Data Residency Act, quality information for sellers.foreign.online falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.70). Reported.
- C-20. Compared with no Corvany Personal Data Residency Act, quality variability for sellers.foreign.online rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.70). Reported.
- C-21. Compared with no Corvany Personal Data Residency Act, search cost for sellers.foreign.online rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.70). Reported.
- C-22. Compared with no Corvany Personal Data Residency Act, compliance cost for sellers.substitutes rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85); Some current sellers or new entrants obtain the license (p = 0.90). Reported.
- C-23. Compared with no Corvany Personal Data Residency Act, employment for sellers.substitutes falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; EN-3: EN-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-24. Compared with no Corvany Personal Data Residency Act, entry rate for sellers.substitutes falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-25. Compared with no Corvany Personal Data Residency Act, informal activity for sellers.substitutes rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85); Some sellers keep selling without a license and are not caught (p = 0.20). Not reported: an assumption is below the 0.5 cut-off.
- C-26. Compared with no Corvany Personal Data Residency Act, lobbying effort for sellers.substitutes rises from the medium run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2; EN-5: EN-5; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The license holders can organize to lobby at a cost below their stake (p = 0.85); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-27. Compared with no Corvany Personal Data Residency Act, net price received for sellers.substitutes rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-28. Compared with no Corvany Personal Data Residency Act, number of sellers for sellers.substitutes falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-29. Compared with no Corvany Personal Data Residency Act, quantity traded for sellers.substitutes falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-4: exchanges that no longer happen are lost to both sides. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-30. Compared with no Corvany Personal Data Residency Act, share of sellers licensed for sellers.substitutes rises from the short run onward (tier B, visible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-31. Compared with no Corvany Personal Data Residency Act, resources available other uses for taxpayers or recipients.other_spending or taxpayers.future falls for at least one of them from the short run onward (tier B, invisible). Why: OC-1: what the payers give up is what they would otherwise have bought; EN-1: EN-1; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
