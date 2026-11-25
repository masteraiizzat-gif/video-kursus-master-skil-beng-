# Transcript — all footage

Engine: **faster-whisper large-v3**, Malay (`ms`), word-level timestamps. Two passes: (1) raw audio, (2) high-pass + denoise + loudness-normalised audio with voice-activity detection, to make sure no quiet speech was missed. Word timings in `transcripts/transcript.json`.

## Result

Only **two clips contain real dialogue** (beng 12 and beng 14), both short coaching cues from an **off-camera voice** (speaker not identified — could be Pak Su Den or the participant). beng 10 has one isolated "Ya". The other 12 raw clips and the reference video have **no speech** (room tone / music).

Consequence for the edit: there is **no long, powerful spoken line** from Pak Su Den in the material. The opening hook therefore uses on-screen kinetic typography ("SKILL IS LEARNED. / MASTERY IS BUILT."), and the real coaching voice is used where it is strongest — as authentic proof of knowledge transfer in Scene 5. No dialogue was invented, cloned or re-voiced.

## Dialogue

| File | Start | End | Dialog asal (BM) | English | Kepentingan | Cadangan penggunaan | Animation | SFX | Keputusan |
|---|---|---|---|---|---|---|---|---|---|
| beng 12 | 0.00 | 0.70 | Lagi, | Further. | Medium — live coaching cue | S5 Knowledge Transfer, J-cut under shot 22 (starts 43.6 s) | Caption fade-in | Music ducked to 30% | **KEEP** |
| beng 12 | 0.70 | 3.60 | Ok, tegak badan, | Straighten your body. | High — correction of posture (teacher-to-student) | S5, subtitle with 'Straighten' in gold | Keyword highlight | — | **KEEP** |
| beng 12 | 3.60 | 4.58 | badan tegak, | Keep it upright. | Medium — repetition, kept because it is the rhythm of real coaching | S5 | — | — | **KEEP** |
| beng 12 | 4.60 | 5.54 | lagi, | Further. | Medium | S5 | — | — | **KEEP** |
| beng 12 | 5.74 | 7.04 | ok, | Okay. | Low — acknowledgement | S5 | — | — | **KEEP (natural flow)** |
| beng 12 | 7.22 | 7.70 | turun. | Now down. | Medium — end of movement | S5, L-cut over B-roll shot 24 | — | — | **KEEP** |
| beng 14 | 0.24 | 1.16 | Relaks. | Relax. | High — care for the client | S5 | Caption | — | **KEEP** |
| beng 14 | 1.38 | 2.00 | Tinggi lagi. | Higher. | High — strongest single coaching word | S5, 'Higher.' in gold | Keyword highlight | — | **KEEP** |
| beng 14 | 2.00 | 3.36 | Haa. | That's it. | Medium — positive confirmation (genuine reaction) | S5 | — | — | **KEEP** |
| beng 14 | 4.14 | 4.84 | Ok, | Okay. | Low | S5 | — | — | **KEEP** |
| beng 14 | 4.84 | 7.28 | lepas tu, turunkan dia. | Then bring it down. | High — closes the knowledge-transfer beat | S5, 'bring it down' in gold | Keyword highlight | Music swells back at 59.9 s | **KEEP** |
| beng 10 | 1.50 | 2.90 | Ya. | Yes. | Low — isolated, off-mic | Not used (falls in the trimmed 0–6.5 s) | — | — | **REMOVE** |

## Analysis

| Category | Finding |
|---|---|
| Most impactful line | "Tinggi lagi." — *Higher.* (beng 14, 1.38 s) |
| Hook candidate from real audio | None strong enough for 0–4 s (all cues are 1–2 words, off-mic). Typography hook chosen. |
| Knowledge & experience | Not spoken in the footage |
| Technique sharing | beng 12 & 14 posture and range cues |
| Motivation | Not spoken in the footage |
| Interaction | Coach → performer/client cues (beng 12, 14) |
| Reactions | "Haa." confirmation (beng 14, 2.0 s) |
| Repetition | "tegak badan, badan tegak" — kept: it is the cadence of real coaching and lasts 2 s |
| Awkward pauses | 3.36–4.14 s in beng 14 — covered by the music bed (still inside the shot) |
| Speech errors | None |
| Background noise | Fan / room hiss on every clip (−31 to −34 dB) — removed by muting native audio; dialogue clips denoised |

## Rejected Whisper output

Whisper produced "Terima kasih kerana menonton!" ("Thanks for watching!") on silent/music-only clips with no-speech probability 0.86–0.98. This is a known hallucination, **not real dialogue**, and was discarded:

- Beng_7_-1 0.4–3.0 s (no_speech 0.95)
- Pak_Su_Den 0.0–30.0 s (no_speech 0.98)
- Pak_Su_Den 30.0–34.2 s (no_speech 0.4)
- beng_13 0.0–8.4 s (no_speech 0.95)
- beng_15 0.0–5.9 s (no_speech 0.95)
- beng_16 0.0–16.3 s (no_speech 0.92)
- beng_17 0.0–5.1 s (no_speech 0.95)
- beng_18 0.0–18.7 s (no_speech 0.93)
- beng_19 1.2–15.7 s (no_speech 0.97)
- beng_20 0.0–2.7 s (no_speech 0.98)
- beng_21 0.0–3.7 s (no_speech 0.97)
- beng_22 0.0–3.4 s (no_speech 0.97)
- beng_8 0.0–15.4 s (no_speech 0.94)
- beng_9 0.0–15.0 s (no_speech 0.89)
