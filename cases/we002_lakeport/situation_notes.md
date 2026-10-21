# WE-002 Lakeport: situation record notes (core-rule pilot, written blind)

Sources: section 1 of WE-002 (S1) and the assumption statements a1..a12 (A-1..A-12; ids, statements, types and p copied).

Disclosure: my first look at the assumption table printed the Evidence column by mistake (a column-selection error). I did not use it; every fact below rests on S1 or an assumption statement. I did not open any other part of the example, nor the old files in cases/we002_lakeport (answers.json, out_of_sample.md, record.json, sample_run).

## Facts and their basis
- Exchange e_dist (retailers.lakeport buy, distributors.registered sell): S1 K1 "collected from distributors on deliveries into the town". Price variables: price_paid for the buyer; net_price_received for the seller (revision r2, see below).
- Charge k1 on e_dist, payer = seller, receiver officials.town, tax_revenue and its shortfall against the static projection: S1 K1 (per_unit_tax, 1.5 cents per ounce); revenue goes to the town (S1 K2 "Revenue funds ...").
- moves(e_dist, buyer) [a1]: retailers, the buyers of the delivery, take the change in their price_paid because they pass at least part of it on (a1). (r2)
- compliance k1 distributors: S1 K3 (registration, monthly returns). enforcer k3 officials.revenue_dept: S1 K3 "Town revenue department".
- alt k1 distributors reclassification [a4]: a4 (relabeling to an exempt category); S1 exemptions (non-caloric, milk-based, 100% juice).
- alt k1 distributors informal_activity [a5]: a5 (evasion).
- stakes k1 for retailers.lakeport, distributors.registered, providers.approved [a12].
- Link retailers price_paid -> households price_paid (output) [a1]: a1 (pass-on in shelf prices).
- Link households price_paid -> quantity_demanded (own_price), no premise: CR-4c. Households quantity_demanded -> retailers.lakeport quantity_supplied (same_act), no premise: the same sale seen from the seller.
- Links households price_paid -> households quantity_substitute, sellers.untaxed_drinks quantity_supplied and net_price_received (substitute) [a2]: a2 (water, diet drinks, juice).
- Link households price_paid -> households cross_border_purchases (substitute) [a3], and -> retailers.neighboring quantity_supplied (same_act) [a3]: a3 and S1 (three neighboring towns without the tax).
- Links households cross_border_purchases -> retailers.neighboring quantity_supplied (complement) and -> retailers.lakeport quantity_supplied (substitute) [a7]: a7 (drinks bought with other groceries on one trip; large stores just outside the line, S1).
- Link retailers.lakeport quantity_supplied -> workers.retail employment,hours_worked (input) [a9]: a9.
- means k2 families.private_preschool in: S1 K2 (free places) with a6 (some families would otherwise have paid private fees). The means fact takes no premise, so a6 is not attached.

## Not recorded for lack of a place in the format
- K2 as an added option (CR-1 op 2). Free pre-school places are not a held price, a charge or a discretionary grant, so nothing makes the families "choosers" for `alt`. Therefore a6 (draw from private places: private providers lose enrolment), a11 (families from home or informal care take a place) and the effect of free places on private providers' demand have no entry point.
- The earmark as a use of revenue: a8 and a10 (the earmark replaces general-revenue funding, or exceeds it; what the town does with freed general funds) have no fact type. `means` has no premises and cannot name the town's general budget.
- (Resolved in r2 by core.lp commit 5cf5f87; the following was the r1 workaround and is no longer needed.) `moves` and `charge` assumed the payer is the buyer. With payer_side seller, core.lp sets the buyer-side price down and the seller-side price (same variable name as the payer's) up; I avoided it by measuring the seller's price as full_cost_per_unit and putting the pass-on in a link. A tax on sellers whose net_price_received falls (incidence on sellers) cannot be recorded.
- Incidence is a premise-free `moves` on the payer's side plus a link with a1; the format cannot say "part of the tax" (a1 says "at least part").
- Exemptions (S1) as a base boundary: only reclassification as an alternative; no exempt-drink market as a separate exchange.
- U1 (private pre-schools as approved providers, U1-a / U1-b): no per-reading facts.
- Households (consumers) are not a party in any exchange; they enter through links only (as in the Halvern record). The retailer-household shelf market is not an exchange, so the charge cannot reach households' means directly (their loss rests on the a1 link only).
- Revenue timing and the child-care budget effects on parents (time freed): nothing in S1 or the assumptions states them.

## Revision r2 (after core.lp 5cf5f87)
Changed: seller_price_var back to net_price_received; moves(e_dist) now on the buyer side with a1 (was seller, no premise); removed the link distributors full_cost_per_unit -> retailers price_paid, since moves now carries the pass-on to retailers' price_paid. Households still reach the tax only through the retailers price_paid -> households price_paid link (a1); no retail exchange is added, since S1 describes no separate rule on it. Everything else unchanged. Effect on output: distributors' full_cost_per_unit row is gone; no distributor net_price_received row appears because the wedge is signed only on the side `moves` names.
