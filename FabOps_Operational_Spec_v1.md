
# FabOps v1.0 — Operational Specification  
*PF Design Labs – 2025*

---

## 0. Introduction

### 0.1 Purpose of FabOps
FabOps is het operationele raamwerk voor het end-to-end ontwikkelen van hardware- en softwareproducten binnen PF Design Labs.  
Het zorgt voor structuur, herhaalbaarheid, documentatie en efficiënte samenwerking tussen mens en AI-agent.

Het systeem standaardiseert:
- projectdefinitie  
- executie  
- documentatie  
- discipline-activatie  
- task management  
- gate reviews  

### 0.2 Scope
FabOps is toepasbaar op alle productontwikkelingsprojecten: hardware, elektronica, firmware, software, content en GTM.

### 0.3 Principles
- **Iteratief** – nooit strikt lineair, altijd learning loops  
- **Lean** – geen over-engineering, geen bureaucratie  
- **Clarity-first** – minimale ambiguïteit  
- **Agent-friendly** – machine-readable structuur  
- **Advisor mode** – AI adviseert, mens beslist  
- **Proactive** – AI signaleert blokkades en fase-transities  

### 0.4 Who Uses FabOps
- PF Design Labs (menselijk team)  
- ChatGPT Agent (operationeel uitvoerder, documentbeheer)  
- Externe engineers wanneer nodig  

### 0.5 Mode of Interaction
- Jij beslist.  
- De agent adviseert, structureert, signaleert en documenteert.  
- Geen autonome commits.  
- Proactieve notificaties bij risico’s, blocking tasks en fase-onderbrekingen.

---

## 1. Input Model (Project Definition)

### 1.1 The 8 Required Input Parameters
Elk nieuw project start met deze ultra-lean set:

1. **Product Name**  
2. **Vision (1 sentence)**  
3. **Target User**  
4. **Primary Job-to-be-Done**  
5. **Core Value Proposition**  
6. **Key Constraints** (time, budget, must-use technology)  
7. **Repository Path + Local Project Root Path**  
8. **Success Criteria** (max. drie meetbare doelen)

### 1.2 Optional Input Parameters
- Competitive references  
- Required integrations (hardware/software/cloud)  
- Early risks  
- Manufacturing preferences  
- Relevante capabilities uit de FabOps capability-library  

### 1.3 Discipline Relevance Detection
De agent bepaalt **autonoom** welke disciplines worden geactiveerd door te kijken naar o.a.:

- aanwezigheid van hardware  
- aanwezigheid van elektronica  
- aanwezigheid van firmware  
- aanwezigheid van backend/software  
- noodzaak voor industrial design  
- noodzaak voor validatie (POC/EVT/DVT/PVT)  
- noodzaak voor productievoorbereiding  
- GTM/verkoopbehoeften  

**Alleen relevante disciplines** worden aangemaakt.

### 1.4 Example Input Template (JSON)
```json
{
  "product_name": "",
  "vision": "",
  "target_user": "",
  "job_to_be_done": "",
  "value_proposition": "",
  "constraints": "",
  "repo_path": "",
  "local_path": "",
  "success_criteria": ["", "", ""]
}
```

### 1.5 How Inputs Are Stored
Alle inputparameters worden opgenomen in:

```text
fabops.config.json
```

Dit is de single source of truth voor het project.

---

## 2. FabOps Lifecycle Overview

### 2.1 Iterative Hardware Product Lifecycle
FabOps is gebouwd voor snelle iteratie. Fases zijn geen lineaire waterval maar cyclische loops:

- Foundation  
- Design / discipline execution  
- Validation  
- Production preparation  
- GTM  
- Launch  
- Post-launch refinement  

### 2.2 Gate Reviews (Medium Severity)
Bij elke major milestone voert de agent een gate-review voor.

Medium betekent:  
→ kort, analytisch, impact-driven  
→ geen corporate PPT-overkill, wél zakelijke discipline  

### 2.3 Phase States
Elke fase bestaat in één van drie staten:

- **inactive** – nog niet relevant  
- **active** – in uitvoering  
- **locked** – afgerond, freeze unless issues arise  

### 2.4 Trigger Logic
De agent signaleert wanneer een fase:

- klaar is om te starten (input voldaan)  
- vastloopt (blocking dependencies)  
- onvoldoende gedefinieerd is  
- afgerond kan worden  

De gebruiker moet altijd bevestigen.

### 2.5 Required Outputs Per Phase (High-Level)
Per fase wordt minimaal vastgelegd:
- Deliverables  
- Decision log updates  
- Open actions  
- Gate review-conclusies  
- Updates in `fabops.config.json`  

---

## 3. Discipline Architecture

### 3.1 Activated Disciplines
Afhankelijk van de input detecteert de agent welke disciplines nodig zijn.

Standaarddisciplines:

- `mechanical`  
- `electronics`  
- `firmware`  
- `software`  
- `industrial_design`  
- `validation`  
- `production`  
- `gtm`  

### 3.2 Deactivation Rules
Disciplines worden **niet aangemaakt** als ze niet relevant zijn.  
Tijdens ontwikkeling kunnen ze alsnog geactiveerd worden als nieuwe inzichten dit vereisen.

### 3.3 Cross-Discipline Dependencies
Voorbeelden:
- `electronics` → `firmware` → `validation`  
- `mechanical` → `industrial_design` → `production`  
- `software` → `gtm`  
- `validation` → gate reviews → roadmap updates  

---

## 4. Folder Structure Specification

### 4.1 Root Structure
Aan het projectroot:

```text
/foundation
/mechanical
/electronics
/firmware
/software
/industrial_design
/validation
/production
/gtm
fabops.config.json
```

De agent maakt alleen relevante folders aan.

### 4.2 Discipline Folder Template
Elke disciplinefolder bevat minimaal:

```text
README.md
open_actions.md
decisions.md
assets/
data/
```

### 4.3 Validation Folder Structure
```text
/validation
    /poc
    /evt
    /dvt
    /pvt
```

### 4.4 GTM Folder Structure
```text
/gtm
    /content
    /branding
    /pricing
    /launch
```

### 4.5 Required Files per Discipline
- **README.md** – uitleg discipline en scope  
- **open_actions.md** – taken + RICE-prioritering  
- **decisions.md** – belangrijke beslissingen voor die discipline  
- **assets/** – schematics, renders, CAD, visuals  
- **data/** – logs, meetdata, experimentresultaten  

### 4.6 Minimal vs Expanded Rules
- De basis is altijd minimalistisch.  
- De agent mag extra structuur voorstellen wanneer dat functioneel noodzakelijk is (bv. submappen per prototypeversie).

---

## 5. Bootstrap Script Requirements (Action 2)

### 5.1 Purpose
Zorgen dat elk project consistent start met een correcte FabOps-structuur.

### 5.2 Script Responsibilities
Het bootstrap-script:

1. Leest de project-inputparameters.  
2. Bepaalt relevante disciplines.  
3. Maakt de benodigde folders aan.  
4. Genereert basis-Markdownbestanden met placeholders.  
5. Maakt een initiële `fabops.config.json`.  
6. Toont een samenvatting aan de gebruiker voor review.  
7. Laat de commit over aan de gebruiker (geen autonome commits).

### 5.3 Markdown Templates (High-Level)
Elke discipline-README bevat minimaal placeholders voor:

```markdown
# <Discipline Name>

## Purpose
<!-- Wat is de rol van deze discipline in dit project? -->

## Goals
<!-- Belangrijkste doelen van deze discipline. -->

## Constraints
<!-- Relevante beperkingen: budget, tijd, tooling, technologie. -->

## Definition of Done
<!-- Wanneer is dit deel 'goed genoeg' om door te gaan? -->

## Risks
<!-- Belangrijkste risico's binnen deze discipline. -->

## Dependencies
<!-- Waar zijn we afhankelijk van (andere disciplines, leveranciers, etc.)? -->
```

`open_actions.md` bevat een lege tabelstructuur voor RICE-taken, bv.:

```markdown
# Open Actions

| ID | Title | Description | Reach | Impact | Confidence | Effort | RICE | Status | Owner | Depends On |
|----|--------|-------------|--------|---------|------------|--------|------|--------|-------|------------|
```

`decisions.md` bevat een logstructuur, bv.:

```markdown
# Decisions

## Decision 001
- **Date:**  
- **Owner:**  
- **Context:**  
- **Decision:**  
- **Alternatives considered:**  
- **Impact:**  
```

### 5.4 fabops.config.json Creation
Het script maakt een initieel bestand zoals:

```json
{
  "product": {
    "name": "",
    "vision": "",
    "target_user": "",
    "job_to_be_done": "",
    "value_proposition": "",
    "constraints": "",
    "success_criteria": [""]
  },
  "paths": {
    "repo_path": "",
    "local_root": ""
  },
  "disciplines": {
    "mechanical": "inactive",
    "electronics": "inactive",
    "firmware": "inactive",
    "software": "inactive",
    "industrial_design": "inactive",
    "validation": "inactive",
    "production": "inactive",
    "gtm": "inactive"
  },
  "prioritization_model": "RICE",
  "metadata": {
    "fabops_version": "1.0.0"
  }
}
```

De agent zet relevante disciplines meteen op `active` zodra het project start.

### 5.5 User Review Step
Na genereren toont de agent:
- folder tree  
- kernbestanden  
- config-overzicht  

De gebruiker bevestigt of vraagt om wijzigingen.  
Daarna kan de gebruiker zelf committen.

---

## 6. Documentation Rules

### 6.1 README.md Standard
Elke README volgt dezelfde structuur:

- Purpose  
- Goals  
- Constraints  
- Definition of Done  
- Risks  
- Dependencies  

### 6.2 Decision Logs (`decisions.md`)
- Elke **belangrijke beslissing** wordt hier vastgelegd.  
- Niet alleen technische beslissingen, ook business- en procesbesluiten.

### 6.3 Task Lists (`open_actions.md`)
Alle taken per discipline:

- krijgen een ID  
- zijn RICE-gescoord  
- hebben een status (todo / in-progress / blocked / done)  
- hebben een owner  
- hebben optioneel dependencies  

### 6.4 Markdown Conventions
- Heldere, korte koppen  
- Bulletpoints boven proza waar mogelijk  
- Eén beslissing per sectie in decisions.md  
- Eén taak per rij in open_actions.md  

### 6.5 Update Triggers
Documenten worden bijgewerkt bij:

- nieuwe info  
- gate reviews  
- nieuwe beslissingen  
- nieuwe of aangepaste taken  
- fase-transities  

### 6.6 Consistency Enforcement
De agent controleert o.a.:

- verweesde taken (geen owner / geen status)  
- inconsistente beslissingen (tegenstrijdig)  
- ontbrekende DoD of risks in README’s  
- disciplines die `active` zijn zonder open actions  

---

## 7. Task Orchestration (Action 3)

### 7.1 RICE Prioritization Model
Standaard task scoring:

- **Reach** – hoeveel gebruikers/impactgebieden worden geraakt?  
- **Impact** – hoe groot is de impact per gebruiker?  
- **Confidence** – hoe zeker zijn we van onze inschatting?  
- **Effort** – hoeveel werk kost het? (bv. in uren of story points)

De agent kan een RICE-score voorstellen, maar de gebruiker kan altijd corrigeren.

### 7.2 Task Generation Rules
Taken ontstaan o.a. wanneer:

- een fase wordt geactiveerd  
- een gate review open items oplevert  
- inputparameters nieuwe eisen introduceren  
- de gebruiker expliciet taken dicteert  

### 7.3 Task Updating
Bij wijzigingen:

- status updaten  
- RICE-score bijstellen indien nodig  
- dependencies toevoegen/verwijderen  
- beslissingen koppelen aan afgeronde taken  

### 7.4 Blocking Logic
De agent markeert taken als **blocked** wanneer:

- een dependency-task niet done is  
- een beslissing nog niet genomen is  
- een externe factor (leverancier, tooling) ontbreekt  

### 7.5 Proactive Signalling
De agent meldt proactief:

- “Je hebt X blocked tasks in discipline Y.”  
- “Je hebt taken zonder owner.”  
- “Je hebt taken in een locked fase die nog open staan.”  

### 7.6 Phase-Based Task Activation
Taken worden alleen aangemaakt of geactiveerd in:

- actieve disciplines  
- actieve fases  

Taken in locked fases mogen alleen aangepast worden na expliciete bevestiging van de gebruiker.

### 7.7 FabTasks Integration
De agent kan alle `open_actions.md`-taken exporteren naar het FabTasks-systeem, zodat daar planning, timers en voortgang gevolgd kunnen worden.

---

## 8. Phase-Specific Requirements

> Let op: dit deel is high-level. Concrete invulling gebeurt per project.

### 8.1 Foundation
**Doel:** het vastleggen van de basisdefinitie van het project.

Outputs:
- ingevulde inputparameters  
- geactiveerde disciplines  
- initiële taken per relevante discipline  
- eerste versie van `fabops.config.json`  
- Foundation gate review (light)  

### 8.2 Industrial Design
**Focus:** vorm, CMF (color, material, finish), user perception.

Typische outputs:
- moodboards  
- vormstudies  
- basisrenders  
- ID-beslissingen in `decisions.md`  

### 8.3 Mechanical
**Focus:** CAD, constructie, sterkte, assemblage.

Typische outputs:
- CAD-modellen  
- samenstellingen  
- productietekeningen (later)  
- mechanische beslissingen + toleranties  

### 8.4 Electronics
**Focus:** schema’s, PCB-layout, componentkeuze.

Outputs:
- schematics  
- PCB-layouts  
- BOM  
- prototype-versies  

### 8.5 Firmware
**Focus:** aansturing hardware, logica, drivers.

Outputs:
- basisfirmware voor EVT/POC  
- configuratie- en update-strategie  
- logica voor testen en validatie  

### 8.6 Software
**Focus:** backend, apps, API’s, dashboards.

Outputs:
- architectuurdiagrammen  
- API-definities  
- MVP-implementatie  

### 8.7 POC
**Focus:** risico’s verminderen, “werkt dit conceptueel?”

Outputs:
- werkende maar ruwe prototypes  
- learnings in `decisions.md`  
- POC gate review  

### 8.8 EVT
**Focus:** functionele validatie van het ontwerp.

Outputs:
- EVT-builds  
- testen op functionaliteit  
- issues + beslissingen  

### 8.9 DVT
**Focus:** betrouwbaarheid, levensduur, edge cases.

Outputs:
- DVT-testresultaten  
- duurzaamheidstesten  
- fixes en updates  

### 8.10 PVT
**Focus:** productieproces, yield, reproductie.

Outputs:
- PVT-builds  
- procesparameters  
- yield-rapporten  

### 8.11 Production
**Focus:** stabiele, reproduceerbare productie.

Outputs:
- definitieve productiedocumenten  
- SOP’s (Standard Operating Procedures)  
- tooling-specificaties  

### 8.12 GTM
**Focus:** content, pricing, branding, lancering.

Outputs:
- contentplanning  
- kernboodschappen  
- prijsstrategie  
- marketingmateriaal  

### 8.13 Launch
**Focus:** daadwerkelijke marktintroductie.

Outputs:
- live productpagina  
- communicatie naar bestaande kanalen  
- initial sales feedback  

### 8.14 Post-launch Ops
**Focus:** feedback terugkoppelen en v2/vn plannen.

Outputs:
- bug/issue-lijsten  
- verbeteringsvoorstellen  
- beslissingen over opvolgversies  

---

## 9. Gate Reviews

### 9.1 Standard Template
Elke gate review wordt vastgelegd in de relevante discipline- of fasecontext met:

```markdown
## Summary  
## Findings  
## Decisions  
## Impact on Cost  
## Impact on Timeline  
## Risks  
## Required Actions  
## Approval  
```

### 9.2 When Reviews Occur
Gate reviews vinden in ieder geval plaats na:
- POC  
- EVT  
- DVT  
- PVT  
- Pre-launch  

### 9.3 Agent Preparation
De agent verzamelt vooraf automatisch:

- open actions  
- relevante beslissingen  
- kernresultaten  
- eventuele blockers  

### 9.4 Revision Handling
Nieuwe inzichten uit gate reviews worden verwerkt in:

- `decisions.md`  
- `open_actions.md`  
- `fabops.config.json`  

---

## 10. Agent Operational Rules

### 10.1 Advisor Mode
- De agent adviseert, de gebruiker besluit.  
- Geen autonome beslissingen op high-impact vlakken.

### 10.2 Proactive Signals
De agent meldt proactief o.a.:

- blockers  
- inconsistenties  
- ontbrekende deliverables  
- open actions in locked fases  
- disciplines die `active` zijn zonder taken  

### 10.3 Updating `fabops.config.json`
De agent werkt `fabops.config.json` automatisch bij na:

- fase-transities  
- wijzigingen in disciplines  
- grote beslissingen  
- wijziging in prioritisatiemodel (indien ooit aangepast)  

### 10.4 Discipline Logic
De agent kan disciplines voorstellen om te activeren of te deactiveren.  
Activatie en deactivatie gebeurt altijd na bevestiging door de gebruiker.

### 10.5 State Changes
State flow: `inactive` → `active` → `locked`.  
Alleen bij sterke reden kan een locked fase heropend worden, altijd met expliciete bevestiging.

### 10.6 Task Generation
- Tasks worden altijd gegenereerd in overleg met de gebruiker.  
- De agent kan suggesties doen, maar nooit zelfstandig een overdaad aan noise-tasks creëren.

### 10.7 Forbidden Actions
De agent doet nadrukkelijk **niet**:

- autonome git commits  
- onomkeerbare workflow-acties zonder menselijke bevestiging  
- kritieke juridische of financiële beslissingen nemen  

---

## 11. Governance & Change Management

### 11.1 Adding Disciplines
- Nieuwe disciplines kunnen worden toegevoegd aan het framework.  
- Dit vereist een update van de FabOps-spec en versieverhoging.

### 11.2 Framework Evolution
- FabOps evolueert iteratief.  
- Wijzigingen worden versioned en per project vastgelegd.

### 11.3 Versioning Standard
- Gebruik SemVer: `vMAJOR.MINOR.PATCH`.  
- `fabops.config.json` bevat de gebruikte FabOps-versie per project.

### 11.4 Multiple Projects
- Elk project heeft zijn eigen `fabops.config.json`.  
- Dezelfde agent kan meerdere projecten parallel bedienen, zolang de config per project gescheiden blijft.

---

## 12. Appendix

### 12.1 Directory Tree (Generic Example)
```text
project_root/
  foundation/
  mechanical/
    README.md
    open_actions.md
    decisions.md
    assets/
    data/
  electronics/
  firmware/
  software/
  industrial_design/
  validation/
    poc/
    evt/
    dvt/
    pvt/
  production/
  gtm/
    content/
    branding/
    pricing/
    launch/
  fabops.config.json
```

### 12.2 Markdown Templates
De standaardtemplates voor README, open_actions en decisions worden door het bootstrap-script gegenereerd.

### 12.3 Input Schema
Het inputmodel kan desgewenst worden vastgelegd als JSON Schema om automatische validatie mogelijk te maken.

### 12.4 Example `fabops.config.json`
Een concreet voorbeeld wordt per project gegenereerd en kan dienen als referentie voor volgende projecten.

### 12.5 Glossary
- **EVT** – Engineering Validation Test  
- **DVT** – Design Validation Test  
- **PVT** – Production Validation Test  
- **CMF** – Color, Material, Finish  
- **JTBD** – Jobs To Be Done  
- **Gate review** – formeel reviewmoment op een overgang tussen fases  
- **Discipline** – inhoudelijk domein zoals mechanical, electronics, firmware, etc.
