# Out-of-sample run of the existing rules on WE-005 (Corvane Emergency Fuel Price Order)

Rules as they were before any change (rule base `rb-thin-0.7`, handbook catalog 1.4). Record: `record.json`, one `price_ceiling` component (bound `stations`, protected `drivers.served`, excluded `drivers.unserved`, neighbour `drivers.brennick`, announcement window, funded from the general budget). Answers: `answers.json` (probabilities from WE-005's assumption table where a row exists; the rationale says which). Run: `python3 -m praxeo cases/we005_corvane --out cases/we005_corvane/sample_run`. Comparison key: (actor class, variable, sign, window), as in the WE-001 test.

Summary: the table has 26 rows (C-1 to C-26). The engine reports 20 consequences (the 3 resources entries are a total and its two items). Rows produced by key: 5 (C-1, C-2, C-15, C-21, C-26). Three more rows (C-4, C-6, C-7) are produced under another actor name (`drivers.unserved`, the record's excluded role; the table puts them on `drivers`). Rows not produced: 18 (including those three). Engine rows classified WRONG: 3.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| drivers.served price_paid decrease | in table | C-1 |
| stations net_price_received decrease | in table | C-2 |
| stations lobbying_effort increase | in table | C-15 |
| taxpayers resources_available_other_uses decrease | in table | C-21 |
| officials.enforcement enforcement_cost increase | in table | C-26 |
| drivers.unserved excess_demand increase | in table (actor name) | C-4; the table's actor is `drivers` |
| drivers.unserved search_cost increase | in table (actor name) | C-6 |
| drivers.unserved allocation_by_non_price_criteria increase | in table (actor name) | C-7 |
| stations maintenance_spending decrease | defensible | PC-4 signs it with quality_per_unit; C-8 describes closed restrooms and air pumps, which is maintenance; the table lists only quality |
| drivers.served quality_per_unit decrease | defensible | PC-4: the protected buyers receive less quality; the table records the same cut on the stations' side (C-8) |
| drivers.served resources_available_other_uses increase | defensible | CR-8b, the buyers keep what stations forgo (the mirror of C-2); the table does not list it |
| stations resources_available_other_uses decrease (total, item rent_forgone) | defensible | CR-8b, the sellers' side of C-1 and C-2; the table does not list it |
| drivers.served quality_adjusted_price ambiguous | defensible | the handbook treats price against quality as ambiguous (WE-001, unnumbered row); WE-005 records the corresponding comparison as full_cost_per_unit (C-23), with different chains |
| drivers.unserved side_payments increase | defensible | PC-6 with RS-3 gives side payments when evasion is possible (A-5); the table records the same trade as informal_activity (C-9) and as premiums in C-23 |
| drivers.unserved disputes_settled_outside_courts increase | defensible | RS-10 for the informal trade in cans (C-9, C-22); the table does not list the variable |
| drivers.served price_paid decrease, window first_months (comparison `first_months_price`) | defensible, but an artefact | same sign as C-1; WE-005 has no first-months row. The combiner forms the window row from the cap chain alone because the opposed chain (window_repricing, p 0.1) exists but is unreported |
| **drivers.brennick price_paid increase** | **WRONG** (weakest call) | RS-4 alone. The handbook prunes the Brennick price effect because it combines the pipeline diversion (more fuel in Brennick, PC-12/C-10) with the ambiguous C-17; the engine has only the buyers-arrive chain and signs an increase. The handbook gives no sign |
| **drivers.served lobbying_effort increase** | **WRONG** | RS-7 requires a gain concentrated on an identifiable group. Six million drivers are not (the table lists the stations only, C-15). The engine has one `can_organize` premise for both groups |
| **stations resources_available_other_uses increase (item key_money)** | **WRONG** | CR-8b with PC-6 gives the above-cap receipt to the bound seller. In WE-005 K2 bans surcharges at stations; the informal sales above the cap are resales of fuel in cans by individuals (C-9), not receipts of stations |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 drivers.served price_paid decrease | yes | |
| C-2 stations net_price_received decrease | yes | |
| C-3 drivers quantity_demanded increase | no | missing rule: PC-1 with LW-3 signs excess_demand only |
| C-4 drivers excess_demand increase | no (actor name) | produced for `drivers.unserved`; record names the excluded role differently |
| C-5 drivers wait_time increase | no | missing rule: PC-2's wait_time member has no question (the engine's comment says it is not signed) |
| C-6 drivers search_cost increase | no (actor name) | produced for `drivers.unserved` |
| C-7 drivers allocation_by_non_price_criteria increase | no (actor name) | produced for `drivers.unserved` |
| C-8 stations quality_per_unit decrease | no | the rules sign quality_per_unit on the protected buyers (`drivers.served`), not on the bound sellers; only maintenance_spending reaches the stations |
| C-9 drivers informal_activity increase | no | PC-6 informal_activity is encoded only in the sublet form (needs `nontransferable`), for the protected buyers |
| C-10 suppliers quantity_supplied decrease | no | missing rule PC-12 (a ceiling passes up to the inputs) and no suppliers role in the record |
| C-11 suppliers net_price_received decrease | no | missing rule PC-12 (price branch) |
| C-12 drivers quantity_demanded decrease (Days 3 to 5) | no | missing rule: RS-8 is encoded for sellers' repricing only; buyers waiting for the lower price is not |
| C-13 stations quantity_demanded decrease (Days 3 to 5) | no | same, with TS-7 for the stations' wholesale purchases |
| C-14 refiner.port_aldis maintenance_spending decrease | no | missing rule PC-12 with RS-6, and a role for the refiner |
| C-15 stations lobbying_effort increase | yes | |
| C-16 drivers.unserved quantity_substitute increase | no | missing rule: RS-1 for a ceiling (encoded for tariffs only) |
| C-17 drivers.border cross_border_purchases ambiguous | no | missing rule: RS-4 signs the neighbours' price, not the buyers' crossing; no combiner entry; no `drivers.border` role |
| C-18 stations (out of fuel) quantity_traded decrease | no | missing rule RS-9; station subclasses are not record facts |
| C-19 stations (with fuel) quantity_traded increase | no | same |
| C-20 drivers.unserved, suppliers quantity_traded decrease | no | OC-4 fires only through PC-5 on the bound role (alternative_uses p 0.15); the suppliers' chain is missing |
| C-21 taxpayers resources_available_other_uses decrease | yes | |
| C-22 drivers (buying in cans) quality_information decrease | no | RS-10 encoded for disputes_settled_outside_courts only |
| C-23 drivers full_cost_per_unit ambiguous | no | no rule or combiner entry for full_cost_per_unit |
| C-24 suppliers quantity_supplied (after Day 95) ambiguous | no | needs PC-12, RS-6 and RS-8 around the expiry date; none encoded |
| C-25 suppliers inventory_held increase | no | RS-8 with TS-7 around expiry is not encoded; no suppliers role |
| C-26 officials.enforcement enforcement_cost increase | yes | |

Two answers are judgement calls that change what the engine can show: `alternative_uses` (p 0.15, from A-15; WE-005's A-6 concerns cargo traders, not the bound stations) and `substitutes` (p 0.2; A-10's substitute is transit, a different market). With A-6 used for `alternative_uses`, the engine would report PC-5, RS-5 and OC-4 rows for the stations (supply falls, reclassification) that the handbook says are not reported.
