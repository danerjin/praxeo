# WE-033 / Analysis: Kestland Household Support Payment Act 2027 (one-time household cash payment funded by borrowing)

Analyst: core-only re-run (Handbook 0.7)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Kestland Household Support Payment Act 2027.** Kestland is a country of 9.6 million people. Its address register lists 4.0 million households; the Tax Agency has 4.6 million tax-filing units with an adult member. The economy produces about 420 billion crowns a year. Government debt is about 45% of that, and the government sells about 35 billion crowns of bonds in a typical year; about 30% of its bonds are held abroad. About 35% of households report less than one month's income in liquid savings. A March 2027 survey of intentions found that 30% of households planned to save most of the payment, 40% to pay bills or debts, and 30% to spend it on goods and services. A 2014 energy rebate of 300 crowns per household was followed by higher card spending in the following two months.

**Out of scope.** Monetary policy and the general price level are out of scope in version 1. The analysis does not ask whether the payment raises prices in general, whether the central bank responds, or whether the bonds end up with the central bank; it takes the bonds as sold to private and foreign buyers, as the Act provides. Where a step can only be answered with monetary analysis, the analysis says so and stops.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Kestland. Outside: non-resident citizens (not eligible), foreign buyers of Support Bonds, foreign sellers of goods that recipients import. | "Households resident in Kestland on 1 April 2027"; "Non-resident citizens are not eligible"; K2 "foreign buyers". |
| Announced / enacted / effective / expires | Announced 4 March 2027 (budget speech). Residence date 1 April 2027. Enacted 29 April 2027. Bond auctions May to August 2027. Direct deposits from 1 July 2027; applications by 31 December 2027, paid within eight weeks (so by about end-February 2028). Repayment installments 2028 to 2037. | Policy record, dates and K1 to K3. |
| Enforcement (who, penalties, resources) | Tax Agency: payment runs, applications, call center, identity checks, funded from K2 (up to 60 million crowns). False claims repaid with a 2,000 crown fine; may be prosecuted as fraud. Bank details changeable online with a password. | K4. |
| Funding | K2 bonds up to 4.1 billion crowns, repaid under K3 from general revenue. | K2, K3. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Payment | `lump_sum_subsidy` (cash) | Households resident on 1 April 2027 | Tax Agency | 1,000 crowns per household, once, tax-free, not counted as income for benefits. Direct deposit from 1 July 2027 to the 3.4 million households with bank details on file; others apply by form with identity documents by 31 December 2027 and are paid within eight weeks. | Non-resident citizens. |
| K2 Borrowing | `government_borrowing` (listed in 2.3 of the ontology; the input record says it had no type) | Ten-year Support Bonds | Treasury | Up to 4.1 billion crowns, auctioned May to August 2027 to banks, pension funds, other private and foreign buyers. Covers payments and up to 60 million crowns of administration. | None |
| K3 Repayment | Budget rule | Principal and interest on K2 | Treasury | Ten equal annual installments from 2028, "from general revenue". No tax named. | None |
| K4 Administration and enforcement | Enforcement | K1 | Tax Agency | As in the enforcement row above. | None |

Unclear provisions:
- **U1.** What a "household" is. U1-a: one payment per registered address (about 4.0 million payments, 4.0 billion crowns, within K2's 4.1 billion with the 60 million of administration). U1-b: one payment per tax-filing unit (about 4.6 million payments, 4.6 billion crowns, about 0.56 billion more than K2 covers; the Act does not say where the rest comes from). Readings get no probability; signs that depend on the reading are given per reading.
- **How the installments are funded (K3).** Treated as assumption A-4 (p 0.45), as the input states. Since A-4 is below the cut-off, no consequence that needs "taxes rise" is reported; the payers are recorded as a group (CR-8, clarification on payers from the general budget).

Counterfactual law: the same country and years with no payment, no Support Bonds and no installments. Existing tax and benefit rules are unchanged; without K1's provision, a payment of this kind would not exist at all, so "not counted as income for benefits" only prevents K1 from reducing anyone's benefits (no benefit consequence is recorded).

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Payment | binary (state gives) | Yes: paid to every eligible household that has bank details or applies | 4 (means transferred to each household, conditioned on no choice after 1 April 2027); 2 (adds the option "apply by form" for those without bank details); 3 (form, identity documents and waiting attached to that option); per reading: U1-b adds a second payment for a second filing unit at an address, so it attaches a payment to the option "file separately" (op 3, dated 1 April 2027) | CR-3b, CR-4 ("a change in means alone", "means over time", "saving is a use"), CR-8b, CR-8c, CR-10a, CR-7b |
| K2 Borrowing | binary (state borrows by voluntary exchange) | Yes: up to 4.1 billion crowns, A-3 for its effect on rates | 2 (adds the option "lend to the state at ten years" for bond buyers); 4 for no one directly: the sale is a voluntary exchange (CR-5) | CR-5, CR-6, CR-7a, CR-7c, CR-8a, CR-8 (borrowing clarification), CR-9, CR-10a, CR-10c |
| K3 Repayment | binary (state takes later) | Yes for interest; for principal, A-11 | 4, dated 2028 to 2037: means transferred from taxpayers or recipients of other spending (group; A-4 below the cut-off) to bondholders | CR-8b, CR-8 (payers from the general budget), CR-4 ("means over time"), CR-10a |
| K4 Administration and enforcement | binary (60 million crowns used up) | Yes | 4 (means to the Tax Agency); 3 (repayment, 2,000 crown fine and prosecution risk attached to false claims; a password attached to changing bank details) | CR-8c, CR-4 (x: claim honestly, y: claim falsely) |

No component fixes a price or a quantity in a private market, so CR-6 enters only through markets the payment and the borrowing reach (loans, goods recipients buy), where prices are free. The one fixed quantity is K2's cap of 4.1 billion crowns, which binds only under U1-b.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| households.recipient | All households paid under K1 | Op 4: +1,000 crowns once (Jul 2027 to Feb 2028). Split by response (CR-1 clarification): |
| households.recipient.spending | Recipients who spend part on present goods (A-1) | Same op 4; CR-4 (change in means), CR-4 (means over time, A-12). |
| households.recipient.saving_or_repaying | Recipients who save part or repay debt (A-2) | Same op 4. |
| households.borrowing_in_advance | Recipients who borrow against the payment before July (A-5) | Op 4 expected from 4 March (CR-10a): the option "borrow now, repay from the payment" improves. |
| households.would_have_borrowed | Recipients who would have borrowed in Jul–Dec 2027 for routine purchases (A-6) | Op 4 replaces the option "borrow". |
| households.applicant | Recipients without bank details on file (about 0.6 million under U1-a) | Op 2 (apply) with op 3 (form, documents, wait of up to eight weeks). |
| households.multi_filing_unit_address | Addresses with more than one tax-filing unit (about 600,000) | Per reading: U1-a one payment per address; U1-b one per filing unit, and op 3 on "file separately" before 1 April 2027 (A-7). |
| co_resident_separate_filers | Adult children and lodgers who file separately | U1-a: no direct payment (the address is paid); U1-b: own payment (op 4). |
| non_resident_citizens; arrivals after 1 April 2027 | Excluded | No operation: options unchanged; CR-4a: none responds on account of K1. |
| taxpayers, recipients_of_other_spending | Those who fund K3 (2028–2037), and the U1-b shortfall in 2027–2028 | Op 4 (dated): means taken by taxes or by lower other spending; which one is A-4 (p 0.45), so recorded as a group. |
| lenders.bond_buyers (banks, pension funds, other private, buyers.foreign) | Buy Support Bonds | Op 2: a new lending option; voluntary (CR-5). |
| borrowers.private | Borrowers for business investment and home purchases (A-8), incl. variable-rate borrowers under existing contracts | Through CR-9: compete with the state for the same lenders' means. |
| lenders.consumer_credit | Card, payday and advance-product lenders | Through CR-9: more advances before July (A-5); fewer new loans Jul–Dec (A-6); early repayments (A-2, contract relation). |
| sellers.consumer_goods, owners.consumer_businesses | Sellers of what recipients buy | Through CR-9 (exchange): more buyers at each price in Jul–Dec 2027. |
| workers.consumer_sectors | Staff of those sellers | Through CR-9 (input_to): sellers adjust staff or hours (A-9). |
| sellers.investment_goods_and_construction, workers.investment_goods_and_construction | Sellers to borrowers.private and their staff | Through CR-9 (exchange, input_to): fewer buyers if loans fall (A-8). |
| holders.existing_bonds_and_fixed_rate_loans | Owners of fixed-yield assets | Through CR-7c and CR-10c: value moves with expected rates. |
| homeowners | Owners of homes bought largely with loans | Through CR-7c, CR-10c and CR-9 (homes complement mortgage loans). |
| sellers.foreign (imports), buyers.foreign (bonds) | Across the currency link | Through CR-9 (currency). |
| claimants.false | Those who divert payments or claim twice (A-14) | Op 3: a false claim now brings a payment, with K4's penalty attached. |
| households.defrauded | Recipients whose payment is diverted | Time spent reporting and reclaiming. |
| officials.tax_agency, officials.treasury, officials.prosecution | Administer K1, K2, K4 | Op 4 (60 million crowns); tasks; fines received; prosecutions. |
| retailers.association | Possible lobby for a repeat | CR-4 (x: accept, y: lobby): needs A-13 (p 0.45), so not reported. |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose situation K1, K2 and K4 change.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | households.recipient | resources_available_other_uses | increase | short (Jul 2027 to Feb 2028) | CR-1 op 4, CR-8b, CR-3b | - |
| C-2 | officials.tax_agency | subsidy_outlay | increase | short | CR-1 op 4, CR-8b | - |
| C-3 | lenders.bond_buyers | quantity_traded (Support Bonds, May–Aug 2027) | increase | short | CR-1 op 2, CR-5 | - |
| C-4 | officials.tax_agency | enforcement_cost | increase | short | CR-1 op 4, CR-8c | - |
| C-5 | taxpayers, recipients_of_other_spending | resources_available_other_uses | U1-a: no_change; U1-b: at_least_one_decrease | short (2027–2028) | CR-8b, CR-8 (payers from the general budget), CR-3c | - |

C-1 holds under both readings: under U1-b more households are paid (4.6 million against 4.0 million). C-2 is about 4.0 billion crowns under U1-a and about 4.6 billion under U1-b; increase under both. C-5: under U1-a, K2 covers the payments and administration (4.06 ≤ 4.1 billion), so no general-budget money is needed in 2027–2028; under U1-b about 0.56 billion crowns more is due than K2 provides, and the Act does not say whether it comes from other spending, taxes, more borrowing or delay to late applicants: at least one of these payers bears it.

## 5. Responses

CR-4 applied to every pair of options each class has; CR-5 for exchanges; CR-10a for timing. Windows: announcement (4 March to 30 June 2027); payment (July to December 2027).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | households.recipient | consumption | increase | short (Jul–Dec 2027) | CR-4 (change in means; A-1 names the use), CR-4 (means over time, A-12), CR-12a, CR-12b with A-N4 | A-1, A-N1, A-N4 |
| C-7 | households.recipient | saving | increase | short (Jul–Dec 2027) | CR-4 (change in means; saving is a use; A-2 names it); CR-4 (means over time, A-12) | A-2 |
| C-8 | households.borrowing_in_advance | consumption | increase | short (Mar–Jun 2027) | CR-10a, CR-4 (x: wait for the payment, y: borrow now and repay from it) | A-5 |
| C-9 | lenders.consumer_credit | quantity_traded (advance loans and card credit, Mar–Jun 2027) | increase | short (Mar–Jun 2027) | CR-10a, CR-5, CR-9 (exchange) | A-5 |
| C-10 | lenders.consumer_credit | quantity_traded (new consumer credit, Jul–Dec 2027) | decrease | short (Jul–Dec 2027) | CR-4 (x: borrow, y: pay from the payment), CR-9 (exchange) | A-6 |
| C-11 | households.would_have_borrowed | resources_available_other_uses | increase | short (2028) | CR-10b, CR-8b, CR-3c | A-6 |
| C-12 | households.multi_filing_unit_address | reclassification (separate tax-filing units formed by 1 April 2027) | U1-a: no_change; U1-b: increase | short (Mar–Apr 2027) | CR-1 op 3 (dated), CR-4 (x: one filing unit, y: two), CR-4a, CR-10a | A-7 |
| C-13 | co_resident_separate_filers | resources_available_other_uses | U1-a: no_change; U1-b: increase | short | CR-1 op 4, CR-8b | - |
| C-14 | households.applicant | compliance_cost | increase | short | CR-1 op 2 and op 3, CR-2, CR-8c | - |
| C-15 | claimants.false | legal_breach (diverted payments, duplicate and false claims) | increase | short | CR-1 op 3, CR-4 (x: comply, y: violate) | A-14 |
| C-16 | claimants.false | resources_available_other_uses | increase | short | CR-8b | A-14 |
| C-17 | households.defrauded | compliance_cost (reporting and reclaiming) | increase | short | CR-1 op 3, CR-8c | A-14 |
| C-18 | officials.tax_agency | non_tax_receipts (repayments and fines) | increase | short; medium | CR-1 op 3, CR-8b | A-14, A-N5 |
| C-19 | officials.prosecution | enforcement_cost | increase | short; medium | CR-8c | A-14, A-N5 |

Responses checked and not recorded: relocation into Kestland before 1 April to qualify (CR-4, x: stay abroad, y: register residence) and separate address registration under U1-a both need a premise that some actors are at the margin for 1,000 crowns; none is in the table. Lobbying for a repeat needs A-13 (p 0.45). Holding back purchases in expectation of a further payment needs A-15 (p 0.25).

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4; chains stopped where noted.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-20 | sellers.consumer_goods | quantity_traded (+), net_price_received (+) (goods and services bought by recipients) | at_least_one_increase | short (Jul–Dec 2027) | CR-9, CR-5, CR-6 | exchange: recipients buy from sellers | A-1, A-N1, A-N4 |
| C-21 | workers.consumer_sectors | employment (+), hours_worked (+) | at_least_one_increase | short (Jul–Dec 2027) | CR-9, LW-10, CR-4 | labor input_to goods sold to recipients | A-1, A-N1, A-N4, A-9 |
| C-22 | owners.consumer_businesses | asset_value | increase | short (from 4 March 2027) | CR-7c, CR-10c, CR-10a | ownership of sellers in the exchange above | A-1, A-N1, A-N4 |
| C-23 | borrowers.private | interest_rate | U1-a: increase; U1-b: ambiguous | short (2027–2028) | CR-9, CR-6, CR-7a, CR-12b, CR-12e | same_market_other_segment: loans to the state and private loans draw on the same lenders; contract for variable-rate loans | A-3, A-1, A-N1 |
| C-24 | borrowers.private | quantity_traded (loans for business investment and home purchases) | U1-a: decrease; U1-b: ambiguous | short (2027–2028) | CR-4c, CR-8a, CR-8 (borrowing clarification) | as C-23 | A-3, A-8, A-1, A-N1 |
| C-25 | sellers.investment_goods_and_construction | quantity_traded | U1-a: decrease; U1-b: ambiguous | short (2027–2028) | CR-9, LW-10 | exchange: borrowers buy equipment and homes from them | A-3, A-8, A-1, A-N1 |
| C-26 | workers.investment_goods_and_construction | employment (-), hours_worked (-) | U1-a: at_least_one_decrease; U1-b: ambiguous | short (2027–2028) | CR-9, LW-10, CR-4 | labor input_to the above | A-3, A-8, A-1, A-N1, A-9 |
| C-27 | lenders.bond_buyers, lenders (all new lending) | return_on_capital | U1-a: increase; U1-b: ambiguous | short (2027–2028) | CR-7a, CR-5c | as C-23 | A-3, A-1, A-N1 |
| C-28 | holders.existing_bonds_and_fixed_rate_loans | asset_value | U1-a: decrease; U1-b: ambiguous | short (from 4 March 2027) | CR-7c, CR-10c, CR-10a | fixed-yield assets same_market_other_segment of new loans | A-3, A-1, A-N1 |
| C-29 | homeowners | asset_value (homes) | U1-a: decrease; U1-b: ambiguous | short (2027–2028) | CR-9, CR-7c, CR-10c | homes complement mortgage loans | A-3, A-8, A-1, A-N1 |
| C-30 | economy-wide (owners of capital) | capital_stock_economy | U1-a: decrease; U1-b: ambiguous | long | CR-8a, CR-10b | via C-24 | A-3, A-8, A-10, A-1, A-N1 |
| C-31 | borrowers.private | interest_rate | ambiguous | medium; long (2028–2037) | CR-12b over two chains | as C-23 | A-11, A-N6 |
| C-32 | buyers.foreign, sellers.foreign (currency) | exchange_rate | ambiguous | short (2027) | CR-9 (currency), CR-6, CR-12b | currency | A-N2, A-N3, A-1, A-N1 |
| C-33 | taxpayers, recipients_of_other_spending | resources_available_other_uses | at_least_one_decrease | medium; long (2028–2037) | CR-8b, CR-8 (payers from the general budget; borrowing), CR-3c, CR-12d | budget: installments paid to bondholders | A-11 |

Stopping points: C-26 and C-29 are depth 3 from K2 (borrowing, then rate, then borrowers' purchases or asset prices); the chain from C-26 to the suppliers of those sellers is a diffuse bystander effect and is pruned. C-32 stops at the exchange rate (depth 2): the next links (exporters' and importers' prices in crowns) would inherit an ambiguous sign, and the effect of the exchange rate on prices in general is out of scope.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise (CR-12e) | Combined sign |
| --- | --- | --- | --- | --- |
| households.recipient, consumption, Jul–Dec 2027 | change in means spent in part on present goods not otherwise bought (CR-4, A-1, A-N1); for households without other credit, the payment financed by later installments is a loan at the state's rate (CR-4 means over time, A-12) | higher interest rates make buying now on credit dearer, and paying more on deposits makes saving more rewarding (CR-4 with x: buy now, y: save or wait; with CR-4's means exception for savers) | Empirical: A-N4 (p 0.6), rates on household deposits and on card and payday credit move little in 2027, so the (-) chain does not reach these households' choices in that window | increase (C-6) |
| households.recipient, saving, Jul–Dec 2027 | part of the payment saved or used to repay debt (A-2); households expecting to bear the installments keep part to meet them (A-12) | none derived in this window (advance borrowing is in Mar–Jun, C-8) | not needed | increase (C-7) |
| borrowers.private, interest_rate, 2027–2028 | the state's added demand for loans of about 4.1 billion crowns, with loan supply not perfectly elastic (CR-6, CR-7a, A-3) | recipients' saving, debt repayment and borrowing avoided add to loan supply or reduce loan demand (C-7, C-10, A-2, A-6) | U1-a: accounting identity on the first round: what recipients add to loan supply is at most the payments (about 4.0 billion) less the part spent on goods not otherwise bought (A-1, A-N1: greater than zero), which is less than the bonds sold (about 4.06 billion). U1-b: payments (4.6 billion) exceed the bonds, and the source of the rest is unclear, so the identity does not settle it | U1-a: increase; U1-b: ambiguous (C-23) |
| borrowers.private, quantity_traded (loans), 2027–2028; and C-25 to C-30 | follow C-23 | follow C-23 | as C-23 | per reading, as C-23 |
| borrowers.private, interest_rate, 2028–2037 | payers meet part of the installments by saving or lending less (A-N6) | principal returned to bondholders is lent again (A-11, CR-7a) | none stated | ambiguous (C-31) |
| exchange_rate, 2027 | recipients buy some imports with the payment, so more crowns are offered for foreign currency (A-N3, A-1, A-N1) | foreign buyers of Support Bonds buy crowns they would not otherwise have bought (A-N2) | none stated | ambiguous (C-32) |
| taxpayers, recipients_of_other_spending, resources_available_other_uses, 2028–2037 | - | interest from general revenue (K3 text; no premise); principal on the ten-year schedule (A-11) | not needed: independent chains with the same sign (CR-12d) | at_least_one_decrease (C-33) |
| households.recipient, resources_available_other_uses, whole period 2027–2037 | the payment (C-1) | the share of the installments a household bears (C-33), which includes interest | none: no premise compares a given household's share with 1,000 crowns; A-4 (taxes) is below the cut-off | not reported (CR-12g: C-1 and C-33 are separate horizons) |
| lenders.consumer_credit, quantity_traded | Mar–Jun 2027 (C-9) | Jul–Dec 2027 (C-10) | different windows (CR-12g) | increase (Mar–Jun); decrease (Jul–Dec) |

No pair of chains cancels by construction (CR-12f).

## 8. Time structure

- **Announcement window (4 March to 30 June 2027).** The payment was expected from 4 March (CR-10a). Households that borrow against it consume more in this window (C-8), and advance lending rises (C-9). Expected issuance of 4.1 billion crowns of bonds moves the value of existing fixed-yield assets and of businesses selling to recipients from the announcement (C-28, C-22; CR-7c: borne or captured by whoever holds them when the change becomes expected, part of the way on 4 March and the rest as passage on 29 April became certain).
- **Qualifying date (1 April 2027).** Under U1-b, households had four weeks between the announcement and the residence date to form separate filing units (C-12). After 1 April no choice changes eligibility, so K1 is a pure transfer to those paid: by CR-7b, a payment conditioned on no option that a seller controls settles on the recipient (no price-level effect is analyzed).
- **Payment window (July 2027 to February 2028).** Direct deposits from 1 July, applications to 31 December, paid within eight weeks. Spending and saving rise (C-6, C-7); new consumer borrowing falls (C-10). The Tax Agency's processing capacity is fixed by its budget, so applicants wait up to eight weeks (CR-6, public supply clarification); without the policy there is no payment to wait for, so this is a path note, not a consequence.
- **Timing shifts (02_ontology.md, 2.5).** (1) Advance borrowing: consumption by advance borrowers rises in Mar–Jun 2027 (C-8); their consumption in Jul–Dec 2027 against the no-payment path depends on the fees they pay, which no premise states, so it is not signed. (2) Borrowing avoided: loans not taken in Jul–Dec 2027 (C-10) are loans not repaid in 2028, so those households have more for other uses in 2028 (C-11). (3) Early repayment of existing debt (A-2) moves lenders' receipts from later years into 2027 (contract relation); per-window signs on lenders' receipts would need a premise on which debts would otherwise have been repaid and when, so this is a note.
- **Rates during issuance and repayment.** The rate effect is signed for 2027–2028 only (A-3's window). During repayment (2028–2037) it is ambiguous (C-31). After 2037, with the bonds repaid (A-11), no rate effect is derived.
- **Durability.** Investment not made in 2027–2028 is a missing addition to a stock that changes only through flows (CR-10b). Under A-10 it is not fully made up, so the capital stock is lower in the long run (C-30), after the payment, the bonds and the installments are all over. Persistence (in the sense of the normal form, which is for repeals) is not applicable; the plain statement is that C-30 outlasts the policy.
- **Consumer-sector effects are temporary.** C-20 to C-22 hold for the payment window. From 2028, payers of the installments have less to spend (C-33), but on which uses CR-4 does not say ("a change in means alone"), so no sign is given for consumer sellers after 2027.
- **Expectations of a repeat.** The Act and the government call the payment one-time; holding back purchases to wait for another (A-15, p 0.25) and lobbying for one (A-13, p 0.45) are below the cut-off.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-33 | taxpayers, recipients_of_other_spending | resources_available_other_uses | at_least_one_decrease | Purchases, saving or public services forgone in 2028–2037 to pay principal and interest | CR-8b, CR-8 (payers from the general budget), CR-3c |
| C-5 | taxpayers, recipients_of_other_spending | resources_available_other_uses | U1-a: no_change; U1-b: at_least_one_decrease | Under U1-b, the 0.56 billion crowns not covered by K2 | CR-8b, CR-8 (payers from the general budget) |
| C-4 | officials.tax_agency | enforcement_cost | increase | Up to 60 million crowns of staff and systems that lenders' funds would otherwise have financed elsewhere | CR-8c |
| C-14 | households.applicant | compliance_cost | increase | Time and documents spent applying | CR-8c |
| C-17 | households.defrauded | compliance_cost (reporting and reclaiming) | increase | Time spent recovering diverted payments | CR-8c |
| C-19 | officials.prosecution | enforcement_cost | increase | Investigators' and courts' time | CR-8c |
| C-24 | borrowers.private | quantity_traded (loans for business investment and home purchases) | U1-a: decrease; U1-b: ambiguous | Projects and home purchases not financed because lenders' means went to the state | CR-8a, CR-8 (borrowing clarification) |
| C-25 | sellers.investment_goods_and_construction | quantity_traded | U1-a: decrease; U1-b: ambiguous | Sales of equipment and buildings to those borrowers (the unseen counterpart of C-20) | CR-9, LW-10 |
| C-30 | economy-wide | capital_stock_economy | U1-a: decrease; U1-b: ambiguous | Capital not built | CR-8a, CR-10b |

Both sides of every transfer (CR-8b): the payment to recipients (C-1, C-13) is matched by the bond buyers' loan (C-3, a voluntary exchange, so the lenders' own means are not reduced: they hold the bonds) and, through the lenders' side, by loans not made to private borrowers (C-24); the installments paid by taxpayers or recipients of other spending (C-33) are matched by receipts of bondholders, which return the principal they lent plus interest; diverted payments (C-16) are part of the outlay (C-2); fines and repayments (C-18) are paid by detected false claimants. Administration, applying, reclaiming and prosecution are used up (CR-8c). Bond buyers are not recorded with a fall in `resources_available_other_uses`: they exchanged voluntarily and are not made to pay a sum they cannot avoid (CR-3 note).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Some recipient households spend part of the payment on present goods and services within six months, rather than saving it all or repaying debt. | other | 0.9 | 35% with less than a month's income in liquid savings; survey (30% plan to spend); card spending after the 2014 rebate. | C-6, C-20 to C-30, C-32 fail or lose this chain. |
| A-2 | Some recipient households save part of the payment or use it to repay debt. | other | 0.9 | Survey (30% save, 40% bills or debt). | C-7 fails (its A-12 chain remains, but A-12 alone is not listed as sufficient); the (-) chain in C-23 weakens. |
| A-3 | The supply of loans to Kestland is not perfectly elastic in 2027 and 2028. | other | 0.6 | Support Bonds add about 12% to a typical year's issuance; foreign share 30%; past auctions. | C-23 to C-30 fail. |
| A-4 | The installments are funded mainly by higher taxes rather than lower spending. | revenue_use | 0.45 | Finance Ministry says spending restraint; opposition says taxes; fiscal rules allow either. | Below the cut-off: no reported consequence rests on it. |
| A-5 | Some households borrow against the expected payment before it arrives. | expectations | 0.55 | Advance products advertised after 4 March; card balances before the 2014 rebate. | C-8, C-9 fail. |
| A-6 | Some recipients would have borrowed in July to December 2027 for purchases they now pay with the payment. | other | 0.8 | Share of households using card credit or payday loans for routine purchases. | C-10, C-11 fail. |
| A-7 | For some households, forming a separate qualifying household costs less than a second payment. | other | 0.7 | 600,000 addresses with more than one filing unit; cost of a separate registration or filing. | C-12 (U1-b) fails. |
| A-8 | Most private borrowing at the margin finances business investment and home purchases. | other | 0.75 | Central bank credit statistics by purpose. | C-24 to C-26, C-29, C-30 lose their named uses. |
| A-9 | Sellers adjust staff or hours to sales within months. | alternative_uses | 0.8 | Share of hourly and part-time staff; scheduling practice. | C-21, C-26 fail. |
| A-10 | Investment crowded out in 2027 and 2028 is not fully made up in later years. | durability | 0.6 | Projects deferred or cancelled when rates rise; planning horizons. | C-30 fails. |
| A-11 | The bonds are repaid on the ten-year schedule rather than rolled over. | expectations | 0.6 | Fiscal rules; past practice with special-purpose bonds. | C-33 keeps only its interest chain; C-31's (-) chain fails. |
| A-12 | Many households expect to bear part of the later installments. | expectations | 0.6 | Survey question on expected taxes. | The "means over time" chains in C-6 and C-7 fail; their other chains remain. |
| A-13 | Retailers can organize to press for a repeat payment, and expect a chance of success. | other | 0.45 | Retail association statements; government calls the payment one-time. | Below the cut-off. |
| A-14 | Some payments are diverted by identity fraud, or made twice. | enforcement | 0.7 | Online change of bank details by password; experience of other one-time payments. | C-15 to C-19 fail. |
| A-15 | Many households expect a further payment and delay purchases to wait for it. | expectations | 0.25 | The Act and the government call the payment one-time. | Below the cut-off. |
| A-N1 | Some of the payment that is spent on present goods buys goods that would not have been bought without it, rather than goods that would have been bought on credit anyway (A-6). | other | 0.85 | NEW. A-1 alone does not separate added purchases from purchases moved off credit; the survey's 30% "spend on goods and services" and the 2014 rise in card spending (spending, not only borrowing). | C-6, C-20 to C-22 fail; the dominance argument in C-23 (U1-a) fails, so C-23 to C-30 become ambiguous. |
| A-N2 | Some Support Bonds are bought by foreign buyers with funds they would not otherwise have placed in Kestland in 2027. | other | 0.7 | NEW. 30% of Kestland bonds held abroad; the Act provides for foreign buyers; A-3 says foreign supply is not perfectly elastic, not that it is nil. | C-32's (-) chain fails; C-32 would become increase. |
| A-N3 | Some of the payment is spent on imported goods. | other | 0.85 | NEW. A country of 9.6 million people imports a share of the goods households buy. | C-32's (+) chain fails; C-32 would become decrease. |
| A-N4 | Rates on household deposits and on card and payday credit move little in 2027 in response to the auctions; the higher rate falls mainly on business and mortgage borrowers. | other | 0.6 | NEW. A-8 (marginal borrowing is business and home); deposit and card rates are administered and adjust slowly. | C-6 becomes ambiguous; C-20 to C-22 lose their premise. |
| A-N5 | The Tax Agency detects some false or duplicate claims and recovers repayments and fines. | enforcement | 0.75 | NEW. K4 identity checks; matching of payments to the tax register; fraud provisions in K4. | C-18, C-19 fail. |
| A-N6 | Those who bear the installments meet part of them by saving or lending less, rather than wholly by consuming less. | other | 0.8 | NEW. Saving is a use (CR-4); payers include pension savers and firms. | C-31 becomes decrease. |

**Not reported** (an assumption below 0.5):
- Tax rates are higher in 2028–2037 than without the policy, with taxpayers (rather than recipients of other spending) bearing the installments, and responses to the tax (CR-4): needs A-4 (p 0.45).
- Retailers lobby for a repeat payment (CR-4, x: accept, y: lobby; CR-8c): needs A-13 (p 0.45).
- Purchases held back in 2027–2028 in expectation of a further payment, with per-window signs (CR-10a): needs A-15 (p 0.25).
- Whole-period position of recipients (payment against their share of the installments): needs a premise comparing shares with 1,000 crowns; none at or above 0.5.

**Tier C notes** (no premise in the table; not chains under CR-12):
- Shared facility: Tax Agency staff and the call center also serve ordinary taxpayers; if the 60 million crowns does not cover the work, other services wait longer (CR-9, shared_facility).
- Gift: recipients may pass part of the payment to relatives, including excluded non-resident citizens, or share it within an address under U1-a (CR-5, gift clarification).
- Payers who expect their share of the installments to exceed 1,000 crowns could consume less in 2027 (CR-4, means over time); needs a premise on such expectations.

### Final check before the report

1. **Uncombined chains.** Every key reached by two chains is in section 7: consumption (dominance A-N4), saving, interest rate in 2027–2028 (per reading, identity under U1-a), interest rate in 2028–2037 (ambiguous), exchange rate (ambiguous), payers (same sign), consumer credit (per window). The timing notes in section 8 add no opposing chain to any signed key.
2. **Group signs.** Workers' employment or hours (C-21, C-26), sellers' quantity or price (C-20), and the payers of the installments (C-5, C-33) are groups.
3. **Baseline.** All signs are against the no-payment, no-bond path; diverted payments are not a loss to the defrauded household against that path (only their time is, C-17).
4. **Worse off is not poorer.** Bond buyers and advance borrowers act voluntarily; no `resources_available_other_uses` decrease is recorded for them. It is recorded for payers of the installments, who cannot avoid them.
5. **Timing shifts.** Advance borrowing and avoided borrowing are signed per window (C-8, C-9, C-10, C-11).
6. **Both sides of every transfer.** See the paragraph after section 9.
7. **Every actor class, every core rule.** Table below.
8. **Unstated premises.** Six premises were added (A-N1 to A-N6) and flagged NEW.

| Actor class | CR-4 (pairs) | CR-6 | CR-7 (incl. 7c) | CR-9 (relations) |
| --- | --- | --- | --- | --- |
| households.recipient | spend/save (C-6, C-7); borrow now/wait (C-8); borrow/pay from payment (C-10); one/two filing units (C-12); apply/not (C-14) | not a fixed price | 7b: no capture by sellers (section 8) | exchange (C-20), contract (early repayment, note), gift (Tier C) |
| taxpayers, recipients_of_other_spending | means alone: uses not named | - | - | budget (C-5, C-33) |
| lenders.bond_buyers | lend to state/lend elsewhere (C-3) | loan market (C-23) | 7a (C-27); 7c on existing holdings (C-28) | currency for foreign buyers (C-32) |
| borrowers.private | borrow/defer (C-24) | C-23 | 7c homes (C-29) | exchange (C-25), contract (variable rates, C-23) |
| lenders.consumer_credit | - | - | - | exchange (C-9, C-10), contract (note) |
| sellers.consumer_goods, owners | - | C-20 | 7c (C-22) | input_to labor (C-21) |
| sellers.investment_goods_and_construction | - | - | - | input_to labor (C-26) |
| claimants.false | comply/violate (C-15) | - | - | - |
| officials | - | public supply capacity (note) | - | shared_facility (Tier C) |
| non_resident_citizens | CR-4a: no response | - | - | gift (Tier C) |
| neighbors (proximity) | no relation found: a cash transfer changes nothing done on property next door | - | - | - |

## 11. Report

**The policy:** Every household resident in Kestland on 1 April 2027 receives 1,000 crowns once, tax-free, from July 2027 (by direct deposit, or by application up to 31 December). The money is raised by selling up to 4.1 billion crowns of ten-year bonds to private and foreign buyers in May to August 2027, to be repaid with interest in ten installments from 2028 out of general revenue. Whether "household" means an address or a tax-filing unit is unclear; under the second reading more is due than the bonds raise.

**Visible consequences:** Households receive the payment (C-1), and the Tax Agency pays it out (C-2) and spends up to 60 million crowns administering it (C-4). Bond buyers take up the Support Bonds (C-3). Recipients spend more in the second half of 2027 (C-6), and some households spend more before July by borrowing against the payment (C-8).

**Invisible consequences:**
- *Recipients:* They also save more or repay debt (C-7). Those who would have borrowed for routine purchases borrow less in Jul–Dec 2027 (C-10) and have more left in 2028 (C-11). Those without bank details spend time applying (C-14). Under the filing-unit reading, separate filing units are formed to collect a second payment (C-12), and adult children and lodgers who file separately are paid (C-13).
- *Fraud:* Some payments are diverted or paid twice (C-15, C-16); victims spend time reclaiming (C-17); the Agency collects repayments and fines (C-18) and prosecutors spend resources (C-19).
- *Sellers and workers:* Sellers of what recipients buy sell more or at better prices in Jul–Dec 2027 (C-20), adjust staff or hours upward (C-21), and their businesses gain value from the announcement (C-22).
- *Borrowers, investment and assets (address reading):* The state's borrowing raises the rate private borrowers pay in 2027–2028 (C-23), so fewer business and home loans are made (C-24), sellers of equipment and construction sell less (C-25) and employ fewer people or hours (C-26). Lenders earn more on new lending (C-27); holders of existing bonds and fixed-rate loans (C-28) and homeowners (C-29) see values fall. The capital stock is lower in the long run (C-30). Under the filing-unit reading each of these is ambiguous.
- *Payers:* From 2028 to 2037 taxpayers or recipients of other public spending, or both, have less for other uses, by the principal and interest (C-33). Under the filing-unit reading some of them also bear the shortfall in 2027–2028 (C-5).

**Ambiguous effects:**
- Private interest rates during repayment, 2028–2037 (C-31): returned principal is lent again (lower), while payers save or lend less to pay the installments (higher). What would decide it: how payers fund the installments against how bondholders redeploy the principal.
- The exchange rate in 2027 (C-32): foreign bond purchases bring crowns into demand (lower price of foreign currency), while imports bought with the payment offer crowns (higher). What would decide it: foreign bond purchases against the import share of spending.
- Every rate, lending, investment and asset-value effect under the filing-unit reading (C-23 to C-30), because the payments then exceed the bonds and the source of the rest is unclear.

**Key conditions:** Some of the payment is spent on goods not otherwise bought (A-1, 0.9; A-N1, 0.85), which drives the consumer-sector effects and is the margin by which state borrowing exceeds what recipients return to lenders. Loan supply is not perfectly elastic (A-3, 0.6), which drives the crowding-out chain; marginal borrowing is for business and homes (A-8, 0.75); crowded-out investment is not made up (A-10, 0.6). Household deposit and consumer-credit rates move little (A-N4, 0.6), which settles the consumption sign. The bonds are repaid on schedule (A-11, 0.6). Whether taxes rise (A-4, 0.45) is below the cut-off, so the payers are a group. Six premises were added (A-N1 to A-N6).

**What this analysis cannot say:** How large any effect is; whether recipients as a whole, or any household, end up ahead over 2027–2037; whether taxes or other spending bear the installments (A-4 is below 0.5); and whether the policy is good. Monetary effects are out of scope: whether the payment raises prices in general, whether the central bank responds, and what happens if the bonds end up with it. The dominance argument for the rate rise (C-23) uses only the first round of spending and saving; later rounds of where sellers' receipts go would need monetary analysis, and the analysis stops there. Health, safety and environmental effects are not analyzed.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | households.recipient | resources_available_other_uses | increase | short (Jul 2027 to Feb 2028) | visible | A | CR-1 (op 4: K1 transfers 1,000 crowns, conditioned on no choice after 1 April); CR-8b (the transfer adds to the recipient what it takes from the payer); CR-3b (an added means cannot make the recipient worse off). Holds under U1-a and U1-b (more recipients under U1-b) | - |
| C-2 | officials.tax_agency | subsidy_outlay | increase | short | visible | A | CR-1 (op 4); CR-8b. About 4.0 billion crowns under U1-a, 4.6 billion under U1-b | - |
| C-3 | lenders.bond_buyers | quantity_traded (Support Bonds, May–Aug 2027) | increase | short | visible | A | CR-1 (op 2: a new option to lend to the state); CR-5 (bought only by buyers who rank the bond above the money) | - |
| C-4 | officials.tax_agency | enforcement_cost | increase | short | visible | A | CR-1 (op 4: up to 60 million crowns from K2); CR-8c (resources spent administering are used up) | - |
| C-5 | taxpayers, recipients_of_other_spending | resources_available_other_uses | U1-a: no_change; U1-b: at_least_one_decrease | short (2027–2028) | invisible | A | CR-8b (every payment is a receipt to someone; under U1-b 0.56 billion crowns of payments is not covered by K2); CR-8 clarification (payers from the general budget recorded as a group); CR-3c. Under U1-a K2 covers all payments and administration | - |
| C-6 | households.recipient | consumption | increase | short (Jul–Dec 2027) | visible | B | CR-4 (a change in means alone: spending on some uses rises; A-1 names present goods, A-N1 that some are not purchases moved off credit); CR-4 clarification (means over time: for households without other credit, a payment repaid through later installments is a loan at the state's rate, A-12); CR-12b and CR-12e (the opposing interest-rate chain does not reach these households' choices, A-N4) | A-1, A-N1, A-N4 |
| C-7 | households.recipient | saving | increase | short (Jul–Dec 2027) | invisible | B | CR-4 (a change in means alone; saving and repaying debt are uses, A-2 names them); CR-4 clarification (means over time: households expecting to bear the installments keep part, A-12, an independent chain under CR-12d) | A-2 |
| C-8 | households.borrowing_in_advance | consumption | increase | short (Mar–Jun 2027) | invisible | B | CR-10a (the payment expected from 4 March alters choices now); CR-4 (x: wait for the payment, y: borrow now and repay from it; y made better) | A-5 |
| C-9 | lenders.consumer_credit | quantity_traded (advance loans and card credit, Mar–Jun 2027) | increase | short (Mar–Jun 2027) | invisible | B | CR-10a; CR-5 (exchanges that take place because both expect to gain); CR-9 (exchange: the lenders who sell to advance borrowers) | A-5 |
| C-10 | lenders.consumer_credit | quantity_traded (new consumer credit, Jul–Dec 2027) | decrease | short (Jul–Dec 2027) | invisible | B | CR-4 (x: borrow for routine purchases, y: pay from the payment; y now open, so those who would have borrowed do not); CR-9 (exchange: the lenders lose those loans) | A-6 |
| C-11 | households.would_have_borrowed | resources_available_other_uses | increase | short (2028) | invisible | B | CR-10b (loans not taken in 2027 are not repaid in 2028); CR-8b (repayments and interest not paid to lenders); CR-3c. Timing shift, second window of C-10 | A-6 |
| C-12 | households.multi_filing_unit_address | reclassification (separate tax-filing units formed by 1 April 2027) | U1-a: no_change; U1-b: increase | short (Mar–Apr 2027) | invisible | B | CR-1 (op 3, dated 1 April: under U1-b a second payment attaches to filing separately); CR-10a (announced 4 March); CR-4 (x: one filing unit, y: two; y made better for those for whom the cost is below 1,000 crowns, A-7). U1-a: CR-4a (filing separately brings nothing, so none switches on account of K1) | A-7 |
| C-13 | co_resident_separate_filers | resources_available_other_uses | U1-a: no_change; U1-b: increase | short | invisible | A | CR-1 (op 4 under U1-b only); CR-8b. Under U1-a the address is paid; any share they receive is a gift (Tier C note) | - |
| C-14 | households.applicant | compliance_cost | increase | short | invisible | A | CR-1 (op 2: the option to apply; op 3: form, identity documents and up to eight weeks attached to it); CR-2 (those who apply rank the payment above the cost); CR-8c (time and documents used up) | - |
| C-15 | claimants.false | legal_breach (diverted payments, duplicate and false claims) | increase | short | invisible | B | CR-1 (op 3: a false claim or a changed bank detail now brings 1,000 crowns, with K4's repayment, fine and prosecution attached); CR-4 (x: comply, y: violate; y made better where no payment existed; CR-4a: none becomes more honest because of it) | A-14 |
| C-16 | claimants.false | resources_available_other_uses | increase | short | invisible | B | CR-8b (a diverted payment adds to the fraudster what it takes from the outlay, C-2) | A-14 |
| C-17 | households.defrauded | compliance_cost (reporting and reclaiming) | increase | short | invisible | B | CR-1 (op 3: time attached to recovering a diverted payment); CR-8c. Against the no-payment path, the diverted payment itself is not a loss to them | A-14 |
| C-18 | officials.tax_agency | non_tax_receipts (repayments and fines) | increase | short; medium | invisible | B | CR-1 (op 3: repayment and 2,000 crown fine attached to detected false claims); CR-8b (paid by detected claimants) | A-14, A-N5 |
| C-19 | officials.prosecution | enforcement_cost | increase | short; medium | invisible | B | CR-8c (resources spent prosecuting are used up) | A-14, A-N5 |
| C-20 | sellers.consumer_goods | quantity_traded (+), net_price_received (+) (goods and services bought by recipients) | at_least_one_increase | short (Jul–Dec 2027) | invisible | B | CR-9 (exchange: recipients buy more from them, C-6); CR-5 and CR-6 (more buyers at each price: either more is sold or the terms move toward sellers, at least one); the price level as a whole is out of scope | A-1, A-N1, A-N4 |
| C-21 | workers.consumer_sectors | employment (+), hours_worked (+) | at_least_one_increase | short (Jul–Dec 2027) | invisible | B | CR-9 and LW-10 (relation: labor input_to the goods sold; demand for it follows sales, C-20); CR-4 (sellers adjust staff or hours within months, A-9) | A-1, A-N1, A-N4, A-9 |
| C-22 | owners.consumer_businesses | asset_value | increase | short (from 4 March 2027) | invisible | B | CR-10a (expected from the announcement); CR-10c and CR-7c (a rise in expected yield of limited duration is capitalized for the yields it affects and captured by whoever owns the business on 4 March and as passage becomes certain) | A-1, A-N1, A-N4 |
| C-23 | borrowers.private | interest_rate | U1-a: increase; U1-b: ambiguous | short (2027–2028) | invisible | B | CR-9 (the state competes with private borrowers for the same lenders' means; relation same_market_other_segment; variable-rate loans by contract); CR-6 (more demand for loans at each rate, with supply not perfectly elastic, A-3, moves the rate up); CR-7a (rates across uses brought back into line); CR-12b against recipients' saving and avoided borrowing; CR-12e: U1-a, first-round accounting identity (funds returned by recipients ≤ payments less the part spent on goods not otherwise bought, A-1, A-N1, < bonds sold); U1-b, payments exceed bonds and the source of the rest is unclear | A-3, A-1, A-N1 |
| C-24 | borrowers.private | quantity_traded (loans for business investment and home purchases) | U1-a: decrease; U1-b: ambiguous | short (2027–2028) | invisible | B | CR-4c (at a higher rate the last project, valued least, is dropped; A-8 names the uses); CR-8a and CR-8 clarification (the means lent to the state are not available to other borrowers); sign follows C-23 per reading | A-3, A-8, A-1, A-N1 |
| C-25 | sellers.investment_goods_and_construction | quantity_traded | U1-a: decrease; U1-b: ambiguous | short (2027–2028) | invisible | B | CR-9 (exchange: fewer borrowers buy equipment and homes, C-24); LW-10. The unseen counterpart of C-20 | A-3, A-8, A-1, A-N1 |
| C-26 | workers.investment_goods_and_construction | employment (-), hours_worked (-) | U1-a: at_least_one_decrease; U1-b: ambiguous | short (2027–2028) | invisible | B | CR-9 and LW-10 (relation: labor input_to the sales in C-25); CR-4 (sellers adjust staff or hours, A-9). Depth 4 from K2; chain stops | A-3, A-8, A-1, A-N1, A-9 |
| C-27 | lenders.bond_buyers, lenders (all new lending) | return_on_capital | U1-a: increase; U1-b: ambiguous | short (2027–2028) | invisible | B | CR-7a (the higher rate, C-23, is earned on every movable loan); CR-5c (terms move toward lenders) | A-3, A-1, A-N1 |
| C-28 | holders.existing_bonds_and_fixed_rate_loans | asset_value | U1-a: decrease; U1-b: ambiguous | short (from 4 March 2027) | invisible | B | CR-10a (expected issuance from the announcement); CR-10c and CR-7c (a fixed yield is worth less when the rate at which buyers could lend elsewhere rises; borne by holders when the rise becomes expected) | A-3, A-1, A-N1 |
| C-29 | homeowners | asset_value (homes) | U1-a: decrease; U1-b: ambiguous | short (2027–2028) | invisible | B | CR-9 (relation: homes complement mortgage loans, A-8); CR-10c and CR-7c (a higher rate on the means used to buy homes lowers what buyers will pay for the same expected yield, for the period the rate is higher) | A-3, A-8, A-1, A-N1 |
| C-30 | economy-wide (owners of capital) | capital_stock_economy | U1-a: decrease; U1-b: ambiguous | long | invisible | B | CR-8a (projects not financed in 2027–2028, C-24); CR-10b (a stock changes only through flows; the missing additions are not made up, A-10) | A-3, A-8, A-10, A-1, A-N1 |
| C-31 | borrowers.private | interest_rate | ambiguous | medium; long (2028–2037) | invisible | B | CR-12b: (-) CR-7a, principal repaid to bondholders on schedule (A-11) is lent again; (+) CR-4 (saving is a use) and CR-6, payers meet the installments partly by saving or lending less (A-N6). No dominance premise | A-11, A-N6 |
| C-32 | buyers.foreign, sellers.foreign (currency) | exchange_rate | ambiguous | short (2027) | invisible | B | CR-12b: (-) CR-9 currency link and CR-6, foreign buyers of Support Bonds buy crowns they would not otherwise have bought (A-N2); (+) CR-9 currency link, imports bought with the payment are paid for with crowns offered for foreign currency (A-N3, A-1, A-N1). No dominance premise | A-N2, A-N3, A-1, A-N1 |
| C-33 | taxpayers, recipients_of_other_spending | resources_available_other_uses | at_least_one_decrease | medium; long (2028–2037) | invisible | B | CR-8b (installments paid to bondholders are taken from someone); CR-8 clarifications (payers from the general budget as a group; borrowing implies later payment only if repaid); CR-3c; CR-12d: chain 1, interest from general revenue under K3 (no premise); chain 2, principal on the ten-year schedule (A-11) | A-11 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-033-C1: Rounds of spending after the first. CR-4 ("a change in means alone") and CR-8b follow a sum to its first recipient. To decide whether the state's borrowing raises private rates (C-23), the analysis needed to know whether sellers' receipts from recipients' spending return to lenders, which is a question about the circulation of money. No core rule follows a sum beyond the first exchange, and the monetary rules are out of scope. The dominance argument therefore uses only the first round and says so.
- GAP-033-C2: An entitlement with a capped budget. Under U1-b the Act promises more payments (4.6 billion crowns) than K2 can fund (4.1 billion). CR-8b establishes that someone pays, and CR-6's public-supply clarification covers a fixed quantity at a set price, but no rule covers a fixed sum of money that must meet a larger legal entitlement (delay to late applicants, a supplementary borrowing or a cut elsewhere). Recorded as a group sign (C-5) and a per-reading ambiguity.

**(b) Core-rule wording that was hard to apply.**
- CR-4 "a change in means alone" with A-1: A-1 names present goods as a use, but does not separate added purchases from purchases moved off credit (A-6). Signing consumption against the counterfactual needed A-N1. The rule could say that a named use must be net of uses the transfer merely refinances.
- CR-4 clarification "means over time": it says the borrowed-transfer case "falls under CR-4 proper" for credit-constrained recipients, but not which options are x and y, nor what it implies for recipients who are not credit-constrained (here, saving part, C-7). Applied as x: future goods, y: present goods.
- CR-12e "accounting identity": unclear whether a first-round identity counts as an identity when later rounds are not analyzed (C-23).
- CR-3 note ("worse off is not poorer") and the CR-8 borrowing clarification pull in different directions for bond buyers: CR-8 asks for the lenders' side to be recorded, while CR-3 forbids a fall in their `resources_available_other_uses`. Recorded on the borrowers who lose the loans (C-24) instead.
- CR-7b for a transfer conditioned on no option: the rule speaks of who "keeps a subsidy" through mobility; for a lump sum with a past qualifying date it gives no capture, but the rule does not say so directly.
- Horizons: the normal form has short/medium/long only, while the case turns on dated windows (Mar–Jun 2027, Jul–Dec 2027, 2028). Windows were written into the horizon field.
- `persistence` is defined for repeals only; for a temporary policy with a lasting effect (C-30) there is no field.

**(c) Vocabulary missing from the ontology.**
- Actor classes: no generic class for lenders, borrowers, bondholders or "recipients of other spending" (used in CR-8's clarification but absent from 2.2).
- Relation types: no type for "compete for the same means" (state and private borrowers drawing on the same lenders), which CR-9 names; `same_market_other_segment` was used.
- Variables: no variable for government debt outstanding, for interest paid or received, for the number of claims or payments made, or for receipts by a creditor of repayments; `quantity_traded (loans)` and `subsidy_outlay` were used.
- Instrument types: `government_borrowing` is in 2.3, contrary to the input record's note; no type for a repayment rule (K3) or for a budget cap on an entitlement.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the skeleton of the case: each household gains 1,000 crowns in the payment window, recipients save or repay debt, bond buyers take up the bonds voluntarily, consumer credit rises before the payment and falls after it, applicants bear a compliance cost, the state's borrowing crowds out private borrowing for business investment and homes (on A-3 and A-8), and the payers of the installments from 2028 are recorded as a group of taxpayers and recipients of other spending. Neither version nets the payment against the installments over the whole period. The differences are of four kinds. (1) The pattern version applies the loan-market identity of an address-based payment to both readings of "household"; under U1-b the payments exceed the bonds, so the core version's per-reading signs (increase under U1-a, ambiguous under U1-b) on the rate and everything downstream of it are the correct form. That accounts for seven of the nine sign differences. (2) The pattern version hides a premise that the core version names (A-N1): only purchases that would not otherwise have been made add to the net demand for loans and to sellers' sales; purchases moved off credit (A-6) do not. (3) The pattern version signs later sellers' sales and jobs down (OC-1, OC-5) although the payers may meet the installments by saving less. Its own Q19 finding says the split between present and future is not a priori, and the bondholders who receive the installments are an opposing chain. (4) The core version records much that the pattern version left in prose or omitted: the fraud chain, advance borrowers' consumption, the 2028 window of avoided borrowing, the U1-b shortfall, and home values. Several of these were blocked in 0.6 by vocabulary (`no_change`, `legal_breach`, `consumption`, `interest_rate`) or by rules that 0.7 added. The pattern version was written under catalog 0.6, and several 0.7 clarifications (CR-4 "means over time" and "saving is a use", CR-8 on payers from the general budget and on borrowing, CR-12g on whole-period signs, CR-12 on underivable opposing chains) were drawn partly from this example. The core version made two errors of its own: it dropped the U1-a form of splitting (a separate address), and it signed the value of consumer businesses up without combining it with the rise in rates.

Counts: M 9, V 0, S 9, OP 15, OC 4.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | Recipients' means increase. The core splits co-resident separate filers out per reading (C-13). |
| C-2 | C-4 | M | | Administration `enforcement_cost`. The core records prosecution separately (C-19). |
| C-3 | C-3 | M | | Bond purchases (CR-5). |
| C-4 | C-7 | M | | Saving and debt repayment, A-2. The core adds an independent "means over time" chain on A-12 (CR-4 0.7 clarification, CR-12d). The pattern version reasoned to the same chain in prose and in its Gaps (b), which is the source of that clarification. |
| C-5 | C-14 | M | | Applicants' compliance cost. |
| C-6 | C-12 | S | E (core) | Pattern: "U1-a: increase; U1-b: increase" (separate qualifying households, A-7). Core: "U1-a: no_change; U1-b: increase", with the variable narrowed to separate tax-filing units. Under U1-a a second registered address brings a second payment (CR-1 op 3, CR-4 with x: one household, y: two). A-7 ("forming a separate qualifying household costs less than a second payment"; evidence: "cost of a separate registration or filing") is the premise the core version says is missing in section 5. **Pattern right on the sign.** The pattern's window is wrong, though: it places splitting "around the deposit runs" in July to December, but eligibility is fixed on 1 April 2027. The core's window (March to April 2027, CR-10a) is the right one. |
| C-7 | C-9 | M | | Credit against the expected payment, March to June, A-5. RS-8 asks for both sides of a timing shift, and the borrowers' side appears only in the core (C-8). |
| C-8 | C-10 | M | | New consumer credit falls July to December, A-6. |
| C-9 | C-23 | S | E (pattern) | Pattern: `price_paid` on loans increase. Core: `interest_rate` (added to 2.4 in 0.7) "U1-a: increase; U1-b: ambiguous". The pattern's CR-12e identity ("the net change in demand for loans equals the part of the payment spent") holds only if the payments are wholly borrowed, which is true under U1-a. Under U1-b about 0.56 billion crowns is paid from an unnamed source (the pattern's own section 8). If it comes from cuts to other spending or from the Treasury's cash, the identity no longer settles the sign without a magnitude premise. The pattern version did not split the reading. A dominance premise from the survey figures (recipients' added purchases well above 0.56 billion) could have closed U1-b, but neither version states one, so the core's ambiguity is the sign the rules give. The pattern's identity also needs A-N1 (see Findings). |
| C-10 | C-24 | S | E (pattern) | Private loans decrease. Follows C-9: the pattern gives one sign, the core gives a decrease under U1-a and ambiguous under U1-b. |
| C-11 | C-25 | S | E (pattern) | Sales of investment goods and construction. Same reading issue as C-9. |
| C-12 | C-26 | S | E (pattern) | Employment or hours there, `at_least_one_decrease`. Same reading issue. |
| C-13 | C-20 | S | P | Pattern: sellers to recipients, `quantity_traded` increase. Core: `quantity_traded` or `net_price_received`, `at_least_one_increase`. CR-6 gives more buyers at each price, so at least one of quantity and price rises. Choosing quantity alone needs a premise that supply is not fixed in the short run, which the pattern version does not state (final check 2). Both also need A-N1, which only the core states. **Core right.** |
| C-14 | C-21 | M | | Employment or hours at sellers to recipients, `at_least_one_increase`, A-9. |
| C-15 | C-28 | S | E (pattern) | Value of existing bonds. The core widens the class to fixed-rate loans and dates it from the announcement (CR-10a). Same reading issue as C-9. |
| C-16 | C-27 | S | E (pattern) | Lenders' `return_on_capital`. Same reading issue. |
| C-17 | C-30 | S | E (pattern) | Capital stock, long run, A-10. Same reading issue. |
| C-18 | none | OC | J | `sellers.all`, all goods and services, ambiguous. The core version records the two sides (C-20, C-25) and no aggregate class. Under CR-12c the aggregate is a separate key, so recording it is defensible, but it adds no signed claim. Both versions stop at the same monetary boundary. |
| C-19 | C-33 | M | | Payers of the installments, `at_least_one_decrease` over taxpayers and recipients of other spending. The pattern version anticipated the 0.7 clarification to CR-8 ("payers from the general budget") and proposed it in its Gaps (d). The core adds a chain that holds without A-11: interest is paid from general revenue in any case (CR-12d). The pattern lists only A-11. |
| C-20 | none (core section 8: "no sign is given for consumer sellers after 2027") | OC | P | Pattern: `sellers.later` `quantity_traded` decrease (OC-1). The payers' means fall (CR-8b), but saving is a use (CR-3c, CR-4 0.7 clarification). Fewer purchases by the payers therefore needs a premise like A-1 for the payers, which is absent; the core's A-N6 (p 0.8) holds that they meet part of the installments by saving less. The installments are also received by bondholders, who spend part of them, which is an opposing chain the pattern version did not record. OC-1's "Then" treats forgone means as forgone purchases; that is an overclaim, and inconsistent with the pattern version's own Q19 point 3. **Core right.** |
| C-21 | none | OC | P | Employment or hours at later sellers, `at_least_one_decrease` (OC-5). Falls with C-20. |
| — (all sectors, employment and hours, ambiguous) | none | OC | J | Aggregate of C-14 and C-12. The core records the parts (C-21, C-26) and no aggregate. Nothing scorable is lost. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-2 | OP | E (pattern) | Tax Agency `subsidy_outlay` increase. This is the payer's side of C-1 (CR-8b); the pattern version records it only in prose. |
| C-5 | OP | E (pattern) | U1-b shortfall: "U1-a: no_change; U1-b: at_least_one_decrease" for payers in 2027 to 2028. The pattern version derived it (its section 8) but left it out because 0.6 had no `no_change` value (its Gaps (d)). That value was added in 0.7, so the omission was forced by the vocabulary of the time. |
| C-6 | OP | E (pattern) | Recipients' `consumption` increase, combined with the opposing rate chain (CR-4, x: buy now, y: save) on dominance premise A-N4. The pattern version states the spending in section 5 but records it only through sellers (C-13). 0.6 had no `consumption` variable, and the version never checked the rate chain against recipients' own choices, though its C-9 raises rates. |
| C-8 | OP | E (pattern) | Advance borrowers' `consumption` increase, March to June (CR-10a, CR-4, A-5). RS-8, which the pattern version cites for C-7, requires the borrowers' side as well. |
| C-11 | OP | E (pattern) | Households that would have borrowed have more in 2028, because no repayment is due (CR-10b, CR-8b, A-6). This is the second window of C-8 in the pattern version, whose final check 5 claims per-window signing but omits it. |
| C-13 | OP | J | Co-resident separate filers, "U1-a: no_change; U1-b: increase". It is a per-reading split of the pattern's C-1, and defensible as either. |
| C-15 | OP | E (pattern) | False claimants, `legal_breach` increase (CR-1 op 3, CR-4 comply/violate, A-14). The pattern version discusses fraud and has the premise, but 0.6 had no variable for it (its Gaps (d)). `legal_breach` is in 2.4 in 0.7. |
| C-16 | OP | E (pattern) | False claimants' means increase (CR-8b). This is the receiving side of diverted payments; check 6 (both sides) was missed. |
| C-17 | OP | E (pattern) | Defrauded households' time spent reclaiming (CR-8c). The pattern version rightly says the diverted payment is not a loss against the baseline, but it misses the time, which is one. |
| C-18 | OP | E (pattern) | Repayments and fines received (K4, CR-8b, A-N5). |
| C-19 | OP | E (pattern) | Prosecution's `enforcement_cost` (CR-8c). The pattern's C-2 covers the Tax Agency's checks, not prosecution. |
| C-22 | OP | E (core) | Owners of consumer businesses, `asset_value` increase, from the announcement (CR-7c, CR-10c). The (+) chain is valid: the payment raises expected yields over a limited window. But the same CR-10c that the core applies to bonds (C-28) and homes (C-29) gives a (−) chain from the higher rate of 2027 to 2028 (C-23, U1-a), which lowers the present value of every expected yield. Neither chain dominates without a premise (CR-12b), so the sign should be ambiguous, and under U1-b it should be at most per reading. This is an uncombined chain, error 1 in the final check. The pattern version's final check 7 says "no other asset is tied to the payment", which misses the key but not a sign. |
| C-29 | OP | P | Homeowners, `asset_value` decrease under U1-a (CR-9 complement with mortgage loans, CR-7c, CR-10c, A-8). The pattern version declined to sign it because "recipients' spending (unnamed)" might raise house prices. That opposing chain cannot be derived: no premise names housing as a use (CR-4 "a change in means alone"). Under the 0.7 CR-12 clarification, an underivable opposing effect is a Tier C note, not a cause of ambiguity. The pattern version predates that clarification. |
| C-31 | OP | J | Private rates during repayment, 2028 to 2037, ambiguous (A-11, A-N6). The pattern version did not examine the period. The key is valid but unsigned. |
| C-32 | OP | A | Exchange rate in 2027, ambiguous (CR-9 currency link, A-N2, A-N3). The pattern version lists the exchange rate among the things it cannot say ("out of scope"). The record's scope note excludes only monetary policy and the general price level, so the core's reading of scope is the narrower one. Both are defensible, and the difference is one of premise. |

### Findings

- **Pattern hides a premise (A-1 for the loan-market identity and for sellers' sales).** A-1 says some recipients spend part of the payment on present goods. It does not separate purchases that would not otherwise have been made from purchases moved off credit (A-6). Under the pattern version's own accounting, the second kind returns to the loan market as borrowing avoided. So the net demand for loans rises by the first kind only, and sellers gain only from the first kind too. The core version's A-N1 (p 0.85) is the missing premise behind the pattern's C-9 to C-17 and C-13.
- **Pattern applies a one-reading identity to both readings (C-9 to C-12, C-15 to C-17).** The pattern version derived the U1-b shortfall in section 8 but did not carry it into the rate chain. Where an identity depends on the reading, the sign must be given per reading (CR-1 recording; 2.5).
- **Pattern overclaims (OC-1 and OC-5 for the later payers, C-20 and C-21).** OC-1's "Then" equates means taken with purchases not made. Under CR-3c and the 0.7 CR-4 clarification that saving is a use, it needs a premise that the payers cut purchases, and it must be combined with the bondholders' receipts. OC-1 should carry an `other` premise when the payers can save less instead. The same applies to SB-1's instruction to "apply OC-1 to its funding source".
- **Pattern overclaims (C-13, single member of a group).** CR-6 gives quantity or price; quantity alone needs a premise.
- **Pattern's Gaps (b) on the whole period is overstated.** It says "the arithmetic decides the net direction without any discount rate" for households that pay little later. That arithmetic rests on A-4 (taxes, p 0.45) and on the income-tax distribution; under spending cuts no premise identifies who pays. The 0.7 CR-12g clarification, drawn from this point, now allows a whole-period consequence when a dominance premise holds. The core version correctly found that none clears the cut-off here.
- **Errors in the pattern version (omissions).** The payer side of the outlay (core C-2); the U1-b shortfall (C-5, forced by 0.6 vocabulary); recipients' consumption as its own key, checked against the rate chain (C-6); advance borrowers' consumption (C-8); the 2028 window of avoided borrowing (C-11); the fraud chain (C-15 to C-19, partly forced by 0.6 vocabulary); and the splitting window, which falls before 1 April, not around the deposit runs (C-6). The pattern's refusal to sign home values (C-29) rested on an underivable opposing chain.
- **Errors in the core version.** (1) C-12 under U1-a: the core dismissed registering a separate address as having no premise, but A-7 is that premise. The pattern's "U1-a: increase" is right. (2) C-22: the capitalized gain to consumer businesses is not combined with the discount-rate chain that the core itself applies to bonds and homes, so it should be ambiguous. (3) A judgment, not an error: under U1-b the core could have stated a magnitude premise from the survey (recipients' added purchases exceed the 0.56 billion shortfall) and signed the rate per CR-12e. Without such a premise, its ambiguity is correct.
- **Limits of the core rules.** No difference was caused by the core rules being unable to derive a valid claim (no K). Two real limits remain, and both versions meet them. GAP-033-C1: no rule follows a sum beyond its first recipient, so both versions' rate identity is a first-round argument and stops at the monetary boundary (the pattern version's C-18 says the same). GAP-033-C2: no rule covers a capped budget against a larger legal entitlement. CR-4's "a change in means alone" correctly gives no named use for the recipients or the later payers. That is the right answer to Q19, not a gap. Many core-only consequences here rest on 0.7 clarifications (CR-4 "means over time" and "saving is a use", CR-8 on payers and borrowing, CR-12 on underivable chains and whole-period signs) and on 0.7 vocabulary (`no_change`, `consumption`, `interest_rate`, `legal_breach`, `government_borrowing`). Those were drawn partly from this example's own Gaps section, so this comparison is not a fully independent test of them.
