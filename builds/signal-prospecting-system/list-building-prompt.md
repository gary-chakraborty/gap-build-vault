# List-building prompt

Copy this into any AI tool that can search the web (Claude, ChatGPT, or a research agent
inside your enrichment tool). Fill in the four bracketed fields from your own signal
definition (Step 1 of `five-step-system.md`) and your niche. The prompt is built so a
row with no source link never makes it into your list. "No source, no row" is not a
suggestion, it's the whole point of the prompt.

```
I'm building a list of [NICHE / INDUSTRY] companies that match one specific signal.

Signal definition: [PASTE YOUR ONE-SENTENCE SIGNAL DEFINITION FROM STEP 1]

Find [TARGET COUNT x 3] companies where this signal happened in the last
[90 days / 12 months]. For each one, give me:

1. Company name
2. What the signal is, in one sentence, specific to this company (not a copy of the
   general definition, the actual event, e.g. "hired a VP of Sales on [date]", not
   "recently hired someone")
3. The exact date the event happened
4. A direct link to the public page where you found it (job post, press release,
   filing, news article, the actual page, not a search results page)
5. The best contact title to reach at this company for this signal

Rules:
- If you cannot find a direct source link for a company, do not include that company.
  A row with no link is worse than a shorter list.
- Do not include a company because it "fits the industry" if you can't point to the
  specific dated event. General industry fit is not the signal.
- If two companies have the exact same signal wording, check both again. A signal that
  reads identically across companies is usually the industry, not the event. Rewrite the
  wording to be specific to each company, or drop the weaker one.
- Give me the list as a table: Company | Signal | Date | Source link | Best contact title
```

## After you run it

Every row still needs a human to open the link and confirm it (Step 3 of
`five-step-system.md`). This prompt gets you a strong first pass, not a finished list.
Treat its output as a draft that hasn't been checked yet, because it hasn't.
