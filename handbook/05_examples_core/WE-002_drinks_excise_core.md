# WE-002 / Analysis: Local excise tax on sweetened drinks, earmarked for pre-school (core-only re-run)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

Rule set: the core rules CR-1 to CR-12 (`../04a_core_rules.md`), AX-1 and LW-1 to LW-10 (`../01_foundations.md`), and arithmetic. No pattern is cited. New premises that the derivations needed are numbered A-N1, A-N2, ... and are listed in section 10 and under "Gaps found".

## 1. Policy record

**Lakeport Beverage Tax.** Lakeport is a town of about 150,000 people. Three neighboring towns, each 10 to 15 minutes' drive from most Lakeport homes, have no such tax. Many Lakeport households already do part of their grocery shopping in large stores just outside the town line.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Excise tax | `per_unit_tax` | Drinks with added sugar, distributed to retailers in Lakeport | Distributors | 1.5 cents per fluid ounce, collected from distributors on deliveries into the town | Drinks sweetened only with non-caloric sweeteners; milk-based drinks; 100% juice |
| K2 Earmark | `lump_sum_subsidy` | Pre-school places | Town | Revenue funds free pre-school places for 3- and 4-year-olds, run by the town and by approved providers | None |
| K3 Administration | Enforcement | K1 | Town revenue department | Distributor registration, monthly returns, audits | None |

Unclear provisions: whether approved providers may include existing private pre-schools on equal terms. Assumed yes, with limits on places.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
| --- | --- | --- | --- |
| K1 Excise tax | binary (forced payment from distributors to the town) | Yes: a per-unit charge binds at any price (pass-through A-1) | CR-1, CR-5c, CR-4, CR-7b, CR-9, CR-8 |
| K2 Earmark | binary (the town gives free places) | Binding on the town's spending; net effect on places depends on A-8 and A-N1 | CR-1, CR-4, CR-8d, CR-9 |
| K3 Administration | binary (paperwork attached to distribution) | Yes for registered distributors | CR-1, CR-8c |

**CR-1 operations, by component and actor class.** Operation 1: removes an option; 2: adds an option; 3: changes what an option brings; 4: transfers means.

| Component | Actor class | CR-1 operations |
| --- | --- | --- |
| K1 | distributors | 3 (a payment of 1.5 cents per ounce attached to delivering covered drinks into Lakeport); 4 (means transferred to the town) |
| K1 | sellers.current (Lakeport retailers) | none directly; the wholesale terms they face change (CR-9, input_to) |
| K1 | buyers.current (Lakeport drink buyers) | none directly; the shelf price changes through CR-5c (A-1) |
| K1 | drink makers | 3 (the covered form now carries the charge; the exempt forms do not) |
| K2 | families.preschool_age | 2 (a free pre-school place added) |
| K2 | sellers.substitutes (private pre-schools) | U1-a: 2 (option to supply funded places, with limits); U1-b: none directly; their customers' options change (CR-9) |
| K2 | town budget | 4 (receives the revenue; spends it on places) |
| K3 | distributors | 3 (registration, monthly returns, audits) |
| K3 | officials.enforcement | 2 (audit powers) |

## 3. Actor classes

| Actor class | Role | How its options change |
| --- | --- | --- |
| distributors | Pay the tax on deliveries into Lakeport | Charge attached to Lakeport deliveries (K1); paperwork (K3) |
| sellers.current (Lakeport retailers) | Sell drinks and groceries in Lakeport | Higher wholesale cost of covered drinks; buyers' options change |
| buyers.current | Lakeport residents who buy drinks | Higher shelf price for covered drinks; untaxed options across the line and in exempt drinks |
| buyers.low_mobility | Buyers with little access to cross-border shopping or substitutes | Same as above, with fewer alternatives |
| drink makers | Produce covered and exempt drinks | Covered form taxed, exempt form not |
| sellers.substitutes (exempt drinks) | Sell water, diet drinks, milk drinks, juice | Demand changes through CR-9 (substitute) |
| sellers.complements (Lakeport grocers) | Sell goods bought on the same trip | Trips change through CR-9 (complement, trip) |
| neighboring_jurisdictions (retailers across the line) | Sell untaxed drinks and groceries | Demand from Lakeport shoppers changes (across_border) |
| families.preschool_age | Families with 3- and 4-year-olds | Free place added (K2) |
| sellers.substitutes (private pre-schools) | Sell paid places | Free substitute appears; possible approval (U1) |
| input_suppliers (pre-school staff) | Work in pre-schools | Demand for staff changes (CR-9, input_to) |
| officials.enforcement (town revenue department) | Collects and audits | New duties (K3) |
| town budget | Receives revenue, funds places | Revenue earmarked; general funds freed (CR-8d) |

## 4. Direct effect

CR-1 and CR-2: the charge on distributors reaches the shelf through the wholesale exchange; the earmark adds a free option for families.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | buyers.current | price_paid (covered drinks in Lakeport) | increase | short | CR-1 (op 3 on distributors, K1) → CR-9 (wholesale terms) → CR-5c (the range of terms moves with what the seller must give) | A-1 |
| C-2 | town budget | tax_revenue | increase | short | CR-1 (op 4, K1) → CR-8b (every payment is a receipt); counterfactual revenue is zero | none |
| C-3 | families.preschool_age | price_paid (pre-school places) | decrease | short | CR-1 (op 2, K2: free place added) → CR-4 mirror (x: paid place, y: free place) → CR-3b | A-6 |
| C-26 | buyers.current | resources_available_other_uses | decrease | short | C-1 → CR-8b (tax paid by those who keep buying is withdrawn from their other uses) and CR-3a (those who switch fall back to a lower-ranked option) | A-1 |
| C-27 | families.preschool_age | resources_available_other_uses | increase | medium | C-3 → CR-8b (the fee no longer paid stays with the family; it is matched by C-26) | A-6 |

## 5. Responses

CR-4 pairs of options examined for each actor class (substitute, adjust terms, evade, relocate, reclassify, exit, lobby, change timing, enter), with CR-6 where a price is fixed and CR-5 where an exchange is prevented or compelled.

| Actor class | Pair of options (CR-4) or rule | Result |
| --- | --- | --- |
| buyers.current | CR-4 (x: covered drink, y: exempt drink or none) | Some substitute (A-2) |
| buyers.current | CR-4 (x: buy in Lakeport, y: buy across the town line) | Some relocate purchases (A-3) |
| buyers.current | CR-4c (last units first given up) | Fewer units bought |
| drink makers | CR-4 (x: covered form, y: exempt form) | Some reformulate or relabel (A-4) |
| distributors | CR-4 (x: comply, y: evade) | A-5, p 0.3: not reported |
| distributors | CR-7a (x: deliver to Lakeport, y: deliver to untaxed towns) | Mobile; burden moves to less mobile sides (CR-7b, A-N2) |
| distributors | CR-4 (x: accept, y: lobby for repeal or wider exemptions) | Some lobby (A-N3) |
| sellers.substitutes (private pre-schools) | CR-4 mirror (x: accept the program, y: lobby to keep or widen approval) | Approved providers lobby to keep it (A-N3) |
| Lakeport retailers | CR-10a (x: take delivery after the effective date, y: before) | Record gives no dates: not reported |
| families.preschool_age | CR-4 mirror (x: paid private place, y: free place); (x: home or informal care, y: free place) | Some switch (A-6, A-N4) |
| sellers.substitutes (private pre-schools) | CR-7a (x: run paid places, y: other use of premises and staff); under U1-a, also supply funded places | Exit under U1-b; ambiguous under U1-a |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-4 | buyers.current | quantity_traded (covered drinks sold in Lakeport) | decrease | short | C-1 → CR-4c (last units first given up) and CR-4 (x: covered drink, y: exempt drink; x: buy in Lakeport, y: buy across the line) | A-1, A-2, A-3 |
| C-5 | buyers.current | cross_border_purchases | increase | short | C-1 → CR-4 (x: buy in Lakeport, y: buy across the town line) | A-1, A-3 |
| C-6 | sellers.substitutes (exempt drinks) | quantity_substitute (exempt drinks) | increase | short | C-1 → CR-4 (x: covered drink, y: exempt drink) → CR-9 (substitute) | A-1, A-2 |
| C-7 | drink makers | reclassification | increase | medium | CR-1 (op 3 on the covered form only) → CR-4 (x: covered form, y: exempt form) → CR-10b (reformulation is a flow) | A-4 |
| C-8 | sellers.current (Lakeport retailers) | tax_share_borne (relative to distributors) | increase | medium | CR-7b (burden settles on the side with fewer alternatives: distributors can redirect deliveries to untaxed towns; retailers' sites are fixed and their buyers can leave) | A-1, A-3, A-N2 |
| C-9 | buyers.low_mobility | tax_share_borne (relative to buyers who can cross the line or substitute) | increase | medium | CR-7b (actors without alternatives keep paying the higher price) | A-1, A-2, A-3 |
| C-10 | distributors | compliance_cost | increase | short | CR-1 (op 3, K3: registration, returns, audits) → CR-8c | none |
| C-11 | officials.enforcement (town revenue department) | enforcement_cost | increase | short | CR-1 (op 2, K3) → CR-8c | none |
| C-12 | distributors | lobbying_effort | increase | medium | CR-1 (op 3) → CR-4 (x: accept, y: lobby for repeal or wider exemptions) → CR-8c | A-N3 |
| C-13 | sellers.substitutes (approved pre-school providers) | lobbying_effort | increase | medium | CR-4 mirror (providers hold a funded option that repeal would remove; x: accept repeal, y: lobby to keep) | A-N3 |
| C-14 | families.preschool_age | quantity_traded (pre-school places used) | increase | medium | CR-1 (op 2) → CR-4 mirror (x: home or informal care, y: free place); arithmetic: a free place taken by a child from a paid place or from a counterfactual town place adds nothing, one taken from home care adds one | A-N1, A-N4 |
| C-15 | sellers.substitutes (private pre-schools) | quantity_substitute (paid private places) | decrease | medium | CR-1 (op 2, K2) → CR-9 (substitute: free places ↔ paid places) → CR-4 (x: paid place, y: free place) | A-6 |

## 6. Second-order effects

Depth limit 4; diffuse bystander effects pruned after depth 3. Each link names the exchange relation it follows (CR-9).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-16 | sellers.substitutes (private pre-schools) | price_substitute (fees for paid places) | decrease | medium | C-15 → CR-6 (with demand lower, the price tends to a lower clearing level) | substitute (free places ↔ paid places), close | A-6 |
| C-17 | sellers.substitutes (private pre-schools) | number_of_sellers | U1-a: ambiguous; U1-b: decrease | long | C-15 → CR-7a (x: run paid places, y: other use of premises and staff); under U1-a, approval adds a funded option (CR-1 op 2) pushing the other way, CR-12b | substitute (free places ↔ paid places), close | A-6 |
| C-18 | sellers.complements (Lakeport grocers) | quantity_complement (other groceries bought in Lakeport) | decrease | medium | C-5 → CR-9 (shoppers who move the drink purchase across the line move the trip's other purchases with it) | complement, trip (drinks ↔ groceries on the same trip) | A-1, A-3, A-7 |
| C-19 | neighboring_jurisdictions (retailers across the line) | quantity_traded (drinks and groceries sold to Lakeport residents) | increase | medium | C-5 → CR-9 (across_border) and CR-9 (complement, trip) | across_border (Lakeport ↔ neighboring stores); complement, trip | A-1, A-3, A-7 |
| C-20 | neighboring_jurisdictions (retail staff across the line) | employment, hours_worked | at_least_one_increase | medium | C-19 → CR-9 (labor used to make the sales) → LW-10 | input_to (retail labor → retail sales) | A-1, A-3, A-7, A-9 |
| C-21 | workers (Lakeport retail) | employment, hours_worked | ambiguous | medium | (−) C-4 and C-18 → CR-9 → LW-10; (+) C-6 (exempt drinks bought in Lakeport) → CR-9 → LW-10; CR-12b | input_to (retail labor → retail sales) | A-1, A-2, A-3, A-7, A-9 |
| C-22 | neighboring_jurisdictions (owners of retail sites near the line) | asset_value | increase | long | C-19 → CR-7c and CR-10c (a lasting rise in expected yield is captured by whoever owns the site when it becomes expected) | across_border; sale of sites | A-1, A-3, A-7, A-N5 |
| C-23 | input_suppliers (pre-school staff) | employment | increase | medium | C-14 → CR-9 (staff used to provide places) → LW-10 | input_to (staff → pre-school places) | A-9, A-N1, A-N4 |
| C-24 | town budget | resources_available_other_uses (general fund) | increase | medium | CR-8d (earmarked revenue for places frees the general money the town would otherwise have spent on places) | the town's own budget | A-8 |
| C-25 | town budget | tax_revenue_vs_static_projection | decrease | short | C-4, C-5, C-7 → arithmetic: the taxed base shrinks below the pre-tax base | the tax base (deliveries into Lakeport) | A-1, A-2, A-3 |

**Where chains were stopped.**

- C-20 and C-21 reach depth 4 (tax → price → trip moved → sales → staffing); stopped.
- Effects of C-24 (what the freed general money is spent on) are not followed: the record does not say, and further links would be diffuse bystander effects.
- Prices of drinks and groceries in neighboring stores: the direction would depend on whether their supply is fixed in the short run (magnitude); not followed.

## 7. Combined effects

Keys reached by one chain, or by chains with the same sign, take that sign (CR-12a). Keys where chains conflict:

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| workers (Lakeport retail), employment and hours, medium | Exempt drinks bought in Lakeport | Fewer covered drinks; trips moved across the line | None | ambiguous (C-21) |
| sellers.substitutes (private pre-schools), number_of_sellers, long (reading U1-a) | Approval opens a funded option | Paid demand falls | None | U1-a: ambiguous; U1-b: decrease (C-17) |
| families.preschool_age, quantity_traded (places), medium | Free places taken by children from home care (A-N4) | None: places taken from paid or counterfactual town places add nothing (arithmetic); the fungibility chain (C-24) would reduce places only if earmarked spending fell below counterfactual spending, excluded by A-N1 | A-N1 | increase (C-14) |

## 8. Time structure

- **Short run.** Shelf prices, purchases, cross-border shopping and exempt-drink sales respond within weeks (C-1, C-4, C-5, C-6).
- **Medium run.** Reformulation and relabeling take product cycles (CR-10b; C-7). Shopping habits that move whole trips across the line build up (C-18, C-19). Pre-school places and staff expand as the program opens (C-14, C-23); private pre-schools adjust fees and, later, numbers (C-16, C-17).
- **Long run.** Site values near the line reflect the expected life of the tax (C-22; CR-7c, CR-10c).
- **Announcement.** The record gives no announcement or effective dates, so stocking up by retailers before the effective date (CR-10a) is not reported.
- **Persistence.** Pre-school capacity built with the revenue (staff, premises) creates holders of a stake in keeping the tax (C-13).

## 9. Opportunity costs

Each written as a signed change in a variable (CR-3, CR-8).

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-4 | buyers.current | quantity_traded (covered drinks sold in Lakeport) | decrease | Drink purchases buyers would have made at the untaxed price (CR-5a) | CR-4c, CR-5a |
| C-10 | distributors | compliance_cost | increase | Staff time on returns and audits (CR-8c) | CR-8c |
| C-11 | officials.enforcement (town revenue department) | enforcement_cost | increase | Budget and staff used on collection and audits (CR-8c) | CR-8c |
| C-12 | distributors | lobbying_effort | increase | Resources spent lobbying (CR-8c) | CR-4 → CR-8c |
| C-26 | buyers.current | resources_available_other_uses | decrease | What buyers would have bought with the tax paid (CR-8a) | CR-8a, CR-8b |

## 10. Assumptions

Case assumptions are used as given. New premises added by this re-run are marked A-N.

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Lakeport retailers pass at least part of the tax on in shelf prices. | other | 0.9 | Distributor-level per-unit taxes; competitive retail; shelf-price surveys from comparable towns. | Fail or lose support: C-1, C-4, C-5, C-6, C-8, C-9, C-18, C-19, C-20, C-21, C-22, C-25, C-26 |
| A-2 | Buyers have untaxed substitutes they consider acceptable (water, diet drinks, juice). | substitutability | 0.9 | Exemption list; shelf range. | Fail or lose support: C-4, C-6, C-9, C-21, C-25 |
| A-3 | Enough Lakeport residents can easily shop in the neighboring towns. | mobility | 0.8 | Drive times of 10 to 15 minutes; existing cross-border shopping habits; car ownership. | Fail or lose support: C-4, C-5, C-8, C-9, C-18, C-19, C-20, C-21, C-22, C-25 |
| A-4 | Reformulation or relabeling to an exempt category is feasible for some products. | other | 0.7 | Existing diet versions; exemption definitions. | Fail or lose support: C-7 |
| A-5 | Distributors evade the tax on a meaningful scale. | enforcement | 0.3 | Small number of registered distributors; audit powers. | Fail or lose support: No reported consequence depends on it alone; see Not reported. |
| A-6 | Free places draw some families who would otherwise have paid for private places. | substitutability | 0.85 | Current private enrollment among 3- and 4-year-olds. | Fail or lose support: C-3, C-15, C-16, C-17, C-27 |
| A-7 | Shoppers bundle drink purchases with other groceries on the same trip. | other | 0.7 | Shopping surveys; store layout and basket composition. | Fail or lose support: C-18, C-19, C-20, C-21, C-22 |
| A-8 | Lakeport would otherwise have funded some pre-school places from general revenue, and the law does not fix that funding level. | revenue_use | 0.65 | Current budget lines for early education; whether the ordinance has a maintenance-of-effort clause. | Fail or lose support: C-24 |
| A-9 | Sellers adjust their staffing to their sales. | alternative_uses | 0.75 | Share of part-time and flexible staff in local retail and services. | Fail or lose support: C-20, C-21, C-23 |
| A-N1 | Earmarked spending on free places exceeds what the town would otherwise have spent on pre-school places from general revenue. (new premise) | revenue_use | 0.7 | The program is described as free places for 3- and 4-year-olds funded by the whole revenue; current early-education budget lines (A-8 evidence). | Fail or lose support: C-14, C-23 |
| A-N2 | Distributors serving Lakeport also serve the neighboring towns and can redirect deliveries there at little cost. (new premise) | mobility | 0.85 | Neighboring towns 10 to 15 minutes away; regional distribution routes. | Fail or lose support: C-8 |
| A-N3 | Distributors and approved pre-school providers can organize and spend to change or defend the tax and the earmark. (new premise) | other | 0.75 | Small number of registered distributors; organized provider associations are common. | Fail or lose support: C-12, C-13 |
| A-N4 | Some families who would have kept their 3- and 4-year-olds at home or in informal care take a free place. (new premise) | substitutability | 0.8 | Share of 3- and 4-year-olds not enrolled in any pre-school before the program. | Fail or lose support: C-14, C-23 |
| A-N5 | Buyers of retail sites near the town line expect the tax to last. (new premise) | expectations | 0.7 | No sunset clause in the record; earmarks create defenders of the tax. | Fail or lose support: C-22 |
| A-N6 | The tax was announced weeks before taking effect and retailers can store extra stock. (new premise) | expectations | 0.45 | The record gives no dates; storage space in small stores is limited. | Fail or lose support: No reported consequence depends on it alone; see Not reported. |

**Not reported** (a premise has p below 0.5, or the record lacks a needed fact):

- Distributors evade the tax (informal_activity increase; CR-4 x: comply, y: violate): A-5, p 0.3.
- Retailers stock up before the effective date (inventory_held increase in the window; CR-10a): A-N6, p 0.45.
- Distributors' net_price_received: CR-7a says their net yields across towns are brought back into line; whether any lasting fall remains is magnitude, not sign. Recorded instead as the relative burden (C-8).

## 11. Report

**The policy:** Lakeport charges distributors 1.5 cents per fluid ounce on drinks with added sugar delivered to Lakeport retailers. Diet drinks, milk drinks and 100% juice are exempt. The revenue funds free pre-school places for 3- and 4-year-olds, run by the town and approved providers. The town's revenue department registers and audits distributors.

**Visible consequences:** Shelf prices of covered drinks in Lakeport rise (C-1) and fewer are sold there (C-4); the town collects revenue (C-2). Families who take a free place instead of a paid one stop paying fees (C-3, C-27); more children attend pre-school and more staff are employed (C-14, C-23).

**Invisible consequences:** Buyers: those who keep buying pay the tax (C-26); some buy across the town line (C-5) or switch to exempt drinks (C-6); buyers with few alternatives bear more of the tax than others (C-9). Sellers: Lakeport retailers bear more of the tax than distributors (C-8); Lakeport grocers lose the other purchases that move with the drinks (C-18); stores across the line gain sales and staff (C-19, C-20) and their sites gain value (C-22); drink makers reformulate or relabel (C-7). Pre-school: private paid places and fees fall (C-15, C-16). Town: general money is freed for other uses (C-24); revenue falls short of a static projection (C-25); collection and compliance use resources (C-10, C-11); distributors and providers lobby (C-12, C-13).

**Ambiguous effects:** Employment and hours in Lakeport retail (C-21): fewer covered drinks and moved trips push down, exempt-drink sales in town push up. The number of private pre-schools under reading U1-a (C-17).

**Key conditions:** Pass-through (A-1, p 0.9); acceptable substitutes (A-2, p 0.9); easy cross-border shopping (A-3, p 0.8); trip bundling (A-7, p 0.7); earmarked spending exceeding counterfactual pre-school spending (A-N1, p 0.7, new); distributors' mobility (A-N2, p 0.85, new).

**What this analysis cannot say:** How much prices, purchases or enrollment change; whether the gains to families outweigh the costs to drink buyers and Lakeport sellers; whether the policy is good. Health and nutrition effects of drinking less sugar, and child development effects of pre-school, are out of scope in version 1.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | buyers.current | price_paid (covered drinks in Lakeport) | increase | short | visible | B | CR-1 (op 3 on distributors, K1) → CR-9 (wholesale terms) → CR-5c (the range of terms moves with what the seller must give) | A-1 |
| C-2 | town budget | tax_revenue | increase | short | visible | A | CR-1 (op 4, K1) → CR-8b (every payment is a receipt); counterfactual revenue is zero | none |
| C-3 | families.preschool_age | price_paid (pre-school places) | decrease | short | visible | B | CR-1 (op 2, K2: free place added) → CR-4 mirror (x: paid place, y: free place) → CR-3b | A-6 |
| C-4 | buyers.current | quantity_traded (covered drinks sold in Lakeport) | decrease | short | visible | B | C-1 → CR-4c (last units first given up) and CR-4 (x: covered drink, y: exempt drink; x: buy in Lakeport, y: buy across the line) | A-1, A-2, A-3 |
| C-5 | buyers.current | cross_border_purchases | increase | short | invisible | B | C-1 → CR-4 (x: buy in Lakeport, y: buy across the town line) | A-1, A-3 |
| C-6 | sellers.substitutes (exempt drinks) | quantity_substitute (exempt drinks) | increase | short | invisible | B | C-1 → CR-4 (x: covered drink, y: exempt drink) → CR-9 (substitute) | A-1, A-2 |
| C-7 | drink makers | reclassification | increase | medium | invisible | B | CR-1 (op 3 on the covered form only) → CR-4 (x: covered form, y: exempt form) → CR-10b (reformulation is a flow) | A-4 |
| C-8 | sellers.current (Lakeport retailers) | tax_share_borne (relative to distributors) | increase | medium | invisible | B | CR-7b (burden settles on the side with fewer alternatives: distributors can redirect deliveries to untaxed towns; retailers' sites are fixed and their buyers can leave) | A-1, A-3, A-N2 |
| C-9 | buyers.low_mobility | tax_share_borne (relative to buyers who can cross the line or substitute) | increase | medium | invisible | B | CR-7b (actors without alternatives keep paying the higher price) | A-1, A-2, A-3 |
| C-10 | distributors | compliance_cost | increase | short | invisible | A | CR-1 (op 3, K3: registration, returns, audits) → CR-8c | none |
| C-11 | officials.enforcement (town revenue department) | enforcement_cost | increase | short | invisible | A | CR-1 (op 2, K3) → CR-8c | none |
| C-12 | distributors | lobbying_effort | increase | medium | invisible | B | CR-1 (op 3) → CR-4 (x: accept, y: lobby for repeal or wider exemptions) → CR-8c | A-N3 |
| C-13 | sellers.substitutes (approved pre-school providers) | lobbying_effort | increase | medium | invisible | B | CR-4 mirror (providers hold a funded option that repeal would remove; x: accept repeal, y: lobby to keep) | A-N3 |
| C-14 | families.preschool_age | quantity_traded (pre-school places used) | increase | medium | visible | B | CR-1 (op 2) → CR-4 mirror (x: home or informal care, y: free place); arithmetic: a free place taken by a child from a paid place or from a counterfactual town place adds nothing, one taken from home care adds one | A-N1, A-N4 |
| C-15 | sellers.substitutes (private pre-schools) | quantity_substitute (paid private places) | decrease | medium | invisible | B | CR-1 (op 2, K2) → CR-9 (substitute: free places ↔ paid places) → CR-4 (x: paid place, y: free place) | A-6 |
| C-16 | sellers.substitutes (private pre-schools) | price_substitute (fees for paid places) | decrease | medium | invisible | B | C-15 → CR-6 (with demand lower, the price tends to a lower clearing level) | A-6 |
| C-17 | sellers.substitutes (private pre-schools) | number_of_sellers | U1-a: ambiguous; U1-b: decrease | long | invisible | B | C-15 → CR-7a (x: run paid places, y: other use of premises and staff); under U1-a, approval adds a funded option (CR-1 op 2) pushing the other way, CR-12b | A-6 |
| C-18 | sellers.complements (Lakeport grocers) | quantity_complement (other groceries bought in Lakeport) | decrease | medium | invisible | B | C-5 → CR-9 (shoppers who move the drink purchase across the line move the trip's other purchases with it) | A-1, A-3, A-7 |
| C-19 | neighboring_jurisdictions (retailers across the line) | quantity_traded (drinks and groceries sold to Lakeport residents) | increase | medium | invisible | B | C-5 → CR-9 (across_border) and CR-9 (complement, trip) | A-1, A-3, A-7 |
| C-20 | neighboring_jurisdictions (retail staff across the line) | employment, hours_worked | at_least_one_increase | medium | invisible | B | C-19 → CR-9 (labor used to make the sales) → LW-10 | A-1, A-3, A-7, A-9 |
| C-21 | workers (Lakeport retail) | employment, hours_worked | ambiguous | medium | invisible | B | (−) C-4 and C-18 → CR-9 → LW-10; (+) C-6 (exempt drinks bought in Lakeport) → CR-9 → LW-10; CR-12b | A-1, A-2, A-3, A-7, A-9 |
| C-22 | neighboring_jurisdictions (owners of retail sites near the line) | asset_value | increase | long | invisible | B | C-19 → CR-7c and CR-10c (a lasting rise in expected yield is captured by whoever owns the site when it becomes expected) | A-1, A-3, A-7, A-N5 |
| C-23 | input_suppliers (pre-school staff) | employment | increase | medium | visible | B | C-14 → CR-9 (staff used to provide places) → LW-10 | A-9, A-N1, A-N4 |
| C-24 | town budget | resources_available_other_uses (general fund) | increase | medium | invisible | B | CR-8d (earmarked revenue for places frees the general money the town would otherwise have spent on places) | A-8 |
| C-25 | town budget | tax_revenue_vs_static_projection | decrease | short | invisible | B | C-4, C-5, C-7 → arithmetic: the taxed base shrinks below the pre-tax base | A-1, A-2, A-3 |
| C-26 | buyers.current | resources_available_other_uses | decrease | short | invisible | B | C-1 → CR-8b (tax paid by those who keep buying is withdrawn from their other uses) and CR-3a (those who switch fall back to a lower-ranked option) | A-1 |
| C-27 | families.preschool_age | resources_available_other_uses | increase | medium | visible | B | C-3 → CR-8b (the fee no longer paid stays with the family; it is matched by C-26) | A-6 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from a core rule. One near-gap: how many free places are added depends on comparing the earmarked spending with what the town would otherwise have spent (CR-8d gives only the direction of the freed money), which needed premise A-N1.

**(b) New premises.**

- A-N1 (p 0.7): CR-8d makes the earmark fungible; to sign the change in places used, the earmarked spending must exceed counterfactual spending.
- A-N2 (p 0.85): CR-7b needs to know which side has fewer alternatives; no case assumption described distributors' mobility.
- A-N3 (p 0.75): CR-4 (x: accept, y: lobby) needs someone at that margin.
- A-N4 (p 0.8): A-6 covers families moving from paid places, which adds no place; a net increase in enrollment needs families moving from home care.
- A-N5 (p 0.7): CR-7c needs an expectation that the change lasts before a site value moves.
- A-N6 (p 0.45, not reported): CR-10a needs an announcement window; the record has no dates.

**(c) Unclear core rules.**

- CR-7b speaks of "the side with fewer alternatives". Here the tax passes through three parties (distributor, retailer, buyer). The rule does not say how to rank more than two sides; it was applied pairwise and recorded with `tax_share_borne` relative to a named subgroup.
- CR-12b refers to a dominance pattern (DM); in a core-only run the dominance for enrollment rests on arithmetic plus A-N1, and the rule does not say this is admissible.
- CR-9 trip complements: 2.8 records them, but CR-9's text speaks of goods "used together"; a trip relation is joint purchase, not joint use. Applied on the strength of 2.8.
- CR-1 for the earmark (K2) with an unclear provision (U1): whether private pre-schools get operation 2 depends on the reading; CR-1 has no way to record an operation that holds only under one reading, so it was written per reading.
