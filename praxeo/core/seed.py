"""The seed of a core run: the policy's own facts in CR-1's terms, written by an LLM from the policy text (or read from a
file). Everything else arrives in the expand loop."""
from __future__ import annotations

import json
import sys

from pydantic import BaseModel, Field, ValidationError

from .. import llm
from .situation import Situation

SEED_SYSTEM = """You read a policy text and write the seed of a praxeological analysis: the policy's own facts in the terms of
core rule CR-1 (what it does to actors' options), as a Situation record. Fill only these parts:
- exchanges: every exchange the policy touches (who buys and who sells, the price variable each side receives, those who
  would trade at a held price but cannot, and the criteria by which the scarce side can choose among them);
- held: a price the policy holds below (a maximum) or above (a minimum), with its binding and enforcement premises;
- charges and moves: a payment the policy attaches to trading (who pays, who receives, the receipt variable), and which
  side's price takes it, with the premise on the other side's response; a charge paid in kind to the counterparty (a
  mandated term) with its quantity premises; a sum fixed per seller (basis "operating"); a charge that is one branch of a
  choice the policy gives the payer (branch premises), where the payers who take each branch are a subclass of their own
  (their options and what they pay differ): give each branch its own exchange, with that subclass on the payer's side and
  its own counterparties on the other (payers.paying and payers.providing, each with the sellers it trades with), never
  two branches on one exchange; payers whose total is capped;
- terms: trading in an exchange made worse or better for one side with no payment (a private rule-maker changing the
  bundle it sells its members; a disclosure showing a good worse or better than believed, with the premise that beliefs
  change); a charge fixed per item offered has basis "item";
- duties: a duty to supply, where sellers must sell what they would otherwise withhold; a charge owed to more than one
  receiver lists the others in other_receivers;
- issued: a right the policy creates and sells in an exchange whose seller is the issuer (an auction of licences);
- penalties: a fine due on breaking a component's rule (who pays, who collects, the premise that some break it and are fined);
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


PRICE_NOTE = """Variables: every variable, the exchanges' price variables included, comes from the controlled list below.
An exchange's price variables must be prices the engine knows: the buyer's price_paid; the seller's net_price_received, or
wage_rate where the seller sells labour. Actor classes: use the listed ones where one fits, as role.qualifier."""


def shared_branches(sit: Situation) -> list[str]:
    """Branches of one choice written on one exchange: the payers who take each branch are then one class, and every
    effect that differs between them (paying in money, providing in kind) lands on it undivided."""
    by_exchange: dict[str, dict[str, set]] = {}     # exchange -> receiver -> components; two routes into one branch
    for c in sit.charges:                             # (a new offer, an upgrade) share a receiver and may share an exchange
        if c.branch_premises or c.branch_premise_sets:
            by_exchange.setdefault(c.exchange, {}).setdefault(c.receiver, set()).add(c.component)
    return [f"charges: branches {', '.join(sorted(set().union(*rs.values())))} share exchange {e}; give each branch its own "
            "exchange, with the subclass of payers that takes it and its counterparties"
            for e, rs in sorted(by_exchange.items()) if len(rs) > 1]


class SeedOut(BaseModel):
    """Structured outputs take closed schemas only, and a Situation has open maps (assumptions), so the seed travels as a
    JSON object in a string and is validated here."""
    situation_json: str = Field(description="The seed as one JSON object of the Situation schema given in the instructions")


def parse_seed_llm(text: str, model: str = "claude-opus-5-5", effort: str = "medium", exclude: tuple[str, ...] = ()) -> Situation:
    """The seed from the policy text. A seed that does not validate, or names a variable outside the controlled list, is
    sent back once with the errors (an invented price variable drops every rule that starts from a price change)."""
    from .expand import off_list, vocabulary_text

    client = llm.client()
    system = (SEED_SYSTEM + "\n\n" + PRICE_NOTE + "\n\n" + vocabulary_text(exclude)
              + "\n\nThe Situation schema:\n" + json.dumps(Situation.model_json_schema()))
    messages = [{"role": "user", "content": f"Policy text:\n\n{text}"}]
    for attempt in range(2):
        resp = llm.parse(client, "seed", model=model, max_tokens=32000, system=system, output_config={"effort": effort},
                                     messages=messages, output_format=SeedOut)
        if resp.stop_reason == "refusal" or resp.parsed_output is None:
            raise RuntimeError(f"seed parser returned nothing (stop_reason={resp.stop_reason})")
        try:
            sit = Situation.model_validate_json(resp.parsed_output.situation_json)
        except ValidationError as e:
            problem = f"The seed does not validate; give it again corrected:\n{e}"
        else:
            names = off_list(sit, actors=False) + shared_branches(sit)
            if not names or attempt == 1:
                for msg in names:
                    print(f"seed: {msg}", file=sys.stderr)
                return sit
            problem = "Correct these and give the seed again:\n" + "\n".join(names)
        messages += [{"role": "assistant", "content": resp.parsed_output.model_dump_json()},
                     {"role": "user", "content": problem}]
    raise RuntimeError("seed parser output did not validate twice")
