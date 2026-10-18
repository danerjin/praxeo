# Out-of-sample run of the existing rules on WE-010

Handbook example: `handbook/05_examples/WE-010_cigarette_tax_border.md`. Case: `cases/we010_marren`. Rules as they stood before any change for this step (`praxeo/rules/*.lp`, `praxeo/questions.py`, `praxeo/engine.py` untouched; rule base built from WE-013). Run: `python3 -m praxeo cases/we010_marren --out cases/we010_marren/sample_run`; compared on (actor, variable, sign, window) with the example's "Consequence list (normal form)".

## Summary

- Table rows: 34. Produced: 8 in full and 0 in part (a part means some of the row's actor classes or variables are missing). Not produced: 26.
- Engine rows reported (one per actor and variable; a group counts once per member): 13. In the table: 8. Not in the table but defensible: 5. WRONG: 0.
- Row C-31 (cigarette tax revenue rises) is produced with the right sign, but as a Tier A consequence with no premise. The handbook's TX-1 (1.1) says a rate rise needs the premise that the base does not fall enough to offset it (WE-010 A-16, p 0.8, Tier B). The engine does not know that K1 raises the rate of an existing tax.

Record notes (what the record could and could not say):

- Only K1 (the $1.50 to $3.50 per-pack increase) is a component. K2 (the floor-stock tax) is a second per_unit_tax whose rows would overwrite K1's under the same actors, so it is left in policy.txt only. K3 and K4 are enforcement, K5 an earmark: no instrument or rule the engine has.
- Roles filled: bound `stamping_agents`, buyer `smokers`, seller `retailers.marren`, revenue `officials.enforcement`, announcement_window true (introduced June, signed 1 October, effective 1 January), definition_line true (other tobacco at 25%). There is no field for the neighbouring states (`neighboring_jurisdictions`, `retailers.neighbors`) or for the border and interior subclasses.
- The unclear provision (use tax on cartons) is recorded with two readings and no reading facts.
- Answers (6): quantity_responds (A-2), buyers_bear (A-1), sellers_bear (A-3, the premise of C-14), stockpile_ahead (A-9), reshaping_pays (A-7) from the table; enforcement_budget_raised (0.2) is my estimate.

## Engine rows

| Actor | Variable | Sign | Window | Class | Where / why |
|---|---|---|---|---|---|
| `retailers.marren` | `net_price_received` | decrease |  | not in table, defensible | TX-2 with sellers_bear (A-3). The handbook signs it for the border retailers only (C-14), but A-1 (most of the increase passed on) leaves some with retailers everywhere; the interior retailers are not contradicted. |
| `retailers.marren` | `resources_available_other_uses` | decrease |  | not in table, defensible | TX-1: the side that bears part of the tax has less to spend. Follows from the row above. |
| `smokers` | `reclassification` | increase |  | not in table, defensible | RS-5 for the buyer side of the definition line. C-6 records the switch to other tobacco as quantity_substitute and C-7 as the producers' reclassification; same pattern, other variable and actor. |
| `stamping_agents` | `quantity_traded` | decrease |  | not in table, defensible | TX-2: the bound agents stamp fewer packs. The table lists the retailers (C-2) and the smokers (C-25). |
| `stamping_agents` | `reclassification` | increase |  | not in table, defensible | RS-5 for the bound actor. C-7 names `producers`, a role the record does not have. |
| `officials.enforcement` | `enforcement_cost` | increase |  | in table | C-32 (OC-3) |
| `officials.enforcement` | `tax_revenue` | increase |  | in table | C-31 (sign right; engine Tier A, no premise: TX-1 1.1 requires A-16 for a rate rise). The key also coincides with C-29 (other tobacco), which this is not. |
| `officials.enforcement` | `tax_revenue_vs_static_projection` | decrease |  | in table | C-21 |
| `retailers.marren` | `quantity_traded` | decrease |  | in table | C-2 (OC-4 and TX-2 wedge) |
| `smokers` | `price_paid` | increase |  | in table | C-1 |
| `smokers` | `quantity_traded` | increase | announcement | in table | C-8 (RS-8, stockpile_ahead = A-9) |
| `smokers` | `quantity_traded` | decrease |  | in table | C-25 (OC-4 prevented exchanges) |
| `smokers` | `resources_available_other_uses` | decrease |  | in table | C-24 |

## Table rows

| ID | Actor class | Variable | Sign | Status | Reason / engine row |
|---|---|---|---|---|---|
| C-1 | smokers | price_paid (stamped, in Marren) | increase | produced | smokers price_paid increase |
| C-2 | retailers.marren | quantity_traded (stamped, in Marren) | decrease | produced | retailers.marren quantity_traded decrease |
| C-3 | smokers.border | cross_border_purchases | increase | not produced | RS-4 / TX-4: cross-border purchases, the stores and the tax authorities across the line. No rule for a tax and no neighbour role in a per_unit_tax record (missing rule and record fact). |
| C-4 | intermediaries.bootleggers | informal_activity | increase | not produced | RS-3: informal activity (bootlegging, smuggling) and its investment (TS-2). No evasion rule for taxes (missing rule). |
| C-5 | intermediaries.smuggling_networks | informal_activity | increase | not produced | RS-3: informal activity (bootlegging, smuggling) and its investment (TS-2). No evasion rule for taxes (missing rule). |
| C-6 | smokers | quantity_substitute (other tobacco, e-cigarettes) | increase | not produced | RS-1 / TX-3: smokers turn to untaxed products. No quantity_substitute rule for the buyers of a taxed good (missing rule). |
| C-7 | producers | reclassification | increase | not produced | Actor: `producers` is not a role in the record; the engine's RS-5 rows name the agents and the smokers (missing record fact). |
| C-8 | smokers | quantity_traded (stamped packs, Oct–Dec) | increase | produced | smokers quantity_traded increase, window announcement |
| C-9 | stamping_agents, retailers.marren | compliance_cost | increase | not produced | TX-5: compliance cost of the stamping agents and retailers. Not encoded (missing rule). |
| C-10 | border retailers, health groups, producers | lobbying_effort | increase | not produced | RS-7: lobbying by border retailers, health groups and producers. No lobbying rule for a tax (missing rule). |
| C-11 | retailers.neighbors | quantity_traded (cigarettes and trip goods) | increase | not produced | RS-4 / TX-4: cross-border purchases, the stores and the tax authorities across the line. No rule for a tax and no neighbour role in a per_unit_tax record (missing rule and record fact). |
| C-12 | retailers.marren.border | quantity_traded (untaxed trip goods) | decrease | not produced | RS-9 / TX-3: untaxed trip goods and the border retailers' labour. Not encoded (missing rule), and the border subclass is not a role in the record. |
| C-13 | retailers.marren.border | employment, hours_worked (group) | at_least_one_decrease | not produced | RS-9 / TX-3: untaxed trip goods and the border retailers' labour. Not encoded (missing rule), and the border subclass is not a role in the record. |
| C-14 | retailers.marren.border | net_price_received (cigarettes) | decrease | not produced | Actor: the border subclass `retailers.marren.border` is not a role in the record; the class-level row appears under `retailers.marren` (see the engine rows). |
| C-15 | smokers.interior | tax_share_borne | increase | not produced | DM-1: `tax_share_borne` for smokers and their subclasses. Not encoded (missing rule). |
| C-16 | smokers.light | tax_share_borne | increase | not produced | DM-1: `tax_share_borne` for smokers and their subclasses. Not encoded (missing rule). |
| C-17 | buyers of informal cigarettes | search_cost | increase | not produced | RS-10: informal buyers' search cost, quality and information. Not encoded (missing rule). |
| C-18 | buyers of informal cigarettes | quality_variability | increase | not produced | RS-10: informal buyers' search cost, quality and information. Not encoded (missing rule). |
| C-19 | neighboring_jurisdictions | tax_revenue | increase | not produced | RS-4 / TX-4: cross-border purchases, the stores and the tax authorities across the line. No rule for a tax and no neighbour role in a per_unit_tax record (missing rule and record fact). |
| C-20 | officials.enforcement | tax_revenue (Marren sales tax on trip goods) | decrease | not produced | TX-10: other taxes' base (sales tax on trip goods, the tax on other tobacco). Not encoded (missing rule). The key (officials.enforcement, tax_revenue, increase) is produced for the cigarette tax, so C-29 is not counted. |
| C-21 | officials.enforcement | tax_revenue_vs_static_projection | decrease | produced | officials.enforcement tax_revenue_vs_static_projection decrease |
| C-22 | quit_program.clients | quantity_traded (services funded from general revenue) | decrease | not produced | SB-7: the earmark's effect on the quit program. No SB rules (missing rule). |
| C-24 | smokers (stamped buyers) | resources_available_other_uses | decrease | produced | smokers resources_available_other_uses decrease |
| C-25 | smokers, retailers.marren | quantity_traded (purchases forgone entirely) | decrease | produced | smokers and retailers.marren quantity_traded decrease |
| C-26 | smokers.border | search_cost | increase | not produced | OC-2: search cost of the border smokers' trips. Not encoded (missing rule). |
| C-27 | general_fund.recipients | resources_available_other_uses | increase | not produced | CR-8b / CR-12e: the general fund's recipients gain from the net revenue. Not encoded: the encoded OC-3 case names the payers, not the recipients (missing rule). |
| C-28 | buyers of informal cigarettes | quality_information | decrease | not produced | RS-10: informal buyers' search cost, quality and information. Not encoded (missing rule). |
| C-29 | officials.enforcement | tax_revenue (other tobacco products) | increase | not produced | TX-10: other taxes' base (sales tax on trip goods, the tax on other tobacco). Not encoded (missing rule). The key (officials.enforcement, tax_revenue, increase) is produced for the cigarette tax, so C-29 is not counted. |
| C-30 | smokers | tax_share_borne (relative to Marren sellers) | increase | not produced | DM-1: `tax_share_borne` for smokers and their subclasses. Not encoded (missing rule). |
| C-31 | officials.enforcement | tax_revenue (cigarette tax) | increase | produced | sign right; engine says Tier A with no premise (see summary) |
| C-32 | officials.enforcement | enforcement_cost | increase | produced | officials.enforcement enforcement_cost increase |
| C-33 | factor_owners.specific (Marren border retail) | asset_value | decrease | not produced | SB-4: asset values of the retail sites on both sides of the line. The SB-4 rule covers a tariff's owners (missing rule for a tax; no owner role). |
| C-34 | factor_owners.specific (sites across the line) | asset_value | increase | not produced | SB-4: asset values of the retail sites on both sides of the line. The SB-4 rule covers a tariff's owners (missing rule for a tax; no owner role). |
| — | retailers.neighbors (new stores) | earnings | ambiguous | not produced | Ambiguous by design (DM-3): new stores' earnings across the line; no rule. |

## Reading

Eight of 34 rows are produced and nothing is contradicted. The produced rows are exactly the ones WE-013's tax and tariff chains give: price, quantity, resources, enforcement cost, shortfall against the static projection, and the announcement-window rush (RS-8), which is the one new capability this example uses and which transfers: the same rule that makes steel users bring imports forward makes smokers buy cartons before 1 January (C-8).

The border mechanism that gives WE-010 most of its rows (RS-4, RS-9, RS-3, RS-10, DM-1, TX-10) is not in the rule base for taxes. The single gap that blocks most rows is the absence of a neighbour: no field in the record and no rule. The one near-error is C-31: the engine presents the cigarette revenue as a Tier A certainty, where the handbook's TX-1 (1.1) makes it Tier B with a premise for a rate rise, and this record states the rise.
