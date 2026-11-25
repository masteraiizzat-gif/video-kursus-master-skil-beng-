# Asset Inventory — Grandmaster Skill Signature (Pak Su Den)

Source: Google Drive folder **"VIDEO KURSUS MASTER SKILL PSD"** (`1YlMl-RPFJ8VyTFEW_RfWrSAhNLamp2mL`).
Checked 25 Nov 2026. 19 files. Every file was downloaded in full, probed with FFprobe and decoded end to end.
Original files are untouched (Drive was read only; local copies in `source/` and `reference/`).

## Access

| Check | Result |
|---|---|
| Drive connector listing | OK — 19 files |
| Download (`drive.usercontent.google.com`) | OK — all 19 files, byte sizes match Drive metadata |
| Files over 10 MB | None (largest is 5.6 MB) |
| Blocked / unreadable files | None |
| Duplicates (md5) | None |
| Corrupt files | None (all decode without errors) |

## Video

All phone footage: **360 × 640 (9:16)**, H.264, ~59–60 fps, AAC 48 kHz stereo.

| File | Role | Duration | fps | Audio | Speech | Content | Verdict |
|---|---|---|---|---|---|---|---|
| `Pak Su Den.mp4` | **REFERENCE** | 34.45 s | 30 | AAC 44.1k | none (music only) | "Personal Coaching by Pak Su Den — Delivery by Mr Kelvin, Indonesia" | Reference only — not used in the edit |
| `Beng 7 -1.mp4` | raw | 7.46 s | 59 | yes | none | Frontal, two-palm press on the back; face visible | **KEEP** — hook & hero |
| `beng 8.mp4` | raw | 15.90 s | 59 | yes | none | Leg stretch, therapist steps onto the table, diagonal pull | **KEEP** |
| `beng 9.mp4` | raw | 15.41 s | 59 | yes | none | Standing on table, lean-back pull; vertical crossed-leg hold | **KEEP** |
| `beng 10.mp4` | raw | 23.04 s | 59 | yes | "Ya" (1.5 s) | Crossed-arm chest-opening stretch from the head end — most graphic shape | **KEEP** (0–6.5 s trimmed) |
| `beng 12.mp4` | raw | 8.18 s | 59 | yes | **yes — coaching** | Seated arm hold; off-camera voice coaching | **KEEP** — knowledge transfer |
| `beng 13.mp4` | raw | 9.96 s | 59 | yes | none | Side-lying hip/leg work, blue wall, face visible | **KEEP** |
| `beng 14.mp4` | raw | 9.50 s | 59 | yes | **yes — coaching** | Arm stretch from behind; voice coaching | **KEEP** — knowledge transfer |
| `beng 15.mp4` | raw | 9.05 s | 59 | yes | none | Seated on floor, wrist/arm technique | **KEEP** |
| `beng 16.mp4` | raw | 17.00 s | 59 | yes | none | Kneeling on table, twist / arm work facing camera | **KEEP** |
| `beng 17.mp4` | raw | 6.49 s | 59 | yes | none | Low angle, standing on the table — stance | **KEEP** |
| `beng 18.mp4` | raw | 19.29 s | 59 | yes | none | Close-up palpation of the back, blue wall | **KEEP** (2 × 2 s) |
| `beng 19.mp4` | raw | 16.34 s | 59 | yes | none | Close-up hands on back, expressive face | **KEEP** (2 × 2 s) |
| `beng 20.mp4` | raw | 3.44 s | 59 | yes | none | Camera dropped — floor/carpet for 2.6 s | **REMOVE** |
| `beng 21.mp4` | raw | 7.44 s | 60 (59.94) | yes | none | 0–3.6 s floor + blur; 3.7–6.2 s palm work | **TRIM** — 2 s used |
| `beng 22.mp4` | raw | 10.85 s | 59 | yes | none | Lunge, leg over shoulder; intense face | **KEEP** |

Missing numbers in the series (`beng 1–6`, `beng 11`) are not in the folder.

## Photos

| File | Size | Content | Use |
|---|---|---|---|
| `gambar beng 1.jpeg` | 576 × 1280 | **Pak Su Den (pink polo)** handing a certificate to the participant (batik shirt). Behind them: the academy's award poster. Certificate reads "…SIGNATURE PAK SU DEN — Professional Massage Training Course", name beginning "BENG…" | Legacy scene |
| `Gambar Beng 2.jpeg` | 960 × 432 | Pak Su Den teaching; projector slide "MASTERCLASS SIGNATURE — URUTAN TRADISIONAL PAK SU DEN — Teknik • Persembahan • Adab Pertandingan" | The Master scene |
| `Gambar beng 3.jpeg` | 960 × 432 | Wider view of the same class: Pak Su Den and the participant | The Master scene |

## Logo and graphics

**No logo file was supplied.** The end card uses a typographic lockup (text only). No logo was designed or redrawn. When the official logo file (PNG/SVG, transparent) is supplied it replaces `#s7-e2` in `compositions/s7-legacy.html`.

## Important identity finding

The man performing every technique in all 15 videos is **the participant (batik shirt)**, not Pak Su Den.
Pak Su Den (pink polo, older) appears **only in the three photos**. This matches the reference video's credit line ("Personal Coaching by Pak Su Den — Delivery by Mr Kelvin"). The edit is built on this: *the master teaches (photos) → the participant performs (video) → the master certifies (photo)*. The participant's name "BENG" is taken from the file names and the certificate and **needs confirmation** (it is a Studio variable: `participantName`).

## Claims and where they come from

| On-screen claim | Source | Status |
|---|---|---|
| PAK SU DEN | Projector slide, certificate, brief | Verified |
| Founder • Therapist • Trainer | Brief; academy carries his name | From the brief — please confirm |
| Overall Winner — World Holistic Massage Championship, Singapore 2025 | Plaque on the award poster in `gambar beng 1.jpeg` | Read from the poster — please confirm |
| Masterclass Signature / Urutan Tradisional Pak Su Den | Projector slide | Verified |
| 25 November 2026 · Permas Jaya, Johor, Malaysia | Brief | From the brief |
| "International Massage Champion" | Brief only | **Not shown** — poster lists international awards but the exact title isn't printed |

## Derived assets (made for the edit)

| Path | What | How |
|---|---|---|
| `assets/footage/*.mp4` | 14 conformed clips, 1080 × 1920, 60 fps CFR | FFmpeg: vidstab (2-pass), hqdn3d, Lanczos ×3, CAS sharpen, BT.709 tags |
| `assets/photos/*-plate.jpg` | Blurred, darkened backgrounds for the photo cards | FFmpeg gblur |
| `assets/audio/dialogue-beng_12.wav`, `dialogue-beng_14.wav` | Cleaned coaching audio | High-pass 95 Hz, FFT denoise, EQ, compressor, −17 LUFS |
| `assets/audio/score-the-art-of-mastery.wav` | Original score (see music-selection.md) | `music/compose_score.py` |
| `assets/sfx/*.mp3` | 6 sound effects | HyperFrames bundled library, Pixabay Content License |
| `assets/fonts/*.ttf` | Bebas Neue, Anton, Montserrat, Inter, Cinzel | Google Fonts, SIL Open Font License |
