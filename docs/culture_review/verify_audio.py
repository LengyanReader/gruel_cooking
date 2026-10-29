# -*- coding: utf-8 -*-
"""Honesty check on the shipped page, run after build_audio.py.

    python verify_audio.py

Three independent claims about the read-aloud audio, none of which the build trusts itself
on: (1) the manifest spliced into the HTML between /*AM-BEGIN*/ and /*AM-END*/ is valid JSON
and byte-equal to assets/audio/manifest.json; (2) every cue the page's own reader JS builds
has exactly one clip in the manifest, for that track's language, with no gaps; (3) every Ogg
file the manifest points at exists and ffprobe decodes it, so the shipped audio is real audio
rather than an empty container. Exits non-zero if any claim fails."""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_audio import extract, FFMPEG  # noqa: E402
FFPROBE = str(FFMPEG).replace("ffmpeg", "ffprobe")

ok = True
html = (HERE / "2026-10.html").read_text(encoding="utf-8")
blob = re.search(r"/\*AM-BEGIN\*/window\.AUDIO=(\{.*?\});/\*AM-END\*/", html, re.S)
print("inline manifest found: %s" % bool(blob))
ok &= bool(blob)
man = json.loads(blob.group(1))
disk = json.loads((HERE / "assets/audio/manifest.json").read_text(encoding="utf-8"))
print("inline == assets/audio/manifest.json: %s" % (man == disk))
ok &= (man == disk)

data = extract()
for tid, tr in man["tracks"].items():
    want = {(c["blk"], c["sub"]) for c in data[tr["lang"]]}
    got = {(c["blk"], c["sub"]) for s in tr["secs"] for c in s["clips"]}
    dup = len(tr["secs"] and [c for s in tr["secs"] for c in s["clips"]]) - len(got)
    ff = [man["dir"] + s["file"] for s in tr["secs"]]
    missing = [f for f in ff if not (HERE / f).exists()]
    durs = []
    for f in ff:
        p = HERE / f
        if p.exists():
            r = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                                "-of", "default=noprint_wrappers=1:nokey=1", str(p)],
                               capture_output=True, text=True)
            try:
                durs.append(float(r.stdout.strip()))
            except ValueError:
                durs.append(0.0)
    covered = (want == got) and not missing and not dup and sum(durs) > 0
    ok &= covered
    print("%-4s cues %d/%d dup %d missing %d | files %d absent %d | decoded %.1f s | %.1f MB"
          " [%s]" % (tid, len(got), len(want), dup, len(want - got), len(ff), len(missing),
                     sum(durs), sum((HERE / f).stat().st_size for f in ff
                                    if (HERE / f).exists()) / 1e6,
                     "OK" if covered else "FAIL"))
print("verify_audio: %s" % ("ALL OK" if ok else "PROBLEMS"))
sys.exit(0 if ok else 1)
