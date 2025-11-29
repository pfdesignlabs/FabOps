#!/usr/bin/env python3
"""
Initialise FabTasks tracking skeleton:
- Epics
- Stories (incl. what we already did)
- A few tasks
- Sprint 1
- Build logs

Run from the FabTasks repo root.
"""

from pathlib import Path
import textwrap

BASE = Path(__file__).resolve().parent


def write(path: Path, content: str, overwrite: bool = False) -> None:
    """Write file if it doesn't exist (unless overwrite=True)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        print(f"[skip] {path}")
        return
    text = textwrap.dedent(content).lstrip("\n")
    path.write_text(text, encoding="utf-8")
    print(f"[write] {path}")


def main() -> None:
    # ---------------------------------------------------------
    # 1) Epics – high-level streams for FabTasks
    # ---------------------------------------------------------
    epics = {
        "00.tracking/01.epics/EPIC-BASIS.md": """
        # EPIC — FabTasks Foundation & Governance

        ## Goal
        Establish FabTasks as the internal, FabOps-aligned tracking product:
        clear governance, repo structure, and conventions for epics, stories,
        tasks, sprints, and evidence.

        ## Objectives
        - FabTasks repo aligned with FabOps manifest and Strom tracking model.
        - Text-first tracking that AI-agents and humans can both consume.
        - Clear conventions for IDs, folder structure, and status reporting.

        ## Scope
        - Defining FabTasks product vision and constraints.
        - Setting up repo structure and baseline documentation.
        - Defining tracking conventions (IDs, statuses, links to evidence).
        - Aligning with FabOps v1.0 operational specification.

        ## Out of Scope
        - Implementation of backend, device, or UI (these are separate epics).
        - Commercialisation and external launch strategy.

        ## KPIs
        - All FabTasks work items traceable via 00.tracking and 01.build_log.
        - STATUS.md reflects real project status at least weekly.
        - New projects can copy this structure with minimal changes.

        ## Links
        - ../README.md
        - ../../STATUS.md
        - FabOps manifest (pfdesignlabs/FabOps)
        """,

        "00.tracking/01.epics/EPIC-BACKEND.md": """
        # EPIC — Backend & FabOps Integration

        ## Goal
        Provide a reliable backend pipeline for FabTasks that plugs into the
        FabOps stack (MQTT → Telegraf → InfluxDB → dashboards / automations).

        ## Objectives
        - Ingest FabTasks device and desktop events via MQTT.
        - Persist task/time events in a queryable store.
        - Provide basic dashboards for utilisation and focus analysis.
        - Expose APIs or topics that other tools can consume.

        ## Scope
        - MQTT topics and message formats for FabTasks.
        - Data ingestion (Telegraf or equivalent) and storage schema.
        - Basic dashboards for internal use (Grafana / similar).
        - Glue scripts / automations (e.g. Node-RED / Python) as needed.

        ## Out of Scope
        - Detailed desktop UI design (covered in EPIC-UI).
        - Non-FabTasks-related analytics.

        ## KPIs
        - Event ingestion reliability > 99% in dogfooding phase.
        - End-to-end event latency (device → dashboard) < 1 s for typical load.
        - No schema-breaking changes without migration notes.

        ## Links
        - ../02.stories/BE/
        - ../../03.architecture/
        """,

        "00.tracking/01.epics/EPIC-ELECTRONICS.md": """
        # EPIC — FabTasks Electronics

        ## Goal
        Develop a small desk device PCB for FabTasks that can:
        - connect over WiFi,
        - talk MQTT to the backend, and
        - drive the required UI hardware (e.g. screen, input).

        This epic also captures the early FR-1 prototypes made with the
        ComMarker laser.

        ## Objectives
        - First working breadboard / FR-1 prototype (proof-of-concept).
        - A revision suitable for small-batch manufacturing.
        - Clear design rules aligned with in-house prototyping capability.

        ## Scope
        - Schematic and PCB design for the FabTasks device.
        - FR-1 laser-etched prototypes (ComMarker-based workflow).
        - Component selection and BOM management.
        - Basic power architecture and connectivity.

        ## Out of Scope
        - Detailed enclosure design (covered in EPIC-ID if added later).
        - High-volume DFM/DFT.

        ## KPIs
        - At least one FR-1 prototype fully assembled and smoke-tested.
        - Board can connect to WiFi and exchange MQTT messages.
        - BOM cost reasonable for internal dogfooding units.

        ## Links
        - ../02.stories/EE/
        - ../../05.electronics/
        """,

        "00.tracking/01.epics/EPIC-FIRMWARE.md": """
        # EPIC — FabTasks Firmware

        ## Goal
        Build firmware for the FabTasks device that:
        - connects reliably to WiFi and MQTT,
        - can send and receive task/time events,
        - is easy to iterate as the product evolves.

        ## Objectives
        - Minimal, robust firmware skeleton (PlatformIO or similar).
        - Configurable MQTT topics and payloads.
        - Support for basic user input and feedback on the device.

        ## Scope
        - Firmware architecture and module layout.
        - WiFi + MQTT connectivity.
        - Handling of core events (start/stop task, status ping, etc.).
        - Logging and basic error handling.

        ## Out of Scope
        - Advanced power management and OTA updates (future work).
        - Non-core experiments that don't touch FabTasks.

        ## KPIs
        - Device connects to WiFi and backend within a few seconds of boot.
        - Event round-trip verified end-to-end in at least one sprint.
        - Firmware project builds reproducibly on a fresh checkout.

        ## Links
        - ../02.stories/FW/
        - ../../06.firmware/
        """,

        "00.tracking/01.epics/EPIC-UI.md": """
        # EPIC — Desktop & Operator UI

        ## Goal
        Provide a simple but effective operator interface for FabTasks:
        desktop tooling that shows connection status, tasks, and time
        in a way that is pleasant to use during real work.

        This includes using the existing FabOps stack where sensible
        and staying close to what was explored earlier (desktop tool
        connecting over WiFi/MQTT to a backend running in Docker).

        ## Objectives
        - MVP desktop tool that can:
          - show connectivity state,
          - send basic commands (e.g. start/stop task),
          - reflect state from the backend.
        - Ability to create new todos/tasks from the UI.
        - Optional: show quotes or motivational snippets on the device/UI.

        ## Scope
        - Desktop application(s) and/or web UI for internal use.
        - Integration with backend for task/time management.
        - Visualisation of current work, recent history, and focus.

        ## Out of Scope
        - Polished commercial UI.
        - Multi-tenant or multi-team features.

        ## KPIs
        - Internal user(s) can run FabTasks during a real workday.
        - No blocking usability issues during dogfooding.

        ## Links
        - ../02.stories/UI/
        - ../../05.electronics/
        - ../../03.architecture/
        """,

        "00.tracking/01.epics/EPIC-DOGFOOD.md": """
        # EPIC — Internal Dogfooding

        ## Goal
        Use FabTasks on real PF Design Labs projects (zoals Strom, GFRC,
        etc.) to validate that the concept actually helps focus and
        documentation instead of adding friction.

        ## Objectives
        - Track at least one full sprint of a real project with FabTasks.
        - Use generated evidence (commits, logs) to update FabOps docs.
        - Collect feedback on what works / what is annoying.

        ## Scope
        - Setting up FabTasks for internal projects.
        - Capturing feedback and converting it to new stories/tasks.
        - Minimal reporting (what did we ship, waar ging tijd heen).

        ## Out of Scope
        - External users of FabTasks.
        - Public beta / SaaS.

        ## KPIs
        - At least one project where >80% van het werk via FabTasks loopt.
        - Concrete list of improvements for a v2.

        ## Links
        - ../02.stories/DG/
        - ../../01.build_log/
        """,

        "00.tracking/01.epics/EPIC-OPEN.md": """
        # EPIC — Open-Source Packaging & Documentation

        ## Goal
        Package FabTasks as an open repository that others can study,
        fork, or adapt — without over-investing in polish at this stage.

        ## Objectives
        - Clean public README with positioning and limitations.
        - Minimal docs for replicating the stack (device + backend + UI).
        - Clear boundaries between "internal hacks" and "reusable patterns".

        ## Scope
        - Public-facing documentation.
        - License and contribution notes.
        - Examples of FabOps-aligned tracking.

        ## Out of Scope
        - Building a SaaS offering.
        - Supporting arbitrary external use cases.

        ## KPIs
        - Repo is understandable for an external engineer in < 30 minutes.
        - Core concepts (FabOps + FabTasks) clearly come across.

        ## Links
        - ../02.stories/OP/
        - ../../README.md
        """
    }

    for rel, content in epics.items():
        write(BASE / rel, content)

    # ---------------------------------------------------------
    # 2) Stories – include what we already did
    # ---------------------------------------------------------
    stories = {
        "00.tracking/02.stories/BASIS/US-BA-01.md": """
        # US-BA-01 — As PF, I want FabTasks aligned with FabOps

        **Epic:** EPIC-BASIS  
        **Status:** done  
        **Priority:** P1  

        ## Story

        As PF Design Labs, I want FabTasks to follow the FabOps manifest
        and reuse the Strom tracking structure so that every new hardware
        project can be tracked in a consistent way.

        ## Acceptance Criteria

        - [x] FabTasks repo exists and is under version control.
        - [x] Baseline folder structure created via bootstrap script.
        - [x] 00.tracking contains epics, stories, tasks, sprints folders.
        - [x] STATUS.md gives a high-level overview.
        - [ ] FabTasks is referenced from broader FabOps documentation.

        ## Notes

        - Initial structure bootstrapped with `bootstrap_fabtasks.py`.
        - Based on lessons from Strom (00.tracking + build_log approach).

        ## Evidence

        - commits: TODO (fill in after pushing to GitHub)
        """,

        "00.tracking/02.stories/EE/US-EE-01.md": """
        # US-EE-01 — As engineer, I want a first FabTasks FR-1 prototype

        **Epic:** EPIC-ELECTRONICS  
        **Status:** in_progress  
        **Priority:** P1  

        ## Story

        As an engineer, I want a first FR-1 prototype PCB for the FabTasks
        device (made with the ComMarker laser) so that we can validate
        the basic layout, footprint choices, and our in-house PCB
        prototyping flow.

        ## Acceptance Criteria

        - [x] At least one FR-1 board is successfully etched and cut.
        - [ ] Board is populated with components.
        - [ ] Basic smoke test performed (no shorts, correct voltages).
        - [ ] Notes captured in 01.build_log and 05.electronics.

        ## Notes

        - “5 pcb gemaakt op fr1 met commarker laser” — captured from
          earlier discussions; this is part of this story.
        - Exact design and schematic still need to be locked in.

        ## Evidence

        - Photos of FR-1 boards: TODO
        - commits: TODO
        """,

        "00.tracking/02.stories/BE/US-BE-01.md": """
        # US-BE-01 — As engineer, I want FabTasks backend plumbing

        **Epic:** EPIC-BACKEND  
        **Status:** backlog  
        **Priority:** P1  

        ## Story

        As an engineer, I want a basic backend stack (MQTT → Telegraf →
        InfluxDB → dashboards / automations in Docker) for FabTasks,
        so that device and desktop tools can exchange task/time data.

        ## Acceptance Criteria

        - [ ] MQTT broker running for FabTasks topics.
        - [ ] Ingestion into a time-series store (e.g. InfluxDB) configured.
        - [ ] At least one dashboard showing FabTasks events.
        - [ ] Topic and payload conventions documented.

        ## Notes

        - Earlier ideas: desktop tooling talking over WiFi/MQTT to a
          backend running in Docker, with data ingestion on the server.
        - Reuse as much as possible from the existing FabOps stack.

        ## Evidence

        - docker-compose files: TODO
        - screenshots of dashboards: TODO
        """,

        "00.tracking/02.stories/UI/US-UI-01.md": """
        # US-UI-01 — As user, I want a simple FabTasks desktop tool

        **Epic:** EPIC-UI  
        **Status:** backlog  
        **Priority:** P2  

        ## Story

        As a user, I want a simple desktop tool that connects to the
        FabTasks backend so that I can see my current task, start/stop
        work, and optionally create new todos without context switching.

        ## Acceptance Criteria

        - [ ] Desktop tool can connect to backend over the network.
        - [ ] User can see current task and basic status.
        - [ ] User can start/stop a task from the tool.
        - [ ] New todos/tasks can be created and propagated to backend.

        ## Notes

        - Eerdere bullets:
          - Desktop tooling
          - WiFi + MQTT connectivity
          - Data ingestion on the server
          - Ability to create new todos
          - Showing quotes on “wink”/device

        ## Evidence

        - repo / directory for desktop tool: TODO
        - screenshots: TODO
        """,

        "00.tracking/02.stories/DG/US-DG-01.md": """
        # US-DG-01 — As PF, I want to dogfood FabTasks on real projects

        **Epic:** EPIC-DOGFOOD  
        **Status:** backlog  
        **Priority:** P2  

        ## Story

        As PF Design Labs, I want to use FabTasks to track at least one
        real project (e.g. Strom or GFRC lamps) end-to-end, so that we
        can validate whether FabTasks genuinely improves focus and
        documentation.

        ## Acceptance Criteria

        - [ ] One project formally selected for FabTasks dogfooding.
        - [ ] Epics/stories/tasks for that project are tracked in FabTasks.
        - [ ] At least one sprint fully executed with FabTasks in the loop.
        - [ ] Retro includes explicit feedback on FabTasks itself.

        ## Evidence

        - build_log entries referencing FabTasks usage: TODO
        """,

        "00.tracking/02.stories/OP/US-OP-01.md": """
        # US-OP-01 — As engineer, I want FabTasks to be understandable externally

        **Epic:** EPIC-OPEN  
        **Status:** backlog  
        **Priority:** P3  

        ## Story

        As an engineer looking at the FabTasks repo from the outside,
        I want to understand what it does, how it ties into FabOps, and
        what parts I can reuse, so that I can learn from or adapt it.

        ## Acceptance Criteria

        - [ ] README explains FabTasks in < 1 page.
        - [ ] High-level architecture available under 03.architecture.
        - [ ] Clear indication of what is experimental vs. stable.
        - [ ] Basic “getting started” path documented.

        ## Evidence

        - README diff after writing external-facing copy: TODO
        """
    }

    for rel, content in stories.items():
        write(BASE / rel, content)

    # ---------------------------------------------------------
    # 3) Tasks – including the FR-1 work you already did
    # ---------------------------------------------------------
    tasks = {
        "00.tracking/03.tasks/foundation/US-BA-01/Task - Foundation - US-BA-01 - Repo Setup.md": """
        # Task — Foundation — US-BA-01 — Repo Setup

        **Parent story:** US-BA-01  
        **Status:** done  
        **Owner:** Jochem  

        ## Definition of Done

        - [x] FabTasks repo created on GitHub.
        - [x] Local clone configured (`/Users/pfdesignlabs/Documents/Projects/FabTasks`).
        - [x] Bootstrap script toegevoegd en uitgevoerd.
        - [x] Basis-README en STATUS.md aanwezig.

        ## Notes

        - FabOps-aligned structuur opgezet via `bootstrap_fabtasks.py`.

        ## Evidence

        - commits: TODO
        """,

        "00.tracking/03.tasks/electronics/US-EE-01/Task - Electronics - US-EE-01 - FR1 Prototype via ComMarker.md": """
        # Task — Electronics — US-EE-01 — FR-1 Prototype via ComMarker

        **Parent story:** US-EE-01  
        **Status:** done (first iteration)  
        **Owner:** Jochem  

        ## Definition of Done

        - [x] PCB-patroon voorbereid voor FR-1.
        - [x] ComMarker laser gebruikt om 5 stuks te maken.
        - [ ] Resultaat gedocumenteerd (foto's + notities).
        - [ ] Lessen vastgelegd in 05.electronics en 01.build_log.

        ## Notes

        - Vanuit eerdere gesprekken: “5 pcb gemaakt op fr1 met commarker laser”.
        - Deze task legt dat expliciet vast als onderdeel van FabTasks.

        ## Evidence

        - Photos: TODO
        - commits / design files: TODO
        """,

        "00.tracking/03.tasks/electronics/US-EE-01/Task - Electronics - US-EE-01 - FR1 Prototype Smoke Test.md": """
        # Task — Electronics — US-EE-01 — FR-1 Prototype Smoke Test

        **Parent story:** US-EE-01  
        **Status:** todo  
        **Owner:** Jochem  

        ## Definition of Done

        - [ ] Prototype volledig bestukt.
        - [ ] Basis-voedingsmeting gedaan (3V3 / 5V indien relevant).
        - [ ] Geen abnormale warmteontwikkeling.
        - [ ] Resultaten gelogd in 01.build_log.

        ## Evidence

        - Multimeter readings: TODO
        - Photos: TODO
        """
    }

    for rel, content in tasks.items():
        write(BASE / rel, content)

    # ---------------------------------------------------------
    # 4) Sprint 1 – skelet & grounding
    # ---------------------------------------------------------
    sprint_1 = """
    # Sprint 1 — FabTasks (skeleton & grounding)

    ## Periode
    Sprint 1  
    Start: 23-11-2025  
    Eind: (fill in when closed)

    ## Sprint Goal

    Een eerste end-to-end “skelet” neerzetten van FabTasks:

    - FabOps-aligned projectstructuur staat.
    - Kern-epics, eerste user stories en een paar tasks bestaan.
    - Minimaal één al eerder uitgevoerd werkitem (FR-1 PCB via ComMarker)
      is vastgelegd als taak + story + evidence-hook.

    Focus: **Foundation + Electronics-basics.**

    ## Scope

    ### Epics in scope

    - EPIC-BASIS — FabTasks Foundation & Governance
    - EPIC-ELECTRONICS — FabTasks Electronics

    ### Stories in scope

    - US-BA-01 — FabTasks aligned with FabOps
    - US-EE-01 — First FabTasks FR-1 prototype

    ### Tasks in scope

    - Task — Foundation — US-BA-01 — Repo Setup
    - Task — Electronics — US-EE-01 — FR-1 Prototype via ComMarker
    - Task — Electronics — US-EE-01 — FR-1 Prototype Smoke Test

    ## Plan

    - Vastleggen wat al gedaan is (repo, structuur, eerste FR-1 prototypes).
    - Opzetten basale epics/stories voor backend, UI, dogfooding, open-source.
    - Aanmaken van eerste build_log entries.

    ## Review (to be filled at end of sprint)

    - Welke items zijn daadwerkelijk “done”?
    - Wat is nog half-af?
    - Wat hebben we geleerd over de structuur?

    ## Retro (to be filled at end of sprint)

    - Start doing: …
    - Stop doing: …
    - Keep doing: …
    """
    write(BASE / "00.tracking/04.sprints/sprint_1.md", sprint_1)

    # ---------------------------------------------------------
    # 5) Build logs – capturing past work
    # ---------------------------------------------------------
    log_early = """
    # 2025-11-02 — Early FabTasks Exploration (pre-structure)

    ## Context

    Vroege verkenning van wat FabTasks moet worden:
    - koppeling met FabOps,
    - desktop tooling die via WiFi/MQTT praat met een backend in Docker,
    - data-ingestie op de server,
    - mogelijkheid om nieuwe todos te maken,
    - quotes weergeven op een “wink”-achtige device,
    - UI die “gewoon werkt”.

    In deze fase zijn vooral ideeën en wensen vastgelegd, plus eerste
    hands-on experimenten met FR-1 PCB-prototyping via de ComMarker.

    ## Worklog

    - [x] Brainstorm features voor FabTasks (device + backend + UI).
    - [x] Eerste FR-1 PCB's geëtst met ComMarker (5 stuks).
    - [ ] Resultaten systematisch gedocumenteerd (dit log en 05.electronics).

    ## Linked Items

    - Story: US-EE-01 — First FabTasks FR-1 prototype
    - Epic: EPIC-ELECTRONICS

    ## Evidence

    - Notities uit ChatGPT-gesprekken (dit project).
    - Foto's / bestanden: TODO
    """
    write(
        BASE / "01.build_log/2025-11-02_early_fabtasks_exploration.md",
        log_early,
    )

    log_today = """
    # 2025-11-23 — FabTasks Structure Bootstrap

    ## Context

    De FabOps-werkwijze is gedefinieerd en er is een referentieproject
    (Strom). FabTasks wordt hernoemd en opgezet als zelfstandig project
    met een duidelijke, herhaalbare structuur.

    ## Worklog

    - [x] Besloten om project te hernoemen naar “FabTasks”.
    - [x] FabTasks repo-structuur gegenereerd met Python bootstrap-script.
    - [x] Skelet voor epics, stories, tasks en sprint 1 toegevoegd.
    - [ ] STATUS.md geüpdatet met de nieuwe epics en sprint.

    ## Linked Items

    - Story: US-BA-01 — FabTasks aligned with FabOps
    - Epic: EPIC-BASIS
    - Sprint: Sprint 1 — FabTasks (skeleton & grounding)

    ## Evidence

    - Dit script: `fabtasks_init_tracking.py`
    - commits: TODO
    """
    write(
        BASE / "01.build_log/2025-11-23_fabtasks_structure_bootstrap.md",
        log_today,
    )


if __name__ == "__main__":
    main()