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

## Step 5: the core path as the default (`praxeo/core/pipeline.py`)

`python -m praxeo CASE` now runs the core path whenever the case has core inputs (`loop/seed.json`, or a one-shot `situation.json`) or the parser is the LLM. Otherwise it falls back to the pattern engine; `--engine patterns` forces the fallback and `--engine core` forces the core path. The run goes:
1. seed;
2. expand loop: a file-driven or LLM proposer, and a file-driven, LLM or human decider;
3. core rules, with CR-12e applied;
4. verifier: vocabulary, derivations, estimated premises, the cut-off;
5. templated explanations, one sentence per core rule used;
6. frozen, hashed log and report.

**The patterns as checks.** `tests/test_core_derives_patterns.py` gives one small situation per pattern, meeting its If-clause, and asserts that the core rules derive its conclusion. That covers 24 patterns:
- PC-1 to PC-11;
- TX-1, TX-2, TX-7, TX-8, TX-9;
- RS-1, RS-4, RS-5, RS-7, RS-8, RS-14, RS-15;
- SB-4, SB-9;
- OC-3, OC-4.

Writing them found one gap: an actor burdened only through a price had no timing response unless it also had an alternative listed.

**Not yet done:**
- The LLM proposer and seed parser have not run against the API: there is no key in this environment.
- The pattern files still hold rules for families the core layer has not been checked on: private rules and disclosure. Licensing, quotas, prohibitions, mandates and subsidies were checked in step 6.
- The CR-12 combiner's declared comparisons are pattern-side; the core path settles clashes with dominance premises instead.

## Step 6: the remaining families on the core path

**New operations.** No instrument names appear in the rules, and the new-operation pattern checks pass.
- A grant (`grants`) is CR-1 op 3 reversed:
  - the wedge runs the other way;
  - more trades take place;
  - the recipient's means rise;
  - the payer's outlay rises.
- Expiry (`expires`) is CR-10a at the end. Actions brought forward into the measure's period fall in an `after_expiry` window.
- A fixed quantity (`capped`) follows CR-6's fixed-quantity clause:
  - the price rations the cap;
  - fewer trades take place;
  - holders of the permission gain its value (CR-7c), or its lease price where the good is priced in a wider market (`wider_price`);
  - shut-out sellers trade less.
- A ban (`banned`) stops the legal trade for both sides.
- A charge can carry quantity premises (`quantity_premises`). This lets a mandated term be a charge paid in kind to the counterparty, as PC-17 needs.
- New pattern checks: SB-1, SB-2, SB-6, EN-1, EN-2, EN-6, EN-7 and PC-17. That makes 32 patterns re-derived in all.

**Blind loop runs, one per family.** These are sonnet stand-ins for the proposer and decider, and they read section 1 and the assumption statements only.

| Case | Family | Core loop | Pattern engine | Contradicts the table |
|---|---|---|---|---|
| WE-020 | subsidy (grant, expiry) | 13/33 | 15 | 1 (landlords' `quantity_supplied`: the record means homes put up for sale, the table rental units) |
| WE-016 | licensing | 8/36 | 16 | 0 |
| WE-028 | quota shares | 18/54 | 16 (8 out of sample) | 1 (crew lay pay linked to price only, not catch) |
| WE-018 | ban | 10/22 | 11 | 0 (1 before the CR-8c fix) |
| WE-036 | mandate (play or pay) | 13/60 | 29 | 1 (the in-kind cover signed for every bound worker, not only those at firms that offer it) |

**General fixes from these runs:**
- **CR-8c.** Compliers' other uses fall. On WE-018, the retailers' resources become ambiguous, as in the table.
- **CR-4 0.8.** A charge fixed per seller (`basis: "operating"`, such as a licence fee) bears on the number of sellers, not on each trade. The WE-016 writer named this gap, but the run was not redone because a merge into its worktree was denied.
- **A `supply` link.** More offered lowers the price (CR-6). The WE-020 writer had no way to set the supply response against the grant's price rise.

**What the format still cannot hold,** from the writers' notes:
- **Mandates.** This is the weakest family on the core path (13 against 29).
  - A firm-size threshold, and the restraint on growth below it.
  - A cap on a charge.
  - Play-or-pay, a choice between two charges where each branch needs a premise.
  - A per-holder limit on a quota.
- **Other gaps:**
  - The race to qualify for an allocation by history (CR-7c, claims before creation).
  - A market the policy creates, where share trades rise against no shares.
  - Quality and information under licensing (CR-11c).
  - Decay of a grandfathered stock.
  - A deadline window before expiry (the table's "before end of Year 4").
  - Exempt subclasses of an exchange.

On the pattern side these come from family rules (`rules/mandates.lp`, `rules/licensing.lp`). The core path needs a general form for each: a threshold on the payer's size, alternative charges, and a holding limit. That is the next step before these families can leave the pattern engine.

## Step 7: general forms for the family gaps

**New forms.** Pattern checks have been added for each; 39 patterns and forms are now checked.
- **A charge branch** (`branch_premises`, for play or pay). Each branch of a choice the policy gives the payer holds only with its own premise that some payers take it.
- **Capped payers** (`capped_payers`). Payers whose total is capped pay a fixed sum. It takes from their means but bears on no margin.
- **A threshold** (`thresholds`, CR-4 at a line). Those near a size line hold the size measure below it. Crossing is an option made worse, so alternatives to growing come in. An optional `chooser` covers the case where another actor decides, such as employers setting hours.
- **A race to qualify** (`qualifies`, CR-7c with CR-8c). A right the policy creates is allocated by history in a period after it is expected. The history variable rises in that period, and what is spent qualifying is used up.
- **A deadline window** (CR-10a). Actions timed into a grant's period are rushed in before it ends (`deadline`), as well as missing afterwards.
- **The receiver of a payment in kind** is a chooser made better.

**Blind runs.** These are second runs, written without sight of the first, plus a first run on WE-055.

| Case | Family | Step 6 | Step 7 | Pattern engine | Contradicts the table |
|---|---|---|---|---|---|
| WE-016 | licensing | 8/36 | 14/36 | 16 | 0 |
| WE-036 | mandate | 13/60 | 18/60 | 29 | 1 (cover signed for all full-time workers, not only at firms that offer it) |
| WE-028 | quota shares | 18/54 | 19/54 | 16 | 0 |
| WE-055 | licensing (new case) | – | 11/37 | 8 | 1 (school enrolment: no chain from the fall in entrants) |

Two caveats on blindness:
- The WE-028 second-run writer printed the start of every table row while looking for section breaks, which showed some class names.
- The WE-055 writer saw the closing check paragraph.
- Both say so in `notes.md`.

**Still open,** from the writers' notes:
- Mandates: the core path now has thresholds and branches but is still at 18 against the pattern engine's 29. What remains:
  - The pay branch replacing the offer branch: the two branches' effects add.
  - A held price already in force (the minimum wage under a mandate) cannot be proposed in the loop.
  - `moves` has no horizon, so short-run stickiness and medium-run adjustment collide.
- Two or more readings of an unclear provision (U1) have no place in the situation record.
- Quality and information under licensing (CR-11c) are not handled.
- Holders who also sell under a cap are not distinguished.
- Consolidation of rights into larger hands is not handled.
- A race conclusion does not propagate, because it is a timing conclusion.

## Step 8: closing the mandate gap

**New forms.** Each has a pattern check.
- **A fixed price** (`fixed`). A price that cannot move in the period, such as a minimum wage in force or a wage already set, leaves a charge's payer to adjust the terms it controls (CR-6 with CR-1 op 3). That is the group fall in hours, hiring and other benefits under a mandate.
- **Unclear provisions** (`unclear`). Each reading lists the components it applies, and any fact can be tied to one reading (`reading: "U1-b"`, for example the exempt alternative only that reading opens). The core run goes once per reading and gives a sign per reading where they differ, using the pattern engine's merge.
- **Revisits in the loop.** A node reached again by new effects can take its own proposals (`actor#2`). Before this, a file-driven run replayed the first list.
- **Naming.** A branch paid in kind names the subclass that receives it.

**Blind runs on mandates:**

| Case | Core path | Pattern engine | Contradicts the table |
|---|---|---|---|
| WE-036, third run | 16/60 (18 in the second, 13 in the first) | 29 | 1: seasonal hiring under the exempting reading, which the reading-tied facts added after the run now let a record state |
| WE-031 (building code, new case) | 12/47 | 9 | 1: construction work, where the run had no chain for more work per home |
| WE-059 (right to repair, new case) | 9/47 | 9 | 3: makers' sales and owners' price, signed through a forced quantity premise where the table leaves them ambiguous |

All three writers report reading slips beyond section 1, recorded in their notes:
- The headings and closing check paragraph that follow the assumption table.
- On WE-059, the start of sections 2 and 3.

**Where mandates stand:**
- On the two new mandate cases the core path matches or beats the pattern engine (12 against 9, 9 against 9).
- On WE-036 it is still well short (16 to 18 against 29). Its table is long, and most of the missing rows are subclass splits (players against payers, near-50 against capped firms) and variables the writers name differently.
- The variation between runs (13, 18, 16) is now as large as the effect of the forms. Further gains on WE-036 depend more on the proposer than on the rules.
