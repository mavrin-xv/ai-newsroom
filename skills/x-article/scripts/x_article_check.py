#!/usr/bin/env python3
"""Check an X long-form article draft for the things that are measurable before you paste it.

Reads a markdown draft (front matter optional: title, cover). Checks:
  title      length (default max 100 characters) and whether it carries a figure
  hook       the first prose line is not a definition or throat-clearing
  cover      image ratio is 5:2 (PNG or JPEG read from disk, or `cover_size: 1500x600`)
  paragraphs no prose paragraph over --max-sentences (default 3)
  links      at most one link per paragraph
  cta        links to the CTA url (from --profile or --cta) within the profile's max
  artifact   at least one code block, checklist or numbered list the reader can copy
  length     words inside the band of the profile's `### x-article` block (skipped without one)
  banned     none of the profile's banned list

Usage:
  python3 x_article_check.py draft.md [--profile brand-profile.md] [--cta URL]
        [--title-max 100] [--max-sentences 3] [--cover cover.png] [--json]

Exit codes: 0 no FAIL, 1 any FAIL, 2 bad input. WARN never fails.

Example:
  python3 x_article_check.py examples/northwind-ledger/x-article.md --profile examples/northwind-ledger/brand-profile.md
"""
import argparse
import json
import pathlib
import re
import struct
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent / "newsroom-review" / "scripts"))
import newsroom_profile as P  # noqa: E402

WEAK_OPEN = re.compile(r"^(in today's|in this (article|post|thread)|let's (dive|explore|talk)|have you ever|imagine|[A-Z][\w-]*( [\w-]+){0,3} (is|are|refers to) (a|an|the)\b)", re.I)
LINK = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)|(?<![(\w])(https?://[^\s)]+)")
FIGURE = re.compile(r"\d|\$")


def image_size(path):
    data = pathlib.Path(path).read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    if data[:2] == b"\xff\xd8":
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return w, h
            i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("draft")
    ap.add_argument("--profile")
    ap.add_argument("--cta", help="CTA url, if not in the profile")
    ap.add_argument("--title-max", type=int, default=100)
    ap.add_argument("--max-sentences", type=int, default=3)
    ap.add_argument("--cover", help="cover image file (PNG or JPEG)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        text = pathlib.Path(a.draft).read_text(encoding="utf-8")
        lim, has_block = dict(P.DEFAULTS), False
        if a.profile:
            try:
                lim, has_block = P.load(a.profile, "x-article")[0], True
            except SystemExit:  # no x-article block: channel rules only, no length band
                lim = P.load(a.profile)[0]
    except (OSError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    d = P.parse_draft(text)
    lines, rows = d["lines"], []

    def add(item, ok, line, detail):
        rows.append({"item": item, "result": ok, "line": line, "detail": detail})

    t = d["title"]
    if not t:
        add("title", "FAIL", "-", "no title in front matter or H1")
    else:
        add("title", "PASS" if len(t) <= a.title_max else "FAIL", d["title_line"], f"{len(t)} chars (max {a.title_max})")
        if not FIGURE.search(t):
            add("title figure", "WARN", d["title_line"], "no number in the title; borrow a named source or state the outcome instead")

    paras = list(P.paragraphs(lines, d["start"]))
    if paras:
        n, first = paras[0]
        add("hook", "FAIL" if WEAK_OPEN.match(first) else "PASS", n, "opens on a definition or throat-clearing" if WEAK_OPEN.match(first) else "opens on a claim, number or scene")

    cover, size = a.cover or d["meta"].get("cover"), d["meta"].get("cover_size")
    if cover and not size:
        p = pathlib.Path(cover)
        if not p.is_absolute():
            p = pathlib.Path(a.draft).resolve().parent / p
        try:
            wh = image_size(p)
            size = f"{wh[0]}x{wh[1]}" if wh else None
        except OSError:
            add("cover", "FAIL", "-", f"cover file not found: {cover}")
    if size:
        w, _, h = size.partition("x")
        ratio = int(w) / int(h)
        add("cover", "PASS" if abs(ratio - 2.5) < 0.03 else "FAIL", "-", f"{size}, ratio {ratio:.2f} (want 5:2 = 2.50)")
    elif not cover:
        add("cover", "WARN", "-", "no cover given; X shows a 5:2 cover above the title")

    long_p = [(n, len(P.sentences(p))) for n, p in paras if len(P.sentences(p)) > a.max_sentences]
    add("paragraphs", "FAIL" if long_p else "PASS", long_p[0][0] if long_p else "-",
        f"{len(long_p)} over {a.max_sentences} sentences, first at line {long_p[0][0]}" if long_p else f"all within {a.max_sentences} sentences")

    multi = [n for n, p in paras if len(LINK.findall(p)) > 1]
    add("links", "FAIL" if multi else "PASS", multi[0] if multi else "-", f"{len(multi)} paragraphs with more than one link" if multi else "at most one link per paragraph")

    cta = a.cta or lim.get("cta_url")
    if cta:
        lo, hi = 1, int(lim.get("cta_max", 2))
        n = text.count(cta.rstrip("/"))
        add("cta", "PASS" if lo <= n <= hi else "FAIL", "-", f"{n} links to the CTA url (want {lo}-{hi})")
    else:
        add("cta", "WARN", "-", "no CTA url in the profile or --cta")

    body = "\n".join(lines[d["start"]:])
    has_artifact = "```" in body or re.search(r"^\s*(\d+\. |- \[ \])", body, re.M)
    add("artifact", "PASS" if has_artifact else "WARN", "-", "has a block the reader can copy" if has_artifact else "no code block, checklist or numbered list")

    if has_block and "words" in lim:
        lo, hi = P.band(lim["words"])
        words = len(re.findall(r"[\w'-]+", re.sub(r"```.*?```", "", body, flags=re.S)))
        add("length", "PASS" if lo <= words <= hi else "FAIL", "-", f"{words} words (band {lo}-{hi})")

    hits = [w for w in lim.get("banned", []) if re.search(r"\b" + re.escape(w) + r"\b", text, re.I)]
    add("banned", "FAIL" if hits else "PASS", "-", ", ".join(hits) if hits else "none of the profile's banned list")

    fails = sum(r["result"] == "FAIL" for r in rows)
    if a.json:
        print(json.dumps({"draft": a.draft, "fail": fails, "rows": rows}, indent=2))
    else:
        print(f"x_article_check: {pathlib.Path(a.draft).name}")
        print("| Item | Result | Line | Detail |\n|---|---|---|---|")
        for r in rows:
            print(f"| {r['item']} | {r['result']} | {r['line']} | {r['detail']} |")
        warns = sum(r["result"] == "WARN" for r in rows)
        print(f"\n{fails} FAIL, {warns} WARN, {len(rows) - fails - warns} PASS")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
