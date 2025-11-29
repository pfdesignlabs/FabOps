# Project Strom — FabOps-Aligned Operational Manifest (v1.0)

Landscape iPhone Dock • HomeKit / Home Assistant integration • Environmental Automation Anchor

⸻

## 1. Strategic Intent

Strom is een capability-development traject vermomd als product.

Het primaire doel is het beheersen en op een hoger niveau brengen van de volgende capabilities:

- computer-aided design  
  - design for manufacturing (Design for Manufacturing)
- elektronica  
  - breadboard prototyping workflow  
  - Atopile PCB design  
  - component layout in KiCad  
  - ProtoEtch prototype workflow
- manufacturing / maakproces  
  - mould design  
  - vacuum casting  
  - concrete casting
- firmware  
  - PlatformIO
- content  
  - content creation workflow rond hardware launches

Omzet is een bonus, niet de driver.  
Strom is de testcase voor de volledige FabOps-pijplijn.

⸻

## 2. Clear Problem Definition

### 2.1 Gebruikersfrictie

- opladen is altijd vervelend  
- presence detection bij gebruikers van home automation is altijd een uitdaging  

### 2.2 Oplossingsrichting

Strom lost dit op door:

- **Presence certainty**  
  Device inserted = betrouwbare trigger voor automatisering.
- **Context switching**  
  Strom fungeert als fysieke automation trigger voor slapen.
- **Environmental sensing**  
  Metingen van temperatuur, luchtvochtigheid en lichtintensiteit.
- **Environment adaptation**  
  Het dock optimaliseert de fysieke omgeving zodra de iPhone wordt geplaatst.

⸻

## 3. Scope van project Strom

### 3.1 Hard Scope

- Landscape iPhone dock
- ESP32 controller
- Qi charging (Apple-compatible coil / module)
- Dual-sensor presence detection:
  - Hall-sensor (mechanische presence)
  - Coil current sensing (charge-state / presence-validatie)
- Licht / temperatuur / humidity sensors (I²C sensorstack)
- HomeKit + MQTT + Home Assistant support
- Optional hidden display for status indicators  
  (bijv. klein segment- of dot-matrixdisplay achter PU / plexi)

### 3.2 Soft Scope (optional / aspirational)

- CNC hybrid materials (wood / beton / PU)
- Touchless capacitive input (mode switching, mute, etc.)
- Ambient LED visual layer (subtiele status / mood)

⸻

## 4. Productarchitectuur — FabOps-structuur

This section maps each subsystem directly to a FabOps capability.

⸻

### 4.1 Industrial design

**Outcome:** manufacturable, Dieter-Rams inspired geometry.

Deliverables:

- Fusion 360 parametric model van de Strom-behuizing:
  - landscape wedge design, met verzonken recess voor iPhone
  - beton body
  - houten accent
  - matte PU backplate

⸻

### 4.2 Mechanische engineering

Deliverables:

- Qi coil alignment fixture (jig voor consistente coil-positie t.o.v. iPhone).
- Ventilatie / airflow voor coil thermals.
- Cable routing + strain relief (USB-C naar binnenzijde).
- Mounting holes voor PCB(s).
- Designed for manufacturing:
  - draft angles
  - mold splits
  - minimale secondary operations

Critical risks:

- Coil-to-device misalignment → charging faalt of is inconsistent.
- Concrete warping / shrinkage variance → slechte fit, spanningen in assembly.
- PU adhesion op beton / wood interfaces → delaminatie op termijn.

⸻

### 4.3 Elektronica

Board (Atopile → KiCad validated):

- ESP32-WROOM module.
- Qi coil driver input sensing (current sensing / status lines).
- Hall sensor voor mechanische presence detectie.
- Temp / humidity / light sensors.
- USB-C input.
- Power path:
  - Qi module supply
  - logic-supply met eigen LDO / buck.
- State override button (forceer / mute automation).
- Optional user interface voor state en sensor-readings  
  (LEDs, klein display of minimalistische indicatoren).

FabOps-koppeling:

- ProtoEtch wordt gebruikt voor vroege PCB-iteraties (FR-1, in-house).

⸻

### 4.4 Firmware

Key modules:

- WiFi provisioning:
  - fallback AP-mode
  - future-proof richting QR-based provisioning.
- Presence algorithm:
  - combinatie van Hall-sensor + coil current delta
  - debouncing / filtering voor betrouwbare triggers.
- Sensor acquisition:
  - periodieke meting temp / RH / lux
  - basale filtering en outlier-detectie.
- Event messaging:
  - MQTT topics richting FabOps backend / Home Assistant.
  - HomeKit integratie.
- OTA-updates:
  - basale OTA pipeline via HTTP / MQTT.
- Local diagnostic mode:
  - LED feedback / display codes voor provisioning, errors, testmodi.

⸻

### 4.5 Backend-integratie

Pipeline:

> Phone docked → ESP32 event → MQTT broker → Telegraf → InfluxDB → Automation (Node-RED / Home Assistant).

Dashboards:

- Presence log (wie / wanneer / hoe vaak).
- Temperature / humidity trends (per kamer / per device).
- Light exposure patterns (dag / nacht / usage).
- Trigger frequency (per context mode: slaap / werk / relax / focus).

⸻

## 5. Aanpak voor manufacturing

### 5.1 Fasen voor rapid prototyping

**Fase 1 — Vormverkenning (industrial design + resin)**

- Resin master from HeyGears Reflex.
- Concrete en PU casting trials:
  - baseline GFRC mix
  - surface finish exploratie.

**Fase 2 — Functioneel prototype**

- Qi alignment jig (3D printed / resin).
- FR-1 PCB via ProtoEtch:
  - basis ESP32 + sensors + Hall.
- Mechanical fit van materialen:
  - passing iPhone
  - kabeldoorvoer
  - coil alignment in real-use scenario.

**Fase 3 — High-fidelity prototype (design validation test)**

- CNC wood shell + GFRC concrete core (productie-relevante materialen).
- Production-grade PCB (FR-4, professioneel gefabriceerd).
- Full sensor suite + firmware (inclusief OTA, MQTT, presence algorithms).

⸻

### 5.2 Small-batch manufacturing (production validation test)

- CNC milled molds voor GFRC / PU componenten (waar relevant).
- In-house kwaliteitscontrole:
  - fit
  - surface quality
  - coil alignment test met test-device.
- Assembly-standaardwerk (stap-voor-stap build-instructie).
- Burn-in test:
  - minimaal 12 uur onder Qi-charging load
  - logging van temperatuur en eventuele errors.
- Geregistreerde units:
  - unieke identificatie per unit
  - event logging enabled richting FabOps backend.

⸻

## 6. Validatiekader

### 6.1 Mechanisch

- Coil alignment tolerance: ±1.5 mm t.o.v. nominale MagSafe-positie.
- Housing thermal envelope:
  - onder 15W charge blijven relevante oppervlakken binnen veilige temperatuurgrenzen (te bepalen in test).

### 6.2 Elektronica

- Power budget, thermal drift, noise:
  - spanningsrails binnen spec
  - geen overmatige ripple.
- Presence detection reliability > 98%:
  - gemeten over representatieve testset (verschillende iPhones / cases).

### 6.3 Firmware

- Watchdog compliance:
  - geen lock-ups onder normale omstandigheden.
- OTA stability:
  - succesvolle update bij minimaal 95% van testcases in labomgeving.
- Latency event → automation < 150 ms:
  - van dock event tot Home Assistant / Node-RED actie.

### 6.4 Manufacturing

- Repeatability van concrete / PU interfaces:
  - dimensionele afwijking binnen gedefinieerde tolerantie (te loggen).
- Jig accuracy voor coil placement:
  - variatie binnen ±1 mm op X/Y.
- Smoothness van top surface finish:
  - visuele rating / standaard (SOP-definitie).

⸻

## 7. Risks & Mitigations

| Risk                               | Impact               | Mitigation                                         |
|------------------------------------|----------------------|---------------------------------------------------|
| Coil misalignment                  | Charging failure     | Alignment jig, calibration pins, QC fixture       |
| Sensor noise                       | Bad automation       | Oversampling, filtering, debouncing               |
| Thermische belasting (Qi + ESP32) | Verminderde laadprestatie | Venting channels, thermals testen / simulatie    |
| Concrete variability               | Fit issues           | Controlled GFRC mix, moisture cure SOP           |
| PU adhesion failures               | Delaminatie          | Surface prep, primer, test series per materiaal  |
| ESP32 WiFi provisioning friction  | Frustratie / returns | QR-based provisioning, fallback AP, UX-flow      |
| RF / EM interference coil ↔ Hall  | Foutieve reads       | Afstand / shielding, PCB-layout tuning           |

⸻

## 8. Kritieke prestatie-indicatoren voor Strom

### 8.1 Primary

- 3D → prototype iteration time < 72 uur.
- PCB iteration time < 24 uur (via ProtoEtch).
- Presence detection reliability > 98%.
- Manufacturing repeatability score > 90%  
  (op basis van gedefinieerde QC-checks).

### 8.2 Secondary

- Cost per unit (PVT target): €28–€42.
- Assembly time < 12 minuten per unit.
- Sensor accuracy:
  - ±3% RH
  - ±0.2 °C (binnen relevante range).

⸻

## 9. Volgende stap: operationeel uitrolplan

Proposed high-level rollout:

1. **Architecture freeze (Week 1)**  
   - Definieer elektrische, mechanische en ID-architectuur.
2. **Electronics v0.1 via ProtoEtch (Week 1–2)**  
   - Simpele ESP32 + Hall + één sensor.
3. **Industrial design master in resin (Week 2)**  
   - Form & ergonomie valideren.
4. **Hybrid materials feasibility trials (Week 2–3)**  
   - Beton + PU + hout combinaties.
5. **Firmware MVP: provisioning + presence (Week 3)**  
   - Basis WiFi + MQTT + presence events.
6. **Backend dashboards live (Week 3)**  
   - Presence / sensor telemetry zichtbaar in Grafana.
7. **High-fidelity design validation prototype (Week 4)**  
   - Full stack: industrial design + elektronica + firmware + backend + manufacturing-flow.

⸻

## 10. Discipline-workflows

### 10.1 Workflow industrial design

**Input:**

- Requirements uit dit manifest.
- Basis form-factor (iPhone models, orientatie, kabelpositie).

**Stappen:**

1. Parametric basis-volume in Fusion 360.
2. Integratie Qi-coil volume + kabelpad.
3. Integratie sensor zones, LED / display zones.
4. Export resin master en print.
5. Fit / feel / UX review.
6. Iteratie tot “ID freeze”.

**Output:**

- STEP / F3D files.
- Basis drawings (afmetingen, materiaalindicatie).
- Notities voor design for manufacturing (draft angles, undercuts, mold splits).

---

### 10.2 Workflow PCB / elektronica

**Input:**

- Functie-eisen (presence, sensing, WiFi, Qi-interface).

**Stappen:**

1. Schematic in Atopile.
2. Generate eerste layout → ProtoEtch-compatibel.
3. FR-1 prototype etsen, boren, assembleren.
4. Smoke test + basisfunctie (ESP32 boot, sensor read).
5. Fixes → KiCad-migratie → productie-layout.
6. Design for manufacturing and assembly-check (connectoren, testpads, jig-compatibiliteit).

**Output:**

- Atopile sources.
- KiCad project.
- Gerbers + BOM.
- Testverslag (functionele validatie).

---

### 10.3 Workflow firmware

**Input:**

- ESP32 board design.
- MQTT / HA / HomeKit requirements.

**Stappen:**

1. PlatformIO project scaffold.
2. Drivers: Hall, sensors, status-LED / display.
3. WiFi provisioning flow.
4. MQTT / HA integratie.
5. OTA implementatie.
6. Logging en basale metrics (uptime, reboots).
7. Bench tests + soak tests.

**Output:**

- Versiebeheerde firmware (git).
- Config templates (WiFi, MQTT).
- Release-notes per firmwareversie.

---

### 10.4 Workflow manufacturing

**Input:**

- ID freeze.
- Validated PCB.
- Material choices (beton, hout, PU).

**Stappen:**

1. Ontwerp mallen (CNC / 3D print / silicone).
2. Schrijven SOPs voor:
   - mixing / casting GFRC
   - PU casting
   - afwerking / post-processing.
3. QC-criteria vastleggen (dimensies, surface rating).
4. Pilot-run (bijv. 5–10 units).
5. Analyse van yield, doorlooptijden, failure modes.
6. Aanpassen van mallen, SOPs en tooling.

**Output:**

- SOPs (Markdown/PDF).
- QC-checklists.
- Productie-logging (tijd, scrap, issues).

⸻

## 11. Deliverables per fase

### P0 — Vormverkenning

- Resin master geprint.
- Basis iPhone fit-case test.
- Kabelpad + coil recess bevestigd.

### Design validation — High-fidelity prototype

- Full-stack werkende unit (ID + EE + FW + backend).
- Logfiles voor aanwezigheid + sensors >48h.
- Thermische metingen onder typical load.

### Production validation — Small batch

- Minimaal 5–10 units gebouwd met dezelfde workflow.
- Yield >90%.
- Gemeten assembly time <12 min.
- Telemetry operational op alle units.

⸻

## 12. Acceptatietestscripts (voorbeelden)

**Testcase elektronica 02: Hall + coil delta presence test**

- Procedure:
  1. Plaats iPhone met MagSafe-case in dock.
  2. Meet coil current baseline zonder device.
  3. Plaats device; log nieuwe coil current.
  4. Lees Hall-sensorstatus uit.
- Acceptance:
  - Δ current ≥ vooraf gedefinieerde drempel.
  - Hall-sensor = “present”.
  - MQTT-event binnen 150 ms op backend.

**Testcase firmware 01: WiFi-provisioning flow**

- Procedure:
  1. Reset device naar factory state.
  2. Doorloop provisioning flow (AP / QR).
  3. Check verbinding met MQTT-broker.
- Acceptance:
  - Provisioning < 2 minuten.
  - Persistent reconnect bij WiFi drop.

⸻

## 13. Eigenaarschap & RASCI (lean)

Voor nu: single-owner model.

| Domain            | Responsible | Accountable | Support             | Consulted              | Informed |
|-------------------|-------------|-------------|---------------------|------------------------|----------|
| Industrial design | Jochem      | Jochem      | –                   | –                      | –        |
| Elektronica       | Jochem      | Jochem      | ProtoEtch tooling   | datasheets / leveranciers | –        |
| Firmware          | Jochem      | Jochem      | FabOps backend      | Home Assistant / HomeKit documentatie | –        |
| Manufacturing     | Jochem      | Jochem      | CNC / casting tools | materiaalleveranciers  | –        |

⸻

## 14. Change Log

| Version | Date       | Description                                  |
|---------|------------|----------------------------------------------|
| 1.0     | 2025-11-22 | Initiële Strom operational spec |
