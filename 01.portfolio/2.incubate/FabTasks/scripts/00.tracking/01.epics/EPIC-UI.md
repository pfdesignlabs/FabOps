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
