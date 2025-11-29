---
phase: proof_of_concept
default_capabilities:
  - hardware
  - electronics
  - cad_design
gate: GATE_POC_REVIEW
---

# Proof of Concept (PoC) Guide

## Objectives
- Retire the riskiest technical assumptions with simple rigs and experiments.
- Capture measurable evidence before scaling effort.

## Required Deliverables
- PoC build log with photos + measurements.
- Updated risk register showing which blockers are cleared.
- Recommendations for EVT scope.

## Evidence Checklist
- Bench data stored under `logs/` with calibration notes.
- Decision log entry referencing whether each PoC hypothesis is validated/invalidated.

## Capability Hooks
- **Hardware:** prototypes mechanical behaviors, tolerances, and assembly feasibility.
- **Electronics:** tests critical circuits, sensors, and noise budgets.
- **CAD Design:** prints or casts proof parts to validate ergonomics/CMF.

## Related Knowledge
- Tie findings back to `knowledge_base/project_foundation.md` for traceability.
