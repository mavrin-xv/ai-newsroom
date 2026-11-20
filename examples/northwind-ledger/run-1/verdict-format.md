# Verdict: format editor

- Topic: how a small service business can close its month faster (receipts, weekly bank match, one checklist, early accountant's list).
- Segment: the operations lead or office manager who does the books, and the owner who signs off.
- Intent: fixing. They close in spreadsheets and want a repeatable way to shorten month-end.
- Current format: guide (declared, and the body is ordered steps).
- Right format: guide.
- Format fit: 7 out of 10.
- Verdict: aligned. The body is the right shape: four steps in a usable order, with a checklist block. The frame around it does not yet meet the guide contract.

## Why it is aligned but only just

The steps (lines 21 to 47) are what a fixing reader wants, and the checklist at line 35 is the right artifact. The problems are structural and sit around the steps, not in them.

1. A required section is missing. The guide format requires "When this does not apply" (the limits section). The draft ends on a conclusion with a sales line instead. A reader who does not have an accountant, or who closes in an accounting package already, gets no way to tell whether the steps fit them.
2. The summary block is not a summary. The "TL;DR" has four fragments ("Receipts", "Bank matching", "A checklist", "Software helps") that carry no outcome and no numbers. It meets the 3 to 5 bullet count but not the purpose. The profile also calls the block "summary", not "TL;DR".
3. Length is under the guide floor. The draft is roughly 450 words against a 700 to 1600 range.
4. The setup is delayed. The introduction (line 19) holds product claims, an unsourced statistic and a pilot result before the first step. A fixing reader has to get through a pitch to reach the runbook. The outcome should lead and the product pitch should sit in the CTA only.
5. The title is a topic ("The Ultimate Guide to ... Seamless Month-End Process"), not an outcome. The format asks for an outcome title.

## Conversion moves (guide to a conforming guide)

1. Add an h2 "When this does not apply" before the CTA, replacing the "Conclusion" section. Say who should not use this path (no accountant involved, already on software that matches weekly, fewer than a handful of expense lines) and keep the CTA as the last line.
2. Replace the TL;DR with a real summary of 3 to 5 bullets that each carry an outcome from the steps (receipts the day money is spent, weekly 20-minute bank match, one ordered checklist, accountant's list on day 2). Retitle it "Summary".
3. Cut the introduction down to two or three sentences that state the outcome and move straight to Step 1; move the pilot numbers into the steps they support, and add the missing 250 or so words in the steps (who owns each step, what to do when a line will not match) rather than in the intro.

## Findings

```json
{
  "editor": "format",
  "score": 7,
  "summary": "Right format (guide) and ordered steps suit a fixing reader, but the required limits section is missing, the summary is fragments, and the draft is under the word floor.",
  "format_fit": "aligned",
  "current_format": "guide",
  "right_format": "guide",
  "findings": [
    {"severity": "blocking", "line": 0, "quote": "",
     "issue": "The guide format requires a 'When this does not apply' section and the draft has none; it ends on a Conclusion instead.",
     "fix": "Replace the Conclusion h2 with 'When this does not apply' listing who should skip these steps, then end on the CTA."},
    {"severity": "blocking", "line": 0, "quote": "",
     "issue": "The draft is roughly 450 words, below the 700 minimum for a guide.",
     "fix": "Add substance to the steps (owners, what to do with unmatched lines), not to the introduction."},
    {"severity": "recommended", "line": 12, "quote": "- Receipts",
     "issue": "The summary block is four fragments with no outcomes, and it is labelled TL;DR instead of 'summary'.",
     "fix": "Rewrite as a 'Summary' of 3 to 5 outcome bullets drawn from Steps 1 to 4."},
    {"severity": "recommended", "line": 19, "quote": "With Northwind Ledger, teams cut close time in half!",
     "issue": "The introduction delays the steps with a product pitch and background; a fixing reader wants the runbook first.",
     "fix": "Cut the introduction to two or three sentences that state the outcome, then go to Step 1; leave the product mention to the CTA."},
    {"severity": "minor", "line": 6, "quote": "The Ultimate Guide to Closing Your Books Faster With a Seamless Month-End Process",
     "issue": "The title is a topic label, not an outcome title.",
     "fix": "Name the outcome, for example the number of working days the close drops to."}
  ]
}
```
