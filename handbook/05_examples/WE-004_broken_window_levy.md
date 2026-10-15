# WE-004 Storm-window replacement funded by a household levy

Analyst: draft (Handbook 0.2)  |  Rule catalog version: 0.2  |  Status: awaiting expert review

A stylized policy in a fictional town, built on the parable of the broken window (Bastiat, "That Which Is Seen, and That Which Is Not Seen"; Hazlitt, *Economics in One Lesson*, ch. 2). It is the simplest case in the Handbook: one levy, one spending program, one season. Its purpose is to show OC-1 done carefully, including the step most often skipped: asking what would have happened to the windows, and to the levy-payers' money, without the program. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Brackwater Storefront Recovery Program.** Brackwater is a coastal town of about 40,000 people in 16,000 households. On 3 March a windstorm broke about 600 ground-floor shop windows in the town center, and many home windows. The storm happens in both worlds: the counterfactual is "the same storm, and no program". About 70% of the damaged shops carry property insurance that covers glass, with a $500 deductible; most of the insurers are based outside the town. Four local glazing firms employ about 40 glaziers; the nearest other glaziers are 90 minutes away. The council debated the program in public from 6 March and adopted it on 14 March. Its supporters said it would "put 40 glaziers to work for two months, and their wages will be spent in our shops".

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Levy | Lump-sum tax (recorded as `per_unit_tax`; see GAP-004-3) | Households | Every household water account holder | $80 per household, once, on the April water bill, due within 60 days. Unpaid levies are added to water arrears and, for owners, become a lien on the property. Total about $1.28 million. | None |
| K2 Replacement program | In-kind transfer (`lump_sum_subsidy`) | Ground-floor commercial windows broken by the storm and not permanently replaced by 14 March | Town | The town hires the four local firms under emergency contracts at a fixed schedule (about $2,000 per window on average) and replaces every eligible window at no charge to the owner. Owners apply within 30 days with photos; a town inspector verifies. | Home windows; windows already permanently replaced by 14 March (no reimbursement). |
| K3 Administration | Enforcement | K1, K2 | Town finance office and building inspector | Billing, collection, inspection of claims, contract management; funded from the general budget. | None |

Revenue use: all levy revenue pays for K2. The town advances the money from its cash reserve in March and repays the reserve from the levy; any surplus goes to the general fund. The council resolution calls the program "a one-time response to an exceptional storm".

Unclear provisions: whether the town, or the shop owners' insurers, can recover the cost of replaced windows from each other (subrogation). The resolution is silent; assumed that insurers simply pay no claim for windows the town replaced (A-5).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: a forced payment to the town | Yes. Collected with water bills and backed by liens. The amount is fixed per household, so no household can reduce it by changing what it buys or sells: TX-2 (wedge and smaller market) does not apply, and there is no incidence question (DM-1) to settle. | TX-1, OC-1 |
| K2 | Binary: a transfer from the town to shop owners, in kind | Yes, for owners who apply | SB, OC |
| K3 | Binary: funded by taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `households.levy_payers` (`taxpayers`) | All 16,000 households, including the shop owners' own households | Each has $80 less to spend or save; nothing it can do changes that. |
| `shop_owners.damaged.would_replace` | Owners who, without the program, would have replaced their windows within the year at their own or their insurer's expense | Receive free what they would have paid for, or claimed for. |
| `shop_owners.damaged.would_not_replace` | Owners who, without the program, would have boarded up for months, used plastic sheeting, or closed | Receive a window they would not otherwise have bought soon. |
| `insurers` | Property insurers of damaged shops | Claims for windows the town replaces fall away. |
| `glaziers` (`sellers.current`) | The four local firms and their workers | Guaranteed work at a fixed schedule. |
| `homeowners.damaged` (`buyers.current`, other segment) | Households with storm-broken windows at home | Compete with the program for the same glaziers. |
| `sellers.forgone` | Shops, restaurants, service firms and banks where levy-payers would have spent or saved the $80 | Lose that spending. |
| `sellers.recipients` | Shops and firms where shop owners and insurers spend what they no longer pay for windows | Gain that spending. |
| `officials.enforcement`, `taxpayers` | Finance office, inspector, and general-budget funders | New administrative task. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `shop_owners.damaged` | `price_paid` (window replacement) | decrease | short | SB-2 | A-1 |
| C-2 | `glaziers` | `hours_worked` | increase | short | SB-2, LW-4 | A-1, A-2 |
| C-3 | `officials.enforcement` | `tax_revenue` (levy) | increase | short | TX-1 | none |

C-1 is the visible gain: damaged shops get new windows at no charge. C-2 is the "jobs" claim. It is real, but it is smaller than the supporters' figure, because the program creates glazing work only for windows that would not otherwise have been replaced (section 7). With capacity limited (A-3), the extra work arrives mainly as longer hours and a longer busy season, not as more glaziers, so `employment` (headcount) is not reported.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `shop_owners.damaged.would_replace` | `resources_available_other_uses` | increase | short | GAP-004-1 | A-4 |
| C-5 | `insurers` | `resources_available_other_uses` | increase | short | GAP-004-1 | A-5 |
| C-6 | `shop_owners.damaged` | `wait_time` (weeks with boarded windows) | increase | short | RS-8 | A-6 |
| C-7 | `shop_owners.damaged` | `reclassification` (claims for windows broken before the storm or by other causes) | increase | short | RS-5 | A-7 |
| C-8 | `shop_owners`, `homeowners.damaged`, `glaziers` | `lobbying_effort` (cover homes too; repeat after future storms) | increase | medium | RS-7 | A-8 |

C-4 is the step the parable turns on. An owner who would have paid $2,000 for a window anyway now keeps the $2,000 and spends it on something else: the new suit in Bastiat's story. The catalog has no rule for this move (in-kind provision of a good the recipient would have bought anyway works as a cash transfer), so C-4 and C-5 are Tier C. C-6: because only windows not yet replaced on the adoption date qualify, owners who heard the public debate from 6 March had a reason to wait rather than call a glazier, and then to wait in the program's queue.

Not reported: shop owners cutting insurance or storm shutters because they expect the town to pay after the next storm (TS-2). The resolution calls the program one-time; A-9 is below the cut-off (p = 0.4). Not reported: households moving or refusing to pay to avoid an $80 levy backed by a lien (RS-3, RS-4); no plausible margin.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-9 | `homeowners.damaged` | `wait_time`, `price_paid` (home glazing) | increase | short | SB-3, LW-4 | shop and home glazing: `same_market_other_segment`, close | A-3 |
| C-10 | `sellers.recipients` | `quantity_traded` | increase | short | GAP-004-1 | | A-4, A-5, A-10 |
| C-11 | `sellers.forgone` | `employment` | decrease | short | OC-1, GAP-004-2 | | none beyond OC-1 (Tier C by GAP) |
| C-12 | `sellers.recipients` | `employment` | increase | short | GAP-004-1, GAP-004-2 | | A-4, A-10 |

C-9: with the town's emergency contracts first in line, glaziers' hours go to shop windows before home windows, so homeowners wait longer and pay more for whatever capacity is left (SB-3: the subsidized use draws resources from unsubsidized ones). C-9, C-11 and C-12 are at depth 3 and reach diffuse groups of bystanders, so the chains stop there.

Checks. RS-9 (bundled trips): no one changes where they shop, so it does not apply. RS-10 (informal trade): no exchange is forbidden, so none moves underground. RS-11 (lock-in): no benefit is tied to staying in a place.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `glaziers`, `hours_worked`, short | Windows of owners who would not have replaced them (A-2). | Debate and queue delays (C-6) move some work later, but within the same year. Windows of owners who would have replaced them add nothing: that work would have happened anyway. | None needed | **increase** (C-2), but only by the work on windows that would not otherwise have been replaced within the year. Much of that comes out of homeowners' repairs (C-9). |
| Brackwater workers outside glazing, `employment`, short | Shop owners spend what they no longer pay for windows (C-12). | Levy-payers do not spend the $80 (C-11); insurers' saved claims are mostly spent or held outside the town (A-10). | None | **ambiguous**. What would decide it: the share of windows that would have been replaced anyway, where each group spends, and where insurers are based. The glaziers' wages "spent in our shops" are not an addition: they are paid out of the levy, which is spending the levy-payers did not do. |

**What the program changes, compared with the same storm without it.** The storm destroyed the same 600 windows in both worlds; the program cannot undo that loss.

- *Windows that would have been replaced anyway* (the large majority, A-4). The same windows are installed, by the same glaziers, at about the same time. What changes is who pays. Households pay $80 each (C-13) and do without what they would have bought (C-14); shop owners and insurers keep what they would have paid (C-4, C-5) and spend it on something else (C-10). For these windows, the program is a transfer from households to shop owners and insurers, plus administrative costs (C-16). It creates no glazing work.
- *Windows that would not have been replaced soon* (A-2). Here Bastiat's case applies exactly. The town has a window it would not otherwise have had, and the glaziers have work they would not otherwise have had. The levy-payers have, in its place, fewer of the goods they would have bought (C-14), and the people who would have sold those goods have that much less work (C-11). The window is seen; the goods not bought are not.

## 8. Time structure

- Everything reported happens within a year. The levy is collected once, in April and May; the replacements are done by early summer.
- The program changes when windows are replaced, not only who pays. From 6 March, owners had a reason to wait (C-6). Without the program, insured owners would have called a glazier within days. So the program probably delays the average replacement by some weeks, even though it speeds up the replacement of windows whose owners would have boarded up.
- The town advances the money from its reserve in March and is repaid by the levy in April and May. For those weeks, the reserve cannot be used for anything else; this is part of C-16.
- Medium horizon: lobbying to cover homes, or to repeat the program after the next storm (C-8). If the town did repeat it, A-9 would rise above the cut-off and shop owners would begin to insure and protect less (TS-2). Nothing is reported for the long horizon: the windows the storm destroyed are a loss in both worlds, and the program neither adds to nor subtracts from the town's capital in the long run, beyond the windows replaced sooner in place of goods that levy-payers would have bought.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-13 | `households.levy_payers` | `resources_available_other_uses` | decrease | $80 per household: groceries, a meal out, a child's shoes, a home repair, or savings. Households that would have saved it hold smaller deposits, and banks lend that much less. | TX-1, OC-1 |
| C-14 | `sellers.forgone` | `quantity_traded` | decrease | The sales of the goods in C-13 that are not bought. These sellers are in Brackwater and elsewhere; none of them knows the sale was lost. | OC-1 |
| C-15 | `homeowners.damaged` | `quantity_traded` (home window repairs completed within the year) | decrease | Home repairs pushed back because the glaziers are busy with shop windows. | SB-3 |
| C-16 | `taxpayers` | `resources_available_other_uses` | decrease | Staff time for billing, collection, inspection and contracts, and the use of the reserve for two months. | OC-3, OC-1 |

The shop owners' own households pay the levy too; they are inside C-13. For an owner who would have replaced the window anyway, C-4 is far larger than the $80, so as a subgroup they are net receivers.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The town completes the eligible replacements within the year, as contracted. | other | 0.9 | Contracts, firm capacity, the town's record on emergency works. | C-1, C-2 shrink. |
| A-2 | Some damaged-shop owners would not have replaced their windows within the year without the program (uninsured, marginal or about to close). | other | 0.8 | Insurance coverage of town-center shops; vacancy and closure rates; what owners did after earlier storms. | C-2 not reported: the program would then create no glazing work at all, only a transfer. |
| A-3 | Glaziers' capacity is limited in the months after the storm: crews cannot be expanded quickly, and outside firms are far away. | mobility | 0.8 | Number of local crews; backlog after the storm; distance to the nearest other firms. | C-9, C-15 not reported. |
| A-4 | Most damaged-shop owners would have replaced their windows within the year at their own or their insurer's expense. | other | 0.9 | Insurance coverage (about 70%); shops cannot trade for long behind boards; past storms. | C-4, C-10, C-12 weaken; the program becomes mostly the case in A-2. |
| A-5 | Insured owners' claims for windows the town replaced are not paid, and the town does not recover the cost from insurers. | other | 0.65 | Policy wording on losses made good by a third party; whether the town pursues subrogation. | C-5 not reported; the insurers' share of the transfer goes back to the town. |
| A-6 | Owners who heard the debate delayed permanent replacement, and the program's queue is slower than hiring a glazier directly. | expectations | 0.7 | Dates of replacements before and after 6 March; the program's schedule. | C-6 not reported. |
| A-7 | Inspection lets through some claims for windows not broken by the storm. | enforcement | 0.6 | Photo-only applications; one inspector for about 600 claims. | C-7 not reported. |
| A-8 | Homeowners and shop owners organize to extend the program to homes or to future storms. | other | 0.6 | Council meeting attendance; existing business association. | C-8 not reported. |
| A-9 | Shop owners come to expect the town to pay after future storms. | expectations | 0.4 | Council's "one-time" resolution; history of repeated relief in the region. | Below cut-off; the TS-2 chain is not reported. |
| A-10 | Insurers spend or hold most of the claims they no longer pay outside Brackwater. | other | 0.8 | Where the insurers are based. | The minus chain in section 7 weakens (the sign is still ambiguous). |

## 11. Report

**The policy.** After a storm broke about 600 shop windows, Brackwater pays local glaziers to replace every one that had not yet been replaced, free to the owner. It funds this with a one-time levy of $80 on every household.

**Visible consequences.** Damaged shops get new windows without paying (C-1). Glaziers work more hours (C-2). The town collects the levy (C-3).

**Invisible consequences.**
- *Every household* has $80 less to spend or save (C-13), and the shops, restaurants and banks where it would have gone lose that business (C-14), and with it some work (C-11).
- *Shop owners who would have replaced their windows anyway*, and *their insurers*, keep the money they would have spent (C-4, C-5) and spend it elsewhere (C-10, C-12). For these windows, which are most of them, the program does not create glazing work at all: it changes who pays.
- *Shop owners generally* may wait longer for their windows, because only windows not yet replaced on the adoption date qualified (C-6). Some claims will be for windows not broken by the storm (C-7).
- *Homeowners with broken windows* wait longer and pay more, because the glaziers are busy with shop windows first (C-9, C-15).
- *Taxpayers* fund the administration (C-16). Some groups will press to extend the program to homes or future storms (C-8).

**Ambiguous effects.** Whether total employment in Brackwater outside glazing is higher or lower. Spending moves from households to shop owners and insurers; the method cannot say which group spends more of it in town.

**Key conditions.** The share of windows that would have been replaced anyway (A-4, p = 0.9) decides what the program mostly is: a transfer from households to shop owners and insurers. Only for the remaining windows (A-2, p = 0.8) does the program add glazing work, and that work replaces the goods that levy-payers would have bought.

**What this analysis cannot say.** How many windows fall in each group; how large any effect is; whether the transfer is fair or the program worthwhile. Safety effects of boarded windows are out of scope for version 1.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | shop_owners.damaged | price_paid (window replacement) | decrease | short | visible | B | SB-2 | A-1 |
| C-2 | glaziers | hours_worked | increase | short | visible | B | SB-2, LW-4 | A-1, A-2 |
| C-3 | officials.enforcement | tax_revenue (levy) | increase | short | visible | A | TX-1 | none |
| C-4 | shop_owners.damaged.would_replace | resources_available_other_uses | increase | short | invisible | C | GAP-004-1 | A-4 |
| C-5 | insurers | resources_available_other_uses | increase | short | invisible | C | GAP-004-1 | A-5 |
| C-6 | shop_owners.damaged | wait_time | increase | short | invisible | B | RS-8 | A-6 |
| C-7 | shop_owners.damaged | reclassification (ineligible claims) | increase | short | invisible | B | RS-5 | A-7 |
| C-8 | shop owners, homeowners, glaziers | lobbying_effort | increase | medium | invisible | B | RS-7 | A-8 |
| C-9 | homeowners.damaged | wait_time, price_paid (home glazing) | increase | short | invisible | B | SB-3, LW-4 | A-3 |
| C-10 | sellers.recipients | quantity_traded | increase | short | invisible | C | GAP-004-1 | A-4, A-5, A-10 |
| C-11 | sellers.forgone | employment | decrease | short | invisible | C | OC-1, GAP-004-2 | none |
| C-12 | sellers.recipients | employment | increase | short | invisible | C | GAP-004-1, GAP-004-2 | A-4, A-10 |
| C-13 | households.levy_payers | resources_available_other_uses | decrease | short | invisible | A | TX-1, OC-1 | none |
| C-14 | sellers.forgone | quantity_traded | decrease | short | invisible | A | OC-1 | none |
| C-15 | homeowners.damaged | quantity_traded (home repairs within the year) | decrease | short | invisible | B | SB-3 | A-3 |
| C-16 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| — | Brackwater workers outside glazing | employment | ambiguous | short | invisible | C | C-12 vs C-11 | A-4, A-10 |

## Gaps found

- GAP-004-1: No rule says what happens when the state provides, in kind, a good the recipient would have bought anyway. Needed for C-4, C-5, C-10, C-12. Proposed new SB rule "In-kind provision of a good the recipient would have bought anyway": for those recipients (and anyone, such as an insurer, who would have paid for it), `resources_available_other_uses` increase and `quantity_traded` increase where they spend it; the quantity of the provided good rises only for recipients who would not have bought it. Assumes: the share who would have bought anyway (`other`). Tier B. Builds on LW-1.
- GAP-004-2: OC-1 stops at `quantity_traded` decrease in the markets where the money would have been spent; no rule carries this on to `employment` in those markets (Bastiat's tailor), or carries the mirror case from GAP-004-1 to employment where recipients spend. Needed for C-11 and C-12. Proposed new OC rule "Diverted spending diverts work": where `quantity_traded` falls (rises) in a market because spending is diverted, `employment` or `hours_worked` in that market decrease (increase). Assumes: sellers adjust labor to sales (`alternative_uses`). Tier B. Builds on OC-1, LW-4.
- GAP-004-3: The instrument list (2.3) has `lump_sum_subsidy` but no lump-sum tax. K1 had to be recorded as a `per_unit_tax` on households, although TX-2 does not apply to it. Proposed fix: add instrument `lump_sum_tax` (binary, TX family), with a note that TX-1 and OC-1 apply and TX-2, TX-9 and DM-1 do not, because no one can reduce the tax by changing behavior.
