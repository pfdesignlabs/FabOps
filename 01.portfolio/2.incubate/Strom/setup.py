#---

## 2. Python-script om de omgeving aan te maken

#Dit script:

#- maakt een **Strom-map** met de voorgestelde subfolders;
#- schrijft het manifest naar `Strom/README.md` (je kunt de bestandsnaam makkelijk aanpassen);
#- is eenvoudig aan te passen naar jouw absolute pad (bijv. `/Users/pfdesignlabs/Documents/Projects/Strom`).

#```python
import os
from pathlib import Path

MANIFEST_MD = """# Project Strom — FabOps-Aligned Operational Manifest (v1.0)

Landscape iPhone Dock • HomeKit / Home Assistant integration • Environmental Automation Anchor

⸻

## 1. Strategic Intent

Strom is een capability-development traject disguised as a product.

Het primaire doel is het beheersen en op een hoger niveau brengen van:

- industrial design / design for manufacturing
- PCB design
- vacuum casting
- concrete casting
- mould making
- PlatformIO / embedded firmware
- design-to-manufacturing workflow binnen FabOps

Revenue is een bonus, niet de driver.  
Strom is de testcase voor de volledige FabOps pipeline.

⸻

## 2. Clear Problem Definition

### 2.1 Gebruikersfrictie

- Telefoons liggen overal en nergens.
- Smart home triggers zijn inconsistent of afhankelijk van soft-presence (WiFi, BT).
- Automatiseringen zijn generiek en niet context-aware (geen onderscheid tussen slapen / werken / relax).

### 2.2 Oplossingsrichting

Strom lost dit op door:

- **Presence certainty**  
  Device inserted = betrouwbare trigger voor automatisering.
- **Context switching**  
  Strom fungeert als fysieke context-anchor voor slapen / werken / relax / focus.
- **Environmental sensing**  
  Metingen van temperatuur, luchtvochtigheid en lichtintensiteit.
- **Physical anchor**  
  Het dock optimaliseert de fysieke omgeving zodra de iPhone wordt geplaatst.

⸻

## 3. Scope of Project Strom

### 3.1 Hard Scope

- Landscape iPhone dock
- Qi charging (Apple-compatible coil / module)
- Dual-sensor presence detection:
  - Hall-sensor (mechanische presence)
  - Coil current sensing (charge-state / presence-validatie)
- ESP32-based logic
- Licht / temperatuur / humidity sensors (I²C sensorstack)
- HomeKit + MQTT + Home Assistant support
- Optional hidden display for status indicators (bijv. klein segment- of dot-matrixdisplay achter PU / plexi)

### 3.2 Soft Scope (optional / aspirational)

- Detachable service bay (elektronica-‘cartridge’)
- CNC hybrid materials (wood / beton / PU)
- Touchless capacitive input (mode switching, mute, etc.)
- Ambient LED visual layer (subtiele status / mood)

⸻

## 4. Product Architecture — FabOps Structure

This section maps each subsystem directly to a FabOps capability.

⸻

### 4.1 Industrial Design (Capability: ID-C3)

**Outcome:** manufacturable, repeatable, Dieter-Rams inspired geometry.

Deliverables:

- Fusion 360 parametric model van de Strom-behuizing.
- Landscape wedge design, met verzonken recess voor iPhone.
- Hybrid material aesthetic:
  - beton body
  - houten accent / shell
  - matte PU voor interface / demping / detaillering
- Hidden LED layer or segmented one-line display (niet zichtbaar wanneer uit).
- Tolerance stack gevalideerd via resin master prints (HeyGears Reflex).
- Alignment markers voor fiberlaser:
  - branding
  - sensor window markers
  - alignment voor mogelijke text / iconografie.

⸻

### 4.2 Mechanical Engineering (Capability: ME-C3)

Deliverables:

- Qi coil alignment fixture (jig voor consistente coil-positie t.o.v. iPhone).
- Multimaterial assembly:
  - wood shell
  - concrete / GFRC core
  - PU gasket / interface parts
- Ventilatie / airflow voor coil thermals.
- Cable routing + strain relief (USB-C naar binnenzijde).
- Mounting bosses voor PCB(s).
- Draft voor small-batch mold tooling:
  - silicone → PU series
  - CNC-gefreesde mallen voor GFRC / PU op termijn.

Critical risks:

- Coil-to-device misalignment → charging faalt of is inconsistent.
- Concrete warping / shrinkage variance → slechte fit, spanningen in assembly.
- PU adhesion op beton / wood interfaces → delaminatie op termijn.

⸻

### 4.3 Electronics (Capability: EE-C2 → C4)

Board (Atopile → KiCad validated):

- ESP32-WROOM module.
- Qi coil driver input sensing (current sensing / status lines).
- Hall sensor voor mechanische presence detectie.
- Temp / humidity / light sensors via I²C (bijv. SHT4x + OPT3001 of equivalent).
- USB-C input (5V vast; PD niet vereist in eerste iteratie).
- Power path:
  - Qi module supply
  - logic-supply met eigen LDO / buck
- Optional room-facing PCB voor LED / display + eventuele touch / capacitive input.

FabOps tie-in:

- ProtoEtch wordt gebruikt voor vroege PCB-iteraties (FR-1, in-house).
- Layouts worden na functionele validatie gemigreerd naar KiCad voor productie-grade boards.

⸻

### 4.4 Firmware (Capability: FW-C2 → C4)

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
  - optioneel: HomeKit accessory server integratie.
- OTA-updates:
  - basale OTA pipeline via HTTP / MQTT.
- Local diagnostic mode:
  - LED feedback / display codes voor provisioning, errors, testmodi.

⸻

### 4.5 Backend Integration (Capability: FabOps-C3)

Pipeline:

> Phone docked → ESP32 event → MQTT broker → Telegraf → InfluxDB → Automation (Node-RED / Home Assistant).

Dashboards:

- Presence log (wie / wanneer / hoe vaak).
- Temperature / humidity trends (per kamer / per Strom).
- Light exposure patterns (dag / nacht / usage).
- Trigger frequency (per context mode: slaap / werk / relax / focus).

⸻

## 5. Manufacturing Approach

### 5.1 Rapid Prototyping Phases

**Phase 1 — Form exploration (ID + resin)**

- Resin master from HeyGears Reflex.
- Concrete en PU casting trials:
  - baseline GFRC mix
  - basic shrink/warp metingen
  - surface finish exploratie.

**Phase 2 — Functional prototype**

- Qi alignment jig (3D printed / resin).
- FR-1 PCB via ProtoEtch:
  - basis ESP32 + sensors + Hall.
- Mechanical fit van hybrid materials:
  - passing iPhone
  - kabeldoorvoer
  - coil alignment in real-use scenario.

**Phase 3 — High-fidelity prototype (DVT)**

- CNC wood shell + GFRC concrete core (productie-relevante materialen).
- Production-grade PCB (FR-4, professioneel gefabriceerd).
- Full sensor suite + firmware (inclusief OTA, MQTT, presence algorithms).

⸻

### 5.2 Small-Batch Manufacturing (PVT)

- CNC milled molds voor GFRC / PU componenten (waar relevant).
- In-house QC:
  - fit
  - surface quality
  - coil alignment test met test-device.
- Assembly SOP (stap-voor-stap build-instructie).
- Burn-in test:
  - minimaal 12 uur onder Qi-charging load
  - logging van temperatuur en eventuele errors.
- Serialised units:
  - unieke ID per Strom
  - event logging enabled richting FabOps backend.

⸻

## 6. Validation Framework

### 6.1 Mechanical

- Coil alignment tolerance: ±1.5 mm t.o.v. nominale MagSafe-positie.
- Housing thermal envelope:
  - onder 15W charge blijven relevante oppervlakken binnen veilige temperatuurgrenzen (te bepalen in test).

### 6.2 Electronics

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
| Sensor noise                       | Bad automation       | Oversampling, filtering, debouncing              |
| Thermal load (Qi + ESP32)         | Degraded charging    | Venting channels, thermals testen / simulatie    |
| Concrete variability               | Fit issues           | Controlled GFRC mix, moisture cure SOP           |
| PU adhesion failures               | Delaminatie          | Surface prep, primer, test series per materiaal  |
| ESP32 WiFi provisioning friction  | Frustratie / returns | QR-based provisioning, fallback AP, UX-flow      |
| RF / EM interference coil ↔ Hall  | Foutieve reads       | Afstand / shielding, PCB-layout tuning           |

⸻

## 8. KPIs for Strom

### 8.1 Primary

- 3D → prototype iteration time < 72 uur.
- PCB iteration time < 24 uur (via ProtoEtch).
- Presence detection reliability > 98%.
- Manufacturing repeatability score > 90% (op basis van gedefinieerde QC-checks).

### 8.2 Secondary

- Cost per unit (PVT target): €28–€42.
- Assembly time < 12 minuten per unit.
- Sensor accuracy:
  - ±3% RH
  - ±0.2 °C (binnen relevante range).

⸻

## 9. Required Capabilities to Mature

Strom is een capability accelerator. Deze trajecten moeten tijdens het project groeien:

- PCB Prototyping (ProtoEtch → C4).
- GFRC small-batch tooling (C1 → C3).
- Qi integration competency (C0 → C2).
- Hybrid material manufacturing (C1 → C3).
- Embedded sensing frameworks (C2 → C4).
- Automation backend maturity (FabOps C3 → C5).

⸻

## 10. Next Step: Operational Rollout Plan

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
7. **High-fidelity DVT prototype (Week 4)**
   - Full stack: ID + EE + FW + backend + manufacturing flow.

⸻

## 11. Discipline-Level Workflows

### 11.1 Industrial Design Workflow (ID-C3)

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
- Notities voor design for manufacturing (draft angles, ondercuts, mold splits).

---

### 11.2 PCB / Electronics Workflow (EE-C2 → C4)

**Input:**

- Functie-eisen (presence, sensing, WiFi, Qi-interface).

**Stappen:**

1. Schematic in Atopile.
2. Generate eerste layout → ProtoEtch-compatibel.
3. FR-1 prototype etsen, boren, assembleren.
4. Smoke test + basisfunctie (ESP32 boot, sensor read).
5. Fixes → Kicad migratie → productie-layout.
6. Design for manufacturing and assembly-check (connectoren, testpads, jig-compatibiliteit).

**Output:**

- Atopile sources.
- KiCad project.
- Gerbers + BOM.
- Testverslag (functionele validatie).

---

### 11.3 Firmware Workflow (FW-C2 → C4)

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

### 11.4 Manufacturing Workflow (MFG-C3)

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

- SOPs (PDF/Markdown).
- QC-checklists.
- Productie-logging (tijd, scrap, issues).

⸻

## 12. Deliverables per Phase

### P0 — Form exploration

- Resin master geprint.
- Basis iPhone fit-case test.
- Kabelpad + coil recess bevestigd.

### DVT — High-fidelity prototype

- Full-stack werkende unit (ID + EE + FW + backend).
- Logfiles voor aanwezigheid + sensors >48h.
- Thermische metingen onder typical load.

### PVT — Small batch

- Minimaal 5–10 units gebouwd met dezelfde workflow.
- Yield >90%.
- Gemeten assembly time <12 min.
- Telemetry operational op alle units.

⸻

## 13. Acceptance Test Scripts (Examples)

**TC-EE-02: Hall + Coil Delta Presence Test**

- Procedure:
  1. Plaats iPhone met MagSafe-case in dock.
  2. Meet coil current baseline zonder device.
  3. Plaats device; log nieuwe coil current.
  4. Lees Hall-sensorstatus uit.
- Acceptance:
  - Δ current ≥ vooraf gedefinieerde drempel.
  - Hall-sensor = “present”.
  - MQTT-event binnen 150 ms op backend.

**TC-FW-01: WiFi Provisioning Flow**

- Procedure:
  1. Reset device naar factory state.
  2. Doorloop provisioning flow (AP / QR).
  3. Check verbinding met MQTT-broker.
- Acceptance:
  - Provisioning < 2 minuten.
  - Persistent reconnect bij WiFi drop.

⸻

## 14. Ownership & RASCI (Lean)

Voor nu: single-owner model.

| Domain          | Responsible | Accountable | Support           | Consulted              | Informed |
|-----------------|-------------|-------------|-------------------|------------------------|----------|
| Industrial Design | Jochem    | Jochem      | –                 | –                      | –        |
| Electronics       | Jochem    | Jochem      | ProtoEtch tooling | datasheets / vendors   | –        |
| Firmware          | Jochem    | Jochem      | FabOps backend    | HA / HomeKit docs      | –        |
| Manufacturing     | Jochem    | Jochem      | CNC / casting tools | materiaalleveranciers | –        |

⸻

## 15. Proposed Repository & Folder Structure

Suggested structure (Strom repo):

```text
/Strom
  /00.tracking           (epics, stories, tasks, sprints)
  /01.build_log          (korte status en logverwijzingen)
  /02.requirements
  /03.architecture
  /04.cad
  /05.electronics
  /06.firmware
  /07.manufacturing
  /08.validation
  README.md              (kan deze Operational Manifest zijn)
"""

# TIP:
# Vervang het bovenste MANIFEST_MD-blok door de volledige Markdown uit sectie 1
# zodat je één bron-of-truth hebt.


def create_strom_environment(base_dir: str):
    """
    Maakt de Strom projectstructuur aan en schrijft het manifest naar README.md.
    base_dir: pad waar de 'Strom' map moet komen, bijvoorbeeld:
              '/Users/pfdesignlabs/Documents/Projects/Strom'
    """
    base_path = Path(base_dir).expanduser().resolve()
    strom_root = base_path / "Strom"

    # Submappen volgens voorstel
    subdirs = [
        "00.tracking",
        "01.build_log",
        "02.requirements",
        "03.architecture",
        "04.cad",
        "05.electronics",
        "06.firmware",
        "07.manufacturing",
        "08.validation",
    ]

    print(f"Creating Strom project structure under: {strom_root}")

    # Maak root + subfolders
    strom_root.mkdir(parents=True, exist_ok=True)
    for sub in subdirs:
        p = strom_root / sub
        p.mkdir(parents=True, exist_ok=True)
        print(f"  - created: {p}")

    # Schrijf README.md met manifest
    readme_path = strom_root / "README.md"
    if "..." in MANIFEST_MD:
        print(
            "WARNING: MANIFEST_MD is nog niet volledig. "
            "Plak de volledige Markdown-tekst in de string."
        )
    readme_path.write_text(MANIFEST_MD, encoding="utf-8")
    print(f"\nWrote manifest to: {readme_path}")

    # Optioneel: simpele .gitignore
    gitignore_path = strom_root / ".gitignore"
    if not gitignore_path.exists():
        gitignore_content = """# Python
__pycache__/
*.pyc

# OS
.DS_Store

# Build artifacts
/build/
dist/
*.log
"""
        gitignore_path.write_text(gitignore_content, encoding="utf-8")
        print(f"Created .gitignore at: {gitignore_path}")


if __name__ == "__main__":
    # PAS DIT PAD AAN NAAR JOUW OMGEVING
    target_base = "/Users/pfdesignlabs/Documents/Projects/Strom"
    create_strom_environment(target_base)
