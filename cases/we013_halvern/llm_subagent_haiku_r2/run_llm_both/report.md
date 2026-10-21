# Thin-slice run: Halvern Steel Safeguard Order

Rule base: rb-thin-0.5 (handbook catalog 1.4: PC-1, PC-3, PC-5, PC-7, PC-21, RS-4, RS-5, TX-1, TX-2, TX-7, TX-8, RS-14; CR-12 totals)  |  Decider: fixture:answers_remapped.json  |  Run: 2026-10-17T20:23:07+00:00
Prediction log sha256 (frozen before the outcome card was opened): `e7f2217e00e8ab3a…`

## Policy record

- Rule-maker: not stated; the Trade Ministry opened the investigation and published the recommendation; enacted not stated; the recommendation was published on 1 January, effective 1 April (year not stated).
- Stated aim: none stated
- C1: tariff on flat_rolled_and_long_steel in halvern; binds importers, protects sellers.domestic_steel. Source: "Importers of record must pay a tariff of 25% of the customs value on imports of flat-rolled and long steel products, for three years."
- Unclear U1: The standard for "sufficient quantity or quality" is not defined. Readings: U1-a: a product qualifies for exclusion if domestic supply is short in either quantity or quality. / U1-b: a product qualifies for exclusion only if domestic supply is short in both quantity and quality.
- Unclear U2: A review in the third year may extend it. Readings: U2-a: the tariff lapses at the end of three years unless the third-year review extends it; the length of any extension is not stated. / U2-b: the text gives the review power over the tariff's duration but does not say whether the review must take place or whether the tariff stays in force until it does.
- Unclear U3: Steel users may apply to exclude a product "not produced domestically in sufficient quantity or quality". Readings: U3-a: an excluded product is no longer subject to the 25% tariff for any importer. / U3-b: the exclusion benefits only the steel user that applied, and other importers of the same product remain subject to the tariff.
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(c1)` | binding | 0.85 | The domestic price rises by a substantial part of the tariff; foreign sellers do not absorb most of it. |
| `domestic_substitutes(c1)` | substitutability | 0.90 | Domestic producers make close substitutes for the covered imports. |
| `no_offset(c1)` | other | 0.68 | Lower imports reduce foreigners' purchases of the country's exports in the medium run; capital flows do not cancel it. |
| `input_not_replaceable(c1)` | substitutability | 0.65 | The taxed good is a material part of downstream costs and cannot be replaced at the old cost. |
| `competitors_exempt(c1)` | other | 0.85 | Many downstream users compete with sellers who do not face the higher input cost. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.current | price_paid | increase | short+ | B | TX-7 | {binding(c1)} | yes |
| C-2 | buyers.current | resources_available_other_uses | decrease | short+ | A | TX-1, TX-7 | {binding(c1)} | yes |
| C-3 | export_industries | quantity_supplied | decrease | medium+ | B | TX-7, TX-2, TX-8 | {binding(c1), no_offset(c1)} | yes |
| C-4 | general_fund | tax_revenue | increase | short+ | A | TX-1 | {} | yes |
| C-5 | importers | quantity_traded | decrease | short+ | B | TX-7, TX-2 | {binding(c1)} | yes |
| C-6 | importers | resources_available_other_uses | decrease | short+ | A | TX-1 | {} | yes |
| C-7 | manufacturers | quantity_supplied | decrease | medium+ | B | TX-7, RS-14 | {binding(c1), competitors_exempt(c1), input_not_replaceable(c1)} | yes |
| C-8 | sellers.domestic_steel | net_price_received | increase | short+ | B | TX-7 | {binding(c1), domestic_substitutes(c1)} | yes |
| C-9 | sellers.domestic_steel | quantity_supplied | increase | short+ | B | TX-7 | {binding(c1), domestic_substitutes(c1)} | yes |
| C-10 | workers.export_industries | employment | decrease | medium+ | B | TX-7, TX-2, TX-8 | {binding(c1), no_offset(c1)} | yes |

## Explanations

- C-1. Compared with no Halvern Steel Safeguard Order, price paid for buyers.current rises from the short run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: The domestic price rises by a substantial part of the tariff; foreign sellers do not absorb most of it (p = 0.85). Reported.
- C-2. Compared with no Halvern Steel Safeguard Order, resources available other uses for buyers.current falls from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: The domestic price rises by a substantial part of the tariff; foreign sellers do not absorb most of it (p = 0.85). Reported.
- C-3. Compared with no Halvern Steel Safeguard Order, quantity supplied for export_industries falls from the medium run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; TX-8: foreigners who sell less to the country earn less of its currency and so buy fewer of its exports. This holds if: The domestic price rises by a substantial part of the tariff; foreign sellers do not absorb most of it (p = 0.85); Lower imports reduce foreigners' purchases of the country's exports in the medium run; capital flows do not cancel it (p = 0.68). Reported.
- C-4. Compared with no Halvern Steel Safeguard Order, tax revenue for general_fund rises from the short run onward (tier A, visible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue. This holds if: no assumption. Reported.
- C-5. Compared with no Halvern Steel Safeguard Order, quantity traded for importers falls from the short run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: The domestic price rises by a substantial part of the tariff; foreign sellers do not absorb most of it (p = 0.85). Reported.
- C-6. Compared with no Halvern Steel Safeguard Order, resources available other uses for importers falls from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue. This holds if: no assumption. Reported.
- C-7. Compared with no Halvern Steel Safeguard Order, quantity supplied for manufacturers falls from the medium run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; RS-14: a dearer input is passed down to the output: its price rises where competitors face the same cost, and its sellers sell less where competitors are exempt. This holds if: The domestic price rises by a substantial part of the tariff; foreign sellers do not absorb most of it (p = 0.85); Many downstream users compete with sellers who do not face the higher input cost (p = 0.85); The taxed good is a material part of downstream costs and cannot be replaced at the old cost (p = 0.65). Reported.
- C-8. Compared with no Halvern Steel Safeguard Order, net price received for sellers.domestic_steel rises from the short run onward (tier B, visible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: The domestic price rises by a substantial part of the tariff; foreign sellers do not absorb most of it (p = 0.85); Domestic producers make close substitutes for the covered imports (p = 0.90). Reported.
- C-9. Compared with no Halvern Steel Safeguard Order, quantity supplied for sellers.domestic_steel rises from the short run onward (tier B, visible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more. This holds if: The domestic price rises by a substantial part of the tariff; foreign sellers do not absorb most of it (p = 0.85); Domestic producers make close substitutes for the covered imports (p = 0.90). Reported.
- C-10. Compared with no Halvern Steel Safeguard Order, employment for workers.export_industries falls from the medium run onward (tier B, invisible). Why: TX-7: a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; TX-8: foreigners who sell less to the country earn less of its currency and so buy fewer of its exports. This holds if: The domestic price rises by a substantial part of the tariff; foreign sellers do not absorb most of it (p = 0.85); Lower imports reduce foreigners' purchases of the country's exports in the medium run; capital flows do not cancel it (p = 0.68). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
