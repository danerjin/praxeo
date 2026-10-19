# Thin-slice run: Sorrel Basin Groundwater Allocation Plan

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T05:51:59+00:00
Prediction log sha256 (frozen before the outcome card was opened): `0bb75029da953ea5…`

## Policy record

- Rule-maker: the Sorrel Basin Water Authority (SBWA); enacted 18 November 2026, effective 1 October 2027.
- Stated aim: none stated
- k1: quota on groundwater in sorrel_basin; binds pumpers, protects None. Source: "The plan caps the groundwater pumped from the basin at 210,000 af a year (70% of the 2017 to 2021 average), binding holders of non-domestic wells."
- k2: rights_allocation on groundwater_shares in sorrel_basin; binds officials.enforcement, protects landholders.history. Source: "90% of the cap (189,000 af) is issued by the SBWA as permanent shares of the annual cap, to whoever holds a parcel on 1 July 2027, in proportion to the parcel's average metered or estimated pumping in water years 2017 to 2021."
- k3: rights_allocation on groundwater_shares_reserve in sorrel_basin; binds officials.enforcement, protects landholders.no_history.eligible. Source: "10% of the cap (21,000 af) is issued by the SBWA as permanent shares in blocks of 100 af, drawn by lottery in September 2027."
- Unclear U1: Trading across sub-basins: whether a share may be pumped only in the sub-basin where its parcel lies, or anywhere in the basin. Readings: U1-a: a share may be pumped only from a well in the sub-basin where the parcel that earned it lies / U1-b: a share may be pumped anywhere in the basin; the impact rules only set conditions on individual wells (spacing, monitoring)
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.95 | The cap holds the quantity below what would otherwise be traded. |
| `enforced(k1)` | enforcement | 0.75 | The cap is enforced. |
| `evasion(k1)` | enforcement | 0.55 | Some trade takes place beyond the cap without being caught. |
| `can_organize(k1)` | other | 0.85 | The holders of the rights can organize to lobby at a cost below their stake. |
| `expected_to_last(k1)` | expectations | 0.75 | Holders and buyers of the rights expect the restriction to last. |
| `values_differ(k1)` | other | 0.85 | Holders' costs or values differ. |
| `trade_cheap(k1)` | mobility | 0.80 | Rights can be sold or leased at low cost. |
| `price_effect_material(k1)` | other | 0.30 | The capped quantity matters enough in the wider market to raise the price there. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | farm_workers | employment or hours_worked | at_least_one_decrease | medium+ | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-2 | growers.nuts | disputes_settled_outside_courts | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-3 | growers.nuts | price_paid | increase | short+ | B | EN-6 | {binding(k1), enforced(k1), price_effect_material(k1)} | no |
| C-4 | growers.nuts | quality_information | decrease | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-5 | growers.nuts | quantity_traded | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |
| C-6 | growers.nuts | resources_available_other_uses | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1), price_effect_material(k1)} | no |
| C-7 | growers.nuts | search_cost | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-8 | landholders.history | asset_value | increase | short+ | B | EN-6, SB-4, EN-12 | {binding(k1), enforced(k1)} | yes |
| C-9 | landholders.history | lobbying_effort | increase | medium+ | B | EN-6, RS-7 | {binding(k1), can_organize(k1), enforced(k1)} | yes |
| C-10 | landholders.history | right_lease_price | increase | short+ | B | EN-6, EN-13, CR-6 | {binding(k1), enforced(k1)} | yes |
| C-11 | officials.enforcement | enforcement_cost | increase | short+ | B | EN-6, OC-3 | {binding(k1), enforced(k1)} | yes |
| C-12 | pumpers | capital_stock_target | decrease | long | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-13 | pumpers | informal_activity | increase | short+ | B | EN-6, RS-3 | {binding(k1), enforced(k1), evasion(k1)} | yes |
| C-14 | pumpers | number_of_sellers | decrease | medium+ | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-15 | pumpers | quantity_supplied | increase | medium+ | B | EN-6, EN-13 | {binding(k1), enforced(k1), trade_cheap(k1), values_differ(k1)} | yes |
| C-16 | pumpers | quantity_traded | decrease | short+ | B | EN-6 | {binding(k1), enforced(k1)} | yes |

## Explanations

- C-1. Compared with no Sorrel Basin Groundwater Allocation Plan, employment or hours worked for farm_workers falls for at least one of them from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75); Rights can be sold or leased at low cost (p = 0.80); Holders' costs or values differ (p = 0.85). Reported.
- C-2. Compared with no Sorrel Basin Groundwater Allocation Plan, disputes settled outside courts for growers.nuts rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-3. Compared with no Sorrel Basin Groundwater Allocation Plan, price paid for growers.nuts rises from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75); The capped quantity matters enough in the wider market to raise the price there (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-4. Compared with no Sorrel Basin Groundwater Allocation Plan, quality information for growers.nuts falls from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-5. Compared with no Sorrel Basin Groundwater Allocation Plan, quantity traded for growers.nuts falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75). Reported.
- C-6. Compared with no Sorrel Basin Groundwater Allocation Plan, resources available other uses for growers.nuts falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75); The capped quantity matters enough in the wider market to raise the price there (p = 0.30). Not reported: an assumption is below the 0.5 cut-off.
- C-7. Compared with no Sorrel Basin Groundwater Allocation Plan, search cost for growers.nuts rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-8. Compared with no Sorrel Basin Groundwater Allocation Plan, asset value for landholders.history rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; SB-4: a lasting change in the return on an asset in slow supply is capitalized in its value; EN-12: EN-12. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75). Reported.
- C-9. Compared with no Sorrel Basin Groundwater Allocation Plan, lobbying effort for landholders.history rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The holders of the rights can organize to lobby at a cost below their stake (p = 0.85); The cap is enforced (p = 0.75). Reported.
- C-10. Compared with no Sorrel Basin Groundwater Allocation Plan, right lease price for landholders.history rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13; CR-6: sellers facing fewer buyers than they planned for cut their price. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75). Reported.
- C-11. Compared with no Sorrel Basin Groundwater Allocation Plan, enforcement cost for officials.enforcement rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75). Reported.
- C-12. Compared with no Sorrel Basin Groundwater Allocation Plan, capital stock target for pumpers falls in the long run (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75); Rights can be sold or leased at low cost (p = 0.80); Holders' costs or values differ (p = 0.85). Reported.
- C-13. Compared with no Sorrel Basin Groundwater Allocation Plan, informal activity for pumpers rises from the short run onward (tier B, invisible). Why: EN-6: EN-6; RS-3: RS-3. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75); Some trade takes place beyond the cap without being caught (p = 0.55). Reported.
- C-14. Compared with no Sorrel Basin Groundwater Allocation Plan, number of sellers for pumpers falls from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75); Rights can be sold or leased at low cost (p = 0.80); Holders' costs or values differ (p = 0.85). Reported.
- C-15. Compared with no Sorrel Basin Groundwater Allocation Plan, quantity supplied for pumpers rises from the medium run onward (tier B, invisible). Why: EN-6: EN-6; EN-13: EN-13. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75); Rights can be sold or leased at low cost (p = 0.80); Holders' costs or values differ (p = 0.85). Reported.
- C-16. Compared with no Sorrel Basin Groundwater Allocation Plan, quantity traded for pumpers falls from the short run onward (tier B, invisible). Why: EN-6: EN-6. This holds if: The cap holds the quantity below what would otherwise be traded (p = 0.95); The cap is enforced (p = 0.75). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
