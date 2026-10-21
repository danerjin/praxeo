# Thin-slice run: Port Halden Taxi Fleet Stabilization Ordinance

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T06:08:22+00:00
Prediction log sha256 (frozen before the outcome card was opened): `97bf34a865b5b64d…`

## Policy record

- Rule-maker: the Port Halden city council; enacted five months before the effective date, effective the effective date.
- Stated aim: none stated
- k1: quota on taxi_service in port_halden; binds drivers.taxi, protects None. Source: "The number of taxi licenses is fixed at the number outstanding on the effective date, and applies to anyone offering taxi service: street hails and taxi ranks."
- Unclear U1: Whether a booking made through a smartphone app a few minutes before pickup meets the 30-minute rule. Readings: U1-a: app booking counts as pre-booked. / U1-b: it does not.
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.80 | The cap holds the quantity below what would otherwise be traded. |
| `enforced(k1)` | enforcement | 0.80 | The cap is enforced. |
| `evasion(k1)` | enforcement | 0.75 | Some trade takes place beyond the cap without being caught. |
| `can_organize(k1)` | other | 0.85 | The holders of the rights can organize to lobby at a cost below their stake. |
| `expected_to_last(k1)` | expectations | 0.75 | Holders and buyers of the rights expect the restriction to last. |
| `values_differ(k1)` | other | 0.60 | Holders' costs or values differ. |
| `trade_cheap(k1)` | mobility | 0.70 | Rights can be sold or leased at low cost. |
| `enforcement_budget_raised(k1)` | revenue_use | 0.55 | The administering agency's budget is raised to cover the new work, so taxpayers fund it. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | drivers.taxi | capital_stock_target | decrease | long | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-2 | drivers.taxi | entry_rate | decrease | medium+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-3 | drivers.taxi | informal_activity | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-4 | drivers.taxi | number_of_sellers | decrease | medium+ | B | EN-6, EN-13 | {binding(k1), enforced(k1)} | yes |
| C-5 | drivers.taxi | quantity_traded | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-6 | medallion_owners.initial | asset_value | increase | short+ | B | EN-6, SB-4 | {binding(k1), enforced(k1), expected_to_last(k1)} | yes |
| C-7 | medallion_owners.initial | lobbying_effort | increase | medium+ | B | EN-6, RS-7 | {binding(k1), can_organize(k1), enforced(k1)} | yes |
| C-8 | medallion_owners.initial | right_lease_price | increase | medium+ | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-9 | officials.enforcement | enforcement_cost | increase | short+ | B | EN-6, OC-3 | {binding(k1), enforced(k1)} | yes |
| C-10 | riders | disputes_settled_outside_courts | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-11 | riders | excess_demand | increase | medium+ | B | EN-6, PC-1 | {binding(k1), enforced(k1)} | yes |
| C-12 | riders | quality_information | decrease | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-13 | riders | quantity_traded | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-14 | riders | search_cost | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-15 | taxpayers or recipients.other_spending or taxpayers.future | resources_available_other_uses | at_least_one_decrease | short+ | B | EN-6, OC-3, OC-1 | {binding(k1), enforced(k1), enforcement_budget_raised(k1)} | yes |

## Explanations

- C-1. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, capital stock target for drivers.taxi falls in the long run (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80); Rights can be sold or leased at low cost (p = 0.70); Holders' costs or values differ (p = 0.60). Reported.
- C-2. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, entry rate for drivers.taxi falls from the medium run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80). Reported.
- C-3. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, informal activity for drivers.taxi rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80); Some trade takes place beyond the cap without being caught (p = 0.75). Reported.
- C-4. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, number of sellers for drivers.taxi falls from the medium run onward (tier B, visible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80). Reported.
- C-5. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, quantity traded for drivers.taxi falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80). Reported.
- C-6. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, asset value for medallion_owners.initial rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80); Holders and buyers of the rights expect the restriction to last (p = 0.75). Reported.
- C-7. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, lobbying effort for medallion_owners.initial rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The holders of the rights can organize to lobby at a cost below their stake (p = 0.85); The cap is enforced (p = 0.80). Reported.
- C-8. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, right lease price for medallion_owners.initial rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80); Rights can be sold or leased at low cost (p = 0.70); Holders' costs or values differ (p = 0.60). Reported.
- C-9. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80). Reported.
- C-10. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, disputes settled outside courts for riders rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80); Some trade takes place beyond the cap without being caught (p = 0.75). Reported.
- C-11. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, excess demand for riders rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; PC-1: a ceiling held below the price the market would reach binds sellers; where new contracts are priced freely, fewer vacancies raise their initial price instead of leaving a shortage. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80). Reported.
- C-12. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, quality information for riders falls from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80); Some trade takes place beyond the cap without being caught (p = 0.75). Reported.
- C-13. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, quantity traded for riders falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80). Reported.
- C-14. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, search cost for riders rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80); Some trade takes place beyond the cap without being caught (p = 0.75). Reported.
- C-15. Compared with no Port Halden Taxi Fleet Stabilization Ordinance, resources available other uses for taxpayers or recipients.other_spending or taxpayers.future falls for at least one of them from the short run onward (tier B, invisible). Why: EN-6: EN-6; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers; OC-1: what the payers give up is what they would otherwise have bought. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.80); The cap is enforced (p = 0.80); The administering agency's budget is raised to cover the new work, so taxpayers fund it (p = 0.55). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
