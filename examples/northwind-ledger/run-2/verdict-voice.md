# Voice verdict

Author: Mara Quinn (named in the brief).
Voice score: 8 / 10.

The draft is close to the profile. The opening is a real number with a cost (9 working days, real numbers on day 10). "Here is the part nobody tells you" appears once, as the signature move. The sentences are short with one longer one per paragraph. There are no exclamation marks, no rhetorical questions and no Banned-list words. Sourced numbers are exact (31%, 14 firms, April 2026). The drift is in a few vague quantities, one bracketed aside, and two sections that end on an observation instead of a plain instruction.

## The 3 lines most off

1. Line 31: "For a firm with a few hundred lines a month, the weekly slot is short." The number is vague, has no source, and the sentence gives no time.
2. Line 51: "(a new hire, a large one-off purchase, a refund)". This is a bracketed aside, which the profile excludes.
3. Line 53: "and day 2 stops feeling early." The section closes on a feeling, not a plain instruction.

## Findings

No Banned-list hits, so nothing is blocking.

- Line 12 (recommended): "it removes most of the chasing" uses "most" where Mara gives an exact figure with a source. Use the 31% from line 19.
- Line 31 (recommended): vague count and unsourced "short". Give the pilot's measured minutes, or say what to time.
- Line 51 (recommended): the brackets break the no-asides rhythm rule. Move the examples into the sentence with a dash or a colon.
- Line 53 (recommended): the section should end on an instruction, such as "Ask for the answers in the same document, line by line."
- Line 57 (recommended): "Under a few dozen bank lines a month" is a rounded, unsourced threshold. State the exact cut-off from the pilot, or say it is a judgement call.
- Line 45 (minor): Step 3 ends on a forecast ("you will see which step eats the time"). Ending on "Write the day each line was done" would match the instruction habit.

```json
{
  "editor": "voice",
  "score": 8,
  "summary": "Close to Mara Quinn: real-number opening, signature move, no banned words; drifts on a few vague numbers, one bracketed aside and two non-instruction section endings.",
  "author": "Mara Quinn",
  "findings": [
    {"severity": "recommended", "line": 31, "quote": "For a firm with a few hundred lines a month, the weekly slot is short.", "issue": "Vague, unsourced quantity; Mara gives exact numbers with their source.", "fix": "For a firm with 300 lines a month, the weekly slot took N minutes in the pilot (source). Replace N and 300 with the pilot figures."},
    {"severity": "recommended", "line": 51, "quote": "(a new hire, a large one-off purchase, a refund)", "issue": "Bracketed aside; the profile allows no asides in brackets.", "fix": "Anything unusual this month: a new hire, a large one-off purchase, a refund."},
    {"severity": "recommended", "line": 53, "quote": "and day 2 stops feeling early.", "issue": "Section ends on a feeling, not a plain instruction.", "fix": "Cut the clause and end on: Ask the accountant to answer in the same document, line by line."},
    {"severity": "recommended", "line": 12, "quote": "it removes most of the chasing.", "issue": "Imprecise 'most' where the author gives an exact figure with its source.", "fix": "it removes the chasing behind the 31% of lines that had no receipt."},
    {"severity": "recommended", "line": 57, "quote": "Under a few dozen bank lines a month, a weekly match is overhead.", "issue": "Rounded, unsourced threshold.", "fix": "Under 40 bank lines a month (state the pilot basis), a weekly match is overhead."},
    {"severity": "minor", "line": 45, "quote": "After two months you will see which step eats the time.", "issue": "Step ends on a forecast, not a plain instruction.", "fix": "Write the day each line was done; after two months, cut the step that eats the time."}
  ]
}
```
