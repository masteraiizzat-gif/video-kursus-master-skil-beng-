# Preview Notes — v1 (25 Nov 2026)

**Stage: PREVIEW ONLY.** Nothing final has been rendered or exported.

| Deliverable | Where |
|---|---|
| Playable preview (draft quality, watermarked "PREVIEW · NOT FINAL") | `preview/PREVIEW-draft-watermarked.mp4` (not in git) |
| Editable, scrubbable timeline | HyperFrames Studio: `npx hyperframes@0.9.94 preview` → `http://localhost:3002` |
| Storyboard with real frames | `documentation/storyboard.md` |

The draft preview is a HyperFrames `-q draft` render with the watermark on. It is for review only, not the deliverable. The final render (H.264, AAC 48 kHz, delivery quality, watermark off) happens only after **APPROVED — RENDER FINAL VIDEO**.

## Quality control

| Check | Result |
|---|---|
| `hyperframes check` (lint, runtime, layout, motion, contrast, audio) | **Pass** — 0 errors |
| Remaining warnings | Photos are nested in timed `div`s (Studio shows them as one row each), and the watermark sits outside the safe zone on purpose. It is switched off for the final. |
| Missing assets | None |
| Broken animation | None (every scene seeks; snapshots checked at 25 instants) |
| Text overflow / safe zone | All copy inside the TikTok / Reels / Shorts safe area; minimum 28 px |
| Subtitle sync | Times from Whisper word timestamps (see `transcript.json`) |
| Audio | Score −14 LUFS / −1.4 dBFS peak; dialogue −17 LUFS / −2 dBFS; music ducked to 30 % under the voice |
| Studio preview | Starts and loads all 8 compositions; timeline 01:26 scrubs (`documentation/studio-preview.png`, kept local) |

Audio was **measured, not heard**: loudness, peaks and timing were checked with tools. Nobody has listened to the mix yet.

## Known limitations

1. **Source resolution is 360 × 640.** It is upscaled 3× with Lanczos and sharpening. It will look soft on a large screen and acceptable on a phone. Better: ask for the **original camera files** (the Drive files look like WhatsApp-compressed copies).
2. **Pak Su Den appears only in photos.** No video of him teaching was supplied. A 10–20 s clip of him demonstrating or speaking would raise the film a lot, and would give a real spoken hook.
3. **No spoken hook line** exists in the footage, so the hook is on-screen typography.
4. **No official logo file** was supplied, so the end card uses a text lockup.
5. **The music is an original synthesised score.** It is a strong temp track, but a licensed library track (see `music-selection.md`) will sound more produced.
6. **The participant's name "BENG"** comes from the file names and certificate and needs confirming. It is the `participantName` variable in `s3-masterclass`.
7. **The award claim** (Overall Winner, World Holistic Massage Championship Singapore 2025) was read from the poster in a photo and needs confirming.
8. **The coaching voice** in beng 12/14 is off camera. The speaker is unconfirmed, so no name is attached to it.

## Suggested improvements (client decisions)

- Supply original-resolution footage, the official logo (PNG/SVG), and any video of Pak Su Den speaking. With those, the hook becomes his own words.
- Choose the final music track (licensed), or approve the original score.
- Confirm the names and the award line.
- Optional: a 30 s cut for ads, and a 15 s cut (hook + climax + end card).

## To render the final after approval

1. Set `previewWatermark` to `false` (the variable on `index.html`).
2. Render: `npx hyperframes@0.9.94 render -q delivery --fps 30 -o exports/grandmaster-skill-signature-final.mp4` (H.264 + AAC 48 kHz).
3. Measure: `npx hyperframes audio exports/… --json`, and play it through once on a phone.

---

## FINAL RENDER — 25 Nov 2026 (after "APPROVED — RENDER FINAL VIDEO")

| File | Spec |
|---|---|
| `exports/grandmaster-skill-signature-FINAL-master.mp4` | H.264 High, 1080 × 1920, 30 fps, yuv420p, 13.4 Mbps, AAC-LC 48 kHz stereo, 86.0 s, 144 MB — HyperFrames `-q delivery` |
| `exports/grandmaster-skill-signature-FINAL-social.mp4` | Same picture re-encoded for social / WhatsApp: H.264 CRF 19, max 6 Mbps, AAC 192 kbps 48 kHz, faststart, 56 MB |

Measured on the master: −13.3 LUFS integrated, −1.0 dBFS peak, LRA 9.0 LU. Full decode with no errors. Watermark off. Frames checked every 4 s.
The video files are not in git (public repository).

The draft watermarked preview was stopped at 27 % when the approval arrived, so no complete preview MP4 exists. The client approved from the snapshot contact sheets.

---

## FINAL RENDER v2 — 25 Nov 2026 (client revision: logos, more energy, less "AI" sound, zoom in/out)

| File | Spec |
|---|---|
| `exports/grandmaster-skill-signature-FINAL-v2-master.mp4` | H.264 High, 1080 × 1920, 30 fps, 13.5 Mbps, AAC-LC 48 kHz stereo, 86.0 s, 145 MB — `-q delivery` (69 min render, software GL) |
| `exports/grandmaster-skill-signature-FINAL-v2-social.mp4` | CRF 19, max 6 Mbps, AAC 192 kbps, faststart, 57 MB |

Measured on the master: −13.0 LUFS integrated, −1.2 dBFS true peak, LRA 8.6 LU. Full decode clean. Contact sheet checked every 2 s.

What changed from v1:

1. **Official logos** (supplied by the client as images, cropped only, colours and shapes untouched, shown on white cards with a gold edge):
   Academy Pak Su Den shield on the title (12.2 s) and after the climax (72.2 s); the PAK SU DEN "Bukan Sekadar Rawatan" logo as the end-card hero (80 s) with the Academy shield below it. The text lockup and the separate big tagline were removed because the logo carries them.
2. **Zoom in / zoom out on every cut**: punch zoom-outs (1.16 → 1.0) on the beat, slow zoom-ins through the climax, logo zoom-ins with a gold ring shock-wave.
3. **Graphics and mentions**: the 2025 award stack (Overall Winner Singapore, Best Performance Singapore, 3rd Place Paris, 1st Place Malaysia — read from the poster in a photo, **to be confirmed**), the course topics from the class slide (Teknik, Persembahan, Adab Pertandingan), and seven technique call-outs (Precision, Touch, Leverage, Balance, Counter-weight, Control, Flow).
4. **Sound**: all synthetic whooshes and sparkles removed. Recorded mouse clicks and key presses with small pitch and level variation on each graphic; low impacts only on the big moments.
5. **Score v2**: still original and self-composed, but with humanised timing and velocity on the drums, hand claps on the backbeats, tom fills, darker and quieter braams, and strings in place of the synth choir.

## 60-second WhatsApp version — 26 Nov 2026

`exports/grandmaster-skill-signature-60s-WhatsApp.mp4`: 60.0 s exactly (fits a WhatsApp Status), 1080 × 1920, H.264 CRF 21 max 5 Mbps, AAC 160 kbps 48 kHz, faststart, 30 MB, −12.8 LUFS.
Cut from the v2 master with `tools/cut_60s.sh` (no re-render): 0–22 + 24–28 + 52–86. Splices are on bar downbeats and existing shot cuts.
Dropped: signature techniques 02–03 and the first coaching take (KNOWLEDGE BECOMES SKILL). Kept: both logos, the awards, the BENG credit, the climax and the end card.
