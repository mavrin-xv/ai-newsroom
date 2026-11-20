#!/usr/bin/env python3
"""Check every link in a draft against the allowed list in the brand profile.

The usual failure is a guessed internal slug: the writer links /blog/receipt-policy because it
sounds right, and the real page is /blog/receipt-rules. This script never fetches anything. It
compares each link with the `## Links` and `## CTA` sections of brand-profile.md and reports:

  allowed   the URL is on the list
  external  another domain (fine, but the claims auditor should see it as a source)
  unknown   same domain as a listed page, not on the list: likely a guessed slug
  bare      a raw URL with no anchor text

Also counts internal links against --min-internal and CTA links against the CTA max.

Usage:
  python3 link_check.py draft.md --profile brand-profile.md [--min-internal 2]

Exit codes: 0 no unknown links and counts within limits, 1 otherwise, 2 bad input.

Example:
  python3 link_check.py examples/northwind-ledger/draft-v2.md --profile examples/northwind-ledger/brand-profile.md
"""
import argparse
import pathlib
import re
import sys
from urllib.parse import urlparse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent / "newsroom-review" / "scripts"))
import newsroom_profile as P  # noqa: E402

LINK = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
BARE = re.compile(r"(?<![(\[<])\bhttps?://[^\s)>\]]+")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft")
    ap.add_argument("--profile", required=True)
    ap.add_argument("--min-internal", type=int, default=1)
    a = ap.parse_args()
    d, pf = pathlib.Path(a.draft), pathlib.Path(a.profile)
    if not d.exists() or not pf.exists():
        print("draft or profile not found", file=sys.stderr)
        sys.exit(2)
    lim, secs = P.load(pf)
    allowed = set(re.findall(r"https?://[^\s)|>]+", secs.get("Links", "")))
    cta = lim.get("cta_url", "")
    if cta:
        allowed.add(cta)
    hosts = {urlparse(u).netloc for u in allowed}
    lines = d.read_text(encoding="utf-8").splitlines()
    rows, internal, cta_n = [], 0, 0
    for i, l in enumerate(lines, 1):
        for text, url in LINK.findall(l):
            u = url.rstrip(".,")
            host = urlparse(u).netloc
            if u in allowed or u.rstrip("/") in {x.rstrip("/") for x in allowed}:
                kind = "allowed"
            elif host in hosts:
                kind = "unknown"
            else:
                kind = "external"
            if host in hosts:
                internal += 1
            if cta and u.rstrip("/") == cta.rstrip("/"):
                cta_n += 1
            rows.append((i, kind, text or "(no anchor text)", u))
        for u in BARE.findall(LINK.sub("", l)):
            rows.append((i, "bare", "", u))
    cmax = int(lim.get("cta_max", 2))
    problems = [r for r in rows if r[1] in ("unknown", "bare")]
    print("| Line | Kind | Anchor | URL |\n|---|---|---|---|")
    for r in rows:
        print(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |")
    print(f"\ninternal links: {internal} (min {a.min_internal}); CTA links: {cta_n} (want 1-{cmax}); unknown or bare: {len(problems)}")
    ok = not problems and internal >= a.min_internal and (not cta or 1 <= cta_n <= cmax)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
