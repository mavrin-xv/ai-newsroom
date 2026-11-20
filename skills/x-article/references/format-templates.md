# Five X article formats

Pick one per article, by what the piece has to do. Mixing two (a list that turns into a story
halfway) loses the reader who came for the first one.

| Format | Job | Body shape | Proof that fits | Close |
|---|---|---|---|---|
| Roundup | reach and saves | N cards with the same shape | links to the thing itself, official repos, docs | follow or save; the list is the value |
| System | authority | numbered phases or named layers, one sub-template per section | the config, prompt or checklist itself | the next piece, or the full version |
| Investigation | trust with sceptical readers | thesis, primary sources, one named idea, what would prove it wrong | quotes from the source, a method the reader can rerun | a deeper report or a call |
| Case | shares | one situation in order, with the steps inside the story | before and after numbers, what it cost, what went wrong | a reply keyword or a link |
| Before and after | teach one skill | the problem, side-by-side versions, the name of the technique | diffs the reader can check | a template or the next lesson |

## Roundup

```text
Title: <N> <things> that <outcome> (<scope tag>)
Hook: the one thing every item on the list has in common, or the cost of not knowing it
Cards, same shape each:
  **<number>. <name>**
  What it does, in one line.
  The result someone got with it, with the figure and where it came from.
  The link, the command or the setting to copy.
Close: what to try first if the reader can only try one
```

Keep every card the same length. A reader who skims ten cards should not hit one that is three
times longer than the others.

## System

```text
Title: How to <outcome> with <N> <layers/steps> (<scope tag>)
Hook: the failure the old way produces, in one concrete case
Why the old way breaks (one paragraph, one number)
For each layer:
  ## <Layer name>
  The job of this layer is ...
  What to set up (a code block, a table or a checklist)
  How you know it works
What gets better over time (the loop that makes the system pay off later)
Close: the next piece, or the full version
```

## Investigation

```text
Title: <the claim people repeat> is wrong / <the number> is not what it looks like
Hook: the claim, quoted, with where it comes from
What the primary source says, quoted with a link
The method: what you checked and how a reader can check it
The idea, named, in one sentence
What would prove this wrong (one short section)
Close: the full data or the next question
```

The "what would prove this wrong" section is what separates this from a hot take. Keep it.

## Case

```text
Title: How <who> went from <number> to <number> in <time>
Hook: the moment it was worst, with the number
What they tried first and why it did not work
What changed, step by step, inside the story
The end number, what it cost, what still is not fixed
Close: a reply keyword, a link, or the template they used
```

## Before and after

```text
Title: <Skill>: <N> before-and-after examples
Hook: one bad version the reader will recognise from their own work
For each pair:
  Before (block)
  After (block)
  What changed, in one sentence, with the name of the technique
Close: the checklist that produces the "after" version
```
