# Structure editor verdict: draft-v2 (format: guide)

## Item table

| # | Item | Result | Line | Note |
|---|---|---|---|---|
| 1 | Title | PASS | 2, 6 | States the outcome (5 days instead of 9), 54 chars, under the 70 limit, no banned framing. |
| 2 | Description / dek | PASS | 3 | Present, about 152 chars (limit 155). It is a clickable sentence with a concrete before/after, though it ends in a list of four fragments. |
| 3 | Summary block | PASS | 10-15 | 4 bullets (want 3-5), each a conclusion, not a topic. |
| 4 | Headings | FAIL | 10, 62 | The draft has 7 H2s (Summary, Steps 1-4, When this does not apply, Run your last month...). The profile sets h2_max 6 and does not exempt the summary block. No banned H2 names; headings say what the section proves. |
| 5 | Template | PASS | 10-62 | Summary, steps in order, one limits section ("When this does not apply", line 55), CTA close. Order matches the guide format. |
| 6 | Hook | PASS | 8 | Opens with a specific number (9 working days, day 10) and a failure the reader has. Not a definition or history. |
| 7 | Code and data | PASS | 37-43 | One block, labelled `text`, complete checklist. No tables or images. |
| 8 | Paragraphs | PASS | all | Longest paragraph is 4 sentences (line 45), within the cap of 4. Line 8 is also 4. |
| 9 | Close | PASS | 62-64 | Last section gives one next step (run last month's close, record the day each step finished) and links the CTA url once. It is not a recap. |
| 10 | Length | PASS | all | My count is roughly 700-735 words depending on whether the H1 and code block are counted; the lint reports 723. Inside the 700-1600 band, but with almost no margin. |

## Mechanical lint check

- title, description, summary block, template, hook, code and media, paragraphs, close, cta count, length, banned words: confirmed.
- headings: REJECTED. The lint line says "6 H2 (max 6, summary block not counted)". That exemption is the script's own assumption. The profile states h2_max: 6 with no carve-out for the summary, and the draft literally has 7 `##` headings (lines 10, 17, 25, 35, 47, 55, 62).
- length: confirmed, but flagged as borderline. A stricter counter that drops the H1 and the code block lands near 700.

## Findings

1. blocking, headings: seventh H2. "Summary" at line 10 plus four step H2s plus the limits section plus the close section makes 7 against h2_max 6. Fix: render the summary block under a bold label (e.g. `**Summary**`) instead of an H2, or merge Steps 3 and 4 into one H2. Do not drop a required section.
2. minor, length: the draft sits at the floor of the 700-1600 band, so any trim in later passes could drop it under 700. Keep the word count above the floor when applying fixes.

```json
{
  "editor": "structure",
  "score": 8,
  "summary": "9 of 10 structure items pass; headings fail because the draft has 7 H2s against h2_max 6 and the profile does not exempt the summary.",
  "findings": [
    {"severity": "blocking", "line": 62, "quote": "Run your last month through the checklist", "issue": "The draft has 7 H2s (lines 10, 17, 25, 35, 47, 55, 62) against h2_max 6 for guide; the lint's 'summary block not counted' exemption is not in the profile.", "fix": "Turn the line 10 '## Summary' into a bold label rather than an H2 (or merge Steps 3 and 4 into one H2) so the H2 count is 6."},
    {"severity": "minor", "line": 0, "quote": "", "issue": "Length sits at the floor of the 700-1600 band (lint 723; roughly 700 without H1 and code block), leaving no margin.", "fix": "Keep the word count above 700 when applying any fixes."}
  ]
}
```
