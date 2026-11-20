# Claims audit verdict

Lane: is every fact true, sourced and checkable. Declared format: guide. No web access, so nothing outside the Proof table was verified externally.

## Claims table

| Line | Claim | Class | What would fix it |
|---|---|---|---|
| 19 | "Most teams spend far too long on month-end." | [VAGUE] recommended | Cut it, or replace with a checkable figure from the pilot report. |
| 19 | "Studies show that small businesses lose 50% of their finance time to manual work." | [NO-SOURCE] blocking | Round number, "studies" unnamed, and it carries the intro's argument. Cite the original study with a link, or delete. Not in the Proof table. |
| 19 | "With Northwind Ledger, teams cut close time in half!" | [WRONG] blocking | The Proof figure is 9 to 5 working days, a 44% cut (median, 14 pilot customers), not half. It also generalises a pilot median to all "teams". Say "cut the median close from 9 to 5 working days in our pilot". |
| 19 | "Our reconciliation module is the fastest way to tie out your accounts." | [VAGUE] blocking | Brand superlative with no method. No Proof entry. Remove it, or state a measured, dated comparison. |
| 19 | "The median close in our pilot went from 9 working days to 5." | [SOURCED] | Matches the Proof row. Recommended: add the link https://example.org/pilot-report, "14 customers" and "April 2026" so the reader can check it. |
| 23 | "In our pilot, 31% of expense lines had no receipt on the first day of close." | [SOURCED] | Matches the Proof row. The scan's "superlative" tag is a false positive. Recommended: link the pilot report here too. |
| 29 | "Weekly, it is a 20-minute job" | [NO-SOURCE] recommended | Unsupported time figure. Mark it as an example ("often about 20 minutes for a small ledger") or give the basis. |
| 43 | "Most teams that close in 7 working days follow a list like this one." | [NO-SOURCE] blocking | Unsourced "most teams" stat. The 7 appears nowhere in Proof, and the draft's other working-days figures are 9 and 5, so the reader gets three different numbers. Remove it, or source it and say what 7 refers to. |
| 51 | "Northwind Ledger is the best-in-class tool to help you do all of it." | [VAGUE] blocking | Brand superlative with no method. "best-in-class" is also on the profile's Banned list. Replace with a plain, factual description of what the product does. |
| 2, 6 | "The Ultimate Guide to Closing Your Books Faster" | [VAGUE] minor | "Ultimate" is an unprovable superlative about the content. Soften it. |

Not counted as claims: the line 8 definition of month-end close, and the process advice in lines 25, 31, 43 and 47. Line 25 ("It works because the cost lands on the person who can fix it") is an unsupported assertion about why a rule works. It is advice, not a checkable fact, so I left it out.

## Mechanical scan check

- Confirmed: lines 19 (x4), 29, 43 and 51 as unsourced or vague.
- Rejected: line 23 "superlative" tag. It is a plain number that matches Proof.
- Refined: line 19 "in half" is not just unsourced. It contradicts Proof (9 to 5 is not half), so it is [WRONG].
- The "7 vs 9 working days" flag is real as a consistency risk. The two figures are not strictly the same metric (7 is an unsourced claim about other teams, 9 is the pilot's before-median), but the draft gives no way to tell them apart.

## Trust score: 3 / 10

The two Proof-backed figures are used accurately. Around them sit one invented-looking stat ("50%", "studies show"), one misstated pilot result ("in half"), two unmeasured brand superlatives ("fastest", "best-in-class", the latter also banned) and an unsourced "most teams ... 7 days" claim. A reader who tests claims would catch most of these.

## Findings

All non-[SOURCED] rows are in the JSON block below.

```json
{
  "editor": "claims",
  "score": 3,
  "summary": "Two Proof figures are used correctly, but 'studies show 50%', 'cut close time in half' (contradicts 9 to 5), 'fastest', 'best-in-class' and the '7 working days' stat are unsourced or wrong.",
  "findings": [
    {"severity": "blocking", "line": 19, "quote": "Studies show that small businesses lose 50% of their finance time to manual work.", "issue": "Unnamed 'studies' and a suspiciously round 50% with no source, carrying the intro's argument. Not in the Proof table.", "fix": "Cite and link the original study, or delete the sentence."},
    {"severity": "blocking", "line": 19, "quote": "With Northwind Ledger, teams cut close time in half!", "issue": "Contradicts Proof: the pilot median went from 9 to 5 working days (44%), not half, and it is a pilot of 14 customers, not all teams.", "fix": "Replace with the pilot figure as stated: median close cut from 9 to 5 working days in the pilot, linked to the pilot report."},
    {"severity": "blocking", "line": 19, "quote": "Our reconciliation module is the fastest way to tie out your accounts.", "issue": "Brand superlative with no method, comparison or source.", "fix": "Delete it, or replace it with a measured, dated claim that is in Proof."},
    {"severity": "blocking", "line": 43, "quote": "Most teams that close in 7 working days follow a list like this one.", "issue": "Unsourced 'most teams' stat. The 7 is not in Proof and sits beside the draft's 9 and 5, giving three different working-day figures.", "fix": "Remove the sentence, or source it and state clearly what 7 days measures."},
    {"severity": "blocking", "line": 51, "quote": "Northwind Ledger is the best-in-class tool to help you do all of it.", "issue": "Brand superlative with no method, and 'best-in-class' is on the profile's Banned list.", "fix": "Replace with a factual description of what the product does, with no ranking claim."},
    {"severity": "recommended", "line": 19, "quote": "Most teams spend far too long on month-end.", "issue": "Uncheckable as written ('most', 'far too long').", "fix": "Cut it, or back it with a figure from the pilot report."},
    {"severity": "recommended", "line": 19, "quote": "The median close in our pilot went from 9 working days to 5.", "issue": "Matches Proof, but the reader cannot check it: no link, sample size or date next to it.", "fix": "Add the link https://example.org/pilot-report plus '14 customers' and 'April 2026'."},
    {"severity": "recommended", "line": 29, "quote": "Weekly, it is a 20-minute job", "issue": "Specific time figure with no basis or source.", "fix": "Frame it as an example ('often about 20 minutes for a small ledger') or give the basis."},
    {"severity": "minor", "line": 6, "quote": "The Ultimate Guide to Closing Your Books Faster", "issue": "'Ultimate' is an unprovable superlative about the guide.", "fix": "Soften, for example 'A Practical Guide to Closing Your Books Faster'."}
  ]
}
```
