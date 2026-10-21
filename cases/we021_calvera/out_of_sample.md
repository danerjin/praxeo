# Out-of-sample run of the subsidy rules on WE-021 (Calvera Rooftop Solar Incentive)

Rules as they were after the subsidy commit (`praxeo/rules/subsidies.lp`, developed on WE-019 only); nothing under `praxeo/` was changed. Record: `record.json`, two components. K1 is a `per_unit_subsidy` (recipients `buyers.adopters`, sellers `installers`, claim handler `installers`, enforcer `officials.enforcement`, payers `customers.electricity`; flags own-revenue funded, eligibility criteria, temporary, budget capped, announcement window; `other_buyer_actor` `buyers.commercial_solar` from the exclusion of commercial and ground-mounted systems). K2 is the surcharge, a `per_unit_tax` (bound and seller `utilities`, buyers `customers.electricity`, collector `officials.enforcement`, own-revenue funded, announcement window). The certification (K3) is folded into K1 as `eligibility_criteria` and the administration (K4) into the enforcer role; neither has an instrument of its own. `renewable` is false because the text says nothing of renewal. Answers: `answers.json`, from WE-021's assumption table (A-1 to A-18) for 11 of 14 questions; three judged from the text (`oversubscribed` 0.45, `quantity_responds` 0.85, `stockpile_ahead` 0.05). Run: `python3 -m praxeo cases/we021_calvera --out cases/we021_calvera/sample_run`. Test: `tests/test_oos_we021.py`. Key: (actor class, variable, sign, window).

Summary: the table has 33 rows (C-1 to C-33). The engine reports 21 consequences. Rows produced by key: 16 of 33 (48%); of these C-4, C-16 and C-21 by key with a different mechanism from the table's. Rows not produced: 17. Engine rows classified WRONG: 1. Verifier and citation problems: none.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| buyers.adopters price_paid decrease | in table | C-1 |
| buyers.adopters quantity_traded decrease, window announcement | in table | C-10 (RS-8) |
| installers quantity_traded increase | in table | C-2 |
| installers net_price_received increase | in table | C-5 (SB-2 with DM-1) |
| installers subsidy_share_received increase | in table | C-23 |
| installers quantity_traded decrease, window after_expiry | in table | C-18 (SB-6) |
| installers compliance_cost increase | in table | C-25 (claims, CR-8) |
| buyers.commercial_solar price_paid increase | in table | C-28 (through `other_buyer_actor`, see General gaps 7) |
| buyers.commercial_solar quantity_traded decrease | in table | C-29 |
| customers.electricity price_paid increase | in table | C-3 (TX-2) |
| customers.electricity resources_available_other_uses decrease | in table | C-4 (TX-1 and TX-2; SB-1 does not fire because the subsidy is own-revenue funded) |
| customers.electricity quantity_traded decrease | in table by key only | C-21 is the businesses' forgone purchases (OC-1); the engine's row is the buyers' side of the wedge (OC-4), which the handbook calls too small for an entry (A-3) |
| utilities quantity_traded decrease | in table by key only | C-16 is the loss of grid sales to adopters (A-2, A-10); the engine's row is the sellers' side of the surcharge's wedge |
| utilities compliance_cost increase | in table | C-26 (TX-5) |
| officials.enforcement tax_revenue increase | in table | C-24 |
| officials.enforcement enforcement_cost increase | in table | C-19 (OC-3) |
| buyers.adopters quantity_traded increase | defensible | the buyers' side of C-2 (an exchange has two sides); the same row is an exception in WE-019 |
| buyers.adopters reclassification increase | defensible | SB-5 with RS-5 for the criteria of K1 (residential rooftop line, certified installer, 10 kW); not in the table. The premise is weak: my answer for `qualifying_pays` used A-5, which is about installers' entry, while the rule puts the reshaping on the recipients |
| customers.electricity quantity_substitute increase | defensible | TX-3 with RS-1: customers turn to untaxed own generation (A-10); the table has only adopters' lower grid purchases (C-16) |
| officials.enforcement tax_revenue_vs_static_projection decrease | defensible | TX-9: revenue short of the static projection because the quantity falls; follows from `quantity_responds` and is trivial at 0.6% of the price |
| **installers net_price_received decrease, window after_expiry** | **WRONG** | SB-6 with CR-6 signs a price fall after expiry from `seller_supply_slow`. A-4 is a first-year premise; the handbook says labor supply grows (C-6), the subsidy shifts to buyers (section 8) and, by the end, entrants are many. The table has the fall in quantity (C-18) and ambiguous earnings (C-22), no price fall |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 buyers.adopters price_paid decrease | yes | |
| C-2 installers quantity_traded increase | yes | |
| C-3 customers.electricity price_paid increase | yes | the premise `quantity_responds` had to be answered high (0.85) for TX-2's wedge to carry it; see General gaps 6 |
| C-4 customers.electricity resources_available_other_uses decrease | yes | through TX-1, not SB-1 |
| C-5 installers net_price_received increase | yes | |
| C-6 installers entry_rate increase | no | missing rule: SB-3 with LW-4, the entry of sellers drawn by the higher price (A-5 has no question on the sellers' side) |
| C-7 buyers.adopters transaction_size increase | no | missing record fact and rule: the 10 kW limit per building has no field; CR-4 for unit size is not encoded for subsidies |
| C-8 buyers.adopters quantity_traded increase (before step-downs) | no | missing record fact and rule: the tiered payment that steps down with funded capacity; RS-8 is encoded for the announcement only |
| C-9 buyers.adopters wait_time increase | no | same as C-8; PC-2's group is not signed (oversubscribed 0.45) and is a different mechanism |
| C-10 buyers.adopters quantity_traded decrease (Sept to Dec, Year 0) | yes | |
| C-11 installers, panel_suppliers, large users lobbying_effort increase | no | missing record fact: no renewal in the text (renewable false); no roles for suppliers and large users |
| C-12 customers.non_adopters tax_share_borne increase | no | missing record fact (no role for payers who receive nothing) and rule (RS-1 with CR-1) |
| C-13 electricians wage_rate increase | no | missing record fact (no role for owners of the scarce factor) and rule |
| C-14 buyers.other_electrical_work price_paid increase | no | same (no role for buyers of the competing use) |
| C-15 panel_suppliers quantity_traded increase | no | missing record fact: no input-supplier role for subsidies |
| C-16 utilities quantity_traded decrease | yes (by key only) | different mechanism, see above |
| C-17 customers.non_adopters price_paid ambiguous | no | combiner (the + chain PC-15 against the - chain RS-13 is not a declared CR-12 comparison); neither rule is encoded; no role |
| C-18 installers quantity_traded decrease (after program ends) | yes | |
| C-19 officials.enforcement enforcement_cost increase | yes | |
| C-20 buyers.other_electrical_work quantity_traded decrease | no | same as C-14 |
| C-21 customers.electricity quantity_traded decrease | yes (by key only) | different mechanism, see above |
| C-22 installers (entrants) earnings ambiguous | no | combiner: DM-3 is not a declared comparison |
| C-23 installers subsidy_share_received increase | yes | |
| C-24 officials.enforcement tax_revenue increase | yes | |
| C-25 installers compliance_cost increase | yes | |
| C-26 utilities compliance_cost increase | yes | |
| C-27 installers asset_value increase | no | missing record fact: the text names no asset in slow supply (`asset_owner_actor`); the handbook gets there through A-4 and A-18 as analysis |
| C-28 buyers.commercial_solar price_paid increase | yes | depends on the `other_buyer_actor` choice |
| C-29 buyers.commercial_solar quantity_traded decrease | yes | same |
| C-30 generators.wholesale net_price_received decrease | no | missing record fact and rule: no role; RS-13 is not encoded |
| C-31 workers.installers employment, hours_worked at_least_one_increase | no | missing record fact (no worker role for subsidies) and rule (LW-4, CR-9, CR-7 for the subsidized sellers) |
| C-32 workers.installers employment, hours_worked at_least_one_decrease | no | same, with SB-6 for the fall after the program |
| C-33 buyers.adopters (inframarginal) resources_available_other_uses increase | no | missing rule: SB-1's receipt side; the engine signs the payers' cost only |

Not met at all: no row fell under "unsupported form" or "case-specific provision". K3 and K4 were absorbed into K1's flags and roles; the K3 compliance cost is produced as C-25 by CR-8c's claim handler, but not through OC-2 (seller-side criteria).

## General gaps

1. **Wrong row: SB-6's post-expiry price fall needs its own supply premise (handbook SB-6, CR-6, DM-1).** `seller_supply_slow` is asked once, for the start of the program. For a program longer than the lead time of supply (here five years against one year of labor scarcity) the premise at expiry is a different question. Fix: ask a separate premise for the end of the program ("is the sellers' supply still fixed when the subsidy ends?") and gate the `after_expiry` price fall on it, as the handbook's DM-3 and section 8 timing treat it. Affects 1 WRONG row; WE-019 (six-month program) would keep its row.
2. **Roles for the activity the subsidy draws on: owners of a scarce factor, competing buyers of it, and the factor's workers (SB-3 with RS-1, LW-4, CR-9).** One pattern gives C-13 (wage rate), C-14 and C-20 (competing buyers' price and quantity), C-31 and C-32 (workers' employment or hours), and with the worker role C-6's entry. Fix: add `factor_owner_actor`, `factor_buyer_actor` and `worker_actor` to the subsidy record, with an SB-3 rule that a subsidy-induced rise in demand for a scarce factor (a premise like A-12) raises its price, lowers competing uses and moves the group of workers. Adds up to 6 rows (C-13, C-14, C-20, C-31, C-32, C-6).
3. **Spillover roles and SB-1's receipt side (SB-1, DM-1, RS-1; SB-2).** Missing: the recipients' gain from the payment they receive without changing behavior (C-33, mirror of the payers' cost; CR-8b), the payers who receive nothing (C-12, `customers.non_adopters`), input suppliers to the subsidized good (C-15), the wholesale market (C-30 via RS-13). Fix: SB-1 signs `resources_available_other_uses` increase on the recipients (with takeup), `non_recipient_payer_actor` signs `tax_share_borne`, and subsidies take `input_supplier_actor` as tariffs do. Adds 3 rows (C-33, C-12, C-15); C-30 and C-17 also need RS-13 and PC-15.
4. **Step-down schedules and size limits as record facts (RS-8, CR-4, SB-2).** C-8 and C-9 (surges and backlogs at each threshold) and C-7 (systems sized to the limit) rest on a schedule of payments that falls with funded capacity and a per-unit limit; the schema has flags but no field for either. Fix: `payment_steps` (true when the rate falls at thresholds) and `unit_limit` (true when the payment stops at a size), with RS-8 applied at each step and CR-4 on the size. Adds 3 rows (C-7, C-8, C-9).
5. **Combiner declarations for ambiguous totals (CR-12; DM-3, PC-15 with RS-13).** C-17 and C-22 are ambiguous by construction. Fix: declare the comparisons (a medium-run grid-price total of a + chain and a - chain; entrants' earnings over the surge and the end), which needs the chains in gaps 2 and 3 first. Adds 2 rows (C-17, C-22).
6. **Premise wording and the tax wedge (TX-2).** `quantity_responds` is the wedge that C-3 needs, but the handbook's own A-3 says demand changes little; the answer had to be a judgment (0.85), so the pass-through row hangs on a premise the handbook does not state. Fix: for a tax whose burden is set by regulation (cost-recovery rates), let TX-2 sign the buyers' price rise from `buyers_bear` alone and keep `quantity_responds` for the quantity row. This secures C-3, not a new row.
7. **`other_buyer_actor` is read broadly.** I set it to `buyers.commercial_solar` from the exclusion of commercial systems, which gives C-28 and C-29 by the DM-1 and CR-4c chain. The role is defined as buyers of the same good who get no payment; the handbook's reason is competition for installer capacity (A-4), not the exclusion. Fix: the parser instruction should say whether excluded categories fill this role, or a separate role for competing buyers of the same sellers' capacity should exist. No row changes, but the two rows rest on a reading.
8. **Seller-side criteria (SB-5, OC-2).** K3 is a condition on the sellers, not the recipients. The reshaping row the engine reports (`buyers.adopters reclassification`) lands on the recipients; the table has the entry rate (C-6) and the compliance cost (C-25) instead. Fix: SB-5 should take the side the criteria bind (recipient or seller) and put RS-5 on that side, with OC-2's compliance cost on it. Affects the one defensible row and C-6.

## After the rule changes (second commit)

The record and answers changed only where a new field or question needs it (temporary payments: `ends_as_scheduled` and `supply_slow_at_expiry`; WE-021: `qualifier_actor`, `tax_named`; WE-033: the payer group's names; WE-056: K1's payer and its two PC-20 questions). Rows produced: 16 of 33 (unchanged). Engine rows WRONG: 0 (was 1). The installers' price after the program ends now rests on a premise about supply at that date (`supply_slow_at_expiry`, judged 0.3 from A-4 and A-5), not on supply at the start. The reshaping row is now on the installers (`qualifier_actor`; K3 binds them), not on the recipients.

## After related markets (third commit)

The record now lists the two inputs the policy text names (`related`, `rules/relations.lp`). One is electrical labour: certification needs a licensed electrician on staff. The other is panels: the payment is per watt of panel capacity. CR-9 signs both suppliers' sales up as installations rise (C-15 for panels). SB-3 with CR-7a signs the electricians' wage up where their supply is slow (A-12: C-13). Panel supply is not slow (A-11, p = 0.05). The other users of electrical work (C-14, C-20) are not named in the policy text, so the record cannot name them, although the rule exists. Rows produced: 18 of 33 (was 16).

## After the payer's side (fourth commit)

SB-1's receipt side (`rules/subsidies.lp`): the paying body's `subsidy_outlay`; what recipients receive (`resources_available_other_uses`, CR-8b); with penalties for false claims in the text (`claim_penalties`), false claims (RS-3, `false_claims`) and their recovery (`non_tax_receipts`, `claims_recovered`); and the other buyers' loss where sellers capture part of the payment. Rows produced: 19 of 33 (was 18): C-33 (adopters keep part of the subsidy, SB-1 with CR-8b). False claims stay below the cut-off (A-16, p = 0.2), as in the example.
