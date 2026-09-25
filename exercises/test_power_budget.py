"""
Tests for power_budget.py. Every expected value matches Lesson 1's worked
example in the interactive tour (1250mA load, 10,000mAh @ 85% efficiency,
~6.8 hours) or a docstring example.
"""
import pytest

from power_budget import (
    total_draw_ma,
    usable_mah,
    estimated_runtime_hours,
    battery_needed_for_target_hours,
)


def test_total_draw_matches_lesson_1_worked_example():
    components = [("Pi 5", 900), ("7\" touchscreen", 300), ("Keyboard dongle", 50)]
    assert total_draw_ma(components) == 1250


def test_total_draw_empty_list_is_zero():
    assert total_draw_ma([]) == 0


def test_usable_mah_matches_lesson_1():
    assert usable_mah(10000, 85) == pytest.approx(8500.0)


def test_usable_mah_100_percent_efficiency_is_unchanged():
    assert usable_mah(5000, 100) == pytest.approx(5000.0)


def test_estimated_runtime_matches_lesson_1_worked_example():
    assert estimated_runtime_hours(10000, 85, 1250) == pytest.approx(6.8, abs=0.05)


def test_battery_needed_for_target_hours_matches_docstring():
    assert battery_needed_for_target_hours(8, 1250, 85) == pytest.approx(11764.7, abs=0.5)


def test_battery_needed_and_runtime_are_inverses():
    # Buying exactly the battery this function recommends should hit the target runtime.
    target = 5
    total_ma = 1000
    efficiency = 80
    needed = battery_needed_for_target_hours(target, total_ma, efficiency)
    actual_hours = estimated_runtime_hours(needed, efficiency, total_ma)
    assert actual_hours == pytest.approx(target, abs=0.01)
