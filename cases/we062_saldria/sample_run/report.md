# Thin-slice run: Saldria Plastic Packaging Tax Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-18T20:31:38+00:00
Prediction log sha256 (frozen before the outcome card was opened): `340489d0b7608534…`

## Policy record

- Rule-maker: Parliament of Saldria; enacted 2027-06-28, effective 2028-01-01.
- Stated aim: none stated
- k1: per_unit_tax on plastic_packaging_components in saldria; binds converters, protects None. Source: "A tax of 200 T per tonne is charged on plastic packaging components (a component in which plastic is the heaviest material by weight) manufactured in or imported into Saldria, empty or around imported goods, on the manufacturer or the importer of record, with quarterly returns."
- Unclear U1: How the 30% recycled content is measured. Readings: U1-a: per component / U1-b: averaged over the person's components in the quarter
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `quantity_responds(k1)` | substitutability | 0.85 | At least one side can reduce the quantity it trades in response to the tax. |
| `buyers_bear(k1)` | other | 0.75 | Part of the tax is passed on to buyers: the price they pay rises. |
| `sellers_bear(k1)` | other | 0.75 | Part of the tax stays with sellers: the price they keep after tax falls. |
| `untaxed_substitutes(k1)` | substitutability | 0.80 | Buyers have acceptable untaxed substitutes they can turn to. |
| `input_not_replaceable(k1)` | substitutability | 0.75 | The taxed good is a material part of downstream costs and cannot be replaced at the old cost. |
| `stockpile_ahead(k1)` | expectations | 0.75 | Buyers and importers can store the good and order ahead of the effective date. |
| `reshaping_pays(k1)` | other | 0.65 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.packaged_goods | price_paid | increase | medium+ | B | TX-2, RS-14 | {buyers_bear(k1), input_not_replaceable(k1), quantity_responds(k1)} | yes |
| C-2 | buyers.packaged_goods | quantity_demanded | decrease | medium+ | B | TX-2, RS-14, CR-4 | {buyers_bear(k1), input_not_replaceable(k1), quantity_responds(k1)} | yes |
| C-3 | converters | compliance_cost | increase | short+ | A | TX-1, TX-5 | {} | yes |
| C-4 | converters | net_price_received | decrease | short+ | B | TX-2 | {quantity_responds(k1), sellers_bear(k1)} | yes |
| C-5 | converters | quantity_traded | decrease | short+ | B | TX-2 | {quantity_responds(k1)} | yes |
| C-6 | converters | reclassification | increase | short+ | B | TX-2, RS-5, TX-4 | {quantity_responds(k1), reshaping_pays(k1)} | yes |
| C-7 | converters | resources_available_other_uses | decrease | short+ | A | TX-1, TX-2 | {sellers_bear(k1)} | yes |
| C-8 | officials.enforcement | enforcement_cost | increase | short+ | A | TX-1, OC-3 | {} | yes |
| C-9 | packaging_users | price_paid | increase | short+ | B | TX-2 | {buyers_bear(k1), quantity_responds(k1)} | yes |
| C-10 | packaging_users | quantity_substitute | increase | short+ | B | TX-2, RS-1, TX-3 | {quantity_responds(k1), untaxed_substitutes(k1)} | yes |
| C-11 | packaging_users | quantity_traded | decrease | short+ | B | TX-2, OC-4 | {quantity_responds(k1)} | yes |
| C-12 | packaging_users | quantity_traded [announcement window] | increase | short | B | RS-8 | {stockpile_ahead(k1)} | yes |
| C-13 | packaging_users | reclassification | increase | short+ | B | TX-2, RS-5, TX-4 | {quantity_responds(k1), reshaping_pays(k1)} | yes |
| C-14 | packaging_users | resources_available_other_uses | decrease | short+ | A | TX-1, TX-2 | {buyers_bear(k1)} | yes |
| C-15 | state budget | tax_revenue | increase | short+ | A | TX-1 | {} | yes |
| C-16 | state budget | tax_revenue_vs_static_projection | decrease | short+ | B | TX-2, TX-9 | {quantity_responds(k1)} | yes |

## Explanations

- C-1. Compared with no Saldria Plastic Packaging Tax Act, price paid for buyers.packaged_goods rises from the medium run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; RS-14: a dearer input is passed down to the output: its price rises where competitors face the same cost, and its sellers sell less where competitors are exempt. This holds if: Part of the tax is passed on to buyers: the price they pay rises (p = 0.75); The taxed good is a material part of downstream costs and cannot be replaced at the old cost (p = 0.75); At least one side can reduce the quantity it trades in response to the tax (p = 0.85). Reported.
- C-2. Compared with no Saldria Plastic Packaging Tax Act, quantity demanded for buyers.packaged_goods falls from the medium run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; RS-14: a dearer input is passed down to the output: its price rises where competitors face the same cost, and its sellers sell less where competitors are exempt; CR-4: buyers who face a higher price take fewer units. This holds if: Part of the tax is passed on to buyers: the price they pay rises (p = 0.75); The taxed good is a material part of downstream costs and cannot be replaced at the old cost (p = 0.75); At least one side can reduce the quantity it trades in response to the tax (p = 0.85). Reported.
- C-3. Compared with no Saldria Plastic Packaging Tax Act, compliance cost for converters rises from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; TX-5: whoever must record, file or collect a tax bears the cost of doing so. This holds if: no assumption. Reported.
- C-4. Compared with no Saldria Plastic Packaging Tax Act, net price received for converters falls from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.85); Part of the tax stays with sellers: the price they keep after tax falls (p = 0.75). Reported.
- C-5. Compared with no Saldria Plastic Packaging Tax Act, quantity traded for converters falls from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.85). Reported.
- C-6. Compared with no Saldria Plastic Packaging Tax Act, reclassification for converters rises from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; RS-5: owners move units out of the rule's reach; TX-4: where an untaxed place is within reach, buyers who can cross the boundary buy there and the sellers across it gain their custom. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.85); Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.65). Reported.
- C-7. Compared with no Saldria Plastic Packaging Tax Act, resources available other uses for converters falls from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: Part of the tax stays with sellers: the price they keep after tax falls (p = 0.75). Reported.
- C-8. Compared with no Saldria Plastic Packaging Tax Act, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-9. Compared with no Saldria Plastic Packaging Tax Act, price paid for packaging_users rises from the short run onward (tier B, visible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: Part of the tax is passed on to buyers: the price they pay rises (p = 0.75); At least one side can reduce the quantity it trades in response to the tax (p = 0.85). Reported.
- C-10. Compared with no Saldria Plastic Packaging Tax Act, quantity substitute for packaging_users rises from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; RS-1: when a good becomes dearer, buyers turn to substitutes; TX-3: buyers of a taxed good turn to the untaxed alternatives they have. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.85); Buyers have acceptable untaxed substitutes they can turn to (p = 0.80). Reported.
- C-11. Compared with no Saldria Plastic Packaging Tax Act, quantity traded for packaging_users falls from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; OC-4: exchanges that no longer happen are lost to both sides. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.85). Reported.
- C-12. Compared with no Saldria Plastic Packaging Tax Act, quantity traded for packaging_users rises in the announcement window (before the effective date), in the short run (tier B, invisible). Why: RS-8: a measure announced before it takes effect treats the same action differently by date, so actors move it toward the favourable window. This holds if: Buyers and importers can store the good and order ahead of the effective date (p = 0.75). Reported.
- C-13. Compared with no Saldria Plastic Packaging Tax Act, reclassification for packaging_users rises from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; RS-5: owners move units out of the rule's reach; TX-4: where an untaxed place is within reach, buyers who can cross the boundary buy there and the sellers across it gain their custom. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.85); Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.65). Reported.
- C-14. Compared with no Saldria Plastic Packaging Tax Act, resources available other uses for packaging_users falls from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: Part of the tax is passed on to buyers: the price they pay rises (p = 0.75). Reported.
- C-15. Compared with no Saldria Plastic Packaging Tax Act, tax revenue for state budget rises from the short run onward (tier A, visible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue. This holds if: no assumption. Reported.
- C-16. Compared with no Saldria Plastic Packaging Tax Act, tax revenue vs static projection for state budget falls from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; TX-9: TX-9. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.85). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
