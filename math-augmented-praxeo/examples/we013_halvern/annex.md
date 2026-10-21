# Annex pass: Halvern Steel Safeguard Order

Sizes attached to reported consequences by `mathpraxeo.bridge.annex_pass`. No consequence was changed.

| Consequence | Actor class | Variable | Sign | Handler | Math rules | Annex range | Rung | Sign check |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.construction | price_paid | increase | cost_pass_through | MR-6 | [0, 0.025] | M1 | indeterminate |
| C-6 | importers | quantity_traded | decrease | tariff_imports | MR-2, MR-4, MR-6 | [-0.803, -0.113] | M1 | agrees |
| C-12 | officials.enforcement | tax_revenue_vs_static_projection | decrease | tariff_revenue_shortfall | MR-2, MR-4, MR-6 | [-0.803, -0.113] | M1 | agrees |
| C-19 | steel_users | price_paid | increase | tariff_domestic_price | MR-6 | [0.15, 0.25] | M1 | agrees |
| C-21 | steel_users | quantity_traded | decrease | tariff_use | MR-4, MR-6 | [-0.15, -0.03] | M1 | agrees |
| C-28 | steelmakers.domestic | net_price_received | increase | tariff_domestic_price | MR-6 | [0.15, 0.25] | M1 | agrees |
| C-29 | steelmakers.domestic | quantity_supplied | increase | tariff_domestic_output | MR-4, MR-6 | [0.03, 0.25] | M1 | agrees |

Sources of the ranges:

- input_price_change: illustrative: tariff of 25% times pass-through of 0.6 to 1.0
- cost_share: illustrative: steel's share of construction costs
- tax_rate: WE-013 K1: 25% of the customs value
- import_share: WE-013 record: domestic firms supply about 60% of use, so imports are about 40% (range for rounding)
- demand_elasticity: illustrative medium-run elasticity of steel demand
- supply_elasticity: illustrative medium-run elasticity of domestic steel supply from spare and idle capacity
- pass_through: illustrative: share of the tariff in the domestic price (1 for a small buyer on the world market; less if foreign sellers absorb part)

Notes:

- C-6: First order is strained: the gap reaches 25%, beyond 15%; treat the range as indicative only.
- C-12: First order is strained: the gap reaches 25%, beyond 15%; treat the range as indicative only.
