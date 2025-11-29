# EPICS — Strom / FabOps Tracking (v1.0)

Epics vormen de hoogste strategische laag binnen het Strom-project.
Ze beschrijven capability-streams: disciplines die over het hele product heen lopen en die structureel volwassen moeten worden.

Epics zijn geen features en geen sprints.  
Het zijn de containers die richting geven aan user stories en tasks.

---

## 1. Doel van epics

Elke epic vertegenwoordigt:

- een capability die Strom moet ontwikkelen (bijv. PCB design, GFRC manufacturing)
- een strategisch doel dat groter is dan één sprint
- een langdurige lijn waar user stories en tasks onder vallen
- een FabOps-competentie die meetbaar moet groeien (C0 → C5)

Epics helpen om:
- focus te houden
- prioriteiten te bepalen
- technische debt te managen
- capabilities structureel te ontwikkelen

---

## 2. Hoe epics passen in de FabOps-workflow

Het proces werkt top-down in planning, bottom-up in executie:

EPIC (capability)  
↓  
USER STORY (weekdoel)  
↓  
TASK (uitvoerbare actie, 15–120 min)  
↓  
BUILD → TEST → LOG → COMMIT → DONE

Epics bepalen richting.  
Stories bepalen wat je deze week bouwt.  
Tasks bepalen wat je vandaag doet.

---

## 3. Strom Epics

Strom kent zes hoofd-epics:

### E1 — Industrial Design (ID)
Vormgeving, ergonomie, design for manufacturing, Fusion 360 parametrics.

### E2 — Electronics
Breadboard → ProtoEtch → Atopile → KiCad → productie-PCB.

### E3 — Firmware
PlatformIO, provisioning, MQTT, HomeKit, sensors, OTA.

### E4 — Manufacturing
Concrete/GFRC, PU casting, mold design, CNC, assemblies.

### E5 — Backend Integration
MQTT → Telegraf → InfluxDB → Grafana → HA automations.

### E6 — Validation & Reliability
Bench tests, thermal tests, soak tests, automation checks.

---

## 4. Structuur per epic

Voor elke epic komt een eigen bestand in deze map:

00.tracking/01.epics/  
    EPIC-ID.md  
    EPIC-ELECTRONICS.md  
    EPIC-FIRMWARE.md  
    EPIC-MANUFACTURING.md  
    EPIC-BACKEND.md  
    EPIC-VALIDATION.md  

### Template:

# EPIC — [NAAM]

## Purpose
Waarom bestaat deze epic? Welk probleem of capability ontwikkelt hij?

## Goals
- Doel 1  
- Doel 2  

## Scope
Wat valt binnen deze capability?

## Out of Scope
Wat hoort hier niet thuis?

## KPIs
Hoe meten we voortgang of volwassenheid?

## Links
- User stories  
- Tasks  
- Engineering docs  

---

## 5. Levenscyclus van een epic

1. Initiation (v0.x)  
2. Growth (v1.x)  
3. Maturity (v2.x)  
4. Sustainment (v3.x)

Een epic wordt nooit “done” — capabilities evolueren altijd.

---

## 6. Hoe vaak epics bijwerken

- Wekelijks → nooit  
- Maandelijks → korte review  
- Per prototype milestone → maturity update

---

## 7. Best Practices

- Gebruik epics alleen voor richting, niet voor micro-planning.  
- Stories starten altijd vanuit één epic.  
- Tasks kunnen epics overstijgen, maar blijven gelinkt aan hun story.  
- Epics blijven lean: geen tasks erin, geen details.

---

## 8. Capabiliteitsniveaus (optioneel)

C0 — Geen capability  
C1 — Experimentele fase  
C2 — Eerste workflow  
C3 — Betrouwbare workflow  
C4 — Kleine serie productie  
C5 — Volwassen capability  

---

## 9. Gerelateerde bestanden

- 00.tracking/02.stories/  
- 00.tracking/03.tasks/  
- manifest.md  
- engineering-README’s

---

## 10. Versiegeschiedenis

v1.0 — Initiële definitie voor Strom/FabOps.
