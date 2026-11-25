#!/bin/bash
# Download the client's media from the Google Drive folder (link-shared files) and prepare it
# for the composition. Media is NOT stored in git (the repository is public).
set -e
P="$(cd "$(dirname "$0")/.." && pwd)"; cd "$P"
mkdir -p source/video source/images reference assets/photos assets/audio
dl(){ [ -s "$2" ] || curl -sS -L --retry 3 -o "$2" "https://drive.usercontent.google.com/download?id=$1&export=download&confirm=t"; echo "ok $2"; }
dl 1YQd3KVW7ygntVKxlo0Ji21KQqnmxVVzl "reference/Pak Su Den.mp4"
dl 1nLtO6Oi2ibXsEi5aHwf4VtLzD8RGO4Hz "source/video/Beng 7 -1.mp4"
dl 1BEFMxp1gByk7C8-lbb4vy1bj9LA14QRk "source/video/beng 8.mp4"
dl 1EXvIihN-pNm8HggGEhZ9KCk825fd6vVT "source/video/beng 9.mp4"
dl 1pqHceVpmVEYbyfEkdI9YFZ4ewCeTNpVb "source/video/beng 10.mp4"
dl 1B6FRQp_58uCsaelOdonvpBcPaGByw6zl "source/video/beng 12.mp4"
dl 1HhwWGm9jVwgTrtRcOPCimoQAw1djfUvZ "source/video/beng 13.mp4"
dl 1RxZzIsQSMiUsMKneQFBE_BZ6GB3a6tGd "source/video/beng 14.mp4"
dl 1Ed-0UQNC1eJUJnenPyk-5ReIaQb_iuda "source/video/beng 15.mp4"
dl 1sNEwZZe06zxhwMwlATYluusaNbZ0OylI "source/video/beng 16.mp4"
dl 1Yl_L3-s2GTi3FSi4QlO9OXtiAOkW_JnL "source/video/beng 17.mp4"
dl 1c-hRGEUeoU_5aoboUjdDfe48K1FAydQZ "source/video/beng 18.mp4"
dl 1Fwo3D79q7DGNceUGNpco7p87VgerqFrk "source/video/beng 19.mp4"
dl 1lnm3Pyg0t1V06HOG-m71M5LXyBRmD-Ak "source/video/beng 20.mp4"
dl 1IvEHuLqnL--cVVQoGeEHDJiS2HaHffFU "source/video/beng 21.mp4"
dl 1Ygrw0Ta7X3gZ8gn55R63hZyqLrRlQffp "source/video/beng 22.mp4"
dl 1pwBXjnOzZskLhJLPkIvF_M1agDmoTi9e "source/images/gambar beng 1.jpeg"
dl 1rsRdHLHaA_hTXy1Qv4juPhMlGZ8WasG2 "source/images/Gambar Beng 2.jpeg"
dl 1-lT-XYL0R7u40fYEEU6ympuXmQpjabPS "source/images/Gambar beng 3.jpeg"
# photos + blurred plates
cp "source/images/Gambar Beng 2.jpeg" assets/photos/class-teach.jpg
cp "source/images/Gambar beng 3.jpeg" assets/photos/class-wide.jpg
cp "source/images/gambar beng 1.jpeg" assets/photos/certificate.jpg
for n in class-teach class-wide certificate; do
  ffmpeg -v error -y -i assets/photos/$n.jpg -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=38,eq=brightness=-0.16:saturation=0.75" -q:v 3 assets/photos/$n-plate.jpg
done
# cleaned coaching dialogue
for n in 12 14; do
  ffmpeg -v error -y -i "source/video/beng $n.mp4" -vn -af "highpass=f=95,lowpass=f=9000,afftdn=nr=14:nf=-42:tn=1,equalizer=f=250:t=q:w=1:g=-2,equalizer=f=3000:t=q:w=1:g=3,acompressor=threshold=-24dB:ratio=3:attack=8:release=120,loudnorm=I=-17:TP=-2:LRA=7" -ar 48000 -ac 2 assets/audio/dialogue-beng_$n.wav
done
# stabilise / denoise / upscale / 60 fps
bash tools/conform_footage.sh
echo "Media ready. Open the preview with: npx hyperframes preview"
