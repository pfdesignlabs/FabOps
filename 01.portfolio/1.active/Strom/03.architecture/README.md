# Strom — Product Architecture (v0.1)

Deze documentatie beschrijft de end-to-end productarchitectuur van Strom:  
het samenspel tussen industrial design, electronics, firmware en backend.

Doel: een eenduidig blueprint die als referentie dient bij elke ontwerpbeslissing.

---

## 1. System Overview

Strom is een landscape iPhone-dock dat:

- Qi-charging combineert met fysieke presence-detectie
- omgeving meet (temp/RH/light)
- home-automation triggers aanstuurt (MQTT, HomeKit, Home Assistant)
- gebouwd is uit beton + hout + PU
- ESP32-gebaseerd is (PlatformIO firmware)

Het systeem bestaat uit **vier hoofdblokken**:

1. **Physical Interface Layer** (ID & Mechanica)  
2. **Electronics Layer** (PCB, sensors, power)  
3. **Firmware Layer** (ESP32 logic)  
4. **Backend Layer** (MQTT → Telegraf → InfluxDB → HA automations)

---

## 2. Architecture Diagram (Textual)

```
         ┌──────────────────────────────────────┐
         │              PHYSICAL LAYER           │
         │  • Concrete body                      │
         │  • Wood accent                        │
         │  • PU backplate (hidden LEDs)         │
         │  • Coil cavity + iPhone recess        │
         └──────────────────────────────────────┘
                          │
                          ▼
         ┌──────────────────────────────────────┐
         │              ELECTRONICS              │
         │  ESP32-WROOM                          │
         │  Hall sensor                          │
         │  Qi coil + current sensing            │
         │  Temp/RH/light sensors (I²C)          │
         │  USB-C 5V → buck/LDO → 3V3 rails      │
         └──────────────────────────────────────┘
                          │
                          ▼
         ┌──────────────────────────────────────┐
         │               FIRMWARE               │
         │  WiFi provisioning                    │
         │  Presence algorithm (Hall+coil)       │
         │  Sensor engine                        │
         │  MQTT + HomeKit                       │
         │  OTA updates                          │
         │  Diagnostics                          │
         └──────────────────────────────────────┘
                          │
                          ▼
         ┌──────────────────────────────────────┐
         │               BACKEND                │
         │  MQTT broker                         │
         │  Telegraf ingest                     │
         │  InfluxDB metrics                    │
         │  Grafana dashboards                  │
         │  Home Assistant automations          │
         └──────────────────────────────────────┘
```

---

## 3. Subsystem Interfaces

### 3.1 ID ↔ Electronics

- Coil center alignment: ±1.5 mm  
- Hall-sensor position: consistent plane met coil  
- Sensor windows: PU diffusor 1–2 mm  
- PCB mounting bosses: 2–4 stuks, M2.5 target  
- Cable path: 5–6 mm diameter + strain relief

---

## 4. Electronics Architecture Summary

- ESP32 als main controller  
- Sensors via shared I²C bus  
- Qi-module levert charge + status-indicatie  
- Power-stage:
  - 5V input  
  - buck naar 3V3  
  - filtering voor sensors  

---

## 5. Firmware Architecture Summary

- Event-driven: presence events prioriteit  
- Periodic sensor publishing  
- OTA partitioning  
- MQTT als main transport, HomeKit als secondary  
- Button/LED interface

---

## 6. Telemetry Architecture

### MQTT Topics

```
strom/<id>/presence
strom/<id>/sensors
strom/<id>/state
strom/<id>/debug
```

### InfluxDB schema

Tags:
- `device_id`
- `room`
- `version`

Fields:
- `temperature_c`
- `humidity_rh`
- `light_lux`
- `present`
- `voltage_5v`
- `voltage_3v3`

---

## 7. Security Model (Basic)

- WiFi creds in ESP32 NVS  
- OTA via internal endpoint (no public OTA)  
- MQTT user/pass  
- SSL optional in P2  

---

## 8. Open Points

- Display integration type (SPI vs I²C)  
- Concrete/hout interface sealing  
- Exact Qi-model selection  
