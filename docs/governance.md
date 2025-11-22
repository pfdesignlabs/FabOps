# FabOps Governance Rules

1. **Advisor-first** – agents propose edits, humans approve merges or governance changes.
2. **Versioned decisions** – any manifest or lifecycle update bumps the spec version and receives a changelog entry.
3. **Open capability proposals** – a new capability requires a metadata definition, roadmap, and at least one supporting playbook and knowledge-base reference.
4. **Gate stewardship** – each lifecycle phase must list a human steward responsible for reviewing gate outcomes.
5. **Schema validation** – automation changes must include updated JSON/YAML schemas in `/config` together with an example file.
6. **Sunsetting** – deprecated flows remain documented for at least one release cycle with clear migration guidance.

Use this file as the short-form reference; detailed policies live inside `FabOps_manifest.md`.
