---
name: newsroom-review
description: Reviews a draft article, blog post, case study or X long-form with five blind editors (format, structure, voice, reader fit, claims) running in parallel, then a chief editor merges their notes into one deduplicated fix list and a SHIP, FIX or REWRITE verdict. Checks every quoted line against the draft and loops until SHIP or a round cap. Use when someone asks to review, edit, critique, fact-check or approve a draft before publishing, says "is this ready", "run the editors", "editorial review", "newsroom review", or pastes a draft from a writer.
---

# Newsroom review

One draft, five editors who cannot see each other, one arbiter. The editors disagree where the
draft is ambiguous; the arbiter turns that into one list a writer can fix in one pass.

**Do not review the draft yourself first.** Your read anchors everything after it. Build the
packet, spawn the editors, and read only what they return.

## Inputs

- The draft as a markdown file. Front matter `title:` and `description:` if the channel needs them.
- `brand-profile.md` (template: `templates/brand-profile.md`; fill it with `newsroom-setup`).
  Without one, run with the defaults and say in the review that the brand rules were not checked.
- Optional: the format key (`guide`, `comparison`, `case`, `x-article` or one of yours), the author
  name, and `sources.md` (template: `templates/sources.md`).

## Procedure

### 1. Mechanical checks (no judgement yet)

```bash
S=skills/newsroom-review/scripts
python3 $S/structure_lint.py draft.md --profile brand-profile.md --format guide > run-1/structure-lint.txt
python3 $S/claims_scan.py draft.md --sources sources.md --profile brand-profile.md > run-1/claims-scan.txt
```

Both exit 1 when they find something. That is expected; they feed the editors, they do not gate.

### 2. Build the blind briefs

```bash
python3 $S/review_run.py packet draft.md --profile brand-profile.md --format guide \
  --author "Author Name" --out run-1 \
  --attach structure=run-1/structure-lint.txt --attach claims=run-1/claims-scan.txt
```

This writes `run-1/brief-<editor>.md` for each of the five editors. Each brief has the editor's role
from `references/editors.md`, only the profile sections that lane needs, the draft with line
numbers, and the output contract (human verdict plus one json block).

### 3. Spawn five editors in ONE message

Send five subagent calls in a single message so they run in parallel and none sees another's output.
Each gets the same instruction:

> Read exactly one file: `run-1/brief-<editor>.md`. Do not read any other file. Follow it and write
> your verdict to `run-1/verdict-<editor>.md`. Reply with one line.

Rules:
- Fresh subagents only. Never the agent that wrote the draft, never one that has seen another verdict.
- Read-only on the draft. Editors name locations and changes; they do not edit.
- If the host cannot spawn subagents, run the five briefs in five separate turns, clear your notes
  between them, and mark the final review **single-context, degraded**. The panel is weaker this way
  because later editors remember earlier ones.

### 4. Merge

```bash
python3 $S/review_run.py merge run-1
```

The script reads the five json blocks and:
- checks each quoted phrase against the draft; a quote that is not there is demoted from blocking;
- groups findings that point at the same words or the same missing thing;
- lists conflicts, where two editors want different fixes for one item;
- proposes a verdict (exit 0 SHIP, 1 FIX or REWRITE):

| Verdict | Rule |
|---|---|
| REWRITE | format editor reports a mismatch, or 3+ blocking items from structure and claims |
| FIX | any blocking item, any score under 6, or 5+ recommended items |
| SHIP | none of the above |

Output: `run-1/merged.md` (for the chief editor) and `run-1/merged.json` (for the next round).

### 5. Chief editor

Spawn one more fresh subagent with `references/chief-editor.md`, `run-1/merged.md`, the five
verdict files and the draft. It confirms each blocking item against the draft, resolves conflicts
in the written order of precedence, may move the verdict one step with a reason, and writes
`run-1/review.md` in the format of `references/verdict-format.md`.

### 6. Act on the verdict

- **SHIP**: hand off to `article-producer` step 6 (publish package) or to the user.
- **FIX**: apply the blocking items, then the cheap recommended ones. Save as `draft-v2.md`, rerun
  steps 1 to 5 into `run-2`, and merge with `--prev run-1/merged.json`. The merge then reports
  which items were resolved and which are still open.
- **REWRITE**: redraft in the right format first (the format editor's moves). Start a new run;
  do not pass `--prev`, because line numbers no longer match.

Stop at round 5 (`--max-rounds`). The merge prints a stop notice; hand the draft and the last
review to a human. Five rounds without SHIP usually means the brief, not the draft, is wrong.

## What the editors check

| Editor | Lane | Blocks on |
|---|---|---|
| Format | right format for the topic and the reader's intent | fit under 7 |
| Structure | 10-item checklist: title, description, summary, headings, template, hook, code and media, paragraphs, close, length | a rule written in the profile |
| Voice | the named author's profile, line by line | a Banned-list hit |
| ICP | share test, the reader's words, segment clarity, admits limits | a fixable line that fails the share test |
| Claims | every number, superlative and "studies show", classed SOURCED / NO-SOURCE / VAGUE / WRONG | a WRONG claim, an unsourced claim that carries the argument, a brand superlative without method |

Full role texts: `references/editors.md`. To add a sixth editor (legal, accessibility, SEO), add an
H2 to that file whose first word is the new key, add the key to `EDITORS` and `SECTIONS` in
`scripts/review_run.py`, and pass `--editors`.

## Rules for you, the orchestrator

- Do not soften a verdict. If the merge says REWRITE, the user hears REWRITE first.
- Do not add findings of your own to the review. If you notice something, put it under
  "Noticed, not reviewed".
- Never invent a source to turn NO-SOURCE into SOURCED. Either the writer adds a real one, or the
  claim changes or goes.
- Report the run honestly: how many editors returned, whether the panel was degraded, the round
  number.

## Files

- `scripts/review_run.py`: `packet` and `merge`.
- `scripts/structure_lint.py`: the countable half of the structure checklist.
- `scripts/claims_scan.py`: the claims table, with sources-file and conflicting-figure checks.
- `scripts/newsroom_profile.py`: reads limits from the profile (shared by the scripts).
- `references/editors.md`, `references/chief-editor.md`, `references/verdict-format.md`.
- Worked example: `examples/northwind-ledger/` (two rounds, real outputs).
