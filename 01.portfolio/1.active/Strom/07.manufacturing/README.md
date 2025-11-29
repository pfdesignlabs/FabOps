# Strom — Manufacturing Specification (v0.1)

Dit document definieert hoe Strom fysiek wordt gemaakt:
materialen, processen, tooling, QC en small-batch productie.

Doel: reproduceerbaar, schaalbaar, zonder verrassingen.

---

## 1. Manufacturing Philosophy

- **Low-volume, high-quality**  
- **FabOps-driven**: elke stap is meetbaar en gedocumenteerd  
- **Modulaire workflow**: GFRC + hout + PU in losse streams  
- **Small-batch ready**: 5–20 units per run  

---

## 2. Manufacturing Stages

### Stage 1 — Resin Master (ID Validation)

- Print via HeyGears Reflex  
- Light sand + prime  
- Test:
  - iPhone fit  
  - coil alignment  
  - thermische ruimte  

### Stage 2 — Concrete / GFRC Casting

- Materials:
  - GFRC mix  
  - glasvezel 2–4 mm  
  - water reducer  
- Silicone molds:
  - Shore 20–30A  
  - 1–2° draft  
  - venting gates waar relevant  
- Process:
  1. mold prep  
  2. GFRC slurry  
  3. face coat  
  4. back coat  
  5. curing 24–48 uur  
- QC:
  - shrink check  
  - surface rating  
  - dimensional check  

### Stage 3 — Wood Components (CNC)

- Material: walnut / ash / oak  
- CNC parameters:
  - 6–8 mm flat endmill  
  - finishing pass met 3 mm  
- Finishing:
  - matte olie of PU  

### Stage 4 — PU Backplate

- Silicone mold (Shore 10–20A)  
- PU Shore 80–90A  
- Purpose:
  - hidden LED diffusion  
  - mounting platform  
- QC:
  - warping <0.3 mm  
  - consistent matte surface  

---

## 3. Electronics Assembly

- Mainboard: FR-4  
- Soldering:
  - hot-air or reflow  
- Test via:
  - USB power  
  - boot test  
  - sensor identification  
  - Hall-sensor trigger test  
  - coil current response  
- Burn-in:
  - 12h continuous charge test  

---

## 4. Mechanical Integration

Assembly sequence:

1. Concrete body clean-up  
2. Wood panel insert + adhesive  
3. Coil mount + fixation  
4. PCB installation  
5. Cable routing  
6. PU backplate mounting  
7. LED/diffusor alignment  
8. Final torque checks  

---

## 5. Quality Control

### Dimensional Checks

- iPhone recess ±0.3 mm  
- coil center alignment ±1.5 mm  
- PCB boss alignment ±0.2 mm  

### Surface Checks

- Beton:
  - pinholes < grade-2  
  - uniforme matte afwerking  
- Hout:
  - glad, geen tear-out  
- PU:
  - diffuse, geen glansplekken  

### Functional Checks

- Charging: must charge iPhone > 8% per 15 min  
- Sensor readings plausible  
- WiFi join < 10s  
- Presence event < 150ms  

---

## 6. Documentation Artifacts

Per batch ontstaat:

- QC checklist (PDF/MD)  
- Material log  
- Test logs  
- Serial number list  
- Assembly timing stats  

---

## 7. Open Questions

- Batch size preference  
- Final finishing options  
- Concrete sealer selection  