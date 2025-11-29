#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT_DIR"

if [[ -z "${VIRTUAL_ENV:-}" && -f ".venv/bin/activate" ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

export XDG_CONFIG_HOME="${ROOT_DIR}/.config"
mkdir -p "$XDG_CONFIG_HOME"

ATO_FLAGS=(
  "--non-interactive"
  "build"
  "--build" "snapsync_v3"
)

ato "${ATO_FLAGS[@]}"

PCB="${ROOT_DIR}/hardware/pcb/SnapSyncV3/SnapSyncV3.kicad_pcb"

if [[ ! -f "$PCB" ]]; then
  echo "Expected PCB at $PCB was not generated" >&2
  exit 1
fi

# Best effort: add KiCad macOS bundle tools if present
if ! command -v kicad-cli >/dev/null 2>&1; then
  if [[ -x "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli" ]]; then
    export PATH="/Applications/KiCad/KiCad.app/Contents/MacOS:${PATH}"
  fi
fi

if [[ -z "${KICAD8_FOOTPRINT_DIR:-}" && -d "/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints" ]]; then
  export KICAD8_FOOTPRINT_DIR="/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints"
fi

if [[ -z "${KICAD9_FOOTPRINT_DIR:-}" && -d "/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints" ]]; then
  export KICAD9_FOOTPRINT_DIR="/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints"
fi

if [[ -z "${KICAD8_3DMODEL_DIR:-}" && -d "/Applications/KiCad/KiCad.app/Contents/SharedSupport/3dmodels" ]]; then
  export KICAD8_3DMODEL_DIR="/Applications/KiCad/KiCad.app/Contents/SharedSupport/3dmodels"
fi

if [[ -z "${KICAD9_3DMODEL_DIR:-}" && -d "/Applications/KiCad/KiCad.app/Contents/SharedSupport/3dmodels" ]]; then
  export KICAD9_3DMODEL_DIR="/Applications/KiCad/KiCad.app/Contents/SharedSupport/3dmodels"
fi

if ! command -v kicad-cli >/dev/null 2>&1; then
  echo "kicad-cli not found on PATH; skipping Gerber/STEP export" >&2
  exit 0
fi

mkdir -p build/gerbers build/step

kicad-cli pcb export gerbers \
  --layers F.Cu,B.Cu,Edge.Cuts,F.SilkS,B.SilkS,F.Mask,B.Mask \
  --output build/gerbers "$PCB"

kicad-cli pcb export drill \
  --format excellon \
  --output build/gerbers "$PCB"

kicad-cli pcb export step \
  --output build/step/SnapSyncV3.step "$PCB"
