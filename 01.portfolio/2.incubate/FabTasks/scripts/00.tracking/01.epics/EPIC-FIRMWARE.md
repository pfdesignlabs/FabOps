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
