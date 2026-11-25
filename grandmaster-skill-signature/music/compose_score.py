#!/usr/bin/env python3
"""
"THE ART OF MASTERY" — original score for Grandmaster Skill Signature (Pak Su Den).
Epic Hybrid Orchestral x Cinematic Trailer x Powerful Percussion.

Composed procedurally for this project (no samples, no third-party audio):
every sound is synthesised here, so the track is 100% owned by the project and
cleared for commercial / social-media use.

Grid: 120 BPM, 4/4, one bar = 2.0 s. Sections land on the edit's scene seams:
  0-4   Hook        dark tension, boom + braam
  4-12  The Master  controlled pulse
  12-24 Masterclass ostinato enters
  24-44 Signature   full percussion, braams
  44-60 Knowledge   emotional strings, drums thin out, riser into 60
  60-74 Climax      epic drop
  74-86 Legacy      resolution to D major, end hit at 80

Usage: python3 compose_score.py out.wav [variant]
variant: "A" (default, 120 bpm D minor)
"""
import sys
import numpy as np
from scipy import signal

SR = 48000
BAR = 2.0
TOTAL = 88.0
N = int(TOTAL * SR)
rng = np.random.default_rng(20261125)  # seeded: deterministic

L = np.zeros(N)
R = np.zeros(N)
BUS_REV = np.zeros((2, N))  # reverb send


def note(name):
    names = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6,
             "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}
    p, o = name[:-1], int(name[-1])
    midi = 12 * (o + 1) + names[p]
    return 440.0 * 2 ** ((midi - 69) / 12)


def place(sig, t0, gain=1.0, pan=0.0, send=0.0):
    i0 = int(t0 * SR)
    if i0 >= N:
        return
    if sig.ndim == 1:
        sl, sr_ = sig, sig
    else:
        sl, sr_ = sig[0], sig[1]
    n = min(len(sl), N - i0)
    gl = gain * np.cos((pan + 1) * np.pi / 4) * np.sqrt(2)
    gr = gain * np.sin((pan + 1) * np.pi / 4) * np.sqrt(2)
    L[i0:i0 + n] += sl[:n] * gl
    R[i0:i0 + n] += sr_[:n] * gr
    if send:
        BUS_REV[0, i0:i0 + n] += sl[:n] * gl * send
        BUS_REV[1, i0:i0 + n] += sr_[:n] * gr * send


def tt(dur):
    return np.arange(int(dur * SR)) / SR


def lp(x, fc, order=2):
    sos = signal.butter(order, min(fc, SR / 2 * 0.95), "low", fs=SR, output="sos")
    return signal.sosfilt(sos, x)


def hp(x, fc, order=2):
    sos = signal.butter(order, fc, "high", fs=SR, output="sos")
    return signal.sosfilt(sos, x)


def bp(x, f1, f2, order=2):
    sos = signal.butter(order, [f1, f2], "band", fs=SR, output="sos")
    return signal.sosfilt(sos, x)


def saw(f, dur, maxf=6000.0, detune_cents=0.0, phase=0.0):
    t = tt(dur)
    f = f * 2 ** (detune_cents / 1200)
    nh = max(1, int(maxf / f))
    out = np.zeros_like(t)
    for h in range(1, nh + 1):
        out += np.sin(2 * np.pi * f * h * t + phase * h) / h
    return out * (2 / np.pi)


def env_adsr(dur, a, d, s, r):
    n = int(dur * SR)
    e = np.ones(n) * s
    na, nd, nr = int(a * SR), int(d * SR), int(r * SR)
    na = min(na, n)
    e[:na] = np.linspace(0, 1, na, endpoint=False) if na else e[:na]
    if nd and na + nd < n:
        e[na:na + nd] = np.linspace(1, s, nd)
    if nr and nr < n:
        e[-nr:] *= np.linspace(1, 0, nr) ** 1.5
    return e


# ---------------------------------------------------------------- instruments
def boom(dur=3.5, f0=58, f1=27):
    t = tt(dur)
    f = f1 + (f0 - f1) * np.exp(-t / 0.35)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t / 1.3)
    click = lp(rng.standard_normal(len(t)), 1800) * np.exp(-t / 0.018) * 0.6
    rumble = lp(rng.standard_normal(len(t)), 140, 4) * np.exp(-t / 0.9) * 0.9
    x = np.tanh(1.6 * (body + click + rumble))
    return x


def taiko(vel=1.0, dur=1.2):
    t = tt(dur)
    f = 52 + 95 * np.exp(-t / 0.025)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t / 0.33)
    skin = lp(rng.standard_normal(len(t)), 900) * np.exp(-t / 0.045) * 0.55
    x = np.tanh(1.4 * (body + skin)) * vel
    return x


def snare(vel=1.0, dur=0.9):
    t = tt(dur)
    nz = bp(rng.standard_normal(len(t)), 900, 7000) * np.exp(-t / 0.13)
    tone = np.sin(2 * np.pi * 185 * t) * np.exp(-t / 0.07) * 0.6
    return (nz * 0.8 + tone) * vel


def tick(vel=1.0):
    t = tt(0.12)
    return hp(rng.standard_normal(len(t)), 7000) * np.exp(-t / 0.018) * vel


def braam(root, dur=3.2, vel=1.0):
    t = tt(dur)
    x = np.zeros(len(t))
    for f, g in ((root / 2, 0.9), (root, 0.8), (root * 1.5, 0.45), (root * 2, 0.3)):
        for dc in (-9, 0, 8):
            x += saw(f, dur, maxf=5000, detune_cents=dc) * g / 3
    cutoff_env = 180 + 2600 * np.exp(-((t - 0.25) / 0.55) ** 2) * (t < 2.5) + 300 * np.exp(-t / 2)
    # time-varying lowpass via short blocks
    out = np.zeros_like(x)
    blk = 1024
    zi = None
    for i in range(0, len(x), blk):
        fc = float(np.clip(cutoff_env[i], 80, 9000))
        sos = signal.butter(2, fc, "low", fs=SR, output="sos")
        if zi is None:
            zi = signal.sosfilt_zi(sos) * 0
        out[i:i + blk], zi = signal.sosfilt(sos, x[i:i + blk], zi=zi)
    e = env_adsr(dur, 0.04, 0.6, 0.55, 1.4)
    return np.tanh(2.2 * out * e) * 0.8 * vel


def pad_chord(freqs, dur, bright=1600, vel=1.0, a=0.7, r=1.0):
    x = np.zeros((2, int(dur * SR)))
    for k, f in enumerate(freqs):
        for ch, dc in enumerate((-7, 7)):
            v = saw(f, dur, maxf=4000, detune_cents=dc + (k % 2) * 3, phase=0.3 * k + ch)
            x[ch] += v
    x /= max(1, len(freqs))
    x[0], x[1] = lp(x[0], bright), lp(x[1], bright)
    e = env_adsr(dur, a, 0.3, 0.9, r)
    return x * e * vel


def string_note(f, dur, vel=1.0, bright=2600):
    v = saw(f, dur, maxf=5000) * 0.6 + saw(f, dur, maxf=5000, detune_cents=6) * 0.4
    v = lp(v, bright)
    e = env_adsr(dur, 0.004, 0.09, 0.25, min(0.05, dur * 0.4))
    return v * e * vel


def lead(f, dur, vel=1.0):
    t = tt(dur)
    vib = 1 + 0.006 * np.sin(2 * np.pi * 5.2 * t) * np.clip((t - 0.25) / 0.4, 0, 1)
    ph = 2 * np.pi * np.cumsum(f * vib) / SR
    x = np.zeros_like(t)
    for h in range(1, 14):
        x += np.sin(h * ph) / (h ** 1.15)
    x = lp(x, 3200)
    e = env_adsr(dur, 0.22, 0.2, 0.85, min(0.6, dur * 0.4))
    return x * e * vel * 0.5


def choir(freqs, dur, vel=1.0):
    t = tt(dur)
    x = np.zeros((2, len(t)))
    for k, f in enumerate(freqs):
        for ch in range(2):
            vib = 1 + 0.004 * np.sin(2 * np.pi * (4.6 + 0.3 * ch + 0.2 * k) * t + k)
            ph = 2 * np.pi * np.cumsum(f * vib) / SR
            v = np.sin(ph) + 0.35 * np.sin(2 * ph) + 0.18 * np.sin(3 * ph) + 0.1 * np.sin(4 * ph)
            x[ch] += bp(v, 250, 2800, 1)
    x /= len(freqs)
    return x * env_adsr(dur, 0.9, 0.3, 0.9, 1.2) * vel


def pluck(f, dur=2.5, vel=1.0):
    t = tt(dur)
    x = np.zeros_like(t)
    for h in range(1, 9):
        x += np.sin(2 * np.pi * f * h * t) * np.exp(-t * (1.6 + 1.2 * h)) / h
    return x * vel


def riser(dur):
    t = tt(dur)
    p = t / dur
    nz = rng.standard_normal(len(t))
    out = np.zeros_like(t)
    blk = 2048
    zi = None
    for i in range(0, len(t), blk):
        fc1 = 250 + 7000 * p[i] ** 2
        sos = signal.butter(2, [fc1, min(fc1 * 2.2, 20000)], "band", fs=SR, output="sos")
        if zi is None:
            zi = signal.sosfilt_zi(sos) * 0
        out[i:i + blk], zi = signal.sosfilt(sos, nz[i:i + blk], zi=zi)
    f = 180 * 2 ** (p * 2.6)
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.25
    return (out * 1.4 + tone) * p ** 2.2


def reverse_swell(dur=1.6):
    t = tt(dur)
    nz = bp(rng.standard_normal(len(t)), 400, 9000)
    return nz * (t / dur) ** 3 * 0.9


def sub_pulse(f, dur=0.25, vel=1.0):
    t = tt(dur)
    return np.sin(2 * np.pi * f * t) * np.exp(-t / 0.09) * vel


# ---------------------------------------------------------------- harmony
CH = {
    "Dm": ["D3", "F3", "A3", "D4"],
    "Bb": ["Bb2", "F3", "Bb3", "D4"],
    "F": ["F2", "C3", "F3", "A3"],
    "C": ["C3", "G3", "C4", "E4"],
    "Gm": ["G2", "D3", "G3", "Bb3"],
    "A": ["A2", "E3", "A3", "C#4"],
    "Dsus": ["D3", "G3", "A3", "D4"],
    "D": ["D3", "F#3", "A3", "D4"],
}
ROOT = {"Dm": "D2", "Bb": "Bb1", "F": "F2", "C": "C2", "Gm": "G1", "A": "A1", "Dsus": "D2", "D": "D2"}
OST = {  # 16th-note ostinato pitch sets
    "Dm": ["D3", "D3", "A3", "D3", "F3", "D3", "A3", "D4"],
    "Bb": ["Bb2", "Bb2", "F3", "Bb2", "D3", "Bb2", "F3", "Bb3"],
    "F": ["F2", "F2", "C3", "F2", "A2", "F2", "C3", "F3"],
    "C": ["C3", "C3", "G3", "C3", "E3", "C3", "G3", "C4"],
    "Gm": ["G2", "G2", "D3", "G2", "Bb2", "G2", "D3", "G3"],
    "A": ["A2", "A2", "E3", "A2", "C#3", "A2", "E3", "A3"],
}
PROG = ["Dm", "Bb", "F", "C"]


def bar_t(b, beat=0.0):
    return b * BAR + beat * 0.5


def chord_for(b):
    if 22 <= b <= 29:
        return ["Bb", "F", "C", "Dm", "Bb", "F", "Gm", "A"][b - 22]
    if 37 <= b:
        return ["Bb", "C", "Dsus", "D", "D", "D"][min(b - 37, 5)]
    return PROG[b % 4]


# ---------------------------------------------------------------- arrangement
def ostinato(b, vel, octave=1.0, bright=2600):
    ch = chord_for(b)
    pat = OST.get(ch, OST["Dm"])
    for i in range(16):
        f = note(pat[i % 8]) * octave
        accent = 1.0 if i % 4 == 0 else 0.72
        place(string_note(f, 0.13, vel * accent, bright), bar_t(b) + i * 0.125,
              gain=0.55, pan=(-0.35 if i % 2 else 0.35), send=0.15)


def pad(b, vel, bright=1500, octave=1.0, bars=1):
    ch = chord_for(b)
    fr = [note(n) * octave for n in CH[ch]]
    place(pad_chord(fr, BAR * bars + 0.9, bright, vel), bar_t(b), gain=0.5, send=0.35)


def bass(b, vel):
    f = note(ROOT[chord_for(b)])
    for i in range(8):
        place(sub_pulse(f, 0.24, vel * (1 if i % 2 == 0 else 0.6)), bar_t(b) + i * 0.25, gain=0.9)


# HOOK 0-4
place(boom(), 0.0, gain=1.0, send=0.25)
place(braam(note("D2"), 3.4, 1.0), 0.0, gain=0.55, send=0.4)
place(pad_chord([note("D2"), note("A2"), note("D3")], 4.2, 600, 0.8, a=0.05, r=1.2), 0.0, gain=0.5, send=0.3)
for tb, v in ((1.0, 0.7), (1.5, 0.9)):
    place(taiko(v), tb, gain=0.8, send=0.3)
place(boom(2.6, 62, 30), 2.0, gain=0.85, send=0.3)
place(braam(note("F2"), 2.0, 0.6), 2.0, gain=0.35, send=0.4)
for tb, v in ((2.75, 0.5), (3.0, 0.65), (3.25, 0.8), (3.5, 0.95), (3.625, 0.8), (3.75, 1.0)):
    place(taiko(v), tb, gain=0.75, send=0.3)
place(reverse_swell(1.2), 2.8, gain=0.4, send=0.3)

# THE MASTER 4-12 (bars 2-5)
for b in range(2, 6):
    pad(b, 0.55, 900)
    bass(b, 0.5)
    place(taiko(0.55), bar_t(b), gain=0.7, send=0.3)
    place(taiko(0.35), bar_t(b, 2.5), gain=0.6, send=0.3)
place(pluck(note("D4"), 3.0, 0.4), 4.0, gain=0.4, pan=-0.2, send=0.5)
place(pluck(note("A4"), 3.0, 0.35), 8.0, gain=0.4, pan=0.2, send=0.5)
for i, v in enumerate((0.4, 0.5, 0.6, 0.8)):
    place(taiko(v), 11.0 + i * 0.25, gain=0.6, send=0.3)

# MASTERCLASS 12-24 (bars 6-11)
place(boom(2.8, 55, 28), 12.0, gain=0.7, send=0.3)
for b in range(6, 12):
    pad(b, 0.6, 1300)
    bass(b, 0.6)
    ostinato(b, 0.5 + 0.05 * (b - 6))
    place(taiko(0.8), bar_t(b), gain=0.75, send=0.3)
    place(taiko(0.6), bar_t(b, 2), gain=0.7, send=0.3)
    for i in range(8):
        place(tick(0.25 if i % 2 else 0.4), bar_t(b) + i * 0.25, gain=0.35, pan=0.3)
place(reverse_swell(1.6), 22.4, gain=0.55, send=0.3)
for i in range(8):
    place(snare(0.25 + 0.08 * i), 23.0 + i * 0.125, gain=0.35, send=0.4)

# SIGNATURE 24-44 (bars 12-21)
place(boom(), 24.0, gain=0.95, send=0.3)
for b in range(12, 22):
    pad(b, 0.62, 1700)
    bass(b, 0.75)
    ostinato(b, 0.7, octave=2.0 if b >= 16 else 1.0, bright=3200)
    for beat, v in ((0, 1.0), (1.5, 0.6), (2, 0.85), (3, 0.5), (3.5, 0.7)):
        place(taiko(v), bar_t(b, beat), gain=0.8, send=0.3)
    place(snare(0.85), bar_t(b, 2), gain=0.55, send=0.5)
    for i in range(16):
        place(tick(0.35 if i % 4 == 0 else 0.18), bar_t(b) + i * 0.125, gain=0.3, pan=-0.3 if i % 2 else 0.3)
    if b in (12, 14, 16, 18, 20):
        place(braam(note(ROOT[chord_for(b)]) * 2, 2.6, 0.7), bar_t(b), gain=0.38, send=0.4)
place(reverse_swell(1.6), 42.4, gain=0.6, send=0.3)

# KNOWLEDGE 44-60 (bars 22-29)
place(boom(3.0, 50, 27), 44.0, gain=0.7, send=0.4)
for b in range(22, 30):
    pad(b, 0.55 + 0.04 * (b - 22), 1200 + 180 * (b - 22))
    if b >= 24:
        bass(b, 0.35 + 0.05 * (b - 24))
    place(taiko(0.45 + 0.05 * (b - 22)), bar_t(b), gain=0.65, send=0.35)
    if b >= 26:
        ostinato(b, 0.35 + 0.08 * (b - 26), octave=1.0, bright=2400)
        place(taiko(0.4 + 0.05 * (b - 26)), bar_t(b, 2), gain=0.6, send=0.35)
melody = [("A4", 44.0, 1.5), ("F4", 45.5, 0.5), ("G4", 46.0, 2.0), ("A4", 48.0, 1.0), ("C5", 49.0, 1.0),
          ("A4", 50.0, 2.0), ("G4", 52.0, 1.5), ("F4", 53.5, 0.5), ("E4", 54.0, 2.0),
          ("D4", 56.0, 1.0), ("F4", 57.0, 1.0), ("A4", 58.0, 1.0), ("C#5", 59.0, 1.0)]
for n_, t0, d in melody:
    place(lead(note(n_), d + 0.35, 0.8), t0, gain=0.45, pan=0.1, send=0.55)
place(riser(4.0), 56.0, gain=0.55, send=0.3)
for i in range(16):
    place(snare(0.2 + 0.05 * i), 58.0 + i * 0.125, gain=0.4, send=0.4)

# CLIMAX 60-74 (bars 30-36)
place(boom(4.0, 60, 26), 60.0, gain=1.0, send=0.35)
for b in range(30, 37):
    pad(b, 0.7, 2400, octave=1.0)
    place(choir([note(n) * 2 for n in CH[chord_for(b)][1:]], BAR + 0.8, 0.55), bar_t(b), gain=0.38, send=0.5)
    bass(b, 0.9)
    ostinato(b, 0.8, octave=2.0, bright=3600)
    for beat in range(8):
        v = 1.0 if beat % 2 == 0 else 0.65
        place(taiko(v), bar_t(b, beat * 0.5), gain=0.85, send=0.3)
    place(snare(0.95), bar_t(b, 1), gain=0.6, send=0.5)
    place(snare(0.95), bar_t(b, 3), gain=0.6, send=0.5)
    for i in range(16):
        place(tick(0.35 if i % 2 == 0 else 0.2), bar_t(b) + i * 0.125, gain=0.32, pan=-0.3 if i % 2 else 0.3)
    if b % 2 == 0:
        place(braam(note(ROOT[chord_for(b)]) * 2, 2.8, 0.95), bar_t(b), gain=0.48, send=0.4)
for i in range(8):
    place(taiko(0.6 + 0.05 * i), 72.0 + i * 0.25, gain=0.8, send=0.3)
place(reverse_swell(1.4), 72.6, gain=0.6, send=0.3)

# LEGACY 74-86 (bars 37-42)
place(boom(4.5, 55, 25), 74.0, gain=0.95, send=0.45)
place(braam(note("D2"), 3.6, 0.8), 74.0, gain=0.4, send=0.5)
for b in range(37, 43):
    pad(b, 0.6 - 0.04 * (b - 37), 1500, bars=1)
    if b < 40:
        place(taiko(0.45), bar_t(b), gain=0.6, send=0.4)
place(choir([note("D4"), note("F#4"), note("A4")], 10.0, 0.6), 76.0, gain=0.4, send=0.6)
for n_, t0, d in (("A4", 74.5, 1.5), ("B4", 76.0, 1.0), ("C#5", 77.0, 1.0), ("D5", 78.0, 3.5)):
    place(lead(note(n_), d + 0.4, 0.75), t0, gain=0.42, send=0.6)
place(boom(5.0, 52, 24), 80.0, gain=0.9, send=0.5)
for n_, t0 in (("D5", 80.0), ("A4", 80.5), ("F#4", 81.0), ("D4", 81.5), ("A3", 82.5)):
    place(pluck(note(n_), 3.5, 0.5), t0, gain=0.4, pan=0.15, send=0.6)
place(pad_chord([note(n) for n in ("D2", "A2", "D3", "F#3", "A3")], 7.0, 1100, 0.8, a=0.3, r=4.0), 80.0, gain=0.5, send=0.5)

# ---------------------------------------------------------------- reverb + master
def make_ir(dur=2.8, seed=7):
    r = np.random.default_rng(seed)
    t = tt(dur)
    ir = r.standard_normal(len(t)) * np.exp(-t / 0.75)
    ir = lp(ir, 6000)
    ir[: int(0.012 * SR)] *= np.linspace(0, 1, int(0.012 * SR))
    return ir / np.sqrt(np.sum(ir ** 2))


irL, irR = make_ir(seed=7), make_ir(seed=11)
revL = signal.fftconvolve(BUS_REV[0], irL)[:N]
revR = signal.fftconvolve(BUS_REV[1], irR)[:N]
L += revL * 0.55
R += revR * 0.55

mix = np.vstack([L, R])
mix = np.vstack([hp(mix[0], 28, 2), hp(mix[1], 28, 2)])
# gentle glue: soft-clip after level normalisation
mix /= np.max(np.abs(mix)) + 1e-9
mix = np.tanh(1.5 * mix) / np.tanh(1.5)
# fades
fade_out = int(4.0 * SR)
mix[:, -fade_out:] *= np.linspace(1, 0, fade_out) ** 2
mix *= 0.89

out = sys.argv[1] if len(sys.argv) > 1 else "score.wav"
pcm = (np.clip(mix.T, -1, 1) * 32767).astype(np.int16)
import wave
with wave.open(out, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print("wrote", out, TOTAL, "s")
