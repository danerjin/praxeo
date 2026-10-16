# WE-034 Non-compete clauses made unenforceable, for new and existing contracts

Analyst: draft (Handbook 0.6)  |  Rule catalog version: 0.6  |  Status: awaiting expert review

A stylized policy in a fictional state, modeled on a common type of law. It is a gap-probing example. The policy does not impose a contract term; it prohibits one, and it does so retroactively. That tests:
- CR-1, where one provision removes an option for both parties and adds one for one of them;
- CR-5c, where the bargaining range moves on every other term of the employment contract;
- RS-5, where restraints are rewritten into forms the law leaves untouched;
- CR-7b and CR-7c, for who bears the loss of a protection paid for in the past;
- CR-8, for whether voiding an existing right is a transfer.

The probabilities are illustrative; the evidence column says what a real analysis would cite. Courts appear only through their enforcement cost.

## 1. Policy record

**Teravel Freedom to Work Act.** The State of Teravel has about 3.2 million private-sector workers. A 2024 survey by the state labor department found that about 17% had signed a non-compete clause. The share is higher in some fields: software and engineering 45%, sales 35%, physicians and dentists in group practices 40%, finance 30%, hair and beauty salons 25%. Until now Teravel courts enforced "reasonable" non-competes (up to two years, within the employer's trading area) under common law. Employers filed about 400 enforcement suits a year, and many more disputes were settled by letter. Teravel's largest city, Halbrook, lies on a river whose far bank is in the State of Mossgrave. Mossgrave enforces non-competes, and about 60,000 people commute across the river each way.

The bill was introduced on 3 February 2025 with the governor's public support. It passed on 12 June 2025 and takes effect on 1 January 2026, with no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Void restraint | Prohibition of a contract term (see Gaps found, d) | "Any term of an employment or independent-contractor agreement that prohibits or restricts a worker, after the work relationship ends, from working for another person or carrying on a business, or that imposes a penalty for doing so" | Employers of workers who primarily work in Teravel, whatever law the contract chooses | Such terms are void. This applies to agreements made before, on or after the effective date, and pending cases are decided under the Act. Includes "forfeiture for competition" clauses (deferred pay lost only if the worker joins a competitor). | K2, K3 |
| K2 Sale of a business | Exemption | Restraints given by "a person who sells the goodwill of a business, or an ownership interest in a business" | — | No minimum share is stated. | — |
| K3 Preserved terms | Exemption | (a) agreements not to disclose trade secrets or confidential information; (b) agreements not to solicit the employer's customers or staff for up to 12 months, "where they do not in effect prevent the worker from working in their field"; (c) "a notice period during which the worker remains employed"; (d) forfeiture of pay or benefits not yet vested, under a plan that applies to every departure | — | No maximum length for (c). | — |
| K4 Notice | Mandated action | Employers | Every employer that has a non-compete with a current worker, or with a former worker who left after 1 January 2024 | Written notice by 1 March 2026 that the term is void. | — |
| K5 Enforcement | Enforcement | K1, K4 | Employers | A worker may sue an employer that tries to enforce a void term, or puts one in a contract after the effective date. Remedies: actual damages, $5,000 per worker, and attorney fees. The Attorney General's Labor Bureau may sue for civil penalties up to $10,000 per violation. No new appropriation; the Bureau works from its existing budget. | — |

**Counterfactual law.** Without the Act, courts keep enforcing reasonable non-competes. The Trade Secrets Act (injunctions against the use of trade secrets) is unchanged in both worlds and stays in force (`existing_rules`).

**Unclear provisions.**
- **U1: long paid notice periods ("garden leave").** Does K3(c) cover a notice period of six to twelve months, paid in full, with no duties, during which the worker may not work for anyone else? U1-a: yes, any paid notice period in which the worker "remains employed" is preserved. U1-b: no, a notice period long enough to keep the worker out of the field is a restraint "in effect", and is void under K1. The Attorney General's draft guidance says only that courts "will look to substance". The text and record do not decide it, so it is a reading.
- **U2: training repayment agreements.** Is a term that requires a worker who leaves within 24 months to repay employer-paid training a "penalty" for working for another person under K1? U2-a: yes, it penalizes leaving, and leaving is how one comes to work for another. U2-b: no, it applies to every departure, whatever the worker does next, and only recovers a cost. K3(d) covers unvested pay, not repayment of a cost already incurred. No court has ruled.
- **Not a reading.** Whether K2 covers token equity grants is treated as an assumption (A-12). A 1998 Teravel partnership statute has the same wording, and courts applying it required a bona fide sale of a substantial interest. That earlier practice is evidence of how K2 will be read.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Triangular: it prohibits a term of exchange between two private parties. For existing contracts, it withdraws state enforcement of a right one party already holds. | Yes, for the roughly 17% of workers with a non-compete, of whom some would otherwise move (A-1). | RS-2, RS-5, RS-7, RS-8, RS-11, OC-4; direct derivation from CR-1, CR-5c, CR-6 and CR-7 where no pattern fits |
| K2, K3 | Exemptions: boundaries that restraints can be moved across | Yes, as routes (A-4, A-11) | RS-5 |
| K4 | Mandated action, with no payment to the state: a compliance cost, and a channel of information to workers | Yes | OC-2; CR-11c |
| K5 | Enforcement: private suits, and the Attorney General on a fixed budget | Yes (A-2, A-18) | OC-3 |

**CR-1 operations, per actor class.** The counterfactual is that reasonable non-competes are enforced.

| Actor class | Operations |
|---|---|
| `workers.bound` (existing contracts) | Operation 2: they may now work for a rival or start a competing firm. Operation 3: a risk (a suit, or an injunction) is removed from that option. |
| `employers.net_trainers` and all employers holding non-competes | Operation 1: enforcing the restraint is removed. Operation 3: a burden is attached to including one ($5,000 per worker plus fees). |
| `workers.trainees` and every future worker | Operation 1: the option to sell a promise not to compete, in exchange for training, pay or a job, is removed. Operation 2: future freedom to leave for a rival. The worker's own side therefore has an option removed as well as one added. CR-1's note on void-contract rules mentions only the second (see Gaps found, b). |
| `employers.rivals` | Operation 2: they may hire bound workers without a buy-out or a suit. |
| `practices.professional` and other employers | Operation 2 in effect: K2 and K3 leave routes into the exempt forms. |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `workers.bound` | About 540,000 current and recent workers with a non-compete in an existing contract | May join a rival or start a firm. They are told so by notice (K4). |
| `workers.trainees` (`buyers.prospective` of training; sellers of labor) | New hires into jobs where the employer funds general training (sales, software, salons, junior clinicians) | Can no longer offer a restraint in exchange for training or pay; will be free to leave once trained. |
| `founders.spinoff` (`sellers.prospective`) | Bound workers who would start a firm in the same field | Entry is no longer barred. |
| `employers.net_trainers` (`sellers.current`, `factor_owners.specific`) | Firms that train more staff than they hire already trained, and that relied on non-competes | Lose the restraint on existing and future staff. May use the preserved forms. |
| `employers.rivals` | Firms, including spin-offs, that hire experienced staff from competitors | Can hire bound workers. |
| `practices.professional` | Medical, dental and accounting group practices | Can move senior staff into partnership buy-ins inside K2. |
| `customers` (`buyers.current`) | Clients of firms in fields with heavy non-compete use | Can follow a provider who moves, and face new spin-off sellers. |
| `intermediaries` | Recruiters placing experienced staff | More candidates are placeable. |
| `officials.enforcement` | Attorney General's Labor Bureau | New task on a fixed budget. |
| `officials.courts` | State courts | Lose non-compete enforcement suits; gain suits under K5, disputes over U1 and U2, and substitute claims. |
| `neighboring_jurisdictions` | Employers and workers in Mossgrave | Mossgrave restraints stay enforceable there; location choices across the river change. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `workers.bound` | `job_changes` (to rivals and to their own start-ups) | increase | short to medium | CR-1 (operation 2), CR-4b (x: stay, y: join a rival), CR-11c (the K4 notice tells them); combined with RS-11 (section 7) | A-1, A-2, A-9 |
| C-2 | `employers.net_trainers` and all employers holding non-competes | `compliance_cost` (contract review and rewriting, K4 notices) | increase | short | OC-2, CR-8c | none |

C-1 is the visible aim: people bound by a non-compete can now leave for a competitor. Many bound workers would not know that their clause is void without being told, and some believed that unenforceable clauses bound them even before the Act. The K4 notice is the channel by which the change in options reaches their beliefs (CR-11c). The sign for moves to rivals holds against an opposing chain only with a dominance premise (A-9); see section 7.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `founders.spinoff` | `entry_rate` (firms founded by former employees in the same field) | increase | medium to long | CR-1 (operation 2), CR-4b (x: stay employed, y: found a firm) | A-1, A-3 |
| C-4 | `employers.net_trainers` | `reclassification` (restraints rewritten into preserved forms: non-solicitation, confidentiality, unvested deferred pay) | increase | short to medium | RS-5 | A-4 |
| C-5 | `employers.net_trainers` | `reclassification` (paid garden leave; reading U1-a only) | increase | short to medium | RS-5 (under U1-a); no chain under U1-b | A-4 |
| C-6 | `employers.net_trainers` | `reclassification` (training repayment agreements; reading U2-b only) | increase | short to medium | RS-5 (under U2-b); no chain under U2-a | A-4, A-5 |
| C-7 | `workers.trainees` | `wage_rate` (during training), `non_wage_compensation` (employer-funded general training), `employment` (trainee hires) (group) | at_least_one_decrease | medium | RS-2, CR-5c, CR-7a, CR-6 | A-5, A-6 |
| C-8 | `workers.bound` | `wage_rate` (pay per hour, including deferred pay as it vests) | increase | short to medium | CR-1, CR-9, CR-6, CR-7a | A-1, A-7 |
| C-9 | `workers.bound` | `job_changes` (to other fields) | decrease | medium | CR-4a, CR-4b; RS-11 | A-8, A-10 |
| C-10 | `workers.bound` | `job_changes` (all destinations) | ambiguous | medium | CR-4b (+); RS-11 (−); CR-12b | A-1, A-10 |
| C-11 | `workers.bound` | `job_changes` (to rivals and start-ups, July to December 2025) | decrease | short | RS-8, CR-10a | A-14 |
| C-12 | `practices.professional` | `reclassification` (salaried senior clinicians moved into partnership buy-ins, so that a restraint on exit comes within K2) | increase | medium | RS-5 | A-11 |
| C-13 | `employers.net_trainers`; worker and start-up associations | `lobbying_effort` (over repeal, over the readings of U1 and U2, and over the scope of K2 and K3) | increase | short to medium | RS-7 | A-13 |
| C-14 | `employers.net_trainers` | `quantity_substitute` (trade-secret and non-solicitation claims brought against departing staff) | increase | short to medium | RS-1 | A-19 |

**C-4 to C-6, reclassification (RS-5).** K3 draws a line between restraints that are void and terms that are preserved. Employers whose non-competes protected something they value move to the preserved forms where these serve nearly the same end.
- Customer and staff non-solicitation protects client relationships.
- Confidentiality protects secrets.
- Unvested deferred pay raises the cost of any departure.

Two forms depend on the readings.
- C-5: under U1-a, a long paid notice period is a close substitute for a non-compete, bought with salary. Under U1-b it is void, so this route is closed and the chain does not run.
- C-6: under U2-b, repayment agreements recover training costs. Under U2-a they are void.

The normal form has no sign for "this chain does not operate under the other reading". So C-5 and C-6 name their reading in the variable, rather than giving a sign per reading (Gaps found, d).

**C-7, trainees: the bargaining range moves (CR-5c).** In the counterfactual, a trainee in a training-intensive job gives a promise not to compete and receives general training: skills that rival employers also value. K1 fixes that term of the exchange at "no restraint". By RS-2, the party disadvantaged by a fixed term adjusts the unregulated terms. The derivation from the core rules is as follows.
- Once trained, the worker can move to a rival. The worker's pay therefore tends toward what rivals would pay for the trained skill (CR-7a, the means can now move), and the employer cannot recover the cost of general training out of pay after training.
- The most an employer will give for an unrestrained trainee is lower than for a restrained one (CR-5c).
- The pressure moves to the margins still open (CR-6): pay during training, training funded, and the number of trainees hired. The other open margin is substitute restraints (C-4, C-6), which move the opposite way.

A group sign cannot hold members that move in opposite directions (Gaps found, b). The group is therefore signed only with the premise that the substitute restraints do not restore the protection fully (A-6). Under U2-a, repayment agreements are void, so A-6 holds more firmly. Under U2-b it rests on the limits of repayment agreements (capped at actual cost, and unenforceable against a worker without means). The sign is the same under both readings, so no per-reading sign is given.

The trainee's own ranking: CR-3 gives no single answer. An option is added (freedom to leave later) and one is removed (selling the promise for training). Those who would have chosen training in exchange for a restraint lose that exchange (C-25, CR-5a).

**C-8, workers already bound: pay.** For a bound worker in an existing job, rivals' options widen (they may hire the worker; CR-1, CR-9 along the `contract` relation). The worker's pay moves toward what rivals would offer (CR-6, CR-7a), through outside offers or counter-offers. Nothing pushes the other way for this group: the worker's value to the current employer in the current job is unchanged, and losing the worker to a rival now costs the employer more. Pay is measured including deferred pay as it vests, so a shift of pay from salary into deferred forms (C-4) does not count as a cut. The premise is that bound workers were paid less than some rival would pay (A-7).

**C-9 to C-11, job changes.**
- C-9: in the counterfactual, some bound workers who wanted a new employer had to leave their field to get one. Those moves are now made inside the field instead (CR-4a, CR-4b), and expanded unvested pay deters some of them as well (RS-11).
- C-10: total job changes combine moves that would not have happened at all (+) with the deterrent of expanded deferred pay on every departure (−). Moves switched from another field to a rival net to zero in the total. The total is ambiguous (section 7).
- C-11 is the first window of a timing shift (RS-8; `02_ontology.md`, 2.5). In the counterfactual, some bound workers would have moved to rivals in the second half of 2025, by buy-out, litigation, or a period out of the field. Knowing that the clause is void from January, they wait. The later window is part of C-1.

**C-12, partnership buy-ins.** Group practices already have partner tracks. Bringing a senior clinician in as an owner, with a bona fide buy-in, makes a later exit a sale of an ownership interest, and a restraint on it falls within K2. Token equity grants made only to fit K2 would probably not qualify (A-12, p = 0.3; not reported).

**Checked and not reported.**
- RS-3 (evasion): an employer can still write a void clause and rely on workers not knowing. K4 notices, the $5,000 damages and fee-shifting make that costly. A-20 (p = 0.35) is below the cut-off.
- RS-4 (relocation) is in section 6.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-15 | `employers.rivals` | `search_cost` (hiring experienced staff) | decrease | short to medium | CR-9, CR-1 | bound worker's employment contract with the old employer, and rivals' hiring: `contract`, close | A-1 |
| C-16 | `employers.net_trainers` | `asset_value` (owners' equity) | decrease | short (from announcement) | CR-7c, CR-10c, CR-7b | | A-15 |
| C-17 | `employers.rivals` | `asset_value` | ambiguous | short to medium | CR-7c, CR-7b; CR-12b | | A-16 |
| C-18 | `customers` | `search_cost` (finding a provider when theirs leaves) | decrease | medium | CR-9, CR-1 | client and individual provider (salons, clinics, advisers): `complement`, close | A-1, A-17 |
| C-19 | `customers` | `price_paid` (services in fields with heavy non-compete use) | ambiguous | medium to long | RS-13 (−); RS-14 (+); CR-12b | spin-off firms and incumbents: `same_market_other_segment`, close; experienced labor `input_to` these services | A-3, A-7, A-23 |
| C-20 | `intermediaries` | `quantity_traded` (placements of experienced staff) | increase | medium | CR-9 | recruiting services `input_to` experienced hires | A-1, A-21 |
| C-21 | `employers.net_trainers` | `investment_target` (new training-intensive establishments in Teravel rather than Mossgrave) | ambiguous | long | RS-4 (−); CR-7 (+); CR-12b | Teravel and Mossgrave labor markets: `across_border`, close | A-22, A-24 |
| C-22 | `officials.courts` | `enforcement_cost` | ambiguous | short to medium | OC-3; CR-4 (−, enforcement suits end; +, K5 suits, reading disputes, C-14) | | A-19 |

**C-16, firm values and incidence (CR-7b, CR-7c).** For firms that train more than they hire trained, the restraint protected part of their expected yield: trained staff and client relationships kept in the firm. The Act lowers that yield, for existing staff at once and for future staff by raising the cost of training or of retaining them. By CR-7c, owners at the time the change became expected bear the loss. The value fell in part from February 2025 as passage became likely, and the rest at passage in June. Later buyers of these firms pay the lower price.

Training already paid for before the announcement is a sunk investment. Its yield to the employer falls and cannot be recovered, so the loss on past training settles on the owners who paid for it (CR-7b, the immobile means). Future training is different. Its cost moves toward the trainees, through lower pay or less training (C-7), because the trained skill is now a means the worker can move.

**Is voiding existing contracts a transfer under CR-8?** It was checked and not recorded as one. CR-8b concerns payments, which add to the recipient exactly what they take from the payer. Voiding a restraint destroys a right; nobody receives it. The employer's loss of expected yield (C-16) is spread over several gainers, and none of them receives it in the same form:
- the worker gains an option and higher pay (C-1, C-8);
- founders gain entry (C-3);
- customers gain a provider they can follow (C-18).

Both sides are recorded, as the final check requires, but they are not claimed to be equal. CR-8e covers a confiscation of goods, not the extinction of a contractual right (Gaps found, b).

**C-17, rivals' firm values.** Hiring rivals gain access to experienced staff without buy-outs or suits (+). Under CR-7b, the gain from making trained workers mobile settles on the workers whose means can now move (C-8), not on the firms that hire them. Rivals pay for that access in competitive wages, and they also face higher retention costs for their own staff (−). Without a premise on which effect is larger, the sign is ambiguous.

**C-19, prices to customers.** Spin-offs add sellers (C-3), and by RS-13 added supply pushes price down. Higher pay for experienced staff (C-8) raises the cost of an input that is a material part of these services, and by RS-14 pushes price up. The result is ambiguous.

**C-21, location (RS-4).** Mossgrave is across the river, and its non-competes are enforceable. Some employers whose model rests on training staff who could be bid away locate new training-intensive work there (A-22). Firms that rely on hiring experienced staff, and founders, find Teravel's pool of mobile staff more attractive (A-24; CR-7 across locations). The result is ambiguous.

**Not reported: Mossgrave-bound workers taking Teravel jobs.** K1 covers anyone who primarily works in Teravel, whatever law the contract chooses. A Mossgrave worker bound by a Mossgrave clause could take a Teravel job to escape it. Mossgrave courts may still enforce the clause there, and A-25 (p = 0.4) is below the cut-off.

**GAP-034-1: know-how carried to a rival.** When a worker takes know-how to a rival, the rival uses it, and the first firm keeps it too. What the first firm loses is only its exclusive use, which is captured in C-16. Whether the field as a whole produces more because the same know-how is now used in two firms cannot be derived. CR-8 treats every means as rival: what one actor uses, another cannot. No core rule covers a means whose use by one actor does not reduce what is available to another. No consequence is reported on total output in the field; the worker-level claims (C-1, C-3, C-8) do not depend on it.

**Stopping points.** Recruiters' own staff (from C-20) are at depth 3 and diffuse; stopped. Suppliers to spin-offs are at depth 3; stopped. RS-9 (bundled trips) and RS-10 (informal trade) do not apply: no trade moves outside the legal market. RS-11 is used in its status form (C-9, C-10).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `workers.bound`, `job_changes` (to rivals and start-ups), short to medium | Option added and made known (CR-1, CR-4b, CR-11c; A-1, A-2). | Employers expand unvested deferred pay and retention bonuses (C-4; A-10), which a worker forfeits on any departure (RS-11). | Empirical premise, CR-12e: the substitute devices deter fewer moves to rivals than the non-compete did (A-9, p = 0.65). A device that deters as much would cost the employer deferred pay paid to every stayer, which a non-compete did not. Places that stopped enforcing non-competes saw mobility to competitors rise. | **increase** (C-1). If A-9 failed, **ambiguous**. |
| `workers.bound`, `job_changes` (to other fields), medium | None. | Moves that had to leave the field now stay in it (CR-4; A-8); expanded deferred pay deters any departure (RS-11; A-10). | None needed | **decrease** (C-9). The chains are independent, so it holds if either chain's premise holds (CR-12d). |
| `workers.bound`, `job_changes` (all), medium | Moves that would not have happened at all now do (CR-4b; A-1). | Expanded deferred pay deters every departure (RS-11; A-10). Moves switched from other fields to rivals do not change the total. | None. A-9 compares deterrence for moves to rivals only. | **ambiguous** (C-10). |
| `workers.trainees`, group, medium | Substitute restraints (C-4, C-6) restore some protection, and they are a different variable. | Lower value of an unrestrained trainee (CR-5c, CR-7a; A-5). | A-6 (substitutes do not fully restore the protection, p = 0.7) leaves at least one member moving down. | **at_least_one_decrease** (C-7). Restraints are not netted against pay (CR-12c). |
| `workers.bound`, `wage_rate`, short to medium | Outside offers and counter-offers (CR-6, CR-7a; A-7). | None found. The worker's value in the current job is unchanged, and pay is measured including deferred pay. | None needed | **increase** (C-8). |
| `employers.rivals`, `asset_value`, short to medium | Access to experienced staff without buy-outs or suits. | Competitive pay for that access, and higher retention costs for their own staff (CR-7b: the gain settles on the mobile workers). | None | **ambiguous** (C-17). |
| `customers`, `price_paid`, medium to long | Higher pay for experienced staff is a cost (RS-14; A-7, A-23). | More sellers from spin-offs (RS-13; A-3, A-23). | None | **ambiguous** (C-19). |
| `employers.net_trainers`, `investment_target` (in Teravel), long | Mobile labor pool attracts firms that hire experienced staff (CR-7; A-24). | Training-intensive work located in Mossgrave (RS-4; A-22). | None | **ambiguous** (C-21). |
| `officials.courts`, `enforcement_cost`, short to medium | K5 suits, disputes over U1, U2 and K2, trade-secret and non-solicitation claims (C-14; A-19). | About 400 enforcement suits a year end. | None | **ambiguous** (C-22). The transition probably raises disputes for a time, but no premise sets the size. |
| `founders.spinoff`, `entry_rate`, medium to long | Entry no longer barred (A-3). | Less employer-funded training (C-7) might mean fewer trained would-be founders later. That chain needs training itself to fall, and C-7 gives only a group sign, so the chain has no sign. | None needed | **increase** (C-3). |

## 8. Time structure

- **Announcement, February to June 2025.** As passage becomes more likely, the values of firms that rely on restraints fall part of the way (C-16; CR-7c), and the rest at passage. Employers' associations lobby (C-13).
- **Window, July to December 2025.** Bound workers who would have moved to rivals by buy-out or litigation wait for January (C-11). Employers begin rewriting contracts and adding retention pay (C-4, C-5, C-6). This is a path note, since none of it happens in the counterfactual.
- **Short run, 2026.** K4 notices go out by 1 March, and moves to rivals rise (C-1). Bound workers get counter-offers or move (C-8), rivals hire more easily (C-15), and recruiters place more (C-20). Courts lose enforcement suits but gain disputes over the readings and the exemptions (C-22). The readings of U1 and U2 are decided in this period. C-5 applies only if U1-a is adopted, and C-6 only if U2-b is; the two provisions are independent, so both, either or neither may apply.
- **Medium run, years 2 to 5.** New hiring cohorts are on new terms, so the trainee adjustments (C-7) apply to a growing share of the workforce. Spin-offs enter (C-3), and partnership buy-ins spread in practices (C-12). As existing contracts expire and are replaced, the effects on bound workers fade into the effects on all workers in these fields.
- **Long run.** Establishment location (C-21) adjusts as firms invest. Effects that exist only during the transition (C-11) have `persistence` n/a; the Act has no expiry.
- **Expectations.** If employers expect repeal or a narrow reading of U1 and U2 (C-13), they hold back irreversible changes such as relocation (C-21) and move first to cheap, reversible ones: retention pay and non-solicitation (TS-2).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-23 | `officials.enforcement` (Labor Bureau) | `enforcement_cost` (K1 and K5 cases) | increase | Staff time on the new task. | OC-3 |
| C-24 | `officials.enforcement` (Labor Bureau, other wage and consumer cases) | `enforcement_cost` (other rules) | decrease | Other enforcement displaced by the new task on a fixed budget. The cost falls on those that enforcement protected. | OC-3, CR-8a |
| C-25 | `workers.trainees`, `employers.net_trainers` | `quantity_traded` (exchanges of training or pay for a restraint) | decrease | Exchanges in which a worker would have promised not to compete in return for training, a job or pay. Both sides lose the gain each expected. | OC-4, CR-5a |

C-2's compliance work (lawyers' time, notices) is the main resource used up by employers (CR-8c), and it is not listed again. The fees are receipts to lawyers (CR-8b); the time is used up. C-23 and C-24 apply OC-3's fixed-budget case. No new appropriation was made, so taxpayers' means are not reduced (A-18); other enforcement is. Courts are in C-22. Their funding does not change with their caseload, so the same fixed-budget logic applies, but the sign of their workload is ambiguous.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Non-competes deter some bound workers from moves to rivals or start-ups they would otherwise make. | binding | 0.8 | 17% bound; about 400 suits a year and many more letters; surveys of workers citing a non-compete as the reason for declining an offer. | C-1, C-3, C-8, C-15, C-18, C-20 fail. |
| A-2 | Employers stop enforcing, and workers learn that the clause is void (K4 notices, damages and fee-shifting). | enforcement | 0.8 | K4 and K5 text; experience with mandated notices. | C-1 weaker; void clauses keep deterring. |
| A-3 | Some bound workers have plans to start a firm in their field that the non-compete blocks. | binding | 0.7 | Founder surveys; spin-off rates in comparable places with and without enforcement. | C-3 fails; one chain of C-19 fails. |
| A-4 | For many employers, reshaping restraints into the preserved forms costs less than the protection it restores. | other | 0.85 | Current use of non-solicitation and deferred pay; legal fees for redrafting. | C-4, C-5, C-6 fail. |
| A-5 | In a material share of trainee jobs, the non-compete protected the employer's recovery of the cost of general training. | other | 0.7 | Training spending by field; how often non-competes go with funded training; employer surveys. | C-7 fails; C-6 weakens. |
| A-6 | Substitute restraints (non-solicitation, unvested pay, and under U2-b repayment agreements) do not fully restore that protection. | substitutability | 0.7 | Repayment capped at actual cost and hard to collect; non-solicitation does not stop a worker serving a rival's clients. | C-7 fails: the pressure could be fully absorbed by restraints. |
| A-7 | Some bound workers are paid less than a rival would pay them. | other | 0.75 | Pay of movers before and after moves; pay gaps between bound and unbound workers in the same job. | C-8 fails; one chain of C-19 fails. |
| A-8 | In the counterfactual, some bound workers change employer by leaving their field. | mobility | 0.6 | Field-switching rates of workers with non-competes against those without. | One chain of C-9 fails; C-9 rests on A-10 alone. |
| A-9 | Substitute retention devices deter fewer moves to rivals than non-competes did (dominance premise, CR-12e). | other | 0.65 | Mobility to competitors after non-competes stopped being enforced in comparable places; cost to employers of retention pay. | C-1 becomes ambiguous. |
| A-10 | Employers expand unvested deferred pay and retention bonuses. | other | 0.6 | Current plan design; benefits consultants' advice after the Act. | The negative chains in C-1, C-9 and C-10 fail; C-10 becomes an increase. |
| A-11 | Courts accept bona fide partnership buy-ins as within K2, and practices use them. | other | 0.6 | Rulings under the 1998 partnership statute; how common partner tracks already are. | C-12 fails. |
| A-12 | Token equity grants, made only to bring a restraint within K2, qualify. | other | 0.3 | The same rulings required a substantial interest. | Below cut-off; not reported. |
| A-13 | Employers' associations, worker groups and start-up associations can organize at a cost below their stake. | other | 0.8 | Existing chambers of commerce, bar and medical associations, start-up councils; the 2025 hearings. | C-13 fails. |
| A-14 | Some bound workers would have moved to rivals in the second half of 2025, by buy-out or litigation, and can wait. | expectations | 0.6 | Monthly counts of suits and settlements; how long offers stay open. | C-11 fails. |
| A-15 | Non-competes protected a material part of net trainers' expected yield. | other | 0.7 | Share prices and deal values of firms relying on restraints, around the votes; how central trained staff and client books are to their earnings. | C-16 fails. |
| A-16 | Some firms hire more trained staff than they train. | other | 0.8 | Hiring records by experience level. | C-17 is not defined for any firm. |
| A-17 | Non-solicitation bars only contact the worker initiates; clients may follow a provider on their own. | other | 0.7 | K3(b) says "solicit"; common-law meaning of solicitation. | C-18 fails. |
| A-18 | The Labor Bureau's budget is not raised for the new task. | revenue_use | 0.7 | No appropriation in the Act; the next budget cycle. | C-24 becomes a cost to taxpayers instead. |
| A-19 | Employers turn to trade-secret and non-solicitation claims against departing staff. | substitutability | 0.7 | Claim filings in places that stopped enforcing non-competes. | C-14 fails; one chain of C-22 fails. |
| A-20 | Employers keep writing void clauses and rely on workers not knowing. | enforcement | 0.35 | K4 notices and K5 damages make it costly. | Below cut-off; not reported. |
| A-21 | Recruiters handle a material share of experienced hires in these fields. | other | 0.7 | Placement data. | C-20 fails. |
| A-22 | Some employers locate new training-intensive work in Mossgrave because restraints are enforceable there. | mobility | 0.55 | Distance across the river; existing two-state employers. | One chain of C-21 fails; C-21 would become an increase. |
| A-23 | Spin-off entry adds supply that is not offset elsewhere (RS-13), and experienced staff pay is a material part of these services' costs (RS-14). | other | 0.6 | Cost structure of salons, clinics and advisory firms; spin-off counts. | One or both chains of C-19 fail. |
| A-24 | Firms that rely on hiring experienced staff, and founders, prefer to locate where staff are mobile. | mobility | 0.6 | Location choices of start-ups and hiring-intensive firms across enforcement boundaries. | One chain of C-21 fails; C-21 would become a decrease. |
| A-25 | Mossgrave-bound workers escape their restraints by taking Teravel jobs. | other | 0.4 | Mossgrave courts may still enforce against them. | Below cut-off; not reported. |

### Final check before the report

The eight checks in `03_workflow.md` were run on the list.

1. **Uncombined chains.** Every key reached by two chains is in section 7:
   - moves to rivals (C-1) against expanded deferred pay;
   - total job changes (C-10);
   - rivals' firm values (C-17);
   - customer prices (C-19);
   - location (C-21);
   - courts (C-22);
   - entry (C-3).

   The timing shift (C-11) and C-1 are different windows, so they are separate keys. Bound workers' pay was checked for an opposing chain, and none was found once pay includes deferred pay.
2. **Single signs for a group.** The trainee response is a group (C-7), signed only with A-6, because its other margin, substitute restraints, moves in the opposite direction.
3. **Baseline.** Every sign is against Teravel with reasonable non-competes enforced, not against Mossgrave's law and not against the time before the bill.
4. **Worse off is not poorer.** No `resources_available_other_uses` is signed. Employers' loss is recorded as `asset_value` (C-16), from a lower expected yield, and as compliance cost.
5. **Timing.** Moves to rivals happen with and without the Act, so the window before 1 January is signed (C-11), as is the window after (C-1). Contract rewriting before January would not happen at all without the Act, so it is a path note.
6. **Both sides of transfers.** Voiding a right is not a payment (section 6). Both the loser (C-16) and the gainers (C-1, C-3, C-8, C-18) are recorded. Lawyers' fees are receipts as well as costs.
7. **Every actor class, every core rule.**
   - CR-7c was applied to net trainers and to rivals.
   - CR-6 was applied to trainee terms and bound workers' pay.
   - CR-9 was applied to rivals, customers and recruiters.
   - OC-3 was applied to the Bureau and the courts.
   - CR-11c was applied to the notice.
   - RS-3 and RS-4 were checked.
8. **Unstated premises.**
   - "Some actors are at the margin" is A-1, A-3 and A-8.
   - The ability to organize is A-13.
   - "The substitute is incomplete" is A-6.
   - The dominance premise is A-9, stated as an empirical premise (CR-12e).

## 11. Report

**The policy.** From 1 January 2026, Teravel will not enforce any term that stops a worker from working for a competitor, or starting a competing business, after leaving a job. This covers contracts already signed. It does not cover a person who sells a business or an ownership stake. Agreements to keep secrets, not to solicit clients or staff for up to a year, notice periods, and forfeiture of unvested pay remain valid. Employers must tell affected current and recent workers by 1 March 2026, and workers can sue for damages if an employer tries to enforce a void clause. Two points are unclear: whether long paid notice periods ("garden leave") count as restraints (U1), and whether training repayment agreements count as penalties (U2).

**Visible consequences.** More bound workers leave for rivals or start their own firms (C-1). This holds given that substitute retention devices deter fewer such moves than non-competes did (A-9). Employers spend on rewriting contracts and sending notices (C-2).

**Invisible consequences.**
- *Workers already bound.*
  - They are paid more, through outside offers and counter-offers (C-8).
  - Fewer of them leave their field just to change employer (C-9).
  - Some who would have moved to a rival in late 2025 waited for January (C-11).
- *New trainees.* In jobs where employers paid for training that rivals value, at least one of these falls: trainee pay, employer-funded training, or the number of trainees hired (C-7). Exchanges of training for a promise not to compete no longer happen (C-25).
- *Employers that train more than they hire.*
  - The value of their firms fell when the Act became likely, a loss borne by their owners then and not by later buyers (C-16).
  - They move restraints into the forms the Act leaves alone (C-4). They use paid garden leave if U1 is read narrowly (C-5), and training repayment agreements if U2 is read narrowly (C-6).
  - They bring more trade-secret and non-solicitation claims (C-14).
- *Professional practices* move senior staff into partnership buy-ins, so that a restraint on leaving falls within the sale-of-business exemption (C-12).
- *Others.*
  - Rival employers find experienced staff more easily (C-15), and recruiters place more of them (C-20).
  - Former employees start more firms in their field (C-3).
  - Clients can follow a provider who moves (C-18).
  - The Attorney General's Labor Bureau spends on the new task, and other enforcement falls (C-23, C-24).
  - Interest groups lobby over repeal and the unclear provisions (C-13).

**Ambiguous effects.**
- Total job changes (C-10): moves that now happen, against wider use of unvested pay, which deters every departure.
- The value of firms that hire experienced staff (C-17): the gain from free movement goes mainly to the workers.
- Prices to customers (C-19): more competitors, against higher pay for experienced staff.
- Whether new training-intensive work locates in Teravel or across the river (C-21).
- Courts' total workload (C-22).

**Key conditions.**
- Moves to rivals rise only if substitute devices deter less than non-competes did (A-9, p = 0.65).
- The trainee effect rests on non-competes having protected training costs (A-5, p = 0.7), and on substitutes not fully replacing them (A-6, p = 0.7).
- Firm values fall where restraints protected a material part of a firm's earnings (A-15, p = 0.7).
- How U1 and U2 are read decides which substitute restraints employers use, not the direction of the main effects.

**What this analysis cannot say.**
- How many more people change jobs, or by how much pay rises.
- Whether the gains to workers who move outweigh the losses to firms and trainees, or whether the Act is desirable.
- Whether the field as a whole produces more because know-how spreads. That question needs a rule for means that two firms can use at once (GAP-034-1).
- Which reading of U1 and U2 the courts will adopt.
- Courts' workload, beyond its direction being ambiguous.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | workers.bound | job_changes (to rivals and start-ups) | increase | short–medium | visible | B | CR-1, CR-4b, CR-11c; RS-11 opposing; CR-12b, CR-12e | A-1, A-2, A-9 |
| C-2 | employers holding non-competes | compliance_cost | increase | short | visible | A | OC-2, CR-8c | none |
| C-3 | founders.spinoff | entry_rate (same-field firms) | increase | medium–long | invisible | B | CR-1, CR-4b | A-1, A-3 |
| C-4 | employers.net_trainers | reclassification (non-solicitation, confidentiality, unvested pay) | increase | short–medium | invisible | B | RS-5 | A-4 |
| C-5 | employers.net_trainers | reclassification (paid garden leave; reading U1-a only) | increase | short–medium | invisible | B | RS-5 under U1-a; no chain under U1-b | A-4 |
| C-6 | employers.net_trainers | reclassification (training repayment agreements; reading U2-b only) | increase | short–medium | invisible | B | RS-5 under U2-b; no chain under U2-a | A-4, A-5 |
| C-7 | workers.trainees | wage_rate (training), non_wage_compensation (funded training), employment (trainee hires) (group) | at_least_one_decrease | medium | invisible | B | RS-2, CR-5c, CR-7a, CR-6 | A-5, A-6 |
| C-8 | workers.bound | wage_rate (including vested deferred pay) | increase | short–medium | invisible | B | CR-1, CR-9, CR-6, CR-7a | A-1, A-7 |
| C-9 | workers.bound | job_changes (to other fields) | decrease | medium | invisible | B | CR-4a, CR-4b; RS-11; CR-12d | A-8, A-10 |
| C-10 | workers.bound | job_changes (all) | ambiguous | medium | invisible | B | CR-4b (+); RS-11 (−); CR-12b | A-1, A-10 |
| C-11 | workers.bound | job_changes (to rivals, July–December 2025) | decrease | short | invisible | B | RS-8, CR-10a | A-14 |
| C-12 | practices.professional | reclassification (partnership buy-ins under K2) | increase | medium | invisible | B | RS-5 | A-11 |
| C-13 | employers.net_trainers; worker and start-up associations | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-13 |
| C-14 | employers.net_trainers | quantity_substitute (trade-secret and non-solicitation claims) | increase | short–medium | invisible | B | RS-1 | A-19 |
| C-15 | employers.rivals | search_cost (experienced hires) | decrease | short–medium | invisible | B | CR-9, CR-1 | A-1 |
| C-16 | employers.net_trainers | asset_value | decrease | short | invisible | B | CR-7c, CR-10c, CR-7b | A-15 |
| C-17 | employers.rivals | asset_value | ambiguous | short–medium | invisible | B | CR-7c, CR-7b; CR-12b | A-16 |
| C-18 | customers | search_cost (replacing a provider) | decrease | medium | invisible | B | CR-9, CR-1 | A-1, A-17 |
| C-19 | customers | price_paid | ambiguous | medium–long | invisible | B | RS-13 (−), RS-14 (+); CR-12b | A-3, A-7, A-23 |
| C-20 | intermediaries (recruiters) | quantity_traded (placements) | increase | medium | invisible | B | CR-9 | A-1, A-21 |
| C-21 | employers.net_trainers | investment_target (training-intensive establishments in Teravel) | ambiguous | long | invisible | B | RS-4 (−), CR-7 (+); CR-12b | A-22, A-24 |
| C-22 | officials.courts | enforcement_cost | ambiguous | short–medium | invisible | B | OC-3, CR-4; CR-12b | A-19 |
| C-23 | officials.enforcement | enforcement_cost (K1, K5 cases) | increase | short | invisible | A | OC-3 | none |
| C-24 | officials.enforcement | enforcement_cost (other rules) | decrease | short–medium | invisible | B | OC-3, CR-8a | A-18 |
| C-25 | workers.trainees, employers.net_trainers | quantity_traded (training-for-restraint exchanges) | decrease | medium | invisible | B | OC-4, CR-5a | A-5 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).**
- GAP-034-1 (open): **non-rival means.** Know-how carried by a worker to a rival is used there without being lost to the first firm, which loses only its exclusive use. CR-8 ("a policy does not create means; it redirects or uses them up") treats every means as rival. No core rule says how to reason about a means whose use by one actor does not reduce what is available to another. As a result, the claim that a field produces more when know-how spreads cannot be derived, nor its negation. Worker-level and firm-value claims are unaffected: CR-1, CR-4, CR-7c and CR-9 derive them. A candidate clause for CR-8: "where a means can be used by several actors at once (knowledge, a design), a policy that widens its use transfers its exclusive yield (CR-7c) but does not withdraw it from its first user." For the experts: is that praxeologically sound, and does it belong in CR-8 or in a new rule?

**(b) Unclear core rules (wording that was hard to apply here).**
- **CR-8 and the extinction of a right.** CR-8b covers payments, which add to the recipient exactly what they take from the payer. CR-8e covers confiscated goods. Neither says whether voiding an existing contractual right is a transfer. Here the employer's lost expected yield goes to no single recipient in the same form: workers gain an option, founders gain entry, customers gain a provider they can follow. The case was handled with CR-1, CR-3 and CR-7c, recording both sides without claiming they are equal. The final check's item 6 ("both sides of every transfer") was hard to apply. Proposed: a clause CR-8f, "a policy that extinguishes a right does not transfer it; the holder's loss is a fall in expected yield (CR-7c), and the gains to others are derived separately by CR-1 and CR-9."
- **CR-1's note on void-contract rules.** The note says such a rule "removes an option for one side and adds one for the other". A ban on a contract term also removes an option from the side it protects: the worker can no longer sell the promise in exchange for training. So both sides lose an option and one side gains one. That matters for CR-3: the trainee's own ranking gives no single answer (section 5). Proposed wording: "a rule that voids a term removes, for both parties, the option of agreeing to it, and for the party it restrained, adds the option it restrained."
- **CR-6 with margins that move in opposite directions.** CR-6 says to record the open margins as a group with `at_least_one_increase` (or decrease). Here the employer's pressure goes to trainee pay and training (down) and to substitute restraints (up). The members do not share a direction, so the group cannot be signed without a premise that one margin does not absorb it all (A-6). CR-6 should say what to do when the margins of one pressure move in opposite directions on their own variables. The same problem arises with RS-14's "price up and/or quantity down" (WE-035).
- **CR-7b when a means becomes mobile.** CR-7b says the lasting gain or loss settles on the means that cannot move. Here the policy makes a means mobile: trained workers who were bound. The gain from that settles on the newly mobile means (C-8), not on the firms that can now hire it (C-17). This is consistent with CR-7a, but the wording of CR-7b does not cover a change in mobility itself. A sentence would help: "a policy that makes a means mobile shifts the yield toward its owner, at the expense of whoever held it fixed."

**(c) Missing patterns (derived moves likely to recur).**
- **Proposed pattern, a banned restraint on an investment embodied in a mobile means.**
  - **If:** a policy voids a term that let one party recover an investment embodied in a means the other party controls and can move: general training in a worker; tenant improvements under a lease; client lists built by an agent.
  - **Then:** for new contracts, the investing party's maximum terms fall (CR-5c). The investment's cost moves to the party who controls the means: lower pay during training, less investment, or fewer such contracts, recorded as a group with `at_least_one_decrease`, given a premise that substitute terms do not fully restore recovery. Exchanges of the investment for the restraint decrease (CR-5a).
  - **Derivation:** CR-5c, CR-7a (the means' yield tends to what others will pay once it can move), CR-6 (pressure to open margins), CR-4. It recurs wherever a contract term protecting a specific investment is banned.
- **Proposed pattern, retroactive voiding of contract terms.**
  - **If:** a policy voids a term in existing contracts.
  - **Then:** the holder of the right bears a fall in `asset_value`, from the time the change becomes expected and in proportion to its probability (CR-7c, CR-10c). The counterparty's options widen (CR-1). Where the contract can be ended or renegotiated at will, the remaining terms adjust as for new contracts (CR-5c). Where it cannot, they do not until renewal. Past consideration given for the term is sunk and is not returned (CR-10b).
  - **Derivation:** CR-1, CR-3, CR-7c, CR-10b, CR-10c. It recurs in rent rules applied to existing leases, rate caps on existing loans, and changes to existing franchise terms.
- **Proposed pattern, removing a mobility restraint.**
  - **If:** a policy removes a restraint on a factor's moving to competitors.
  - **Then:**
    - moves to competitors increase and moves out of the field decrease (CR-4);
    - same-field entry by the factor's owners increases (CR-4);
    - the factor's pay moves toward what competitors would pay (CR-6, CR-7a);
    - the gain settles on the factor, not on the hiring firms (CR-7b).

    Holders of the restraint substitute other retention devices (RS-5), whose lock-in (RS-11) opposes the rise in total moves.
  - **Derivation:** as listed. It is the mirror of RS-11.
- **Note on the catalog.** RS-2 fitted the trainee case ("a policy fixes ... one term of an exchange"), but its Then clause speaks of quality, maintenance and contract length, not of moving the cost of an investment between the parties.

**(d) Vocabulary.**
- **No instrument type for prohibiting a contract term.** In 2.3, `prohibition` is "of a good or service". A ban on a term of exchange (non-competes, mandatory arbitration, certain lease clauses), especially a retroactive one, is triangular but not a ban on a good. Proposed: `term_prohibition`, with a field for whether it applies to existing contracts.
- **No variable for the prevalence of a contract term.** `reclassification` records only reshaping to avoid a policy, so it cannot record a fall in a term that exists in the counterfactual. Under U1-b, garden leave clauses that would have existed become void, and there is no variable for that fall. Proposed: `restrictive_terms` (share of contracts in a market with a named restrictive term).
- **No sign for "no chain under this reading".** 2.5 asks for one sign per reading, and the checker requires a sign for each. Where a chain operates under one reading and not at all under the other (C-5, C-6), neither "increase" nor "ambiguous" is right for the second reading. The workaround here was to name the reading in the variable and give the sign plainly. Proposed: allow `none` as a per-reading sign ("U1-a: increase; U1-b: none").
- **Group signs whose members move in opposite directions.** These are needed for CR-6 and RS-14 (see b). One option is to allow a group of the form `wage_rate decrease, reclassification increase: at_least_one`, scored as correct if at least one member moves as stated and none moves the other way.
