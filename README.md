
# FabOps — Product Development Operating System  
*PF Design Labs — 2025*

## What is FabOps?  
FabOps is our open‑framework for documenting, validating and eventually automating fabrication processes — from PCB prototyping and laser ablation to FDM and resin printing. It closes the gap between one‑off maker prototypes and scalable small‑batch production by treating every workflow as code: versioned, reproducible and human‑readable.

## Why FabOps?  
- Ensures consistency across projects.  
- Speeds up iteration while maintaining rigour.  
- Makes decision‑history, tasks and deliverables transparent.  
- Supports mixed human + AI workflows.  
- Enables hardware/software/content to live in the same operational model.

## Core Principles  
- **Iterative first** — loops over waterfall.  
- **Lean structure** — only what adds value.  
- **Agent‑friendly** — clear, deterministic, machine‑readable.  
- **Advisor mode** — human makes final call.  
- **Documentation‑first** — decisions, tasks, phases are always tracked.

## Repository Structure  
```
/docs/                     → Manifest, governance + changelog  
/01.capabilities/          → Capability modules + metadata  
/02.product_development/   → Lifecycle phases, templates, phase_capabilities.yaml  
/03.sales_marketing/       → GTM workspace (mirrors capability playbooks)  
/04.finance/               → Financial models referenced by capabilities  
/knowledge_base/           → Evergreen references linked from playbooks  
/config/                   → Schemas + bootstrap templates  
README.md                  → Entry point  
LICENSE
```

> All folders, files and templates follow naming and structure conventions defined in the Operational Spec now stored in `docs/`.

## Getting Started  
1. Clone the repo:  
   ```bash
   git clone https://github.com/pfdesignlabs/FabOps.git
   ```  
2. Review the operational specification: `docs/FabOps_manifest.md`.  
3. Use the bootstrap script (when available) to start a new project with the standard structure.  
4. Fill in your project inputs (product name, vision, constraints, etc.).  
5. Let the agent generate the folder structure and templates.  
6. Commit the initial scaffold. Start executing tasks.  

## For Engineers & Makers  
- Each capability folder under `01.capabilities/` documents scope + maturity and ships playbooks.
- Active project disciplines mirror the capability pattern (`README`, `open_actions.md`, `decisions.md`, `assets/`, `data/`).
- `knowledge_base/` offers canonical measurement guides and readiness examples referenced from playbooks and gate reviews.

## For AI Agents  
- The repository layout and config demonstrate machine‑readable structure (`fabops.config.json`).  
- Agents signal phase transitions, blockers, missing documents and update the config JSON.  
- Agents adhere to advisor mode: they propose, human validates.

## Versioning & Governance  
- Spec version: **v1.0.0**  
- Framework follows Semantic Versioning (SemVer).  
- Each project records the spec version used in its `fabops.config.json`.  
- Major changes to the spec go through a review process, version bump and changelog.

## License  
This project is licensed under the MIT License — see the LICENSE file for details.

---

## Contributing  
We welcome contributions.  
Please open issues for suggestions, improvements or modular capabilities.  
For significant changes (especially to the core specification), submit a pull request and reference the versioning guidelines.
