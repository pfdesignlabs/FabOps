# PCB Prototyping Research:

**Project:** NESP / PCB Design  
**Researcher:** PF Design Labs  
**Date:** 2025-10-29 
**Status:** Completed – transitioned to process development  

---

## 1. Objective

Evaluate the feasibility of rapid in-house PCB prototyping as part of the FabOps electronics capability.
The objective is not to achieve production-grade quality, but to establish a reliable method for verifying:
- the correctness of the schematic and net connectivity,
- the basic routing and layout integrity, and
- the fit and placement of selected components.

By enabling same-day fabrication of functional prototype boards, this capability would significantly shorten the hardware iteration loop.
External PCB manufacturing typically requires 8–14 days from order to delivery (including production, shipping, and customs), whereas a controlled in-house process could potentially reduce this to less than one day per iteration.
---

## 2. Equipment and Materials

| Category | Item / Model | Notes |
|-----------|---------------|-------|
| laser system | **xTool F1 Ultra**, 20 W fiber + UV hybrid | Used for ablation and drilling tests |
| laser system | **ComMarker B6 MOPA 60 W** | Used for ablation and drilling tests |
| Substrates | FR-1 copper-clad boards | Preferred due to lower thermal mass |
| 3D printing system | HeyGears Reflex SLA printer (PAWR-10 resin) | Used for drill-guide jigs |
| Etchant system | **ProtoEtch** (in-development) | Used for controlled sodium persulfate etching |
| Etchant | Sodium persulfate solution | 40–50 °C bath |
| Masking | **Motip High Heat Lacquer** (black) | Used as laser-removable resist |
| Tools | Drill press, squeegee, UV curing station | For validation and silkscreen work |

---

## 3. Methodology

This section documents the sequence of process experiments performed to establish an in-house PCB prototyping workflow.  
Three core operations were studied:  
1. **Creation of conductive traces**  
2. **Drilling of holes and board cutting**  
3. **Application of soldermask and silkscreen**

---

## 3.1 Trace Creation

### 3.1.1 Direct Laser Ablation (xTool F1 Ultra)

**Setup**  
Initial tests aimed to directly remove unwanted copper using the **xTool F1 Ultra (20 W fiber/UV hybrid)**. FR-1 copper-clad boards were used to evaluate thermal response and adhesion differences. Multiple laser parameter grids were generated—varying scan speed, power, and focus height—to observe ablation behavior.

**Procedure**  
Grids of small test squares and trace patterns were burned at different power/speed combinations to determine the energy density required for full copper removal. Each sample was inspected under magnification for completeness, edge quality, substrate damage, and thermal discoloration. Focus adjustments were performed manually between tests.

**Observations**  
- Copper’s **high reflectivity** caused inconsistent energy absorption.  
- The process was extremely **focus-sensitive**; small surface warping of the FR-1 (~±0.1 mm) led to large variation in results.  
- Local heating caused the substrate to **warp**, compounding focus drift mid-process.  
- The **galvo scanning field (~150 mm)** produced non-uniform spot shapes—more elliptical near the edges—resulting in uneven ablation across the board.  
- Effective copper removal occurred sporadically, requiring operator intervention and frequent recalibration.

**Evaluation**  
Although ablation occasionally succeeded, it lacked the consistency and autonomy needed for a viable rapid-prototyping workflow.  
The method required excessive manual adjustment, offered low repeatability, and risked substrate deformation.  
It was therefore classified as **non-viable for production-level prototyping** and replaced by a hybrid etching process.

---

### 3.1.2 Mask + Etch (Hybrid Process)

**Setup**  
The alternative method used **Motip High Heat Lacquer (black)** as a laser-removable resist layer.  
Copper was selectively exposed by ablating the **negative pattern** of the PCB layout using the same xTool F1 Ultra.  
After ablation, the boards were etched in **sodium persulfate** solution (40–50 °C) under gentle agitation.  
Temperature and agitation control were later managed via the **ProtoEtch** system for process repeatability.

**Procedure**  
1. Apply an even coat of black lacquer; allow full drying.  
2. Import the negative trace pattern into the laser software.  
3. Ablate exposed copper regions while preserving the masked traces.  
4. Submerge the board in sodium persulfate until all unmasked copper is removed.  
5. Rinse, strip remaining lacquer.  

**Observations**  
- The laser cleanly removed lacquer without damaging copper.  
- The etching process yielded **sharp, well-defined traces** with high isolation fidelity.  
- Residual lacquer could be wiped off with isopropyl alcohol post-etch.  
- The method proved tolerant to small focus or surface variations.  

**Evaluation**  
The hybrid approach demonstrated high reliability and repeatability.  
It combined the precision of laser patterning with the proven chemistry of wet etching.  
Integration with ProtoEtch provides the potential for **closed-loop temperature control, agitation logging, and process telemetry**, making this method the **preferred baseline for FabOps PCB prototyping**.

---

## 3.2 Hole Drilling and Board Cutting

### 3.2.1 Laser Drilling on xTool F1 Ultra

**Setup**  
After trace fabrication, attempts were made to laser-drill vias and mounting holes directly with the xTool F1 Ultra.

**Procedure & Observations**  
- Multiple low-speed high power passes were required to penetrate FR-1.  
- With reduced copper mass near holes, **heat dissipation was poor**, causing pad delamination and trace lifting.  
- Even minor overheating destroyed pad integrity, rendering boards unusable.

**Evaluation**  
The 20 W laser lacked sufficient control and thermal headroom for micro-drilling.  
This approach was discontinued.

---

### 3.2.2 Drill Guides (HeyGears Reflex + PAWR-10)

**Setup**  
To achieve precise manual drilling, **drill templates** were printed in **PAWR-10 resin** using the **HeyGears Reflex SLA printer**.  
The high resolution of SLA printing enabled accurate hole alignment—something unachievable with FDM due to lower XY precision.

**Procedure**  
- STL jigs were exported from CAD with 1 mm drill pilot holes.  
- Printed templates were aligned to the board outline and fixed.  
- Holes were drilled manually using a **mini drill press (Dremel)**.

**Observations**  
- Alignment accuracy was high; hole registration matched the design closely.  
- However, the workflow was **time-intensive** (≈ 12 h print time per jig).  
- Reusable jigs **wore quickly** after multiple uses, leading to progressive misalignment.  

**Evaluation**  
The method achieved good precision but lacked scalability for rapid iteration.  
Suitable for one-off prototypes but not for daily design cycles.

---

### 3.2.3 ComMarker B6 MOPA 60 W Laser Drilling

**Setup**  
A **ComMarker B6 MOPA 60 W** laser was introduced to overcome power and focus limitations.  
Drilling tests targeted hole diameters between 0.6 mm – 1.0 mm.

**Procedure & Observations**  
- The higher energy density allowed clean penetration of FR-1 without visible thermal delamination.  
- Hole circularity and edge quality were significantly improved.  
- Focus stability across the field was consistent; no localized over-burn observed.  

**Evaluation**  
This configuration proved capable of precise and consistent **micro-drilling**, representing the most promising in-house approach to replace mechanical drilling for small-scale PCB prototyping.

---

## 3.3 Soldermask and Silkscreen Application

**Setup**  
A **custom screen-printing jig** was developed to apply **UV-curable soldermask and silkscreen ink**.  
A fine **120 T mesh screen** was used for resolution and edge sharpness.  
Curing was performed in the **HeyGears Cure station**.

**Procedure**  
1. Mount board and align jig.  
2. Apply UV-curable ink and spread evenly using a squeegee.  
3. Expose under UV until fully hardened.  
4. Use the **fiber laser** for precise post-cure labeling or marking on the silkscreen layer.

**Observations & Evaluation**  
- The first application yielded **excellent results**—smooth surface finish, crisp edges, and strong adhesion.  
- The process was repeatable and compatible with both etched and laser-drilled boards.  
- The laser post-marking step allowed high-contrast, permanent legends without secondary print passes.  

**Conclusion**  
The silkscreen/soldermask process is **production-grade in quality** and can be fully integrated into the FabOps PCB finishing pipeline.

---

### Summary of Process Outcomes

| Operation | Tool / Method | Result | Viability |
|------------|----------------|---------|------------|
| Trace creation (ablation) | xTool F1 Ultra 20 W | Inconsistent, low repeatability | ❌ Not viable |
| Trace creation (mask + etch) | Laser + Motip + Sodium Persulfate | Sharp, repeatable, controllable | ✅ Adopted |
| Hole drilling (manual) | HeyGears SLA Jig + Drill Press | Accurate but time-intensive | ⚠️ Limited |
| Hole drilling (laser) | ComMarker B6 MOPA 60 W | Clean holes ≥ 0.6 mm – consistent | ✅ Adopted |
| Soldermask / silkscreen | Screen printing + UV cure + Laser mark | High quality, repeatable | ✅ Adopted |

---

**Document Control**  
- Author: PF Design Labs / FabOps  
- Version: 1.0
- Last updated: 2025-10-29
