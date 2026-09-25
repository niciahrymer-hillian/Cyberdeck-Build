"""
Power Budget Calculator — fill in the four functions below.

Same math as the Power Budget Planner tab in the interactive tour
(docs/interactive/index.html), and the same numbers as Lesson 1's worked
example. The browser tool is for quick what-if planning; this is for
understanding — and reusing — the actual formulas yourself.

Run the tests as you go:  pytest exercises/test_power_budget.py -v
All four start failing. Implement one function, re-run, watch it turn green,
move to the next.
"""


def total_draw_ma(components):
    """Total current draw in mA across every component.

    `components` is a list of (name, ma) tuples.

    >>> total_draw_ma([("Pi", 900), ("Display", 300), ("Dongle", 50)])
    1250
    """
    # TODO: sum the ma value across all components
    raise NotImplementedError


def usable_mah(battery_mah, efficiency_pct):
    """Usable capacity in mAh after boost-conversion losses.

    A power bank's printed mAh rating is measured at the cell's native
    ~3.7V — see Lesson 1's trap. This applies the conversion efficiency to
    get the real usable capacity at the regulated output voltage.

    >>> usable_mah(10000, 85)
    8500.0
    """
    # TODO: return battery_mah * (efficiency_pct / 100)
    raise NotImplementedError


def estimated_runtime_hours(battery_mah, efficiency_pct, total_ma):
    """Estimated runtime in hours, given battery capacity, conversion
    efficiency, and total load.

    Reuse usable_mah() rather than recomputing the conversion inline —
    that's the point of having written it. Matches Lesson 1's worked
    example: 10,000mAh at 85% efficiency, 1250mA load, ~6.8 hours.

    >>> round(estimated_runtime_hours(10000, 85, 1250), 1)
    6.8
    """
    # TODO: return usable_mah(battery_mah, efficiency_pct) / total_ma
    raise NotImplementedError


def battery_needed_for_target_hours(target_hours, total_ma, efficiency_pct):
    """The reverse question: what battery capacity (mAh) do you need to buy
    to hit a target runtime, given your load and expected conversion
    efficiency?

    This is the actually useful direction when you're standing in front of
    a battery listing trying to decide which capacity to buy.

    >>> round(battery_needed_for_target_hours(8, 1250, 85), 1)
    11764.7
    """
    # TODO: return target_hours * total_ma / (efficiency_pct / 100)
    raise NotImplementedError
