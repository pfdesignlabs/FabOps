# Sprint 1 — Strom (v0.1)

## Periode
Sprint 1  
Start: 23-11-2025  
Eind:  

## Sprint Goal

Een eerste end-to-end “skelet” neerzetten van Strom:

- ESP32 draait op een breadboard en is programmeerbaar.
- Basis firmwareproject staat (PlatformIO).
- MQTT-structuur is gedefinieerd en getest met een heartbeat.

Focus: **Electronics + Firmware + Backend-basics.**  
Geen ID of manufacturing in deze sprint — die komen in Sprint 2.

---

## Scope — Geselecteerde User Stories

### 1) US-EE-01 — Breadboard ESP32 setup

> As engineer, I want a breadboard ESP32 setup so basic logic boots.  
> Acceptance:
> - stable serial output

**Beoogd resultaat deze sprint:**
- ESP32 op breadboard met voeding.
- USB-serieel werkt, simpele testfirmware draait.

---

### 2) US-FW-01 — PlatformIO skeleton

> As engineer, I want PlatformIO skeleton so modules can plug in.  
> Acceptance:
> - compiles clean

**Beoogd resultaat deze sprint:**
- Werkend PlatformIO-project in de Strom-repo.
- Basisstructuur voor modules (WiFi, MQTT, sensors, presence).

---

### 3) US-BE-01 — MQTT topics gedefinieerd

> As engineer, I want MQTT topics defined so data structured.  
> Acceptance:
> - mapping documented

**Beoogd resultaat deze sprint:**
- Duidelijke topic-structuur voor Strom.
- Handmatige/test-publish werkt (via mosquitto_pub / Node-RED / HA).

---

## Taken (6 stuks) — gekoppeld aan bestanden

> Let op: paden en bestandsnamen gaan uit van de eerder gegenereerde tasks-structuur  
> (`tasks_full/…`). Gebruik in deze repo bij voorkeur `00.tracking/03.tasks/…`.

---

### US-EE-01 — Breadboard ESP32 setup

**Task 1 — Voorbereiding breadboard ESP32**

Bestand:  
`00.tracking/03.tasks/electronics/US-EE-01/Task - Electronics - US-EE-01 - Voorbereiding Uitvoeren.md`

Doel:
- ESP32-module, voeding, USB-serial en basisbekabeling klaarzetten.

Concreet:
- ESP32 pinout checken
- 3V3 / GND rails op breadboard
- USB-UART koppelen
- Basis smoke-check (geen oververhitting, juiste spanning)

---

**Task 2 — Implementatie en validatie breadboard setup**

Bestand:  
`00.tracking/03.tasks/electronics/US-EE-01/Task - Electronics - US-EE-01 - Implementatie en Validatie.md`

Doel:
- Simpele testfirmware flashen en seriële output valideren.

Concreet:
- “Blink” of “hello world” firmware flashen
- Seriële output loggen
- Resultaat vastleggen in log + foto van breadboard toevoegen

---

### US-FW-01 — PlatformIO skeleton

**Task 3 — Voorbereiding PlatformIO project**

Bestand:  
`00.tracking/03.tasks/firmware/US-FW-01/Task - Firmware - US-FW-01 - Voorbereiding Uitvoeren.md`

Doel:
- Basisprojectstructuur neerzetten.

Concreet:
- Nieuw PlatformIO-project `strom_firmware` aanmaken
- Board-config (ESP32) instellen
- Mapstructuur voor modules (core, wifi, mqtt, sensors, presence) aanleggen
- Project in repo plaatsen

---

**Task 4 — Implementatie en validatie PlatformIO skeleton**

Bestand:  
`00.tracking/03.tasks/firmware/US-FW-01/Task - Firmware - US-FW-01 - Implementatie en Validatie.md`

Doel:
- Skeleton build clean laten compileren en flashen.

Concreet:
- Lege main-loop + eenvoudige logregel
- Build uitvoeren (geen warnings ideally)
- Firmware flashen naar breadboard-ESP32
- Seriële logging bevestigen
- Log + screenshot committen

---

### US-BE-01 — MQTT topics gedefinieerd

**Task 5 — Voorbereiding MQTT structuur**

Bestand:  
`00.tracking/03.tasks/backend/US-BE-01/Task - Backend - US-BE-01 - Voorbereiding Uitvoeren.md`

Doel:
- Topic-structuur en naamgevingsconventies bepalen.

Concreet:
- Basisstructuur uitwerken, bv.:

  - `strom/<device_id>/presence`  
  - `strom/<device_id>/sensors`  
  - `strom/<device_id>/state`  
  - `strom/<device_id>/debug`  

- Mapping doc maken onder `06.firmware` en/of `03.architecture`
- Brokerconfig checken (adres, user/pass)

---

**Task 6 — Implementatie en validatie MQTT structuur**

Bestand:  
`00.tracking/03.tasks/backend/US-BE-01/Task - Backend - US-BE-01 - Implementatie en Validatie.md`

Doel:
- Handmatig (of via simpele script/CLI) berichten publiceren en checken.

Concreet:
- Mosquitto_pub / Node-RED / HA gebruiken om testmessages op de nieuwe topics te zetten
- Subscriben en valideren dat berichten correct binnenkomen
- Screenshots van subscriber + korte log in repo onder `08.validation` of `06.firmware`

---

## Definition of Done — Sprint 1

Sprint 1 is “done” als:

- US-EE-01, US-FW-01 en US-BE-01 op **Done** staan in je board.
- Breadboard-ESP32 draait een testfirmware met stabiele seriële output.
- PlatformIO-project in de Strom-repo staat en clean buildt & flasht.
- MQTT-topicstructuur is gedocumenteerd én getest met echte berichten.
- Minimaal één logbestand + één foto zijn toegevoegd als bewijs.

---

## Aanbevolen volgorde in de week

1. **Dag 1–2**  
   - US-EE-01 → breadboard + flash test  
2. **Dag 2–3**  
   - US-FW-01 → PlatformIO skeleton + testbuild  
3. **Dag 3–4**  
   - US-BE-01 → MQTT topics + testpublish  
4. **Dag 5**  
   - Opschonen, documentatie, commits, taggen van Sprint 1 resultaten
