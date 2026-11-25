# GRANDMASTER SKILL SIGNATURE — PAK SU DEN
### THE ART OF MASTERY · Cinematic masterclass film (9:16, 86 s) — HyperFrames project

**Status: PREVIEW ONLY.** The final MP4 is not rendered. It waits for the client's reply:
`APPROVED — RENDER FINAL VIDEO`. (`npm run render` is locked on purpose.)

## Open the preview on your computer

Needs Node.js 22+, FFmpeg and Chrome.

```bash
git clone https://github.com/masteraiizzat-gif/video-kursus-master-skil-beng-.git
```

```bash
cd video-kursus-master-skil-beng-/grandmaster-skill-signature
```

The client media is not in git (the repository is public). Download it from the Drive folder and prepare it (stabilise, denoise, upscale to 1080 × 1920, 60 fps — about 10 minutes):

```bash
bash tools/fetch_media.sh
```

```bash
npx hyperframes@0.9.94 preview
```

The Studio opens at `http://localhost:3002`: play, scrub the timeline, edit text and timing, toggle the `previewWatermark` variable.

## Layout

| Path | What |
|---|---|
| `index.html` | Root composition: picture edit (38 video shots, 3 photos), music, coaching voice, SFX, scene hosts |
| `compositions/s1-hook … s7-legacy.html` | One graphics scene per story beat (GSAP, seekable) |
| `compositions/captions.html` | English subtitles (+ original Malay) |
| `documentation/` | asset-inventory, reference-analysis, transcript, editing-plan, edit-decision-list.json, storyboard, music-selection, subtitles-en.srt, preview-notes |
| `music/compose_score.py` | Generates the original score |
| `tools/build_root.py` | Scaffolds `index.html` from the EDL (`tools/rebuild.sh` also re-applies the grade) |
| `tools/fetch_media.sh`, `tools/conform_footage.sh` | Media download and FFmpeg normalisation |
| `tools/transcribe_pass1.py`, `transcribe_pass2.py` | faster-whisper large-v3 Malay transcription |
| `graphics/grade/*.json` | Colour grades applied with `hyperframes media-treatment` |

## Licences

- Score: original work for this project (`music/`).
- SFX: HyperFrames bundled library, Pixabay Content License (`assets/sfx/CREDITS.md`).
- Fonts: Bebas Neue, Anton, Montserrat, Inter — SIL Open Font License (`assets/fonts/OFL.txt`).
- GSAP 3.15 (`assets/gsap.min.js`) — GreenSock standard licence (free, including commercial use).
- Footage and photos: property of the client; not redistributed here.
