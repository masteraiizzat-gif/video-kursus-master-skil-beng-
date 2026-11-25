import sys, json, os, glob, wave, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel(os.environ.get("WHISPER_MODEL","large-v3"), device="cpu", compute_type="int8", cpu_threads=4)
res={}
for w in sorted(glob.glob(os.path.join(sys.argv[1], "*.wav"))):
    name=os.path.basename(w)[:-4]
    wf=wave.open(w);a=np.frombuffer(wf.readframes(wf.getnframes()),dtype=np.int16).astype(np.float32)/32768.0
    segs,info=m.transcribe(a,language="ms",word_timestamps=True,vad_filter=True,vad_parameters={"threshold":0.3,"min_silence_duration_ms":300},beam_size=5,condition_on_previous_text=False)
    L=[{"start":round(s.start,2),"end":round(s.end,2),"text":s.text.strip(),"no_speech":round(s.no_speech_prob,2),"logprob":round(s.avg_logprob,2),"words":[{"w":x.word,"s":round(x.start,2),"e":round(x.end,2),"p":round(x.probability,2)} for x in (s.words or [])]} for s in segs]
    res[name]={"duration":info.duration,"segments":L}
    print(name,flush=True)
    for s in L: print("  ",s["start"],s["end"],s["text"],s["no_speech"],s["logprob"],flush=True)
json.dump(res,open(sys.argv[2],"w"),ensure_ascii=False,indent=1)
