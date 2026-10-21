# WE-028 expand loop, blind run: notes

Read: section 1 of the example and the ID / Statement / Type / p columns of its assumption table only. Final engine output: DONE in 3 rounds, 19 questions, 15 nodes, 31 proposals (`situation.json`).

## Seed (policy's own facts, CR-1)

- Exchanges: `e_proc` (processing plants buy from vessel owners; 70% of landings), `e_fresh` (fish shops and restaurants buy from vessel owners; 30%), `e_shares` (quota shares and leases traded between owners), `e_crew` (owners and crew, paid by lay). Unsatisfied seller on both catch exchanges: `vessel_owners.shut_out` (owners who would land more than their tonnage).
- `capped` K1 on `e_proc` (wider_price true: output sold in the North Basin market) and `e_fresh` (wider_price false: sold at home), holders `vessel_owners` (K2 shares go to vessel owners). Premises a1 (A-1 binding 0.9) and a2 (A-2 enforcement 0.8) from the table.
- `means` K2 in for vessel_owners (shares given free).
- `charges`: K2 transfer fee 1% on `e_shares` (non_tax_receipts); K4 dockside fee 15 marks/t paid by sellers on `e_proc` and `e_fresh`; K3 on `e_crew` as a mandated term paid in kind to crew (non_wage_compensation) with quantity premise a_k3.
- `announced` K1 (a4 = A-4, 0.8). `compliance` K4 vessel_owners, `enforcers` K4 officials.enforcement, `funded` K4 taxpayers (a22 = A-22, 0.9).
- Answers from the table: a1, a2, a4, a22. Judged: a_k3 "Vessel owners cannot recover the crew's share of quota costs through the other terms of the crew contract." p 0.7 (near A-26, lay stays at 45%, 0.75, but not the same claim).

## Round 1 (9 nodes: buyers.fresh_fish, crew.ridge_cod, officials.enforcement, processors.ridge_cod, taxpayers, vessel_owners, vessel_owners.acquiring, vessel_owners.selling, vessel_owners.shut_out)

- buyers.fresh_fish: alternative (saithe and ling, A-25) and substitute links to `sellers.substitutes` price and quantity (A-25, A-16). Sentence: "Nearby fisheries for saithe and ling are open as well."
- crew.ridge_cod: stake in K3 (A-15), alternative job_changes (A-7).
- processors.ridge_cod: alternative of other species (judged premise), alternative of buying a vessel to hold shares (A-14), input link to processing workers (no premise), substitute links to foreign sellers' price (A-28) and quantity (A-29) and to North Basin buyers' price (A-28), asset and yield (A-18, A-19), stake (A-15).
- vessel_owners: outside margins discards (A-9, A-10), informal_activity (A-11), reclassification as saithe or ling (A-12); input links to crew employment/hours and to input suppliers' demand (trip expenses named in section 1); yield link from net price to crew wage_rate (lay, judged premise); cost link from lease price to acquirers (A-6); yield link from asset value to sales of shares (A-23); stake (A-15).
- vessel_owners.shut_out: alternative of other fisheries (A-7), outside margins (A-12, A-11), links from quantity to vessel asset_value and capital_stock_target (A-21).
- officials.enforcement, taxpayers, vessel_owners.acquiring, vessel_owners.selling: empty lists (nothing from section 1 or the table reaches anyone else; the fee and funding are already in the seed).
- Table answers: A-25 .7, A-16 .7, A-15 .85, A-7 .7, A-14 .6, A-28 .6, A-29 .6, A-18 .6, A-19 .7, A-9 .85, A-10 .75, A-11 .55, A-12 .35, A-6 .8, A-23 .8, A-21 .6. Judged: "The plants can replace some ridge cod with other species." 0.7 (A-19 says they cannot replace it fully, so partly); "Crew on most vessels are paid by the lay ..." 0.9 (section 1: standard contract on about 80% of vessels, 45% of trip revenue).

## Round 2 (5 nodes: buyers.north_basin, input_suppliers, sellers.foreign, sellers.substitutes, workers.processing)

- buyers.north_basin: alternative (close substitutes, A-17 .8 from the table) and an own-price link to its quantity demanded.
- sellers.substitutes: input link to `crew.other_fisheries` employment/hours (A-7).
- input_suppliers, sellers.foreign, workers.processing: empty (no sentence supports a further reach).

## Round 3 (1 node: crew.other_fisheries): empty. Depth limit reached.

## What the format could not hold

1. The race for catch history (K2 allocates by 2025 to 2027 landings; A-4). `timing` only has bring_forward / carry_over, and the sign follows whether the chooser is made better or worse. Owners are made better (holders), so bring_forward gives a decrease and carry_over an increase; neither means "land more now to qualify". I proposed no timing fact, so `announced` (A-4) is unused and the engine derives nothing for the announcement window. The claim-before-creation asset (A-5, A-3, CR-7c 0.7) also has no home: `asset` ties an owner to an exchange side and signs it from the cap, not from the date the formula became expected.
2. A market that exists only because of the policy (shares). The transfer fee is a charge, so the engine signs share trades down; against a counterfactual of no shares they are an increase (CR-12 0.9). I added a yield link from asset value to sales (A-23); the result is `vessel_owners.selling quantity_traded` ambiguous, which is an artifact of this, not a finding.
3. Per-holder limit (8% of shares, affiliates; A-13) and "only vessel owners may hold shares": `capped` fixes the quantity traded in an exchange; it cannot hold a limit on one holder's stock or a restriction on who may buy. Left out of the seed.
4. K3 and the two readings of U1 (lease payments in or out of "acquiring quota"): charges cannot carry readings; modelled as a mandated term to crew with one quantity premise. The receipt variable choice (non_wage_compensation rather than wage_rate) is a judgement, since the lay is crew pay.
5. Who pays the 1% transfer fee is not stated; payer_side buyer was an arbitrary choice and no `moves` were given (no premise or sentence on incidence).
6. A price in a wider market moved by an export fall: no relation takes a quantity change to a price change in another market. I used `substitute` (quantity down gives the other market's price and quantity up) for North Basin buyers' price and foreign sellers; `own_price` for buyers' demand.
7. `vessel_owners` is one class for sellers of catch, holders of shares, payers of the crew term and payers of fees, so `resources_available_other_uses` is ambiguous (free shares against fees and quota costs). Splitting by role would need `parts` and a dominance premise with figures the section does not give.
8. Opposing chains on prices of shares (fee, consolidation A-20, the 8% limit) and the lease price have no variable beyond `right_lease_price` for holders; the acquirers' price (`price_paid` on `e_shares`) is never moved because `moves` has no premise.
9. The `reclassification` outside margins (A-12, p .35) did not report (below the cut-off), as intended by the table.
