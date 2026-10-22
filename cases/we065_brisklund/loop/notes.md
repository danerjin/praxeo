# WE-065 Brisklund wheat deficiency payment: blind expand loop (notes)

Read: section 1 and the assumption table only. Nothing under handbook/05_examples*, tests/ or any existing cases/we065_brisklund file was opened.
Files: `seed.json`, `proposals.json`, `answers.json`, `situation.json` (final), `policy.txt` (section 1 copy for `--policy`).
Result: DONE in 3 rounds; 25 node visits (6 + 14 + 5); 19 questions (16 from the table, 3 judged); 5 more table premises sit in the seed.

## Seed (the policy's own facts)
- Exchange `e_wheat`: buyers / growers, `price_paid` / `net_price_received`. No held price, so no unsatisfied side.
- U1 as `unclear`: U1-a -> `k1a`, a `grant` to the seller side paid by `general_fund` (premises A-1, A-2; sentence: "Rate: Th 220 less the national average farm-gate price ..., if positive"). U1-b -> `k1b`, a `means` "in" for `growers.established` (the lump sum on established production no choice avoids).
- `moves` on the seller side (A-10, A-18): "The farm-gate price follows the export price less freight", and Brisklund is under 1% of world trade, so the sellers' price takes the payment.
- `enforcers` (k3, `officials.enforcement`), `compliance` (k3, growers: claims and declarations), `funded` k2 and k3 -> `taxpayers` (A-1: "paid out of the Consolidated Fund", "from its general appropriation").
- `announced` and `expires` on k1a and k1b with A-11 (known from February 2027, a term to 2032). A-11 is the nearest table premise; it is about land buyers, not the Act's end date.
- Not used: `qualifies` (the 2022-2026 history was fixed before the Act was expected, a windfall, not a race), `charges`, `capped`, `banned`, `held`, `incidence`, `fixed`, `thresholds`, `terms`.

## Round 1 (6 nodes: buyers, general_fund, growers, growers.established, officials.enforcement, taxpayers)
- growers: alternatives to the better option (barley/other crops, A-4; pasture conversion, A-13; price cover bought less, A-7; milling to feed variety, A-5, reading U1-a); outside margin `legal_breach` (A-6, U1-a); links: price -> quantity_supplied (A-3), price -> landlords' rent (A-14) -> tenants' rent paid (A-15) -> owners' asset_value (A-12), price -> borrowers' interest_rate (A-16), legal_breach -> fines (A-21); an `asset` for owners.farmland (A-11); stakes for unions (A-8); a dominance premise (claims cost far smaller than payments, judged).
- growers.established: part_of growers; U1-b alternative "land kept registered" with number_of_sellers as an inverse measure (A-19), and its link to quantity_supplied; U1-b capitalization of the lump sum into farm value (A-11 + a judged premise from "the holder (the person registered as farming the land)"); stake (A-8).
- buyers: link to exporters (A-10: extra output goes abroad); millers' stake (A-8).
- general_fund: spending paid_from its balance (no premise; "paid out of the Consolidated Fund").
- officials.enforcement, taxpayers: empty.

## Round 2 (14 nodes) and round 3 (5 nodes)
- exporters: world price falls for foreign buyers and sellers (supply relation, no premise: small effects are signed, "under 1% of world trade"); currency link to importers (A-17).
- growers.barley: fewer barley tonnes -> barley price_paid up for buyers.substitutes. growers#2: lower milling quality -> millers' price_paid up (no premise beyond the A-5 alternative).
- officials.enforcement#2: fines paid_into general_fund; general_fund#2: dominance, repayments and fines far smaller than payments (judged).
- Round 3: sellers.foreign price -> quantity_supplied (A-9); buyers.substitutes -> buyers quantity_demanded (A-20). Empty: borrowers.growers, buyers.millers, intermediaries, landlords, owners.farmland, owners.pasture, tenants, unions, buyers.foreign, importers, growers.established#2.
- Not proposed: tenants' rent -> their output (would pit a cost chain against A-3 with no dominance premise); effects of lower rates on borrowing and investment (no table premise); labor and input suppliers (not in section 1).

## Answers
From the table: A-1, A-2, A-10, A-11, A-18 (seed); A-3, A-4, A-5, A-6, A-7, A-8, A-9, A-12, A-13, A-14, A-15, A-16, A-17, A-19, A-20, A-21 (loop), each at its table p.
Judged (section 1 only): "The cost to growers of making claims and declarations is far smaller than the payments they receive." 0.9 (a claim against Th 160 million a low year over 18,000 farms); "The repayments and fines collected are far smaller than the payments made." 0.9 (3% sampling); "The payment on established production goes to the holder registered as farming the land, so the claim passes with the farm." 0.8 (the Act's own definition of the holder).

## Final engine output
Unconditional: growers compliance_cost, quantity_supplied and resources_available_other_uses increase; officials.enforcement enforcement_cost increase; owners.farmland asset_value increase; taxpayers resources decrease; unions lobbying_effort increase. Under U1-a only (none under U1-b): growers quantity_traded, net_price_received, legal_breach, quality_per_unit (decrease); general_fund outlay up and fund balance down; landlords and tenants rent up; barley quantity down and barley price up; exporters and importers up; foreign price and foreign growers' output down; interest rate down. U1-b only: growers.established means and lobbying up. The A-19 chain (p 0.35) is not reported; `growers number_of_sellers` is unreported.

## What the format could not hold
- A lump-sum payment has no payer side: under U1-b nothing records the outlay (`subsidy_outlay`) or the fund balance; `means` only moves the recipient's resources.
- Fines and repayments (A-21) are not a charge on trading: they enter only as a `same_act` link to `non_tax_receipts`, then `paid_into` the fund; the net against the outlay needs a dominance premise.
- Barley acreage, price cover, pasture land and milling quality have no variable of their own: `quantity_substitute`, `quality_per_unit`, `number_of_sellers` (inverse) stand in, carried by the actor name (`growers.barley`, `owners.pasture`). A-7 uses `intermediaries` as the seller of cover.
- No relation for "income up, so risk and rate down" (A-16): `cost` (price to price, opposite) was used. No relation for exchange-rate appreciation squeezing other exporters (A-17): only `currency` to imports.
- Land rent has no variable or exchange (`net_price_received` / `price_paid` stand in); later land buyers earning a normal return (CR-7c) cannot be stated; `qualifies` cannot express a history fixed before the Act was expected.
- One `premise_class` per proposal: A-12, A-15 and similar premises took the class of the proposal that first used them.
- A reading's chain that passes in the reading run can collapse the by-reading sign: `growers quantity_supplied` shows plain `increase` although under U1-b it rests only on the A-19 chain (p 0.35), whose assumption set sits among the alternatives.
- Tenants and owner-operators are not split: the payment goes to the holder, not the landowner, but the exchange side is one class `growers`.
