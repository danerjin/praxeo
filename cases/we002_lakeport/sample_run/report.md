# Thin-slice run: Lakeport Beverage Tax

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-18T20:31:30+00:00
Prediction log sha256 (frozen before the outcome card was opened): `88cdbfde96927dcb…`

## Policy record

- Rule-maker: Lakeport town; enacted not stated, effective not stated.
- Stated aim: none stated
- k1: per_unit_tax on sweetened_drinks in lakeport; binds distributors, protects None. Source: "Three neighboring towns, each 10 to 15 minutes' drive from most Lakeport homes, have no such tax."
- Unclear U1: Whether approved providers may include existing private pre-schools on equal terms. Readings: U1-a: yes, with limits on places / U1-b: no
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `quantity_responds(k1)` | substitutability | 0.90 | At least one side can reduce the quantity it trades in response to the tax. |
| `buyers_bear(k1)` | other | 0.90 | Part of the tax is passed on to buyers: the price they pay rises. |
| `sellers_bear(k1)` | other | 0.40 | Part of the tax stays with sellers: the price they keep after tax falls. |
| `untaxed_substitutes(k1)` | substitutability | 0.90 | Buyers have acceptable untaxed substitutes they can turn to. |
| `cross_border_feasible(k1)` | mobility | 0.80 | Enough buyers can easily buy across the boundary, where the tax does not apply. |
| `reshaping_pays(k1)` | other | 0.70 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.lakeport | price_paid | increase | short+ | B | TX-2 | {buyers_bear(k1), quantity_responds(k1)} | yes |
| C-2 | buyers.lakeport | quantity_substitute | increase | short+ | B | TX-2, RS-1, TX-3 | {quantity_responds(k1), untaxed_substitutes(k1)} | yes |
| C-3 | buyers.lakeport | quantity_traded | decrease | short+ | B | TX-2, OC-4 | {quantity_responds(k1)} | yes |
| C-4 | buyers.lakeport | reclassification | increase | short+ | B | TX-2, RS-5, TX-4 | {quantity_responds(k1), reshaping_pays(k1)} | yes |
| C-5 | buyers.lakeport | resources_available_other_uses | decrease | short+ | A | TX-1, TX-2 | {buyers_bear(k1)} | yes |
| C-6 | buyers.lakeport.mobile | cross_border_purchases | increase | short+ | B | TX-2, TX-4 | {cross_border_feasible(k1), quantity_responds(k1)} | yes |
| C-7 | distributors | compliance_cost | increase | short+ | A | TX-1, TX-5 | {} | yes |
| C-8 | distributors | quantity_traded | decrease | short+ | B | TX-2 | {quantity_responds(k1)} | yes |
| C-9 | distributors | reclassification | increase | short+ | B | TX-2, RS-5, TX-4 | {quantity_responds(k1), reshaping_pays(k1)} | yes |
| C-10 | officials.enforcement | enforcement_cost | increase | short+ | A | TX-1, OC-3 | {} | yes |
| C-11 | officials.enforcement | tax_revenue | increase | short+ | A | TX-1 | {} | yes |
| C-12 | officials.enforcement | tax_revenue_vs_static_projection | decrease | short+ | B | TX-2, TX-9 | {quantity_responds(k1)} | yes |
| C-13 | retailers.lakeport | net_price_received | decrease | short+ | B | TX-2 | {quantity_responds(k1), sellers_bear(k1)} | no |
| C-14 | retailers.lakeport | quantity_traded | decrease | short+ | B | TX-2, OC-4 | {quantity_responds(k1)} | yes |
| C-15 | retailers.lakeport | resources_available_other_uses | decrease | short+ | A | TX-1, TX-2 | {sellers_bear(k1)} | no |
| C-16 | retailers.neighbors | quantity_traded | increase | short+ | B | TX-2, TX-4 | {cross_border_feasible(k1), quantity_responds(k1)} | yes |

## Explanations

- C-1. Compared with no Lakeport Beverage Tax, price paid for buyers.lakeport rises from the short run onward (tier B, visible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: Part of the tax is passed on to buyers: the price they pay rises (p = 0.90); At least one side can reduce the quantity it trades in response to the tax (p = 0.90). Reported.
- C-2. Compared with no Lakeport Beverage Tax, quantity substitute for buyers.lakeport rises from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; RS-1: when a good becomes dearer, buyers turn to substitutes; TX-3: buyers of a taxed good turn to the untaxed alternatives they have. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.90); Buyers have acceptable untaxed substitutes they can turn to (p = 0.90). Reported.
- C-3. Compared with no Lakeport Beverage Tax, quantity traded for buyers.lakeport falls from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; OC-4: exchanges that no longer happen are lost to both sides. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.90). Reported.
- C-4. Compared with no Lakeport Beverage Tax, reclassification for buyers.lakeport rises from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; RS-5: owners move units out of the rule's reach; TX-4: where an untaxed place is within reach, buyers who can cross the boundary buy there and the sellers across it gain their custom. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.90); Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.70). Reported.
- C-5. Compared with no Lakeport Beverage Tax, resources available other uses for buyers.lakeport falls from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: Part of the tax is passed on to buyers: the price they pay rises (p = 0.90). Reported.
- C-6. Compared with no Lakeport Beverage Tax, cross border purchases for buyers.lakeport.mobile rises from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; TX-4: where an untaxed place is within reach, buyers who can cross the boundary buy there and the sellers across it gain their custom. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.80); At least one side can reduce the quantity it trades in response to the tax (p = 0.90). Reported.
- C-7. Compared with no Lakeport Beverage Tax, compliance cost for distributors rises from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; TX-5: whoever must record, file or collect a tax bears the cost of doing so. This holds if: no assumption. Reported.
- C-8. Compared with no Lakeport Beverage Tax, quantity traded for distributors falls from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.90). Reported.
- C-9. Compared with no Lakeport Beverage Tax, reclassification for distributors rises from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; RS-5: owners move units out of the rule's reach; TX-4: where an untaxed place is within reach, buyers who can cross the boundary buy there and the sellers across it gain their custom. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.90); Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.70). Reported.
- C-10. Compared with no Lakeport Beverage Tax, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-11. Compared with no Lakeport Beverage Tax, tax revenue for officials.enforcement rises from the short run onward (tier A, visible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue. This holds if: no assumption. Reported.
- C-12. Compared with no Lakeport Beverage Tax, tax revenue vs static projection for officials.enforcement falls from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; TX-9: TX-9. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.90). Reported.
- C-13. Compared with no Lakeport Beverage Tax, net price received for retailers.lakeport falls from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.90); Part of the tax stays with sellers: the price they keep after tax falls (p = 0.40). Not reported: an assumption is below the 0.5 cut-off.
- C-14. Compared with no Lakeport Beverage Tax, quantity traded for retailers.lakeport falls from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; OC-4: exchanges that no longer happen are lost to both sides. This holds if: At least one side can reduce the quantity it trades in response to the tax (p = 0.90). Reported.
- C-15. Compared with no Lakeport Beverage Tax, resources available other uses for retailers.lakeport falls from the short run onward (tier A, invisible). Why: TX-1: a tax that is collected takes resources from those who bear it and yields revenue; TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks. This holds if: Part of the tax stays with sellers: the price they keep after tax falls (p = 0.40). Not reported: an assumption is below the 0.5 cut-off.
- C-16. Compared with no Lakeport Beverage Tax, quantity traded for retailers.neighbors rises from the short run onward (tier B, invisible). Why: TX-2: a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks; TX-4: where an untaxed place is within reach, buyers who can cross the boundary buy there and the sellers across it gain their custom. This holds if: Enough buyers can easily buy across the boundary, where the tax does not apply (p = 0.80); At least one side can reduce the quantity it trades in response to the tax (p = 0.90). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
