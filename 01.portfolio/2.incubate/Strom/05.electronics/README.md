# Strom — Electronics Specification (v0.1)

## 1. Overview

Dit document definieert de elektronische architectuur van Strom:

- ESP32-based main board.
- Qi-module interfacing (power + status).
- Dual presence-detectie (Hall + coil current).
- Sensorstack (temp / RH / light).
- User interface (status-LED, state override button, optioneel display).
- Power-in via USB-C (5V).

---

## 2. System Block Diagram (Textual)

- **Power In**
  - USB-C 5V input
  - ESD bescherming
  - eventueel reverse-polarity / surge bescherming

- **Power Distribution**
  - 5V → Qi-module
  - 5V → buck / LDO → 3V3 rail voor ESP32 + sensors

- **Main MCU**
  - ESP32-WROOM met:
    - WiFi
    - GPIO voor Hall, button, LED, sensors, optional UI

- **Sensors**
  - Temp/RH: I²C sensor
  - Light: I²C of analoge sensor

- **Presence Detectie**
  - Hall-sensor nabij iPhone-positie
  - Qi-coil current sense / status line (afhankelijk van module)

- **Interface naar Backend**
  - WiFi → MQTT / HA / HomeKit (via firmware).

---

## 3. Key Components (Draft)

> Exacte typenummers worden later definitief, dit is een eerste ontwerpset.

- MCU: ESP32-WROOM-32E (of recente variant met voldoende flash/RAM).
- Power:
  - USB-C receptacle (5V only)
  - Buck converter 5V → 3V3 (bijv. MP1584-klasse of compacte synchronous buck)
  - LDO voor ruisarme supplies indien nodig (sensors).
- Qi:
  - Prefab Qi-transmitter module (Apple-compatible, 5V input).
  - Current sense:
    - shunt + INA-style current sense, of status pins van module.
- Hall-sensor:
  - Omnipolar Hall switch, low-power.
- Sensors:
  - Temp/RH: Sensirion SHT4x of equivalent.
  - Light: OPT3001 of equivalent, of basic LDR + ADC-resistor divider.
- UI:
  - 1× RGB- of single-color-LED (status).
  - 1× tact switch (state override / factory reset).
  - Optioneel: I²C of SPI-display (bijv. small segment/mono OLED).

---

## 4. Interfaces & Pinning (Concept)

### 4.1 ESP32 IO Allocation (indicatief)

- I²C (SDA/SCL) → temp/RH + light + optional display.
- GPIO_X → Hall-sensor input.
- GPIO_Y → state override button (met debouncing in FW).
- GPIO_Z → status-LED (PWM-capable pin bij RGB).
- UART / USB-bridge → debug en flashing.
- extra pins gereserveerd voor future expansion.

Details worden vastgelegd in Atopile source (`strom_mainboard.ato`).

---

## 5. Design Rules

- 4-layer preferred voor productieversie; 2-layer toegestaan voor FR-1 ProtoEtch versie.
- DRC:
  - clearance/width afgestemd op 5V rails en stroom voor Qi-module.
- Grounding:
  - solide ground plane.
  - zorgvuldige routing rond coil / Hall-sensor (minimale interferentie).
- Testability:
  - testpads voor:
    - 5V
    - 3V3
    - reset
    - boot
    - I²C bus
  - zodat debugging met probes eenvoudig is.

---

## 6. ProtoEtch Flow (v0.x)

1. Atopile schematic + eerste layout.
2. Export naar ProtoEtch pattern:
   - enkelzijdig of dubbelzijdig FR-1 board.
3. Etsen + boren + hand-assemble.
4. Basis smoke-test:
   - 5V → 3V3 ok
   - ESP32 boot
   - sensor-identificatie via I²C
5. Logging van issues:
   - power issues
   - footprint- mismatches
   - layout-problemen


---

## 7. Acceptance Criteria (Electronics v1.0)

- Board kan op 5V gevoed worden en stabiel 3V3 leveren.
- ESP32 kan geprogrammeerd worden via standaard flashing flow (PlatformIO).
- Hall-sensor en current sense leveren consistente signalen aan firmware.
- Sensoren leveren plausibele waarden in een simpele testfirmware.
- USB-C connector is mechanisch stabiel en degelijk verankerd.

---

## 8. To-Do (EE Backlog)

- Definitieve componentselectie (typecodes, leveranciers).
- Atopile module schrijven voor mainboard.
- Eerste ProtoEtch layout genereren.
- Testfixture bedenken voor coil alignment + current sense.