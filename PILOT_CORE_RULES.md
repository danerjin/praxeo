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

## Steps 1 and 2 (after the pilot)

**Step 1.** CR-1 operation 3 (a payment attached to trading) and operation 4 (a transfer of means) were added to `core.lp`, along with an option granted at discretion and further CR-9 relations: cost, own price, currency, and links to a group. The wedge raises what buyers pay and lowers what sellers keep, whichever side the payment is levied on. The first rule had this wrong, and a blind record found it. **Step 2.** CR-10a was added: announcement windows, actions brought forward or carried over, and prices set before a line binds. So was the buyer of last resort of CR-6. Changes inside a timing window do not propagate along CR-9 links.

| Case | Record | Core rules alone | Pattern engine |
|---|---|---|---|
| WE-001 rent freeze | in sample | 29 of 30 | 28 of 30 |
| WE-009 minimum wage | in sample | 19 of 19 | 19 of 19 |
| WE-013 steel tariff | in sample | 31 of 32 | 31 of 32 |
| WE-005 gasoline cap | blind, revised by the same writer for CR-10a | 13 of 26 | 13 after its fixes |
| WE-008 milk floor | blind, revised for the buyer of last resort | 11 of 28 | 10 after its fixes |
| WE-002 drinks excise | blind | 9 of 26 | 5 at its first run |
| WE-010 cigarette tax | blind | 16 of 33 | 12 after its fixes |

On every blind record the core layer equals or passes the pattern engine. It has no instrument-specific rule.

**Rows that still conflict with the examples:**
- WE-005: two rows on crossing the border. They need a CR-12 comparison.
- WE-008: two rows on commodity plants. The record cannot net the state's purchase of their product against the floor on their input. That would be a CR-12 comparison across exchanges.

**What the blind writers still could not record:**
- an expiry window;
- netting across exchanges;
- a closed margin;
- legal against economic incidence;
- subgroups such as border and interior smokers;
- the earmark of a revenue;
- an assumption that defeats a fact;
- product markets made from a held good.

## Step 3: CR-12 on the core output

Three CR-12 pieces were added to `core.lp`. Opposing chains on one key were already ambiguous before this step, and a chain below the cut-off still does not count.
- **Class totals over parts (`parts`, a).** A whole's total takes every chain that reaches its parts.
- **Dominance premises (`dominance`, e).** They are applied after the run. A settled sign rests on the dominance premise too.
- **The first months after a line binds (h with CR-10b).** A price set before the line stays in force against the line.

**Results:**
- WE-001 is 30 of 30 in sample. C-21, the first-months total, is produced, against 28 for the pattern engine.
- The blind writers were offered the new facts in general terms (r3).
  - The WE-005 writer added none. Section 1 names no total over drivers and no assumption that settles a clash. Its two conflicting rows stay: served drivers cross less and unserved drivers cross more, where the example's analyst chose to report border drivers as one ambiguous class. Each part is correctly signed. The class the table nets them into is the analyst's choice, and the text does not give it.
  - The WE-008 writer linked the plants' product sales to their milk purchases and added a class total over Velmora plants. The plants' milk purchases are now ambiguous rather than wrongly a decrease.
  - Two rows still conflict for WE-008: the plants' quantity demanded falls and their out-of-state purchases rise. The plants' position is netted across exchanges only on the variable a link reaches. Netting their CR-4 choice as a whole (burdened on the input, made whole on the output) is not in the layer.

Blind scores after step 3: WE-005 13 of 26, WE-008 11 of 28, WE-002 9 of 26, WE-010 16 of 33. They are unchanged by step 3 itself, and each is equal to or above the pattern engine.

## Step 4: expand as you go (`praxeo/core/expand.py`)

**How the loop works.** The policy's own facts seed the run. Each round, the core rules derive effects. For every newly reached actor, a proposer proposes the facts that node needs, each with the questions its premises ask, and a decider answers them. The facts are added and the rules run again, to depth 3.
- The proposer does open-ended work, so it is an LLM.
- The decider makes bounded, typed judgments with a probability: an LLM now, Jev once its calibration is checked.
- Given the same facts, the loop reproduces the one-shot results on WE-001, WE-009 and WE-013, asking 11 to 14 questions.

**Blind runs.** A stand-in for the proposer and decider wrote the seed and answered the loop node by node, from the policy section and the assumption statements only.

| Case | Rounds, nodes, questions | Core loop | Pattern engine |
|---|---|---|---|
| WE-006 price-gouging law | 3, 12, 16 | 17 of 26 | 15 after its fixes |
| WE-062 plastic packaging tax | 3, 25, 29 | 23 of 68 | 12 after its fixes |

**Rows that conflict with the examples:**
- WE-006: one. The engine signs local sellers' inventory up outside the windows, against C-20 (less stock held before each season).
- WE-062: one opposite sign. Converters' investment falls, where the table has a rise in recycling equipment and an ambiguous total.
- WE-062 also has five rows signed ambiguous where the table signs an increase: recyclers' output, investment and workers, municipalities' collection, and recycled content. They all trace to one gap: the format has no fact for the 30% recycled-content exemption, so the push toward recycled resin cannot be recorded.

**What the loop and the layer still lack**, from the writers' notes:
1. **Revisits.** Each node is visited once, so effects that reach a visited actor later get no new proposals.
2. **CR-4 for anyone whose price moved.** Alternatives fire only for the parties of a held or charged exchange. An actor who bears a tax through a price, such as packaging users, must be reached by links.
3. **CR-7 for anyone whose yield moved.** Assets and yields are tied to a held exchange's side, not to any change in an actor's yield.
4. **Exemptions and lines as CR-1 facts.** RS-5 and RS-17 need them: the 30% line, the 10 t notch.
5. **Supply response.** No relation takes a change in demand to a price through the response of supply (CR-6 0.9).
6. **Premises with no fact to rest on.** There is no premise-only fact, and no time-trend fact.

**After the loop fixes.** Four changes were made to the core layer:
- revisits;
- CR-4 for anyone whose price moved;
- CR-7 on charged exchanges;
- the `supply_price` relation.

Both writers then reran (r2), revising only what the new features let them record. A fifth change, the CR-12e response argument, came next. A step that runs around a loop of links and parts is reported for the class it reaches, but it does not feed back to reverse its cause. The loop is read from the facts, and the cause is the step out of a variable an actor's alternative drives.

| Case | Core loop | Pattern engine |
|---|---|---|
| WE-006 | 17 of 26 (unchanged; one new defensible row, inland buyers' price) | 15 |
| WE-062 | 26 of 68 (was 23) | 12 |

On WE-062, the recyclers' supply, investment, price and workers, and the municipalities' collection, now increase as the table signs them. Converters' recycled content now increases (C-4). One conflicting row remains: converters' investment falls, where the table splits it into recycling equipment, which rises, and an ambiguous total.
