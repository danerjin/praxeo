# Thin-slice run: Calvar Sugar Market Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-18T20:58:30+00:00
Prediction log sha256 (frozen before the outcome card was opened): `d95618f7d8500bc5…`

## Policy record

- Rule-maker: the Calvar parliament; enacted four months after the bill was introduced, effective nine months after the bill was introduced.
- Stated aim: none stated
- k1: quota on raw_sugar in calvar; binds importers, protects None. Source: "Imports of raw and refined sugar, and of mixtures containing more than 65% sugar by weight, are limited to 350,000 tonnes a year from the effective date, and importers are bound by the limit."
- Unclear u1: Whether the 65% threshold counts sugar against dry weight or total weight. Assumed total weight, the reading more favorable to importers of syrups and blends. Readings: U1-a: the threshold counts sugar against total weight (assumed) / U1-b: the threshold counts sugar against dry weight
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.95 | The cap holds the quantity below what would otherwise be traded. |
| `enforced(k1)` | enforcement | 0.85 | The cap is enforced. |
| `evasion(k1)` | enforcement | 0.30 | Some trade takes place beyond the cap without being caught. |
| `can_organize(k1)` | other | 0.85 | The holders of the rights can organize to lobby at a cost below their stake. |
| `expected_to_last(k1)` | expectations | 0.65 | Holders and buyers of the rights expect the restriction to last. |
| `domestic_substitutes(k1)` | substitutability | 0.90 | Domestic producers make close substitutes for the covered imports. |
| `no_offset(k1)` | other | 0.60 | Lower imports reduce foreigners' purchases of the country's exports in the medium run; capital flows do not cancel it. |
| `enforcement_budget_raised(k1)` | revenue_use | 0.70 | The administering agency's budget is raised to cover the new work, so taxpayers fund it. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.sugar | disputes_settled_outside_courts | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | no |
| C-2 | buyers.sugar | price_paid | increase | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-3 | buyers.sugar | quality_information | decrease | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | no |
| C-4 | buyers.sugar | quantity_traded | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-5 | buyers.sugar | resources_available_other_uses | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-6 | buyers.sugar | search_cost | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | no |
| C-7 | export_industries | quantity_supplied | decrease | medium+ | B | EN-6, TX-8 | {binding(k1), enforced(k1), no_offset(k1)} | yes |
| C-8 | growers.beet | net_price_received | increase | short+ | B | EN-6, TX-7 | {binding(k1), domestic_substitutes(k1), enforced(k1)} | yes |
| C-9 | growers.beet | quantity_supplied | increase | short+ | B | EN-6, TX-7 | {binding(k1), domestic_substitutes(k1), enforced(k1)} | yes |
| C-10 | importers | informal_activity | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | no |
| C-11 | importers | quantity_traded | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-12 | officials.enforcement | enforcement_cost | increase | short+ | B | EN-6, OC-3 | {binding(k1), enforced(k1)} | yes |
| C-13 | quota_holders | asset_value | increase | short+ | B | EN-6, SB-4 | {binding(k1), enforced(k1), expected_to_last(k1)} | yes |
| C-14 | quota_holders | lobbying_effort | increase | medium+ | B | EN-6, RS-7 | {binding(k1), can_organize(k1), enforced(k1)} | yes |
| C-15 | quota_holders | net_price_received | increase | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-16 | taxpayers or recipients.other_spending or taxpayers.future | resources_available_other_uses | at_least_one_decrease | short+ | B | EN-6, OC-3, OC-1 | {binding(k1), enforced(k1), enforcement_budget_raised(k1)} | yes |
| C-17 | workers.export_industries | employment or hours_worked | at_least_one_decrease | medium+ | B | EN-6, TX-8 | {binding(k1), enforced(k1), no_offset(k1)} | yes |

## Explanations

- C-1. Compared with no Calvar Sugar Market Act, disputes settled outside courts for buyers.sugar rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85); Some trade takes place beyond the cap without being caught (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-2. Compared with no Calvar Sugar Market Act, price paid for buyers.sugar rises from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85). Reported.
- C-3. Compared with no Calvar Sugar Market Act, quality information for buyers.sugar falls from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85); Some trade takes place beyond the cap without being caught (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-4. Compared with no Calvar Sugar Market Act, quantity traded for buyers.sugar falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85). Reported.
- C-5. Compared with no Calvar Sugar Market Act, resources available other uses for buyers.sugar falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85). Reported.
- C-6. Compared with no Calvar Sugar Market Act, search cost for buyers.sugar rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85); Some trade takes place beyond the cap without being caught (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-7. Compared with no Calvar Sugar Market Act, quantity supplied for export_industries falls from the medium run onward (tier B, invisible). Why: EN-6: EN-6; TX-8: foreigners who sell less to the country earn less of its currency and so buy fewer of its exports. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85); Lower imports reduce foreigners' purchases of the country's exports in the medium run; capital flows do not cancel it (p = 0.60). Reported.
- C-8. Compared with no Calvar Sugar Market Act, net price received for growers.beet rises from the short run onward (tier B, visible). Why: EN-6: EN-6; TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); Domestic producers make close substitutes for the covered imports (p = 0.90); The cap is enforced (p = 0.85). Reported.
- C-9. Compared with no Calvar Sugar Market Act, quantity supplied for growers.beet rises from the short run onward (tier B, visible). Why: EN-6: EN-6; TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); Domestic producers make close substitutes for the covered imports (p = 0.90); The cap is enforced (p = 0.85). Reported.
- C-10. Compared with no Calvar Sugar Market Act, informal activity for importers rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85); Some trade takes place beyond the cap without being caught (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-11. Compared with no Calvar Sugar Market Act, quantity traded for importers falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85). Reported.
- C-12. Compared with no Calvar Sugar Market Act, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85). Reported.
- C-13. Compared with no Calvar Sugar Market Act, asset value for quota_holders rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85); Holders and buyers of the rights expect the restriction to last (p = 0.65). Reported.
- C-14. Compared with no Calvar Sugar Market Act, lobbying effort for quota_holders rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The holders of the rights can organize to lobby at a cost below their stake (p = 0.85); The cap is enforced (p = 0.85). Reported.
- C-15. Compared with no Calvar Sugar Market Act, net price received for quota_holders rises from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85). Reported.
- C-16. Compared with no Calvar Sugar Market Act, resources available other uses for taxpayers or recipients.other_spending or taxpayers.future falls for at least one of them from the short run onward (tier B, invisible). Why: EN-6: EN-6; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers; OC-1: what the payers give up is what they would otherwise have bought. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85); The administering agency's budget is raised to cover the new work, so taxpayers fund it (p = 0.70). Reported.
- C-17. Compared with no Calvar Sugar Market Act, employment or hours worked for workers.export_industries falls for at least one of them from the medium run onward (tier B, invisible). Why: EN-6: EN-6; TX-8: foreigners who sell less to the country earn less of its currency and so buy fewer of its exports. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.85); Lower imports reduce foreigners' purchases of the country's exports in the medium run; capital flows do not cancel it (p = 0.60). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
