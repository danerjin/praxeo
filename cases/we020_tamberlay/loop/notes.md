# WE-020 expand loop, blind run: notes

Read: handbook/04a_core_rules.md, praxeo/core/{core.lp,situation.py,expand.py}, the cases we001/we009/we013 situation records, WE-020 section 1 and the ID/Statement/Type/p columns of its assumption table only. Nothing else of the example, no existing we020 case files.
`policy_s1.txt` is section 1 verbatim. `final_output.txt` is the last engine output. Assumption ids are `a<n>` for table row A-<n> (clingo needs lowercase atoms).

## Seed (CR-1, the policy's own facts)
- exchange `e_home`: buyers.first_time / sellers.entry_level_homes, price vars price_paid / net_price_received. No unsatisfied side (no held price).
- `grants`: K1, recipient side buyer, payer state_budget, outlay subsidy_outlay.
- `moves`: seller side (a2, slow supply), buyer side (a1, price rise smaller than grant). Both from the table, since the wedge must show on both prices.
- `expires` K1 (a15, "not renewed after Year 4", p 0.4 so below cut-off); `announced` K1 (a5, buyers knew from March).
- `compliance` K2 (buyers.first_time, sworn declarations); `enforcers` K4 (officials.enforcement); `funded` K1 by taxpayers (general revenue, no premise).
- Not seeded: held / capped / banned / charges / means (none fits, see "format could not hold").
- Seed assumptions: a1, a2, a5, a15 (all table values).

## Round 1 (5 nodes, 15 questions)
Nodes: buyers.first_time, officials.enforcement, sellers.entry_level_homes, state_budget, taxpayers.
- buyers.first_time (10 proposals):
  - link substitute to landlords.entry_level (renters buy sooner, A-4);
  - alternatives: Lowen suburbs (A-12), buying above the cap (A-20), moving jobs within 24 months (A-9, the clawback/occupancy condition);
  - timing bring_forward twice: A-5 (hold back until July) and A-16 (sign earlier near the deadline);
  - stake (lobby for renewal, judged);
  - link to agents.real_estate (A-21);
  - links same_act to buyers.prior_owners (A-7, declarations) and investors.nominee (A-14).
- sellers.entry_level_homes (7): timing (A-6); link yield to landlords.entry_level (A-13) and developers.investment_target (A-10); link output to buyers.ineligible price_paid (judged "same market"); asset for owners.entry_level_homes (A-3, A-2); yield for developers (A-2); stake (A-17).
- officials.enforcement, state_budget, taxpayers: empty (nothing in section 1 or the table to say what they do next).

## Round 2 (8 nodes, 8 new questions)
Nodes reached: agents.real_estate, buyers.ineligible, buyers.prior_owners, developers, landlords.entry_level, owners.entry_level_homes, sellers.homes_above_cap, sellers.lowen_suburb_homes.
- agents.real_estate: stake (A-17).
- buyers.ineligible: own_price link to own quantity_traded (judged margin premise); alternative Lowen (A-12); stake (judged, diffuse).
- developers: input link to workers.construction wage_rate (A-11); stake (A-17).
- owners.entry_level_homes: yield link to own resources_available_other_uses (A-19); complement link to sellers.homes_above_cap net_price_received (A-18); stake (A-17).
- sellers.homes_above_cap: supply_price link (judged "supply above the cap slow"); substitute link to side_payments (A-8).
- sellers.lowen_suburb_homes: supply_price link (judged "Lowen supply slow").
- buyers.prior_owners, landlords.entry_level: empty. For landlords the rental market has demand falling (renters buy) and supply falling (landlords sell); no relation signs rent, so nothing proposed.

## Round 3 (1 node)
- workers.construction (wage_rate up): cost link to developers.other_segments investment_target (A-11, same statement as round 2).

## Answers
From the table (p as in the table): A-3 .75, A-4 .85, A-6 .55, A-7 .6, A-8 .6, A-9 .7, A-10 .65, A-11 .8, A-12 .7, A-13 .7, A-14 .3, A-16 .7, A-17 .85, A-18 .6, A-19 .75, A-20 .7, A-21 .85 (seed: a1 .7, a2 .85, a5 .85, a15 .4).
Judged from section 1 (no table row):
- First-time buyers can organize to lobby at a cost below their stake: .6 (renewal is open and review is in Year 3, but buyers are diffuse).
- Buyers of entry-level homes who receive no grant buy in the same market as grant recipients: .9 (60,000 sales a year, a third under $450k, only 18,000 by first-time buyers).
- Some buyers who receive no grant are at the margin between buying and renting: .8.
- Buyers who receive no grant can organize to lobby at a cost below their stake: .3 (diffuse, unorganised).
- The supply of homes above the cap responds slowly: .85 (the section 1 permit and build times apply to all homes).
- The supply of homes in Lowen's suburbs responds slowly: .8 (same reasoning; section 1 states it for Tamberlay only).

## Result
3 rounds, 14 nodes, 23 questions asked of the decider (4 seed assumptions besides). Final engine output is in `final_output.txt`; situation in `situation.json`.
Not reported (below cut-off): after_expiry decreases (a15 p .4), investors.nominee informal_activity (a14 p .3), buyers.ineligible lobbying (.3).
Ambiguous: sellers.homes_above_cap net_price_received, sellers.lowen_suburb_homes net_price_received and quantity_traded (opposing chains from the engine).

## What the format could not hold
1. Eligibility cap ($450,000, fixed in money terms): it is a notch on the exchange (grant only below the price), not a held price, cap or ban. No field for a threshold on the grant, so the bunching under the cap, the pull of buyers from above-cap homes and the "value moved outside the contract price" (A-8) are carried only by hand-made alternatives and links (the substitute link to side_payments is a stretch).
2. Clawback of the grant if the buyer does not occupy for 24 months: a repayment attached to the option of moving. Charges attach to trading in an exchange, not to a later act. I used a job_changes alternative (A-9), whose sign (decrease) comes from "grant makes the bundle better", not from the clawback.
3. Evasion that the grant creates (false declarations, nominee buyers): alternatives for a "better" chooser always decrease; evasion needs an increase. I used same_act links from first-time buyers' purchases to the evaders' informal_activity.
4. Supply response: developers' investment rise cannot be turned into more homes and so a smaller price rise (A-1); the link relations carry no quantity-to-price fall, and the loop would be a response-argument case. The offsetting chain is missing.
5. Rental market: renters leaving (demand falls) and landlords selling (supply falls) both lower landlords' quantity_traded; no way to record that rent is then ambiguous, or the loss of rental supply to tenants.
6. Fixed appropriation (about $300m, 20,000 grants) with the law silent on excess applications: `fixed_budget` is for an enforcer's other work. Rationing of grants (a queue or first-come) cannot be stated; `discretion` is for case-by-case grants.
7. One timing fact per mode: the announcement hold-back (A-5) and the deadline rush (A-16) are different acts but both are bring_forward on quantity_traded, so I proposed two facts; each also feeds the after-expiry drop.
8. Atoms for assumptions must be lowercase: table ids A-n were recorded as a<n>.
9. The seeded `moves` on both sides each carry one table premise; the table gives no premise for "buyer side takes the change" as such.
