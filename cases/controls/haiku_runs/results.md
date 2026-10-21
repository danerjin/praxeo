## Round-1 decider prompt (Haiku), easy and hard controls

| Case | Question | Expected | p | Right side |
|---|---|---|---|---|
| ceiling_clear_yes | r4.binding | yes | 0.97 | yes |
| ceiling_clear_yes | r4.enforced | yes | 0.85 | yes |
| ceiling_clear_yes | r4.nontransferable | yes | 0.95 | yes |
| ceiling_not_binding | r1.binding | no | 0.03 | yes |
| ceiling_not_binding | r1.enforced | yes | 0.90 | yes |
| ceiling_unenforced | r2.enforced | no | 0.15 | yes |
| ceiling_unenforced | r2.binding | yes | 0.60 | yes |
| hard_car_makers | h5.domestic_substitutes | yes | 0.95 | yes |
| hard_copper_exporter | h4.binding | no | 0.08 | yes |
| hard_paper_enforcer | h2.enforced | no | 0.08 | yes |
| hard_shrinking_city | h1.binding | no | 0.05 | yes |
| hard_soda_tax | h6.quantity_responds | yes | 0.92 | yes |
| hard_successor_payments | h3.nontransferable | no | 0.15 | yes |
| hard_void_leases | h7.enforced | yes | 0.60 | yes |
| hard_waiting_lists | h8.binding | yes | 0.93 | yes |
| land_tax | x1.quantity_responds | no | 0.20 | yes |
| tariff_no_domestic_producers | t2.domestic_substitutes | no | 0.05 | yes |
| tariff_no_domestic_producers | t2.binding | yes | 0.92 | yes |
| tariff_no_imports | t1.binding | no | 0.04 | yes |
| tenancy_assignable | r3.nontransferable | no | 0.03 | yes |
| tenancy_assignable | r3.enforced | yes | 0.60 | yes |

- Expected no: 10 of 10 on the right side of 0.5; mean p 0.09.
- Expected yes: 11 of 11 on the right side of 0.5; mean p 0.84.

## Round-2 decider prompt (Haiku), easy and hard controls

| Case | Question | Expected | p | Right side |
|---|---|---|---|---|
| ceiling_clear_yes | r4.binding | yes | 0.95 | yes |
| ceiling_clear_yes | r4.enforced | yes | 0.85 | yes |
| ceiling_clear_yes | r4.nontransferable | yes | 0.95 | yes |
| ceiling_not_binding | r1.binding | no | 0.05 | yes |
| ceiling_not_binding | r1.enforced | yes | 0.80 | yes |
| ceiling_unenforced | r2.enforced | no | 0.12 | yes |
| ceiling_unenforced | r2.binding | yes | 0.70 | yes |
| hard_car_makers | h5.domestic_substitutes | yes | 0.92 | yes |
| hard_copper_exporter | h4.binding | no | 0.12 | yes |
| hard_paper_enforcer | h2.enforced | no | 0.08 | yes |
| hard_shrinking_city | h1.binding | no | 0.05 | yes |
| hard_soda_tax | h6.quantity_responds | yes | 0.92 | yes |
| hard_successor_payments | h3.nontransferable | no | 0.10 | yes |
| hard_void_leases | h7.enforced | yes | 0.62 | yes |
| hard_waiting_lists | h8.binding | yes | 0.90 | yes |
| land_tax | x1.quantity_responds | no | 0.12 | yes |
| tariff_no_domestic_producers | t2.domestic_substitutes | no | 0.06 | yes |
| tariff_no_domestic_producers | t2.binding | yes | 0.92 | yes |
| tariff_no_imports | t1.binding | no | 0.05 | yes |
| tenancy_assignable | r3.nontransferable | no | 0.03 | yes |
| tenancy_assignable | r3.enforced | yes | 0.75 | yes |

- Expected no: 10 of 10 on the right side of 0.5; mean p 0.08.
- Expected yes: 11 of 11 on the right side of 0.5; mean p 0.84.

