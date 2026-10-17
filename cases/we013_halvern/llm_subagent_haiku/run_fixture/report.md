# Thin-slice run: Halvern Steel Safeguard Order

Rule base: rb-thin-0.5 (handbook catalog 1.4: PC-1, PC-3, PC-5, PC-7, PC-21, RS-4, RS-5, TX-1, TX-2, TX-7, TX-8, RS-14; CR-12 totals)  |  Decider: fixture:answers.json  |  Run: 2026-10-17T20:18:54+00:00
Prediction log sha256 (frozen before the outcome card was opened): `ac487be2f30a75f7…`

## Policy record

- Rule-maker: Trade Ministry of Halvern; enacted year 0, effective year 0, 1 April.
- Stated aim: none stated
- k1: tariff on steel_flat_rolled_and_long in halvern; binds importers, protects steelmakers.domestic. Source: "Importers of record must pay a tariff of 25% of the customs value on imports of flat-rolled and long steel products, for three years."
- Unclear U1: The standard for 'sufficient quantity or quality' in the exclusion process (K2). Readings: U1-a: applied case by case, with weight given to objections from domestic steelmakers / U1-b: applied by a fixed domestic-capacity test
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.85 | Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff. |
| `domestic_substitutes(k1)` | substitutability | 0.75 | Domestic producers can raise output and make close substitutes for most imports. |
| `no_offset(k1)` | other | 0.60 | The fall in imports is not offset by capital flows or other adjustments within the medium run. |
| `input_not_replaceable(k1)` | substitutability | 0.80 | The taxed good is a material part of downstream costs and cannot be replaced at the old cost. |
| `competitors_exempt(k1)` | other | 0.80 | Many downstream users compete with sellers who do not face the higher input cost. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.construction | price_paid | increase | medium+ | B | TX-7, RS-14 | {binding(k1), input_not_replaceable(k1)} | yes |
| C-2 | export_industries | quantity_supplied | decrease | medium+ | B | TX-7, TX-2, TX-8 | {binding(k1), no_offset(k1)} | yes |
| C-3 | importers | quantity_traded | decrease | short+ | B | TX-7, TX-2 | {binding(k1)} | yes |
| C-4 | importers | resources_available_other_uses | decrease | short+ | A | TX-1 | {} | yes |
| C-5 | officials.enforcement | tax_revenue | increase | short+ | A | TX-1 | {} | yes |
| C-6 | steel_users | price_paid | increase | short+ | B | TX-7 | {binding(k1)} | yes |
| C-7 | steel_users | quantity_supplied | decrease | medium+ | B | TX-7, RS-14 | {binding(k1), competitors_exempt(k1), input_not_replaceable(k1)} | yes |
| C-8 | steel_users | resources_available_other_uses | decrease | short+ | A | TX-1, TX-7 | {binding(k1)} | yes |
| C-9 | steelmakers.domestic | net_price_received | increase | short+ | B | TX-7 | {binding(k1), domestic_substitutes(k1)} | yes |
| C-10 | steelmakers.domestic | quantity_supplied | increase | short+ | B | TX-7 | {binding(k1), domestic_substitutes(k1)} | yes |
| C-11 | workers.export_industries | employment | decrease | medium+ | B | TX-7, TX-2, TX-8 | {binding(k1), no_offset(k1)} | yes |

## Explanations

- C-1. Compared with no Halvern Steel Safeguard Order, price paid for buyers.construction rises from the medium run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; RS-14: a dearer input is passed down to the output: its price rises where competitors face the same cost, and its sellers sell less where competitors are exempt. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.85); The taxed good is a material part of downstream costs and cannot be replaced at the old cost (p = 0.80). Reported.
- C-2. Compared with no Halvern Steel Safeguard Order, quantity supplied for export_industries falls from the medium run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; TX-8: foreigners who sell less to the country earn less of its currency and so buy fewer of its exports. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.85); The fall in imports is not offset by capital flows or other adjustments within the medium run (p = 0.60). Reported.
- C-3. Compared with no Halvern Steel Safeguard Order, quantity traded for importers falls from the short run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.85). Reported.
- C-4. Compared with no Halvern Steel Safeguard Order, resources available other uses for importers falls from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue. This holds if: no assumption. Reported.
- C-5. Compared with no Halvern Steel Safeguard Order, tax revenue for officials.enforcement rises from the short run onward (tier A, visible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue. This holds if: no assumption. Reported.
- C-6. Compared with no Halvern Steel Safeguard Order, price paid for steel_users rises from the short run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.85). Reported.
- C-7. Compared with no Halvern Steel Safeguard Order, quantity supplied for steel_users falls from the medium run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; RS-14: a dearer input is passed down to the output: its price rises where competitors face the same cost, and its sellers sell less where competitors are exempt. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.85); Many downstream users compete with sellers who do not face the higher input cost (p = 0.80); The taxed good is a material part of downstream costs and cannot be replaced at the old cost (p = 0.80). Reported.
- C-8. Compared with no Halvern Steel Safeguard Order, resources available other uses for steel_users falls from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.85). Reported.
- C-9. Compared with no Halvern Steel Safeguard Order, net price received for steelmakers.domestic rises from the short run onward (tier B, visible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.85); Domestic producers can raise output and make close substitutes for most imports (p = 0.75). Reported.
- C-10. Compared with no Halvern Steel Safeguard Order, quantity supplied for steelmakers.domestic rises from the short run onward (tier B, visible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.85); Domestic producers can raise output and make close substitutes for most imports (p = 0.75). Reported.
- C-11. Compared with no Halvern Steel Safeguard Order, employment for workers.export_industries falls from the medium run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; TX-8: foreigners who sell less to the country earn less of its currency and so buy fewer of its exports. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.85); The fall in imports is not offset by capital flows or other adjustments within the medium run (p = 0.60). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
