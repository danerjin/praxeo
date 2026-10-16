# WE-024 Abolition of the braiding license requirement

Analyst: draft (Handbook 0.5)  |  Rule catalog version: 0.5  |  Status: awaiting expert review

A stylized repeal of the licensing rule analyzed in WE-003, in the same fictional state, five years after it took effect. It doubles as a metamorphic check: the analysis of the abolition should reverse the signs of WE-003, except where the license caused lasting changes. The check is at the end of section 7. The counterfactual throughout is **the license requirement stays in force**; every sign is relative to that, not to the situation before the abolition and not to a Westmark that never licensed braiding. "In reverse" after a rule ID means the rule is applied to the removal of its precondition; where that direction is not obviously valid, the text says so. The catalog states some directions explicitly: RS-10 has a reverse clause for trade returning to the legal market (with `quality_variability` ambiguous where the repeal admits sellers a training requirement excluded), RS-7 has a clause for repeals, where lobbying takes place in the counterfactual too, and TS-5 and TS-6 are written for repeals (see "Analyzing a repeal" in the workflow). The probabilities are illustrative.

## 1. Policy record

**Westmark State Cosmetology Act, amendment 9 (braiding exemption).** Five years after amendment 7 (WE-003) required a full cosmetology license to braid hair for pay, the legislature removes braiding from the definition of cosmetology. The bill was introduced, with the votes to pass visible, about nine months before the exemption took effect. The starting point, taken from WE-003's analysis and stated here as the situation at abolition rather than as findings: some braiders trained and became licensed, at a cost of 1,500 hours and $12,000 to $18,000 in tuition; some left the trade for other work; some kept braiding without a license; cosmetology schools enrolled braiders who wanted only to braid legally; legal braiding costs more than it did. The neighboring states still do not license braiding.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Exemption | Removal of a `licensing_requirement` | Braiding hair for pay (braids, twists and locs, with no cutting or chemicals) | Braiders and businesses that employ them | No license, registration or training is required to braid for pay, or to employ braiders. Existing cosmetology licenses remain valid. Tuition already paid is not refunded. Cutting, coloring and chemical treatments still require a cosmetology license. | None |
| R2 Enforcement | End of enforcement | WE-003 K2 as it applies to braiding | State Board of Cosmetology | Inspections and fines for unlicensed braiding end; pending braiding cases are dropped. | None |

Unclear provisions: whether a licensed salon must ensure that its braiders hold a license because the establishment itself is licensed. Assumed not: the exemption applies to the service, wherever it is performed.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| R1 | Removal of a triangular intervention: customers and unlicensed braiders may again trade legally; the privilege of license holders ends | Yes: many people who would braid for pay do not hold a cosmetology license (A-1) | EN in reverse, RS, RS-8, RS-10 (reverse clause), OC, TS-5, TS-6 |
| R2 | Removal of a binary intervention (enforcement funded by taxpayers and license fees) | Yes | OC-3 in reverse |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `braiders.licensed` | Braiders who obtained the license under amendment 7 | Lose the price advantage of being among the few legal providers; tuition and hours are already spent; keep the right to offer cutting, coloring and chemical services. |
| `braiders.in_training` | Braiders enrolled in cosmetology school at the time of the exemption | Can stop and braid legally without finishing. |
| `braiders.informal` | People braiding for pay without a license | Can work openly, advertise and use the courts. |
| `braiders.former` | People who left braiding because of the license | May return; five years on, their skills, clients and alternatives have changed. |
| `braiders.prospective` | People who would start braiding | Entry costs only the skill itself. |
| `cosmetologists.licensed` | Licensees other than former braiders who offer braiding | Face more competition in braiding. |
| `schools.cosmetology` (`input_suppliers`) | Licensed schools | Lose students who enrolled only to braid legally. |
| `customers.braiding` | People who pay for braiding | More legal providers, lower prices. |
| `businesses.braiding` (salons) | Shops that employ braiders | May employ unlicensed braiders; no license checks or fines. |
| `sellers.cosmetology_other`, `buyers.cosmetology_other` | Sellers and buyers of cutting, coloring and chemical services | Licensed braiders move some of their time into these services. |
| `braiders.with_pending_cases` | Braiders with braiding cases pending at the board | Cases are dropped (R2). |
| `officials.enforcement`, `taxpayers` | Board of Cosmetology and its funders | Braiding enforcement ends; braiders no longer buy licenses. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | braiders in the legal market | `share_of_sellers_licensed` | decrease | short | EN-1 in reverse | A-1 |
| C-2 | `braiders.informal` | `informal_activity` | decrease | short | RS-3, EN-3 in reverse | A-2 |

The visible effects: legal braiders no longer need to be licensed, and braiders who were working outside the law can work openly. RS-3 in reverse is valid here without qualification: once braiding without a license is legal, there is no rule left to evade.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | braiders | `number_of_sellers` (legal) | increase | short | EN-1 in reverse | A-2 |
| C-4 | `braiders.prospective` | `entry_rate` | increase | short to medium | EN-1 in reverse | A-3 |
| C-5 | `braiders.in_training` | `compliance_cost` (remaining hours and tuition) | decrease | short | OC-2 in reverse | A-4 |
| C-6 | `schools.cosmetology` | `quantity_demanded` for programs | decrease | short (from the announcement) | EN-1 in reverse, RS-8 | A-5 |
| C-7 | `braiders.former` | `employment` (in braiding) | increase | medium | EN-3 in reverse, TS-6 | A-6, A-15 |
| C-8 | `braiders.licensed` | `quantity_supplied` (services that only licensees may offer: cutting, coloring, chemical treatments) | increase | medium | LW-4, RS-6 | A-7 |
| C-9 | `schools.cosmetology`, `braiders.licensed`, `cosmetologists.licensed`, braiders | `lobbying_effort` | ambiguous (see section 7) | medium | RS-7 (repeal clause), EN-5 | A-8 |
| C-22 | `braiders.with_pending_cases` | `resources_available_other_uses` | increase | short | CR-1, CR-8 | none |
| C-23 | `businesses.braiding` | `compliance_cost` (license checks, risk of fines) | decrease | short | OC-2 in reverse | A-1 |
| C-24 | `businesses.braiding` | `employment`, `hours_worked` (braiders in shops) | at_least_one_increase | medium | EN-1 in reverse, CR-4, CR-9 | A-1, A-3 |
| C-10 | braiders formerly working informally | `investment_target` (premises, chairs, signage) | increase | medium | RS-6 in reverse, LW-4, TS-5 | A-2, A-11 |

C-3 is fast because almost nothing has to be built: informal braiders already have the skill, the tools and the customers, and need only to stop hiding.

C-6 starts at the announcement (RS-8, "delay until after a repeal is expected"): would-be braiders stop enrolling once the exemption is expected.

C-7 is Tier B in catalog 0.3 (Tier C in the 0.2 draft). EN-3 says that sellers excluded by a license move to their next-best occupation. Applied in reverse it would say they move back once the license goes, but TS-6 limits that five years on: skills unused for five years decay, clients have found other braiders, and some former braiders have built experience in their new work, which raises what they would give up by returning (A-15, `reversal_cost`). Former braiders return only where the restored return exceeds that cost. The sign is an increase, because some will return (A-6); how many, the method cannot say. Persistence against a Westmark that never licensed braiding is partial (metamorphic check, WE-003 C-2 and C-4).

C-8: with the braiding premium gone, licensed braiders shift some of their time to the services their license still reserves to them (LW-4). Their training, sunk in both the repeal and the counterfactual, now earns its return there or not at all.

C-9: RS-7's repeal clause applies. Every class here lobbied with the license in force: schools and licensees to defend it, braiders for an exemption (WE-003 C-8). After the exemption schools and licensees lobby to restore it and braiders to defend the exemption. Each class lobbied in both worlds, so the change in each class's effort is `ambiguous` without a premise. RS-7's premise, that each can organize at a cost below its stake, is A-8.

C-22: R2 drops pending braiding cases, so the fines are not paid; what would have gone to the state stays with the braiders (CR-1, op 3 removed; CR-8b).

C-23 and C-24 mirror WE-003's C-18: shops no longer check licenses or risk fines for employing unlicensed braiders (OC-2 in reverse), and can hire from the larger legal pool (EN-1 in reverse; CR-4 for the shop, x: no braider or a licensed one, y: an unlicensed one; CR-9 along braiders' labor `input_to` shop braiding). Shops may add braiders or hours, so only the group is signed.

C-10 is Tier B in catalog 0.3 (Tier C in the 0.2 draft). Braiders who come into the open may rent premises and equipment, to the extent they expect the exemption to last long enough to pay them back (TS-5, A-11, p = 0.7). Braiding capital is small and pays back quickly, so this expectation matters much less here than in WE-022 or WE-023.

Not reported:
- A rush to enter braiding before the license might return with existing braiders grandfathered (TS-5, grandfathering clause). It needs braiders to expect both re-imposition and grandfathering (A-13, p = 0.25).
- Braiders returning from neighboring states. WE-003 found little relocation in the first place (A-14, p = 0.2).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-11 | `customers.braiding` | `price_paid` (legal braiding) | decrease | short to medium | EN-1 in reverse | | A-2, A-3 |
| C-12 | `braiders.licensed`, `cosmetologists.licensed` who braid | `net_price_received` (braiding) | decrease | short to medium | EN-2 in reverse | | A-2, A-3 |
| C-13 | `customers.braiding` | `quantity_substitute` (braiding by family and friends, or going without) | decrease | short | EN-3, RS-1 in reverse | paid and home braiding: `substitute`, partial | A-9 |
| C-14 | `customers.braiding` | `search_cost` | decrease | short | RS-10 in reverse | | A-2 |
| C-15 | `customers.braiding` | `quality_per_unit` received | not reported (see section 7) | medium | EN-4 in reverse, DM-2 | | A-10, A-16 |
| C-16 | `braiders.licensed` | `earnings` | decrease (see section 7) | medium | EN-2 in reverse, LW-2 | | A-2, A-3 |
| C-20 | `customers.braiding` | `quality_information` | increase | short to medium | RS-10 (reverse clause) | | A-2 |
| C-21 | `customers.braiding` | `quality_variability` | ambiguous | medium | RS-10 (reverse clause) | | A-2, A-3 |
| C-25 | `customers.braiding` | `disputes_settled_outside_courts` | decrease | short to medium | RS-10 (reverse clause) | | A-2 |
| C-26 | `buyers.cosmetology_other` | `price_paid` (cutting, coloring and chemical services) | decrease | medium | RS-13 | braiding and other cosmetology services: `same_market_other_segment`, partial (shared sellers) | A-7 |
| C-27 | `sellers.cosmetology_other` | `net_price_received` (cutting, coloring and chemical services) | decrease | medium | RS-13 | as C-26 | A-7 |
| C-28 | `schools.cosmetology` (instructors) | `employment`, `hours_worked` | at_least_one_decrease | medium | CR-9, RS-6 | instruction `input_to` licensed braiding, partial | A-5 |
| C-29 | `officials.enforcement` (board) | `tax_revenue` (license fees from braiders) | decrease | medium to long | CR-1, CR-8 | | A-5 |
| C-30 | `customers.braiding` (legal market) | `resources_available_other_uses` | increase | short to medium | EN-1 in reverse, CR-8 | | A-2, A-3 |

C-14, C-20, C-21 and C-25 apply RS-10's reverse clause: braiders who come into the open can advertise, collect public reviews and be taken to court, so customers find them more easily (C-14), can judge their quality before buying (C-20) and settle fewer disputes outside the courts (C-25). The spread of quality between braiders they might use (C-21) is `ambiguous`: better information lets customers screen out poor braiders, but the exemption also admits new entrants who were previously excluded by the training requirement (C-4), some with little experience, which widens the spread of sellers. Licensed braiders can still advertise their license as a voluntary signal. C-21 is about the spread of quality, C-15 about its level; they are separate consequences.

C-26 and C-27: licensed braiders move some of their time into the services their license still reserves (C-8), adding supply there (RS-13), so those services cost buyers less and their incumbent sellers receive less. C-28: fewer enrollments (C-6) mean less demand for instruction (CR-9); schools may cut instructors or hours (RS-6, group). C-29: braiders who would have bought a cosmetology license under the counterfactual (A-5) no longer pay license fees to the board (CR-1, CR-8b). C-30: customers who keep buying legal braiding pay less for it (C-11), the other side of licensed braiders' lower receipts (C-12; CR-8b). Customers who move from home braiding to paid braiding may spend more on it, so no sign is given for them.

C-15 is not reported. In reverse, EN-4's chains are: (+) customers move back from home braiding and hidden informal braiders to an open legal market; (−) legal providers are no longer all trained to the license standard. Under DM-2 (0.5) each chain needs its own premise. The (−) chain is inactive, because the training is largely unrelated to braiding (A-10). The (+) chain needs what customers leave to be of lower quality than the open paid braiding they return to (A-16, p = 0.45, the mirror of WE-003's A-7): informal braiders are largely the same people who braid openly. A further route, from better information (C-20) to higher quality supplied, would need its own premise about sellers' quality choices, which the case does not supply.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `customers.braiding`, `quality_per_unit` received, medium | Customers move back from home braiding and hidden informal providers to an open legal market with reviews and recourse (C-13, C-14, C-20; EN-3 in reverse, RS-10 reverse clause). Active only if what they leave is of lower quality (A-16, p = 0.45). | Legal providers are no longer all trained to the license standard (EN-4's "up" chain removed). Inactive: the training is largely unrelated to braiding (A-10, p = 0.85). | DM-2 (0.5): each chain needs its own premise. | **Not reported** (C-15). Neither chain is active at the cut-off. The mirror of WE-003's C-13, which is also not reported. If A-16 held, the sign would be an increase. |
| `customers.braiding`, `quality_variability`, medium | Untrained or inexperienced entrants, previously excluded by the training requirement, widen the spread of sellers (C-4). | Reviews, advertising and recourse let customers screen sellers (C-20). | None | **ambiguous** (C-21), as RS-10's reverse clause requires where the repeal admits previously excluded sellers. |
| `braiders.licensed`, `earnings`, medium | They may shift time to services their license reserves (C-8). But that option was open to them in the counterfactual too; that they braided instead shows they ranked braiding higher (LW-2). | The price of braiding falls (C-12), and they face more legal competitors (C-3). | None needed | **decrease**. The tuition and the 1,500 hours were spent before the exemption and are spent in the counterfactual as well, so they are not a consequence of the exemption. DM-3 does not apply, because only the stream of gains is in the comparison. |
| `schools.cosmetology`, `braiders.licensed`, `cosmetologists.licensed`, braiders, `lobbying_effort`, medium | Schools and licensed braiders, who paid a large sunk cost for an advantage the exemption removes, now have a concentrated stake in restoring the license (RS-7, EN-5, A-8). Braiders now organized in the open defend the exemption. | The contest over the license that would have continued with it in force (WE-003 C-8): schools and licensees defending it, braiders seeking an exemption. | None (RS-7, repeal clause) | **ambiguous** for each class. Each lobbied in both worlds; the exemption changes what each lobbies for. |

### Metamorphic check against WE-003

"Reverses" means the expected sign under the exemption is the opposite of WE-003's. "Partly reverses" means the sign reverses for what happens from now on, but not for a change the license already caused. **Persistence** (TS-6; `02_ontology.md`, 2.5) is how much of WE-003's effect remains after the exemption, compared with a Westmark that never licensed braiding: none, partial or full. It is "partial" or "full" where the effect ran through exit from the trade and the loss of skills and clients that cost something to rebuild, or through a cost already sunk; "none" where a flow simply stops; "n/a" where there is nothing to compare. It may be given per horizon (`02_ontology.md`, 2.5): where fewer former braiders return than left, but free entry (A-3) can make up the gap, it is "partial (medium); none (long)". The same values are recorded on each consequence in the consequence list.

| WE-003 ID | Actor class, variable | Sign in WE-003 | Expected sign under the exemption (this example) | Reverses? | Persistence (TS-6) | Reason |
|---|---|---|---|---|---|---|
| C-1 | braiders (legal market), `share_of_sellers_licensed` | increase | decrease (C-1) | Reverses | none | Licensed braiders keep their licenses; the share falls as unlicensed braiders join the legal market. |
| C-2 | braiders, `number_of_sellers` (legal), `entry_rate` | decrease | increase (C-3, C-4) | Partly reverses | partial (medium); none (long) | Informal braiders become legal at once, and new entry resumes. Former braiders return only in part: skills have decayed, clients have dispersed, and some have built careers elsewhere (C-7; TS-6, A-15). New entrants can fill the gap over time (A-3). |
| C-3 | braiders in training, `compliance_cost` | increase | decrease for those still in training (C-5); no change for those who finished | Partly reverses | full for training already completed | Hours and tuition already spent are sunk, are not refunded (R1), and appear in both the exemption and the counterfactual. |
| C-4 | `braiders.current`, `employment` (paid braiding, legal and informal) | decrease | `employment` in braiding of former braiders increase (C-7); entry (C-4) | Partly reverses | partial | Returning is a choice, so those who return expect to gain (LW-5). Those whose skills or alternatives have changed too much stay where they are (TS-6, A-15). |
| C-5 | braiders, `informal_activity` | increase | decrease (C-2) | Reverses | none | Nothing is left to evade. Some braiders may stay out of sight for reasons that have nothing to do with the license, such as taxes, but that is part of the counterfactual too. |
| C-6 | `schools.cosmetology`, `quantity_demanded` | increase | decrease (C-6) | Reverses | none | From the announcement. Schools' capacity is mostly general cosmetology capacity, which they keep using for other students. Instructors' employment or hours fall with enrollment (C-28), which WE-003 did not record. |
| C-7 (retired) | braiders, timing around the deadline (now a path note in WE-003's section 8) | — | — | Not compared | n/a | Without the license there is no deadline, so there is no counterfactual timing to reverse. Under the 2.5 timing convention this is a path note, not a consequence. |
| C-8 | schools, licensees, braiders, `lobbying_effort` | increase | ambiguous (C-9) | Does not reverse | n/a | RS-7, repeal clause: each class lobbied in both worlds. The license created a group with sunk costs and a stake in restoring it: licensed braiders and the schools that trained them. |
| C-9 | `customers.braiding`, `price_paid` | increase | decrease (C-11) | Reverses | partial (medium); none (long) | Fewer sellers return than left in the medium run; free entry closes the gap in the long run. |
| C-10 | licensed braiders, `net_price_received` | increase | decrease (C-12) | Reverses | none (price); full for the sunk training | |
| C-11 | `customers.braiding`, `quantity_substitute` (home braiding) | increase | decrease (C-13) | Reverses | none | |
| C-12 | `customers.braiding`, `search_cost` | increase | decrease (C-14) | Reverses | none | |
| C-17 | `customers.braiding`, `quality_information` | decrease | increase (C-20) | Reverses | none | |
| C-19 | `customers.braiding`, `disputes_settled_outside_courts` | increase | decrease (C-25) | Reverses | none | RS-10 reverse clause. |
| C-13 | `customers.braiding`, `quality_per_unit` | not reported | not reported (C-15) | Consistent | n/a | Both rest on the same premise below the cut-off (WE-003 A-7, here A-16); the training chain is inactive in both (A-5, A-10). |
| C-15 | customers and braiders, `quantity_traded` (legal services) | decrease | increase (C-17) | Reverses | partial (medium); none (long) | New entrants (A-3) can take the place of former braiders who do not return. |
| C-16 | `taxpayers`, `resources_available_other_uses` | decrease | increase (C-19) | Reverses | none | If the board's budget falls with its workload (A-12). |
| C-18 | `businesses.braiding`, `employment` (unlicensed braiders in shops) | decrease | `employment`, `hours_worked` at_least_one_increase (C-24) | Reverses | none | Shops may again employ braiders without a license. |
| C-20 | `customers.braiding` (legal), `resources_available_other_uses` | decrease | increase (C-30) | Reverses | partial (medium); none (long) | Follows the price (C-11). |
| C-21 | `officials.enforcement`, `enforcement_cost` | increase | decrease (C-18) | Reverses | none | |
| — | licensed braiders, `earnings` | ambiguous (DM-3) | decrease (C-16) | Does not reverse | full for the sunk training | Under the license, a one-time training cost was set against a later stream of gains, so the sign was ambiguous by design. Under the exemption, the cost is sunk in both the exemption and the counterfactual; only the lost stream of gains remains, so the sign is a decrease. |

Consequences with no counterpart in WE-003: C-8 (licensed braiders shift to other licensed services), C-10 (investment by braiders coming into the open), C-21 (`quality_variability`, which WE-003 did not record), C-22 (pending fines), C-23 (shops' compliance cost), C-26 and C-27 (other cosmetology services), C-28 (instructors) and C-29 (license fees).

## 8. Time structure

- **Announcement window (about nine months).** Enrollment by would-be braiders stops (C-6). Braiders midway through training weigh whether to finish (C-5). Informal braiders have no reason to enroll and wait for the exemption.
- **Effective date.** Informal braiders come into the open at once (C-2, C-3), because braiding needs almost no capital and their skills are in use. Prices for legal braiding fall quickly (C-11), and search costs fall as braiders advertise (C-14); customers can judge braiders by reviews and reputation as these build up (C-20), while new entrants of uneven experience arrive (C-21). Pending cases are dropped (C-22).
- **Sunk costs.** The tuition and hours licensed braiders spent are gone in both the exemption and the counterfactual. The exemption removes the price premium those costs were meant to earn (C-12, C-16). This is why the ambiguous earnings sign in WE-003 becomes a decrease here, and why licensed braiders and the schools now have a stake in restoring the license (C-9).
- **Skill loss and changed alternatives.** Five years is long enough for unused braiding skills to decay and for clients to settle with other braiders. Some former braiders have built experience in other work, which raises what they would give up by returning. Their return is slower and smaller than their exit was (C-7; TS-6, A-15). Apprentices who would have learned informally from them during those five years did not, and that gap closes only as new braiders are trained.
- **Expectations of re-imposition.** Because braiding needs little capital, most responses to the exemption pay back within months and do not depend much on whether braiders expect the license to return. Only investments in premises (C-10) depend on it (TS-5, A-11). A belief that the license would return with existing braiders grandfathered would bring entry forward instead (TS-5), but A-13 is below the cut-off. This is the main difference in time structure from WE-022 and WE-023, where long-lived capital makes credibility central.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-17 | `customers.braiding`, braiders | `quantity_traded` (legal braiding services) | increase | Nothing given up; exchanges are freed. Services that customers and unlicensed braiders want to trade, and that the license prevented, now happen legally. | OC-4 in reverse |
| C-18 | `officials.enforcement` | `enforcement_cost` (braiding) | decrease | Nothing given up; inspection and prosecution of unlicensed braiding end. | OC-3 in reverse |
| C-19 | `taxpayers` | `resources_available_other_uses` | increase | Nothing given up; the part of the board's budget spent on braiding is freed, if the budget is cut accordingly (OC-3's first funding case, as in WE-003). Against it, the board loses braiders' license fees (C-29); where those fees funded braiding enforcement, the two offset within the board's budget. | OC-3, OC-1 in reverse |
| C-23 | `businesses.braiding` | `compliance_cost` | decrease | Nothing given up; license checks and the risk of fines end. | OC-2 in reverse |

The hours and tuition that braiders in training no longer have to spend are C-5, not listed again.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The license still binds: many people who would braid for pay do not hold a cosmetology license. | binding | 0.95 | Board license records against estimates of informal and former braiders. | Almost every consequence fails. |
| A-2 | A meaningful number of people braid for pay without a license and will come into the open. | enforcement | 0.8 | Complaint-driven enforcement; home-based work (WE-003 A-3). | C-2, C-3, C-11 to C-16, C-20 and C-21 weaken. |
| A-3 | The license deterred some would-be braiders, who will now enter. | binding | 0.85 | Entry before and after amendment 7; school enrollment of braiders. | C-4 weakens; C-11, C-12 weaken. |
| A-4 | Students midway through training can stop without owing the remaining tuition. | other | 0.7 | School contracts; billing per term. | C-5 not reported. |
| A-5 | Some of the schools' students enrolled only to braid legally. | other | 0.85 | Enrollment records; students' stated plans. | C-6, C-28 and C-29 not reported. |
| A-6 | Some former braiders kept enough skill and contacts, and earn little enough in their current work, that they will return within a few years. | mobility | 0.6 | Survey of former braiders; earnings in their current work. | C-7 not reported. |
| A-7 | Licensed braiders can sell cutting, coloring or chemical services, and some customers will buy them from them. | alternative_uses | 0.6 | Services licensed braiders already offer; demand in their neighborhoods. | C-8, C-26 and C-27 not reported. |
| A-8 | Schools, licensees and braiders can organize at a cost below their stake (RS-7's premise). | other | 0.8 | Their lobbying under amendment 7 (WE-003 C-8). | C-9 not reported. |
| A-9 | Home braiding by family or friends is a feasible substitute for some customers. | substitutability | 0.75 | Prevalence of home braiding (WE-003 A-4). | C-13 weakens. |
| A-10 | The required training is largely unrelated to braiding quality. | other | 0.85 | Curriculum hours by topic; exam content (WE-003 A-5). | EN-4's training chain becomes active; C-15 would be ambiguous with A-16, or a decrease without it. |
| A-11 | Braiders expect the exemption to last long enough to pay back premises and equipment (a few years). | expectations | 0.7 | Margin of the vote; strength of the school and licensee lobby. | C-10 not reported. |
| A-12 | The board's budget falls with its braiding workload rather than being redirected to other work. | revenue_use | 0.6 | Budget process for the board; share of the budget from license fees. | C-19 not reported. |
| A-13 | Braiders expect the license to return, with those then practicing grandfathered. | expectations | 0.25 | Legislative history; how the board's earlier rules treated existing practitioners. | Below cut-off; not reported. |
| A-14 | Braiders who moved to neighboring states return on a meaningful scale. | mobility | 0.2 | WE-003 A-6 (little relocation in the first place). | Below cut-off; not reported. |
| A-16 | What customers leave when they return to open paid braiding (home braiding by family and friends, hidden informal braiders) is of lower quality than the open paid braiding they return to. | other | 0.45 | The mirror of WE-003 A-7: informal braiders are largely the same people who braid openly; home braiding is used mainly for simpler styles. | Below cut-off: C-15 not reported. If above, C-15 is an increase. |
| A-15 | For many former braiders, returning costs more than the restored return: skills unused for five years have decayed, clients have settled with other braiders, and experience built in other work raises what they would give up. | reversal_cost | 0.75 | Survey of former braiders; how long they have been away; earnings in their current work. | Former braiders return more fully; the WE-003 C-2 and C-4 rows of the metamorphic check would show persistence none. |

## 11. Report

**The policy.** Five years after Westmark began requiring a full cosmetology license to braid hair for pay, it removes braiding from the license requirement. Anyone may braid for pay, or employ braiders, without a license. Existing licenses stay valid; tuition is not refunded; enforcement against unlicensed braiding ends.

**Visible consequences.** Legal braiders no longer need to be licensed (C-1), and braiders who were working outside the law can work openly (C-2).

**Invisible consequences.**
- *Customers* pay less for legal braiding (C-11), turn less often to family and friends or go without (C-13), find braiders more easily (C-14), can judge a braider's quality better before buying, through reviews, advertising and legal recourse (C-20), settle fewer disputes outside the courts (C-25), and have more left for other things if they keep buying legal braiding (C-30).
- *Braiders* who were working informally come into the open (C-3), and more people take up braiding (C-4). Some who left the trade return, but not all: five years away has eroded skills and client lists, and some have built careers elsewhere (C-7). Braiders midway through training can stop (C-5). Those who came into the open invest in premises and equipment, to the extent they expect the exemption to last (C-10).
- *Licensed braiders* receive lower prices for braiding (C-12) and earn less overall (C-16); their tuition and hours are already spent and cannot be recovered. Some shift toward services their license still reserves to them (C-8).
- *Shops* may employ braiders without a license, no longer check licenses or risk fines, and employ more braiders or hours (C-23, C-24). *Buyers of cutting, coloring and chemical services* pay less as licensed braiders move into them, and incumbent sellers of those services receive less (C-26, C-27).
- *Cosmetology schools* lose students who enrolled only to braid (C-6), and employ fewer instructors or hours (C-28). Schools and licensed braiders now have a stake in restoring the license (C-9). Braiders with pending cases do not pay the fines (C-22); the board loses braiders' license fees (C-29).
- *Taxpayers* save the cost of braiding enforcement, if the board's budget is cut accordingly (C-18, C-19).

**Ambiguous effects.** Whether any class's lobbying rises or falls: each lobbied with the license in force, and the exemption changes what each lobbies for (C-9). Whether the spread of quality between braiders narrows (better information) or widens (inexperienced entrants) (C-21).

**Not determined.** Whether the quality of braiding customers receive changes (C-15): the training was largely unrelated to braiding (A-10), and whether home and hidden braiding was worse than open paid braiding is not established (A-16, p = 0.45), as in WE-003.

**What does not reverse.** The training cost licensed braiders paid is not returned, which turns WE-003's ambiguous result for their earnings into a decrease. Former braiders return only in part. The group with a stake in the license, schools and licensed braiders, remains and now seeks to restore it.

**Key conditions.** That many people would braid without a license (A-1, p = 0.95) and that a meaningful informal trade exists to come into the open (A-2, p = 0.8) drive most of the results. That the training is unrelated to braiding (A-10, p = 0.85) means that removing it does not lower quality; whether quality rises is not determined.

**What this analysis cannot say.** How many braiders will enter or return, or how much prices will fall; health and safety effects of unlicensed braiding (out of scope for version 1); whether gains to customers and new braiders outweigh losses to licensed braiders and schools; whether the exemption is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
|---|---|---|---|---|---|---|---|---|---|
| C-1 | braiders (legal market) | share_of_sellers_licensed | decrease | short | visible | B | EN-1 in reverse | A-1 | none |
| C-2 | braiders.informal | informal_activity | decrease | short | visible | B | RS-3, EN-3 in reverse | A-2 | none |
| C-3 | braiders | number_of_sellers (legal) | increase | short | invisible | B | EN-1 in reverse | A-2 | partial (medium); none (long) |
| C-4 | braiders.prospective | entry_rate | increase | short–medium | invisible | B | EN-1 in reverse | A-3 | none |
| C-5 | braiders.in_training | compliance_cost | decrease | short | invisible | B | OC-2 in reverse | A-4 | full for training already completed |
| C-6 | schools.cosmetology | quantity_demanded | decrease | short | invisible | B | EN-1 in reverse, RS-8 | A-5 | none |
| C-7 | braiders.former | employment (in braiding) | increase | medium | invisible | B | EN-3 in reverse, TS-6 | A-6, A-15 | partial (A-15) |
| C-8 | braiders.licensed | quantity_supplied (licensed-only services) | increase | medium | invisible | B | LW-4, RS-6 | A-7 | n/a (no counterpart) |
| C-9 | schools, licensees, braiders | lobbying_effort | ambiguous | medium | invisible | B | RS-7 (repeal clause), EN-5 | A-8 | n/a |
| C-10 | braiders (formerly informal) | investment_target (premises, equipment) | increase | medium | invisible | B | RS-6 in reverse, LW-4, TS-5 | A-2, A-11 | n/a (no counterpart) |
| C-11 | customers.braiding | price_paid (legal braiding) | decrease | short–medium | invisible | B | EN-1 in reverse | A-2, A-3 | partial (medium); none (long) |
| C-12 | braiders.licensed, cosmetologists.licensed who braid | net_price_received (braiding) | decrease | short–medium | invisible | B | EN-2 in reverse | A-2, A-3 | none |
| C-13 | customers.braiding | quantity_substitute (home braiding) | decrease | short | invisible | B | EN-3, RS-1 in reverse | A-9 | none |
| C-14 | customers.braiding | search_cost | decrease | short | invisible | B | RS-10 in reverse | A-2 | none |
| C-16 | braiders.licensed | earnings | decrease | medium | invisible | B | EN-2 in reverse, LW-2 | A-2, A-3 | full for the sunk training |
| C-17 | customers, braiders | quantity_traded (legal services) | increase | short–medium | invisible | B | OC-4 in reverse | A-2, A-3 | partial (medium); none (long) |
| C-18 | officials.enforcement | enforcement_cost (braiding) | decrease | short | invisible | A | OC-3 in reverse | none | none |
| C-19 | taxpayers | resources_available_other_uses | increase | short | invisible | B | OC-3, OC-1 in reverse | A-12 | none |
| C-20 | customers.braiding | quality_information | increase | short–medium | invisible | B | RS-10 (reverse clause) | A-2 | none |
| C-21 | customers.braiding | quality_variability | ambiguous | medium | invisible | B | RS-10 (reverse clause); CR-12b | A-2, A-3 | n/a (no counterpart) |
| C-22 | braiders.with_pending_cases | resources_available_other_uses | increase | short | invisible | A | CR-1, CR-8 | none | n/a (transition) |
| C-23 | businesses.braiding | compliance_cost | decrease | short | invisible | B | OC-2 in reverse | A-1 | none |
| C-24 | businesses.braiding | employment, hours_worked (braiders in shops) | at_least_one_increase | medium | invisible | B | EN-1 in reverse, CR-4, CR-9 | A-1, A-3 | none |
| C-25 | customers.braiding | disputes_settled_outside_courts | decrease | short–medium | invisible | B | RS-10 (reverse clause) | A-2 | none |
| C-26 | buyers.cosmetology_other | price_paid (cutting, coloring, chemical services) | decrease | medium | invisible | B | RS-13 | A-7 | n/a (no counterpart) |
| C-27 | sellers.cosmetology_other | net_price_received | decrease | medium | invisible | B | RS-13 | A-7 | n/a (no counterpart) |
| C-28 | schools.cosmetology (instructors) | employment, hours_worked | at_least_one_decrease | medium | invisible | B | CR-9, RS-6 | A-5 | n/a (no counterpart) |
| C-29 | officials.enforcement (board) | tax_revenue (license fees from braiders) | decrease | medium–long | invisible | B | CR-1, CR-8 | A-5 | n/a (no counterpart) |
| C-30 | customers.braiding (legal market) | resources_available_other_uses | increase | short–medium | invisible | B | EN-1 in reverse, CR-8 | A-2, A-3 | partial (medium); none (long) |

C-15 (`quality_per_unit` received) is not reported: it needs A-16 (p = 0.45). See section 7.

## Gaps found

- GAP-024-1 (closed in catalog 0.3: TS-6, assumption type `reversal_cost`, `persistence` field). Re-entry after skill loss. C-7 now Tier B (EN-3 in reverse, TS-6; A-6 and the new A-15, `reversal_cost`); persistence recorded in the metamorphic check, where the WE-003 C-2 and C-4 rows are no longer Tier C.
- GAP-024-2 (closed in catalog 0.3: TS-5, including its grandfathering clause). Expectations of re-imposition. C-10 now Tier B on A-11 (p = 0.7); the grandfathering rush cites TS-5 and stays unreported (A-13, p = 0.25).
- GAP-024-3 (closed in catalog 0.3: `quality_information`, `quality_variability`, named in RS-10 with a reverse clause). No variable for how well buyers can judge quality. New consequences C-20 and C-21.
- GAP-024-4 (closed in catalog 0.3: timing convention in 2.5; WE-003 C-7 moved to section 8). Timing shifts have no signed form. WE-003 records its RS-8 response (C-7) with the sign "(shift)", which is not a valid sign in normal form, and leaves it out of its consequence list, so the metamorphic check can compare it only "in kind". WE-022 (C-12) and WE-023 (C-11) already write their RS-8 responses as a signed change in a named window. *Proposed fix:* in workflow step 5 and `02_ontology.md` 2.5, require each RS-8 response to be written as signed consequences per window, as SB-6 and DM-5 do (here: `entry_rate` and `quantity_demanded` for school places increase just before the deadline and decrease after it, compared with the counterfactual), and amend WE-003 C-7 accordingly.
- Catalog 0.5: corrected after the core-only comparison (see ../05_examples_core/WE-024_braiding_license_repeal_core.md): `quality_variability` (C-21) made ambiguous under RS-10's revised reverse clause (untrained entrants are admitted); quality received (C-15) no longer reported, mirroring WE-003 as corrected (DM-2 0.5; new premise A-16, p 0.45); lobbying kept ambiguous under RS-7's repeal clause, with braiders added to its premise (A-8); added pending fines (C-22), shops' compliance cost and braider employment or hours (C-23, C-24), disputes outside courts (C-25, RS-10's own variable), other cosmetology services (C-26, C-27, RS-13), instructors (C-28), license fees (C-29) and customers' means (C-30); persistence recorded on every consequence, per horizon for price, quantity and sellers; metamorphic check rebuilt against WE-003 as corrected for catalog 0.5. Not adopted from the core version: its braiding-supplies increase (the comparison found it drops the home-braiding chain).
