# Preferred Parts

## Connectors
- **SJ1-2503A** — 2.5 mm TRRS jack used by Sony Multiport. Reference datasheet for drill pattern and plating thickness.

## Sensors
- **Reed switch (SMD glass capsule)** — Footprint placeholder `Switch:Reed_SMD_Custom`; replace with exact part number once final package is selected.

## Active Components
- **Transistor**: 2N3904 (TO-92 inline) for focus and shutter switching.

## Passive Components
- **Base resistors**: 1 kΩ axial (DIN0207) for focus and shutter drive.
- **Pull-down resistor**: 10 kΩ axial (DIN0207) on shutter base.
- **Debounce capacitor**: 0.1 µF disc ceramic (5 mm pitch), optionally tune up to 1 µF as needed.
- **Clamp diodes**: 1N4148 axial for transistor protection (stripe → collector).

## Action Items
- Attach SJ1-2503A and reed switch datasheets to this directory or link to their sources.
- Update footprint mapping once exact reed package is confirmed.
