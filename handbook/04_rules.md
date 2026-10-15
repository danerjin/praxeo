# 4. Rule catalog 0.3

Each rule is one reusable inference. Format:

- **If:** the preconditions, stated as facts about the policy record or earlier consequences.
- **Then:** the conclusion, as a consequence in normal form (actor class, variable, sign).
- **Assumes:** empirical premises, each of which needs an estimate in the case at hand.
- **Unless:** known exceptions that block the rule.
- **Tier / visibility / horizon:** proposed defaults. A rule's tier is the tier of its conclusion when its preconditions hold; it is A only if it has no empirical assumptions.
- **Builds on:** foundations from `01_foundations.md`.
- **Source:** where the reasoning comes from (from memory; to be checked).

Rules are deliberately small. A full analysis chains several of them, and each link is reviewed on its own.

**Changes in 0.3.** New: RS-12 to RS-15, OC-5 to OC-7, TS-5 to TS-9, PC-12 to PC-15, TX-10, TX-11, SB-8, SB-9, EN-9, EN-10, DM-4, DM-5. Widened: RS-4, RS-10, RS-11, TS-1, TS-3, PC-8, TX-6, TX-8, TX-9, SB-4, EN-6, EN-8, DM-1. Each change traces to a gap found in the worked examples (`06_gaps.md`, 6.2).

---

## RS: Generic responses

These apply to any intervention. Workflow step 5 runs through them for every actor class.

### RS-1 Substitution
- **If:** a policy raises the cost (money or otherwise) to an actor class of using a good or means, relative to an alternative that serves the same end.
- **Then:** `actor_class.quantity_substitute` increase; use of the target decreases at the margin.
- **Assumes:** a substitute exists and is not covered by the policy (`substitutability`).
- **Unless:** the actor class has no margin of choice (a fixed contract during its term).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-2, LW-3.

### RS-2 Adjustment of quality and terms
- **If:** a policy fixes the money price or one term of an exchange below (or above) what the parties would agree.
- **Then:** the party disadvantaged adjusts unregulated terms in its own favor: `quality_per_unit`, `maintenance_spending`, service, contract length, or added conditions move against the other party.
- **Assumes:** some terms of the exchange are unregulated and adjustable.
- **Unless:** every relevant term is fixed and enforced.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** AX-1, LW-5.
- **Source:** Hazlitt, *Economics in One Lesson*, chapters on price-fixing and rent control.

### RS-3 Evasion
- **If:** complying with a rule costs an actor more than the expected cost of breaking it (probability of detection times penalty, plus moral and reputational cost).
- **Then:** `informal_activity` increase; `side_payments` increase where the rule fixes a price.
- **Assumes:** enforcement is imperfect (`enforcement`).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** AX-1, LW-1.

### RS-4 Relocation across a boundary
- **If:** the policy applies within a boundary, and the activity can be carried out or bought on the other side of it.
- **Then:** activity and purchases move to whichever side the policy favors. Where the policy burdens activity inside: `cross_border_purchases` increase (buyers), or sellers and production relocate outside; activity inside decreases. Where it favors activity inside (a floor, subsidy or exemption that applies only there): `entry_rate` increase inside and `quantity_supplied` decrease just outside.
- **Assumes:** the boundary is near enough for crossing to be worth its cost to some actors (`mobility`).
- **Tier** B. **Visibility** invisible. **Horizon** short (purchases) to long (firms).
- **Builds on:** RS-1.

### RS-5 Reclassification
- **If:** the policy's definitions or exemptions draw a line between covered and uncovered goods, contracts or actors.
- **Then:** `reclassification` increase: goods, contracts and organizations are reshaped to fall on the favorable side (for example, conversion of rental units to owner-occupied units; reformulating a product below a tax threshold).
- **Assumes:** reshaping costs less than the policy's burden for some actors.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** AX-1.

### RS-6 Exit and reallocation
- **If:** the policy lowers the expected return of using resources in the target activity, relative to other uses.
- **Then:** `investment_target` decrease, then `quantity_supplied` and `capital_stock_target` decrease; `number_of_sellers` decrease or `entry_rate` decrease. Resources go to other uses, where quantities rise.
- **Assumes:** resources have other uses (`alternative_uses`); speed depends on how specific and durable the resources are (`durability`; see TS-1).
- **Tier** B. **Visibility** invisible. **Horizon** medium to long.
- **Builds on:** LW-4.

### RS-7 Lobbying and rent-seeking
- **If:** the policy creates a gain that is concentrated on an identifiable group and depends on political decisions (renewal, extension, exemption, enforcement).
- **Then:** `lobbying_effort` by that group increase. Those concentrated groups harmed by the policy also lobby, for repeal or exemption.
- **Assumes:** the group can organize at a cost lower than its stake.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** AX-1, LW-1.

### RS-8 Change of timing
- **If:** the policy treats the same action differently depending on when it is taken (announcement before effective date, phase-in, deadline, expected tightening or repeal).
- **Then:** actions are moved toward the favorable time: rush before a tax or cap takes effect, delay until after a repeal is expected, purchases pulled forward into a temporary subsidy.
- **Assumes:** actors know the timing and can shift their actions.
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-7.

### RS-9 Bundled trips carry other purchases with them
- **If:** buyers of a good change where they buy it (RS-4 cross-border buying, or a switch to another store or channel), and they usually buy other goods on the same trip (a `complement` relation noted `trip`).
- **Then:** the other goods bought on those trips move with it: `quantity_traded` of untaxed or unregulated goods decrease at the sellers left behind and increase at the sellers gained.
- **Assumes:** buyers bundle purchases on trips (`other`); the destination sells the other goods too.
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1 (a trip has a cost, so buyers spread it over several purchases), RS-4.

### RS-10 Driving trade into the informal market
- **If:** some trade in a good or service moves outside the legal market (RS-3, PC-6, EN-3, EN-7).
- **Then:** for that trade: `search_cost` increase (sellers cannot advertise openly); `quality_information` decrease and `quality_variability` increase (no brands, licensing, reviews or recourse to rely on); `disputes_settled_outside_courts` increase; sellers charge for the risk of punishment. In reverse (trade returning to the legal market after a repeal), each sign flips.
- **Assumes:** penalties for informal trade are enforced at least sometimes (`enforcement`).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** AX-1, LW-1.

### RS-11 Lock-in spills into linked markets
- **If:** an actor class holds a non-transferable benefit that is lost by a change of location or status: moving (PC-7: a controlled tenancy, a place on a list), leaving an occupation, or letting a registration lapse (a grandfathered status).
- **Then:** members of the class turn down opportunities that would cost them the benefit: `job_changes` decrease, longer commutes, forgone breaks or better work elsewhere.
- **Assumes:** some valued opportunities would require the change (`mobility`); the benefit is not transferable.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1 (losing the benefit is part of the cost of moving), PC-7.

### RS-12 Complement spillover
- **If:** the quantity traded, or the stock in use, of a good changes, and another good is recorded as its `complement` in use (not `trip`): cars and repairs, cars and fuel.
- **Then:** `quantity_complement` changes in the same direction; where the complement's supply is slow to adjust, `price_complement` moves the same way too.
- **Assumes:** the complement relation is close, and the complement has few other uses (`substitutability`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-2.

### RS-13 Supply spillover
- **If:** a policy adds quantity supplied to a linked market (exempt new building next to a capped segment, subsidized output fed into a wholesale market, released public stocks).
- **Then:** the price in that market decreases (`price_substitute` decrease, or that market's `price_paid` decrease), compared with the counterfactual.
- **Assumes:** the added supply is not offset by withdrawal elsewhere; buyers there do not absorb it at an unchanged price (`substitutability`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-3. This is the general form of the opposing chain noted under PC-8.

### RS-14 Input cost pass-through
- **If:** a policy raises the cost of an input (a tax or floor on labor, a tariff on a material, a regulated price) that is a material part of the cost of some output.
- **Then:** for the output: `price_paid` by its buyers increase and/or `quantity_supplied` decrease (at least one). Where the sellers' competitors face the same increase, the price rise dominates; where competitors are exempt (imports, untaxed or uncovered sellers), RS-6 applies and the quantity effect dominates.
- **Assumes:** the input cannot be fully replaced at the old cost (`substitutability`); the competitors' exposure (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-4, TX-2. The upstream counterpart, for a cap on the output, is PC-12.

### RS-15 Discretionary relief is rationed by non-price criteria
- **If:** relief from a policy's burden (an exclusion, waiver, permit or exemption) is granted case by case at officials' discretion, and is worth more to applicants than its fee.
- **Then:** `allocation_by_non_price_criteria` increase among applicants; `compliance_cost` of applying increase; `lobbying_effort` increase, both by applicants and by those who gain when relief is denied.
- **Assumes:** the grant is discretionary and valuable (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-6 (relief is scarce and not priced), RS-7.

---

## OC: Opportunity cost

Opportunity costs are recorded as signed changes in variables (`02_ontology.md`, 2.5), never as a separate "loss" entry.

### OC-1 Diverted resources
- **If:** the policy takes resources from an actor class (tax, mandated purchase, compliance) or directs resources to a use.
- **Then:** `resources_available_other_uses` decrease for that actor class; the goods they would have bought or produced with those resources are not produced, so `quantity_traded` decrease in the markets where they would have spent it. The spending or use is visible; the forgone alternative is not.
- **Tier** A, given that resources are taken. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1.
- **Source:** Bastiat, "That Which Is Seen, and That Which Is Not Seen" (the broken window); Hazlitt, *Economics in One Lesson*, ch. 2 to 4.

### OC-2 Unpriced time and effort
- **If:** the policy causes actors to spend time or effort that buys nothing they value for its own sake: queuing (PC-2), searching, paperwork, qualification hours beyond what buyers would demand (EN-1).
- **Then:** `wait_time`, `search_cost` or `compliance_cost` increase; the forgone uses of that time are an invisible cost.
- **Tier** A, given the time is spent. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1.

### OC-3 Administration and enforcement
- **If:** the policy must be administered or enforced.
- **Then:** `enforcement_cost` increase for `officials.enforcement`, funded by `taxpayers` (OC-1 applies to that funding).
- **Tier** A, given positive enforcement activity. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1.

### OC-4 Prevented exchanges
- **If:** the policy prevents exchanges that buyers and sellers would otherwise have made (a ceiling, a floor, a license requirement, a prohibition, a tax that prices some buyers out).
- **Then:** `quantity_traded` decrease for the prevented exchanges; both parties to each lose the gain they expected from it. Name both sides.
- **Tier** A (ex ante, by each party's own ranking). **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-5.
- **Source:** Rothbard, *Power and Market*, ch. 3.

### OC-5 Diverted spending diverts work (Bastiat's tailor)
- **If:** a policy changes where an actor class spends (OC-1: money taken and spent by others; SB-8: money freed), so that `quantity_traded` falls in some markets and rises in others.
- **Then:** `employment` or `hours_worked` decrease in the markets that lose the spending and increase in those that gain it. The jobs the policy creates are visible; the jobs it prevents elsewhere are not.
- **Assumes:** sellers adjust their labor to their sales (`alternative_uses`).
- **Tier** B. **Visibility**: the gain is visible, the loss invisible. **Horizon** short to medium.
- **Builds on:** OC-1, LW-4.
- **Source:** Bastiat, "That Which Is Seen, and That Which Is Not Seen" (the window, and the tailor who does not get the order); Hazlitt, *Economics in One Lesson*, ch. 2.

### OC-6 Lost revenue is made up elsewhere
- **If:** a repeal or cut reduces `tax_revenue` that the budget was spending.
- **Then:** other taxes rise, borrowing rises (implying later taxes), or spending falls. Apply TX-1 and OC-1 to whichever group bears the replacement, named from the budget response. If the record does not say, state the replacement chain with a `revenue_use` assumption; where it frees resources for the same group that the repeal relieves, combine the chains (workflow step 7).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-1, SB-1 (its mirror case).

### OC-7 Revaluation changes holders' means
- **If:** `asset_value` of an asset held by an actor class rises or falls (SB-4).
- **Then:** when they sell or borrow against it, their `resources_available_other_uses` change in the same direction, and so do their purchases in linked markets (homeowners whose homes gain value bid for larger homes).
- **Assumes:** the change can be realized by sale or borrowing (`other`), and is not offset by an equal change in the price of what they intend to buy.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1.

---

## TS: Time structure

### TS-1 Durable capital lag
- **If:** a consequence works through reduced investment or maintenance in durable capital (buildings, equipment, trained skills).
- **Then:** the effect on `capital_stock_target` and `quantity_supplied` is small at first and grows as the existing stock wears out and is not replaced. Set horizon to medium or long; `quality_per_unit` often falls before quantity does.
- **In the other direction:** when a policy (or a repeal) raises the return on durable capital, the stock grows at the speed of new investment (planning, permits, finance, construction, training), which is not the mirror of wear-out. State that lag as a `durability` assumption; TS-5 may slow it further.
- **Assumes:** the durability of the capital involved (`durability`).
- **Tier** B. **Horizon** medium to long.
- **Builds on:** LW-4, LW-7.

### TS-2 Expectations
- **If:** actors expect the policy to be extended, tightened, made permanent or applied to new categories.
- **Then:** responses that the policy would cause in future are brought forward: investment falls now in categories expected to be covered; actors rush to get into exempt categories before the rules change.
- **Assumes:** what actors expect (`expectations`).
- **Tier** B. **Horizon** short to medium.
- **Builds on:** LW-7.

### TS-3 Erosion of a fixed parameter
- **If:** a cap, floor, rate, threshold or quantity is fixed in money terms or in physical units (a number of licenses, a tonnage), or indexed at a rate different from the change in the relevant market price or demand.
- **Then:** the component becomes more binding (or less) over time as prices or demand move. A ceiling or quota that is not binding at enactment can become binding later.
- **Assumes:** the expected path of market prices or demand.
- **Tier** B. **Horizon** medium to long.

### TS-4 The intervention spiral (proposed, contested)
- **If:** a policy produces consequences that its supporters regard as problems (shortages, black markets, evasion).
- **Then:** pressure for further intervention to address them (extending controls to substitutes, rationing schemes, penalties), or for repeal.
- **Tier** C until the experts decide whether and how to encode it; it is a claim about political dynamics rather than market action. See `06_gaps.md`, Q4.
- **Source:** Mises, *A Critique of Interventionism* (1929) and *Human Action*, ch. XXXVI.

### TS-5 Credibility of a repeal
- **If:** a policy is repealed (or not renewed), and actors give a meaningful probability to its return within the payback period of their investments.
- **Then:** responses that pay back quickly (repairs, pricing, lettings, short contracts) go ahead; responses that pay back only over long periods (major renovation, new construction, entry with sunk costs) are smaller and later than the mirror of the original policy's effects. Where the expected return would exempt existing practitioners (grandfathering), it brings entry forward instead.
- **Assumes:** the probability of re-imposition over a named period (`expectations`).
- **Tier** B. **Horizon** medium to long.
- **Builds on:** LW-7, TS-2.

### TS-6 Stock changes persist after repeal
- **If:** a policy caused reclassification (RS-5), exit (RS-6, EN-3), or the loss of specific capital, skills or client relationships, and reversing these has a cost (reassembling converted units, rebuilding capacity, retraining, re-establishing a client base).
- **Then:** a repeal reverses the flow but not the stock already changed, except where the restored return exceeds the cost of reversal. Former sellers return only partly and slowly; firms that closed re-enter as the sunk costs of entry are paid; people displaced stay displaced. Record the expected `persistence` (none, partial, full) on each repeal consequence.
- **Assumes:** the cost of reversal (`reversal_cost`), including how long people and capital have been away.
- **Tier** B. **Horizon** medium to long.
- **Builds on:** LW-1, LW-4, TS-1.

### TS-7 Expected caps reduce stocks held
- **If:** sellers expect a `price_ceiling` to apply in future periods of scarcity (an anti-gouging rule, a standing threat of price controls).
- **Then:** `inventory_held` before those periods decreases, because the expected return to storing goods for the scarce period falls. Less is available when scarcity arrives.
- **Assumes:** storage is costly and the cap is expected to bind (`expectations`, `binding`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-4, LW-7.

### TS-8 Habit adjustment
- **If:** a policy changes the cost of a routine, often-repeated action (carrying bags, a commute, a shopping pattern).
- **Then:** responses are smaller at first and grow over weeks or months as routines change; some short-run effects (fee payments, use of the costlier option) shrink over the same period without any change in prices or capital. Set the horizon of the full response to short-to-medium and describe the path.
- **Assumes:** the action is repeated often (`other`).
- **Tier** B. **Horizon** short to medium.
- **Builds on:** AX-1, LW-1 (learning a new routine has a cost).

### TS-9 Capital per worker and wages
- **If:** a policy reduces saving or investment across the economy (TX-6), so that `capital_stock_economy` is smaller over time than it would have been.
- **Then:** `wage_rate` across the economy is lower in the long run than it would have been, because labor works with less capital.
- **Assumes:** no offsetting inflow of foreign capital (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** long.
- **Builds on:** LW-7, LW-4.
- **Source:** Mises, *Human Action*, ch. XXI.

---

## PC: Price controls

### PC-1 Binding ceiling: excess demand
- **If:** `price_ceiling` on a good, below the price at which quantity demanded would equal quantity supplied.
- **Then:** `excess_demand` increase: at the controlled price, quantity demanded exceeds quantity supplied.
- **Assumes:** the ceiling is binding (`binding`) and enforced (`enforcement`).
- **Unless:** the ceiling is above the market price (not binding); price is a quality signal (LW-3 exception).
- **Tier** B. **Visibility** invisible (the shortage is often noticed, but its cause is not attributed to the policy). **Horizon** short.
- **Builds on:** LW-3, LW-4.
- **Source:** Mises, *Human Action*, ch. XXX; Hazlitt, *Economics in One Lesson*, chapter on government price-fixing.

### PC-2 Shortage is rationed by other means
- **If:** `excess_demand` increase (PC-1).
- **Then:** `wait_time`, `search_cost`, `side_payments` and `allocation_by_non_price_criteria` increase for `buyers.prospective`; which ones depend on the market. The good does not go to whoever is willing to give up the most for it, but by these other criteria.
- **Tier** A, given the shortage; the particular form is B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-6.

### PC-3 Buyers split into insiders and outsiders
- **If:** `excess_demand` increase (PC-1).
- **Then:** `buyers.current` who obtain the good at the controlled price gain (`price_paid` decrease for them); `buyers.prospective` who cannot obtain it lose: they pay more elsewhere, wait, or go without.
- **Tier** A, given the shortage. **Visibility**: the insiders' gain is visible; the outsiders' loss is invisible. **Horizon** short.
- **Builds on:** LW-5, LW-6.

### PC-4 Quality falls under a ceiling
- **If:** binding `price_ceiling` (PC-1), and sellers control unregulated aspects of quality.
- **Then:** `quality_per_unit` and `maintenance_spending` decrease; the quality-adjusted price moves back toward the market level.
- **Assumes:** quality and maintenance are not fully regulated or enforced (`enforcement`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** RS-2.

### PC-5 Supply shrinks under a ceiling
- **If:** binding `price_ceiling` (PC-1).
- **Then:** `investment_target` decrease, then `quantity_supplied` decrease, as resources move to uncontrolled uses.
- **Assumes:** `alternative_uses` exist for the resources (for housing: conversion to owner-occupation or other uses, demolition, keeping units off the market); speed governed by TS-1.
- **Unless:** the resources are completely specific and have no other use, in which case quantity supplied from the existing stock holds until it wears out (TS-1 still applies to new investment).
- **Tier** B. **Visibility** invisible. **Horizon** medium to long.
- **Builds on:** LW-4, RS-6, TS-1.
- **Source:** Hazlitt, *Economics in One Lesson*, chapter on rent control.

### PC-6 Black and grey markets under a ceiling
- **If:** binding `price_ceiling` (PC-1).
- **Then:** `informal_activity` and `side_payments` increase: some exchanges happen at prices above the ceiling, disguised or illegal (key money, tie-in sales, sublets at market rent). RS-10 applies to that trade.
- **Assumes:** imperfect `enforcement`.
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** RS-3.

### PC-7 Reduced turnover where the benefit is tied to holding
- **If:** binding `price_ceiling`, and the right to buy at the controlled price is tied to keeping the good (a tenancy, a place on a list), and cannot be sold.
- **Then:** `turnover` decrease among insiders: they move less, even when another unit, job or place would otherwise suit them better.
- **Assumes:** the benefit is not transferable (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-2, LW-5.

### PC-8 Spillover to uncontrolled substitutes
- **If:** a binding `price_ceiling` or `price_floor` covers part of a market, and an uncontrolled substitute or segment exists (recorded market relation).
- **Then:** demand moves to the uncontrolled segment (under a ceiling, from outsiders who cannot obtain the good, PC-3; under a floor, from buyers avoiding the higher price): `price_substitute` increase, which harms `buyers.substitutes`.
- **Assumes:** `substitutability` between the segments.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** RS-1, PC-3.
- **Note:** another chain can push `price_substitute` the other way: resources withdrawn from the controlled segment (PC-5) may reappear in the uncontrolled one (for example, new building that is exempt from the cap), adding supply there (RS-13). Combine the chains using the procedure in workflow step 7.

### PC-9 Binding floor: excess supply
- **If:** `price_floor` on a good, above the price at which quantity demanded would equal quantity supplied.
- **Then:** `excess_supply` increase; `quantity_traded` decrease (buyers buy less at the higher price).
- **Assumes:** `binding`, `enforcement`.
- **Unless:** the state buys the surplus (then see SB rules for the purchase).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-3, LW-6.

### PC-10 Minimum wage: fewer hires of the least productive
- **If:** `price_floor` on labor (minimum wage) above the wage some workers can command.
- **Then:** for workers whose labor employers value below the floor: `employment` decrease or `hours_worked` decrease, or `non_wage_compensation` decrease (RS-2). Workers who keep their jobs at the floor: `wage_rate` increase.
- **Assumes:** `binding` for an identifiable group; `enforcement`; employers can adjust hours, staffing, automation or non-wage terms.
- **Tier** B. **Visibility**: the wage rise is visible; lost hires and cut hours are invisible. **Horizon** short to medium.
- **Builds on:** PC-9, LW-4.
- **Note:** the empirical size of the employment effect is contested (Card and Krueger, 1994, and the literature since). Earnings of the low-wage group as a whole combine opposite chains and are `ambiguous` unless a dominance rule applies. This is a designated contested case for evaluation.

### PC-11 Non-price selection under a floor
- **If:** binding `price_floor` (PC-9).
- **Then:** buyers choose among excess sellers by non-price criteria: `allocation_by_non_price_criteria` increase. Under a minimum wage, employers become more selective (credentials, experience), and the cost to them of discriminating falls.
- **Tier** A, given the surplus; its form is B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-6 (applied to the selling side).

### PC-12 A ceiling passes up to the inputs
- **If:** a binding `price_ceiling` on a good, and the capped sellers buy most of a named input (relation `input_to`).
- **Then:** `net_price_received` by input suppliers for sales into the capped market decreases, and/or the capped sellers buy less of the input (`quantity_demanded` of the input decreases).
- **Assumes:** the input has few uncapped outlets in the period considered (`alternative_uses`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-4, PC-5. The downstream counterpart is RS-14.

### PC-13 Ceilings that allow documented costs
- **If:** a binding `price_ceiling` allows increases only for documented costs (invoiced freight, wholesale prices), not for costs that leave no paper trail (the owner's labor, risk, the value of the goods elsewhere).
- **Then:** `number_of_sellers` decreases most among sellers whose main costs are undocumented (occasional and informal suppliers, people bringing goods from outside); `compliance_cost` increases for sellers who use the defense.
- **Assumes:** the enforcing agency's definition of a documentable cost (`enforcement`).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-4, RS-6.

### PC-14 Rate caps bind hardest on small and short transactions
- **If:** a binding `price_ceiling` is stated as a rate per unit of value and time (an annual interest rate, a percentage markup), and a material part of the seller's cost is fixed per transaction (processing, collection).
- **Then:** sellers raise the minimum size and length of the transactions they offer: `transaction_size` increase; `quantity_supplied` of small, short transactions decreases most; `variety` decreases at the small end.
- **Assumes:** the share of fixed per-transaction costs (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-4, RS-2.

### PC-15 Regulated cost recovery over a shrinking base
- **If:** a regulator sets a price to recover largely fixed costs per unit sold (utility rates), and a policy reduces the units sold through the regulated channel.
- **Then:** at the next rate review, `price_paid` per unit increases for the remaining buyers.
- **Assumes:** the regulator's rate method (`other`); fixed costs do not fall with sales.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1.

---

## TX: Taxes and tariffs

### TX-1 Tax takes resources
- **If:** a tax is imposed and collected.
- **Then:** `resources_available_other_uses` decrease for the actor classes that bear it (see TX-2 for who bears it); `tax_revenue` increase. Apply OC-1 to what those actors would have done with the money, and analyze the spending of the revenue as a separate component.
- **Tier** A, given collection. **Visibility**: the payment is visible; the forgone uses are invisible. **Horizon** short.
- **Builds on:** LW-1.
- **Source:** Rothbard, *Power and Market*, ch. 4.

### TX-2 Per-unit tax: wedge and smaller market
- **If:** `per_unit_tax` or `ad_valorem_tax` on the sale of a good.
- **Then:** `price_paid` by buyers increase and/or `net_price_received` by sellers decrease (at least one must happen); `quantity_traded` decrease.
- **Assumes:** at least one side can reduce its quantity in response (some `substitutability` for buyers, or `alternative_uses` for sellers).
- **Tier** B. **Visibility**: the price rise is visible; the fall in quantity and in sellers' net price is invisible. **Horizon** short.
- **Builds on:** LW-3, LW-4.
- **Note:** how the burden splits between buyers and sellers is not fixed by this rule. Use DM-1, or report the split as ambiguous.

### TX-3 Taxed activity shrinks; resources move to untaxed uses
- **If:** TX-2 applies.
- **Then:** `investment_target` and `employment` in the taxed activity decrease over time; `quantity_substitute` increase.
- **Assumes:** `alternative_uses`, `substitutability`.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** RS-1, RS-6.

### TX-4 Avoidance of a local tax
- **If:** a tax applies within a jurisdiction with nearby untaxed places, or with definitions that can be avoided.
- **Then:** RS-4 (cross-border purchases), RS-5 (reformulation, reclassification) and RS-3 (evasion) apply. Taxed sales inside the boundary fall by more than total consumption does.
- **Assumes:** `mobility`; cost of reformulating.
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** RS-3, RS-4, RS-5.

### TX-5 Compliance cost
- **If:** a tax requires record-keeping, filing, labeling or collection by private parties.
- **Then:** `compliance_cost` increase for those parties; OC-1 applies to those resources.
- **Tier** A, given positive compliance work. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1.

### TX-6 Taxes on the return to saving and investment
- **If:** a tax falls on interest, dividends, capital gains or profits.
- **Then:** the net return on providing future goods falls; at the margin, saving and `investment_target` decrease, and the capital stock is smaller over time than it would have been.
- **Assumes:** savers and investors respond to net returns at the margin.
- **Unless:** some savers aim at a fixed future sum, for whom a lower net return calls for more saving. Where such savers are a material part of the group, total saving by the group is `ambiguous`; the sign holds firmly only for saving in the taxed forms by savers who have untaxed alternatives. (Pending expert decision, `06_gaps.md` Q14.)
- **Tier** B. **Visibility** invisible. **Horizon** long. Variables: `saving`, `investment_target`, `capital_stock_economy`; TS-9 carries the effect on wages.
- **Builds on:** LW-7, LW-4.

### TX-7 Tariff: domestic buyers pay more, protected sellers gain
- **If:** `tariff` on an imported good.
- **Then:** `price_paid` for the imported good and for domestic substitutes increase for `buyers.current`; `sellers.substitutes` (domestic producers of competing goods) see `net_price_received` and `quantity_supplied` increase. Domestic firms that use the good as an input face higher costs.
- **Assumes:** domestic substitutes exist; the tariff is not absorbed entirely by foreign sellers.
- **Tier** B. **Visibility**: gains to protected producers are visible; higher prices to buyers and input users are invisible. **Horizon** short to medium.
- **Builds on:** TX-2, RS-1.
- **Source:** Hazlitt, *Economics in One Lesson*, chapter on tariffs; Bastiat, "Petition of the Candlemakers".

### TX-8 Import restrictions: export industries lose
- **If:** a `tariff` (TX-7) or an import `quota` (EN-6) reduces imports.
- **Then:** foreigners earn less of the domestic currency from selling to the country, and so have less to spend on its exports: `quantity_supplied` and `employment` in export industries decrease over time.
- **Assumes:** trade is not offset by capital flows or other adjustments in the period considered (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-5, OC-4.
- **Source:** Hazlitt, *Economics in One Lesson*, chapter on tariffs.

### TX-9 Revenue falls short of a static projection
- **If:** TX-2 applies (the taxed quantity falls), or TX-4 applies (avoidance shrinks the base).
- **Then:** `tax_revenue_vs_static_projection` decrease: revenue is less than the rate times the pre-tax base.
- **Unless:** the tax is ad valorem on a price that the tax itself pushes up (a tax on interest that raises the gross interest rate). Then the remaining base is worth more per unit and the sign is open: combine the chains (workflow step 7).
- **Tier** B (inherits the assumptions of TX-2 or TX-4). **Visibility** invisible until revenue is reported. **Horizon** short.
- **Builds on:** TX-2, TX-4.

### TX-10 Base erosion and base shift across taxes
- **If:** a policy reduces `quantity_traded`, wages, employment or sales that bear other taxes in the jurisdiction (directly, or through RS-4 and RS-9), or a prohibition removes the base of an existing tax.
- **Then:** `tax_revenue` from those other taxes decreases. Where part of the spending moves to other goods taxed in the jurisdiction, revenue there increases, and the combined sign is `ambiguous` unless the substitutes are untaxed (informal or cross-border purchases), in which case it is a decrease.
- **Tier** B, inheriting the assumptions of the rules that shrink the base. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** TX-1, RS-1.

### TX-11 Tax on nominal returns
- **If:** a tax falls on nominal interest or gains, and prices are rising.
- **Then:** the share of the real return taken exceeds the statutory rate, and rises with the rate of inflation; the TX-6 responses are correspondingly stronger.
- **Tier** A for the arithmetic, B for the responses. **Visibility** invisible. **Horizon** medium to long.
- **Builds on:** TX-6.

---

## SB: Subsidies

### SB-1 Subsidy is funded by someone
- **If:** a subsidy is paid.
- **Then:** apply TX-1 and OC-1 to its funding source (taxes now, borrowing that implies taxes later, or monetary expansion). Name the payers.
- **Tier** A, given payment. **Visibility** invisible. **Horizon** short to long, depending on funding.
- **Builds on:** LW-1.

### SB-2 Subsidized activity expands
- **If:** `per_unit_subsidy` or `purchase_rebate` on a good.
- **Then:** `price_paid` by buyers decrease and/or `net_price_received` by sellers increase; `quantity_traded` increase.
- **Assumes:** at least one side can expand its quantity.
- **Tier** B. **Visibility** visible. **Horizon** short.
- **Builds on:** LW-3, LW-4.

### SB-3 Resources drawn from unsubsidized uses
- **If:** SB-2 applies.
- **Then:** resources move into the subsidized activity from other uses, where quantities fall: `quantity_substitute` decrease and output elsewhere decreases.
- **Assumes:** resources are scarce and in use elsewhere.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1, LW-4.

### SB-4 Capitalization of lasting changes in returns
- **If:** a lasting policy raises or lowers the expected net return from an asset in fixed or slowly expandable supply (land, buildings, licenses, quota rights, shares in firms with specific capital): a subsidy or a restriction that raises returns (EN-2, EN-6), or a tax, cap or competing entry that lowers them.
- **Then:** `asset_value` changes in the same direction from the time the change becomes expected. Owners at that time capture the gain or bear the loss; later buyers pay the new price, so they neither gain nor lose from the policy as it stands. When an expected gain later erodes (the subsidy ends, exempt competitors enter, repeal becomes likely), the value falls on whoever holds the asset then, including recent buyers who paid the capitalized price.
- **Assumes:** fixed or slowly expandable supply of the resource; the change is expected to last, or to end, at a stated probability (`expectations`).
- **Tier** B. **Visibility** invisible. **Horizon** short (announcement) to medium.
- **Builds on:** LW-4, LW-7.

### SB-5 Seeking to qualify
- **If:** a subsidy is conditional on criteria.
- **Then:** RS-5 (reshaping to qualify) and RS-7 (lobbying to widen or keep the criteria) apply.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.

### SB-6 Temporary purchase subsidy: pull-forward and dip
- **If:** a purchase subsidy available only during a limited window.
- **Then:** purchases are moved into the window (RS-8): `quantity_traded` increase during it and decrease after it, compared with the counterfactual. If the subsidy requires destroying a used good (scrappage), the stock of used goods falls: `price_substitute` increase for buyers of used goods.
- **Assumes:** buyers can shift purchase timing; for scrappage, the scrapped goods would otherwise have stayed in use.
- **Tier** B. **Visibility**: the surge is visible; the dip and the used-goods effect are invisible. **Horizon** short.
- **Builds on:** RS-8, OC-1.

### SB-7 Earmarked revenue is fungible
- **If:** a tax's revenue is earmarked for a purpose that the budget already funds, or would have funded, from general revenue.
- **Then:** general funding for the purpose decreases in part, so spending on the purpose rises by less than the earmarked amount, and the rest of the revenue in effect funds other spending or lower borrowing.
- **Assumes:** the purpose already receives, or would have received, general funding; budget-makers can reduce it (`revenue_use`).
- **Unless:** the law also fixes the general funding level (a maintenance-of-effort clause) and it is enforced.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1, AX-1 (budget-makers act on the whole budget).

### SB-8 In-kind provision of a good the recipient would have bought anyway
- **If:** the state provides a good, free or below cost, to recipients some of whom would have bought it themselves (or had it paid for, for example by an insurer).
- **Then:** for those recipients (and their payers), the provision works like a cash transfer: `resources_available_other_uses` increase, and they spend the freed money elsewhere (OC-5 applies there). The quantity of the provided good rises only for recipients who would not have bought it. Providers of the good who would have been paid privately are paid by the state instead.
- **Assumes:** the share of recipients who would have bought anyway (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1, SB-1.

### SB-9 Public stocks and their disposal
- **If:** the state buys a surplus at a support price (PC-9 Unless clause).
- **Then:** `inventory_held` by the agency increases while the floor binds. When the stock is released, `quantity_traded` decreases for the private sellers it displaces (donation, school meals) or `price_paid` decreases in the market it is sold into (resale, including abroad, RS-13); if it is destroyed, OC-1 applies to the resources used to produce and store it.
- **Assumes:** the product's shelf life and the disposal routes allowed (`durability`, `other`).
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1, RS-13.

---

## EN: Licensing, quotas and prohibition

### EN-1 Licensing requirement restricts supply
- **If:** `licensing_requirement` whose conditions (training hours, exams, fees, waiting periods) cost would-be sellers more than some of them would otherwise spend.
- **Then:** `entry_rate` and `number_of_sellers` decrease; `quantity_supplied` decrease and `price_paid` increase compared with no licensing.
- **Assumes:** `binding` (the requirement goes beyond what some current or prospective sellers already meet); `enforcement`.
- **Unless:** existing sellers are exempt (grandfathered), which delays the effect on supply (TS: horizon medium).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-1, LW-4, LW-5.
- **Source:** Rothbard, *Power and Market*, ch. 3 (grants of monopolistic privilege).

### EN-2 Licensed incumbents gain
- **If:** EN-1 applies.
- **Then:** `sellers.current` who hold licenses: `net_price_received` increase. If licenses are transferable, `asset_value` of a license increases (SB-4).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** EN-1, SB-4.

### EN-3 Excluded sellers and priced-out buyers
- **If:** EN-1 applies.
- **Then:** would-be sellers who do not qualify move to their next-best occupation (OC-4): their `earnings` decrease compared with the counterfactual. Buyers priced out of the licensed service substitute toward doing it themselves, unlicensed providers (RS-3) or going without (RS-1).
- **Assumes:** `substitutability` for buyers.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** OC-4, RS-1, RS-3, RS-10.

### EN-4 Quality received by buyers: ambiguous by default
- **If:** EN-1 applies and the requirement is related to the quality of the service.
- **Then:** two chains push `quality_per_unit` received by buyers in opposite directions: licensed providers meet a minimum standard (up), while buyers priced out move to self-provision or unlicensed providers (EN-3, down). The combined sign is `ambiguous` unless DM-2 applies.
- **Tier** B for each chain. **Visibility** the first chain is visible; the second is invisible. **Horizon** medium.
- **Note:** the canonical example for workflow step 7.

### EN-5 Incumbents push for tighter requirements
- **If:** EN-2 applies (incumbents gain from restriction).
- **Then:** RS-7: `lobbying_effort` by incumbents for stricter or broader requirements.
- **Tier** B. **Visibility** invisible. **Horizon** medium to long.

### EN-6 Quota
- **If:** `quota` limiting the quantity produced, sold or imported, below the quantity that would otherwise be traded.
- **Then:** `quantity_traded` decrease; `price_paid` increase; holders of quota rights gain, and their `asset_value` increases where rights are tradable (SB-4). Domestic sellers of the same good (for an import quota): `net_price_received` and `quantity_supplied` increase, as under TX-7. Buyers lose (OC-4). For an import quota, TX-8 applies to export industries; DM-4 governs how the gap between the domestic and world price is split.
- **Assumes:** `binding`, `enforcement`.
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-3, LW-5.

### EN-7 Prohibition of a good moves trade underground
- **If:** `prohibition` of a good that some buyers continue to value highly.
- **Then:** `quantity_traded` legally falls to near zero; `informal_activity` increase; `price_paid` increase (sellers require compensation for the risk of punishment). RS-10 applies to the informal trade: higher search costs, less predictable quality, disputes settled outside the courts.
- **Assumes:** demand persists for some buyers; imperfect `enforcement`.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** RS-3, RS-10, LW-3.

### EN-8 Prohibition favors concentrated forms
- **If:** EN-7 applies, and penalties or detection risk depend on bulk or volume rather than on potency.
- **Then:** sellers shift toward more concentrated, potent forms of the good, which are cheaper to hide per unit of effect: `share_concentrated_forms` increase.
- **Assumes:** penalties scale with volume (`enforcement`).
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Source:** the "iron law of prohibition" (Cowen, 1986; Thornton, *The Economics of Prohibition*, 1991). Not a classical praxeological text; flagged for expert decision.

### EN-9 Supervised-practice requirement
- **If:** a license requires a period of practice supervised by existing license holders.
- **Then:** incumbents' willingness to supervise becomes a bottleneck on entry: `entry_rate` is limited by the number of supervised places, and where places are scarce relative to candidates, `wage_rate` of those in supervised practice decreases, as incumbents capture part of the value of the license through their trainees' pay.
- **Assumes:** supervision is costly or limited per supervisor (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** EN-1, LW-6.

### EN-10 Penalty records
- **If:** a prohibition (EN-7) or licensing rule is enforced by criminal convictions that are recorded and checked by employers.
- **Then:** for those convicted, `employment` and `earnings` decrease over the long run, compared with the counterfactual.
- **Assumes:** record-keeping and checking practice (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** long.
- **Builds on:** LW-1.

---

## DM: Dominance rules

Dominance rules decide the combined sign when chains conflict (workflow step 7). Each is itself an assumption and needs an estimate.

### DM-1 Incidence follows the alternatives
- **If:** TX-2 (a tax) or SB-2 (a subsidy) applies, and one side of the market has clearly fewer or worse alternatives than the other (buyers with no substitutes; sellers with highly specific, immobile resources).
- **Then:** that side bears the larger part of a tax, or receives the larger part of a subsidy. For a tax: if buyers have fewer alternatives, `price_paid` rises by most of the tax; if sellers do, `net_price_received` falls by most of it. For a subsidy: if buyers have fewer alternatives, `price_paid` falls by most of the subsidy; if sellers do, `net_price_received` rises by most of it. Record the split with `tax_share_borne` or `subsidy_share_received`.
- **Assumes:** the comparison of alternatives (`substitutability`, `mobility`), with evidence.
- **Tier** B. **Horizon**: over time, the side that owns redeployable capital gains alternatives as it redeploys (TS-1), so the burden shifts away from that side. In product markets the sellers own the capital, so incidence shifts toward buyers; in factor markets such as labor the buyers (employers) own it, so a payroll tax's incidence shifts toward workers.
- **Note:** Rothbard argued (*Power and Market*, ch. 4) that a general sales tax cannot be shifted forward to buyers and falls on factor owners. This differs from the standard treatment and applies to general, not selective, taxes. Whether to encode it as an option is question Q3 in `06_gaps.md`.

### DM-2 Quality under licensing
- **No default rule.** EN-4 stays ambiguous unless the case supplies evidence that one chain dominates: for example, the requirement is unrelated to the quality buyers care about (then only the "down" chain is active), or close unlicensed substitutes are unavailable (then the "down" chain is weak). Record such evidence as an assumption.

### DM-3 One-time cost against later gains (ambiguous by design)
- **No default rule.** When one chain imposes a one-time cost (training, conversion, relocation) and another produces a later stream of gains (a higher price, a lower cost), the combined effect on the actor class's earnings or welfare is `ambiguous`. Comparing them needs magnitudes and a discount rate, which the method does not supply. Report both chains, and state that the actors who chose to bear the cost expected the gains to be worth it (LW-5), while those who did not, did not.

### DM-4 Quota rent follows the scarce side
- **If:** EN-6 (an import quota) raises the domestic price above the world price.
- **Then:** if foreign supply comes from many competing sellers, the holders of quota rights capture most of the gap; if it comes from a few sellers who can coordinate, or if exporting countries administer their own shares of the quota, foreign sellers capture part of it.
- **Assumes:** the structure of foreign supply and of quota administration (`other`).
- **Tier** B.

### DM-5 Netting a timing shift
- **If:** SB-6 (or RS-8) produces a surge in one period and a dip in another, and the question is the total over a horizon that includes both.
- **Then:** the total rises if some purchases in the surge are additional, provided the dip consists only of purchases moved into the surge. If the policy is expected to recur, buyers wait for it, and the dip can include purchases that are merely delayed; then the total is `ambiguous`.
- **Assumes:** what the dip contains (`expectations`).
- **Tier** B.
