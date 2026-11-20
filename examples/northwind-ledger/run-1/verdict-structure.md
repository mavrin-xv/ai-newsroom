# Structure editor verdict: guide format

Every one of the 10 items fails. Two of the lint's calls are rejected (summary block, H2 count); the rest are confirmed.

## Item table

| # | Item | Result | Line | Note |
|---|---|---|---|---|
| 1 | Title | FAIL | 2 (H1 at 6) | "The Ultimate Guide to Closing Your Books Faster With a Seamless Month-End Process" is about 81 characters against a 70 limit. It uses the banned "Ultimate" and "Guide to". |
| 2 | Description | FAIL | 3 | About 169 characters against a 155 limit. It opens with "Learn how" and reads as a feature list. |
| 3 | Summary block | FAIL | 12-15 | There are 4 bullets, but all are topics ("Receipts", "Bank matching", "A checklist", "Software helps"), not conclusions. The lint's PASS counted bullets only; I reject it. |
| 4 | Headings | FAIL | 17, 49 | I count 7 H2s (TL;DR, Introduction, Steps 1-4, Conclusion) against a max of 6. The lint says 6; I reject that count. "Introduction" and "Conclusion" are banned names. |
| 5 | Template | FAIL | 0 | The required "When this does not apply" section is missing. The summary is present and the steps follow it, but there is no limits section before the CTA. |
| 6 | Hook | FAIL | 8 | The opening sentence is a definition of month-end close. It has no number, hidden failure or counter-claim. |
| 7 | Code and data | FAIL | 35 | The checklist code fence has no language label. There are no tables or images. |
| 8 | Paragraphs | FAIL | 19 | The paragraph has 9 sentences against a cap of 4. The other paragraphs are within the cap. |
| 9 | Close | FAIL | 49-51 | The last section is "Conclusion". It recaps the article and pitches the product. The CTA link is present but does not ask for the one step in the CTA section (run your last month through the checklist). |
| 10 | Length | FAIL | 0 | About 437 words against a band of 700-1600. This is confirmed. |

## Mechanical lint check

- title, description, template, hook, code, paragraphs, length, close: confirmed.
- summary block PASS: rejected. The count is right, but the bullets are topics.
- headings: the FAIL is confirmed, but the count is wrong. There are 7 H2s, not 6, so the cap is breached as well as the banned names.
- cta count PASS: confirmed. There is 1 link to https://example.org/start (line 51).
- punctuation and padding, banned words: confirmed. "!" is on line 19, "Additionally" and "It is worth noting" are on line 19, "seamless" is in the title and "best-in-class" is on line 51. These are mostly voice issues and outside my lane, so I list no separate findings for them.
- Lint line numbers for title and description say 1; in the numbered draft they are lines 2 and 3.

## Findings

All findings are in the JSON block below.

```json
{
  "editor": "structure",
  "score": 1,
  "summary": "All 10 structure items fail: oversized banned-word title and description, topic-only summary, 7 H2s with Introduction/Conclusion, missing limits section, definition hook, unlabelled code, 9-sentence paragraph, summary close, 437 words.",
  "findings": [
    {"severity": "blocking", "line": 2, "quote": "The Ultimate Guide to Closing Your Books Faster With a Seamless Month-End Process", "issue": "Title is about 81 characters (limit 70) and uses the banned 'Ultimate' and 'Guide to'; it names a topic, not an outcome.", "fix": "Replace with an outcome title under 70 characters, for example one that states how many working days the close drops by."},
    {"severity": "blocking", "line": 3, "quote": "Learn how small service businesses can close the books faster", "issue": "Description is about 169 characters (limit 155) and reads as a feature list.", "fix": "Cut to 155 characters or fewer, one clickable sentence that leads with the 9-to-5 working-day result."},
    {"severity": "recommended", "line": 12, "quote": "- Receipts", "issue": "Summary bullets (lines 12-15) are topics, not conclusions. Count is fine at 4, content fails. This rejects the lint PASS. The quote is under the 3-word minimum because the bullet is that short.", "fix": "Rewrite each bullet as a conclusion with a number, for example 'Weekly bank matching turns a monthly slog into a 20-minute job'."},
    {"severity": "blocking", "line": 17, "quote": "## Introduction", "issue": "Banned H2 name. The draft also has 7 H2s against the max of 6 (the lint's 6 is wrong).", "fix": "Delete the Introduction section, move its one usable fact into the hook, and bring the total to 6 H2s or fewer."},
    {"severity": "blocking", "line": 49, "quote": "## Conclusion", "issue": "Banned H2 name, and it is the closing section.", "fix": "Rename to a heading that carries the next step, and drop the recap."},
    {"severity": "blocking", "line": 0, "quote": "", "issue": "Required guide section 'When this does not apply' is missing, so the template (summary, steps, limits, CTA) is incomplete.", "fix": "Add an H2 'When this does not apply' after Step 4 and before the close, stating who this routine will not help."},
    {"severity": "blocking", "line": 8, "quote": "Month-end close is the process of reviewing, reconciling and finalising", "issue": "Hook is a definition. It has no specific number, unseen failure or counter-claim.", "fix": "Open with the pilot number, that the median close fell from 9 working days to 5, or that 31% of expense lines had no receipt on day one."},
    {"severity": "recommended", "line": 35, "quote": "```", "issue": "Code fence has no language label. The quote is under the 3-word minimum because the line is only the fence.", "fix": "Label the fence, for example ```text, so the checklist copies cleanly."},
    {"severity": "blocking", "line": 19, "quote": "Most teams spend far too long on month-end.", "issue": "Paragraph runs 9 sentences against a cap of 4, a wall of text.", "fix": "Split or cut to 4 sentences or fewer. Most of it is dropped with the Introduction section."},
    {"severity": "blocking", "line": 51, "quote": "Closing faster is not about working harder.", "issue": "Close recaps the article and pitches the product instead of giving one next step. The CTA link text does not match the single ask in the CTA section.", "fix": "Replace the recap with one sentence asking the reader to run last month through the free close checklist, linked once to https://example.org/start."},
    {"severity": "blocking", "line": 0, "quote": "", "issue": "Draft is about 437 words, under the 700-1600 band for a guide.", "fix": "Add the missing limits section and develop the steps with pilot numbers until the draft sits inside the band."}
  ]
}
```
