# 4a. Core rules (the calculus)

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

**Source.** Mises, *Human Action*, ch. I and ch. XXVII; Rothbard, *Power and Market*, ch. 2 (pending verification).

### CR-2 Choice

**Statement.** Each actor chooses, from the options they believe open, the one they expect to serve their most highly ranked end. What an actor chooses reveals that they ranked it above the alternatives open at the time (demonstrated preference).

**Derivation.** AX-1, with LW-2 (ordinal valuation).

**Premises.** None for the statement. What actors believe about their options is a fact about them, and may be wrong (CR-11).

**Source.** Mises, *Human Action*, ch. I and IV; Rothbard, "Toward a Reconstruction of Utility and Welfare Economics" (1956) (pending verification).

### CR-3 Cost and loss

**Statement.** The cost of an action is the most highly ranked alternative given up by taking it. Hence:
- (a) removing an actor's chosen option, or attaching a burden to it, makes the actor worse off by their own ranking, unless their next-best was ranked equal;
- (b) only adding options, or removing burdens, cannot make an actor worse off by their own ranking at the time of choice;
- (c) means used for one end are not available for any other (LW-1).

**Derivation.** CR-2 and LW-1. Under (a) the actor must fall back to an alternative they ranked lower. Under (b) the previously chosen option is still open.

**Premises.** None. (Statement (b) is about the actor's ranking at the time of choice; it says nothing about how things turn out.)

**Source.** Mises, *Human Action*, ch. IV and VII; Rothbard, *Power and Market*, ch. 2 (pending verification).

### CR-4 Response at the margin

**Statement.** Suppose a change makes option x worse relative to option y for an actor (x costs more, brings less, or y improves). Then:
- (a) no actor who was choosing y switches to x on account of the change;
- (b) among actors who were choosing x, those for whom x was ranked only narrowly above y (or above some other alternative) switch away from it; the rest keep choosing x and bear the change (CR-3a);
- (c) the same holds for each unit when an actor chooses how many units of x to take: the last unit, which was valued least (LW-2), is the first given up.

The mirror case (x made better) reverses every direction.

**What is a priori and what is not.** Statement (a) and the direction in (b) and (c) are a priori. That some actors actually are at the margin, so that someone does switch, is empirical: it is the premise behind `substitutability`, `alternative_uses` and `mobility`. **Exception:** when the change also alters the actor's total means (a price rise on something they spend much of their means on; a lower return on something they save toward a fixed sum), the change in means can shift their ranking among other options in the opposite direction. Where such an effect matters, the direction for that actor class is `ambiguous` unless a premise says which effect dominates (this is the exception recorded under LW-3 and TX-6).

**Derivation.** CR-2 and CR-3. Under (a), y was ranked above x before, and x is now worse, so y still ranks above it. Under (b) and (c), LW-2.

**Use.** All the generic responses are this one rule applied to different pairs of options: substitution (x: the good, y: a substitute), evasion (x: comply, y: violate), relocation (x: here, y: there), reclassification (x: the covered form, y: the uncovered form), exit (x: this use, y: another use), lobbying (x: accept, y: lobby), timing (x: now, y: later), entry (x: stay out, y: enter).

**Source.** Mises, *Human Action*, ch. VII; Rothbard, *Man, Economy, and State*, ch. 1 and 2 (pending verification).

### CR-5 Exchange

**Statement.** A voluntary exchange takes place only if each party ranks what they receive above what they give. Hence:
- (a) a policy that prevents an exchange that would otherwise have taken place deprives both parties of a gain each expected;
- (b) a policy that compels a transfer that would not have taken place voluntarily makes at least one party worse off by their own ranking;
- (c) the terms of any exchange that does take place lie within the range both parties accept, and any change in what one party must give or may receive moves that range.

**Derivation.** CR-2 applied to both parties; CR-3.

**Premises.** None for (a) to (c). Whether a given exchange would have taken place without the policy is the empirical question.

**Source.** Rothbard, *Man, Economy, and State*, ch. 2; *Power and Market*, ch. 1 and 2; Mises, *Human Action*, ch. XV (pending verification).

### CR-6 Price formation and displaced pressure

**Statement.** At any price at which the quantity buyers wish to buy differs from the quantity sellers wish to sell, some unsatisfied party can gain by offering better terms, and some party on the other side can gain by accepting them (CR-5). Prices therefore tend toward the level at which planned purchases and sales are compatible.

If a rule prevents the price from moving, the gain from closing the gap does not disappear. Unsatisfied parties pursue it along every margin that is still open:
- the terms that are not regulated (quality, service, conditions, timing);
- the criteria by which the scarce side chooses among the other side (queues, connections, preference for some buyers or sellers);
- exchanges outside the rule, where the expected gain exceeds the expected penalty (CR-4 with x: comply, y: violate).

The full price, meaning the money price plus everything else given up, moves toward the clearing level as far as the open margins allow.

**What is a priori and what is not.** That the pressure exists and moves to open margins is a priori. Which margins are open, and how wide, is a fact about the case: which terms are regulated, and how well the rule is enforced (`enforcement`, `binding`).

**Symmetry.** The same rule covers a price held too low (pressure from buyers) and too high (pressure from sellers), in any market: goods, labor, loans, housing, permits.

**Derivation.** CR-2, CR-4, CR-5.

**Source.** Mises, *Human Action*, ch. XVI and XXX; Rothbard, *Man, Economy, and State*, ch. 2; *Power and Market*, ch. 3 (pending verification).

### CR-7 Equalization across uses

**Statement.** Wherever a means (labor, capital, money, land, a purchase, an activity, a moment in time) can be moved between uses that serve the same end, its owners move it from the use that yields less to the use that yields more, until the difference in yield at the margin is no greater than the cost of moving. Hence:
- (a) after any change in yields, yields on the means that can move are brought back into line, net of moving costs;
- (b) the lasting gain or loss from the change settles on the means that cannot move: specific, immobile or fixed resources, and actors without alternatives (this decides who bears a tax and who keeps a subsidy or a privilege);
- (c) the price of a durable asset adjusts until a buyer expects to earn on it what they could earn elsewhere, so a lasting change in its expected yield is borne or captured by whoever owns it when the change becomes expected, not by later buyers.

**What is a priori and what is not.** The direction of every movement is a priori (CR-4 for each owner). How mobile each means is, and how fast it moves, is empirical (`mobility`, `alternative_uses`, `durability`).

**Symmetry.** It applies to yields raised and lowered, to buyers and sellers, to the present and to future uses.

**Derivation.** CR-2 and CR-4 applied to every owner of a movable means; CR-10 for (c).

**Source.** Mises, *Human Action*, ch. XIV and XV (the evenly rotating economy; the tendency to eliminate profit and loss); Rothbard, *Man, Economy, and State*, ch. 6 and 7 (equalization of returns; capitalization); Rothbard, *Power and Market*, ch. 4 (shifting and incidence) (pending verification).

### CR-8 Conservation of means

**Statement.** A policy does not create means; it redirects or uses them up. Hence:
- (a) every resource the policy directs to one use is withdrawn from another use its owner would have chosen (the seen and the unseen);
- (b) every payment is a receipt to someone, and every transfer adds to the recipient exactly what it takes from the payer;
- (c) resources spent on complying with, administering, enforcing or evading a policy, or on queuing, searching or lobbying because of it, are used up and serve no other end of those who spend them;
- (d) money is fungible: a sum earmarked for one purpose frees other money for other purposes, unless the other spending is also fixed.

**Derivation.** LW-1 and CR-3c.

**Premises.** None for (a) to (d). Which use the means would otherwise have gone to is the empirical question (`revenue_use`).

**Symmetry.** Applies to taxes and subsidies, imposition and repeal, public and private budgets. A rule that counts a gain to the recipient of a transfer, or to the seller of an asset that has risen in value, must count the matching loss to the payer or buyer.

**Source.** Bastiat, "That Which Is Seen, and That Which Is Not Seen" (1850); Hazlitt, *Economics in One Lesson*, ch. 2 and 4; Rothbard, *Power and Market*, ch. 5 (pending verification).

### CR-9 Propagation

**Statement.** When an actor changes what they do, the situation of everyone who would have dealt with them changes too: those who would have sold to them or bought from them, those who compete with them for the same means or customers, and those whose goods are used together with theirs. Apply CR-1 to CR-8 to each of these actors in turn, following actual exchange relations and the relations recorded under `02_ontology.md`, 2.8.

The value to anyone of a means depends on the ends it serves and on what it is used with (LW-10). So when the use of a good changes, the demand for the means that produce it and for the goods used with it changes in the same direction, and the demand for goods that compete with it in the opposite direction.

**Derivation.** CR-1 (one actor's choice changes the options open to those who deal with them), CR-5, LW-10.

**Limits.** Propagation follows exchange relations only, and stops at the depth limit in workflow step 6. Every link must name the relation it uses.

**Source.** Menger, *Principles of Economics*, ch. I to III; Mises, *Human Action*, ch. XVI; Rothbard, *Man, Economy, and State*, ch. 7 (pending verification).

### CR-10 Time

**Statement.** Action takes place in time, on expectations, and present satisfaction is preferred to the same satisfaction later (LW-7). Hence:
- (a) a change expected in the future alters choices now, as far as present actions' payoffs depend on it: announcement effects, rushes before deadlines, holding back when a policy may return;
- (b) a stock (buildings, equipment, skills, inventories, a client base) changes only through flows (production, investment, maintenance, wear, conversion), so its response to a change in returns is gradual, and changes that cost something to undo persist after the cause is removed;
- (c) the value of a durable means reflects the yields it is expected to bring, discounted by time preference (with CR-7c).

**Premises.** What actors expect (`expectations`); how durable the stock is (`durability`); what reversal costs (`reversal_cost`).

**Derivation.** AX-1 (action aims at a future state), LW-7, CR-4.

**Source.** Mises, *Human Action*, ch. V and XVIII; Rothbard, *Man, Economy, and State*, ch. 6 (pending verification).

### CR-11 Knowledge

**Statement.** Actors act on what they know and believe. Hence:
- (a) a price that is prevented from moving stops conveying the scarcity it would have revealed, and those who rely on it act as if conditions were other than they are;
- (b) where an exchange is moved outside the legal market, the means by which buyers and sellers ordinarily learn about each other (advertising, reputation, brands, certification, courts) are not available to it;
- (c) a policy can change actions by conveying information (a license as a signal, a record of conviction), and only to that extent can it change what actors believe.

**Derivation.** AX-1 (action rests on the actor's understanding of the situation), CR-1, LW-8.

**Source.** Hayek, "The Use of Knowledge in Society" (1945); Mises, *Human Action*, ch. XXVI; Mises, "Economic Calculation in the Socialist Commonwealth" (1920) (pending verification).

### CR-12 Composition

**Statement.** When several chains of reasoning reach the same actor class, variable and horizon:
- (a) if all push in the same direction, that is the combined direction;
- (b) if they push in opposite directions, the combined direction is `ambiguous`, unless a premise establishes that one chain dominates (a dominance pattern, `DM`, with its premises stated);
- (c) different variables are never netted against each other;
- (d) a consequence takes the lowest tier of any link in its chain, and holds only if all its premises hold.

**Derivation.** None needed: this is the logic of combining qualitative signs. The method states directions, not magnitudes, so opposing directions cannot be netted without a further premise.

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
