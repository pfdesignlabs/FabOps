#!/usr/bin/env python3
"""
Bootstrap FabTasks repo structure + baseline READMEs.

Usage:
    - Place this file in the root of the FabTasks repo
      (e.g. /Users/pfdesignlabs/Documents/Projects/FabTasks)
    - Run: python bootstrap_fabtasks.py
"""

from pathlib import Path
import textwrap

# -------------------------------------------------------------------
# Content templates
# -------------------------------------------------------------------

ROOT_README = """
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
"""

STATUS_MD = """
# FabTasks — Status Overview

_Last updated: (set this date manually when you update the file)_

## 1. Project Snapshot

**Project:** FabTasks  
**Owner:** PF Design Labs  
**Methodology:** FabOps v1.0  

**Mission:**  
Build an internal-first time and task tracking product that tightly
integrates with FabOps and supports evidence-based delivery
(epics → stories → tasks → commits → outcomes).

## 2. Epics (High-Level)

> This is a living table. Start with placeholders and refine as you go.

| Epic ID       | Name                          | Status       | Phase        |
|---------------|-------------------------------|-------------|--------------|
| FT-EP-BASIS   | FabTasks foundation           | planned     | Discovery    |
| FT-EP-DEVICE  | Hardware / device             | planned     | Architecture |
| FT-EP-BACKEND | Backend & data platform       | planned     | Architecture |
| FT-EP-DESKTOP | Desktop / client tools        | planned     | EVT          |
| FT-EP-DOGFOOD | Internal dogfooding           | planned     | DVT          |
| FT-EP-RELEASE | Open-source release & launch  | planned     | Launch       |

## 3. Current Sprint

**Current sprint:** (e.g. `Sprint 01 – 2025-W48`)  
**Goal:** (1–2 lines, what absolutely must be “shippable”)  

### 3.1 Scope

- Epics in scope:
  - …
- Stories in scope:
  - …
- Tasks in scope:
  - …

## 4. Risks & Decisions

Log only the relevant, non-trivial items.

### 4.1 Key Risks

- YYYY-MM-DD — Risk: …

### 4.2 Key Decisions

- YYYY-MM-DD — Decision: …

## 5. Links

- FabOps: `pfdesignlabs/FabOps`
- Reference structure: Strom sprint repo
"""

TRACKING_ROOT_README = """
# 00.tracking — FabTasks Delivery Tracking

This folder is the **single source of truth** for all work tracking:

- **01.epics**: strategic capability streams that run across disciplines  
- **02.stories**: user stories linked to epics  
- **03.tasks**: executable work items linked to stories  
- **04.sprints**: time-boxed delivery windows (planning, review, retro)

The intent is to keep tracking **tool-agnostic** and text-first, so it
can be consumed by humans, scripts, and AI agents.
"""

EPICS_README = """
# 01.epics — Strategic Streams

Epics represent the highest-level capability streams within FabTasks.
They are **not** features and **not** sprints. They describe
cross-cutting capabilities that must mature over time.

Examples (to be refined):

- FT-EP-BASIS   — FabTasks foundation / governance
- FT-EP-DEVICE  — Hardware / desk device
- FT-EP-BACKEND — Data backend & integrations
- FT-EP-DESKTOP — Desktop tools / UI
- FT-EP-DOGFOOD — Internal dogfooding & usage
- FT-EP-RELEASE — Open-source release & external launch

Each epic file should minimally include:

- Goal
- Problem
- Success criteria
- Scope (in / out)
- Linked user stories
- Decisions & notes
"""

STORIES_README = """
# 02.stories — User Stories

User stories describe behaviour from a user perspective:
“As a \<user\> I want \<capability\> so that \<value\>.”

Conventions:

- One file per story: `FT-US-XXX-short-handle.md`
- Explicit link back to a single epic (`Epic: FT-EP-…`)
- Status: backlog / ready / in_progress / in_review / done
- Acceptance criteria as a checklist
- Evidence section with links to commits, PRs, screenshots, etc.

Stories are the bridge between epics (direction) and tasks (execution).
"""

TASKS_README = """
# 03.tasks — Executable Work Items

Tasks are the atomic units of execution. They live inside this folder,
organised in a way that makes sense for you (per domain, per story, etc.).

Conventions:

- One directory per story, or per domain + story ID
- Inside that directory: one or more task files
- Task IDs: `FT-T-XXXX` where `XXXX` is a zero-padded integer

Each task file should cover:

- Parent story
- Status (todo / doing / review / done)
- Owner
- Sprint
- Definition of done
- Evidence links (commits, PRs, artifacts)

Tasks should be small enough to complete in a focused block of work.
"""

SPRINTS_README = """
# 04.sprints — Time-Boxed Delivery

Sprints capture planning, execution, and retro in one place.

File naming convention:

- `sprint-01-YYYY-WWW.md` (use ISO week numbers if helpful)

Each sprint file should include:

- Goal (1–2 lines: what must be shippable)
- Scope (epics, stories, tasks in scope)
- Plan (focus, constraints, risks)
- Review (what got done, what slipped, why)
- Retro (start / stop / keep)

This structure mirrors the Strom project approach but is tailored
specifically for FabTasks.
"""

BUILD_LOG_README = """
# 01.build_log — Daily Work Logs

This folder is your chronological execution history.

Conventions:

- One file per focused work session or per day
- Naming: `YYYY-MM-DD_short-handle.md`
  - Example: `2025-11-23_bootstrap-structure.md`

Each log should cover:

- Context: what you intended to work on
- Worklog: bullet list of actions (checked when completed)
- Linked items: epics, stories, tasks
- Evidence: commit hashes, PRs, screenshots, photos, etc.

The build log is not a planning tool; it is **what actually happened**.
"""

REQS_README = """
# 02.requirements — Product Requirements

Central place for FabTasks requirements.

Suggested structure:

- `product_vision.md`
- `personas.md`
- `use_cases.md`
- `non_functional_requirements.md`

Keep this level stable and high-signal. Detailed behaviour lives
in the user stories under `00.tracking/02.stories/`.
"""

ARCH_README = """
# 03.architecture — System Architecture

This folder holds system-level architecture for FabTasks:

- Context diagrams (how FabTasks interacts with FabOps stack)
- Logical architecture (modules, data flows)
- Deployment / runtime view (where things run)

Keep architecture lean but explicit, so it can drive
implementation choices and risk management.
"""

CAD_README = """
# 04.cad — Industrial Design / Enclosures

This folder contains all CAD assets for FabTasks hardware:

- Enclosure concepts and iterations
- Final enclosure models
- Exploded views and drawings

Use subfolders per iteration or per major concept if needed.
"""

ELECTRONICS_README = """
# 05.electronics — Hardware Design

Electronics design for FabTasks hardware:

- Schematics
- Layouts
- Prototypes (e.g. FR-1 laser-etched boards)
- BOMs and component notes

Align documentation with FabOps electronics capability,
so lessons learned can be upstreamed easily.
"""

FIRMWARE_README = """
# 06.firmware — Embedded Software

Firmware for the FabTasks device:

- Architecture and module overview
- PlatformIO / build configuration
- Experiments and prototypes
- Integration with FabOps stack (MQTT, etc.)

Every firmware experiment that influences the final product
should be captured here, even if it started in a scratch repo.
"""

MANUFACTURING_README = """
# 07.manufacturing — Manufacturing Process

This folder captures everything related to manufacturing:

- Process definitions (CNC, printing, casting, assembly)
- Jigs and fixtures
- Work instructions
- Quality checks

The goal is to move from “one-off prototype” to
repeatable, documented small-batch manufacturing.
"""

VALIDATION_README = """
# 08.validation — Test & Validation

Test and validation strategy for FabTasks:

- Functional tests
- Integration tests (device ↔ backend ↔ desktop tools)
- Long-term reliability tests (if relevant)
- Test protocols and checklists

Validation closes the loop: it connects requirements and architecture
to measurable outcomes in the real world.
"""

# -------------------------------------------------------------------
# Directory → file mapping
# -------------------------------------------------------------------

STRUCTURE = {
    "": {
        "README.md": ROOT_README,
        "STATUS.md": STATUS_MD,
    },
    "00.tracking": {
        "README.md": TRACKING_ROOT_README,
    },
    "00.tracking/01.epics": {
        "README.md": EPICS_README,
    },
    "00.tracking/02.stories": {
        "README.md": STORIES_README,
    },
    "00.tracking/03.tasks": {
        "README.md": TASKS_README,
    },
    "00.tracking/04.sprints": {
        "README.md": SPRINTS_README,
    },
    "01.build_log": {
        "README.md": BUILD_LOG_README,
    },
    "02.requirements": {
        "README.md": REQS_README,
    },
    "03.architecture": {
        "README.md": ARCH_README,
    },
    "04.cad": {
        "README.md": CAD_README,
    },
    "05.electronics": {
        "README.md": ELECTRONICS_README,
    },
    "06.firmware": {
        "README.md": FIRMWARE_README,
    },
    "07.manufacturing": {
        "README.md": MANUFACTURING_README,
    },
    "08.validation": {
        "README.md": VALIDATION_README,
    },
}


# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------

def write_file(path: Path, content: str, overwrite: bool = False) -> None:
    """Write text file, optionally preserving existing content."""
    if path.exists() and not overwrite:
        print(f"[skip] {path} (already exists)")
        return

    text = textwrap.dedent(content).lstrip("\n")
    path.write_text(text, encoding="utf-8")
    print(f"[write] {path}")


def bootstrap(base_dir: Path, overwrite: bool = False) -> None:
    """Create directories and baseline README / STATUS files."""
    for rel_dir, files in STRUCTURE.items():
        dir_path = base_dir / rel_dir if rel_dir else base_dir
        dir_path.mkdir(parents=True, exist_ok=True)
        for filename, content in files.items():
            write_file(dir_path / filename, content, overwrite=overwrite)


def main():
    # Default: run in the directory where this script lives
    base_dir = Path(__file__).resolve().parent
    print(f"Bootstrapping FabTasks structure in: {base_dir}")
    bootstrap(base_dir, overwrite=False)
    print("Done. Review STATUS.md and start filling in epics, stories, and sprints.")


if __name__ == "__main__":
    main()