import sys, json, os, glob, wave, numpy as np
from faster_whisper import WhisperModel
src, out = sys.argv[1], sys.argv[2]
m = WhisperModel(os.environ.get("WHISPER_MODEL","large-v3"), device="cpu", compute_type="int8", cpu_threads=4)
res = {}
for w in sorted(glob.glob(os.path.join(src, "*.wav"))):
    name = os.path.basename(w)[:-4]
    wf=wave.open(w);a=np.frombuffer(wf.readframes(wf.getnframes()),dtype=np.int16).astype(np.float32)/32768.0
    segs, info = m.transcribe(a, language="ms", word_timestamps=True, vad_filter=False, beam_size=5,
        initial_prompt="Pak Su Den mengajar teknik urutan kepada peserta kursus. Urut, tekan, otot, saraf, urat.")
    L=[]
    for s in segs:
        L.append({"start":round(s.start,2),"end":round(s.end,2),"text":s.text.strip(),"no_speech":round(s.no_speech_prob,2),"logprob":round(s.avg_logprob,2),
                  "words":[{"w":x.word,"s":round(x.start,2),"e":round(x.end,2),"p":round(x.probability,2)} for x in (s.words or [])]})
    res[name]={"duration":info.duration,"segments":L}
    print(name, len(L), flush=True)
    for s in L: print("  ",s["start"],s["end"],s["text"], s["no_speech"], flush=True)
    json.dump(res, open(out,"w"), ensure_ascii=False, indent=1)
