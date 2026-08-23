# Setup checklist

The order matters more than the tools. Follow it once, then it is a routine.

---

## Before day one — the six logins, 15 minutes

Do these in one sitting. Stopping halfway through a build to go and make an account is
how people put this down and never come back. Open a plain text file and paste each key
into it with the tool name beside it.

- [ ] **Claude** — sign up at https://claude.ai. Free works to start. Pro is $20/month,
      $17 if you pay yearly, and buys higher limits. No key: you use it in the browser.
- [ ] **Scrapling** (free scraper) — https://github.com/D4Vinci/Scrapling.
      `pip install "scrapling[fetchers]"` then `scrapling install`. No key.
      Works when `scrapling shell` opens.
- [ ] **Serper** (search key) — https://serper.dev, no card, 2,500 free searches.
      Key is on the **API Key** page in the dashboard. Works when the balance is not zero.
- [ ] **A contact tool** — use what you already pay for (Apollo, Clay, ZoomInfo, Lusha).
      If you have none, start free at https://apollo.io. In Apollo the key is under
      **Settings → Integrations → API**, and API access is not on every plan — check yours.
      Works when one company you know returns a real name.
- [ ] **MillionVerifier** (verifier) — https://www.millionverifier.com, 100 free credits,
      then from about $1.80 per 1,000, cheaper in bulk, credits never expire. Key is under
      **API** in the left menu. Works when your own address comes back good.
      If you call it from a script, send a normal browser user-agent header — it returns
      403 without one, and a 403 looks exactly like a dead key.
- [ ] **A sending tool** — whatever you use (Smartlead, Instantly, Lemlist, Apollo).
      Two things have to be true: it holds a two-email sequence, and it fires a webhook on
      reply. Works when you send yourself one email, reply, and see the reply in the tool.

**Agents 1, 2, 3 and 8 need nothing but the Claude account.** If you only have 20 minutes
tonight, do that box and go to agent 8.

---

## Day one — 25 minutes, no tools

- [ ] Open https://claude.ai and sign in. A free account works to start.
- [ ] Left sidebar → **Projects** → **New project**. Name it `Outbound Stack`.
- [ ] Open `claude-md-snippet.md`. Fill in **every** bracket. Every one.
- [ ] In the project, right side → **Project knowledge** → **Add content** → **Add text**.
      Paste your filled-in block. Save.
- [ ] Leave the "words my buyers actually use" line blank for now. Agent 2 fills it.

**You know this worked when:** you open a new chat inside the project, ask "what do I
sell and who do I sell it to", and it answers with your real offer and your real buyer.

---

## Day one, part two — learn (agents 1 and 2)

- [ ] New chat. Paste `01-market-researcher-prompt.md`. Let it run.
- [ ] Read the brief. Delete any fact that has no date on it.
- [ ] New chat. Paste `02-buyer-psychologist-prompt.md`.
- [ ] Check three of the quotes yourself. Open the link. If a quote has no source, it
      was invented — say so and make it redo that section.
- [ ] Take the top 5 phrases back into `claude-md-snippet.md` and update your project
      knowledge.

**You know this worked when:** you read a phrase and think "I would never have written
that". That is the point.

---

## Day two — build the list (agents 3, 4, 5)

- [ ] Paste `03-offer-writer-prompt.md`. One promise. One number.
- [ ] Run the pin test on the output. Any slot two people could fill two ways gets
      pinned harder before you move on.
- [ ] Paste `04-list-builder-prompt.md`. Start with **200 leads, not 5,000.**
- [ ] Read the BIN list. That is where you find out your search was wrong.
- [ ] Paste `05-contact-finder-prompt.md`.
- [ ] Verify every address. Drop the invalids. Park the catch-alls in their own list.

**You know this worked when:** your bin list has reasons in it, and you agree with most
of them.

> **Start small on purpose.** A bad list at 5,000 costs you your sending domain. A bad
> list at 200 costs you an afternoon.

---

## Day three — time it (agent 6)

- [ ] Paste `06-signal-finder-prompt.md`.
- [ ] Check five signals at the source yourself. Open the job ad. Read the date on the
      page, not the date on the filter.
- [ ] Split the list: has a live signal → campaign. No signal → watch list.

**You know this worked when:** most of your list did not make it. That is normal. On one
real run, 235 out of 18,799 were worth emailing.

---

## Day four — send and answer (agents 7 and 8)

- [ ] Paste `07-email-writer-prompt.md`.
- [ ] Count the words on email 1 yourself. Under 64 or cut.
- [ ] Load it as **its own campaign**, with its own list. Not as variants.
- [ ] Set it up as two emails: first, then one follow-up on day two. Then it stops.
- [ ] Make the thing your follow-up offers, before you send. It has to actually exist.
- [ ] Paste `08-inbox-agent-prompt.md` into a chat and leave that tab open.
- [ ] Send a test to yourself. Reply to it. Run your own reply through agent 8.

**You know this worked when:** you paste a reply and get back a colour and a draft you
would only change a word or two of.

---

## Week one routine

**Every morning, 10 minutes**
- Paste yesterday's replies into agent 8. Colour, draft, send.
- Paste your two real open call times into the chat first, so it stops inventing them.

**Every Friday, 20 minutes**
- Reply rate **per signal type**, never blended. A blended number hides the one lane
  that works.
- Re-run agent 6 on the watch list. Signals expire. Yesterday's watch list has this
  week's sends in it.
- Anything you changed, write down what and when. A number with no date is not a number.

---

## The gates that are not optional

| Gate | Where | What happens without it |
|---|---|---|
| Every fact carries its date | Agent 1 | You act on an 18-month-old market as if it were today |
| Quotes are sourced or dropped | Agent 2 | An invented phrase reaches a real buyer and reads as invented |
| Somebody opens and reads the sites | Agent 4 | A quarter of your list is the wrong kind of company |
| Every address verified | Agent 5 | Bounces, then your domain |
| Signal confirmed at the source | Agent 6 | You open with a change that never happened |
| Word count on email 1 | Agent 7 | It becomes a pitch and it gets deleted |
| A human presses send | Agent 8 | Eventually it sends something you would not have |
| **A block fails loudly** | All of them | An empty result looks exactly like "nothing to find", and you ship a decision built on it |

That last one holds up everything else. When a site blocks you, it has to say so. An
agent that returns an empty list on a 403 is the most expensive bug in this build,
because nothing looks wrong.
