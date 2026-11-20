#!/usr/bin/env python3
"""Build blind editor briefs for one draft, then merge the editors' verdicts into one fix list.

  packet  draft.md --profile brand-profile.md [--format KEY] [--author NAME] [--out run/]
          [--editors format,structure,voice,icp,claims] [--attach structure=checks.md ...]
          Writes one brief per editor: its role, only the profile sections that editor
          needs, the draft with line numbers, and the output contract. Each editor reads
          its own brief and nothing else, so none sees another's verdict.

  merge   run/ [--prev run-1/merged.json] [--recommended-limit 5] [--max-rounds 5]
          Reads run/verdict-*.md (each must end with one ```json block), checks that every
          quoted phrase really is in the draft, dedupes findings across editors, applies
          the verdict rules and writes run/merged.md and run/merged.json for the chief editor.

Verdict rules (merge):
  REWRITE  the format editor reports format_fit "mismatch", or --rewrite-at (default 3) blocking
           findings raised by the structure or claims editor
  FIX      any blocking finding, any editor score under 6, or recommended findings >= limit
  SHIP     none of the above

Exit codes: packet 0 ok, 2 bad input. merge 0 = SHIP, 1 = FIX or REWRITE, 2 = bad input.

Examples:
  python3 review_run.py packet examples/northwind-ledger/draft-v1.md --profile examples/northwind-ledger/brand-profile.md --format guide --author "Mara Quinn" --out run-1
  python3 review_run.py merge run-1
  python3 review_run.py merge run-2 --prev run-1/merged.json
"""
import argparse
import json
import pathlib
import random
import re
import sys

EDITORS = ["format", "structure", "voice", "icp", "claims"]
PRIORITY = {e: i for i, e in enumerate(["format", "claims", "structure", "icp", "voice"])}
SECTIONS = {
    "format": ["Brand", "Audience", "Formats", "Channels"],
    "structure": ["Formats", "Links", "CTA", "Channels"],
    "voice": ["Voices", "Banned"],
    "icp": ["Brand", "Audience", "Banned"],
    "claims": ["Proof", "Banned", "Links"],
}
SEV = {"blocking": 3, "recommended": 2, "minor": 1}
CUT = re.compile(r"\b(cut|delete|remove|drop|shorten)\b", re.I)
KEEP = re.compile(r"\b(keep|expand|develop|lengthen|add more|move .* (up|earlier)|soften)\b", re.I)
STOP = set("a an the and or of to in on for with is are be this that it as at by from not no".split())

CONTRACT = """
## Output contract

Write your verdict for a human first, in the format your role gives. Then end with ONE fenced
json block, exactly this shape:

```json
{
  "editor": "%(editor)s",
  "score": 7,
  "summary": "one line",%(extra)s
  "findings": [
    {"severity": "blocking", "line": 12, "quote": "exact words from that line",
     "issue": "what is wrong, in your lane only", "fix": "the surgical change"}
  ]
}
```

- `severity`: `blocking` (breaks a rule in the profile, a wrong or unproven claim, a format
  mismatch), `recommended` (better, not gating) or `minor` (polish; logged, never re-raised).
- `quote`: 3 to 15 words copied exactly from the numbered draft, without the line number.
  Something missing? Use `"quote": ""`, `"line": 0` and name what is missing in `issue`.
- Stay in your lane. Name the location and the change; never redraft the article.
- You are blind to the other editors on purpose. Do not guess what they will say.
"""
EXTRA = {
    "format": '\n  "format_fit": "aligned or mismatch",\n  "current_format": "key",\n  "right_format": "key",',
    "voice": '\n  "author": "who you graded against",',
}


def die(msg):
    print(msg, file=sys.stderr)
    sys.exit(2)


def sections(md):
    """Split a markdown file into {H2 title: body}."""
    out, cur = {}, None
    for line in md.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m and not line.startswith("###"):
            cur = m.group(1).strip()
            out[cur] = []
            continue
        if cur is not None:
            out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def role_texts():
    ref = pathlib.Path(__file__).resolve().parent.parent / "references" / "editors.md"
    if not ref.exists():
        die(f"missing {ref}")
    roles = {}
    for title, body in sections(ref.read_text(encoding="utf-8")).items():
        key = title.split()[0].lower()
        if key in EDITORS:
            roles[key] = f"## {title}\n\n" + body.rstrip().rstrip("-").rstrip()
    return roles


def numbered(text):
    return "\n".join(f"{i:4d} | {l}" for i, l in enumerate(text.splitlines(), 1))


def cmd_packet(a):
    draft_p, prof_p = pathlib.Path(a.draft), pathlib.Path(a.profile)
    for p in (draft_p, prof_p):
        if not p.exists():
            die(f"not found: {p}")
    draft = draft_p.read_text(encoding="utf-8")
    prof = sections(prof_p.read_text(encoding="utf-8"))
    roles = role_texts()
    eds = [e.strip() for e in a.editors.split(",") if e.strip()]
    bad = [e for e in eds if e not in EDITORS]
    if bad:
        die(f"unknown editor(s): {', '.join(bad)}; choose from {', '.join(EDITORS)}")
    attach = {}
    for item in a.attach or []:
        k, _, f = item.partition("=")
        if k not in EDITORS or not pathlib.Path(f).exists():
            die(f"bad --attach {item}: use editor=existing_file")
        attach.setdefault(k, []).append(pathlib.Path(f))
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "draft.md").write_text(draft, encoding="utf-8")
    meta = {"draft": draft_p.as_posix(), "format": a.format, "author": a.author, "editors": eds}
    (out / "packet.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    for e in eds:
        parts = [f"# Brief: {e} editor\n",
                 "You are one of five independent editors. You did not write this draft and owe it nothing.",
                 "Read this brief only. Judge only your lane.\n",
                 roles.get(e, f"## {e}\n(role text missing from references/editors.md)")]
        parts.append("\n## Context")
        parts.append(f"- Declared format: {a.format or 'not given: detect it from the Formats section'}")
        if e == "voice":
            parts.append(f"- Author to grade against: {a.author or 'not given: infer it from the Voices section and say so'}")
        parts.append("\n## Brand profile (the sections your lane needs)\n")
        for s in SECTIONS[e]:
            body = prof.get(s)
            parts.append(f"### {s}\n\n{body if body else '(empty in this profile: say what you could not check)'}\n")
        for f in attach.get(e, []):
            parts.append(f"## Mechanical check output ({f.name})\n\nA script produced this. Confirm or reject each line against the draft; do not copy it blindly.\n\n```\n{f.read_text(encoding='utf-8').strip()}\n```\n")
        parts.append("## Draft (line numbers are for your quotes)\n\n```text\n" + numbered(draft) + "\n```")
        parts.append(CONTRACT % {"editor": e, "extra": EXTRA.get(e, "")})
        (out / f"brief-{e}.md").write_text("\n".join(parts), encoding="utf-8")
        print(f"wrote {(out / ('brief-' + e + '.md')).as_posix()}")
    print(f"\nNext: give each brief to a fresh subagent in ONE message, save each answer as {out.as_posix()}/verdict-<editor>.md, then run: merge {out.as_posix()}")
    return 0


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip().lower()


def words(s):
    return {w for w in re.findall(r"[a-z0-9']+", norm(s)) if w not in STOP and len(w) > 2}


def jacc(a, b):
    a, b = words(a), words(b)
    return len(a & b) / len(a | b) if a and b else 0.0


def last_json(text):
    # Decode from the last ```json marker instead of matching to the next fence:
    # editors quote code fences inside their findings, and a fence inside a string
    # would cut a regex match short.
    at = text.rfind("```json")
    if at == -1:
        return None
    start = text.find("{", at)
    if start == -1:
        return None
    try:
        obj, _ = json.JSONDecoder().raw_decode(text[start:])
        return obj
    except json.JSONDecodeError:
        return None


def locate(quote, lines, hint):
    q = norm(quote)
    if not q:
        return 0
    if 0 < hint <= len(lines) and q in norm(lines[hint - 1]):
        return hint
    for i, l in enumerate(lines, 1):
        if q in norm(l):
            return i
    joined = [norm(" ".join(lines[i:i + 5])) for i in range(len(lines))]
    for i, l in enumerate(joined, 1):
        if q in l:
            return i
    return -1


def same(f, g):
    a, b = norm(f["quote"]), norm(g["quote"])
    if a and b and len(min(a, b, key=len)) >= 8:
        if a in b or b in a:
            return True
    if f["line"] > 0 and abs(f["line"] - g["line"]) <= 1 and jacc(f["issue"], g["issue"]) >= 0.25:
        return True
    if f["line"] == 0 and g["line"] == 0 and jacc(f["issue"], g["issue"]) >= 0.35:
        return True
    return False


def cmd_merge(a):
    run = pathlib.Path(a.run)
    draft_p = run / "draft.md"
    if not draft_p.exists():
        die(f"{draft_p} missing: run packet first, or copy the reviewed draft there")
    lines = draft_p.read_text(encoding="utf-8").splitlines()
    files = sorted(run.glob("verdict-*.md"))
    if not files:
        die(f"no verdict-*.md in {run}")
    verdicts, problems = {}, []
    for f in files:
        data = last_json(f.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or "findings" not in data:
            problems.append(f"{f.name}: no valid json block at the end")
            continue
        verdicts[data.get("editor") or f.stem.split("-", 1)[1]] = data
    if problems:
        die("\n".join(problems))
    items, unverified = [], []
    for ed, v in verdicts.items():
        for raw in v.get("findings", []):
            f = {"editor": ed, "severity": str(raw.get("severity", "recommended")).lower(),
                 "line": int(raw.get("line") or 0), "quote": str(raw.get("quote") or ""),
                 "issue": str(raw.get("issue") or ""), "fix": str(raw.get("fix") or "")}
            if f["severity"] not in SEV:
                f["severity"] = "recommended"
            if not norm(f["quote"]):
                f["quote"] = ""  # a quote of only markup (a bare fence) carries no words to match
            where = locate(f["quote"], lines, f["line"]) if f["quote"] else max(f["line"], 0)
            if where == -1:
                f["demoted_from"] = f["severity"]
                f["severity"] = "recommended" if f["severity"] == "blocking" else f["severity"]
                f["unverified"] = True
                unverified.append(f)
            else:
                f["line"] = where
            items.append(f)
    merged = []
    for f in sorted(items, key=lambda x: (-SEV[x["severity"]], PRIORITY.get(x["editor"], 9), x["line"])):
        for m in merged:
            if same(f, m):
                m["editors"].append(f["editor"])
                m["fixes"].append((f["editor"], f["fix"]))
                if SEV[f["severity"]] > SEV[m["severity"]]:
                    m["severity"] = f["severity"]
                break
        else:
            merged.append({**f, "editors": [f["editor"]], "fixes": [(f["editor"], f["fix"])]})
    conflicts = []
    for m in merged:
        m["editors"] = list(dict.fromkeys(m["editors"]))
        fx = [x for x in m["fixes"] if x[1]]
        cut = {e for e, x in fx if CUT.search(x)}
        keep = {e for e, x in fx if KEEP.search(x) and not CUT.search(x)}
        if cut and keep and cut != keep:
            m["conflict"] = True
            conflicts.append(m)

    blocking = [m for m in merged if m["severity"] == "blocking"]
    recommended = [m for m in merged if m["severity"] == "recommended"]
    minor = [m for m in merged if m["severity"] == "minor"]
    fmt = verdicts.get("format", {})
    reasons = []
    if str(fmt.get("format_fit", "")).lower() == "mismatch":
        reasons.append("format editor reports a mismatch")
    sc_block = [m for m in blocking if set(m["editors"]) & {"structure", "claims"}]
    if len(sc_block) >= a.rewrite_at:
        reasons.append(f"{len(sc_block)} blocking findings from structure + claims")
    if reasons:
        verdict = "REWRITE"
    else:
        low = [e for e, v in verdicts.items() if isinstance(v.get("score"), (int, float)) and v["score"] < 6]
        if blocking:
            reasons.append(f"{len(blocking)} blocking finding(s)")
        if low:
            reasons.append("score under 6: " + ", ".join(low))
        if len(recommended) >= a.recommended_limit:
            reasons.append(f"{len(recommended)} recommended findings (limit {a.recommended_limit})")
        verdict = "FIX" if reasons else "SHIP"
        if not reasons:
            reasons.append("no blocking findings, all scores 6+, recommended under the limit")

    rnd, resolved, still = 1, [], []
    if a.prev:
        pp = pathlib.Path(a.prev)
        if not pp.exists():
            die(f"not found: {pp}")
        prev = json.loads(pp.read_text(encoding="utf-8"))
        rnd = prev.get("round", 1) + 1
        for p in prev.get("items", []):
            if p["severity"] == "minor":
                continue
            hit = any(jacc(p["issue"], m["issue"]) >= 0.3 or (p["quote"] and m["quote"] and norm(p["quote"]) == norm(m["quote"])) for m in merged)
            (still if hit else resolved).append(p)

    def fmt_item(i, m):
        loc = f"line {m['line']}" if m["line"] > 0 else "missing"
        q = f' "{m["quote"]}"' if m["quote"] else ""
        fixes = "\n     - ".join(f"{e}: {x}" for e, x in m["fixes"] if x) or "no fix given"
        if len([x for _, x in m["fixes"] if x]) > 1:
            fixes = "(pick one)\n     - " + fixes
        tag = " **[conflict]**" if m.get("conflict") else ""
        unv = " **[quote not found in draft]**" if m.get("unverified") else ""
        return f"{i}. {loc}{q} ({', '.join(m['editors'])}){tag}{unv}\n   - issue: {m['issue']}\n   - fix: {fixes}"

    title = next((l.lstrip("# ").strip() for l in lines if l.startswith("# ")), draft_p.name)
    md = [f"# Merged review: {title}", "",
          f"**Round {rnd}. Verdict proposal: {verdict}** ({'; '.join(reasons)})", "",
          "| Editor | Score | Summary |", "|---|---|---|"]
    for e in EDITORS:
        if e in verdicts:
            v = verdicts[e]
            extra = f" [{v.get('current_format')} -> {v.get('right_format')}, {v.get('format_fit')}]" if e == "format" else ""
            md.append(f"| {e} | {v.get('score', '-')} | {str(v.get('summary', '')).replace('|', '/')}{extra} |")
    missing = [e for e in EDITORS if e not in verdicts]
    if missing:
        md.append(f"\nNo verdict from: {', '.join(missing)}. The panel is incomplete; say so in the final review.")
    md += ["", f"## Blocking ({len(blocking)})", ""] + [fmt_item(i, m) for i, m in enumerate(blocking, 1)]
    md += ["", f"## Recommended ({len(recommended)})", ""] + [fmt_item(i, m) for i, m in enumerate(recommended, 1)]
    md += ["", f"## Minor ledger ({len(minor)}): logged, not re-raised", ""] + [f"- line {m['line']}: {m['issue']} ({', '.join(m['editors'])})" for m in minor]
    md += ["", f"## Conflicts for the chief editor ({len(conflicts)})", ""]
    md += [f"- line {m['line']} \"{m['quote']}\": " + " vs ".join(f"{e} wants: {x}" for e, x in m["fixes"] if x) for m in conflicts] or ["- none"]
    md += ["", f"## Findings whose quote is not in the draft ({len(unverified)})", "",
           "Demoted from blocking. The chief editor checks each by hand before using it."]
    md += [f"- {f['editor']}: \"{f['quote']}\" ({f['issue']})" for f in unverified] or ["- none"]
    if a.prev:
        md += ["", f"## Since round {rnd - 1}: {len(resolved)} resolved, {len(still)} still open", ""]
        md += [f"- resolved: {p['issue']}" for p in resolved] + [f"- STILL OPEN: {p['issue']}" for p in still]
    if rnd >= a.max_rounds and verdict != "SHIP":
        md += ["", f"**Round cap ({a.max_rounds}) reached without SHIP. Stop the loop and hand the draft and this file to a human editor.**"]
    (run / "merged.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (run / "merged.json").write_text(json.dumps({"round": rnd, "verdict": verdict, "reasons": reasons, "items": merged}, indent=2), encoding="utf-8")
    print("\n".join(md))
    return 0 if verdict == "SHIP" else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("packet", help="write one blind brief per editor")
    p.add_argument("draft")
    p.add_argument("--profile", required=True)
    p.add_argument("--format")
    p.add_argument("--author")
    p.add_argument("--out", default="review-run")
    p.add_argument("--editors", default=",".join(EDITORS))
    p.add_argument("--attach", action="append", help="editor=file: script output to show that editor")
    m = sub.add_parser("merge", help="merge verdict-*.md into one list and a verdict proposal")
    m.add_argument("run")
    m.add_argument("--prev", help="merged.json from the previous round")
    m.add_argument("--recommended-limit", type=int, default=5)
    m.add_argument("--max-rounds", type=int, default=5)
    m.add_argument("--rewrite-at", type=int, default=3, help="blocking items from structure + claims that make it REWRITE")
    a = ap.parse_args()
    random.seed(0)
    sys.exit(cmd_packet(a) if a.cmd == "packet" else cmd_merge(a))


if __name__ == "__main__":
    main()
