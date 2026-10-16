# 4a. Core rules (the calculus)

Citations use the short forms in `07_sources.md`, which records how each was checked.

The rule catalog has two layers.

- **Core rules** (this file, `CR-1` to `CR-12`) are universal. They are stated over any actor, any option, any means and any time, with no reference to a particular instrument, good or market. Each is derived from the action axiom and the laws in `01_foundations.md`, and each states exactly which part of its conclusion is a priori and which part needs an empirical premise.
- **Patterns** (`04_rules.md`) are derived results for recurring situations: a binding price ceiling, a per-unit tax, a license requirement. Each pattern carries its derivation from the core rules. A pattern is a shortcut, never an independent source of truth.

The relation is that of the limit definition of the derivative to the power rule. Any consequence that a pattern yields can also be derived step by step from the core rules; the pattern saves the work and must give the same answer. When no pattern fits a situation, the analyst derives from the core rules directly and cites them (workflow, "When no pattern fits"). A new pattern enters the catalog only with a written derivation.

## What makes a rule universal

A rule is admitted to this file only if it meets all four tests. Patterns must meet the second and fourth.

1. **Generality.** It is stated over arbitrary actors, options, means and times. It names no instrument (tax, ceiling, license), good or market.
2. **Grounding.** It follows from AX-1 and the laws in `01_foundations.md` by a derivation written out below. Whatever empirical content it needs is isolated in named premises, never hidden in its wording.
3. **Symmetry.** It applies in the same way to imposing and to removing a policy, to raising and to lowering a cost, to buyers and to sellers, and to private and to political actors. A rule that works only in one direction is a pattern, not a core rule.
4. **Answerability.** It says what would have to be true for its conclusion to fail, so that a miss in evaluation can be traced to a failed premise rather than explained away.

## The objects the rules work on

- An **actor** is an individual. An actor class is a set of actors in the same situation; a class "responds" when some of its members do.
- An actor's **situation** is the set of options they believe are open to them, what they expect each option to bring, and the means they command.
- An actor's **ranking** of ends is their own, ordinal, and revealed only in choice. The rules never assume a particular ranking. They reason only from the fact that there is one.
- A **policy** is a change in the rules that others will enforce. Its effect on any actor is described entirely by CR-1.

---

### CR-1 Representation: what a policy can do to an actor

**Statement.** A policy affects an actor's action only by doing one or more of four things to their situation:
1. removing an option (a prohibition, a license requirement for those who lack the license, a price above a ceiling);
2. adding an option (a permission, a free service, an exemption);
3. changing what an option brings: attaching a payment, penalty, delay, paperwork or risk to it, or removing one;
4. transferring means to or from the actor (a tax, a grant, a confiscation).

A policy does not change anyone's ranking of ends, except through what it tells them about the world (CR-11).

**Derivation.** Action is the choice of means for ends within a situation (AX-1). The rule-maker cannot choose for the actor; it can only alter the situation within which the actor chooses: the options, their consequences, and the means available.

**Use.** Workflow steps 1 and 2: for each component and each actor class, write down which of the four operations it performs. Every later step works on that list.

**Premises.** Whether a stated rule is actually enforced is empirical (`enforcement`). An unenforced prohibition does not remove an option; it attaches a risk to it (operation 3).

**Recording.** A provision often does more than one thing: a free tradable right adds an option and transfers means; a void-contract rule removes, for both parties, the option of agreeing to the term, and may add an option for one of them (the worker who may now join a rival); a prohibition removes an option where enforced and attaches a risk where not. Record every operation that applies, for each actor class, and split an actor class where the operation differs within it. Which operation a provision performs depends on what the law would be without it, so state that counterfactual law. Where an operation holds only under one reading of an unclear provision, record the operation per reading (U1-a, U1-b), as consequences are (`02_ontology.md`, 2.5).

**Source.** HA ch. I §1; HA ch. XXVII; P&M ch. 2 §1.

**0.7 clarifications.**
- A charge paid only when an option is taken (a deposit on a purchase, a fee on a transaction) is operation 3: it changes what the option brings. Operation 4 is a transfer that no choice avoids (a lump-sum tax, a grant).
- *0.8.* A refund attached to a thing rather than to a person (a deposit refunded to whoever returns the container) is operation 3 on the option of returning it, for anyone who holds the thing; that is what makes collectors and charities recipients. A charge per unit paid by a seller to a fund (distributors' deposits) is also operation 3, on the option of selling.
- Operations may be dated: a provision that removes an option from a future date, or tightens each year, performs its operation on that date. Record the date. Before it, the operation acts only through expectations (CR-10a): an option nobody currently chooses can be removed with no present effect on choices, while assets whose yields depend on the future option change value at once (CR-7c).
- Where every member of a class faces the same operation but responds differently (some return containers and some do not), split the class by response, not by operation.
- Information that changes how much an actor values an option (a calorie count) is not one of the four operations; it works through CR-11c.

**0.9 clarifications.**
- A single provision can perform different operations for one actor on either side of a threshold: a charge per worker capped per firm is operation 3 below the cap and operation 4 above it. Record the operation per range.

### CR-2 Choice

**Statement.** Each actor chooses, from the options they believe open, the one they expect to serve their most highly ranked end. What an actor chooses reveals that they ranked it above the alternatives open at the time (demonstrated preference).

**Derivation.** AX-1, with LW-2 (ordinal valuation).

**Premises.** None for the statement. What actors believe about their options is a fact about them, and may be wrong (CR-11).

**Source.** HA ch. I §1 and ch. VII §1 ("action sorts and grades"); Rothbard, "Toward a Reconstruction of Utility and Welfare Economics" (1956), on demonstrated preference.

**0.7 clarification: absence of an exchange.** That a term or an exchange was absent before a policy demonstrates only that, in the situation as it was, no pair of parties found it worth agreeing on (CR-5). Whether that reflects the parties' own rankings or an obstacle to agreeing (one side knowing more than the other, costs of writing the term) is an empirical question and needs a premise; the rules do not presume either.

### CR-3 Cost and loss

**Statement.** The cost of an action is the most highly ranked alternative given up by taking it. Hence:
- (a) removing an actor's chosen option, or attaching a burden to it, makes the actor worse off by their own ranking, unless their next-best was ranked equal;
- (b) only adding options, or removing burdens, cannot make an actor worse off by their own ranking at the time of choice;
- (c) means used for one end are not available for any other (LW-1).

A loss by the actor's own ranking (a) is not the same as a fall in their spending on other things. An actor who must pay more for something may respond by buying less of it, and so spend more, not less, elsewhere. `resources_available_other_uses` falls for an actor class only if its members keep spending on the burdened option, or are made to pay a sum they cannot avoid. A charge that is later refunded burdens only those who do not claim the refund, and those who claim it bear only the cost of claiming and the time the money is held. An actor who also sold part of what the policy stops them producing loses those receipts too (CR-5a); combine the lost receipts with the saved outlays under CR-12b.

**Derivation.** CR-2 and LW-1. Under (a) the actor must fall back to an alternative they ranked lower. Under (b) the previously chosen option is still open.

**Premises.** None. (Statement (b) is about the actor's ranking at the time of choice; it says nothing about how things turn out.)

**Source.** HA ch. IV §4 (cost as the value of the satisfaction forgone); P&M ch. 2 §2.

**0.9 clarifications.**
- The note on refunded charges covers partial refunds and refunds computed on a standard rather than on what was used (yield tables, deemed amounts). Those who claim on the standard and use less than it receive more than they paid; those who use more receive less. Split the class by its position against the standard.

### CR-4 Response at the margin

**Statement.** Suppose a change makes option x worse relative to option y for an actor (x costs more, brings less, or y improves). Then:
- (a) no actor who was choosing y switches to x on account of the change;
- (b) among actors who were choosing x, those for whom x was ranked only narrowly above y (or above some other alternative) switch away from it; the rest keep choosing x and bear the change (CR-3a);
- (c) the same holds for each unit when an actor chooses how many units of x to take: the last unit, which was valued least (LW-2), is the first given up.

The mirror case (x made better) reverses every direction.

**What is a priori and what is not.** Statement (a) and the direction in (b) and (c) are a priori. That some actors actually are at the margin, so that someone does switch, is empirical: it is the premise behind `substitutability`, `alternative_uses` and `mobility`. **Exception:** when the change also alters the actor's total means (a price rise on something they spend much of their means on; a lower return on something they save toward a fixed sum), the change in means can shift their ranking among other options in the opposite direction. Where such an effect matters, the direction for that actor class is `ambiguous` unless a premise says which effect dominates (this is the exception recorded under LW-3 and TX-6). The exception can bear on the burdened option itself (a heavy buyer of a good whose price rises) and on what an actor offers as well as what they buy (hours of work offered when the wage falls).

**A change in means alone.** When a policy changes an actor's means without changing the relative cost of any option (a lump-sum tax or grant), CR-3c and CR-8 establish that spending on some uses falls (or rises) by the amount taken (or given). Which uses, and by how much each, CR-4 does not say: it depends on the actor's ranking, which the rules never assume. A claim about a named use ("sales at local shops fall") therefore needs a premise. Whether anything more can be said a priori is `06_gaps.md`, Q19.

**Units and lumpy costs.** In (c), the unit is the unit of the end served (a dose, not a gram; a trip, not a mile), since that is what the actor ranks. Where a change attaches a large one-time cost to an option (training hours, a license fee), "narrowly ranked" in (b) covers every actor whose ranking of x over y is reversed by that cost, which may be many.

**Derivation.** CR-2 and CR-3. Under (a), y was ranked above x before, and x is now worse, so y still ranks above it. Under (b) and (c), LW-2.

**Use.** All the generic responses are this one rule applied to different pairs of options: substitution (x: the good, y: a substitute), evasion (x: comply, y: violate), relocation (x: here, y: there), reclassification (x: the covered form, y: the uncovered form), exit (x: this use, y: another use), lobbying (x: accept, y: lobby), timing (x: now, y: later), entry (x: stay out, y: enter).

**Source.** HA ch. VII §1; MES ch. 1 §5, ch. 2 §5 and ch. 4.

**0.7 clarifications.**
- *Means over time.* A transfer financed by borrowing that the recipient expects to repay through later taxes is, for that recipient, partly a loan at the government's rate: it changes the cost of present against future goods for those who could not borrow on such terms, and so falls under CR-4 proper, not only under "a change in means alone".
- *Saving is a use.* Saving and repaying debt are among the uses on which spending rises or falls when means change. By LW-2, the use added is the next in the actor's own ranking and the use given up is the last ranked; this is a statement about rank and names no good. With lumpy goods it may be a new kind of item rather than more of an old one.
- *Fixed costs per item offered.* A cost incurred once for each item a seller offers (testing and labeling a menu item, certifying a model) bears on which items are offered, not on the price of each unit sold: it is a cost of the option of offering the item (x: offer it, y: drop it). *0.8:* the same holds for a cost fixed per outlet or per firm (a menu board, a registration): it bears on whether the outlet or firm operates, and on the size at which it pays to do so, not on the price of each unit. The unit price is signed only with a premise about entry and exit.

**0.9 clarifications.**
- *Lobbying in repeals.* Applying the rule to political action (x: accept, y: lobby), remember that in a repeal the counterfactual is the old rule still in force, which may itself have been contested. Lobbying is signed against that path, not against no lobbying; where the old rule was contested, the sign needs a premise.

### CR-5 Exchange

**Statement.** A voluntary exchange takes place only if each party ranks what they receive above what they give. Hence:
- (a) a policy that prevents an exchange that would otherwise have taken place deprives both parties of a gain each expected;
- (b) a policy that compels a transfer that would not have taken place voluntarily makes at least one party worse off by their own ranking;
- (c) the terms of any exchange that does take place lie within the range both parties accept, and any change in what one party must give or may receive moves that range. The terms include everything either party gives or receives, money or not: hours that count toward a qualification, training, flexibility, security of tenure.

**Derivation.** CR-2 applied to both parties; CR-3.

**Premises.** None for (a) to (c). Whether a given exchange would have taken place without the policy is the empirical question.

**Source.** MES ch. 2 §4 ("a double inequality of values"); HA ch. XVI §1; P&M ch. 2 §2.

**0.7 clarifications.**
- A gift is a transfer the giver ranks above keeping the thing given; a policy that removes the means of a gift (a ban on the production whose output was given away) removes a gain for the giver and a receipt for the recipient (CR-8b).
- (a) applies to an exchange that would otherwise have taken place. Where a policy only makes another offer more attractive, so that a buyer takes the better offer instead, the party who loses the sale loses; the buyer does not.

### CR-6 Price formation and displaced pressure

**Statement.** At any price at which the quantity buyers wish to buy differs from the quantity sellers wish to sell (whatever the reason the price is where it is), some unsatisfied party can gain by offering better terms, and some party on the other side can gain by accepting them (CR-5). Prices therefore tend toward the level at which planned purchases and sales are compatible.

If a rule prevents the price from moving, the gain from closing the gap does not disappear. The rule may be the policy, a rule already in force (a regulated fare), or a buyer of last resort that holds the price. The same holds when a rule fixes the quantity (a quota, a cap on the number of sellers) and leaves the price free: the price then rises to ration the fixed quantity, and the gap between that price and what sellers would accept is the pressure that seeks other margins (entry outside the rule, the value of the permission). Unsatisfied parties pursue it along every margin that is still open:
- the terms that are not regulated (quality, service, conditions, timing);
- the criteria by which the scarce side chooses among the other side (queues, connections, preference for some buyers or sellers);
- exchanges outside the rule, where the expected gain exceeds the expected penalty (CR-4 with x: comply, y: violate).

The full price, meaning the money price plus everything else given up, moves toward the clearing level as far as the open margins allow. CR-6 establishes that at least one open margin is used; which ones, and whether each is used, needs a premise per margin. Without such premises, record the margins as a group with sign `at_least_one_increase` (02_ontology.md, 2.5).

**What is a priori and what is not.** That the pressure exists and moves to open margins is a priori. Which margins are open, and how wide, is a fact about the case: which terms are regulated, and how well the rule is enforced (`enforcement`, `binding`).

**Symmetry.** The same rule covers a price held too low (pressure from buyers) and too high (pressure from sellers), in any market: goods, labor, loans, housing, permits.

**Derivation.** CR-2, CR-4, CR-5.

**Source.** HA ch. XVI §1 and ch. XXX §2; MES ch. 2 §5; P&M ch. 3 §1; EIOL 1946 ch. 15 and 17.

**0.7 clarifications.**
- *Public supply.* Where the supplier is the rule-maker itself and supplies a fixed quantity at a set price (zero, for a free service), the unsatisfied buyers' pressure goes to the margins open to buyers sharing that quantity: waiting, crowding, time of travel. The supplier does not respond as a seller would, unless the budget rule changes. *0.8:* the mirror case is a public buyer at a fixed price with no fixed quantity (a fund paying a set fee per container redeemed): the quantity supplied to it is set by sellers' response to the fee (CR-4), and any pressure goes to the margins open to sellers (who gets the business, waiting to be paid). A private supplier that chooses not to charge (an animal rescue) is not bound by a rule; its rationing is its own choice (CR-2), and the margins (waiting, criteria) are signed as a group as under the main clause.
- *A fixed quantity of a good priced in a wider market.* Where a cap fixes the quantity of a good whose price is set in a wider market (a catch quota, a local quota on a traded good), the price of the good does not ration the capped quantity. The price (or lease price) of the right to produce or sell does. *0.8:* the wider-market price still moves in the CR-6 direction, by as much as the capped quantity matters to that market; record its sign, with a premise if the effect may be negligible. Where only part of the capped good is sold in the wider market, the part sold at home is rationed by its own price as under the main clause.
- *Margins that move in opposite directions.* Where the open margins differ in direction (quality falls while waiting rises; pay falls while a substitute restraint becomes more common), record them as a group with each member's direction stated and the sign `at_least_one_as_stated` (02_ontology.md, 2.5).
- *Illegal margins.* The price of a legal right can satisfy the "at least one margin" conclusion on its own. Illegal margins (misreporting, discarding) each need their own premise.
- *Existing contracts.* Terms fixed by existing contracts count as regulated while those contracts last. *0.8:* for at-will employment and other contracts without a fixed term, terms are regulated only for as long as changing them costs more than it gains (custom, pay scales, the cost of renegotiating): treat their stickiness as a premise with a probability, not as a rule.
- *0.8. A free price's rise is enough.* Where a margin is a free price (a rater's fee, a lease price), its rise satisfies the "at least one margin" conclusion by itself; waiting or other non-price margins then need their own premise.

**0.9 clarifications.**
- *Splitting a shift.* A shift in demand (or supply) gives the direction of the pressure; how it divides between price and quantity needs a premise about the other side's response (supply that can or cannot expand in the period). Sign the price and the quantity separately only with that premise; otherwise record them as a group.
- *A public seller with an open quantity.* Where the state sells at a set price and supplies whatever is demanded (a utility, a network with spare capacity), there is no excess demand to ration: the main clause applies in the markets it competes in. Buyers move to it by CR-4 and rival sellers face lower demand (CR-9), with the price and quantity split as above. Where capacity can be added from the fees it earns, but only after a lag, the public-supply clause applies until the capacity arrives.
- *A capped price with a free fee.* Where a capped price can be paid together with a fee that is not capped (a platform's charge on a capped resale), the buyer's price is the total paid. Record the capped part and the fee as two items of `price_paid` (CR-12, two items) where the policy moves them differently.

### CR-7 Equalization across uses

**Statement.** Wherever a means (labor, capital, money, land, a purchase, an activity, a moment in time) can be moved between uses that serve the same end, its owners move it from the use that yields less to the use that yields more, until the difference in yield at the margin is no greater than the cost of moving. Hence:
- (a) after any change in yields, yields on the means that can move are brought back into line, net of moving costs;
- (b) the lasting gain or loss from the change settles on the means that cannot move: specific, immobile or fixed resources, and actors without alternatives (this decides who bears a tax and who keeps a subsidy or a privilege). This is a matter of degree: where both sides have some alternatives, each bears part, and the side whose alternatives are clearly worse bears more than the other. Ranking the shares needs a premise comparing the alternatives; with three or more parties (a distributor, a retailer and a buyer), rank each pair. Without such a premise, only the direction of each side's price is signed;
- (c) the price of a durable asset adjusts until a buyer expects to earn on it what they could earn elsewhere, so a change in its expected yield is borne or captured by whoever owns it when the change becomes expected, not by later buyers. A change of limited duration is capitalized for the yields it affects. An asset the policy itself creates (a quota right, a medallion, a transferable license) is valued the same way, and its value is captured by whoever receives it at creation. "Becomes expected" is a matter of probability: as a measure becomes more likely to pass, or more likely to be renewed, the asset's price moves part of the way, so the loss or gain is shared among those who hold the asset as the probability rises. CR-7c states what happens in the market for the asset; CR-10c states why its value reflects expected yields. Cite both.

**What is a priori and what is not.** The direction of every movement is a priori (CR-4 for each owner). How mobile each means is, and how fast it moves, is empirical (`mobility`, `alternative_uses`, `durability`).

**Symmetry.** It applies to yields raised and lowered, to buyers and sellers, to the present and to future uses.

**Derivation.** CR-2 and CR-4 applied to every owner of a movable means; CR-10 for (c).

**Source.** HA ch. XIV §5 (the evenly rotating economy) and ch. XV §4; MES ch. 6 §1 and ch. 8 §1 (equalization of returns); MES ch. 7 §5 "Capitalization and Rent" (clause c); EIOL 1946 ch. 15. On incidence (clause b), see the dispute recorded under DM-1: the formulation here is the standard one, not Rothbard's.

**0.7 clarifications.**
- *A policy that makes a means mobile.* Where a policy removes a restraint on moving a means between uses (a ban on non-compete clauses, an end to a residence requirement), the gain from its mobility goes to the owner of the means (the worker), and the loss falls on those who held the restraint. This is (b) applied to the change in mobility itself.
- *Gross and net burdens.* Where a mandated term is worth something to the side that receives it, the burden "borne" by the paying side is the cost net of anything it recovers through the other terms. Say whether a share is gross or net.
- *A tax whose revenue buys something the payers value.* Where the payers of a tax receive part of what it funds (employers whose staff ride the transit their payroll tax pays for), their net burden is smaller than the tax; sign each side separately and combine only with a premise (CR-12e).
- *Claims before creation.* Where the claim to a right the policy will create travels with a tradable asset before the right exists (quota shares allocated to vessels), the claim's value is capitalized into that asset when the allocation rule becomes expected, and captured by its holder then. *0.8:* where the qualifying history was fixed before the measure became expected, the value is a windfall to its holders. Where actors compete to qualify for the claim (a race to build catch history), part of the value is used up in the competition (CR-8c).

**0.9 clarifications.**
- *Assets without a market price.* CR-7c applies to durable assets whether or not they can be sold. Inventories that take time to finish (cattle on feed, stock in process) are durable assets in this sense. For an asset that cannot be sold (a license, training), the change in its expected yield is a loss or gain by the holder's own ranking (CR-3a); a change in money earnings needs a premise about the holder's next-best use.
- *A contract term that removes an option.* Where an agreement binds an asset's owner (a team's commitment not to relocate), the asset's value falls by the value of the option given up, against whatever the agreement pays for it. Sign the net only with a dominance premise.
- *Persistence of an asset's value.* After a repeal, an asset price persists only as far as the stock its value depends on persists (homes built under the rule, a scarce license count). Give its persistence from that stock, not from who held the asset when the change was capitalized.

### CR-8 Conservation of means

**Statement.** A policy does not create means; it redirects or uses them up. Hence:
- (a) every resource the policy directs to one use is withdrawn from another use its owner would have chosen (the seen and the unseen);
- (b) every payment is a receipt to someone, and every transfer adds to the recipient exactly what it takes from the payer;
- (c) resources spent on complying with, administering, enforcing or evading a policy, or on queuing, searching or lobbying because of it, are used up and serve no other end of those who spend them;
- (d) money is fungible: a sum earmarked for one purpose frees other money for other purposes, unless the other spending is also fixed;
- (e) a confiscation (seized stock, a forfeited asset) is a transfer under (b), recorded on both sides: the holder's means fall, and the state's rise by what it can realize from what it seized. Where the seized goods are destroyed, (a) applies instead: the means are used up.

**Derivation.** LW-1 and CR-3c.

**Premises.** None for (a) to (d). Which use the means would otherwise have gone to is the empirical question (`revenue_use`).

**Symmetry.** Applies to taxes and subsidies, imposition and repeal, public and private budgets. A rule that counts a gain to the recipient of a transfer, or to the seller of an asset that has risen in value, must count the matching loss to the payer or buyer.

**Source.** Bastiat 1850, §1; EIOL 1946 ch. 2 and 4; P&M ch. 5.

**0.7 clarifications.**
- *Residual claimants.* Where a fund pays out of what it collects (a deposit fund that refunds deposits and keeps the rest), the residual claimant's receipt can be negative; record its sign per reading or with a premise, not as a gain by default.
- *Payers from the general budget.* Where a cost is funded from the general budget, CR-8b establishes that someone pays but not who: record the payers as a group of actor classes (taxpayers, recipients of other spending, future taxpayers through borrowing) with sign `at_least_one_decrease`.
- *Borrowing.* Borrowing now implies taxes later only if the debt is expected to be repaid; that is a premise. The lenders' side of a public borrowing is recorded too: the means they lend are not available to other borrowers (OC-8).
- *Voiding a contract right.* A rule that voids a right one party held under an existing contract (an enforceable non-compete) is a transfer under (b): the holder loses the value of the right and the other party gains it. That includes deferred pay that a voided clause would have let the holder withhold.
- *0.8. Contingent payers and capped budgets.* Where a budget pays only if something happens (a general fund that covers a shortfall in a dedicated tax), record its payers per reading or with a premise on the contingency. Where a law promises more than its budget can pay, record who bears the shortfall per reading (claimants paid less or later, or a group of other payers if it is made up).
- *0.8. Value created by ending a race.* Where a policy ends a competition that used up means (a race to fish, to queue, to qualify), part of the value of the rights it creates is means no longer used up (a), which no one pays. Only the rest is a transfer under (b), with a payer to name.
- *Non-rival means.* Knowledge, techniques and know-how can be used by several actors at once without being used up. (a) applies to the time and materials used with them, not to the knowledge itself. Whether a policy that spreads knowledge raises total output therefore cannot be signed by conservation of means; it needs a premise. Whether this is a gap in the calculus is `06_gaps.md`, Q21.

**0.9 clarifications.**
- *The borrowing baseline.* Public borrowing is compared with the borrowing that would have taken place without the policy, including private borrowing for the same purpose (a team that would have renovated with its own loan). Where the counterfactual also borrows, the effect on other borrowers' interest rate is `ambiguous` without a premise on the difference. Borrowing repaid from the project's own fees (revenue bonds) implies later taxes only for any shortfall. Interest exempt from tax reduces tax receipts, and those who make up the receipts are payers too. The lenders' side gives no sign by itself: they would have lent elsewhere.
- *A reading that permits.* Where one reading of an unclear provision allows a source of funds without requiring it, record the payers under that reading as a group that includes the permitted source.
- *Mutual rights.* Where every member of a class both holds a right and is bound by it (owners under a covenant that each can enforce), voiding it is not a transfer between classes: each member loses the right to enforce and gains freedom from enforcement. Sign the net per member only with a premise about which they value more.

### CR-9 Propagation

**Statement.** When an actor changes what they do, the situation of everyone who would have dealt with them changes too: those who would have sold to them or bought from them, those who compete with them for the same means or customers, and those linked to them by any other relation recorded under `02_ontology.md`, 2.8: goods used together, goods bought together on one trip, goods put to a secondary use, contracts (a lease, an insurance policy, an employment contract), and the currency link (payments for imports are the means with which foreigners buy exports or assets). Apply CR-1 to CR-8 to each of these actors in turn, following those relations.

The value to anyone of a means depends on the ends it serves and on what it is used with (LW-10). So when the use of a good changes, the demand for the means that produce it and for the goods used with it changes in the same direction, and the demand for goods that compete with it in the opposite direction.

**Derivation.** CR-1 (one actor's choice changes the options open to those who deal with them), CR-5, LW-10.

**Limits.** Propagation follows exchange relations only, and stops at the depth limit in workflow step 6. Every link must name the relation it uses.

**Source.** Menger, *Principles of Economics*, ch. I and III; HA ch. XVI §3; MES ch. 7 §1.

**0.7 clarifications.**
- *The currency link runs both ways.* More imports provide foreigners with means to buy more exports or assets; more exports provide the country's residents with means to buy more imports. Exporters of different goods also compete for the same foreign buyers' means. Follow the link in whichever direction the policy moves it.
- *Shared facilities and proximity.* An actor's use of a facility others share (a road, a vehicle, a common fishing ground) changes what is available to them; an actor's activity on their own property can change their neighbors' situation (noise, smell, gifts of produce). These are relations, not exchanges, and are recorded as `shared_facility` and `proximity` (02_ontology.md, 2.8). Propagation along them follows the same rules. Whether such effects belong to praxeological analysis at all, given that the affected party does not choose them, is `06_gaps.md`, Q20; until the experts decide, chains through them are reported at Tier C.

### CR-10 Time

**Statement.** Action takes place in time, on expectations, and present satisfaction is preferred to the same satisfaction later (LW-7). Hence:
- (a) a change expected in the future alters choices now, as far as present actions' payoffs depend on it: announcement effects, rushes before deadlines, holding back when a policy may return;
- (b) a stock (buildings, equipment, skills, inventories, a client base) changes only through flows (production, investment, maintenance, wear, conversion), so its response to a change in returns is gradual, and changes that cost something to undo persist after the cause is removed. Two cases need care in repeals. A cost already incurred under the policy (training paid for, a conversion completed) is the same with and without the repeal, so it is not a consequence of the repeal; it enters only through what it makes cheaper or dearer next. An effect that exists only during the transition (units held empty before decontrol, buyouts before a deadline) has no lasting stock to persist: record its `persistence` as `n/a`;
- (c) the value of a durable means reflects the yields it is expected to bring, discounted by time preference (with CR-7c).

**Premises.** What actors expect (`expectations`); how durable the stock is (`durability`); what reversal costs (`reversal_cost`).

**Derivation.** AX-1 (action aims at a future state), LW-7, CR-4.

**Source.** HA ch. XVIII §2, §5 and §8; MES ch. 6 §3 and ch. 7 §5.

### CR-11 Knowledge

**Statement.** Actors act on what they know and believe. Hence:
- (a) a price that is prevented from moving stops conveying the scarcity it would have revealed, and those who rely on it act as if conditions were other than they are;
- (b) where an exchange is moved outside the legal market, the means by which buyers and sellers ordinarily learn about each other (advertising, reputation, brands, certification, courts) are not available to it; where it moves back into the legal market, they become available again;
- (c) a policy can change actions by conveying information (a license as a signal, a record of conviction), and only to that extent can it change what actors believe.

**Derivation.** AX-1 (action rests on the actor's understanding of the situation), CR-1, LW-8.

**Source.** Hayek, "The Use of Knowledge in Society" (1945); Mises, "Economic Calculation in the Socialist Commonwealth" (1920); HA ch. XXVI.

**0.7 clarifications.**
- *What a sign needs.* A consequence of information conveyed by a policy needs two premises: what the actors believed before (otherwise nothing changes), and which way those who learn something move (otherwise the direction is open).
- *Silence.* Where a policy requires some sellers to disclose and exempts others, buyers may infer something from an exempt seller's silence. That inference is information conveyed by the policy and falls under (c), with its own premise.

**0.9 clarifications.**
- *Sellers' response to silence.* Where buyers infer something from an exempt seller's silence, exempt sellers whose goods would compare well choose to disclose voluntarily (CR-4). Record it.
- *When a policy stops conveying something.* After a repeal, or when a signal becomes noisier, buyers' beliefs adjust as they learn; how fast is empirical. Record such consequences with `persistence: partial` and no long-run sign unless a premise gives one.

### CR-12 Composition

**Statement.** When several chains of reasoning reach the same actor class, variable and horizon:
- (a) if all push in the same direction, that is the combined direction;
- (b) if they push in opposite directions, the combined direction is `ambiguous`, unless a premise establishes that one chain dominates (stated under (e); a dominance pattern may be cited for it where one fits);
- (c) different variables are never netted against each other;
- (d) a consequence takes the lowest tier of any link in its chain, and holds only if all its premises hold. Where the same consequence is reached by independent chains with the same sign, it holds if any one chain's premises hold: list the premises of each chain separately, and report the consequence if at least one chain clears the cut-off.
- (e) a premise that establishes dominance under (b) may be an empirical premise with a probability, an accounting identity, arithmetic on the case's figures (a cost far smaller than a revenue), or the argument that a response cannot reverse the change that causes it (sellers moving sales abroad cannot push the domestic price back below its old level, since the move stops once the yields are equal). Say which. *0.8:* the response argument binds the response as a whole, not each member of a class (riders already aboard can be worse off from crowding by new riders, though new riders as a whole cannot reverse the fare cut that drew them); and it does not cover a response driven partly by a second change the policy also causes, which needs its own premise. A count over a distribution (how many homes cross a threshold) is arithmetic only if the distribution is in the case's figures; otherwise it is a premise.
- (f) where chains cancel exactly by construction (one provision undoes what another creates), the consequence is not reported, and section 7 says so.
- (g) chains at different horizons are not combined: a one-time effect in the short run and a lasting effect in the long run are separate consequences, one per horizon.
- (h) where a policy raises an activity in every window against the counterfactual, but also moves some of it from one window to another (bunching before each step-down of a subsidy), sign each window against the counterfactual and describe the bunching as a path note in section 8, with its effect on waiting or prices recorded as consequences where it has one.

**Derivation.** None needed: this is the logic of combining qualitative signs. The method states directions, not magnitudes, so opposing directions cannot be netted without a further premise.

**0.7 clarifications.**
- (g) does not forbid a separate consequence for a whole period ("over the ten years") where a dominance premise under (e) establishes its sign, such as a repayment plainly smaller than the receipt. That consequence is recorded with the horizon `whole period`, alongside the per-horizon ones.
- An opposing chain that cannot be derived from the rules is not a chain. Where a derived chain meets a suspected but underivable opposing effect, report the derived sign and record the suspected effect as a Tier C note, not as an ambiguity.
- *0.8. Three kinds of opposing chain.* (1) A chain no rule derives: a Tier C note, as above. (2) A chain the rules derive but that needs a premise the case lacks: it is a chain. State the premise with an estimated probability; if p is at least 0.5 the result is `ambiguous` without a dominance premise; if below 0.5, report the derived sign and record the chain in section 10 with its premise. (3) A chain whose own sign is `ambiguous`: it can push either way, so the combined sign is `ambiguous` unless a dominance premise covers the other chain against both of its directions.
- *0.8. Two items in one variable.* Where a policy moves two named items of the same variable in opposite directions (mandated sick time up, other benefits down, both `non_wage_compensation`), record each item as its own consequence with a qualifier, and record the total separately, combined under (b).
- The same action at different times is "the same" for timing shifts only if it is paid and performed in the same way; where the policy changes how it is paid (paid absence where it was unpaid), record the change in kind separately from any change in timing.

**0.9 clarifications.**
- *0.9. Tier C against Tier B.* Where a Tier C chain (through a `proximity` or `shared_facility` relation) opposes a Tier B chain on the same key, record two consequences: the Tier B chain's sign at Tier B, qualified "not counting effects through [relation]", and the combined sign at Tier C (`ambiguous` unless a dominance premise covers the Tier C chain). The Tier C chain never lowers the tier of the Tier B consequence by itself, and never raises its own tier by being combined.
- *0.9. What the response argument gives.* CR-12e's response argument shows that the result is not reversed: the price stays at or above its old level. To report `increase` rather than an increase or no change, the response must be partial: state that supply cannot fully expand at the old cost in the period, as a premise or from the case's figures.
- *0.9. Kind 3.* A chain whose own parts push in opposite directions is a kind (3) chain under the 0.8 note, unless its parts cancel by construction (CR-12f).
- *0.9. Activities that exist only under the policy.* An activity the policy creates (filings to hold a place in a queue, refund claims) is an `increase` in its window against a counterfactual of none. Say whether a timing consequence is signed on a flow (actions in the window) or on a stock (employment at a date).

---

## How the earlier laws relate to the core rules

Three of the laws in `01_foundations.md` are results of the core rules rather than independent premises: LW-3 (law of demand) is CR-4c applied to buyers, with CR-4's exception; LW-4 (resources move toward higher returns) is CR-7; LW-6 (non-price rationing) is CR-6. They keep their IDs because patterns and worked examples cite them.

## Map from workflow steps to core rules

| Workflow step | Core rules applied |
|---|---|
| 1, 2. State and classify the policy | CR-1 |
| 3. Actor classes | CR-1 (whose situation changes), CR-9 (whose situation changes in turn) |
| 4. Direct effect | CR-1, CR-2 |
| 5. Responses | CR-4 for every pair of options each actor class has; CR-6 where a price is fixed; CR-5 for prevented or compelled exchanges |
| 6. Second-order effects | CR-9, then CR-5 to CR-7 in each market reached |
| 7. Combine | CR-12 |
| 8. Time structure | CR-10 |
| 9. Opportunity costs | CR-3, CR-8 |
| 10. Conditions | The premises each core rule names |
