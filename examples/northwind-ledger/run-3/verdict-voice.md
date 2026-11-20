# Voice verdict

Author graded against: Mara Quinn (named in the brief).

Voice score: 8 / 10

The draft is close to her profile. It opens with one customer's month-end number and what it cost them (9 working days, owner sees the numbers on day 10). It uses her signature "Here is the part nobody tells you" (line 23) and a list of exactly three (line 51). Most sections end on a plain instruction. There are no exclamation marks, no rhetorical questions, no bracketed asides in the prose, and no Banned-list words. Sources sit next to the numbers. The drift is in a few vague quantities where she is always exact, one bracketed aside in the checklist, and one section ending that is a statement, not an instruction.

## The 3 lines most off

1. Line 57: "Under a few dozen bank lines a month, in our judgement" is a vague number with no source. She is exact, with a source.
2. Line 19: "the shoebox was where a lot of month-end time went" is a vague quantity and a metaphor, placed right before an exact, sourced number.
3. Line 42: "(it goes out on day 2, before the lines above are done)" is a bracketed aside. Her profile allows none.

## Findings

Banned list: no hits. Opening pattern: passes. Rhetorical questions and exclamation marks: none found.

- recommended, line 57: replace the unsourced vague threshold with an instruction she would give. Fix: "Count your bank lines for one month first. If the count is small, a weekly match is overhead; we did not measure a cut-off."
- recommended, line 19: drop "a lot of" and the shoebox image. Fix: "In our pilot, 31% of expense lines had no receipt on the first day of close ([pilot report](https://example.org/pilot-report), 14 firms, April 2026)."
- recommended, line 42: bracketed aside breaks the no-brackets rule. Fix: "[ ] accountant's list sent on day 2, before the lines above are done"
- recommended, line 60: the section ends on a statement, not a plain instruction as she does. Fix: "Fix the chart of accounts first; no routine survives books that don't tie out."
- minor, line 59: semicolon joins two clauses where she uses short sentences. Fix: "Steps 1 and 4 still help. Steps 2 and 3 are theirs."

```json
{
  "editor": "voice",
  "score": 8,
  "summary": "Close to Mara Quinn: right opener, signature move, exact sourced numbers; drift is a few vague quantities, one bracketed aside and one non-instruction section ending.",
  "author": "Mara Quinn",
  "findings": [
    {"severity": "recommended", "line": 57, "quote": "Under a few dozen bank lines a month, in our judgement", "issue": "Vague, unsourced number; she always gives the exact figure with its source.", "fix": "Count your bank lines for one month first. If the count is small, a weekly match is overhead; we did not measure a cut-off."},
    {"severity": "recommended", "line": 19, "quote": "the shoebox was where a lot of month-end time went", "issue": "Vague quantity and a metaphor right before the exact sourced figure; breaks her precision.", "fix": "In our pilot, 31% of expense lines had no receipt on the first day of close."},
    {"severity": "recommended", "line": 42, "quote": "(it goes out on day 2, before the lines above are done)", "issue": "Bracketed aside; her rhythm has no asides in brackets.", "fix": "[ ] accountant's list sent on day 2, before the lines above are done"},
    {"severity": "recommended", "line": 60, "quote": "No routine survives books that don't tie out.", "issue": "Section ends on a general statement, not a plain instruction as her sections do.", "fix": "Fix the chart of accounts first; no routine survives books that don't tie out."},
    {"severity": "minor", "line": 59, "quote": "Steps 1 and 4 still help; Steps 2 and 3 are theirs.", "issue": "Semicolon-joined clauses; she writes short sentences.", "fix": "Steps 1 and 4 still help. Steps 2 and 3 are theirs."}
  ]
}
```
