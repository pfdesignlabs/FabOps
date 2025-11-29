# FabTasks

FabTasks is PF Design Labs' internal project for structured task, time,
and evidence tracking, fully aligned with the FabOps operational model.

This repository provides:
- A FabOps-compatible project structure
- A single source of truth for epics, stories, tasks, and sprints
- Build logs and architecture documentation for the FabTasks product

FabTasks is not intended as a production-facing product repository yet.
It is the **delivery workspace** for developing, testing, and dogfooding
the FabTasks concept.

## Governance

- Methodology: FabOps v1.0
- Reference: `pfdesignlabs/FabOps` (docs/FabOps_manifest.md)
- Tracking model reference: Strom project structure (00.tracking, build_log, etc.)

All day-to-day progress should be reflected in:
- `00.tracking/` — epics, stories, tasks, sprints
- `01.build_log/` — dated worklogs
- `STATUS.md` — high-level status overview