---
phase: design_validation_test
default_capabilities:
  - hardware
  - electronics
  - cad_design
gate: GATE_DVT_REVIEW
---

# Design Validation Test (DVT) Guide

## Objectives
- Verify robustness, compliance readiness, and cosmetic quality.
- Validate packaging, CMF, and user experience with production-like parts.

## Required Deliverables
- Reliability test report (temperature, vibration, drop, humidity, etc.).
- Usability feedback summary.
- Pre-compliance EMC report + mitigation plan.

## Evidence Checklist
- Fixture calibration logs and test scripts stored under `logs/`.
- DVT issue tracker referencing analytics + severity.
- Evidence of CMF + cosmetic sign-off (photos, measurements).

## Capability Hooks
- **Hardware:** owns reliability + structural integrity.
- **Electronics:** validates EMC/EMI, power thermals, firmware stability.
- **CAD Design:** ensures cosmetic criteria + material transitions meet spec.

## Related Knowledge
- Align with `02.knowledge_base/product_development.md` section 7 for deeper context.
