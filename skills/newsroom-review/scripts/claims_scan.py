#!/usr/bin/env python3
"""List every checkable claim in a draft and say whether a source sits next to it.

A claim is a sentence with a number, a percentage, a multiplier (3x), a money amount, a year,
a superlative ("fastest", "the only", "#1", "best") or a research phrase ("studies show",
"according to", "research"). A claim counts as sourced when the same sentence has a markdown
link or a footnote marker, or when its figure appears in the sources file.

The script does not decide truth. It builds the claims table so the claims auditor starts from
a complete list instead of from what it happened to notice.

Usage:
  python3 claims_scan.py draft.md [--sources sources.md] [--profile brand-profile.md] [--json]

sources.md is a markdown table whose first column is the figure as written in the draft
(for example `| 38% | survey of 412 users, 2026-03 | https://... |`). See templates/sources.md.

Also flags the same metric word with two different figures (for example "close time" given as
9 days in one place and 7 in another).

Exit codes: 0 every claim sourced, 1 at least one unsourced claim, 2 bad input.

Example:
  python3 claims_scan.py examples/northwind-ledger/draft-v1.md --sources examples/northwind-ledger/sources.md --profile examples/northwind-ledger/brand-profile.md
"""
import argparse
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import newsroom_profile as P  # noqa: E402

NUM = re.compile(r"(?<![\w.])(?:[$€£]\s?\d[\d,.]*\s?[kKmMbB]?|\d[\d,.]*\s?(?:%|x\b|times\b|percent\b)|\d[\d,.]*)")
SUPER = re.compile(r"\b(fastest|cheapest|best|the only|leading|the first (?:to|company|tool|platform|product)|#1|number one|the most \w+|the least \w+|unmatched|unrivalled|industry-leading|world-class|best-in-class)\b", re.I)
MULT = re.compile(r"\b(in half|halved?|doubled?|tripled?|twice as|three times)\b", re.I)
UNIT = re.compile(r"^\s?-?\s?(%|x\b|times|percent|days?|working days|hours?|minutes?|weeks?|months?|years?|people|customers|users|teams)", re.I)
RESEARCH = re.compile(r"\b(studies show|research shows|according to|data shows|surveys? (show|found)|experts say|it is known)\b", re.I)
VAGUE = re.compile(r"\b(much|significantly|dramatically|substantially|far) (faster|cheaper|better|more|less|higher|lower)\b|\b(most|many) (teams|companies|businesses|users|people)\b", re.I)
SOURCE = re.compile(r"\]\(https?://|\[\^\w+\]|\(source:|\bsource:\s", re.I)
METRIC = re.compile(r"(\d[\d,.]*)\s?(%|days?|hours?|minutes?|weeks?|x\b)?\s+(?:of |in |for |to )?(?:the )?([a-z][a-z-]+(?: [a-z][a-z-]+)?)", re.I)


def figures(sentence):
    out = [m.group(0).lower() for m in MULT.finditer(sentence)]
    for m in NUM.finditer(sentence):
        f = m.group(0).strip().rstrip(".,")
        if re.fullmatch(r"\d", f) and not UNIT.match(sentence[m.end():]) and not re.search(r"(from|to)\s$", sentence[:m.start()]):
            continue
        if re.fullmatch(r"(19|20)\d\d", f):
            out.append(f)
            continue
        out.append(f)
    return out


def load_sources(path):
    if not path:
        return set()
    figs = set()
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            cell = line.strip("|").split("|")[0].strip().strip("`")
            if cell and cell.lower() not in ("figure", "claim"):
                figs.add(cell.lower())
    return figs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft")
    ap.add_argument("--sources")
    ap.add_argument("--profile", help="brand-profile.md: links to its CTA url do not count as a source")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    p = pathlib.Path(a.draft)
    if not p.exists() or (a.sources and not pathlib.Path(a.sources).exists()):
        print("draft or sources file not found", file=sys.stderr)
        sys.exit(2)
    d = P.parse_draft(p.read_text(encoding="utf-8"))
    srcs = load_sources(a.sources)
    cta = P.load(a.profile)[0].get("cta_url", "") if a.profile else ""
    rows, seen_metric = [], {}
    in_code = False
    for i, line in enumerate(d["lines"]):
        if i < d["start"]:
            continue
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or line.startswith("#") or not line.strip():
            continue
        for s in P.sentences(re.sub(r"^\s*([-*]|\d+\.)\s+", "", line)):
            plain = re.sub(r"\]\([^)]*\)", "]", s)
            figs = figures(plain)
            kinds = []
            if figs:
                kinds.append("number")
            if SUPER.search(plain):
                kinds.append("superlative")
            if RESEARCH.search(plain):
                kinds.append("research")
            if VAGUE.search(plain):
                kinds.append("vague")
            if not kinds:
                continue
            s_links = s.replace("](" + cta + ")", "]") if cta else s
            linked = bool(SOURCE.search(s_links))
            # A figure counts as filed when the sources table has it exactly, or when a
            # filed figure of 3+ characters ("9 working days", "day 10") is in the sentence.
            in_file = any(f.lower() in srcs for f in figs) or any(len(x) >= 3 and x in plain.lower() for x in srcs)
            status = "sourced" if linked or in_file else ("unsourced" if kinds != ["vague"] else "vague")
            if "vague" in kinds and not figs:
                status = "vague"
            rows.append({"line": i + 1, "kinds": kinds, "figures": figs, "status": status,
                         "via": "link" if linked else ("sources file" if in_file else ""), "text": s.strip()[:160]})
            for m in METRIC.finditer(plain):
                key = m.group(3).lower()
                val = m.group(1) + (m.group(2) or "")
                if key in ("the", "and", "of"):
                    continue
                seen_metric.setdefault(key, set()).add((val, i + 1))
    conflicts = []
    for key, vals in seen_metric.items():
        uniq = {v for v, _ in vals}
        if len(uniq) > 1 and len(key) > 3:
            conflicts.append({"metric": key, "values": sorted(f"{v} (line {n})" for v, n in vals)})
    bad = [r for r in rows if r["status"] != "sourced"]
    if a.json:
        print(json.dumps({"draft": str(p), "claims": rows, "conflicts": conflicts, "unsourced": len(bad)}, indent=2))
    else:
        print(f"claims_scan: {p.name}, {len(rows)} claims, {len(bad)} not sourced")
        print("| Line | Kind | Status | Claim |\n|---|---|---|---|")
        for r in rows:
            print(f"| {r['line']} | {', '.join(r['kinds'])} | {r['status']}{(' via ' + r['via']) if r['via'] else ''} | {r['text'].replace('|', '/')} |")
        if conflicts:
            print("\nSame metric, different figures (check which is right):")
            for c in conflicts:
                print(f"- {c['metric']}: {', '.join(c['values'])}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
