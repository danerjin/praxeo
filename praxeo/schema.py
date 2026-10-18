"""Typed records passed between the stages of the pipeline."""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator, model_validator

# at_least_one_* are the group signs of 02_ontology.md 2.5: at least one of the listed variables moves that way.
Sign = Literal["increase", "decrease", "ambiguous", "no_change", "at_least_one_increase", "at_least_one_decrease"]
GROUP_SIGNS = {"at_least_one_increase": "increase", "at_least_one_decrease": "decrease"}
# Timing windows (02_ontology.md 2.5, RS-8): None is the ordinary, unwindowed consequence. "announcement" is the
# stretch between announcement and the effective date. "first_months" is the first stretch after the effective date,
# which the handbook signs on its own where the announcement-window response still bears on the price (WE-001 C-21).
# "after_expiry" is the stretch after a temporary measure ends, where purchases brought into its window are missing (SB-6).
Window = Literal["announcement", "first_months", "after_expiry"]
Horizon = Literal["short", "medium", "long"]
HORIZON_ORDER = {"short": 0, "medium": 1, "long": 2}


# --- parser output -------------------------------------------------------

class Downstream(BaseModel):
    """Users of a taxed or tariffed good as an input (RS-14): who they are, who buys their output, and
    whether their competitors face the same cost (`same`) or are exempt, as imports are (`exempt`)."""
    actor: str = Field(description="Actor class that uses the good as an input, e.g. steel_users")
    buyer_actor: str = Field(default="", description="Actor class that buys their output; needed when competitors face the same cost")
    competitors: Literal["same", "exempt"] = "same"
    owner_actor: Optional[str] = Field(default=None, description="Owners of these users' firms (SB-4), e.g. owners.steel_users")
    exporter_actor: Optional[str] = Field(default=None, description="The exporting part of these users, who sell at world prices (RS-6)")
    worker_actor: Optional[str] = Field(default=None, description="Employees of these users (RS-14, RS-6): their employment or hours fall as a group (at_least_one_decrease)")

    @model_validator(mode="after")
    def _buyer_for_same(self) -> "Downstream":
        if self.competitors == "same" and not self.buyer_actor:
            raise ValueError("a downstream group whose competitors face the same cost needs a buyer_actor")
        return self


class Component(BaseModel):
    """One operative provision of the policy, as the parser read it."""
    id: str
    instrument: str = Field(description="Instrument type from 02_ontology.md section 2.3, e.g. price_ceiling, per_unit_tax, tariff")
    good: str = Field(description="Snake-case name of the good or service, e.g. rental_housing")
    market: str = Field(description="Snake-case name of the market, e.g. san_francisco")
    bound_actor: str = Field(description="Actor class the rule binds, from the ontology, e.g. landlords.controlled")
    protected_actor: Optional[str] = Field(default=None, description="Actor class the rule is meant to benefit")
    excluded_actor: Optional[str] = Field(default=None, description="Actor class of buyers the rule leaves outside, e.g. tenants.prospective")
    cap: Optional[float] = Field(default=None, description="Numeric ceiling, if the text states one")
    cap_unit: Optional[str] = None
    neighbor_actor: Optional[str] = Field(default=None, description="Price ceilings: buyers in a neighbouring market outside the rule's reach, where shut-out buyers can go (RS-4), e.g. renters.neighbors")
    enforcer_actor: str = Field(default="officials.enforcement", description="Price ceilings: who administers and enforces the rule (OC-3)")
    vacancy_decontrol: bool = Field(default=False, description="True when the price of a new contract is free and the cap binds only on renewals")
    evasion_by_resellers: bool = Field(default=False, description="Price ceilings: true when the text makes sales above the cap by the bound sellers themselves detectable (a posted-price rule, a ban on surcharges and tied purchases), so that what trade there is above the cap is resale by buyers")
    buyer_actor: str = Field(default="buyers.current", description="Taxes and tariffs: buyers of the taxed good")
    seller_actor: Optional[str] = Field(default="sellers.current", description="Per-unit taxes: sellers of the taxed good; null where the good has no private seller (a charge paid to the state for using its road)")
    domestic_seller_actor: str = Field(default="sellers.substitutes", description="Tariffs: domestic producers of the protected good")
    importer_actor: Optional[str] = Field(default=None, description="Tariffs: importers of record; defaults to bound_actor")
    revenue_actor: str = Field(default="officials.enforcement", description="Taxes and tariffs: who collects")
    exporter_actor: str = Field(default="export_industries", description="Tariffs: export industries linked to imports through the currency (TX-8)")
    exporter_worker_actor: Optional[str] = Field(default=None, description="Tariffs: their workers; defaults to workers.<exporter_actor>")
    downstream: list[Downstream] = Field(default=[], description="Users of the good as an input (RS-14)")
    taxpayer_actor: str = Field(default="taxpayers", description="Taxes and tariffs: who funds new administration if the agency budget rises (OC-3)")
    foreign_seller_actor: str = Field(default="sellers.foreign", description="Tariffs: foreign sellers of the tariffed good (OC-4)")
    input_supplier_actor: Optional[str] = Field(default=None, description=(
        "Tariffs: suppliers of inputs to the protected domestic producers (CR-9). Price ceilings: suppliers of the input "
        "that the capped sellers buy (PC-12); the capped sellers must be the main buyers of that input"))
    domestic_seller_owner_actor: Optional[str] = Field(default=None, description="Tariffs: owners of the protected domestic producers (SB-4)")
    renewable: bool = Field(default=False, description="True when the gain depends on a later decision: the measure expires or is reviewed, and may be renewed or extended (RS-7, TS-2)")
    definition_line: bool = Field(default=False, description="True when the definitions or exemptions draw a line between covered and uncovered goods (RS-5)")
    relief_applicant_actor: Optional[str] = Field(default=None, description="Who may apply to officials for exclusions, waivers or exemptions granted case by case (RS-15)")
    domestic_seller_worker_actor: Optional[str] = Field(default=None, description="Tariffs: employees of the protected domestic producers; employment or hours rise as a group (TX-7, LW-4)")
    announcement_window: bool = Field(default=False, description=(
        "True when the measure was announced (enacted, put on a ballot, recommended) some time before it takes effect, "
        "so that actors can shift actions into the window (RS-8). The engine fact is announced(C)."))
    protected_concentrated: bool = Field(default=True, description=(
        "Price ceilings: True when the protected buyers are an identifiable group with a concentrated stake (sitting tenants), "
        "False when they are the whole diffuse public (everyone who buys fuel). RS-7 signs the protected group's lobbying only in the first case"))
    rate_rise: bool = Field(default=False, description="Taxes and tariffs: the measure raises the rate of an existing tax, so that the revenue rises only if the base does not fall enough to offset it (TX-1, 1.1)")
    own_revenue_funded: bool = Field(default=False, description="Taxes and tariffs: the cost of administering the measure is paid from its own revenue or from the budget that receives it, not from a budget raised on taxpayers (OC-3, third funding case)")
    mobile_buyer_actor: Optional[str] = Field(default=None, description="Per-unit taxes: buyers who can easily buy the taxed good across the boundary, in a neighbouring jurisdiction without the tax (TX-4, RS-4)")
    neighbor_seller_actor: Optional[str] = Field(default=None, description="Per-unit taxes: sellers just across the boundary who gain those buyers (TX-4, RS-4)")
    general_budget: bool = Field(default=False, description="Price ceilings: enforcement is funded from the general budget, so OC-3 and OC-1 name the payers")
    # subsidies (per_unit_subsidy, purchase_rebate, lump_sum_subsidy): bound_actor is who receives the payment, seller_actor
    # the sellers of the subsidized good (null where the recipients are the sellers), taxpayer_actor who funds it (SB-1),
    # enforcer_actor the agency that pays and checks it (OC-3); own_revenue_funded, renewable and announcement_window apply.
    other_buyer_actor: Optional[str] = Field(default=None, description="Subsidies: buyers of the same good who receive no payment (DM-1, CR-4c), e.g. buyers.other")
    substitute_seller_actor: Optional[str] = Field(default=None, description="Subsidies: sellers of the unsubsidized goods the recipients would otherwise have bought (SB-3, RS-1)")
    asset_owner_actor: Optional[str] = Field(default=None, description="Subsidies: owners of an asset in slow supply whose return the subsidy raises (SB-4), e.g. landowners")
    claim_handler_actor: Optional[str] = Field(default=None, description="Subsidies: who files or processes claims (CR-8c); defaults to bound_actor")
    eligibility_criteria: bool = Field(default=False, description="Subsidies: the payment is conditional on criteria the recipient must meet (SB-5)")
    temporary: bool = Field(default=False, description="Subsidies: available only during a limited window, after which it expires (SB-6)")
    debt_funded: bool = Field(default=False, description="Subsidies: paid from borrowing now and repaid from taxes later (SB-1)")
    budget_capped: bool = Field(default=False, description="Subsidies: a fixed budget or number of payments, handed out first come, first served (PC-2 group form, LW-6)")
    scrappage: bool = Field(default=False, description="Subsidies: the payment requires destroying a used good (SB-6)")
    used_buyer_actor: Optional[str] = Field(default=None, description="Subsidies with scrappage: buyers of the used goods (SB-6), e.g. buyers.used_cars")
    used_owner_actor: Optional[str] = Field(default=None, description="Subsidies with scrappage: owners who keep their used goods (SB-6, SB-4)")
    scrapper_actor: Optional[str] = Field(default=None, description="Subsidies with scrappage: who destroys the scrapped goods (SB-6), e.g. dismantlers")
    tax_named: bool = Field(default=False, description="Subsidies: the text names the tax that pays for the payment; otherwise it comes from a general budget and the payers are a group (OC-1, who pays)")
    other_spending_actor: Optional[str] = Field(default="recipients.other_spending", description="Subsidies from a general budget: recipients of the other spending it could fund (OC-1, who pays)")
    future_taxpayer_actor: Optional[str] = Field(default="taxpayers.future", description="Subsidies from a general budget: future taxpayers (OC-1, who pays); null where the record names the payers otherwise")
    qualifier_actor: Optional[str] = Field(default=None, description="Subsidies: who must meet the criteria, when not the recipients (SB-5), e.g. installers who must be certified")
    third_party_payer_actor: Optional[str] = Field(default=None, description=(
        "Price ceilings: set when the cap is on what buyers pay out of pocket and a third party (an insurer, a fund) must "
        "pay the seller the rest (PC-20). The seller's price is not capped, so no shortage follows from the cap itself"))
    field_contested: bool = Field(default=False, description=(
        "The policy field the measure settles (rent regulation, farm support) was already fought over before it and would "
        "stay contested without it, so lobbying on that question is signed against the counterfactual contest (RS-7 Unless)"))
    repay_on_move: bool = Field(default=False, description="Subsidies: the payment is repaid if the recipient moves or sells within a period (RS-11)")
    source_sentences: list[str] = Field(description="Sentences of the policy text this component rests on, quoted exactly")

    @field_validator("instrument")
    @classmethod
    def _known_instrument(cls, v: str) -> str:
        from .vocabulary import check_instrument
        if (msg := check_instrument(v)):
            raise ValueError(msg)
        return v


class Unclear(BaseModel):
    """A provision the parser could not read one way only (workflow step 2).

    Each reading is labelled by the text before its first colon ("U1-a: ...").
    `reading_facts` maps a label to engine facts that hold under that reading
    (for example an exception); the engine runs once per reading.
    """
    id: str
    text: str
    readings: list[str]
    reading_facts: dict[str, str] = Field(default={}, description=(
        "Engine facts in clingo syntax per reading label, e.g. {\"U1-b\": \"exception(pc_5, c1).\"}. "
        "Written by a person who knows the rule base; a parser should leave this empty. "
        "Text that is not valid clingo is ignored by the engine and reported by the verifier."))

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
    confidence: Optional[float] = None


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
    window: Optional[Window] = Field(default=None, description=(
        "Timing window the consequence is signed for (RS-8, 2.5). None for an ordinary consequence. An announcement-window "
        "consequence has horizon ['short'] and is scored as a short-horizon prediction."))
    group: list[str] = Field(default=[], description=(
        "Members of a group consequence: the sign is then at_least_one_increase or at_least_one_decrease and `variable` "
        "is the first member. Empty for an ordinary consequence."))
    actor_group: list[str] = Field(default=[], description=(
        "Members of a group over actor classes (OC-1, who pays: taxpayers, recipients of other spending): at least one "
        "of them moves, so the sign is at_least_one_increase or at_least_one_decrease and `actor_class` is the first. "
        "Empty for an ordinary consequence."))
    item: Optional[str] = Field(default=None, description=(
        "Qualifier of one item of a variable that a policy moves in opposite directions (CR-12 0.8: two items in one "
        "variable). Items are parts: the CR-12 total over them is a separate consequence with no item, and scoring uses the total."))
    comparison: Optional[str] = Field(default=None, description="Name of the declared CR-12 comparison (praxeo/combiner.py) that formed or settled this consequence")

    def members(self) -> list[str]:
        """The variables the consequence is about: the group, or the one variable."""
        return list(self.group) or [self.variable]

    def actors(self) -> list[str]:
        """The actor classes the consequence is about: the actor group, or the one class."""
        return list(self.actor_group) or [self.actor_class]


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
    actor_roles: dict[str, str] = Field(default={}, description=(
        "Card actor class -> the record role field it stands for (e.g. landlords.controlled: bound_actor). "
        "Scoring then matches predictions by role, so a parser's own label for the same role still matches."))
