"""Parser: policy text -> PolicyRecord (workflow steps 1 and 2).

The LLM parser fills the schema and must quote the sentences each component
rests on. `check_citations` then verifies in code that every quoted sentence
occurs in the source text; a component whose quotes are not found is flagged.

Enrichment (plan 5.3) is a second step: from the context sources dated before enactment, the LLM proposes related markets
(`Component.related`) that the policy text does not name, each with the source it rests on and a quoted sentence.
`check_source_quotes` verifies every quote in code against that source, and refuses a source dated on or after enactment.
"""
from __future__ import annotations

import re
from pathlib import Path

from pydantic import BaseModel

from .decider import MODEL
from .schema import PolicyRecord, Related, Source

PARSER_SYSTEM = """You turn the text of a policy into a structured policy record for a praxeological analysis.
For each operative provision, give one component: the instrument, the good and market, the actor classes it
affects, and the sentences of the text it rests on, quoted exactly.
If a provision can be read more than one way, record it under `unclear` with each reading; do not pick one.
Leave `reading_facts` empty: it takes engine facts written by a person, not text. Where a reading changes what a
component is or does, record it in `reading_fields` as the Component fields that reading sets, per component id (e.g.
under a reading where the payment is on a fixed historical base, {"U1-b": {"k1": {"instrument": "lump_sum_subsidy"}}}).
Copy into `context` only facts stated in the text about the market at enactment. Use nothing from after the enactment date.

Actor roles. The rules attach consequences to the role fields, so fill every role field that applies to the
instrument, even when the text states no aim:
- price_ceiling: bound_actor (sellers bound by the cap), protected_actor (buyers who hold the good at the capped
  price), excluded_actor (buyers seeking the good), vacancy_decontrol (true if the price of a new contract is free),
  evasion_by_resellers (true if the text makes the sellers' own sales above the cap detectable, e.g. the posted price must be
  the price charged and surcharges or tied purchases are banned),
  neighbor_actor (buyers in a neighbouring market outside the rule's reach, only if the text or context names one),
  enforcer_actor (who administers and enforces the cap, e.g. officials.enforcement). Where the cap is on what buyers
  pay out of pocket and an insurer or fund must pay the seller the rest, set third_party_payer_actor to that payer and
  protected_actor to the buyers whose share is capped: the seller's own price is not capped.
- per_unit_tax: bound_actor (who pays it to the state), buyer_actor, seller_actor, revenue_actor (who collects),
  taxpayer_actor (who funds new administration; default taxpayers), enforcer_actor (the agency that administers it,
  default officials.enforcement; revenue_actor may be a budget), definition_line (true if the definitions or
  exemptions draw a line between covered and uncovered goods), relief_applicant_actor (who may apply for
  case-by-case exclusions or waivers, if the text provides them), rate_rise (true if the measure raises the rate of
  an existing tax), own_revenue_funded (true if the administration is paid from the measure's own revenue or the
  budget that receives it), mobile_buyer_actor and neighbor_seller_actor (buyers who can easily buy across the
  boundary, and the sellers there, if an untaxed place is within reach). seller_actor is null where the good has no
  private seller (a charge paid to the state for using its road).
- tariff: bound_actor and importer_actor (importers of record), buyer_actor (domestic users of the good),
  domestic_seller_actor and protected_actor (domestic producers the tariff shelters), revenue_actor,
  exporter_actor and exporter_worker_actor (export industries and their workers), and `downstream` (each group
  that uses the good as an input, the buyers of its output, whether its competitors face the same cost or
  are exempt, e.g. imported finished goods, and where the text names them, owner_actor (owners of those firms) and
  exporter_actor (their exporting part)); also, where the text gives them: foreign_seller_actor, taxpayer_actor,
  input_supplier_actor (suppliers of inputs to the protected producers), domestic_seller_owner_actor (their
  owners), renewable (true if the measure expires or is reviewed and may be renewed or extended),
  definition_line (true if the definitions or exemptions draw a line between covered and uncovered goods) and
  relief_applicant_actor (who may apply for case-by-case exclusions or waivers).
- per_unit_subsidy, purchase_rebate, lump_sum_subsidy: bound_actor (who receives the payment), seller_actor (sellers
  of the subsidized good; null where the recipients are the sellers), taxpayer_actor (who funds it), enforcer_actor
  (the agency that pays and checks it), debt_funded (true if it is borrowed now and repaid from taxes later),
  own_revenue_funded (true if a dedicated revenue pays it), tax_named (true if the text names the tax that pays;
  otherwise the payers are taxpayers, other_spending_actor and future_taxpayer_actor as a group), qualifier_actor
  (who must meet the criteria, if not the recipients), eligibility_criteria (true if the payment depends on
  criteria), temporary (true if it is offered only for a limited window), budget_capped (true if a fixed budget or
  number is handed out first come, first served), renewable, announcement_window, repay_on_move (true if the payment
  is repaid when the recipient moves or sells within a period), claim_handler_actor (who files or processes claims,
  if not the recipients); where the text or context names them: other_buyer_actor (buyers of the same good who get no
  payment), substitute_seller_actor (sellers of the goods the payment does not cover), asset_owner_actor (owners of an
  asset in slow supply whose return the payment raises); and for a payment that requires scrapping a used good,
  scrappage, used_buyer_actor, used_owner_actor (owners who keep theirs) and scrapper_actor.
For a tax or subsidy, list in `related` the markets the text or context names as related to the good: an input or factor
its sellers use (kind input: who sells it, price_variable wage_rate for workers, and its other users if named), or a
complement used with it (kind complement).
For any instrument, set field_contested to true if the text or context says the policy field the measure settles
(rent regulation, farm support) was already being fought over before it (a campaign, a petition, a recurring debate).
Name actor classes from the controlled list below where one fits. Otherwise use role.qualifier
(e.g. sellers.domestic_steel); never invent a new name when a listed one fits."""


def instructions() -> str:
    """The parser's full instructions: the system prompt and the controlled list of actor-class names."""
    from .vocabulary import actor_classes
    return PARSER_SYSTEM + "\n\nControlled actor-class names:\n" + ", ".join(actor_classes())


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def check_citations(record: PolicyRecord, text: str) -> list[str]:
    """Return a problem line for every quoted source sentence not found in the text."""
    body = _norm(text)
    problems = []
    for comp in record.components:
        if not comp.source_sentences:
            problems.append(f"{comp.id}: no source sentence quoted")
        for sent in comp.source_sentences:
            if _norm(sent) not in body:
                problems.append(f"{comp.id}: quoted sentence not in source: {sent[:80]!r}")
    return problems


def check_source_quotes(record: PolicyRecord, text: str, kept: list[Source]) -> list[str]:
    """Every related market that cites a source must quote it exactly, and the source must be one dated before enactment
    (`kept`); one that cites none and gives a quote must quote the policy text."""
    by_id = {s.id: _norm(s.text) for s in kept}
    body = _norm(text)
    problems = []
    for comp in record.components:
        for i, rel in enumerate(comp.related, start=1):
            where = f"{comp.id} related r{i} ({rel.good})"
            if rel.source_id is not None and rel.source_id not in by_id:
                problems.append(f"{where}: source {rel.source_id} is not a source dated before enactment")
            elif rel.source_id is not None and not (rel.quote and _norm(rel.quote) in by_id[rel.source_id]):
                problems.append(f"{where}: quote not found in source {rel.source_id}")
            elif rel.source_id is None and rel.quote and _norm(rel.quote) not in body:
                problems.append(f"{where}: quote not found in the policy text")
    return problems


ENRICH_SYSTEM = """You add related markets to a structured policy record for a praxeological analysis, using only the
context sources given (each published before the policy was enacted). For each component, list the markets the sources
name as related to its good: an input or factor its sellers use (kind input: who sells it, price_variable wage_rate where
they are workers, and its other users where a source names them), or a complement used together with the good (kind
complement). Every entry must give the id of the source it rests on and quote the sentence exactly. Add nothing a source
does not state; an empty list is a correct answer. Name actor classes as in the record (role.qualifier)."""


class ComponentRelations(BaseModel):
    id: str
    related: list[Related]


class Enrichment(BaseModel):
    components: list[ComponentRelations]


def enrich(record: PolicyRecord, enrichment: Enrichment) -> PolicyRecord:
    """The record with each component's proposed relations added to the ones it has (a relation already listed for the
    same good and kind is kept, not duplicated)."""
    add = {c.id: c.related for c in enrichment.components}
    comps = []
    for comp in record.components:
        have = {(r.kind, r.good) for r in comp.related}
        new = [r for r in add.get(comp.id, []) if (r.kind, r.good) not in have]
        comps.append(comp.model_copy(update={"related": list(comp.related) + new}) if new else comp)
    return record.model_copy(update={"components": comps})


def enrich_llm(record: PolicyRecord, kept: list[Source], model: str = MODEL, effort: str = "medium") -> PolicyRecord:
    """Ask the LLM for related markets from the pre-enactment sources, then add them to the record. The quotes are checked
    afterwards by `check_source_quotes` (the pipeline reports every failure)."""
    if not kept:
        return record
    import anthropic

    client = anthropic.Anthropic()
    sources = "\n\n".join(f"[{s.id}] ({s.citation}, {s.date})\n{s.text}" for s in kept)
    resp = client.messages.parse(
        model=model,
        max_tokens=8000,
        system=ENRICH_SYSTEM,
        output_config={"effort": effort},
        messages=[{"role": "user", "content": f"Policy record:\n\n{record.model_dump_json(indent=1)}\n\nContext sources:\n\n{sources}"}],
        output_format=Enrichment,
    )
    if resp.stop_reason == "refusal" or resp.parsed_output is None:
        raise RuntimeError(f"enrichment returned nothing (stop_reason={resp.stop_reason})")
    return enrich(record, resp.parsed_output)


def parse_fixture(path: Path) -> PolicyRecord:
    return PolicyRecord.model_validate_json(path.read_text())


def parse_llm(text: str, model: str = MODEL, effort: str = "medium") -> PolicyRecord:
    import anthropic

    client = anthropic.Anthropic()
    resp = client.messages.parse(
        model=model,
        max_tokens=16000,
        system=instructions(),
        output_config={"effort": effort},
        messages=[{"role": "user", "content": f"Policy text:\n\n{text}"}],
        output_format=PolicyRecord,
    )
    if resp.stop_reason == "refusal" or resp.parsed_output is None:
        raise RuntimeError(f"parser returned no record (stop_reason={resp.stop_reason})")
    return resp.parsed_output
