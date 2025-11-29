---
phase: engineering_validation_test
default_capabilities:
  - electronics
  - hardware
  - cad_design
gate: GATE_EVT_REVIEW
---

# Engineering Validation Test (EVT) Guide

## Objectives
- Validate functional performance of the integrated system with near-final prototypes.
- Capture measurement data to prove requirements are met.

## Required Deliverables
- EVT build manifest (units, configuration, firmware versions).
- Measurement logs + plots linked to requirements.
- Issue list with severity and owner.

## Evidence Checklist
- Bench data cross-referenced in `knowledge_base/evt_measurement.md`.
- CAD readiness status for every part feeding EVT builds.
- Firmware/software versions pinned in `fabops.config.json`.

## Capability Hooks
- **Electronics:** owns schematic/layout quality, sensor accuracy, thermals.
- **Hardware:** tracks assembly precision, mechanical durability, fixture health.
- **CAD Design:** ensures prints/casts meet tolerance + cosmetics to unblock EVT.

## Related Knowledge
- Use `knowledge_base/evt_measurement.md` and `01.capabilities/cad design/README.md` for SOP links.
