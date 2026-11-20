"""Shared helpers: read limits out of brand-profile.md and split a draft into parts.

brand-profile.md keeps human prose and a few machine lines of the form `- key: value`.
Only those lines are read here; everything else is for the editors.
"""
import pathlib
import re

DEFAULTS = {
    "title_max": 70,
    "description_max": 155,
    "paragraph_max_sentences": 4,
    "h2_max": 6,
    "words": "800-2000",
    "summary_bullets": "3-6",
}


def sections(md, level=2):
    marker = "#" * level + " "
    out, cur = {}, None
    for line in md.splitlines():
        if line.startswith(marker):
            cur = line[len(marker):].strip()
            out[cur] = []
        elif cur is not None:
            if level == 2 or not line.startswith("#" * (level - 1) + " "):
                out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def keyvals(text):
    kv = {}
    for m in re.finditer(r"^\s*-\s*([a-z_]+)\s*:\s*(.+?)\s*$", text or "", re.M):
        kv[m.group(1)] = m.group(2)
    return kv


def load(profile_path, fmt=None):
    """Return (limits, profile_sections). Format block overrides channel defaults."""
    limits = dict(DEFAULTS)
    if not profile_path:
        return limits, {}
    md = pathlib.Path(profile_path).read_text(encoding="utf-8")
    secs = sections(md)
    limits.update(keyvals(secs.get("Channels", "")))
    for k, v in keyvals(secs.get("CTA", "")).items():
        limits["cta_" + k] = v
    limits["banned"] = [b.strip().strip('"').lower() for b in re.findall(r"^\s*-\s*(.+)$", secs.get("Banned", ""), re.M)
                        if ":" not in b[:15]]
    if fmt:
        fsecs = sections(secs.get("Formats", ""), level=3)
        block = next((v for k, v in fsecs.items() if k.split()[0].lower() == fmt.lower()), None)
        if block is None:
            raise SystemExit(f"format '{fmt}' not found under '## Formats' in {profile_path}; have: {', '.join(k.split()[0] for k in fsecs)}")
        limits.update(keyvals(block))
    return limits, secs


def band(value):
    a, _, b = str(value).partition("-")
    return int(a), int(b or a)


def parse_draft(text):
    """Return dict: meta (front matter), lines, title, body_lines (with original line numbers)."""
    lines = text.splitlines()
    meta, start = {}, 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                for l in lines[1:i]:
                    k, _, v = l.partition(":")
                    if v:
                        meta[k.strip().lower()] = v.strip().strip('"')
                start = i + 1
                break
    title = meta.get("title")
    title_line = 1 if title else 0
    for i in range(start, len(lines)):
        if lines[i].startswith("# "):
            if not title:
                title, title_line = lines[i][2:].strip(), i + 1
            break
    return {"meta": meta, "lines": lines, "start": start, "title": title or "", "title_line": title_line}


def paragraphs(lines, start=0):
    """Yield (first_line_no, text) for prose paragraphs, skipping code, tables, lists, headings."""
    buf, first, in_code = [], 0, False
    for i in range(start, len(lines)):
        l = lines[i]
        if l.strip().startswith("```"):
            in_code = not in_code
            if buf:
                yield first, " ".join(buf)
                buf = []
            continue
        prose = l.strip() and not in_code and not re.match(r"^\s*(#|\||[-*+] |\d+\. |>|!\[|<)", l)
        if prose:
            if not buf:
                first = i + 1
            buf.append(l.strip())
        elif buf:
            yield first, " ".join(buf)
            buf = []
    if buf:
        yield first, " ".join(buf)


def sentences(text):
    text = re.sub(r"\b(e\.g|i\.e|vs|etc|approx|Inc|Ltd)\.", r"\1", text)
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", text) if s.strip()]
