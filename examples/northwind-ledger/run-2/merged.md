# Merged review: How to close your books in 5 working days instead of 9

**Round 2. Verdict proposal: FIX** (1 blocking finding(s); 13 recommended findings (limit 5))

| Editor | Score | Summary |
|---|---|---|
| format | 8 | Guide is the right format for a fixing reader; only the h2 count (7 vs max 6) breaks the spec. [guide -> guide, aligned] |
| structure | 8 | 9 of 10 structure items pass; headings fail because the draft has 7 H2s against h2_max 6 and the profile does not exempt the summary. |
| voice | 8 | Close to Mara Quinn: real-number opening, signature move, no banned words; drifts on a few vague numbers, one bracketed aside and two non-instruction section endings. |
| icp | 8 | Passes the share test: native vocabulary, clear segment in the first paragraph, honest limits section; only small tone and precision fixes remain. |
| claims | 7 | Headline figures 9 to 5 and 31% match Proof and are linked; no blocking claims, but the anecdote, 'no new software', 'most', and the title promise are unsourced or vague. |

## Blocking (1)

1. line 62 "## Run your last month through the checklist" (format, structure)
   - issue: The draft has 7 h2 headings (Summary, Steps 1-4, When this does not apply, this CTA); the guide format allows at most 6.
   - fix: (pick one)
     - format: Remove this h2 and make the CTA a closing paragraph under the limits section, or an unheaded final paragraph, so the count is 6.
     - structure: Turn the line 10 '## Summary' into a bold label rather than an H2 (or merge Steps 3 and 4 into one H2) so the H2 count is 6.

## Recommended (13)

1. line 2 "How to close your books in 5 working days instead of 9" (claims)
   - issue: A pilot median is presented as the reader's outcome.
   - fix: claims: Add 'median' or 'in our pilot' to the title.
2. line 3 "took 14 small service firms from a 9-day close to 5" (claims)
   - issue: Proof says 14 pilot customers; 'small service firms' is unsourced and 'took' implies causation.
   - fix: claims: Use '14 pilot customers' or source the firm profile.
3. line 8 "The owner saw real numbers on day 10" (claims)
   - issue: Unsourced anecdote; 9 working days is about calendar day 11 to 13, and day 10 is not 'a third' of working days. The scan's 'sourced via sources file' is not checkable by the reader.
   - fix: claims: Link or label the case as illustrative, and state working vs calendar day.
4. line 8 "None of them needs new software." (claims)
   - issue: Absolute claim about all firms with no source.
   - fix: claims: Cite the pilot report or say 'None of the four changes requires new software'.
5. line 12 "it removes most of the chasing" (claims, voice)
   - issue: 'Most' cannot be checked.
   - fix: (pick one)
     - claims: Replace with the pilot figure or drop 'most'.
     - voice: it removes the chasing behind the 31% of lines that had no receipt.
6. line 19 "The shoebox is where month-end time goes." (claims)
   - issue: Unmeasured claim about where time goes.
   - fix: claims: Qualify as pilot observation or support with data.
7. line 21 "It works because the cost lands on the person who can fix it." (claims)
   - issue: Causal claim stated as fact, no evidence.
   - fix: claims: Cite pilot evidence or frame as reasoning.
8. line 42 "[ ] accountant's list sent" (claims)
   - issue: Checklist puts the list last after payroll and accruals, contradicting Step 4 (send on day 2, before everything is finished).
   - fix: claims: Reconcile the checklist order with the day-2 instruction.
9. line 23 "Here is the part nobody tells you:" (icp)
   - issue: Teaser opener reads as content-marketing tone; this reader skims past it and it mildly undercuts the plain, peer voice of the rest.
   - fix: icp: State the point directly: 'The rule only holds if someone checks it weekly.'
10. line 31 "the weekly slot is short" (icp, voice, claims)
   - issue: No figure for the weekly match time; the operations lead needs a number to defend the routine to the owner.
   - fix: (pick one)
     - icp: Give the pilot's typical weekly time if the data supports it, otherwise say plainly that it is unmeasured and the reader should time their own.
     - voice: For a firm with 300 lines a month, the weekly slot took N minutes in the pilot (source). Replace N and 300 with the pilot figures.
     - claims: Give a pilot time or drop the claim.
11. line 51 "(a new hire, a large one-off purchase, a refund)" (voice)
   - issue: Bracketed aside; the profile allows no asides in brackets.
   - fix: voice: Anything unusual this month: a new hire, a large one-off purchase, a refund.
12. line 53 "and day 2 stops feeling early." (voice)
   - issue: Section ends on a feeling, not a plain instruction.
   - fix: voice: Cut the clause and end on: Ask the accountant to answer in the same document, line by line.
13. line 57 "Under a few dozen bank lines a month, a weekly match is overhead." (voice)
   - issue: Rounded, unsourced threshold.
   - fix: voice: Under 40 bank lines a month (state the pilot basis), a weekly match is overhead.

## Minor ledger (5): logged, not re-raised

- line 53: Prediction with no data. (claims)
- line 0: Length sits at the floor of the 700-1600 band (lint 723; roughly 700 without H1 and code block), leaving no margin. (structure)
- line 8: Day 10 in working days is about half a month; a careful reader may stop on the arithmetic. (icp)
- line 60: Generic phrasing where the reader has a native one. (icp)
- line 45: Step ends on a forecast, not a plain instruction. (voice)

## Conflicts for the chief editor (0)

- none

## Findings whose quote is not in the draft (0)

Demoted from blocking. The chief editor checks each by hand before using it.
- none

## Since round 1: 22 resolved, 0 still open

- resolved: The guide format requires a 'When this does not apply' section and the draft has none; it ends on a Conclusion instead.
- resolved: The draft is roughly 450 words, below the 700 minimum for a guide.
- resolved: Unnamed 'studies' and a suspiciously round 50% with no source, carrying the intro's argument. Not in the Proof table.
- resolved: Contradicts Proof: the pilot median went from 9 to 5 working days (44%), not half, and it is a pilot of 14 customers, not all teams.
- resolved: Brand superlative with no method, comparison or source.
- resolved: Unsourced 'most teams' stat. The 7 is not in Proof and sits beside the draft's 9 and 5, giving three different working-day figures.
- resolved: Brand superlative with no method, and 'best-in-class' is on the profile's Banned list.
- resolved: Required guide section 'When this does not apply' is missing, so the template (summary, steps, limits, CTA) is incomplete.
- resolved: Draft is about 437 words, under the 700-1600 band for a guide.
- resolved: Title is about 81 characters (limit 70) and uses the banned 'Ultimate' and 'Guide to'; it names a topic, not an outcome.
- resolved: Description is about 169 characters (limit 155) and reads as a feature list.
- resolved: Hook is a definition. It has no specific number, unseen failure or counter-claim.
- resolved: Banned H2 name. The draft also has 7 H2s against the max of 6 (the lint's 6 is wrong).
- resolved: Paragraph runs 9 sentences against a cap of 4, a wall of text.
- resolved: Banned H2 name, and it is the closing section.
- resolved: Close recaps the article and pitches the product instead of giving one next step. The CTA link text does not match the single ask in the CTA section.
- resolved: Connective padding.
- resolved: Throat-clearing filler and a hedge; Mara states things directly.
- resolved: The summary block is four fragments with no outcomes, and it is labelled TL;DR instead of 'summary'.
- resolved: Matches Proof, but the reader cannot check it: no link, sample size or date next to it.
- resolved: Specific time figure with no basis or source.
- resolved: Code fence has no language label. The quote is under the 3-word minimum because the line is only the fence.
