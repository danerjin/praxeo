# Pilot: deriving consequences from the core rules alone

**Question.** Can the engine reason from the core rules (CR-1 to CR-12, `handbook/04a_core_rules.md`) directly, instead of from the instrument patterns of `04_rules.md`? The pattern files grow by one per instrument, and most rows they miss out of sample are "missing rule": things a core rule derives but no pattern covers.

**What was built.**
- `praxeo/core/core.lp` holds CR-4, CR-5a, CR-6, CR-7 (b, c), CR-8 (b, c) and CR-9 as engine rules. It names no instrument, good or market (a test checks this). No pattern file is loaded when it runs.
- `praxeo/core/situation.py` defines the situation record. Following CR-1's own "Use" section, it says what the policy does to each actor class:
  - which exchanges it touches, and which price it holds and in which direction;
  - which terms and quantities each side controls, and the criteria the scarce side can choose by;
  - which trade can go outside the rule;
  - each actor's alternatives, and who has a stake;
  - the links between markets (complement, input, substitute, output, yield, same act);
  - assets and returns tied to a side, transfers, compliance and enforcement.

  Every empirical fact names its assumptions. The record never states a sign.
- **Where the signs come from:**
  - CR-6: a maximum burdens sellers and leaves buyers wanting more; a minimum does the reverse. Those who trade, trade at the line. The pressure goes to the open margins (a group, with members signed alone on their own premise), and the burdened side gives less of what the line leaves free.
  - CR-4: the burdened side uses its alternatives more; the favored side uses them less.
  - CR-7: returns and assets fall on the burdened side and rise on the favored side.
  - CR-8: transfers are recorded on both sides.
  - CR-9: a link's direction comes from the relation, and from whether the source change is in a price or a quantity.
- `tests/test_core_pilot.py` scores the runs with the same harness as the pattern engine's tests.

## Results

| Case | Situation written by | Core rules alone | Pattern engine |
|---|---|---|---|
| WE-001 rent freeze | me, with the example's analysis in view | 28 of 30 rows | 28 of 30 |
| WE-009 minimum wage, youth rate | me, with the analysis in view | 19 of 19 | 19 of 19 (development case) |
| WE-005 gasoline price cap | a subagent, blind (section 1 and the assumption statements only) | 12 of 26 | 13 of 26 after the ceiling fixes |
| WE-008 milk price floor | a subagent, blind | 9 of 28 | 6 of 28 first run, 10 after the floor fixes |

Blind actor names were mapped to the table's names only where they denote the same class. Unmapped, the scores are 4 of 26 and 7 of 28: naming matters as much here as it does for the pattern engine's records.

**Rows that conflict with the example.**
- In sample: none.
- WE-005 (blind): two. Drivers who are served cross the border less, and drivers who are not served cross more. The example nets these into one ambiguous row for border drivers (C-17), which needs a CR-12 comparison the pilot lacks. One produced row, C-18, matches by key only: the engine's row is lost gasoline sales, the table's is in-store goods.
- WE-008 (blind): two. Commodity plants buy less Velmora milk and more from out of state. The example has the state's purchase at a support price keep them whole (C-9), and the record had no way to say the state buys the surplus.

**What the blind writers could not record.** This is the list of what the pilot is missing:
1. **CR-10, time.** Announcement windows, effective dates, expiry, scheduled steps. This accounts for most of WE-005's misses (C-3, C-12, C-13, C-24, C-25).
2. **CR-12, comparisons.** Opposing chains are kept apart (C-17, C-23, C-25, C-26).
3. **A buyer of last resort.** CR-6 names it ("a buyer of last resort that holds the price"), but the record has no fact for it, nor for public stocks and their disposal (WE-008 C-2, C-20, C-21, C-28).
4. **A second restriction that closes a margin.** WE-005's ban on surcharges: the record can list open margins but cannot close one.
5. **Products made from a held good**, and pass-through limited by competition, other than the `output` link.
6. **Classes the record has no way to name**, so their rows cannot be reached: plants.market, workers.dairy, food programs.

## What it shows

- **On the same situation, the core rules reach what the patterns reach.** In both development cases, two instruments derive from one rule file with no instrument in it. Ceilings and floors share every rule.
- **Blind, the core layer is about as good as the pattern engine after its general fixes.** It got 12 against 13 on WE-005, and 9 against 10 on WE-008. That was with no per-instrument rules and without the gaps above. Its misses are almost all missing core rules (CR-10, CR-12) or missing record facts. None comes from a missing instrument pattern.
- **The knowledge moves from the rules to the situation record.** Who trades, the alternatives, the free terms and the links have to be stated per case. That is CR-1's workflow step, and it is the step a parser or decider would have to do well. The typed questions would change accordingly: "what can the burdened side do instead?" as a choice question, rather than a yes/no question per pattern.
- **The patterns keep a role as checks.** Each pattern is a derived result. A test can confirm that the core layer re-derives it on a small situation, as the catalog's own derivations say it should.

## Recommendation

Make the core layer the engine's main path, and grow it by core rule rather than by instrument:
1. **Add CR-1 operation 3** (a cost attached to an option: taxes, subsidies, fees) and operation 4 (transfers), and run them on WE-013. A tariff is the first case with no held price, so this tests whether the layer generalizes across families.
2. **Add CR-10** (dated operations, windows) and the **buyer of last resort**.
3. **Bring the CR-12 combiner onto the core output.**
4. **Have the parser write situation records,** with the actor-name list. Measure blind coverage on the 33 out-of-sample cases against the pattern engine's.
5. **Keep the pattern files and their tests** until the core layer matches them family by family. Then turn the patterns into derivation checks.
