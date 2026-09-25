# Cyberdeck-Build

### A portable, handmade computer: Raspberry Pi + touchscreen + mini keyboard + battery in a custom enclosure.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[🎮 Interactive Tour](docs/interactive/index.html) · [📋 Cheat Sheet](docs/CHEATSHEET.pdf) · [📖 Full Lesson](docs/LESSON.pdf) · [🔗 Resources](docs/RESOURCES.pdf)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

Part of **Chain K — Hardware & Systems Foundations**. Builds directly on **Raspberry-Pi-Tinkering** —
do that project first if you haven't.

## What this is

We're designing and building a handmade portable computer around a Raspberry Pi, where every decision —
power, display, input, enclosure, thermals — is one you make rather than one a manufacturer already
made for you. This is where the rest of Chain K converges: the headless-setup and systemd skills from
Raspberry-Pi-Tinkering apply directly once you're trimming the OS for battery life, and the soldering
and multimeter skills from Electronics-Circuits-Bench apply directly once you're wiring a battery and
diagnosing a connector that's failing intermittently. The lessons here are ordered by real failure
cost: get the power budget and the display right on a bench *before* you commit to an enclosure design,
because undoing enclosure work is expensive in a way undoing a wiring change isn't.

## Prerequisites

| Requirement | Notes |
|---|---|
| **Raspberry-Pi-Tinkering completed** | This project assumes headless setup, SSH, and systemd basics already covered there |
| A modern browser | Chrome, Firefox, Safari, or Edge — the interactive tour is a single HTML file, no install |
| Python 3.8+ (for the exercises) | Check with `python3 --version` |
| Nothing else required to start | Real hardware only needed once you move to the build itself — see below before buying anything |

## Items Needed

Covered in the [Hardware Buying Guide](#hardware-buying-guide-what-to-look-for--red-flags) below and
the chain-wide [Hardware Shopping List](../HARDWARE_SHOPPING_LIST.md#cyberdeck-build) with tiered picks
and links:

- [ ] Raspberry Pi 4 or 5 (already have one from Raspberry-Pi-Tinkering? Reuse it here)
- [ ] Official or well-reviewed power supply
- [ ] A 5–7" touchscreen (DSI preferred — see Lesson 2 before buying an HDMI one)
- [ ] A compact keyboard (mechanical or membrane)
- [ ] A USB battery bank or a LiPo/Li-ion pack **with an integrated BMS** — never bare cells
- [ ] MicroSD or NVMe storage
- [ ] Enclosure material (3D-printed via **3D-Printer-Build**, laser-cut, or a project box)
- [ ] An inline USB power meter, for Lesson 1's real-draw measurement

## Quick Start

1. **Open the interactive tour.** Double-click `docs/interactive/index.html` — no server, no build step.
2. **Work Lesson 1 (Power budgeting) first**, then open the **Power Budget Planner** tab and enter your
   own component list before buying a battery.
   > ⚠️ **You may get stuck here:** if your estimated runtime looks too good to be true, check your
   > efficiency percentage — 85% is realistic for a decent power bank; anything above ~90% is
   > optimistic for a real boost-converter.
3. **Work Lesson 2 (Display) before buying a screen.** Decide DSI vs HDMI touchscreen based on the
   lesson's tradeoffs, not just price.
4. **Do the skeleton-code exercise.**
   ```bash
   cd exercises
   python3 -m venv .venv && source .venv/bin/activate
   pip install pytest
   pytest -v
   ```
   You'll see 7 failing tests. Open `exercises/power_budget.py` and implement the four functions — full
   instructions in [`exercises/README.md`](exercises/README.md).
5. **Work Lessons 3 and 4**, then the Quiz, then Flashcards/Match/Pop Quiz for review.
   > ⚠️ **You may get stuck here:** Lesson 3's rule — electronics working loose on a bench before any
   > enclosure work — is the one people skip under time pressure. Don't. Redoing enclosure work because
   > a wiring problem surfaced late costs far more time than the bench test would have.
6. **When you're building for real:** follow the Build Order in `docs/LESSON_PLAN.md`, which has a
   verified video linked at the LiPo-safety step.
7. **Check the Report Card tab** any time — it shows your current Power Budget Planner estimate
   alongside your quiz/lesson progress. Click **Print / Save as PDF** to keep a dated copy in `docs/`.

## Exercise Overview

| # | Lesson | Concept | Hands-on |
|---|---|---|---|
| 1 | Power budgeting | Real vs nameplate draw, boost-converter efficiency, runtime formula | Power Budget Planner tab + `exercises/power_budget.py` |
| 2 | Display | DSI vs HDMI touch, config.txt overlays, touch coordinate rotation | Get video *and* touch working before any enclosure design |
| 3 | Assembly & thermals | "Electronics before enclosure," strain relief, thermal throttling | Sketch vent placement before finalizing an enclosure |
| 4 | Real-world testing | Measured vs calculated endurance, OS trimming | Time a real battery discharge; compare to your Lesson 1 estimate |

**Learning path:**
```
Lesson 1 (power budget)  →  Lesson 2 (display)  →  Lesson 3 (assembly & thermals)  →  Lesson 4 (test)
        ↓                                                                                    ↓
Power Budget Planner tab + exercises/power_budget.py                          Quiz → Report Card
```

## Hardware Buying Guide (what to look for & red flags)

**Parts list:** Raspberry Pi (4 or 5), official or well-reviewed power supply, a 5–7" touchscreen (HDMI
or DSI), a compact mechanical or membrane keyboard, a USB battery bank or Li-ion pack with a proper BMS,
microSD or NVMe storage, and enclosure material.

**What to look for:** buy the Pi from an authorised reseller — supply shortages produced a lot of
marked-up grey-market stock. Prefer DSI/official displays for driver support; generic HDMI panels often
need manual config and may not scale cleanly. For batteries, insist on an integrated protection circuit
and a known cell brand.

**Red flags:** Li-ion cells with no BMS or no brand marking (a genuine fire risk), microSD cards priced
far below market — counterfeit cards misreport capacity and fail silently — and screens sold with no
driver documentation or model number.

**Common failure points:** under-powered supplies causing brownouts and SD corruption, SD card wear from
constant writes, thermal throttling once the Pi is enclosed, and connectors under strain because the
internal layout leaves no slack.

## Why This Matters (Industry Application)

Building custom hardware end to end demonstrates persistence and systems thinking in a way software
alone doesn't. Power budgets, physical constraints, and integration problems are real engineering, and
the finished object is a conversation piece that shows genuine curiosity.

## How This Connects

Chain K (Hardware & Systems Foundations). Built on **Raspberry-Pi-Tinkering**; extended by
**Cyberdeck-Cellular-And-Media**.

## Project Layout

```
Cyberdeck-Build/
├── docs/
│   ├── interactive/index.html   # tour: lessons, quiz, flashcards, match, pop quiz, power budget planner, report card
│   ├── LESSON_PLAN.md           # short build-plan reference, with a step-specific video link
│   ├── LESSON.pdf               # the full written lesson, printable
│   ├── CHEATSHEET.pdf           # one-page formula/rule recap, printable
│   └── RESOURCES.pdf            # further-reading links, printable
├── exercises/
│   ├── power_budget.py          # skeleton — implement the 4 functions
│   ├── test_power_budget.py
│   └── README.md
└── README.md                    # this file
```

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
