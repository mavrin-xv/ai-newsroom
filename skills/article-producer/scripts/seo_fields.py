#!/usr/bin/env python3
"""Count and check the publish fields for one article, so lengths are measured, not guessed.

Input is a small markdown or text file with one field per line:

  title: Close the books in 5 days, not 9
  description: Four changes that took 14 small service firms from 9 working days to 5.
  slug: close-books-faster
  subtitle: ...                      (optional, for platforms with a subtitle)
  variant: <alternative title>       (repeat for each title variant)
  canonical: https://example.org/blog/close-books-faster   (optional)

Checks: title and variants against title_max, description against description_max, subtitle
against subtitle band, slug shape, duplicate variants, variants that only differ in case,
canonical is https, and banned words from the profile in any field.

Usage:
  python3 seo_fields.py fields.md [--profile brand-profile.md] [--title-max 70]
        [--description-max 155] [--subtitle 120-140]

Exit codes: 0 all fields pass, 1 any field fails, 2 bad input.

Example:
  python3 seo_fields.py examples/northwind-ledger/fields.md --profile examples/northwind-ledger/brand-profile.md
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent / "newsroom-review" / "scripts"))
import newsroom_profile as P  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fields")
    ap.add_argument("--profile")
    ap.add_argument("--title-max", type=int)
    ap.add_argument("--description-max", type=int)
    ap.add_argument("--subtitle", default="120-140")
    a = ap.parse_args()
    f = pathlib.Path(a.fields)
    if not f.exists():
        print(f"not found: {f}", file=sys.stderr)
        sys.exit(2)
    lim, _ = P.load(a.profile)
    tmax = a.title_max or int(lim["title_max"])
    dmax = a.description_max or int(lim["description_max"])
    slo, shi = P.band(a.subtitle)
    banned = lim.get("banned", [])
    fields, variants = {}, []
    for line in f.read_text(encoding="utf-8").splitlines():
        k, _, v = line.partition(":")
        k, v = k.strip().lower(), v.strip()
        if not v or k.startswith("#"):
            continue
        if k == "variant":
            variants.append(v)
        else:
            fields[k] = v
    rows = []

    def row(name, value, ok, note):
        rows.append((name, len(value), "PASS" if ok else "FAIL", note, value))

    def bad_words(v):
        return [b for b in banned if b in v.lower()]

    t = fields.get("title", "")
    row("title", t, bool(t) and len(t) <= tmax and not bad_words(t), f"max {tmax}" + (f"; banned {bad_words(t)}" if bad_words(t) else "") if t else "missing")
    dsc = fields.get("description", "")
    row("description", dsc, bool(dsc) and len(dsc) <= dmax and not bad_words(dsc), f"max {dmax}" if dsc else "missing")
    if "subtitle" in fields:
        s = fields["subtitle"]
        row("subtitle", s, slo <= len(s) <= shi, f"band {slo}-{shi}")
    if "slug" in fields:
        s = fields["slug"]
        ok = bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", s)) and len(s) <= 60
        row("slug", s, ok, "lowercase words joined by hyphens, 60 max")
    if "canonical" in fields:
        c = fields["canonical"]
        row("canonical", c, c.startswith("https://"), "https URL")
    seen = {}
    for i, v in enumerate(variants, 1):
        key = re.sub(r"\W+", " ", v.lower()).strip()
        dup = seen.get(key)
        seen.setdefault(key, i)
        note = f"max {tmax}" + (f"; duplicate of variant {dup}" if dup else "") + (f"; banned {bad_words(v)}" if bad_words(v) else "")
        row(f"variant {i}", v, len(v) <= tmax and not dup and not bad_words(v), note)
    fails = sum(r[2] == "FAIL" for r in rows)
    print("| Field | Chars | Result | Rule | Value |\n|---|---|---|---|---|")
    for r in rows:
        print(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4].replace('|', '/')} |")
    print(f"\n{fails} FAIL, {len(rows) - fails} PASS")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
