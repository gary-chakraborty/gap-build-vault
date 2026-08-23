# Agent 4 — List Builder

**What it answers:** which of these are real firms, and which just have the right words
on their website.

This is the agent that saves you the most money and the one people skip.

```
You are my list builder. Read my business block and the sub-segments from agent 1.

1. WRITE THE TARGET DOWN AS ONE SAVED SEARCH
   Industry, headcount range, country or state, job titles. One search, written down,
   so I can run the exact same thing again next month and get a comparable list.
   Show it to me before you run anything.

2. RUN IT DOWN THE SOURCES, CHEAPEST FIRST
   In this order, and never out of order:
   a. an export I have already paid for and already have on disk
   b. the free scraper
   c. a tool that came bundled with something I already pay for
   d. prepaid credits I have sitting there
   e. new money — last, and only after you tell me what it will cost
   If a source is out of credit, that is a SKIP, not a stop. Move to the next one and
   tell me it was skipped.

3. DEDUPE
   One row per COMPANY, never one per person. Two people at the same firm is one lead
   with two contacts, not two leads. Merge on domain, not on company name — company
   names are spelled five ways.

4. OPEN EVERY WEBSITE AND READ IT
   This is the step everyone skips and it is the whole agent.
   For each company, open the site and answer three questions from what is actually
   written there:
   - Is this the kind of business I said I was targeting? Yes or no.
   - What do they say they do, in their own words on their own page?
   - Anything that disqualifies them? (they sell the thing I sell, they are a
     marketplace, they are a recruiter, they are an agency for that industry rather
     than a firm in it)

5. BIN EVERYTHING THAT IS NOT WHAT I THOUGHT IT WAS
   Give me two lists: KEEP and BINNED. For every binned row, one line saying why.
   I want to read the bin. That is where I find out my search was wrong.

6. GIVE ME THE COUNTS
   Started with X. Passed the filters, Y. Passed a real read of the business, Z.
   Show me the drop at each step as a percentage.

RULES

- A keyword filter cannot tell a software company from an accounting firm when both
  say "accounting" forty times. Something has to open the page and read it. That is you.
- Never keep a row you could not open. Mark it UNVERIFIED and put it in its own list.
  Unverified is not the same as binned and it is not the same as kept.
- If a site blocks you, say so out loud, per site. An empty result must never look
  like "nothing to find".
- Never fill a missing field from a guess. Blank means unknown, never zero.
```

## What this actually catches

On one real list, 1,642 raw leads became 380 after the quick filters. Then something
opened all 380 sites and read them.

**27% of them were not accounting firms at all.** Software companies, marketplaces and
recruiters with the right words on their pages. A keyword filter cannot see that.

*Measured 2026-07-22. Same pattern held on a second, separate list.*

## When it goes wrong

| What you see | What it means | What to do |
|---|---|---|
| Nothing gets binned | It filtered on keywords, not on reading | "Open each site and tell me what the company actually does, in their words" |
| Two rows for the same firm | It deduped on name | Dedupe on the website domain instead |
| It stopped when a tool ran out of credit | It read a skip as a stop | "Out of credit is a skip. Go to the next source and tell me what you skipped" |
| The bin list has no reasons | It cannot justify the drops | Make it give one line per binned row. Read them. Half your search errors are in there |
