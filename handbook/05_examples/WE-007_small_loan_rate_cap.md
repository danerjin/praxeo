# WE-007 Interest-rate cap on small consumer loans

Analyst: draft (Handbook 0.3)  |  Rule catalog version: 0.3  |  Status: awaiting expert review

A stylized policy in a fictional state. Rate caps of this kind are common; this one is not modeled on any particular law. The probabilities are illustrative; the evidence column says what a real analysis would cite. A loan is treated as an exchange of present money for future money; its price is the interest and fees, stated as an annual percentage rate (APR), recorded under `price_paid`.

## 1. Policy record

**Wexmoor Small Loan Act.** Wexmoor is a state of about four million people. Before the Act, about 40 companies licensed under Wexmoor's consumer lending law ran about 380 storefronts, and 12 online lenders held Wexmoor licenses. Typical loans were two-week payday loans of $300 to $600 at about $15 per $100 borrowed (roughly 390% APR) and six-month installment loans of $500 to $1,500 at 150% to 250% APR. Banks charge an overdraft fee of about $34. Pawn loans are governed by a separate Pawn Act, which allows fees of up to 15% a month. Some credit unions offer small loans below 28% APR, mostly to members with a history at the credit union.

The neighboring state of Kestria has no rate cap. Its border is 20 minutes from Brannock (Wexmoor's second city, about 300,000 people) and two hours from Wexmoor City. Informal lending (family, employers, street lenders) exists in both states.

The bill was introduced in January, with polls showing wide support; it passed in April and takes effect on October 1. Loans made before October 1 are honored on their original terms; a loan renewed or refinanced after that date is a new loan.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Rate cap | `price_ceiling` | Consumer loans of $2,500 or less | Lenders licensed under Wexmoor's consumer lending law | All-in APR of at most 36%, counting interest, all fees and any product sold with the loan (credit insurance, memberships). | Loans over $2,500. Banks and credit unions (chartered under other laws). Pawn loans (Pawn Act). |
| K2 License reach | `licensing_requirement` (existing, restated) | Any consumer loan to a Wexmoor resident | All lenders, including online lenders based elsewhere | A Wexmoor license is required; loans by unlicensed lenders, and loans above the cap, are void (the borrower owes neither interest nor principal). | As K1 |
| K3 Enforcement | Administration and enforcement | K1, K2 | Department of Financial Institutions; Attorney General | Examinations of licensees; license revocation; civil suits against unlicensed lenders. Lenders based in other states or abroad are hard to reach. Funded from license fees and the general budget. | None |

Unclear provisions:
- **U1.** Whether "earned wage access" products (advances on wages already earned, repaid from the next paycheck, with optional "tips" and fees for fast delivery) are loans. The Act defines a loan as an agreement with an obligation to repay; many such products are written without one. Reading U1-a: products written without a repayment obligation are not loans and fall outside the Act. Reading U1-b: they are loans, and their fees count toward the 36% APR. Readings get no probability; C-19 reports one sign for each.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: fixes the terms of exchange between lenders and borrowers | Yes, for almost all loans under $2,500 (A-1): at 36% APR, a $400 loan for one month earns about $12, less than the cost of processing it and covering expected defaults. | PC, RS, TS |
| K2 | Triangular: prohibits exchanges with unlicensed lenders | Yes in law; its reach depends on enforcement against out-of-state lenders (A-10) | RS-3, RS-10 |
| K3 | Binary: funded by licensees and taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `borrowers.served` | People who still obtain small loans from licensed lenders | Pay at most 36%. |
| `borrowers.unserved` | People who would have borrowed at the old rates but are no longer offered a loan | Must use pawn, overdrafts, late payment, family, unlicensed lenders, or go without. |
| `borrowers.brannock` | Borrowers within reach of the Kestria border | Can borrow at Kestria storefronts. |
| `lenders.licensed` | Wexmoor-licensed storefront and online lenders | Small loans become unprofitable for most borrowers; can lend larger amounts, convert to pawn, or leave. |
| `lenders.prospective` | Would-be entrants | Entry into small-loan lending no longer pays. |
| `lenders.unlicensed` | Online lenders based outside Wexmoor | Face less competition from licensed lenders; risk void loans and suits. |
| `providers.wage_access` (`sellers.substitutes`) | Firms offering wage advances | Outside the Act under reading U1-a; capped like small loans under U1-b. |
| `pawnshops` (`sellers.substitutes`) | Pawn lenders | More demand. |
| `storefronts.kestria` | Lenders and check cashers just across the border | Some Wexmoor customers. |
| `officials.enforcement`, `taxpayers` | Department, Attorney General and their funders | More examination and litigation. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `borrowers.served` | `price_paid` (APR on small loans from licensed lenders) | decrease | short | K1, PC-3 | A-1, A-2 |

The visible effect: anyone who borrows $2,500 or less from a licensed lender pays at most 36% a year, instead of rates of 150% to 390%.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-2 | `lenders.licensed` | `quantity_supplied` (loans of $2,500 or less) | decrease | short | PC-5, RS-6 | A-1, A-3 |
| C-3 | `lenders.licensed` | `number_of_sellers` (storefronts and licensed online lenders) | decrease | short to medium | RS-6, PC-5 | A-1, A-3 |
| C-4 | `borrowers.unserved` | `excess_demand` (for small loans at 36% or less) | increase | short | PC-1 | A-1, A-2 |
| C-5 | `borrowers.unserved` | `allocation_by_non_price_criteria` (credit score, steady employment, existing customer record) | increase | short | PC-2 | A-1, A-2 |
| C-6 | `lenders.licensed` | `variety` (small, short loans offered) | decrease | short | PC-14 | A-1, A-14 |
| C-7 | `lenders.licensed` | `reclassification` (loans written above $2,500; storefronts relicensed as pawnshops) | increase | short to medium | RS-5 | A-1, A-4 |
| C-8 | `lenders.licensed` | `quantity_supplied` (loans made April to September, with longer terms, before the effective date) | increase | short | RS-8 | A-5 |
| C-9 | `lenders.prospective` | `entry_rate` (new storefronts) | decrease | short (from January) | TS-2, RS-6 | A-1, A-6 |
| C-10 | `lenders.licensed`, consumer groups | `lobbying_effort` (lenders for a higher cap or larger exempt loans; consumer groups to cover wage-access products) | increase | medium | RS-7 | A-1 |

C-2 and C-3: lenders do not cut the price to 36%; for most small loans they stop making them. PC-5 is applied at a short horizon because the capital in small-loan lending is mostly the money lent, which comes back within weeks or months and can be lent elsewhere or not at all. The storefronts and trained staff are more specific, and closures follow lease ends (short to medium).

C-5: lenders who stay keep lending to the borrowers least likely to default, who can be served profitably at 36%. Borrowers with thin or poor credit records are the first to be turned away.

C-6 applies PC-14 (rate caps bind hardest on small and short transactions). Because the cost of making and collecting a loan is mostly per loan, not per dollar (A-14), an annual rate cap squeezes small and short loans hardest: a $300 two-week loan earns about $4 at 36%, a $2,000 one-year loan about $400. Lenders who stay therefore offer larger and longer loans and drop the smallest ones. The same rule gives the rise in loan size for borrowers who are still served (C-18).

C-7: loans over $2,500 are exempt, so lenders offer $2,600 installment loans to borrowers who wanted $400, and some storefronts convert to pawnshops, which are governed by the Pawn Act (RS-5).

C-8: loans made before October 1 keep their terms. Lenders gain by making loans in the window, and by writing them for longer terms than usual, so that their pre-cap terms run on after October 1 (RS-8). C-9: from January, when the bill was introduced and expected to pass, new storefronts stop opening (TS-2).

Not reported: lenders adding fees or products to loans that stay under the cap (RS-2). The Act counts all fees and products in the APR, which closes that route; A-12 is below the cut-off (p = 0.3). Also not reported: more borrowing from street lenders (RS-3); A-13 is below the cut-off (p = 0.35).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-11 | `borrowers.unserved` | `quantity_substitute` (pawn loans, bank overdrafts, late payment of bills, borrowing from family or employers) | increase | short | PC-3, RS-1 | small loans and pawn, overdrafts, late payment: `substitute`, partial | A-1, A-7 |
| C-12 | `borrowers.brannock` | `cross_border_purchases` (loans from Kestria storefronts) | increase | short | RS-4 | Wexmoor and Kestria storefronts: `across_border`, close for Brannock | A-1, A-8 |
| C-13 | `storefronts.kestria` | `quantity_traded` (check cashing, money orders, bill payment) | increase | short | RS-9 | small loans and other storefront services: `complement`, note `trip` | A-1, A-8, A-9 |
| C-14 | `borrowers.unserved` | `informal_activity` (loans from unlicensed online lenders) | increase | short | RS-3, PC-6 | | A-1, A-10 |
| C-15 | borrowers from unlicensed lenders | `search_cost` (finding lenders that do not advertise openly) | increase | short | RS-10 | | A-1, A-10 |
| C-16 | `borrowers.unserved` | `price_substitute` (pawn loan fees) | ambiguous (section 7) | short to medium | PC-8 vs RS-5, RS-13 | same as C-11 | A-1, A-4, A-7 |
| C-17 | `lenders.licensed` | `employment` (storefront staff) | decrease | medium | RS-6 | | A-1, A-3 |
| C-18 | `borrowers.served` | `transaction_size` (loans larger and longer than the borrower sought) | increase | short | PC-14, RS-5 | | A-1, A-4, A-14 |
| C-19 | `providers.wage_access` | `quantity_supplied` (wage advances to Wexmoor workers) | U1-a: increase; U1-b: decrease | short to medium | U1-a: PC-8, RS-1, RS-5; U1-b: PC-5, PC-14 | wage advances and small loans: `substitute`, partial | A-1, A-11 |
| C-22 | borrowers from unlicensed lenders | `quality_information` (no license, regulator or legal recourse to check the lender or its terms against) | decrease | short | RS-10 | | A-1, A-10 |

C-13 applies RS-9: borrowers who cross to Kestria for a loan also cash their paycheck and buy money orders there, because these services are sold in the same storefronts. The chain stops at depth 3; the effect on Wexmoor check cashers is the mirror image at the same depth and falls on a group already counted in C-3.

C-14, C-15 and C-22: online lenders without a Wexmoor license face less competition from licensed lenders. Their loans are void under K2, but a borrower who does not know this, or who wants to keep borrowing, still pays. RS-10 applies: such lenders are harder to find, cannot be checked against a license, and disputes go to no regulator.

C-16: two chains meet in the pawn market. Demand moves there from small loans (PC-8); storefronts converted to pawnshops add pawn supply (RS-5, then RS-13). See section 7.

C-18: lenders who stay raise the minimum size and length of loans (PC-14), and some borrowers who are offered only a larger loan (C-7) take it. They borrow more, for longer, than they would have.

C-19 depends on reading U1. Under U1-a, wage advances are an uncapped substitute for small loans: demand moves to them (PC-8, RS-1), and providers that wrote advances with a repayment obligation rewrite them without one to stay outside the Act (RS-5), so more are supplied. Under U1-b, their delivery fees count toward the 36% APR; on a $200 advance repaid in two weeks, a $5 fee is already about 65% APR, so they are capped like small loans and fewer are supplied (PC-5, PC-14).

RS-11 was checked and does not apply: no benefit is tied to a place. Pruned at depth 3: landlords of closed storefronts (diffuse; `factor_owners.specific` with many other tenants).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `borrowers.unserved`, `price_substitute` (pawn fees), short to medium | Demand moves from small loans to pawn (PC-8, C-11). | Storefronts converted to pawnshops add pawn supply (C-7, RS-5, RS-13), as the note to PC-8 anticipates. | None | **ambiguous**. If the Pawn Act's 15% monthly limit binds, pawn fees cannot rise and the extra demand shows up as more items pawned, or turned away, instead. |

Two further questions were considered and not entered as combined consequences, because no variable in the list records them:
- *Borrowers who are still served:* the APR on loans under $2,500 falls (C-1), but some take larger, longer loans than they sought (C-18), so the total charge for meeting a given need may rise or fall. Each of C-1 and C-18 has a clear sign; their combination per need cannot be recorded.
- *Borrowers who are not served:* they now use options they ranked below a small loan at the old price (C-11, C-14). By LW-5, each is worse off by their own ranking at the time of choosing. That is a statement about their rankings, not about money: some substitutes, such as a loan from family, cost less in money, and others, such as overdraft fees, may cost more. The money effect is therefore not signed.

## 8. Time structure

- **January to October (announcement window).** New storefronts stop opening once the bill is expected to pass (C-9). Between April and October lenders write as many loans as they can, on longer terms, because these keep their pre-cap terms (C-8). Borrowers who take such loans carry them past October 1.
- **October and the following months.** Small loans from licensed lenders fall at once (C-2); outstanding loans run off over weeks (payday) to months (installment), so lenders' loan books shrink gradually. Storefronts close as leases end (C-3); staff are let go (C-17).
- **Over the following years, the cap's reach changes in two opposite ways (TS-3).** The $2,500 threshold is fixed in money. As prices and wages rise, a loan of the same real size crosses $2,500 sooner, so more loans fall outside the cap. The 36% rate is also fixed. If lenders' cost of funds and wages rise, the range of loans that can be made profitably at 36% narrows, so within the threshold the cap binds harder. The method cannot say which change dominates; it can say that the cap's coverage will not stay as enacted.
- **Time preference (LW-7).** A loan is the purchase of present money with future money. Borrowers who would have paid 100% or more for money now, rather than a month later, reveal a strong preference for the present (often because of an urgent bill). The cap does not change that preference; it removes one way of acting on it. The exchanges it prevents are those between borrowers with the highest time preference or risk of default and the lenders willing to serve them (C-20).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-20 | `borrowers.unserved`, `lenders.licensed` | `quantity_traded` (small loans) | decrease | Loans that borrowers would have taken and lenders made at rates above 36%. Each side expected to gain: borrowers valued money now above the money repaid later; lenders expected the charges to cover cost and default. | OC-4, LW-7 |
| C-21 | `taxpayers` | `resources_available_other_uses` | decrease | What the Department's examinations and the Attorney General's suits would otherwise have funded, beyond what license fees cover. | OC-3, OC-1 |

Fees paid on overdrafts and late bills by unserved borrowers are not listed as an opportunity cost: they replace loan charges that would have been paid in the counterfactual, so their net effect on these borrowers' resources is not signed (section 7).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Small loans to most current borrowers cannot be made profitably at 36% APR. | binding | 0.9 | Lenders' cost per loan and default rates; experience in places with similar caps. | Most consequences shrink. |
| A-2 | Licensed lenders comply: they do not lend above the cap. | enforcement | 0.85 | Examinations; void-loan penalty; license revocation. | C-1 shrinks; evasion by licensees grows. |
| A-3 | Lenders' capital and staff have other uses (other products, other states, other work). | alternative_uses | 0.85 | Multi-state lenders; storefront lease terms. | C-2, C-3 and C-17 slow down. |
| A-4 | Some borrowers accept loans over $2,500, and the Pawn Act allows storefronts to convert. | other | 0.7 | Underwriting standards; pawn licensing rules. | C-7, C-16 (− chain) and C-18 not reported. |
| A-5 | Lenders can raise volume and lengthen terms between April and October, and know the effective date. | expectations | 0.6 | Loan volumes in the window; lender statements. | C-8 not reported. |
| A-6 | From January, would-be entrants expected the bill to pass. | expectations | 0.8 | Polls; sponsors; legislative calendar. | C-9 starts in April, not January. |
| A-7 | Unserved borrowers have legal substitutes (pawn, overdraft, late payment, family). | substitutability | 0.85 | Bank account holding among borrowers; pawn store locations. | C-11 weakens; more go without. |
| A-8 | Borrowers in Brannock can easily reach Kestria storefronts and may legally borrow there. | mobility | 0.6 | Drive time of 20 minutes; Kestria law on lending to non-residents. | C-12, C-13 not reported. |
| A-9 | Borrowers use the same storefront for loans, check cashing and money orders. | other | 0.7 | Storefront transaction data. | C-13 not reported. |
| A-10 | Some unlicensed online lenders reach Wexmoor borrowers, and enforcement against them is incomplete. | enforcement | 0.7 | Online advertising aimed at Wexmoor; record of suits against out-of-state lenders. | C-14, C-15 not reported. |
| A-11 | Wage advances are a usable substitute for small loans for some borrowers (they have a regular paycheck and access to a provider). | substitutability | 0.65 | Share of small-loan borrowers in regular employment; providers' reach among Wexmoor employers. | C-19 not reported under reading U1-a; under U1-b the decrease still follows, but concerns few borrowers. |
| A-12 | Lenders can add fees or products to capped loans without breaching the all-in APR rule. | other | 0.3 | Text of K1. | Below cut-off; not reported. |
| A-13 | Borrowing from street lenders rises on a meaningful scale. | enforcement | 0.35 | Police reports; surveys of borrowers in places with similar caps. | Below cut-off; not reported. |
| A-14 | A material part of the cost of a small loan is fixed per loan (underwriting, servicing, collection), not proportional to the amount lent. | other | 0.85 | Lenders' cost accounts; the cost per loan relative to the charge on a $300 loan. | C-6 and the PC-14 chain of C-18 not reported; lenders would cut all loan sizes alike. |

## 11. Report

**The policy.** Wexmoor caps the all-in annual rate on consumer loans of $2,500 or less from state-licensed lenders at 36%, where most such loans had cost 150% to 390%. Loans by unlicensed lenders and loans above the cap are void. Banks, credit unions, pawn loans and loans over $2,500 are outside the cap.

**Visible consequences.** People who still borrow small sums from licensed lenders pay far lower rates (C-1).

**Invisible consequences.**
- *Licensed lenders* make far fewer small loans (C-2), close storefronts (C-3) and let staff go (C-17). New lenders stop opening, starting from when the bill was expected to pass (C-9). Before the effective date, lenders write extra loans on longer terms (C-8). Afterwards they lend to the best-qualified borrowers (C-5), offer loans over $2,500 or convert to pawnshops (C-7), and drop their smallest and shortest loans first (C-6).
- *Borrowers who are no longer offered a loan* (C-4) use pawn, overdrafts, late payment of bills and family (C-11), options they ranked below the loan they would have taken (LW-5). Some borrow from unlicensed online lenders, which are harder to find and which they cannot check or complain about to a regulator (C-14, C-15, C-22). Those near the border borrow in Kestria (C-12), and cash their checks there too (C-13). Fewer small loans are made in all (C-20).
- *Some borrowers who are served* take larger, longer loans than they wanted (C-18).
- *Wage-advance providers* supply more advances if products written without a repayment obligation fall outside the Act (reading U1-a), shaping their products to stay outside it; if they are loans under the Act (reading U1-b), they supply fewer (C-19). The Act's text, not this analysis, decides between the readings.
- *Interested groups* lobby over the threshold and coverage (C-10). *Taxpayers* fund part of the enforcement (C-21).

**Ambiguous effects.** Whether pawn fees rise or fall (C-16).

**Key conditions.** The cap must make small loans unprofitable for most borrowers (A-1, p = 0.9). How much of the trade moves to unlicensed online lenders depends on enforcement against lenders outside the state (A-10, p = 0.7). The cap's reach will change as the fixed $2,500 threshold and the fixed 36% rate meet changing prices and funding costs (section 8).

**What this analysis cannot say.** How many borrowers lose access; whether borrowers who are still served pay more or less per need once larger loans are counted; whether borrowers who no longer get loans are better or worse off afterwards than they would have been (LW-5 speaks only to their ranking when they chose); effects on financial distress, health or family life (out of scope for version 1); whether the cap is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | borrowers.served | price_paid (APR) | decrease | short | visible | B | K1, PC-3 | A-1, A-2 |
| C-2 | lenders.licensed | quantity_supplied (loans ≤ $2,500) | decrease | short | invisible | B | PC-5, RS-6 | A-1, A-3 |
| C-3 | lenders.licensed | number_of_sellers | decrease | short–medium | invisible | B | RS-6, PC-5 | A-1, A-3 |
| C-4 | borrowers.unserved | excess_demand | increase | short | invisible | B | PC-1 | A-1, A-2 |
| C-5 | borrowers.unserved | allocation_by_non_price_criteria | increase | short | invisible | B | PC-1, PC-2 | A-1, A-2 |
| C-6 | lenders.licensed | variety (small, short loans) | decrease | short | invisible | B | PC-14 | A-1, A-14 |
| C-7 | lenders.licensed | reclassification | increase | short–medium | invisible | B | RS-5 | A-1, A-4 |
| C-8 | lenders.licensed | quantity_supplied (April–September) | increase | short | invisible | B | RS-8 | A-5 |
| C-9 | lenders.prospective | entry_rate | decrease | short | invisible | B | TS-2, RS-6 | A-1, A-6 |
| C-10 | lenders, consumer groups | lobbying_effort | increase | medium | invisible | B | RS-7 | A-1 |
| C-11 | borrowers.unserved | quantity_substitute | increase | short | invisible | B | PC-3, RS-1 | A-1, A-7 |
| C-12 | borrowers.brannock | cross_border_purchases | increase | short | invisible | B | RS-4 | A-1, A-8 |
| C-13 | storefronts.kestria | quantity_traded (other services) | increase | short | invisible | B | RS-4, RS-9 | A-1, A-8, A-9 |
| C-14 | borrowers.unserved | informal_activity | increase | short | invisible | B | RS-3, PC-6 | A-1, A-10 |
| C-15 | borrowers (unlicensed lenders) | search_cost | increase | short | invisible | B | RS-3, RS-10 | A-1, A-10 |
| C-16 | borrowers.unserved | price_substitute (pawn) | ambiguous | short–medium | invisible | B | PC-8 vs RS-5, RS-13 | A-1, A-4, A-7 |
| C-17 | lenders.licensed | employment | decrease | medium | invisible | B | RS-6 | A-1, A-3 |
| C-18 | borrowers.served | transaction_size (loans larger than sought) | increase | short | invisible | B | PC-14, RS-5 | A-1, A-4, A-14 |
| C-19 | providers.wage_access | quantity_supplied (wage advances) | U1-a: increase; U1-b: decrease | short–medium | invisible | B | U1-a: PC-8, RS-1, RS-5; U1-b: PC-5, PC-14 | A-1, A-11 |
| C-20 | borrowers.unserved, lenders.licensed | quantity_traded (small loans) | decrease | short | invisible | B | PC-5, OC-4, LW-7 | A-1, A-3 |
| C-21 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| C-22 | borrowers (unlicensed lenders) | quality_information | decrease | short | invisible | B | RS-3, RS-10 | A-1, A-10 |

## Gaps found

- GAP-007-1 (closed in catalog 0.3: PC-14 and `transaction_size`). C-6 is now Tier B (PC-14, with the new assumption A-14 on fixed per-loan costs); C-18 is recorded as `transaction_size` increase instead of a qualified `quantity_traded`.
