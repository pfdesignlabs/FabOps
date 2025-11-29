# Strom — Industrial Design Specification (v0.1)

## 1. Purpose

Dit document definieert de industriële vormgeving, materiaalkeuzes en DFM-richtlijnen voor Strom.
ID vormt de basis van de totale productarchitectuur en moet:

- esthetisch coherent zijn (Dieter Rams, reductie, rustige geometrie)
- mechanisch reproduceerbaar zijn in kleine series
- compatibel zijn met beton, hout, en PU-fabricage
- integreren met electronics + firmware constraints

---

## 2. Design Principles

1. **Reduction**  
   Vorm volgt functie; minimalisme zonder complexiteit.

2. **Balance**  
   Landscape-oriëntatie met visueel laag zwaartepunt.

3. **Material authenticity**  
   Materialen blijven herkenbaar: beton voelt als beton, hout als hout.

4. **Hidden technology**  
   Sensors, LEDs en display zijn onzichtbaar wanneer ze uit staan.

5. **Manufacturing realism**  
   Elke curve, hoek en wanddikte moet maakbaar zijn in:
   - resin prototypes  
   - GFRC beton  
   - PU casting  
   - CNC hout

---

## 3. Form Factor

### 3.1 Orientation & Overall Shape

- Landscape wedge form
- Low-profile front, hogere rug
- iPhone ligt in een verzonken sleuf (0.5–1 mm clearance)
- Hoekconfiguratie geoptimaliseerd voor:
  - leesbaarheid in liggende oriëntatie
  - opladen met MagSafe-compatible coil
  - stabiel neerleggen in het donker

### 3.2 Dimensions (initial targets)

> Definitieve maten volgen na eerste fit-prints.

- Width: 160–190 mm  
- Depth: 70–90 mm  
- Height (rear): 40–55 mm  
- Angle: 20–28° landscape viewing angle  
- Channel width (iPhone): 78–80 mm (targeting modern iPhones)

---

## 4. Material Stackup

### 4.1 Concrete (GFRC)

- Functie: body, massa, stabiliteit, premium tactility  
- Specificaties:
  - GFRC mix  
  - 2–4 mm glasvezel  
- kleine shrink-range (<0.5 mm)  
  - oppervlak: licht gezandstraald / mat  
- Min. wanddikte: 3.0 mm  
- Draft angles: 1–2° voor demolding

### 4.2 Hout (accent)

- Functie: front lip of achterpaneel  
- Soorten: walnoot, essen, eiken (consistent grain)  
- Afwerking: matte olie of PU-coating  
- Tolerantie: ±0.2 mm (CNC)

### 4.3 PU Backplate

- Functie: interne mounting interface + diffusor  
- Shore hardness: 80–90A  
- Eigenschappen:
  - matte afwerking
  - lichtdiffusie voor hidden LED layer
  - dempt interne resonantie  
- Wanddikte: 1.5–2.5 mm

---

## 5. ID → Mechanical Handoff

### 5.1 Critical Interfaces

- **Qi-coil dock recess**  
  - coil center aligned op iPhone center (±1.5 mm)
  - coil cavity: 0.2–0.4 mm radial clearance

- **Sensor windows**  
  - verborgen achter PU-backplate  
  - min. 1 mm lichtdoorlaat

- **Cable path**  
  - 5 mm minimum diameter  
  - klem / strain relief inbegrepen

### 5.2 Alignment Features

- Pins voor:
  - PCB bevestiging
  - coil alignment jig  
- Flats / bosses voor consistent materiaalcontact

---

## 6. Resin Master Requirements (Prototype Phase)

- Print via HeyGears Reflex  
- Layer height: 0.05–0.1 mm  
- Toleranties testen:
  - fit of iPhone  
  - coil cavity alignment  
  - sensor zones  

---

## 7. DFM Guidelines

- Geen scherpe inwendige hoeken → fillets van 0.7–2.0 mm  
- Draft angles in mal-georiënteerde vlakken  
- Betonnen delen zoveel mogelijk uniforme wanddikte  
- Houten delen genereren via CNC met:
  - 6–8 mm flat endmill  
  - 1–3 mm fillets binnenin  
- PU backplate gegoten in silicone mal (Shore 10–20A)

---

## 8. Open Questions

- Definitieve zichtbare houtpositie: front lip vs full back panel  
- Hidden display-integratie  
