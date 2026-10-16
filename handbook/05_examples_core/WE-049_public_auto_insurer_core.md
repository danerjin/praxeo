# WE-049 / Analysis: Public auto insurer at a uniform statutory premium, with a surcharge for its losses

Analyst: core-only re-run (Handbook 0.9)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**The Lissmark State Auto Insurance Office Act.** Every registered private vehicle in Lissmark must carry basic liability cover; registration requires proof; driving uninsured is fined $500. About 4.0 million policies are in force (Metro 2.0 million, Valley 1.2 million, Upland 0.8 million); about 500,000 more vehicles (11%) are driven uninsured (about 30% among drivers quoted above $1,500, about 7% among others). Thirty-eight private insurers price each driver by risk. Average basic premium in 2026: Metro $820 (about $380 to $3,600), Valley $560, Upland $450. About 120,000 drivers (3%) have a serious offense in the past three years; their average premium is about $2,600. Private premiums carry a loading of about 20% over expected claims; most policies are sold through agents on commission. Neighboring Norvey has no public insurer.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | State of Lissmark; Norvey (no public insurer) | Act s. 1 |
| Announced / enacted / effective / expires | 10 January 2027 (bill introduced) / 30 June 2027 / 1 January 2028 / none | Act s. 2 |
| Enforcement (who, penalties, resources) | The State Auto Insurance Office (SAIO) issues policies online and at motor vehicle offices, without agents. The Insurance Commissioner sets the surcharge. Existing compulsory-insurance rules and fines continue. | Act s. 4, 9 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Public insurer | `public_supply` (open quantity) | Basic liability cover | SAIO | Sells to any eligible driver who applies and pays, no limit on numbers. Premium set by statute, uniform within each region, not rated by driver: Metro $820, Valley $560, Upland $450, indexed to CPI. Basic cover only. | See U1 |
| K2 Surcharge | `per_unit_tax` (contingent) | Every motor liability policy, public and private | Insurers collect as a separate bill line; policyholders pay | If SAIO's reserves fall below zero, the Commissioner sets a per-policy surcharge for the next year to restore reserves to $200 million; insurers remit it to SAIO. | - |
| K3 Initial reserves | `lump_sum_subsidy` | SAIO | General budget | $200 million once, not repaid. | - |

**Existing rules.** Compulsory basic liability cover; proof at registration; $500 fine. They stay in place in the counterfactual.

**Counterfactual.** Lissmark without the Act: private, risk-rated insurers only; no surcharge.

**Figures.** If drivers whose quotes exceed the statutory premium by more than about 10% switch (about 700,000 policies, average private quote about $1,350, expected claims about $1,100), the Office's premiums average about $740 against claims of $1,100 and expenses of about $74: a deficit of about $430 a policy and $300 million a year. Reserves run out in 2028; the surcharge is then about $75 a policy. Under U1-b, if 80,000 serious offenders also switch (expected claims about $2,150), the deficit rises by about $120 million and the surcharge to about $105.

Unclear provisions:
- **U1, drivers with recent serious offenses.** s. 6(1) (the Office "shall issue" to any licensed driver who registers a vehicle and pays) against s. 6(4) (it "may refuse or cancel" where the applicant "presents an exceptional hazard as defined by rule"; no rule made). **U1-a:** a serious offense in the past three years is an exceptional hazard, and the Office refuses such drivers. **U1-b:** the term refers to the vehicle or its use, and the Office must accept every licensed driver. Readings get no probability.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
|---|---|---|---|---|
| K1 Public insurer | binary (state sells at a set price below cost for part of its buyers) | Yes for drivers whose risk-rated quote exceeds the statutory premium (A-1) | Op 2 (a new option: cover at the regional statutory premium) for every eligible driver; under U1-a, not for serious offenders (A-20) | CR-4, CR-6 (0.9 public seller with open quantity), CR-9, CR-11a |
| K2 Surcharge | binary (state takes) | Yes from 2029 (A-2) | Op 3 on the option 'insure a vehicle' (a charge per policy, avoidable only by not insuring or not owning); op 3 on insurers (collect and remit) | CR-3, CR-4, CR-8a, CR-8b, CR-8c |
| K3 Initial reserves | binary (state gives) | Yes | Op 4 (from the general budget to SAIO) | CR-8b, CR-8 (0.7) |

Existing rule made more relevant: compulsory cover means the uninsured option already carries a risk of a $500 fine (op 3); K1 and K2 change the cost of the insured option relative to it.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| drivers.high_risk.switching | Drivers whose private quote exceeds the statutory premium by enough to switch (about 700,000) | Op 2: cheaper cover; from 2029 op 3: surcharge |
| drivers.high_risk.previously_uninsured | High-quote drivers who drove uninsured | Op 2 makes insuring cheaper than before |
| drivers.low_risk | Drivers whose quote is below the statutory premium | No useful new option; op 3: surcharge from 2029 |
| drivers.serious_offenders | About 120,000 drivers | U1-a: refused (no op 2), surcharge only; U1-b: op 2 at the statutory premium |
| drivers.renewing_late_2027 | Drivers whose annual renewal falls before 1 January 2028 | CR-10a: switching date known |
| policyholders.all | Every holder of a liability policy | Op 3: surcharge line from 2029 |
| sellers.private_insurers | 38 risk-rating insurers | Through CR-9 (substitute): lose high-quote buyers; op 3: collect the surcharge |
| intermediaries.agents | Agents on commission | Through CR-9 (contract, input_to): fewer policies to place |
| workers.private_insurers | Staff of private insurers | Through CR-9 (input_to) |
| officials.saio | The Office | Sells at a set price; reserves; claims staff |
| claimants.saio | Third parties claiming against Office policyholders | Through CR-9 (contract: the Office's policy pays them) |
| victims.of_previously_uninsured | Third parties hit by drivers who would have been uninsured | Through CR-9 (contract): now paid by an insurer |
| sellers.uninsured_motorist_cover | Insurers selling optional uninsured-motorist cover | Through CR-9 (substitute) |
| sellers.vehicles | Sellers of vehicles | Through CR-9 (complement: cover is used with a vehicle) |
| registrants.motor_vehicle_offices | Users of motor vehicle offices | shared_facility: the Office sells policies there |
| taxpayers | Fund K3 | Op 4 via the general budget |
| neighboring_jurisdictions (Norvey) | Possible place of registration | across_border; A-N4 (p 0.2): not reported |
| insurers' and agents' associations, drivers' and consumer groups | Political action | CR-4 (x: accept, y: lobby) |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | drivers.high_risk.switching | price_paid (basic cover premium) | decrease | short | CR-1 op 2, CR-2, CR-4 | A-1 |
| C-3 | policyholders.all | price_paid (surcharge line) | increase | medium; long | CR-1 op 3, CR-8b | A-2, A-19 |
| C-4 | officials.saio | subsidy_outlay (initial reserves) | increase | short | CR-1 op 4, CR-8b | - |
| C-5 | taxpayers, recipients of other spending | resources_available_other_uses | at_least_one_decrease | short | CR-8b, CR-8 (0.7) | - |
| C-6 | officials.saio | tax_revenue (surcharge receipts) | increase | medium; long | CR-8b | A-2, A-19 |
| C-8 | drivers.high_risk.switching | quantity_traded (Office policies) | increase | short; medium; long | CR-4 | A-1 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-2 | drivers.high_risk.switching | price_paid (premium plus surcharge) | decrease | medium; long | CR-12b, CR-12e (arithmetic) | A-1, A-2, A-19 |
| C-11 | drivers.high_risk.previously_uninsured | informal_activity (uninsured driving) | decrease | short; medium; long | CR-4 | A-1, A-6 |
| C-12 | drivers.low_risk | informal_activity (uninsured driving) | increase | medium; long | CR-4 | A-2, A-6, A-19 |
| C-13 | drivers (all) | informal_activity (uninsured driving) | decrease | medium; long | CR-12b, CR-12e | A-6, A-7 |
| C-14 | drivers.serious_offenders | price_paid (basic cover) | U1-a: no_change; U1-b: decrease | short | CR-1 op 2 (U1-b), CR-4 | A-1, A-20 |
| C-15 | drivers.serious_offenders | price_paid (basic cover plus surcharge) | U1-a: increase; U1-b: decrease | medium; long | CR-1, CR-12e | A-1, A-2, A-19, A-20 |
| C-16 | drivers.serious_offenders | informal_activity (uninsured driving) | U1-a: increase; U1-b: decrease | medium; long | CR-4 | A-2, A-8, A-20 |
| C-17 | drivers.high_risk | quantity_complement (vehicles owned) | increase | short; medium; long | CR-4, CR-9, CR-11a | A-1, A-9 |
| C-18 | drivers.low_risk | quantity_complement (vehicles owned) | decrease | medium; long | CR-4 | A-2, A-6, A-19 |
| C-21 | drivers.metro (some) | legal_breach (garaging address misstated to the Office) | increase | short; medium; long | CR-4 (x: comply, y: violate) | A-1, A-10 |
| C-23 | drivers.renewing_late_2027 | term_prevalence (short-term policies bought in late 2027) | increase | short | CR-10a, CR-4 | A-1, A-12 |
| C-29 | officials.saio | enforcement_cost (running the Office) | increase | short; medium; long | CR-8a, CR-8c | A-1 |
| C-36 | officials.saio | enforcement_cost (conviction-record checks) | U1-a: increase; U1-b: no_change | short; medium; long | CR-1, CR-8c | A-20 |
| C-28 | sellers.private_insurers | compliance_cost (collecting and remitting the surcharge) | increase | medium; long | CR-1 op 3, CR-8c | A-2 |
| C-33 | sellers.private_insurers, intermediaries.agents | lobbying_effort (to restrict or repeal the Office) | increase | short; medium; long | CR-4, CR-8c | A-11, A-14 |
| C-34 | drivers' and consumer groups | lobbying_effort (over the surcharge and statutory premiums) | increase | medium; long | CR-4, CR-8c | A-2, A-11 |

## 6. Second-order effects

CR-9 along named relations. Depth limit 4. Fuel and repairs as complements of extra vehicles are pruned at depth 3 as diffuse.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-7 | policyholders.private (staying) | resources_available_other_uses | decrease | medium; long | CR-3 (note), CR-8a | - | A-2, A-19 |
| C-9 | sellers.private_insurers | quantity_traded (private basic policies) | decrease | short; medium; long | CR-9, CR-6 (0.9) | Office cover substitute for private cover (close) | A-1, A-3 |
| C-10 | sellers.private_insurers | net_price_received (premium per risk class) | no_change | short; medium | CR-6 (0.9 split), CR-12 (0.8 kind 2) | as above | A-3 |
| C-19 | sellers.vehicles | quantity_traded (vehicles) | increase | short | CR-9 | cover complement to vehicles | A-1, A-9 |
| C-20 | sellers.vehicles | quantity_traded (vehicles) | ambiguous | medium; long | CR-9, CR-12b | as above | A-2, A-6, A-9, A-19 |
| C-24 | sellers.private_insurers | asset_value (Lissmark books and capital) | decrease | short (from introduction) | CR-7b, CR-7c, CR-10c | - | A-1, A-3, A-14 |
| C-25 | workers.private_insurers | employment | decrease | medium; long | CR-9, LW-10 | staff input_to private policies | A-1, A-3, A-16 |
| C-26 | intermediaries.agents | earnings (commissions) | decrease | short; medium; long | CR-9, LW-10 | agents' services input_to private policies | A-1, A-15 |
| C-27 | sellers.private_insurers | number_of_sellers | decrease | medium; long | CR-4, CR-7a | - | A-1, A-3, A-N1 |
| C-30 | claimants.saio | wait_time (claims settlement) | increase | short | CR-6 (0.7), CR-9 | contract (the Office's policy) | A-1, A-13 |
| C-31 | victims.of_previously_uninsured | resources_available_other_uses | increase | short; medium; long | CR-9, CR-8b | contract (the new policy) | A-6, A-7, A-17 |
| C-32 | sellers.uninsured_motorist_cover | price_substitute (uninsured-motorist cover) | decrease | medium; long | CR-9, CR-7a | own uninsured-motorist cover substitute for the at-fault driver's liability cover | A-6, A-7, A-N2 |
| C-35 | registrants.motor_vehicle_offices | wait_time | increase | short | CR-9 (0.7 shared facility) | shared_facility (motor vehicle offices) | A-1, A-N3 |
| C-39 | drivers.high_risk.switching | resources_available_other_uses | increase | short; medium; long | CR-8b, CR-12e | - | A-1, A-2, A-19 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| drivers.high_risk.switching, price_paid, medium; long | surcharge $75 to $105 (C-3) | statutory premium against risk-rated quote (C-1) | Arithmetic on the case figures (CR-12e): average quote about $1,350 against average Office premium about $740 plus $75 to $105. Holds for the class; members whose quotes are just over the switching line may pay more than without the Act | decrease (C-2) |
| drivers (all), informal_activity, medium; long | low-risk drivers drop cover because of the surcharge (C-12); U1-a offenders (C-16) | high-quote drivers insure (C-11); U1-b offenders (C-16) | A-7 (empirical, 0.7) covers the low-risk chain; under U1-a the offender chain is the same kind of surcharge chain and is covered by A-7's comparison of price changes | decrease (C-13); short run, decrease with no opposing chain |
| sellers.vehicles, quantity_traded, medium; long | high-risk drivers keep or buy vehicles (A-9) | surcharge on low-risk owners (A-6) | None | ambiguous (C-20); short run increase (C-19) |
| sellers.private_insurers, net_price_received per risk class | fixed costs over a smaller book (A-5, p 0.35) | supply cannot contract at once (A-4, p 0.35) | Both opposing chains have p < 0.5 (kind 2 below cut-off): report the derived sign under A-3 | no_change (C-10) |
| drivers.serious_offenders, price_paid, medium; long | U1-a: surcharge | U1-b: statutory premium $820 or less against $2,600 | Per reading; under U1-b arithmetic ($2,600 against at most $820 plus $105) | U1-a: increase; U1-b: decrease (C-15) |
| policyholders.all, price_paid (surcharge) | deficit from switchers (A-2); less care by unrated Office policyholders (A-18); misstated addresses (A-10); U1-b offenders; claims outrunning CPI (A-21, long) | - | All chains the same sign | increase (C-3) |
| victims.of_previously_uninsured, resources_available_other_uses, medium; long | more of those who would hit them are insured (C-11) | low-risk drivers dropping cover (C-12) | A-7 | increase (C-31) |

## 8. Time structure

Horizons: **short** = 10 January 2027 to the end of 2028 (introduction, enactment and the Office's first year, before any surcharge); **medium** = 2029-2030 (surcharge in force); **long** = after 2030.

- **Introduction and enactment.** The bill became likely to pass from January 2027 and certain on 30 June 2027; private insurers' state-specific capital loses value as the probability rises (CR-7c, C-24). Drivers renewing in late 2027 buy short-term policies so as to switch on 1 January 2028 (C-23); against the counterfactual, short-term policies in that window rise, and the annual policies they would have bought fall in that window (both against the same renewals).
- **2028.** Switching takes place at once (A-1); the Office's claims staff lag the inflow (A-13), so claims settle more slowly (C-30). Reserves run out during the year (A-2).
- **From 2029.** The surcharge applies to every policy (C-3), with the responses of low-risk drivers (C-12, C-18) and the opposing chains on uninsured driving and vehicles (C-13, C-20).
- **Long run.** Statutory premiums are indexed to CPI while claims costs rise faster (A-21), so the gap between Office premiums and claims widens each year: more drivers' quotes exceed the statutory premium, more switch, private books shrink further (C-9, C-25, C-26) and the surcharge grows (C-3). The Office's uniform price conveys no information about each driver's risk (CR-11a), so the drivers it attracts and their care respond to the price rather than to their risk (A-18).
- **Durability.** Private insurers' agency ties and claims offices are specific (A-14) and change only through flows (CR-10b), so employment and the number of sellers fall gradually (C-25, C-27).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-5 | taxpayers, recipients of other spending | resources_available_other_uses | at_least_one_decrease | The $200 million initial reserves | CR-8b, CR-8 (0.7) |
| C-7 | policyholders.private (staying) | resources_available_other_uses | decrease | Purchases forgone out of the surcharge | CR-3 (note), CR-8a |
| C-28 | sellers.private_insurers | compliance_cost | increase | Billing and remittance work | CR-8c |
| C-29 | officials.saio | enforcement_cost (running the Office) | increase | Staff and systems (about $74 a policy) | CR-8a, CR-8c |
| C-33, C-34 | insurers, agents, drivers' groups | lobbying_effort | increase | Staff time and money on political action | CR-8c |
| C-35 | registrants.motor_vehicle_offices | wait_time | increase | Time at shared offices | CR-9 (0.7) |

CR-8b, both sides: switchers' lower premiums (C-39) are paid by the reserves (C-4, C-5) and then by every policyholder through the surcharge (C-3, C-6, C-7). Victims of drivers who would have been uninsured receive payments (C-31) funded within the same pool. Agents' commissions not earned (C-26) are matched by the Office's direct-sale costs (C-29), not by a gain to any class.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The Office issues policies promptly to all eligible applicants at the statutory premium. | other | 0.9 | Act s. 6; online issuance. | Most switching chains fail or are delayed |
| A-2 | Switchers' expected claims and expenses exceed their premiums by enough to exhaust reserves in about a year, so the surcharge applies from 2029. | other | 0.85 | Actuary: deficit about $300 million against $200 million. | All surcharge chains (C-3, C-6, C-7, C-12, C-18, C-28) move later or fail |
| A-3 | Private insurers' supply per risk class contracts at about unchanged cost, so lower demand shows in quantity. | durability | 0.65 | Cost mostly expected claims; capital moves. | C-10 fails; C-9 smaller |
| A-4 | Private supply cannot contract at once, so premiums per risk class fall. | durability | 0.35 | As A-3. | Not reported |
| A-5 | State-specific fixed costs make private cost per policy rise as books shrink. | other | 0.35 | Agency and claims-office costs a modest share. | Not reported |
| A-6 | Some drivers are at the margin between insuring and driving uninsured (or not owning a vehicle). | substitutability | 0.75 | Uninsured rates 30% and 7%. | C-11, C-12, C-18, C-31, C-32 fail |
| A-7 | The fall in uninsured driving among high-risk drivers exceeds any rise among others from the surcharge. | other | 0.7 | Changes of hundreds of dollars against $75 to $105. | C-13, C-31, C-32 become ambiguous in the medium and long run |
| A-8 | Some serious offenders are at the margin of insuring. | substitutability | 0.6 | Their quotes average $2,600. | C-16 fails |
| A-9 | Some high-risk drivers buy or keep a vehicle when cover is cheaper. | other | 0.6 | Young drivers' ownership against insurance cost. | C-17, C-19 fail; C-20 becomes decrease |
| A-10 | The Office's address checks are weak enough that some drivers register at addresses in cheaper regions. | enforcement | 0.6 | No inspection of garaging. | C-21 fails; C-3 loses one chain |
| A-11 | Insurers, drivers' groups and consumer groups organize at a cost below their stakes. | other | 0.85 | Existing associations. | C-33, C-34 fail |
| A-12 | Drivers renewing in late 2027 can buy short-term policies. | other | 0.6 | Six-month and monthly policies offered. | C-23 fails |
| A-13 | The Office's claims staff lag the inflow of policies in 2028. | durability | 0.6 | Hiring adjusters takes months. | C-30 fails |
| A-14 | Private insurers hold capital specific to the State. | mobility | 0.7 | Local claims operations. | C-24, C-33 fail or shrink |
| A-15 | Switchers would have bought through agents and buy from the Office direct. | other | 0.8 | Most private policies sold by agents. | C-26 fails |
| A-16 | Private staff adjust to the size of the book. | alternative_uses | 0.7 | Staffing ratios. | C-25 fails |
| A-17 | Some victims of drivers who would have been uninsured lack their own uninsured-motorist cover. | other | 0.6 | Optional cover. | C-31 fails |
| A-18 | Without rating by record, some Office policyholders take less care. | other | 0.6 | Experience rating in private cover. | C-3 loses one chain |
| A-19 | The surcharge, billed as a separate line, is paid by policyholders. | other | 0.9 | Act s. 9. | Surcharge chains fall on insurers instead |
| A-20 | Under U1-a, the Office checks conviction records before issuing and refuses offenders. | other | 0.8 | State conviction database. | Under U1-a, C-14 to C-16 take the U1-b signs; C-36 fails |
| A-21 | Claims costs rise faster than CPI. | counterfactual_trend | 0.7 | Medical and repair cost trends. | Long-run growth of the surcharge and switching (section 8) fails |
| A-N1 | Some private insurers whose Lissmark business is concentrated in high-quote drivers leave the State's basic-liability market. | alternative_uses | 0.55 | NEW. 38 insurers; about 700,000 of 4.0 million policies switch, all from the high-quote end; insurers' mix of risks differs (no figures in the record). | C-27 fails |
| A-N2 | Uninsured-motorist premiums follow expected claims under competition among insurers. | other | 0.7 | NEW. Cover sold by the same 38 risk-rating insurers; loading about 20% across lines. | C-32 fails |
| A-N3 | Motor vehicle offices are not staffed up in step with policy sales in 2028. | durability | 0.6 | NEW. Policies sold at motor vehicle offices from 1 January 2028; the Act gives the offices no new appropriation. | C-35 fails |
| A-N4 | Some Lissmark drivers register vehicles in Norvey to avoid the surcharge. | mobility | 0.2 | NEW. Registration requires residence; the surcharge is $75 to $105. | Not reported |

**Not reported** (an assumption below 0.5):
- Private premiums per risk class fall because supply cannot contract at once (CR-6): needs A-4 (p 0.35). Recorded as a kind 2 opposing chain to C-10.
- Private cost per policy rises over a smaller book, raising premiums (CR-6, CR-4 0.8 fixed costs): needs A-5 (p 0.35). Kind 2 chain to C-10.
- Registration moved to Norvey (CR-4, x: here, y: there): needs A-N4 (p 0.2).

## 11. Report

**The policy:** From 1 January 2028 a State office sells basic liability cover to any eligible Lissmark driver at a statutory premium that is the same for every driver in a region (Metro $820, Valley $560, Upland $450, indexed to CPI). It starts with $200 million from the budget; when its reserves run out, every motor policy in the State pays a surcharge to restore them.

**Visible consequences:** Drivers whose risk-rated quotes are above the statutory premium switch and pay less (C-1, C-8), and still pay less after the surcharge (C-2, C-39). Every policyholder pays a surcharge from 2029, about $75 a year, or about $105 if serious offenders are accepted (C-3), which the Office receives (C-6); taxpayers or other spending provide the $200 million (C-4, C-5).

**Invisible consequences:**
- *Low-risk drivers:* pay the surcharge with nothing to gain from the Office (C-7); some drop cover or a vehicle (C-12, C-18).
- *High-risk drivers:* more of them insure (C-11) and own vehicles (C-17); some misstate their address to get a cheaper region (C-21).
- *Private insurers and their agents and staff:* fewer policies (C-9), loss of value of State-specific capital from the bill's introduction (C-24), fewer staff (C-25), lower commissions (C-26), some exits (C-27), surcharge collection costs (C-28); premiums per risk class unchanged (C-10). They lobby against the Office (C-33).
- *Others:* claimants against Office policyholders wait longer in 2028 (C-30); victims of drivers who would have been uninsured are paid (C-31); uninsured-motorist cover becomes cheaper (C-32); vehicle sales rise in the short run (C-19); users of motor vehicle offices wait longer (C-35, Tier C).

**Ambiguous effects:** Vehicle sales from 2029 (C-20): cheaper cover for high-risk drivers against the surcharge on everyone else.

**Key conditions:** The Office's losses exhaust reserves in a year (A-2, 0.85); private supply contracts at unchanged cost (A-3, 0.65); uninsured driving falls more among high-risk drivers than it rises among others (A-7, 0.7); claims outrun CPI (A-21, 0.7), which makes the surcharge grow. U1 decides whether serious offenders pay less (U1-b) or only pay the surcharge (U1-a), and the surcharge is larger under U1-b. Added premises: some insurers exit (A-N1, 0.55), uninsured-motorist premiums follow claims (A-N2, 0.7), motor vehicle offices are not staffed up (A-N3, 0.6).

**What this analysis cannot say:** Sizes; net welfare; whether the policy is good. Road safety, accidents and injuries (including any effect of less care, A-18, or more high-risk vehicles on the road) are out of scope; only their effect on the Office's claims and the surcharge is traced.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | drivers.high_risk.switching | price_paid (basic cover premium) | decrease | short | visible | B | CR-1 op 2 (a new option at the statutory premium); CR-4 (x: risk-rated private cover, y: Office cover; y better for those quoted above it); CR-2 | A-1 |
| C-2 | drivers.high_risk.switching | price_paid (premium plus surcharge) | decrease | medium; long | visible | B | CR-12b: (−) C-1; (+) C-3; dominance by arithmetic on the case figures (CR-12e: average quote $1,350 against $740 plus $75 to $105), for the class as a whole | A-1, A-2, A-19 |
| C-3 | policyholders.all | price_paid (surcharge line) | increase | medium; long | visible | B | CR-1 op 3 (a charge per policy set to cover the Office's deficit); CR-8b (the deficit, switchers' claims and expenses over premiums, is paid by someone: here every policyholder); same-sign chains (CR-12a) from less care by unrated policyholders (CR-11a, CR-4, A-18), misstated addresses (A-10) and, under U1-b, accepted offenders | A-2, A-19 |
| C-4 | officials.saio | subsidy_outlay (initial reserves) | increase | short | visible | A | CR-1 op 4 ($200 million); CR-8b | none |
| C-5 | taxpayers, recipients of other spending | resources_available_other_uses | at_least_one_decrease | short | invisible | A | CR-8b; CR-8 (0.7: payers from the general budget as a group) | none |
| C-6 | officials.saio | tax_revenue (surcharge receipts) | increase | medium; long | visible | B | CR-8b (what policyholders pay through insurers is received by the Office) | A-2, A-19 |
| C-7 | policyholders.private (staying) | resources_available_other_uses | decrease | medium; long | invisible | B | CR-3 note (they keep insuring and pay a sum they cannot avoid while insured); CR-8a | A-2, A-19 |
| C-8 | drivers.high_risk.switching | quantity_traded (Office policies) | increase | short; medium; long | visible | B | CR-4 (x: private, y: Office); CR-6 (0.9: a public seller with open quantity has no excess demand to ration) | A-1 |
| C-9 | sellers.private_insurers | quantity_traded (private basic policies) | decrease | short; medium; long | visible | B | CR-9 (relation: Office cover substitute for private cover); CR-6 (0.9: rival sellers face lower demand; the split goes to quantity under A-3) | A-1, A-3 |
| C-10 | sellers.private_insurers | net_price_received (premium per risk class) | no_change | short; medium | invisible | B | CR-6 (0.9 split: supply contracts at unchanged cost, A-3, so the price per risk class stays); opposing kind 2 chains need A-4 and A-5 (p 0.35 each) and are not counted | A-3 |
| C-11 | drivers.high_risk.previously_uninsured | informal_activity (uninsured driving) | decrease | short; medium; long | visible | B | CR-4 (x: drive uninsured, at the risk of the fine; y: insure, now cheaper; those for whom x ranked narrowly above y switch) | A-1, A-6 |
| C-12 | drivers.low_risk | informal_activity (uninsured driving) | increase | medium; long | invisible | B | CR-4 (y: insure, made worse by the surcharge; some switch to x) | A-2, A-6, A-19 |
| C-13 | drivers (all) | informal_activity (uninsured driving) | decrease | medium; long | invisible | B | CR-12b: (−) C-11; (+) C-12; dominance premise A-7 (empirical, CR-12e). Short run: C-11 alone | A-6, A-7 |
| C-14 | drivers.serious_offenders | price_paid (basic cover) | U1-a: no_change; U1-b: decrease | short | invisible | B | U1-a: no new option (A-20 refuses them), no surcharge yet; U1-b: CR-1 op 2 and CR-4 (Office at $820 or less against $2,600) | A-1, A-20 |
| C-15 | drivers.serious_offenders | price_paid (basic cover plus surcharge) | U1-a: increase; U1-b: decrease | medium; long | invisible | B | U1-a: CR-1 op 3 (surcharge only); U1-b: CR-12e (arithmetic: $2,600 against at most $820 plus $105) | A-1, A-2, A-19, A-20 |
| C-16 | drivers.serious_offenders | informal_activity (uninsured driving) | U1-a: increase; U1-b: decrease | medium; long | invisible | B | CR-4 (x: uninsured, y: insure); U1-a: y made worse by the surcharge; U1-b: y made much better | A-2, A-8, A-20 |
| C-17 | drivers.high_risk | quantity_complement (vehicles owned) | increase | short; medium; long | invisible | B | CR-9 (relation: compulsory cover complement to a vehicle); CR-4 (x: no vehicle, y: vehicle; y cheaper); CR-11a (the uniform premium no longer conveys their risk) | A-1, A-9 |
| C-18 | drivers.low_risk | quantity_complement (vehicles owned) | decrease | medium; long | invisible | B | CR-4 (y: own a vehicle, made worse by the surcharge) | A-2, A-6, A-19 |
| C-19 | sellers.vehicles | quantity_traded (vehicles) | increase | short | invisible | B | CR-9 (complement), C-17 | A-1, A-9 |
| C-20 | sellers.vehicles | quantity_traded (vehicles) | ambiguous | medium; long | invisible | B | CR-12b: (+) C-17; (−) C-18; no dominance premise | A-2, A-6, A-9, A-19 |
| C-21 | drivers.metro (some) | legal_breach (garaging address misstated to the Office) | increase | short; medium; long | invisible | B | CR-4 (x: comply, y: give a cheaper region's address; the gain is up to $370 a year against weak checks) | A-1, A-10 |
| C-23 | drivers.renewing_late_2027 | term_prevalence (short-term policies bought in late 2027) | increase | short | invisible | B | CR-10a; CR-4 (x: annual policy running past 1 January 2028, y: short policy, then the Office) | A-1, A-12 |
| C-24 | sellers.private_insurers | asset_value (Lissmark books and capital) | decrease | short (from introduction) | invisible | B | CR-10c and CR-7c (expected yield of State-specific capital falls as passage becomes likely, from 10 January 2027); CR-7b (the loss settles on the capital that cannot move) | A-1, A-3, A-14 |
| C-25 | workers.private_insurers | employment | decrease | medium; long | invisible | B | CR-9 and LW-10 (relation: staff input_to private policies) | A-1, A-3, A-16 |
| C-26 | intermediaries.agents | earnings (commissions) | decrease | short; medium; long | invisible | B | CR-9 and LW-10 (relation: agents' services input_to private policies; switchers buy direct) | A-1, A-15 |
| C-27 | sellers.private_insurers | number_of_sellers | decrease | medium; long | invisible | B | CR-4 (x: stay in Lissmark basic liability, y: other lines or states); CR-7a | A-1, A-3, A-N1 |
| C-28 | sellers.private_insurers | compliance_cost (collecting and remitting the surcharge) | increase | medium; long | invisible | B | CR-1 op 3; CR-8c | A-2 |
| C-29 | officials.saio | enforcement_cost (running the Office) | increase | short; medium; long | invisible | B | CR-8a and CR-8c (staff and systems; about $74 a policy) | A-1 |
| C-30 | claimants.saio | wait_time (claims settlement) | increase | short | invisible | B | CR-9 (contract: the Office's policy pays them); CR-6 (0.7: claims capacity fixed by staff while the inflow rises; the gap is closed by waiting) | A-1, A-13 |
| C-31 | victims.of_previously_uninsured | resources_available_other_uses | increase | short; medium; long | invisible | B | CR-9 (contract: the new policy pays them); CR-8b; medium and long: CR-12b with dominance premise A-7 against C-12 | A-6, A-7, A-17 |
| C-32 | sellers.uninsured_motorist_cover | price_substitute (uninsured-motorist cover) | decrease | medium; long | invisible | B | CR-9 (relation: substitute); fewer uninsured drivers (C-13) lower expected claims; CR-7a (premiums follow cost under competition, A-N2) | A-6, A-7, A-N2 |
| C-33 | sellers.private_insurers, intermediaries.agents | lobbying_effort (to restrict or repeal the Office) | increase | short; medium; long | invisible | B | CR-4 (x: accept, y: lobby); CR-8c | A-11, A-14 |
| C-34 | drivers' and consumer groups | lobbying_effort (over the surcharge and statutory premiums) | increase | medium; long | invisible | B | CR-4 (x: accept, y: lobby); CR-8c | A-2, A-11 |
| C-35 | registrants.motor_vehicle_offices | wait_time | increase | short | invisible | C | CR-9 (0.7: shared_facility, Tier C pending Q20); policy sales added to fixed office capacity | A-1, A-N3 |
| C-36 | officials.saio | enforcement_cost (conviction-record checks) | U1-a: increase; U1-b: no_change | short; medium; long | invisible | B | CR-1 (U1-a: the Office must check before issuing); CR-8c | A-20 |
| C-39 | drivers.high_risk.switching | resources_available_other_uses | increase | short; medium; long | invisible | B | CR-8b (they receive what the reserves and the surcharge pay); medium and long: CR-12e arithmetic as C-2 | A-1, A-2, A-19 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-049-C1: Adverse selection. That only drivers whose expected claims exceed the uniform premium switch, so that the Office's pool is worse than average, was derived from CR-4 (each driver compares quotes) plus the actuary's figures (A-2). No core rule states that a uniform price offered to a population with known differences in cost draws the high-cost members; the derivation needs the premise that insurers' quotes track expected claims.
- GAP-049-C2: Care taken by Office policyholders (A-18). CR-4 and CR-11a give the direction (a premium not rated by record attaches no price to less care), but care, accidents and injuries are safety effects, out of scope for version 1. Only their effect on claims and the surcharge was traced.

**(b) Core-rule wording that was hard to apply.**
- CR-6 (0.9, public seller with an open quantity): it covers a public seller pricing for all buyers, but not one whose single price is below cost for some buyers and above cost for others; the split between price and quantity for rivals (A-3 against A-4) is then per risk class, not for the market as a whole.
- CR-12e arithmetic for C-2 holds for the class average; the rule's note on counts over a distribution suggests that the marginal switchers (quotes just above the switching line) may pay more. The class was signed on the average, and the note recorded.
- CR-8 (0.8, contingent payers): the surcharge is contingent on reserves falling below zero; the note asks for a premise or per-reading signs, and A-2 supplied it, but the rule does not say how to date a contingent payer's consequence.

**(c) Vocabulary missing from the ontology.**
- No variable for insurance claims or expected claims (used `price_paid (surcharge line)` and `tax_revenue` to carry them).
- No variable for vehicle ownership (used `quantity_complement (vehicles owned)`).
- No variable for the care taken by an insured party; it is a safety effect and out of scope.
- No variable for a public body's reserves other than `fund_balance`, whose counterfactual is undefined when the body does not exist without the policy.
