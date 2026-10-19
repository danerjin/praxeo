# Out-of-sample run of the prohibition rules on WE-053 (Corvany Personal Data Residency Act)

Rules as they were (`praxeo/rules/prohibition.lp`, written from WE-017 only; licensing rules for K3), handbook catalog 1.0 for the example. Record: `record.json`, two components: K1 as a `prohibition` of hosting abroad (bound `sellers.foreign`, buyers `firms.covered`, informal buyers `sellers.foreign.online`, `substitute_seller_actor` `firms.near_threshold` with `definition_line`, announcement window, general budget) and K3 as a `licensing_requirement` (bound `sellers.substitutes`, buyers `firms.covered`, general budget). K2 (officer and statement) has no instrument in the ontology (section 2.3) and is left out; K4 is carried by the enforcer, general-budget and fee facts. U1 (backups abroad) is an `unclear` entry with no `reading_fields`: neither reading changes a Component field, so both readings give the same engine run. Answers: `answers.json`, 9 of 17 from the assumption table (A-1, A-2 twice, A-8, A-12, A-13 twice, A-22, A-26), the other 8 judged from the text. Run: `python3 -m praxeo cases/we053_corvany --out cases/we053_corvany/sample_run` (verifier and citation problems empty). Key: (actor class, variable, sign, window). Test: `tests/test_oos_we053.py`. Nothing under `praxeo/` was changed.

Summary: the table has 41 rows (C-1 to C-41). The engine reports 23 consequences (31 derived; 8 unreported below the cut-off), which are 25 keys. Rows produced by key: 7 of 41 (C-6, C-9, C-14, C-19, C-31, C-34, C-35); C-19 and C-34 by key only (the mechanism is not the handbook's, see below). Rows not produced: 34. Engine keys classified: 8 in table, 6 defensible, **11 WRONG** (9 consequences).

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| sellers.foreign quantity_traded decrease | in table | C-6 |
| firms.near_threshold reclassification increase | in table | C-9 (RS-5 through `substitute_seller_actor`: the controllers near the line stand in for "sellers of goods just outside the definition"; a stretch of the role, the right row) |
| sellers.foreign lobbying_effort increase; sellers.substitutes lobbying_effort increase | in table | C-14 (the second from the licensing rules, the first from RS-7 on the bound sellers) |
| officials.enforcement enforcement_cost increase | in table | C-31 |
| sellers.substitutes compliance_cost increase | in table | C-35 |
| sellers.substitutes net_price_received increase | in table (by key only) | C-19. The engine gets it from EN-1 (licence holders gain from the restriction); the handbook gets it from the shifted demand (RS-16, CR-6) with the certificate (CR-4 0.8) as a second chain. Same sign, other mechanism |
| firms.covered resources_available_other_uses decrease | in table (by key only) | C-34 (staying above the line). The engine derives it from the licensing rules (the fee passed on), the handbook from CR-3 and CR-8a: the cost of compliance |
| firms.covered lobbying_effort increase | defensible | RS-7 on the buyers; section 5 names covered controllers among the interested parties (A-13); C-14 lists others |
| firms.covered price_paid increase | defensible | from K3 (buyers pay more where sellers are restricted); C-4 is the subclass `firms.covered.abroad` and the dearer local hosting (CR-6), so C-4 is not credited |
| firms.covered quantity_substitute increase | defensible | RS-1: they turn to local hosting; the table has C-2 and C-17 |
| firms.covered quantity_traded decrease | defensible | OC-4, the buyers' side of C-6 |
| sellers.foreign number_of_sellers decrease | defensible | EN-7; the table has the buyers' side (C-5, A-6) |
| sellers.substitutes share_of_sellers_licensed increase | defensible | EN-1; not in the table |
| **sellers.foreign.online search_cost increase; quality_variability increase; quality_information decrease; disputes_settled_outside_courts increase** | **WRONG** | RS-10 on "informal buyers". The only role that fits the foreign services that ignore the Act is the informal buyer, but the handbook says (C-13) their breach is "breach within a legal market, not informal trade" (`legal_breach`): no search cost, no quality uncertainty, no disputes outside courts. With the role left out the same four rows fall on `firms.covered` (the default informal buyers), also wrong |
| **sellers.substitutes employment decrease; number_of_sellers decrease; quantity_traded decrease; entry_rate decrease** | **WRONG** | EN-1 and EN-3 with OC-4 on K3 alone. K1 is the component that moves demand to local operators: C-2 has their quantity supplied increase, C-22 entry increase, C-38 staff increase, C-20 the number of facilities ambiguous. The licensing rules do not know that the certificate lands on sellers whose market the other component enlarges |
| **taxpayers, recipients.other_spending, taxpayers.future resources_available_other_uses at_least_one_decrease** | **WRONG** | OC-1 for the appropriation. C-32 is `ambiguous`: the same general budget receives the certificate fees (K3) and fines (C-33), and the appropriation is 6 million a year; no declared comparison, so the rule signs the cost alone |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 firms.covered compliance_cost | no | missing instrument (K2) and rule: no cost fixed per controller (CR-4 0.8) |
| C-2 sellers.substitutes quantity_supplied increase | no | missing rule: demand shifted to local sellers under a prohibition (CR-9, CR-6); the engine's quantity_traded decrease is WRONG |
| C-3 sellers.foreign investment_target | no | missing rule and variable: complying by building in Corvany (CR-4 0.8 per outlet) |
| C-4 firms.covered.abroad price_paid | no | missing record fact (the subclass) and the mechanism (CR-6) |
| C-5 firms.covered number_of_sellers decrease | no | missing rule: the buyers' side of the ban |
| C-6 sellers.foreign quantity_traded decrease | yes | |
| C-7 firms.covered quantity_traded (backups), per reading | no | the readings carry no engine facts; the engine has a plain decrease on hosting |
| C-8 firms.covered.local compliance_cost, per reading | no | subclass and reading; no rule |
| C-9 firms.near_threshold reclassification increase | yes | RS-5 through a stretched role |
| C-10 firms.near_threshold number_of_sellers increase | no | missing rule: RS-17 bunching below a notch |
| C-11 firms.below_threshold asset_value ambiguous | no | missing rule: RS-17 0.9 and CR-12b; no role |
| C-12 sellers.foreign.online quantity_supplied decrease | no | missing rule: CR-4 (0.8) per outlet, RS-6 |
| C-13 sellers.foreign.online legal_breach increase | no | missing rule: RS-4 0.9 (reach of enforcement) and the variable; the RS-10 rows are WRONG |
| C-14 lobbying_effort increase | yes (part) | sellers.substitutes and sellers.foreign; no role for firms.near_threshold |
| C-15 intermediaries quantity_traded (window) | no | missing role and rule: RS-8 with CR-12 (0.9) for activities that exist only under the policy |
| C-16 firms.covered.abroad quality_per_unit ambiguous | no | missing rule: CR-12b opposing chains |
| C-17 firms.covered price_substitute increase | no | missing rule: RS-16 per unit of quality, CR-6 splitting a shift |
| C-18 firms.covered price_substitute ambiguous | no | same, with CR-12e and RS-13 |
| C-19 sellers.substitutes net_price_received increase | yes (key only) | other mechanism (EN-1) |
| C-20 sellers.substitutes number_of_sellers ambiguous | no | the engine signs decrease (WRONG); no (+) chain |
| C-21 sellers.substitutes asset_value ambiguous | no | missing rule: CR-7c for the substitute sellers under a prohibition |
| C-22 sellers.prospective entry_rate increase | no | missing role and rule (entrants under a prohibition); the engine's decrease is on another class and WRONG |
| C-23 factor_owners.specific asset_value increase | no | missing rule: CR-9 inputs to the substitute (`related` is for taxes and subsidies only) |
| C-24 input_suppliers quantity_traded increase | no | same |
| C-25 input_suppliers employment increase | no | same (OC-5) |
| C-26 buyers price_paid / quantity (RS-14) | no | missing rule: downstream users of the banned input |
| C-27 buyers variety decrease | no | missing rule |
| C-28 sellers.domestic_digital quantity or price | no | missing role and rule (CR-6 rivals) |
| C-29 exporters ambiguous | no | missing rule: TX-8 for an import ban |
| C-30 neighboring_jurisdictions quantity_supplied decrease | no | the neighbour role signs a gain from crossing buyers; the loss of the bound sellers abroad has no separate role |
| C-31 officials.enforcement enforcement_cost increase | yes | |
| C-32 taxpayers etc. resources_available_other_uses ambiguous | no | contradicted: the engine signs at_least_one_decrease |
| C-33 state budget non_tax_receipts increase | no | missing rule and variable: licence fees to the general budget (CR-8b) |
| C-34 firms.covered resources_available_other_uses decrease | yes (key only) | other mechanism |
| C-35 sellers.substitutes compliance_cost increase | yes | |
| C-36 buyers quantity_traded decrease | no | missing rule (CR-5a, OC-4) |
| C-37 sellers.domestic_digital asset_value ambiguous | no | missing role and rule |
| C-38 workers.data_centers employment increase | no | missing rule: CR-9, LW-10 labor of the substitute sellers |
| C-39 sellers.foreign resources_available_other_uses decrease | no | missing rule: CR-8a investment drawn from elsewhere |
| C-40 sellers.substitutes net_price_received ambiguous (medium) | no | the engine's increase is C-19's sign; the medium-run chain is not encoded |
| C-41 neighboring_jurisdictions net_price_received decrease | no | missing rule: CR-9, CR-6 on the wider market |

## General gaps

Ranked by rows added or corrected.

1. **A prohibition that falls on a class of buyers, with a compliance route through local supply (a barrier to foreign suppliers, handbook section 2 and CR-1, CR-4, CR-6, CR-9, RS-16).** The prohibition rules sign the loss of the bound sellers and the underground trade, and nothing for the sellers of the substitute whose market the ban enlarges. A general rule would give them the shifted demand: `quantity_supplied` increase (C-2), the short-run price of the substitute when its supply is slow (RS-16 with CR-6; premise: free capacity is limited, A-16: C-17, C-19), entry (C-22), and, with `related` markets allowed on a prohibition as on a tax, the input and labor chains (CR-9: C-23, C-24, C-25, C-38). That is up to 8 rows added (C-2, C-17, C-19 by the right mechanism, C-22, C-23, C-24, C-25, C-38) and removes four WRONG keys if the licensing rules defer to it.
2. **Two components on the same sellers (CR-12 the chains of different components, final check (1)).** The K3 certificate was signed as if it were the only force on `sellers.substitutes` (employment, entry, number of sellers and quantity all decrease). Where another component of the record raises the demand for the same class, the combiner should join the two chains and sign the disputed variables `ambiguous` (C-20) or drop the licensing-only sign. Fixes 4 WRONG keys and gives C-20, C-21, C-40 their ambiguous signs.
3. **Breach within a legal market (CR-4, RS-4 0.9, and a `legal_breach` variable).** RS-10's consequences (search, quality variability, disputes outside the courts) should attach only to a trade that goes underground, not to buyers who simply ignore a rule that cannot reach them. The parser has no role for "controllers in breach", and `informal_buyer_actor` pulls them into the wrong rule. A general rule: where enforcement cannot reach a class (no establishment, no assets), derive `legal_breach` increase for it (C-13) and do not apply RS-10. Fixes 4 WRONG keys and adds C-13; C-12 (RS-6, CR-4 0.8) follows with a premise.
4. **Funding from a budget that receives the policy's own receipts (OC-1, 1.0; CR-8, 1.0).** OC-1 signs the payers' loss from the supplementary appropriation alone. Where the record says that fees or fines go to the same general budget, the group's sign should be `ambiguous` (C-32) and the receipts `non_tax_receipts` increase (C-33, CR-8b). Fixes 3 WRONG keys (one consequence) and adds C-33 and C-32.
5. **Fixed costs per firm and thresholds (CR-4 0.8, RS-17, RS-21).** A cost fixed per controller (K2, an officer and a statement) has no instrument; neither does the notch at 50,000 beyond the stretched RS-5 reuse. Adding the instrument `compliance_requirement` (named in the example's section 2 but not in the ontology) with CR-4 gives C-1; a threshold flag with RS-17 would give C-10, C-11 and the deletions of RS-21 in C-9. Up to 3 rows (C-1, C-10, C-11).
6. **Non-sale roles that a prohibition needs.** Entrants (`sellers.prospective`), the loss of the neighbours' sellers when buyers may no longer cross (`neighbor_seller` currently signs only gains: C-30, C-41), downstream users (RS-14: C-26, C-27, C-36) and the currency link (TX-8: C-29). Each is a role plus an existing handbook pattern; up to 6 rows.
7. **Readings that change no record field.** U1-a and U1-b differ only in whether backups are covered; with no `reading_fields` the engine runs the same record twice, so C-7 and C-8 (per-reading signs) cannot be produced. A general `scope` flag on the prohibition (copies included or not) would let a parser state it. 2 rows.

## After the rule changes (second commit)

General fixes from the out-of-sample runs on WE-018, WE-037, WE-044, WE-050 and WE-053 (`rules/prohibition.lp`): fewer legal sellers only where they cannot turn to other products (`no_other_use`); the underground trade needs the ban to be enforced; the risk price needs an underground trade; the buyers lobby only with their own premise (`buyers_organize`); buying across the boundary costs time only where it takes an extra trip (`crossing_extra_trip`); a ban on a practice of legal firms (`practice_ban`) makes evasion a legal breach, not an informal market; fees or fines paid into the budget that funds enforcement (`fees_to_budget`) leave the payers' net unsigned. The answers gained the two new questions. The record sets `practice_ban` and `fees_to_budget` (fees go to the general budget). Rows produced: 7 of 41 (unchanged). WRONG keys: 4 (was 11): left are the four rows on local hosting firms, which the facility license (K3) and the residency rule (K1) push in opposite directions; the engine has no comparison across components.
