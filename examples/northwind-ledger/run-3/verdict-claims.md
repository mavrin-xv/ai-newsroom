# Claims audit: draft-v3 (guide)

Lane: is every fact true, sourced and checkable. I had no web access and only this brief, so I did not open the pilot report or the "sources file" the scan mentions. Classes below follow what the draft shows plus the Proof table.

## Mechanical scan: confirm or reject

The scan says 5 claims, 0 not sourced. I reject the count and the "0 not sourced". It skipped the title and description (lines 2, 3, 6), "None of the four changes requires new software" (line 8), "a lot of month-end time" (line 19), the payroll and accruals dependency claim (line 45), and the "two lines will keep coming back" claim (line 33). Its line 8 claim "One pilot firm spent 9 working days" is marked sourced via a sources file I cannot see. The Proof table only supports 9 as a median across 14 firms, not one firm's figure. Its line 12 row is accepted but needs scoping (see table).

## Claims table

| Line | Claim | Class | What would fix it |
|---|---|---|---|
| 2, 3, 6 | 14 firms, median close 9 to 5 working days | [SOURCED] | Matches Proof (9 to 5, 14 customers, median, 2026-04). Linked at line 8. The title and description carry no link of their own, which is fine for a title. |
| 3, 6 | "with four changes" (cause of the 9 to 5 drop) | [NO-SOURCE] | Proof only supports the before and after medians. Confirm in the pilot report that all four changes were applied and that the drop is attributed to them. Otherwise write "firms that also adopted four changes" or similar. |
| 8 | One pilot firm spent 9 working days on its close | [NO-SOURCE] | 9 is the pilot median in Proof. A single firm's figure is a separate fact. Cite the source for this firm or reword to "the median pilot firm spent 9 working days". |
| 8 | Owner saw the numbers on calendar day 10, "a third of the way into the next month" | [NO-SOURCE] | No source. Arithmetic holds (10 of 30 days). But 9 working days counted from the 1st ends on calendar day 11 at the earliest, so day 10 only works if the close clock starts before the month ends. State the start point or fix the day. |
| 8 | Median close 9 to 5 working days across 14 firms | [SOURCED] | Linked to the pilot report, matches Proof. |
| 8 | "None of the four changes requires new software" | [NO-SOURCE] | Not in Proof. Back it with the pilot report or soften to "none of the four needs software we sell". Step 1 needs a phone camera and Step 3 a printed list, which is consistent, but it is still an unsourced absolute. |
| 12 | 31% of lines had no receipt | [SOURCED] | Matches Proof and is cited at line 19. The bullet drops "on day 1 of close" and "pilot". Add the scope so the number is not read as a general rate. |
| 19 | 31% of expense lines had no receipt on day 1 of close (pilot report, 14 firms, April 2026) | [SOURCED] | Cited as the profile directs. Matches figure, measure, source and date. |
| 19 | "the shoebox was where a lot of month-end time went" | [VAGUE] | Proof measures missing receipts, not time spent. Either cite the time figure or reword to "31% of lines had no receipt". |
| 27 | Monthly match means "four weeks of lines at once", "a payment from five weeks ago" | [SOURCED] | Plain arithmetic and illustration, not a factual claim. |
| 31 | "We did not time the weekly slot in the pilot" | [SOURCED] | Self-disclosure, honest. It also means no per-step effect is claimed, which is the right limit. |
| 33 | "Two lines will keep coming back: card refunds ... and transfers between your own accounts" | [VAGUE] | Presented as fact about every reader's books. Add "in our experience" or cite the pilot. |
| 45 | "Payroll and accruals depend on a clean bank match, so doing them first means doing them twice" | [NO-SOURCE] | Step 3's whole case for the order rests on this. Payroll journals often do not depend on the bank match. Give the reason concretely or frame it as the team's practice. |
| 15, 42, 49 | Day 2 vs day 6 for the accountant's list | [VAGUE] | Calendar vs working day not stated. Say which. Minor. |
| 57 | "Under a few dozen bank lines a month, in our judgement" | [VAGUE] | Marked as judgement, so honest. "A few dozen" is soft but acceptable. |
| 60 | "No routine survives books that don't tie out" | [VAGUE] | Absolute with no basis. Soften to "is hard to keep up". Minor. |
| 64 | "free close checklist" at example.org/start | [SOURCED] | Link is in the profile Links list. I cannot check that the checklist is free. |

No brand superlatives, no banned words in the claims, and no number appears twice with different values (9, 5, 14, 31%, day 2, day 6 are consistent throughout). No stat chains.

## Trust score: 7 / 10

Both Proof figures are used correctly and linked with the date. The article is careful about what it did not measure. Points lost for the causal "four changes" attribution, the one-firm 9-day figure that Proof only supports as a median, an unsourced "no new software" absolute, a time-spent claim that Proof does not measure, and the day 10 timeline that does not reconcile with 9 working days. Nothing is blocking, but the first three should be settled against the pilot report before ship.

```json
{
  "editor": "claims",
  "score": 7,
  "summary": "Proof figures (9 to 5, 14 firms, 31%) are used correctly and linked; no blocking claims, but the one-firm 9 days, the causal four-changes line, and the unsourced no-software and time-spent claims need fixing or sourcing.",
  "findings": [
    {"severity": "recommended", "line": 8, "quote": "One pilot firm spent 9 working days on its month-end close.", "issue": "Proof supports 9 working days only as the median across 14 firms, not as one firm's figure. The scan marks it sourced via a sources file I cannot see.", "fix": "Cite the source for this specific firm, or reword to the median pilot firm."},
    {"severity": "recommended", "line": 8, "quote": "The owner saw the month's numbers on calendar day 10, a third of the way into the next month.", "issue": "No source. 9 working days from the 1st ends on calendar day 11 at the earliest, so day 10 does not reconcile unless the close starts before month end.", "fix": "State when the close clock starts, or correct the calendar day, and name the source."},
    {"severity": "recommended", "line": 8, "quote": "None of the four changes requires new software.", "issue": "Unsourced absolute not in the Proof section.", "fix": "Back it with the pilot report or soften to a claim the draft can support."},
    {"severity": "recommended", "line": 8, "quote": "the median close went from 9 working days to 5 after four changes", "issue": "Proof gives the before and after medians, not that the four changes caused the drop. The title and description repeat this causal framing.", "fix": "Confirm attribution in the pilot report or word it as before and after, with the four changes as what the firms did."},
    {"severity": "recommended", "line": 12, "quote": "the chasing behind the 31% of lines that had no receipt.", "issue": "Drops the scope in Proof: pilot customers' expense lines on day 1 of close. Reads as a general rate.", "fix": "Add \"in our pilot, on day 1 of close\" or link the figure here."},
    {"severity": "recommended", "line": 19, "quote": "the shoebox was where a lot of month-end time went", "issue": "Time spent on receipts is not in Proof, which measures missing receipts only. Also vague.", "fix": "Cite a time figure or reword to what Proof measures: 31% of lines had no receipt."},
    {"severity": "recommended", "line": 45, "quote": "Payroll and accruals depend on a clean bank match, so doing them first means doing them twice.", "issue": "Unsourced technical claim that carries Step 3's argument for the order; payroll journals often do not depend on the bank match.", "fix": "Give the concrete dependency or frame it as the team's practice."},
    {"severity": "recommended", "line": 33, "quote": "Two lines will keep coming back: card refunds that land weeks after the purchase", "issue": "Stated as universal fact with no basis.", "fix": "Add \"in our experience\" or cite the pilot."},
    {"severity": "minor", "line": 42, "quote": "accountant's list sent (it goes out on day 2, before the lines above are done)", "issue": "Day 2 and day 6 do not say calendar or working days.", "fix": "State the unit once, in Step 4."},
    {"severity": "minor", "line": 60, "quote": "No routine survives books that don't tie out.", "issue": "Absolute with no basis.", "fix": "Soften to \"is hard to keep up\"."}
  ]
}
```
