# Thin-slice run: Brisklund Wheat Price Assurance Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-18T20:16:56+00:00
Prediction log sha256 (frozen before the outcome card was opened): `1acdd1db9ba141fe…`

## Policy record

- Rule-maker: the Parliament of Brisklund; enacted 30 June 2027, effective crop year 2028.
- Stated aim: none stated
- k1: per_unit_subsidy on wheat in brisklund; binds wheat_growers, protects None. Source: "A deficiency payment is paid to the holder (the person registered as farming the land) of each registered farm."
- Unclear U1: Whether the payment is made on each farm's actual output (the harvest declared for the crop year) or on a fixed historical base (its established production). Readings: U1-a: the payment is on the harvest declared for the crop year (actual output) / U1-b: the payment is on the farm's established production, the crop year fixing only the year whose price sets the rate
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `takeup(k1)` | other | 0.90 | Many eligible recipients value the payment above the cost of qualifying, and claim it. |
| `not_fully_captured(k1)` | other | 0.90 | The producers keep part of the payment: the price they receive, including it, rises. |
| `quantity_expands(k1)` | alternative_uses | 0.85 | At least one side can expand its quantity: more of the subsidized good is traded. |
| `seller_supply_slow(k1)` | durability | 0.25 | The sellers' supply of the subsidized good cannot grow at once. |
| `sellers_fewer_alternatives(k1)` | substitutability | 0.30 | While supply is fixed, the sellers have clearly fewer alternatives than the recipients. |
| `asset_supply_slow(k1)` | durability | 0.80 | The supply of the asset whose return the payment raises is fixed or slowly expandable. |
| `expected_to_last(k1)` | expectations | 0.80 | Buyers of the affected assets expect the payment to last for several years. |
| `beneficiaries_organize(k1)` | other | 0.90 | The sellers who gain can organize to lobby for renewal at a cost below their stake. |
| `can_delay(k1)` | expectations | 0.10 | Eligible buyers knew of the payment before it started and could delay purchases. |
| `pulled_forward(k1)` | expectations | 0.10 | Many window buyers would have bought within the next few years anyway. |
| `ends_as_scheduled(k1)` | expectations | 0.45 | The payment ends as scheduled: it is not renewed, extended or repeated soon after. |
| `supply_slow_at_expiry(k1)` | durability | 0.70 | When the payment ends, the sellers cannot cut their supply at once. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |
| C-2 | owners.wheat_land | asset_value | increase | short+ | B | SB-2, SB-4 | {asset_supply_slow(k1), expected_to_last(k1)} | yes |
| C-3 | taxpayers or recipients.other_spending or taxpayers.future | resources_available_other_uses | at_least_one_decrease | short+ | A | SB-1, OC-1 | {} | yes |
| C-4 | wheat_growers | compliance_cost | increase | short+ | A | CR-8 | {} | yes |
| C-5 | wheat_growers | lobbying_effort | U1-a: increase; U1-b: none | medium+ | B | SB-2, RS-7 | {beneficiaries_organize(k1), takeup(k1)} | yes |
| C-6 | wheat_growers | net_price_received | U1-a: increase; U1-b: none | short+ | B | SB-2 | {not_fully_captured(k1), takeup(k1)} | yes |
| C-7 | wheat_growers | quantity_supplied | U1-a: increase; U1-b: none | short+ | B | SB-2 | {quantity_expands(k1), takeup(k1)} | yes |

## Explanations

- C-1. Compared with no Brisklund Wheat Price Assurance Act, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-2. Compared with no Brisklund Wheat Price Assurance Act, asset value for owners.wheat_land rises from the short run onward (tier B, invisible). Why: SB-2: a payment per unit is a wedge in the other direction: buyers pay less net of it, sellers may receive more, and more is traded; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value. This holds if: The supply of the asset whose return the payment raises is fixed or slowly expandable (p = 0.80); Buyers of the affected assets expect the payment to last for several years (p = 0.80). Reported.
- C-3. Compared with no Brisklund Wheat Price Assurance Act, resources available other uses for taxpayers or recipients.other_spending or taxpayers.future falls for at least one of them from the short run onward (tier A, invisible). Why: SB-1: a subsidy is paid by someone: taxes now, or borrowing repaid from taxes later; OC-1: what the payers give up is what they would otherwise have bought. This holds if: no assumption. Reported.
- C-4. Compared with no Brisklund Wheat Price Assurance Act, compliance cost for wheat_growers rises from the short run onward (tier A, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: no assumption. Reported.
- C-5. Compared with no Brisklund Wheat Price Assurance Act, lobbying effort for wheat_growers may move either way from the medium run onward (tier B, invisible). Why: SB-2: a payment per unit is a wedge in the other direction: buyers pay less net of it, sellers may receive more, and more is traded; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The sellers who gain can organize to lobby for renewal at a cost below their stake (p = 0.90); Many eligible recipients value the payment above the cost of qualifying, and claim it (p = 0.90). Sign per reading: U1-a: increase; U1-b: none. Reported.
- C-6. Compared with no Brisklund Wheat Price Assurance Act, net price received for wheat_growers may move either way from the short run onward (tier B, visible). Why: SB-2: a payment per unit is a wedge in the other direction: buyers pay less net of it, sellers may receive more, and more is traded. This holds if: The producers keep part of the payment: the price they receive, including it, rises (p = 0.90); Many eligible recipients value the payment above the cost of qualifying, and claim it (p = 0.90). Sign per reading: U1-a: increase; U1-b: none. Reported.
- C-7. Compared with no Brisklund Wheat Price Assurance Act, quantity supplied for wheat_growers may move either way from the short run onward (tier B, visible). Why: SB-2: a payment per unit is a wedge in the other direction: buyers pay less net of it, sellers may receive more, and more is traded. This holds if: At least one side can expand its quantity: more of the subsidized good is traded (p = 0.85); Many eligible recipients value the payment above the cost of qualifying, and claim it (p = 0.90). Sign per reading: U1-a: increase; U1-b: none. Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
