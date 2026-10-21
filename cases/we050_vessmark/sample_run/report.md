# Thin-slice run: Vessmark Clean Cars Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T19:14:08+00:00
Prediction log sha256 (frozen before the outcome card was opened): `6c34dc0fbf402e0d…`

## Policy record

- Rule-maker: the Vessmark legislature; enacted 30 June 2026, effective 1 January 2035.
- Stated aim: none stated
- k1: prohibition on new_combustion_cars in vessmark; binds importers, protects None. Source: "From 1 January 2035 the Registry shall not register for the first time a new passenger car fitted with an internal combustion engine."
- k2: prohibition on new_phevs in vessmark; binds importers, protects None. Source: "plug-in hybrids with at least 50 km of electric range are exempt until 31 December 2037 and banned from 1 January 2038."
- k5: lump_sum_tax on bev_ownership in vessmark; binds owners.bev, protects None. Source: "a charge of $250 a year is levied on each battery-electric passenger car from 1 January 2035, paid by its owner, collected with the annual registration renewal and paid to the general budget."
- Unclear U1: Whether a used car imported from abroad after 2035 counts as a new passenger car: 'not previously been registered' (section 2) does not say registered where. Readings: U1-a: previously registered in Vessmark: a car first registered in Vessmark after 2035 is new whatever its age, so used combustion cars imported from abroad can no longer be registered / U1-b: previously registered anywhere: a used combustion car registered in Drevland can still be imported and registered after 2035, and so can a new one registered in Drevland first
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `enforced(k1)` | enforcement | 0.95 | The legal sellers comply with the ban. |
| `demand_persists(k1)` | other | 0.85 | A meaningful share of buyers keep wanting the good after the ban. |
| `evasion(k1)` | enforcement | 0.30 | Enforcement is imperfect: many informal sales go undetected. |
| `enforcement_risk(k1)` | enforcement | 0.70 | Informal sellers face a real risk of punishment. |
| `no_other_use(k1)` | alternative_uses | 0.10 | The legal sellers cannot replace the banned good with other products for most of their business. |
| `buyer_substitutes(k1)` | substitutability | 0.80 | Legal substitutes are acceptable to some buyers. |
| `can_organize(k1)` | other | 0.85 | The former legal sellers can organize to seek repeal. |
| `buyers_organize(k1)` | other | 0.85 | The buyers have a concentrated stake and can organize for repeal. |
| `stockpile_ahead(k1)` | expectations | 0.85 | Buyers and importers can store the good and order ahead of the effective date. |
| `enforced(k2)` | enforcement | 0.95 | The legal sellers comply with the ban. |
| `demand_persists(k2)` | other | 0.60 | A meaningful share of buyers keep wanting the good after the ban. |
| `evasion(k2)` | enforcement | 0.30 | Enforcement is imperfect: many informal sales go undetected. |
| `enforcement_risk(k2)` | enforcement | 0.70 | Informal sellers face a real risk of punishment. |
| `no_other_use(k2)` | alternative_uses | 0.10 | The legal sellers cannot replace the banned good with other products for most of their business. |
| `buyer_substitutes(k2)` | substitutability | 0.85 | Legal substitutes are acceptable to some buyers. |
| `can_organize(k2)` | other | 0.85 | The former legal sellers can organize to seek repeal. |
| `buyers_organize(k2)` | other | 0.85 | The buyers have a concentrated stake and can organize for repeal. |
| `stockpile_ahead(k2)` | expectations | 0.70 | Buyers and importers can store the good and order ahead of the effective date. |
| `reshaping_pays(k1)` | other | 0.60 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.new_combustion | disputes_settled_outside_courts | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-2 | buyers.new_combustion | lobbying_effort | increase | medium+ | B | RS-7 | {buyers_organize(k1)} | yes |
| C-3 | buyers.new_combustion | price_paid | increase | short+ | B | EN-7, RS-3, CR-7 | {demand_persists(k1), enforced(k1), enforcement_risk(k1), evasion(k1)} | no |
| C-4 | buyers.new_combustion | quality_information | decrease | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-5 | buyers.new_combustion | quality_variability | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-6 | buyers.new_combustion | quantity_demanded | decrease | short+ | B | EN-7, RS-3, CR-7 | {demand_persists(k1), enforced(k1), enforcement_risk(k1), evasion(k1)} | no |
| C-7 | buyers.new_combustion | quantity_demanded [announcement window] | increase | short | B | RS-8 | {stockpile_ahead(k1)} | yes |
| C-8 | buyers.new_combustion | quantity_substitute | increase | short+ | B | RS-1 | {buyer_substitutes(k1)} | yes |
| C-9 | buyers.new_combustion | quantity_traded | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-10 | buyers.new_combustion | search_cost | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), enforced(k1), evasion(k1)} | no |
| C-11 | buyers.new_phev | disputes_settled_outside_courts | increase | short+ | B | EN-7, RS-3 | {demand_persists(k2), enforced(k2), evasion(k2)} | no |
| C-12 | buyers.new_phev | lobbying_effort | increase | medium+ | B | RS-7 | {buyers_organize(k2)} | yes |
| C-13 | buyers.new_phev | price_paid | increase | short+ | B | EN-7, RS-3, CR-7 | {demand_persists(k2), enforced(k2), enforcement_risk(k2), evasion(k2)} | no |
| C-14 | buyers.new_phev | quality_information | decrease | short+ | B | EN-7, RS-3 | {demand_persists(k2), enforced(k2), evasion(k2)} | no |
| C-15 | buyers.new_phev | quality_variability | increase | short+ | B | EN-7, RS-3 | {demand_persists(k2), enforced(k2), evasion(k2)} | no |
| C-16 | buyers.new_phev | quantity_demanded | decrease | short+ | B | EN-7, RS-3, CR-7 | {demand_persists(k2), enforced(k2), enforcement_risk(k2), evasion(k2)} | no |
| C-17 | buyers.new_phev | quantity_demanded [announcement window] | increase | short | B | RS-8 | {stockpile_ahead(k2)} | yes |
| C-18 | buyers.new_phev | quantity_substitute | increase | short+ | B | RS-1 | {buyer_substitutes(k2)} | yes |
| C-19 | buyers.new_phev | quantity_traded | decrease | short+ | B | EN-7 | {enforced(k2)} | yes |
| C-20 | buyers.new_phev | search_cost | increase | short+ | B | EN-7, RS-3 | {demand_persists(k2), enforced(k2), evasion(k2)} | no |
| C-21 | importers | asset_value | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} or {enforced(k2), no_other_use(k2)} | no |
| C-22 | importers | employment | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} or {enforced(k2), no_other_use(k2)} | no |
| C-23 | importers | lobbying_effort | increase | medium+ | B | RS-7 | {can_organize(k1)} or {can_organize(k2)} | yes |
| C-24 | importers | number_of_sellers | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} or {enforced(k2), no_other_use(k2)} | no |
| C-25 | importers | quantity_traded | decrease | short+ | B | EN-7 | {enforced(k1)} or {enforced(k2)} | yes |
| C-26 | importers.used | quantity_traded | U1-a: decrease; U1-b: none | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-27 | importers.used | reclassification | U1-a: none; U1-b: increase | short+ | B | RS-5 | {reshaping_pays(k1)} | yes |
| C-28 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |

## Explanations

- C-1. Compared with no Vessmark Clean Cars Act, disputes settled outside courts for buyers.new_combustion rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.85); The legal sellers comply with the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-2. Compared with no Vessmark Clean Cars Act, lobbying effort for buyers.new_combustion rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The buyers have a concentrated stake and can organize for repeal (p = 0.85). Reported.
- C-3. Compared with no Vessmark Clean Cars Act, price paid for buyers.new_combustion rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3; CR-7: CR-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.85); The legal sellers comply with the ban (p = 0.95); Informal sellers face a real risk of punishment (p = 0.70); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-4. Compared with no Vessmark Clean Cars Act, quality information for buyers.new_combustion falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.85); The legal sellers comply with the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-5. Compared with no Vessmark Clean Cars Act, quality variability for buyers.new_combustion rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.85); The legal sellers comply with the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-6. Compared with no Vessmark Clean Cars Act, quantity demanded for buyers.new_combustion falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3; CR-7: CR-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.85); The legal sellers comply with the ban (p = 0.95); Informal sellers face a real risk of punishment (p = 0.70); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-7. Compared with no Vessmark Clean Cars Act, quantity demanded for buyers.new_combustion rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: RS-8: a measure announced before it takes effect treats the same action differently by date, so actors move it toward the favourable window. This holds if: Buyers and importers can store the good and order ahead of the effective date (p = 0.85). Reported.
- C-8. Compared with no Vessmark Clean Cars Act, quantity substitute for buyers.new_combustion rises from the short run onward (tier B, invisible). Why: RS-1: when a good becomes dearer, buyers turn to substitutes. This holds if: Legal substitutes are acceptable to some buyers (p = 0.80). Reported.
- C-9. Compared with no Vessmark Clean Cars Act, quantity traded for buyers.new_combustion falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.95). Reported.
- C-10. Compared with no Vessmark Clean Cars Act, search cost for buyers.new_combustion rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.85); The legal sellers comply with the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-11. Compared with no Vessmark Clean Cars Act, disputes settled outside courts for buyers.new_phev rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.60); The legal sellers comply with the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-12. Compared with no Vessmark Clean Cars Act, lobbying effort for buyers.new_phev rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The buyers have a concentrated stake and can organize for repeal (p = 0.85). Reported.
- C-13. Compared with no Vessmark Clean Cars Act, price paid for buyers.new_phev rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3; CR-7: CR-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.60); The legal sellers comply with the ban (p = 0.95); Informal sellers face a real risk of punishment (p = 0.70); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-14. Compared with no Vessmark Clean Cars Act, quality information for buyers.new_phev falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.60); The legal sellers comply with the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-15. Compared with no Vessmark Clean Cars Act, quality variability for buyers.new_phev rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.60); The legal sellers comply with the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-16. Compared with no Vessmark Clean Cars Act, quantity demanded for buyers.new_phev falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3; CR-7: CR-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.60); The legal sellers comply with the ban (p = 0.95); Informal sellers face a real risk of punishment (p = 0.70); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-17. Compared with no Vessmark Clean Cars Act, quantity demanded for buyers.new_phev rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: RS-8: a measure announced before it takes effect treats the same action differently by date, so actors move it toward the favourable window. This holds if: Buyers and importers can store the good and order ahead of the effective date (p = 0.70). Reported.
- C-18. Compared with no Vessmark Clean Cars Act, quantity substitute for buyers.new_phev rises from the short run onward (tier B, invisible). Why: RS-1: when a good becomes dearer, buyers turn to substitutes. This holds if: Legal substitutes are acceptable to some buyers (p = 0.85). Reported.
- C-19. Compared with no Vessmark Clean Cars Act, quantity traded for buyers.new_phev falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.95). Reported.
- C-20. Compared with no Vessmark Clean Cars Act, search cost for buyers.new_phev rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.60); The legal sellers comply with the ban (p = 0.95); Enforcement is imperfect: many informal sales go undetected (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-21. Compared with no Vessmark Clean Cars Act, asset value for importers falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.95); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.10). It also follows under 1 other minimal assumption set(s). Not reported: an assumption is below the 0.5 cut-off.
- C-22. Compared with no Vessmark Clean Cars Act, employment for importers falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.95); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.10). It also follows under 1 other minimal assumption set(s). Not reported: an assumption is below the 0.5 cut-off.
- C-23. Compared with no Vessmark Clean Cars Act, lobbying effort for importers rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The former legal sellers can organize to seek repeal (p = 0.85). It also follows under 1 other minimal assumption set(s). Reported.
- C-24. Compared with no Vessmark Clean Cars Act, number of sellers for importers falls from the short run onward (tier B, visible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.95); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.10). It also follows under 1 other minimal assumption set(s). Not reported: an assumption is below the 0.5 cut-off.
- C-25. Compared with no Vessmark Clean Cars Act, quantity traded for importers falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.95). It also follows under 1 other minimal assumption set(s). Reported.
- C-26. Compared with no Vessmark Clean Cars Act, quantity traded for importers.used may move either way from the short run onward (tier B, invisible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.95). Sign per reading: U1-a: decrease; U1-b: none. Reported.
- C-27. Compared with no Vessmark Clean Cars Act, reclassification for importers.used may move either way from the short run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.60). Sign per reading: U1-a: none; U1-b: increase. Reported.
- C-28. Compared with no Vessmark Clean Cars Act, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
