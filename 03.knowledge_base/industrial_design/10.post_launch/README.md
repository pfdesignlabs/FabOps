---
phase: post_launch
default_capabilities:
  - software
gate: GATE_POST_LAUNCH_REVIEW
---

# Post-Launch Guide

## Objectives
- Monitor field performance, support incidents, and plan iterative releases.
- Feed learnings back into capabilities and the knowledge base.

## Required Deliverables
- Telemetry dashboard snapshots (uptime, adoption, error rates).
- RMA / support report with root-cause notes.
- Lessons-learned summary and backlog updates.

## Evidence Checklist
- Linked monitoring/runbook references.
- Ticketing exports or aggregated stats.
- Updates to `open_actions.md` for follow-up engineering work.

## Capability Hooks
- **Software:** owns telemetry + release cadence.
- Works with Hardware/Electronics to triage escalations requiring physical design changes.

## Related Knowledge
- Keep `02.knowledge_base/product_development.md` (section 11) and `knowledge_base/launch_readiness.md` handy for context.
