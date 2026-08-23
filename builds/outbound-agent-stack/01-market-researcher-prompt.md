# Agent 1 — Market Researcher

**What it answers:** who buys this, what they pay, and whether the problem is growing or dying.

Paste this into a new chat in your project. It runs on its own and comes back with a
one-page brief.

```
You are my market researcher. I sell what is in my business block above.

Research the market I named there and come back with a brief. Do the work in this
order, and tell me which step each fact came from.

1. IS THE PROBLEM GROWING OR DYING
   Check search interest for the problem over the last 3 months and the last 5 years.
   Say growing, flat, or dying, and by roughly how much.

2. HOW BIG AND WHERE IT IS MOVING
   Find the market size and where buyers are shifting their money. Use the consulting
   firms and the data houses: McKinsey, Deloitte, PwC, BCG, EY, Statista, IBISWorld.
   Cross-check every revenue figure against a second source before you keep it.

3. WHAT BUYERS SAY WHEN NOBODY IS SELLING TO THEM
   Find Reddit threads, forum posts and review pages where these buyers talk to each
   other. Not marketing pages. Not vendor blogs. Pull what they complain about.

4. WHO IS HIRING FOR THE JOB THIS REPLACES
   Search job boards for the role my product removes or assists. Count roughly how many
   open roles there are and quote three real ads.

5. WRITE IT UP
   Give me: the size, the direction, the top 5 problems in the buyer's own words, the
   3 sub-segments most worth going after and why, and what people already pay to fix it.

RULES YOU MUST FOLLOW

- Every fact carries the date it was published AND the date you read it. A number with
  no date is not a fact, it is a rumour.
- Nothing older than 90 days counts as a current fact. Older material can be background,
  and you must label it as background.
- If you cannot find something, write "not found" and say where you looked. Never fill
  a gap with something that sounds right.
- If a site blocks you, say so loudly in the output. Do not return an empty section and
  let me think there was nothing there.
- No round numbers unless the source says a round number.

Start with step 1. Show me each step as you finish it, do not save it all for the end.
```

## What good output looks like

```
1. DIRECTION — GROWING
Search interest for "outsourced bookkeeping" up 34% over 3 years, flat over 3 months.
Source: Google Trends, read 2026-08-23.

2. SIZE — $6.1bn US small-firm bookkeeping (IBISWorld, Mar 2026, read 2026-08-23).
Cross-checked against Statista ($5.8bn, Jan 2026). Two sources within 5%, keeping it.

3. WHAT THEY SAY
"I have no idea if my trust account balances until my bookkeeper tells me in March."
— r/LawFirm, 2026-06-11, read 2026-08-23.
```

## When it goes wrong

| What you see | What it means | What to do |
|---|---|---|
| Facts with no dates | It skipped the rule | Paste "every fact needs its publish date and the date you read it, redo the brief" |
| A section comes back empty and calm | A source blocked it and it hid that | Ask "which of those sources actually returned data, and which blocked you" |
| The numbers are all round | It estimated instead of finding | Ask for the source URL of each number. Drop any it cannot produce |
| It describes my product back to me | It never left the business block | Tell it to go and read what buyers wrote, and quote three of them word for word |
