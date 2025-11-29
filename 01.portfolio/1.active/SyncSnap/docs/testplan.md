# Test Plan

## Bench Tests
- Verify reed switch actuation using a magnet; ensure focus base resistor pulls low before releasing shutter path.
- Use LEDs (with current-limiting resistors) in place of camera lines to visualize focus and shutter timing.
- Confirm clamp diodes limit reverse voltage spikes when switching inductive loads during bench simulation.

## Camera Integration
- Connect to a Sony camera in AF mode; ensure focus engages before shutter triggers when reed closes.
- Validate that releasing the reed returns both focus and shutter to idle without latch-up.

## Regression
- Re-run `scripts/build.sh` after schematic or footprint edits; inspect generated Gerbers/STEP for regressions.
- Document any observed timing issues or mechanical fit problems in `CHANGELOG.md` and update component values as needed.
