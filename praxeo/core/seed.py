"""The seed of a core run: the policy's own facts in CR-1's terms, written by an LLM from the policy text (or read from a
file). Everything else arrives in the expand loop."""
from __future__ import annotations

from .situation import Situation

SEED_SYSTEM = """You read a policy text and write the seed of a praxeological analysis: the policy's own facts in the terms of
core rule CR-1 (what it does to actors' options), as a Situation record. Fill only these parts:
- exchanges: every exchange the policy touches (who buys and who sells, the price variable each side receives, those who
  would trade at a held price but cannot, and the criteria by which the scarce side can choose among them);
- held: a price the policy holds below (a maximum) or above (a minimum), with its binding and enforcement premises;
- charges and moves: a payment the policy attaches to trading (who pays, who receives, the receipt variable), and which
  side's price takes it, with the premise on the other side's response; a charge paid in kind to the counterparty (a
  mandated term) with its quantity premises; a sum fixed per seller (basis "operating"); a charge that is one branch of a
  choice the policy gives the payer (branch premises); payers whose total is capped;
- terms: trading in an exchange made worse or better for one side with no payment (a private rule-maker changing the
  bundle it sells its members; a disclosure showing a good worse or better than believed, with the premise that beliefs
  change); a charge fixed per item offered has basis "item";
- grants (a payment to one side of an exchange), capped (a rule fixing the quantity traded, with the holders of the
  permission), banned (a rule stopping the legal trade), expires (the measure ends and is expected to);
- incidence: where the text or context makes one side's alternatives clearly worse than the other's, that side, with the
  premise comparing them; moves and fixed may carry a horizon (wages sticky in the short run, adjusting in the medium);
- fixed: a price on one side of an exchange that cannot move in the period, by a rule already in force (a minimum wage)
  or a term already set, with its premise; for a branch paid in kind, name as receiver the subclass that receives it;
- thresholds (the measure binds only above a size: those near the line, the measure of size), qualifies (a right the policy
  creates is allocated by history in a period after it is expected);
- backstops (a buyer of last resort), discretion (an option granted case by case), means (a transfer no choice avoids),
  announced and early_price (a measure known before it binds), transfers, compliance, enforcers, funded or fixed_budget;
- assumptions: only the premises those facts use, each a statement whose truth is asked one at a time (one concept each).
Leave alternatives, links, margins other than an exchange's own criteria, stakes, assets, yields, timing, parts and dominance
empty: they are proposed node by node later. Never state a sign. Name actor classes as role.qualifier. Use only what the
text says or what was knowable at enactment."""


def parse_seed_llm(text: str, model: str = "claude-opus-5-5", effort: str = "medium") -> Situation:
    import anthropic

    client = anthropic.Anthropic()
    resp = client.messages.parse(model=model, max_tokens=16000, system=SEED_SYSTEM, output_config={"effort": effort},
                                 messages=[{"role": "user", "content": f"Policy text:\n\n{text}"}], output_format=Situation)
    if resp.stop_reason == "refusal" or resp.parsed_output is None:
        raise RuntimeError(f"seed parser returned nothing (stop_reason={resp.stop_reason})")
    return resp.parsed_output
