# Music Selection

## What happened

The brief asks for licensed Epic Hybrid Orchestral music. From this environment the music libraries are **blocked by the network policy** (tested: Pixabay, Freesound, Openverse, Incompetech, archive.org → proxy 403). HeyGen's music catalogue needs an account sign-in that this session doesn't have. AI music generators that run locally (MusicGen) use weights licensed **CC-BY-NC** (non-commercial) — not acceptable for a commercial promo.

So the preview uses an **original score composed for this film** — every sound synthesised in code (`music/compose_score.py`), no samples, no third-party audio. It is **owned outright and cleared for commercial and social use**.

Honest caveat: it was measured, not heard. I verified structure, loudness and spectrum (spectrogram in `music/score-viz.png`), not musical taste. A synthesised score is a strong temp track but will not sound like a professionally produced library track. **Option 1 below is the recommended final.**

## Preview track (in use) — "The Art of Mastery" (original)

| | |
|---|---|
| File | `assets/audio/score-the-art-of-mastery.wav` (48 kHz stereo, 88 s) |
| Tempo / key | 120 BPM half-time feel, D minor → D major resolution |
| Loudness | −14 LUFS integrated, −1.4 dBFS peak |
| Licence | Original work for this project — no restrictions |

| Section | Time | Music | Loudness |
|---|---|---|---|
| Hook | 0–4 | Sub boom + braam, taiko roll, reverse swell | −13.9 LUFS |
| The Master | 4–12 | Controlled pulse: sub-bass 8ths, soft taiko, pads | −18.6 |
| Masterclass | 12–24 | String ostinato enters, hi-ticks | −14.8 |
| Signature | 24–44 | Full percussion, snare backbeat, braams every 4 bars | −12.4 |
| Knowledge | 44–60 | Drums thin out, emotional lead line, riser + snare roll into 60 (ducked to 30% under the voice) | −15.6 |
| Climax | 60–74 | Drop: boom, choir, double-time taiko, brass braams | −10.4 |
| Legacy | 74–86 | D-major resolution, end hit at 80 (logo), long tail | −18.1 |

## Recommended licensed alternatives (for the final)

Search terms chosen for the film's feel and tempo (not its subject). All three libraries license commercial + social use under a subscription; the track must be cut to the 120 BPM grid (or the edit re-snapped with `hyperframes beats`).

| # | Library | Search | Why |
|---|---|---|---|
| 1 | Artlist / Musicbed | "epic hybrid trailer percussion 120 bpm rise drop no vocals" | Best production quality for the "international championship" feel |
| 2 | Epidemic Sound | "cinematic hybrid orchestral emotional build epic drop" | Ships stems — can drop the drums under the coaching voice |
| 3 | Envato Elements | "epic inspiring trailer taiko strings 2 minute" | Cheapest; many tracks have 60 s / 90 s edits |

To swap: copy the file into `assets/audio/`, change `src` on `#music-score` in `index.html`, run `npx hyperframes beats --json` and nudge the scene boundaries to the new bar lines.

## Sound effects (in use)

HyperFrames bundled library — **Pixabay Content License** (commercial use, no attribution required). See `assets/sfx/CREDITS.md`.

| Time | Effect | Cause on screen |
|---|---|---|
| 1.87 | whoosh | "MASTERY" slam |
| 3.85 | whoosh (0.85×) | flash into the master |
| 12.62 | sparkle | gold light sweep on the title |
| 23.87 / 29.87 / 36.85 | whoosh variants (rotated rate) | chapter cuts 01 / 02 / 03 |
| 59.96 | impact-bass-1 | the drop |
| 63.87 / 67.87 | whoosh variants | climax lines |
| 71.53 | whoosh-cinematic (peak at 74.0) | flash into the certificate |
| 79.92 + 80.45 | impact-bass-2 + sparkle | logo lockup reveal |

Native room ambience is muted everywhere except the two coaching clips (it was fan hiss, not useful atmosphere).
