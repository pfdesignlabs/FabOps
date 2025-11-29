# SnapSync v3

Passive Sony Multiport camera trigger — **Atopile-driven**, fully reproducible hardware design.

## Features
- Reed sensor input → NPN base drive
- Separate focus + shutter paths with 1k base resistors
- Shutter debounce RC (0.1–1 µF + 10k pull-down)
- Clamp diodes (1N4148, stripe → collector)
- SJ1-2503A TRS jack: Pin1=GND, 2/3=Focus (bridged), 4=Shutter

## Build
```bash
pip install atopile
# KiCad 7/8 with kicad-cli required
bash scripts/build.sh
```

The helper script wraps `ato --non-interactive build --build snapsync_v3`,
so make sure the Atopile CLI (>=0.12) is on your PATH or use the repo's
`.venv`. If `kicad-cli` is unavailable the script will skip the Gerber/STEP
export step after generating the KiCad project.

Repo map
atoms/        # Atopile components
designs/      # SnapSync circuit (DSL)
footprints/   # Footprint mapping & PCB rules
scripts/      # Build/export scripts
docs/         # SOPs, manuals
hardware/pcb/ # Final locked releases (v3.0, v3.1, …)
.github/      # CI workflows

---
