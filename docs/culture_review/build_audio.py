# -*- coding: utf-8 -*-
"""Render the culture review's read-aloud queue with Microsoft neural voices and ship it
as a set of Ogg/Opus files (one per section per voice) plus a cue manifest that is spliced
back into the page.

    python build_audio.py                 # whole issue, all four voices
    python build_audio.py --dry           # extract and measure only
    python build_audio.py --pilot         # one voice, one section (smoke test)
    python build_audio.py --only zh-M     # one track
    python build_audio.py --refresh       # ignore the cache and re-render every unit

Why pre-rendered audio at all: the browser this page is heard in (an Electron/Chromium
webview) exposes only legacy SAPI desktop voices, and Edge's "(Natural)" online voices can
only be enumerated inside Edge. Neural speech therefore has to arrive as ordinary audio.
The page keeps its live Web Speech path as the fallback.

How the reading is kept from sounding robotic - two things, both in stage 2/3:

1. Context. A neural voice given ONE sentence gives back one flat, self-contained
   intonation curve: every cue starts high, ends down, and the sequence of cues has the
   cadence of a dictation machine, not of a reader. So the text is handed to the service
   in units of connected discourse (up to UNIT_MAX characters of the same element, i.e. a
   run of sentences), and the sentence-level timings come back with the audio as
   SentenceBoundary events. One render per unit, one highlight per cue.
2. Breathing. Concatenating isolated clips stacks their individual silence pads, so
   pauses arrive irregularly - sometimes none, sometimes a second and a half. Each unit's
   head and tail silence is therefore trimmed to a fixed target and re-padded, which makes
   the gap between units a deliberate paragraph pause, while the pauses *inside* a unit
   are left exactly as the model spoke them.
3. Rank. A pause has to answer to the break it stands for. Two sentences of one paragraph
   keep whatever gap the render gave them; the handover from one element to the next gets
   ELEMENT_GAP extra seconds, so a new paragraph is audibly a new paragraph and not just
   another full stop. The last unit of a section is left alone - the player reopens a new
   file there and adds its own latency to the gap already there.

Stage 1  extract   - a literal port of the page's own reader JS (SKIP / READ / hidden /
                     textNodes / segs / clean / build), so that a cue in the sound and a
                     cue in the DOM are the same object. Cues are addressed by (blk, sub):
                     blk = index in document.querySelectorAll(READ), sub = sentence number
                     inside that element. The queue this prints is what the page reports
                     when you press the button (this issue: 443 cues zh, 396 en - recount
                     on every build; the number moves with the text).
Stage 2  synth     - edge-tts, one mp3 per unit, cached under _audio_cache/<voice>/<sha1>
                     with a sidecar <sha1>.json holding the measured duration and the
                     SentenceBoundary list. The sidecar is written last, so a half-finished
                     or refused unit never counts as done: the service does sometimes hand
                     back a couple of kilobytes for a paragraph of text, and a render
                     shorter than MIN_FRAC of its expected speaking time is deleted and
                     retried rather than shipped.
Stage 3  assemble  - ffmpeg decodes each unit to 24 kHz mono s16, silence is normalised,
                     cues are timed from the boundary events, and the frames are
                     concatenated per section, so cue boundaries stay sample-exact.
Stage 4  encode    - one ffmpeg pass per section to Ogg/Opus, then the manifest is written
                     to assets/audio/manifest.json and spliced between /*AM-BEGIN*/ and
                     /*AM-END*/ in the HTML (byte level: the document is not re-encoded).

Needs: beautifulsoup4, edge-tts, ffmpeg on PATH (or edit FFMPEG below), and a network.
"""
import argparse, asyncio, hashlib, io, json, os, pathlib, re, subprocess, sys, wave
from array import array
from bs4 import BeautifulSoup, NavigableString

HERE = pathlib.Path(__file__).resolve().parent          # docs/culture_review
HTML = HERE / "2026-10.html"
DUMP = HERE / "_audio_sentences.json"
CACHE = HERE / "_audio_cache"
TMP = HERE / "_audio_tmp"
OUT = HERE / "assets" / "audio"
FFMPEG = os.environ.get("FFMPEG", r"C:\Users\data\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe")
SR = 24000
BITRATE = "32k"
VOICES = {                                  # ids are what the page's voice picker shows
    "zh-F": "zh-CN-XiaoxiaoNeural",         # 晓晓 - female, standard Mandarin
    "zh-M": "zh-CN-YunxiNeural",            # 云希 - male, standard Mandarin
    "en-F": "en-US-AvaMultilingualNeural",
    "en-M": "en-US-AndrewMultilingualNeural",
}
CONCURRENCY = 5
UNIT_MAX = 600          # characters handed to the model per request (~6-10 sentences)
TICK = 1e7              # the service reports offsets in 100 ns units
HEAD_KEEP = 0.05        # seconds of silence kept in front of a unit
TAIL_KEEP = 0.40        # seconds of silence after a unit = the paragraph pause
NOISE = 160             # int16 amplitude below which a sample counts as silence
SILENCE = 0.4           # seconds kept for a unit that carries no speakable character
ELEMENT_GAP = 0.30      # extra silence at a unit that ends one element and hands over to
#                        the next: a paragraph break must outlast a full stop inside one
RATE = {"zh": {"han": 5.5, "latin": 13.0, "digit": 5.0},
        "en": {"han": 5.5, "latin": 13.0, "digit": 5.0}}
# Characters per second at the FAST end of what these voices do with each class, measured
# on this issue's own renders (Han 4.0/s, Latin 11/s, a Chinese voice reading English 10/s).
# The expectation is deliberately generous, because its only job is to catch the failure
# mode where the service answers a whole paragraph with a couple of hundred milliseconds -
# not to insist on a particular speaking speed.
MIN_FRAC = 0.5          # refuse a render shorter than this share of the expected time

# ── stage 1: the reader JS, ported ──────────────────────────────────────────────────
SKIP_TAGS = {"nav", "footer", "figcaption"}
SKIP_CLS = {"reader", "src", "who", "stamp", "kicker", "lens", "lang-tag", "issue-tag",
            "en-title", "dateline", "orig"}
READ = (".masthead h1,.masthead .epigraph,.sec-head h2,.sec-lede,.item h3,.item p,"
        ".q .tr,.q .note,.ten .quote,.eyebrow h4,.eyebrow p,.method p,.mcard h4,.mcard p")
TERM = "\u3002\uff01\uff1f\uff1b\u2026"
MAXLEN = 260


def matches_skip(el):
    return el.name in SKIP_TAGS or bool(set(el.get("class", [])) & SKIP_CLS)


def hidden(el, other):
    p = el
    while p is not None and p.name != "[document]":
        if not isinstance(p, NavigableString) and (
                p.name in SKIP_TAGS or bool(set(p.get("class", [])) & SKIP_CLS) or p.has_attr(other)):
            return True
        p = p.parent
    return False


def text_nodes(el, other):
    out = []

    def walk(n):
        if isinstance(n, NavigableString):
            if not hidden(n, other):
                out.append(n)
            return
        if matches_skip(n) or n.has_attr(other):
            return
        for c in n.children:
            walk(c)

    for c in el.children:
        walk(c)
    return out


def segs(t):
    r, s = [], 0
    for k, c in enumerate(t):
        nx = t[k + 1] if k + 1 < len(t) else ""
        term = c in TERM or (c in ".!?" and (k + 1 == len(t) or nx.isspace()))
        if term:
            r.append((s, k + 1, True))
            s = k + 1
    if s < len(t):
        r.append((s, len(t), False))
    return r


def clean(s):
    s = re.sub(r"[\u2714\u2713\u25c7]", "", s)                       # ticks and the doubt mark
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"\b[a-z0-9.-]+\.(?:org|com|net|edu|gov|au|uk|io|cn|news)\b", "", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[\uff0c\u3001\uff1a\uff1b\u00b7\u2013\u2014\u002d]\s*$", "", s)
    return s.strip()


def section_of(el):
    p = el
    while p is not None and p.name != "[document]":
        if p.name == "section" and p.get("id"):
            return p["id"]
        cls = set(p.get("class") or [])
        if "masthead" in cls:
            return "front"
        if "eyebrow" in cls:
            return "eyebrow"
        if "sec-head" in cls and p.find_next_sibling(class_="eyebrow-grid"):
            return "eyebrow"
        p = p.parent
    return "extra"


def build(lang, soup):
    other = "data-en" if lang == "zh" else "data-zh"
    Q, els = [], list(soup.select(READ))
    for blk, el in enumerate(els):
        if hidden(el, other):
            continue
        parts, sub = [], 0
        sec = section_of(el)

        def flush():
            nonlocal sub
            if not parts:
                return
            text = clean("".join(p[2] for p in parts))
            if len(text) > 1:
                Q.append({"sec": sec, "blk": blk, "sub": sub, "tag": el.name, "text": text})
                sub += 1
            parts.clear()

        for node in text_nodes(el, other):
            t = str(node)
            for a, b, term in segs(t):
                parts.append((node, a, t[a:b]))
                if term or len(clean("".join(p[2] for p in parts))) > MAXLEN:
                    flush()
        flush()
    return Q


def extract():
    soup = BeautifulSoup(HTML.read_text(encoding="utf-8"), "html.parser")
    data = {lang: build(lang, soup) for lang in ("zh", "en")}
    DUMP.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    for lang, rows in data.items():
        groups = len({r["sec"] for r in rows})
        print("%s: %d cues, %d chars, %d sections" % (lang, len(rows), sum(len(r["text"]) for r in rows), groups))
    if "extra" in {r["sec"] for r in data["zh"] + data["en"]}:
        raise SystemExit("a cue fell outside every section - extend section_of() before rendering")
    return data


def groups_of(rows):
    out = []
    for r in rows:
        if out and out[-1][0] == r["sec"]:
            out[-1][1].append(r)
        else:
            out.append([r["sec"], [r]])
    return out


# ── stage 2: edge-tts, one request per unit of connected text ───────────────────────
def key_of(voice, text):
    return CACHE / voice / (hashlib.sha1(text.encode("utf-8")).hexdigest()[:24])


def meta_of(voice, text):
    return key_of(voice, text).with_suffix(".json")


def expect_sec(text, lang):
    """The least audio this text could honestly take, given what each character class costs."""
    r = RATE[lang]
    han = len(re.findall(r"[\u4e00-\u9fff]", text))
    latin = len(re.findall(r"[A-Za-z]", text))
    digit = len(re.findall(r"\d", text))
    return han / r["han"] + latin / r["latin"] + digit / r["digit"]


def norm(s):
    """Alphanumerics only - so a cue and the boundary the service reports for it can be
    compared, and counted in characters, without punctuation disagreeing."""
    return "".join(c for c in s if c.isalnum())


def speakable(text):
    return bool(re.search(r"\w", text))


# ── reading overrides: the synthesis layer only ─────────────────────────────────────
# The free endpoint refuses <phoneme> SSML (probe: _pron_probe.py -> NoAudioReceived),
# so a forced reading goes in as ordinary text: replace the risky span with homophones
# that have ONE reading. Applied to a cue's text before units are glued, so the cache
# key, the request, and the SentenceBoundary comparison all see the same string; the
# page and _audio_sentences.json keep displaying the original. List built by pron_audit
# (pypinyin G2P over every zh cue): each row is a span whose default reading the G2P
# either demonstrably gets wrong (朝阳公园 in phrase mode -> zhāo) or splits ambiguously
# (爱乐 -> ài lè). Replacement preserves syllables, not characters.
READING_ZH = [
    ("朝阳公园", "潮阳公园"),      # 朝阳 as a place name is cháo yáng, not zhāo
    ("朝光游去", "晨光游去"),      # the alga swims toward MORNING light: zhāo, and a
                                # bare 朝 before 光 reads more safely as 晨
    ("爱乐", "音乐"),             # 中国爱乐 / 爱乐乐团: yuè, G2P's first reading is lè
    ("流行乐", "流行音乐"),        # when 乐 ends a breath it tends to flatten to lè
    ("供应链", "公应链"),          # 供 is gōng here, not gòng
    ("供人改编", "公人改编"),      # same verb 供 (= provide) in "供人改编的资源"
    ("和歌", "贺歌"),             # the Japanese form is hè gē, not hé
    ("千鶴", "千鹤"),             # the variant 鶴 can be dropped by the reader
    ("硤合", "峡合"),             # rare 硤 stands for 峡 in this name
    ("社媒帖", "社媒贴"),          # a social-media post is tiē, 帖 alone flirts with tiě
]


def reading(text):
    """Cue text as the page shows it, with the risky spans swapped for their forced
    readings. Length may change (音乐 for 乐): the boundary check in cue_starts falls
    back to proportional placement, and the cache key is hash(text) either way."""
    for old, new in READING_ZH:
        if old in text:
            text = text.replace(old, new)
    return text


def units_of(items):
    """Consecutive cues of the same element, glued into one request. Splitting stays on
    cue borders, so the manifest's (blk, sub) addressing is untouched. Cue text enters at
    the reading layer: an en cue never matches a zh span, so one path serves both."""
    out = []
    for it in items:
        text = reading(it["text"])
        if out and out[-1]["blk"] == it["blk"] and out[-1]["chars"] + len(text) <= UNIT_MAX:
            u = out[-1]
        else:
            u = {"blk": it["blk"], "subs": [], "parts": [], "chars": 0}
            out.append(u)
        u["subs"].append(it["sub"])
        u["parts"].append(text)
        u["chars"] += len(text)
    for u in out:
        u["text"] = " ".join(u["parts"])
    return out


def validated(meta):
    """A cache entry only counts once it went through the duration check below. That check
    arrived after the first renders, so the older sidecars - a bare list of boundaries -
    are treated as unverified and re-rendered."""
    try:
        d = json.loads(meta.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return isinstance(d, dict) and "dur" in d


async def synth_unit(sem, voice, unit, stats, lang, refresh=False):
    stem, meta = key_of(voice, unit["text"]), meta_of(voice, unit["text"])
    dest = stem.with_suffix(".mp3")
    if not refresh and dest.exists() and dest.stat().st_size > 400 and validated(meta):
        stats["cached"] += 1
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not speakable(unit["text"]):        # a punctuation-only tail (e.g. closing quote
        stats["silent"] += 1               # marks left by the sentence split): nothing for
        meta.write_text(json.dumps({"dur": SILENCE, "bounds": []}), encoding="utf-8")
        return True                        # the service to say; assemble keeps silence
    import edge_tts
    async with sem:
        for attempt in range(5):
            try:
                buf, bounds = bytearray(), []
                async for ch in edge_tts.Communicate(unit["text"], voice).stream():
                    if ch["type"] == "audio":
                        buf.extend(ch["data"])
                    elif ch["type"] == "SentenceBoundary":
                        bounds.append({"t": ch["offset"] / TICK, "d": ch["duration"] / TICK,
                                       "s": norm(ch.get("text", ""))})
                if len(buf) < 400:
                    raise RuntimeError("empty audio (%d bytes)" % len(buf))
                tmp = dest.with_suffix(".part")
                tmp.write_bytes(bytes(buf))
                os.replace(tmp, dest)
                got = len(wav_frames(decode_wav(dest))) / 2 / SR        # bytes can pass the
                exp = expect_sec(unit["text"], lang)                    # size test and still
                if got < MIN_FRAC * exp:                                 # be a truncated
                    dest.unlink()                                        # answer: refuse it,
                    meta.unlink(missing_ok=True)                         # delete, retry
                    raise RuntimeError("short audio %.2f s for %d chars (expected >= %.1f s)"
                                       % (got, len(unit["text"]), exp))
                meta.write_text(json.dumps({"dur": round(got, 3), "bounds": bounds},
                                           ensure_ascii=True), encoding="utf-8")
                stats["synth"] += 1
                stats["bounds"] += len(bounds)
                stats["nocue"] += 1 if not bounds else 0
                return True
            except Exception as exc:                    # noqa: BLE001
                stats["retry"] += 1
                stats.setdefault("errors", []).append("%s: %s" % (type(exc).__name__, exc))
                await asyncio.sleep(1.0 + attempt * 2.0)
    stats.setdefault("failures", []).append((voice, unit["text"]))
    return False


# ── stage 3: decode, normalise silence, place cues, concat ──────────────────────────
def decode_wav(mp3):
    out = subprocess.run([FFMPEG, "-v", "error", "-nostdin", "-i", str(mp3),
                          "-f", "wav", "-ar", str(SR), "-ac", "1", "-sample_fmt", "s16", "-"],
                         capture_output=True, check=True)
    if not out.stdout.startswith(b"RIFF"):
        raise RuntimeError("ffmpeg did not emit wav: %r" % out.stdout[:24])
    return out.stdout


def wav_frames(wavbytes):
    with wave.open(io.BytesIO(wavbytes), "rb") as w:
        if (w.getframerate(), w.getnchannels(), w.getsampwidth()) != (SR, 1, 2):
            raise RuntimeError("unexpected wav format %s" % ((w.getframerate(), w.getnchannels(), w.getsampwidth()),))
        return w.readframes(w.getnframes())


def has_unit(voice, text):
    return validated(meta_of(voice, text)) and (
        not speakable(text) or (key_of(voice, text).with_suffix(".mp3").exists()
                               and key_of(voice, text).with_suffix(".mp3").stat().st_size > 400))


def head_tail(frames):
    """(samples of leading silence, samples of trailing silence)."""
    a = array("h")
    a.frombytes(frames)
    n = len(a)
    lo = 0
    while lo < n and abs(a[lo]) < NOISE:
        lo += 1
    hi = n
    while hi > lo and abs(a[hi - 1]) < NOISE:
        hi -= 1
    if lo >= hi:                       # pure silence
        return n, 0
    return lo, n - hi


def normalise_silence(frames):
    """Cut or pad so the unit opens with HEAD_KEEP and closes with TAIL_KEEP seconds of
    silence. Returns (frames, shift, interior) where shift is the seconds the boundary
    offsets have to move by, because the head was re-cut, and interior is the length in
    seconds of every silent run inside the finished unit - the breaths the reader takes
    between sentences, which are the model's own and are only measured, never moved.
    Counts here are samples; frames are bytes."""
    lead, lag = head_tail(frames)
    head = int(HEAD_KEEP * SR)
    tail = int(TAIL_KEEP * SR)
    out = bytearray(frames)
    shift = 0.0
    if lead > head:
        cut = lead - head
        del out[:cut * 2]
        shift = -cut / SR
    elif lead < head:
        pad = head - lead
        out[:0] = b"\x00\x00" * pad
        shift = pad / SR
    _, lag2 = head_tail(bytes(out))
    if lag2 > tail:
        del out[len(out) - (lag2 - tail) * 2:]
    elif lag2 < tail:
        out.extend(b"\x00\x00" * (tail - lag2))
    return bytes(out), shift, interior_pauses(bytes(out))


def interior_pauses(frames):
    """Seconds of each silent run strictly inside a unit, for the breathing report."""
    a = array("h")
    a.frombytes(frames)
    runs, run = [], 0
    for v in a:
        if abs(v) < NOISE:
            run += 1
        elif run:
            if run >= int(0.15 * SR):
                runs.append(run / SR)
            run = 0
    return runs


def cue_starts(unit, bounds, dur):
    """Start second of every cue inside one rendered unit, relative to the unit start."""
    weights = [max(len(norm(p)), 1) for p in unit["parts"]]
    n = len(weights)
    if len(bounds) == n and all(b["s"] == norm(p) for b, p in zip(bounds, unit["parts"])):
        return [b["t"] for b in bounds]          # the usual case: one boundary per cue
    tot = float(sum(weights))
    if not bounds:                               # the service sent no metadata back
        acc, starts = 0.0, []
        for w in weights:
            starts.append(acc)
            acc += dur * w / tot
        return starts
    btot = float(sum(max(len(b["s"]), 1) for b in bounds))
    # boundary time spans, re-scaled onto the cue character axis
    segs_, acc = [], 0.0
    for b in bounds:
        ln = max(len(b["s"]), 1) * tot / btot
        segs_.append((acc, acc + ln, b["t"], b["t"] + b["d"]))
        acc += ln

    def at(x):
        for c0, c1, t0, t1 in segs_:
            if x <= c1:
                return t0 + (t1 - t0) * ((x - c0) / (c1 - c0) if c1 > c0 else 0.0)
        return segs_[-1][3]

    acc, starts = 0.0, []
    for w in weights:
        starts.append(min(at(acc), dur))
        acc += w
    return starts


def unit_audio(voice, unit, lang):
    """PCM frames of one unit plus the cue start times inside it, and a reason when the
    render cannot be trusted (missing, or too short to have spoken this much text)."""
    text = unit["text"]
    if not speakable(text):
        fr = b"\x00\x00" * int(SILENCE * SR)
        return fr, ramp(cue_starts(unit, [], len(fr) // 2 / SR), len(fr) // 2 / SR), None, []
    mp3 = key_of(voice, text).with_suffix(".mp3")
    if not (mp3.exists() and mp3.stat().st_size > 400):
        return None, None, "no render", []
    meta = json.loads(meta_of(voice, text).read_text(encoding="utf-8"))
    if isinstance(meta, dict):
        meta = meta.get("bounds", [])
    fr, shift, pauses = normalise_silence(wav_frames(decode_wav(mp3)))
    dur = len(fr) // 2 / SR
    exp = expect_sec(text, lang)
    if dur < MIN_FRAC * exp:
        return (None, None,
                "truncated: %.1f s of audio, needs >= %.1f s for this text" % (dur, exp), [])
    starts = ramp([s + shift for s in cue_starts(unit, meta, dur)], dur)
    return fr, starts, None, pauses


def ramp(starts, dur):
    """Cue starts the highlight can walk: non-negative, non-decreasing, inside the unit.
    The first cue opens at once so the highlight does not wait out the pad, and a unit
    whose metadata came back odd (a boundary out of order, a merge we did not expect) still
    degrades to a monotone ladder instead of a manifest that skips sentences."""
    out, prev = [], 0.0
    cap = max(dur - 0.05, 0.05)
    for k, s in enumerate(starts):
        v = 0.0 if k == 0 else min(max(s, prev + 0.05), cap)
        out.append(v)
        prev = v
    return out


def encode_ogg(wavpath, oggpath):
    oggpath.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([FFMPEG, "-y", "-v", "error", "-nostdin", "-i", str(wavpath),
                    "-c:a", "libopus", "-b:a", BITRATE, "-vbr", "on",
                    "-application", "audio", str(oggpath)], capture_output=True, check=True)


def patch_html_manifest(manifest):
    """Byte-level splice between the markers; the manifest is pure ASCII, so the rest of
    the document - which is full of Chinese - is never re-encoded."""
    BEGIN, END = b"/*AM-BEGIN*/", b"/*AM-END*/"
    blob = HTML.read_bytes()
    i, j = blob.find(BEGIN), blob.find(END)
    if i < 0 or j < 0 or j < i:
        print("manifest markers not found in the HTML - inline manifest NOT updated", flush=True)
        return False
    payload = BEGIN + b"window.AUDIO=" + json.dumps(
        manifest, ensure_ascii=True, separators=(",", ":")).encode("ascii") + b";" + END
    HTML.write_bytes(blob[:i] + payload + blob[j + len(END):])
    print("inline manifest spliced (%d bytes)" % len(payload), flush=True)
    return True


def audit(manifest, data):
    """Check the finished manifest against the queue it was built from: an entry that runs
    backwards over its neighbour, or a cue timed so far off the speaking time its own text
    calls for that the highlight would visibly race the voice or drag behind it. The yard-
    stick is expect_sec(), not a raw character count, because a section legitimately mixes
    scripts - the third-language tens carry an English line inside the Chinese track and a
    Chinese gloss inside the English one, and counting both at their own section's rate
    reads as a three-fold anomaly that is nothing of the kind. This is the check that
    catches a render the service truncated - the failure mode where audio is short but the
    text is long."""
    bad = 0
    for tid, tr in manifest["tracks"].items():
        idx = {(c["blk"], c["sub"]): c["text"] for c in data[tr["lang"]]}
        for s in tr["secs"]:
            prev, rows = -1.0, []
            for c in s["clips"]:
                if c["t"] + c["d"] > prev + 0.01 and c["t"] < prev - 0.01:
                    print("OVERLAP %s/%s blk %d sub %d t %.2f d %.2f (previous cue ended %.2f)"
                          % (tid, s["sec"], c["blk"], c["sub"], c["t"], c["d"], prev), flush=True)
                    bad += 1
                prev = max(prev, c["t"] + c["d"])
                exp = expect_sec(idx.get((c["blk"], c["sub"]), ""), tr["lang"])
                rows.append((exp / c["d"] if c["d"] else 0.0, c, round(exp, 1)))
            if len(rows) < 3:
                continue
            med = sorted(r[0] for r in rows)[len(rows) // 2]
            for ratio, c, exp in rows:
                if med and exp >= 3.0 and not (0.5 <= ratio / med <= 2.0):
                    print("SKEW %s/%s blk %d sub %d t %.2f d %.2f expected %.1f s of speech "
                          "(%s) - the highlight would visibly race or drag here"
                          % (tid, s["sec"], c["blk"], c["sub"], c["t"], c["d"], exp,
                             "%.1fx the section rate" % ratio), flush=True)
                    bad += 1
    print("audit: %d cue timings to look at" % bad, flush=True)


def run(only=None, sec_only=None, dry=False, refresh=False):
    data = extract()
    plan = []
    for tid, voice in VOICES.items():
        if only and tid not in only:
            continue
        lang = "zh" if tid.startswith("zh") else "en"
        for sec, items in groups_of(data[lang]):
            if sec_only and sec != sec_only:
                continue
            plan.append((tid, voice, lang, sec, units_of(items)))   # the unit list is what
    cues = sum(len(u["subs"]) for _, _, _, _, us in plan for u in us)   # stage 3 assembles,
    units = [(v, u) for _, v, _, _, us in plan for u in us]              # so a fallback that
    where = {}                            # (voice, text) -> where that unit is used   # splits
    for _, v, _, _, us in plan:                                          # a unit has to
        for pos, u in enumerate(us):                                     # reach the
            where.setdefault((v, u["text"]), []).append((us, pos))       # finished audio
    print("tracks %d | sections %d | cues %d | units %d (%d already rendered)" % (
        len({p[0] for p in plan}), len(plan), cues, len(units),
        sum(1 for v, u in units if has_unit(v, u["text"]))), flush=True)
    if dry:
        tid, voice, lang, sec, us = plan[0]
        print("  e.g. %s/%s: %d cues -> %d units (%s chars)" % (
            tid, sec, sum(len(u["subs"]) for u in us), len(us),
            [len(u["text"]) for u in us][:8]))
        return None

    stats = {"cached": 0, "synth": 0, "retry": 0, "silent": 0, "bounds": 0, "nocue": 0,
             "errors": [], "failures": []}

    async def pump(jobs, tag):
        sem = asyncio.Semaphore(CONCURRENCY)
        uniq = {}
        for v, u in jobs:                       # identical unit text, identical render
            uniq.setdefault((v, u["text"]), (v, u))
        todo = list(uniq.values())
        done = 0
        for fut in asyncio.as_completed([asyncio.ensure_future(
                synth_unit(sem, v, u, stats, "zh" if v.startswith("zh") else "en", refresh))
                for v, u in todo]):
            if not await fut:
                print("FAILED a unit after 5 attempts", flush=True)
            done += 1
            if done % 30 == 0 or done == len(todo):
                print("  %s %d/%d (new %d, cached %d, retries %d, silent %d)" % (
                    tag, done, len(todo), stats["synth"], stats["cached"], stats["retry"],
                    stats["silent"]), flush=True)
    asyncio.run(pump(units, "synth"))
    if stats["errors"]:
        print("last errors:", stats["errors"][:3], flush=True)

    # A unit the service keeps answering with truncated audio gets rendered one sentence at
    # a time instead: flatter cadence for that one passage than a connected render, and a
    # lot better than the silence of a dropped paragraph.
    split, passages = [], len(stats["failures"])
    for v, text in list(stats["failures"]):
        for us, pos in sorted(where.get((v, text), []), key=lambda p: -p[1]):
            u = us[pos]
            if len(u["parts"]) < 2:
                continue                      # already one sentence: nothing left to split
            parts = [{"blk": u["blk"], "subs": [s], "parts": [p], "chars": len(p), "text": p}
                     for s, p in zip(u["subs"], u["parts"])]
            us[pos:pos + 1] = parts
            split.extend((v, p) for p in parts)
    if split:
        print("%d units refused as connected text - retrying them as %d single sentences"
              % (passages, len(split)), flush=True)
        stats["failures"] = []
        asyncio.run(pump(split, "resplit"))
        if stats["failures"]:
            print("still refused: %d single sentences" % len(stats["failures"]), flush=True)
    print("units rendered %d, sentence boundaries %d, units without boundaries %d" % (
        stats["synth"] + stats["cached"] + stats["silent"], stats["bounds"], stats["nocue"]),
        flush=True)

    TMP.mkdir(exist_ok=True)
    manifest = {"format": "opus+ogg", "sr": SR, "bitrate": int(BITRATE[:-1]) * 1000,
                "dir": "assets/audio/", "tracks": {}}
    seconds = 0.0
    breaths, handovers = [], []      # measured, not asserted: see the report below
    for tid, voice, lang, sec, us in plan:
        kept, frames, clips, start = [], [], [], 0        # start counts samples, not bytes
        for ui, u in enumerate(us):
            fr, starts, why, pauses = unit_audio(voice, u, lang)
            if fr is None:                                 # no render, or one the duration
                kept.append((u["blk"], u["subs"], why))    # check refuses: drop these cues
                continue
            breaths += pauses
            n = len(fr) // 2
            if ui + 1 < len(us) and us[ui + 1]["blk"] != u["blk"]:
                fr = fr + b"\x00\x00" * int(ELEMENT_GAP * SR)   # the last cue absorbs the
                n = len(fr) // 2                                # paragraph break after it
                handovers.append(TAIL_KEEP + ELEMENT_GAP)
            for k, sub in enumerate(u["subs"]):
                s0 = int(round(starts[k] * SR))
                s1 = int(round(starts[k + 1] * SR)) if k + 1 < len(starts) else n
                s0 = min(max(s0, 0), max(n - 1, 0))
                s1 = min(max(s1, s0 + 1), n)                 # a cue runs to the next cue,
                clips.append({"blk": u["blk"], "sub": sub,   # pauses included, and never
                              "t": round((start + s0) / SR, 3),   # past the end of its unit
                              "d": round((s1 - s0) / SR, 3)})
            frames.append(fr)
            start += n
        if kept:
            print("MISSING %d units in %s/%s - rerun this script to retry" % (len(kept), tid, sec),
                  flush=True)
            for blk, subs, why in kept:
                print("   blk %d subs %s : %s" % (blk, subs, why), flush=True)
        seconds += start / SR
        master = TMP / ("%s_%s.wav" % (tid, sec))
        with wave.open(str(master), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(SR)
            w.writeframes(b"".join(frames) if frames else b"\x00\x00" * int(1.0 * SR))
        ogg = OUT / tid / ("%s.ogg" % sec)
        encode_ogg(master, ogg)
        master.unlink()
        node = manifest["tracks"].setdefault(tid, {"voice": voice, "lang": lang, "secs": [], "bytes": 0})
        node["secs"].append({"sec": sec, "file": "%s/%s.ogg" % (tid, sec), "clips": clips})
        node["bytes"] += ogg.stat().st_size
        print("%-5s %-9s %3d cues  %3d units  %6.1f s  %7d B" % (
            tid, sec, len(clips), len(us), start / SR, ogg.stat().st_size), flush=True)
    for node in manifest["tracks"].values():
        node["minutes"] = round(max((c["t"] + c["d"] for s in node["secs"] for c in s["clips"]),
                                    default=0.0) / 60, 1)
    if breaths and handovers:
        import statistics
        print("breathing: %d pauses inside a paragraph mean %.2f s (sd %.2f, max %.2f); "
              "%d paragraph breaks mean %.2f s" % (
                  len(breaths), statistics.mean(breaths), statistics.pstdev(breaths),
                  max(breaths), len(handovers), statistics.mean(handovers)), flush=True)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, separators=(",", ":")),
                                       encoding="utf-8")
    audit(manifest, data)
    print("audio rendered: %.1f min across %d tracks | %.1f MB on disk" % (
        seconds / 60, len(manifest["tracks"]),
        sum(f.stat().st_size for f in OUT.rglob("*.ogg")) / 1e6), flush=True)
    if not only and not sec_only:
        patch_html_manifest(manifest)
    return manifest


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=None, help="track ids, e.g. zh-F en-M")
    ap.add_argument("--sec", default=None, help="only this section")
    ap.add_argument("--pilot", action="store_true", help="zh-F, section books, nothing else")
    ap.add_argument("--dry", action="store_true", help="extract and measure, no audio")
    ap.add_argument("--refresh", action="store_true", help="ignore the cache, re-render units")
    a = ap.parse_args()
    if a.pilot:
        run({"zh-F"}, "books")
    else:
        run(set(a.only) if a.only else None, a.sec, a.dry, a.refresh)
