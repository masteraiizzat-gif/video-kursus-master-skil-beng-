#!/bin/bash
# Rebuild the root composition from the EDL, then re-apply the colour grades.
set -e
cd "$(dirname "$0")/.."
python3 tools/build_root.py
npx --yes hyperframes@0.9.94 media-treatment --selector "video.shot" --grading graphics/grade/mastery-grade.json --apply --json >/dev/null
npx --yes hyperframes@0.9.94 media-treatment --selector "img.still" --grading graphics/grade/photo-grade.json --apply --json >/dev/null
echo "rebuilt index.html (grades applied)"
