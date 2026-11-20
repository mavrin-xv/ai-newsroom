# Voice editor verdict

Author: Mara Quinn
Voice score: 3 / 10

The draft body (Steps 1 to 4) is close to Mara's register: short sentences, exact numbers with a source ("In our pilot, 31%"), plain instructions. The frame around it is not. The title, the Introduction, the TL;DR and the Conclusion break the profile repeatedly, and two Banned-list words appear.

## The 3 lines most off

1. Line 19, the Introduction paragraph: opens with a vague claim, uses "Additionally", an exclamation mark, an unproven superlative, "It is worth noting", and an uncited "50%" statistic.
2. Lines 2 and 6, the title: "Ultimate Guide" and "Seamless" (Banned).
3. Line 51, the Conclusion: "best-in-class" (Banned) and a sales pitch where Mara ends on a plain instruction.

## Findings

- Opening (line 8): the guide opens with a dictionary definition. Mara opens with one number from a real customer's month-end and what it cost them. Recommended.
- Line 19 is the worst offender. Mara never uses an exclamation mark, connective padding or unsourced numbers. "Studies show ... 50%" has no source, and "cut close time in half" conflicts with the pilot's own 9 to 5 (44%). Blocking.
- Line 12 to 15 (TL;DR): four bare fragments, not a list of exactly three. Recommended.
- Line 43: "Most teams that close in 7 working days" is a number with no source. Recommended.
- Steps 1 to 4 are mostly on voice. Line 25 ("It sounds harsh. It works because...") and line 23 are good Mara rhythm. Line 29, "Weekly, it is a 20-minute job", gives no source for the 20 minutes. Minor.

```json
{
  "editor": "voice",
  "score": 3,
  "summary": "Body steps are close to Mara, but the title, intro and conclusion hit two Banned words, an exclamation mark, padding and unsourced numbers, and the opening is a definition, not a customer month-end number.",
  "author": "Mara Quinn",
  "findings": [
    {"severity": "blocking", "line": 2, "quote": "Closing Your Books Faster With a Seamless Month-End Process", "issue": "Banned word 'seamless'; 'Ultimate Guide' is an empty superlative Mara does not use.", "fix": "Title in her plain way, e.g. 'How to close your books in 5 working days'."},
    {"severity": "blocking", "line": 6, "quote": "The Ultimate Guide to Closing Your Books Faster With a Seamless Month-End Process", "issue": "Same title repeated in the H1: Banned word 'seamless' plus 'Ultimate'.", "fix": "Match the corrected frontmatter title, no 'Ultimate', no 'seamless'."},
    {"severity": "blocking", "line": 19, "quote": "With Northwind Ledger, teams cut close time in half!", "issue": "Exclamation mark (Mara never uses them) and a claim that contradicts the pilot figure given later (9 to 5 days is about 44%, not half).", "fix": "With Northwind Ledger, the median close in our pilot went from 9 working days to 5."},
    {"severity": "blocking", "line": 19, "quote": "Our reconciliation module is the fastest way to tie out your accounts.", "issue": "Unproven superlative; Mara proves with a sourced number instead.", "fix": "Cut the sentence, or: Our reconciliation module matched 1 week of lines in 20 minutes in the pilot."},
    {"severity": "blocking", "line": 19, "quote": "Studies show that small businesses lose 50% of their finance time", "issue": "Number with no source; Mara always says where a number came from.", "fix": "Name the study and year, or replace with a pilot figure: 'In our pilot, 31% of expense lines had no receipt on day one.'"},
    {"severity": "blocking", "line": 19, "quote": "Additionally, the longer the close takes, the later", "issue": "Connective padding.", "fix": "The longer the close takes, the later the owner sees real numbers."},
    {"severity": "blocking", "line": 19, "quote": "It is worth noting that every business is different.", "issue": "Throat-clearing filler and a hedge; Mara states things directly.", "fix": "Delete the sentence and the one after it."},
    {"severity": "blocking", "line": 51, "quote": "Northwind Ledger is the best-in-class tool to help you", "issue": "Banned phrase 'best-in-class'; also a sales line where Mara ends sections on a plain instruction.", "fix": "End on an instruction: 'Print the checklist and run it on the next close.'"},
    {"severity": "recommended", "line": 8, "quote": "Month-end close is the process of reviewing, reconciling and finalising", "issue": "Opens with a definition. Mara opens with one number from a real customer's month-end and what it cost them.", "fix": "One customer month-end number first, e.g. 'One pilot team spent 9 working days on close. The owner saw real numbers on day 10.'"},
    {"severity": "recommended", "line": 12, "quote": "- Receipts - Bank matching - A checklist - Software helps", "issue": "Four bare fragments; Mara's signature is a short list of exactly three, in full sentences.", "fix": "Three items: photograph receipts the day of spend, match the bank weekly, use one checklist in the same order."},
    {"severity": "recommended", "line": 19, "quote": "Most teams spend far too long on month-end.", "issue": "Vague claim with no number or source.", "fix": "The median close in our pilot took 9 working days."},
    {"severity": "recommended", "line": 43, "quote": "Most teams that close in 7 working days follow a list like this one.", "issue": "Exact-looking number with no source.", "fix": "Say where 7 came from, e.g. 'In our pilot, the teams that closed in 7 working days used a list like this one.'"},
    {"severity": "minor", "line": 29, "quote": "Weekly, it is a 20-minute job", "issue": "Exact number but no stated source.", "fix": "Add 'in our pilot' after the number."}
  ]
}
```
