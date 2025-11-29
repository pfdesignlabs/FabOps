# Strom — Requirements & Context (v0.1)

## 1. Product Context

Strom is een landscape iPhone-dock met geïntegreerde ESP32-controller, Qi-charging en sensorstack.
Het primaire doel is tweeledig:

1. Een fijne, stijlvolle manier van opladen.
2. Een betrouwbare, fysieke presence-trigger voor home automation (met name slapen / bedtime routine).

Capability-focus:
- CAD & DFM
- Electronics (breadboard → Atopile → KiCad → ProtoEtch)
- Manufacturing (GFRC, PU, moulds)
- Firmware (PlatformIO, ESP32)
- Content creation rond het traject

---

## 2. Target User & Use Cases

### 2.1 Target user

- Gebruiker met Home Assistant / HomeKit (of beide).
- iPhone met MagSafe (recente generaties).
- Thuisomgeving met minimaal 1 “slapen” / bed routine automation.

### 2.2 Primary use cases

1. **Bedtime dock**
   - User legt iPhone in Strom op nachtkastje.
   - Strom triggert “slaap”-profiel:
     - lichten dimmen / uit
     - thermostaat omlaag
     - white-noise / ventilator aan
     - notificaties beperken (via HA / Apple Focus).

2. **Environmental sensing**
   - Strom logt temperatuur, luchtvochtigheid en licht in de slaapkamer.
   - Data zichtbaar in Grafana / Home Assistant dashboards.
   - Gebruik in rules: te warm / te droog / te veel licht.

3. **Presence certainty**
   - Strom rapporteert aan backend dat de telefoon fysiek geplaatst is.
   - Automations gebruiken dit als harde presence-indicator (naast WiFi/BT).

---

## 3. Functional Requirements

### 3.1 Charging & Presence

- Strom moet een iPhone met MagSafe-compatible positie kunnen opladen.
- Strom moet kunnen detecteren:
  - of er een device fysiek geplaatst is (Hall-sensor).
  - of er daadwerkelijk geladen wordt (coil current sensing).
- Presence event wordt binnen 150 ms na plaatsen van de iPhone gepubliceerd naar MQTT / HA.

### 3.2 Sensing

- Strom meet:
  - Temperatuur (°C)
  - Relatieve luchtvochtigheid (%)
  - Lichtintensiteit (lux / relatieve waarde)

- Sampling:
  - default elke 30–60 seconden (instelbaar in firmware / config).
- Data wordt verzonden via MQTT naar FabOps backend en / of HA.

### 3.3 Integraties

- **MQTT**
  - Minimaal 1 topic voor presence-events.
  - Minimaal 1 topic voor sensor payloads.
  - Config van broker en topics via configbestand of provisioning.

- **Home Assistant**
  - Strom exposeert zich als:
    - binary_sensor: presence
    - sensor: temperature, humidity, light
    - optional: switch / input_boolean voor override-state.

- **HomeKit**
  - Presence en basis-sensors beschikbaar als HomeKit-accessory (later uit te bouwen).

### 3.4 Local UX / Interface

- Minimaal:
  - status-LED voor:
    - provisioning mode
    - normal operation
    - error / fault state.
- Optioneel:
  - klein hidden display of extra LEDs voor sensor- of mode-indicatie.
- State override button:
  - korte druk: mute / override automation.
  - lange druk: factory reset / provisioning mode (details in FW-spec).

---

## 4. Non-Functional Requirements

### 4.1 Form factor & ID

- Landscape orientation.
- iPhone ligt stabiel en niet “wiebelend”.
- Esthetiek: beton body, houtaccent, matte PU backplate.
- Kabel discreet weggewerkt (achter- of onderzijde).

### 4.2 Performance & betrouwbaarheid

- Presence-detectie:
  - >98% juiste detecties over representatieve testset.
- Uptime:
  - device moet 24/7 kunnen draaien zonder ingestelde reboots.
- Thermisch:
  - geen onveilig warme zones aan buitenzijde onder normale belasting.

### 4.3 Safety

- Geen blootliggende netspannings-onderdelen.
- 5V-voeding via externe USB-C adapter.
- Basis ESD/EMI hygiene in PCB-layout.

---

## 5. Technical Constraints

- Controller: ESP32-WROOM.
- Firmware: PlatformIO (C/C++).
- Qi: gebruik van bestaande Apple-compatible module, geen zelfgebouwde high-voltage driver.
- Prototyping:
  - PCB proto’s via ProtoEtch (FR-1) voor v0.x
  - productie via externe fabrikant (FR-4) vanaf DVT.

---

## 6. Success Criteria (v1.0)

- Strom kan een iPhone betrouwbaar opladen in de beoogde oriëntatie.
- Strom levert consistente presence-events aan HA / MQTT bij plaatsen/weghalen.
- Strom stuurt bruikbare sensor-data (temp/RH/light) naar backend.
- Minstens 1 end-to-end “slaap”-automation draait stabiel:
  - iPhone plaatsen → automation chain → lichten/klimaat aanpassen.
- Minimaal 5 units (PVT) kunnen met dezelfde workflow worden gebouwd, met >90% yield.

---

## 7. Open Questions / To Decide

- Precieze vorm-factors voor iPhones (welke generaties expliciet ondersteunen).
