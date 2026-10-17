# Control cases for the decider

Fictional mini-cases whose text settles some typed questions plainly. `expected.json` gives the direction a
decider should answer for those questions (most are "no", to detect a bias toward "yes"). They test the
decider's reading of the record, not the rules. Run them with `tools/prep_llm_stage_inputs.py` and score with
`tools/score_controls.py`.
