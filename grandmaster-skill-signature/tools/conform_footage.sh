#!/bin/bash
# Footage normalization (not a final render): stabilize, denoise, upscale, CFR 60
set -e
P="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p $P/assets/footage $P/proxies/trf
cd $P/source/video
for f in *.mp4; do
  n=$(echo "${f%.mp4}" | tr 'A-Z ' 'a-z_' | sed 's/_-1/-1/;s/__/_/g')
  [ "$n" = "beng_20" ] && continue
  out=$P/assets/footage/$n.mp4
  [ -s "$out" ] && continue
  ffmpeg -v error -y -i "$f" -vf "vidstabdetect=shakiness=6:accuracy=12:result=$P/proxies/trf/$n.trf" -f null -
  ffmpeg -v error -y -i "$f" -vf "vidstabtransform=input=$P/proxies/trf/$n.trf:smoothing=12:zoom=4:optzoom=0:interpol=bicubic,hqdn3d=1.5:1.5:4:4,fps=60,scale=1080:1920:flags=lanczos,cas=0.45,format=yuv420p" \
    -c:v libx264 -preset fast -crf 18 -g 30 -colorspace bt709 -color_primaries bt709 -color_trc bt709 -movflags +faststart \
    -c:a aac -ar 48000 -b:a 160k "$out"
  echo "done $n"
done
echo ALL_PROXIES_DONE
