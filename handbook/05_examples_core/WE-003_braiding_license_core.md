# WE-003 / Analysis: Cosmetology license required for hair braiding (core-only re-run)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

Rule set: the core rules CR-1 to CR-12 (`../04a_core_rules.md`), AX-1 and LW-1 to LW-10 (`../01_foundations.md`), and arithmetic. No pattern is cited. New premises that the derivations needed are numbered A-N1, A-N2, ... and are listed in section 10 and under "Gaps found".

## 1. Policy record

**Westmark State Cosmetology Act, amendment 7.** Hair braiding (braids, twists and locs, with no cutting or chemicals) was previously unregulated in Westmark. About 2,000 people braid for pay, mostly self-employed, many working from home or in small shops. Two neighboring states do not license braiding; their borders are a long drive from the main cities.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 License requirement | `licensing_requirement` | Braiding hair for pay | Anyone who braids for pay, and any business that employs them | A full cosmetology license: 1,500 hours at a licensed cosmetology school (typical tuition $12,000 to $18,000) and a state exam. The curriculum covers cutting, coloring and chemical treatments; braiding is a small part or absent. | None. Existing braiders have 12 months to comply. |
| K2 Penalties and enforcement | Enforcement | K1 | State Board of Cosmetology | Fines for unlicensed practice and for businesses that employ unlicensed braiders. Inspections are complaint-driven. | None |

Unclear provisions: whether unpaid braiding for family and friends is covered. Assumed not covered (only braiding for pay is).

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
| --- | --- | --- | --- |
| K1 License requirement | triangular (prohibits paid braiding between a customer and an unlicensed braider) | Yes (A-1, p 0.95) | CR-1, CR-4, CR-5a, CR-6, CR-7, CR-9, CR-10, CR-11 |
| K2 Penalties and enforcement | triangular (penalties) and binary (fines; board costs) | Partly: complaint-driven (A-2, A-3) | CR-1, CR-4, CR-8 |

**CR-1 operations, by component and actor class.** Operation 1: removes an option; 2: adds an option; 3: changes what an option brings; 4: transfers means.

| Component | Actor class | CR-1 operations |
| --- | --- | --- |
| K1 | braiders.current (unlicensed) | 1 (legal paid braiding without a license removed after 12 months, where enforced); 3 (fine risk attached to continuing, where not enforced); 3 (tuition and 1,500 hours attached to regaining the option) |
| K1 | sellers.prospective (would-be braiders) | 3 (training cost attached to entry) |
| K1 | buyers.current (braiding customers) | 1 (buying from an unlicensed braider removed, where enforced); 3 (risk and search attached where not) |
| K1 | sellers.substitutes (licensed cosmetologists) | none directly; competitors' options change (CR-9) |
| K1 | households braiding for family and friends | U1-a: none (unpaid braiding not covered); U1-b: 1 or 3 |
| K2 | businesses employing braiders | 3 (fines attached to employing unlicensed braiders) |
| K2 | officials.enforcement (State Board of Cosmetology) | 2 (power to inspect and fine) |
| K2 | braiders.current (unlicensed, caught) | 4 (fines transferred to the state) |

## 3. Actor classes

| Actor class | Role | How its options change |
| --- | --- | --- |
| braiders.current | About 2,000 people who braid for pay, mostly self-employed, few licensed | Must license within 12 months, stop, or work illegally (K1, K2) |
| sellers.prospective | People who would have started braiding for pay | Entry now requires the full license |
| buyers.current | Customers of paid braiding | Fewer legal sellers; informal sellers harder to find |
| sellers.substitutes (licensed cosmetologists) | Licensed providers who offer or could offer braiding | Competitors removed or burdened (CR-9) |
| input_suppliers (cosmetology schools) | Sell the required training | Demand for training changes (CR-9, input_to) |
| businesses employing braiders | Shops that employ braiders | Fines for employing unlicensed braiders (K2) |
| households (home braiding) | Family and friends who braid unpaid | Substitute for paid braiding (U1-a) |
| sellers.complements (braiding hair and supplies) | Sell hair extensions and products | Use of complements changes (CR-9) |
| officials.enforcement | State Board of Cosmetology | New enforcement duty |
| neighboring_jurisdictions | Two states without braiding licenses, far from the main cities | Relocation possible but unlikely (A-6, p 0.3) |

## 4. Direct effect

CR-1 with CR-2: after 12 months, paid braiding without the license is removed as a legal option for the roughly 2,000 current braiders, few of whom hold it (A-1).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | braiders.current | number_of_sellers (legal paid braiders) | decrease | medium | CR-1 (op 1, K1) → CR-4 (x: train for the license, y: stop braiding for pay or braid illegally) → CR-4b (those for whom training costs more than braiding is worth switch) | A-1, A-2 |
| C-2 | braiders.current | compliance_cost | increase | medium | CR-1 (op 3: tuition and 1,500 hours attached to legal braiding) → CR-8c | A-1, A-N2 |
| C-19 | officials.enforcement | enforcement_cost | increase | short | CR-1 (op 2, K2) → CR-8c | A-2 |

## 5. Responses

CR-4 pairs of options examined for each actor class (substitute, adjust terms, evade, relocate, reclassify, exit, lobby, change timing, enter), with CR-6 where a price is fixed and CR-5 where an exchange is prevented or compelled.

| Actor class | Pair of options (CR-4) or rule | Result |
| --- | --- | --- |
| braiders.current | CR-4 (x: train for the license, y: stop braiding for pay) | Some train (A-N2), some stop |
| braiders.current | CR-4 (x: comply, y: braid without a license) | Some violate (A-3) |
| braiders.current | CR-4 (x: braid here, y: relocate to a neighboring state) | A-6, p 0.3: not reported |
| braiders.current | CR-4 (x: braid for pay, y: braid unpaid or for in-kind return) | Reclassification toward unpaid work: no premise in the record; not reported |
| braiders.current | CR-4 (x: accept, y: lobby) | Some lobby (A-N1) |
| braiders.current | CR-10a (12-month window: x: decide later, y: start training now or wind down) | Note in section 8 |
| sellers.prospective | CR-4 (x: stay out, y: enter) | Fewer enter |
| buyers.current | CR-4 (x: paid braiding, y: home braiding) | Some switch (A-4) |
| buyers.current | CR-4 (x: legal seller, y: informal seller) | Some buy informally (A-3) |
| buyers.current | CR-10a (x: book after the deadline, y: book before) | Needs a premise on customer expectations (A-N3, p 0.4): not reported |
| businesses employing braiders | CR-4 (x: employ unlicensed braiders, y: stop) | Fewer employed in shops |
| sellers.substitutes (licensed cosmetologists) | CR-4 mirror (x: accept repeal, y: lobby to keep) | Some lobby (A-N1) |
| buyers.current | CR-5a (exchanges with unlicensed braiders prevented) | Legal trades fall |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-3 | braiders.current | employment (paid braiding, legal and informal) | decrease | medium | C-1 → CR-4b (those at the margin leave paid braiding for other work); those who violate stay (CR-4b, the rest bear the change) | A-1, A-2 |
| C-4 | braiders.current | resources_available_other_uses | decrease | medium | C-2 → CR-3c and CR-8c (tuition and training time withdrawn from other uses); CR-3a for those who stop braiding (fall back to a lower-ranked option) | A-1, A-2 |
| C-5 | braiders.current | informal_activity | increase | medium | CR-1 (op 3 in practice: fine risk) → CR-4 (x: comply, y: braid without a license) | A-1, A-3 |
| C-6 | businesses employing braiders | employment (unlicensed braiders employed in shops) | decrease | medium | CR-1 (op 3, K2: fines for employers) → CR-4 (x: employ an unlicensed braider, y: stop) | A-1, A-2 |
| C-7 | buyers.current | price_paid (legal paid braiding) | increase | medium | C-1 → CR-6 (fewer sellers at the old price; unsatisfied buyers offer better terms) and CR-7a (new legal braiders enter only if expected earnings cover the training cost) | A-1, A-2 |
| C-8 | buyers.current | quantity_traded (legal paid braiding) | decrease | medium | CR-5a (exchanges with unlicensed braiders prevented) and C-7 → CR-4c | A-1, A-2 |
| C-9 | buyers.current | quantity_substitute (home braiding by family or friends) | U1-a: increase; U1-b: ambiguous | medium | C-7 and C-8 → CR-4 (x: paid braiding, y: home braiding) → CR-9 (substitute); under U1-b home braiding is also covered (op 1 or 3), pushing the other way, CR-12b | A-1, A-2, A-4 |
| C-10 | buyers.current | search_cost | increase | medium | C-1 → CR-6 (fewer legal sellers) and C-5 → CR-11b (informal braiders cannot advertise openly) | A-1, A-2, A-3 |
| C-13 | sellers.prospective | entry_rate | decrease | long | CR-1 (op 3: training cost attached to entry) → CR-4 (x: stay out, y: enter; entry made worse) → CR-4b | A-1, A-2 |
| C-17 | braiders.current | lobbying_effort | increase | medium | CR-1 (op 1) → CR-4 (x: accept, y: lobby for an exemption or a braiding-specific license) → CR-8c | A-1, A-N1 |
| C-18 | sellers.substitutes (licensed cosmetologists and schools) | lobbying_effort | increase | medium | CR-4 mirror (they hold a gain, C-14 and C-15, that repeal would remove; x: accept repeal, y: lobby to keep) | A-1, A-N1 |

## 6. Second-order effects

Depth limit 4; diffuse bystander effects pruned after depth 3. Each link names the exchange relation it follows (CR-9).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-11 | buyers.current | quality_information (informal braiding) | decrease | medium | C-5 → CR-11b (reviews, open advertising and legal recourse unavailable outside the legal market) | same_market_other_segment (legal ↔ informal braiding) | A-1, A-3 |
| C-12 | buyers.current | disputes_settled_outside_courts | increase | medium | C-5 → CR-11b (courts unavailable to an exchange outside the legal market) | same_market_other_segment (legal ↔ informal braiding) | A-1, A-3 |
| C-14 | sellers.substitutes (licensed cosmetologists) | net_price_received (braiding) | increase | medium | C-1 → CR-9 (competitors removed from the same market) → CR-6 (price tends to a higher clearing level) | same_market_other_segment (unlicensed ↔ licensed braiding), close | A-1, A-2 |
| C-15 | input_suppliers (cosmetology schools) | quantity_traded (school places) | increase | short | C-2 → CR-9 (training is the input that the license requires) → LW-10 | input_to (training → licensed braiding) | A-1, A-N2 |
| C-16 | sellers.complements (braiding hair and supplies) | quantity_complement | ambiguous | medium | (−) C-8 → CR-9 (fewer paid braids use fewer supplies); (+) C-9 and C-5 use the same supplies; CR-12b | complement (supplies ↔ braiding) | A-1, A-2, A-4 |
| C-20 | buyers.current (who keep buying legal braiding) | resources_available_other_uses | decrease | medium | C-7 → CR-8b (the higher price is a receipt to licensed sellers) and C-10 → CR-8c | the braiding exchange | A-1, A-2 |

**Where chains were stopped.**

- Braiders who leave paid braiding enter other labor markets (CR-9, substitute uses of labor); effects on wages there are diffuse bystander effects at depth 3; stopped.
- Effects of C-16 on supply makers' staff: stopped at depth 3 (ambiguous and diffuse).
- Effects of C-15 on the schools' own staff and premises: stopped at depth 3.

## 7. Combined effects

Keys reached by one chain, or by chains with the same sign, take that sign (CR-12a). Keys where chains conflict:

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| buyers.current, quantity_substitute (home braiding), medium (reading U1-b) | Paid braiding dearer and scarcer | Home braiding also covered under U1-b | None | U1-a: increase; U1-b: ambiguous (C-9) |
| sellers.complements, quantity_complement, medium | Home and informal braiding | Fewer paid braids | None | ambiguous (C-16) |
| braiders.current, employment, medium | None (those who violate stay in braiding: no push upward) | Exits by braiders at the margin | Not needed | decrease (C-3) |

## 8. Time structure

- **The 12-month window (CR-10a).** Braiders can keep working legally for 12 months. Those who will train have reason to start early, because 1,500 hours take most of a year or more; those who will stop can wind down. Legal supply therefore falls mainly at and after the deadline (C-1), while school enrollment rises in the window (C-15).
- **Stocks (CR-10b).** A braider's client base and skill are a stock. Braiders with established clients are best placed to continue informally (C-5); new entrants have no stock and face the full training cost (C-13). The fall in entry builds over years.
- **Persistence.** Training already paid for is sunk; licensed braiders and schools acquire a stake in keeping the requirement (C-18). If the requirement were repealed, braiders who left would not all return quickly (CR-10b).
- **Enforcement over time.** Complaint-driven enforcement (A-2, A-3) means the split between exit and informal work depends on complaints, which may come from licensed competitors who gain from them (C-14).

## 9. Opportunity costs

Each written as a signed change in a variable (CR-3, CR-8).

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-2 | braiders.current | compliance_cost | increase | Tuition and 1,500 hours of training largely unrelated to braiding (A-5) | CR-3c, CR-8c |
| C-4 | braiders.current | resources_available_other_uses | decrease | What braiders would have done with the tuition and the training hours, and the braiding work given up | CR-3a, CR-3c, CR-8c |
| C-8 | buyers.current | quantity_traded (legal paid braiding) | decrease | Braiding exchanges both parties expected to gain from (CR-5a) | CR-5a |
| C-10 | buyers.current | search_cost | increase | Time spent finding a braider (CR-8c) | CR-6, CR-11b → CR-8c |
| C-17 | braiders.current | lobbying_effort | increase | Resources spent lobbying (CR-8c) | CR-8c |
| C-19 | officials.enforcement | enforcement_cost | increase | Board inspection time and budget (CR-8c) | CR-8c |
| C-20 | buyers.current (who keep buying legal braiding) | resources_available_other_uses | decrease | What customers would have bought with the price difference and search time | CR-8b, CR-8c |

## 10. Assumptions

Case assumptions are used as given. New premises added by this re-run are marked A-N.

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Few current braiders already hold a cosmetology license, so the requirement binds. | binding | 0.95 | Board license records against a census of braiders. | Fail or lose support: C-1, C-2, C-3, C-4, C-5, C-6, C-7, C-8, C-9, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-20 |
| A-2 | The board enforces the requirement often enough that many braiders comply or stop. | enforcement | 0.7 | Board inspection budget; complaint volumes; fines. | Fail or lose support: C-1, C-3, C-4, C-6, C-7, C-8, C-9, C-10, C-13, C-14, C-16, C-19, C-20 |
| A-3 | Some braiders keep working without a license and are not caught. | enforcement | 0.8 | Complaint-driven enforcement; home-based work. | Fail or lose support: C-5, C-10, C-11, C-12 |
| A-4 | Home braiding by family or friends is a feasible substitute for some customers. | substitutability | 0.75 | Prevalence of home braiding. | Fail or lose support: C-9, C-16 |
| A-5 | The required training is largely unrelated to braiding quality. | other | 0.85 | Curriculum hours by topic; exam content. | Fail or lose support: No reported consequence depends on it alone; see Not reported. |
| A-6 | Braiders relocate to neighboring states on a meaningful scale. | mobility | 0.3 | Distance from cities to the borders; local customer base. | Fail or lose support: No reported consequence depends on it alone; see Not reported. |
| A-N1 | Braiders, licensed cosmetologists and schools can organize and spend to change or defend the requirement. (new premise) | other | 0.7 | Existing cosmetology trade associations; braiders are dispersed and mostly self-employed, which lowers but does not remove their capacity. | Fail or lose support: C-17, C-18 |
| A-N2 | Some current braiders or new entrants choose to obtain the full license. (new premise) | alternative_uses | 0.8 | Some braiders earn enough to justify $12,000 to $18,000 and 1,500 hours; some may already be partway through training. | Fail or lose support: C-2, C-15 |
| A-N3 | Customers expect paid braiding to be dearer or harder to find after the deadline and bring appointments forward. (new premise) | expectations | 0.4 | Publicity of the deadline among customers is uncertain; braids last weeks to months, limiting how far appointments can move. | Fail or lose support: No reported consequence depends on it alone; see Not reported. |

**Not reported** (a premise has p below 0.5, or the record lacks a needed fact):

- Braiders relocate to neighboring states (CR-4, x: here, y: there): A-6, p 0.3.
- Customers bring appointments forward before the deadline (CR-10a): A-N3, p 0.4.
- Quality of legal braiding: with A-5 (training largely unrelated to braiding), no core rule gives a sign for `quality_per_unit` of legal braiding. CR-11c allows the license to act as a signal that customers may read as quality; whether they do is empirical and no premise was available, so no sign is reported.
- Braiders reshape paid work as unpaid or in-kind (reclassification): the direction follows from CR-4, but no premise in the record says anyone is at that margin.

## 11. Report

**The policy:** Westmark requires anyone who braids hair for pay, and any business that employs them, to hold a full cosmetology license: 1,500 hours at a licensed school (typical tuition $12,000 to $18,000) and a state exam whose curriculum mostly covers cutting, coloring and chemicals. Existing braiders have 12 months to comply. The Board of Cosmetology fines unlicensed practice on complaint.

**Visible consequences:** There are fewer legal paid braiders (C-1), and those who license pay tuition and spend 1,500 hours training (C-2).

**Invisible consequences:** Braiders: fewer work in paid braiding (C-3); those who train or stop lose resources and options (C-4); some continue without a license (C-5); shops stop employing unlicensed braiders (C-6); some lobby (C-17). Customers: legal braiding costs more (C-7), fewer legal braids are bought (C-8), finding a braider takes more effort (C-10), more braiding is done at home (reading U1-a; C-9), and customers of informal braiders have less information and recourse (C-11, C-12); those who keep buying legally have less for other uses (C-20). Competitors and suppliers: licensed cosmetologists receive more for braiding (C-14); cosmetology schools fill more places (C-15); both lobby to keep the rule (C-18). Fewer people enter braiding (C-13). The board spends on enforcement (C-19).

**Ambiguous effects:** Sales of braiding hair and supplies (C-16): fewer paid braids push down, home and informal braiding push up. Home braiding under reading U1-b (C-9).

**Key conditions:** The requirement binds (A-1, p 0.95) and is enforced often enough to matter (A-2, p 0.7); some evade (A-3, p 0.8); home braiding is a feasible substitute (A-4, p 0.75); some braiders do get licensed (A-N2, p 0.8, new).

**What this analysis cannot say:** How many braiders license, leave or go informal; whether the gains to licensed competitors and schools outweigh the losses to braiders and customers; whether the policy is good. Health and safety effects of braiding, licensed or not, are out of scope in version 1. Whether customers read the license as a sign of quality is not decided by the core rules.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | braiders.current | number_of_sellers (legal paid braiders) | decrease | medium | visible | B | CR-1 (op 1, K1) → CR-4 (x: train for the license, y: stop braiding for pay or braid illegally) → CR-4b (those for whom training costs more than braiding is worth switch) | A-1, A-2 |
| C-2 | braiders.current | compliance_cost | increase | medium | visible | B | CR-1 (op 3: tuition and 1,500 hours attached to legal braiding) → CR-8c | A-1, A-N2 |
| C-3 | braiders.current | employment (paid braiding, legal and informal) | decrease | medium | invisible | B | C-1 → CR-4b (those at the margin leave paid braiding for other work); those who violate stay (CR-4b, the rest bear the change) | A-1, A-2 |
| C-4 | braiders.current | resources_available_other_uses | decrease | medium | invisible | B | C-2 → CR-3c and CR-8c (tuition and training time withdrawn from other uses); CR-3a for those who stop braiding (fall back to a lower-ranked option) | A-1, A-2 |
| C-5 | braiders.current | informal_activity | increase | medium | invisible | B | CR-1 (op 3 in practice: fine risk) → CR-4 (x: comply, y: braid without a license) | A-1, A-3 |
| C-6 | businesses employing braiders | employment (unlicensed braiders employed in shops) | decrease | medium | invisible | B | CR-1 (op 3, K2: fines for employers) → CR-4 (x: employ an unlicensed braider, y: stop) | A-1, A-2 |
| C-7 | buyers.current | price_paid (legal paid braiding) | increase | medium | invisible | B | C-1 → CR-6 (fewer sellers at the old price; unsatisfied buyers offer better terms) and CR-7a (new legal braiders enter only if expected earnings cover the training cost) | A-1, A-2 |
| C-8 | buyers.current | quantity_traded (legal paid braiding) | decrease | medium | invisible | B | CR-5a (exchanges with unlicensed braiders prevented) and C-7 → CR-4c | A-1, A-2 |
| C-9 | buyers.current | quantity_substitute (home braiding by family or friends) | U1-a: increase; U1-b: ambiguous | medium | invisible | B | C-7 and C-8 → CR-4 (x: paid braiding, y: home braiding) → CR-9 (substitute); under U1-b home braiding is also covered (op 1 or 3), pushing the other way, CR-12b | A-1, A-2, A-4 |
| C-10 | buyers.current | search_cost | increase | medium | invisible | B | C-1 → CR-6 (fewer legal sellers) and C-5 → CR-11b (informal braiders cannot advertise openly) | A-1, A-2, A-3 |
| C-11 | buyers.current | quality_information (informal braiding) | decrease | medium | invisible | B | C-5 → CR-11b (reviews, open advertising and legal recourse unavailable outside the legal market) | A-1, A-3 |
| C-12 | buyers.current | disputes_settled_outside_courts | increase | medium | invisible | B | C-5 → CR-11b (courts unavailable to an exchange outside the legal market) | A-1, A-3 |
| C-13 | sellers.prospective | entry_rate | decrease | long | invisible | B | CR-1 (op 3: training cost attached to entry) → CR-4 (x: stay out, y: enter; entry made worse) → CR-4b | A-1, A-2 |
| C-14 | sellers.substitutes (licensed cosmetologists) | net_price_received (braiding) | increase | medium | invisible | B | C-1 → CR-9 (competitors removed from the same market) → CR-6 (price tends to a higher clearing level) | A-1, A-2 |
| C-15 | input_suppliers (cosmetology schools) | quantity_traded (school places) | increase | short | invisible | B | C-2 → CR-9 (training is the input that the license requires) → LW-10 | A-1, A-N2 |
| C-16 | sellers.complements (braiding hair and supplies) | quantity_complement | ambiguous | medium | invisible | B | (−) C-8 → CR-9 (fewer paid braids use fewer supplies); (+) C-9 and C-5 use the same supplies; CR-12b | A-1, A-2, A-4 |
| C-17 | braiders.current | lobbying_effort | increase | medium | invisible | B | CR-1 (op 1) → CR-4 (x: accept, y: lobby for an exemption or a braiding-specific license) → CR-8c | A-1, A-N1 |
| C-18 | sellers.substitutes (licensed cosmetologists and schools) | lobbying_effort | increase | medium | invisible | B | CR-4 mirror (they hold a gain, C-14 and C-15, that repeal would remove; x: accept repeal, y: lobby to keep) | A-1, A-N1 |
| C-19 | officials.enforcement | enforcement_cost | increase | short | invisible | B | CR-1 (op 2, K2) → CR-8c | A-2 |
| C-20 | buyers.current (who keep buying legal braiding) | resources_available_other_uses | decrease | medium | invisible | B | C-7 → CR-8b (the higher price is a receipt to licensed sellers) and C-10 → CR-8c | A-1, A-2 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from a core rule. Near-gap: the effect of the license on the quality of legal braiding. CR-11c allows a policy to change beliefs by conveying information, but with training unrelated to braiding (A-5) no rule gives a sign without a premise on what customers believe; none was available, so it is listed as not reported.

**(b) New premises.**

- A-N1 (p 0.7): CR-4 (x: accept, y: lobby) needs someone at that margin.
- A-N2 (p 0.8): CR-4b says some switch each way only if some are at each margin; school enrollment and compliance costs need some braiders to choose the license.
- A-N3 (p 0.4, not reported): CR-10a needs customer expectations about the deadline.

**(c) Unclear core rules.**

- CR-1 with partial enforcement: CR-1's premise says an unenforced prohibition is operation 3, not 1. With complaint-driven enforcement (A-2 p 0.7 and A-3 p 0.8 both hold), the same rule is operation 1 for some braiders and operation 3 for others; CR-1 does not say how to split a class by enforcement. Both were recorded.
- CR-4b and "those for whom x was ranked only narrowly above y": with a large fixed cost (tuition, 1,500 hours), the margin is not narrow for anyone; the rule reads as if changes are small. Applied as "those whose gain from braiding is below the training cost switch".
- CR-6 is stated for a price "prevented from moving". A license restricts who may sell, not the price; the first paragraph of CR-6 (price formation) was used for the price rise, which the rule's title does not make obvious.
- CR-7c (asset values) has no tradable asset here: a cosmetology license cannot be sold. The capitalized gain is in licensed providers' earnings, which no variable records as an asset.
