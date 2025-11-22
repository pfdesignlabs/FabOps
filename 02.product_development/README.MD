# PF DESIGN LABS — PRODUCT LIFECYCLE FRAMEWORK


_A standardized end-to-end development process for hardware, firmware, mechanical and digital products._

---

## 🧭 PURPOSE

This framework defines how every PF Design Labs project moves from idea to market-ready product.  
It combines proven methodologies:

---

## 🧩 FOLDER STRUCTURE

```
product_lifecycle/
│
├── 00_Discovery/          → Empathize → Define → Ideate  
├── 01_Strategic_Fit/      → Prioritize & align with PF Design Labs mission  
├── 02_System_Definition/  → Architecture, BOM, risk & compliance  
├── 03_PoC/                → Proof of concept builds  
├── 04_EVT/                → Engineering Validation Test  
├── 05_DVT/                → Design Validation Test  
├── 06_PVT/                → Production Validation Test  
├── 07_MP/                 → Mass Production & ramp-up  
├── 08_Launch/             → Packaging, marketing, documentation  
├── 09_PostLaunch/         → Field data, support, updates  
└── 10_Knowledge/          → Retrospective & lessons learned
```

Refer to `phase_capabilities.yaml` for the canonical mapping between lifecycle phases and FabOps capabilities; agents use it to decide which playbooks to load.

Each phase folder contains:

- `*_GUIDE.md` – what to do in that phase  
- `*_TEMPLATE.md` – ready-to-use structure for deliverables  
- `GATE_*.md` – checklist for phase-end review (GO / HOLD / KILL)

---

## ⚙️ HOW TO USE

1. **Clone or instantiate** this template for a new project  
   ```bash
   fabops new project --from-template product_lifecycle --name "MyProject"
   ```

2. **Work phase-by-phase**
   - Complete templates inside each folder.  
   - Keep all design assets (CAD, PCB, firmware) referenced here.

3. **Run gate reviews**
   - Use each `GATE_*.md` checklist to decide GO / HOLD / KILL.  
   - Commit decisions to Git (`/reviews/` folder recommended).

4. **Automate validation**
   - FabOps agents can parse gates, verify deliverables, and push results to dashboards.

---

## 🚀 PHASE OVERVIEW

| # | Phase | Goal | Typical Output |
|---|--------|------|----------------|
| 00 | **Discovery** | Understand users & define meaningful problems | JTBD interviews, value maps, opportunity list |
| 01 | **Strategic Fit** | Select projects aligned with strategy & capability | Fit matrix, decision memo |
| 02 | **System Definition** | Translate concept into architecture | Arch.md, BOM, risk register |
| 03 | **PoC** | Validate key technical assumptions | PoC report, measurements |
| 04 | **EVT** | Verify functional performance | PCB v1, firmware v1, EVT log |
| 05 | **DVT** | Verify robustness & compliance readiness | Reliability report, pre-compliance data |
| 06 | **PVT** | Validate manufacturing process | Pilot run report, QA plan |
| 07 | **MP** | Controlled production ramp-up | Yield dashboard, ECO log |
| 08 | **Launch** | Prepare for public release | Packaging, manual, marketing assets |
| 09 | **Post-Launch** | Monitor & improve in field | Telemetry, RMA log, firmware updates |
| 10 | **Knowledge** | Capture lessons & metrics | Lessons Learned.md, updated SOPs |

---

## 🧠 GATE REVIEWS

Each major phase ends with a **Gate Review**:

| Gate | Purpose |
|------|----------|
| `GATE_DISCOVERY_REVIEW.md` | Are problems validated and worth pursuing? |
| `GATE_STRATEGIC_FIT.md` | Does this fit PF Design Labs strategy and capabilities? |
| `GATE_POC_REVIEW.md` | Are key risks retired? |
| `GATE_EVT_REVIEW.md` | Is the engineering design functionally solid? |
| `GATE_DVT_REVIEW.md` | Is the design robust, safe, compliant? |
| `GATE_PVT_APPROVAL.md` | Is the process stable and ready for ramp? |
| `GATE_LAUNCH_REVIEW.md` | Is launch material complete and approved? |

Each gate form supports automated FabOps parsing to track project readiness.

---

## 📊 DOCUMENTATION & TRACEABILITY

- Version control all deliverables (`GitHub`, `FabOps`, `Databricks`, or internal server).  
- Store decision logs under `/reviews/`.  
- Maintain one `project.yaml` or `metadata.yaml` file with current phase and gate status.  
- Use consistent naming: `EVT-1`, `DVT-1`, `PVT-1`, `MP-1`, etc.

---

## 🔗 CROSS-CUTTING THEMES

| Domain | Description |
|---------|--------------|
| **Design Thinking** | Human-centered discovery process |
| **Lean Startup Loop** | Build → Measure → Learn iterations |
| **DFM / DFT / DFA** | Manufacturability & testability from day 1 |
| **Compliance** | CE, FCC, RoHS, REACH, Safety |
| **Sustainability** | Lifecycle, repairability, recyclability |
| **Telemetry / FabOps** | Production & field data feedback loop |
| **Stage-Gate Governance** | Objective decisions, transparent transitions |

---

## 📚 REFERENCES

- IDEO / Stanford d.school — *Design Thinking Bootcamp Bootleg*  
- Christensen — *Competing Against Luck (Jobs-to-Be-Done)*  
- Ulrich & Eppinger — *Product Design and Development*  
- Norman — *The Design of Everyday Things*  
- Cooper — *Winning at New Products (Stage-Gate Process)*  
- Ries — *The Lean Startup*  
- Bolt.io — *Hardware Development Guide*  
- IPC-7351 / IPC-A-610 — PCB Manufacturability Standards  
- IEEE-1149.1 — Boundary-Scan / JTAG  
- NASA Systems Engineering Handbook  

---

**Maintainer:** PF Design Labs · FabOps Core  
**Version:** 1.0 (October 2025)
