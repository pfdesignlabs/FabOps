# EPIC — Firmware

## Purpose
Deliver the intelligence layer of Strom: provisioning, presence detection, MQTT, HomeKit-ready architecture.

## Goals
- WiFi provisioning MVP
- Presence engine (Hall + coil delta)
- MQTT telemetry pipeline
- OTA baseline

## Scope
- PlatformIO project
- Sensor drivers
- Presence logic
- OTA partitions

## Out of Scope
- Backend automations
- Hardware design

## KPIs
- Boot → MQTT < 8s
- Presence latency < 150ms
- Uptime 48h without crash

## Links
- ../02.stories/
- ../../06.firmware/README.md
