# 4. Rule catalog 0.8: patterns

This file holds the **patterns**: derived results for recurring situations. They rest on the **core rules** in `04a_core_rules.md`, which are the universal calculus. Every pattern below carries a **Derivation** line that shows which core rules it instantiates and how; a pattern adds no reasoning of its own beyond that derivation and the premises it names. If a pattern and a direct derivation from the core rules ever disagree, the derivation wins and the pattern is corrected.

Each pattern is one reusable inference. Format:

- **If:** the preconditions, stated as facts about the policy record or earlier consequences.
- **Then:** the conclusion, as a consequence in normal form (actor class, variable, sign).
- **Assumes:** empirical premises, each of which needs an estimate in the case at hand.
- **Unless:** known exceptions that block the rule.
- **Tier / visibility / horizon:** proposed defaults. A rule's tier is the tier of its conclusion when its preconditions hold; it is A only if it has no empirical assumptions.
- **Builds on:** foundations from `01_foundations.md`.
- **Source:** where the reasoning comes from, in the short forms of `07_sources.md`, which records how each citation was checked.
- **Derivation:** how the pattern follows from the core rules (`04a_core_rules.md`).

Patterns are deliberately small. A full analysis chains several of them, and each link is reviewed on its own.

**Changes in 0.8.** From the core-only re-runs of WE-026 to WE-035 (`08_core_rerun_report.md`, second round). Revised: OC-3 (enforcement the policy makes unnecessary), OC-1 and TX-1 (payers from a general budget are a group), RS-1 (the split between price and quantity of a substitute needs a supply premise), OC-5 (new activities), TS-3 (product standards), EN-6 (the wider-market price still moves), SB-10 (checks on the return crossing), RS-8 (opposing timing chains).

**Changes in 0.7.** From the ten gap-probing examples (WE-026 to WE-035). New patterns for moves that are general or recurred: PC-17 (mandated contract term), PC-18 (prohibited contract term), PC-19 (public supply at a set price), RS-17 (size thresholds), RS-18 (a per-head cost with a cap), OC-8 (crowding out by public borrowing), SB-10 (export subsidy). Widened: TX-8 (both directions of the currency link), RS-4, RS-8, RS-16, OC-1, OC-4, SB-8, EN-6. Moves seen once are listed as candidates in `06_gaps.md`, 6.2e.

**Changes in 0.6.** New patterns for moves that recurred in the core-only re-run without a pattern to prompt them: PC-16 (a ceiling as a transfer), RS-16 (a substitute's price after a demand shift), EN-11 (a license as a signal). RS-8 and SB-6 now state both sides of a timing shift.

**Changes in 0.5.** The core-only re-run of the 25 worked examples (`08_core_rerun_report.md`) found no claim the core rules could not derive, but found patterns that overclaim or lack a clause. Revised: EN-3, EN-4, DM-1, DM-2, RS-6, TX-3, RS-7, RS-10, PC-2, PC-8, OC-3, SB-1, SB-3, SB-4.

**Changes in 0.4.** The core rules (CR-1 to CR-12) are introduced and every pattern is given a derivation from them. Writing the derivations exposed four problems, now fixed: TX-6 stated as a priori a direction that depends on an empirical premise (CR-4's exception); OC-7 counted the gain to an asset's seller without the matching outlay of its buyer (CR-8 symmetry); RS-13 covered added supply but not withdrawn supply (symmetry); TS-4 cannot be derived at all and is quarantined.

**Changes in 0.3.** New: RS-12 to RS-15, OC-5 to OC-7, TS-5 to TS-9, PC-12 to PC-15, TX-10, TX-11, SB-8, SB-9, EN-9, EN-10, DM-4, DM-5. Widened: RS-4, RS-10, RS-11, TS-1, TS-3, PC-8, TX-6, TX-8, TX-9, SB-4, EN-6, EN-8, DM-1. Each change traces to a gap found in the worked examples (`06_gaps.md`, 6.2).

---

## RS: Generic responses

These apply to any intervention. Workflow step 5 runs through them for every actor class.

### RS-1 Substitution
- **If:** a policy raises the cost (money or otherwise) to an actor class of using a good or means, relative to an alternative that serves the same end.
- **Then:** `actor_class.quantity_substitute` increase; use of the target decreases at the margin.
- **Assumes:** a substitute exists and is not covered by the policy (`substitutability`). CR-4 gives only that more buyers turn to the substitute; `quantity_substitute` increase as a traded quantity also needs a premise that the substitute's supply can expand, and its price is then RS-16's question.
- **Unless:** the actor class has no margin of choice (a fixed contract during its term).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-2, LW-3.
- **Derivation:** CR-4 (x: the target, y: a substitute serving the same end).

### RS-2 Adjustment of quality and terms
- **If:** a policy fixes the money price or one term of an exchange below (or above) what the parties would agree.
- **Then:** the party disadvantaged adjusts unregulated terms in its own favor: `quality_per_unit`, `maintenance_spending`, service, contract length, or added conditions move against the other party.
- **Assumes:** some terms of the exchange are unregulated and adjustable.
- **Unless:** every relevant term is fixed and enforced.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** AX-1, LW-5.
- **Source:** HA ch. XXX §2; EIOL 1979 ch. 18 "What Rent Control Does" (maintenance; not in the 1946 edition).
- **Derivation:** CR-6 (pressure displaced to unregulated terms) with CR-5c.

### RS-3 Evasion
- **If:** complying with a rule costs an actor more than the expected cost of breaking it (probability of detection times penalty, plus moral and reputational cost).
- **Then:** `informal_activity` increase; `side_payments` increase where the rule fixes a price.
- **Assumes:** enforcement is imperfect (`enforcement`).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** AX-1, LW-1.
- **Derivation:** CR-4 (x: comply, y: violate; the expected penalty is a burden attached to y, CR-1).

### RS-4 Relocation across a boundary
- **If:** the policy applies within a boundary, and the activity can be carried out or bought on the other side of it.
- **Then:** activity and purchases move to whichever side the policy favors. Where the policy burdens activity inside: `cross_border_purchases` increase (buyers), or sellers and production relocate outside; activity inside decreases. Where it favors activity inside (a floor, subsidy or exemption that applies only there): `entry_rate` increase inside and `quantity_supplied` decrease just outside.
- Where a payment inside the boundary depends on an item crossing it (a refund, a subsidy on exports), items are drawn across it, including round trips made only to claim the payment.
- **Assumes:** the boundary is near enough for crossing to be worth its cost to some actors (`mobility`).
- **Tier** B. **Visibility** invisible. **Horizon** short (purchases) to long (firms).
- **Builds on:** RS-1.
- **Derivation:** CR-4 (x: act on this side, y: act on the other side), then CR-7 for the market on each side.

### RS-5 Reclassification
- **If:** the policy's definitions or exemptions draw a line between covered and uncovered goods, contracts or actors.
- **Then:** `reclassification` increase: goods, contracts and organizations are reshaped to fall on the favorable side (for example, conversion of rental units to owner-occupied units; reformulating a product below a tax threshold).
- **Assumes:** reshaping costs less than the policy's burden for some actors.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** AX-1.
- **Derivation:** CR-4 (x: the covered form, y: an uncovered form that serves nearly the same end).

### RS-6 Exit and reallocation
- **If:** the policy lowers the expected return of using resources in the target activity, relative to other uses.
- **Then:** `investment_target` decrease, then `quantity_supplied` and `capital_stock_target` decrease; `number_of_sellers` decrease or `entry_rate` decrease; labor in the activity: `employment` and `hours_worked` as a group, `at_least_one_decrease` (sellers may cut hours rather than staff). Resources go to other uses, where quantities rise.
- **Assumes:** resources have other uses (`alternative_uses`); speed depends on how specific and durable the resources are (`durability`; see TS-1).
- **Tier** B. **Visibility** invisible. **Horizon** medium to long.
- **Builds on:** LW-4.
- **Derivation:** CR-4 for each owner (x: this use, y: another use), aggregated by CR-7; timing by CR-10b.

### RS-7 Lobbying and rent-seeking
- **If:** the policy creates a gain that is concentrated on an identifiable group and depends on political decisions (renewal, extension, exemption, enforcement).
- **Then:** `lobbying_effort` by that group increase. Those concentrated groups harmed by the policy also lobby, for repeal or exemption.
- **Assumes:** the group can organize at a cost lower than its stake (`other`). This premise must be stated and estimated in each case, like any other.
- **Unless:** the counterfactual also has lobbying on the same question (a repeal, where the policy's beneficiaries would lobby to keep it in force). Then compare with that: the side that gains from the change lobbies more, the side that loses may lobby more or less, and the combined sign for a class that lobbied in both worlds is `ambiguous` without a premise.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** AX-1, LW-1.
- **Derivation:** CR-4 applied to political action (x: accept the decision, y: spend means to change it). The payoff to y rises with the concentrated gain or loss at stake.

### RS-8 Change of timing
- **If:** the policy treats the same action differently depending on when it is taken (announcement before effective date, phase-in, deadline, expected tightening or repeal).
- **Then:** actions are moved toward the favorable time: rush before a tax or cap takes effect, delay until after a repeal is expected, purchases pulled forward into a temporary subsidy. Every such move has two sides: the action rises in the favored window and falls in the window it was taken from. Record both, each signed against the counterfactual (`02_ontology.md`, 2.5).
- **Unless:** where a stock must be run down to a common deadline with no grandfathering (a phase-out), there is no favorable window to move toward, and the sign before the deadline is `ambiguous` rather than a rush. Where a claim on a future payment can be acquired before the charge that funds it starts (containers refundable before deposits are charged), holders acquire it in the gap. Where the policy also improves the earlier window (a clause applying the new rule to cases already pending, so that acting before the effective date is already partly protected), the two timing chains oppose each other. Check every provision for this before signing: the sign in that window is `ambiguous` without a dominance premise.
- **Assumes:** actors know the timing and can shift their actions.
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-7.
- **Derivation:** CR-10a with CR-4 (x: act at one time, y: act at another).

### RS-9 Bundled trips carry other purchases with them
- **If:** buyers of a good change where they buy it (RS-4 cross-border buying, or a switch to another store or channel), and they usually buy other goods on the same trip (a `complement` relation noted `trip`).
- **Then:** the other goods bought on those trips move with it: `quantity_traded` of untaxed or unregulated goods decrease at the sellers left behind and increase at the sellers gained.
- **Assumes:** buyers bundle purchases on trips (`other`); the destination sells the other goods too.
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1 (a trip has a cost, so buyers spread it over several purchases), RS-4.
- **Derivation:** CR-3c (a trip is a joint cost spread over the purchases made on it), so CR-4 moves the other purchases with the trip; CR-9 carries the change to sellers.

### RS-10 Driving trade into the informal market
- **If:** some trade in a good or service moves outside the legal market (RS-3, PC-6, EN-3, EN-7).
- **Then:** for that trade: `search_cost` increase (sellers cannot advertise openly); `quality_information` decrease and `quality_variability` increase (no brands, licensing, reviews or recourse to rely on); `disputes_settled_outside_courts` increase; sellers charge for the risk of punishment. In reverse (trade returning to the legal market after a repeal), `search_cost` and `disputes_settled_outside_courts` decrease and `quality_information` increases; `quality_variability` is `ambiguous` if the repeal also admits sellers who were previously excluded by a training or quality requirement.
- **Assumes:** penalties for informal trade are enforced at least sometimes (`enforcement`).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** AX-1, LW-1.
- **Derivation:** CR-1 (the options of advertising, open reputation and court enforcement are removed for illegal trade), CR-11b (less information), CR-7 (sellers' net yield is equalized, so the price includes compensation for penalty risk).

### RS-11 Lock-in spills into linked markets
- **If:** an actor class holds a non-transferable benefit that is lost by a change of location or status: moving (PC-7: a controlled tenancy, a place on a list), leaving an occupation, or letting a registration lapse (a grandfathered status).
- **Then:** members of the class turn down opportunities that would cost them the benefit: `job_changes` decrease, longer commutes, forgone breaks or better work elsewhere.
- **Assumes:** some valued opportunities would require the change (`mobility`); the benefit is not transferable.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1 (losing the benefit is part of the cost of moving), PC-7.
- **Derivation:** CR-3 (moving or changing status now also costs the forfeited benefit), then CR-4 (x: take the opportunity, y: keep the benefit).

### RS-12 Complement spillover
- **If:** the quantity traded, or the stock in use, of a good changes, and another good is recorded as its `complement` in use (not `trip`): cars and repairs, cars and fuel.
- **Then:** `quantity_complement` changes in the same direction; where the complement's supply is slow to adjust, `price_complement` moves the same way too.
- **Assumes:** the complement relation is close, and the complement has few other uses (`substitutability`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-2.
- **Derivation:** CR-9 with LW-10 (complements: the value of a means depends on what it is used with).

### RS-13 Supply spillover
- **If:** a policy adds quantity supplied to a linked market (exempt new building next to a capped segment, subsidized output fed into a wholesale market, released public stocks), or withdraws it (units removed from a segment, production stopped).
- **Then:** the price in that market decreases where supply is added, and increases where it is withdrawn (`price_substitute`, or that market's `price_paid`), compared with the counterfactual.
- **Assumes:** the added supply is not offset by withdrawal elsewhere; buyers there do not absorb it at an unchanged price (`substitutability`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-3. This is the general form of the opposing chain noted under PC-8.
- **Derivation:** CR-9 then CR-6 in the linked market: added supply at an unchanged price leaves sellers unsatisfied, so the price falls; withdrawn supply is the mirror case.

### RS-14 Input cost pass-through
- **If:** a policy raises the cost of an input (a tax or floor on labor, a tariff on a material, a regulated price) that is a material part of the cost of some output.
- **Then:** for the output: `price_paid` by its buyers increase and/or `quantity_supplied` decrease (at least one). Where the sellers' competitors face the same increase, the price rise dominates; where competitors are exempt (imports, untaxed or uncovered sellers), RS-6 applies and the quantity effect dominates.
- **Assumes:** the input cannot be fully replaced at the old cost (`substitutability`); the competitors' exposure (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-4, TX-2. The upstream counterpart, for a cap on the output, is PC-12.
- **Derivation:** CR-9 with LW-10 (an input's price is part of the cost of the output), then CR-7: where competitors face the same cost, no seller can avoid it and the price of the output moves; where they do not, the exposed sellers are the ones that must move (CR-4, exit).

### RS-15 Discretionary relief is rationed by non-price criteria
- **If:** relief from a policy's burden (an exclusion, waiver, permit or exemption) is granted case by case at officials' discretion, and is worth more to applicants than its fee.
- **Then:** `allocation_by_non_price_criteria` increase among applicants; `compliance_cost` of applying increase; `lobbying_effort` increase, both by applicants and by those who gain when relief is denied.
- **Assumes:** the grant is discretionary and valuable (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-6 (relief is scarce and not priced), RS-7.
- **Derivation:** CR-6 (relief is scarce and not priced, so it is allocated by other criteria) and CR-4 applied to applicants and to political action.

### RS-16 A substitute's price after a demand shift
- **If:** a policy moves buyers from a good to a substitute (by taxing, banning, capping or licensing the good), outside any price control on the substitute.
- **Then:** `quantity_substitute` increases, and `price_substitute` increases where the substitute's supply cannot expand at an unchanged cost in the period considered.
- **Assumes:** `substitutability`; the substitute's supply is not perfectly elastic in the period (`durability`, `alternative_uses`).
- **Unless:** the policy also adds supply to the substitute's market (RS-13), in which case the price is `ambiguous` without a premise.
- **Mirror case:** a policy that makes a good cheaper or more available (a free public service) pulls buyers from its substitutes: `quantity_substitute` decreases and `price_substitute` decreases where their supply cannot contract at once.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-3.
- **Derivation:** CR-9 (buyers turn to the substitute) then CR-6 in the substitute's market (at the old price, buyers wish to buy more than sellers wish to sell, so the price rises as far as supply cannot expand). PC-8 is the same move for a controlled market.

### RS-17 Size thresholds
- **If:** a policy applies only above a size threshold (outlets, employees, revenue), measured at a date or over a past period.
- **Then:** firms near the threshold stay below it (`number_of_sellers` just below the threshold increases relative to just above), split activity across separately counted units (second brands, separate entities: `reclassification` increase), and the value of growing past the threshold falls (CR-7c: `asset_value` of firms near it decreases). Where the threshold is measured over a past period, the response comes in that period, before the policy takes effect.
- **Assumes:** the cost of the policy is material relative to the gain from growing (`binding`); splitting is legal and cheap enough (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-2.
- **Derivation:** CR-1 (the operation applies only above the threshold), CR-4 (x: grow past it, y: stay below or split), CR-7c, CR-10a.

### RS-18 A per-head cost with a cap
- **If:** a policy imposes a cost per worker (or per unit) that stops at a cap (a contribution up to a ceiling, a leave entitlement up to a maximum).
- **Then:** below the cap the cost raises the price of every hour and every head; above it, an extra hour from an existing worker adds nothing while an extra worker adds the full cost. Employers shift hours toward fewer heads: `hours_worked` per worker increases and `employment` decreases where workers are above the cap, as a mixed group.
- **Assumes:** hours and heads are substitutes in production (`substitutability`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-2.
- **Derivation:** CR-4 (x: another worker, y: more hours from existing workers) with the cost attached only to x above the cap.

---

## OC: Opportunity cost

Opportunity costs are recorded as signed changes in variables (`02_ontology.md`, 2.5), never as a separate "loss" entry.

### OC-1 Diverted resources
- **If:** the policy takes resources from an actor class (tax, mandated purchase, compliance) or directs resources to a use.
- **Then:** `resources_available_other_uses` decrease for that actor class; the goods they would have bought or produced with those resources are not produced, so `quantity_traded` decrease in the markets where they would have spent it. The spending or use is visible; the forgone alternative is not.
- **Naming the forgone uses.** Where means are taken directly (a tax, a levy), which uses are given up needs a premise (CR-4, a change in means alone). Where they are taken through a market (public borrowing draws on the loan market), the forgone uses are those of that market's marginal participants (the borrowers crowded out), which can be named with a premise about who they are.
- **Who pays.** Where the means come from a general budget and the record names no tax, the payers are a group (taxpayers, recipients of other spending, future taxpayers) with `at_least_one_decrease`; do not name taxpayers alone. Where the means are borrowed, the lenders' side is recorded too (OC-8).
- **Saving is a use.** For payers who may cut saving rather than purchases, `quantity_traded` falls in named markets only with a premise (CR-4, 0.7).
- **Tier** A, given that resources are taken. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1.
- **Source:** Bastiat 1850, §1 "The Broken Window"; EIOL 1946 ch. 2 to 4.
- **Derivation:** CR-8a.

### OC-2 Unpriced time and effort
- **If:** the policy causes actors to spend time or effort that buys nothing they value for its own sake: queuing (PC-2), searching, paperwork, qualification hours beyond what buyers would demand (EN-1).
- **Then:** `wait_time`, `search_cost` or `compliance_cost` increase; the forgone uses of that time are an invisible cost.
- **Tier** A, given the time is spent. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1.
- **Derivation:** CR-3c and CR-8c.

### OC-3 Administration and enforcement
- **If:** the policy must be administered or enforced.
- **Then:** `enforcement_cost` increase for `officials.enforcement`. Who bears it depends on the funding, which must be stated:
  - from a budget that rises with the new task: `taxpayers` (OC-1 applies);
  - from a fixed budget: enforcement of other rules falls instead (CR-8a), and the cost falls on those whom that enforcement protected;
  - from the policy's own revenue: it reduces what the revenue does elsewhere (CR-8d), not general taxpayers' means.
  - from a general budget where the record names no tax: the payers are a group (taxpayers, recipients of other spending, future taxpayers through borrowing) with `at_least_one_decrease` (CR-8, 0.7).
- **Against the right baseline.** The comparison is enforcement without the policy, not zero. Where the policy shrinks an activity that was itself enforced (complaints about backyard flocks under a nuisance law), enforcement of the old rule falls; the net sign is `ambiguous` without a dominance premise (arithmetic on the case's figures may supply one).
- **Tier** A, given positive enforcement activity and no enforcement the policy makes unnecessary; otherwise B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1.
- **Derivation:** CR-8c, with CR-8a for the funding.

### OC-4 Prevented exchanges
- **If:** the policy prevents exchanges that buyers and sellers would otherwise have made (a ceiling, a floor, a license requirement, a prohibition, a tax that prices some buyers out).
- **Then:** `quantity_traded` decrease for the prevented exchanges; both parties to each lose the gain they expected from it. Name both sides.
- **Unless:** the exchange is not prevented but lost to a better offer the policy creates elsewhere (a subsidy draws a buyer to another seller). Then only the party who loses the sale loses (CR-5).
- **Tier** A (ex ante, by each party's own ranking). **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-5.
- **Source:** P&M ch. 2 §2 and ch. 3 §1.
- **Derivation:** CR-5a.

### OC-5 Diverted spending diverts work (Hazlitt's tailor)
- **If:** a policy changes where an actor class spends (OC-1: money taken and spent by others; SB-8: money freed), so that `quantity_traded` falls in some markets and rises in others.
- **Then:** `employment` or `hours_worked` decrease in the markets that lose the spending and increase in those that gain it. The jobs the policy creates are visible; the jobs it prevents elsewhere are not.
- **Assumes:** sellers adjust their labor to their sales (`alternative_uses`).
- **New activities.** Where the activity that gains is new (a redemption center, a new service), it starts from zero, so hours cannot substitute for jobs: `employment` increase alone is derivable there. The group form applies to existing activities.
- **Tier** B. **Visibility**: the gain is visible, the loss invisible. **Horizon** short to medium.
- **Builds on:** OC-1, LW-4.
- **Source:** EIOL 1946 ch. 2 (the tailor who does not get the order for a suit) and ch. 4 ("for every public job created ... a private job has been destroyed somewhere else"); Bastiat 1850, §1, where the forgone purchase is shoes or a book.
- **Derivation:** CR-8b (spending diverted from some sellers is received by others), then CR-9 with LW-10 (demand for labor is derived from demand for what it produces).

### OC-6 Lost revenue is made up elsewhere
- **If:** a repeal or cut reduces `tax_revenue` that the budget was spending.
- **Then:** other taxes rise, borrowing rises (implying later taxes), or spending falls. Apply TX-1 and OC-1 to whichever group bears the replacement, named from the budget response. If the record does not say, state the replacement chain with a `revenue_use` assumption; where it frees resources for the same group that the repeal relieves, combine the chains (workflow step 7).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-1, SB-1 (its mirror case).
- **Derivation:** CR-8b (the budget's spending must be paid for by someone), with CR-8a for whoever pays.

### OC-7 Revaluation changes holders' means
- **If:** `asset_value` of an asset held by an actor class rises or falls (SB-4).
- **Then:** when they sell or borrow against it, their `resources_available_other_uses` change in the same direction, and so do their purchases in linked markets (homeowners whose homes gain value bid for larger homes). The buyers of the asset have correspondingly fewer means for other purchases; record that chain too.
- **Assumes:** the change can be realized by sale or borrowing (`other`), and is not offset by an equal change in the price of what they intend to buy.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1.
- **Derivation:** CR-8b: when an asset that has risen in value is sold, the seller's gain in means is the buyer's outlay. Symmetry requires the matching chain: buyers of the asset have fewer means for other purchases. Combine the two with CR-12.

### OC-8 Crowding out by public borrowing
- **If:** `government_borrowing` finances a policy.
- **Then:** the means lent to the state are not available to other borrowers (CR-8a): `interest_rate` increases for them and their borrowing (for investment, house purchase) decreases, unless the lending comes from abroad; repayment implies taxes later (CR-8b), recorded as a group of later payers. Lenders receive the interest (CR-8b).
- **Assumes:** the loans come from domestic saving that would otherwise have been lent at home (`other`); the debt is expected to be repaid, not rolled over (`expectations`).
- **Tier** B. **Visibility** invisible. **Horizon** short to long.
- **Builds on:** LW-1, LW-7.
- **Derivation:** CR-8a and CR-8b; CR-6 in the loan market (more demand for loans at the old rate); CR-7a (lenders move to the higher rate); CR-10 for the later taxes.

---

## TS: Time structure

### TS-1 Durable capital lag
- **If:** a consequence works through reduced investment or maintenance in durable capital (buildings, equipment, trained skills).
- **Then:** the effect on `capital_stock_target` and `quantity_supplied` is small at first and grows as the existing stock wears out and is not replaced. Set horizon to medium or long; `quality_per_unit` often falls before quantity does.
- **In the other direction:** when a policy (or a repeal) raises the return on durable capital, the stock grows at the speed of new investment (planning, permits, finance, construction, training), which is not the mirror of wear-out. State that lag as a `durability` assumption; TS-5 may slow it further.
- **Assumes:** the durability of the capital involved (`durability`).
- **Tier** B. **Horizon** medium to long.
- **Builds on:** LW-4, LW-7.
- **Derivation:** CR-10b.

### TS-2 Expectations
- **If:** actors expect the policy to be extended, tightened, made permanent or applied to new categories.
- **Then:** responses that the policy would cause in future are brought forward: investment falls now in categories expected to be covered; actors rush to get into exempt categories before the rules change.
- **Assumes:** what actors expect (`expectations`).
- **Tier** B. **Horizon** short to medium.
- **Builds on:** LW-7.
- **Derivation:** CR-10a.

### TS-3 Erosion of a fixed parameter
- **If:** a cap, floor, rate, threshold or quantity is fixed in money terms or in physical units (a number of licenses, a tonnage), or indexed at a rate different from the change in the relevant market price or demand.
- **Then:** the component becomes more binding (or less) over time as prices or demand move. A ceiling or quota that is not binding at enactment can become binding later.
- **Assumes:** the expected path of market prices or demand.
- **Tier** B. **Horizon** medium to long.
- **Product standards.** A standard on a product's specification has no clearing price to move past. It binds on the share of designs actors would choose below it (CR-1, CR-4 over the spread of designs), and that share changes as costs and the counterfactual trend move (CR-10a).
- **Derivation:** CR-6 (a fixed parameter binds when the clearing price or demand moves past it) with CR-10a (expected path); for a product standard, CR-1 and CR-4 with CR-10a.

### TS-4 The intervention spiral (proposed, contested)
- **If:** a policy produces consequences that its supporters regard as problems (shortages, black markets, evasion).
- **Then:** pressure for further intervention to address them (extending controls to substitutes, rationing schemes, penalties), or for repeal.
- **Tier** C. **Status:** not derivable (see Derivation); kept out of Tier A and B results until the experts decide what premises would make it a pattern. See `06_gaps.md`, Q4.
- **Source:** Mises, *A Critique of Interventionism* (1929), Part I; HA ch. XXX §2 (a price ceiling must be extended to other goods) and ch. XXXVI.
- **Derivation:** Not derivable from the core rules. It needs a premise about what a policy's supporters believe about its effects and how political decisions respond, which is neither a core rule nor a fact about the policy record.

### TS-5 Credibility of a repeal
- **If:** a policy is repealed (or not renewed), and actors give a meaningful probability to its return within the payback period of their investments.
- **Then:** responses that pay back quickly (repairs, pricing, lettings, short contracts) go ahead; responses that pay back only over long periods (major renovation, new construction, entry with sunk costs) are smaller and later than the mirror of the original policy's effects. Where the expected return would exempt existing practitioners (grandfathering), it brings entry forward instead. The losing side responds too: those who gained from the policy and expect it back delay scrapping, selling or retraining, and keep capacity on standby.
- **Assumes:** the probability of re-imposition over a named period (`expectations`).
- **Tier** B. **Horizon** medium to long.
- **Builds on:** LW-7, TS-2.
- **Derivation:** CR-10a with CR-4: the expected yield of a long-lived investment includes the chance that the old policy returns; quick-payback actions depend on it less.

### TS-6 Stock changes persist after repeal or erosion
- **If:** a policy is repealed, or its incentive erodes (TS-3), and it had caused reclassification (RS-5), exit (RS-6, EN-3), or the loss of specific capital, skills or client relationships, and reversing these has a cost (reassembling converted units, rebuilding capacity, retraining, re-establishing a client base).
- **Then:** a repeal (or erosion) reverses the flow but not the stock already changed, except where the restored return exceeds the cost of reversal. Responses that required sunk investment (a smuggling network, converted buildings) shrink by less than the incentive does. Former sellers return only partly and slowly; firms that closed re-enter as the sunk costs of entry are paid; people displaced stay displaced. Record the expected `persistence` (none, partial, full) on each repeal consequence.
- **Assumes:** the cost of reversal (`reversal_cost`), including how long people and capital have been away.
- **Tier** B. **Horizon** medium to long.
- **Builds on:** LW-1, LW-4, TS-1.
- **Derivation:** CR-10b with CR-3: undoing a stock change has a cost, so it is undone only where the restored yield exceeds it (CR-4).

### TS-7 Expected caps reduce stocks held
- **If:** sellers expect a `price_ceiling` to apply in future periods of scarcity (an anti-gouging rule, a standing threat of price controls).
- **Then:** `inventory_held` before those periods decreases, because the expected return to storing goods for the scarce period falls. Less is available when scarcity arrives.
- **Assumes:** storage is costly and the cap is expected to bind (`expectations`, `binding`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-4, LW-7.
- **Derivation:** CR-7 across time (storage moves a good from a time of plenty to a time of scarcity) and CR-10a: a cap expected in the scarce period lowers the yield of storing.

### TS-8 Habit adjustment
- **If:** a policy changes the cost of a routine, often-repeated action (carrying bags, a commute, a shopping pattern).
- **Then:** responses are smaller at first and grow over weeks or months as routines change; some short-run effects (fee payments, use of the costlier option) shrink over the same period without any change in prices or capital. Set the horizon of the full response to short-to-medium and describe the path.
- **Assumes:** the action is repeated often (`other`).
- **Tier** B. **Horizon** short to medium.
- **Builds on:** AX-1, LW-1 (learning a new routine has a cost).
- **Derivation:** CR-3 and CR-10b: changing a routine has a cost (attention, learning) paid over time, so CR-4's switches happen gradually.

### TS-9 Capital per worker and wages
- **If:** a policy reduces saving or investment across the economy (TX-6), so that `capital_stock_economy` is smaller over time than it would have been.
- **Then:** `wage_rate` across the economy is lower in the long run than it would have been, because labor works with less capital.
- **Assumes:** no offsetting inflow of foreign capital (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** long.
- **Builds on:** LW-7, LW-4.
- **Source:** HA ch. XXI §6 "Wages and Subsistence".
- **Derivation:** CR-7 (labor's price tends to its discounted marginal value product) with LW-9 and LW-10 (labor's product depends on the capital it works with).

---

## PC: Price controls

### PC-1 Binding ceiling: excess demand
- **If:** `price_ceiling` on a good, below the price at which quantity demanded would equal quantity supplied.
- **Then:** `excess_demand` increase: at the controlled price, quantity demanded exceeds quantity supplied.
- **Assumes:** the ceiling is binding (`binding`) and enforced (`enforcement`).
- **Unless:** the ceiling is above the market price (not binding); price is a quality signal (LW-3 exception).
- **Tier** B. **Visibility** invisible (the shortage is often noticed, but its cause is not attributed to the policy). **Horizon** short.
- **Builds on:** LW-3, LW-4.
- **Source:** HA ch. XXX §2; P&M ch. 3 §1; EIOL 1946 ch. 17.
- **Derivation:** CR-6 (a price held below the clearing level).

### PC-2 Shortage is rationed by other means
- **If:** `excess_demand` increase (PC-1).
- **Then:** for `buyers.prospective`, the group `wait_time`, `search_cost`, `side_payments`, `allocation_by_non_price_criteria`: `at_least_one_increase`. Any one member is signed on its own only with a premise that that margin is open and used in this market. The good does not go to whoever is willing to give up the most for it, but by these other criteria.
- **Tier** A, given the shortage; the particular form is B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-6.
- **Derivation:** CR-6 (the scarce side chooses by other criteria).

### PC-3 Buyers split into insiders and outsiders
- **If:** `excess_demand` increase (PC-1).
- **Then:** `buyers.current` who obtain the good at the controlled price gain (`price_paid` decrease for them); `buyers.prospective` who cannot obtain it lose: they pay more elsewhere, wait, or go without.
- **Tier** A, given the shortage. **Visibility**: the insiders' gain is visible; the outsiders' loss is invisible. **Horizon** short.
- **Builds on:** LW-5, LW-6.
- **Derivation:** CR-6 and CR-5: those who obtain the good gain the gap between the controlled and the clearing price; those who do not, lose the exchange (CR-5a) or pay more elsewhere.

### PC-4 Quality falls under a ceiling
- **If:** binding `price_ceiling` (PC-1), and sellers control unregulated aspects of quality.
- **Then:** `quality_per_unit` and `maintenance_spending` decrease; the quality-adjusted price moves back toward the market level.
- **Assumes:** quality and maintenance are not fully regulated or enforced (`enforcement`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** RS-2.
- **Derivation:** CR-6 (pressure displaced to quality) with CR-5c.

### PC-5 Supply shrinks under a ceiling
- **If:** binding `price_ceiling` (PC-1).
- **Then:** `investment_target` decrease, then `quantity_supplied` decrease, as resources move to uncontrolled uses.
- **Assumes:** `alternative_uses` exist for the resources (for housing: conversion to owner-occupation or other uses, demolition, keeping units off the market); speed governed by TS-1.
- **Unless:** the resources are completely specific and have no other use, in which case quantity supplied from the existing stock holds until it wears out (TS-1 still applies to new investment).
- **Tier** B. **Visibility** invisible. **Horizon** medium to long.
- **Builds on:** LW-4, RS-6, TS-1.
- **Source:** EIOL 1979 ch. 18 "What Rent Control Does" (not in the 1946 edition).
- **Derivation:** CR-7 (owners move resources to uses whose yield is not capped), timed by CR-10b.

### PC-6 Black and grey markets under a ceiling
- **If:** binding `price_ceiling` (PC-1).
- **Then:** `informal_activity` and `side_payments` increase: some exchanges happen at prices above the ceiling, disguised or illegal (key money, tie-in sales, sublets at market rent). RS-10 applies to that trade.
- **Assumes:** imperfect `enforcement`.
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** RS-3.
- **Derivation:** CR-6 (exchanges outside the rule) via CR-4 (x: comply, y: violate).

### PC-7 Reduced turnover where the benefit is tied to holding
- **If:** binding `price_ceiling`, and the right to buy at the controlled price is tied to keeping the good (a tenancy, a place on a list), and cannot be sold.
- **Then:** `turnover` decrease among insiders: they move less, even when another unit, job or place would otherwise suit them better.
- **Assumes:** the benefit is not transferable (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-2, LW-5.
- **Derivation:** CR-3 (giving up the good now forfeits the gap between controlled and market price) and CR-4.

### PC-8 Spillover to uncontrolled substitutes
- **If:** a binding `price_ceiling` or `price_floor` covers part of a market, and an uncontrolled substitute or segment exists (recorded market relation).
- **Then:** demand moves to the uncontrolled segment (under a ceiling, from outsiders who cannot obtain the good, PC-3; under a floor, from buyers avoiding the higher price): `price_substitute` increase, which harms `buyers.substitutes`.
- **Assumes:** `substitutability` between the segments.
- **Unless:** the policy also pushes sellers into the uncontrolled segment (sellers shut out of the controlled one by a cap on their number, owners moving units out of the controlled segment, exempt new building). Then RS-13 adds supply there, and the combined sign of `price_substitute` is `ambiguous` unless a premise says which chain dominates.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** RS-1, PC-3.
- **Note:** another chain can push `price_substitute` the other way: resources withdrawn from the controlled segment (PC-5) may reappear in the uncontrolled one (for example, new building that is exempt from the cap), adding supply there (RS-13). Combine the chains using the procedure in workflow step 7.
- **Derivation:** CR-9 (unsatisfied buyers, or buyers avoiding a floor, turn to the uncontrolled segment) and CR-6 in that segment.

### PC-9 Binding floor: excess supply
- **If:** `price_floor` on a good, above the price at which quantity demanded would equal quantity supplied.
- **Then:** `excess_supply` increase; `quantity_traded` decrease (buyers buy less at the higher price).
- **Assumes:** `binding`, `enforcement`.
- **Unless:** the state buys the surplus (then see SB rules for the purchase).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-3, LW-6.
- **Derivation:** CR-6 (a price held above the clearing level).

### PC-10 Minimum wage: fewer hires of the least productive
- **If:** `price_floor` on labor (minimum wage) above the wage some workers can command.
- **Then:** for workers whose labor employers value below the floor: `employment` decrease or `hours_worked` decrease, or `non_wage_compensation` decrease (RS-2). Workers who keep their jobs at the floor: `wage_rate` increase.
- **Assumes:** `binding` for an identifiable group; `enforcement`; employers can adjust hours, staffing, automation or non-wage terms.
- **Tier** B. **Visibility**: the wage rise is visible; lost hires and cut hours are invisible. **Horizon** short to medium.
- **Builds on:** PC-9, LW-4.
- **Source:** HA ch. XXX §3 "Minimum Wage Rates"; EIOL 1946 ch. 18 "Minimum Wage Laws" (ch. 19 in 1979).
- **Note:** the empirical size of the employment effect is contested (Card and Krueger, *American Economic Review* 84(4), 1994, and the literature since). Earnings of the low-wage group as a whole combine opposite chains and are `ambiguous` unless a dominance rule applies. This is a designated contested case for evaluation.
- **Derivation:** CR-6 applied to labor (a price held above the level some workers can command), with CR-4 for employers' margins: hiring, hours, non-wage terms.

### PC-11 Non-price selection under a floor
- **If:** binding `price_floor` (PC-9).
- **Then:** buyers choose among excess sellers by non-price criteria: `allocation_by_non_price_criteria` increase. Under a minimum wage, employers become more selective (credentials, experience), and the cost to them of discriminating falls.
- **Tier** A, given the surplus; its form is B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-6 (applied to the selling side).
- **Derivation:** CR-6 (the scarce side, here buyers, chooses by other criteria).

### PC-12 A ceiling passes up to the inputs
- **If:** a binding `price_ceiling` on a good, and the capped sellers buy most of a named input (relation `input_to`).
- **Then:** `net_price_received` by input suppliers for sales into the capped market decreases, and/or the capped sellers buy less of the input (`quantity_demanded` of the input decreases).
- **Assumes:** the input has few uncapped outlets in the period considered (`alternative_uses`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-4, PC-5. The downstream counterpart is RS-14.
- **Derivation:** CR-9 with LW-10 (the input's demand derives from the capped output), then CR-7 (the input supplier with few other outlets bears it).

### PC-13 Ceilings that allow documented costs
- **If:** a binding `price_ceiling` allows increases only for documented costs (invoiced freight, wholesale prices), not for costs that leave no paper trail (the owner's labor, risk, the value of the goods elsewhere).
- **Then:** `number_of_sellers` decreases most among sellers whose main costs are undocumented (occasional and informal suppliers, people bringing goods from outside); `compliance_cost` increases for sellers who use the defense.
- **Assumes:** the enforcing agency's definition of a documentable cost (`enforcement`).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-4, RS-6.
- **Derivation:** CR-1 (the cap with a documented-cost exception burdens sellers differently by the kind of cost they bear), then CR-4 for each kind of seller.

### PC-14 Rate caps bind hardest on small and short transactions
- **If:** a binding `price_ceiling` is stated as a rate per unit of value and time (an annual interest rate, a percentage markup), and a material part of the seller's cost is fixed per transaction (processing, collection).
- **Then:** sellers raise the minimum size and length of the transactions they offer: `transaction_size` increase; `quantity_supplied` of small, short transactions decreases most; `variety` decreases at the small end.
- **Assumes:** the share of fixed per-transaction costs (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-4, RS-2.
- **Derivation:** CR-6 with CR-4: where part of the cost is fixed per transaction, a cap stated as a rate leaves small transactions unprofitable first.

### PC-15 Regulated cost recovery over a shrinking base
- **If:** a regulator sets a price to recover largely fixed costs per unit sold (utility rates), and a policy reduces the units sold through the regulated channel.
- **Then:** at the next rate review, `price_paid` per unit increases for the remaining buyers.
- **Assumes:** the regulator's rate method (`other`); fixed costs do not fall with sales.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1.
- **Derivation:** CR-1 (the regulator's pricing rule is part of the situation), applied with CR-2 to the regulator.

### PC-16 A binding ceiling is a transfer
- **If:** a binding `price_ceiling` (PC-1), and some buyers obtain the good at the controlled price.
- **Then:** for each unit traded at the controlled price, the buyer pays less and the seller receives less than at the clearing price, by the same amount: `price_paid` decrease for buyers who obtain the good and `net_price_received` decrease for sellers. Record both sides. Side payments (PC-6) and lower quality (PC-4) take back part of the transfer.
- **Tier** A, given the ceiling binds and is enforced for those units. **Visibility**: the buyers' gain is visible; the sellers' loss is invisible. **Horizon** short to long.
- **Builds on:** LW-5.
- **Derivation:** CR-8b (every payment is a receipt: what the buyer does not pay, the seller does not receive) with CR-6 (the clearing price is the comparison).

### PC-17 Mandated contract term
- **If:** a `mandated_contract_term` requires every contract of a kind to include a term (paid sick leave, a notice period), and the term is absent from some contracts that would otherwise be made.
- **Then:** for those contracts, the cost to the party who must provide the term rises (CR-1, operation 3); the bargaining range moves (CR-5c), so the other terms adjust: for an employment term, a mixed group of `wage_rate` (−), `non_wage_compensation` (−) and `employment`/`hours_worked` (−), sign `at_least_one_as_stated`. Parties who already included the term are not bound (not binding for them). Where the term is worth something to the side that receives it, part of the cost is recovered through the other terms (CR-7, gross and net).
- **Assumes:** the term was absent for some contracts (`binding`); `enforcement`. Why it was absent (the parties' own rankings, or an obstacle to agreeing) is a premise (CR-2), and decides whether the receiving side is better off by its own ranking.
- **Tier** B. **Visibility**: the term is visible; the adjustment of other terms is invisible. **Horizon** short to medium.
- **Builds on:** LW-5.
- **Derivation:** CR-1 (operation 3 on the option of contracting without the term), CR-5c (the range moves), CR-6 (pressure displaced to the other terms), CR-7b (who bears the net cost), CR-12 (the group).

### PC-18 Prohibited contract term
- **If:** a `term_prohibition` makes a contract term unenforceable (a non-compete clause, an exclusivity clause), in new contracts and possibly in existing ones.
- **Then:** the option of buying the term's protection is removed for one party and the option of breaking it is added for the other (CR-1). The bargaining range moves (CR-5c): the party who valued the term offers less on other terms or shifts to substitute terms (a mixed group: `wage_rate` (−), training it funds (−), `term_prevalence` of substitute terms (+), sign `at_least_one_as_stated`). Where existing contracts are voided, the right voided is transferred from its holder to the other party (CR-8, voiding). Where the term restrained the mobility of a means, the gain from mobility goes to its owner (CR-7, a policy that makes a means mobile).
- **Assumes:** the term was in use (`binding`); substitute terms are available or not (`substitutability`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-5.
- **Derivation:** CR-1, CR-5c, CR-6 (pressure displaced to the other terms), CR-7 (mobility), CR-8 (voiding), CR-12.

### PC-19 Public supply at a set price
- **If:** `public_supply` of a good at a set price below the clearing price (zero, for a free service), with the quantity fixed by a budget.
- **Then:** excess demand at the set price (PC-1); the pressure goes to the margins open to buyers sharing the fixed quantity: `wait_time`, crowding (`quality_per_unit` down), `travel_time`, as a mixed group (CR-6, public supply). Buyers who would have paid anyway gain what they no longer pay (SB-8). Buyers move from substitutes (RS-16, mirror case). The funding is binary and analyzed separately (SB-1).
- **Assumes:** `binding`; the budget does not expand with use (`revenue_use`).
- **Tier** B. **Visibility**: the free service is visible; crowding and the funding are invisible. **Horizon** short to medium.
- **Builds on:** LW-3, LW-6.
- **Derivation:** CR-6 (public supply), CR-8b, CR-9.

---

## TX: Taxes and tariffs

### TX-1 Tax takes resources
- **If:** a tax is imposed and collected.
- **Then:** `resources_available_other_uses` decrease for the actor classes that bear it (see TX-2 for who bears it); `tax_revenue` increase. Apply OC-1 to what those actors would have done with the money, and analyze the spending of the revenue as a separate component. Where a shortfall in revenue is made up from a general budget, its payers are a group (OC-1, Who pays).
- **Tier** A, given collection. **Visibility**: the payment is visible; the forgone uses are invisible. **Horizon** short.
- **Builds on:** LW-1.
- **Source:** P&M ch. 4.
- **Derivation:** CR-8a and CR-8b.

### TX-2 Per-unit tax: wedge and smaller market
- **If:** `per_unit_tax` or `ad_valorem_tax` on the sale of a good.
- **Then:** `price_paid` by buyers increase and/or `net_price_received` by sellers decrease (at least one must happen); `quantity_traded` decrease.
- **Assumes:** at least one side can reduce its quantity in response (some `substitutability` for buyers, or `alternative_uses` for sellers).
- **Tier** B. **Visibility**: the price rise is visible; the fall in quantity and in sellers' net price is invisible. **Horizon** short.
- **Builds on:** LW-3, LW-4.
- **Note:** how the burden splits between buyers and sellers is not fixed by this rule. Use DM-1, or report the split as ambiguous.
- **Derivation:** CR-5c (the tax is a wedge between what buyers pay and sellers keep) with CR-4 for each side.

### TX-3 Taxed activity shrinks; resources move to untaxed uses
- **If:** TX-2 applies.
- **Then:** `investment_target` in the taxed activity decreases over time; `employment` and `hours_worked` there, as a group, `at_least_one_decrease`; `quantity_substitute` increase.
- **Assumes:** `alternative_uses`, `substitutability`.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** RS-1, RS-6.
- **Derivation:** CR-7.

### TX-4 Avoidance of a local tax
- **If:** a tax applies within a jurisdiction with nearby untaxed places, or with definitions that can be avoided.
- **Then:** RS-4 (cross-border purchases), RS-5 (reformulation, reclassification) and RS-3 (evasion) apply. Taxed sales inside the boundary fall by more than total consumption does.
- **Assumes:** `mobility`; cost of reformulating.
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** RS-3, RS-4, RS-5.
- **Derivation:** CR-4 (relocate, reclassify, evade), as RS-3 to RS-5.

### TX-5 Compliance cost
- **If:** a tax requires record-keeping, filing, labeling or collection by private parties.
- **Then:** `compliance_cost` increase for those parties; OC-1 applies to those resources.
- **Tier** A, given positive compliance work. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1.
- **Derivation:** CR-8c.

### TX-6 Taxes on the return to saving and investment
- **If:** a tax falls on interest, dividends, capital gains or profits.
- **Then:** the net return on providing future goods falls; at the margin, saving and `investment_target` decrease, and the capital stock is smaller over time than it would have been.
- **Assumes:** for the group as a whole, the substitution response (save less as the future becomes dearer) outweighs the response of savers aiming at a fixed sum (`other`). Without this premise the direction is `ambiguous` (see Derivation).
- **Unless:** some savers aim at a fixed future sum, for whom a lower net return calls for more saving. Where such savers are a material part of the group, total saving by the group is `ambiguous`; the sign holds firmly only for saving in the taxed forms by savers who have untaxed alternatives. (Pending expert decision, `06_gaps.md` Q14.)
- **Tier** B. **Visibility** invisible. **Horizon** long. Variables: `saving`, `investment_target`, `capital_stock_economy`; TS-9 carries the effect on wages.
- **Builds on:** LW-7, LW-4.
- **Derivation:** CR-4 with x: future goods, y: present goods; the tax raises the cost of the future relative to the present. CR-4's exception applies: savers aiming at a fixed future sum must save more. So the a priori direction for total saving is `ambiguous`; the stated decrease holds only with the premise that the substitution response dominates for the group (`other`), or for saving in the taxed forms by savers with untaxed alternatives.

### TX-7 Tariff: domestic buyers pay more, protected sellers gain
- **If:** `tariff` on an imported good.
- **Then:** `price_paid` for the imported good and for domestic substitutes increase for `buyers.current`; `sellers.substitutes` (domestic producers of competing goods) see `net_price_received` and `quantity_supplied` increase. Domestic firms that use the good as an input face higher costs.
- **Assumes:** domestic substitutes exist; the tariff is not absorbed entirely by foreign sellers.
- **Tier** B. **Visibility**: gains to protected producers are visible; higher prices to buyers and input users are invisible. **Horizon** short to medium.
- **Builds on:** TX-2, RS-1.
- **Source:** EIOL 1946 ch. 11 "Who's 'Protected' by Tariffs?"; Bastiat, *Economic Sophisms*, First Series (1845), ch. VII (the candlemakers' petition).
- **Derivation:** CR-5c and CR-7 for the importing side; CR-9 for domestic sellers of the same good (their buyers' alternative has become dearer) and for users of the good as an input.

### TX-8 Import restrictions: export industries lose
- **If:** a `tariff` (TX-7) or an import `quota` (EN-6) reduces imports.
- **Then:** foreigners earn less of the domestic currency from selling to the country, and so have less to spend on its exports: `quantity_supplied` and `employment` in export industries decrease over time.
- **Assumes:** trade is not offset by capital flows or other adjustments in the period considered (`other`).
- **Mirror case:** a policy that raises exports (an export subsidy, SB-10) gives the country's residents more foreign means, so imports rise and `quantity_supplied` and `employment` (as a group with `hours_worked`) in import-competing industries decrease over time; exporters of other goods also lose foreign buyers' means to the subsidized exporters (CR-9, currency).
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-5, OC-4.
- **Source:** EIOL 1946 ch. 11 and ch. 12 "The Drive for Exports" ("Without imports we can have no exports, for foreigners will have no funds with which to buy our goods").
- **Derivation:** CR-8b (foreigners' receipts from selling to the country are the means with which they buy its exports or assets) and CR-9.

### TX-9 Revenue falls short of a static projection
- **If:** TX-2 applies (the taxed quantity falls), or TX-4 applies (avoidance shrinks the base).
- **Then:** `tax_revenue_vs_static_projection` decrease: revenue is less than the rate times the pre-tax base.
- **Unless:** the tax is ad valorem on a price that the tax itself pushes up (a tax on interest that raises the gross interest rate). Then the remaining base is worth more per unit and the sign is open: combine the chains (workflow step 7).
- **Tier** B (inherits the assumptions of TX-2 or TX-4). **Visibility** invisible until revenue is reported. **Horizon** short.
- **Builds on:** TX-2, TX-4.
- **Derivation:** Arithmetic with CR-4 (the base falls).

### TX-10 Base erosion and base shift across taxes
- **If:** a policy reduces `quantity_traded`, wages, employment or sales that bear other taxes in the jurisdiction (directly, or through RS-4 and RS-9), or a prohibition removes the base of an existing tax.
- **Then:** `tax_revenue` from those other taxes decreases. Where part of the spending moves to other goods taxed in the jurisdiction, revenue there increases, and the combined sign is `ambiguous` unless the substitutes are untaxed (informal or cross-border purchases), in which case it is a decrease.
- **Tier** B, inheriting the assumptions of the rules that shrink the base. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** TX-1, RS-1.
- **Derivation:** CR-8b and CR-9 (spending moved elsewhere carries other taxes' bases with it).

### TX-11 Tax on nominal returns
- **If:** a tax falls on nominal interest or gains, and prices are rising.
- **Then:** the share of the real return taken exceeds the statutory rate, and rises with the rate of inflation; the TX-6 responses are correspondingly stronger.
- **Tier** A for the arithmetic, B for the responses. **Visibility** invisible. **Horizon** medium to long.
- **Builds on:** TX-6.
- **Derivation:** Arithmetic (a tax on the nominal return takes a larger share of the real return) with TX-6.

---

## SB: Subsidies

### SB-1 Subsidy is funded by someone
- **If:** a subsidy is paid.
- **Then:** apply TX-1 and OC-1 to its funding source (taxes now, borrowing that implies taxes later, or monetary expansion). Name the payers. By CR-8b, the recipients' means increase by what the payers give up, before any response: record both sides.
- **Tier** A, given payment. **Visibility** invisible. **Horizon** short to long, depending on funding.
- **Builds on:** LW-1.
- **Derivation:** CR-8a and CR-8b.

### SB-2 Subsidized activity expands
- **If:** `per_unit_subsidy` or `purchase_rebate` on a good.
- **Then:** `price_paid` by buyers decrease and/or `net_price_received` by sellers increase; `quantity_traded` increase.
- **Assumes:** at least one side can expand its quantity.
- **Tier** B. **Visibility** visible. **Horizon** short.
- **Builds on:** LW-3, LW-4.
- **Derivation:** CR-5c (the subsidy is a wedge in the other direction) with CR-4 for each side.

### SB-3 Resources drawn from unsubsidized uses
- **If:** SB-2 applies.
- **Then:** resources move into the subsidized activity from other uses, where quantities fall: `quantity_substitute` decrease and output elsewhere decreases.
- **Assumes:** resources are scarce and in use elsewhere.
- **Unless:** the policy only moves an activity in time (a temporary program that brings work forward and leaves it undone later). Then the effect on other uses is a timing shift (RS-8, SB-6), signed per window, not a lasting reduction.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1, LW-4.
- **Derivation:** CR-7 and CR-8a.

### SB-4 Capitalization of lasting changes in returns
- **If:** a policy expected to last for some period raises or lowers the expected net return from an asset in fixed or slowly expandable supply (land, buildings, licenses, quota rights, shares in firms with specific capital): a subsidy or a restriction that raises returns (EN-2, EN-6), or a tax, cap or competing entry that lowers them.
- **Then:** `asset_value` changes in the same direction from the time the change becomes expected. Owners at that time capture the gain or bear the loss; later buyers pay the new price, so they neither gain nor lose from the policy as it stands. When an expected gain later erodes (the subsidy ends, exempt competitors enter, repeal becomes likely), the value falls on whoever holds the asset then, including recent buyers who paid the capitalized price.
- **Assumes:** fixed or slowly expandable supply of the resource; how long the change is expected to last (`expectations`). A change of limited duration is capitalized only for the yields it affects, so its effect on `asset_value` is smaller, but its sign is the same. Assets the policy itself creates (quota rights, medallions, transferable licenses) are covered too: their value is the expected yield of the privilege, captured by whoever receives them at creation.
- **Tier** B. **Visibility** invisible. **Horizon** short (announcement) to medium.
- **Builds on:** LW-4, LW-7.
- **Derivation:** CR-7c with CR-10c.

### SB-5 Seeking to qualify
- **If:** a subsidy is conditional on criteria.
- **Then:** RS-5 (reshaping to qualify) and RS-7 (lobbying to widen or keep the criteria) apply.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Derivation:** CR-4 (x: as before, y: qualify), as RS-5 and RS-7.

### SB-6 Temporary purchase subsidy: pull-forward and dip
- **If:** a purchase subsidy available only during a limited window.
- **Then:** purchases are moved into the window (RS-8): `quantity_traded` increase during it and decrease after it, compared with the counterfactual. If the subsidy requires destroying a used good (scrappage), the stock of used goods falls: `price_substitute` increase for buyers of used goods.
- **Assumes:** buyers can shift purchase timing; for scrappage, the scrapped goods would otherwise have stayed in use.
- **Price side:** in the dip after the window, sellers face fewer buyers than they would have, so `net_price_received` decreases for them in that window where their supply cannot adjust at once (CR-6).
- **Tier** B. **Visibility**: the surge is visible; the dip and the used-goods effect are invisible. **Horizon** short.
- **Builds on:** RS-8, OC-1.
- **Derivation:** CR-10a with CR-4 (x: buy at another time, y: buy in the window).

### SB-7 Earmarked revenue is fungible
- **If:** a tax's revenue is earmarked for a purpose that the budget already funds, or would have funded, from general revenue.
- **Then:** general funding for the purpose decreases in part, so spending on the purpose rises by less than the earmarked amount, and the rest of the revenue in effect funds other spending or lower borrowing.
- **Assumes:** the purpose already receives, or would have received, general funding; budget-makers can reduce it (`revenue_use`).
- **Unless:** the law also fixes the general funding level (a maintenance-of-effort clause) and it is enforced.
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1, AX-1 (budget-makers act on the whole budget).
- **Derivation:** CR-8d with CR-2 applied to budget-makers.

### SB-8 In-kind provision of a good the recipient would have bought anyway
- **If:** the state provides a good, free or below cost, to recipients some of whom would have bought it themselves (or had it paid for, for example by an insurer).
- **Then:** for those recipients (and their payers), the provision works like a cash transfer: `resources_available_other_uses` increase, and they spend the freed money elsewhere (OC-5 applies there). The quantity of the provided good rises only for recipients who would not have bought it. Providers of the good who would have been paid privately are paid by the state instead.
- Where the good is supplied with fixed capacity, those who would have bought anyway share it with new users: `wait_time` or crowding (`quality_per_unit`) worsens for them (CR-6, public supply).
- **Assumes:** the share of recipients who would have bought anyway (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-1, SB-1.
- **Derivation:** CR-8b (for those who would have bought anyway, the good provided frees the money they would have spent) and CR-4.

### SB-9 Public stocks and their disposal
- **If:** the state buys a surplus at a support price (PC-9 Unless clause).
- **Then:** `inventory_held` by the agency increases while the floor binds. When the stock is released, `quantity_traded` decreases for the private sellers it displaces (donation, school meals) or `price_paid` decreases in the market it is sold into (resale, including abroad, RS-13); if it is destroyed, OC-1 applies to the resources used to produce and store it.
- **Assumes:** the product's shelf life and the disposal routes allowed (`durability`, `other`).
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Builds on:** LW-1, RS-13.
- **Derivation:** CR-8, CR-10b (the stock accumulates) and CR-6 in the market the stock is released into.

### SB-10 Export subsidy
- **If:** an `export_subsidy` pays a fixed sum per unit of a good exported.
- **Then:** sellers move sales abroad until the domestic price rises toward the export price plus the subsidy (CR-7a): domestic buyers' `price_paid` increases and their `quantity_traded` decreases; producers' `net_price_received` and `quantity_supplied` increase; `asset_value` of the land or capital specific to the good increases (SB-4); foreign buyers gain (`price_paid` for `buyers.foreign` decreases); TX-8's mirror case applies; round trips to claim the subsidy appear (RS-4), unless the policy checks the return crossing (rules of origin, re-import bans); where it does, combine the round-trip chain with the check under CR-12b. The funding is analyzed under SB-1.
- **Assumes:** the domestic market is open to the world price (`mobility`); producers can expand (`alternative_uses`).
- **Tier** B. **Visibility**: the subsidy is visible; the higher domestic price is invisible. **Horizon** short to medium.
- **Builds on:** LW-4.
- **Derivation:** CR-7a (sales move to the higher-yielding market), CR-12e (the response cannot push the domestic price below its old level), CR-7c, CR-8b, CR-9 (currency).

---

## EN: Licensing, quotas and prohibition

### EN-1 Licensing requirement restricts supply
- **If:** `licensing_requirement` whose conditions (training hours, exams, fees, waiting periods) cost would-be sellers more than some of them would otherwise spend.
- **Then:** `entry_rate` and `number_of_sellers` decrease; `quantity_supplied` decrease and `price_paid` increase compared with no licensing.
- **Assumes:** `binding` (the requirement goes beyond what some current or prospective sellers already meet); `enforcement`.
- **Unless:** existing sellers are exempt (grandfathered), which delays the effect on supply (TS: horizon medium).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** LW-1, LW-4, LW-5.
- **Source:** P&M ch. 3 §3 "Product Control: Grant of Monopolistic Privilege".
- **Derivation:** CR-1 (the option of selling is removed for those without a license, and a cost is attached to obtaining one), CR-4 for would-be sellers, CR-6 in the market.

### EN-2 Licensed incumbents gain
- **If:** EN-1 applies.
- **Then:** `sellers.current` who hold licenses: `net_price_received` increase. If licenses are transferable, `asset_value` of a license increases (SB-4).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** EN-1, SB-4.
- **Derivation:** CR-6 and CR-7b: with entry restricted, the gain from the higher price settles on those who hold the scarce permission.

### EN-3 Excluded sellers and priced-out buyers
- **If:** EN-1 applies.
- **Then:** would-be sellers who do not qualify move to their next-best occupation (OC-4); by their own ranking they are worse off (CR-3a). Their money `earnings` decrease only with the premise that the next-best occupation pays less in money (`other`): an occupation chosen second may pay more and be valued less for other reasons. Buyers priced out of the licensed service substitute toward doing it themselves, unlicensed providers (RS-3) or going without (RS-1).
- **Assumes:** `substitutability` for buyers.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** OC-4, RS-1, RS-3, RS-10.
- **Derivation:** CR-3a and CR-4 for excluded sellers and priced-out buyers.

### EN-4 Quality received by buyers: ambiguous by default
- **If:** EN-1 applies and the requirement is related to the quality of the service.
- **Then:** two chains push `quality_per_unit` received by buyers in opposite directions: licensed providers meet a minimum standard (up), while buyers priced out move to self-provision or unlicensed providers (EN-3, down). The "down" chain needs its own premise: that what buyers move to is of lower quality than the paid provision it replaces (`other`). Without it, that chain gives no sign. The combined sign is `ambiguous` unless DM-2 applies.
- **Tier** B for each chain. **Visibility** the first chain is visible; the second is invisible. **Horizon** medium.
- **Note:** the canonical example for workflow step 7.
- **Derivation:** CR-12 (two chains with opposite signs).

### EN-5 Incumbents push for tighter requirements
- **If:** EN-2 applies (incumbents gain from restriction).
- **Then:** RS-7: `lobbying_effort` by incumbents for stricter or broader requirements.
- **Tier** B. **Visibility** invisible. **Horizon** medium to long.
- **Derivation:** CR-4 applied to political action, as RS-7.

### EN-6 Quota
- **If:** `quota` limiting the quantity produced, sold or imported, below the quantity that would otherwise be traded.
- **Then:** `quantity_traded` decrease; `price_paid` increase; holders of quota rights gain, and their `asset_value` increases where rights are tradable (SB-4). Domestic sellers of the same good (for an import quota): `net_price_received` and `quantity_supplied` increase, as under TX-7. Buyers lose (OC-4). For an import quota, TX-8 applies to export industries; DM-4 governs how the gap between the domestic and world price is split.
- **Assumes:** `binding`, `enforcement`.
- **Unless:** the capped good's price is set in a wider market (fish sold into a regional market, a traded commodity). Then the lease price of the right (`right_lease_price`) rations the capped quantity (CR-6), not `price_paid`. `price_paid` still moves up in the wider market, by as much as the capped quantity matters there: record it as `increase` with a premise that the effect is not negligible, or note it as negligible. Where part of the good is sold only at home, that part's price rises as in the main case.
- **Tier** B. **Visibility** invisible. **Horizon** short.
- **Builds on:** LW-3, LW-5.
- **Derivation:** CR-6 (quantity held below the clearing level), CR-7b (the gain settles on the holders of quota rights, the scarce side) and CR-9 (domestic sellers of the same good).

### EN-7 Prohibition of a good moves trade underground
- **If:** `prohibition` of a good that some buyers continue to value highly.
- **Then:** `quantity_traded` legally falls to near zero; `informal_activity` increase; `price_paid` increase (sellers require compensation for the risk of punishment). RS-10 applies to the informal trade: higher search costs, less predictable quality, disputes settled outside the courts.
- **Assumes:** demand persists for some buyers; imperfect `enforcement`.
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** RS-3, RS-10, LW-3.
- **Derivation:** CR-1 (legal trade removed), CR-6 and CR-4 (trade outside the rule where the expected gain exceeds the expected penalty), CR-7 (the price includes compensation for risk).

### EN-8 Prohibition favors concentrated forms
- **If:** EN-7 applies, and penalties or detection risk depend on bulk or volume rather than on potency.
- **Then:** sellers shift toward more concentrated, potent forms of the good, which are cheaper to hide per unit of effect: `share_concentrated_forms` increase.
- **Assumes:** penalties scale with volume (`enforcement`).
- **Tier** B. **Visibility** invisible. **Horizon** medium.
- **Source:** the "iron law of prohibition" (Richard Cowan, "How the Narcs Created Crack", *National Review*, 1986; Mark Thornton, *The Economics of Prohibition*, 1991). Not a classical praxeological text; flagged for expert decision (Q7).
- **Derivation:** CR-7 with CR-4: where penalties scale with volume, sellers minimize volume per unit of effect, so the concentrated forms yield more net of expected penalty.

### EN-9 Supervised-practice requirement
- **If:** a license requires a period of practice supervised by existing license holders.
- **Then:** incumbents' willingness to supervise becomes a bottleneck on entry: `entry_rate` is limited by the number of supervised places, and where places are scarce relative to candidates, `wage_rate` of those in supervised practice decreases, as incumbents capture part of the value of the license through their trainees' pay.
- **Assumes:** supervision is costly or limited per supervisor (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** short to medium.
- **Builds on:** EN-1, LW-6.
- **Derivation:** CR-1 (entry requires a supervised place), then CR-6: supervised places are scarce and the gap is closed through trainees' pay.

### EN-10 Penalty records
- **If:** a prohibition (EN-7) or licensing rule is enforced by criminal convictions that are recorded and checked by employers.
- **Then:** for those convicted, `employment` and `earnings` decrease over the long run, compared with the counterfactual.
- **Assumes:** record-keeping and checking practice (`other`).
- **Tier** B. **Visibility** invisible. **Horizon** long.
- **Builds on:** LW-1.
- **Derivation:** CR-11c (a record conveys information employers act on) with CR-4 for employers.

### EN-11 A license as a signal
- **If:** a license requirement tests something buyers care about but cannot easily judge for themselves (competence, safety, honesty), and the license is visible to buyers.
- **Then:** for licensed sellers, `quality_information` increases for their buyers. Where the requirement tests something buyers do not care about, the license conveys nothing about the quality they want, and this chain gives no sign.
- **Assumes:** the requirement's content bears on the quality buyers value (`other`); buyers can see who holds a license.
- **Tier** B. **Visibility** visible. **Horizon** short to medium.
- **Builds on:** AX-1.
- **Derivation:** CR-11c (a policy changes actions by conveying information) with CR-2 for buyers.

---

## DM: Dominance rules

Dominance rules decide the combined sign when chains conflict (workflow step 7). Each is itself an assumption and needs an estimate.

### DM-1 Incidence follows the alternatives
- **If:** TX-2 (a tax) or SB-2 (a subsidy) applies, and one side of the market has clearly fewer or worse alternatives than the other (buyers with no substitutes; sellers with highly specific, immobile resources).
- **Then:** that side bears more of a tax, or receives more of a subsidy, than the other side does (CR-7b, with the premise that the difference in alternatives is clear). This compares the two sides' shares; it says nothing about how large either is. For a tax: if buyers have fewer alternatives, the rise in `price_paid` exceeds the fall in `net_price_received`; if sellers do, the reverse. For a subsidy, the same with the signs reversed. Without a clear difference in alternatives, the split is not signed: each side's price moves in the direction TX-2 or SB-2 gives, and `tax_share_borne` or `subsidy_share_received` is `ambiguous`. Record the split with `tax_share_borne` or `subsidy_share_received`.
- **Assumes:** the comparison of alternatives (`substitutability`, `mobility`), with evidence.
- **Tier** B. **Horizon**: over time, the side that owns redeployable capital gains alternatives as it redeploys (TS-1), so the burden shifts away from that side. In product markets the sellers own the capital, so incidence shifts toward buyers; in factor markets such as labor the buyers (employers) own it, so a payroll tax's incidence shifts toward workers.
- **Source and dispute:** the rule as stated is the standard treatment of incidence, not Rothbard's. Rothbard's "first law of incidence" (P&M ch. 4 §3A) holds that no tax can be shifted forward: a general sales tax is in effect a tax on the incomes of original factors, and where a price later rises, that comes about through reduced supply, which he classes as an effect of the tax rather than shifting. The two accounts agree that the burden falls first on those who cannot escape it, and that prices rise only as supply contracts; they differ in what they call shifting, and in Rothbard's case for general taxes. Whether to encode Rothbard's account as an option is Q3 in `06_gaps.md`.
- **Derivation:** CR-7b: the side whose means can move away bears less; the burden or benefit settles on the side with fewer alternatives.

### DM-2 Quality under licensing
- **No default rule.** Both chains of EN-4 need their premises: the "up" chain that the requirement bears on the quality buyers care about, and the "down" chain that the alternatives buyers move to are of lower quality. EN-4 stays ambiguous unless the case supplies evidence that one chain dominates: for example, the requirement is unrelated to the quality buyers care about (then only the "down" chain is active), or close unlicensed substitutes are unavailable (then the "down" chain is weak). Record such evidence as an assumption.
- **Derivation:** CR-12 (no dominance premise by default).

### DM-3 One-time cost against later gains (ambiguous by design)
- **No default rule.** When one chain imposes a one-time cost (training, conversion, relocation) and another produces a later stream of gains (a higher price, a lower cost), the combined effect on the actor class's earnings or welfare is `ambiguous`. Comparing them needs magnitudes and a discount rate, which the method does not supply. Report both chains, and state that the actors who chose to bear the cost expected the gains to be worth it (LW-5), while those who did not, did not.
- **Derivation:** CR-12 (the method has no magnitudes or discount rates with which to net the two).

### DM-4 Quota rent follows the scarce side
- **If:** EN-6 (an import quota) raises the domestic price above the world price.
- **Then:** if foreign supply comes from many competing sellers, the holders of quota rights capture most of the gap; if it comes from a few sellers who can coordinate, or if exporting countries administer their own shares of the quota, foreign sellers capture part of it.
- **Assumes:** the structure of foreign supply and of quota administration (`other`).
- **Tier** B.
- **Derivation:** CR-7b: the gap between domestic and world price settles on whichever side is scarce and cannot be competed away.

### DM-5 Netting a timing shift
- **If:** SB-6 (or RS-8) produces a surge in one period and a dip in another, and the question is the total over a horizon that includes both.
- **Then:** the total rises if some purchases in the surge are additional, provided the dip consists only of purchases moved into the surge. If the policy is expected to recur, buyers wait for it, and the dip can include purchases that are merely delayed; then the total is `ambiguous`.
- **Assumes:** what the dip contains (`expectations`).
- **Tier** B.
- **Derivation:** CR-12 with CR-10a: the total over the horizon is the sum of the surge and the dip, whose net sign depends on what the dip contains.

