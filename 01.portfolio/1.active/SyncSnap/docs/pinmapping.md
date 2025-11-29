# Sony Multiport Pin Mapping

## TRS Jack (SJ1-2503A)
- Pin 1: Ground (sleeve)
- Pin 2: Focus (ring 1)
- Pin 3: Focus (ring 2) — hard-bridged to Pin 2 on the PCB
- Pin 4: Shutter (tip)

## System Nets
- `focus` net drives the base of `q_focus` to pull the camera focus line low.
- `shutter` net drives the base of `q_shutter` to actuate the shutter after focus settles.
- `GND` is common between the camera and reed switch return.

## Notes
- Pin bridging of 2 ↔ 3 matches Sony Multiport requirement for duplicated focus contacts.
- Confirm orientation of SJ1-2503A footprint so Pin 1 (ground) aligns with board outline and cable exit.
