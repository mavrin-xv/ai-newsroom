# Structure editor verdict

Format: guide. Draft: draft-v3. Line numbers refer to the numbered draft in the brief.

## 10-item table

| # | Item | Result | Line | Note |
|---|---|---|---|---|
| 1 | Title | PASS | 2, 6 | States the outcome ("cut their month-end close from 9 working days to 5"). 63 characters, limit 70. No banned opener. |
| 2 | Description / dek | PASS | 3 | Present. I count 155 characters, exactly at the limit of 155. It is a sentence with a number and a result, not a keyword list. No slack for any later edit. |
| 3 | Summary block | PASS | 10-15 | 4 bullets (want 3-5). Each is a conclusion or an instruction with a reason, not a topic. |
| 4 | Headings | PASS | 17-62 | 6 H2 excluding the Summary block (Step 1, Step 2, Step 3, Step 4, When this does not apply, the CTA section). Limit is 6 and the CTA counts. No Introduction, Overview or Conclusion. |
| 5 | Template | PASS | 17-62 | Summary, then steps in order, then one limits section ("When this does not apply", line 55, the required section), then the CTA section. Matches "outcome title, summary block, steps in order, one limits section, CTA". |
| 6 | Hook | PASS | 8 | Opens on a specific number: 9 working days, numbers seen on calendar day 10. Not a definition or history. |
| 7 | Code and data | PASS | 37-43 | The only block is labelled `text` and is a complete, copyable checklist. No tables and no images, so nothing is missing alt text or a header row. |
| 8 | Paragraphs | PASS | all | The longest paragraphs (lines 8 and 45) are 4 sentences, within the cap of 4. No walls of text. |
| 9 | Close | PASS | 62-64 | The last section gives one next step (write down the day each step finished) and the CTA ask from the CTA section, linked once to https://example.org/start. It is not a recap. |
| 10 | Length | PASS | - | My hand count is about 740 words with headings, and the lint says 731. Both are inside the 700-1600 band. The margin over the floor is thin. |

## Mechanical check review

I confirm all 13 lint lines. Two points to be aware of:

- The lint reports the description at "line 1". In the numbered draft it is on line 3 (frontmatter). The result is correct and only the line reference is off.
- The lint's 155-character description count agrees with my count. It is a pass at the limit, not under it.

## Findings

No FAIL items, so no blocking or recommended findings. Two watch notes, not raised as findings:

- The description sits exactly at the 155-character cap and the body sits about 31 words above the 700-word floor. A later cut or rewrite could break either limit, so re-run the check after any edit.

```json
{
  "editor": "structure",
  "score": 9,
  "summary": "All 10 structure items pass for the guide format; description is exactly at its 155-char cap and length is only ~31 words over the floor, so watch both on later edits.",
  "findings": []
}
```
