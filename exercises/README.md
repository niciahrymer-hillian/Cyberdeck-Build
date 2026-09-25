# Exercises — Power Budget Calculator

A hands-on companion to Lesson 1 (power budgeting) in the interactive tour. Same math as the tour's
Power Budget Planner tab — this is about understanding and reusing the formulas yourself, in code you
can drop into a real script later.

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 7 failing tests — every function in `power_budget.py` currently raises `NotImplementedError`.

## What to do

Open `power_budget.py`. Implement in this order:

1. `total_draw_ma` — sum the mA draw across a list of (name, mA) components.
2. `usable_mah` — apply the boost-conversion efficiency to a battery's rated capacity.
3. `estimated_runtime_hours` — reuse `usable_mah`, divide by total load. This is the forward
   question: "how long will this battery last?"
4. `battery_needed_for_target_hours` — the reverse question: "what capacity do I need to buy to hit a
   target runtime?" — the one you actually ask standing in front of a battery listing.

Check every result against Lesson 1's worked example (1250mA load, 10,000mAh @ 85% efficiency ≈ 6.8
hours) as you go.

## When you're done

All 7 tests passing means you have a real, reusable power-budget calculator — not just numbers you
trust the browser tool to get right, but math you can verify and extend yourself.
