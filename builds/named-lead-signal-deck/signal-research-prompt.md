# The signal-research prompt

Paste this into any AI tool that can search the web (Claude with web search on, ChatGPT with
browsing on, Perplexity) or use it to sort through links you already found by hand on Google or
LinkedIn. Its whole job is to find real, dated, checkable events, not to guess or round up.

## The five signal types worth hunting for

Mix these across your 6 to 8 companies. Never fill a whole deck with one type, that reads as a
market condition, not a signal (see `deck-template.md` for why that matters).

1. **A new hire in a decision-making seat.** Especially a new operations, finance, or growth
   lead. New people re-examine who they work with. Give this one a 12-month window, not 90
   days, since it takes a while for a new hire to start changing vendors.
2. **A hiring spike.** A run of open roles on their careers page or a job board that implies
   the exact pain your service solves.
3. **A funding round, acquisition, or new office.** Usually comes with a spending and hiring
   plan the current team wasn't built to run alone.
4. **A new service line, market, or product.** They are doing something today they weren't
   doing six months ago.
5. **A deadline or regulatory pressure.** Something with a real date attached, that pulls their
   own team's attention away from what they'd normally be doing.

## The prompt

```
I am building a list of [NUMBER, 6 to 8] real companies in this market:

Niche or ICP: [describe who you sell to, e.g. "mid-size third-party logistics companies,
100 to 400 staff, US-based"]

What I sell: [one sentence, in plain words]

[Pick one:]
(A) Here is a list of company names I already have: [paste names]. Find a live buying
    signal for each one.
(B) I don't have a list yet. Find [NUMBER] real, currently-operating companies that fit
    the niche above, then find a live buying signal for each.

For each company, find ONE event from this list: a new hire in an operations, finance,
or growth-leadership seat (within the last 12 months); a run of job postings that implies
the pain I solve (within the last 90 days); a funding round, acquisition, or new office
(within the last 90 days); a new service line, market, or product (within the last
90 days); or a deadline/regulatory event that hits their team (within the last
90 days).

Rules, follow these exactly:
1. Every signal must be something you can point to a real, specific source for: a news
   article, a press release, a company's own page, or a job posting. Name the source type
   and the date for every one.
2. If you cannot find a real, dated, sourced signal for a company, say so and drop that
   company. Do not invent one, do not round up a guess into a fact, do not soften an old
   event into a recent one.
3. Do not use the same signal type for more than 2 companies in the list. Mix types.
4. Do not use a fact that is true of the whole industry (like "this market is growing") as
   a signal. It has to be specific to that one company.
5. For each signal, write one plain sentence explaining why it makes this company more
   likely to need what I sell right now than it did six months ago.

Give me the results as a table: Company name | Signal | Date | Source (name the source
type, e.g. "company press release," "job board listing," "local business news") | One
sentence on why it matters.
```

## Checking the output before you trust it

The prompt above is a starting point, not the finished deck. Before any row goes into your
deck:

1. **Open the actual source yourself.** If the tool can't give you a real link or a specific
   source you can go find, treat that row as unverified.
2. **Confirm the date is inside the window.** 90 days for most signal types, 12 months for a
   new hire.
3. **Read the "why it matters" sentence out loud.** If it sounds like it could apply to any
   company in the niche, it's not specific enough. Ask the tool to sharpen it, or write it
   yourself.
4. **If you can't verify it in about three minutes, drop the row.** A deck of six verified
   companies is worth more than one of eight with two soft ones. See `deck-template.md`.

Once you have your verified rows, move to `opener-writing-prompt.md` to turn each one into a
finished opener.
