#!/usr/bin/env python3
"""Scaffold index.html (the root composition) from documentation/edit-decision-list.json.

Run once to (re)build the picture/audio layer. After that, index.html is the
source of truth and can be edited by hand or in the HyperFrames Studio; re-running
this script overwrites those edits.

    python3 tools/build_root.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EDL = json.load(open(os.path.join(ROOT, "documentation", "edit-decision-list.json")))
DUR = EDL["canvas"]["duration"]

# camera moves on the untimed wrapper around each shot: (from_scale, to_scale, from_y, to_y)
MOVES = {
    1: (1.12, 1.04, 0, 0), 5: (1.0, 1.10, 0, -20), 8: (1.06, 1.14, 0, 0), 9: (1.0, 1.06, 0, 0),
    13: (1.10, 1.02, 0, 0), 16: (1.0, 1.07, 0, 0), 20: (1.02, 1.10, 0, 0), 22: (1.0, 1.12, 0, 0),
    26: (1.18, 1.0, 0, 0), 32: (1.0, 1.10, 0, 0),
    37: (1.04, 1.12, 0, 0), 40: (1.0, 1.14, 0, -30),
}
# punch-in inside a long take (time inside shot, scale) — hides a jump without a cut
PUNCH = {23: (4.0, 1.16), 25: (4.1, 1.14)}  # punch-in: the push is split around it
IRIS = {16: 0.4, 20: 0.4}  # incoming shot n opens through a circle; shot n-1 is held under it

shots_html, tl = [], []
z = 1
for s in EDL["shots"]:
    n = s["n"]
    sid = f"shot-{n:02d}"
    start, dur = s["start"], s["dur"]
    if n + 1 in IRIS:
        dur = round(dur + IRIS[n + 1], 3)
    if "src" in s:
        rate = s.get("rate", 1.0)
        attrs = [
            f'id="{sid}"', 'class="clip shot"', f'data-start="{start}"', f'data-duration="{dur}"',
            f'data-media-start="{s["in"]}"', f'data-track-index="{1 + (n % 2)}"', "muted", "playsinline",
            f'src="assets/footage/{s["src"]}.mp4"',
        ]
        if rate != 1.0 and "ramp" not in s:
            attrs.append(f'data-playback-rate="{rate}"')
        if "ramp" in s:
            pts = ",".join(f'{{&quot;t&quot;:{t},&quot;v&quot;:{v}}}' for t, v in s["ramp"])
            attrs.append(f'data-automation="{{&quot;version&quot;:1,&quot;lanes&quot;:[{{&quot;target&quot;:&quot;rate&quot;,&quot;points&quot;:[{pts}]}}]}}"')
        shots_html.append(
            f'      <!-- {n:02d} {s["scene"]} · {s["src"]} @ {s["in"]}s{" · x" + str(rate) if rate != 1 else ""} — {s.get("why", "")} -->\n'
            f'      <div class="cam" id="cam-{n:02d}" style="z-index:{z}"><video {" ".join(attrs)}></video></div>'
        )
    elif "photo" in s:
        p = s["photo"]
        shots_html.append(
            f'      <!-- {n:02d} {s["scene"]} · photo {p} — {s.get("why", "")} -->\n'
            f'      <div id="{sid}" class="clip photo" data-start="{start}" data-duration="{dur}" data-track-index="{1 + (n % 2)}" style="z-index:{z}">\n'
            f'        <img id="{sid}-plate" class="plate" src="assets/photos/{p}-plate.jpg" alt="" />\n'
            f'        <div class="frame frame-{p}" id="{sid}-frame"><img id="{sid}-img" class="still" src="assets/photos/{p}.jpg" alt="" /></div>\n'
            f'      </div>'
        )
    else:  # end card ground: drawn by the legacy scene
        z += 1
        continue
    if n in MOVES:
        s0, s1, y0, y1 = MOVES[n]
        target = f"#cam-{n:02d}" if "src" in s else f"#{sid}-frame"
        tl.append(f'      tl.fromTo("{target}", {{ scale: {s0}, y: {y0} }}, {{ scale: {s1}, y: {y1}, duration: {dur}, ease: "none" }}, {start});')
    if n in IRIS:
        tl.append(f'      tl.fromTo("#cam-{n:02d}", {{ clipPath: "circle(0% at 50% 44%)" }}, {{ clipPath: "circle(78% at 50% 44%)", duration: {IRIS[n]}, ease: "power3.out" }}, {start});')
    if n in PUNCH:
        t, sc = PUNCH[n]
        tl.append(f'      tl.fromTo("#cam-{n:02d}", {{ scale: 1.0 }}, {{ scale: 1.03, duration: {t}, ease: "none" }}, {start});')
        tl.append(f'      tl.fromTo("#cam-{n:02d}", {{ scale: {sc} }}, {{ scale: {round(sc + 0.03, 3)}, duration: {round(dur - t, 3)}, ease: "none", immediateRender: false }}, {start + t});')
    z += 1

# photo push / pan moves
tl.append('      tl.fromTo("#shot-06-frame", { scale: 1.0, x: 0 }, { scale: 1.12, x: -40, duration: 4, ease: "none" }, 4);')
tl.append('      tl.fromTo("#shot-07-frame", { scale: 1.08, x: 60 }, { scale: 1.08, x: -60, duration: 4, ease: "none" }, 8);')
tl.append('      tl.fromTo("#shot-41-frame", { scale: 1.0, y: 0 }, { scale: 1.10, y: -30, duration: 6, ease: "none" }, 74);')

dialogue = []
for i, d in enumerate(EDL["dialogue"]):
    dialogue.append(
        f'    <audio id="vo-{d["src"]}" class="clip" data-start="{d["start"]}" data-duration="{d["dur"]}" data-media-start="{d["in"]}" '
        f'data-track-index="20" data-volume="1" data-fade-in="0.08" data-fade-out="{d["fade_out"]}" data-audio-group="voice" '
        f'src="assets/audio/dialogue-{d["src"]}.wav"></audio>'
    )

# music: full level, ducked under the two coaching clips (43.6–59.4)
duck = '{&quot;version&quot;:1,&quot;lanes&quot;:[{&quot;target&quot;:&quot;volume&quot;,&quot;points&quot;:[{&quot;t&quot;:0,&quot;v&quot;:1},{&quot;t&quot;:43.3,&quot;v&quot;:1},{&quot;t&quot;:43.7,&quot;v&quot;:0.3},{&quot;t&quot;:59.3,&quot;v&quot;:0.3},{&quot;t&quot;:59.9,&quot;v&quot;:1},{&quot;t&quot;:86,&quot;v&quot;:1}]}]}'

SFX_LEN = {"whoosh": 0.57, "whoosh-short": 0.57, "sparkle": 1.8, "impact-bass-1": 2.1, "impact-bass-2": 2.59, "whoosh-cinematic": 5.54}
SFX = [  # (id, file, start, volume, rate) — start = picture time − file peak offset + 1 frame
    ("sfx-hook-slam", "whoosh", 1.87, 0.45, 1.0),
    ("sfx-to-master", "whoosh", 3.85, 0.40, 0.85),
    ("sfx-title-shimmer", "sparkle", 12.62, 0.35, 1.0),
    ("sfx-ch01", "whoosh-short", 23.87, 0.32, 1.0),
    ("sfx-ch02", "whoosh", 29.87, 0.32, 1.15),
    ("sfx-ch03", "whoosh-short", 36.85, 0.32, 0.9),
    ("sfx-climax-impact", "impact-bass-1", 59.96, 0.55, 1.0),
    ("sfx-climax-line1", "whoosh", 63.87, 0.38, 1.0),
    ("sfx-climax-line2", "whoosh-short", 67.87, 0.38, 1.1),
    ("sfx-to-legacy", "whoosh-cinematic", 71.53, 0.42, 1.0),
    ("sfx-logo-impact", "impact-bass-2", 79.92, 0.5, 1.0),
    ("sfx-logo-shimmer", "sparkle", 80.45, 0.4, 1.0),  # lane 23 (overlaps the impact)
]
sfx_html = []
for i, (sid, f, st, vol, rate) in enumerate(SFX):
    extra = f' data-playback-rate="{rate}"' if rate != 1.0 else ""
    ln = round(SFX_LEN[f] / rate, 2)
    sfx_html.append(
        f'    <audio id="{sid}" class="clip" data-start="{st}" data-duration="{ln}" data-track-index="{23 if sid == 'sfx-logo-shimmer' else 22}" data-volume="{vol}"{extra} '
        f'data-audio-group="sfx" src="assets/sfx/{f}.mp3"></audio>'
    )

SCENES = [s for s in EDL["scenes"]]
hosts = []
for s in SCENES:
    hosts.append(
        f'    <div id="{s["id"]}" data-composition-id="{s["id"]}" data-composition-src="compositions/{s["id"]}.html" '
        f'data-start="{s["start"]}" data-duration="{s["end"] - s["start"]}" data-track-index="10" data-track-kind="graphics" '
        f'data-width="1080" data-height="1920" style="z-index:200"></div>'
    )

html = f'''<!doctype html>
<html
  lang="ms"
  data-composition-variables='[
    {{"id":"previewWatermark","type":"boolean","label":"Preview watermark (turn off for the approved final)","default":true}}
  ]'
>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Grandmaster Skill Signature — Pak Su Den · The Art of Mastery</title>
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Bebas Neue"; src: url("assets/fonts/BebasNeue.ttf") format("truetype"); font-weight: 400; }}
      @font-face {{ font-family: "Anton"; src: url("assets/fonts/Anton.ttf") format("truetype"); font-weight: 400; }}
      @font-face {{ font-family: "Montserrat"; src: url("assets/fonts/Montserrat.ttf") format("truetype"); font-weight: 100 900; }}
      @font-face {{ font-family: "Inter"; src: url("assets/fonts/Inter.ttf") format("truetype"); font-weight: 100 900; }}
      :root {{
        --navy: #071426; --midnight: #080a0f; --blue: #168cff; --baby: #89cfff; --gold: #d4af37; --white: #ffffff;
      }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: var(--midnight); }}
      #ground {{ position: absolute; inset: 0; background: var(--midnight); }}
      .cam {{ position: absolute; inset: 0; overflow: hidden; transform-origin: 50% 46%; }}
      .cam video {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; object-fit: cover; }}
      .photo {{ position: absolute; inset: 0; overflow: hidden; }}
      .photo .plate {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; object-fit: cover; }}
      .photo .frame {{ position: absolute; left: 0; width: 1080px; overflow: hidden; transform-origin: 50% 50%; }}
      .photo .frame img {{ display: block; width: 100%; height: 100%; object-fit: cover; }}
      .frame-class-teach, .frame-class-wide {{ top: 676px; height: 760px; box-shadow: 0 0 0 2px rgba(212,175,55,.55), 0 40px 120px rgba(0,0,0,.65); }}
      .frame-certificate {{ top: 0; height: 1920px; }}
      #watermark {{ position: absolute; inset: 0; pointer-events: none; z-index: 900; }}
      #watermark span {{
        position: absolute; left: 0; width: 1080px; top: 196px; text-align: center; font: 700 28px/1 Inter, sans-serif; letter-spacing: .3em;
        color: #ffffff; text-shadow: 0 1px 3px #000, 0 0 12px rgba(0,0,0,.9);
      }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
      <div id="ground"></div>

      <!-- ===================== PICTURE (from documentation/edit-decision-list.json) ===================== -->
{chr(10).join(shots_html)}

      <!-- ===================== GRAPHICS: one scene composition per story beat ===================== -->
{chr(10).join(hosts)}

      <!-- English subtitles (burned-in) for the two coaching clips -->
      <div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html"
        data-start="43.6" data-duration="16.4" data-track-index="11" data-track-kind="captions"
        data-width="1080" data-height="1920" style="z-index:300"></div>

      <!-- ===================== SOUND ===================== -->
    <audio id="music-score" class="clip" data-start="0" data-duration="{DUR}" data-track-index="21" data-volume="1"
      data-timeline-role="music" data-fade-out="1.5" data-audio-group="music"
      data-automation="{duck}"
      src="assets/audio/score-the-art-of-mastery.wav"></audio>
{chr(10).join(dialogue)}
{chr(10).join(sfx_html)}

      <div id="watermark"><span id="watermark-label">PREVIEW · NOT FINAL</span></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      const vars = (window.__hyperframes && window.__hyperframes.getVariables && window.__hyperframes.getVariables()) || {{}};
      document.getElementById("watermark").style.opacity = vars.previewWatermark === false ? 0 : 1;
      // camera: slow push-ins, settles and punch-ins on the untimed wrapper of each shot
{chr(10).join(tl)}
      tl.set("#ground", {{ opacity: 1 }}, {DUR - 0.01});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
open(os.path.join(ROOT, "index.html"), "w").write(html)
print("index.html written:", len(EDL["shots"]), "shots,", len(SFX), "sfx")
