# Electronics Capability

Designs, builds, and validates electronic subsystems from schematic through EVT/DVT.

## Deliverables
- Controlled schematics and PCB layouts (versioned per gate)
- BOM with sourcing strategy and alternates
- Bench logs, EVT/DVT measurement data
- Compliance readiness notes (EMC, safety)

## KPIs
- Prototype cycle time per spin
- First-pass yield during EVT
- Number of unresolved blockers per gate

## Operating Rhythm
1. Kickoff: define architecture, risks, and compliance targets.
2. Execution: maintain `open_actions.md`, `decisions.md`, and test data under `data/`.
3. Validation: sync measurement data with `knowledge_base/evt_measurement.md` to populate gate reviews.

## Interfaces
- Consumes inputs from hardware + CAD for mechanical constraints.
- Provides firmware + software teams with pin maps, APIs, and telemetry hooks.

See `metadata.yaml` for automation-friendly configuration.
