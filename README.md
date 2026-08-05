# Cyberdeck-Build

### A portable, handmade computer: Raspberry Pi + touchscreen + mini keyboard + battery in a custom enclosure.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[📖 Lesson Plan](docs/LESSON_PLAN.md)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

> ⬜ **Scaffold pending.** Directory created to portfolio standard; full content to be built. Real-hardware build with an emulation/planning-first path. Part of **Chain K — Hardware & Systems Foundations**.

## Why This Was Built

A cyberdeck is a handmade portable computer, and building one is the point where all of Chain K converges:
a Pi as the brain, a screen, a keyboard, a battery, and an enclosure I design around them. Nothing about it
is bought pre-solved.

I want the experience of building a machine that isn't a product — figuring out power draw, physical layout,
and thermals myself, and ending up with something that works because I made the decisions rather than
because a manufacturer did.

## Hardware Buying Guide (What to look for & red flags)

**Parts list:** Raspberry Pi (4 or 5), official or well-reviewed power supply, a 5–7" touchscreen (HDMI or
DSI), a compact mechanical or membrane keyboard, a USB battery bank or Li-ion pack with a proper BMS,
microSD or NVMe storage, and enclosure material.

**What to look for:** buy the Pi from an authorised reseller — supply shortages produced a lot of marked-up
grey-market stock. Prefer DSI/official displays for driver support; generic HDMI panels often need manual
config and may not scale cleanly. For batteries, insist on an integrated protection circuit and a known
cell brand.

**Red flags:** Li-ion cells with no BMS or no brand marking (a genuine fire risk), microSD cards priced far
below market — counterfeit cards misreport capacity and fail silently — and screens sold with no driver
documentation or model number.

**Common failure points:** under-powered supplies causing brownouts and SD corruption, SD card wear from
constant writes, thermal throttling once the Pi is enclosed, and connectors under strain because the
internal layout leaves no slack.

## Why This Matters (Industry Application)

Building custom hardware end to end demonstrates persistence and systems thinking in a way software alone
doesn't. Power budgets, physical constraints, and integration problems are real engineering, and the
finished object is a conversation piece that shows genuine curiosity.

## Topics Covered

| Area | What this project covers |
|------|--------------------------|
| Design | Physical layout, ergonomics, and enclosure |
| Power | Battery capacity, draw, and safe charging |
| Display | Touchscreen selection, drivers, and configuration |
| Input | Compact keyboards and pointing devices |
| Assembly | Wiring, mounting, and thermal management |
| OS | Configuring the software for a small screen |

## How This Connects

Chain K (Hardware & Systems Foundations). Built on **Raspberry-Pi-Tinkering**; extended by **Cyberdeck-Cellular-And-Media**.

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
