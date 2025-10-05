# FabOps v0.1 — PF Design Labs (Process Documentation Mode)

**FabOps** is the open fabrication knowledge framework used across PF Design Labs projects.  
v0.1 focuses on **documenting** working processes, machine setups, and validated recipes — a single source of truth for in-house prototyping and small-batch production.

> Road to v1.0: this documentation layer will evolve into an automation runtime (Home-Assistant-like), where these same YAML workflows drive real equipment (MQTT/REST).

## Scope (current machines)
- **ComMarker B6 60 W MOPA** (fiber laser)
- **BambuLab P1S** (FDM 3D printer)
- **HeyGears Reflex** (resin 3D printer) + **HeyGears Wash** + **HeyGears Cure**
- **ProtoEtch v1** (PCB etching station, in development)
- **PrintNC** (CNC router, planned)

## Repository Layout
- `/machines/` — machine specifications, capabilities, firmware notes, calibration
- `/processes/` — workflows & SOPs (PCB prototyping, FDM, resin)
- `/docs/` — safety, methodology, materials, glossary, UI concept
- `/schemas/` — minimal JSON schemas for validation

## Usage
Treat each **workflow YAML** as the canonical procedure with versions.  
SOP markdown files break down the human steps. Validation photos and metrics go into the workflow’s `validation/`.

## Roadmap
- **v0.1:** Process documentation & validation (this repo).
- **v0.2:** Add “operator cards” rendering from YAML (PDF/HTML).
- **v0.3:** Introduce “actions” fields to workflows for future automation.
- **v0.4:** Optional local dashboards (Grafana/Streamlit).
- **v1.0:** FabOps runtime (API + MQTT orchestration with the same YAML).

**License:** MIT  
(C) 2025 PF Design Labs
