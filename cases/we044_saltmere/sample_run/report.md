# Thin-slice run: Saltmere Housing Preservation Ordinance

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T18:54:11+00:00
Prediction log sha256 (frozen before the outcome card was opened): `b7587ad236e66485…`

## Policy record

- Rule-maker: the Saltmere city council; enacted 8 December 2026 (introduced 3 November 2026), effective 1 July 2027.
- Stated aim: none stated
- k1: prohibition on whole_unit_short_term_rentals in saltmere; binds hosts.non_primary, protects None. Source: "From 1 July 2027, no whole unit may be let for under 30 nights unless it is the owner's primary residence, registered under the registry, and then for no more than 90 nights in a calendar year (45 nights for July to December 2027)."
- k2: disclosure_mandate on whole_unit_short_term_rentals in saltmere; binds platforms, protects None. Source: "From 1 July 2027, booking platforms must display a valid registration number on every whole-unit listing, remove a listing within 10 days of a city notice that it is non-compliant, and report nights booked per registration number each quarter."
- k3: licensing_requirement on primary_residence_short_term_lets in saltmere; binds hosts.primary, protects None. Source: "Owners who let their primary residence must register for $250 a year, with proof of residence (driver's license, voter registration, homestead tax exemption)."
- Unclear U1: Whether the primary-residence exception covers the second unit of a two-unit building whose owner lives in the other unit. Readings: U1-a: the dwelling is the building, so the second unit is part of the primary residence and may be let up to 90 nights a year / U1-b: the dwelling is the unit, so the second unit may not be let for under 30 nights at all
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `enforced(k1)` | enforcement | 0.85 | The legal sellers comply with the ban. |
| `demand_persists(k1)` | other | 0.70 | A meaningful share of buyers keep wanting the good after the ban. |
| `evasion(k1)` | enforcement | 0.75 | Enforcement is imperfect: many informal sales go undetected. |
| `enforcement_risk(k1)` | enforcement | 0.80 | Informal sellers face a real risk of punishment. |
| `no_other_use(k1)` | alternative_uses | 0.15 | The legal sellers cannot replace the banned good with other products for most of their business. |
| `buyer_substitutes(k1)` | substitutability | 0.80 | Legal substitutes are acceptable to some buyers. |
| `can_organize(k1)` | other | 0.85 | The former sellers or the buyers can organize to seek repeal. |
| `cross_border_feasible(k1)` | mobility | 0.70 | Enough buyers can easily buy across the boundary, where the tax does not apply. |
| `reshaping_pays(k1)` | other | 0.60 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |
| `stockpile_ahead(k1)` | expectations | 0.70 | Buyers and importers can store the good and order ahead of the effective date. |
| `binding(k3)` | binding | 0.60 | The requirement goes beyond what some current or would-be sellers already meet. |
| `enforced(k3)` | enforcement | 0.85 | The requirement is enforced often enough that many sellers comply or stop. |
| `some_qualify(k3)` | alternative_uses | 0.90 | Some current sellers or new entrants obtain the license. |
| `evasion(k3)` | enforcement | 0.60 | Some sellers keep selling without a license and are not caught. |
| `buyer_substitutes(k3)` | substitutability | 0.80 | Some buyers have a feasible substitute for the licensed service. |
| `tests_valued_quality(k3)` | other | 0.15 | The license tests something buyers value but cannot easily judge. |
| `can_organize(k3)` | other | 0.85 | The license holders can organize to lobby at a cost below their stake. |
| `enforcement_budget_raised(k3)` | revenue_use | 0.90 | The administering agency's budget is raised to cover the new work, so taxpayers fund it. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | guests.off_platform | disputes_settled_outside_courts | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-2 | guests.off_platform | quality_information | decrease | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-3 | guests.off_platform | quality_variability | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-4 | guests.off_platform | search_cost | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-5 | guests.whole_unit | cross_border_purchases | increase | short+ | B | RS-4 | {cross_border_feasible(k1)} | yes |
| C-6 | guests.whole_unit | disputes_settled_outside_courts | increase | short+ | B | EN-1, RS-3 | {binding(k3), enforced(k3), evasion(k3)} | yes |
| C-7 | guests.whole_unit | lobbying_effort | increase | medium+ | B | RS-7 | {can_organize(k1)} | yes |
| C-8 | guests.whole_unit | price_paid | increase | short+ | B | CR-7, EN-7, EN-1 | {binding(k3), enforced(k3)} or {demand_persists(k1), enforcement_risk(k1)} | yes |
| C-9 | guests.whole_unit | quality_information | decrease | short+ | B | EN-1, RS-3 | {binding(k3), enforced(k3), evasion(k3)} | yes |
| C-10 | guests.whole_unit | quantity_demanded | decrease | short+ | B | CR-7, EN-7 | {demand_persists(k1), enforcement_risk(k1)} | yes |
| C-11 | guests.whole_unit | quantity_demanded [announcement window] | increase | short | B | RS-8 | {stockpile_ahead(k1)} | yes |
| C-12 | guests.whole_unit | quantity_substitute | increase | short+ | B | RS-1, EN-1 | {buyer_substitutes(k1)} or {binding(k3), buyer_substitutes(k3), enforced(k3)} | yes |
| C-13 | guests.whole_unit | quantity_traded | decrease | short+ | B | EN-7, EN-1, OC-4 | {enforced(k1)} or {binding(k3), enforced(k3)} | yes |
| C-14 | guests.whole_unit | resources_available_other_uses | decrease | short+ | B | EN-1 | {binding(k3), enforced(k3)} | yes |
| C-15 | guests.whole_unit | search_cost | increase | short+ | B | RS-4, EN-1, RS-3 | {cross_border_feasible(k1)} or {binding(k3), enforced(k3), evasion(k3)} | yes |
| C-16 | hosts.in_breach | disputes_settled_outside_courts | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-17 | hosts.in_breach | informal_activity | increase | short+ | B | EN-7, RS-3 | {demand_persists(k1), evasion(k1)} | yes |
| C-18 | hosts.in_breach | reclassification | increase | short+ | B | RS-5 | {reshaping_pays(k1)} | yes |
| C-19 | hosts.mid_term | reclassification | increase | short+ | B | RS-5 | {reshaping_pays(k1)} | yes |
| C-20 | hosts.non_primary | asset_value | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | no |
| C-21 | hosts.non_primary | employment | decrease | short+ | B | EN-7, CR-1, SB-4 | {enforced(k1), no_other_use(k1)} | no |
| C-22 | hosts.non_primary | lobbying_effort | increase | medium+ | B | RS-7 | {can_organize(k1)} | yes |
| C-23 | hosts.non_primary | number_of_sellers | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-24 | hosts.non_primary | quantity_traded | decrease | short+ | B | EN-7 | {enforced(k1)} | yes |
| C-25 | hosts.primary | compliance_cost | increase | short+ | B | EN-1, CR-8 | {binding(k3), enforced(k3), some_qualify(k3)} | yes |
| C-26 | hosts.primary | employment | decrease | short+ | B | EN-1, EN-3 | {binding(k3), enforced(k3)} | yes |
| C-27 | hosts.primary | entry_rate | decrease | short+ | B | EN-1 | {binding(k3), enforced(k3)} | yes |
| C-28 | hosts.primary | informal_activity | increase | short+ | B | EN-1, RS-3 | {binding(k3), enforced(k3), evasion(k3)} | yes |
| C-29 | hosts.primary | lobbying_effort | increase | medium+ | B | EN-1, EN-2, EN-5, RS-7 | {binding(k3), can_organize(k3), enforced(k3)} | yes |
| C-30 | hosts.primary | net_price_received | increase | short+ | B | EN-1, EN-2 | {binding(k3), enforced(k3)} | yes |
| C-31 | hosts.primary | number_of_sellers | decrease | short+ | B | EN-1 | {binding(k3), enforced(k3)} | yes |
| C-32 | hosts.primary | quantity_traded | decrease | short+ | B | EN-1, OC-4 | {binding(k3), enforced(k3)} | yes |
| C-33 | hosts.primary | share_of_sellers_licensed | increase | short+ | B | EN-1 | {binding(k3), enforced(k3)} | yes |
| C-34 | neighboring_jurisdictions | quantity_traded | increase | short+ | B | RS-4 | {cross_border_feasible(k1)} | yes |
| C-35 | officials.enforcement | enforcement_cost | increase | short+ | B | OC-3, EN-1 | {} | yes |
| C-36 | officials.revenue | tax_revenue | decrease | short+ | B | EN-7, TX-10 | {enforced(k1)} | yes |
| C-37 | taxpayers or recipients.other_spending or taxpayers.future | resources_available_other_uses | at_least_one_decrease | short+ | B | OC-1, EN-1, OC-3 | {} | yes |

## Explanations

- C-1. Compared with no Saltmere Housing Preservation Ordinance, disputes settled outside courts for guests.off_platform rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); Enforcement is imperfect: many informal sales go undetected (p = 0.75). Reported.
- C-2. Compared with no Saltmere Housing Preservation Ordinance, quality information for guests.off_platform falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); Enforcement is imperfect: many informal sales go undetected (p = 0.75). Reported.
- C-3. Compared with no Saltmere Housing Preservation Ordinance, quality variability for guests.off_platform rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); Enforcement is imperfect: many informal sales go undetected (p = 0.75). Reported.
- C-4. Compared with no Saltmere Housing Preservation Ordinance, search cost for guests.off_platform rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); Enforcement is imperfect: many informal sales go undetected (p = 0.75). Reported.
- C-5. Compared with no Saltmere Housing Preservation Ordinance, cross border purchases for guests.whole_unit rises from the short run onward (tier B, invisible). Why: RS-4: shut-out buyers turn to uncovered units, which are close substitutes. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.70). Reported.
- C-6. Compared with no Saltmere Housing Preservation Ordinance, disputes settled outside courts for guests.whole_unit rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85); Some sellers keep selling without a license and are not caught (p = 0.60). Reported.
- C-7. Compared with no Saltmere Housing Preservation Ordinance, lobbying effort for guests.whole_unit rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The former sellers or the buyers can organize to seek repeal (p = 0.85). Reported.
- C-8. Compared with no Saltmere Housing Preservation Ordinance, price paid for guests.whole_unit rises from the short run onward (tier B, invisible). Why: CR-7: CR-7; EN-7: EN-7; EN-1: EN-1. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); Informal sellers face a real risk of punishment (p = 0.80). It also follows under 1 other minimal assumption set(s). Reported.
- C-9. Compared with no Saltmere Housing Preservation Ordinance, quality information for guests.whole_unit falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85); Some sellers keep selling without a license and are not caught (p = 0.60). Reported.
- C-10. Compared with no Saltmere Housing Preservation Ordinance, quantity demanded for guests.whole_unit falls from the short run onward (tier B, invisible). Why: CR-7: CR-7; EN-7: EN-7. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); Informal sellers face a real risk of punishment (p = 0.80). Reported.
- C-11. Compared with no Saltmere Housing Preservation Ordinance, quantity demanded for guests.whole_unit rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: RS-8: a measure announced before it takes effect treats the same action differently by date, so actors move it toward the favourable window. This holds if: Buyers and importers can store the good and order ahead of the effective date (p = 0.70). Reported.
- C-12. Compared with no Saltmere Housing Preservation Ordinance, quantity substitute for guests.whole_unit rises from the short run onward (tier B, invisible). Why: RS-1: when a good becomes dearer, buyers turn to substitutes; EN-1: EN-1. This holds if: Legal substitutes are acceptable to some buyers (p = 0.80). It also follows under 1 other minimal assumption set(s). Reported.
- C-13. Compared with no Saltmere Housing Preservation Ordinance, quantity traded for guests.whole_unit falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; EN-1: EN-1; OC-4: exchanges that no longer happen are lost to both sides. This holds if: The legal sellers comply with the ban (p = 0.85). It also follows under 1 other minimal assumption set(s). Reported.
- C-14. Compared with no Saltmere Housing Preservation Ordinance, resources available other uses for guests.whole_unit falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-15. Compared with no Saltmere Housing Preservation Ordinance, search cost for guests.whole_unit rises from the short run onward (tier B, invisible). Why: RS-4: shut-out buyers turn to uncovered units, which are close substitutes; EN-1: EN-1; RS-3: RS-3. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.70). It also follows under 1 other minimal assumption set(s). Reported.
- C-16. Compared with no Saltmere Housing Preservation Ordinance, disputes settled outside courts for hosts.in_breach rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); Enforcement is imperfect: many informal sales go undetected (p = 0.75). Reported.
- C-17. Compared with no Saltmere Housing Preservation Ordinance, informal activity for hosts.in_breach rises from the short run onward (tier B, invisible). Why: EN-7: EN-7; RS-3: RS-3. This holds if: A meaningful share of buyers keep wanting the good after the ban (p = 0.70); Enforcement is imperfect: many informal sales go undetected (p = 0.75). Reported.
- C-18. Compared with no Saltmere Housing Preservation Ordinance, reclassification for hosts.in_breach rises from the short run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.60). Reported.
- C-19. Compared with no Saltmere Housing Preservation Ordinance, reclassification for hosts.mid_term rises from the short run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.60). Reported.
- C-20. Compared with no Saltmere Housing Preservation Ordinance, asset value for hosts.non_primary falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.85); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-21. Compared with no Saltmere Housing Preservation Ordinance, employment for hosts.non_primary falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; CR-1: CR-1; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The legal sellers comply with the ban (p = 0.85); The legal sellers cannot replace the banned good with other products for most of their business (p = 0.15). Not reported: an assumption is below the 0.5 cut-off.
- C-22. Compared with no Saltmere Housing Preservation Ordinance, lobbying effort for hosts.non_primary rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The former sellers or the buyers can organize to seek repeal (p = 0.85). Reported.
- C-23. Compared with no Saltmere Housing Preservation Ordinance, number of sellers for hosts.non_primary falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.85). Reported.
- C-24. Compared with no Saltmere Housing Preservation Ordinance, quantity traded for hosts.non_primary falls from the short run onward (tier B, visible). Why: EN-7: EN-7. This holds if: The legal sellers comply with the ban (p = 0.85). Reported.
- C-25. Compared with no Saltmere Housing Preservation Ordinance, compliance cost for hosts.primary rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85); Some current sellers or new entrants obtain the license (p = 0.90). Reported.
- C-26. Compared with no Saltmere Housing Preservation Ordinance, employment for hosts.primary falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; EN-3: EN-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-27. Compared with no Saltmere Housing Preservation Ordinance, entry rate for hosts.primary falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-28. Compared with no Saltmere Housing Preservation Ordinance, informal activity for hosts.primary rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; RS-3: RS-3. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85); Some sellers keep selling without a license and are not caught (p = 0.60). Reported.
- C-29. Compared with no Saltmere Housing Preservation Ordinance, lobbying effort for hosts.primary rises from the medium run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2; EN-5: EN-5; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The license holders can organize to lobby at a cost below their stake (p = 0.85); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-30. Compared with no Saltmere Housing Preservation Ordinance, net price received for hosts.primary rises from the short run onward (tier B, invisible). Why: EN-1: EN-1; EN-2: EN-2. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-31. Compared with no Saltmere Housing Preservation Ordinance, number of sellers for hosts.primary falls from the short run onward (tier B, invisible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-32. Compared with no Saltmere Housing Preservation Ordinance, quantity traded for hosts.primary falls from the short run onward (tier B, invisible). Why: EN-1: EN-1; OC-4: exchanges that no longer happen are lost to both sides. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-33. Compared with no Saltmere Housing Preservation Ordinance, share of sellers licensed for hosts.primary rises from the short run onward (tier B, visible). Why: EN-1: EN-1. This holds if: The requirement goes beyond what some current or would-be sellers already meet (p = 0.60); The requirement is enforced often enough that many sellers comply or stop (p = 0.85). Reported.
- C-34. Compared with no Saltmere Housing Preservation Ordinance, quantity traded for neighboring_jurisdictions rises from the short run onward (tier B, invisible). Why: RS-4: shut-out buyers turn to uncovered units, which are close substitutes. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.70). Reported.
- C-35. Compared with no Saltmere Housing Preservation Ordinance, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers; EN-1: EN-1. This holds if: no assumption. Reported.
- C-36. Compared with no Saltmere Housing Preservation Ordinance, tax revenue for officials.revenue falls from the short run onward (tier B, invisible). Why: EN-7: EN-7; TX-10: TX-10. This holds if: The legal sellers comply with the ban (p = 0.85). Reported.
- C-37. Compared with no Saltmere Housing Preservation Ordinance, resources available other uses for taxpayers or recipients.other_spending or taxpayers.future falls for at least one of them from the short run onward (tier B, invisible). Why: OC-1: what the payers give up is what they would otherwise have bought; EN-1: EN-1; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
