# Thin-slice run: Kallmark Ridge Cod Fishery Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T05:43:54+00:00
Prediction log sha256 (frozen before the outcome card was opened): `b703a0e2c79845fd…`

## Policy record

- Rule-maker: the Kallmark government and legislature; enacted 14 October 2026, effective 1 January 2028.
- Stated aim: none stated
- k1: quota on ridge_cod in kallmark; binds vessel_owners.history, protects None. Source: "The Act sets a total allowable catch of ridge cod of 40,000 tonnes a year for 2028 to 2032, binding vessel owners."
- k2: rights_allocation on ridge_cod_quota_shares in kallmark; binds vessel_owners.history, protects share_recipients. Source: "The catch is divided into one million shares."
- k3: term_prohibition on crew_share_agreement in kallmark; binds vessel_owners.history, protects crew. Source: "The Act says: "The cost of acquiring quota shall not be deducted as a trip expense in crew settlements.""
- Unclear U1: Whether "the cost of acquiring quota" in K3 covers leasing a year's tonnage, or only buying shares. Readings: U1-a: only purchases are covered, so lease payments may be deducted before the crew share / U1-b: leases are covered too, so the owner pays them from the owner's side
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.90 | The cap holds the quantity below what would otherwise be traded. |
| `enforced(k1)` | enforcement | 0.80 | The cap is enforced. |
| `evasion(k1)` | enforcement | 0.55 | Some trade takes place beyond the cap without being caught. |
| `can_organize(k1)` | other | 0.85 | The holders of the rights can organize to lobby at a cost below their stake. |
| `expected_to_last(k1)` | expectations | 0.70 | Holders and buyers of the rights expect the restriction to last. |
| `values_differ(k1)` | other | 0.80 | Holders' costs or values differ. |
| `trade_cheap(k1)` | mobility | 0.80 | Rights can be sold or leased at low cost. |
| `allocation_known(k1)` | expectations | 0.80 | Actors know the allocation rule during the base period. |
| `price_effect_material(k1)` | other | 0.60 | The capped quantity matters enough in the wider market to raise the price there. |
| `enforcement_budget_raised(k1)` | revenue_use | 0.90 | The administering agency's budget is raised to cover the new work, so taxpayers fund it. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.fresh_domestic | disputes_settled_outside_courts | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-2 | buyers.fresh_domestic | quality_information | decrease | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-3 | buyers.fresh_domestic | search_cost | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-4 | buyers.regional | price_paid | increase | short+ | B | EN-6 | {binding(k1), enforced(k1), price_effect_material(k1)} | yes |
| C-5 | buyers.regional | quantity_traded | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-6 | buyers.regional | resources_available_other_uses | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1), price_effect_material(k1)} | yes |
| C-7 | crew | employment or hours_worked | at_least_one_decrease | medium+ | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-8 | crew | employment or hours_worked [announcement window] | at_least_one_increase | short | B | CR-10, EN-12 | {allocation_known(k1)} | yes |
| C-9 | entrants.prospective | entry_rate [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k1)} | yes |
| C-10 | officials.enforcement | enforcement_cost | increase | short+ | B | EN-6, OC-3 | {binding(k1), enforced(k1)} | yes |
| C-11 | ports.minor | quantity_traded | decrease | medium+ | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-12 | share_recipients | asset_value | increase | short+ | B | EN-6, SB-4 | {binding(k1), enforced(k1), expected_to_last(k1)} | yes |
| C-13 | share_recipients | lobbying_effort | increase | medium+ | B | EN-6, RS-7 | {binding(k1), can_organize(k1), enforced(k1)} | yes |
| C-14 | share_recipients | right_lease_price | increase | short+ | B | EN-6, EN-13, CR-6 | {binding(k1), enforced(k1)} | yes |
| C-15 | taxpayers or recipients.other_spending | resources_available_other_uses | at_least_one_decrease | short+ | B | EN-6, OC-3, OC-1 | {binding(k1), enforced(k1), enforcement_budget_raised(k1)} | yes |
| C-16 | vessel_owners.history | asset_value [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k1)} | yes |
| C-17 | vessel_owners.history | capital_stock_target | decrease | long | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-18 | vessel_owners.history | informal_activity | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-19 | vessel_owners.history | investment_target [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k1)} | yes |
| C-20 | vessel_owners.history | number_of_sellers | decrease | medium+ | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-21 | vessel_owners.history | quantity_supplied | increase | medium+ | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-22 | vessel_owners.history | quantity_traded | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-23 | vessel_owners.history | quantity_traded [announcement window] | increase | short | B | CR-10, EN-12 | {allocation_known(k1)} | yes |
| C-24 | vessel_owners.history | resources_available_other_uses [announcement window] | decrease | short | B | CR-10, EN-12 | {allocation_known(k1)} | yes |

## Explanations

- C-1. Compared with no Kallmark Ridge Cod Fishery Act, disputes settled outside courts for buyers.fresh_domestic rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-2. Compared with no Kallmark Ridge Cod Fishery Act, quality information for buyers.fresh_domestic falls from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-3. Compared with no Kallmark Ridge Cod Fishery Act, search cost for buyers.fresh_domestic rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-4. Compared with no Kallmark Ridge Cod Fishery Act, price paid for buyers.regional rises from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); The capped quantity matters enough in the wider market to raise the price there (p = 0.60). Reported.
- C-5. Compared with no Kallmark Ridge Cod Fishery Act, quantity traded for buyers.regional falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80). Reported.
- C-6. Compared with no Kallmark Ridge Cod Fishery Act, resources available other uses for buyers.regional falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); The capped quantity matters enough in the wider market to raise the price there (p = 0.60). Reported.
- C-7. Compared with no Kallmark Ridge Cod Fishery Act, employment or hours worked for crew falls for at least one of them from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); Rights can be sold or leased at low cost (p = 0.80); Holders' costs or values differ (p = 0.80). Reported.
- C-8. Compared with no Kallmark Ridge Cod Fishery Act, employment or hours worked for crew rises for at least one of them in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-9. Compared with no Kallmark Ridge Cod Fishery Act, entry rate for entrants.prospective rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-10. Compared with no Kallmark Ridge Cod Fishery Act, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80). Reported.
- C-11. Compared with no Kallmark Ridge Cod Fishery Act, quantity traded for ports.minor falls from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); Rights can be sold or leased at low cost (p = 0.80); Holders' costs or values differ (p = 0.80). Reported.
- C-12. Compared with no Kallmark Ridge Cod Fishery Act, asset value for share_recipients rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); Holders and buyers of the rights expect the restriction to last (p = 0.70). Reported.
- C-13. Compared with no Kallmark Ridge Cod Fishery Act, lobbying effort for share_recipients rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The holders of the rights can organize to lobby at a cost below their stake (p = 0.85); The cap is enforced (p = 0.80). Reported.
- C-14. Compared with no Kallmark Ridge Cod Fishery Act, right lease price for share_recipients rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13; CR-6: sellers facing fewer buyers than they planned for cut their price. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80). Reported.
- C-15. Compared with no Kallmark Ridge Cod Fishery Act, resources available other uses for taxpayers or recipients.other_spending falls for at least one of them from the short run onward (tier B, invisible). Why: EN-6: EN-6; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers; OC-1: what the payers give up is what they would otherwise have bought. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); The administering agency's budget is raised to cover the new work, so taxpayers fund it (p = 0.90). Reported.
- C-16. Compared with no Kallmark Ridge Cod Fishery Act, asset value for vessel_owners.history rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-17. Compared with no Kallmark Ridge Cod Fishery Act, capital stock target for vessel_owners.history falls in the long run (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); Rights can be sold or leased at low cost (p = 0.80); Holders' costs or values differ (p = 0.80). Reported.
- C-18. Compared with no Kallmark Ridge Cod Fishery Act, informal activity for vessel_owners.history rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-19. Compared with no Kallmark Ridge Cod Fishery Act, investment target for vessel_owners.history rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-20. Compared with no Kallmark Ridge Cod Fishery Act, number of sellers for vessel_owners.history falls from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); Rights can be sold or leased at low cost (p = 0.80); Holders' costs or values differ (p = 0.80). Reported.
- C-21. Compared with no Kallmark Ridge Cod Fishery Act, quantity supplied for vessel_owners.history rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80); Rights can be sold or leased at low cost (p = 0.80); Holders' costs or values differ (p = 0.80). Reported.
- C-22. Compared with no Kallmark Ridge Cod Fishery Act, quantity traded for vessel_owners.history falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.90); The cap is enforced (p = 0.80). Reported.
- C-23. Compared with no Kallmark Ridge Cod Fishery Act, quantity traded for vessel_owners.history rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.
- C-24. Compared with no Kallmark Ridge Cod Fishery Act, resources available other uses for vessel_owners.history falls in the announcement window (before the effective date), in the short run (tier B, invisible). Why: CR-10: CR-10; EN-12: EN-12. This holds if: Actors know the allocation rule during the base period (p = 0.80). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
