# WE-059 expand loop, blind run: notes

Read: handbook/04a_core_rules.md, praxeo/core/{core.lp,situation.py,expand.py}, handbook/02_ontology.md (variable and actor lists), the
we009/we013 situation records and the we036 loop (style), and section 1 of the WE-059 record (copied verbatim to `policy.txt`, with the
ID / Statement / Type / p columns of the assumption table appended).

Disclosure on the forbidden-reading rule: my first Read of the example used `limit 60` by mistake and returned lines 1 to 60, which is
past the end of section 1 (line 37). I therefore saw the title block and intro paragraph (lines 1 to 6: a list of the handbook rules and
notes the example probes, including that "prices per unit of quality" and "authorized repair as the substitute" matter) and lines 39 to 60
(the start of section 2: the classification table with its "Binding?" column and rule families, the "Who is bound" paragraph, and the
first rows of the section 3 actor-class table). I did not read anything else outside section 1 and the four allowed table columns, and I
did not use the "If false" / "Evidence" columns, the report, the consequence list, corrections, gaps, `05_examples_core/`, or any file under
`cases/we059_kestrava/` or `tests/` for this case (the directory did not exist in the worktree). I tried to ignore the extra lines. Where
they could have shaped a choice, I say so below (the "quality_adjusted_price" idea was set aside for `full_cost_per_unit`; the seed's use of
A-2 as the binding premise follows the table's own "binding" type, not the section 2 text; the actor-class names `dealers.ag`, `makers.ag`,
`makers.phone`, `independents.*`, `owners.*`, `authorized_providers.phone` were already in my head from section 1 and the task text, but
they match the section 3 names, so treat that overlap as contaminated).

Result: DONE in 3 rounds, 19 premise questions asked by the loop (all answered from the table or judged), 20 nodes in the proposals file
(10 with proposals, 10 answered empty), 51 proposals logged, 57 reported consequence lines and none unreported. Engine output is in
`situation.json` (the final run) and in the summary at the end of this file.

## Seed (CR-1, the Act's own facts), `seed.json`

- Exchanges (7): `e_ag_sale` (owners.ag buy covered farm equipment from makers.ag), `e_phone_sale` (owners.phone from makers.phone),
  `e_ag_parts` and `e_phone_parts` (independents buy parts, tools and software from makers; the independents are the unsatisfied buyers,
  section 1: "cannot buy the software"), `e_ag_terms` and `e_phone_terms` (the exchange in which an anti-repair term is agreed: makers buy
  the restriction, owners sell their freedom to repair), `e_phone_pairing` (the maker's authorization of a part to a device).
- K1 (mandated term) as a `charge` on the two sale exchanges: payer seller, receiver the buyer class (owners.ag, owners.phone), paid in
  kind (receipt `quality_per_unit`: access to repair inputs, which the vocabulary files under maintenance and service).
  `quantity_premises` A-1, A-2, A-25: the fall in sales is not a priori because the term is worth something to buyers (A-22), so it rests on
  the premise that cost to makers exceeds that worth (A-25) and that the term binds (A-2) and is complied with (A-1).
- `moves`: e_ag_sale buyer (A-18, list prices rise in Kestrava), e_ag_sale and e_phone_sale seller (A-6, makers bear the cost).
- `fixed`: e_phone_sale buyer, premise judged "Phone makers keep their prices the same in every state during the period" (p 0.7), from
  section 1: "at the same prices in every state". This sends the phone makers' recovery to the other terms they control (CR-6, CR-1 op 3).
  Not set for farm equipment, where A-18 has makers raising Kestrava list prices.
- K2 (void terms) as `banned` on the two term exchanges (premises A-2, and judged "Makers and dealers stop using terms that restrict repair
  once such terms are void", p 0.8).
- K3 and U1 as `unclear`: U1-a gives component `k3_a` (a ban on the pairing-authorization exchange, premise judged "Where pairing needs
  the maker's authorization, makers remove that need once pairing is forbidden", p 0.8); U1-b gives component `k3_b` (compliance only: the
  lock is lawful with an owner's tool, so no option is removed).
- `announced` k1, k2, k3_a, k3_b (passed 18 Feb 2027, effective 1 Sept 2028; premise judged "Makers and dealers expected the Act to take
  effect on 1 September 2028 once it was signed on 1 March 2027", p 0.9).
- Compliance: k1 makers.ag, makers.phone; k2 makers.ag, dealers.ag, makers.phone; k3_a and k3_b makers.phone. Enforcer k4:
  officials.enforcement. `fixed_budget` k4 (section 1: "No new appropriation ... budget ... unchanged"; premise judged "The Consumer
  Protection Division handles fewer of its other complaints when repair complaints take its time", p 0.7). No `funded`.
- Not in the seed: held (see "could not hold"), grants, capped, expires ("No expiry"), thresholds, qualifies, backstops, discretion, means,
  transfers, early_price.

Seed premises from the table: A-1 0.7, A-2 0.9, A-6 0.85, A-18 0.55, A-25 0.7. Judged: j_ann 0.9, j_nat 0.7, j_k2 0.8, j_k3 0.8, j_bud 0.7.

## Round 1 (depth 1): six nodes (dealers.ag, makers.ag, makers.phone, officials.enforcement, owners.ag, owners.phone)

Effects arriving: dealers.ag (compliance_cost +, resources -); makers.ag and makers.phone (compliance_cost +, net_price_received -,
quantity_traded -, resources -); officials.enforcement (enforcement_cost + and -); owners.ag (price_paid +, quality_per_unit +,
quantity_traded -); owners.phone (quality_per_unit +, quantity_traded -).

- makers.ag: alternatives to selling covered equipment as covered: reclassify compact tractors as grounds-care equipment (A-9; "designed
  primarily for agricultural use"); integrate components so parts are not separable (A-24); drop specialty models in Kestrava, measured
  as farms buying across the line (A-11; "14 specialty models sell fewer than 20 units a year"). Margin: recover the cost through other
  terms of sale, group quality_per_unit / variety (A-6). Margin outside the rule: legal_breach (A-10, enforcement on complaint only).
  Asset: investors.makers_ag asset_value (A-12, A-20) and yield: makers' return_on_capital (A-25). Stakes in k1 and k2 (A-23, "campaigns
  on both sides"). Link: makers' quantity_traded same_act dealers.ag (the dealers sell the makers' equipment: "four makers sell through
  140 authorized dealer locations").
- makers.phone: alternative: extend parts and tool programs to owners in all states (A-8), measured as quality_per_unit for
  owners.phone.other_states; integrate components (A-24). Margins: adjust (quality_per_unit / variety, A-6; the engine presses it
  because the buyer price is fixed), outside legal_breach (A-10), and trade in stolen parts outside the legal market under U1-a
  (A-17; actor intermediaries.stolen_parts, variable informal_activity). Asset/yield as for ag. Stakes in k1, k2 and k3_a (A-23).
- dealers.ag: stakes in k1 and k2 (A-23). Added at the same time because the node is visited again when makers' sales reach it
  (the proposals file is replayed at each visit, so these show at depth 1 in the log): asset (factor_owners.dealers, A-19 and A-20 through
  a yield link), dealers' return_on_capital (A-4, capacity cannot contract at once), input link to workers.dealers.
- owners.ag: alternative of buying new equipment from Darnholt dealers (judged: "Some farms within 30 km of the state line buy new
  equipment from Darnholt dealers when Kestrava prices are higher", p 0.65; section 1: 3,000 farms within 30 km and six dealers across the
  line); same_act link from quality_per_unit (access to inputs) to independents.ag quantity_traded (A-3 and A-5); timing: owners defer
  repairs until the Act binds (A-7); stakes in k1 and k2 (A-23).
- owners.phone: same_act link to independents.phone quantity_traded (A-3, A-5); timing (A-7).
- officials.enforcement: supply link from enforcement_cost to buyers.complainants wait_time (judged j_bud, section 1: 22,000 complaints a
  year on an unchanged budget).

Answers in round 1: A-9 0.55, A-24 0.55, A-11 0.5, A-6 0.85, A-10 0.7, A-12 0.85, A-20 0.8, A-25 0.7, A-23 0.85, A-8 0.6, A-17 0.65,
A-3 0.9, A-5 0.75, A-7 0.6 (all from the table); the Darnholt-dealers statement (0.65) judged.

## Round 2 (depth 2): three new nodes with proposals and six answered empty

New nodes reached: independents.ag and independents.phone (quantity_traded +), intermediaries.stolen_parts (informal_activity,
ambiguous by reading), buyers.complainants, factor_owners.dealers, investors.makers_ag, investors.makers_phone,
owners.phone.other_states, workers.dealers.

- independents.ag: input link to workers.independent_shops (employment, hours_worked as a group; A-5); substitute link to dealers.ag
  quantity_traded (A-3); supply links to owners.ag full_cost_per_unit (A-5) and wait_time (A-14: "average wait for a dealer technician at
  harvest at 2.5 days"); stakes k1, k2 (A-23, repair associations).
- independents.phone: input link to workers.independent_phone_shops (A-5); substitute link to authorized_providers.phone quantity_traded
  (A-3; $280 against $160); supply link to owners.phone full_cost_per_unit (A-5); input link to sellers.salvaged_parts (A-21); stakes.
- owners.ag, owners.phone (revisited): supply link from quality_per_unit to their own search_cost (A-16, owners "could not read fault codes
  or documentation before").
- intermediaries.stolen_parts: input link to sellers.stolen_phones informal_activity (judged: "Thieves steal more phones when the parts of
  stolen phones work in other devices", p 0.6; section 1: 40,000 phones stolen a year).
- Answered with an empty list: buyers.complainants, factor_owners.dealers, investors.makers_ag, investors.makers_phone,
  owners.phone.other_states, workers.dealers (terminal effects, nothing further the rules need).

Answers in round 2: A-19 0.75, A-4 0.75, A-14 0.75, A-16 0.85, A-21 0.6 (table); the theft statement 0.6 judged.

## Round 3 (depth 3): five nodes

authorized_providers.phone (quantity_traded -): yield link to its own return_on_capital (A-4); input link to
workers.authorized_providers; stake in k1 (A-23). Empty: sellers.salvaged_parts, sellers.stolen_phones (theft is a safety matter outside
version 1), workers.independent_phone_shops, workers.independent_shops. The run stops at depth 3; workers.authorized_providers (reached by
the last link) is never asked.

## Which answers came from the table and which were judged

Table (22 statements, 18 asked as loop questions and 4 in the seed): A-3 0.9, A-4 0.75, A-5 0.75, A-6 0.85, A-7 0.6, A-8 0.6, A-9 0.55, A-10 0.7, A-11 0.5, A-12 0.85, A-14 0.75,
A-16 0.85, A-17 0.65, A-19 0.75, A-20 0.8, A-21 0.6, A-23 0.85, A-24 0.55 (loop questions), and A-1 0.7, A-2 0.9, A-18 0.55, A-25 0.7 in the
seed. Judged from section 1 (7, five in the seed and two loop questions): seed j_ann 0.9, j_nat 0.7, j_k2 0.8, j_k3 0.8, j_bud 0.7; loop questions: Darnholt dealers 0.65, theft
0.6 (the Darnholt-dealers and theft statements are two of the 19 loop questions; the other 17 are table statements, and j_bud was reused from the seed).
A-11 sits exactly at the 0.5 cut-off and is reported; A-13 and A-15 and A-22 were not used (see below).

## What the format could not hold

1. K1 is a compelled sale at a price no worse than dealers' (a ceiling on the independents' price combined with a duty to supply). `held`
   would derive excess demand, fewer trades and a queue, the opposite of a duty to supply; so the independents' parts market has no
   operation of its own and appears only through links from owners' quality_per_unit. The parts price independents pay (their cost of
   inputs) and the part of the maker's margin lost on it are not derived.
2. K2 voiding existing contracts is a CR-8b transfer from makers/dealers to owners; `transfers` needs a held line, so none is recorded. The
   "exchange" for an anti-repair term has no price variable, and a ban on it also signs quantity_traded for the owner class (the term is
   not traded), which reads oddly for owners.
3. K3 is a rule on a product (CR-1 op 1 on a design choice), not a ban on a trade; it is carried as a ban on the pairing-authorization
   exchange, which signs quantity_traded for owners.phone and makers.phone under U1-a. Under U1-b nothing is removed, so k3_b carries only
   compliance. The differences between readings (what happens to non-genuine parts, stolen parts) have to be built from margins and links
   whose own conditions are not conditional on the reading (the outside margin for stolen parts needs the ban to be "on", so it does show
   per reading, which worked).
4. CR-11c information (A-15, used-phone buyers reading part notices; A-16 diagnostic information) has no part of the format. A-16 was
   forced into a `supply` link from quality_per_unit to search_cost; A-15 and the fall of a used-phone resale discount under U1-a could not
   be held and were left out. A-22 (buyers value access) is the reason the seed's quantity effect needs a premise; it has no fact of its own.
5. Dominance (A-25's balance) is a seed `quantity_premises` entry, not a `dominance` fact: dominance is proposable only for an actor and
   variable that is already ambiguous, and none of the ambiguous ones (owners.ag announcement window, cross_border_purchases,
   buyers.complainants wait_time, stolen-parts activity) has a premise in the table that settles it.
6. Alternatives with a `better` chooser: the receiving owners (K1 improves their option) and the same owners as buyers facing a higher price
   (A-18) are both choosers for an alternative they hold, so cross_border_purchases and the announcement-window quantity come out
   `ambiguous`; the engine cannot say that the price effect is the one that matters for the line-crossing choice.
7. `enforcement_cost` carries two effects, one up (the enforcer) and one down (other work gives way); a link from it propagates both, so
   buyers.complainants wait_time is `ambiguous` instead of rising.
8. Quality of the farm-equipment sales and repair markets share `quantity_traded` and `price_paid`/`full_cost_per_unit` across new
   equipment and repair (dealers.ag quantity_traded is both new-equipment sales and repair work); the format has no qualifier on variable.
9. A-13 (constant cost in the long run) and the lost dealer-service revenue figure ($100 million) are the kind of premise and arithmetic
   CR-12e uses for a price, but no price in the final run is both signed by opposing chains and reached by a premise of that form, so no
   `dominance` fact was proposed. A-15, A-22 unused as above.
10. Timing: owners' deferred repairs are signed on quantity_traded in the announcement window, the same variable as their equipment
    purchases (the window separates them).
11. Fixed vs moved prices: whether phone prices are fixed (j_nat) is a judgment from "same prices in every state"; `fixed` is not a
    proposable part, so it had to be decided in the seed before the loop could use A-8.

## Final engine output (57 lines, all reported)

See `situation.json` (run `python -m praxeo.core.expand cases/we059_kestrava/loop/seed.json cases/we059_kestrava/loop/proposals.json
cases/we059_kestrava/loop/answers.json --policy cases/we059_kestrava/loop/policy.txt` to print them). Signs of note: makers.ag and
makers.phone quantity_traded -, net_price_received -, compliance_cost +, return_on_capital -, reclassification +, lobbying_effort +;
owners.ag price_paid +, quality_per_unit +, quantity_traded -, full_cost_per_unit -, wait_time -, search_cost -; owners.phone
quality_per_unit +, quantity_traded -, full_cost_per_unit -, search_cost -, group (quality_per_unit, variety) at least one -;
independents.ag/phone quantity_traded +; dealers.ag and authorized_providers.phone quantity_traded -, return_on_capital -;
investors.makers_ag / makers_phone and factor_owners.dealers asset_value -; officials.enforcement enforcement_cost + and - (two items);
ambiguous: owners.ag cross_border_purchases, owners.ag quantity_traded (announcement), buyers.complainants wait_time,
intermediaries.stolen_parts informal_activity (U1-a +, U1-b none) and sellers.stolen_phones informal_activity.
