---
phase: production_validation_test
default_capabilities:
  - hardware
  - cad_design
gate: GATE_PVT_APPROVAL
---

# Production Validation Test (PVT) Guide

## Objectives
- Prove that the manufacturing process, tooling, and SOPs can produce at target yield.
- Validate packaging, labeling, and traceability.

## Required Deliverables
- Pilot build report (units built, yield, major issues).
- Process FMEA + control plan updates.
- Certification / regulatory submission packet status.

## Evidence Checklist
- Readiness checklist referencing `knowledge_base/manufacturing_readiness.md`.
- Signed SOPs stored in `01.capabilities/cad design/*/06.standard_operating_procedure/`.
- Manufacturing logs with parameter ranges and approvals.

## Capability Hooks
- **Hardware:** ensures assemblies meet fit/function, manages ECO/ECR.
- **CAD Design:** freezes tooling geometry and owns documentation for every process.

## Related Knowledge
- Combine this guide with `01.capabilities/cad design/roadmap.md` for maturity planning.
