"""The Decider interface (plan 5.2): one typed question in, one typed answer out.

Implementations:
- FixtureDecider: answers from a JSON file (offline runs, tests, a human's answers written down).
- LLMDecider: Claude through the Anthropic SDK, with a structured-output schema.
- HumanDecider: asks on the terminal.
A Jev decider would slot in behind the same interface.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol

from . import llm
from .schema import Answer, PolicyRecord, Question

MODEL = "claude-opus-5-5"

DECIDER_SYSTEM = """You answer one narrow typed question about a policy, for a praxeological policy analysis.
Reason from the policy record, its context facts, and what was generally knowable when the policy was enacted.
Do not use any knowledge of what happened after the enactment date: the answer is a prediction, scored later.
For a yes/no (noul) question, `value` is "yes" or "no" and `probability` is your probability that the answer is yes.
Cite in `evidence` the record or context lines your answer rests on, quoted exactly.
Before answering, check that your probability agrees with your rationale: if the rationale argues for yes, p is above 0.5.
Where the record is silent, say so and answer from what was generally knowable at enactment; silence is not evidence against."""


class Decider(Protocol):
    name: str

    def answer(self, question: Question, record: PolicyRecord) -> Answer: ...


class FixtureDecider:
    def __init__(self, path: Path):
        self.name = f"fixture:{path.name}"
        self.answers = {a["question_id"]: a for a in json.loads(path.read_text())}

    def answer(self, question: Question, record: PolicyRecord) -> Answer:
        if question.id not in self.answers:
            raise KeyError(f"fixture has no answer for {question.id}")
        return Answer(**self.answers[question.id], decider=self.name)


class HumanDecider:
    name = "human"

    def answer(self, question: Question, record: PolicyRecord) -> Answer:
        print(f"\n[{question.id}] {question.text}")
        p = float(input("P(yes) = "))
        why = input("why: ")
        return Answer(question_id=question.id, value="yes" if p >= 0.5 else "no",
                      probability=p, rationale=why, decider=self.name)


class LLMDecider:
    def __init__(self, model: str = MODEL, effort: str = "medium"):
        self.client = llm.client()
        self.model = model
        self.effort = effort
        self.name = f"llm:{model}"

    def answer(self, question: Question, record: PolicyRecord) -> Answer:
        # the policy record is the same on every question of a run: cached up to it
        prompt = [
            {"type": "text", "text": f"Policy record:\n{record.model_dump_json(indent=1)}", "cache_control": {"type": "ephemeral"}},
            {"type": "text", "text": f"Question id: {question.id}\nKind: {question.kind}\n"
                                     + (f"Options: {question.options}\n" if question.options else "")
                                     + f"Question: {question.text}"},
        ]
        resp = llm.parse(
            self.client,
            "decider",
            model=self.model,
            max_tokens=16000,
            system=DECIDER_SYSTEM,
            output_config={"effort": self.effort},
            messages=[{"role": "user", "content": prompt}],
            output_format=Answer,
        )
        if resp.stop_reason == "refusal" or resp.parsed_output is None:
            raise RuntimeError(f"decider gave no answer for {question.id} (stop_reason={resp.stop_reason})")
        ans = resp.parsed_output
        return ans.model_copy(update={"question_id": question.id, "decider": self.name})
