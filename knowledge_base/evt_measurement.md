---
phase: validation
capabilities:
  - electronics
  - fabrication
last_reviewed: 2025-01-10
---

# EVT Measurement Playbook Companion

- Capture instrument configuration (firmware, calibration ID) per test case.
- Log measurements as CSV in `electronics/data/evt/` and store plots in `assets/`.
- Summaries roll into `EVT_REPORT.md` before the gate review.
- Agents verify that every blocker found here is mirrored in each discipline `open_actions.md`.
