# Fabrication Notes

## Process
- Board fabricated via laser ablation + wet etching; drills completed with laser or Dremel.
- Expect hobby-grade tolerances; avoid fine-pitch or sub-10 mil geometries.

## Design Rules
- Clearance: 0.4064 mm (16 mil)
- Minimum trace width: 0.3048 mm (12 mil)
- Power trace width: 0.508 mm (20 mil)
- Thermal relief spoke width: 0.6 mm (24 mil)
- Edge clearance: 0.4 mm
- Keep hole diameters generous for manual drilling; verify SJ1-2503A drill chart before release.

## Documentation
- Matching constraints are encoded in `designs/snapsync_v3.ato` and enforced by `scripts/build.sh`.
- Update this document alongside any rule changes so CI and manual fabrication stay aligned.
