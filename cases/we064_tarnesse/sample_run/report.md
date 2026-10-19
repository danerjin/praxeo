# Thin-slice run: Tarnesse 2.9 GHz Award Regulations

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T06:08:26+00:00
Prediction log sha256 (frozen before the outcome card was opened): `eba795c61720f507…`

## Policy record

- Rule-maker: the Tarnesse Communications Authority and the government; enacted 1 March 2027, effective 1 January 2028.
- Stated aim: none stated
- k1: rights_allocation on spectrum_licenses_2_9ghz in tarnesse; binds bidders, protects licensees. Source: "The Regulations create six national licenses of 20 MHz in the 2.9 GHz band, sold to bidders who qualify by deposit."
- k2: mandated_contract_term on spectrum_licenses_2_9ghz in tarnesse; binds licensees, protects customers.towns. Source: "Each licensee must provide service in the band to areas containing 90% of the population by 31 December 2032, or the license is revoked without refund."
- k3: quota on spectrum_blocks_2_9ghz in tarnesse; binds bidders, protects None. Source: "No more than two blocks may be awarded to, or held by, one person and its affiliates."
- Unclear U1: Whether a license may be resold before the coverage deadline. Readings: U1-a: transfers are allowed at any time with consent (reg. 14), and reg. 9(3) only states the purpose of the obligation / U1-b: reg. 9(3) bars any transfer until the obligation is met or the deadline passes
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k3)` | binding | 0.60 | The cap holds the quantity below what would otherwise be traded. |
| `enforced(k3)` | enforcement | 0.85 | The cap is enforced. |
| `evasion(k3)` | enforcement | 0.55 | Some trade takes place beyond the cap without being caught. |
| `can_organize(k3)` | other | 0.85 | The holders of the rights can organize to lobby at a cost below their stake. |
| `expected_to_last(k3)` | expectations | 0.70 | Holders and buyers of the rights expect the restriction to last. |
| `values_differ(k3)` | other | 0.60 | Holders' costs or values differ. |
| `trade_cheap(k3)` | mobility | 0.40 | Rights can be sold or leased at low cost. |
| `value_above_price(k3)` | other | 0.60 | Some buyers win the rights below their own value for them. |
| `enforcement_budget_raised(k3)` | revenue_use | 0.90 | The administering agency's budget is raised to cover the new work, so taxpayers fund it. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | bidders | capital_stock_target | U1-a: decrease; U1-b: none | long | B | EN-6, EN-13 | {binding(k3), enforced(k3), trade_cheap(k3), values_differ(k3)} | no |
| C-2 | bidders | disputes_settled_outside_courts | increase | short+ | B | EN-6, RS-3 | {binding(k3), enforced(k3), evasion(k3)} | yes |
| C-3 | bidders | informal_activity | increase | short+ | B | EN-6, RS-3 | {binding(k3), enforced(k3), evasion(k3)} | yes |
| C-4 | bidders | number_of_sellers | U1-a: decrease; U1-b: none | medium+ | B | EN-6, EN-13 | {binding(k3), enforced(k3), trade_cheap(k3), values_differ(k3)} | no |
| C-5 | bidders | quality_information | decrease | short+ | B | EN-6, RS-3 | {binding(k3), enforced(k3), evasion(k3)} | yes |
| C-6 | bidders | search_cost | increase | short+ | B | EN-6, RS-3 | {binding(k3), enforced(k3), evasion(k3)} | yes |
| C-7 | licensees | asset_value | increase | short+ | B | CR-8, CR-7, SB-4, EN-6 | {binding(k3), enforced(k3), expected_to_last(k3)} or {value_above_price(k3)} | yes |
| C-8 | licensees | lobbying_effort | increase | medium+ | B | EN-6, RS-7 | {binding(k3), can_organize(k3), enforced(k3)} | yes |
| C-9 | licensees | right_lease_price | U1-a: increase; U1-b: none | medium+ | B | EN-6, EN-13 | {binding(k3), enforced(k3), trade_cheap(k3), values_differ(k3)} | no |
| C-10 | officials.enforcement | enforcement_cost | increase | short+ | B | EN-6, OC-3 | {binding(k3), enforced(k3)} | yes |
| C-11 | tower_owners | quantity_traded | U1-a: decrease; U1-b: none | medium+ | B | EN-6, EN-13 | {binding(k3), enforced(k3), trade_cheap(k3), values_differ(k3)} | no |
| C-12 | treasury | non_tax_receipts | increase | short+ | B | CR-8 | {} | yes |

## Explanations

- C-1. Compared with no Tarnesse 2.9 GHz Award Regulations, capital stock target for bidders may move either way in the long run (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.60); The cap is enforced (p = 0.85); Rights can be sold or leased at low cost (p = 0.40); Holders' costs or values differ (p = 0.60). Sign per reading: U1-a: decrease; U1-b: none. Not reported: an assumption is below the 0.5 cut-off.
- C-2. Compared with no Tarnesse 2.9 GHz Award Regulations, disputes settled outside courts for bidders rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.60); The cap is enforced (p = 0.85); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-3. Compared with no Tarnesse 2.9 GHz Award Regulations, informal activity for bidders rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.60); The cap is enforced (p = 0.85); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-4. Compared with no Tarnesse 2.9 GHz Award Regulations, number of sellers for bidders may move either way from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.60); The cap is enforced (p = 0.85); Rights can be sold or leased at low cost (p = 0.40); Holders' costs or values differ (p = 0.60). Sign per reading: U1-a: decrease; U1-b: none. Not reported: an assumption is below the 0.5 cut-off.
- C-5. Compared with no Tarnesse 2.9 GHz Award Regulations, quality information for bidders falls from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.60); The cap is enforced (p = 0.85); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-6. Compared with no Tarnesse 2.9 GHz Award Regulations, search cost for bidders rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.60); The cap is enforced (p = 0.85); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-7. Compared with no Tarnesse 2.9 GHz Award Regulations, asset value for licensees rises from the short run onward (tier B, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses; CR-7: CR-7; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value; EN-6: EN-6. This holds if: Some buyers win the rights below their own value for them (p = 0.60). It also follows under 1 other minimal assumption set(s). Reported.
- C-8. Compared with no Tarnesse 2.9 GHz Award Regulations, lobbying effort for licensees rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.60); The holders of the rights can organize to lobby at a cost below their stake (p = 0.85); The cap is enforced (p = 0.85). Reported.
- C-9. Compared with no Tarnesse 2.9 GHz Award Regulations, right lease price for licensees may move either way from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.60); The cap is enforced (p = 0.85); Rights can be sold or leased at low cost (p = 0.40); Holders' costs or values differ (p = 0.60). Sign per reading: U1-a: increase; U1-b: none. Not reported: an assumption is below the 0.5 cut-off.
- C-10. Compared with no Tarnesse 2.9 GHz Award Regulations, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.60); The cap is enforced (p = 0.85). Reported.
- C-11. Compared with no Tarnesse 2.9 GHz Award Regulations, quantity traded for tower_owners may move either way from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.60); The cap is enforced (p = 0.85); Rights can be sold or leased at low cost (p = 0.40); Holders' costs or values differ (p = 0.60). Sign per reading: U1-a: decrease; U1-b: none. Not reported: an assumption is below the 0.5 cut-off.
- C-12. Compared with no Tarnesse 2.9 GHz Award Regulations, non tax receipts for treasury rises from the short run onward (tier B, visible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: no assumption. Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
