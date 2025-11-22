# FabOps Documentation Hub

This directory centralizes every reference that explains how FabOps works and evolves.

## Contents
- `FabOps_manifest.md` – the canonical operational specification.
- `CHANGELOG.md` – specification evolution log (create a new entry whenever the manifest changes).
- `governance.md` – lightweight rules for proposing and approving framework updates.
- `playbook_map.md` – link table between capability playbooks, lifecycle phases and knowledge-base articles.

## Usage
1. Start with `FabOps_manifest.md` to understand the principles, lifecycle and agent rules.
2. When tooling, capabilities or workflows are updated, record the change summary in `CHANGELOG.md` and cross-link to affected files.
3. Keep `playbook_map.md` in sync with new capabilities so agents can reason over the framework without scraping the entire repo.
4. Treat this folder as a knowledge source for onboarding; files should remain narrative and human-readable while other folders stay action-oriented.

## Maintenance Norms
- Prefer Markdown for human guidance and YAML/JSON schemas for automation references.
- Keep files short and purpose-built; if a document grows beyond ~500 lines consider splitting it with clear navigation links.
- Every release of FabOps should snapshot this folder to maintain historical traceability.
