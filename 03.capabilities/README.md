# FabOps Capability Library

Every folder in this directory represents an operational capability family. Each family describes:

- **Mission & scope** – what problems this capability solves for FabOps projects.
- **Deliverables & KPIs** – the artefacts and metrics that keep the capability accountable.
- **Sub-capabilities** – repeatable processes (e.g. `3d_printing_fdm`) with numbered lifecycle folders (`01.research` → `07.scripts`).
- **Knowledge hooks** – references to `02.knowledge_base` (phase guidance) and `knowledge_base/` (detailed measurement guides).

## Folder Conventions

```
01.capabilities/
  cad design/
    README.md
    metadata.yaml
    roadmap.md
    3d_printing_fdm/
      README.md
      01.research/
      02.process_development/
      ...
  electronics/
    README.md
    metadata.yaml
    roadmap.md
  hardware/
  software/
  capability_index.yaml
```

1. **README.md** — narrative description, deliverables, KPIs, dependencies.
2. **metadata.yaml** — machine-readable schema consumed by agents / bootstrap tooling.
3. **roadmap.md** — capability growth path (H1/H2, maturity targets).
4. **Sub-capabilities** — optional nested folders with research → SOP structure for specialised processes.

## Extending the Library

1. Create a new folder under `01.capabilities/` using a short descriptive name.
2. Copy `metadata.yaml` from an existing capability and update the fields.
3. Document your growth path in `roadmap.md`.
4. If the capability requires process-specific folders, mirror the `cad design` structure.
5. Reference relevant articles inside `02.knowledge_base/` and `knowledge_base/` so agents can suggest material automatically.
6. Add the capability to `capability_index.yaml` with owner, maturity level, and knowledge hooks.
