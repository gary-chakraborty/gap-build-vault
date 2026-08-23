# Agent 2 — Buyer Psychologist

**What it answers:** the words the buyer uses for their own problem.

This is the cheapest agent in the stack and the one that changes the most. Run it after
agent 1, in the same project.

```
You are my buyer psychologist. Read the market brief from agent 1 above.

Your job is to come back with the words these buyers use themselves. Not my words for
their problem. Theirs.

Work in this order.

1. FIND WHERE THEY ACTUALLY TALK
   Their subreddits. Their trade forums. The review pages for the tools they already
   pay for. Their LinkedIn comment threads, not the posts. List where you looked.

2. READ THE BODIES, NOT THE RATINGS
   On G2 and Capterra, ignore the star scores. Read what people wrote in the 3-star
   reviews. That is where the real complaint lives.

3. LIFT THE PHRASES WORD FOR WORD
   Pull at least 15 direct quotes. Never tidy them up. Never paraphrase. Keep the
   typos. Give me the source and the date for each one.

4. SORT THEM INTO FOUR PILES
   - What their day actually looks like
   - What they are scared of
   - What they want instead
   - What they have already tried that did not work

5. BUILD ONE PERSON
   Not a demographic. One person: their job, their week, the thing that keeps them up,
   the sentence they would say out loud about this problem.

6. GIVE ME THE TOP 5 PHRASES
   The five that a buyer would recognise as their own. These go into my business block
   and every email after this reads from them.

RULES

- A quote you cannot source is not a quote. Drop it.
- If you cannot find real threads, say so. Do not write plausible-sounding quotes. An
  invented quote in an email is the fastest way to sound like every other cold sender.
- Nothing older than 90 days counts as current. Older is background, and label it.
- Do not clean up their language into industry terms. The whole point is that they do
  not talk the way vendors talk.
```

## What good output looks like

> "who reconciles the trust account"
> — r/LawFirm, 2026-05-02, read 2026-08-23

That phrase is not marketing language. It is what small law firms call the thing they
are afraid of. It became the subject line of the campaign in this build, and it is the
whole reason the email worked.

We did not write it. We found it.

## What to do with the output

Open `claude-md-snippet.md`, find the line "words my buyers actually use for their own
problem", and paste the top five in. Update the project knowledge.

Every agent after this one now writes in their language instead of yours.

## When it goes wrong

| What you see | What it means | What to do |
|---|---|---|
| Quotes that sound like ad copy | It wrote them | Ask for the URL and date of every quote. Delete the ones it cannot produce |
| Everything comes from one subreddit | It stopped at the first hit | Name three more places and tell it to go back |
| The phrases are all industry jargon | It read vendor pages, not buyers | Tell it: 3-star reviews and forum threads only, no vendor sites |
| Only 4 quotes came back | The source blocked it and it stayed quiet | Ask which sites returned data and which refused |
