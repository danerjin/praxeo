# 3. The analysis workflow

This is the procedure for analyzing a policy. It has eleven steps. Do them in order on the first pass; later steps often send you back to earlier ones, which is expected. Record everything in `templates/analysis_template.md`.

Before starting, keep four habits in mind:

1. **People act, policies do not.** Every claimed effect must be a choice by some actor class (AX-1).
2. **Compare with the counterfactual, not the past.** The question is always "compared with the same place and time without the policy".
3. **Look for the unseen.** For each effect you find, ask who else is affected and what was given up (LW-1).
4. **Say what you assume.** If a step needs a fact about the world (that the law is enforced, that a substitute exists), write it down as an assumption and estimate how likely it is.

---

## Step 1. State the policy precisely

**Goal.** A policy record (see `02_ontology.md`, 2.1) that says exactly what is required, prohibited, taxed, subsidized or transferred, by whom, for whom, from when, and with what enforcement.

**Questions to ask**
- What exactly does each provision require or forbid? Split the policy into components, one per instrument.
- When was it announced or first expected, and when does it take effect? The gap between the two is when announcement effects happen (RS-8).
- Who is bound? Who is exempt, and on what conditions?
- What are the parameters (cap, rate, number of hours, quantity)? How do they change over time?
- Who enforces it, with what penalties, and with what resources?
- For taxes: where does the revenue go? For subsidies and spending: where does the money come from?
- Where is the jurisdiction's boundary, and what lies just outside it?

**Pitfalls**
- Analyzing the policy's stated purpose instead of its provisions. The title says "affordable housing"; the provisions say "no rent increase above 2% a year".
- Missing exemptions. Exemptions create boundaries, and boundaries create incentives to move across them (RS-5).
- Guessing unclear provisions. Mark them `unclear` and, if they matter, analyze both readings.

**Output.** Policy record with components.

---

## Step 2. Classify each component

**Goal.** For each component, its instrument type and Rothbard type (`02_ontology.md`, 2.3), and the rule families that apply.

**Questions to ask**
- Does it force or prohibit an exchange between private parties (triangular), force an exchange with the state (binary), or restrict a person's own action (autistic)?
- Is it binding? A price ceiling above the market-clearing price, or a licensing requirement that everyone already meets, changes nothing now. Record bindingness as an assumption, with its estimate and how it may change over time (a cap fixed in money terms becomes binding as other prices rise).

**Pitfalls**
- Classifying the whole policy as one type when components differ. A tariff is a tax on importers (binary) and a grant of privilege to domestic producers (triangular); analyze both sides.

**Output.** A component table: instrument, Rothbard type, binding (with assumption ID), rule families.

---

## Step 3. Identify the actor classes

**Goal.** A list of every actor class whose options change, using the generic list in `02_ontology.md`, 2.2 as a checklist.

**Questions to ask**
- Who is directly bound? Who directly benefits? Who pays?
- Who is a current participant and who is a prospective one? (Prospective buyers and sellers are the most often forgotten.)
- Who owns resources specific to this market, which cannot easily move elsewhere?
- Who participates in markets for substitutes and complements, or just across the border?
- Who administers and enforces the policy? Who would gain from changing it?

**Pitfall.** Treating a group as homogeneous when the policy splits it. Rent control splits tenants into those who have a controlled unit and those looking for one. Licensing splits providers into those who qualify and those who do not.

**Output.** Actor-class table: class, role, and how its options change.

---

## Step 4. Identify the direct effect

**Goal.** The immediate, intended change: the visible consequence the policy's supporters expect.

**Questions to ask**
- What does the policy change first, for whom, at once? (Rents paid by sitting tenants; prices paid at the shelf; who may legally offer a service.)
- Is the direct effect what the supporters claim, given the provisions? It sometimes is not.

**Pitfall.** Stopping here. The direct effect is usually real; it is just not the whole story.

**Output.** One or more consequences in normal form, marked `visible`.

---

## Step 5. Trace the responses

**Goal.** For each actor class, how its constraints and incentives change and what its members will do differently at the margin.

**Questions to ask**, for each actor class:
- Which of its options became more costly, cheaper, forbidden or newly available?
- Who in the class is at the margin (LW-2): for whom does the ranking of the best and next-best options change?
- Which generic responses are open to them? Work through the list:

| Response | Rule | Ask |
|---|---|---|
| Substitute | RS-1 | What else serves the same end? Is it covered by the policy? |
| Adjust quality or terms | RS-2 | Can the non-price terms of the exchange change (quality, maintenance, service, contract length)? |
| Evade | RS-3 | Is breaking the rule cheaper than complying, given the enforcement? |
| Relocate | RS-4 | Can the activity move outside the jurisdiction? |
| Reclassify | RS-5 | Can the good or contract be reshaped to fall outside the definitions or into an exemption? |
| Exit or stop producing | RS-6 | Do resources have better uses elsewhere (LW-4)? How quickly can they move? |
| Lobby | RS-7 | Does anyone now have a concentrated stake in extending, changing or repealing the policy? |
| Change timing | RS-8 | Does the policy reward acting sooner or later (deadlines, phase-ins, expected changes)? |

**Pitfalls**
- Assuming everyone responds. Only those at the margin do; the others carry on, which is why the direct effect is often visible while the responses are not.
- Assuming responses are instant. Note how fast each can happen; that becomes step 8.

**Output.** Responses as consequences in normal form, each with its rule and assumptions.

---

## Step 6. Trace second-order effects

**Goal.** How the responses affect other actor classes and other markets.

**Questions to ask**
- When an actor class changes its behavior, whose options change as a result? (Landlords cut maintenance; tenants receive worse quality. Buyers move to substitutes; prices rise there.)
- Which recorded market relations (`02_ontology.md`, 2.8) does the effect travel along? If you need a relation that is not recorded, record it with its evidence first.
- What happens to the people who would have made the exchanges that no longer happen (LW-5)?
- Three second-order patterns to check every time:
  - **Bundled trips (RS-9).** If buyers now shop somewhere else for the target good, what else do they buy on the same trip?
  - **Informal trade (RS-10).** If some trade goes underground, what happens to search costs, quality and dispute resolution?
  - **Lock-in (RS-11).** If people now hold a benefit they lose by moving or by changing status, which other choices (jobs, breaks, schools) do they now turn down?
- Four more links to check:
  - **Complements in use (RS-12).** If the stock or use of a good changes, what is used with it?
  - **Added supply (RS-13).** Does the policy push extra supply into a linked market?
  - **Inputs (RS-14, PC-12).** If the policy changes the cost of an input, what happens to the price of the output? If it caps the output, what happens to the input?
  - **Asset values (SB-4).** Does the policy change the lasting return to an asset in fixed supply? Its value moves at announcement.
- **Policies with several components.** For each pair of components, ask:
  - Does one close or open an exit route from the other?
  - Does one change who is bound by the other?
  - Does one fund the other (SB-7)?
  - Does one tax or restrict the other's intended output?

  Record the components each interaction chain runs through.

**Stopping rule.** Stop each chain at depth 4 (four links from the policy), and stop any branch earlier if it has reached a diffuse effect on bystanders at depth 3. Note where you stopped. Chains are not stopped because an effect "seems small"; this method cannot measure size.

**Pitfall.** Following a chain through an unrecorded market relation, such as "this will hurt restaurants" without saying why restaurants are linked to the target.

**Output.** Second-order consequences in normal form.

---

## Step 7. Combine effects

**Goal.** One sign for each actor class and variable, where several chains reach the same place.

**Procedure** (plan, Section 4.5):
1. List every consequence by (actor class, variable, horizon).
2. If all chains for that key have the same sign, that is the combined sign.
3. If signs conflict and a dominance rule (DM family) applies, apply it, and add its assumption.
4. If signs conflict and no dominance rule applies, the sign is `ambiguous`. Keep all chains, and state what would decide it.
5. A one-time cost in one chain against a later stream of gains in another is ambiguous by design (DM-3): say so, and do not try to net them.
6. Never merge different variables. "Wage rate rises" and "hours fall" are two consequences.

**Output.** Combined consequence list.

---

## Step 8. Add time structure

**Goal.** A horizon for each consequence, and a note on effects that grow, fade or reverse over time.

**Questions to ask**
- How durable are the goods and capital involved? Supply responses for durable goods (buildings, equipment, trained skills) arrive as the existing stock wears out and is not replaced (TS-1).
- Does the policy bind more tightly over time (a cap fixed in money terms while other prices rise)?
- What do actors expect: that the policy will be extended, tightened, repealed? Expectations bring responses forward (TS-2).
- Does the policy shift activity in time (a temporary subsidy that pulls purchases forward, followed by a dip; see SB-6)?

**Output.** Horizon field filled in for every consequence; notes on growth and reversal.

---

## Step 9. Identify opportunity costs

**Goal.** The unseen consequences: what the resources used by or because of the policy would otherwise have done.

**Questions to ask**
- What resources does the policy take (taxes, borrowing) or direct (mandated spending, compliance, enforcement)? What would their owners have done with them (OC-1)?
- What time and effort do people now spend that does not appear in any price: queues, searches, paperwork, training hours that serve only to qualify (OC-2)?
- What exchanges no longer happen, and what did each party expect to gain from them (LW-5)?
- What production does not happen because resources moved elsewhere?
- Whose work depended on the spending that was diverted (OC-5, Bastiat's tailor)?

**Pitfall.** Counting what the money is spent on as a pure gain. The spending is visible; what the taxpayers would have bought is not. Both must appear.

**Output.** Opportunity-cost consequences, almost always `invisible`, each written as a signed change in a variable (for example `resources_available_other_uses` decrease, `quantity_traded` decrease for prevented exchanges), never as a bare "loss".

---

## Step 10. State and estimate conditions

**Goal.** For every Tier B consequence, its assumptions, an estimate of how likely each is to hold in this case, the evidence for the estimate, and what would reverse the conclusion.

**Questions to ask**
- Is the policy binding, now and later?
- Will it be enforced, and how strictly?
- Do substitutes exist, inside and outside the policy's reach?
- Can resources move to other uses, and how quickly?
- What are actors likely to expect about the policy's future?

**Rules for estimates**
- Estimates are made now, before any outcome is known, and are not revised after.
- Each estimate cites its evidence: the policy text, enforcement budgets, the existence of a border nearby, conversion rules, past behavior in comparable places.
- A consequence is reported if each of its assumptions has p of at least 0.5. Consequences below the cut-off are listed separately as conditional possibilities. (Whether the cut-off should apply to the joint probability instead is open: `06_gaps.md`, Q9.)
- Readings of an unclear provision are not assumptions and get no probability. Where a sign depends on the reading, report one sign per reading (`02_ontology.md`, 2.5).

**Output.** Assumption table; each consequence linked to its assumptions.

---

## Step 11. Report

**Goal.** A report a non-expert can follow, that commits to clear claims.

**Structure**
1. **The policy in one paragraph:** what it does, not what it is for.
2. **Visible consequences:** the direct effects, with who gains and who pays.
3. **Invisible consequences:** grouped by actor class, each with its chain in plain words, its horizon and its key assumptions.
4. **Ambiguous effects:** what pushes each way, and what would decide it.
5. **Conditions:** the assumptions that matter most, their estimates, and what would change the picture.
6. **What the method cannot say:** sizes, net welfare, whether the policy is good, and (in version 1) health, safety and environmental effects. These are left to the reader or to other methods.

**Pitfalls**
- Advocacy. Describe consequences by group and horizon; do not weigh them.
- Unsupported claims. Every sentence in the report must trace to a consequence in the list; anything else is labelled as a Tier C suggestion.

**Output.** The report, and the full consequence list in normal form.

---

## Analyzing a repeal

A repeal is analyzed with the same eleven steps, with three differences.

1. **The counterfactual is that the policy stays in force.** Signs are relative to that path, not to the world before the policy.
2. **Check what does not reverse.** For each consequence of the original policy, ask whether the repeal reverses it, partly reverses it or leaves it in place (TS-6). Converted buildings, closed firms, lost skills and displaced people do not come back just because the rule is gone. Record `persistence` on each consequence, and include a table that checks the repeal against the original analysis, as in WE-022 to WE-024.
3. **Ask whether the repeal is believed (TS-5).** If actors think the policy may return, quick-payback responses go ahead and long-payback ones are held back. Ask also who must make up any lost revenue (OC-6), and who now has a stake in restoring the policy (RS-7).
