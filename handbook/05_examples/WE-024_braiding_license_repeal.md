# WE-024 Abolition of the braiding license requirement

Analyst: draft (Handbook 0.3)  |  Rule catalog version: 0.3  |  Status: awaiting expert review

A stylized repeal of the licensing rule analyzed in WE-003, in the same fictional state, five years after it took effect. It doubles as a metamorphic check: the analysis of the abolition should reverse the signs of WE-003, except where the license caused lasting changes. The check is at the end of section 7. The counterfactual throughout is **the license requirement stays in force**; every sign is relative to that, not to the situation before the abolition and not to a Westmark that never licensed braiding. "In reverse" after a rule ID means the rule is applied to the removal of its precondition; where that direction is not obviously valid, the text says so. Catalog 0.3 states some directions explicitly: RS-10 has a reverse clause for trade returning to the legal market, and TS-5 and TS-6 are written for repeals (see "Analyzing a repeal" in the workflow). The probabilities are illustrative.

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
| `officials.enforcement`, `taxpayers` | Board of Cosmetology and its funders | Braiding enforcement ends. |

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
| C-9 | `schools.cosmetology`, `braiders.licensed`, `cosmetologists.licensed`, braiders | `lobbying_effort` | ambiguous (see section 7) | medium | RS-7, EN-5 | A-8 |
| C-10 | braiders formerly working informally | `investment_target` (premises, chairs, signage) | increase | medium | RS-6 in reverse, LW-4, TS-5 | A-2, A-11 |

C-3 is fast because almost nothing has to be built: informal braiders already have the skill, the tools and the customers, and need only to stop hiding.

C-6 starts at the announcement (RS-8, "delay until after a repeal is expected"): would-be braiders stop enrolling once the exemption is expected.

C-7 is Tier B in catalog 0.3 (Tier C in the 0.2 draft). EN-3 says that sellers excluded by a license move to their next-best occupation. Applied in reverse it would say they move back once the license goes, but TS-6 limits that five years on: skills unused for five years decay, clients have found other braiders, and some former braiders have built experience in their new work, which raises what they would give up by returning (A-15, `reversal_cost`). Former braiders return only where the restored return exceeds that cost. The sign is an increase, because some will return (A-6); how many, the method cannot say. Persistence against a Westmark that never licensed braiding is partial (metamorphic check, WE-003 C-2 and C-4).

C-8: with the braiding premium gone, licensed braiders shift some of their time to the services their license still reserves to them (LW-4). Their training, sunk in both the repeal and the counterfactual, now earns its return there or not at all.

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
| C-15 | `customers.braiding` | `quality_per_unit` received | increase (see section 7) | medium | EN-4 in reverse, DM-2 | | A-2, A-10 |
| C-16 | `braiders.licensed` | `earnings` | decrease (see section 7) | medium | EN-2 in reverse, LW-2 | | A-2, A-3 |
| C-20 | `customers.braiding` | `quality_information` | increase | short to medium | RS-10 (reverse clause) | | A-2 |
| C-21 | `customers.braiding` | `quality_variability` | decrease | medium | RS-10 (reverse clause) | | A-2 |

C-14, C-20 and C-21 apply RS-10's reverse clause: braiders who come into the open can advertise, collect public reviews and be taken to court, so customers find them more easily (C-14) and can judge their quality before buying (C-20), and the spread of quality between braiders they might use narrows (C-21). Licensed braiders can still advertise their license as a voluntary signal. C-21 is about the spread of quality, C-15 about its level; they are separate consequences.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `customers.braiding`, `quality_per_unit` received, medium | Customers move back from home braiding and hidden informal providers to an open legal market with reviews and recourse (C-13, C-14, C-20; EN-3 in reverse, RS-10 reverse clause). | Legal providers are no longer all trained to the license standard (EN-4's "up" chain removed). | DM-2: the training is largely unrelated to braiding (A-10, p = 0.85), so removing it takes little away. | **increase**. The mirror of WE-003's C-13, with the same dominance judgment. If the training were related to braiding quality, the sign would be **ambiguous**. |
| `braiders.licensed`, `earnings`, medium | They may shift time to services their license reserves (C-8). But that option was open to them in the counterfactual too; that they braided instead shows they ranked braiding higher (LW-2). | The price of braiding falls (C-12), and they face more legal competitors (C-3). | None needed | **decrease**. The tuition and the 1,500 hours were spent before the exemption and are spent in the counterfactual as well, so they are not a consequence of the exemption. DM-3 does not apply, because only the stream of gains is in the comparison. |
| `schools.cosmetology`, `braiders.licensed`, `cosmetologists.licensed`, braiders, `lobbying_effort`, medium | Schools and licensed braiders, who paid a large sunk cost for an advantage the exemption removes, now have a concentrated stake in restoring the license (RS-7, EN-5, A-8). Braiders now organized in the open defend the exemption. | The contest over the license that would have continued with it in force (WE-003 C-8) ends in its old form. | None | **ambiguous**. The exemption changes who lobbies for what; the method cannot say whether total effort rises or falls. |

### Metamorphic check against WE-003

"Reverses" means the expected sign under the exemption is the opposite of WE-003's. "Partly reverses" means the sign reverses for what happens from now on, but not for a change the license already caused. **Persistence** (TS-6; `02_ontology.md`, 2.5) is how much of WE-003's effect remains after the exemption, compared with a Westmark that never licensed braiding: none, partial or full. It is filled in where TS-6 applies, that is, where the effect ran through exit from the trade and the loss of skills and clients that cost something to rebuild; "—" means TS-6 does not apply (a flow that simply stops, a sunk cost borne in both paths, or a change in who acts).

| WE-003 ID | Actor class, variable | Sign in WE-003 | Expected sign under the exemption (this example) | Reverses? | Persistence (TS-6) | Reason |
|---|---|---|---|---|---|---|
| C-1 | braiders (legal market), `share_of_sellers_licensed` | increase | decrease (C-1) | Reverses | — | Licensed braiders keep their licenses; the share falls as unlicensed braiders join the legal market. |
| C-2 | braiders, `number_of_sellers` (legal), `entry_rate` | decrease | increase (C-3, C-4) | Partly reverses | partial | Informal braiders become legal at once, and new entry resumes. Former braiders return only in part: skills have decayed, clients have dispersed, and some have built careers elsewhere (C-7; TS-6, A-15). |
| C-3 | braiders in training, `compliance_cost` | increase | decrease for those still in training (C-5); no change for those who finished | Partly reverses | — | Hours and tuition already spent are sunk, are not refunded (R1), and appear in both the exemption and the counterfactual. |
| C-4 | braiders who left, `earnings` | decrease | no separate consequence; `employment` in braiding of former braiders increase (C-7) | Partly reverses | partial | Returning is a choice, so those who return expect to gain (LW-5); their money earnings are not listed as a consequence. Those whose skills or alternatives have changed too much stay where they are; for them the exemption changes nothing (TS-6, A-15). |
| C-5 | braiders, `informal_activity` | increase | decrease (C-2) | Reverses | — | Nothing is left to evade. Some braiders may stay out of sight for reasons that have nothing to do with the license, such as taxes, but that is part of the counterfactual too. |
| C-6 | `schools.cosmetology`, `quantity_demanded` | increase | decrease (C-6) | Reverses | — | From the announcement. Schools' capacity is mostly general cosmetology capacity, which they keep using for other students. |
| C-7 | braiders, timing around the deadline (section 5 only; not in WE-003's consequence list) | shift (rush to enroll or exit) | shift (enrollment stops at the announcement, C-6) | Reverses in kind | — | RS-8 in both cases; the action moves to the favorable time. See GAP-024-4. |
| C-8 | schools, licensees, braiders, `lobbying_effort` | increase | ambiguous (C-9) | Does not reverse | — | The license created a group with sunk costs and a stake in restoring it: licensed braiders and the schools that trained them. |
| C-9 | `customers.braiding`, `price_paid` | increase | decrease (C-11) | Reverses | — | |
| C-10 | licensed braiders, `net_price_received` | increase | decrease (C-12) | Reverses | — | |
| C-11 | `customers.braiding`, `quantity_substitute` (home braiding) | increase | decrease (C-13) | Reverses | — | |
| C-12 | `customers.braiding`, `search_cost` | increase | decrease (C-14) | Reverses | — | |
| C-13 | `customers.braiding`, `quality_per_unit` | decrease | increase (C-15) | Reverses | — | Same dominance judgment (DM-2, A-10). |
| C-15 | customers and braiders, `quantity_traded` (legal services) | decrease | increase (C-17) | Reverses | — | New entrants (A-3) can take the place of former braiders who do not return. |
| C-16 | `taxpayers`, `resources_available_other_uses` | decrease | increase (C-19) | Reverses | — | If the board's budget falls with its workload (A-12). |
| — | licensed braiders, `earnings` | ambiguous (DM-3) | decrease (C-16) | Does not reverse | — | Under the license, a one-time training cost was set against a later stream of gains, so the sign was ambiguous by design. Under the exemption, the cost is sunk in both the exemption and the counterfactual; only the lost stream of gains remains, so the sign is a decrease. |

Consequences with no counterpart in WE-003: C-8 (licensed braiders shift to other licensed services), C-10 (investment by braiders coming into the open), C-18 (board enforcement cost, recorded only through taxpayers in WE-003), C-20 and C-21 (`quality_information` and `quality_variability`, which WE-003 did not record; their mirror under the license follows from RS-10).

## 8. Time structure

- **Announcement window (about nine months).** Enrollment by would-be braiders stops (C-6). Braiders midway through training weigh whether to finish (C-5). Informal braiders have no reason to enroll and wait for the exemption.
- **Effective date.** Informal braiders come into the open at once (C-2, C-3), because braiding needs almost no capital and their skills are in use. Prices for legal braiding fall quickly (C-11), and search costs fall as braiders advertise (C-14); customers can judge braiders by reviews and reputation as these build up (C-20, C-21).
- **Sunk costs.** The tuition and hours licensed braiders spent are gone in both the exemption and the counterfactual. The exemption removes the price premium those costs were meant to earn (C-12, C-16). This is why the ambiguous earnings sign in WE-003 becomes a decrease here, and why licensed braiders and the schools now have a stake in restoring the license (C-9).
- **Skill loss and changed alternatives.** Five years is long enough for unused braiding skills to decay and for clients to settle with other braiders. Some former braiders have built experience in other work, which raises what they would give up by returning. Their return is slower and smaller than their exit was (C-7; TS-6, A-15). Apprentices who would have learned informally from them during those five years did not, and that gap closes only as new braiders are trained.
- **Expectations of re-imposition.** Because braiding needs little capital, most responses to the exemption pay back within months and do not depend much on whether braiders expect the license to return. Only investments in premises (C-10) depend on it (TS-5, A-11). A belief that the license would return with existing braiders grandfathered would bring entry forward instead (TS-5), but A-13 is below the cut-off. This is the main difference in time structure from WE-022 and WE-023, where long-lived capital makes credibility central.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-17 | `customers.braiding`, braiders | `quantity_traded` (legal braiding services) | increase | Nothing given up; exchanges are freed. Services that customers and unlicensed braiders want to trade, and that the license prevented, now happen legally. | OC-4 in reverse |
| C-18 | `officials.enforcement` | `enforcement_cost` (braiding) | decrease | Nothing given up; inspection and prosecution of unlicensed braiding end. | OC-3 in reverse |
| C-19 | `taxpayers` | `resources_available_other_uses` | increase | Nothing given up; the part of the board's budget spent on braiding is freed, if the budget is cut accordingly. | OC-3, OC-1 in reverse |

The hours and tuition that braiders in training no longer have to spend are C-5, not listed again.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The license still binds: many people who would braid for pay do not hold a cosmetology license. | binding | 0.95 | Board license records against estimates of informal and former braiders. | Almost every consequence fails. |
| A-2 | A meaningful number of people braid for pay without a license and will come into the open. | enforcement | 0.8 | Complaint-driven enforcement; home-based work (WE-003 A-3). | C-2, C-3, C-11 to C-16, C-20 and C-21 weaken. |
| A-3 | The license deterred some would-be braiders, who will now enter. | binding | 0.85 | Entry before and after amendment 7; school enrollment of braiders. | C-4 weakens; C-11, C-12 weaken. |
| A-4 | Students midway through training can stop without owing the remaining tuition. | other | 0.7 | School contracts; billing per term. | C-5 not reported. |
| A-5 | Some of the schools' students enrolled only to braid legally. | other | 0.85 | Enrollment records; students' stated plans. | C-6 not reported. |
| A-6 | Some former braiders kept enough skill and contacts, and earn little enough in their current work, that they will return within a few years. | mobility | 0.6 | Survey of former braiders; earnings in their current work. | C-7 not reported. |
| A-7 | Licensed braiders can sell cutting, coloring or chemical services, and some customers will buy them from them. | alternative_uses | 0.6 | Services licensed braiders already offer; demand in their neighborhoods. | C-8 not reported. |
| A-8 | Schools and licensees can organize at a cost below their stake. | other | 0.8 | Their lobbying under amendment 7 (WE-003 C-8). | C-9 not reported. |
| A-9 | Home braiding by family or friends is a feasible substitute for some customers. | substitutability | 0.75 | Prevalence of home braiding (WE-003 A-4). | C-13 weakens. |
| A-10 | The required training is largely unrelated to braiding quality. | other | 0.85 | Curriculum hours by topic; exam content (WE-003 A-5). | C-15 becomes ambiguous. |
| A-11 | Braiders expect the exemption to last long enough to pay back premises and equipment (a few years). | expectations | 0.7 | Margin of the vote; strength of the school and licensee lobby. | C-10 not reported. |
| A-12 | The board's budget falls with its braiding workload rather than being redirected to other work. | revenue_use | 0.6 | Budget process for the board; share of the budget from license fees. | C-19 not reported. |
| A-13 | Braiders expect the license to return, with those then practicing grandfathered. | expectations | 0.25 | Legislative history; how the board's earlier rules treated existing practitioners. | Below cut-off; not reported. |
| A-14 | Braiders who moved to neighboring states return on a meaningful scale. | mobility | 0.2 | WE-003 A-6 (little relocation in the first place). | Below cut-off; not reported. |
| A-15 | For many former braiders, returning costs more than the restored return: skills unused for five years have decayed, clients have settled with other braiders, and experience built in other work raises what they would give up. | reversal_cost | 0.75 | Survey of former braiders; how long they have been away; earnings in their current work. | Former braiders return more fully; the WE-003 C-2 and C-4 rows of the metamorphic check would show persistence none. |

## 11. Report

**The policy.** Five years after Westmark began requiring a full cosmetology license to braid hair for pay, it removes braiding from the license requirement. Anyone may braid for pay, or employ braiders, without a license. Existing licenses stay valid; tuition is not refunded; enforcement against unlicensed braiding ends.

**Visible consequences.** Legal braiders no longer need to be licensed (C-1), and braiders who were working outside the law can work openly (C-2).

**Invisible consequences.**
- *Customers* pay less for legal braiding (C-11), turn less often to family and friends or go without (C-13), find braiders more easily (C-14), can judge a braider's quality better before buying, through reviews, advertising and legal recourse (C-20), meet less variation in quality between braiders (C-21), and receive higher-quality braiding overall (C-15), because the training the license required was largely unrelated to braiding.
- *Braiders* who were working informally come into the open (C-3), and more people take up braiding (C-4). Some who left the trade return, but not all: five years away has eroded skills and client lists, and some have built careers elsewhere (C-7). Braiders midway through training can stop (C-5). Those who came into the open invest in premises and equipment, to the extent they expect the exemption to last (C-10).
- *Licensed braiders* receive lower prices for braiding (C-12) and earn less overall (C-16); their tuition and hours are already spent and cannot be recovered. Some shift toward services their license still reserves to them (C-8).
- *Cosmetology schools* lose students who enrolled only to braid (C-6). Schools and licensed braiders now have a stake in restoring the license (C-9).
- *Taxpayers* save the cost of braiding enforcement, if the board's budget is cut accordingly (C-18, C-19).

**Ambiguous effects.** Whether total lobbying effort rises or falls: the exemption changes who lobbies for what (C-9).

**What does not reverse.** The training cost licensed braiders paid is not returned, which turns WE-003's ambiguous result for their earnings into a decrease. Former braiders return only in part. The group with a stake in the license, schools and licensed braiders, remains and now seeks to restore it.

**Key conditions.** That many people would braid without a license (A-1, p = 0.95) and that a meaningful informal trade exists to come into the open (A-2, p = 0.8) drive most of the results. That the training is unrelated to braiding (A-10, p = 0.85) is what makes the quality result an increase rather than ambiguous.

**What this analysis cannot say.** How many braiders will enter or return, or how much prices will fall; health and safety effects of unlicensed braiding (out of scope for version 1); whether gains to customers and new braiders outweigh losses to licensed braiders and schools; whether the exemption is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | braiders (legal market) | share_of_sellers_licensed | decrease | short | visible | B | EN-1 in reverse | A-1 |
| C-2 | braiders.informal | informal_activity | decrease | short | visible | B | RS-3, EN-3 in reverse | A-2 |
| C-3 | braiders | number_of_sellers (legal) | increase | short | invisible | B | EN-1 in reverse | A-2 |
| C-4 | braiders.prospective | entry_rate | increase | short–medium | invisible | B | EN-1 in reverse | A-3 |
| C-5 | braiders.in_training | compliance_cost | decrease | short | invisible | B | OC-2 in reverse | A-4 |
| C-6 | schools.cosmetology | quantity_demanded | decrease | short | invisible | B | EN-1 in reverse, RS-8 | A-5 |
| C-7 | braiders.former | employment (in braiding) | increase | medium | invisible | B | EN-3 in reverse, TS-6 | A-6, A-15 |
| C-8 | braiders.licensed | quantity_supplied (licensed-only services) | increase | medium | invisible | B | LW-4, RS-6 | A-7 |
| C-9 | schools, licensees, braiders | lobbying_effort | ambiguous | medium | invisible | B | RS-7, EN-5 | A-8 |
| C-10 | braiders (formerly informal) | investment_target (premises, equipment) | increase | medium | invisible | B | RS-6 in reverse, LW-4, TS-5 | A-2, A-11 |
| C-11 | customers.braiding | price_paid (legal braiding) | decrease | short–medium | invisible | B | EN-1 in reverse | A-2, A-3 |
| C-12 | braiders.licensed, cosmetologists.licensed who braid | net_price_received (braiding) | decrease | short–medium | invisible | B | EN-2 in reverse | A-2, A-3 |
| C-13 | customers.braiding | quantity_substitute (home braiding) | decrease | short | invisible | B | EN-3, RS-1 in reverse | A-9 |
| C-14 | customers.braiding | search_cost | decrease | short | invisible | B | RS-10 in reverse | A-2 |
| C-15 | customers.braiding | quality_per_unit | increase | medium | invisible | B | EN-4 in reverse, DM-2 | A-2, A-10 |
| C-16 | braiders.licensed | earnings | decrease | medium | invisible | B | EN-2 in reverse, LW-2 | A-2, A-3 |
| C-17 | customers, braiders | quantity_traded (legal services) | increase | short–medium | invisible | B | OC-4 in reverse | A-2, A-3 |
| C-18 | officials.enforcement | enforcement_cost (braiding) | decrease | short | invisible | A | OC-3 in reverse | none |
| C-19 | taxpayers | resources_available_other_uses | increase | short | invisible | B | OC-3, OC-1 in reverse | A-12 |
| C-20 | customers.braiding | quality_information | increase | short–medium | invisible | B | RS-10 (reverse clause) | A-2 |
| C-21 | customers.braiding | quality_variability | decrease | medium | invisible | B | RS-10 (reverse clause) | A-2 |

## Gaps found

- GAP-024-1 (closed in catalog 0.3: TS-6, assumption type `reversal_cost`, `persistence` field). Re-entry after skill loss. C-7 now Tier B (EN-3 in reverse, TS-6; A-6 and the new A-15, `reversal_cost`); persistence recorded in the metamorphic check, where the WE-003 C-2 and C-4 rows are no longer Tier C.
- GAP-024-2 (closed in catalog 0.3: TS-5, including its grandfathering clause). Expectations of re-imposition. C-10 now Tier B on A-11 (p = 0.7); the grandfathering rush cites TS-5 and stays unreported (A-13, p = 0.25).
- GAP-024-3 (closed in catalog 0.3: `quality_information`, `quality_variability`, named in RS-10 with a reverse clause). No variable for how well buyers can judge quality. New consequences C-20 and C-21.
- GAP-024-4 (open, new in this revision). Timing shifts have no signed form. WE-003 records its RS-8 response (C-7) with the sign "(shift)", which is not a valid sign in normal form, and leaves it out of its consequence list, so the metamorphic check can compare it only "in kind". WE-022 (C-12) and WE-023 (C-11) already write their RS-8 responses as a signed change in a named window. *Proposed fix:* in workflow step 5 and `02_ontology.md` 2.5, require each RS-8 response to be written as signed consequences per window, as SB-6 and DM-5 do (here: `entry_rate` and `quantity_demanded` for school places increase just before the deadline and decrease after it, compared with the counterfactual), and amend WE-003 C-7 accordingly.
