---
phase: system_architecture
default_capabilities:
  - hardware
  - electronics
  - cad_design
gate: GATE_SYSTEM_ARCHITECTURE
---

# System Architecture Guide

## Objectives
- Translate value proposition into functional blocks with clear interfaces.
- Freeze initial BOM, budgets, and compliance targets.

## Required Deliverables
- Architecture diagram (mechanical, electrical, software blocks).
- Interface contracts (signals, protocols, mechanical envelopes).
- Preliminary BOM with cost targets and alternates.
- Risk register updated with mitigation owners.

## Evidence Checklist
- Block diagram stored under `02.product_architecture/` or project equivalent.
- Link to CAD envelopes (even coarse volumes) for mechanical-electrical alignment.
- Compliance + certification checklist started.

## Capability Hooks
- **Hardware:** drives tolerance stack-ups and assembly strategy.
- **Electronics:** defines voltage rails, MCU/SoC selection, sensor architecture.
- **CAD Design:** begins envelope studies to ensure manufacturability.

## Related Knowledge
- Reference `02.knowledge_base/product_development.md` section 3.
