# WE-022 Repeal of the Riverton rent ordinance

Analyst: draft (Handbook 0.5)  |  Rule catalog version: 0.5  |  Status: awaiting expert review

A stylized repeal of the ordinance analyzed in WE-001, in the same fictional city, ten years after it took effect. It doubles as a metamorphic check: the analysis of a repeal should reverse the signs of WE-001, except where the ordinance caused lasting changes. The check is at the end of section 7. The counterfactual throughout is **the ordinance stays in force on its current terms**; every sign below is relative to that, not to the situation before the repeal and not to a Riverton that never had the ordinance. Most rules in the catalog are written for imposing a policy. "In reverse" after a rule ID means the rule is applied to the removal of its precondition; where that direction is not obviously valid, the text says so. The catalog states some directions explicitly: SB-4 covers returns that rise or fall, TS-1 has a clause for capital that grows, TS-5 and TS-6 are written for repeals, RS-7 has a clause for repeals (lobbying takes place in the counterfactual too) and RS-10 has a reverse clause (see "Analyzing a repeal" in the workflow). The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Riverton Rent Stabilization Repeal.** Ten years after the WE-001 ordinance took effect, voters approve a ballot measure to repeal it. The measure qualified for the ballot six months before its effective date, and polls showed it was likely to pass. The starting point, taken from WE-001's analysis and stated here as the situation at repeal rather than as findings: controlled rents were frozen for three years and have risen at most 2% a year since, while rents for comparable exempt units have kept rising faster; some covered buildings have been converted to condominiums through the K3 permit route; maintenance in covered buildings has been below what it would otherwise have been; Eastfield and Northgate remain unregulated.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Decontrol with phase-in | Removal of a `price_ceiling` | Rent on units covered by WE-001's K1 | Landlords and tenants of covered units | Vacancy decontrol from the effective date: a covered unit that becomes vacant may be let at any rent. Sitting tenants: during each of the two years after the effective date, rent may rise by at most 15% at renewal. From the second anniversary, no limit. | None |
| R2 Tenancy rules | Removal of a restriction on contract terms | Leases of covered units (WE-001 K2) | Landlords and tenants | Eviction only for cause, and the ban on assigning a tenancy, stay in force for the two phase-in years and end at the second anniversary. | None |
| R3 Rent board | End of administration | WE-001 K4 | City | The board handles phase-in disputes and overcharge claims for two years, then is dissolved. | None |
| (unchanged) | — | Condominium-conversion permit process (WE-001 K3) | — | Not repealed: the 12-month permit process and relocation payments continue to apply to all rental buildings. | — |

Unclear provisions: whether a unit vacated during the phase-in by a tenant who accepted a payment to leave counts as a vacancy, and is therefore decontrolled at once. Assumed yes; the measure does not regulate such payments.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| R1 | Removal of a triangular intervention: landlords and tenants may again agree the rent | Yes: for most covered units the controlled rent is now well below the rent of a comparable exempt unit (A-1) | PC in reverse, RS-8, SB-4, TS-1, TS-5, TS-6 |
| R2 | Removal of a triangular intervention | Yes, from the second anniversary | PC-7 and RS-11 in reverse |
| R3 | Removal of a binary intervention (taxpayer-funded board) | Yes, from the second anniversary | OC-3 in reverse |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `tenants.controlled` | Sitting tenants of covered units at the effective date | Rent rises toward the market level over two years; lose the reason to stay put; may be offered payments to leave during the phase-in. |
| `tenants.controlled.displaced` | Sitting tenants who will not or cannot pay the higher rent | Must find other housing in Riverton or a neighboring city. |
| `tenants.prospective` | People looking for a rental in Riverton | Formerly covered units come up for rent at market rents; no shortage at a controlled price to queue for. |
| `landlords.controlled` | Current owners of covered buildings, including those who bought during the ten years at prices that reflected the control | Can charge market rents; the return on maintaining and improving the buildings rises; conversion to condominiums becomes less attractive. |
| `developers` (`sellers.prospective`) | Builders of new rental housing | The rent premium in the exempt segment shrinks; must judge whether controls might return. |
| `landlords.uncontrolled` | Owners of exempt units built since the ordinance | Face competition from decontrolled units. |
| `homebuyers` | Buyers of owner-occupied housing | Fewer rental buildings are converted to condominiums. |
| `buyers.covered_buildings` | People who buy covered buildings after the repeal is expected | Pay a price that reflects decontrolled rents. |
| `renters.neighbors` | Renters in Eastfield and Northgate | Some Riverton seekers return to Riverton; some displaced sitting tenants arrive. |
| `officials.enforcement`, `taxpayers` | Rent board and its funders | Board's work ends after two years. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `tenants.controlled` | `price_paid` | increase | short to medium (phased over two years) | PC-3 in reverse, TS-3 | A-1, A-2 |
| C-2 | `landlords.controlled` | `net_price_received` | increase | short to medium | PC-3 in reverse | A-1, A-2 |

The visible effect: sitting tenants pay more than they would have under the ordinance, and their landlords receive more. The size of the step is the gap that built up over ten years of a 2% cap (TS-3), released at once for vacant units and over two years for sitting tenants.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `tenants.prospective` (formerly covered units) | `excess_demand` | decrease | short | PC-1 in reverse | A-1, A-2 |
| C-4 | `tenants.prospective` | `search_cost` | decrease | short | PC-2 in reverse | A-1, A-2, A-21 |
| C-5 | `tenants.prospective` | `allocation_by_non_price_criteria` | decrease | short | PC-2 in reverse | A-1, A-2, A-21 |
| C-6 | `tenants.prospective` | `side_payments` (key money, premiums on illegal sublets) | decrease | short to medium (sublets of units still in the phase-in continue until it ends) | PC-6, RS-3 in reverse | A-1, A-2, A-21 |
| C-28 | `tenants.prospective` who obtain formerly covered units | `price_paid` (covered units let on vacancy) | increase | short to medium | PC-3 in reverse | A-1, A-2 |
| C-30 | `tenants.controlled` | `informal_activity` (illegal sublets) | decrease | short to medium | PC-6, RS-3 in reverse | A-1, A-21 |
| C-32 | `landlords.controlled` | `compliance_cost` (board proceedings, conversion permit applications) | decrease | medium (after the board is dissolved) | OC-2 in reverse | A-1, A-3 |
| C-7 | `tenants.controlled` | `turnover` | increase | medium (mostly after the phase-in) | PC-7 in reverse | A-1, A-6 |
| C-8 | `landlords.controlled` | `maintenance_spending` | increase | short to medium | PC-4, RS-2 in reverse, TS-5 | A-1, A-3 |
| C-9 | `landlords.controlled` | `reclassification` (new conversions to condominiums) | decrease | medium | RS-5, PC-5 in reverse | A-1, A-3 |
| C-10 | `landlords.controlled` | `quantity_supplied` of formerly covered rental units | increase | short to medium | PC-5 in reverse | A-1, A-3, A-15 |
| C-11 | `tenants.controlled` | `side_payments` received (payments from landlords to leave during the phase-in) | increase | short | RS-8, LW-5 | A-1, A-13 |
| C-12 | `tenants.prospective` | `quantity_traded` (lettings of covered units that fall vacant in the announcement window) | decrease | short (announcement window only) | RS-8 | A-11 |
| C-13 | `tenants.controlled.displaced` | `search_cost` | increase | medium | PC-3 in reverse, OC-2 | A-1, A-6 |
| C-14 | `tenants.controlled`, `landlords.controlled` | `lobbying_effort` | ambiguous (see section 7) | medium | RS-7 (repeal clause) | A-14 |

C-10 has two quick sources: units that owners were holding off the market, and buildings in the conversion permit process whose owners withdraw (A-15). It does not include converted condominiums returning to rental; see C-23 and the metamorphic check.

C-11 and C-12 are both timing responses (RS-8), and neither has a counterpart in WE-001. Because a vacancy is decontrolled at once while a sitting tenant's rent is phased in, a landlord gains from a vacancy during the phase-in and may pay the tenant to leave. Before the effective date, a landlord with a vacant unit gains by leaving it empty until decontrol rather than letting it at the controlled rent.

C-13 applies only to tenants who move because of the rent increase. Sitting tenants who would have moved anyway now search in a market without a shortage, which is part of C-4.

C-4 to C-6 and C-30 reverse the margins WE-001 found open and used under the ordinance (its A-3, A-15, A-16): searching, selection by connections, key money and illegal sublets. They reverse only where those margins were in fact used, which is A-21. WE-001 does not sign `wait_time` (there is no waiting list), so the repeal does not either. C-28 is the other side of PC-3 in reverse: seekers who would have obtained a covered unit at the controlled rent now pay the market rent for it.

C-32: the board's proceedings end at the second anniversary (R3), and fewer owners apply for conversion permits (C-9), so landlords spend less on them. Phase-in disputes continue for two years, so the decrease starts at the medium horizon.

C-14: RS-7's repeal clause applies. Both classes lobbied in the counterfactual too: sitting tenants to keep the ordinance, owners to loosen or repeal it (WE-001 C-11). After the repeal, tenants lobby to restore it and owners to defend the repeal. Each class lobbied in both worlds, so the change in each class's effort is `ambiguous` without a premise. RS-7's premise, that each can organize at a cost below its stake, is A-14.

Not reported: reconversion of condominiums to rental. Converted units have been sold to separate owners, and reassembling a building costs more than the difference in return (TS-6; A-9, p = 0.9; its converse A-16, p = 0.1, is below the cut-off).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-15 | `tenants.prospective` in exempt units | `price_substitute` (rent of exempt units) | decrease | medium (from the effective date) | PC-8 in reverse; CR-12b with an accounting identity (CR-12e) | covered and exempt units: `same_market_other_segment`, close | A-1, A-5 |
| C-27 | `tenants.prospective` in exempt units | `price_substitute` (rent of exempt units) | increase | short (announcement window) | RS-8, PC-8 | as C-15 | A-5, A-11 |
| C-16 | `developers` | `investment_target` (new rental construction) | decrease (see section 7) | medium | PC-8, LW-4 in reverse | | A-5, A-8 |
| C-17 | `landlords.controlled` | `asset_value` (formerly covered buildings) | increase | short (from the announcement) | SB-4, TS-5 | | A-1, A-2, A-3 |
| C-29 | `buyers.covered_buildings` | `price_paid` (covered buildings) | increase | short to medium | SB-4, OC-7 | sale of buildings | A-1, A-3 |
| C-31 | `tenants.prospective` (subtenants) | `disputes_settled_outside_courts` | decrease | short to medium | RS-10 in reverse | the sublet (tenant to subtenant) | A-1, A-21 |
| C-18 | `homebuyers` | `quantity_substitute` (condominiums from new conversions) | decrease | medium | RS-5 in reverse | rental and owner-occupied housing: `substitute`, partial | A-1, A-3 |
| C-19 | `tenants.controlled` | `job_changes` | increase | medium (mostly after the phase-in) | RS-11, PC-7 in reverse | controlled tenancy and jobs: `complement`, note `location` | A-1, A-12 |
| C-20 | `tenants.controlled` | `quality_per_unit` | increase | medium | PC-4 in reverse, TS-1, TS-5 | | A-1, A-3 |
| C-21 | `renters.neighbors` | `price_paid` in Eastfield and Northgate | ambiguous (see section 7) | medium | RS-4, PC-3 | Riverton and neighbors: `across_border`, partial | A-6, A-7 |
| C-22 | `landlords.controlled` | `investment_target` (major renovation of formerly covered buildings) | increase | medium to long | PC-5 in reverse, TS-5 | | A-1, A-4 |
| C-23 | `landlords.controlled` | `capital_stock_target` (formerly covered rental stock) | increase | long | PC-5 in reverse, TS-1 (upward clause), TS-5, TS-6 | | A-1, A-4, A-9, A-18 |

C-15 and C-27: PC-8 in reverse holds only from the effective date. In the announcement window, landlords hold vacant covered units empty (C-12), so seekers who would have taken them turn to exempt units and exempt rents rise (C-27; RS-8 with PC-8). From the effective date two chains reach exempt rents. (−) Seekers who were rationed out of the covered segment can now rent there (PC-8 in reverse), and withheld units return to use (C-10). (+) Sitting tenants who will not pay the higher rent move, and some move to exempt units (A-6). The (+) chain is offset one for one: each sitting tenant who leaves frees a covered unit that a seeker takes, so households move into the covered segment, net, only as the number of covered units in use rises (C-10, C-23, C-24 are all increases). This is an accounting identity used as a dominance premise (CR-12e), and it is the same identity WE-001 uses (rationing changes who occupies the covered stock, not how many households it houses). So the combined sign is a decrease (section 7). PC-8's Unless clause does not apply: the repeal pushes no sellers into the exempt segment.

C-31: RS-10 in reverse. As illegal sublets fall (C-30), fewer subtenants hold arrangements with no recourse to the courts. No previously excluded sellers enter, so RS-10's quality-variability caveat does not arise.

C-17 applies SB-4, which covers a lasting change in returns in either direction: the ordinance lowered the expected return of a fixed stock of buildings, and the repeal raises it again, so building prices rise as soon as the repeal is expected. The gain goes to whoever owns the buildings at the announcement. Owners who sold during the ten years, at prices that already reflected the control, bore the loss and do not share in the gain. Expectations of re-imposition (TS-5) make the rise smaller but do not change its sign as long as owners give the repeal some chance of lasting (A-3). By OC-7's symmetry clause, the gain to owners who sell is the outlay of those who buy: later buyers pay the higher price (C-29), and so neither gain nor lose from the repeal as it stands.

C-22 and C-23 are Tier B in catalog 0.3 (Tier C in the 0.2 draft). PC-5 in reverse says investment returns when the ceiling goes; TS-5 adds that investment paying back only over ten or more years is smaller and later than the mirror of the ordinance's effect, and goes ahead only as far as owners expect decontrol to last that long (A-4, p = 0.6). C-23 also uses TS-6, under which the stock converted under the ordinance does not come back (A-9), and the upward clause of TS-1, under which rebuilding runs at the speed of new investment rather than as the mirror of wear-out (A-18). Its persistence against a Riverton that never had the ordinance is partial (metamorphic check, WE-001 C-9).

C-21 is at depth 3 and reaches a diffuse group of bystanders, so the chain stops there.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `developers`, `investment_target` (new rental construction), medium | Repeal removes the risk that the new-construction exemption would be withdrawn while the ordinance stood. Rests on developers having feared that (negation of A-8, A-17, p = 0.4). | The rent premium that spillover demand gave exempt units shrinks (C-15), so new building pays less (LW-4). Rests on A-5 and A-8 (p = 0.6). A further chain under TS-5: if developers expect controls to return and to cover new buildings next time, expected returns fall further. Rests on A-19 (p = 0.35), so it is a conditional possibility, not reported; it would push the same way. | None | **decrease**. The + chain rests on an assumption below the 0.5 cut-off and is not reported. This is the mirror of WE-001's C-13 and rests on the same judgment about what developers expected. |
| `tenants.controlled`, `quality_adjusted_price`, medium | Rent rises (C-1). | Quality rises (C-20). | None | **ambiguous**. Same as in WE-001, with both chains reversed. |
| `tenants.prospective` in exempt units, `price_substitute`, medium | Sitting tenants who move out of covered units, some to exempt units (A-6). | Rationed-out seekers move into covered units (PC-8 in reverse); withheld units return (C-10). | Accounting identity (CR-12e): every sitting tenant who leaves frees a covered unit that a seeker takes, so net demand for exempt units falls by the rise in covered units in use (C-10, C-23, C-24). | **decrease** (C-15). In the announcement window, **increase** (C-27), a separate window. |
| `landlords.controlled`, `resources_available_other_uses`, short to medium | Higher rent on every covered unit at renewal and on vacancy (C-2); fewer relocation payments and permit costs (C-9, C-32). | Key money no longer received by the landlords who took it (C-6); payments to sitting tenants to leave (C-11). | A-2 with A-21: rents rise on every covered unit each month, while key money was confined to a minority of lettings (WE-001's premise that the cap was enforced against most landlords); payments to leave are made only where the landlord expects the vacancy to be worth more (CR-5). Empirical premise (CR-12e). | **increase** (C-34). |
| `renters.neighbors`, `price_paid`, medium | Displaced sitting tenants move to cheaper neighboring cities (C-13, A-6, A-7). | Riverton seekers who had been pushed out to the neighbors can now find units in Riverton (C-3, C-15). | None | **ambiguous**. WE-001's C-15 does not simply reverse: the repeal pushes some people out of Riverton as well as drawing others back. |
| `tenants.controlled`, `landlords.controlled`, `lobbying_effort`, medium | Sitting tenants now bear a concentrated loss that re-imposition would undo, and organize for it (RS-7, A-14). Owners who have capitalized the gain (C-17) defend the repeal. | In the counterfactual, tenants would have kept lobbying to defend the ordinance and owners to loosen it (WE-001 C-11); that effort ends. | None (RS-7, repeal clause) | **ambiguous** for each class: each lobbied in both worlds. The repeal changes what each lobbies for; the method cannot say whether either class's effort rises or falls. |

### Metamorphic check against WE-001

"Reverses" means the expected sign under repeal is the opposite of WE-001's. "Partly reverses" means the sign reverses for the flow (what happens from now on) but not for a stock that the ordinance already changed. **Persistence** (TS-6; `02_ontology.md`, 2.5) is how much of WE-001's effect remains after the repeal, compared with a Riverton that never had the ordinance: none, partial or full. It is "partial" or "full" where the effect ran through a stock change that costs something to reverse (conversions, deferred maintenance that became structural damage, displaced tenants), and also during the phase-in, while rents are still held below the path without the ordinance; "none" where a flow simply stops; "n/a" for transition effects with no counterpart on that path. It may be given per horizon (`02_ontology.md`, 2.5). The same values are recorded on each consequence in the consequence list.

| WE-001 ID | Actor class, variable | Sign in WE-001 | Expected sign under repeal (this example) | Reverses? | Persistence (TS-6) | Reason |
|---|---|---|---|---|---|---|
| C-1 | `tenants.controlled`, `price_paid` (medium to long) | decrease | increase (C-1) | Reverses | partial (short: the 15% steps); none (from the second anniversary) | Phased by R1; vacancies go to market at once (C-28). |
| C-21 | `tenants.controlled`, `price_paid` (first months after the effective date) | ambiguous | no counterpart | Does not reverse | n/a | A transition effect of the original's announcement (pre-emptive raises against the cap). The repeal sets no base date. |
| C-17 | `tenants.controlled` renewing before the effective date, `price_paid` | increase (short) | no counterpart | Does not reverse | n/a | The repeal's announcement effect works through a different margin: landlords hold vacant units empty (C-12) instead of raising rents early. |
| C-27 | `landlords.controlled`, `net_price_received` | decrease | increase (C-2) | Reverses | partial (short: the 15% steps); none (from the second anniversary) | The mirror of C-1. |
| C-2 | `tenants.prospective`, `excess_demand` | increase | decrease (C-3) | Reverses | none | The shortage exists only at the controlled price. |
| C-3 | `tenants.prospective`, `search_cost` | increase | decrease (C-4) | Reverses | none | For seekers. Displaced sitting tenants newly bear search costs (C-13), which has no counterpart in WE-001. |
| C-4 | `tenants.prospective`, `allocation_by_non_price_criteria` | increase | decrease (C-5) | Reverses | none | Landlords still screen on credit, as in any rental market; what falls is selection made possible by the shortage. |
| C-7 | `tenants.prospective`, `side_payments` (key money) | increase | decrease (C-6) | Reverses | none | Key money loses its reason once rents can rise. Payments now flow the other way, from landlords to sitting tenants (C-11), which has no counterpart in WE-001. |
| C-22 | `tenants.controlled`, `informal_activity` (illegal sublets) | increase | decrease (C-30) | Reverses | none | The gap between the tenant's rent and the market rent closes over the phase-in. |
| C-23 | subtenants, `disputes_settled_outside_courts` | increase | decrease (C-31) | Reverses | none | RS-10 in reverse, with the sublets. |
| C-5 | `tenants.controlled`, `turnover` | decrease | increase (C-7) | Reverses, delayed | none | Lock-in lasts while a below-market rent remains, so mostly after the phase-in. |
| C-18 | `tenants.controlled`, `job_changes` | decrease | increase (C-19) | Reverses, delayed | none | Mostly after the phase-in, when the remaining below-market rent ends. |
| C-6 | `landlords.controlled`, `maintenance_spending`, `quality_per_unit` | decrease | increase (C-8 spending, C-20 quality) | Partly reverses | partial | Maintenance spending responds at once (A-3; TS-5, quick payback). Ten years of deferred maintenance have partly become structural damage (A-10, `reversal_cost`), which is repaired only as owners choose to invest, and repairs with long payback depend on owners trusting the repeal (TS-5, A-4). Quality does not jump back. |
| C-8 | `landlords.controlled`, `reclassification` | increase | decrease (C-9) | Partly reverses | full for buildings already converted; none for the flow | New conversions fall and pending applications are withdrawn. Buildings already converted stay condominiums: reconversion is not worth its cost (TS-6; A-9; A-16 below the cut-off). |
| C-9 | `landlords.controlled`, `quantity_supplied` | decrease | increase (C-10 short to medium; C-23 long) | Partly reverses | partial | Withheld units and pending conversions return quickly. Units lost to conversion do not return (TS-6, A-9). Rebuilding runs at the speed of new investment (TS-1 upward clause, A-18) and depends on credibility (TS-5, A-4), not as a mirror of the wear-out in WE-001. |
| C-24 | `landlords.controlled`, `units_held_vacant` (medium) | increase | increase in the announcement window (C-12, units held for decontrol); then units return to use (C-10) | Reverses after a temporary rise | partial | Units held vacant pending conversion return to use from the effective date; units that need major repair return only as owners invest (A-18). |
| C-10 | `tenants.controlled` in converted buildings, `turnover` | increase | no separate consequence; follows from C-9 (fewer conversions) | Partly reverses | full for tenants already displaced | Tenants already displaced by past conversions are not restored; their buildings stay converted (TS-6, A-9). Fewer tenants are displaced by conversion from now on. |
| C-30 | `tenants.controlled` in converted buildings, `resources_available_other_uses` (relocation payment) | increase | no separate consequence; follows from C-9 | Partly reverses | full for payments already made | Fewer conversions mean fewer relocation payments from now on; payments already received stay with the tenants. |
| C-25 | `landlords.controlled`, `compliance_cost` | increase | decrease (C-32, after the board is dissolved) | Partly reverses | partial | Board proceedings end; the K3 permit process is not repealed, so owners who still convert still bear it. |
| C-11 | landlords, tenants, developers, `lobbying_effort` | increase | ambiguous (C-14) | Does not reverse | n/a | RS-7, repeal clause: each class lobbied in both worlds. The repeal changes what each lobbies for. |
| C-12 | `tenants.prospective`, `price_substitute` (exempt units) | increase | decrease from the effective date (C-15); increase in the announcement window (C-27) | Reverses after a temporary rise | partial | Against a Riverton that never had the ordinance, the stock lost to conversion keeps the whole market tighter (TS-6, A-9), so part of WE-001's effect remains. |
| C-13 | `developers`, `investment_target` (new rental) | increase | decrease (C-16) | Reverses | partial | Rests on the same judgment about developers' expectations (A-8 here, A-9 in WE-001). Buildings built under the ordinance remain. |
| C-14 | `homebuyers`, `quantity_substitute` (condominiums) | increase | decrease (C-18) | Partly reverses | partial | The flow of new conversions falls; the condominiums already converted stay on the owner-occupied market (TS-6, A-9). |
| C-15 | `renters.neighbors`, `price_paid` | increase | ambiguous (C-21) | Does not reverse | none | Displaced sitting tenants move out while other seekers move back. |
| C-16 | `tenants.prospective`, `landlords`, `quantity_traded` (covered rentals) | decrease | decrease in the announcement window (C-12); increase from the effective date (C-24) | Reverses after a temporary dip | partial | RS-8 holds vacant units off the market until decontrol. Lettings of units already converted do not come back (TS-6, A-9). |
| C-20 | `landlords.controlled`, `asset_value` | decrease | increase (C-17) | Partly reverses | partial | It reverses for the asset, not for those who sold under the ordinance at a depressed price (SB-4), and converted or damaged buildings do not regain it (A-9, A-10). |
| C-28 | `landlords.controlled`, `resources_available_other_uses` | decrease | increase (C-34) | Reverses | partial (short: the 15% steps); none (from the second anniversary) | Same dominance premise as WE-001 (rent on every unit against key money for a minority). |
| C-29 | `tenants.controlled`, `resources_available_other_uses` | increase | decrease (C-33, those who stay) | Reverses | partial (short: the 15% steps); none (from the second anniversary) | The other side of C-34. |
| C-19 | `taxpayers`, `resources_available_other_uses` | decrease | increase (C-25) | Reverses, delayed | none | The board runs for two more years (R3), and the saving reaches taxpayers only if the city does not redirect the board's budget (A-20). |
| C-26 | `officials.enforcement`, `enforcement_cost` | increase | decrease (C-26) | Reverses, delayed | none | After the board is dissolved. |
| — | `tenants.controlled`, `quality_adjusted_price` | ambiguous | ambiguous | Reverses (stays ambiguous) | — | Both chains reverse. |

Consequences with no counterpart in WE-001: C-11 (payments to leave), C-12 (vacant units held back, as a window effect), C-13 (search costs of displaced tenants), C-22 and C-23 (renovation and rebuilding), C-27 (exempt rents in the announcement window), C-28 (new tenants of covered units, the other side of PC-3), C-29 (later buyers of covered buildings).

## 8. Time structure

- **Announcement window (six months).** Building prices rise as soon as the repeal is expected (C-17). Landlords with vacancies hold them empty until decontrol (C-12), which pushes seekers into exempt units and raises exempt rents in the window (C-27); exempt rents fall below the counterfactual only from the effective date (C-15). Owners pause conversion applications (C-9, C-10).
- **Phase-in (two years).** Vacancies go to market rent at once; sitting tenants' rents rise in two steps of at most 15% (C-1). Because a vacancy is worth more to the landlord than a phased tenancy, payments to leave are concentrated here (C-11). Lock-in weakens but does not end, so most of the rise in turnover and job changes comes after the second anniversary, when R2 also ends (C-7, C-19). The board keeps running, so taxpayers save nothing yet (C-25), and landlords' board proceedings continue (C-32).
- **Flows reverse quickly; stocks do not.** The repeal changes what owners do from now on: maintenance spending, conversion applications, key money and lettings respond within months. What ten years of the ordinance left behind changes only as new flows accumulate. Deferred maintenance that has become structural damage is repaired only as owners choose to invest (A-10). Converted buildings stay converted (A-9). This is TS-6, and the main reason several WE-001 consequences only partly reverse; the persistence column of the metamorphic check records it.
- **Rebuilding is not the mirror of decline.** Under the ordinance, the covered stock shrank at the speed of wear-out and conversion (TS-1). Under the repeal, it grows at the speed of new investment, which is governed by planning, permits, finance and construction (TS-1, upward clause; A-18). C-23 is set to long for this reason.
- **Expectations of re-imposition.** Riverton has shown it will impose rent control, and sitting tenants now have a reason to campaign for it again (C-14). Repairs that pay back within a few years proceed if owners expect the repeal to last that long (A-3, p = 0.8). Major renovation and new construction, which pay back over ten or more years, depend on a weaker expectation (A-4, p = 0.6), and are smaller and later than the mirror of WE-001's effects (TS-5).
- **Who gains from the capital gain.** The rise in building values (C-17) goes to owners at the time of the announcement. Owners who sold during the ten years bore the capital loss and get nothing back. The persons who gain from the repeal are not the persons who lost from the ordinance.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-24 | `tenants.prospective`, `landlords.controlled` | `quantity_traded` (lettings of formerly covered units) | increase | Nothing given up; exchanges are freed. Rentals at market rent that the cap prevented now happen, and both sides expect to gain from them. | OC-4 in reverse |
| C-25 | `taxpayers` | `resources_available_other_uses` | increase (after the board is dissolved) | Nothing given up; the board's budget is freed for other uses, if the city does not redirect it to other spending (A-20). | OC-3, OC-1 in reverse |
| C-26 | `officials.enforcement` | `enforcement_cost` (rent board) | decrease | Nothing given up; board staff and budget move to other work. | OC-3 in reverse |
| C-32 | `landlords.controlled` | `compliance_cost` | decrease | Nothing given up; time spent on board proceedings and permit applications is freed. | OC-2 in reverse |
| C-33 | `tenants.controlled` (those who stay) | `resources_available_other_uses` | decrease | The higher rent they keep paying, which they would otherwise have spent on other things. | CR-8b (matching C-34) |
| C-34 | `landlords.controlled` | `resources_available_other_uses` | increase | The higher rent received, net of key money no longer taken and payments to leave (section 7). | CR-8b; CR-12b with A-2, A-21 |

C-33 and C-34 are the two sides of the rent transfer (CR-8b), the mirror of WE-001's C-28 and C-29. C-33 is signed only for sitting tenants who stay and keep paying the higher rent; those who move may spend less on housing, so no sign is given for them. Search time for displaced tenants is C-13. C-25 rests on OC-3's first funding case, as in WE-001 (the board was paid from a budget that rose with the task), and on A-20 for what the city does with the saving.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | For most covered units, the controlled rent is now well below the rent of a comparable exempt unit. | binding | 0.95 | Rent board registry against rents of comparable exempt units; ten years of a 2% cap against the market trend. | Almost every consequence weakens or disappears. |
| A-2 | Landlords raise rents toward the market level at renewal and on vacancy, as R1 allows. | other | 0.85 | Ownership structure of covered buildings; landlord behavior in exempt units. | C-1, C-2, C-17, C-28, C-33 and C-34 shrink; the other chains weaken. |
| A-3 | Owners expect decontrol to last at least a few years, long enough for routine repairs to pay back. | expectations | 0.8 | Size of the ballot majority; council composition; how hard it would be to put a new ordinance on the ballot. | C-8, C-9, C-10, C-17, C-18 and C-20 weaken. |
| A-4 | Owners expect decontrol to last ten to fifteen years, long enough for major renovation and new building to pay back. | expectations | 0.6 | As A-3, plus the strength of tenant organizing after the repeal (C-14). | C-22 and C-23 not reported. |
| A-5 | Covered and exempt units are close substitutes. | substitutability | 0.85 | Similar locations and sizes; same tenant pool (WE-001 A-7). | C-15 and C-16 weaken. |
| A-6 | Some sitting tenants will not pay the higher rent and will move. | mobility | 0.85 | Incomes of sitting tenants against market rents for their units. | C-7, C-13 and C-21 weaken. |
| A-7 | Commuting from neighboring cities is practical for many renters. | mobility | 0.7 | Travel times of 15 to 25 minutes; transit links. | C-21 not reported. |
| A-8 | Developers had expected the new-construction exemption to last, so the exempt-segment premium was feeding new building. | expectations | 0.6 | Same evidence as WE-001 A-9. | The sign of C-16 flips to increase. |
| A-9 | Condominium conversions are costly to undo: converted units have been sold to separate owners. | reversal_cost | 0.9 | Condominium registry; number of owners per converted building. | Some converted buildings could return to rental; C-8, C-9 and C-14 in the metamorphic check would reverse more fully. |
| A-10 | Some deferred maintenance has become structural damage that costs more to repair than ongoing maintenance would have. | reversal_cost | 0.75 | Inspection records; age of the covered stock. | Quality recovers faster (C-20). |
| A-11 | Some covered units fall vacant in the announcement window, and landlords can keep them empty until decontrol at small cost. | expectations | 0.7 | Normal vacancy rate; rent forgone for a few months against the gain from decontrol. | C-12 and C-27 not reported. |
| A-12 | Some job opportunities for sitting tenants would require moving or a much longer commute. | mobility | 0.75 | Size of the region; where jobs are (WE-001 A-12). | C-19 not reported. |
| A-13 | Payments to leave are legal and some sitting tenants accept them. | other | 0.7 | The measure does not regulate them; practice in comparable markets. | C-11 not reported. |
| A-14 | Sitting tenants and owners can organize at a cost below their stake. | other | 0.75 | The ballot campaigns on both sides. | C-14 not reported. |
| A-15 | Some buildings are in the conversion permit process at the effective date, and their owners can withdraw. | other | 0.7 | Pending permit applications. | C-10 rests only on units held off the market. |
| A-16 | Reconverting condominiums to rental is worth its cost for some buildings. | reversal_cost | 0.1 | Number of owners per building; cost of buying out owners. | Below cut-off; not reported. |
| A-17 | Developers had feared that the new-construction exemption would be withdrawn (negation of A-8). | expectations | 0.4 | As A-8. | Below cut-off; the + chain for C-16 is not reported. |
| A-18 | Restoring capacity in formerly covered buildings (major renovation, repair of structural damage, bringing units back into use) takes several years of permits, finance and construction. | durability | 0.85 | Permit times for major alterations; construction lead times; the age of the covered stock. | C-23 comes sooner; its horizon would be medium. |
| A-19 | Developers give a meaningful probability to controls returning, and covering new buildings, within the payback period of a new rental building (ten to fifteen years). | expectations | 0.35 | The original ordinance exempted new construction; size of the repeal majority; strength of tenant organizing after the repeal (C-14). | Below cut-off; the further − chain for C-16 is not reported. |
| A-20 | The city reduces taxes or other borrowing, or funds other spending it would otherwise have cut, by the amount of the board's budget, rather than leaving the saving unused or absorbed by administration elsewhere. | revenue_use | 0.7 | City budget process; whether the board's appropriation is a separate line. | C-25 not reported. |
| A-21 | Under the ordinance, the search, selection, key-money and illegal-sublet margins were open and used (WE-001 A-3, A-15, A-16). | other | 0.8 | WE-001's evidence for those premises; rent board overcharge and sublet complaints. | C-4, C-5, C-6, C-30 and C-31 not reported for the margins that were not used; the C-34 dominance premise is unaffected. |

## 11. Report

**The policy.** Ten years after Riverton froze and capped rents on existing rental units, the city repeals the ordinance. Units that fall vacant can be let at any rent from the effective date. Sitting tenants' rents may rise by at most 15% a year for two years, after which there is no limit; their protection against eviction ends at the same time. The rent board closes after two years. The condominium-conversion permit rules stay.

**Visible consequences.** Sitting tenants pay more than they would have under the ordinance, and their landlords receive more (C-1, C-2).

**Invisible consequences.**
- *People looking for a home in Riverton* find more formerly covered units on offer, with no shortage, less searching, less selection by connections and no key money (C-3 to C-6, C-10). Those who would have obtained a covered unit at the controlled rent now pay the market rent for it (C-28). From the effective date, rents in newer, exempt buildings are lower than they would have been (C-15). In the months before the repeal takes effect, some vacant units are held empty instead (C-12), and exempt rents are higher in those months (C-27). Illegal sublets, and subtenants' disputes settled outside the courts, decline (C-30, C-31).
- *Sitting tenants* move more often, and change jobs more often, once the phase-in ends (C-7, C-19). Some are paid by their landlords to leave early (C-11). Those who cannot pay the higher rent must search for other housing (C-13), in Riverton or in neighboring cities. Those who stay have less to spend on other things (C-33). Maintenance and quality rise (C-8, C-20), but not at once.
- *Owners of covered buildings* see building values rise as soon as the repeal is expected (C-17), convert fewer buildings to condominiums (C-9), and, to the extent they trust the repeal to last ten years or more, invest in major renovation (C-22). The owners who gain are those who own at the announcement, not necessarily those who bore the loss when the ordinance began; later buyers pay the higher price (C-29). Owners have more to spend on other things (C-34) and spend less on board proceedings and permits (C-32).
- *Developers* build less new rental housing than they would have, because the premium that the shortage gave new, exempt units shrinks (C-16).
- *Homebuyers* see fewer new conversions to condominiums (C-18).
- *Taxpayers* stop funding the rent board after two years, provided the city does not redirect its budget (C-25).

**Ambiguous effects.** Whether sitting tenants are better off overall, taking higher rent and higher quality together. Whether rents in neighboring cities rise or fall: some Riverton seekers move back while some displaced tenants move out (C-21). Whether tenants' or owners' lobbying effort rises or falls: both lobbied with the ordinance in force, and both lobby after the repeal, for different ends (C-14).

**What does not reverse.** Buildings converted to condominiums under the ordinance stay condominiums; tenants already displaced by those conversions are not restored; structural damage from deferred maintenance is repaired only over time; and the capital loss borne by owners who sold during the ten years is not returned to them. The formerly covered rental stock grows again (C-23), but at the speed of new investment, held back by the chance that controls return, and without the units already converted.

**Key conditions.** Almost everything rests on controlled rents being well below market rents at the time of repeal (A-1, p = 0.95). The fall in exempt rents from the effective date rests on an accounting identity: sitting tenants who leave free covered units that seekers take. Long-lived investment in the formerly covered stock rests on owners expecting the repeal to last (A-4, p = 0.6). The fall in new construction rests on developers having trusted the exemption (A-8, p = 0.6); if they had not, it would flip.

**What this analysis cannot say.** How large any of these effects will be; how far, or how fast, Riverton's rental market comes to resemble the one it would have had without the ordinance; whether gains to owners and seekers outweigh losses to sitting tenants; whether the repeal is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
|---|---|---|---|---|---|---|---|---|---|
| C-1 | tenants.controlled | price_paid | increase | short–medium | visible | B | PC-3 in reverse, TS-3 | A-1, A-2 | partial (short: the 15% steps); none (from the second anniversary) |
| C-2 | landlords.controlled | net_price_received | increase | short–medium | visible | B | PC-3 in reverse | A-1, A-2 | partial (short: the 15% steps); none (from the second anniversary) |
| C-3 | tenants.prospective | excess_demand (formerly covered units) | decrease | short | invisible | B | PC-1 in reverse | A-1, A-2 | none |
| C-4 | tenants.prospective | search_cost | decrease | short | invisible | B | PC-2 in reverse | A-1, A-2, A-21 | none |
| C-5 | tenants.prospective | allocation_by_non_price_criteria | decrease | short | invisible | B | PC-2 in reverse | A-1, A-2, A-21 | none |
| C-6 | tenants.prospective | side_payments (key money, sublet premiums) | decrease | short–medium | invisible | B | PC-6, RS-3 in reverse | A-1, A-2, A-21 | none |
| C-7 | tenants.controlled | turnover | increase | medium | invisible | B | PC-7 in reverse | A-1, A-6 | none |
| C-8 | landlords.controlled | maintenance_spending | increase | short–medium | invisible | B | PC-4, RS-2 in reverse, TS-5 | A-1, A-3 | partial (A-10) |
| C-9 | landlords.controlled | reclassification (new conversions) | decrease | medium | invisible | B | RS-5, PC-5 in reverse | A-1, A-3 | full for buildings already converted (A-9); none for the flow |
| C-10 | landlords.controlled | quantity_supplied (formerly covered units) | increase | short–medium | invisible | B | PC-5 in reverse | A-1, A-3, A-15 | partial (A-9) |
| C-11 | tenants.controlled | side_payments received (payments to leave) | increase | short | invisible | B | RS-8, LW-5 | A-1, A-13 | n/a (transition) |
| C-12 | tenants.prospective | quantity_traded (vacant covered units, announcement window) | decrease | short | invisible | B | RS-8 | A-11 | n/a (transition) |
| C-13 | tenants.controlled.displaced | search_cost | increase | medium | invisible | B | PC-3 in reverse, OC-2 | A-1, A-6 | n/a (no counterpart) |
| C-14 | tenants.controlled, landlords.controlled | lobbying_effort | ambiguous | medium | invisible | B | RS-7 (repeal clause) | A-14 | n/a |
| C-15 | tenants.prospective | price_substitute (exempt units) | decrease | medium | invisible | B | PC-8 in reverse; CR-12b, CR-12e (accounting identity) | A-1, A-5 | partial (A-9) |
| C-16 | developers | investment_target (new rental) | decrease | medium | invisible | B | PC-8, LW-4 in reverse | A-5, A-8 | partial (buildings built under the ordinance remain) |
| C-17 | landlords.controlled | asset_value (formerly covered buildings) | increase | short | invisible | B | SB-4, TS-5 | A-1, A-2, A-3 | partial (owners who sold under the ordinance do not recover; A-9, A-10) |
| C-18 | homebuyers | quantity_substitute (condominiums from new conversions) | decrease | medium | invisible | B | RS-5 in reverse | A-1, A-3 | partial (A-9) |
| C-19 | tenants.controlled | job_changes | increase | medium | invisible | B | RS-11, PC-7 in reverse | A-1, A-12 | none |
| C-20 | tenants.controlled | quality_per_unit | increase | medium | invisible | B | PC-4 in reverse, TS-1, TS-5 | A-1, A-3 | partial (A-10, A-18) |
| C-21 | renters.neighbors | price_paid | ambiguous | medium | invisible | B | RS-4, PC-3 | A-6, A-7 | none |
| C-22 | landlords.controlled | investment_target (major renovation, formerly covered buildings) | increase | medium–long | invisible | B | PC-5 in reverse, TS-5 | A-1, A-4 | partial (A-10, A-18) |
| C-23 | landlords.controlled | capital_stock_target (formerly covered rental stock) | increase | long | invisible | B | PC-5 in reverse, TS-1, TS-5, TS-6 | A-1, A-4, A-9, A-18 | partial (A-9, A-18) |
| C-24 | tenants.prospective, landlords.controlled | quantity_traded (lettings of formerly covered units) | increase | medium | invisible | B | OC-4 in reverse | A-1, A-2 | partial (A-9) |
| C-25 | taxpayers | resources_available_other_uses | increase | medium | invisible | B | OC-3, OC-1 in reverse | A-20 | none |
| C-26 | officials.enforcement | enforcement_cost (rent board) | decrease | medium | invisible | A | OC-3 in reverse | none | none |
| C-27 | tenants.prospective | price_substitute (exempt units, announcement window) | increase | short | invisible | B | RS-8, PC-8 | A-5, A-11 | n/a (transition) |
| C-28 | tenants.prospective | price_paid (covered units let on vacancy) | increase | short–medium | invisible | B | PC-3 in reverse | A-1, A-2 | none |
| C-29 | buyers.covered_buildings | price_paid (covered buildings) | increase | short–medium | invisible | B | SB-4, OC-7 | A-1, A-3 | none |
| C-30 | tenants.controlled | informal_activity (illegal sublets) | decrease | short–medium | invisible | B | PC-6, RS-3 in reverse | A-1, A-21 | none |
| C-31 | tenants.prospective (subtenants) | disputes_settled_outside_courts | decrease | short–medium | invisible | B | RS-10 in reverse | A-1, A-21 | none |
| C-32 | landlords.controlled | compliance_cost | decrease | medium | invisible | B | OC-2 in reverse | A-1, A-3 | partial (the K3 permit process is not repealed) |
| C-33 | tenants.controlled (those who stay) | resources_available_other_uses | decrease | short–medium | invisible | B | CR-8b (matching C-34) | A-1, A-2 | partial (short: the 15% steps); none (from the second anniversary) |
| C-34 | landlords.controlled | resources_available_other_uses | increase | short–medium | invisible | B | CR-8b; CR-12b with A-2, A-21 | A-1, A-2, A-21 | partial (short: the 15% steps); none (from the second anniversary) |
| — | tenants.controlled | quality_adjusted_price | ambiguous | medium | invisible | B | C-1 vs C-20 | A-1, A-3 | none |

## Gaps found

- GAP-022-1 (closed in catalog 0.3: TS-5). Expectations of re-imposition. C-8, C-17, C-20, C-22 and C-23 now cite TS-5; C-22 raised from Tier C to Tier B on A-4 (p = 0.6); the developers' re-imposition chain in section 7 rests on A-19 (p = 0.35) and is listed as a conditional possibility.
- GAP-022-2 (closed in catalog 0.3: TS-6, assumption type `reversal_cost`, `persistence` field). Irreversible changes. A-9, A-10 and A-16 retyped as `reversal_cost`; persistence recorded in the metamorphic check; the rows for WE-001 C-6, C-8, C-9, C-10 and C-14 are no longer Tier C.
- GAP-022-3 (closed in catalog 0.3: TS-1, upward clause). Speed of rebuilding. The lag is stated as A-18 (`durability`); C-23 raised from Tier C to Tier B.
- GAP-022-4 (closed in catalog 0.3: `persistence` may be given per horizon (2.5)). Persistence has no horizon. The `persistence` field compares the repeal with the path on which the ordinance was never imposed, but does not say at what horizon. The effect of conversions on exempt rents (WE-001 C-12) is partial in the medium run and may fall to none in the long run, as new building replaces the converted stock; deferred maintenance (C-6) may be repaired within a decade. One value per consequence forces the analyst to pick a horizon silently. *Proposed fix:* in `02_ontology.md` 2.5, define `persistence` at the consequence's horizon, and allow one value per horizon where they differ (for example "partial (medium); none (long)"), with the `reversal_cost` assumption naming what would end the persistence.
- Catalog 0.5: corrected after the core-only comparison (see ../05_examples_core/WE-022_rent_freeze_repeal_core.md): exempt rents split by window (C-15 decrease from the effective date, resting on the occupancy identity; new C-27 increase in the announcement window); lobbying kept ambiguous under RS-7's repeal clause; added new tenants of covered units (C-28), later buyers of buildings (C-29, OC-7 symmetry), illegal sublets and subtenants' disputes (C-30, C-31, RS-10 in reverse), landlords' compliance cost (C-32) and both sides of the rent transfer (C-33, C-34); `wait_time` dropped from C-4 and the PC-2 margins tied to A-21; C-26 recorded as `enforcement_cost`; the cross-variable total-cost row removed (CR-12c); persistence recorded on every consequence, with the core version's values for rents during the phase-in; metamorphic check rebuilt against WE-001 as corrected for catalog 0.5.
