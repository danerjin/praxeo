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
