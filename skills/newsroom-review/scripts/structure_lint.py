#!/usr/bin/env python3
"""Mechanical structure check for a markdown draft. Counts what a script can count, so the
structure editor spends its attention on judgement instead of on counting H2s.

Usage:
  python3 structure_lint.py draft.md [--profile brand-profile.md] [--format KEY] [--json]

Limits come from the profile: `## Channels` (title_max, description_max,
paragraph_max_sentences) and the `### <format>` block under `## Formats` (words, h2_max,
summary_bullets, requires). Without a profile the defaults in newsroom_profile.py apply.

Checks: title length and banned openers; description present and under the limit; summary block
bullet count; H2 count and banned H2 names; opening line type; code fences without a language;
images without alt text; long paragraphs; word band; required sections; a CTA link in the last
section; exclamation marks and padding connectives.

Exit codes: 0 all PASS, 1 one or more FAIL, 2 bad input.

Example:
  python3 structure_lint.py examples/northwind-ledger/draft-v1.md --profile examples/northwind-ledger/brand-profile.md --format guide
"""
import argparse
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import newsroom_profile as P  # noqa: E402

BAD_TITLE = re.compile(r"^(an? )?(introduction to|guide to|the ultimate|ultimate guide|everything you need to know|a complete guide|all about)\b", re.I)
BAD_H2 = re.compile(r"^(introduction|intro|overview|conclusion|conclusions|final thoughts|summary|wrapping up|in conclusion)\s*$", re.I)
SUMMARY_H = re.compile(r"^(tl;?dr|key takeaways|in short|the short version|summary)\b", re.I)
WEAK_OPEN = re.compile(r"^(in today's|in this (article|post|guide)|let's (dive|explore|talk)|have you ever|imagine|[A-Z][\w-]*( [\w-]+){0,3} (is|are|refers to) (a|an|the)\b)", re.I)
PADDING = re.compile(r"\b(Additionally|Moreover|Furthermore|It is worth noting|It's worth noting|Needless to say)\b")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft")
    ap.add_argument("--profile")
    ap.add_argument("--format")
    ap.add_argument("--json", action="store_true", help="print machine output instead of a table")
    a = ap.parse_args()
    p = pathlib.Path(a.draft)
    if not p.exists():
        print(f"not found: {p}", file=sys.stderr)
        sys.exit(2)
    lim, _ = P.load(a.profile, a.format)
    d = P.parse_draft(p.read_text(encoding="utf-8"))
    lines, start = d["lines"], d["start"]
    rows = []

    def add(item, ok, line, detail):
        rows.append({"item": item, "result": "PASS" if ok else "FAIL", "line": line, "detail": detail})

    t = d["title"]
    tmax = int(lim["title_max"])
    add("title", bool(t) and len(t) <= tmax and not BAD_TITLE.search(t), d["title_line"],
        f"{len(t)} chars (max {tmax})" + ("; banned opener" if BAD_TITLE.search(t) else "") if t else "no title")

    desc = d["meta"].get("description", "")
    dmax = int(lim["description_max"])
    add("description", bool(desc) and len(desc) <= dmax, 1 if desc else 0,
        f"{len(desc)} chars (max {dmax})" if desc else "no description in front matter")

    h2 = [(i + 1, l[3:].strip()) for i, l in enumerate(lines) if l.startswith("## ")]
    summ = next(((n, h) for n, h in h2 if SUMMARY_H.match(h)), None)
    bl, bh = P.band(lim["summary_bullets"])
    if summ:
        j, bullets = summ[0], 0
        while j < len(lines) and not lines[j].startswith("## "):
            bullets += bool(re.match(r"^\s*[-*] ", lines[j]))
            j += 1
        add("summary block", bl <= bullets <= bh, summ[0], f"{bullets} bullets (want {bl}-{bh})")
    elif str(lim.get("summary", "")).lower().startswith("req"):
        add("summary block", False, 0, "format requires one, none found")

    body_h2 = [(n, h) for n, h in h2 if not SUMMARY_H.match(h)]
    hmax = int(lim["h2_max"])
    banned = [f"line {n} '{h}'" for n, h in body_h2 if BAD_H2.match(h)]
    add("headings", len(body_h2) <= hmax and not banned, body_h2[0][0] if body_h2 else 0,
        f"{len(body_h2)} H2 (max {hmax}, summary block not counted)" + (f"; banned: {', '.join(banned)}" if banned else ""))

    req = [r.strip() for r in str(lim.get("requires", "")).split(",") if r.strip()]
    missing = [r for r in req if not any(r.lower() in h.lower() for _, h in h2)]
    if req:
        add("template", not missing, 0, "missing: " + ", ".join(missing) if missing else f"has {', '.join(req)}")

    first = next(P.paragraphs(lines, start), None)
    if first:
        weak = WEAK_OPEN.match(first[1])
        add("hook", not weak, first[0], f"opens with '{weak.group(0)}'" if weak else "opening is not a definition or throat-clearing")

    fences = [i + 1 for i, l in enumerate(lines) if l.strip().startswith("```")]
    opens = fences[0::2]
    bare = [n for n in opens if lines[n - 1].strip() == "```"]
    noalt = [i + 1 for i, l in enumerate(lines) if "![](" in l]
    if opens or noalt or "|" in "".join(lines):
        add("code and media", not bare and not noalt, (bare or noalt or [0])[0],
            "; ".join(x for x in [f"code without language at {bare}" if bare else "", f"image without alt at {noalt}" if noalt else ""] if x) or "labelled")

    cap = int(lim["paragraph_max_sentences"])
    long_p = [(n, len(P.sentences(tx))) for n, tx in P.paragraphs(lines, start) if len(P.sentences(tx)) > cap]
    add("paragraphs", not long_p, long_p[0][0] if long_p else 0,
        ", ".join(f"line {n}: {c} sentences" for n, c in long_p) + f" (max {cap})" if long_p else f"all within {cap} sentences")

    text = "\n".join(l for l in lines[start:] if not l.strip().startswith("```"))
    wc = len(re.findall(r"[A-Za-z0-9][\w'-]*", re.sub(r"```.*?```", "", "\n".join(lines[start:]), flags=re.S)))
    wl, wh = P.band(lim["words"])
    add("length", wl <= wc <= wh, 0, f"{wc} words (band {wl}-{wh})")

    url = lim.get("cta_url", "")
    if h2:
        last = h2[-1][0]
        tail = "\n".join(lines[last - 1:])
        has_link = (url and url in tail) or (not url and re.search(r"\]\(https?://", tail))
        add("close", bool(has_link) and not BAD_H2.match(h2[-1][1]), last,
            f"last H2 '{h2[-1][1]}'" + ("" if has_link else f"; no CTA link{(' to ' + url) if url else ''}"))
        if url:
            n_cta = text.count(url)
            cmax = int(lim.get("cta_max", 2))
            add("cta count", 1 <= n_cta <= cmax, 0, f"{n_cta} links to the CTA url (want 1-{cmax})")

    excl = [i + 1 for i, l in enumerate(lines) if i >= start and re.search(r"\w!(\s|$)", l) and not l.strip().startswith(("```", "    "))]
    pad = [(i + 1, m.group(0)) for i, l in enumerate(lines) for m in PADDING.finditer(l)]
    add("punctuation and padding", not excl and not pad, (excl or [n for n, _ in pad] or [0])[0],
        "; ".join(x for x in [f"'!' at lines {excl}" if excl else "", "padding: " + ", ".join(f"{w} (line {n})" for n, w in pad) if pad else ""] if x) or "none")

    ban = [b for b in lim.get("banned", []) if b and b in text.lower()]
    if lim.get("banned"):
        add("banned words", not ban, 0, "found: " + ", ".join(ban) if ban else "none of the profile's banned list")

    fails = sum(r["result"] == "FAIL" for r in rows)
    if a.json:
        print(json.dumps({"draft": str(p), "fails": fails, "rows": rows}, indent=2))
    else:
        print(f"structure_lint: {p.name}" + (f" (format {a.format})" if a.format else ""))
        print("| Item | Result | Line | Detail |\n|---|---|---|---|")
        for r in rows:
            print(f"| {r['item']} | {r['result']} | {r['line'] or '-'} | {r['detail']} |")
        print(f"\n{fails} FAIL, {len(rows) - fails} PASS")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
