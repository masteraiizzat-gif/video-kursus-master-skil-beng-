#!/usr/bin/env bash
# 60-second WhatsApp cut-down of the v2 master. Every splice is on a bar downbeat (120 BPM, 2 s bar)
# and on an existing shot cut, so the music keeps its pulse and no shot is jump-cut.
#   0–22  hook, master + awards, Academy logo title, BENG credit, course chips
#   24–28 signature technique 01 (hand positioning, precision)
#   52–86 coaching voice (SKILL BECOMES MASTERY), climax, certificate, logo end card
set -euo pipefail
cd "$(dirname "$0")/.."
M=exports/grandmaster-skill-signature-FINAL-v2-master.mp4
O=exports/grandmaster-skill-signature-60s-WhatsApp.mp4
ffmpeg -v error -y -i "$M" -filter_complex "\
[0:v]trim=0:22,setpts=PTS-STARTPTS[v1];[0:a]atrim=0:22,asetpts=PTS-STARTPTS,afade=t=out:st=21.96:d=0.04[a1];\
[0:v]trim=24:28,setpts=PTS-STARTPTS[v2];[0:a]atrim=24:28,asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st=3.9:d=0.1[a2];\
[0:v]trim=52:86,setpts=PTS-STARTPTS[v3];[0:a]atrim=52:86,asetpts=PTS-STARTPTS,afade=t=in:d=0.06[a3];\
[v1][a1][v2][a2][v3][a3]concat=n=3:v=1:a=1[v][a]" -map "[v]" -map "[a]" \
  -c:v libx264 -profile:v high -preset slow -crf 21 -maxrate 5M -bufsize 10M -pix_fmt yuv420p -r 30 \
  -c:a aac -b:a 160k -ar 48000 -movflags +faststart "$O"
