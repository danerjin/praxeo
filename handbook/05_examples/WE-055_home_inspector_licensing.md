# WE-055 Home inspector licensing with grandfathering and complaint-only enforcement

Analyst: draft (Handbook 0.9 held-out test, corrected under 1.0)  |  Rule catalog version: 1.0  |  Status: awaiting expert review

A stylized policy in a fictional state. It resembles real home inspector licensing laws but is not modeled on any one of them. It was written as a held-out test of catalog 0.9, whose changes were drawn from WE-036 to WE-045. It probes: the licensing patterns EN-1 to EN-4 on a market where most buyers find their inspector through a real-estate agent; EN-11 with its 0.9 Unless clause, where the license is issued on one requirement for newcomers but on experience for incumbents, and the counterfactual is no license at all; RS-20 (complaint-only enforcement, promoted in 0.9), where only buyers and agents may complain; RS-17 applied to a grandfathering line drawn in time (three years and 250 inspections, measured at application); CR-7's 0.9 clause on assets that cannot be sold (a license, a grandfathered status), where money earnings need a premise; RS-7 and RS-8 with their 0.9 clauses, including a rush to qualify for grandfathering; and CR-11's 0.9 clauses on what sellers do when buyers read a missing license. Health and safety effects of inspection quality (defects found or missed) are outside the scope of version 1, except as the quality of the service buyers receive. The probabilities are illustrative; the evidence column says what a real analysis would cite. After its core-only comparison (`05_examples_core/WE-055_home_inspector_licensing_core.md`) it was corrected under catalog 1.0; the changes are listed before "Gaps found", and part (e) of "Gaps found" keeps the 0.9 verdicts as first recorded.

## 1. Policy record

**Aldenmoor Home Inspector Licensing Act.** The State of Aldenmoor has about 68,000 home sales a year. About 54,000 buyers commission a pre-purchase inspection; sellers commission about 4,000 pre-listing inspections, and builders and buyers about 3,000 inspections of new homes under construction: about 61,000 inspections a year. The average fee is about $450. About 610 people inspect homes for pay. About 400 began practice before 1 January 2025 (they will have three years of practice by 31 December 2027); of these, about 320 will have at least 250 fee-paid inspections in the three years before that date at their present pace, about 60 began practice between 1 July 2024 and 31 December 2024 and reach three years only during the application window, and about 80 are part-timers with three years or more but a pace of 40 to 80 inspections a year. About 210 began on or after 1 January 2025 and cannot reach three years by 31 December 2027. About 70 people enter a year and about 50 leave. About 45% of inspectors hold a voluntary national certification (100 hours of training and an exam); about 40% carry no errors-and-omissions or liability insurance. About 35 licensed professional engineers inspect homes. A state survey of agents finds that about 70% of buyers hire an inspector their agent recommended.

Approved training will cost about $3,200 in tuition and about three weeks of time; the exam about $200, with an expected pass rate of about 70%; the required insurance ($300,000 of errors-and-omissions and general liability cover) about $1,800 a year; the license fee $250 a year. The neighboring State of Linmouth has no license; about 12% of Aldenmoor's sales are in the Brask River metro on the border, where about 40 Linmouth inspectors do some Aldenmoor jobs.

The bill was introduced on 12 January 2026 and enacted on 3 June 2026. Training courses are approved from 1 January 2027 and the exam is offered from March 2027. From 1 July 2027 no one may begin practice without a license; those in practice on that date may continue until 31 December 2027; from 1 January 2028 every inspector must hold a license. No expiry.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Inspections of residential property in Aldenmoor, wherever the inspector lives. Linmouth, across the Brask River, has no license. | Act, s. 2. |
| Announced / enacted / effective / expires | Introduced 12 January 2026; enacted 3 June 2026; new entrants need a license from 1 July 2027; everyone from 1 January 2028; grandfather applications 1 July to 31 December 2027; no expiry. | Act, s. 3, 9, 14. |
| Enforcement (who, penalties, resources) | Home Inspector Board, two investigators, funded by license, exam and application fees. Unlicensed practice: fine up to $2,500 per inspection. Licensees: suspension or revocation. "The Board shall investigate an alleged violation of this Act only upon a written complaint by a buyer of residential property or by a licensed real-estate agent." | Act, s. 10 to 12. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 License | `licensing_requirement` | Home inspection for pay | Anyone inspecting a home in Aldenmoor | 120 hours of approved training; state exam; $300,000 insurance; $250 a year. A license not renewed for 12 months can be restored only by meeting the requirements for a new license. | Licensed professional engineers and architects. |
| K2 Grandfathering | Exemption | Training and exam | Incumbent inspectors | Licensed without training or exam on application between 1 July and 31 December 2027, if at the date of application the applicant has at least three years of practice and at least 250 fee-paid inspections in those three years, documented by reports. Insurance and fee still required. | — |
| K3 Enforcement on complaint | Enforcement | K1, K2, K4 | Board | Investigation only on a written complaint by a buyer or a licensed agent. | — |
| K4 Agents and inspectors | Rule on agents' conduct | Real-estate agents | Agents | "A real-estate licensee shall not direct, steer or require a client to use a particular home inspector." See U1. | — |

Unclear provision:
- U1, agents' recommendations. K4 forbids an agent to "direct, steer or require" a client to use a particular inspector. Reading U1-a: the provision forbids only requiring or conditioning (making a transaction depend on the inspector); an agent may still name or recommend inspectors when asked, as now. Reading U1-b: naming a particular inspector is "steering"; an agent may give a client only the Board's public list of licensed inspectors.

Readings get no probability; where a sign depends on one, each reading's sign is reported.

**Figures.** About 210 incumbents (34%) cannot be grandfathered and must train or stop. For a full-time inspector doing 200 inspections a year, insurance and the license fee add about $10 per inspection; for a part-timer doing 40, about $50, over 10% of the fee. A near-line inspector at 60 inspections a year, with 180 by mid-2027, needs about 70 more by the end of 2027, more than double their pace. Training plus three weeks' lost work is about $3,200 plus about $4,000 of fees forgone at full-time pace.

The counterfactual is Aldenmoor without the Act: no license, inspectors entering and leaving as now, agents recommending inspectors as now, and the inspectors' association continuing the campaign for licensing that it had run since 2022.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Triangular: removes the option of selling inspections without a license (CR-1, operation 1 where enforced; operation 3, a penalty risk, where not), and attaches costs to obtaining one (operation 3). | Yes: most inspectors lack the training, many lack insurance (A-1). | EN-1 (1.0: refill) to EN-4, EN-2 (1.0: an unsellable license), EN-11 (0.9 Unless; 1.0: its baseline), OC-2, CR-4 (0.8: fixed cost per seller), RS-1, RS-3, RS-10, RS-11, RS-16 (1.0: per unit of quality), CR-11 (0.9), CR-12 (1.0: what the response argument needs), DM-2, DM-3 |
| K2 | An exemption drawn on a line in time and in inspections: removes the training and exam burden for those above the line. | Yes for those near the line (A-12). | RS-17 (a line on another measure; 1.0: mirrors and notches), RS-8 (0.9; 1.0: races and rivals), CR-1 (1.0: notches), CR-7 (0.9: assets without a market price), CR-10a, TS-5 (1.0: lines fixed before announcement) |
| K3 | Enforcement limited to complaints by two classes | Yes | RS-20 (1.0: baseline), RS-10, CR-4 (x: comply, y: violate), CR-5c, CR-11b, CR-8b (1.0: receipts into the same budget) |
| K4 | Triangular, per reading: under U1-b it removes agents' option of recommending a named inspector; under U1-a it changes nothing that agents did. | U1-a: no; U1-b: yes (A-23). | CR-1 (per reading), CR-11c, CR-7c, RS-7 (1.0), CR-4 (1.0: lobbying, generally) |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `inspectors.grandfathered` | Incumbents above the line (about 320, plus near-line inspectors who reach it) | Licensed without training or exam; must insure and pay the fee; lose their license status if it lapses for 12 months. |
| `inspectors.near_line` | About 60 who reach three years only in the window, and about 80 part-timers short of 250 inspections | Qualify for grandfathering only by reaching the line by their application date. |
| `inspectors.new_requirement` | About 210 who cannot be grandfathered, and near-line inspectors who miss the line | Must train, pass the exam and insure, or stop by 1 January 2028. |
| `inspectors.prospective` (`sellers.prospective`) | Would-be entrants | Must train, pass and insure before starting (from 1 July 2027). |
| `inspectors.licensed` | Every licensee | Exposed to complaints by buyers and agents, and to discipline. |
| `engineers.exempt` (`sellers.substitutes`) | About 35 professional engineers who inspect homes | Exempt; now compete with fewer inspectors. |
| `buyers.engineering_other` | Clients of those engineers for their other engineering work | Engineers' time moves toward home inspections. |
| `buyers.unlicensed` | Clients of unlicensed inspectors (sellers, builders, some buyers in the border metro) | Their inspections are now outside the legal market. |
| `inspectors.linmouth` (`neighboring_jurisdictions`) | About 40 Linmouth inspectors with Aldenmoor jobs | Need an Aldenmoor license for those jobs. |
| `inspection_firms` | Multi-inspector firms, sellable businesses with agent referral networks | Fewer rivals; under U1-b, referral networks lose their use. |
| `buyers.current` | Home buyers who commission inspections | Pay more; see a license; under U1-b find an inspector themselves. |
| `sellers.homes` | Sellers who commission pre-listing inspections | Cannot complain under K3. |
| `agents` (`intermediaries`) | Real-estate agents | May complain; may or may not recommend (U1). |
| `training_schools`, `insurers` (`input_suppliers`) | Approved schools; errors-and-omissions insurers | New demand from license applicants. |
| `officials.enforcement` | Home Inspector Board | Licensing, exams, complaint investigations; fee receipts. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `inspectors.new_requirement`, `inspectors.prospective`, `inspectors.grandfathered` | `compliance_cost` (training and exam for the first two; the license fee for all; insurance for those not already insured) | increase | short (from 2027) to long | CR-1 (operation 3), OC-2, CR-8c | A-1, A-2, A-27 |
| C-2 | inspectors (all active) | `share_of_sellers_licensed` | increase | short (from 1 July 2027) | CR-1, CR-12 (0.9: a status that exists only under the policy) | A-3 |
| C-3 | `buyers.current` | `quality_information` (whether an inspector has trained, passed an exam and is insured) | U1-a: increase; U1-b: ambiguous | short to medium | EN-11 (1.0: baseline of the Unless), CR-11c (0.7: what a sign needs), CR-12b | A-4, A-5, A-6 |

C-1 and C-2 are what the Act does at once. Insurance is a new cost only for the about 40% who carried none (A-27); for those already insured the Act requires what they bought anyway, so it is not counted in C-1 for them. C-3 is what its supporters expect: buyers can tell trained, tested and insured inspectors from others.

**The license as a signal (C-3, EN-11).** EN-11 needs two premises (CR-11, 0.7): that buyers did not already know what the license tells them, and which way it moves them. Buyers seldom knew whether an inspector had trained or was insured (A-5, p = 0.7); the training and exam bear on competence buyers value and cannot easily judge (A-4, p = 0.65). The license is on the Board's public list, so buyers and agents can see it. So `quality_information` increases.

EN-11's 0.9 Unless clause says that a license issued on different requirements conveys less than a license issued on one. Here the license is issued on one requirement for newcomers and on experience for the grandfathered. But the Unless clause compares with a license on one requirement, which is not this case's counterfactual. Against no license at all, a grandfathered license still tells buyers something they did not know (at least three years, at least 250 inspections, insured), and a newcomer's license tells them more. The Unless clause therefore bears only on size here, not on sign. EN-11's 1.0 clause on the baseline of the Unless now says exactly this: where the counterfactual has no license, the main clause applies, by less where requirements vary. Over time, as grandfathered inspectors retire, the license comes to be issued on one requirement (section 8).

Two opposing chains were checked:
- *The national certification.* Once every licensee has some training, the voluntary certification distinguishes less, and some holders may drop it. For this to lower what buyers know, the certification would also have to convey more than the license does; it requires 100 hours against the license's 120. Both premises together are A-30 (p = 0.35). By CR-12's 0.8 kind 2 note, the chain is below the cut-off: the derived sign is reported and the chain is recorded in section 10.
- *Agents' recommendations, under U1-b.* About 70% of buyers now rely on an agent's recommendation. Agents see many inspections and know which inspectors are competent, though their interest also favors inspectors who do not upset sales. If agents' recommendations conveyed competence that buyers cannot learn otherwise (A-6, p = 0.6), removing them under U1-b lowers what buyers know. With p at least 0.5, this is a kind 2 chain: under U1-b, `quality_information` is `ambiguous`. Under U1-a recommendations continue, and the sign is `increase`.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `inspectors.prospective` | `entry_rate` | decrease | short (from January 2026 to 2028) | EN-1, CR-1, CR-4 (lumpy cost), CR-10a, TS-5 (1.0) | A-1, A-3 |
| C-5 | inspectors (all) | `number_of_sellers` | decrease | short (from January 2028) to medium | EN-1, CR-4 (0.8: a cost fixed per seller), CR-7 | A-1, A-3, A-7 |
| C-6 | `buyers.current` | `price_paid` (inspection fee) | increase | short to medium (from January 2028) | EN-1, CR-6, CR-12e (response argument), CR-12 (0.9, 1.0) | A-1, A-3, A-8, A-33 |
| C-7 | `buyers.current` | `quantity_traded` (legal inspections commissioned: by licensed inspectors and exempt engineers) | decrease | short to medium | EN-1, EN-3, OC-4, CR-4c | A-1, A-3, A-8, A-9, A-33 |
| C-8 | `inspectors.grandfathered`, `inspectors.new_requirement` (who qualify and stay) | `net_price_received` (fee per inspection) | increase | short to medium | EN-2, CR-6, CR-7b | A-1, A-3, A-8, A-33 |
| C-9 | `inspectors.grandfathered` | `earnings` (fee income from inspection) | increase | medium | EN-2 (1.0: an unsellable license), CR-7 (0.9: an asset without a market price) | A-1, A-3, A-8, A-10, A-33 |
| C-10 | `inspectors.near_line` | `quantity_supplied` (inspections they perform before applying, January 2026 to December 2027; a flow in the window) | increase | short | RS-8 (0.9; 1.0: races and rivals), RS-17 (1.0: mirrors), CR-10a, CR-4 | A-12, A-14 |
| C-11 | `inspectors.near_line` | `net_price_received` (fees, January 2026 to June 2027) | decrease | short | CR-4, CR-5c, CR-6 | A-12, A-13 |
| C-12 | other incumbent inspectors | `quantity_supplied` (inspections, same window) | decrease | short | RS-8 (1.0: races and rivals), CR-9 (competitors for the same buyers), CR-8b | A-12, A-14 |
| C-13 | `inspectors.new_requirement` | `enrollment` (approved training, January to December 2027; a flow in the window) | increase | short | RS-8, CR-10a, CR-12 (0.9) | A-2 |
| C-14 | `training_schools` | `enrollment` (home-inspection training, from 2028) | ambiguous | medium to long | CR-9, CR-12b | A-1, A-2 |
| C-15 | `inspectors.grandfathered`, `inspectors.near_line` | `compliance_cost` (grandfather applications: documenting 250 inspections) | increase | short | OC-2, CR-8c, CR-12 (0.9) | none |
| C-16 | `inspectors.grandfathered` | `job_changes` (leaving inspection for other work for a year or more) | decrease | medium to long | RS-11, CR-3, CR-4 | A-15 |
| C-17 | unlicensed inspectors (incumbents who miss the deadline, Linmouth inspectors, newcomers) | `informal_activity` (unlicensed inspections) | increase | short to medium | RS-20 (1.0: baseline), RS-3, CR-4, CR-12 (0.9) | A-16 |
| C-18 | `agents`, `training_schools` | `lobbying_effort` (agents for reading U1-a; schools for more hours) | increase | short to medium | RS-7 (Unless; 1.0), CR-4 (1.0: lobbying, generally) | A-17, A-31 |
| C-19 | `inspectors.grandfathered` (association) | `lobbying_effort` (for tighter requirements and Board-initiated enforcement) | ambiguous | medium | RS-7 (Unless; 1.0), EN-5, CR-4 (1.0) | A-17, A-18 |
| C-20 | `engineers.exempt` | `quantity_substitute` (home inspections by exempt engineers) | increase | short to medium | RS-1, RS-16, EN-3 | A-19 |
| C-21 | `buyers.substitutes` (buyers who use engineers) | `price_substitute` (engineers' fee per home inspection of a given scope) | increase | short to medium | RS-16 (1.0: per unit of quality), CR-6 | A-19, A-20 |
| C-22 | `engineers.exempt` | `quality_information` (engineers telling buyers of their engineering license) | increase | short to medium | CR-11 (0.9: sellers' response to silence), CR-4 | A-21 |
| C-23 | `inspectors.linmouth` | `quantity_supplied` (inspections in Aldenmoor) | decrease | short to medium | CR-1, CR-4 (0.8: a cost fixed per seller) | A-3, A-28 |
| C-32 | `inspectors.prospective` | `entry_rate` (medium run, after the 2028 exits) | ambiguous | medium | EN-1 (1.0: refill), CR-4, CR-7a, CR-12b | A-1, A-3, A-8 |
| C-33 | `inspectors.prospective` | `entry_rate` (long run) | decrease | long | EN-1 (1.0: refill), CR-4, CR-7a, CR-10b | A-1, A-3, A-32 |
| C-36 | `inspectors.new_requirement` (those who train and stay) | `resources_available_other_uses` | decrease | short (2027) | CR-3 (note), CR-8b | A-2 |

**Entry and exit (C-4, C-5; EN-1).** The training, exam and insurance are a large one-time cost and a yearly fixed cost attached to the option of practicing; by CR-4's note on lumpy costs, every would-be entrant whose ranking of inspection over their next-best work is reversed by them stays out (C-4). The fall begins at the announcement, not at the effective date: someone who enters in 2026 will need the license anyway by 2028, because entry after 31 December 2024 can never reach three years by the end of the window (CR-10a). So there is no rush to enter before the deadline, which TS-5's grandfathering clause might suggest; the line was fixed before the announcement. The insurance and fee are a cost fixed per seller (CR-4, 0.8): they bear on whether a part-timer operates at all, and they fall on grandfathered part-timers too (A-7). Grandfathering delays the effect of the training requirement (EN-1 Unless) but not of the insurance. Incumbents who cannot be grandfathered and do not train stop in January 2028 (C-5). TS-5's 1.0 clause on lines fixed before the announcement now says there is no rush to qualify in such a case.

**Entry after 2028 (C-32, C-33; EN-1 1.0).** The 0.9 version signed entry `decrease` from 2026 to the long run. EN-1's 1.0 refill clause asks for more where the requirement removes part of the stock of sellers at one date, as here (about 210 incumbents who cannot be grandfathered, less those who train). The higher fee (C-6) raises the yield of entering against the lumpy cost (CR-4, CR-7a), so in the medium run entry by those who meet the requirement is pulled above what the cost alone would give: the two chains oppose and no premise ranks them, so entry in the medium run is `ambiguous` (C-32). In the long run, entry replaces exits; the licensed stock is smaller and its grandfathered members leave less often (C-16), so replacement entry falls below the counterfactual flow (A-32, p = 0.65): `decrease` (C-33). C-4 now covers the short run only, from the bill to 2028, where the line fixed in the past gives a fall with no rush.

**Fees and inspections: what the response argument gives (C-6, C-7).** With fewer sellers, fees rise (EN-1; CR-6). Exempt engineers (C-20), unlicensed practice (C-17), entrants drawn by the higher fee (C-32) and buyers who go without respond to the higher fee; none of them can take it back below its counterfactual level, since each stops once the gain it responds to is gone (CR-12e). CR-12's 1.0 clause treats each further response as a chain to combine; all of these respond to the same higher fee and stop when it is gone, so the argument is applied to them together. The total it bounds is legal inspections, by licensed inspectors (grandfathered, trained and new) and exempt engineers together, not licensed inspections alone; unlicensed inspections are a different service (CR-11b, C-34). To report `increase` rather than "increase or no change", the response must be partial (CR-12, 0.9): there are 35 engineers with well-paid alternative work, entrants need the training and exam, and unlicensed practice is deterred for most inspections (A-8, A-3). CR-12's 1.0 clause also asks that cost per inspection not fall as the number of inspectors falls: the license adds insurance and fees per inspector, and an inspection's cost is mostly the inspector's time per job, which does not fall with fewer inspectors (A-33, p = 0.75). Legal inspections fall: some buyers at the margin go without, or turn to unlicensed inspectors (C-7; EN-3; A-9). The 0.9 version called them "licensed inspections", which against a no-license counterfactual rise from none; the variable now reads "legal inspections". These are prevented exchanges (OC-4): both the buyer and the excluded inspector lose the gain each expected.

**Licensed inspectors (C-8, C-9; EN-2 and CR-7 0.9).** The license cannot be sold, so EN-2's `asset_value` clause does not apply to it; EN-2's 1.0 clause now says its value is by the holder's own ranking only (CR-7, 1.0). CR-7's 0.9 clause says that CR-7c still applies to an asset without a market price: the higher expected yield of the license, and of the grandfathered status, is a gain by the holder's own ranking (CR-3), and a change in money earnings needs a premise. The fee per inspection rises for every licensee (C-8). Grandfathered inspectors' fee income rises only if their volume does not fall with the fee, which holds if their rivals' exit takes away more inspections than buyers drop (A-10, p = 0.65; C-9). For excluded inspectors, EN-3 and CR-7 0.9 both say a fall in money earnings needs the premise that their next-best work pays less; many came from building trades that pay about as much (A-11, p = 0.4). Not reported: they are worse off by their own ranking (CR-3a), but no money sign is given.

Incumbents who cannot be grandfathered but train and stay bear a one-time cost (C-1) and then receive the higher fee (C-8). DM-3 applies: the one-time cost against a later stream is ambiguous by design, and those who chose to train expected it to pay. The two are different variables and are not netted (CR-12c). In 2027 they pay tuition and give up about three weeks of fees while keeping the burdened option (practice), so their means for other uses fall in that window (C-36; CR-3 note, CR-8b); the later fee rise is a different horizon (CR-12g).

**The grandfathering line in time (C-10 to C-12; RS-17 and RS-8).** RS-17 was written for a policy that burdens those above a line; here the burden (training and exam) falls on those below, and the favored side is above. RS-17's 1.0 clause now covers this mirror case (a training requirement grandfathered above an experience line) and asks that it be signed the same way; the line is a notch, since crossing it removes the whole training burden (CR-1, 1.0). Applying its derivation (CR-1, CR-4 with x: stay below, y: get above): those near the line push to get above it. The line has two parts. The start date (practice since 31 December 2024 at the latest) was fixed before the announcement, so no one could cross it after January 2026; for that part, grandfathering is a windfall to those already above, with no competition to qualify, as in EN-12's first branch. The count (250 fee-paid inspections in the three years before application) can still be reached. RS-17 says that where the threshold is measured over a past period, the response comes in that period, before the policy takes effect: near-line inspectors take on more inspections between the announcement and their application, asking agents for referrals and cutting fees (C-10; A-12). It is signed on a flow in the window, against a counterfactual in which they would work at their usual pace.

RS-8's 0.9 clause covers this as a rush to qualify, but its "two sides" are not a rise in one window and a fall in a later one: total inspections in the window are set by home sales (A-14), so the extra jobs come from other inspectors in the same window (C-12; CR-9). RS-8's 1.0 clause on races and rivals now records a rush of this kind on both classes, as done here. After licensing, near-line inspectors work in a market with higher fees, so no later dip is derived. Fees in the window (C-11): before July 2027 they win jobs mainly by cutting fees (A-13), a decrease; from July 2027 the market fee starts rising as entry closes, so the sign in July to December 2027 is not recorded. Those who reach the line apply late in the window, so applications bunch toward December 2027 (section 8).

RS-17's 0.9 clause on the value of firms near a line carries over in mirror form. Those just above the line gain twice: no training, and fewer rivals. Those just below bear the training and also gain from the burden on others once licensed (C-8): DM-3, as above.

**Training (C-13, C-14).** Incumbents who cannot be grandfathered and choose to stay must train before January 2028, so enrollment in approved courses bunches in 2027 (C-13; a flow in its window, against a counterfactual of none, CR-12 0.9). After 2028, fewer people enter (C-4) but every entrant trains 120 hours, where before only some took a voluntary course: the two chains oppose and no premise ranks them (C-14).

**Lock-in (C-16; RS-11).** A license that lapses for 12 months can be restored only by training and the exam. A grandfathered inspector who would have left for building work in a busy year and come back now forfeits the status by doing so, so fewer leave (A-15). RS-11 names a grandfathered status that lapses; it applied as written.

**Complaint-only enforcement (C-17; RS-20).** The Board acts only on a complaint by a buyer or an agent. The expected penalty for unlicensed practice therefore differs by counterparty: it is lowest for inspections ordered by sellers (pre-listing) and builders, who cannot complain, for jobs where the agent arranged the inspector and will not complain, and in the Brask River metro, where Linmouth inspectors are used to working (A-16). Against the no-Act counterfactual, unlicensed practice did not exist as a category, so any unlicensed inspection is an `increase` against none (CR-12, 0.9). RS-20's "increases there relative to uniform enforcement" compares with another policy, not with the counterfactual; its 1.0 baseline clause now says that against no policy breach increases from none wherever enforcement is less than certain, and that "concentrated where complaint is least likely" describes where it falls, which is how it is used here. RS-20's other clauses enter elsewhere: complaints give buyers and agents a bargaining threat over licensees (C-26), and complaints that are strategic add to licensees' costs (C-28).

**What clients of unlicensed inspectors lose (C-34; RS-10, CR-11b).** The 0.9 version declined RS-10 on the ground that unlicensed inspectors still advertise, which the record does not say. The trade is outside the legal market whether or not it is advertised, and CR-11b follows from that: the same inspection had, without the Act, the channels by which buyers learn about inspectors (agents' referrals, the voluntary certification shown openly, recourse in the courts). An unlicensed inspector cannot get an agent's referral, since agents may complain, and has reason not to show credentials that identify unlicensed practice; clients' recourse for a missed defect is weaker against someone practicing illegally. So `quality_information` falls for clients of unlicensed inspectors (C-34; A-16). RS-10's other members (search cost, disputes settled outside the courts) would need a premise on how openly unlicensed inspectors can advertise, which the record does not give; not reported. The activity is recorded as `informal_activity` (C-17; Gaps found, d).

**Lobbying (C-18, C-19; RS-7).** Agents have a concentrated stake in reading U1-a, and schools in more hours (C-18). Under RS-7's 1.0 Unless clause and CR-4's 1.0 clause, lobbying by each side of a question contested on the counterfactual path is signed against that contest; whether agents and schools would have taken part in the association's licensing campaign without the Act is a premise, not a given. They had no stake in K4 or in hours of approved training without a bill, and the record shows the campaign as the association's (A-31, p = 0.6 that they would not have lobbied on it). The opposing chain, counterfactual lobbying by them, therefore has p = 0.4, below the cut-off (CR-12, 0.8: kind 2): C-18 is `increase`, with the chain recorded in section 10. The inspectors' association lobbied for licensing since 2022 and, without the Act, would have kept doing so (A-18). Under the Act it lobbies for tighter rules and for the Board to act on its own (EN-5). RS-7's Unless clause, and CR-4's 0.9 note on lobbying, were written for repeals; their 1.0 clauses extend them to any policy, so the imposition sought by incumbents is covered directly. Compared with the counterfactual campaign, the association's lobbying is `ambiguous` (C-19).

**Engineers and the missing license (C-20 to C-22).** Engineers are exempt, so they are a close substitute outside the policy (RS-1). More buyers turn to them, and with only 35 engineers whose time has well-paid other uses, their fees rise (RS-16; A-20). By RS-16's 1.0 clause the fee is signed per home inspection of a given scope, so a shift toward engineers' longer inspections is not itself a price rise. Engineers move time from their other work into home inspections until the yields are equal (CR-7a), so the price of their other engineering work rises for its clients too (C-35; CR-9, CR-6; A-19, A-20). Buyers who now look for a license may read an engineer's lack of a home-inspector license as unlicensed practice. By CR-11's 0.9 clause on sellers' response to silence, engineers whose credentials compare well tell buyers of their engineering license, which some did not do before (A-21): buyers of engineers know more (C-22).

**Linmouth (C-23).** The inspected home cannot cross the border, so RS-4 does not apply: the only way to keep serving Aldenmoor is to be licensed there. Most Linmouth inspectors do too few Aldenmoor jobs to pay for training, insurance and the fee (A-28), so they drop those jobs or continue unlicensed in the Brask River metro (C-17).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-24 | `inspection_firms` | `asset_value` (firms with licensed staff and agent referral networks) | U1-a: increase; U1-b: ambiguous | short (from January 2026) to medium | CR-7c, CR-10c, EN-2, CR-12b | agents' referrals `input_to` firms' sales | A-1, A-3, A-8, A-22, A-33 |
| C-25 | `buyers.current` (who used agents' referrals) | `search_cost` (finding an inspector) | U1-a: no_change; U1-b: increase | short to medium | CR-1 (per reading), CR-9 | agents' referral and inspection: `complement` | A-23 |
| C-26 | `buyers.current` | `quality_per_unit` (the inspection received) | ambiguous | medium | EN-4, DM-2, RS-20, CR-12b | — | A-4, A-9, A-24, A-25, A-26 |
| C-27 | `insurers` | `quantity_traded` (inspectors' errors-and-omissions and liability policies) | increase | short | CR-1, CR-9 | insurance `input_to` licensed inspection | A-27 |
| C-28 | `inspectors.licensed` | `compliance_cost` (responding to complaints, including strategic ones) | increase | medium | RS-20, CR-8c, CR-12 (0.9) | — | A-25 |
| C-29 | `buyers.current` (who still commission an inspection) | `resources_available_other_uses` | decrease | medium | CR-3 (note), CR-8b | — | A-1, A-3, A-8, A-33 |
| C-34 | `buyers.unlicensed` (clients of unlicensed inspectors) | `quality_information` (referrals, credentials and recourse available on the inspection) | decrease | short to medium | RS-10, CR-11b, CR-1 | inspection moved outside the legal market | A-16 |
| C-35 | `buyers.engineering_other` | `price_paid` (engineers' other engineering work) | increase | short to medium | CR-9, CR-7a, CR-6 | engineers' time `input_to` home inspections and other work | A-19, A-20 |

**Firms (C-24).** Multi-inspector firms are sellable businesses: with entry restricted, their expected yield rises, and the rise is capitalized from the announcement (CR-7c, CR-10c; EN-2's move for a sellable asset). Much of their business comes from agents' recommendations. Under U1-a those continue: `increase`. Under U1-b the referral networks lose their use (A-22), an opposing chain on the same asset: `ambiguous`.

**Buyers' search (C-25).** Under U1-b, buyers who relied on an agent's name must choose from a list themselves (A-23): their search cost rises against the counterfactual, in which agents recommend. Under U1-a nothing changes in that channel: `no_change`, signed for the referral channel only.

**Quality received (C-26; EN-4, RS-20).** Four chains reach it:
- (+) newly trained licensees meet the training floor, where training bears on competence (EN-4; A-4);
- (+) buyers can now complain about missed defects, with discipline behind the complaint (RS-20, a bargaining threat; A-25);
- (−) buyers priced out go without or use unlicensed inspectors, which needs the premise that these are worse than the inspection replaced (EN-4's "down" chain; A-9, A-26);
- (−) agents can also complain, and some threaten complaints against inspectors whose reports upset sales (RS-20; A-24), which pushes reports toward the agents' interest.

DM-2 gives no default, and no premise ranks the chains: `ambiguous`. Under U1-b agents lose their referral leverage, but the complaint threat remains, so the sign is the same under both readings.

**Insurance (C-27).** About 40% of inspectors carried no insurance; the Act requires it (A-27). Premiums are a cost to inspectors (C-1) and a receipt to insurers (CR-8b); both are recorded.

**Complaints (C-28).** Complaints to a Board exist only under the Act. Licensees spend time answering them, genuine or strategic (RS-20: where complaint is costless, some complaints are unrelated to breach).

**Buyers' means (C-29).** Buyers who still commission an inspection pay a higher fee, which they keep paying, so their means for other uses fall (CR-3 note); licensed inspectors receive it (C-8).

Stopping points: home sales that fall through or close because of an inspection, and lenders' and insurers' reliance on inspections: depth 3, and their direction depends on C-26, which is ambiguous; stopped. Health and safety: out of scope.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `buyers.current`, `quality_information`, short to medium | The license as a signal (EN-11; A-4, A-5). | Under U1-b, agents' recommendations removed (A-6). Certification dropped (A-30, p = 0.35, below the cut-off). | None | **U1-a: increase; U1-b: ambiguous** (C-3). |
| `buyers.current`, `price_paid` (fee), short to medium | Fewer sellers (EN-1). | Engineers, unlicensed practice, entrants drawn by the fee, buyers going without. | CR-12e response argument, applied to the responses together and bounding legal inspections (licensed and engineers together); A-8 makes the response partial (CR-12, 0.9); A-33 rules out a fall in cost per inspection (CR-12, 1.0). | **increase** (C-6). Legal inspections: **decrease** (C-7). |
| `inspectors.prospective`, `entry_rate`, per horizon | Medium: the higher fee draws entrants who meet the requirement (C-6, EN-1 1.0). | The training, exam and insurance (EN-1); long run: a smaller stock that leaves less often (A-32). | None in the medium run; A-32 in the long run | Short: **decrease** (C-4). Medium: **ambiguous** (C-32). Long: **decrease** (C-33). |
| `agents`, `training_schools`, `lobbying_effort`, short to medium | On U1 and hours under the Act. | Counterfactual lobbying on the association's campaign (A-31: p = 0.4 that they would have; below the cut-off, kind 2). | CR-12 (0.8, kind 2 below 0.5) | **increase** (C-18). |
| `officials.enforcement`, `fund_balance` (Board), short to long | Fees and fines (C-31). | The Board's costs (C-30). | None: the record gives neither the Board's budget nor the fee yield in a form that settles the net (CR-8, 1.0) | **ambiguous** (C-37). |
| `inspectors.grandfathered`, `earnings`, medium | Higher fee (C-8). | Fewer inspections if buyers drop more than rivals exit. | A-10 | **increase** (C-9). |
| `inspectors.new_requirement` (excluded), `earnings` | — | Next-best work pays less (A-11, p = 0.4). | — | Not reported (CR-7, 0.9; EN-3). |
| `inspectors.new_requirement` (who train), training cost against fee | Higher fee later (C-8). | Training (C-1). | DM-3: none | Different variables, not netted (CR-12c). |
| `inspectors.near_line`, `net_price_received`, January 2026 to June 2027 | — | Fee cuts to win jobs (A-13). | — | **decrease** (C-11). July to December 2027: market fees rising against the cuts; not signed. |
| `training_schools`, `enrollment`, from 2028 | Every entrant trains. | Fewer entrants (C-4). | None | **ambiguous** (C-14). In 2027: **increase** (C-13). |
| `inspectors.grandfathered` (association), `lobbying_effort`, medium | For tighter rules under the Act. | The counterfactual campaign for licensing (A-18). | None (RS-7 Unless) | **ambiguous** (C-19). |
| `inspection_firms`, `asset_value`, short to medium | Fewer rivals. | Under U1-b, referral networks lose use (A-22). | None | **U1-a: increase; U1-b: ambiguous** (C-24). |
| `buyers.current`, `quality_per_unit`, medium | Training floor; buyers' complaints. | Priced-out buyers' alternatives; agents' complaints. | DM-2: none | **ambiguous** (C-26). |

## 8. Time structure

- **January 2026: the bill.** The line's start date (practice by 31 December 2024) is already fixed, so no one can enter in time to be grandfathered: entry falls from the announcement (C-4), with no rush. Firms' values move as enactment becomes likely (C-24). Near-line inspectors begin to take more jobs (C-10, C-11).
- **2027: training and the window.** Approved courses open in January 2027 and the exam in March; incumbents who cannot be grandfathered train during 2027 (C-13), paying tuition and giving up weeks of work (C-36). From 1 July 2027 new entrants need a license; grandfather applications open and, because experience is measured at the date of application, near-line inspectors apply late, so applications bunch toward December 2027. This is a path note, not a separate consequence: applications exist only under the Act and are recorded through their cost (C-15).
- **January 2028: the license binds on everyone.** Those who did not qualify stop or continue unlicensed (C-5, C-17); fees rise (C-6).
- **Medium to long run.** Grandfathered inspectors stay in the occupation longer (C-16) and retire over 10 to 25 years. As they do, the license comes to be issued on one requirement only, and what it tells buyers grows (C-3, same sign; CR-11 0.9 on a signal that changes). Entry in the medium run, after the 2028 exits, is drawn up by the higher fee and held down by the requirement (C-32, ambiguous); in the long run it replaces exits from a smaller stock that leaves less often (C-33, decrease).
- **Per reading of U1.** Under U1-b, from enactment buyers search for themselves (C-25) and firms' referral networks lose value (C-24); under U1-a the referral channel is unchanged.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-30 | `officials.enforcement` (Board) | `enforcement_cost` (licensing, exams, complaint investigations) | increase | Staff and systems, funded from fees. | OC-3, CR-8c |
| C-31 | `officials.enforcement` (Board) | `non_tax_receipts` (license, exam and application fees; fines) | increase | Paid by inspectors (C-1, C-15) and those fined. | CR-1, CR-8b |
| C-37 | `officials.enforcement` (Board) | `fund_balance` (fees and fines less the Board's costs) | ambiguous | Whatever the fees do not cover, or the surplus they leave. | CR-8b (1.0: receipts into the same budget), OC-1 (1.0), CR-12b |
| C-1 | inspectors | `compliance_cost` (training hours, exam, insurance, fees) | increase | About $7,000 of tuition and lost work per newcomer; $1,800 a year of insurance and $250 of fees for all. Training hours beyond what buyers would have paid for are OC-2 costs. | OC-2, CR-8c |
| C-7 | `buyers.current`, excluded inspectors | `quantity_traded` (legal inspections) | decrease | The inspections not made; both sides lose the gain each expected. | OC-4, CR-5a |

**Who pays the Board (OC-3).** From the policy's own revenue: license, exam and application fees (C-31), paid by inspectors and passed in part to buyers through the fee (C-6). The right baseline is zero here: without the Act there is no board and no enforcement of anything it does. By CR-8's 1.0 clause the Board's outlay (C-30) and the fees and fines paid into its budget (C-31) are two items, and the net is its own consequence (C-37): the record gives neither the Board's budget nor the fee yield in a form that settles it, so it is `ambiguous`. Both sides of each payment are recorded: fees (C-1, C-15 and C-31), premiums (C-1 and C-27), fees for inspections (C-29 and C-8), tuition (C-36 and the schools' enrollment, C-13).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The requirements cost some current and would-be inspectors more than they would otherwise spend. | binding | 0.9 | 55% hold no certification; 40% carry no insurance; 34% cannot be grandfathered. | The license does not bind; C-4 to C-9, C-29, C-32 and C-33 fail. |
| A-2 | Some incumbents who cannot be grandfathered train and sit the exam to stay in practice. | other | 0.75 | Their investment in tools and agent networks; course capacity in 2027. | C-13 and C-36 are not reported; C-1's training part applies only to newcomers. |
| A-3 | Despite complaint-only enforcement, unlicensed practice is deterred for most inspections: agents' forms and lenders ask for the license number, and buyers and agents complain. | enforcement | 0.7 | Agents' association forms; lender practice; complaint rates in states with such laws. | C-4 to C-9 shrink; C-17 grows. |
| A-4 | The training and exam bear on competence that buyers value and cannot easily judge. | other | 0.65 | Course syllabus; buyers' difficulty judging an inspection before defects appear. | C-3's (+) chain and C-26's training chain fail. |
| A-5 | Buyers and agents did not already know which inspectors had trained, passed an exam or were insured, and can see the license. | other | 0.7 | Inspectors' advertising; the Board's public list. | C-3 is not reported. |
| A-6 | Agents' recommendations conveyed information on competence that buyers cannot get otherwise. | other | 0.6 | Agents see many inspections; buyers buy one every few years. | C-3 under U1-b is `increase`. |
| A-7 | For some part-time inspectors, insurance and the fee exceed their margin, so they stop. | alternative_uses | 0.7 | $50 per inspection at 40 a year. | C-5 rests on non-grandfathered exit only (still a decrease, by A-1). |
| A-8 | Exempt engineers and unlicensed practice cannot replace the excluded supply at the old fee (the response is partial). | other | 0.75 | 35 engineers with other work; A-3. | C-6 is "increase or no change"; C-8, C-9, C-24 and C-29 fail; C-32 loses its (+) chain. |
| A-9 | Some buyers at the margin go without an inspection or use an unlicensed inspector when the fee rises. | substitutability | 0.6 | Cash investors; buyers of new homes with builders' warranties. | C-7 is not reported; C-26 loses its first (−) chain. |
| A-10 | Grandfathered inspectors stay in the occupation and their volume does not fall: rivals' exit takes away more inspections than buyers drop. | other | 0.65 | 210 incumbents who cannot be grandfathered against a small fall in total inspections. | C-9 is not reported. |
| A-11 | Excluded inspectors' next-best work pays less in money. | other | 0.4 | Many came from building trades with similar pay. | Below the cut-off: their earnings are not reported. |
| A-12 | Some near-line inspectors would otherwise fall short of 250 inspections by their application date, and can find extra jobs. | other | 0.7 | About 80 part-timers and 60 late starters; agents' referrals. | C-10 to C-12 are not reported. |
| A-13 | They win the extra jobs mainly by cutting fees. | other | 0.55 | Price as the quickest margin with buyers; agents' referrals are not enough alone. | C-11 is not reported. |
| A-14 | Total inspections in the window are set by home sales, not raised by the rush. | other | 0.75 | Inspections are bought for a sale. | C-12 is not reported. |
| A-15 | Some grandfathered inspectors would otherwise leave for a year or more and return. | mobility | 0.6 | Moves to building work in busy years. | C-16 is not reported. |
| A-16 | Some unlicensed practice continues where complaint is least likely. | enforcement | 0.7 | 4,000 pre-listing and 3,000 builders' inspections a year; Linmouth inspectors in the border metro. | C-17 and C-34 are not reported. |
| A-17 | Agents, schools and the inspectors' association can organize at a cost below their stake. | other | 0.85 | State associations exist. | C-18 and C-19 are not reported. |
| A-18 | Without the Act, the inspectors' association would have kept lobbying for licensing. | counterfactual_trend | 0.7 | Its campaign since 2022. | C-19 is `increase`. |
| A-19 | Some exempt engineers add home inspections, and some buyers accept them. | substitutability | 0.6 | Engineers already inspecting. | C-20, C-21 and C-35 are not reported. |
| A-20 | Engineers' supply cannot expand at unchanged cost in the period. | other | 0.65 | 35 engineers; their other work pays well. | C-21 and C-35 are not reported. |
| A-21 | Some engineers did not tell home buyers of their engineering license before, and buyers now look for a license. | other | 0.55 | Engineers' advertising to buyers. | C-22 is not reported. |
| A-22 | Firms' business came largely through agents' recommendations, which lose their use under U1-b. | other | 0.7 | 70% of buyers use agents' referrals. | C-24 under U1-b is `increase`. |
| A-23 | Most buyers used agents' referrals, and under U1-b must search themselves. | other | 0.85 | Agents' survey. | C-25 under U1-b is not reported. |
| A-24 | Some agents use, or threaten, complaints against inspectors whose reports upset sales. | other | 0.55 | Agents' commission depends on closing; complaints are costless to file. | C-26 loses its second (−) chain (still ambiguous). |
| A-25 | Some buyers complain after missed defects, and discipline follows some complaints. | other | 0.8 | Complaint rates in other states. | C-26 loses its second (+) chain; C-28 is not reported. |
| A-26 | What priced-out buyers move to is of lower quality than the inspection replaced. | other | 0.6 | Going without; unlicensed inspectors without insurance. | C-26 loses its first (−) chain (still ambiguous). |
| A-27 | Some inspectors carried no insurance before. | other | 0.85 | 40% uninsured. | C-27 is not reported; C-1 loses its insurance part. |
| A-28 | Most Linmouth inspectors serving Aldenmoor do too few jobs there to cover the license's costs. | alternative_uses | 0.65 | About 40 inspectors; 12% of sales in the border metro, shared with Aldenmoor inspectors. | C-23 is not reported. |
| A-29 | Some grandfather applicants overstate their inspections, and the Board, checking on paper and acting otherwise only on complaint, misses it. | enforcement | 0.45 | Reports are the evidence; no audit power. | Below the cut-off: not reported. If true, near-line inspectors' rush (C-10) is smaller and `legal_breach` rises. |
| A-30 | Holders of the national certification drop it, and it conveyed more about competence than the license does. | other | 0.35 | 100 hours against 120; the certification's continuing-education requirement. | Below the cut-off: C-3's opposing chain is recorded here only. If true, C-3 is `ambiguous` under both readings. |
| A-31 | Without the Act, agents and training schools would not have lobbied on the association's licensing campaign. | counterfactual_trend | 0.6 | The campaign since 2022 is recorded as the association's; agents' and schools' stakes (K4, approved hours) arise only with a bill. | Its negation (p = 0.4) is a kind 2 chain below the cut-off. If they would have lobbied, C-18 is `ambiguous`. |
| A-32 | In the long run, licensed inspectors leave at a lower rate from a smaller stock than inspectors would without the Act, so replacement entry is below the counterfactual flow. | other | 0.65 | Grandfathered inspectors leave less often (C-16); the stock falls by about a third in 2028; entry replaces exits once the stock has adjusted. | C-33 is `ambiguous`. |
| A-33 | Inspectors' cost per inspection does not fall below its counterfactual level as the number of inspectors falls (constant or rising cost). | other | 0.75 | An inspection's cost is mostly the inspector's time per job; the license adds insurance and fees per inspector. | C-6 to C-9, C-24 and C-29 are not signed by the response argument (CR-12, 1.0). |

**Final check before the report.**
1. *Uncombined chains.* `quality_information` (C-3), the fee (C-6), entry by horizon (C-4, C-32, C-33), grandfathered earnings (C-9), near-line fees (C-11, by window), enrollment (C-13, C-14, by window), agents' and schools' lobbying (C-18), the association's lobbying (C-19), firms' values (C-24), quality received (C-26) and the Board's balance (C-37) are combined in section 7.
2. *Groups.* No pattern here licensed only "at least one of"; EN-3's priced-out buyers are recorded through `quantity_traded` and `informal_activity`, each with its own premise.
3. *Baseline.* Every sign is against Aldenmoor without the Act. EN-11's 0.9 Unless and RS-20's "relative to uniform enforcement" both compare with another policy; neither is used for a sign (C-3, C-17), and their 1.0 clauses now say so. C-25 under U1-a is `no_change` against the counterfactual, not against U1-b. Legal inspections, not licensed ones, are the variable that falls (C-7). Lobbying is signed against the counterfactual licensing campaign for every class (C-18, C-19).
4. *Worse off is not poorer.* Excluded inspectors' earnings are not signed (A-11 below the cut-off); buyers' means are signed only for those who keep buying (C-29); trainees' means only for those who train and stay (C-36). Insurance is a cost only for those who were uninsured (C-1, A-27).
5. *Timing.* The rush to qualify and the training bunch are flows in their windows (C-10, C-13); entry has no rush (C-4).
6. *Both sides.* Fees, premiums, tuition and inspection fees (section 9); near-line inspectors' extra jobs and rivals' lost jobs (C-10, C-12); the Board's receipts and outlays (C-30, C-31, C-37).
7. *Every class, every core rule.* CR-7c checked for licenses (unsellable: CR-7 0.9), firms (C-24) and the grandfathered status; CR-6 for fees, engineers' fees and engineers' other work (C-35); CR-9 for insurers, schools, engineers, Linmouth; CR-11b for clients of unlicensed inspectors (C-34); CR-4 with CR-7a for entry after 2028 (C-32, C-33); enforcement cost and its payers (OC-3).
8. *Unstated premises.* Lobbying (A-17, A-18, A-31), margins (A-7, A-9, A-12), the response being partial (A-8), constant cost (A-33), exit rates (A-32) and every information premise (A-4 to A-6, A-21, A-30) are in the table.
9. *The baseline of every pattern (1.0).* EN-11's Unless and RS-20 compared with another policy; both are re-based in 1.0 and their main signs are taken against no license (C-3, C-17). EN-1 compared with no licensing but omitted the refill chain; entry is re-signed per horizon (C-4, C-32, C-33). RS-17 and RS-8 are applied in their 1.0 mirror and rivals forms against no Act (C-10, C-12). RS-7's Unless is applied against the counterfactual campaign for every class (C-18, C-19). EN-2, EN-3, EN-4, EN-5, RS-1, RS-3, RS-10, RS-11, RS-16, OC-2, OC-3, OC-4, TS-5 and DM-2, DM-3 compare with no Act: no re-signing needed.

## 11. Report

**The policy.** From 2028 everyone who inspects homes for pay in Aldenmoor needs a license: 120 hours of training, an exam and $300,000 of insurance. Inspectors with three years of practice and 250 inspections at the time they apply, in the second half of 2027, are licensed without training or exam. The Board investigates only when a home buyer or a real-estate agent complains. Agents may not "direct, steer or require" clients to use a particular inspector; whether that stops them recommending one is unclear.

**Visible consequences.** Inspectors bear training and exam costs, the license fee and, for those who were uninsured, insurance (C-1). Every legal inspector holds a license (C-2), and buyers can tell who has trained, passed and insured (C-3), unless agents' recommendations are also forbidden, in which case buyers may end up knowing more or less (C-3, U1-b).

**Invisible consequences.**
- *Fewer inspectors, higher fees.* Fewer people enter, from the day the bill was introduced (C-4); fewer inspectors work, including part-timers for whom insurance does not pay (C-5); fees rise (C-6) and fewer legal inspections are bought (C-7), so buyers who still buy have less for other things (C-29). After the 2028 exits, the higher fee draws some entrants back, so whether entry is lower in the medium run is open (C-32); in the long run it is lower (C-33). Licensed inspectors receive more per inspection (C-8), and grandfathered inspectors earn more (C-9). Excluded inspectors are worse off by their own reckoning, but whether they earn less money depends on their next job, and is not claimed.
- *Racing the line.* Inspectors just short of 250 inspections take on extra jobs before applying, at lower fees (C-10, C-11), at other inspectors' expense (C-12). Incumbents who cannot be grandfathered crowd into training in 2027 (C-13), with less to spend that year (C-36); later enrollment may rise or fall (C-14). Grandfathered inspectors stay in the trade rather than lose their status (C-16).
- *Around the license.* Exempt engineers do more inspections, at higher fees (C-20, C-21), and tell buyers of their engineering license (C-22); their other clients pay more (C-35). Linmouth inspectors do fewer Aldenmoor jobs (C-23). Insurers sell more policies (C-27). Agents and schools lobby (C-18).
- *Complaint-only enforcement.* Unlicensed inspection continues where no one who may complain is the client: sellers' and builders' inspections, agents' own arrangements, the border metro (C-17). Its clients lose referrals, credentials and recourse they had for the same inspection without the Act (C-34). Licensees spend time answering complaints, some of them strategic (C-28).
- *Costs.* The Board's work (C-30), paid from fees it receives (C-31); whether the fees cover it is open (C-37).

**Per reading of U1.** If agents may still recommend (U1-a), buyers' search is unchanged (C-25), buyers know more about inspectors (C-3), and firms with agent networks gain value (C-24). If they may not (U1-b), buyers search more (C-25), and what buyers know and firms' values may move either way (C-3, C-24).

**Ambiguous effects.** The quality of inspection buyers receive (C-26): a training floor and buyers' complaints against priced-out buyers' alternatives and agents' complaints. The association's lobbying against its counterfactual campaign (C-19). Enrollment after 2028 (C-14). Entry in the medium run (C-32). The Board's balance (C-37).

**Key conditions.** That the license binds (A-1, p = 0.9); that complaint-only enforcement still deters most unlicensed practice (A-3, p = 0.7); that engineers and unlicensed inspectors cannot fill the gap (A-8, p = 0.75) and cost per inspection does not fall as inspectors leave (A-33, p = 0.75); that the training bears on competence buyers value and did not already know (A-4, A-5).

**What this analysis cannot say.** How large any effect is; whether inspections find more defects (health and safety are out of scope); whether excluded inspectors earn less money; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | inspectors.new_requirement, inspectors.prospective, inspectors.grandfathered | compliance_cost (training, exam, fee; insurance for the uninsured) | increase | short–long | visible | B | CR-1, OC-2, CR-8c | A-1, A-2, A-27 |
| C-2 | inspectors (all active) | share_of_sellers_licensed | increase | short | visible | B | CR-1, CR-12 | A-3 |
| C-3 | buyers.current | quality_information | U1-a: increase; U1-b: ambiguous | short–medium | visible | B | EN-11 (1.0), CR-11c, CR-12b | A-4, A-5, A-6 |
| C-4 | inspectors.prospective | entry_rate (to 2028) | decrease | short | invisible | B | EN-1, CR-1, CR-4, CR-10a, TS-5 | A-1, A-3 |
| C-5 | inspectors (all) | number_of_sellers | decrease | short–medium | invisible | B | EN-1, CR-4, CR-7 | A-1, A-3, A-7 |
| C-6 | buyers.current | price_paid (inspection fee) | increase | short–medium | invisible | B | EN-1, CR-6, CR-12e, CR-12 (0.9, 1.0) | A-1, A-3, A-8, A-33 |
| C-7 | buyers.current | quantity_traded (legal inspections) | decrease | short–medium | invisible | B | EN-1, EN-3, OC-4, CR-4c | A-1, A-3, A-8, A-9, A-33 |
| C-8 | inspectors.grandfathered, inspectors.new_requirement (who qualify) | net_price_received (fee per inspection) | increase | short–medium | invisible | B | EN-2, CR-6, CR-7b | A-1, A-3, A-8, A-33 |
| C-9 | inspectors.grandfathered | earnings (fee income) | increase | medium | invisible | B | EN-2 (1.0), CR-7 | A-1, A-3, A-8, A-10, A-33 |
| C-10 | inspectors.near_line | quantity_supplied (inspections before applying) | increase | short | invisible | B | RS-8 (1.0), RS-17 (1.0), CR-10a, CR-4 | A-12, A-14 |
| C-11 | inspectors.near_line | net_price_received (fees, January 2026 to June 2027) | decrease | short | invisible | B | CR-4, CR-5c, CR-6 | A-12, A-13 |
| C-12 | other incumbent inspectors | quantity_supplied (inspections, same window) | decrease | short | invisible | B | RS-8 (1.0), CR-9, CR-8b | A-12, A-14 |
| C-13 | inspectors.new_requirement | enrollment (approved training in 2027) | increase | short | invisible | B | RS-8, CR-10a, CR-12 | A-2 |
| C-14 | training_schools | enrollment (from 2028) | ambiguous | medium–long | invisible | B | CR-9, CR-12b | A-1, A-2 |
| C-15 | inspectors.grandfathered, inspectors.near_line | compliance_cost (grandfather applications) | increase | short | invisible | A | OC-2, CR-8c, CR-12 | none |
| C-16 | inspectors.grandfathered | job_changes | decrease | medium–long | invisible | B | RS-11, CR-3, CR-4 | A-15 |
| C-17 | unlicensed inspectors | informal_activity (unlicensed inspections) | increase | short–medium | invisible | B | RS-20 (1.0), RS-3, CR-4, CR-12 | A-16 |
| C-18 | agents, training_schools | lobbying_effort | increase | short–medium | invisible | B | RS-7 (1.0), CR-4 (1.0) | A-17, A-31 |
| C-19 | inspectors.grandfathered (association) | lobbying_effort | ambiguous | medium | invisible | B | RS-7 (1.0), EN-5, CR-4 (1.0) | A-17, A-18 |
| C-20 | engineers.exempt | quantity_substitute (inspections by engineers) | increase | short–medium | invisible | B | RS-1, RS-16, EN-3 | A-19 |
| C-21 | buyers.substitutes | price_substitute (engineers' fee per inspection of a given scope) | increase | short–medium | invisible | B | RS-16 (1.0), CR-6 | A-19, A-20 |
| C-22 | engineers.exempt | quality_information (engineering license told to buyers) | increase | short–medium | invisible | B | CR-11, CR-4 | A-21 |
| C-23 | inspectors.linmouth | quantity_supplied (inspections in Aldenmoor) | decrease | short–medium | invisible | B | CR-1, CR-4 | A-3, A-28 |
| C-24 | inspection_firms | asset_value | U1-a: increase; U1-b: ambiguous | short–medium | invisible | B | CR-7c, CR-10c, EN-2, CR-12b | A-1, A-3, A-8, A-22, A-33 |
| C-25 | buyers.current (referral users) | search_cost | U1-a: no_change; U1-b: increase | short–medium | invisible | B | CR-1, CR-9 | A-23 |
| C-26 | buyers.current | quality_per_unit (inspection received) | ambiguous | medium | invisible | B | EN-4, DM-2, RS-20, CR-12b | A-4, A-9, A-24, A-25, A-26 |
| C-27 | insurers | quantity_traded (inspectors' policies) | increase | short | invisible | B | CR-1, CR-9 | A-27 |
| C-28 | inspectors.licensed | compliance_cost (answering complaints) | increase | medium | invisible | B | RS-20, CR-8c, CR-12 | A-25 |
| C-29 | buyers.current | resources_available_other_uses | decrease | medium | invisible | B | CR-3, CR-8b | A-1, A-3, A-8, A-33 |
| C-30 | officials.enforcement (Board) | enforcement_cost | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-31 | officials.enforcement (Board) | non_tax_receipts (fees, fines) | increase | short–long | invisible | A | CR-1, CR-8b | none |
| C-32 | inspectors.prospective | entry_rate (medium run) | ambiguous | medium | invisible | B | EN-1 (1.0), CR-4, CR-7a, CR-12b | A-1, A-3, A-8 |
| C-33 | inspectors.prospective | entry_rate (long run) | decrease | long | invisible | B | EN-1 (1.0), CR-4, CR-7a, CR-10b | A-1, A-3, A-32 |
| C-34 | buyers.unlicensed | quality_information (on unlicensed inspections) | decrease | short–medium | invisible | B | RS-10, CR-11b, CR-1 | A-16 |
| C-35 | buyers.engineering_other | price_paid (engineers' other work) | increase | short–medium | invisible | B | CR-9, CR-7a, CR-6 | A-19, A-20 |
| C-36 | inspectors.new_requirement (who train and stay) | resources_available_other_uses | decrease | short | invisible | B | CR-3, CR-8b | A-2 |
| C-37 | officials.enforcement (Board) | fund_balance (fees and fines less costs) | ambiguous | short–long | invisible | B | CR-8b (1.0), OC-1, CR-12b | none |

## Corrections after the core-only comparison

The core-only re-run (`05_examples_core/WE-055_home_inspector_licensing_core.md`) was compared with this analysis. Each correction below was checked against the core rules before it was applied; the catalog is now 1.0.

**Changed.**
- C-1: insurance counted only for inspectors who were uninsured (A-27 added); for the 60% already insured it is not a new cost.
- C-4: horizon narrowed to the short run (the bill to 2028). The comparison's S row (cause J) is now settled by EN-1's 1.0 refill clause, so the medium and long runs are recorded separately (C-32, C-33).
- C-7: variable renamed from "licensed inspections" to "legal inspections" (licensed inspectors and exempt engineers): against a no-license counterfactual, licensed inspections rise from none. Sign kept; the core's opposing information chain lacks CR-11 0.7's direction premise (comparison, cause E against the core version).
- C-6, C-7, C-8, C-9, C-24, C-29: signs unchanged; CR-12's 1.0 clause on the response argument is applied: the responses (engineers, unlicensed practice, entrants drawn by the fee, buyers going without) are combined, the total bounded is named (legal inspections), and the constant-cost premise A-33 is added.
- C-18: sign kept (`increase`), now on A-31, the premise that agents and schools would not have lobbied on the counterfactual licensing campaign (RS-7 1.0, CR-4 1.0); its negation is a kind 2 chain below the cut-off.
- C-3, C-17: signs unchanged; EN-11's and RS-20's 1.0 baseline clauses now give them directly, where 0.9 needed an override.
- C-10, C-12: cite RS-17's and RS-8's 1.0 clauses (mirror case; races and rivals). C-9: cites EN-2's 1.0 clause on an unsellable license. C-19: cites RS-7's 1.0 Unless directly. C-21: signed per inspection of a given scope (RS-16, 1.0).
- Section 5: the claim that unlicensed inspectors still advertise, which the record does not contain, is withdrawn.
- Sections 2, 3, 7, 8, 9, the final check (now with item 9) and the report updated to match.

**Added.** C-32 (entry in the medium run, ambiguous), C-33 (entry in the long run, decrease; A-32), C-34 (clients of unlicensed inspectors, `quality_information` decrease), C-35 (engineers' other clients, `price_paid` increase), C-36 (trainees' means, decrease, 2027), C-37 (the Board's balance, ambiguous; CR-8 1.0). New actor classes `buyers.engineering_other` and `buyers.unlicensed`. New assumptions A-31 to A-33.

**Removed.** None.

**Comparison conclusions rejected or not applied.**
- Core C-35 (excluded inspectors' employment in other work increases, cause A): not added. It needs a premise that they find other paid work, and catalog 1.0 does not settle it; they are worse off by their own ranking, with no sign on employment.
- Core C-37 (grandfathered inspectors' means net of fee and insurance, `ambiguous`, cause J): not added; 1.0 does not settle it, and C-9 (gross fee income) is a different variable.
- Core C-3 and C-9 (subclasses' `employment`, cause J): not added; they are carried inside C-5 and add no sign.
- C-14 (training enrollment in general, cause J): kept as recorded.
- Core C-24 (legal inspections `ambiguous` through an information chain): rejected. The chain lacks the direction premise CR-11 0.7 requires (that buyers who learn the license buy more inspections rather than choose among inspectors), so it is not a chain; C-7 stays `decrease`.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12.

**(b) Unclear core rules.**
1. *CR-7 0.9, assets without a market price.* The clause says a change in money earnings needs "a premise about the holder's next-best use". For holders who stay in the occupation (grandfathered inspectors), the relevant premise is about their volume, not their next-best use (A-10); for those excluded, it is about the next-best use (A-11). The clause fits the second case as written and the first only by extension. *1.0:* not changed in 1.0; still read so.
2. *CR-12 0.8, kind 2, when the opposing chain needs two premises.* The certification chain (A-30) needs both that holders drop it and that it conveyed more than the license. Read as: the chain's premise is the conjunction, estimated as one probability. The rule does not say whether to estimate each part or the conjunction (related to Q9).
3. *CR-4 0.9, lobbying where the counterfactual had a campaign.* Written for repeals; the same question arises for an imposition sought by incumbents (C-19). Applied by symmetry, which CR-4's symmetry test supports. *1.0:* settled by CR-4's 1.0 clause, which also reaches agents and schools (C-18, A-31).

**(c) Missing or wrong patterns.**
1. *RS-20 applied as written gave the wrong baseline.* Its conclusion, "`legal_breach` increases there relative to uniform enforcement", compares with another policy. Against the no-policy counterfactual, breach of a rule that does not exist is an increase from none in every segment; RS-20's real content is the distribution of breach across counterparties, which the normal form cannot express as a sign. Sign overridden: recorded as `increase` against none (C-17), with the distribution in the text. RS-20 should say that against the counterfactual its distribution claim is a note, not a sign. *1.0:* RS-20's baseline clause now says so.
2. *RS-17 is written for a burden above the line.* Here the burden is below and the favored side above. Its derivation carried over in mirror form (those near the line push over it; the response comes in the measured period), but its "Then" (stay below, split units) does not fit. RS-17 could state the mirror case. *1.0:* RS-17's 1.0 clause now does.
3. *RS-8 0.9 and a rush that takes from rivals.* RS-8's "two sides" are a rise in the favored window and a fall in the window the action came from. A rush to qualify takes jobs from rivals in the same window (C-12), not from the rusher's later activity. Derived from CR-9 and CR-8b. *1.0:* RS-8's clause on races and rivals now covers it.
4. *TS-5's grandfathering clause misleads for a line fixed in the past.* TS-5 says that expected grandfathering brings entry forward. That holds only where a newcomer can still qualify; here the start date was fixed before the announcement, so entry fell from the announcement with no rush (C-4). EN-12's two branches (history fixed before or after the announcement) are the right frame for a grandfathering line too; neither TS-5 nor EN-1's Unless says so. *1.0:* TS-5's clause on lines fixed before the announcement now does.
5. *EN-2 for an unsellable license.* EN-2's `asset_value` clause applies only to transferable licenses; the gain to holders of an unsellable license has no variable (d1) and is signed through `net_price_received` and, with a premise, `earnings`. *1.0:* EN-2's clause now says the value is by the holder's own ranking only; the vocabulary gap (d1) remains.
6. *EN-11 0.9 Unless against a no-license counterfactual.* Applied as written, the clause would give `quality_information` a decrease for buyers of grandfathered inspectors. Against no license it bears only on size; the sign from EN-11's main clause stands (C-3). Sign overridden, not by the pattern's conclusion being wrong in its own case (a change from a single-requirement license), but by its baseline not being this case's. *1.0:* EN-11's baseline clause now says so.

**(d) Vocabulary.**
1. No variable for the value to its holder of an asset that cannot be sold (a license, a grandfathered status): `asset_value` is a market value. Used `net_price_received` and `earnings` (C-8, C-9).
2. `informal_activity` against `legal_breach` for unlicensed practice (C-17): neither fits exactly. Repeats the line question in 6.2f. (The 0.9 text said the practice is openly advertised; the record does not say so, and that claim is withdrawn.)
3. No variable for the number of complaints filed (06_gaps lists "complaints"); recorded through licensees' `compliance_cost` (C-28).
4. `no_change` per reading with a qualifier for a channel (C-25: the referral channel) is not described in 2.5.

**(e) Test of 0.9.**
- *EN-11 0.9 Unless (license issued on different requirements).* Needed interpretation: the clause's decrease is relative to a single-requirement license; against this case's no-license counterfactual it bears only on size (c6). The main clause, with CR-11 0.7's two premises, worked.
- *RS-20 (0.9, promoted).* Needed interpretation, and its main sign was overridden for baseline (c1). Its bargaining-threat and strategic-complaint clauses worked as written (C-26, C-28).
- *RS-17 0.9 (a line on another measure; value near the line).* Needed interpretation: a line in time and count, with the burden below it (c2). The 0.9 clause on value near the line carried over in mirror form, ending in DM-3 for those just below who train.
- *CR-7 0.9 (assets without a market price).* Worked as written for excluded inspectors (earnings not reported, A-11 below the cut-off); needed extension for those who stay (b1).
- *RS-7 0.9 (repeals) and the Unless clause.* Worked by symmetry for an imposition with a counterfactual campaign (C-19, b3).
- *RS-8 0.9 (more timing chains; rush to qualify).* Worked for the training bunch (C-13); needed interpretation for the rush to the line, whose second side is rivals in the same window (c3). The case's main timing point, that there is no rush to enter, came from CR-10a, not RS-8.
- *CR-11 0.9 (sellers' response to silence).* Worked as written for exempt engineers (C-22). The clause on a signal that changes was used only as a path note (section 8).
- *CR-12 0.9 (what the response argument gives).* Worked as written: A-8 turns "the fee does not fall" into "the fee rises" (C-6).
- *CR-12 0.9 (activities that exist only under the policy).* Worked as written for licensing status, unlicensed practice, applications and complaints (C-2, C-15, C-17, C-28).
- *CR-4 0.8 (a cost fixed per seller).* Worked as written: insurance drives part-timers out, including grandfathered ones (C-5).
- *EN-1 to EN-4.* Worked as written. EN-1's Unless (grandfathering delays the effect) holds for training but not insurance; EN-3's earnings premise and EN-4's "down" premise were needed and stated.
- *Candidates from 6.2e.* "Selection under a uniform term" was not needed. EN-12's frame (history fixed before or after the announcement) was needed by analogy for the grandfathering line (c4); it is a promoted pattern, so this is a note on its reach, not a candidate use.
- Re-run note: the core-only comparison contradicted the "EN-1 to EN-4 worked as written" verdict in three places: EN-1 signed entry `decrease` in every horizon without the refill chain from the higher fee (now C-4, C-32, C-33 under EN-1 1.0), C-1 counted insurance as new for all inspectors, and C-7 named the falling variable "licensed" rather than "legal" inspections; it also qualified the RS-7 verdict, since agents' and schools' lobbying needed a counterfactual premise (A-31), and found RS-10 wrongly declined on a fact not in the record (C-34).
