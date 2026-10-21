"""Every annex function and handler names the math core rules it is derived from."""
import inspect
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from mathpraxeo import bounds, bridge, capital, exchange, identities, statics  # noqa: E402
from mathpraxeo.rules import COUNTERPART, MATH_RULES  # noqa: E402

PUBLIC_EXEMPT = {"bridge": {"annex_pass", "diagnose", "to_markdown", "dump"}}


def test_every_public_function_declares_its_rules():
    for mod in (exchange, identities, capital, statics, bounds, bridge):
        exempt = PUBLIC_EXEMPT.get(mod.__name__.split(".")[-1], set())
        for name, fn in inspect.getmembers(mod, inspect.isfunction):
            if fn.__module__ != mod.__name__ or name.startswith("_") or name in exempt:
                continue
            rules = getattr(fn, "__math_rules__", None)
            assert rules, f"{mod.__name__}.{name} declares no math rules"
            assert set(rules) <= set(MATH_RULES), (name, rules)


def test_every_handler_has_a_derivation_line():
    for h in bridge.HANDLERS:
        assert h.rules and set(h.rules) <= set(MATH_RULES), h.name


def test_handlers_need_nothing_beyond_mr2_to_mr6():
    """Handlers attach sizes; only the CR-12 machinery uses MR-7, and MR-1 governs everything."""
    used = {r for h in bridge.HANDLERS for r in h.rules}
    assert used <= {"MR-2", "MR-3", "MR-4", "MR-5", "MR-6"}
    assert used == {"MR-2", "MR-3", "MR-4", "MR-5", "MR-6"}


def test_rules_document_matches_registry():
    doc = (HERE / "MATH_CORE_RULES.md").read_text()
    for r in MATH_RULES:
        assert f"### {r} " in doc, r
    assert set(COUNTERPART) == set(MATH_RULES)
