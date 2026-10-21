# Thin-slice run: Halvern Steel Safeguard Order

Rule base: rb-thin-0.5 (handbook catalog 1.4: PC-1, PC-3, PC-5, PC-7, PC-21, RS-4, RS-5, TX-1, TX-2, TX-7, TX-8, RS-14; CR-12 totals)  |  Decider: fixture:answers_remapped.json  |  Run: 2026-10-17T20:18:54+00:00
Prediction log sha256 (frozen before the outcome card was opened): `8a2c2831922cf87f…`

## Policy record

- Rule-maker: Trade Ministry (issuing authority of the order not explicitly stated); enacted not stated, effective 1 April (year not stated).
- Stated aim: none stated
- C1: tariff on flat_rolled_and_long_steel_products in halvern; binds importers.current, protects None. Source: "Importers of record must pay a tariff of 25% of the customs value on imports of flat-rolled and long steel products, for three years."
- C2: tariff on flat_rolled_and_long_steel_products in halvern; binds importers.current, protects steel_users. Source: "Steel users may apply to exclude a product "not produced domestically in sufficient quantity or quality"."
- Unclear U1: A review in the third year may extend it. Readings: U1-a: 'it' is the tariff; the review may extend the 25% tariff beyond its three-year term, and no limit on the extension is stated. / U1-b: 'it' is the three-year term; the review may lengthen the term, and the tariff continues during any extension.
- Unclear U2: Steel users may apply to exclude a product "not produced domestically in sufficient quantity or quality". The standard for "sufficient quantity or quality" is not defined. Readings: U2-a: a product qualifies for exclusion when domestic production is insufficient in quantity or insufficient in quality (either shortfall is enough). / U2-b: a product qualifies for exclusion only when domestic production is insufficient in both quantity and quality.
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(c1)` | binding | 0.72 | Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff. |
| `domestic_substitutes(c1)` | substitutability | 0.30 | Domestic producers can raise output and make close substitutes for most imports. |
| `no_offset(c1)` | other | 0.35 | The fall in imports is not offset by capital flows or other adjustments within the medium run. |
| `binding(c2)` | binding | 0.72 | Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff. |
| `domestic_substitutes(c2)` | substitutability | 0.30 | Domestic producers can raise output and make close substitutes for most imports. |
| `no_offset(c2)` | other | 0.35 | The fall in imports is not offset by capital flows or other adjustments within the medium run. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.current | price_paid | increase | short+ | B | TX-7 | {binding(c1)} | yes |
| C-2 | buyers.current | resources_available_other_uses | decrease | short+ | A | TX-1, TX-7 | {binding(c1)} | yes |
| C-3 | export_industries | quantity_supplied | decrease | medium+ | B | TX-7, TX-2, TX-8 | {binding(c1), no_offset(c1)} | no |
| C-4 | importers.current | quantity_traded | decrease | short+ | B | TX-7, TX-2 | {binding(c1)} | yes |
| C-5 | importers.current | resources_available_other_uses | decrease | short+ | A | TX-1 | {} | yes |
| C-6 | officials.enforcement | tax_revenue | increase | short+ | A | TX-1 | {} | yes |
| C-7 | sellers.substitutes | net_price_received | increase | short+ | B | TX-7 | {binding(c1), domestic_substitutes(c1)} | no |
| C-8 | sellers.substitutes | quantity_supplied | increase | short+ | B | TX-7 | {binding(c1), domestic_substitutes(c1)} | no |
| C-9 | workers.export_industries | employment | decrease | medium+ | B | TX-7, TX-2, TX-8 | {binding(c1), no_offset(c1)} | no |

## Explanations

- C-1. Compared with no Halvern Steel Safeguard Order, price paid for buyers.current rises from the short run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.72). Reported.
- C-2. Compared with no Halvern Steel Safeguard Order, resources available other uses for buyers.current falls from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.72). Reported.
- C-3. Compared with no Halvern Steel Safeguard Order, quantity supplied for export_industries falls from the medium run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; TX-8: foreigners who sell less to the country earn less of its currency and so buy fewer of its exports. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.72); The fall in imports is not offset by capital flows or other adjustments within the medium run (p = 0.35). Not reported: an assumption is below the 0.5 cut-off.
- C-4. Compared with no Halvern Steel Safeguard Order, quantity traded for importers.current falls from the short run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.72). Reported.
- C-5. Compared with no Halvern Steel Safeguard Order, resources available other uses for importers.current falls from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue. This holds if: no assumption. Reported.
- C-6. Compared with no Halvern Steel Safeguard Order, tax revenue for officials.enforcement rises from the short run onward (tier A, visible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue. This holds if: no assumption. Reported.
- C-7. Compared with no Halvern Steel Safeguard Order, net price received for sellers.substitutes rises from the short run onward (tier B, visible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.72); Domestic producers can raise output and make close substitutes for most imports (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-8. Compared with no Halvern Steel Safeguard Order, quantity supplied for sellers.substitutes rises from the short run onward (tier B, visible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.72); Domestic producers can raise output and make close substitutes for most imports (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-9. Compared with no Halvern Steel Safeguard Order, employment for workers.export_industries falls from the medium run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; TX-8: foreigners who sell less to the country earn less of its currency and so buy fewer of its exports. This holds if: Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff (p = 0.72); The fall in imports is not offset by capital flows or other adjustments within the medium run (p = 0.35). Not reported: an assumption is below the 0.5 cut-off.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
