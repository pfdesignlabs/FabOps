# EPIC — BACKEND (MQTT → Influx → Grafana → Automations)

## Purpose
Build FabTasks backend pipeline for ingesting, storing, and analyzing task/time events, aligned with FabOps data stack.

## Goals
- MQTT topics and payload spec
- Telegraf ingestion pipeline
- InfluxDB schema for tasks/time
- Grafana dashboards for focus analytics

## Scope (In)
- MQTT broker config
- Ingestion logic
- Database schema
- Dashboards
- Server-side scripts/automations

## Out of Scope
- Desktop UI implementation
- Hardware logic

## KPIs
- 99% ingestion reliability
- Dashboards load < 1s
- Schema remains stable across revisions

## Capability Level
Current: **C0**  
Next: **C1 – ingestion working**

## Links
- Backend stories
- Architecture folder
