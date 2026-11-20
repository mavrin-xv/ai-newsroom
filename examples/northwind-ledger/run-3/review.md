# Review: How 14 firms cut their month-end close from 9 working days to 5

**Verdict: FIX** (round 3 of 5). The move to SHIP is only allowed when the blocking items turn out false, and here the FIX comes from 11 real recommended items against a limit of 5, not from blocking items.

| Editor | Score | One line |
|---|---|---|
| Format | 8 | Aligned: guide for a fixing reader; one forward reference, one checklist line out of time order |
| Structure | 9 | All 10 items pass; description at the 155 cap, length about 31 words over the 700 floor |
| Voice (Mara Quinn) | 8 | One vague quantity, one bracketed aside, one vague threshold, one section that ends on a statement |
| ICP | 8 | Passes the share test; first screen never says who the guide is for |
| Claims | 7 | Proof figures used correctly; the opening paragraph mixes one firm's figure with the median and implies cause |

## Blocking (fix all before the next round)

None. The merge found 0 and nothing in the recommended list rises to blocking.

## Recommended (11; fix all or the verdict stays FIX)

1. **Line 8** "One pilot firm spent 9 working days on its month-end close." (claims) `sources.md` has 9 working days only as the pilot median, and has calendar day 10 for firm P-07 only. Drop the one-firm 9-day sentence and open on the P-07 fact: "One pilot firm's owner saw the month's numbers on calendar day 10, a third of the way into the next month." This also clears the merged item on line 8 "calendar day 10" (see Dropped below).
2. **Lines 3 and 8** "with four changes" / "after four changes" (claims). Proof gives the before and after medians, not cause. In line 8 write "the median close was 9 working days before the four changes and 5 after". In line 3 change "with" to "after" and cut one "a" to stay under the cap: "14 pilot customers cut their median close from 9 working days to 5 after four changes: receipts on the day, weekly bank match, a checklist, an early list." (154 characters). The title can stay; it reports what the firms did, with the number from Proof.
3. **Line 8** "Across the 14 firms in our" (icp). Add one sentence at the end of the paragraph saying who the guide is for: "This guide is for service businesses of 10 to 60 people that still close in spreadsheets." Do not say the pilot firms were that segment; neither Proof nor `sources.md` records it. The paragraph is then 4 sentences, at the cap.
4. **Line 12** "the chasing behind the 31% of lines that had no receipt." (claims) Add the scope: "the chasing behind the 31% of expense lines that had no receipt on day 1 of close in our pilot."
5. **Line 19** "the shoebox was where a lot of month-end time went" (claims, voice). Proof measures missing receipts, not time. Replace the clause so the sentence starts: "In our pilot, 31% of expense lines had no receipt on the first day of close ([pilot report](https://example.org/pilot-report), 14 firms, April 2026)." Keep the next sentence.
6. **Line 23** "Put the receipt count on the same Tuesday slot as the bank match in Step 2." (format) Write: "Check the receipt count once a week. Step 2 sets the slot." Then in Step 2, line 29, add after the first sentence: "Count missing receipts in the same slot."
7. **Line 33** "Two lines will keep coming back" (claims). Write "In our experience, two lines keep coming back".
8. **Line 42** "accountant's list sent (it goes out on day 2, before the lines above are done)" (icp, voice, format, claims). Move it to the top of the checklist as "[ ] day 2: accountant's list sent, before the other lines are done". In Step 4, line 49, write "working day 2" and "working day 6" once, so the unit is stated.
9. **Line 45** "Payroll and accruals depend on a clean bank match, so doing them first means doing them twice." (claims) Frame it as a practice, not a rule of bookkeeping: "Post payroll and accruals after the bank match, so the cash side is settled before you book against it." Do not add a figure or a pilot claim the report does not hold.
10. **Line 57** "Under a few dozen bank lines a month, in our judgement" (voice). Write: "Count your bank lines for one month first. If the count is small, a weekly match costs more time than it saves. We did not measure a cut-off. Match monthly and keep the checklist."
11. **Line 60** "No routine survives books that don't tie out." (voice, claims; still open from round 2). Write: "If the close is slow because the chart of accounts is a mess, a routine is hard to keep up on books that don't tie out. Fix the chart of accounts first."

Dropped after checking the draft and `sources.md`:

- Line 8 "calendar day 10" as NO-SOURCE (claims): `sources.md` backs it (firm P-07 interview notes). The arithmetic clash with 9 working days came only from pairing it with the median; item 1 removes the pairing.
- Line 8 "None of the four changes requires new software." (claims): the four changes are fully described on the page (phone photo, weekly slot, printed list, a document to the accountant), so the reader can check it against the steps. It was round 2's own fix. ICP asked to keep it unchanged.

## Conflicts resolved

- Item 3, line 8: icp wanted the pilot firms named as 10 to 60 person service businesses; claims dropped "small service firms" in round 2 as unsourced. Claims accuracy wins, so the segment names the reader the guide is for, not the pilot firms.
- Item 5, line 19: claims and voice offered two fixes in the same direction; took voice's wording because it states only what Proof measures and keeps the link.
- Item 8, line 42: voice wanted the line kept last without brackets, icp and format wanted it moved to the top with a day-2 label. The reader beats the author's habit, so it moves to the top, and the label is written without brackets, which also meets the profile's no-brackets rule.
- Item 10, line 57: in round 2 claims kept the rounded threshold as judgement; this round voice asks for it out. The profile's written rule for Mara ("Numbers: exact... always with where they came from") wins, and voice's fix is also the more accurate sentence because no cut-off was measured. Took icp's minor wording for "overhead".
- Item 11, line 60: voice wanted an instruction ending, claims wanted the absolute softened. Both apply: the profile's signature move puts the instruction last, and claims accuracy softens the statement before it.

## One highest-leverage change

Rewrite the opening paragraph, line 8, as items 1, 2 and 3 describe. It carries four of the eleven items, it is where the claims score (the lowest at 7) and the ICP score both lose points, and it is the paragraph the owner reads first.

## Minor ledger (logged, not re-raised)

- Line 23: "Here is the part nobody tells you" reads as mild hype (icp). Item 6 rewrites the sentence after it; the phrase itself stays as Mara's signature move, as ruled in round 2.
- Line 57: "overhead" to "costs more time than it saves" (icp). Folded into item 10.
- Line 59: "Steps 1 and 4 still help; Steps 2 and 3 are theirs." to two sentences (voice).

## Noticed, not reviewed

- Length sits about 31 words over the 700 floor and the description is at 154 after item 2; re-run the structure lint after the edits.
- `sources.md` still has no row for "14 firms" as a count or for the P-07 close length; add rows if the opening keeps either.
