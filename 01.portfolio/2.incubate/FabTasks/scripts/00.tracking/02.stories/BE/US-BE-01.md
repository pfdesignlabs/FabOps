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
