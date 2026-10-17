import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mathpraxeo.capital import cap_gap_path, capitalized_loss, gap_share  # noqa: E402
from mathpraxeo.exchange import implied_velocity_change, price_level_change  # noqa: E402
from mathpraxeo.interval import Interval  # noqa: E402
from mathpraxeo.result import check_sign  # noqa: E402
from mathpraxeo.statics import ceiling_quantity_supplied, ceiling_shortage, tax_incidence  # noqa: E402


def test_interval_arithmetic():
    a, b = Interval(1, 2), Interval(-1, 3)
    assert (a + b) == Interval(0, 5)
    assert (a * b) == Interval(-2, 6)
    assert (a - b) == Interval(-2, 3)
    assert Interval(2, 4) / Interval(1, 2) == Interval(1, 4)
    with pytest.raises(ZeroDivisionError):
        a / b
    assert Interval(0.1, 0.2).sign == "increase" and Interval(-1, 1).sign == "ambiguous"


def test_equation_of_exchange_is_exact_identity():
    r = price_level_change(0.10, 0.0, 0.0)
    assert (r.value.lo, r.value.hi) == (pytest.approx(0.10), pytest.approx(0.10))
    r = price_level_change(0.10, Interval(-0.03, 0.02), Interval(0.01, 0.03))
    assert r.value.lo == pytest.approx(1.10 * 0.97 / 1.03 - 1)
    assert r.value.hi == pytest.approx(1.10 * 1.02 / 1.01 - 1)
    assert r.rung == "M0" and r.value.sign == "increase"
    v = implied_velocity_change(0.10, r.value.lo, 0.03)
    assert v.value.lo == pytest.approx(-0.03) and v.value.hi == pytest.approx(-0.03)


def test_shortage_and_supply_signs_follow_the_laws():
    s = ceiling_shortage(0.10, Interval(-0.5, -0.1), Interval(0, 0.2))
    assert (s.value.lo, s.value.hi) == (pytest.approx(0.01), pytest.approx(0.07))
    assert check_sign("increase", s) == "agrees" and s.note == ""
    q = ceiling_quantity_supplied(Interval(0.1, 0.3), Interval(0.3, 1.0))
    assert q.value.sign == "decrease" and "strained" in q.note
    with pytest.raises(ValueError):
        ceiling_shortage(0.1, Interval(-0.5, 0.2), 0.1)  # upward-sloping demand is rejected


def test_tax_incidence_shares_sum_to_the_tax():
    buyers, sellers = tax_incidence(0.10, -0.5, 0.5)
    assert buyers.value.lo == pytest.approx(0.05) and sellers.value.lo == pytest.approx(-0.05)
    buyers, sellers = tax_incidence(0.10, 0.0 - 1e-9, 1.0)  # inelastic demand: buyers bear almost all
    assert buyers.value.lo == pytest.approx(0.10, abs=1e-6)
    buyers, sellers = tax_incidence(0.10, Interval(-1.0, -0.2), Interval(0.2, 1.0))
    assert buyers.value.sign == "increase" and sellers.value.sign == "decrease"


def test_capitalization_is_monotone_and_signs_agree():
    gaps = cap_gap_path(10, Interval(0.03, 0.07), [0, 0, 0] + [0.02] * 7)
    assert (gaps[0].value.lo, gaps[0].value.hi) == (pytest.approx(0.03), pytest.approx(0.07))
    assert gap_share(gaps[2], Interval(0.03, 0.07), 3).lo > 0
    narrow = capitalized_loss(gaps, 0.06, 5)
    wide = capitalized_loss(gaps, Interval(0.04, 0.08), Interval(3, 10))
    assert wide.value.lo <= narrow.value.lo <= narrow.value.hi <= wide.value.hi
    with pytest.raises(ValueError):
        capitalized_loss(gaps, 0.05, 12)


def test_check_sign_never_overrides():
    r = ceiling_shortage(0.1, -0.3, 0.1)
    assert check_sign("decrease", r) == "contradicts"
    assert check_sign("ambiguous", r) == "indeterminate"


from mathpraxeo.capital import present_value  # noqa: E402
from mathpraxeo.identities import (debt_path, doubling_time, expected_penalty, inflation_tax,  # noqa: E402
                                   real_rate, sectoral_balance, stock_path, wait_time)
from mathpraxeo.statics import (cost_pass_through, equilibrium_shift, floor_surplus,  # noqa: E402
                                quantity_under_wedge, quota_rent, revenue_change, spending_change,
                                subsidy_incidence, tariff)


def test_identities():
    assert wait_time(300, 25).value.lo == pytest.approx(12)
    assert expected_penalty((0.1, 0.2), 1000).value == Interval(100, 200)
    assert inflation_tax(0.10, 1000).value.lo == pytest.approx(1000 * 0.1 / 1.1)
    assert real_rate(0.05, 0.02).value.lo == pytest.approx(1.05 / 1.02 - 1)
    assert sectoral_balance(private_surplus=0.03, foreign_surplus=0.01).value.lo == pytest.approx(-0.04)
    with pytest.raises(ValueError):
        sectoral_balance(private_surplus=0.03)
    d = debt_path(1.0, 0.05, 0.02, 0.0, 1).value
    assert d.lo == pytest.approx(1.05 / 1.02)
    k = stock_path(100, 0.02, 0, 1).value
    assert k.lo == pytest.approx(98)
    assert doubling_time(0.07).value.lo == pytest.approx(10.24, abs=0.01)
    assert present_value(100, 0.0, 5).value.lo == pytest.approx(500)


def test_supply_demand_intersection():
    p, q = equilibrium_shift(0.10, 0.0, -0.5, 0.5)  # demand up 10%: price up 10%, quantity up 5%
    assert p.value.lo == pytest.approx(0.10) and q.value.lo == pytest.approx(0.05)
    p, q = equilibrium_shift(0.0, 0.10, (-1.0, -0.2), (0.2, 1.0))  # supply up: price down, quantity up
    assert p.value.sign == "decrease" and q.value.sign == "increase"
    with pytest.raises(ValueError):
        equilibrium_shift(0.1, 0.0, 0.0, 0.0)


def test_partial_equilibrium_signs():
    assert floor_surplus(0.1, -0.3, 0.2).value.sign == "increase"
    assert quantity_under_wedge(0.1, -0.5, 0.5).value.lo == pytest.approx(-0.025)
    b, s = subsidy_incidence(0.1, -0.5, 0.5)
    assert b.value.sign == "decrease" and s.value.sign == "increase"
    r = tariff(0.25, 0.4, -0.4, 0.5)
    assert r["domestic_price"].value.lo == pytest.approx(0.25)
    assert r["domestic_output"].value.lo == pytest.approx(0.125)
    # imports = use - output: m * dM = ed * dp - (1 - m) * es * dp
    assert r["imports"].value.lo == pytest.approx((-0.4 * 0.25 - 0.6 * 0.5 * 0.25) / 0.4)
    assert quota_rent(10, 1000).value.lo == 10000
    assert spending_change(0.1, -0.5).value.sign == "increase" and spending_change(0.1, -1.5).value.sign == "decrease"
    cp = cost_pass_through(0.2, 0.1).value
    assert cp.lo == 0 and cp.hi == pytest.approx(0.02)
    assert revenue_change(0.2, 0.3, 0.0).value.lo == pytest.approx(0.5)  # no base response: revenue up by the rate ratio
    assert revenue_change(0.2, 0.3, (0.2, 0.6)).value.hi < 0.5


def test_examples_run_and_agree():
    import importlib.util
    root = Path(__file__).resolve().parents[1] / "examples"
    for name in ("we001_annex", "we013_annex"):
        spec = importlib.util.spec_from_file_location(name, root / f"{name}.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        text = mod.main()
        assert "contradicts" not in text
