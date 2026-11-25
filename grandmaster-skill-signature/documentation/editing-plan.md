# Editing Plan — GRANDMASTER SKILL SIGNATURE · PAK SU DEN

**Concept:** THE ART OF MASTERY · *Beyond Technique. Beyond Experience. Beyond Limits.*
**Format:** 9:16 · 1080 × 1920 · 30 fps · 86.0 s · Bahasa Melayu audio, English subtitles.

## The story the material can honestly tell

The footage shows one participant performing techniques; the master appears in three photos. So the film is a **lineage**:

> The master teaches → the student performs his signature techniques → the master's voice of correction → the master certifies the student → the academy.

This is stronger than pretending the participant is Pak Su Den, and it is exactly what "Grandmaster Skill Signature" sells: a course that builds therapists.

## Structure (cuts on a 120 BPM grid, 1 bar = 2 s)

| # | Scene | Time | Picture | Text | Sound |
|---|---|---|---|---|---|
| 1 | The Hook | 0–4 | 4 fast cuts (0.5 s) → speed-ramp into slow-motion palm press | SKILL IS LEARNED. → **MASTERY** IS BUILT. | Boom + braam at 0, boom at 2.0, taiko roll, flash |
| 2 | The Master | 4–12 | Pak Su Den teaching (photo card, push-in) → classroom wide (pan) | THE MASTER · PAK SU DEN · Founder • Therapist • Trainer → World Holistic Massage Championship · OVERALL WINNER · Singapore 2025 | Controlled pulse |
| 3 | The Masterclass | 12–24 | Slow-mo hands → participant hero → 3 techniques | MASTERCLASS SIGNATURE · GRANDMASTER SKILL SIGNATURE · Knowledge. Precision. Mastery. → credit: SIGNATURE DEMONSTRATION · BENG | Ostinato enters, shimmer on title |
| 4 | Signature Techniques | 24–44 | 10 shots in 3 chapters, slow motion on the openers | 01 HAND POSITIONING · 02 BODY MECHANICS · 03 CONTROLLED MOVEMENT (+ BM sub-lines) | Full percussion, braams, whooshes on chapters |
| 5 | Knowledge Transfer | 44–60 | Two long coaching takes, punch-ins, one B-roll cutaway | KNOWLEDGE BECOMES SKILL. · SKILL BECOMES MASTERY. + subtitles | **Real coaching voice**, music ducked to 30%, emotional strings, riser |
| 6 | The Climax | 60–74 | 15 cuts (0.5–2 s), book-ends the opening shape | MORE THAN JUST TECHNIQUE. · BUILDING THE NEXT GENERATION OF THERAPISTS. (word per beat) | Drop: boom + impact, choir, full drums |
| 7 | The Legacy | 74–86 | Certificate photo (push-in) → navy end card | GRANDMASTER SKILL SIGNATURE · PAK SU DEN · 25 NOVEMBER 2026 · PERMAS JAYA, JOHOR, MALAYSIA → PAK SU DEN lockup · AKADEMI & PUSAT RAWATAN HOLISTIK & KOMPLEMENTARI PAK SU DEN · BUKAN SEKADAR RAWATAN · MORE THAN JUST TREATMENT | Resolution to D major, end hit at 80, shimmer |

Shot-by-shot: `edit-decision-list.json` (42 events, every in-point and speed).

## Editing rules applied

- **Every cut has a reason**: on a beat, on a change of idea, or to cover a jump (B-roll shot 24 covers the change between the two coaching takes).
- **J-cut**: the coaching voice starts 0.4 s before its picture (43.6 s). **L-cut**: "turun" carries over the B-roll at 51.5 s.
- **Speed**: 60 fps sources → clean 0.5× slow motion (shots 5, 8, 13, 20, 22, 32, 40); one speed ramp (1.0 → 0.45×) on the hook.
- **Camera**: slow push-ins on wrappers; two punch-ins inside the long takes (48.0 s, 56.1 s).
- **Transitions (5 kinds, each motivated)**: exposure flash (4.0, 60.0, 74.0), dip cut (12.0, 44.0), iris with a gold ring (30.0, 37.0), colour flood (79.5), hard cuts everywhere else.
- **Removed**: beng 20 (camera dropped), beng 21 first 3.6 s (floor), beng 10 first 6.5 s (back to camera), long repeated palpation in beng 18/19, all native room hiss.

## Technical corrections

| Problem | Fix |
|---|---|
| 360 × 640 source | Lanczos ×3 + contrast-adaptive sharpen + light 3D denoise (no AI "invented" detail) |
| Handheld shake | vidstab 2-pass, smoothing 12, 4% zoom |
| Variable 59/60 fps | Conformed to 60 fps CFR (enables 0.5× slow motion) |
| Over-saturated cyan walls, green sheets | HSL secondaries in the grade (blue −18% sat, green −30% sat and shifted toward teal) |
| Flat contrast | Deep-contrast preset @ 0.4, navy shadow wheel, gold highlight wheel |
| Skin | Kept neutral: no wheel push into skin hues; checked on two shots (grade-compare sheets in `graphics/grade/`) |
| Dialogue hiss | FFT denoise, high-pass 95 Hz, +3 dB presence, compression, −17 LUFS |

Not done (and why): **face relighting / exposure per face** — HyperFrames treatments are whole-frame; no region tracking was performed. **White balance per clip** — all clips come from one camera in one room; one grade keeps them consistent.

## Safe zones

All text sits inside the TikTok / Reels / Shorts safe area (y 288–1248; x 120–888 above y 840, 120–780 below). Subtitles' bottom edge at y 1240. Minimum type size 28 px. Verified by `hyperframes check` (layout + contrast).
