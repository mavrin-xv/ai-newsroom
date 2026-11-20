# ICP editor verdict

## Share-test verdict: NO

An operations lead or owner would not paste this into the owner's group chat without an apology. The body (Steps 1 to 4) is solid and native: the shoebox, weekly bank match, the accountant's list on day 2. But the frame around it reads as an ad. It opens with a "Ultimate Guide ... Seamless" title, defines month-end to someone who closes the books every month, makes an unsourced "50%" claim, and ends on "best-in-class". Every one of those is fixable with a line edit, so each is flagged on its line.

## ICP fit score: 5 / 10

Steps 1 to 4 would score 8. The title, opener, introduction and conclusion pull it down.

## Generic to native rewrites

| Line | Generic (as written) | Native (what the reader says) |
|---|---|---|
| 2, 6 | "Seamless Month-End Process" | "Closing the books faster": drop "seamless", it is banned and empty |
| 2, 6 | "The Ultimate Guide to ..." | A plain promise, e.g. "How to close the month in 5 working days" |
| 19 | "Our reconciliation module" | "bank match" (the reader's term; "reconciliation module" is an outsider word) |
| 19 | "tie out your accounts" | "so it ties out" (fine, keep it in the reader's phrasing) |
| 19 | "manual work" | "chasing receipts and matching lines by hand" |
| 8 | "reviewing, reconciling and finalising a company's accounts" | cut the definition entirely; the reader closes the books monthly |
| 51 | "the best-in-class tool" | say what the product does in one concrete sentence, e.g. "keeps the bank match and the receipt list in one place" |

## Findings

1. Share test and respect: the first screen after the title is a textbook definition of month-end close (line 8). The reader knows this. It signals "beginner guide" and costs the segment-clarity test. Open instead with the reader's own pain (the shoebox, the day-6 accountant email).
2. Banned words: "Seamless" in title and H1 (lines 2, 6), "best-in-class" in the conclusion (line 51). Both are on the Banned list.
3. Trust posture: the only limit offered is "every business is different. Some will see more improvement than others" (line 19), a generic hedge that reads as boilerplate. Real limits are missing. Step 2's weekly match does not pay off for a business with a handful of transactions a month. Step 1's "pause the card" rule does not cover out-of-pocket expenses or cash. The guide never says when software is not needed.
4. Claims a skeptical reader will test: "Studies show ... 50%" has no source, "cut close time in half!" contradicts the pilot's own 9 to 5 days (about 44%) and uses an exclamation point, "the fastest way" is unproven, and "Most teams that close in 7 working days follow a list like this" (line 43) has no data behind it. This is outside my lane to verify, but an ICP reader who spots an unsourced stat stops trusting the rest.
5. Voice drift: line 19 shifts from a peer-to-peer guide into a sales pitch mid-introduction ("With Northwind Ledger, teams cut close time in half!"). The pitch belongs once, at the end, in the reader's words.
6. TL;DR (lines 12 to 15) is four bare fragments. A busy owner cannot act on "Receipts" or "A checklist". Write each as the rule it stands for.
7. What works and should stay: the shoebox framing, the 31% no-receipt figure with its pilot attribution, the "cost lands on the person who can fix it" line, the Tuesday-morning slot, the checklist order with the reason (payroll and accruals depend on a clean bank match), and "day 2, not day 6". These are respectful, specific and native.

```json
{
  "editor": "icp",
  "score": 5,
  "summary": "Steps 1-4 are native and useful, but the title, textbook opener, unsourced stat, outsider vocabulary and 'best-in-class' close make it read as an ad and fail the share test.",
  "findings": [
    {"severity": "blocking", "line": 2, "quote": "Closing Your Books Faster With a Seamless Month-End Process", "issue": "'Seamless' is on the Banned list, and 'Ultimate Guide' is generic hype the reader does not use. The same title repeats on line 6.", "fix": "Drop 'Ultimate' and 'Seamless'; use a plain promise such as 'How to close the month in 5 working days' in both title and H1."},
    {"severity": "blocking", "line": 8, "quote": "Month-end close is the process of reviewing, reconciling and finalising", "issue": "Defines month-end for a reader who closes the books every month. It signals beginner content and fails segment clarity on the first screen.", "fix": "Delete the definition; open with the reader's own problem (the shoebox, the accountant waiting until day 6)."},
    {"severity": "blocking", "line": 19, "quote": "Studies show that small businesses lose 50% of their finance time to manual work.", "issue": "Unsourced statistic; a reader who checks claims before sharing will stop trusting the piece.", "fix": "Cite the study or replace it with the pilot's own 31% no-receipt figure."},
    {"severity": "blocking", "line": 19, "quote": "With Northwind Ledger, teams cut close time in half!", "issue": "Ad voice with an exclamation point in a peer guide; also overstates the pilot's own 9 to 5 days (about 44%).", "fix": "Move the product mention to the end and state the pilot result as measured: median close 9 to 5 working days."},
    {"severity": "blocking", "line": 19, "quote": "Our reconciliation module is the fastest way to tie out", "issue": "'Reconciliation module' is an outsider word from the profile, and 'the fastest way' is an unproven superlative.", "fix": "Use 'bank match' and describe what it does; remove the superlative."},
    {"severity": "blocking", "line": 51, "quote": "Northwind Ledger is the best-in-class tool to help you do all of it.", "issue": "'best-in-class' is Banned and turns the close into a sales line.", "fix": "Replace with one concrete sentence on what the product does for steps 1 and 2."},
    {"severity": "recommended", "line": 19, "quote": "It is worth noting that every business is different. Some will see more improvement than others.", "issue": "Only limit in the text is a generic hedge; it reads as boilerplate, not as a real trade-off.", "fix": "Name real limits: weekly bank match is not worth it under a few dozen transactions a month; the card-pause rule does not cover out-of-pocket or cash spend; say when a spreadsheet is enough."},
    {"severity": "recommended", "line": 12, "quote": "- Receipts", "issue": "TL;DR is four bare fragments (lines 12 to 15); an owner skimming cannot act on them.", "fix": "Rewrite each as the rule: receipt the day it is spent, match the bank weekly, one checklist in one order, send the accountant's list on day 2."},
    {"severity": "recommended", "line": 43, "quote": "Most teams that close in 7 working days follow a list", "issue": "Unsupported generalisation presented as a norm.", "fix": "Cite where it comes from or say 'in our pilot'."},
    {"severity": "recommended", "line": 19, "quote": "Most teams spend far too long on month-end.", "issue": "Generic opener that explains the pain the reader lives with; filler transitions ('Additionally', 'It is worth noting') add distance.", "fix": "Start with a concrete scene in the reader's words, such as the shoebox on day 1 of close."},
    {"severity": "minor", "line": 8, "quote": "reviewing, reconciling and finalising a company's accounts", "issue": "British spelling 'finalising' next to a US-style product voice; moot if the sentence is cut.", "fix": "Cut the sentence; otherwise match one spelling convention."}
  ]
}
```
