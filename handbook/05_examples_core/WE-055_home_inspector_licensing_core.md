# WE-055 / Analysis: Home inspector licensing with grandfathering and complaint-only enforcement

Analyst: core-only re-run (Handbook 0.9)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Aldenmoor Home Inspector Licensing Act.** Aldenmoor has about 68,000 home sales a year and about 61,000 inspections a year (about 54,000 pre-purchase for buyers, 4,000 pre-listing for sellers, 3,000 of new homes for builders and buyers), at an average fee of about $450. About 610 people inspect homes for pay. About 400 began before 1 January 2025: about 320 will have at least 250 fee-paid inspections in the three years to 31 December 2027; about 60 began in the second half of 2024 and reach three years only during the application window; about 80 are part-timers with three years or more at 40 to 80 inspections a year. About 210 began on or after 1 January 2025 and cannot reach three years by the end of 2027. About 70 enter and 50 leave each year. About 45% hold a voluntary national certification; about 40% carry no errors-and-omissions or liability insurance. About 35 licensed professional engineers inspect homes. About 70% of buyers hire an inspector their agent recommended. Approved training will cost about $3,200 and three weeks; the exam about $200 (pass rate about 70%); the required insurance about $1,800 a year; the license $250 a year. Neighboring Linmouth has no license; about 12% of Aldenmoor's sales are in the Brask River border metro, where about 40 Linmouth inspectors do some Aldenmoor jobs.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Inspections of residential property in Aldenmoor, wherever the inspector lives. Linmouth, across the Brask River, has no license. | Act, s. 2. |
| Announced / enacted / effective / expires | Introduced 12 January 2026; enacted 3 June 2026; courses approved from 1 January 2027, exam from March 2027; new entrants need a license from 1 July 2027; everyone from 1 January 2028; grandfather applications 1 July to 31 December 2027; no expiry. | Act, s. 3, 9, 14. |
| Enforcement (who, penalties, resources) | Home Inspector Board, two investigators, funded by license, exam and application fees. Unlicensed practice: fine up to $2,500 per inspection; licensees: suspension or revocation. The Board investigates "only upon a written complaint by a buyer of residential property or by a licensed real-estate agent." | Act, s. 10 to 12. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 License | `licensing_requirement` | Home inspection for pay | Anyone inspecting a home in Aldenmoor | 120 hours of approved training; state exam; $300,000 insurance; $250 a year. A license not renewed for 12 months is restored only by meeting the requirements for a new one. | Licensed professional engineers and architects. |
| K2 Grandfathering | Exemption | Training and exam | Incumbent inspectors | Licensed without training or exam on application between 1 July and 31 December 2027, if at the date of application the applicant has three years of practice and 250 fee-paid inspections in those three years, documented by reports. Insurance and fee still required. | - |
| K3 Enforcement on complaint | Enforcement | K1, K2, K4 | Board | Investigation only on a written complaint by a buyer or a licensed agent. | - |
| K4 Agents and inspectors | Rule on agents' conduct | Real-estate agents | Agents | "A real-estate licensee shall not direct, steer or require a client to use a particular home inspector." See U1. | - |

Counterfactual: Aldenmoor without the Act: no license, inspectors entering and leaving as now, agents recommending inspectors as now, and the inspectors' association continuing its campaign for licensing (A-18).

Unclear provisions:
- U1, agents' recommendations. U1-a: K4 forbids only requiring or conditioning; agents may still name or recommend inspectors when asked. U1-b: naming a particular inspector is "steering"; agents may give clients only the Board's public list.

Horizons used: short = from introduction (12 January 2026) to 31 December 2027, including the application window (1 July to 31 December 2027); medium = 2028 to about 2030; long = after 2030.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 License | triangular (prohibits inspections for pay by the unlicensed) | Yes: 55% hold no certification, 40% no insurance, 34% cannot be grandfathered (A-1); deterrence depends on complaint-only enforcement (A-3) | 1 (unlicensed inspection removed where enforced); 3 (training, exam, insurance and fee attached to the option of inspecting; a risk of a fine attached to unlicensed inspection where it is not deterred, A-16); 3 (the 12-month lapse rule attaches requalification to leaving and returning) | CR-3a, CR-4, CR-5a, CR-6, CR-7, CR-9, CR-10, CR-11b, CR-11c |
| K2 Grandfathering | exemption (adds an option for qualifying incumbents) | Yes for the about 320 who qualify and for near-line inspectors who can reach the threshold (A-12) | 2 (license without training or exam); 3 before the window (each extra fee-paid inspection before the application date brings a chance of qualifying) | CR-4, CR-7c, CR-10a |
| K3 Enforcement on complaint | enforcement rule | Yes | 3 (penalty risk attached to unlicensed practice only where a buyer or agent is likely to complain); 3 (a complaint by an agent attaches an investigation risk to licensees' reports) | CR-4 (x: comply, y: violate), CR-6, CR-8c |
| K4 Agents | triangular (restricts agents' advice to clients) | U1-a: no change from current practice; U1-b: binding on the 70% of buyers who use agents' referrals (A-23) | U1-a: 1 only for requiring or conditioning (rare); U1-b: 1 (naming an inspector removed) | CR-1 per reading, CR-4, CR-9, CR-11c |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| inspectors.grandfathered | About 320 incumbents who meet K2, plus near-line inspectors who reach it | Op 2 (license without training); op 3 (insurance and fee); op 3 (12-month lapse rule). Rivals leave. |
| inspectors.near_line | About 80 part-timers and 60 late starters near the K2 threshold | Op 3 before the window: each extra inspection before applying raises the chance of qualifying. |
| inspectors.non_grandfathered | About 210 who began from 2025, and near-line inspectors who miss K2 | Op 1 unless they train and pass (op 3: $3,200, three weeks, exam, insurance, fee). |
| inspectors.part_time | Low-volume inspectors | Op 3: insurance and fee are about $50 per inspection at 40 a year. |
| inspectors.prospective | Would-be entrants | Op 3: training, exam, insurance, fee attached to entry; from 1 July 2027 op 1 without a license. |
| inspectors.linmouth | About 40 Linmouth inspectors working in the border metro | Op 3: the full license cost for a small Aldenmoor volume. |
| inspectors.unlicensed | Those who keep inspecting without a license | CR-4 (x: comply, y: violate) where complaint is unlikely: pre-listing, builders', border jobs. |
| engineers.exempt | About 35 professional engineers who inspect homes, and others who could | Exempt; through CR-9 (substitute) more demand. |
| buyers.inspections | Home buyers, sellers and builders who commission inspections | Through CR-9: fewer sellers, higher fees; a license as information; under U1-b no named recommendation. |
| buyers.engineering_services | Buyers of engineers' other work | Through CR-9: compete for engineers' time. |
| agents | Real-estate agents | U1-b: op 1 on naming inspectors; op 2: may file complaints that trigger investigations. |
| schools.training | Approved course providers | Through CR-9 (input_to): more students. |
| insurers | Writers of errors-and-omissions and liability cover | Through CR-9 (input_to): more policies. |
| officials.board | Home Inspector Board | Op 3: licensing and investigations; receives fees. |
| inspectors.association | The inspectors' association that campaigned for licensing | Its campaign's goal is met. |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1 and K2 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | inspectors | share_of_sellers_licensed | increase | medium; long | CR-1 op 1, CR-12 | A-3 |
| C-2 | inspectors | number_of_sellers | decrease | medium; long | CR-1 op 1, CR-4b, CR-12e | A-1, A-8 |
| C-3 | inspectors.non_grandfathered | employment (home inspection) | decrease | medium; long | CR-1 op 1 and op 3, CR-4b | A-1, A-3 |
| C-4 | inspectors.non_grandfathered | compliance_cost (training and exam) | increase | short | CR-1 op 3, CR-8c | A-2 |
| C-5 | inspectors | compliance_cost (license fee; insurance for those uninsured) | increase | medium; long | CR-1 op 3, CR-8c | A-27 |

## 5. Responses

CR-4 applied to every pair of options each actor class has; CR-6 where the number of sellers is restricted; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | inspectors.near_line | quantity_supplied (inspections before the application date) | increase | short (2027 to application) | CR-10a, CR-4 | A-12 |
| C-7 | buyers.inspections | price_paid (inspections by near-line inspectors in 2027) | decrease | short (2027 to application) | CR-4, CR-5c | A-12, A-13 |
| C-8 | inspectors.grandfathered | quantity_supplied (inspections by other inspectors in 2027) | decrease | short (2027 to application) | CR-9, CR-12e | A-12, A-14 |
| C-9 | inspectors.part_time | employment (home inspection) | decrease | medium; long | CR-4 (fixed cost per firm, 0.8), CR-4b | A-7 |
| C-10 | inspectors.prospective | entry_rate | decrease | short | CR-10a, CR-4 (x: stay out, y: enter) | A-1 |
| C-11 | inspectors.prospective | entry_rate | ambiguous | medium; long | CR-4, CR-7a, CR-12b | A-1, A-8 |
| C-12 | inspectors.linmouth | quantity_supplied (inspections in Aldenmoor) | decrease | medium; long | CR-4 (x: serve Aldenmoor, y: stay in Linmouth), CR-4a | A-28, A-3 |
| C-13 | inspectors.unlicensed | informal_activity (unlicensed inspections) | increase | medium; long | CR-4 (x: comply, y: violate), CR-6, CR-12 | A-16 |
| C-14 | inspectors.grandfathered | job_changes (temporary exits from inspection) | decrease | medium; long | CR-1 op 3, CR-4, CR-10b | A-15 |
| C-15 | inspectors.grandfathered | quantity_supplied (inspections per inspector) | increase | medium | CR-9, CR-4 | A-10 |
| C-16 | engineers.exempt | quantity_supplied (home inspections by engineers) | increase | medium; long | CR-9, CR-4 | A-19 |
| C-17 | engineers.exempt | quality_information (engineering license disclosed to home buyers) | increase | medium | CR-11c, CR-4 | A-21 |
| C-18 | agents, schools.training, insurers, inspectors.non_grandfathered | lobbying_effort (on U1, course rules and the requirements) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-17 |
| C-19 | inspectors.association | lobbying_effort | ambiguous | medium; long | CR-4, CR-12b | A-18, A-17 |
| C-20 | officials.board | enforcement_cost | increase | short; medium; long | CR-1 op 3, CR-8c | - |
| C-21 | officials.board | non_tax_receipts (license, exam and application fees) | increase | short; medium; long | CR-8b | - |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Effects of higher inspection fees on home prices and sales are pruned at depth 3 as diffuse (an inspection is a small part of a home purchase).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-22 | buyers.inspections | price_paid (inspection fees) | increase | medium; long | CR-6, CR-9, CR-12e | insurance and license input_to inspections | A-1, A-8 |
| C-23 | inspectors.grandfathered | net_price_received (per inspection) | increase | medium; long | CR-6, CR-7b | - | A-1, A-8 |
| C-24 | buyers.inspections | quantity_traded (inspections in the legal market) | ambiguous | medium; long | CR-4c, CR-11c, CR-12b | - | A-9, A-8, A-4, A-5 |
| C-25 | buyers.inspections | quality_per_unit (checks obtained by priced-out buyers) | decrease | medium; long | CR-4, CR-3a | substitutes: no inspection, unlicensed inspection | A-9, A-26 |
| C-26 | buyers.inspections | quality_information | U1-a: increase; U1-b: ambiguous | medium; long | CR-11c, CR-5c, CR-12b | - | A-4, A-5, A-27, A-6 |
| C-27 | buyers.inspections | quality_information (clients of unlicensed inspectors) | decrease | medium; long | CR-11b | - | A-16 |
| C-28 | buyers.inspections | search_cost (finding an inspector) | U1-a: no_change; U1-b: increase | medium; long | CR-1 per reading, CR-4 | - | A-23 |
| C-29 | inspectors.grandfathered | asset_value (inspection practices) | U1-a: increase; U1-b: ambiguous | short; medium | CR-7c (0.9), CR-10c, CR-12b | agents' referrals input_to inspection business | A-1, A-8, A-10, A-22 |
| C-30 | inspectors | quality_per_unit (licensed inspections) | ambiguous | medium; long | CR-4, CR-12b | agents' complaints (contract-like relation through the sale) | A-4, A-2, A-25, A-24 |
| C-31 | engineers.exempt | net_price_received (home inspections by engineers) | increase | medium; long | CR-9, CR-6 | engineers' inspections substitute for inspectors' (partial) | A-19, A-20 |
| C-32 | buyers.engineering_services | price_paid (engineers' other work) | increase | medium | CR-9, CR-7a | engineers' time input_to both (close) | A-19, A-20 |
| C-33 | schools.training | enrollment (approved home-inspection courses) | increase | short; medium; long | CR-9, LW-10, CR-12 | training input_to licensed inspection (close) | A-2 |
| C-34 | insurers | quantity_traded (errors-and-omissions and liability policies for inspectors) | increase | medium; long | CR-9, LW-10 | insurance input_to licensed inspection (close) | A-27 |
| C-35 | inspectors.non_grandfathered | employment (other work, mainly building trades) | increase | medium | CR-7a, CR-8a | labor input_to other trades | A-1, A-N1 |
| C-36 | buyers.inspections | resources_available_other_uses (buyers who keep buying inspections) | decrease | medium; long | CR-3, CR-8a | - | A-1, A-8 |
| C-37 | inspectors.grandfathered | resources_available_other_uses (fees received, net of license fee and insurance) | ambiguous | medium; long | CR-8b, CR-12b (two items, 0.8) | - | A-1, A-8, A-27 |
| C-38 | inspectors.non_grandfathered | resources_available_other_uses (those who train) | decrease | short | CR-3c, CR-8a | - | A-2 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| buyers.inspections, price_paid, short (2027) against medium; long | - | near-line inspectors cut fees to reach 250 (C-7) | Different windows (CR-12g) | decrease for near-line jobs in 2027 (C-7); increase from 2028 (C-22) |
| buyers.inspections, price_paid, medium; long | fewer sellers (CR-6, C-2); insurance and fee costs (CR-9); license conveys competence, raising buyers' valuation (CR-11c, A-4, A-5) | engineers and unlicensed inspectors add supply (C-16, C-13) | CR-12e response argument: the added supply is a response to the higher fee and cannot reverse it; A-8 states it is partial (0.9 note) | increase (C-22) |
| buyers.inspections, quantity_traded (legal market), medium; long | the license conveys competence buyers value and could not judge (CR-11c, A-4, A-5): demand rises | higher fees: marginal buyers go without or use unlicensed inspectors (A-9); U1-b: agents' information lost (A-6) | None | ambiguous (C-24) |
| buyers.inspections, quality_information, medium; long | the license and the Board list (A-4, A-5); insurance adds legal recourse (A-27) | U1-b only: agents' recommendations, which carried information, are lost (A-6) | None | U1-a: increase; U1-b: ambiguous (C-26) |
| inspectors, quality_per_unit, medium; long | training for those who qualify by exam (A-4, A-2); buyers' complaints after missed defects lead to discipline (A-25) | agents' complaints (or threats) against inspectors whose reports upset sales (A-24); grandfathered inspectors are licensed without training | None | ambiguous (C-30) |
| inspectors.grandfathered, asset_value | rivals leave and fees rise (A-1, A-8, A-10) | U1-b: business built on agents' referrals loses its channel (A-22) | None | U1-a: increase; U1-b: ambiguous (C-29) |
| inspectors.prospective, entry_rate, medium; long | higher fees for licensees (C-22) make entry more rewarding (CR-7a) | training, exam, insurance and fee attached to entry (CR-4, lumpy costs) | None | ambiguous (C-11); short: decrease (C-10) |
| inspectors.grandfathered, resources_available_other_uses | higher fees and volume (C-23, C-15) | license fee; insurance for those uninsured before (A-27) | None | ambiguous (C-37) |
| inspectors.association, lobbying_effort | defending the Act, seeking stricter terms | the campaign's goal is met | None (the counterfactual campaign continues, A-18) | ambiguous (C-19) |
| inspectors, number_of_sellers, medium; long | engineers enter (C-16) | incumbents and part-timers who cannot or will not qualify leave; Linmouth inspectors withdraw (C-3, C-9, C-12) | CR-12e response argument with A-8 (partial) | decrease (C-2) |

No chains cancel by construction (CR-12f).

## 8. Time structure

- **Announcement (12 January 2026 to 30 June 2027).** Entrants in this period know they must be licensed by 2028 and cannot be grandfathered, so fewer begin (C-10, CR-10a). Grandfathered inspectors' practices gain value as the Act becomes likely and then enacted (C-29, CR-7c probability clause).
- **Application window (1 July to 31 December 2027).** K2 tests experience "at the date of application", so near-line inspectors apply as late as possible and add inspections before then (C-6, A-12), mainly by cutting fees (C-7, A-13). Since total inspections are set by home sales (A-14), the extra jobs come from other inspectors (C-8). This is a timing shift signed per window: near-line inspectors' volume up in 2027 against the counterfactual; their fee cuts end once they apply. Over-statement of inspections in applications needs A-29 (p 0.45) and is not reported.
- **From 1 January 2028.** The about 210 who cannot be grandfathered have trained or stopped (C-3, C-4, C-38); part-timers leave as insurance and fee costs are spread over few jobs (C-9). The number of sellers is lower (C-2) and fees higher (C-22).
- **Durability.** Skills, tools and agent networks are a stock that changes only through flows (CR-10b): excluded inspectors' skills lose their use in inspection at once, while engineers' supply (C-16, C-31) expands only slowly (A-20). The 12-month lapse rule makes the license a stock that is lost by leaving, so grandfathered inspectors leave for spells less often (C-14); its effect grows as the grandfathered group would otherwise have aged and moved.
- **Enforcement drift.** Complaint-only enforcement deters unlicensed practice most where a buyer or agent would complain; pre-listing, builders' and border work are the least covered (C-13, A-16).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-4 | inspectors.non_grandfathered | compliance_cost (training and exam) | increase | About $3,200 and three weeks of work for each who trains | CR-1 op 3, CR-8c |
| C-5 | inspectors | compliance_cost (license fee; insurance for those uninsured) | increase | $250 a year each; about $1,800 a year for the 40% who were uninsured | CR-1 op 3, CR-8c |
| C-18 | agents, schools.training, insurers, inspectors.non_grandfathered | lobbying_effort | increase | Staff time and money spent on U1 and the requirements | CR-4, CR-8c |
| C-20 | officials.board | enforcement_cost | increase | Licensing staff and two investigators, paid from fees | CR-1 op 3, CR-8c |
| C-24 | buyers.inspections | quantity_traded (inspections in the legal market) | ambiguous | Inspections not bought by marginal buyers, against those bought because of the license | CR-5a, CR-4c, CR-11c |
| C-28 | buyers.inspections | search_cost | U1-a: no_change; U1-b: increase | Buyers' time finding an inspector without a recommendation | CR-4, CR-8c |
| C-36 | buyers.inspections | resources_available_other_uses | decrease | Purchases forgone by buyers who keep buying inspections at higher fees | CR-3, CR-8a |
| C-38 | inspectors.non_grandfathered | resources_available_other_uses | decrease | Tuition and earnings forgone during training | CR-3c, CR-8a |

CR-8 symmetry: the Board's fees (C-21) are paid by licensees (C-5); buyers' higher fees (C-36) are received by licensed inspectors and exempt engineers (C-23, C-31); prevented exchanges between buyers and excluded inspectors (C-3, C-9, C-12) deprive both of an expected gain (CR-5a).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | The requirements cost some current and would-be inspectors more than they would otherwise spend. | binding | 0.9 | 55% hold no certification; 40% carry no insurance; 34% cannot be grandfathered. | C-2, C-3, C-10, C-11, C-22, C-23, C-29, C-35 to C-37 fail. |
| A-2 | Some incumbents who cannot be grandfathered train and sit the exam to stay in practice. | other | 0.75 | Their investment in tools and agent networks; course capacity in 2027. | C-4, C-33, C-38 fail; C-30 loses a (+) chain. |
| A-3 | Despite complaint-only enforcement, unlicensed practice is deterred for most inspections: agents' forms and lenders ask for the license number, and buyers and agents complain. | enforcement | 0.7 | Agents' forms; lender practice; complaint rates elsewhere. | C-1, C-3, C-12 fail. |
| A-4 | The training and exam bear on competence that buyers value and cannot easily judge. | other | 0.65 | Syllabus; buyers' difficulty judging an inspection. | C-26 loses its (+) chain; C-24 becomes decrease; C-30 loses a (+) chain. |
| A-5 | Buyers and agents did not already know which inspectors had trained, passed an exam or were insured, and can see the license. | other | 0.7 | Inspectors' advertising; the Board's public list. | As A-4. |
| A-6 | Agents' recommendations conveyed information on competence that buyers cannot get otherwise. | other | 0.6 | Agents see many inspections. | C-26 under U1-b becomes increase. |
| A-7 | For some part-time inspectors, insurance and the fee exceed their margin, so they stop. | alternative_uses | 0.7 | $50 per inspection at 40 a year. | C-9 fails. |
| A-8 | Exempt engineers and unlicensed practice cannot replace the excluded supply at the old fee (the response is partial). | other | 0.75 | 35 engineers with other work; A-3. | C-2, C-22, C-23, C-36 lose their sign. |
| A-9 | Some buyers at the margin go without an inspection or use an unlicensed inspector when the fee rises. | substitutability | 0.6 | Cash investors; new homes with builders' warranties. | C-24 becomes increase; C-25 fails. |
| A-10 | Grandfathered inspectors stay in the occupation and their volume does not fall: rivals' exit takes away more inspections than buyers drop. | other | 0.65 | 210 who cannot be grandfathered against a small fall in inspections. | C-15, C-29 fail. |
| A-11 | Excluded inspectors' next-best work pays less in money. | other | 0.4 | Many came from building trades with similar pay. | Not reported. |
| A-12 | Some near-line inspectors would otherwise fall short of 250 inspections by their application date, and can find extra jobs. | other | 0.7 | About 80 part-timers and 60 late starters; agents' referrals. | C-6 to C-8 fail. |
| A-13 | They win the extra jobs mainly by cutting fees. | other | 0.55 | Price as the quickest margin. | C-7 fails. |
| A-14 | Total inspections in the window are set by home sales, not raised by the rush. | other | 0.75 | Inspections are bought for a sale. | C-8 fails. |
| A-15 | Some grandfathered inspectors would otherwise leave for a year or more and return. | mobility | 0.6 | Moves to building work in busy years. | C-14 fails. |
| A-16 | Some unlicensed practice continues where complaint is least likely. | enforcement | 0.7 | Pre-listing and builders' inspections; Linmouth inspectors in the border metro. | C-13, C-27 fail. |
| A-17 | Agents, schools and the inspectors' association can organize at a cost below their stake. | other | 0.85 | State associations exist. | C-18, C-19 fail. |
| A-18 | Without the Act, the inspectors' association would have kept lobbying for licensing. | counterfactual_trend | 0.7 | Its campaign since 2022. | C-19 becomes increase. |
| A-19 | Some exempt engineers add home inspections, and some buyers accept them. | substitutability | 0.6 | Engineers already inspecting. | C-16, C-31, C-32 fail. |
| A-20 | Engineers' supply cannot expand at unchanged cost in the period. | other | 0.65 | 35 engineers; their other work pays well. | C-31, C-32 fail. |
| A-21 | Some engineers did not tell home buyers of their engineering license before, and buyers now look for a license. | other | 0.55 | Engineers' advertising. | C-17 fails. |
| A-22 | Firms' business came largely through agents' recommendations, which lose their use under U1-b. | other | 0.7 | 70% of buyers use agents' referrals. | C-29 under U1-b becomes increase. |
| A-23 | Most buyers used agents' referrals, and under U1-b must search themselves. | other | 0.85 | Agents' survey. | C-28 fails. |
| A-24 | Some agents use, or threaten, complaints against inspectors whose reports upset sales. | other | 0.55 | Agents' commission depends on closing; complaints are costless. | C-30 becomes increase. |
| A-25 | Some buyers complain after missed defects, and discipline follows some complaints. | other | 0.8 | Complaint rates in other states. | C-30 loses a (+) chain. |
| A-26 | What priced-out buyers move to is of lower quality than the inspection replaced. | other | 0.6 | Going without; uninsured unlicensed inspectors. | C-25 fails. |
| A-27 | Some inspectors carried no insurance before. | other | 0.85 | 40% uninsured. | C-5 (insurance part), C-34 fail; C-26 loses a chain. |
| A-28 | Most Linmouth inspectors serving Aldenmoor do too few jobs there to cover the license's costs. | alternative_uses | 0.65 | About 40 inspectors; 12% of sales in the border metro. | C-12 fails. |
| A-29 | Some grandfather applicants overstate their inspections, and the Board, checking on paper and acting otherwise only on complaint, misses it. | enforcement | 0.45 | Reports are the evidence; no audit power. | Not reported. |
| A-30 | Holders of the national certification drop it, and it conveyed more about competence than the license does. | other | 0.35 | 100 hours against 120; continuing education. | Not reported. |
| A-N1 | Inspectors who leave inspection because of the license find other paid work, mainly in building trades. | alternative_uses | 0.7 | NEW. Many came from building trades (A-11's evidence); trades' demand. | C-35 fails. |

**Not reported** (an assumption below 0.5):
- Excluded inspectors earn less in money in their next-best work (CR-7b, CR-7 0.9 note): needs A-11 (p 0.4). That they are worse off by their own ranking is a priori (CR-3a), but it has no variable.
- Grandfather applications overstate experience and are approved (CR-4, x: report honestly, y: overstate): needs A-29 (p 0.45).
- Buyers lose information as holders drop the national certification (CR-11c): needs A-30 (p 0.35).

## 11. Report

**The policy:** From 1 July 2027 no one may begin inspecting homes for pay in Aldenmoor without a license (120 hours of training, an exam, $300,000 of insurance, $250 a year), and from 1 January 2028 every inspector must hold one. Inspectors with three years of practice and 250 fee-paid inspections at the date they apply (1 July to 31 December 2027) are licensed without training or exam. Engineers and architects are exempt. The Board investigates only on a complaint by a buyer or an agent. Agents may not "direct, steer or require" clients to use a particular inspector (U1).

**Visible consequences:** Almost all legal inspectors are licensed (C-1); fewer people inspect homes (C-2), including many of the about 210 recent entrants who cannot be grandfathered (C-3); those who stay pay training, insurance and fees (C-4, C-5). The Board collects fees (C-21) and spends them on licensing and investigations (C-20).

**Invisible consequences:**
- *Buyers:* Fees rise from 2028 (C-22), and buyers who keep buying inspections have less for other things (C-36). Buyers priced out get a lesser check or none (C-25). Clients of unlicensed inspectors lose recourse (C-27). Under U1-b, buyers must find inspectors themselves (C-28).
- *Inspectors:* Near-line inspectors rush to reach 250 inspections before applying, cutting fees and taking jobs from others in 2027 (C-6 to C-8). Part-timers and Linmouth inspectors withdraw (C-9, C-12). Grandfathered inspectors receive higher fees and more jobs (C-23, C-15) and leave for spells less often because a lapsed license is costly to restore (C-14). Fewer start in the run-up (C-10). Excluded inspectors move to other work (C-35); those who train bear tuition and lost earnings (C-38).
- *Others:* Exempt engineers inspect more homes at higher fees (C-16, C-31) and advertise their license (C-17), so their other clients pay more (C-32). Course enrollment and insurance policies rise (C-33, C-34). Some unlicensed practice continues where no one is likely to complain (C-13). Agents, schools, insurers and excluded inspectors lobby (C-18).

**Ambiguous effects:** The number of inspections in the legal market (the license makes inspections worth more to buyers who could not judge competence; higher fees drive marginal buyers out; C-24). Buyers' information under U1-b (the license against the loss of agents' recommendations; C-26). The quality of licensed inspections (training and buyers' complaints against agents' complaints and untrained grandfathered inspectors; C-30). Grandfathered practices' value under U1-b (C-29). Entry after 2028 (C-11). Grandfathered inspectors' net receipts (C-37). The association's lobbying (C-19).

**Key conditions:** The requirements bind (A-1, 0.9); complaint-only enforcement still deters most unlicensed practice (A-3, 0.7); substitutes are partial (A-8, 0.75), which signs fees; the license conveys competence buyers value and did not know (A-4, 0.65; A-5, 0.7), which makes demand and information ambiguous rather than lower; near-line inspectors find extra jobs by cutting fees (A-12, 0.7; A-13, 0.55). One premise was added: excluded inspectors find other work (A-N1, 0.7).

**What this analysis cannot say:** How large any effect is; whether buyers on balance gain from the information the license conveys more than they lose from higher fees; whether the quality of inspections rises; whether the Act is good. Effects on the safety of homes are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | inspectors | share_of_sellers_licensed | increase | medium; long | visible | B | CR-1 (op 1: K1 removes unlicensed inspection where enforced, A-3); CR-12 (0.9: no licenses exist in the counterfactual) | A-3 |
| C-2 | inspectors | number_of_sellers | decrease | medium; long | visible | B | CR-1 (op 1 for those who do not qualify; op 3 for all); CR-4b (those for whom inspection ranked only narrowly above other work, including many who must train, leave; CR-4 lumpy costs); (+) engineers enter (C-16): CR-12e response argument, partial by A-8 | A-1, A-8 |
| C-3 | inspectors.non_grandfathered | employment (home inspection) | decrease | medium; long | visible | B | CR-1 (op 1 unless they train; op 3: $3,200, three weeks, exam with a 70% pass rate); CR-4b (those for whom inspection was narrowly preferred stop; CR-4a: none start because of the cost); deterrence (A-3) | A-1, A-3 |
| C-4 | inspectors.non_grandfathered | compliance_cost (training and exam) | increase | short | visible | B | CR-1 (op 3: training and exam attached to continuing); some train (A-2); CR-8c (used up) | A-2 |
| C-5 | inspectors | compliance_cost (license fee; insurance for those uninsured) | increase | medium; long | visible | B | CR-1 (op 3: $250 a year for all; insurance for the 40% uninsured, A-27); CR-8c | A-27 |
| C-6 | inspectors.near_line | quantity_supplied (inspections before the application date) | increase | short (2027 to application) | invisible | B | CR-10a (qualifying depends on inspections done by the application date); CR-4 (x: normal pace, y: extra jobs; y now brings a license without training); A-12 | A-12 |
| C-7 | buyers.inspections | price_paid (inspections by near-line inspectors in 2027) | decrease | short (2027 to application) | invisible | B | CR-4 (near-line inspectors offer better terms to win extra jobs, A-13); CR-5c (any change in what one party may receive moves the range of terms) | A-12, A-13 |
| C-8 | inspectors.grandfathered | quantity_supplied (inspections by other inspectors in 2027) | decrease | short (2027 to application) | invisible | B | CR-9 (competitors for the same customers); total inspections fixed by home sales (A-14), so the near-line rush (C-6) takes jobs from others | A-12, A-14 |
| C-9 | inspectors.part_time | employment (home inspection) | decrease | medium; long | invisible | B | CR-4 (0.8: a cost fixed per firm, insurance and fee, bears on whether a firm operates; at 40 inspections a year it is about $50 each); CR-4b (A-7) | A-7 |
| C-10 | inspectors.prospective | entry_rate | decrease | short | invisible | B | CR-10a (entrants in 2026 to mid-2027 know they must be licensed by 2028 without grandfathering); CR-4 (x: stay out, y: enter; y made worse by the coming training, exam and insurance) | A-1 |
| C-11 | inspectors.prospective | entry_rate | ambiguous | medium; long | invisible | B | CR-12b: (-) CR-4 (training, exam, insurance and fee attached to entry); (+) CR-7a (higher fees for licensees, C-22, draw entrants). No dominance premise | A-1, A-8 |
| C-12 | inspectors.linmouth | quantity_supplied (inspections in Aldenmoor) | decrease | medium; long | invisible | B | CR-4 (x: serve Aldenmoor with the full license cost, y: stay in Linmouth; A-28: their Aldenmoor volume does not cover the cost); CR-4a; deterrence (A-3) | A-28, A-3 |
| C-13 | inspectors.unlicensed | informal_activity (unlicensed inspections) | increase | medium; long | invisible | B | CR-4 (x: comply, y: violate; K3 attaches a penalty risk only where a buyer or agent may complain); CR-6 (the higher licensed fee is pressure toward the exchange outside the rule); CR-12 (0.9: none exist without the Act); A-16 | A-16 |
| C-14 | inspectors.grandfathered | job_changes (temporary exits from inspection) | decrease | medium; long | invisible | B | CR-1 (op 3: a license not renewed for 12 months must be re-earned by training and exam); CR-4 (x: leave for a year and return, y: stay or keep renewing; x made worse); CR-10b (the license is a stock lost by leaving); A-15 | A-15 |
| C-15 | inspectors.grandfathered | quantity_supplied (inspections per inspector) | increase | medium | invisible | B | CR-9 (rivals' exit, C-2, sends their customers to remaining inspectors); CR-4; A-10 (more than buyers drop) | A-10 |
| C-16 | engineers.exempt | quantity_supplied (home inspections by engineers) | increase | medium; long | invisible | B | CR-9 (relation: engineers' inspections substitute for inspectors'; demand moves to them as fees rise); CR-4 (x: other engineering work, y: home inspections); A-19 | A-19 |
| C-17 | engineers.exempt | quality_information (engineering license disclosed to home buyers) | increase | medium | invisible | B | CR-11c (a policy that makes a license the expected credential changes what buyers look for); CR-4 and CR-11 (0.9, sellers' response: exempt sellers who compare well disclose); A-21 | A-21 |
| C-18 | agents, schools.training, insurers, inspectors.non_grandfathered | lobbying_effort (on U1, course rules and the requirements) | increase | short; medium | invisible | B | CR-4 (x: accept, y: lobby; each has a concentrated stake: agents in U1, schools in course hours, insurers in the cover, excluded inspectors in the grandfather terms); CR-8c; A-17 | A-17 |
| C-19 | inspectors.association | lobbying_effort | ambiguous | medium; long | invisible | B | CR-4 against a counterfactual in which the campaign continues (A-18): (-) the goal is met; (+) defending or tightening the Act. CR-12b: no dominance premise | A-18, A-17 |
| C-20 | officials.board | enforcement_cost | increase | short; medium; long | invisible | A | CR-1 (op 3: licensing, exam, grandfather review and investigations); CR-8c | none |
| C-21 | officials.board | non_tax_receipts (license, exam and application fees) | increase | short; medium; long | invisible | A | CR-8b (fees paid by applicants and licensees, C-5, are received by the Board) | none |
| C-22 | buyers.inspections | price_paid (inspection fees) | increase | medium; long | visible | B | CR-6 (fewer sellers, C-2: buyers' pressure moves the fee toward a higher clearing level); CR-9 (insurance and license fees are added costs, input_to inspections); CR-11c (the license raises some buyers' valuation, A-4, A-5, same direction); (-) engineers and unlicensed supply respond: CR-12e response argument, partial by A-8 (0.9 note) | A-1, A-8 |
| C-23 | inspectors.grandfathered | net_price_received (per inspection) | increase | medium; long | invisible | B | CR-6 (as C-22); CR-7b (the gain from a restriction settles on those inside it who cannot be replaced at the old fee, A-8) | A-1, A-8 |
| C-24 | buyers.inspections | quantity_traded (inspections in the legal market) | ambiguous | medium; long | invisible | B | CR-12b (kind 2): (-) CR-4c (at a higher fee marginal buyers go without or go unlicensed, A-9, A-8); (+) CR-11c (the license conveys competence that buyers value and could not judge, A-4, A-5, so more buyers commission an inspection). No dominance premise | A-9, A-8, A-4, A-5 |
| C-25 | buyers.inspections | quality_per_unit (checks obtained by priced-out buyers) | decrease | medium; long | invisible | B | CR-4 (x: licensed inspection at the higher fee, y: none or unlicensed; marginal buyers switch, A-9); the alternative is worse (A-26) | A-9, A-26 |
| C-26 | buyers.inspections | quality_information | U1-a: increase; U1-b: ambiguous | medium; long | invisible | B | U1-a: CR-11c (the license and the Board's list convey training and an exam that buyers could not see, A-4, A-5); CR-5c (required insurance adds legal recourse to the terms, A-27); all (+). U1-b: the same (+) chains; (-) CR-1 op 1 on agents and CR-11c (agents' recommendations carried competence information, A-6). CR-12b: no dominance premise | A-4, A-5, A-27, A-6 |
| C-27 | buyers.inspections | quality_information (clients of unlicensed inspectors) | decrease | medium; long | invisible | B | CR-11b (an exchange moved outside the legal market loses certification, reputation and legal recourse); unlicensed practice continues (A-16) | A-16 |
| C-28 | buyers.inspections | search_cost (finding an inspector) | U1-a: no_change; U1-b: increase | medium; long | invisible | B | U1-a: CR-1 (agents may still recommend). U1-b: CR-1 (op 1: agents may give only the list); CR-4 (most buyers used referrals and must search themselves, A-23); CR-8c | A-23 |
| C-29 | inspectors.grandfathered | asset_value (inspection practices) | U1-a: increase; U1-b: ambiguous | short; medium | invisible | B | CR-7c (0.9: assets without a market price; the practice's expected yield rises as rivals leave and fees rise, C-22, C-15, captured by its holder when it becomes expected); CR-10c. U1-b: (-) the referral channel loses its use (A-22); CR-12b: no dominance premise | A-1, A-8, A-10, A-22 |
| C-30 | inspectors | quality_per_unit (licensed inspections) | ambiguous | medium; long | invisible | B | CR-12b: (+) training for those licensed by exam (A-2, A-4); (+) CR-4 (x: careless report, y: careful report; discipline after buyers' complaints, A-25); (-) CR-4 (x: report defects fully, y: soften; K3 lets agents trigger investigations, A-24); grandfathered inspectors are licensed untrained (no chain). No dominance premise | A-4, A-2, A-25, A-24 |
| C-31 | engineers.exempt | net_price_received (home inspections by engineers) | increase | medium; long | invisible | B | CR-9 (relation: substitute; demand moves to engineers, A-19); CR-6 (their supply cannot expand at unchanged cost, A-20, so the price takes part of the shift) | A-19, A-20 |
| C-32 | buyers.engineering_services | price_paid (engineers' other work) | increase | medium | invisible | B | CR-9 (relation: engineers' time input_to home inspections and to their other work); CR-7a (engineers' time moves to inspections until yields are equal, raising the price of the other work, A-20). Depth 4: chain stops | A-19, A-20 |
| C-33 | schools.training | enrollment (approved home-inspection courses) | increase | short; medium; long | invisible | B | CR-9 and LW-10 (relation: training input_to licensed inspection; incumbents who train, A-2, and all entrants by exam); CR-12 (0.9: no approved courses exist without the Act) | A-2 |
| C-34 | insurers | quantity_traded (errors-and-omissions and liability policies for inspectors) | increase | medium; long | invisible | B | CR-9 and LW-10 (relation: insurance input_to licensed inspection; the uninsured must buy it, A-27) | A-27 |
| C-35 | inspectors.non_grandfathered | employment (other work, mainly building trades) | increase | medium | invisible | B | CR-7a (labor moves to the uses still open); CR-8a (labor withdrawn from inspection goes to other uses); A-N1 | A-1, A-N1 |
| C-36 | buyers.inspections | resources_available_other_uses (buyers who keep buying inspections) | decrease | medium; long | invisible | B | CR-3 (note: falls for those who keep buying the burdened option at the higher fee, C-22); CR-8a | A-1, A-8 |
| C-37 | inspectors.grandfathered | resources_available_other_uses (fees received, net of license fee and insurance) | ambiguous | medium; long | invisible | B | CR-12b (0.8, two items): (+) CR-8b (higher fees and volume received, C-23, C-15); (-) CR-8b (license fee to the Board, C-21; insurance for those uninsured, A-27). No dominance premise | A-1, A-8, A-27 |
| C-38 | inspectors.non_grandfathered | resources_available_other_uses (those who train) | decrease | short | invisible | B | CR-3c and CR-8a (tuition and three weeks' earnings are paid by those who train to continue, A-2) | A-2 |

## Gaps found

**(a) Calculus gaps.**
- GAP-055-C1. A rule that tests eligibility "at the date of application" within a window (K2) makes the applicant choose the date. CR-10a covers the rush, but no core rule addresses an actor choosing when a test is applied to them; it was handled as CR-4 over dates (section 8).
- GAP-055-C2. Complaint-only enforcement (K3) gives a private party (agents) the power to trigger sanctions against another (inspectors) with whom it has a commercial interest in the outcome of the inspection. CR-1 op 3 and CR-4 give the inspector's direction, but CR-9 has no relation type for "can trigger enforcement against", so the link in C-30 was named loosely.

**(b) Core-rule wording that was hard to apply.**
- CR-11c with CR-12b: the license as a signal raises buyers' valuation, which pushes the legal quantity up while the fee pushes it down (C-24). CR-11's 0.7 note asks for two premises (prior beliefs and direction); both were in the case (A-4, A-5), so the opposing chain is kind 2 and makes the quantity ambiguous. The rules do not say whether information effects should be treated as a demand shift in CR-6 terms; it was treated as one.
- CR-7a for entry under a lumpy entry cost (C-11): CR-4's lumpy-cost note covers the cost side, and CR-7a the yield side, but no wording says how to sign an entry flow (as against the stock of sellers) when both move; left ambiguous.
- CR-4's 0.9 note on lobbying against a contested baseline is written for repeals; it was applied by analogy to the association's lobbying after enactment (C-19).

**(c) Vocabulary missing from the ontology.**
- No variable for occupational exit and return (spells out of an occupation); `job_changes` was used for C-14.
- No variable for whether a seller discloses a credential; `quality_information` was used with the engineers as the actor class (C-17), although the ontology defines it from the buyer's side.
- No variable for a credential's own value to the holder (a non-transferable license); CR-7's 0.9 note on assets without a market price was applied with `asset_value` on the practice (C-29).
- Safety of homes and health effects of missed defects are out of scope.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on most of the Aldenmoor case. Inspectors bear training, exam, insurance and fee costs. Every legal inspector is licensed, and fewer inspect. Fees rise with A-8 as the partial-response premise, and licensees receive more per inspection. Near-line inspectors rush to reach 250 inspections at their rivals' expense. Grandfathered inspectors leave for spells less often. Unlicensed practice appears where no one likely to complain is the client. Engineers inspect more, at higher fees, and disclose their license. Linmouth inspectors withdraw, and insurers sell more policies. Buyers who keep buying have less for other uses. Under U1-b buyers search more. Information is `increase` under U1-a and `ambiguous` under U1-b in both, and so are the values of practices and firms. The association's lobbying is `ambiguous`, and quality received is `ambiguous`. Both versions reject the baselines of EN-11's 0.9 Unless and of RS-20, the core version without the prompt of either pattern. There are two S rows. On legal inspections bought (pattern C-7 decrease, core C-24 ambiguous), the core's opposing chain lacks the direction premise CR-11 requires, so the pattern's sign stands. On entry after 2028 (pattern C-4 decrease, core C-11 ambiguous), both readings are defensible. The core version omits the cost of grandfather applications, licensees' cost of answering complaints and a general training-enrollment key. The pattern version omits what clients of unlicensed inspectors lose in information and recourse, engineers' other clients, trainees' means and excluded inspectors' other work. It also counts insurance as a new cost for all inspectors, although 60% were already insured.

Counts: M 19, V 7, S 2, OP 7, OC 3.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-4, C-5 | V | | Split into training and exam (C-4) and fee and insurance (C-5). The core restricts insurance to the 40% who were uninsured (A-27). The pattern's "insurance ... for all" overstates: for the insured 60% insurance is not a new cost. |
| C-2 | C-1 | M | | The core's horizon omits `short`, though licenses exist from July 2027. |
| C-3 | C-26 | M | | Same signs per reading. The core adds required insurance as a (+) chain (legal recourse), which is a term of the exchange (CR-5c) rather than information. The sign is unaffected. |
| C-4 | C-10, C-11 | S | J | Short horizon: both `decrease` (CR-10a; the line was fixed before the announcement). Medium and long: the pattern gives `decrease` (EN-1, lumpy cost); the core gives `ambiguous` (C-11). In the core, the higher fee (C-22) draws entrants by CR-7a against the entry cost (CR-4). Both are defensible. The pattern's own C-6 and C-8 establish the fee rise and do not combine it with entry. Once some 210 incumbents leave at one date, a refill above the counterfactual flow in the medium run is a derivable kind 2 chain. In the long run, entry replaces exits from a smaller stock that leaves less often (C-14/C-16), so `decrease` is derivable with a premise on exit rates. Neither version split the horizons this way. |
| C-5 | C-2 | M | | The core also records the subclasses (C-3, C-9) as their own rows. |
| C-6 | C-22 | M | | The core adds two (+) chains: the insurance and fee costs (CR-9) and the license's information (CR-11c). |
| C-7 | C-24 | S | E | Pattern: legal inspections `decrease` (CR-4c with A-9). Core: `ambiguous`, with a (+) chain in which the license conveys competence, so more buyers commission an inspection (CR-11c; A-4, A-5). CR-11 0.7 asks for two premises, prior belief and direction. A-4 and A-5 give the first and that the license tells buyers something. Neither says that buyers who learn it buy more inspections rather than choose among inspectors, when about 54,000 of 68,000 buyers already inspect. The core's chain therefore lacks its direction premise. As a kind 2 chain it needs that premise with a probability; as stated it is not a chain, and the pattern's `decrease` stands. Core-version error. The pattern's variable, "licensed inspections", should read "legal inspections": against a no-license counterfactual, licensed inspections increase from none. |
| C-8 | C-23 | M | | The core signs grandfathered inspectors only; the pattern also covers non-grandfathered inspectors who qualify. Same derivation. |
| C-9 | C-15, C-23 | V | | Grandfathered inspectors' fee income `increase` (price up, C-23; volume up on A-10, C-15). The core records the components but not `earnings`. It adds the net after the license fee and insurance as `ambiguous` (C-37). |
| C-10 | C-6 | M | | The core's window starts in 2027; the pattern's in January 2026. The rush begins from the announcement, so the core's window is too narrow. |
| C-11 | C-7 | V | | Sellers' `net_price_received` (pattern) against buyers' `price_paid` for near-line jobs (core). The pattern signs January 2026 to June 2027 and declines July to December 2027, where entry closes and the market fee starts to rise. The core signs all of 2027 to the date of application, so it does not combine that opposing chain in the later window. The pattern's split is more exact. |
| C-12 | C-8 | M | | |
| C-13 | C-33 | M | | 2027 enrollment in approved courses. The core also signs approved-course enrollment `increase` in the medium and long run, which holds by CR-12 0.9 (no approved courses without the Act). |
| C-14 | none | OC | J | Training enrollment in general (including the voluntary certification) from 2028 is `ambiguous`: every entrant trains, but fewer enter. The core recorded only approved courses, a different key that is trivially `increase`. Nothing scorable lost. |
| C-15 | none | OC | E | Grandfather applicants' `compliance_cost` (documenting 250 inspections) `increase`, Tier A (CR-1 op 3, CR-8c). Core-version omission; the core counts only the Board's side of the review (C-20). |
| C-16 | C-14 | M | | |
| C-17 | C-13 | M | | Both sign against none (CR-12 0.9); neither uses RS-20's baseline. |
| C-18 | C-18 | M | | The core adds insurers and excluded inspectors. |
| C-19 | C-19 | M | | |
| C-20 | C-16 | V | | `quantity_substitute` against `quantity_supplied`. |
| C-21 | C-31 | V | | Buyers' `price_substitute` against engineers' `net_price_received`. Same premises (A-19, A-20). |
| C-22 | C-17 | M | | |
| C-23 | C-12 | M | | |
| C-24 | C-29 | V | | Same signs per reading. The pattern has multi-inspector firms (sellable); the core has grandfathered inspectors' practices (CR-7c 0.9). |
| C-25 | C-28 | M | | |
| C-26 | C-25, C-30 | V | | The pattern gives quality received by all buyers `ambiguous`. The core splits it: priced-out buyers' checks `decrease` (A-9, A-26; C-25), and licensed inspections `ambiguous` (C-30). The two records are consistent. |
| C-27 | C-34 | M | | |
| C-28 | none | OC | E | Licensees' `compliance_cost` of answering complaints, genuine or strategic, `increase` (CR-8c; CR-12 0.9, complaints exist only under the Act; A-25). Core-version omission. The core uses the same complaints for the quality chains in C-30. |
| C-29 | C-36 | M | | |
| C-30 | C-20 | M | | |
| C-31 | C-21 | M | | The core omits fines from the receipts; the pattern includes them. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-3 | OP | J | Non-grandfathered inspectors' home-inspection `employment` decreases. This is a subclass of the exit the pattern records as `number_of_sellers` (C-5) and describes in its text. It adds no sign. |
| C-9 | OP | J | Part-timers' `employment` decreases (CR-4 0.8, a cost fixed per firm; A-7). The pattern carries it inside C-5 with A-7. It adds no sign. |
| C-27 | OP | E | Clients of unlicensed inspectors have less `quality_information` (CR-11b): an exchange outside the legal market loses certification, agents' referrals (agents may complain) and recourse in the courts, all of which the same exchange had in the counterfactual. The pattern declined RS-10 because "unlicensed inspectors still advertise", which the record does not say. Even if true, it leaves the other channels lost. Pattern-version omission. |
| C-32 | OP | E | Engineers' other clients pay more (CR-9, CR-7a; A-19, A-20). Derivable at depth 3 on the pattern's own premises. Pattern-version omission. |
| C-35 | OP | A | Excluded inspectors' `employment` in other work increases, given A-N1 (they find other paid work). The pattern did not consider it. It needs the core's added premise, since an excluded inspector may also not work. |
| C-37 | OP | J | Grandfathered inspectors' means, net of the license fee and insurance, `ambiguous` (CR-12, 0.8, two items). Defensible. The pattern signed gross fee income (C-9), a different variable. |
| C-38 | OP | E | Non-grandfathered inspectors who train have less for other uses: they pay tuition and give up three weeks' earnings, and they keep the burdened option (CR-3 note). Pattern-version omission. It records the cost (C-1) but not its effect on means. |

### Findings

- **Pattern overclaims or hidden premises.** *EN-11 0.9 Unless* applied as written would sign `quality_information` down for buyers of grandfathered inspectors. Its decrease is against a single-requirement license, not against no license. The pattern version overrode it, and the core version, using CR-11c alone, reached the same `increase` under U1-a. *RS-20* compares with uniform enforcement, not with the no-policy counterfactual. The pattern overrode it, and the core reached `informal_activity` `increase` against none from CR-4 and CR-12 0.9, without the pattern. *EN-1* signs `entry_rate` decrease without the opposing chain from the higher price it also derives. Where a license removes part of the stock at one date, the medium-run refill is a derivable chain (C-4, J). *TS-5's* grandfathering clause would have suggested a rush to enter; the core derived "no rush" from CR-10a, as the pattern did by overriding it. *EN-2* has no variable or clause for an unsellable license (Gaps c5); the core also had to use `asset_value` on the practice. Pattern C-1 counts insurance as a new cost for all inspectors without A-27.
- **Errors in the core version.** Legal inspections bought (C-24) are made `ambiguous` by an information chain that lacks CR-11 0.7's direction premise (S, E). Near-line fees (C-7) are signed through July to December 2027 without combining the rising market fee. The near-line rush (C-6) starts its window in 2027, not at the announcement. Omissions: applicants' compliance cost (pattern C-15), licensees' cost of answering complaints (C-28), and fines in the Board's receipts. Required insurance is listed as an information chain (C-26), though it is a term of the exchange.
- **Errors in the pattern version.** Omissions: what unlicensed inspectors' clients lose (core C-27), declined on a fact the record does not contain; engineers' other clients (C-32); trainees' means (C-38); excluded inspectors' other work (C-35, which needs a premise). Insurance is counted as new for the 60% already insured (C-1). The variable "licensed inspections" (C-7) should be "legal inspections" against a no-license counterfactual. On lobbying (C-18), the counterfactual has the association's continuing licensing campaign. Whether agents and schools would have lobbied on such bills there is a premise the pattern asserts ("neither lobbied on this question") without evidence. This is a weaker form of the point the pattern itself makes for the association (C-19).
- **Test of 0.9 verdicts.** *EN-11 0.9 Unless (needed interpretation; listed as a failure in 6.2g):* confirmed. Without the clause, the core version signed information from CR-11c against no license, with the same signs per reading. *RS-20 (needed interpretation, sign overridden; listed as a failure in 6.2g):* confirmed. The core signed unlicensed practice against none, with the counterparty distribution as text (section 8). It also found that the bargaining-threat and strategic-complaint clauses rest on a relation CR-9 does not name (GAP-055-C2). *RS-17 for a line in time and count with the burden below it (needed interpretation):* confirmed. The core derived the rush to the line directly from CR-10a and CR-4 (C-6 to C-8), with no threshold pattern. It found one point the pattern handled only as a path note: the applicant chooses the date of the test (GAP-055-C1). *CR-7 0.9 for stayers (needed extension):* confirmed. The core needed A-10 for stayers' volume and did not sign money earnings net of costs (C-37), which supports the pattern's point that "next-best use" is the wrong premise for holders who stay. *RS-7 0.9 by symmetry for an imposition:* confirmed; the core applied CR-4 0.9 by the same analogy (C-19). *RS-8 0.9 for a rush whose second side is rivals in the same window (needed interpretation):* confirmed. The core derived the rivals' loss from CR-9 with A-14 (C-8). *TS-5 (Gaps c4):* confirmed by core C-10.
- **Limits of the core rules.** None produced a difference: no S, OP or OC row has cause K. Unclear core-rule wording: (1) CR-11 0.7 with CR-6: whether information conveyed by a policy is to be treated as a shift in demand for the quantity bought, and what the direction premise must then say (C-24). (2) CR-7 0.9: "a premise about the holder's next-best use" fits those excluded, not holders who stay, for whom the premise is about volume. (3) CR-4 0.9 on lobbying names repeals only. (4) CR-4's lumpy-cost note and CR-7a do not say how to sign an entry flow, as against the stock, when the cost and the yield both rise (C-11). (5) CR-10a does not cover an actor choosing the date at which a test is applied to them (GAP-055-C1). (6) CR-9 has no relation for a party that can trigger enforcement against another (GAP-055-C2). (7) CR-12 0.8, kind 2, does not say whether a chain that needs two premises takes their joint probability (A-30).
