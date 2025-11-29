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
