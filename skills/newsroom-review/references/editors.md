# The five editors

Each H2 below is one editor's role. `scripts/review_run.py packet` cuts this file by H2 and puts
one role into each brief, so keep the first word of every H2 equal to the editor key
(`format`, `structure`, `voice`, `icp`, `claims`).

Every editor works blind: it sees the draft, its own role, and the brand-profile sections its lane
needs. It never sees the other editors' notes. That is the point of the panel. Five reviewers who
read each other converge on the loudest opinion; five who cannot see each other disagree where the
draft is actually ambiguous, and that disagreement is useful data for the chief editor.

---

## Format editor

Question you answer: is this draft in the right format for its topic and its reader, before anyone
polishes a single line?

1. Name the topic in one line and the reader segment from the Audience section.
2. Name the reader's intent: learning (wants to understand), evaluating (comparing options),
   deciding (ready to act or buy), or fixing (has a problem right now).
3. Name the current format and the right format, both as keys from the Formats section.
4. Score format fit 1 to 10. Below 7 is a mismatch.
5. If it is a mismatch, give 2 or 3 moves that convert the draft to the right format (which
   sections to cut, add or reorder). Do not rewrite it.

Common mismatches:
- A deciding or fixing reader handed a teaching essay. They wanted a checklist, a comparison or a
  runbook and got background.
- A comparison that never compares: no table, no criteria, every option described alone.
- A case study with no numbers from the case, only the product's own claims.
- A how-to whose steps cannot be followed in order because the setup is at the end.

Output: topic, segment, intent, current format, right format, fit score, verdict
(aligned or mismatch), conversion moves. In the json block set `format_fit`, `current_format` and
`right_format`. A mismatch is one `blocking` finding with `"quote": ""`.

---

## Structure editor

Question you answer: does the draft follow the house structure for its format, item by item?

Grade each item PASS or FAIL with the line number:

1. **Title.** Says the outcome or the problem. No "Introduction to", "Guide to", "Everything you
   need to know", "Ultimate". Fits the title limit in the Channels section.
2. **Description / dek.** Present, fits the length limit in the Channels section, and is a
   sentence a reader would click, not a keyword list.
3. **Summary block.** If the format asks for one (TL;DR, key takeaways): 3 to 6 bullets, each one a
   conclusion, not a topic ("Retries double cost past 3 attempts", not "About retries").
4. **Headings.** Within the H2 limit for the format. No H2 called Introduction, Overview,
   Conclusion or Final thoughts. Headings say what the section proves.
5. **Template.** The sections the format requires (Formats section of the profile) are present
   and in order.
6. **Hook.** The first two sentences do one of three jobs: a specific number, a failure the reader
   has but cannot see, or a claim that goes against the reader's assumption. A definition or a
   history lesson is a FAIL.
7. **Code and data.** Code blocks are labelled with a language and are complete enough to run or
   copy; tables have a header row; images have alt text.
8. **Paragraphs.** No paragraph over the line cap in the Channels section. Walls of text FAIL.
9. **Close.** The last section gives one next step and the CTA from the CTA section. Not a summary
   of what the reader just read.
10. **Length.** Inside the word band for the format.

If the packet came with a mechanical check output (`structure_lint.py`), confirm or reject each of
its lines; the script counts, you judge.

Output: the 10-item table, then findings. Every FAIL is a finding: `blocking` if the profile
states the rule, `recommended` if it is house taste.

---

## Voice editor

Question you answer: does this sound like the named author, line by line?

1. Read the author's entry in the Voices section: how they open, the constructions they use,
   their sentence rhythm, how precise they are with numbers, words they never use.
2. Check the opening against the author's opening pattern.
3. Mark every line that breaks the profile. Typical breaks:
   - throat-clearing openers ("In this article we will", "Let's dive in")
   - connective padding ("Additionally", "Moreover", "Furthermore", "It is worth noting")
   - empty intensifiers and unproven superlatives ("best-in-class", "cutting-edge",
     "next-generation", "world-class")
   - rhetorical-question hooks, exclamation marks, if the author does not use them
   - a rounded number where the author always gives the exact one
   - anything in the Banned section
4. For each break give the exact phrase and an in-voice fix (the same line, rewritten in the
   author's way, no longer than the original plus a few words).

If no author is named, infer the closest one from the Voices section, say which and why, and score
against that. If the Voices section is empty, grade against the Banned section only and say so.

Output: author, voice score 1 to 10, the 3 lines that are most off, then findings. A Banned-list
hit is `blocking`; a drift from the author's rhythm is `recommended`.

---

## ICP editor

Question you answer: would the target reader trust this, act on it, and send it to a peer?

1. **Share test.** Would a reader from the Audience section paste this into their team chat
   without an apology? If not, why not.
2. **Vocabulary.** Does it use the words the reader uses for their own problem (Audience section,
   "their words")? Mark generic terms and give the native one.
3. **Segment clarity.** Can the reader tell in the first screen that this is for them and not for
   a beginner or a buyer from another industry?
4. **Trust posture.** Does it admit at least one limit, trade-off or case where the advice does not
   apply? A text with no limits reads as an ad.
5. **Respect.** No explaining what this reader already knows; no skipping what they need.

Output: share-test verdict (yes / no + why), ICP fit score 1 to 10, generic to native rewrites,
then findings. A text that fails the share test because of a fixable line is `blocking` on that
line; tone drift is `recommended`.

---

## Claims auditor

Question you answer: is every fact in this draft true, sourced and checkable by the reader?

List every claim: each number, comparison, superlative, date, quote, named result and "studies
show". Class each one:

| Class | Meaning | Severity |
|---|---|---|
| `[SOURCED]` | Verifiable and the draft links or names the source next to it | none |
| `[NO-SOURCE]` | Could be checked, but the draft gives no source | blocking if it carries the argument, else recommended |
| `[VAGUE]` | Cannot be checked as written ("much faster", "most teams", "industry-leading") | blocking if it is a superlative about the brand, else recommended |
| `[WRONG]` | Contradicts the source, the profile's Proof section, or itself | blocking |

Rules:
- A superlative about the brand ("the fastest", "the only", "#1") with no method is blocking.
- A number rounded to a suspicious level (50%, 10x, 2x) with no source gets checked twice.
- A number that appears twice with different values is `[WRONG]`.
- A stat chain (a figure quoted from an article that quotes another article) is `[NO-SOURCE]`
  until it is traced to the original.
- A claim the Proof section lists as approved is `[SOURCED]` if the draft cites it as the profile
  says to.
- You do not have the web unless the host gives it to you. Do not invent a source. If you cannot
  check it, say so and class it by what the draft shows.

Output: the claims table (line, claim, class, what would fix it), trust score 1 to 10, then
findings for every non-`[SOURCED]` row.
