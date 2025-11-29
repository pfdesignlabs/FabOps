# Strom — Validation Plan (v0.1)

Dit document definieert alle tests, protocollen en criteria die bepalen
wanneer Strom functioneel, mechanisch en firmware-matig "geslaagd" is.

Dit valideert het volledige product — niet alleen een prototype.

---

## 1. Validation Philosophy

- **Evidence-based**: elke claim wordt gemeten  
- **Reproduceerbaar**: testen kunnen door iemand anders worden herhaald  
- **End-to-end**: van presence-triggers tot Home Assistant automations  
- **FabOps-native**: logging → dashboards → analysis  

---

## 2. Validation Scope

Covered:

- Mechanical fit & alignment  
- Electronics stability  
- Firmware stability & OTA  
- Connectivity  
- Charging performance  
- Sensor accuracy  
- Backend event integrity  
- Environmental robustness  

---

## 3. Mechanical Validation

### Tests

1. **Coil Alignment Test**
   - meet coil → phone offset in X/Y/Z  
   - target: ±1.5 mm  

2. **Drop-in Fit Test**
   - iPhone moet met één hand geplaatst kunnen worden  
   - geen scherpe randen  

3. **Warp & Shrink Test (GFRC + PU)**
   - meet dimensional drift over 48 uur curing  

4. **Cable Strain Test**
   - USB-C connector moet 3× plug cycles zonder verschuiving doorstaan  

---

## 4. Electronics Validation

### Tests

1. **Smoke Test**
   - power rails controleren  
   - ESP32 boot  

2. **Hall Sensor Test**
   - magnet trigger op 5–10 mm afstand  

3. **Coil Current Delta Test**
   - meten van loaded vs unloaded current profile  

4. **Sensor Bus Test**
   - I²C detectie van alle sensors  

5. **Thermal Test**
   - 15W Qi-charge 30 minuten  
   - max extern oppervlak onder veiligheidslimiet  

---

## 5. Firmware Validation

### Functional Tests

1. **WiFi Provisioning**
   - AP-mode join  
   - credential persistence  

2. **MQTT Event Timing**
   - dock → MQTT <150 ms  

3. **Sensor Payload Validation**
   - plausibility + jitter tracking  

4. **Watchdog**
   - geforceerde hang → automatische reboot  

5. **OTA Update**
   - firmware upgrade → reboot → restored state  

---

## 6. Backend Validation

1. **MQTT Integrity Test**
   - subscribe op alle topics  
   - geen missende events  

2. **Telegraf → Influx ingest**
   - meet 1 uur telemetry:  
     - no gaps  
     - correct timestamps  

3. **Grafana Dashboard Review**
   - presence spikes  
   - sensor drift  
   - uptime  

4. **Home Assistant Automation Test**
   - iPhone plaatsen → lights off → thermostat adjust  

---

## 7. Extended Tests

- **48h soak test**
- **WiFi stress test** (router reboot)  
- **sleep automation test** elke nacht 5 dagen  

---

## 8. Acceptance Thresholds

- Presence detection >98%
- Charging: +8% per 15 min minimum  
- Sensor timestamps: geen drift >5s over 24h  
- No firmware crashes >48h  
- Backend ingest 100% event integrity  

---

## 9. Validation Artifacts

- Logs (serial + MQTT + InfluxDB exports)  
- Video bewijs van kritische tests  
- Screenshot set van dashboards  
- Batch validation report (PDF)

---

## 10. Open Items

- validating display behaviour  
- UX scoring voor nacht-gebruik  
