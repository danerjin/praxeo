# WE-034 Non-compete clauses made unenforceable, for new and existing contracts

Analyst: draft (Handbook 0.6, corrected under 0.8)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional state, modeled on a common type of law. It is a gap-probing example. The policy does not impose a contract term; it prohibits one, and it does so retroactively. That tests:
- CR-1, where one provision removes an option for both parties and adds one for one of them;
- CR-5c, where the bargaining range moves on every other term of the employment contract;
- RS-5, where restraints are rewritten into forms the law leaves untouched;
- CR-7b and CR-7c, for who bears the loss of a protection paid for in the past;
- CR-8, for whether voiding an existing right is a transfer (it is, under the 0.7 CR-8 clarification and PC-18).

The probabilities are illustrative; the evidence column says what a real analysis would cite. Courts appear only through their enforcement cost.

## 1. Policy record

**Teravel Freedom to Work Act.** The State of Teravel has about 3.2 million private-sector workers. A 2024 survey by the state labor department found that about 17% had signed a non-compete clause. The share is higher in some fields: software and engineering 45%, sales 35%, physicians and dentists in group practices 40%, finance 30%, hair and beauty salons 25%. Until now Teravel courts enforced "reasonable" non-competes (up to two years, within the employer's trading area) under common law. Employers filed about 400 enforcement suits a year, and many more disputes were settled by letter. Teravel's largest city, Halbrook, lies on a river whose far bank is in the State of Mossgrave. Mossgrave enforces non-competes, and about 60,000 people commute across the river each way.

The bill was introduced on 3 February 2025 with the governor's public support. It passed on 12 June 2025 and takes effect on 1 January 2026, with no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Void restraint | `term_prohibition`, applying to existing contracts and pending cases | "Any term of an employment or independent-contractor agreement that prohibits or restricts a worker, after the work relationship ends, from working for another person or carrying on a business, or that imposes a penalty for doing so" | Employers of workers who primarily work in Teravel, whatever law the contract chooses | Such terms are void. This applies to agreements made before, on or after the effective date, and pending cases are decided under the Act. Includes "forfeiture for competition" clauses (deferred pay lost only if the worker joins a competitor). | K2, K3 |
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
| K1 | Triangular: it prohibits a term of exchange between two private parties. For existing contracts, it withdraws state enforcement of a right one party already holds. | Yes, for the roughly 17% of workers with a non-compete, of whom some would otherwise move (A-1). | PC-18, RS-4, RS-5, RS-7, RS-8, RS-11, OC-4; CR-1, CR-5c, CR-6, CR-7 and CR-8 as PC-18 cites them |
| K2, K3 | Exemptions: boundaries that restraints can be moved across | Yes, as routes (A-4, A-11) | RS-5 |
| K4 | Mandated action, with no payment to the state: a compliance cost, and a channel of information to workers | Yes | OC-2; CR-11c |
| K5 | Enforcement: private suits, and the Attorney General on a fixed budget | Yes (A-2, A-18) | OC-3 |

**CR-1 operations, per actor class.** The counterfactual is that reasonable non-competes are enforced. Following the 0.8 CR-1 recording note, a void-contract rule removes, for both parties, the option of agreeing to the term, and adds an option for the party it restrained.

| Actor class | Operations |
|---|---|
| `workers.bound` (existing contracts) | Operation 2: they may now work for a rival or start a competing firm. Operation 3: a risk (a suit, or an injunction) is removed from that option. |
| `employers.net_trainers` and all employers holding non-competes (`employers.restraining`) | Operation 1: enforcing the restraint, and agreeing to a new one, is removed. Operation 3: a burden is attached to including one ($5,000 per worker plus fees). Under K1's pending-cases clause, operation 1 also applies to suits filed before 1 January 2026 and still pending then. |
| `workers.trainees` and every future worker | Operation 1: the option to sell a promise not to compete, in exchange for training, pay or a job, is removed. Operation 2: future freedom to leave for a rival. The worker's own side therefore has an option removed as well as one added, as the 0.8 CR-1 recording note now states. |
| `employers.rivals` | Operation 3: the litigation risk, demand letters and buy-outs attached to hiring a bound worker are removed (A-28). |
| `practices.professional` and other employers | Operation 2 in effect: K2 and K3 leave routes into the exempt forms. |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `workers.bound` | About 540,000 current and recent workers with a non-compete in an existing contract | May join a rival or start a firm. They are told so by notice (K4). |
| `workers.trainees` (`buyers.prospective` of training; sellers of labor) | New hires into jobs where the employer funds general training (sales, software, salons, junior clinicians) | Can no longer offer a restraint in exchange for training or pay; will be free to leave once trained. |
| `founders.spinoff` (`sellers.prospective`) | Bound workers who would start a firm in the same field | Entry is no longer barred. |
| `employers.net_trainers` (`sellers.current`, `factor_owners.specific`) | Firms that train more staff than they hire already trained, and that relied on non-competes | Lose the restraint on existing and future staff. May use the preserved forms. |
| `employers.restraining` | All employers holding non-competes, net trainers included | Lose the restraint, buy-out receipts and forfeiture-for-competition clauses; must give notice. |
| `employers.rivals` | Firms, including spin-offs, that hire experienced staff from competitors | Can hire bound workers without buy-outs or suits. |
| `practices.professional` | Medical, dental and accounting group practices | Can move senior staff into partnership buy-ins inside K2. |
| `customers` (`buyers.current`) | Clients of firms in fields with heavy non-compete use | Can follow a provider who moves, and face new spin-off sellers. |
| `intermediaries` | Recruiters placing experienced staff; lawyers advising employers | More candidates are placeable; legal work shifts from enforcing non-competes to redrafting and other claims. |
| `officials.enforcement` | Attorney General's Labor Bureau | New task on a fixed budget. |
| `officials.courts` | State courts | Lose non-compete enforcement suits; gain suits under K5, disputes over U1 and U2, and substitute claims. |
| `neighboring_jurisdictions` | Employers and workers in Mossgrave | Mossgrave restraints stay enforceable there; location choices across the river change (C-36, C-37). |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `workers.bound` | `job_changes` (to rivals and to their own start-ups, from 1 January 2026) | increase | short to medium | CR-1 (operation 2), CR-4b (x: stay, y: join a rival), CR-11c (the K4 notice tells them); PC-18 (mobility); combined with RS-11 (section 7) | A-1, A-2, A-9 |
| C-2 | `employers.restraining` | `compliance_cost` (contract review and rewriting, K4 notices) | increase | short | OC-2, CR-8c | none |

C-1 is the visible aim: people bound by a non-compete can now leave for a competitor. Many bound workers would not know that their clause is void without being told, and some believed that unenforceable clauses bound them even before the Act. The K4 notice is the channel by which the change in options reaches their beliefs (CR-11c). The sign for moves to rivals holds against an opposing chain only with a dominance premise (A-9); see section 7.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `founders.spinoff` | `entry_rate` (firms founded by former employees in the same field) | increase | medium to long | CR-1 (operation 2), CR-4b (x: stay employed, y: found a firm); CR-12, 0.8 (opposing chain below 0.5, section 7) | A-1, A-3 |
| C-4 | `employers.net_trainers` | `term_prevalence` (non-solicitation, confidentiality and unvested deferred pay terms) | increase | short to medium | RS-5, PC-18 (substitute terms) | A-4 |
| C-5 | `employers.net_trainers` | `term_prevalence` (paid notice periods of six months or more, "garden leave") | U1-a: increase; U1-b: decrease | short to medium | U1-a: RS-5, PC-18. U1-b: CR-1 (operation 1), PC-18 | A-4, A-26 |
| C-6 | `employers.net_trainers` | `term_prevalence` (training repayment agreements) | U2-a: decrease; U2-b: increase | short to medium | U2-a: CR-1 (operation 1), PC-18. U2-b: RS-5, PC-18 | A-4, A-5, A-26 |
| C-7 | `workers.trainees` | `wage_rate` (during training), `non_wage_compensation` (employer-funded general training), `employment` (trainee hires) (group) | at_least_one_decrease | medium | PC-18, RS-2, CR-5c, CR-7a, CR-6 | A-5, A-6 |
| C-8 | `workers.bound` | `wage_rate` (pay per hour, including deferred pay as it vests) | increase | short to medium | CR-1, CR-9, CR-6, CR-7a; CR-7 (a policy that makes a means mobile) | A-1, A-7 |
| C-9 | `workers.bound` | `job_changes` (to other fields) | decrease | medium | CR-4a, CR-4b; RS-11 | A-8, A-10 |
| C-10 | `workers.bound` | `job_changes` (all destinations) | ambiguous | medium | CR-4b (+); RS-11 (−); CR-12b | A-1, A-10 |
| C-11 | `workers.bound` | `job_changes` (to rivals and start-ups, 3 February to 31 December 2025) | ambiguous | short | RS-8 (−, and its 0.8 clause on a pending-cases provision, +), CR-10a, CR-4; CR-12b; CR-12, 0.8 (opposing chain with p ≥ 0.5) | A-14, A-27 |
| C-12 | `practices.professional` | `reclassification` (salaried senior clinicians moved into partnership buy-ins, so that a restraint on exit comes within K2) | increase | medium | RS-5 | A-11 |
| C-13 | `employers.net_trainers`; worker and start-up associations | `lobbying_effort` (over repeal, over the readings of U1 and U2, and over the scope of K2 and K3) | increase | short to medium | RS-7 | A-13 |
| C-14 | `employers.net_trainers` | `quantity_substitute` (trade-secret and non-solicitation claims brought against departing staff) | increase | short to medium | RS-1 | A-19 |
| C-26 | `workers.bound` | `non_wage_compensation` (unvested deferred pay and retention bonuses) | increase | short to medium | PC-18 (substitute terms), CR-4 (x: lose the worker to a rival, y: pay to retain), CR-5c, CR-6 | A-10 |
| C-27 | `employers.restraining` | `quantity_traded` (buy-outs sold: releases of bound workers for payment) | decrease | short to medium | CR-10a (2025: workers wait, A-14); CR-1 operation 1 (2026 on: nothing to buy out, A-28); CR-8b; CR-12d | chain 1: A-14; chain 2: A-28 |
| C-28 | `employers.rivals` | `quantity_traded` (buy-outs bought: payments to release bound workers they hire) | decrease | short to medium | CR-8b (the other side of C-27), CR-1 operation 3 | chain 1: A-14; chain 2: A-28 |
| C-29 | `employers.restraining` | `quantity_traded` (client accounts served) | decrease | short to medium | CR-9 (client and provider), CR-4 for clients (x: stay with the firm, y: follow the provider) | A-1, A-2, A-17 |

**C-4 to C-6, substitute terms (RS-5, PC-18).** K3 draws a line between restraints that are void and terms that are preserved. Employers whose non-competes protected something they value move to the preserved forms where these serve nearly the same end. PC-18 records this as a rise in `term_prevalence` of the substitute terms.
- Customer and staff non-solicitation protects client relationships.
- Confidentiality protects secrets.
- Unvested deferred pay raises the cost of any departure. The amount of such pay is C-26.

Two forms depend on the readings, and each is signed per reading.
- C-5: under U1-a, a long paid notice period is a close substitute for a non-compete, bought with salary: more of them (RS-5). Under U1-b they are void, so those that exist in the counterfactual (A-26) are removed (CR-1, operation 1): fewer of them.
- C-6: under U2-b, repayment agreements recover training costs and are used more (RS-5, given A-5). Under U2-a they are void, and those in the counterfactual are removed (A-26).

**C-7, trainees: the bargaining range moves (PC-18, CR-5c).** In the counterfactual, a trainee in a training-intensive job gives a promise not to compete and receives general training: skills that rival employers also value. K1 fixes that term of the exchange at "no restraint". PC-18 gives the response; the derivation from the core rules is as follows.
- Once trained, the worker can move to a rival. The worker's pay therefore tends toward what rivals would pay for the trained skill (CR-7a, the means can now move), and the employer cannot recover the cost of general training out of pay after training.
- The most an employer will give for an unrestrained trainee is lower than for a restrained one (CR-5c).
- The pressure moves to the margins still open (CR-6): pay during training, training funded, and the number of trainees hired. The other open margin is substitute restraints (C-4, C-6), which move the opposite way.

Under 0.7, PC-18 and the CR-6 clarification would allow the whole set as a mixed group with `at_least_one_as_stated`, substitute terms (+) included. The narrower claim here, that at least one of the three trainee terms falls, needs the premise that the substitute restraints do not restore the protection fully (A-6), and with it is valid. Under U2-a, repayment agreements are void, so A-6 holds more firmly. Under U2-b it rests on the limits of repayment agreements (capped at actual cost, and unenforceable against a worker without means). The sign is the same under both readings, so no per-reading sign is given. No single member is signed: lower trainee pay is an open margin, and no premise excludes it (CR-6 needs a premise per margin).

The trainee's own ranking: CR-3 gives no single answer. An option is added (freedom to leave later) and one is removed (selling the promise for training), as the 0.8 CR-1 recording note states. Those who would have chosen training in exchange for a restraint lose that exchange (C-25, CR-5a).

**C-8, workers already bound: pay.** For a bound worker in an existing job, rivals' options widen (they may hire the worker; CR-1, CR-9 along the `contract` relation). The worker's pay moves toward what rivals would offer (CR-6, CR-7a), through outside offers or counter-offers; the gain from the worker's new mobility goes to the worker (CR-7, a policy that makes a means mobile). Nothing pushes the other way for this group: the worker's value to the current employer in the current job is unchanged, and losing the worker to a rival now costs the employer more. Pay is measured including deferred pay as it vests, so a shift of pay from salary into deferred forms (C-4, C-26) does not count as a cut. The premise is that bound workers were paid less than some rival would pay (A-7).

**C-9 to C-11, job changes.**
- C-9: in the counterfactual, some bound workers who wanted a new employer had to leave their field to get one. Those moves are now made inside the field instead (CR-4a, CR-4b), and expanded unvested pay deters some of them as well (RS-11).
- C-10: total job changes combine moves that would not have happened at all (+) with the deterrent of expanded deferred pay on every departure (−). Moves switched from another field to a rival net to zero in the total. The total is ambiguous (section 7).
- C-11 is the window before the effective date (RS-8; `02_ontology.md`, 2.5), from introduction, when the Act first became expected (CR-10a). Two timing chains meet in it. Some bound workers who would have moved to rivals in 2025, by buy-out, litigation or a period out of the field, wait for January (−, A-14); those moves are part of C-1. But K1 applies to pending cases, so a worker who moves late in 2025 and is sued has the suit decided under the Act: the earlier window is also made better, and some who would not have moved in 2025 move then (+, A-27). This is the case named in RS-8's 0.8 clause. The (+) chain needs a premise the record does not settle (preliminary injunctions before 1 January limit it); with p = 0.55 it is a chain under the 0.8 CR-12 note, and no dominance premise is available. The window is **ambiguous**.

**C-12, partnership buy-ins.** Group practices already have partner tracks. Bringing a senior clinician in as an owner, with a bona fide buy-in, makes a later exit a sale of an ownership interest, and a restraint on it falls within K2. Token equity grants made only to fit K2 would probably not qualify (A-12, p = 0.3; not reported).

**C-26, retention pay.** Employers who lose the restraint keep staff by paying them to stay (CR-4, x: lose the worker, y: retain). The pressure goes to unregulated terms (CR-6): unvested deferred pay, which K3(d) preserves, and retention bonuses (A-10). This is the response whose lock-in is the (−) chain in C-1, C-9 and C-10.

**C-27 and C-28, buy-outs.** In the counterfactual, a rival that wanted a bound worker often paid the old employer to release them, or bore a suit (A-28). From 2026 there is no enforceable restraint to buy out of (CR-1, operation 1); in 2025, workers who wait for January (A-14) are not bought out, and workers who move early under the pending-cases clause rely on the Act, not on a buy-out. Both windows have fewer buy-outs. Each buy-out is an exchange with two sides, a receipt to the old employer and an outlay of the hiring firm (CR-8b), so both are recorded.

**C-29, clients lost.** A client may follow a provider who moves (C-18), since non-solicitation bars only contact the worker initiates (A-17). Each client who follows is an account the old employer no longer serves (CR-9, CR-4 applied to the client).

**Checked and not reported.**
- RS-3 (evasion): an employer can still write a void clause and rely on workers not knowing (`legal_breach`). K4 notices, the $5,000 damages and fee-shifting make that costly. A-20 (p = 0.35) is below the cut-off.
- RS-4 (relocation) is in section 6.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-15 | `employers.rivals` | `search_cost` (hiring experienced staff) | decrease | short to medium | CR-9, CR-1 (operation 3) | bound worker's employment contract with the old employer, and rivals' hiring: `contract`, close | A-1, A-28 |
| C-16 | `employers.net_trainers` | `asset_value` (owners' equity) | decrease | short (from announcement) | CR-7c, CR-10c, CR-7b; CR-8 (voiding a contract right); PC-18 | | A-15 |
| C-17 | `employers.rivals` | `asset_value` | ambiguous | short to medium | CR-7c, CR-7b; CR-12b | | A-16, A-28 |
| C-18 | `customers` | `search_cost` (finding a provider when theirs leaves) | decrease | medium | CR-9, CR-1 | client and individual provider (salons, clinics, advisers): `complement`, close | A-1, A-17 |
| C-19 | `customers` | `price_paid` (services in fields with heavy non-compete use) | ambiguous | medium to long | RS-13 (−); RS-14 (+); CR-12b | spin-off firms and incumbents: `same_market_other_segment`, close; experienced labor `input_to` these services | A-3, A-7, A-23 |
| C-20 | `intermediaries` (recruiters) | `quantity_traded` (placements of experienced staff) | increase | medium | CR-9 | recruiting services `input_to` experienced hires | A-1, A-21 |
| C-21 | `employers.net_trainers` | `investment_target` (new training-intensive establishments in Teravel rather than Mossgrave) | decrease | long | RS-4, CR-4 (x: here, y: there), CR-7a | Teravel and Mossgrave labor markets: `across_border`, close | A-22 |
| C-22 | `officials.courts` | `enforcement_cost` (total) | ambiguous | short to medium | OC-3; CR-12b over C-33 (−) and C-34 (+) | | A-2, A-4, A-19 |
| C-30 | `intermediaries` (lawyers) | `quantity_traded` (non-compete enforcement work) | decrease | short to medium | CR-9, CR-1 (operation 1) | legal services `input_to` employers' enforcement, close | A-2 |
| C-31 | `intermediaries` (lawyers) | `quantity_traded` (redrafting, trade-secret and non-solicitation work) | increase | short to medium | CR-9, CR-8b; CR-12d | legal services `input_to` employers' contracting and claims, close | chain 1: A-4; chain 2: A-19 |
| C-32 | `intermediaries` (lawyers) | `quantity_traded` (total legal work for employers on restraints) | ambiguous | short to medium | CR-12b over C-30 (−) and C-31 (+); CR-12, 0.8 (two items in one variable) | as above | A-2, A-4, A-19 |
| C-33 | `officials.courts` | `enforcement_cost` (non-compete enforcement suits) | decrease | short to medium | CR-1 (operation 1, pending cases included), CR-4a, CR-8c | | A-2 |
| C-34 | `officials.courts` | `enforcement_cost` (disputes over U1, U2 and K2; trade-secret and non-solicitation suits) | increase | short to medium | CR-4, CR-8c; CR-12d | | chain 1: A-4; chain 2: A-19 |
| C-35 | `employers.rivals` (hiring-intensive firms and founders) | `investment_target` (establishments in Teravel rather than Mossgrave) | increase | long | CR-4 (x: there, y: here; y made better), CR-7a | Teravel and Mossgrave labor markets: `across_border`, close | A-24 |
| C-36 | `neighboring_jurisdictions` (Mossgrave employers) | `investment_target` (training-intensive establishments in Mossgrave) | increase | long | RS-4, CR-4, CR-7a | `across_border`, close | A-22 |
| C-37 | `neighboring_jurisdictions` (Mossgrave) | `entry_rate` (hiring-intensive firms and start-ups) | decrease | long | CR-4 (x: there, y: here), CR-7a | `across_border`, close | A-24 |
| C-38 | `employers.restraining` | `resources_available_other_uses` | decrease | short to medium | CR-8b (voiding a contract right is a transfer, including deferred pay a voided clause would have withheld); CR-3 note; PC-18; CR-12d | contract (wages and deferred pay under existing contracts) | chain 1: A-2, A-7; chain 2: A-1, A-2, A-29 |
| C-39 | `workers.bound` | `resources_available_other_uses` | increase | short to medium | CR-8b (the other side of C-38) | contract (as above) | chain 1: A-2, A-7; chain 2: A-1, A-2, A-29 |

**C-16, firm values and incidence (CR-7b, CR-7c).** For firms that train more than they hire trained, the restraint protected part of their expected yield: trained staff and client relationships kept in the firm. The Act lowers that yield, for existing staff at once and for future staff by raising the cost of training or of retaining them. By CR-7c, owners at the time the change became expected bear the loss. The value fell in part from February 2025 as passage became likely, and the rest at passage in June. Later buyers of these firms pay the lower price.

Training already paid for before the announcement is a sunk investment. Its yield to the employer falls and cannot be recovered, so the loss on past training settles on the owners who paid for it (CR-7b, the immobile means). Future training is different. Its cost moves toward the trainees, through lower pay or less training (C-7), because the trained skill is now a means the worker can move.

**Voiding existing contracts is a transfer (CR-8, PC-18).** Under the 0.7 CR-8 clarification, a rule that voids a right one party held under an existing contract is a transfer under CR-8b: the holder loses the value of the right and the other party gains it, including deferred pay that a voided clause would have let the holder withhold. PC-18 applies the same clause. So:
- the employer's side is the fall in owners' equity (C-16) and, where money changes hands, `resources_available_other_uses` (C-38): higher pay kept up to hold staff, which the employer keeps paying (CR-3 note; A-7), and deferred pay that a forfeiture-for-competition clause would have withheld and that must now be paid on a move to a competitor, a sum the employer cannot avoid (A-1, A-29);
- the worker's side is the freedom to move (C-1), higher pay (C-8) and those same sums (C-39).

Gains to others do not come out of this transfer: founders gain entry (C-3) and customers a provider they can follow (C-18), each derived separately (CR-1, CR-9). The 0.6 version of this example treated voiding as the extinction of a right with no recipient; the catalog did not adopt that proposal (Gaps found, b).

**C-17, rivals' firm values.** Hiring rivals gain access to experienced staff without buy-outs or suits (+; C-15, C-28). Under the CR-7 clarification on a means made mobile, the gain from making trained workers mobile settles on the workers whose means can now move (C-8), not on the firms that hire them. Rivals pay for that access in competitive wages, and they also face higher retention costs for their own staff (−). Without a premise on which effect is larger, the sign is ambiguous.

**C-19, prices to customers.** Spin-offs add sellers (C-3), and by RS-13 added supply pushes price down. Higher pay for experienced staff (C-8) raises the cost of an input that is a material part of these services, and by RS-14 pushes price up. The result is ambiguous.

**C-21 and C-35 to C-37, location (RS-4).** Mossgrave is across the river, and its non-competes are enforceable. Two location choices move, and they reach different keys.
- Some employers whose model rests on training staff who could be bid away locate new training-intensive work in Mossgrave rather than Teravel (A-22): fewer such establishments in Teravel (C-21), more in Mossgrave (C-36). Nothing pushes training-intensive establishments toward Teravel: a mobile labor pool makes them worse off there, not better.
- Firms that rely on hiring experienced staff, and founders, find Teravel's pool of mobile staff more attractive (A-24; CR-4, CR-7a across locations): more of them locate in Teravel (C-35), fewer enter in Mossgrave (C-37).

The 0.6 version combined the second chain with the first on C-21, as if both reached net trainers' establishments. They do not, so CR-12b does not apply between them, and C-21 is a decrease. Where the two would meet, total employment in these fields in Teravel, no key is recorded (section 10, not reported).

**C-22 and C-30 to C-34, courts and lawyers.** About 400 enforcement suits a year end, pending ones included (C-33), and so does lawyers' enforcement work (C-30). Lawyers gain redrafting work (the receipt side of C-2's fees, CR-8b) and trade-secret and non-solicitation claims (C-14), and courts gain those claims and the disputes through which U1, U2 and the scope of K2 are decided (C-31, C-34). Each pair is two items of one variable moving in opposite directions, so each item is recorded with a qualifier and the total separately, as ambiguous (C-22, C-32), under the 0.8 CR-12 note on two items in one variable.

**Not reported: Mossgrave-bound workers taking Teravel jobs.** K1 covers anyone who primarily works in Teravel, whatever law the contract chooses. A Mossgrave worker bound by a Mossgrave clause could take a Teravel job to escape it. Mossgrave courts may still enforce the clause there, and A-25 (p = 0.4) is below the cut-off.

**GAP-034-1: know-how carried to a rival.** When a worker takes know-how to a rival, the rival uses it, and the first firm keeps it too. What the first firm loses is only its exclusive use, which is captured in C-16. Whether the field as a whole produces more because the same know-how is now used in two firms cannot be derived. The 0.7 CR-8 clarification on non-rival means says so: CR-8a applies to the time and materials used with knowledge, not to the knowledge itself, and a claim about total output needs a premise. No consequence is reported on total output in the field; the worker-level claims (C-1, C-3, C-8) do not depend on it.

**Stopping points.** Recruiters' own staff (from C-20) are at depth 3 and diffuse; stopped. Suppliers to spin-offs are at depth 3; stopped. Suppliers and landlords of establishments relocated across the river (from C-21, C-36) are at depth 3; stopped. RS-9 (bundled trips) and RS-10 (informal trade) do not apply: no trade moves outside the legal market. RS-11 is used in its status form (C-9, C-10).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `workers.bound`, `job_changes` (to rivals and start-ups), from 2026, short to medium | Option added and made known (CR-1, CR-4b, CR-11c; A-1, A-2). | Employers expand unvested deferred pay and retention bonuses (C-26; A-10), which a worker forfeits on any departure (RS-11); long notice periods under U1-a (C-5). | Empirical premise, CR-12e: the substitute devices deter fewer moves to rivals than the non-compete did (A-9, p = 0.65). A device that deters as much would cost the employer deferred pay paid to every stayer, which a non-compete did not. Places that stopped enforcing non-competes saw mobility to competitors rise. | **increase** (C-1). If A-9 failed, **ambiguous**. |
| `workers.bound`, `job_changes` (to rivals and start-ups), 3 February to 31 December 2025 | Pending-cases clause: a move late in 2025 is judged under the Act (RS-8, 0.8 clause; CR-10a; A-27, p = 0.55). | Workers who would have moved by buy-out or litigation wait for January (RS-8, CR-10a; A-14). | None. The (+) chain needs a premise with p ≥ 0.5, so it counts under the 0.8 CR-12 note. | **ambiguous** (C-11). |
| `workers.bound`, `job_changes` (to other fields), medium | None. | Moves that had to leave the field now stay in it (CR-4; A-8); expanded deferred pay deters any departure (RS-11; A-10). | None needed | **decrease** (C-9). The chains are independent, so it holds if either chain's premise holds (CR-12d). |
| `workers.bound`, `job_changes` (all), medium | Moves that would not have happened at all now do (CR-4b; A-1). | Expanded deferred pay deters every departure (RS-11; A-10). Moves switched from other fields to rivals do not change the total. | None. A-9 compares deterrence for moves to rivals only. | **ambiguous** (C-10). |
| `workers.trainees`, group, medium | Substitute restraints (C-4, C-6) restore some protection; they are a different variable. | Lower value of an unrestrained trainee (PC-18, CR-5c, CR-7a; A-5). | A-6 (substitutes do not fully restore the protection, p = 0.7) leaves at least one member moving down. | **at_least_one_decrease** (C-7). Restraints are not netted against pay (CR-12c). |
| `workers.bound`, `wage_rate`, short to medium | Outside offers and counter-offers (CR-6, CR-7a; A-7). | None found. The worker's value in the current job is unchanged, and pay is measured including deferred pay. | None needed | **increase** (C-8). |
| `employers.rivals`, `asset_value`, short to medium | Access to experienced staff without buy-outs or suits (C-15, C-28; A-28). | Competitive pay for that access, and higher retention costs for their own staff (CR-7: the gain settles on the mobile workers). | None | **ambiguous** (C-17). |
| `customers`, `price_paid`, medium to long | Higher pay for experienced staff is a cost (RS-14; A-7, A-23). | More sellers from spin-offs (RS-13; A-3, A-23). | None | **ambiguous** (C-19). |
| `officials.courts`, `enforcement_cost`, short to medium | Disputes over U1, U2 and K2; trade-secret and non-solicitation claims (C-34; A-4, A-19). | About 400 enforcement suits a year end (C-33; A-2). | None. The items are recorded separately (C-33, C-34) and the total here (CR-12, 0.8). | **ambiguous** (C-22). The transition probably raises disputes for a time, but no premise sets the size. |
| `intermediaries` (lawyers), `quantity_traded`, short to medium | Redrafting and new claims (C-31; A-4, A-19). | Non-compete enforcement work (C-30; A-2). | None. Items recorded separately (CR-12, 0.8). | **ambiguous** (C-32). |
| `founders.spinoff`, `entry_rate`, medium to long | Entry no longer barred (A-1, A-3). | Less employer-funded training or fewer trainee hires (C-7) would mean fewer trained would-be founders later. C-7 is a group, so this chain needs a premise that training or hiring, not only pay, falls enough to thin the pool of founders within the horizon (A-30, p = 0.4). | Under the 0.8 CR-12 note, an opposing chain whose premise is below 0.5 does not make the sign ambiguous; it is recorded in section 10. | **increase** (C-3). |
| `employers.restraining`, `resources_available_other_uses`, short to medium | None. | Higher pay to keep staff (A-7); deferred pay no longer forfeited (A-1, A-29). | None needed; CR-12d | **decrease** (C-38). |

The location chains (C-21, C-35 to C-37) each reach their own key and are not combined (section 6). No chains cancel exactly by construction (CR-12f).

## 8. Time structure

- **Announcement, February to June 2025.** As passage becomes more likely, the values of firms that rely on restraints fall part of the way (C-16; CR-7c), and the rest at passage. Employers' associations lobby (C-13).
- **Window, 3 February to 31 December 2025.** Bound workers who would have moved to rivals by buy-out or litigation wait for January, while others move late in 2025 because a suit would be decided under the Act (C-11, ambiguous; RS-8's 0.8 clause). Buy-outs fall in this window as in the next (C-27, C-28). Employers begin rewriting contracts and adding retention pay (C-4, C-5, C-6, C-26). The rewriting is a path note, since it does not happen in the counterfactual.
- **Short run, 2026.** The Act applies at once to existing contracts and pending suits, so the transfer from employers to bound workers (C-38, C-39) happens on 1 January, not as contracts expire. K4 notices go out by 1 March, and moves to rivals rise (C-1). Bound workers get counter-offers or move (C-8), rivals hire more easily (C-15), recruiters place more (C-20), and clients follow departing providers (C-18, C-29). Non-compete suits end (C-30, C-33), while disputes over the readings and the exemptions begin (C-31, C-34). The readings of U1 and U2 are decided in this period, and C-5 and C-6 take the sign of the reading adopted; the two provisions are independent.
- **Medium run, years 2 to 5.** New hiring cohorts are on new terms, so the trainee adjustments (C-7) apply to a growing share of the workforce. Spin-offs enter (C-3), and partnership buy-ins spread in practices (C-12). As existing contracts expire and are replaced, the effects on bound workers fade into the effects on all workers in these fields.
- **Long run.** Establishment location (C-21, C-35 to C-37) adjusts as firms invest. Effects that exist only during the transition (C-11, and C-27 and C-28 in 2025) have `persistence` n/a; the Act has no expiry.
- **Expectations.** If employers expect repeal or a narrow reading of U1 and U2 (C-13), they hold back irreversible changes such as relocation (C-21, C-36) and move first to cheap, reversible ones: retention pay and non-solicitation (TS-2).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-23 | `officials.enforcement` (Labor Bureau) | `enforcement_cost` (K1 and K5 cases) | increase | Staff time on the new task. | OC-3 |
| C-24 | `officials.enforcement` (Labor Bureau, other wage and consumer cases) | `enforcement_cost` (other rules) | decrease | Other enforcement displaced by the new task on a fixed budget. The cost falls on those that enforcement protected. | OC-3, CR-8a |
| C-25 | `workers.trainees`, `employers.net_trainers` | `quantity_traded` (exchanges of training or pay for a restraint) | decrease | Exchanges in which a worker would have promised not to compete in return for training, a job or pay. Both sides lose the gain each expected. | OC-4, CR-5a, PC-18 |
| C-38 | `employers.restraining` | `resources_available_other_uses` | decrease | Higher pay to keep staff, and deferred pay no longer forfeited, which they cannot avoid. | CR-8b, CR-3 note |

C-2's compliance work (lawyers' time, notices) is the main resource used up by employers (CR-8c), and it is not listed again. The fees are receipts to lawyers (C-31, CR-8b); the time is used up. C-23 and C-24 apply OC-3's fixed-budget case. The Bureau did not enforce non-competes before, so no enforcement is made unnecessary for it (OC-3, against the right baseline). No new appropriation was made, so taxpayers' means are not reduced (A-18); other enforcement is. Courts are in C-22, C-33 and C-34. Their funding does not change with their caseload, so the same fixed-budget logic applies, but the sign of their total workload is ambiguous. Buy-outs (C-27, C-28) and the voided rights (C-38, C-39) are recorded on both sides.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Non-competes deter some bound workers from moves to rivals or start-ups they would otherwise make. | binding | 0.8 | 17% bound; about 400 suits a year and many more letters; surveys of workers citing a non-compete as the reason for declining an offer. | C-1, C-3, C-8, C-15, C-18, C-20, C-29 fail; C-38 and C-39 lose chain 2. |
| A-2 | Employers stop enforcing, and workers learn that the clause is void (K4 notices, damages and fee-shifting). | enforcement | 0.8 | K4 and K5 text; experience with mandated notices. | C-1 weaker; void clauses keep deterring. C-29, C-30, C-33 fail; C-38 and C-39 weaken. |
| A-3 | Some bound workers have plans to start a firm in their field that the non-compete blocks. | binding | 0.7 | Founder surveys; spin-off rates in comparable places with and without enforcement. | C-3 fails; one chain of C-19 fails. |
| A-4 | For many employers, reshaping restraints into the preserved forms costs less than the protection it restores. | other | 0.85 | Current use of non-solicitation and deferred pay; legal fees for redrafting. | C-4, C-5 (U1-a), C-6 (U2-b) fail; C-31 and C-34 lose a chain. |
| A-5 | In a material share of trainee jobs, the non-compete protected the employer's recovery of the cost of general training. | other | 0.7 | Training spending by field; how often non-competes go with funded training; employer surveys. | C-7 fails; C-6 weakens under U2-b. |
| A-6 | Substitute restraints (non-solicitation, unvested pay, and under U2-b repayment agreements) do not fully restore that protection. | substitutability | 0.7 | Repayment capped at actual cost and hard to collect; non-solicitation does not stop a worker serving a rival's clients. | C-7 fails: the pressure could be fully absorbed by restraints. |
| A-7 | Some bound workers are paid less than a rival would pay them. | other | 0.75 | Pay of movers before and after moves; pay gaps between bound and unbound workers in the same job. | C-8 fails; one chain of C-19 fails; C-38 and C-39 lose chain 1. |
| A-8 | In the counterfactual, some bound workers change employer by leaving their field. | mobility | 0.6 | Field-switching rates of workers with non-competes against those without. | One chain of C-9 fails; C-9 rests on A-10 alone. |
| A-9 | Substitute retention devices deter fewer moves to rivals than non-competes did (dominance premise, CR-12e). | other | 0.65 | Mobility to competitors after non-competes stopped being enforced in comparable places; cost to employers of retention pay. | C-1 becomes ambiguous. |
| A-10 | Employers expand unvested deferred pay and retention bonuses. | other | 0.6 | Current plan design; benefits consultants' advice after the Act. | C-26 fails. The negative chains in C-1, C-9 and C-10 fail; C-10 becomes an increase. |
| A-11 | Courts accept bona fide partnership buy-ins as within K2, and practices use them. | other | 0.6 | Rulings under the 1998 partnership statute; how common partner tracks already are. | C-12 fails. |
| A-12 | Token equity grants, made only to bring a restraint within K2, qualify. | other | 0.3 | The same rulings required a substantial interest. | Below cut-off; not reported. |
| A-13 | Employers' associations, worker groups and start-up associations can organize at a cost below their stake. | other | 0.8 | Existing chambers of commerce, bar and medical associations, start-up councils; the 2025 hearings. | C-13 fails. |
| A-14 | Some bound workers would have moved to rivals in 2025, by buy-out or litigation, and can wait. | expectations | 0.6 | Monthly counts of suits and settlements; how long offers stay open. | The (−) chain of C-11 fails, and C-11 becomes an increase; C-27 and C-28 lose chain 1. |
| A-15 | Non-competes protected a material part of net trainers' expected yield. | other | 0.7 | Share prices and deal values of firms relying on restraints, around the votes; how central trained staff and client books are to their earnings. | C-16 fails. |
| A-16 | Some firms hire more trained staff than they train. | other | 0.8 | Hiring records by experience level. | C-17 is not defined for any firm. |
| A-17 | Non-solicitation bars only contact the worker initiates; clients may follow a provider on their own. | other | 0.7 | K3(b) says "solicit"; common-law meaning of solicitation. | C-18 and C-29 fail. |
| A-18 | The Labor Bureau's budget is not raised for the new task. | revenue_use | 0.7 | No appropriation in the Act; the next budget cycle. | C-24 becomes a cost to a group of payers instead (taxpayers, recipients of other spending, future taxpayers; OC-3). |
| A-19 | Employers turn to trade-secret and non-solicitation claims against departing staff. | substitutability | 0.7 | Claim filings in places that stopped enforcing non-competes. | C-14 fails; C-31 and C-34 lose a chain. |
| A-20 | Employers keep writing void clauses and rely on workers not knowing. | enforcement | 0.35 | K4 notices and K5 damages make it costly. | Below cut-off; not reported. |
| A-21 | Recruiters handle a material share of experienced hires in these fields. | other | 0.7 | Placement data. | C-20 fails. |
| A-22 | Some employers locate new training-intensive work in Mossgrave because restraints are enforceable there. | mobility | 0.55 | Distance across the river; existing two-state employers. | C-21 and C-36 fail. |
| A-23 | Spin-off entry adds supply that is not offset elsewhere (RS-13), and experienced staff pay is a material part of these services' costs (RS-14). | other | 0.6 | Cost structure of salons, clinics and advisory firms; spin-off counts. | One or both chains of C-19 fail. |
| A-24 | Firms that rely on hiring experienced staff, and founders, prefer to locate where staff are mobile. | mobility | 0.6 | Location choices of start-ups and hiring-intensive firms across enforcement boundaries. | C-35 and C-37 fail. |
| A-25 | Mossgrave-bound workers escape their restraints by taking Teravel jobs. | other | 0.4 | Mossgrave courts may still enforce against them. | Below cut-off; not reported. |
| A-26 | In the counterfactual, some Teravel employment contracts contain paid notice periods of six months or more, and some contain training repayment agreements. | other | 0.7 | U1 and U2 are raised because such terms exist; garden leave is common in finance, repayment agreements in funded training. | C-5 loses its U1-b sign and C-6 its U2-a sign. |
| A-27 | Some bound workers who would not have moved in 2025 in the counterfactual move late in 2025, because a suit against them would be pending on 1 January 2026 and decided under the Act. | expectations | 0.55 | K1 applies to pending cases; enforcement suits take months; offers stay open. Preliminary injunctions before 1 January limit it. | The (+) chain of C-11 fails, and C-11 becomes a decrease. |
| A-28 | In the counterfactual, firms that hire a bound worker from a rival bear litigation risk, demand letters or buy-out payments. | other | 0.85 | About 400 suits a year and many more letters; buy-outs are common in sales and medicine. | C-15 fails; C-27 and C-28 lose chain 2; C-17 loses its (+) chain. |
| A-29 | Some existing contracts contain forfeiture-for-competition clauses (deferred pay lost only on joining a competitor). | other | 0.75 | K1 names such clauses; deferred-pay plans in finance and sales. | C-38 and C-39 lose chain 2. |
| A-30 | Employer-funded training or trainee hiring (not only trainee pay) falls enough to thin the pool of would-be founders in the bound fields within the horizon of C-3. | other | 0.4 | Trainee pay has a floor (minimum wage, what trainees will accept), so some adjustment falls on training; but trainees from 2026 found firms only years later. | Below 0.5: the opposing chain on C-3 is recorded here, not reported. If it held, C-3 would become ambiguous in the long run. |

**Not reported.**
- Total employment in the bound fields in Teravel: spin-offs and hiring-intensive firms locating in Teravel (A-3, A-24) against training-intensive work moving to Mossgrave (A-22). The key would be ambiguous; it is left out as a judgment of depth, and its chains are each recorded (C-3, C-21, C-35).
- Opposing chain on C-3 through less training (A-30, p = 0.4).

### Final check before the report

The eight checks in `03_workflow.md` were run on the list.

1. **Uncombined chains.** Every key reached by two chains is in section 7:
   - moves to rivals from 2026 (C-1) against expanded deferred pay and long notice periods;
   - moves to rivals in the 2025 window (C-11), where the pending-cases clause opposes the wait (RS-8, 0.8);
   - total job changes (C-10);
   - rivals' firm values (C-17);
   - customer prices (C-19);
   - courts (C-22) and lawyers (C-32), with their items recorded separately;
   - entry (C-3), with the opposing chain below 0.5.

   The location chains reach different keys (C-21, C-35 to C-37) and are not combined. Bound workers' pay was checked for an opposing chain, and none was found once pay includes deferred pay.
2. **Single signs for a group.** The trainee response is a group (C-7), signed only with A-6, because its other margin, substitute restraints, moves in the opposite direction. No member is signed alone.
3. **Baseline.** Every sign is against Teravel with reasonable non-competes enforced, not against Mossgrave's law and not against the time before the bill. C-5 and C-6 under the void readings are signed against the long notice periods and repayment agreements that exist in that world (A-26).
4. **Worse off is not poorer.** `resources_available_other_uses` is signed only for restraining employers and bound workers (C-38, C-39), where employers keep paying higher pay to staff they keep, and pay deferred pay they cannot avoid. Trainees who lose training are worse off (CR-3a), but no `resources_available_other_uses` sign is given for them.
5. **Timing.** Moves to rivals happen with and without the Act, so each window is signed: 2025 (C-11, ambiguous) and 2026 on (C-1). Buy-outs fall in both windows (C-27, C-28). Contract rewriting before January would not happen at all without the Act, so it is a path note.
6. **Both sides of transfers.** Voiding a right is a transfer (CR-8, 0.7; PC-18): employers C-16 and C-38, workers C-39. Buy-outs: C-27 and C-28. Lawyers' fees are receipts as well as costs (C-2, C-31).
7. **Every actor class, every core rule.**
   - CR-7c was applied to net trainers and to rivals.
   - CR-6 was applied to trainee terms, retention pay and bound workers' pay.
   - CR-9 was applied to rivals, customers, recruiters, lawyers and the old employer's clients (C-29).
   - CR-4 across the border was applied to both sides of each location choice (C-21, C-35 to C-37).
   - OC-3 was applied to the Bureau and the courts.
   - CR-11c was applied to the notice.
   - RS-3 and RS-4 were checked.
8. **Unstated premises.**
   - "Some actors are at the margin" is A-1, A-3, A-8, A-22, A-24 and A-27.
   - The ability to organize is A-13.
   - "The substitute is incomplete" is A-6.
   - The dominance premise is A-9, stated as an empirical premise (CR-12e).
   - Premises added in the correction: A-26 (the terms U1 and U2 concern exist), A-27 (early moves under the pending-cases clause), A-28 (hiring firms bore litigation risk and buy-outs), A-29 (forfeiture-for-competition clauses exist), A-30 (the opposing chain on entry).

## 11. Report

**The policy.** From 1 January 2026, Teravel will not enforce any term that stops a worker from working for a competitor, or starting a competing business, after leaving a job. This covers contracts already signed and suits already pending. It does not cover a person who sells a business or an ownership stake. Agreements to keep secrets, not to solicit clients or staff for up to a year, notice periods, and forfeiture of unvested pay remain valid. Employers must tell affected current and recent workers by 1 March 2026, and workers can sue for damages if an employer tries to enforce a void clause. Two points are unclear: whether long paid notice periods ("garden leave") count as restraints (U1), and whether training repayment agreements count as penalties (U2).

**Visible consequences.** More bound workers leave for rivals or start their own firms from 2026 (C-1). This holds given that substitute retention devices deter fewer such moves than non-competes did (A-9). Employers spend on rewriting contracts and sending notices (C-2).

**Invisible consequences.**
- *Workers already bound.*
  - They are paid more, through outside offers and counter-offers (C-8), and receive more unvested deferred pay and retention bonuses (C-26).
  - They gain what their employers lose on the voided clauses: higher pay, and deferred pay no longer forfeited on joining a competitor (C-39).
  - Fewer of them leave their field just to change employer (C-9).
- *New trainees.* In jobs where employers paid for training that rivals value, at least one of these falls: trainee pay, employer-funded training, or the number of trainees hired (C-7). Exchanges of training for a promise not to compete no longer happen (C-25).
- *Employers that held non-competes.*
  - The value of their firms fell when the Act became likely, a loss borne by their owners then and not by later buyers (C-16). They have less to spend on other things (C-38).
  - They move restraints into the forms the Act leaves alone (C-4). Long paid notice periods become more common if U1 is read broadly and less common if it is read narrowly (C-5); training repayment agreements become more common if U2 is read narrowly and less common if broadly (C-6).
  - They bring more trade-secret and non-solicitation claims (C-14), lose clients who follow departing staff (C-29), and stop receiving buy-out payments (C-27).
  - Some locate new training-intensive work in Mossgrave rather than Teravel (C-21, C-36).
- *Professional practices* move senior staff into partnership buy-ins, so that a restraint on leaving falls within the sale-of-business exemption (C-12).
- *Others.*
  - Rival employers find experienced staff more easily and pay no buy-outs (C-15, C-28), and recruiters place more of them (C-20). Firms that rely on hiring experienced staff, and founders, locate more in Teravel (C-35) and less in Mossgrave (C-37).
  - Former employees start more firms in their field (C-3).
  - Clients can follow a provider who moves (C-18).
  - Lawyers lose non-compete enforcement work (C-30) and gain redrafting and other claims (C-31). Courts hear fewer non-compete suits (C-33) and more disputes over the unclear provisions and trade secrets (C-34).
  - The Attorney General's Labor Bureau spends on the new task, and other enforcement falls (C-23, C-24).
  - Interest groups lobby over repeal and the unclear provisions (C-13).

**Ambiguous effects.**
- Moves to rivals during 2025 (C-11): some wait for the Act, others move early because a suit would be decided under it.
- Total job changes (C-10): moves that now happen, against wider use of unvested pay, which deters every departure.
- The value of firms that hire experienced staff (C-17): the gain from free movement goes mainly to the workers.
- Prices to customers (C-19): more competitors, against higher pay for experienced staff.
- Courts' total workload (C-22) and lawyers' total work on restraints (C-32).

**Key conditions.**
- Moves to rivals rise only if substitute devices deter less than non-competes did (A-9, p = 0.65).
- The trainee effect rests on non-competes having protected training costs (A-5, p = 0.7), and on substitutes not fully replacing them (A-6, p = 0.7).
- Firm values fall where restraints protected a material part of a firm's earnings (A-15, p = 0.7).
- How U1 and U2 are read decides the direction of C-5 and C-6, not of the main effects.
- The location effects rest on A-22 (p = 0.55) and A-24 (p = 0.6).

**What this analysis cannot say.**
- How many more people change jobs, or by how much pay rises.
- Whether the gains to workers who move outweigh the losses to firms and trainees, or whether the Act is desirable.
- Whether the field as a whole produces more because know-how spreads. That needs a premise about non-rival means (CR-8, 0.7), and the question is open with the experts (GAP-034-1).
- Which reading of U1 and U2 the courts will adopt.
- Courts' and lawyers' total workload, beyond its direction being ambiguous.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | workers.bound | job_changes (to rivals and start-ups, from 1 January 2026) | increase | short–medium | visible | B | CR-1, CR-4b, CR-11c, PC-18; RS-11 opposing; CR-12b, CR-12e | A-1, A-2, A-9 |
| C-2 | employers.restraining | compliance_cost | increase | short | visible | A | OC-2, CR-8c | none |
| C-3 | founders.spinoff | entry_rate (same-field firms) | increase | medium–long | invisible | B | CR-1, CR-4b; opposing chain below 0.5 (CR-12, 0.8; A-30) | A-1, A-3 |
| C-4 | employers.net_trainers | term_prevalence (non-solicitation, confidentiality, unvested pay terms) | increase | short–medium | invisible | B | RS-5, PC-18 | A-4 |
| C-5 | employers.net_trainers | term_prevalence (paid notice periods of six months or more) | U1-a: increase; U1-b: decrease | short–medium | invisible | B | U1-a: RS-5, PC-18; U1-b: CR-1 operation 1, PC-18 | A-4, A-26 |
| C-6 | employers.net_trainers | term_prevalence (training repayment agreements) | U2-a: decrease; U2-b: increase | short–medium | invisible | B | U2-a: CR-1 operation 1, PC-18; U2-b: RS-5, PC-18 | A-4, A-5, A-26 |
| C-7 | workers.trainees | wage_rate (training), non_wage_compensation (funded training), employment (trainee hires) (group) | at_least_one_decrease | medium | invisible | B | PC-18, RS-2, CR-5c, CR-7a, CR-6 | A-5, A-6 |
| C-8 | workers.bound | wage_rate (including vested deferred pay) | increase | short–medium | invisible | B | CR-1, CR-9, CR-6, CR-7a, CR-7 (means made mobile) | A-1, A-7 |
| C-9 | workers.bound | job_changes (to other fields) | decrease | medium | invisible | B | CR-4a, CR-4b; RS-11; CR-12d | A-8, A-10 |
| C-10 | workers.bound | job_changes (all) | ambiguous | medium | invisible | B | CR-4b (+); RS-11 (−); CR-12b | A-1, A-10 |
| C-11 | workers.bound | job_changes (to rivals, 3 February–31 December 2025) | ambiguous | short | invisible | B | RS-8 (−; 0.8 pending-cases clause +), CR-10a, CR-4; CR-12b | A-14, A-27 |
| C-12 | practices.professional | reclassification (partnership buy-ins under K2) | increase | medium | invisible | B | RS-5 | A-11 |
| C-13 | employers.net_trainers; worker and start-up associations | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-13 |
| C-14 | employers.net_trainers | quantity_substitute (trade-secret and non-solicitation claims) | increase | short–medium | invisible | B | RS-1 | A-19 |
| C-15 | employers.rivals | search_cost (experienced hires) | decrease | short–medium | invisible | B | CR-9, CR-1 | A-1, A-28 |
| C-16 | employers.net_trainers | asset_value | decrease | short | invisible | B | CR-7c, CR-10c, CR-7b, CR-8 (voiding), PC-18 | A-15 |
| C-17 | employers.rivals | asset_value | ambiguous | short–medium | invisible | B | CR-7c, CR-7b; CR-12b | A-16, A-28 |
| C-18 | customers | search_cost (replacing a provider) | decrease | medium | invisible | B | CR-9, CR-1 | A-1, A-17 |
| C-19 | customers | price_paid | ambiguous | medium–long | invisible | B | RS-13 (−), RS-14 (+); CR-12b | A-3, A-7, A-23 |
| C-20 | intermediaries (recruiters) | quantity_traded (placements) | increase | medium | invisible | B | CR-9 | A-1, A-21 |
| C-21 | employers.net_trainers | investment_target (training-intensive establishments in Teravel) | decrease | long | invisible | B | RS-4, CR-4, CR-7a | A-22 |
| C-22 | officials.courts | enforcement_cost (total) | ambiguous | short–medium | invisible | B | OC-3; CR-12b over C-33, C-34 | A-2, A-4, A-19 |
| C-23 | officials.enforcement | enforcement_cost (K1, K5 cases) | increase | short | invisible | A | OC-3 | none |
| C-24 | officials.enforcement | enforcement_cost (other rules) | decrease | short–medium | invisible | B | OC-3, CR-8a | A-18 |
| C-25 | workers.trainees, employers.net_trainers | quantity_traded (training-for-restraint exchanges) | decrease | medium | invisible | B | OC-4, CR-5a, PC-18 | A-5 |
| C-26 | workers.bound | non_wage_compensation (unvested deferred pay, retention bonuses) | increase | short–medium | invisible | B | PC-18, CR-4, CR-5c, CR-6 | A-10 |
| C-27 | employers.restraining | quantity_traded (buy-outs sold) | decrease | short–medium | invisible | B | CR-10a, CR-1, CR-8b; CR-12d | A-14, A-28 |
| C-28 | employers.rivals | quantity_traded (buy-outs bought) | decrease | short–medium | invisible | B | CR-8b, CR-1; CR-12d | A-14, A-28 |
| C-29 | employers.restraining | quantity_traded (client accounts served) | decrease | short–medium | invisible | B | CR-9, CR-4 | A-1, A-2, A-17 |
| C-30 | intermediaries (lawyers) | quantity_traded (non-compete enforcement work) | decrease | short–medium | invisible | B | CR-9, CR-1 | A-2 |
| C-31 | intermediaries (lawyers) | quantity_traded (redrafting, trade-secret and non-solicitation work) | increase | short–medium | invisible | B | CR-9, CR-8b; CR-12d | A-4, A-19 |
| C-32 | intermediaries (lawyers) | quantity_traded (total work on restraints) | ambiguous | short–medium | invisible | B | CR-12b over C-30, C-31 | A-2, A-4, A-19 |
| C-33 | officials.courts | enforcement_cost (non-compete suits) | decrease | short–medium | invisible | B | CR-1, CR-4a, CR-8c | A-2 |
| C-34 | officials.courts | enforcement_cost (reading disputes, trade-secret and non-solicitation suits) | increase | short–medium | invisible | B | CR-4, CR-8c; CR-12d | A-4, A-19 |
| C-35 | employers.rivals (hiring-intensive firms, founders) | investment_target (establishments in Teravel) | increase | long | invisible | B | CR-4, CR-7a | A-24 |
| C-36 | neighboring_jurisdictions (Mossgrave employers) | investment_target (training-intensive establishments in Mossgrave) | increase | long | invisible | B | RS-4, CR-4, CR-7a | A-22 |
| C-37 | neighboring_jurisdictions (Mossgrave) | entry_rate (hiring-intensive firms and start-ups) | decrease | long | invisible | B | CR-4, CR-7a | A-24 |
| C-38 | employers.restraining | resources_available_other_uses | decrease | short–medium | invisible | B | CR-8b (voiding), CR-3 note, PC-18; CR-12d | A-1, A-2, A-7, A-29 |
| C-39 | workers.bound | resources_available_other_uses | increase | short–medium | invisible | B | CR-8b (voiding), PC-18; CR-12d | A-1, A-2, A-7, A-29 |

## Corrections after the core-only comparison

- **Header** changed to catalog 0.8; K1 is now a `term_prohibition` and PC-18 is cited where it applies (C-1, C-4 to C-7, C-16, C-25, C-26, C-38, C-39).
- **C-4 to C-6**: variable changed from `reclassification` to `term_prevalence` (0.7). C-5 and C-6 now carry per-reading signs: the void reading is a decrease, not "no chain", since such terms exist in the counterfactual (new A-26).
- **C-11**: sign changed from decrease to ambiguous, and the window widened to 3 February–31 December 2025. K1's pending-cases clause makes the earlier window better too (RS-8, 0.8 clause; new A-27, p = 0.55, so a chain under the 0.8 CR-12 note).
- **C-21**: sign changed from ambiguous to decrease. The (+) chain (A-24) concerns hiring-intensive firms, not net trainers' establishments, and now has its own consequences: C-35 (Teravel) and C-37 (Mossgrave). C-36 is the Mossgrave side of A-22.
- **C-15, C-17**: the hidden premise that hiring firms bore litigation risk and buy-outs is now A-28.
- **C-22**: kept as the courts' total, with its items added as C-33 and C-34 (0.8 CR-12 note on two items in one variable). The same treatment gives lawyers' work, C-30 to C-32.
- **C-3**: the opposing chain through less training is now a premised chain (A-30, p = 0.4) under the 0.8 CR-12 note. The sign is unchanged.
- **Added**: C-26 retention pay (A-10 was already used as a chain but never recorded); C-27 and C-28 buy-outs on both sides; C-29 clients lost by employers; C-38 and C-39 the transfer from voiding existing contracts, including deferred pay under forfeiture-for-competition clauses (CR-8, 0.7; new A-29).
- **Section 6** no longer says voiding is not a transfer; the 0.7 CR-8 clarification says it is. Final check items 4 and 6 were revised to match.
- **Rejected**: the core's single-member sign for employer-funded training (core C-11). Lower trainee pay is an open CR-6 margin that no premise excludes, so the group in C-7 stays as it is.
- **Rejected**: the core's cross-river commuter keys (core C-19, C-39). CR-3 gives no single direction for a worker who gains a freedom and loses the option of selling it, and the escape route is A-25, which is below the cut-off.
- **Not adopted (J)**: an aggregate for employment in the bound fields (core C-30) and pay keys for new hires, unbound workers and other fields (core C-24 to C-26). 0.8 does not settle them, and leaving them out is a choice of depth. The first is noted under "Not reported".

## Gaps found

**(a) Calculus gaps (a step no core rule covers).**
- GAP-034-1 (open): Referred to the experts as Q21 (`06_gaps.md`). Catalog 0.7 gives provisional handling (CR-8, non-rival means: a claim about total output needs a premise). **non-rival means.** Know-how carried by a worker to a rival is used there without being lost to the first firm, which loses only its exclusive use. CR-8 ("a policy does not create means; it redirects or uses them up") treats every means as rival. No core rule says how to reason about a means whose use by one actor does not reduce what is available to another. As a result, the claim that a field produces more when know-how spreads cannot be derived, nor its negation. Worker-level and firm-value claims are unaffected: CR-1, CR-4, CR-7c and CR-9 derive them. A candidate clause for CR-8: "where a means can be used by several actors at once (knowledge, a design), a policy that widens its use transfers its exclusive yield (CR-7c) but does not withdraw it from its first user." For the experts: is that praxeologically sound, and does it belong in CR-8 or in a new rule?

**(b) Unclear core rules (wording that was hard to apply here).**
- **CR-8 and the extinction of a right** (closed in 0.7: the CR-8 clarification on voiding a contract right makes it a transfer from holder to counterparty, including withheld deferred pay; the proposed CR-8f, that it is not a transfer, was not adopted, and this example now records C-38 and C-39). CR-8b covers payments, which add to the recipient exactly what they take from the payer. CR-8e covers confiscated goods. Neither said whether voiding an existing contractual right is a transfer.
- **CR-1's note on void-contract rules** (closed in 0.8: the CR-1 recording note now says such a rule removes, for both parties, the option of agreeing to the term, and may add an option for one of them). The note said such a rule "removes an option for one side and adds one for the other". A ban on a contract term also removes an option from the side it protects: the worker can no longer sell the promise in exchange for training. That matters for CR-3: the trainee's own ranking gives no single answer (section 5).
- **CR-6 with margins that move in opposite directions** (closed in 0.7: CR-6 clarification and the `at_least_one_as_stated` sign). Here the employer's pressure goes to trainee pay and training (down) and to substitute restraints (up). The same problem arose with RS-14's "price up and/or quantity down" (WE-035).
- **CR-7b when a means becomes mobile** (closed in 0.7: CR-7 clarification, a policy that makes a means mobile). The gain from making trained workers mobile settles on the newly mobile means (C-8), not on the firms that can now hire it (C-17).

**(c) Missing patterns (derived moves likely to recur).**
- **Proposed pattern, a banned restraint on an investment embodied in a mobile means** (largely covered in 0.7 by PC-18, whose mixed group includes training it funds). Kept as a note for a wider form covering tenant improvements under a lease and client lists built by an agent.
  - **If:** a policy voids a term that let one party recover an investment embodied in a means the other party controls and can move: general training in a worker; tenant improvements under a lease; client lists built by an agent.
  - **Then:** for new contracts, the investing party's maximum terms fall (CR-5c). The investment's cost moves to the party who controls the means: lower pay during training, less investment, or fewer such contracts, recorded as a group with `at_least_one_decrease`, given a premise that substitute terms do not fully restore recovery. Exchanges of the investment for the restraint decrease (CR-5a).
  - **Derivation:** CR-5c, CR-7a (the means' yield tends to what others will pay once it can move), CR-6 (pressure to open margins), CR-4.
- **Proposed pattern, retroactive voiding of contract terms** (covered in part in 0.7 by PC-18 and the CR-8 voiding clause; the timing in a pending-cases clause is covered by RS-8's 0.8 clause).
  - **If:** a policy voids a term in existing contracts.
  - **Then:** the holder of the right bears a fall in `asset_value`, from the time the change becomes expected and in proportion to its probability (CR-7c, CR-10c). The counterparty's options widen (CR-1). Where the contract can be ended or renegotiated at will, the remaining terms adjust as for new contracts (CR-5c). Where it cannot, they do not until renewal. Past consideration given for the term is sunk and is not returned (CR-10b).
  - **Derivation:** CR-1, CR-3, CR-7c, CR-8, CR-10b, CR-10c. It recurs in rent rules applied to existing leases, rate caps on existing loans, and changes to existing franchise terms.
- **Proposed pattern, removing a mobility restraint** (largely covered in 0.7 by PC-18 and the CR-7 clarification on a means made mobile).
  - **If:** a policy removes a restraint on a factor's moving to competitors.
  - **Then:** moves to competitors increase and moves out of the field decrease (CR-4); same-field entry by the factor's owners increases (CR-4); the factor's pay moves toward what competitors would pay (CR-6, CR-7a); the gain settles on the factor, not on the hiring firms (CR-7b). Holders of the restraint substitute other retention devices (RS-5), whose lock-in (RS-11) opposes the rise in total moves.
  - **Derivation:** as listed. It is the mirror of RS-11.
- **Note on the catalog** (closed in 0.7: PC-18 now fits the trainee case directly). RS-2 fitted the trainee case, but its Then clause speaks of quality, maintenance and contract length, not of moving the cost of an investment between the parties.

**(d) Vocabulary.**
- **No instrument type for prohibiting a contract term** (closed in 0.7: `term_prohibition`).
- **No variable for the prevalence of a contract term** (closed in 0.7: `term_prevalence`, now used in C-4 to C-6).
- **No sign for "no chain under this reading"** (closed in 0.7: `no_change`). Here the void readings turned out to have a sign of their own (decrease, C-5 and C-6), since the terms exist in the counterfactual.
- **Group signs whose members move in opposite directions** (closed in 0.7: `at_least_one_as_stated`).
