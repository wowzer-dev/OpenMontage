# OpenMontage MP-0047 comparison handoff

## Project

Video Editing Automation — VEA-002 OpenMontage comparison, implemented in the separate `wowzer-dev/OpenMontage` fork on branch `codex/mp0047-comparison-fix`.

## Current state

PASS locally. The same MP-0047 source used for the CapCut test now has an OpenMontage comparison render with readable captions and two fade-through-black transitions.

## Changed

- Corrected caption word spacing and active-word rendering.
- Added two full-frame fade-through-black transitions at 18.562s and 90.220s.
- Preserved full source duration and original portrait dimensions.
- Fixed staged-media path handling and source-dimension probing.
- Preserved the original mono AAC packet stream without re-encoding.
- Added focused regression coverage for the comparison workflow.

## Evidence

- Render: `/Users/jakehaning/AI-Video-Factory/OpenMontage/projects/capcut-comparison-mp0047-openmontage/renders/MP-0047_openmontage_comparison.mp4`
- Media: 1080x1920, 30 fps, 124.128125s, H.264 video plus AAC audio.
- Audio packet MD5, source and output: `7c1392337098e82631d1fca398e855b2`.
- Visual review: nine sampled frames passed, including both transition centers.
- Automated checks: 21 focused tests passed; Remotion TypeScript validation passed.
- Compose checkpoint: `completed`, review result `pass`.
- Supabase readback: row `b7c7acc1-a261-4faf-9167-22656c761bd4`, idempotency key `openmontage-mp0047-comparison-pass-2026-09-13`.

## Conflicts / UNKNOWNs

- The render is intentionally gitignored and remains local; GitHub contains the reusable source fix and regression tests, not the 151 MB output.
- Whether OpenMontage should replace or complement the CapCut workflow remains an owner decision after side-by-side review.

## Exact next action

Jake compares the OpenMontage render with the CapCut output, then decides whether to adopt OpenMontage as a retained workflow.
