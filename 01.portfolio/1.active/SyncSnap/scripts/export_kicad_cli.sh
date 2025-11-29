#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <path-to-kicad-pcb>" >&2
  exit 1
fi

pcb_path=$1
output_dir=${2:-build}

mkdir -p "${output_dir}/gerbers" "${output_dir}/step"

gerber_out="${output_dir}/gerbers"
step_out="${output_dir}/step"

kicad-cli pcb export gerbers \
  --layers F.Cu,B.Cu,Edge.Cuts,F.SilkS,B.SilkS,F.Mask,B.Mask \
  --output "${gerber_out}" "${pcb_path}"

kicad-cli pcb export drill \
  --format excellon \
  --output "${gerber_out}" "${pcb_path}"

kicad-cli pcb export step \
  --output "${step_out}/$(basename "${pcb_path}" .kicad_pcb).step" "${pcb_path}"
