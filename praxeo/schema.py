"""Typed records passed between the stages of the pipeline."""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

Sign = Literal["increase", "decrease", "ambiguous", "no_change"]
Horizon = Literal["short", "medium", "long"]
HORIZON_ORDER = {"short": 0, "medium": 1, "long": 2}


# --- parser output -------------------------------------------------------

class Component(BaseModel):
    """One operative provision of the policy, as the parser read it."""
    id: str
    instrument: Literal["price_ceiling", "price_floor", "tax", "subsidy", "quota",
                        "licence", "mandate", "ban", "private_rule", "other"]
    good: str = Field(description="Snake-case name of the good or service, e.g. rental_housing")
    market: str = Field(description="Snake-case name of the market, e.g. san_francisco")
    bound_actor: str = Field(description="Actor class the rule binds, from the ontology, e.g. landlords.controlled")
    protected_actor: Optional[str] = Field(default=None, description="Actor class the rule is meant to benefit")
    excluded_actor: Optional[str] = Field(default=None, description="Actor class of buyers the rule leaves outside, e.g. tenants.prospective")
    cap: Optional[float] = Field(default=None, description="Numeric ceiling, if the text states one")
    cap_unit: Optional[str] = None
    vacancy_decontrol: bool = Field(default=False, description="True when the price of a new contract is free and the cap binds only on renewals")
    source_sentences: list[str] = Field(description="Sentences of the policy text this component rests on, quoted exactly")


class Unclear(BaseModel):
    """A provision the parser could not read one way only (workflow step 2).

    Each reading is labelled by the text before its first colon ("U1-a: ...").
    `reading_facts` maps a label to engine facts that hold under that reading
    (for example an exception); the engine runs once per reading.
    """
    id: str
    text: str
    readings: list[str]
    reading_facts: dict[str, str] = {}

    def labels(self) -> list[str]:
        return [r.split(":", 1)[0].strip() for r in self.readings]


class PolicyRecord(BaseModel):
    """Workflow step 1: what the rule does, to whom, from when."""
    name: str
    jurisdiction: str
    rule_maker: str
    enacted: str
    effective: str
    stated_aim: Optional[str] = None
    components: list[Component]
    unclear: list[Unclear] = []
    context: list[str] = Field(default=[], description="Facts about the market as it stood at enactment, each with its source")


# --- decider -------------------------------------------------------------

class Question(BaseModel):
    """A narrow typed question (plan 4.4). One concept per question."""
    id: str
    kind: Literal["noul", "choice", "score"]
    text: str
    options: list[str] = []
    assumption: Optional[str] = Field(default=None, description="Engine atom this question estimates, e.g. enforced")
    assumption_class: Optional[str] = Field(default=None, description="Ontology assumption type, e.g. enforcement")


class Answer(BaseModel):
    """A decider's answer. For noul questions, `probability` is P(yes)."""
    question_id: str
    value: str
    probability: float = Field(ge=0.0, le=1.0)
    rationale: str
    evidence: list[str] = []
    decider: str = ""


# --- engine output -------------------------------------------------------

class Assumption(BaseModel):
    id: str
    text: str
    assumption_class: str
    p: float


class Step(BaseModel):
    """One rule firing in a derivation: rule, the premises it used, what it concluded."""
    rule: str
    conclusion: str
    premises: list[str]


class Consequence(BaseModel):
    id: str
    actor_class: str
    variable: str
    sign: Sign
    horizon: list[Horizon]
    visibility: Literal["visible", "invisible"]
    tier: Literal["A", "B", "J", "C"]
    derivation: list[Step]
    assumption_sets: list[list[str]] = Field(description="Minimal sets of assumptions under each of which the consequence follows (ATMS label)")
    assumptions: list[str] = Field(description="The reported set: the minimal set with the highest joint probability")
    reported: bool = Field(description="True when every assumption in the reported set has p >= cut-off")
    sign_by_reading: dict[str, str] = Field(default={}, description="Per-reading signs when they differ ('none' = not derived under that reading); sign is then 'ambiguous'")
    combines: list[str] = Field(default=[], description="IDs of the consequences a CR-12 combination was formed from")


# --- outcome card --------------------------------------------------------

class Source(BaseModel):
    """A dated piece of context for grounding (plan 5.3)."""
    id: str
    date: str = Field(description="ISO date of publication")
    text: str
    citation: str


class Finding(BaseModel):
    id: str
    actor_class: str
    variable: str
    finding_type: Literal["effect", "null", "opposite"]
    sign: Optional[Sign] = None
    horizon: list[Horizon]
    magnitude: Optional[str] = None
    source: str
    confidence: Literal["high", "low"] = "high"
    note: Optional[str] = None


class AssumptionStatus(BaseModel):
    assumption: str
    held: Optional[bool] = Field(description="True, False, or None when the evidence does not say")
    evidence: str


class OutcomeCard(BaseModel):
    case: str
    written_by: str
    checked_by: Optional[str] = None
    findings: list[Finding]
    assumption_status: list[AssumptionStatus]
    confounders: list[str]
    verification: str
