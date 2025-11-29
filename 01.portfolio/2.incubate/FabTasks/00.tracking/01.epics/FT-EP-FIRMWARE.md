# EPIC — FIRMWARE (Connectivity, MQTT, Provisioning, UX Logic)

## Purpose
Create reliable firmware for the FabTasks device enabling WiFi provisioning, MQTT connectivity, and task-related UX flows.

## Goals
- Stable WiFi connectivity
- Correct MQTT publish/subscribe
- UX logic for task start/stop
- Device heartbeat & diagnostics

## Scope (In)
- WiFi stack
- MQTT handlers
- State machine
- Logging
- Error handling

## Out of Scope
- Backend storage
- Complex power management

## KPIs
- Connection within <3 seconds
- 99% reliable MQTT send/receive

## Capability Level
Current: **C0**  
Target: **C1 experimental firmware**

## Links
- Firmware directory
- Stories FW
- Tasks FW
