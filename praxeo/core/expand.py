"""Expand as you go (step 4 of the core-layer plan): the situation is not written in one pass. The policy's own facts (CR-1:
the exchanges it touches, the prices it holds, the payments it attaches, who enforces and funds it) seed the run; the core
rules derive the first effects; for each actor those effects reach, a Proposer proposes what the core rules need to go on
(that actor's alternatives, the markets linked to it, the terms it controls, its stakes and assets), each fact with the
question its premise asks; a Decider answers the questions; the facts are added and the rules run again. The loop stops
when no new actor is reached or at the depth limit (the handbook prunes diffuse chains at depth 3).

The Proposer does open-ended work (naming classes and links, quoting what they rest on): an LLM. The Decider gives a
probability per premise: the existing Decider interface (an LLM now, Jev when available). The deduction is core.lp's.
Every proposal and answer is logged, in order, so a run can be replayed.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Literal, Optional, Protocol

from pydantic import BaseModel, Field

from ..schema import Answer, PolicyRecord, Question
from . import situation as S

# The parts of a situation a proposal may add, and which field of each names the actor whose node proposes it (assets: the
# party of the side named, since the owner is reached only through the asset).
PARTS = {"alternatives": "chooser", "links": "source_actor", "margins": "actor", "stakes": "actor", "assets": "actor",
         "yields": "actor", "timing": "actor", "parts": "part", "dominance": "actor"}
MAX_DEPTH = 3


class Proposal(BaseModel):
    """One fact a node needs, with the questions its premises ask (one concept each, answered yes or no)."""
    part: Literal["alternatives", "links", "margins", "stakes", "assets", "yields", "timing", "parts", "dominance", "incidence"]
    fact: dict = Field(description="The fields of that situation part, without `premises`")
    premises: list[str] = Field(default=[], max_length=3, description="Each premise as a statement whose truth is asked")
    premise_class: str = "other"
    source: Optional[str] = Field(default=None, description="The sentence of the policy or context the fact rests on, quoted")


class Node(BaseModel):
    actor: str
    depth: int
    visit: int = Field(default=1, description="1 on the first visit; a revisit (new effects reached the actor) counts up")
    effects: list[tuple[str, str, Optional[str]]] = Field(description="(variable, sign, window) of the reported effects on it")


class Proposer(Protocol):
    name: str

    def propose(self, node: Node, situation: S.Situation, policy: str) -> list[Proposal]: ...


class FixtureProposer:
    """Proposals from a JSON file keyed by actor class (replays, tests, a proposer's answers written down)."""

    def __init__(self, path: Path):
        self.name = f"fixture:{path.name}"
        self.by_actor = {a: [Proposal(**p) for p in ps] for a, ps in json.loads(path.read_text()).items()}

    def propose(self, node: Node, situation: S.Situation, policy: str) -> list[Proposal]:
        # a revisit k also gets what was written for it under "actor#k" (proposals made once the new effects were seen)
        return [p for k in range(1, node.visit + 1) for p in self.by_actor.get(_key(node.actor, k), [])]


class TextDecider:
    """Answers premise questions from a table of statement -> probability (replays and tests)."""

    def __init__(self, table: dict[str, float], name: str = "table"):
        self.table, self.name = table, name

    def answer(self, question: Question, record: PolicyRecord) -> Answer:
        p = self.table[question.text]
        return Answer(question_id=question.id, value="yes" if p >= 0.5 else "no", probability=p, rationale="from table", decider=self.name)


def _key(actor: str, visit: int) -> str:
    return actor if visit == 1 else f"{actor}#{visit}"


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")[:40]


class Run(BaseModel):
    situation: S.Situation
    log: list[dict] = []
    rounds: int = 0


def expand(seed: S.Situation, proposer: Proposer, decider, policy: str = "", max_depth: int = MAX_DEPTH,
           record: Optional[PolicyRecord] = None) -> Run:
    """Grow the situation from its seed, round by round, until no new actor is reached or `max_depth` rounds are done."""
    sit = seed.model_copy(deep=True)
    record = record or PolicyRecord(name=seed.name, jurisdiction="-", rule_maker="-", enacted="-", effective="-", components=[])
    by_text = {v["text"]: k for k, v in sit.assumptions.items()}
    seen: dict[str, set] = {}        # actor -> the effects it was last proposed for (a node is revisited when new ones reach it)
    visits: dict[str, int] = {}
    added: set[str] = set()          # facts already in the situation, so a revisit does not add them twice
    run = Run(situation=sit)
    for depth in range(1, max_depth + 1):
        cons = [c for c in S.run(sit) if c.reported]
        reached: dict[str, list] = {}
        for c in cons:
            for a in (c.actor_group or [c.actor_class]):
                reached.setdefault(a, []).append((",".join(c.group) or c.variable, c.sign, c.window))
        frontier = sorted(a for a in reached if not set(reached[a]) <= seen.get(a, set()))
        if not frontier:
            break
        run.rounds = depth
        for actor in frontier:
            seen[actor] = set(reached[actor])
            visits[actor] = visits.get(actor, 0) + 1
            node = Node(actor=actor, depth=depth, visit=visits[actor], effects=sorted(reached[actor], key=str))
            for prop in proposer.propose(node, sit, policy):
                atoms = []
                for text in prop.premises:
                    if text not in by_text:
                        atom = f"q{len(sit.assumptions) + 1}_{_slug(text)}"
                        q = Question(id=atom, kind="noul", text=text, assumption=atom, assumption_class=prop.premise_class)
                        ans = decider.answer(q, record)
                        sit.assumptions[atom] = {"text": text, "p": ans.probability, "class": prop.premise_class}
                        by_text[text] = atom
                        run.log.append({"depth": depth, "node": actor, "question": text, "atom": atom,
                                        "p": ans.probability, "rationale": ans.rationale, "decider": getattr(decider, "name", "")})
                    atoms.append(by_text[text])
                fact = {**prop.fact, "premises": atoms}
                sig = json.dumps([prop.part, fact], sort_keys=True)
                if sig in added:
                    continue
                added.add(sig)
                getattr(sit, prop.part).append(_coerce(prop.part, fact))
                run.log.append({"depth": depth, "node": actor, "proposal": prop.model_dump(), "proposer": proposer.name})
    run.situation = sit
    return run


def _coerce(part: str, fact: dict):
    """A proposed fact as the Situation part's model (dict parts stay dicts)."""
    field = S.Situation.model_fields[part]
    inner = field.annotation.__args__[0]
    return inner(**fact) if isinstance(inner, type) and issubclass(inner, BaseModel) else fact


def split(full: S.Situation) -> tuple[S.Situation, dict[str, list[dict]]]:
    """A one-shot situation as a seed (the policy's own facts) and proposals keyed by the actor whose node proposes them;
    used to check that the loop reproduces a one-shot record."""
    seed = full.model_copy(deep=True)
    props: dict[str, list[dict]] = {}
    texts = {k: v["text"] for k, v in full.assumptions.items()}
    for part, key in PARTS.items():
        for item in getattr(full, part):
            d = item if isinstance(item, dict) else item.model_dump()
            fact = {k: v for k, v in d.items() if k != "premises"}
            node = d[key]
            if part == "assets":   # proposed at the node of the party whose activity the asset serves (its owner is reached only through it)
                ex = next(e for e in full.exchanges if e.id == d["exchange"])
                node = ex.buyer if d["side"] == "buyer" else ex.seller
            props.setdefault(node, []).append({"part": part, "fact": fact, "premises": [texts[p] for p in d.get("premises", [])]})
        setattr(seed, part, [])
    used = {p for ps in props.values() for p in ps for p in p["premises"]}
    seed.assumptions = {k: v for k, v in full.assumptions.items() if v["text"] not in used or _in_seed(full, k)}
    return seed, props


def _in_seed(full: S.Situation, atom: str) -> bool:
    seed_parts = [p for p in S.Situation.model_fields if p not in PARTS and p not in ("name", "exchanges", "assumptions")]
    return any(f'"{atom}"' in json.dumps([x if isinstance(x, dict) else x.model_dump() for x in getattr(full, p)]) for p in seed_parts)


PROPOSER_SYSTEM = """You propose facts for a praxeological analysis that a rule engine (the core rules CR-1 to CR-12) will reason
from. You are given the policy text, the situation as recorded so far, and one node: an actor class and the effects the
engine has already derived for it. Propose only what this node needs for the reasoning to go on, as facts of these kinds:
- alternatives (CR-4): what this actor can do instead of an option the policy makes worse or better; `fact`: {component,
  chooser: this actor, actor: whose variable measures the alternative's use, variables: [one, or several for a group]}.
- links (CR-9): markets reached through this actor's changed variables; `fact`: {source_actor: this actor, source_variable,
  relation: complement | input | substitute | output | yield | same_act | cost | own_price | currency | supply_price (more demand raises the price where supply is slow) | supply (more offered lowers the price), actor, variable}.
- margins (CR-6): terms or quantities this actor controls under a held or fixed price, criteria it is chosen by, trade outside the rule.
- incidence (CR-7b): on an exchange a charge or grant acts on, the side whose alternatives are clearly worse than the
  other side's (it bears more of the charge, or keeps more of the grant); `fact`: {component, exchange, side}. Only with a
  premise comparing the two sides' alternatives.
- stakes (lobbying), assets and yields tied to an exchange side, timing (bring_forward or carry_over), parts (a class total),
  dominance (only where a premise states that one direction outweighs another).
Never state a sign: the engine derives every sign. Name actor classes as role.qualifier from the controlled list where one
fits. Each fact gets up to three premises, written as statements whose truth will be asked one at a time (one concept each,
no "and"); reuse the exact wording of a premise already recorded when it is the same premise. Quote in `source` the sentence
of the policy or context the fact rests on. Propose nothing for an effect that reaches no one else, and nothing you would
need to invent: an empty list is a valid answer. Use only what was knowable at enactment.
Names: every variable comes from the controlled list below, chosen by its meaning there (quantity_supplied is what sellers
offer, not what owners put up for sale in another market); use actor classes from the list where one fits, as role.qualifier.
Where the policy or the reasoning treats parts of a class differently (those who take one branch of a choice and those who
take the other; those near a line and those past it; those already in the trade and those who would enter), name each
part as its own subclass rather than the whole class."""


def vocabulary_text(exclude: tuple[str, ...] = ()) -> str:
    """The controlled names the proposer chooses from: variables with their meanings (02_ontology.md 2.4) and actor classes
    (2.2 plus names used in at least two worked examples, not counting `exclude`)."""
    from .. import vocabulary as V
    lines = ["Variables (controlled list):"] + [f"- {n}: {m}" for n, m in sorted(V.variable_meanings().items())]
    lines += ["", "Actor classes (use one where it fits; otherwise role.qualifier with a listed role):",
              ", ".join(V.actor_classes(exclude=tuple(exclude)))]
    return "\n".join(lines)


def off_list(sit: S.Situation) -> list[str]:
    """Names in the situation outside the controlled lists: variables not in 2.4, actor classes whose role is unknown."""
    from .. import vocabulary as V
    out = []
    for part, items in sit.model_dump().items():
        if not isinstance(items, list):
            continue
        for x in items:
            if not isinstance(x, dict):
                continue
            for k in ("variable", "source_variable", "receipt_variable", "projection_variable", "outlay_variable"):
                for v in (x.get(k) or "").split(","):
                    if v and (msg := V.check_variable(v)):
                        out.append(f"{part}: {msg}")
            for v in x.get("variables") or []:
                if (msg := V.check_variable(v)):
                    out.append(f"{part}: {msg}")
            for k in ("actor", "chooser", "source_actor", "buyer", "seller", "receiver", "payer"):
                if isinstance(x.get(k), str) and (msg := V.check_actor(x[k])):
                    out.append(f"{part}: {msg}")
    return list(dict.fromkeys(out))


class Proposals(BaseModel):
    proposals: list[Proposal]


class LLMProposer:
    """Claude through the Anthropic SDK, with a structured-output schema (the open-ended part of each node)."""

    def __init__(self, model: str = "claude-opus-5-5", effort: str = "medium", exclude: tuple[str, ...] = ()):
        import anthropic

        self.client = anthropic.Anthropic()
        self.model, self.effort, self.name = model, effort, f"llm:{model}"
        self.system = PROPOSER_SYSTEM + "\n\n" + vocabulary_text(exclude)

    def propose(self, node: Node, situation: S.Situation, policy: str) -> list[Proposal]:
        prompt = (f"Policy text:\n{policy}\n\nSituation so far:\n{situation.model_dump_json(indent=1)}\n\n"
                  f"Node: {node.model_dump_json()}")
        resp = self.client.messages.parse(model=self.model, max_tokens=16000, system=self.system,
                                          output_config={"effort": self.effort},
                                          messages=[{"role": "user", "content": prompt}], output_format=Proposals)
        if resp.stop_reason == "refusal" or resp.parsed_output is None:
            raise RuntimeError(f"proposer gave nothing for {node.actor} (stop_reason={resp.stop_reason})")
        return resp.parsed_output.proposals


class Pending(Exception):
    """A file-driven run needs more input: proposals for these nodes, or answers to these questions."""

    def __init__(self, nodes: list[Node], questions: list[str]):
        super().__init__(f"{len(nodes)} nodes need proposals, {len(questions)} questions need answers")
        self.nodes, self.questions = nodes, questions


class FileProposer(FixtureProposer):
    """A proposer whose answers are written into a file between runs (a person or a stand-in for the LLM): a node missing from
    the file stops the run and is listed."""

    def __init__(self, path: Path):
        self.path = path
        self.name = f"file:{path.name}"
        self.by_actor = {a: [Proposal(**p) for p in ps] for a, ps in json.loads(path.read_text()).items()} if path.exists() else {}
        self.missing: list[Node] = []

    def propose(self, node: Node, situation: S.Situation, policy: str) -> list[Proposal]:
        if _key(node.actor, node.visit) not in self.by_actor:
            self.missing.append(node)
        return super().propose(node, situation, policy)


class FileDecider(TextDecider):
    """Answers from a file {statement: probability}; a missing statement is listed and answered 0 for this run."""

    def __init__(self, path: Path):
        super().__init__(json.loads(path.read_text()) if path.exists() else {}, name=f"file:{path.name}")
        self.missing: list[str] = []

    def answer(self, question: Question, record: PolicyRecord) -> Answer:
        if question.text not in self.table:
            self.missing.append(question.text)
            return Answer(question_id=question.id, value="no", probability=0.0, rationale="pending", decider=self.name)
        return super().answer(question, record)


def main() -> None:
    """python -m praxeo.core.expand SEED.json PROPOSALS.json ANSWERS.json [--policy TEXT] [--out SITUATION.json]
    python -m praxeo.core.expand --vocab [--exclude WE-NNN]

    Runs the loop with file-driven proposer and decider. If a node or a question is not yet covered, prints what is needed
    (each node with its derived effects) and stops; fill the files in and run again until it completes."""
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("seed", type=Path, nargs="?")
    ap.add_argument("proposals", type=Path, nargs="?")
    ap.add_argument("answers", type=Path, nargs="?")
    ap.add_argument("--vocab", action="store_true", help="print the controlled names the proposer chooses from, and stop")
    ap.add_argument("--exclude", action="append", default=[], help="with --vocab: an example id (WE-036) not to count")
    ap.add_argument("--policy", type=Path)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    if a.vocab:
        print(vocabulary_text(tuple(a.exclude)))
        return
    prop, dec = FileProposer(a.proposals), FileDecider(a.answers)
    run = expand(S.load(a.seed), prop, dec, a.policy.read_text() if a.policy else "")
    for msg in off_list(run.situation):
        print(f"off-list: {msg}")
    if prop.missing or dec.missing:
        print("PENDING")
        for n in prop.missing:
            print(f"node {_key(n.actor, n.visit)} (depth {n.depth}" + (", revisit: new effects reached it" if n.visit > 1 else "") + "): " + "; ".join(f"{v} {s}" + (f" [{w}]" if w else "") for v, s, w in n.effects))
        for q in dict.fromkeys(dec.missing):
            print(f"question: {q}")
        return
    print(f"DONE in {run.rounds} rounds, {sum(1 for e in run.log if 'question' in e)} questions")
    for c in S.run(run.situation):
        print(("R " if c.reported else "- ") + f"{c.actor_group or c.actor_class} {c.group or c.variable} {c.window or ''} {c.sign}")
    if a.out:
        a.out.write_text(run.situation.model_dump_json(indent=1))


if __name__ == "__main__":
    main()
