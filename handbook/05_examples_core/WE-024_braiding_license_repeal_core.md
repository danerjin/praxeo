# WE-024 / Analysis: Abolition of the braiding license requirement

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Westmark State Cosmetology Act, amendment 9 (braiding exemption).** Five years after amendment 7 (WE-003) required a full cosmetology license to braid hair for pay, the legislature removes braiding from the definition of cosmetology. The bill was introduced, with the votes to pass visible, about nine months before the exemption took effect. The starting point, taken from WE-003's analysis and stated here as the situation at abolition rather than as findings: some braiders trained and became licensed, at a cost of 1,500 hours and $12,000 to $18,000 in tuition; some left the trade for other work; some kept braiding without a license; cosmetology schools enrolled braiders who wanted only to braid legally; legal braiding costs more than it did. The neighboring states still do not license braiding.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Exemption | Removal of a `licensing_requirement` | Braiding hair for pay (braids, twists and locs, with no cutting or chemicals) | Braiders and businesses that employ them | No license, registration or training is required to braid for pay, or to employ braiders. Existing cosmetology licenses remain valid. Tuition already paid is not refunded. Cutting, coloring and chemical treatments still require a cosmetology license. | None |
| R2 Enforcement | End of enforcement | WE-003 K2 as it applies to braiding | State Board of Cosmetology | Inspections and fines for unlicensed braiding end; pending braiding cases are dropped. | None |

Unclear provisions: whether a licensed salon must ensure that its braiders hold a license because the establishment itself is licensed. Assumed not: the exemption applies to the service, wherever it is performed.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| R1 Exemption of braiding | removal of a triangular intervention (a licensing requirement) | Yes: many who would braid for pay hold no license (A-1) | 2 for unlicensed braiders, former braiders and would-be braiders (braiding for pay becomes a legal option); 2 for businesses (employing unlicensed braiders becomes legal); 2 for students in training (braiding legally without finishing); no direct operation on licensed braiders, whose situation changes through new competitors (CR-9) | CR-4, CR-5, CR-6, CR-7b, CR-7c, CR-9, CR-10a, CR-10b, CR-11b |
| R2 End of enforcement for braiding | end of administration | Yes | 3 for unlicensed braiders (the risk of inspection and fines is removed; pending cases dropped); 4 for the board (tasks and their cost removed) | CR-4 (x: hidden, y: open), CR-8c |

The counterfactual is that amendment 7 stays: a full cosmetology license required to braid for pay, enforced by complaint-driven inspections. Every sign is relative to that path; persistence is relative to the path on which the requirement was never imposed. Facts about WE-003 come from the WE-024 starting point and the WE-003 input (background only).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| braiders.unlicensed | People braiding for pay without a license (A-2) | Op 2 and op 3: braiding openly becomes legal; the risk of fines ends. |
| braiders.with_pending_cases | Unlicensed braiders facing pending board cases | Op 3: pending cases dropped. |
| braiders.former | People who left braiding for other work | Op 2: returning without a license becomes legal. |
| braiders.prospective | Would-be braiders deterred by the requirement (A-3) | Op 2: entry without 1,500 hours of training. |
| braiders.licensed | Braiders who trained and hold a cosmetology license | No direct operation; new competitors (CR-9, same market). |
| students.braiding_only | Students who enrolled only to braid legally (A-5) | Op 2: braiding legally without finishing. |
| schools.cosmetology | Licensed cosmetology schools | Through CR-9: training is no longer an input to legal braiding. |
| buyers.braiding | Customers of braiders | Through CR-9: more sellers, more of them in the open. |
| salons | Businesses that employ braiders | Op 2: may employ unlicensed braiders (unclear provision read as the input assumes). |
| sellers.cosmetology_other | Licensed sellers of cutting, coloring and chemical services | Through CR-9: licensed braiders may move into their segment (A-7). |
| buyers.cosmetology_other | Customers for cutting, coloring and chemical services | Through CR-9. |
| input_suppliers.braiding_products | Sellers of braiding hair and supplies | Through CR-9 (complement). |
| officials.board | State Board of Cosmetology | Op 4: braiding enforcement and license fees from braiders end. |
| officials.tax | Income tax authority | Through CR-11b: open work leaves records (A-N1). |
| taxpayers | Those who fund the board | Op 4 in reverse, if the board's budget falls (A-12). |

## 4. Direct effect

CR-1 and CR-2: the immediate change.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | braiders.unlicensed, braiders.prospective | number_of_sellers (legal braiders) | increase | short; medium | CR-1 op 2 | A-1, A-2, A-3 |
| C-2 | braiders.licensed | share_of_sellers_licensed | decrease | short; medium | CR-1 op 2, arithmetic | A-1, A-2 |
| C-3 | buyers.braiding | price_paid (braiding) | decrease | short; medium | CR-5c, CR-6 | A-1, A-3 |
| C-4 | officials.board | enforcement_cost (braiding) | decrease | short | CR-1 op 4, CR-8c | - |
| C-5 | braiders.with_pending_cases | resources_available_other_uses | increase | short | CR-1 op 3, CR-8b | - |

## 5. Responses

CR-4 for each pair of options; CR-5 for exchanges the requirement prevented; CR-10a for the announcement window; CR-7c for the license's value.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | braiders.unlicensed | informal_activity (unlicensed braiding for pay) | decrease | short | CR-4 (x: braid hidden, y: braid openly) | A-2 |
| C-7 | braiders.prospective | entry_rate | increase | short; medium | CR-4 (x: stay out, y: enter), CR-10a | A-3 |
| C-8 | braiders.former | job_changes (return to braiding) | increase | medium | CR-4 (x: current work, y: return), CR-10b | A-6, A-15 |
| C-9 | schools.cosmetology | quantity_traded (enrollment of students who want only to braid) | decrease | short (from announcement) | CR-4 (x: continue or enroll, y: stop or do not enroll), CR-10a | A-4, A-5 |
| C-10 | students.braiding_only | resources_available_other_uses | increase | short | CR-3b, CR-8a | A-4, A-5 |
| C-11 | braiders.licensed | net_price_received (braiding) | decrease | short; medium | CR-9, CR-6, CR-7b | A-1, A-3 |
| C-12 | braiders.licensed | asset_value (cosmetology license, as used for braiding) | decrease | short (from announcement) | CR-7c, CR-10c | A-1, A-3 |
| C-13 | braiders.licensed | quantity_supplied (cutting, coloring and chemical services) | increase | medium | CR-4 (x: braiding, y: other licensed services), CR-7a | A-7 |
| C-14 | buyers.braiding | quantity_traded (paid braiding) | increase | short; medium | CR-5, CR-4c | A-1, A-3 |
| C-15 | buyers.braiding | quantity_substitute (home braiding by family or friends) | decrease | short; medium | CR-4 (x: home braiding, y: paid braiding) | A-9, A-3 |
| C-16 | salons | compliance_cost | decrease | short | CR-1 op 2, CR-8c | A-1 |
| C-17 | salons | employment (braiders in salons) | increase | medium | CR-4 (x: hire licensed braiders only, y: hire any braider), CR-9 | A-1, A-3 |
| C-18 | braiders.unlicensed | investment_target (premises and equipment for braiding) | increase | medium | CR-4 (x: home and hidden, y: shop), CR-10c | A-2, A-11 |
| C-19 | schools.cosmetology, braiders.licensed | lobbying_effort (to restore the requirement) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-8 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7, and CR-11 for information. Depth limit 4. Effects on landlords of shop space and on employers that former braiders leave are diffuse bystander effects pruned at depth 3.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-20 | buyers.braiding | quality_information | increase | short; medium | CR-11b (reversed) | unlicensed braiding same_market_other_segment of licensed braiding (it joins the legal market) | A-2 |
| C-21 | buyers.braiding | disputes_settled_outside_courts | decrease | short; medium | CR-11b (reversed) | as above | A-2 |
| C-22 | buyers.braiding | search_cost | decrease | short; medium | CR-11b, CR-6 | as above | A-2, A-3 |
| C-23 | buyers.cosmetology_other | price_paid (cutting, coloring and chemical services) | decrease | medium | CR-9, CR-6 | braiding same_market_other_segment of cutting, coloring and chemical services (partial) | A-7 |
| C-24 | sellers.cosmetology_other | net_price_received | decrease | medium | CR-9, CR-6 | as above | A-7 |
| C-25 | input_suppliers.braiding_products | quantity_complement (braiding hair and supplies) | increase | medium | CR-9, LW-10 | braiding hair complement of braiding services (close) | A-1, A-3 |
| C-26 | schools.cosmetology | employment (instructors) | decrease | medium | CR-9, LW-10 | cosmetology instruction input_to licensed braiding (partial) | A-5, A-4 |
| C-27 | officials.board | tax_revenue (license fees from braiders) | decrease | medium; long | CR-1 op 2, CR-8b | - | A-5 |
| C-28 | officials.tax | tax_revenue (income tax on braiding earnings) | increase | medium | CR-11b, CR-4 | - | A-2, A-N1 |
| C-29 | taxpayers | resources_available_other_uses | increase | medium | CR-8a, CR-8d | - | A-12 |
| C-30 | buyers.braiding | resources_available_other_uses | increase | short; medium | CR-8b, CR-3b | - | A-1, A-3 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| buyers.braiding, price_paid, short; medium | - | more sellers (CR-6): informal braiders in the open, entrants, some returners | - | decrease (C-3) |
| braiders.licensed, net_price_received (braiding) | - | new competitors (CR-9, CR-6) | - | decrease (C-11) |
| braiders.licensed, quantity_supplied | other licensed services (C-13) | - | Different markets: braiding quantity not signed for this class | increase (other services) |
| officials (board and tax authority), tax_revenue | income tax (C-28) | license fees (C-27) | Different variables in practice (different taxes and recipients): not netted (CR-12c) | increase (income tax); decrease (license fees) |

Metamorphic check: added in the comparison phase.

## 8. Time structure

- **Announcement window (nine months).** The exemption was expected about nine months before it took effect. Prospective students stop enrolling and some current students stop (CR-10a; C-9); license values for braiding fall as soon as the exemption is expected (CR-7c; C-12). Would-be entrants have a reason to wait for the effective date rather than risk fines (CR-4, x: enter now, y: enter after; C-7).
- **At the effective date.** Informal braiders come into the open at once (C-6); pending cases are dropped (C-5); enforcement ends (C-4).
- **Gradual.** Entry and the shift of licensed braiders into other services take months to years (C-7, C-13). Premises are taken only if braiders expect the exemption to last (A-11, 0.7; C-18).
- **What does not reverse (CR-10b, CR-8c).** The training already done is used up: tuition is not refunded, and the 1,500 hours cannot be recovered. Many former braiders do not return, because unused skills decayed, clients settled elsewhere and their current work pays more than before (A-15, 0.75). Braiders who moved to neighboring states are unlikely to return on a meaningful scale (A-14, 0.2: not reported).
- **Belief in the exemption.** If braiders expected the requirement to return with practicing braiders grandfathered (A-13, 0.25), they would rush to practice before it returned (CR-10a); the premise is below the cut-off and nothing rests on it.

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-4 | officials.board | enforcement_cost (braiding) | decrease | (released) inspection and case work | CR-1 op 4, CR-8c |
| C-19 | schools.cosmetology, braiders.licensed | lobbying_effort (to restore the requirement) | increase | Resources spent seeking to restore the requirement | CR-4 (x: accept, y: lobby), CR-8c |

CR-8's symmetry: buyers' lower prices (C-3, C-30) are matched by licensed braiders' lower receipts (C-11); students' saved tuition (C-10) is matched by schools' lost enrollment (C-9); fines not paid (C-5) and license fees not paid (C-27) are matched by lower receipts of the board. Resources released from enforcement and compliance (C-4, C-16) are counted as released.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | The license still binds: many people who would braid for pay do not hold a cosmetology license. | binding | 0.95 | Board license records against estimates of informal and former braiders. | These consequences fail or lose this chain: C-1, C-2, C-3, C-11, C-12, C-14, C-16, C-17, C-25, C-30. |
| A-2 | A meaningful number of people braid for pay without a license and will come into the open. | enforcement | 0.8 | Complaint-driven enforcement; home-based work (WE-003 A-3). | These consequences fail or lose this chain: C-1, C-2, C-6, C-18, C-20, C-21, C-22, C-28. |
| A-3 | The license deterred some would-be braiders, who will now enter. | binding | 0.85 | Entry before and after amendment 7; school enrollment of braiders. | These consequences fail or lose this chain: C-1, C-3, C-7, C-11, C-12, C-14, C-15, C-17, C-22, C-25, C-30. |
| A-4 | Students midway through training can stop without owing the remaining tuition. | other | 0.7 | School contracts; billing per term. | These consequences fail or lose this chain: C-9, C-10, C-26. |
| A-5 | Some of the schools' students enrolled only to braid legally. | other | 0.85 | Enrollment records; students' stated plans. | These consequences fail or lose this chain: C-9, C-10, C-26, C-27. |
| A-6 | Some former braiders kept enough skill and contacts, and earn little enough in their current work, that they will return within a few years. | mobility | 0.6 | Survey of former braiders; earnings in their current work. | These consequences fail or lose this chain: C-8. |
| A-7 | Licensed braiders can sell cutting, coloring or chemical services, and some customers will buy them from them. | alternative_uses | 0.6 | Services licensed braiders already offer; demand in their neighborhoods. | These consequences fail or lose this chain: C-13, C-23, C-24. |
| A-8 | Schools and licensees can organize at a cost below their stake. | other | 0.8 | Their lobbying under amendment 7. | These consequences fail or lose this chain: C-19. |
| A-9 | Home braiding by family or friends is a feasible substitute for some customers. | substitutability | 0.75 | Prevalence of home braiding (WE-003 A-4). | These consequences fail or lose this chain: C-15. |
| A-10 | The required training is largely unrelated to braiding quality. | other | 0.85 | Curriculum hours by topic; exam content (WE-003 A-5). | No reported consequence rests on it (see Not reported). |
| A-11 | Braiders expect the exemption to last long enough to pay back premises and equipment (a few years). | expectations | 0.7 | Margin of the vote; strength of the school and licensee lobby. | These consequences fail or lose this chain: C-18. |
| A-12 | The board's budget falls with its braiding workload rather than being redirected to other work. | revenue_use | 0.6 | Budget process for the board; share of the budget from license fees. | These consequences fail or lose this chain: C-29. |
| A-13 | Braiders expect the license to return, with those then practicing grandfathered. | expectations | 0.25 | Legislative history; how the board's earlier rules treated existing practitioners. | No reported consequence rests on it (see Not reported). |
| A-14 | Braiders who moved to neighboring states return on a meaningful scale. | mobility | 0.2 | WE-003 A-6 (little relocation in the first place). | No reported consequence rests on it (see Not reported). |
| A-15 | For many former braiders, returning costs more than the restored return: skills unused for five years have decayed, clients have settled with other braiders, and experience built in other work raises what they would give up. | reversal_cost | 0.75 | Survey of former braiders; how long they have been away; earnings in their current work. | These consequences fail or lose this chain: C-8. |
| A-N1 | Braiders who come into the open declare income they did not declare while working without a license. | other | 0.6 | NEW. Open work leaves records (premises, advertising, card payments); informal work was hidden from the board and, by the same means, from the tax authority. | These consequences fail or lose this chain: C-28. |

**Not reported** (an assumption below 0.5):
- Braiders who moved to neighboring states return (CR-4, x: there, y: here): needs A-14 (p 0.2).
- A rush to practice before an expected return of the requirement with grandfathering (CR-10a): needs A-13 (p 0.25).
- A fall in the quality of braiding because braiders no longer train: needs the negation of A-10 (p 0.15). With A-10, the training is largely unrelated to braiding quality, so no quality sign is reported.

## 11. Report

**The policy:** Five years after Westmark required a full cosmetology license to braid hair for pay, the legislature removes braiding from the definition of cosmetology and ends enforcement against unlicensed braiding. Existing licenses stay valid; tuition already paid is not refunded. The comparison is with the license requirement staying in force.

**Visible consequences:** More people may legally braid for pay (C-1); unlicensed braiders come into the open (C-6); customers pay less and buy more braiding (C-3, C-14); licensed braiders receive less for braiding (C-11); enrollment of students who wanted only to braid falls (C-9); the board stops enforcing (C-4).

**Invisible consequences:**
- *Braiders:* would-be braiders enter (C-7); some former braiders return, but many do not (C-8); braiders take premises (C-18); those with pending cases keep what they would have paid (C-5). Licensed braiders' licenses lose their value for braiding (C-12), and some move into cutting, coloring and chemical services (C-13), where prices and other sellers' receipts fall (C-23, C-24). The share of sellers who are licensed falls (C-2).
- *Customers:* can learn about braiders, find them and use courts more easily (C-20, C-22, C-21); use home braiding less (C-15); have more to spend elsewhere (C-30).
- *Students and schools:* students who stop keep the remaining tuition (C-10); schools need fewer instructors (C-26) and, with licensees, lobby to restore the requirement (C-19).
- *Salons and suppliers:* salons save compliance costs and hire more braiders (C-16, C-17); sellers of braiding hair and supplies sell more (C-25).
- *The state:* license fees from braiders fall (C-27); income tax from braiding rises if open braiders declare income (C-28); taxpayers gain if the board's budget falls (C-29).

**Ambiguous effects:** None reported as ambiguous.

**What does not reverse:** Training already completed stays used up: the 1,500 hours and the tuition. Many former braiders do not come back (A-15).

**Key conditions:** The license binds (A-1, 0.95); many braid informally (A-2, 0.8); the license deterred entrants (A-3, 0.85); returning is costly for many former braiders (A-15, 0.75); licensed braiders can sell other services (A-7, 0.6). One premise was added: braiders who come into the open declare income (A-N1, 0.6).

**What this analysis cannot say:** How many braiders enter or return, how far prices fall, or how much licensed braiders lose. It does not weigh customers' and new braiders' gains against licensed braiders' and schools' losses, or say whether the change is good. Health and safety effects, including any effect on hygiene or injuries from braiding, are out of scope, as are environmental effects.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | braiders.unlicensed, braiders.prospective | number_of_sellers (legal braiders) | increase | short; medium | visible | B | CR-1 (op 2: braiding for pay without a license becomes legal); the requirement bound (A-1), so the set of legal sellers grows as informal braiders come into the open (A-2) and deterred braiders enter (A-3) | A-1, A-2, A-3 | partial (former braiders mostly do not return, A-15) |
| C-2 | braiders.licensed | share_of_sellers_licensed | decrease | short; medium | invisible | B | CR-1 (op 2); arithmetic: unlicensed legal sellers are added, C-1, while licensed ones keep their licenses | A-1, A-2 | none |
| C-3 | buyers.braiding | price_paid (braiding) | decrease | short; medium | visible | B | CR-6 (with more sellers offering at each price, the price tends toward a lower clearing level); CR-5c (the range of acceptable terms moves); A-3: some new sellers enter | A-1, A-3 | partial (fewer sellers return than left, A-15) |
| C-4 | officials.board | enforcement_cost (braiding) | decrease | short | visible | A | CR-1 (R2: inspections and fines for unlicensed braiding end); CR-8c (resources no longer used up in enforcing) | none | none |
| C-5 | braiders.with_pending_cases | resources_available_other_uses | increase | short | invisible | A | CR-1 (op 3: pending cases are dropped, so the fines are not paid); CR-8b (what would have been paid to the state stays with the braider) | none | n/a (transition effect) |
| C-6 | braiders.unlicensed | informal_activity (unlicensed braiding for pay) | decrease | short | visible | B | CR-4 (x: braid hidden, y: braid openly; y is now legal and free of risk, so those who were hiding come into the open; CR-4a: none move the other way) | A-2 | none |
| C-7 | braiders.prospective | entry_rate | increase | short; medium | invisible | B | CR-4 (x: stay out, y: enter; entry no longer costs 1,500 hours and $12,000 to $18,000); CR-10a (some wait for the effective date) | A-3 | none |
| C-8 | braiders.former | job_changes (return to braiding) | increase | medium | invisible | B | CR-4 (x: stay in current work, y: return to braiding; y improved, so former braiders who kept skill and contacts and earn little elsewhere return, A-6); CR-10b (for many, returning costs more than the restored return: skills decayed, clients gone, A-15) | A-6, A-15 | partial (A-15: many former braiders do not return) |
| C-9 | schools.cosmetology | quantity_traded (enrollment of students who want only to braid) | decrease | short (from announcement) | visible | B | CR-4 (x: continue training, y: stop and braid legally; y improved; A-4: students can stop without owing the rest); CR-10a (from the announcement, nine months before the effective date, prospective students hold off); A-5: some enrolled only to braid | A-4, A-5 | none for new enrollment; full for training already completed (tuition not refunded) |
| C-10 | students.braiding_only | resources_available_other_uses | increase | short | invisible | B | CR-3b (adding an option cannot make them worse off); CR-8a (the remaining tuition and hours are no longer directed to training and are available for other uses, A-4) | A-4, A-5 | partial: tuition and hours already spent are used up and not refunded (CR-8c, CR-10b) |
| C-11 | braiders.licensed | net_price_received (braiding) | decrease | short; medium | visible | B | CR-9 (relation: new legal sellers are in the same market); CR-6 (the price moves to a lower clearing level, C-3); CR-7b (the loss settles on the means that cannot move: licensed braiders' training is specific and sunk) | A-1, A-3 | none (price); full for the training cost, which stays sunk |
| C-12 | braiders.licensed | asset_value (cosmetology license, as used for braiding) | decrease | short (from announcement) | invisible | B | CR-10c (the value of a durable means reflects the yields it brings); CR-7c (the fall in the license's yield for braiding, C-11, is borne by those who hold it when the repeal becomes expected) | A-1, A-3 | full: the 1,500 hours and tuition stay used up (CR-8c); the license's premium for braiding does not |
| C-13 | braiders.licensed | quantity_supplied (cutting, coloring and chemical services) | increase | medium | invisible | B | CR-4 (x: braiding, y: services that still require their license; x made worse); CR-7a (their skill moves to the use that now yields more, A-7) | A-7 | none |
| C-14 | buyers.braiding | quantity_traded (paid braiding) | increase | short; medium | visible | B | CR-5 (exchanges the requirement prevented now take place); CR-4c (at a lower price more is bought, LW-3) | A-1, A-3 | partial (A-15) |
| C-15 | buyers.braiding | quantity_substitute (home braiding by family or friends) | decrease | short; medium | invisible | B | CR-4 (x: home braiding, y: paid braiding; y made cheaper and easier to find, so customers for whom the two were close switch to paid braiding, A-9) | A-9, A-3 | none |
| C-16 | salons | compliance_cost | decrease | short | invisible | B | CR-1 (op 2: salons may employ unlicensed braiders; read as the input assumes, that the exemption applies to the service wherever performed); CR-8c (checking licenses and the risk of fines no longer use up resources) | A-1 | none |
| C-17 | salons | employment (braiders in salons) | increase | medium | invisible | B | CR-4 (salons may now hire from a larger pool at lower cost); CR-9 (relation: braiders' labor input_to salon braiding) | A-1, A-3 | none |
| C-18 | braiders.unlicensed | investment_target (premises and equipment for braiding) | increase | medium | invisible | B | CR-4 (x: braid from home out of sight, y: take premises; y no longer exposes them to fines); CR-10c (premises pay back only if the exemption lasts a few years, A-11) | A-2, A-11 | none |
| C-19 | schools.cosmetology, braiders.licensed | lobbying_effort (to restore the requirement) | increase | short; medium | invisible | B | CR-4 (x: accept the exemption, y: lobby to restore the requirement; the exemption makes x worse for them); CR-8c (resources spent lobbying are used up) | A-8 | n/a |
| C-20 | buyers.braiding | quality_information | increase | short; medium | invisible | B | CR-11b (where an exchange is outside the legal market, the means by which buyers learn about sellers are not available; moving it back into the legal market restores advertising, reviews, reputation and recourse to courts) | A-2 | none |
| C-21 | buyers.braiding | disputes_settled_outside_courts | decrease | short; medium | invisible | B | CR-11b (open, legal sellers can be taken to court and have reputations to protect) | A-2 | none |
| C-22 | buyers.braiding | search_cost | decrease | short; medium | invisible | B | CR-11b (sellers can advertise); CR-6 (with more sellers, buyers find one at lower cost) | A-2, A-3 | none |
| C-23 | buyers.cosmetology_other | price_paid (cutting, coloring and chemical services) | decrease | medium | invisible | B | CR-9 (relation: braiding same_market_other_segment of other cosmetology services; licensed braiders move into the latter, C-13); CR-6 (more sellers move the price to a lower clearing level) | A-7 | none |
| C-24 | sellers.cosmetology_other | net_price_received | decrease | medium | invisible | B | CR-9 (same relation); CR-6 (the mirror of C-23: sellers already in that segment receive less) | A-7 | none |
| C-25 | input_suppliers.braiding_products | quantity_complement (braiding hair and supplies) | increase | medium | invisible | B | CR-9 and LW-10 (relation: braiding hair and supplies complement braiding services; more braiding at a lower price, C-14, raises demand for them) | A-1, A-3 | none |
| C-26 | schools.cosmetology | employment (instructors) | decrease | medium | invisible | B | CR-9 and LW-10 (relation: instruction input_to licensed braiding; demand for it follows enrollment, C-9) | A-5, A-4 | none |
| C-27 | officials.board | tax_revenue (license fees from braiders) | decrease | medium; long | invisible | B | CR-1 (no license is needed to braid, so braiders who would have bought one in the counterfactual, A-5, do not); CR-8b (what they no longer pay the board no longer reaches it) | A-5 | none |
| C-28 | officials.tax | tax_revenue (income tax on braiding earnings) | increase | medium | invisible | B | CR-4 (braiders come into the open, C-6); CR-11b (open work leaves records: advertising, premises, card payments), so income previously not declared is declared (A-N1) | A-2, A-N1 | none |
| C-29 | taxpayers | resources_available_other_uses | increase | medium | invisible | B | CR-8a (the board's braiding work no longer draws on its budget); CR-8d (the saving reaches other uses only if the budget falls, A-12) | A-12 | none |
| C-30 | buyers.braiding | resources_available_other_uses | increase | short; medium | invisible | B | CR-8b (the lower price, C-3, leaves buyers more for other uses; CR-8 symmetry with C-11); CR-3b (adding sellers cannot make buyers worse off by their own ranking) | A-1, A-3 | partial (A-15) |

## Gaps found

**(a) Calculus gaps.** None. Every step used CR-1 to CR-12, LW-3, LW-10 or arithmetic. CR-11b was applied in reverse (an exchange moved back into the legal market regains the means of learning about sellers); the rule is stated one way but its derivation (CR-1, AX-1) is symmetric, as its universality test requires.

**(b) New premises.**
- A-N1 (p 0.6): needed for C-28. CR-11b says the means of learning about an exchange return when it is legal, but whether the tax authority learns of the income, and the braider declares it, is empirical and not among the case assumptions.

**(c) Unclear core rules.**
- CR-11b is worded only for exchanges moved outside the legal market. Its use for exchanges moved back in relies on the symmetry test in the preamble rather than on the rule's own statement.
- CR-10b and CR-8c on sunk training: the training cost is used up on both the repeal path and the counterfactual, so it is not a signed consequence of the repeal; but it is the clearest case of an effect of the original policy that persists. The persistence field was used to record it on C-12 and C-9; the core rules do not say where such a persisting cost belongs when it has no sign against the counterfactual.
- CR-4 for lobbying on a repeal (C-19): as in the other repeal cases, the counterfactual also has defensive lobbying. Signed increase on the ground that the repeal makes accepting worse for schools and licensees, but the rule does not settle the comparison across paths.
