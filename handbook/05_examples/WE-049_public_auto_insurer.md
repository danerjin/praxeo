# WE-049 Public auto insurer at a uniform statutory premium, with a surcharge for its losses

Analyst: draft (Handbook 0.9, held-out test)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized, fictional policy in a fictional state. It resembles proposals for a "public option" in auto insurance but is not modeled on any of them. It was written as a held-out test of catalog 0.9. It probes a public seller with an open quantity (PC-19 and CR-6, 0.9), selling at a price that is uniform within a region while its private rivals price by risk, so that buyers sort themselves by risk (the candidate "selection under a uniform term" in `06_gaps.md`, 6.2e); losses paid by a surcharge that falls due only if reserves run out (CR-8, contingent payers); the private insurers' prices (RS-16) and values (CR-7c); and CR-12's 0.9 statement of what the response argument gives. Accidents, injuries and road safety are outside the scope of version 1; only money flows through claims are analyzed. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**The Lissmark State Auto Insurance Office Act.** The State of Lissmark requires every registered private vehicle to carry basic liability cover (30,000/60,000 bodily injury, 15,000 property damage); registration requires proof, and driving uninsured is fined $500. About 4.0 million policies are in force: Metro region 2.0 million, Valley 1.2 million, Upland 0.8 million. About 500,000 more vehicles (11%) are driven uninsured, about 30% among drivers whose quotes exceed $1,500 and about 7% among others. Thirty-eight private insurers sell cover; they price each driver by risk (age, record, vehicle, address). Average basic premium in 2026: Metro $820 (range about $380 to $3,600), Valley $560, Upland $450. About 120,000 drivers (3%) have a serious offense (drunk driving, reckless driving, driving while suspended) in the past three years; their average basic premium is about $2,600. Private premiums carry a loading of about 20% over expected claims. Most policies are sold through agents on commission. Neighboring Norvey has no public insurer.

**Dates.** Bill introduced 10 January 2027; enacted 30 June 2027; the Office issues policies from 1 January 2028. No expiry. Statutory premiums are indexed to the consumer price index.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | State of Lissmark; Norvey (no public insurer) | Act s. 1 |
| Announced / enacted / effective / expires | 10 January 2027 / 30 June 2027 / 1 January 2028 / none | Act s. 2 |
| Enforcement (who, penalties, resources) | The State Auto Insurance Office (SAIO) issues policies online and at motor vehicle offices, with no agents. The Insurance Commissioner sets the surcharge. Existing compulsory-insurance rules and fines continue. | Act s. 4, 9 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Public insurer | `public_supply` (open quantity) | Basic liability cover | SAIO | Sells to any eligible driver who applies and pays, with no limit on the number of policies. Premium set by statute, uniform within each region, not rated by driver: Metro $820, Valley $560, Upland $450 (the 2026 regional average private premiums), indexed to CPI. Basic cover only. | See U1 |
| K2 Surcharge | `per_unit_tax` (contingent) | Every motor liability policy in the State, public and private | Insurers collect, as a separate line on the bill; policyholders pay | If SAIO's reserves fall below zero, the Commissioner sets a surcharge per policy for the next year at the amount needed to restore reserves to $200 million; insurers remit it to SAIO. | — |
| K3 Initial reserves | `lump_sum_subsidy` | SAIO | General budget | $200 million appropriated once, not repaid. | — |

**Existing rules.** Compulsory basic liability cover; proof at registration; $500 fine for driving uninsured. They stay in place in the counterfactual.

Unclear provision:
- **U1, drivers with recent serious offenses.** Section 6(1): "The Office shall issue a basic policy to any person who holds a valid Lissmark driver's license, registers a vehicle in the State and pays the premium." Section 6(4): "The Office may refuse or cancel a policy where the applicant has made a material misrepresentation, or presents an exceptional hazard as defined by rule." No rule has been made, and the committee record supports both views. Reading **U1-a**: "exceptional hazard" includes a conviction for a serious offense in the past three years, and the Office refuses such drivers. Reading **U1-b**: it refers to the vehicle or its use (unroadworthy, commercial), and the Office must accept every licensed driver.

Readings get no probability; where a sign depends on one, each reading's sign is reported.

**Figures.** The State's actuary estimates that if drivers whose quotes exceed the statutory premium by more than about 10% switch (about 700,000 policies, average private quote about $1,350, expected claims about $1,100), the Office's premiums average about $740 against claims of $1,100 and expenses of about $74, a deficit of about $430 a policy and $300 million a year. Reserves of $200 million would run out in 2028; the surcharge would then be about $75 a policy ($300 million over 4.0 million policies). Under U1-b, if 80,000 serious offenders also switch (expected claims about $2,150), the deficit rises by about $120 million and the surcharge to about $105.

The counterfactual is Lissmark without the Act: private insurers only, risk-rated, no surcharge.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Binary: the state sells a service at a price it sets, with no fixed quantity. For drivers it adds an option (CR-1, operation 2): under U1-b for every driver, under U1-a for every driver without a serious offense. | Yes for drivers whose quotes exceed the statutory premium (figures; A-1) | PC-19 (0.9: open quantity), CR-6 (0.9: a public seller with an open quantity), CR-4, CR-9, RS-16, CR-7c; candidate "selection under a uniform term" (6.2e) |
| K2 | Binary: a charge per policy, due only if reserves run out. Operation 3 on the option of insuring (and so of driving legally). | Yes if SAIO's losses exceed its reserves (A-2) | CR-8 (0.8: contingent payers), TX-1, TX-2, OC-1, CR-12 (0.8: two items in one variable) |
| K3 | Binary: a one-time transfer from the general budget | Yes | OC-1 (Who pays), CR-8 (0.7) |

**Why selection follows (candidate, 6.2e).** The Office's price is the same for every driver in a region, while its cost of covering a driver differs by driver. Each driver compares it with a private quote that tracks that driver's cost (CR-4 per counterparty; CR-5c). Those whose quotes exceed the statutory premium switch; those below it stay private. The Office therefore covers the drivers who cost it most per dollar of premium, and its claims per policy exceed its premium (A-2). Under U1-a, the Office also screens counterparties, refusing those it may (the provider's side of the candidate, as in WE-029).

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `drivers.high_risk` | Drivers without a serious offense whose private quote exceeds the statutory premium | May buy from SAIO at the regional premium. |
| `drivers.serious_offense` | About 120,000 drivers with a serious offense in three years | U1-a: refused by SAIO; U1-b: may buy from SAIO. |
| `drivers.low_risk` | Drivers whose quote is below the statutory premium plus the surcharge | Stay private; pay the surcharge. |
| `drivers.uninsured` | Drivers of about 500,000 uninsured vehicles | A cheaper legal option for many. |
| `policyholders.all` | Every insured driver, public and private | Pay the surcharge once it applies. |
| `sellers.current` | 38 private insurers | Lose high-risk policies; collect the surcharge. |
| `intermediaries` | Agents and brokers | Lose commissions on switchers. |
| `officials.public_insurer` | SAIO | Sells, pays claims, receives the surcharge; screens under U1-a. |
| `claimants.third_party` | People injured or whose property is damaged by insured drivers | Claim against SAIO policies; fewer face uninsured drivers. |
| `sellers.complements` | Vehicle sellers, especially used cars | Insurance is a cost of owning a vehicle. |
| `taxpayers` | Payers from the general budget | Fund the initial reserves. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `drivers.high_risk` | `price_paid` (premium for basic cover) | decrease | short (from January 2028) | CR-1 (operation 2), CR-4, PC-19 (0.9) | A-1 |
| C-2 | `officials.public_insurer` | `quantity_supplied` (policies issued) | increase | short to long | CR-6 (0.9), CR-12 (0.9: activities that exist only under the policy) | A-1 |
| C-3 | `drivers.serious_offense` | `price_paid` (premium for basic cover) | U1-a: no_change; U1-b: decrease | short | CR-1, CR-4 | A-1 |

C-1 and C-3 are what supporters point to. Under U1-a, serious offenders gain no option and face the private market as before (C-3, `no_change` before the surcharge; the private premium per risk class has no reported sign, section 6).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `sellers.current` | `quantity_supplied` (private basic policies) | decrease | short to medium | PC-19 (0.9), CR-6 (0.9: a public seller with an open quantity; splitting a shift), CR-9, RS-16 | A-1, A-3 |
| C-5 | `drivers.uninsured`, `drivers.high_risk` | `legal_breach` (uninsured driving) | decrease | short (2028, before the surcharge) | CR-4 (x: drive uninsured, y: insure), CR-1 | A-1, A-6 |
| C-6 | all drivers | `legal_breach` (uninsured driving) | decrease | medium | CR-4, CR-12b, CR-12e (dominance, A-7) | A-2, A-6, A-7, A-8 |
| C-7 | `drivers.serious_offense` | `legal_breach` (uninsured driving) | U1-a: increase; U1-b: decrease | medium | CR-4, CR-12e (arithmetic on the figures, U1-b) | A-2, A-8 |
| C-8 | `drivers.high_risk` (Metro) | `legal_breach` (vehicles registered at addresses in a cheaper region, or in Lissmark by Norvey residents) | increase | short to medium | RS-5, RS-3, CR-4 | A-10 |
| C-9 | `officials.public_insurer` | `allocation_by_non_price_criteria` (refusals by offense record) | U1-a: increase; U1-b: no_change | short to long | CR-4 per counterparty, CR-5c (candidate: selection under a uniform term) | A-20 |
| C-10 | `officials.public_insurer` | `enforcement_cost` (record checks, refusals and appeals) | U1-a: increase; U1-b: no_change | short to long | OC-3, CR-8c | A-20 |
| C-11 | `sellers.current`, `drivers.low_risk`, `drivers.high_risk`, `drivers.serious_offense` | `lobbying_effort` (insurers for a broad "exceptional hazard" rule and limits on SAIO; low-risk drivers against the surcharge; high-risk and young drivers' groups to keep the premium low) | increase | short to medium | RS-7 | A-11 |
| C-12 | `drivers.high_risk` | `term_prevalence` (short-term private policies bought in July to December 2027 so as to switch in January 2028) | increase | short | RS-8, CR-10a | A-12 |
| C-13 | `claimants.third_party` (claims against SAIO-insured drivers who would otherwise have been privately insured) | `wait_time` (claim settlement) | increase | short (2028) | CR-6 (0.9: capacity added after a lag), PC-19 | A-13 |
| C-14 | `drivers.high_risk` | `quantity_complement` (vehicles owned and bought, mostly used cars by young drivers) | increase | medium | RS-12, CR-9 | A-1, A-9 |
| C-15 | `drivers.low_risk` | `quantity_complement` (vehicles owned, such as second cars) | decrease | medium | RS-12, CR-4, CR-8 (0.8: contingent) | A-2, A-6 |

**Open quantity (C-2, C-4; PC-19 and CR-6, 0.9).** The Office supplies whatever is demanded at its price, so there is no excess demand and no queue to buy (PC-19's rationing clause does not apply). Buyers whose quotes exceed its price move to it (CR-4), and private insurers face lower demand (CR-9). CR-6's 0.9 clause says the split between private price and quantity needs a premise. A-3 (p = 0.65) gives it: an insurer's cost of covering a driver is mostly the expected claim, and its capital moves between lines and states, so the shift shows in quantity (C-4). The opposite premise, that private supply cannot contract and premiums per risk class fall (RS-16's mirror case), is A-4, p = 0.35: not reported. PC-19's 0.9 note that rivals' immobile plant keeps operating while it covers running costs applies to private claims offices and agency networks (section 8).

**Uninsured driving (C-5 to C-7).** For an uninsured driver with a $2,000 quote, legal cover now costs the regional premium (CR-4: insuring improved, so some switch; A-6). In 2028, before any surcharge, nothing pushes the other way (C-5). From 2029 the surcharge raises the price of cover for everyone, and some drivers at the margin of insuring stop (A-6 applied to them). For drivers as a whole that is a kind 2 chain with p ≥ 0.5, so a dominance premise is needed: A-7 (p = 0.7) says the fall among high-risk drivers, whose price falls by hundreds of dollars and whose uninsured rate is 30%, exceeds the rise among others, whose price rises by about $75 to $105 and whose rate is 7%. That is an empirical premise, not arithmetic: the figures give the price changes and rates but not how many at each price respond (CR-12e, 0.8). Under U1-a, serious offenders gain nothing and face the surcharge, so their uninsured driving rises (C-7, A-8). Under U1-b their price falls from about $2,600 to the regional premium plus a surcharge of about $105, so the cut exceeds the surcharge by arithmetic on the case's figures (CR-12e), and their uninsured driving falls.

**Address (C-8).** A Metro driver who registers at an Upland address pays $450 instead of $820. Private insurers already rated by address, so the gain from misreporting rises only for drivers who buy from the Office (A-10).

**Screening (C-9, C-10).** Under U1-a the Office checks conviction records and refuses those it may: selection by non-price criteria where the uniform price would otherwise draw the costliest counterparties. Under U1-b there is no such step.

**Timing (C-12).** High-risk drivers whose policies renew in the second half of 2027 buy short-term policies, which they would not otherwise have, so as to switch in January 2028 (RS-8; A-12). There is no matching dip later, because the short terms exist only to reach the date.

**Claims handling (C-13).** CR-6's 0.9 clause: where capacity can be added from fees, but after a lag, the public-supply clause applies until it arrives. The Office's claims staff are hired as policies come in; in 2028 claimants against its policyholders wait longer than they would have with the private insurers that would otherwise have covered those drivers (A-13).

**Vehicles (C-14, C-15).** Insurance is a complement of owning a vehicle (RS-12). Cheaper cover raises vehicle ownership among high-risk drivers, many of them young (A-9); the surcharge lowers it at the margin among others (A-6). The total is not signed (section 7).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-16 | `officials.public_insurer` | `subsidy_outlay` (claims and expenses paid beyond premiums) | increase | short to long | CR-4 per counterparty, CR-5c (candidate: selection under a uniform term), CR-8b, CR-12 (0.9) | insurance policy: `contract` | A-1, A-2, A-18 |
| C-17 | `policyholders.all` | `price_paid` (surcharge) | increase | medium (from 2029) | CR-8 (0.8: contingent payers), CR-1 (operation 3), TX-2 | — | A-2, A-19 |
| C-18 | `drivers.low_risk` | `price_paid` (premium and surcharge together) | increase | medium | CR-12 (0.8: two items; kind 2 below the cut-off), RS-16 (0.9: costs on the substitute) | private policy `substitute` for SAIO policy | A-2, A-19 |
| C-19 | `drivers.high_risk` (quotes above the statutory premium by more than the surcharge) | `price_paid` (premium and surcharge together) | decrease | medium | CR-12b, CR-12e (arithmetic: true by the class's definition) | — | A-1 |
| C-20 | `policyholders.all` | `resources_available_other_uses` (surcharge) | decrease | medium | CR-8 (0.8: contingent), CR-3 (note: a sum insured drivers cannot avoid while they drive), OC-1 | — | A-2, A-19 |
| C-21 | `officials.public_insurer` | `non_tax_receipts` (surcharge received) | increase | medium | CR-8b, CR-12 (0.9) | — | A-2 |
| C-22 | `sellers.current` | `asset_value` (Lissmark books of business, claims offices, agency ties) | decrease | short (from January 2027) | CR-7c, CR-10c, CR-7b | — | A-1, A-14 |
| C-23 | `intermediaries` (agents) | `quantity_traded` (policies placed) | decrease | short to medium | CR-9 | agent services `input_to` private policies | A-15 |
| C-24 | `sellers.current` | `employment`, `hours_worked` (Lissmark underwriting and claims staff) | at_least_one_decrease | medium | RS-6, CR-9 | — | A-3, A-16 |
| C-25 | `officials.public_insurer` | `employment` | increase | short | OC-5 (new activities), CR-9 | — | A-1 |
| C-26 | `claimants.third_party` (victims of drivers who would have been uninsured) | `resources_available_other_uses` (claims paid) | increase | short to medium | CR-9 (`contract`), CR-8b | liability policy covers third parties: `contract` | A-6, A-17 |
| C-27 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` (initial reserves) | at_least_one_decrease | short | OC-1 (Who pays), CR-8 (0.7) | — | none |

**The deficit (C-16).** The Office's policyholders are, by selection, those whose expected claims exceed its premium (A-2). A second chain in the same direction: the Office does not rate by record, so an at-fault claim or an offense no longer raises a policyholder's premium, and some take less care (CR-4; A-18). The accidents themselves are a safety effect, out of scope; the claims they bring are money and are counted. Both chains raise the outlay; it is an activity that exists only under the Act, so it is an `increase` against none (CR-12, 0.9).

**Who pays (C-17, C-20, C-21, C-27; CR-8 0.8).** The deficit is paid first from the $200 million appropriated from the general budget, whose payers are a group (C-27; OC-1), and then, if reserves run out, by the surcharge on every policy. The surcharge is a contingent payment, recorded with a premise on the contingency: A-2 (p = 0.85) from the actuary's estimate that reserves run out in 2028. Short-run (2028): no surcharge; medium run: the surcharge. Every insured driver pays it, including the Office's own policyholders, and cannot avoid it while driving legally (CR-3 note), so `resources_available_other_uses` falls (C-20). The Office receives it (C-21). Because it is the same on public and private policies, it does not change any driver's choice between them.

**Private prices (C-18; RS-16 and CR-12, 0.9).** For a driver who stays private there are two items in `price_paid`. The surcharge is an increase from 2029 (C-17; A-19: billed as a separate line, so it reaches drivers). The premium for the driver's risk class has two possible chains, both below the cut-off: RS-16's mirror case (demand falls, and private supply cannot contract at once, A-4, p = 0.35) would lower it; fixed costs per insurer in the State spread over fewer policies (A-5, p = 0.35) would raise it. CR-12's response argument was tried on the first: insurers' contraction is a response to lower demand and, by CR-12e, cannot raise the premium above its old level. That fails here, because insurers' costs per policy rise as their books shrink when part of their costs is fixed; the response restores equal yields, not the old price (Gaps found, b1). With both premium chains below the cut-off, the derived sign for the total is the surcharge's: `increase` (C-18; CR-12, 0.8, kind 2). RS-16's 0.9 clause on costs attached to the substitute itself prompted the surcharge as an opposing chain on the private price, as written; under A-19 it falls on `price_paid`, not on insurers' net price.

**High-risk drivers' total (C-19).** For drivers whose quotes exceed the statutory premium by more than the surcharge, the total paid falls by definition of the class; drivers whose quotes exceed it by less still switch (the surcharge is on both policies) but pay more in total than in the counterfactual once the surcharge applies, and are included in C-18's class.

**Private insurers' values and staff (C-22 to C-24).** The loss of about 700,000 policies lowers the return on capital that is specific to the State: agency relationships, claims offices, brand (CR-7b, CR-7c; A-14). Their value falls from when the bill became likely, part from January 2027 and the rest at enactment (CR-10c). Agents lose placements (C-23), and private staff fall (C-24); the Office hires (C-25), a new activity (OC-5).

**Victims (C-26).** Fewer uninsured drivers means that more people injured by them are paid by an insurer (A-17: some lack their own uninsured-motorist cover). Their receipts are paid from the Office's premiums and the surcharge (C-16, C-20). The insurers that would have paid victims through uninsured-motorist cover pay less; depth 3, not followed.

Stopping points: used-car prices (from C-14 and C-15, opposite directions, depth 3); agents' and insurers' staff spending; roads and accidents (safety, out of scope; congestion would run over a `shared_facility` relation, Tier C, not followed).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `drivers.high_risk` (quotes above statutory premium plus surcharge), `price_paid` (total), medium | Surcharge. | Uniform premium below quote. | CR-12e: arithmetic, by the class's definition | **decrease** (C-19) |
| `drivers.low_risk`, `price_paid` (total), medium | Surcharge (A-2, A-19); fixed costs per insurer (A-5, p = 0.35). | Lower demand for private cover (A-4, p = 0.35). | CR-12 0.8 kind 2 below the cut-off | **increase** (C-18) |
| all drivers, `legal_breach` (uninsured), short | Cheaper cover for high-risk drivers. | None (no surcharge in 2028). | None needed | **decrease** (C-5) |
| all drivers, `legal_breach` (uninsured), medium | Surcharge at the margin of insuring (A-6). | Cheaper cover for high-risk drivers. | A-7 (empirical) | **decrease** (C-6) |
| `drivers.serious_offense`, `legal_breach`, medium | U1-a and U1-b: surcharge. | U1-b: price cut from about $2,600 to the regional premium. | U1-b: arithmetic on the figures | U1-a: **increase**; U1-b: **decrease** (C-7) |
| all drivers, `quantity_complement` (vehicles owned), medium | High-risk drivers (C-14). | Low-risk drivers (C-15). | None | **ambiguous** (not recorded as a separate consequence; per-class signs C-14, C-15) |
| `officials.public_insurer`, `subsidy_outlay` | Selection (A-2); less care without rating (A-18). | None. | None needed | **increase** (C-16) |
| `sellers.current`, premium per risk class, medium | Fixed costs (A-5). | Lower demand (A-4). | — | Not reported: both chains below the cut-off. |

## 8. Time structure

- **January to December 2027: expectation.** Private insurers' values fall as the bill becomes likely and then law (C-22). High-risk drivers renewing in the second half of 2027 buy short terms (C-12).
- **2028: the Office opens.** Switching is fast: a policy lasts at most a year, so the switch completes within a year (C-1, C-4). Claims handling lags (C-13). Reserves are drawn down; no surcharge (C-5).
- **From 2029: the surcharge.** Set each year on the past year's deficit, so it lags losses by a year (C-17 to C-21).
- **Erosion (TS-3).** Premiums are indexed to CPI; if claims costs rise faster (medical and repair costs, A-21), the statutory premium falls relative to cost each year, more drivers switch, and the deficit and the surcharge grow.
- **Private insurers' plant.** Claims offices and agency networks keep operating while they cover running costs (PC-19, 0.9), so private capacity in the State shrinks over several years (C-24, TS-1).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-27 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` | at_least_one_decrease | The $200 million in reserves. | OC-1, CR-8 |
| C-20 | `policyholders.all` | `resources_available_other_uses` | decrease | Whatever the surcharge would have bought. | OC-1, CR-8 |
| C-28 | `officials.public_insurer` | `enforcement_cost` (administration: issuing policies, claims handling) | increase | Staff and systems, paid from premiums and so, at the margin, from the surcharge. | OC-3 (own revenue), CR-8c |
| C-29 | `drivers.high_risk` | `compliance_cost` (switching insurer, short-term policies, separate purchase of optional cover from private insurers) | increase | Time spent switching. | OC-2, CR-8c |

Both sides of every transfer: premiums below cost (C-1 / C-16), surcharge (C-20 / C-21), reserves (C-27 / C-16), claims to victims (C-26 / C-16).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The Office issues policies promptly to all eligible applicants at the statutory premium. | other | 0.9 | Act s. 6; online issuance. | C-1 to C-4 and all that follows shrink. |
| A-2 | Switchers' expected claims and expenses exceed their premiums by enough to exhaust the reserves in about a year, so the surcharge applies from 2029. | other | 0.85 | Actuary's estimate: deficit about $300 million a year against $200 million of reserves. | C-16 smaller; C-17, C-18, C-20, C-21 and the (+) chains of C-6, C-7 and C-15 are delayed or not reported. |
| A-3 | Private insurers' supply per risk class contracts at about unchanged cost, so lower demand shows in quantity. | durability | 0.65 | Cost is mostly expected claims; capital moves between lines and states. | C-4 is recorded as a group with the private premium; C-24 not reported. |
| A-4 | Private supply cannot contract at once, so premiums per risk class fall. | durability | 0.35 | As A-3. | Below the cut-off: not reported. |
| A-5 | State-specific fixed costs make private insurers' cost per policy rise as books shrink. | other | 0.35 | Agency and claims-office costs are a modest share of premium. | Below the cut-off: not reported. |
| A-6 | Some drivers are at the margin between insuring and driving uninsured (or not owning a vehicle). | substitutability | 0.75 | Uninsured rates of 30% and 7%. | C-5, C-6, C-15, C-26 are not reported. |
| A-7 | The fall in uninsured driving among high-risk drivers exceeds any rise among other drivers from the surcharge. | other | 0.7 | Price changes of hundreds of dollars against $75 to $105; uninsured rate 30% against 7%. | C-6 is `ambiguous`. |
| A-8 | Some serious offenders are at the margin of insuring. | substitutability | 0.6 | Their quotes average $2,600. | C-7 is not reported. |
| A-9 | Some high-risk drivers buy or keep a vehicle when cover is cheaper. | other | 0.6 | Young drivers' ownership against insurance cost. | C-14 is not reported. |
| A-10 | The Office's address checks are weak enough that some drivers register at addresses in cheaper regions. | enforcement | 0.6 | No inspection of garaging; $370 a year at stake in Metro. | C-8 is not reported. |
| A-11 | Insurers, drivers' groups and consumer groups organize at a cost below their stakes. | other | 0.85 | Existing associations. | C-11 is not reported. |
| A-12 | Drivers renewing in late 2027 can buy short-term policies. | other | 0.6 | Six-month and monthly policies are offered. | C-12 is not reported. |
| A-13 | The Office's claims staff lag the inflow of policies in 2028. | durability | 0.6 | Hiring and training of adjusters takes months. | C-13 is not reported. |
| A-14 | Private insurers hold capital specific to the State (agency ties, claims offices, brand). | mobility | 0.7 | Local claims operations. | C-22 is not reported. |
| A-15 | Switchers would have bought through agents and buy from the Office direct. | other | 0.8 | Most private policies sold by agents. | C-23 is not reported. |
| A-16 | Private staff adjust to the size of the book. | alternative_uses | 0.7 | Staffing ratios. | C-24 is not reported. |
| A-17 | Some victims of drivers who would have been uninsured lack their own uninsured-motorist cover. | other | 0.6 | Optional cover; take-up rates. | C-26 is not reported. |
| A-18 | Without rating by record, some Office policyholders take less care. | other | 0.6 | Experience rating in private cover. | C-16 rests on selection alone. |
| A-19 | The surcharge, billed as a separate line, is paid by policyholders. | other | 0.9 | Act s. 9. | C-17, C-18, C-20 fall partly on insurers' net price instead. |
| A-20 | Under U1-a, the Office checks conviction records before issuing and refuses offenders. | other | 0.8 | State conviction database. | C-9, C-10 under U1-a are not reported. |
| A-21 | Claims costs rise faster than CPI. | counterfactual_trend | 0.7 | Medical and repair cost trends. | The erosion in section 8 does not arise. |

## 11. Report

**The policy.** From January 2028 a state office sells basic auto liability cover to any driver at a premium fixed by statute for each of three regions, the same for every driver in the region. Its losses beyond $200 million of reserves are paid by a surcharge on every auto policy in the State. Whether it may refuse drivers with recent serious offenses is unclear.

**Visible consequences.** Drivers who were quoted more than the regional premium pay less (C-1); the Office sells many policies (C-2).

**Invisible consequences.**
- *Selection and its cost.* The drivers who move are those who cost most to cover, so the Office pays out more than it takes in (C-16), first from the general budget's reserves (C-27), then through a surcharge on every insured driver (C-17, C-20), which the Office receives (C-21). Drivers who stay private pay more in total (C-18); high-risk switchers still pay less (C-19).
- *Private insurers.* They sell fewer policies (C-4), lose value from when the bill became likely (C-22), and cut staff (C-24), while agents place fewer policies (C-23) and the Office hires (C-25).
- *Uninsured driving.* It falls in 2028 (C-5) and, on a dominance premise, after the surcharge too (C-6). More victims are paid by an insurer (C-26).
- *Other responses.* Misreported addresses (C-8); short-term policies before the opening (C-12); slower claims in the first year (C-13); more vehicles owned by high-risk drivers and fewer by others (C-14, C-15); lobbying (C-11); administration and switching costs (C-28, C-29).

**Per reading of U1.** If the Office may refuse offenders (U1-a), it screens them (C-9, C-10), their premiums do not fall (C-3), and the surcharge pushes some of them into driving uninsured (C-7). If it may not (U1-b), their premiums fall sharply and their uninsured driving falls; the deficit and the surcharge are larger.

**Ambiguous effects.** The total number of vehicles owned (section 7). The private premium for a given driver is not signed: the chains that would move it are each below the cut-off.

**Key conditions.** Selection and the timing of the surcharge (A-2, p = 0.85); private supply contracting at constant cost (A-3, p = 0.65); the dominance premise on uninsured driving (A-7, p = 0.7).

**What this analysis cannot say.** The effect on accidents, injuries and road safety (out of scope for version 1); sizes; whether the cross-subsidy from low-risk to high-risk drivers is fair; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | drivers.high_risk | price_paid (premium) | decrease | short | visible | B | CR-1, CR-4, PC-19 | A-1 |
| C-2 | officials.public_insurer | quantity_supplied (policies) | increase | short–long | visible | B | CR-6, CR-12 | A-1 |
| C-3 | drivers.serious_offense | price_paid (premium) | U1-a: no_change; U1-b: decrease | short | visible | B | CR-1, CR-4 | A-1 |
| C-4 | sellers.current | quantity_supplied (private policies) | decrease | short–medium | invisible | B | PC-19, CR-6, CR-9, RS-16 | A-1, A-3 |
| C-5 | drivers.uninsured, drivers.high_risk | legal_breach (uninsured driving) | decrease | short | invisible | B | CR-4, CR-1 | A-1, A-6 |
| C-6 | all drivers | legal_breach (uninsured driving) | decrease | medium | invisible | B | CR-4, CR-12b, CR-12e | A-2, A-6, A-7, A-8 |
| C-7 | drivers.serious_offense | legal_breach (uninsured driving) | U1-a: increase; U1-b: decrease | medium | invisible | B | CR-4, CR-12e | A-2, A-8 |
| C-8 | drivers.high_risk (Metro) | legal_breach (address misreporting) | increase | short–medium | invisible | B | RS-5, RS-3, CR-4 | A-10 |
| C-9 | officials.public_insurer | allocation_by_non_price_criteria (refusals) | U1-a: increase; U1-b: no_change | short–long | invisible | B | CR-4, CR-5c | A-20 |
| C-10 | officials.public_insurer | enforcement_cost (record checks, appeals) | U1-a: increase; U1-b: no_change | short–long | invisible | B | OC-3, CR-8c | A-20 |
| C-11 | sellers.current, drivers | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-11 |
| C-12 | drivers.high_risk | term_prevalence (short-term policies, late 2027) | increase | short | invisible | B | RS-8, CR-10a | A-12 |
| C-13 | claimants.third_party | wait_time (claim settlement) | increase | short | invisible | B | CR-6, PC-19 | A-13 |
| C-14 | drivers.high_risk | quantity_complement (vehicles owned) | increase | medium | invisible | B | RS-12, CR-9 | A-1, A-9 |
| C-15 | drivers.low_risk | quantity_complement (vehicles owned) | decrease | medium | invisible | B | RS-12, CR-4, CR-8 | A-2, A-6 |
| C-16 | officials.public_insurer | subsidy_outlay (claims and expenses beyond premiums) | increase | short–long | invisible | B | CR-4, CR-5c, CR-8b, CR-12 | A-1, A-2, A-18 |
| C-17 | policyholders.all | price_paid (surcharge) | increase | medium | invisible | B | CR-8, CR-1, TX-2 | A-2, A-19 |
| C-18 | drivers.low_risk | price_paid (premium and surcharge) | increase | medium | invisible | B | CR-12, RS-16 | A-2, A-19 |
| C-19 | drivers.high_risk (quote above premium plus surcharge) | price_paid (premium and surcharge) | decrease | medium | invisible | B | CR-12b, CR-12e | A-1 |
| C-20 | policyholders.all | resources_available_other_uses (surcharge) | decrease | medium | invisible | B | CR-8, CR-3, OC-1 | A-2, A-19 |
| C-21 | officials.public_insurer | non_tax_receipts (surcharge) | increase | medium | invisible | B | CR-8b, CR-12 | A-2 |
| C-22 | sellers.current | asset_value (Lissmark operations) | decrease | short | invisible | B | CR-7c, CR-10c, CR-7b | A-1, A-14 |
| C-23 | intermediaries (agents) | quantity_traded (policies placed) | decrease | short–medium | invisible | B | CR-9 | A-15 |
| C-24 | sellers.current | employment, hours_worked | at_least_one_decrease | medium | invisible | B | RS-6, CR-9 | A-3, A-16 |
| C-25 | officials.public_insurer | employment | increase | short | visible | B | OC-5, CR-9 | A-1 |
| C-26 | claimants.third_party | resources_available_other_uses (claims paid) | increase | short–medium | invisible | B | CR-9, CR-8b | A-6, A-17 |
| C-27 | taxpayers, recipients of other spending, future taxpayers | resources_available_other_uses (reserves) | at_least_one_decrease | short | invisible | A | OC-1, CR-8 | none |
| C-28 | officials.public_insurer | enforcement_cost (administration) | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-29 | drivers.high_risk | compliance_cost (switching) | increase | short | invisible | B | OC-2, CR-8c | A-1 |

**Final check.** (1) Uncombined chains: price paid by each driver class, uninsured driving and vehicles owned are combined in section 7; the private premium per risk class is left unsigned with both chains recorded. (2) Groups: private staff (C-24), payers of the reserves (C-27). (3) Baseline: every sign is against no Act; U1-b's larger surcharge is not used as a sign against U1-a. Switchers whose quote exceeds the premium by less than the surcharge pay more than in the counterfactual and are not included in C-19. (4) Worse off is not poorer: `resources_available_other_uses` falls only for those who keep paying an unavoidable surcharge (C-20) and the reserves' payers (C-27). (5) Timing: 2028 against 2029 on are separate windows (C-5 / C-6); C-12 exists only under the Act. (6) Both sides: section 9. (7) Capitalization: private insurers (C-22); agents' books follow C-23; drivers hold no priced asset tied to the policy. (8) Premises: section 10, including those below the cut-off.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Selection, the deficit and the surcharge were derived from CR-4 per counterparty, CR-5c and CR-8. Effects through accidents are safety (out of scope); congestion would be a `shared_facility` chain (GAP-026-1, Q20, closed in 0.7 as Tier C), not followed.

**(b) Unclear core rules.**
1. *CR-12e and its 0.9 note (what the response argument gives).* The argument says a response cannot reverse the change that causes it, because it stops once yields are equal. Equal yields restore the old price only where the cost per unit of the sellers who remain does not change with their volume. Here, insurers' contraction with fixed costs per insurer could leave the premium per risk class above its old level. The note should say that the response argument gives "not reversed" only with a premise of constant cost per unit, or should speak of yields rather than prices.
2. *CR-6 0.9 (a public seller with an open quantity).* Says buyers move to it and rivals face lower demand, but not that, where the seller's price is uniform and its cost differs by buyer, the buyers who move are not a random sample. The seller's cost per unit then rises with its sales; that had to come from CR-4 per counterparty.
3. *CR-8 0.8 (contingent payers), cited in the brief as 0.9.* Worked, but the contingency is set by a rule (reserves below zero) whose timing decides the horizon; recorded by window (no surcharge in 2028, surcharge from 2029). CR-8's 0.9 "reading that permits" was not exercised: the surcharge is required.

**(c) Missing or wrong patterns.**
1. *RS-16 (mirror case), in a market priced by risk.* Applied as written, it signs the substitute's price as a decrease. Here "price" must be read per risk class: the average private premium per policy falls because high-risk drivers leave, which is a change in the mix, not in any driver's price. Per risk class, the mirror's premise (supply that cannot contract) is weak where cost is mostly the expected claim (A-4, p = 0.35), so no sign was reported. RS-16 should say that the price is signed per unit of a given quality or risk, and that composition changes are not price changes.
2. *PC-19 0.9 (open quantity).* Correct as far as it goes, but silent on selection: a public seller at a uniform price with no fixed quantity meets rivals who price by buyer. Proposed addition: "where the public price is uniform and rivals price by counterparty, buyers who move are those whose cost to the seller exceeds its price, so its outlay per unit rises (candidate: selection under a uniform term)".
3. *Candidate "selection under a uniform term"* (6.2e, from WE-029). Needed. Proposed wider form: "If: a term or price is uniform across counterparties while the cost of serving them differs, and counterparties can choose an alternative priced by cost (or the provider can choose counterparties). Then: counterparties for whom the uniform term is a better deal than their alternative choose it (CR-4 per counterparty), so the provider's cost per unit exceeds the average; where the provider may refuse, it screens by non-price criteria. Derivation: CR-4, CR-5c, CR-6."

**(d) Vocabulary.**
1. No variable for the risk mix or expected cost per unit of a seller's book; `subsidy_outlay` was used for claims beyond premiums.
2. `public_supply` (2.3) is defined with "quantity set by a budget"; a public seller with an open quantity has no instrument type of its own.
3. No actor class for third parties paid under a contract they are not party to (accident victims); `claimants.third_party` used.

**(e) Test of 0.9.**
- *PC-19 0.9, open quantity.* Worked as written: no rationing; buyers move to the Office; the private price-quantity split taken from a premise (C-4); immobile plant noted. Silent on selection (c2).
- *CR-6 0.9, a public seller with an open quantity.* Worked as written, including the lag clause for claims staff (C-13). Did not prompt selection (b2).
- *Selection under a uniform term (candidate, 6.2e).* Needed, on both sides: buyers sort themselves (C-16) and, under U1-a, the provider screens (C-9). Each consequence is signed against no Act (the outlay and the screening exist only under it), so this second use is valid and promotes the candidate, in the wider form in c3.
- *CR-8 contingent payers (0.8; cited as 0.9).* Worked as written, with a premise on the contingency and separate windows (C-17, C-20, C-21); the reserves' general-budget payers recorded as a group (C-27).
- *RS-16 (private insurers' prices), with its 0.9 costs-on-the-substitute clause.* The 0.9 clause worked: it prompted the surcharge as a chain on the private price (C-18). The main mirror clause needed interpretation (price per risk class, composition) and gave no reportable sign (c1).
- *CR-7c (private insurers' values).* Worked as written, with a premise of State-specific capital (A-14, C-22).
- *CR-12 0.9, what the response argument gives.* Failed on the case where it was tried: it assumes the response restores the old price, but with fixed costs per seller it restores equal yields at a possibly higher price (b1). Not used to sign anything; arithmetic (C-7 under U1-b, C-19) and an empirical dominance premise (A-7, C-6) were used instead.
- *CR-12 0.9, activities that exist only under the policy.* Worked (C-2, C-12, C-16, C-21).
- *CR-12 0.8, two items and kind 2 below the cut-off.* Worked (C-18).
- *OC-1 payers (0.8).* Worked: general-budget reserves as a group (C-27).
