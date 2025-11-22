# FabOps Capability Library

Each subfolder defines a reusable capability module that can be activated per project. A capability bundles:

- a mission statement (`capability.md`)
- machine-readable metadata (`metadata.yaml`)
- maturity guidance (`maturity/`)
- execution guides (`playbooks/`)
- a forward-looking `roadmap.md`

Automation uses `capability_index.yaml` to determine which folder to load during scaffolding.
