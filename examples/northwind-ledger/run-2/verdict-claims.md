# Claims verdict: draft-v2 ("How to close your books in 5 working days instead of 9")

Lane: is every fact true, sourced and checkable by the reader. I checked against the Proof table and the draft only. I had no web access, so I could not open the pilot report link and class everything by what the draft shows.

## Mechanical scan: confirmed or rejected

The scan reports 4 claims, 0 not sourced. I confirm two of its rows and reject two.

- Line 8, "median close went from 9 working days to 5": confirmed. It matches the Proof row (9 to 5 working days, median, 14 pilot customers, 2026-04) and the draft links the pilot report.
- Line 19, 31% of expense lines with no receipt on day 1 of close: confirmed. Figure, population (14 firms) and date (April 2026) match the Proof row, and the link is cited as the profile says.
- Line 8, "One pilot team spent 9 working days": rejected as "sourced". The scan credits a "sources file" the reader cannot see. In the draft this is an unnamed anecdote with no link. It also equals the median exactly, so it can read as the median restated as a story.
- Line 8, "owner saw real numbers on day 10, a third of the way into the next month": rejected as "sourced", for the same reason. It also does not reconcile with "9 working days" (see table).
- The scan missed at least eight other checkable or vague claims, listed below.

## Claims table

| Line | Claim | Class | What would fix it |
|---|---|---|---|
| 2 | Title: "close your books in 5 working days instead of 9" | [VAGUE] | The 9 to 5 figure is a pilot median, not a promise. Add "median" or "in our pilot" to the title, or reword as "how 14 firms cut their close from 9 days to 5". |
| 3 | "took 14 small service firms from a 9-day close to 5" | [NO-SOURCE] | Proof says "14 pilot customers"; "small service firms" is not in Proof. Use "14 pilot customers", or add the firm profile with a source. "Took" also implies the four changes caused the drop; Proof only shows before and after. |
| 8 | One pilot team spent 9 working days on month-end close | [NO-SOURCE] | Link or name the case, or mark it as an illustrative composite. |
| 8 | Owner saw real numbers on day 10, "a third of the way into the next month" | [NO-SOURCE] | 9 working days is roughly calendar day 11 to 13, not day 10, and 10 working days is about half a month. State "working day" or "calendar day" and fix the "third" comparison. |
| 8 | Median close 9 to 5 working days, 14 firms, four changes | [SOURCED] | None. Optional: add the date (April 2026) as line 19 does. |
| 8 | "None of them needs new software." | [NO-SOURCE] | Absolute claim about all 14 firms. Add the pilot-report finding or soften to "None of the four changes requires new software". |
| 12 | Receipt photo "removes most of the chasing" | [VAGUE] | "Most" cannot be checked. Use the pilot figure or drop "most". |
| 19 | 31% of expense lines had no receipt on day 1 of close | [SOURCED] | None. |
| 19 | "The shoebox is where month-end time goes." | [VAGUE] | Unmeasured superlative-style claim. Say "a large share of month-end time went on chasing receipts in our pilot" only if the report supports it. |
| 21 | Receipt rule "works because the cost lands on the person who can fix it" | [NO-SOURCE] | Causal claim presented as fact. Cite pilot evidence or phrase as the author's reasoning. |
| 31 | "a few hundred lines a month, the weekly slot is short" | [VAGUE] | Give a measured time from the pilot, or tell the reader to time it (the next sentence already does). |
| 45 | "doing them first means doing them twice" | [NO-SOURCE] | Mechanism is plausible but asserted. Low weight; fine as advice. |
| 53 | "By month three the list gets shorter" (also line 31, "month three") | [NO-SOURCE] | A prediction with no data. Mark as "in our experience" or cite pilot data. |
| 42 vs 49 | Checklist puts "accountant's list sent" last, after payroll and accruals; Step 4 says send it on day 2, before everything is finished, and the summary says payroll and accruals come after the bank match | [WRONG] (self-contradiction, minor in scope) | Reconcile: either move the list item in the checklist to its day-2 position or say the checklist runs in two passes. |

## Findings

No row is blocking. The two headline figures (9 to 5 and 31%) match the Proof table and are cited as the profile requires. There are no brand superlatives, no "studies show", and no banned words in the claims. The risk is the unsourced scaffolding around the proven numbers: the anecdote that does not reconcile with its own unit, the all-firms "no new software" claim, the unmeasured "most" and "a few hundred", and the title that turns a median into a promise.

Trust score: 7 of 10. The proven numbers are exact and linked; the remaining claims are recommended fixes, none gating.

```json
{
  "editor": "claims",
  "score": 7,
  "summary": "Headline figures 9 to 5 and 31% match Proof and are linked; no blocking claims, but the anecdote, 'no new software', 'most', and the title promise are unsourced or vague.",
  "findings": [
    {"severity": "recommended", "line": 2, "quote": "How to close your books in 5 working days instead of 9",
     "issue": "A pilot median is presented as the reader's outcome.",
     "fix": "Add 'median' or 'in our pilot' to the title."},
    {"severity": "recommended", "line": 3, "quote": "took 14 small service firms from a 9-day close to 5",
     "issue": "Proof says 14 pilot customers; 'small service firms' is unsourced and 'took' implies causation.",
     "fix": "Use '14 pilot customers' or source the firm profile."},
    {"severity": "recommended", "line": 8, "quote": "The owner saw real numbers on day 10",
     "issue": "Unsourced anecdote; 9 working days is about calendar day 11 to 13, and day 10 is not 'a third' of working days. The scan's 'sourced via sources file' is not checkable by the reader.",
     "fix": "Link or label the case as illustrative, and state working vs calendar day."},
    {"severity": "recommended", "line": 8, "quote": "None of them needs new software.",
     "issue": "Absolute claim about all firms with no source.",
     "fix": "Cite the pilot report or say 'None of the four changes requires new software'."},
    {"severity": "recommended", "line": 12, "quote": "it removes most of the chasing",
     "issue": "'Most' cannot be checked.",
     "fix": "Replace with the pilot figure or drop 'most'."},
    {"severity": "recommended", "line": 19, "quote": "The shoebox is where month-end time goes.",
     "issue": "Unmeasured claim about where time goes.",
     "fix": "Qualify as pilot observation or support with data."},
    {"severity": "recommended", "line": 21, "quote": "It works because the cost lands on the person who can fix it.",
     "issue": "Causal claim stated as fact, no evidence.",
     "fix": "Cite pilot evidence or frame as reasoning."},
    {"severity": "minor", "line": 31, "quote": "For a firm with a few hundred lines a month, the weekly slot is short.",
     "issue": "Vague quantities and no measured time.",
     "fix": "Give a pilot time or drop the claim."},
    {"severity": "minor", "line": 53, "quote": "By month three the list gets shorter",
     "issue": "Prediction with no data.",
     "fix": "Mark as experience or cite pilot data."},
    {"severity": "recommended", "line": 42, "quote": "[ ] accountant's list sent",
     "issue": "Checklist puts the list last after payroll and accruals, contradicting Step 4 (send on day 2, before everything is finished).",
     "fix": "Reconcile the checklist order with the day-2 instruction."}
  ]
}
```
