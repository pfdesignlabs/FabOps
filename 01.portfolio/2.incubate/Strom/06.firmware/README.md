# Strom — Firmware Specification (v0.1)

Firmware draait op de ESP32-WROOM en vormt de “intelligence layer” van Strom.
Dit document specificeert modules, architectuur, interfaces en testcriteria.

---

## 1. Firmware Architecture (v0.1)

### Modules:

1. **Core System**
   - boot sequence  
   - hardware init  
   - watchdog handler  
   - configuration loader (JSON / NVS)

2. **WiFi Provisioning**
   - fallback AP-mode  
   - QR-based provisioning (phase 2)  
   - persistent credentials  

3. **Presence Engine**
   - Hall-sensor polling  
   - coil current sensing / module pin-status  
   - debouncing  
   - edge detection  
   - event publishing  

4. **Sensor Engine**
   - I²C bus manager  
   - SHT4x drivers  
   - light sensor drivers  
   - oversampling / filtering  
   - payload creation  

5. **MQTT Layer**
   - broker connect  
   - heartbeat (online/offline)  
   - publish presence events  
   - publish sensor frames  
   - LWT (last will/testament)

6. **HomeKit Integration (phase 2–3)**
   - basic HAP server  
   - mirror MQTT state → HomeKit accessories  

7. **OTA Update Handler**
   - HTTP-based OTA  
   - fallback partition  
   - version check  

8. **UI Layer**
   - status LED PWM  
   - override button (short/long press)  
   - optional display driver  

---

## 2. Data Model

### MQTT Topics

```
strom/<device_id>/presence
strom/<device_id>/sensors
strom/<device_id>/state
strom/<device_id>/debug
strom/<device_id>/ota
```

### Sensor Payload (JSON)

```json
{
  "temperature_c": 21.8,
  "humidity_rh": 49.3,
  "light_lux": 12.4,
  "timestamp": 1714503423
}
```

### Presence Payload

```json
{
  "present": true,
  "via": "hall + coil",
  "ts": 1714503419
}
```

---

## 3. Boot Sequence

1. Load config from NVS  
2. Start WiFi
   - if fail → AP-mode provisioning  
3. Initialize sensors  
4. Initialize MQTT  
5. Start presence engine  
6. Enter main loop  
7. Periodic sensor publish  

---

## 4. Event Timing Requirements

- Presence event:  
  `dock → MQTT publish < 150ms`

- Sensor update:  
  default 30–60s

- WiFi reconnect:  
  retry every 5s, exponential fallback

---

## 5. Button UX

### Short press  
→ toggle override state   
(mute automation voor X minuten)

### Long press (>6s)  
→ factory reset  
→ ga naar provisioning mode  

---

## 6. OTA Strategy

- Firmware hosted on internal endpoint (Nginx, HA add-on, of eenvoudige Python server).  
- Device checkt:
  - version.json
  - download URL  
- OTA moet:
  - partition-aware zijn  
  - fallback partition bevatten  

---

## 7. Acceptance Criteria

- Strom verbindt binnen 8 sec met WiFi na boot.
- MQTT-event komt binnen 150 ms aan na plaatsing device.
- Sensor payloads worden minimaal 95% betrouwbaar verzonden.
- Device blijft 48 uur operationeel zonder reboot.
- OTA update slaagt bij minstens 95% van test attempts.

---

## 8. Open Issues

- homekit-hap library integratiekeuze  
- LED-status patterns → defineren  
