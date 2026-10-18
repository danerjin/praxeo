# Out-of-sample run of the existing rules on WE-002

Handbook example: `handbook/05_examples/WE-002_drinks_excise.md`. Case: `cases/we002_lakeport`. Rules as they stood before any change for this step (`praxeo/rules/*.lp`, `praxeo/questions.py`, `praxeo/engine.py` untouched; rule base built from WE-013). Run: `python3 -m praxeo cases/we002_lakeport --out cases/we002_lakeport/sample_run`; compared on (actor, variable, sign, window) with the example's "Consequence list (normal form)".

## Summary

- Table rows: 26. Produced: 5 in full and 0 in part (a part means some of the row's actor classes or variables are missing). Not produced: 21.
- Engine rows reported (one per actor and variable; a group counts once per member): 10. In the table: 5. Not in the table but defensible: 5. WRONG: 0.

Record notes (what the record could and could not say):

- Only K1 (the excise tax) is a component. K2 (the earmark, a `lump_sum_subsidy`) and K3 (administration; `Enforcement` is not an instrument in 02_ontology.md section 2.3) are in policy.txt but cannot be components the rules use: no rule covers the spending of the revenue.
- Roles filled: bound_actor `distributors`, buyer_actor `buyers.lakeport`, seller_actor `retailers.lakeport`, revenue_actor `officials.enforcement`, taxpayer_actor `taxpayers`, definition_line true (the exemptions draw a line). No neighbour, mobile-buyer, producer, worker or subsidy-recipient role exists for a per_unit_tax, so the record has nowhere to put them.
- U1 (approved providers) is recorded with two readings and no `reading_facts`: no rule depends on it.
- Answers (5): quantity_responds, buyers_bear, reshaping_pays from A-2, A-1, A-4; sellers_bear (0.4) and enforcement_budget_raised (0.15) are my estimates, marked as such in the rationale.

## Engine rows

| Actor | Variable | Sign | Window | Class | Where / why |
|---|---|---|---|---|---|
| `buyers.lakeport` | `reclassification` | increase |  | not in table, defensible | TX-4 with RS-5 (definition_line, reshaping_pays = A-4). The handbook puts the reformulation with `producers` (C-6) and records the buyers' switch as quantity_substitute (C-5); the buyers' row is the same switch under another variable. Not contradicted. |
| `distributors` | `quantity_traded` | decrease |  | not in table, defensible | TX-2: the bound distributors deliver less taxed drink. The handbook lists the buyers' side (C-2, C-28); this is the same trade seen from the seller. |
| `distributors` | `reclassification` | increase |  | not in table, defensible | RS-5 for the bound actor. C-6 names `producers`, a role the record does not have; the distributors are who reformulate or relabel what they deliver. Same pattern, different actor. |
| `officials.enforcement` | `tax_revenue` | increase |  | not in table, defensible | TX-1. C-25 gives this row to the `town budget`; the record's revenue_actor is `officials.enforcement`, which the handbook uses for C-18 and C-21 in the same table. Naming only. |
| `retailers.lakeport` | `quantity_traded` | decrease |  | not in table, defensible | OC-4, the sellers' side of the prevented drink sales (handbook OC-4: both parties lose the exchange). The key coincides with C-11, but C-11 is the other groceries bought on drink trips (RS-4, RS-9), which the engine does not produce; this row is not credited to C-11. |
| `buyers.lakeport` | `price_paid` | increase |  | in table | C-1 (TX-2, A-1) |
| `buyers.lakeport` | `quantity_traded` | decrease |  | in table | C-2 (OC-4 prevented exchanges, A-1, A-2) |
| `buyers.lakeport` | `resources_available_other_uses` | decrease |  | in table | C-15 (TX-1, OC-1) |
| `officials.enforcement` | `enforcement_cost` | increase |  | in table | C-18 (OC-3) |
| `officials.enforcement` | `tax_revenue_vs_static_projection` | decrease |  | in table | C-21 (TX-9) |

## Table rows

| ID | Actor class | Variable | Sign | Status | Reason / engine row |
|---|---|---|---|---|---|
| C-1 | buyers.lakeport | price_paid (taxed drinks, in town) | increase | produced | buyers.lakeport price_paid increase |
| C-2 | buyers.lakeport | quantity_traded (taxed drinks, in town) | decrease | produced | buyers.lakeport quantity_traded decrease (OC-4) |
| C-3 | families.preschool | price_paid (pre-school) | decrease | not produced | SB-2, SB-3, SB-7, SB-8 and CR-9/CR-12: the spending of the earmark. The record has no subsidy component and the rule base has no SB rules (missing rules). |
| C-4 | buyers.lakeport.mobile | cross_border_purchases | increase | not produced | RS-4 / TX-4: cross-border purchases and the sellers across the line. No rule gives them for a tax, and a per_unit_tax record has no neighbour or mobile-buyer role (missing rule and missing record fact). |
| C-5 | buyers.lakeport | quantity_substitute (exempt drinks) | increase | not produced | RS-1 / TX-3: quantity_substitute for the buyers of a taxed good. No such rule for a per-unit tax (the tariff rules sign it only for the buyers of downstream users) (missing rule). |
| C-6 | producers | reclassification | increase | not produced | Actor: `producers` is not a role in the record; the engine's RS-5 row names the bound distributors and the buyers (missing record fact: the producers). |
| C-7 | distributors | compliance_cost | increase | not produced | TX-5: compliance cost of the tax. Not encoded (missing rule), although it is Tier A. |
| C-8 | providers.private_preschool | quantity_demanded (paid places) | decrease | not produced | SB-2, SB-3, SB-7, SB-8 and CR-9/CR-12: the spending of the earmark. The record has no subsidy component and the rule base has no SB rules (missing rules). |
| C-9 | retailers, distributors, approved providers | lobbying_effort | increase | not produced | RS-7 / SB-5: lobbying. The lobbying rules cover a tariff that is renewable or has relief applicants; nothing for a tax (missing rule). |
| C-10 | retailers.neighbors | quantity_traded (all goods) | increase | not produced | RS-4 / TX-4: cross-border purchases and the sellers across the line. No rule gives them for a tax, and a per_unit_tax record has no neighbour or mobile-buyer role (missing rule and missing record fact). |
| C-11 | retailers.lakeport | quantity_traded (other groceries on drink trips) | decrease | not produced | RS-4 / RS-9: other groceries bought on the same trip. Missing rule. The key (retailers.lakeport, quantity_traded, decrease) is produced, but by OC-4 for the drinks, so the row is not counted. |
| C-12 | retailers.lakeport | employment, hours_worked | at_least_one_decrease | not produced | TX-3 / OC-5: employment and hours of the sellers as a group (and of those funded by the revenue). The labour group is encoded for a tariff only (missing rule). |
| C-13 | buyers.lakeport.immobile | tax_share_borne | increase | not produced | DM-1: `tax_share_borne` for subclasses (mobile and immobile buyers). Not encoded, and the record has no such subclasses (missing rule and record fact). |
| C-14 | providers.private_preschool | number_of_sellers | U1-a: ambiguous; U1-b: decrease | not produced | SB-3, RS-6, CR-1 and CR-12b under U1: needs subsidy rules and reading facts (missing rule). |
| C-15 | buyers.lakeport | resources_available_other_uses | decrease | produced | buyers.lakeport resources_available_other_uses decrease |
| C-16 | buyers.lakeport.mobile | search_cost | increase | not produced | RS-4 / TX-4: cross-border purchases and the sellers across the line. No rule gives them for a tax, and a per_unit_tax record has no neighbour or mobile-buyer role (missing rule and missing record fact). |
| C-18 | officials.enforcement | enforcement_cost | increase | produced | officials.enforcement enforcement_cost increase |
| C-20 | town budget | resources_available_other_uses (general fund) | increase | not produced | SB-2, SB-3, SB-7, SB-8 and CR-9/CR-12: the spending of the earmark. The record has no subsidy component and the rule base has no SB rules (missing rules). |
| C-21 | officials.enforcement | tax_revenue_vs_static_projection | decrease | produced | officials.enforcement tax_revenue_vs_static_projection decrease |
| C-22 | families.preschool (would have paid anyway) | resources_available_other_uses | increase | not produced | SB-2, SB-3, SB-7, SB-8 and CR-9/CR-12: the spending of the earmark. The record has no subsidy component and the rule base has no SB rules (missing rules). |
| C-23 | sellers (forgone purchases) | employment, hours_worked | at_least_one_decrease | not produced | TX-3 / OC-5: employment and hours of the sellers as a group (and of those funded by the revenue). The labour group is encoded for a tariff only (missing rule). |
| C-24 | pre-school providers | employment, hours_worked | at_least_one_increase | not produced | TX-3 / OC-5: employment and hours of the sellers as a group (and of those funded by the revenue). The labour group is encoded for a tariff only (missing rule). |
| C-25 | town budget | tax_revenue | increase | not produced | Actor name: the engine produces tax_revenue increase, but for `officials.enforcement` (see the engine rows), not for the `town budget`. |
| C-26 | families.preschool (paid places) | price_substitute (private fees) | decrease | not produced | SB-2, SB-3, SB-7, SB-8 and CR-9/CR-12: the spending of the earmark. The record has no subsidy component and the rule base has no SB rules (missing rules). |
| C-27 | families.preschool | quantity_traded (places used, all providers) | increase | not produced | SB-2, SB-3, SB-7, SB-8 and CR-9/CR-12: the spending of the earmark. The record has no subsidy component and the rule base has no SB rules (missing rules). |
| C-28 | buyers.lakeport | quantity_demanded (taxed drinks, from all sources) | decrease | not produced | Variable: quantity_demanded of taxed drinks from all sources (TX-2 with RS-1 across the line). The tax rules sign quantity_traded only (missing rule). |

## Reading

WE-002 is the case with the thinnest overlap with the rule base: the table is half about the earmark's spending (SB) and half about avoidance across a nearby border (RS-4, RS-9). Of the tax rules, the ones built from WE-013 (TX-1, TX-2, TX-9, OC-3, OC-4, RS-5) transfer without change and give every row they should (C-1, C-2, C-15, C-18, C-21). Nothing the engine reports contradicts the table.

What the run shows about generality. (1) The tax rules assume a private seller and the roles of a tariff; a per_unit_tax record cannot name a neighbouring jurisdiction or a producer. (2) TX-5 (compliance cost, Tier A) and the TX-3 group are missing for taxes. (3) The tax revenue is attached to the same actor as the enforcement cost, while the handbook gives them to the budget and to the agency. None of these is a fit to WE-002; each is a handbook pattern the rule base does not yet state.
