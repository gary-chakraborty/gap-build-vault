# 03b · Competitor ads: what is paying for itself right now

Run this after agent 3 drafts your offer, before you lock it. You need web access in Claude,
or the results of an Apify run on the Meta Ad Library pasted in.

```text
You are checking my offer against what competitors are paying to say right now.

My business file is in project knowledge. Read it first.

1. List up to 10 competitors from my file and from a search. For each, find their ads in the
   Meta Ad Library (facebook.com/ads/library) and the Google Ads Transparency Center
   (adstransparency.google.com). Search by the advertiser's page, not by a keyword. A keyword
   search returns everyone who mentions the word.

2. For every ad you find, record: advertiser, first seen date, days live, how many versions
   of the same ad exist, the promise, the mechanism (how they say it works), the proof, the
   risk reversal, and the call to action. Quote their words exactly.

3. Sort the ads:
   WINNER = live 60 days or more AND 3 or more versions. Someone is paying for it and keeps
   making more of it.
   SURVIVING = live 30 days or more.
   EVERYTHING ELSE = untested. Ignore it.

4. For the WINNERS only, tell me in plain words:
   - the promise most of them make (so mine does not sound the same)
   - the proof most of them skip (so mine can lead with it)
   - one line from my offer to change, and the exact new wording.

Rules:
- If an ad library refuses you or returns nothing, say so. Never write "they are not running
  ads". A zero can mean a parent brand or a different page name.
- Never guess spend. Commercial ad spend is not published.
- Every claim gets the ad's link and the date you read it.
```

**You know this worked when:** you change one line of your offer because a winner already says
what you were about to say.
