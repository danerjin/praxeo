"""Confidence thresholds and escalation (plan 5.4).

An answer is accepted when its confidence clears the threshold for its
question. Below threshold, the question goes to a fallback decider (a human,
a stronger model, or a fixture written by hand) and the escalation is logged.

Thresholds must be set from a labelled question bank (plan 4.6, 6.2), not by
hand. The values in cases/*/thresholds.example.json are placeholders.
"""
from __future__ import annotations

from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel, field_validator

from .decider import Decider
from .schema import Answer, PolicyRecord, Question

Kind = Literal["noul", "choice", "score"]


class Thresholds(BaseModel):
    """Minimum confidence per question kind and per assumption class.

    An assumption-class threshold takes precedence over the kind threshold.
    With neither set, the question is never escalated.
    """
    note: Optional[str] = None
    kind: dict[Kind, float] = {}
    assumption_class: dict[str, float] = {}

    @field_validator("kind", "assumption_class")
    @classmethod
    def _in_unit_interval(cls, v: dict) -> dict:
        if any(not 0.0 <= t <= 1.0 for t in v.values()):
            raise ValueError("thresholds must lie in [0, 1]")
        return v

    def for_question(self, question: Question) -> Optional[float]:
        if question.assumption_class in self.assumption_class:
            return self.assumption_class[question.assumption_class]
        return self.kind.get(question.kind)


def load_thresholds(path: Path) -> Thresholds:
    return Thresholds.model_validate_json(path.read_text())


def confidence(question: Question, answer: Answer) -> float:
    """Noul: distance of P(yes) from a coin flip. Other kinds: the answer's own
    confidence; with none reported, 0, so they escalate under any threshold > 0."""
    if question.kind == "noul":
        return max(answer.probability, 1 - answer.probability)
    return answer.confidence if answer.confidence is not None else 0.0


class EscalatingDecider:
    """Asks `primary`; if the answer is below threshold, asks `fallback` instead
    and logs the escalation in `self.log`."""

    def __init__(self, primary: Decider, fallback: Decider, thresholds: Thresholds):
        self.primary = primary
        self.fallback = fallback
        self.thresholds = thresholds
        self.name = f"escalating:{primary.name}->{fallback.name}"
        self.log: list[dict] = []

    def answer(self, question: Question, record: PolicyRecord) -> Answer:
        first = self.primary.answer(question, record)
        threshold = self.thresholds.for_question(question)
        conf = confidence(question, first)
        if threshold is None or conf >= threshold:
            return first
        second = self.fallback.answer(question, record)
        self.log.append({
            "question_id": question.id,
            "kind": question.kind,
            "assumption_class": question.assumption_class,
            "primary": self.primary.name,
            "primary_p": first.probability,
            "primary_confidence": conf,
            "threshold": threshold,
            "fallback": self.fallback.name,
            "fallback_p": second.probability,
        })
        return second
