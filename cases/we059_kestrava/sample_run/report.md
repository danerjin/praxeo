# Thin-slice run: Kestrava Fair Repair Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T20:21:06+00:00
Prediction log sha256 (frozen before the outcome card was opened): `2f3a81ffe49cdb6b…`

## Policy record

- Rule-maker: the Kestrava legislature; enacted 1 March 2027, effective 1 September 2028.
- Stated aim: none stated
- k1a: mandated_contract_term on farm_equipment_repair_inputs in kestrava_farm_equipment; binds makers.ag, protects None. Source: "K1, duty to supply (a mandated term of every sale of covered equipment, owed to the owner and to any independent repair provider)."
- k1p: mandated_contract_term on phone_repair_inputs in kestrava_phones; binds makers.phone, protects None. Source: "K1, duty to supply (a mandated term of every sale of covered equipment, owed to the owner and to any independent repair provider)."
- k2a: term_prohibition on farm_equipment_sale_terms in kestrava_farm_equipment; binds makers.ag, protects None. Source: "K2, void terms."
- k2d: term_prohibition on farm_equipment_sale_terms in kestrava_farm_equipment; binds dealers.ag, protects None. Source: "K2, void terms."
- k2p: term_prohibition on phone_sale_terms in kestrava_phones; binds makers.phone, protects None. Source: "K2, void terms."
- k3a: product_standard on farm_equipment_software in kestrava_farm_equipment; binds makers.ag, protects None. Source: "K3, software locks (a rule on the software of covered equipment, binding makers)."
- k3p: product_standard on phone_software in kestrava_phones; binds makers.phone, protects None. Source: "K3, software locks (a rule on the software of covered equipment, binding makers)."
- Unclear U1: §5(c) forbids "a software lock to prevent the functioning of a part supplied, repaired or replaced in accordance with this Act". §2(f): "'Software lock' means any technical measure that restricts the functioning of a part unless the manufacturer authorizes it." Readings: U1-a: pairing that needs the maker's authorization is itself the lock §5(c) forbids; any part installed, genuine, salvaged or non-genuine, must work fully without contacting the maker, and makers must remove pairing from covered devices and leave it out of new ones / U1-b: §3(a)(iv) presupposes that pairing continues; a lock is lawful if the owner (or a repairer acting for the owner) can pair a genuine part using a tool the maker supplies on fair and reasonable terms
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1a)` | binding | 0.90 | The term was absent from some contracts, so the mandate binds for them. |
| `enforced(k1a)` | enforcement | 0.70 | Most bound providers comply. |
| `worth_less(k1a)` | other | 0.60 | The term is worth less to the marginal recipient than it costs the provider. |
| `can_organize(k1a)` | other | 0.85 | The bound providers can organize to lobby. |
| `recipients_organize(k1a)` | other | 0.85 | The recipients can organize to lobby. |
| `reshaping_pays(k1a)` | other | 0.55 | Reshaping goods to fall outside the definitions costs some actors less than the burden. |
| `complaint_unlikely(k1a)` | enforcement | 0.60 | Complaints are unlikely from some recipients. |
| `complaints_filed(k1a)` | enforcement | 0.70 | Complaints are filed in meaningful numbers. |
| `contested_otherwise(k1a)` | other | 0.80 | The groups that gain from or are bound by the measure would have lobbied on the same question without it. |
| `binding(k1p)` | binding | 0.90 | The term was absent from some contracts, so the mandate binds for them. |
| `enforced(k1p)` | enforcement | 0.70 | Most bound providers comply. |
| `worth_less(k1p)` | other | 0.60 | The term is worth less to the marginal recipient than it costs the provider. |
| `can_organize(k1p)` | other | 0.85 | The bound providers can organize to lobby. |
| `recipients_organize(k1p)` | other | 0.30 | The recipients can organize to lobby. |
| `conditions_differ(k1p)` | other | 0.20 | Some existing policies offer the term on conditions the mandate forbids. |
| `compete_with_bound(k1p)` | substitutability | 0.90 | The unbound firms compete with the bound providers. |
| `complaint_unlikely(k1p)` | enforcement | 0.70 | Complaints are unlikely from some recipients. |
| `complaints_filed(k1p)` | enforcement | 0.70 | Complaints are filed in meaningful numbers. |
| `contested_otherwise(k1p)` | other | 0.80 | The groups that gain from or are bound by the measure would have lobbied on the same question without it. |
| `binding(k2a)` | binding | 0.90 | The term was in use. |
| `substitute_terms(k2a)` | substitutability | 0.80 | Lawful substitute terms give part of the same protection. |
| `can_organize(k2a)` | other | 0.85 | The parties that used the term can organize to lobby. |
| `contested_otherwise(k2a)` | other | 0.80 | The groups that gain from or are bound by the measure would have lobbied on the same question without it. |
| `binding(k2d)` | binding | 0.90 | The term was in use. |
| `substitute_terms(k2d)` | substitutability | 0.40 | Lawful substitute terms give part of the same protection. |
| `can_organize(k2d)` | other | 0.85 | The parties that used the term can organize to lobby. |
| `contested_otherwise(k2d)` | other | 0.80 | The groups that gain from or are bound by the measure would have lobbied on the same question without it. |
| `binding(k2p)` | binding | 0.90 | The term was in use. |
| `substitute_terms(k2p)` | substitutability | 0.80 | Lawful substitute terms give part of the same protection. |
| `can_organize(k2p)` | other | 0.85 | The parties that used the term can organize to lobby. |
| `contested_otherwise(k2p)` | other | 0.80 | The groups that gain from or are bound by the measure would have lobbied on the same question without it. |
| `binding(k3a)` | binding | 0.80 | The standard binds on some designs. |
| `enforced(k3a)` | enforcement | 0.70 | Most makers comply. |
| `can_organize(k3a)` | other | 0.85 | The makers can organize to lobby. |
| `buyers_value_standard(k3a)` | other | 0.70 | Buyers value the standard enough to prefer covered units. |
| `stock_competes(k3a)` | substitutability | 0.70 | Existing units compete with new ones. |
| `contested_otherwise(k3a)` | other | 0.80 | The groups that gain from or are bound by the measure would have lobbied on the same question without it. |
| `binding(k3p)` | binding | 0.80 | The standard binds on some designs. |
| `enforced(k3p)` | enforcement | 0.70 | Most makers comply. |
| `can_organize(k3p)` | other | 0.85 | The makers can organize to lobby. |
| `buyers_value_standard(k3p)` | other | 0.70 | Buyers value the standard enough to prefer covered units. |
| `stock_competes(k3p)` | substitutability | 0.60 | Existing units compete with new ones. |
| `contested_otherwise(k3p)` | other | 0.80 | The groups that gain from or are bound by the measure would have lobbied on the same question without it. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.prospective | price_paid | increase | short+ | B | EN-14 | {binding(k3a), enforced(k3a)} or {binding(k3p), enforced(k3p)} | yes |
| C-2 | buyers.prospective | specification_level | increase | short+ | B | EN-14 | {binding(k3a), enforced(k3a)} or {binding(k3p), enforced(k3p)} | yes |
| C-3 | dealers.ag | asset_value | decrease | short+ | B | CR-8 | {binding(k2d)} | yes |
| C-4 | dealers.ag | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k2d), can_organize(k2d)} | yes |
| C-5 | dealers.ag | lobbying_effort (policy_field) | ambiguous | medium+ | B | RS-7 | {binding(k2d), can_organize(k2d), contested_otherwise(k2d)} | yes |
| C-6 | dealers.ag | resources_available_other_uses | decrease | short+ | B | CR-8 | {binding(k2d)} | yes |
| C-7 | dealers.ag | term_prevalence | increase | short+ | B | PC-18 | {binding(k2d), substitute_terms(k2d)} | no |
| C-8 | makers.ag | asset_value | decrease | short+ | B | CR-8 | {binding(k2a)} | yes |
| C-9 | makers.ag | compliance_cost | increase | short+ | A | EN-14, OC-2 | {} | yes |
| C-10 | makers.ag | legal_breach | increase | short+ | B | RS-20 | {binding(k1a), complaint_unlikely(k1a)} | yes |
| C-11 | makers.ag | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k2a), can_organize(k2a)} or {binding(k1a), can_organize(k1a)} or {binding(k3a), can_organize(k3a)} | yes |
| C-12 | makers.ag | lobbying_effort (policy_field) | ambiguous | medium+ | B | RS-7 | {binding(k3a), can_organize(k3a), contested_otherwise(k3a)} or {binding(k1a), can_organize(k1a), contested_otherwise(k1a)} or {binding(k2a), can_organize(k2a), contested_otherwise(k2a)} | yes |
| C-13 | makers.ag | quantity_supplied | ambiguous | medium+ | B | EN-14 | {binding(k3a), enforced(k3a)} | yes |
| C-14 | makers.ag | reclassification | increase | medium+ | B | RS-5 | {binding(k1a), enforced(k1a), reshaping_pays(k1a)} | yes |
| C-15 | makers.ag | resources_available_other_uses | decrease | short+ | B | CR-8 | {binding(k2a)} | yes |
| C-16 | makers.ag | term_prevalence | increase | short+ | B | PC-18 | {binding(k2a), substitute_terms(k2a)} | yes |
| C-17 | makers.phone | asset_value | decrease | short+ | B | CR-8 | {binding(k2p)} | yes |
| C-18 | makers.phone | compliance_cost | increase | short+ | A | EN-14, OC-2 | {} | yes |
| C-19 | makers.phone | legal_breach | increase | short+ | B | RS-20 | {binding(k1p), complaint_unlikely(k1p)} | yes |
| C-20 | makers.phone | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k1p), can_organize(k1p)} or {binding(k2p), can_organize(k2p)} or {binding(k3p), can_organize(k3p)} | yes |
| C-21 | makers.phone | lobbying_effort (policy_field) | ambiguous | medium+ | B | RS-7 | {binding(k2p), can_organize(k2p), contested_otherwise(k2p)} or {binding(k3p), can_organize(k3p), contested_otherwise(k3p)} or {binding(k1p), can_organize(k1p), contested_otherwise(k1p)} | yes |
| C-22 | makers.phone | quantity_supplied | ambiguous | medium+ | B | EN-14 | {binding(k3p), enforced(k3p)} | yes |
| C-23 | makers.phone | resources_available_other_uses | decrease | short+ | B | CR-8 | {binding(k2p)} | yes |
| C-24 | makers.phone | term_prevalence | increase | short+ | B | PC-18 | {binding(k2p), substitute_terms(k2p)} | yes |
| C-25 | makers.phone.matching | compliance_cost | increase | short+ | B | PC-17 | {conditions_differ(k1p), enforced(k1p)} | no |
| C-26 | makers.phone.matching | quantity_supplied | increase | medium+ | B | PC-17, CR-12, CR-2, CR-9 | {binding(k1p), compete_with_bound(k1p), enforced(k1p), worth_less(k1p)} | yes |
| C-27 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |
| C-28 | owners.ag | compliance_cost | increase | short+ | B | OC-2 | {complaints_filed(k1a)} | yes |
| C-29 | owners.ag | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k1a), recipients_organize(k1a)} | yes |
| C-30 | owners.ag | lobbying_effort (policy_field) | ambiguous | medium+ | B | RS-7 | {binding(k1a), contested_otherwise(k1a), recipients_organize(k1a)} | yes |
| C-31 | owners.ag | non_wage_compensation | increase | short+ | B | PC-17 | {binding(k1a), enforced(k1a)} | yes |
| C-32 | owners.ag | resources_available_other_uses | increase | short+ | B | CR-8 | {binding(k2a)} or {binding(k2d)} | yes |
| C-33 | owners.ag.exempt | asset_value | ambiguous | medium+ | B | EN-14, CR-7 | {binding(k3a), buyers_value_standard(k3a), enforced(k3a)} or {binding(k3a), enforced(k3a), stock_competes(k3a)} | yes |
| C-34 | owners.ag.exempt | stock_age | ambiguous | long | B | EN-14, CR-7 | {binding(k3a), buyers_value_standard(k3a), enforced(k3a)} or {binding(k3a), enforced(k3a), stock_competes(k3a)} | yes |
| C-35 | owners.phone | compliance_cost | increase | short+ | B | OC-2 | {complaints_filed(k1p)} | yes |
| C-36 | owners.phone | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k1p), recipients_organize(k1p)} | no |
| C-37 | owners.phone | lobbying_effort (policy_field) | ambiguous | medium+ | B | RS-7 | {binding(k1p), contested_otherwise(k1p), recipients_organize(k1p)} | no |
| C-38 | owners.phone | non_wage_compensation | increase | short+ | B | PC-17 | {binding(k1p), enforced(k1p)} | yes |
| C-39 | owners.phone | resources_available_other_uses | increase | short+ | B | CR-8 | {binding(k2p)} | yes |
| C-40 | owners.phone.exempt | asset_value | ambiguous | medium+ | B | EN-14, CR-7 | {binding(k3p), buyers_value_standard(k3p), enforced(k3p)} or {binding(k3p), enforced(k3p), stock_competes(k3p)} | yes |
| C-41 | owners.phone.exempt | stock_age | ambiguous | long | B | EN-14, CR-7 | {binding(k3p), buyers_value_standard(k3p), enforced(k3p)} or {binding(k3p), enforced(k3p), stock_competes(k3p)} | yes |

## Explanations

- C-1. Compared with no Kestrava Fair Repair Act, price paid for buyers.prospective rises from the short run onward (tier B, invisible). Why: EN-14: EN-14. This holds if: The standard binds on some designs (p = 0.80); Most makers comply (p = 0.70). It also follows under 1 other minimal assumption set(s). Reported.
- C-2. Compared with no Kestrava Fair Repair Act, specification level for buyers.prospective rises from the short run onward (tier B, visible). Why: EN-14: EN-14. This holds if: The standard binds on some designs (p = 0.80); Most makers comply (p = 0.70). It also follows under 1 other minimal assumption set(s). Reported.
- C-3. Compared with no Kestrava Fair Repair Act, asset value for dealers.ag falls from the short run onward (tier B, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The term was in use (p = 0.90). Reported.
- C-4. Compared with no Kestrava Fair Repair Act, lobbying effort for dealers.ag rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was in use (p = 0.90); The parties that used the term can organize to lobby (p = 0.85). Reported.
- C-5. Compared with no Kestrava Fair Repair Act, lobbying effort (policy field) for dealers.ag may move either way from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was in use (p = 0.90); The parties that used the term can organize to lobby (p = 0.85); The groups that gain from or are bound by the measure would have lobbied on the same question without it (p = 0.80). Reported.
- C-6. Compared with no Kestrava Fair Repair Act, resources available other uses for dealers.ag falls from the short run onward (tier B, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The term was in use (p = 0.90). Reported.
- C-7. Compared with no Kestrava Fair Repair Act, term prevalence for dealers.ag rises from the short run onward (tier B, invisible). Why: PC-18: PC-18. This holds if: The term was in use (p = 0.90); Lawful substitute terms give part of the same protection (p = 0.40). Not reported: an assumption is below the 0.5 cut-off.
- C-8. Compared with no Kestrava Fair Repair Act, asset value for makers.ag falls from the short run onward (tier B, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The term was in use (p = 0.90). Reported.
- C-9. Compared with no Kestrava Fair Repair Act, compliance cost for makers.ag rises from the short run onward (tier A, invisible). Why: EN-14: EN-14; OC-2: OC-2. This holds if: no assumption. Reported.
- C-10. Compared with no Kestrava Fair Repair Act, legal breach for makers.ag rises from the short run onward (tier B, invisible). Why: RS-20: RS-20. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); Complaints are unlikely from some recipients (p = 0.60). Reported.
- C-11. Compared with no Kestrava Fair Repair Act, lobbying effort for makers.ag rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was in use (p = 0.90); The parties that used the term can organize to lobby (p = 0.85). It also follows under 2 other minimal assumption set(s). Reported.
- C-12. Compared with no Kestrava Fair Repair Act, lobbying effort (policy field) for makers.ag may move either way from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); The bound providers can organize to lobby (p = 0.85); The groups that gain from or are bound by the measure would have lobbied on the same question without it (p = 0.80). It also follows under 2 other minimal assumption set(s). Reported.
- C-13. Compared with no Kestrava Fair Repair Act, quantity supplied for makers.ag may move either way from the medium run onward (tier B, invisible). Why: EN-14: EN-14. This holds if: The standard binds on some designs (p = 0.80); Most makers comply (p = 0.70). Reported.
- C-14. Compared with no Kestrava Fair Repair Act, reclassification for makers.ag rises from the medium run onward (tier B, invisible). Why: RS-5: owners move units out of the rule's reach. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); Most bound providers comply (p = 0.70); Reshaping goods to fall outside the definitions costs some actors less than the burden (p = 0.55). Reported.
- C-15. Compared with no Kestrava Fair Repair Act, resources available other uses for makers.ag falls from the short run onward (tier B, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The term was in use (p = 0.90). Reported.
- C-16. Compared with no Kestrava Fair Repair Act, term prevalence for makers.ag rises from the short run onward (tier B, invisible). Why: PC-18: PC-18. This holds if: The term was in use (p = 0.90); Lawful substitute terms give part of the same protection (p = 0.80). Reported.
- C-17. Compared with no Kestrava Fair Repair Act, asset value for makers.phone falls from the short run onward (tier B, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The term was in use (p = 0.90). Reported.
- C-18. Compared with no Kestrava Fair Repair Act, compliance cost for makers.phone rises from the short run onward (tier A, invisible). Why: EN-14: EN-14; OC-2: OC-2. This holds if: no assumption. Reported.
- C-19. Compared with no Kestrava Fair Repair Act, legal breach for makers.phone rises from the short run onward (tier B, invisible). Why: RS-20: RS-20. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); Complaints are unlikely from some recipients (p = 0.70). Reported.
- C-20. Compared with no Kestrava Fair Repair Act, lobbying effort for makers.phone rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); The bound providers can organize to lobby (p = 0.85). It also follows under 2 other minimal assumption set(s). Reported.
- C-21. Compared with no Kestrava Fair Repair Act, lobbying effort (policy field) for makers.phone may move either way from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was in use (p = 0.90); The parties that used the term can organize to lobby (p = 0.85); The groups that gain from or are bound by the measure would have lobbied on the same question without it (p = 0.80). It also follows under 2 other minimal assumption set(s). Reported.
- C-22. Compared with no Kestrava Fair Repair Act, quantity supplied for makers.phone may move either way from the medium run onward (tier B, invisible). Why: EN-14: EN-14. This holds if: The standard binds on some designs (p = 0.80); Most makers comply (p = 0.70). Reported.
- C-23. Compared with no Kestrava Fair Repair Act, resources available other uses for makers.phone falls from the short run onward (tier B, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The term was in use (p = 0.90). Reported.
- C-24. Compared with no Kestrava Fair Repair Act, term prevalence for makers.phone rises from the short run onward (tier B, invisible). Why: PC-18: PC-18. This holds if: The term was in use (p = 0.90); Lawful substitute terms give part of the same protection (p = 0.80). Reported.
- C-25. Compared with no Kestrava Fair Repair Act, compliance cost for makers.phone.matching rises from the short run onward (tier B, invisible). Why: PC-17: PC-17. This holds if: Some existing policies offer the term on conditions the mandate forbids (p = 0.20); Most bound providers comply (p = 0.70). Not reported: an assumption is below the 0.5 cut-off.
- C-26. Compared with no Kestrava Fair Repair Act, quantity supplied for makers.phone.matching rises from the medium run onward (tier B, invisible). Why: PC-17: PC-17; CR-12: CR-12; CR-2: CR-2; CR-9: an owner who leaves the rental market ends the leases of those who live in the building. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); The unbound firms compete with the bound providers (p = 0.90); Most bound providers comply (p = 0.70); The term is worth less to the marginal recipient than it costs the provider (p = 0.60). Reported.
- C-27. Compared with no Kestrava Fair Repair Act, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-28. Compared with no Kestrava Fair Repair Act, compliance cost for owners.ag rises from the short run onward (tier B, invisible). Why: OC-2: OC-2. This holds if: Complaints are filed in meaningful numbers (p = 0.70). Reported.
- C-29. Compared with no Kestrava Fair Repair Act, lobbying effort for owners.ag rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); The recipients can organize to lobby (p = 0.85). Reported.
- C-30. Compared with no Kestrava Fair Repair Act, lobbying effort (policy field) for owners.ag may move either way from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); The groups that gain from or are bound by the measure would have lobbied on the same question without it (p = 0.80); The recipients can organize to lobby (p = 0.85). Reported.
- C-31. Compared with no Kestrava Fair Repair Act, non wage compensation for owners.ag rises from the short run onward (tier B, visible). Why: PC-17: PC-17. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); Most bound providers comply (p = 0.70). Reported.
- C-32. Compared with no Kestrava Fair Repair Act, resources available other uses for owners.ag rises from the short run onward (tier B, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The term was in use (p = 0.90). It also follows under 1 other minimal assumption set(s). Reported.
- C-33. Compared with no Kestrava Fair Repair Act, asset value for owners.ag.exempt may move either way from the medium run onward (tier B, invisible). Why: EN-14: EN-14; CR-7: CR-7. This holds if: The standard binds on some designs (p = 0.80); Buyers value the standard enough to prefer covered units (p = 0.70); Most makers comply (p = 0.70). It also follows under 1 other minimal assumption set(s). Reported.
- C-34. Compared with no Kestrava Fair Repair Act, stock age for owners.ag.exempt may move either way in the long run (tier B, invisible). Why: EN-14: EN-14; CR-7: CR-7. This holds if: The standard binds on some designs (p = 0.80); Buyers value the standard enough to prefer covered units (p = 0.70); Most makers comply (p = 0.70). It also follows under 1 other minimal assumption set(s). Reported.
- C-35. Compared with no Kestrava Fair Repair Act, compliance cost for owners.phone rises from the short run onward (tier B, invisible). Why: OC-2: OC-2. This holds if: Complaints are filed in meaningful numbers (p = 0.70). Reported.
- C-36. Compared with no Kestrava Fair Repair Act, lobbying effort for owners.phone rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); The recipients can organize to lobby (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-37. Compared with no Kestrava Fair Repair Act, lobbying effort (policy field) for owners.phone may move either way from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); The groups that gain from or are bound by the measure would have lobbied on the same question without it (p = 0.80); The recipients can organize to lobby (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-38. Compared with no Kestrava Fair Repair Act, non wage compensation for owners.phone rises from the short run onward (tier B, visible). Why: PC-17: PC-17. This holds if: The term was absent from some contracts, so the mandate binds for them (p = 0.90); Most bound providers comply (p = 0.70). Reported.
- C-39. Compared with no Kestrava Fair Repair Act, resources available other uses for owners.phone rises from the short run onward (tier B, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The term was in use (p = 0.90). Reported.
- C-40. Compared with no Kestrava Fair Repair Act, asset value for owners.phone.exempt may move either way from the medium run onward (tier B, invisible). Why: EN-14: EN-14; CR-7: CR-7. This holds if: The standard binds on some designs (p = 0.80); Buyers value the standard enough to prefer covered units (p = 0.70); Most makers comply (p = 0.70). It also follows under 1 other minimal assumption set(s). Reported.
- C-41. Compared with no Kestrava Fair Repair Act, stock age for owners.phone.exempt may move either way in the long run (tier B, invisible). Why: EN-14: EN-14; CR-7: CR-7. This holds if: The standard binds on some designs (p = 0.80); Buyers value the standard enough to prefer covered units (p = 0.70); Most makers comply (p = 0.70). It also follows under 1 other minimal assumption set(s). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
