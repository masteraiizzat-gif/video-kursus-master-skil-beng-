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
