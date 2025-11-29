# CAD Design Capability

The CAD Design capability covers geometry exploration, parametric modeling, and translation into manufacturable artefacts. It bundles hands-on prototyping methods (FDM, resin, vacuum casting) with a consistent research → SOP workflow.

## Deliverables
- Parametric CAD sources (versions tagged per gate)
- CMF documentation and ergonomic evaluations
- Manufacturing-ready exports (STEP/STL/DXF) tied to SOPs
- Readiness scorecards for each fabrication route

## KPIs
- Prototype readiness lead time per iteration
- % of CAD assets with linked manufacturing SOP
- Yield of printed / cast components during validation builds

## Sub-Capabilities
Each process folder implements the same lifecycle:

1. `01.research` – machine settings, materials, tolerance studies.
2. `02.process_development` – experiments to dial in print/casting parameters.
3. `03.validation` – measurement logs, QC snapshots, and sign-off notes.
4. `04.standardization` – checklists/templates for recurring work.
5. `05.examples` – reference builds with annotated CAD and photos.
6. `06.standard_operating_procedure` – versioned SOP documents.
7. `07.scripts` – automation (G-code snippets, Python helpers).

## Knowledge Hooks
- `02.knowledge_base/04.proof_of_concept/README.md`
- `knowledge_base/manufacturing_readiness.md`

## Interfaces
- Feeds manufacturing capability with validated geometries + SOPs.
- Consumes inputs from hardware and industrial research (ergonomics, tolerances).

Maintain the README of each sub-capability with the specifics of the material/process so agents can recommend the right path during project setup.
