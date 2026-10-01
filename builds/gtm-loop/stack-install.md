# Stack install: every account, key, permission and check

Go top to bottom. Do not start the next tool until the check on the current one passes.
A tool you installed but never checked is the one that fails quietly in week three.

## Where keys live

One folder on your computer for secrets. One file per tool, for example `secrets/smartlead.env`
holding one line: `SMARTLEAD_API_KEY=...`

- Lock the files so only you can read them. On a Mac or Linux: `chmod 600 secrets/*.env`
- Never paste a key into a chat, Slack, an email or a shared doc. Email apps and chat tools
  reformat long strings, and a key that arrives with one character changed fails as if it were
  revoked.
- Never type a key into a script. Scripts read it from the file.
- When you replace a key, put the new one in and check it works **before** you revoke the old one.

---

## 1. Claude

**Used in:** every step.

1. Sign in at https://claude.ai. Pro ($20 a month) if you hit limits.
2. Make a Project for the loop and add your business file to Project knowledge.
3. For any step you automate later, make an API key at https://console.anthropic.com
   (Settings, API keys). Set a monthly spend limit in the same console.

**Connections (MCP).** In claude.ai: Settings, then Connectors. Add the tools you use from the
list. In Claude Code, the terminal version: `claude mcp add` (details in `connections.md`).

**Check:** in the Project, ask "what do I sell and who buys it". It answers from your file.

---

## 2. Scrapling (free scraper)

**Used in:** steps 1, 2, 4 and 5. Reads company sites, forums, review pages and job boards.

```bash
pip install "scrapling[all]"
scrapling install
```

The second line downloads the browsers it uses. It is open source (BSD-3) and costs nothing.

**Do not use it for:** LinkedIn or Instagram. Reading those with your own login puts the
LinkedIn account you send from at risk. Use Apify for those (tool 4).

**Check:** fetch one company website and print its first 300 characters. Then fetch a page you
know blocks bots and make sure your code **raises an error**, not an empty result.

---

## 3. Serper (Google search)

**Used in:** steps 1, 2 and 4. Finds reports, forum threads and job ads through Google.

1. Sign up at https://serper.dev. The first 2,500 searches are free, no card.
2. Copy the API key from the dashboard into `secrets/serper.env`.
3. Calls go to `https://google.serper.dev/search` with the key in the `X-API-KEY` header.

**Why not scrape Google directly:** Google returns a near-empty page to most scrapers. It looks
like "no results". It is a block.

**Search inside one forum:** Reddit's own search page loads with JavaScript and comes back blank
to a plain fetch. Search Google instead: `site:reddit.com/r/<subreddit> <your words>`.

**Check:** one search returns results with real URLs and dates.

---

## 4. Apify

**Used in:** step 2 (what buyers say on LinkedIn), steps 3 and 4 (competitor ads, Instagram).

1. Sign up at https://apify.com. Pay per run.
2. Console, Settings, Integrations: copy your API token into `secrets/apify.env`.
3. Actors used in this loop (search them in the Apify Store):
   - `harvestapi/linkedin-profile-posts` for a person's recent posts. About $2 per 1,000 posts.
   - `apify/facebook-ads-scraper` for the Meta Ad Library. About half a cent per ad.
   - `apify/instagram-scraper` for a public Instagram account. A few cents per company.

**Watch for:** a keyword search in the ad library returns everyone who **mentions** the word,
not the company itself. Search by the advertiser's page ID when you have it.

**Check:** run one actor on one profile. Look at the cost line in the run before you run 500.

---

## 5. Apollo (or your existing contact tool)

**Used in:** step 5. Finds the person and their email.

1. Settings, Integrations, API: create a key. Turn on the permission for **people search** when
   you create it. A key without it fails on search and looks like a broken account.
2. Save it to `secrets/apollo.env`.
3. The search call is `POST /api/v1/mixed_people/api_search`. It costs no credits. Getting an
   email (`people/match`) costs credits.

**Watch for:**
- The older `mixed_people/search` returns 422 "deprecated for API callers". The key is fine.
  Change the endpoint.
- `organizations/bulk_enrich` costs credits. When you run out it returns **422** "insufficient
  credits", not the 402 or 403 most tools use. Code that only stops on 402 and 403 keeps
  running, does nothing, and reports success.
- Apollo also has a Claude connector. It is optional, and its login can expire mid-session
  ("run /login"). That is the connector, not Apollo being down.

**Check:** one people search for one company returns names. Then one `people/match` returns an
email and you can see the credit come off.

---

## 6. MillionVerifier

**Used in:** step 5. Checks every address before anything is sent.

1. Sign up at https://millionverifier.com. 100 free checks, then about $1.80 per 1,000. Credits
   do not expire.
2. API key from the dashboard into `secrets/millionverifier.env`.

**Watch for:** it blocks the default Python user agent with a 403. It reads exactly like a dead
key. Send a normal browser user agent in the request header.

**Rule:** "ok" goes on the send list. "catch_all" goes on its own list. Everything else is dropped.

**Check:** verify your own address (ok) and a made-up one at your domain (invalid).

---

## 7. Smartlead (email)

**Used in:** steps 6, 7 and 10.

1. Settings: copy the API key into `secrets/smartlead.env`.
2. REST calls go to `https://server.smartlead.ai/api/v1/...?api_key=YOUR_KEY`.
3. Connect it to Claude Code (optional):
   `claude mcp add --transport sse smartlead "https://mcp.smartlead.ai/sse?user_api_key=YOUR_KEY"`

**Watch for:**
- Its firewall blocks the default Python user agent (error 1010). Send a browser user agent.
- The sequence you read back comes in `camelCase` (`delayInDays`). The one you save must be
  `snake_case` (`delay_in_days`), or it fails with a 400.
- The limit is 200 calls a minute **for the whole account**. Two scripts polling at once slow
  each other into errors.
- **Webhooks have three levels:** account, client and single sequence. The public API only shows
  the single-sequence level. A 404 on the others does not mean they do not exist; they are set
  in the app. Use one account-level webhook for replies. A webhook on each sequence is a
  stopgap you will forget to remove.
- **A follow-up sequence made through the API has no schedule.** It accepts people, shows them
  as started, and sends nothing, forever, with no error. Set the schedule and read the status
  back as ACTIVE.

**Check:** load 5 test people, start it, and confirm Email 1 went out in the tool's own
analytics after the first sending window.

---

## 8. HeyReach (LinkedIn)

**Used in:** steps 6, 7 and 10.

1. Connect each LinkedIn account you send from (a "seat").
2. Integrations: create an API key into `secrets/heyreach.env`. Calls go to
   `https://api.heyreach.io/api/public/...` with the key in the `X-API-KEY` header.
3. HeyReach also has a Claude connector for reading stats and building.

**Watch for. Each of these has cost a real build:**
- **A person with no first name or no last name is dropped silently.** The response says 200,
  0 added, 0 failed, and no error. After every load, read the list's total count back and
  compare it with your file.
- **No schedule means no sends.** The campaign shows IN_PROGRESS, people move to "in progress",
  and nothing goes out. Set the schedule before you press start.
- **The steps freeze the moment it starts.** You can edit the text later. You cannot add a step.
  Decide the two touches (first message + one bump) before you start.
- **A new campaign does nothing for 30 to 40 minutes.** That is normal. Pausing and resuming
  restarts the wait. Do not diagnose it in the first hour.
- **Two live campaigns per seat at most:** one for connection requests, one for InMail. More
  campaigns share one queue and slow each other down.
- Variables use single braces: `{FIRST_LINE}`. Double braces send the braces themselves to the
  person. Read one message that actually went out before you trust the rest.
- The endpoint to create a campaign is `/campaign/Create`. Some older guides name a different
  path that returns 404.

**Check:** one test person on a seat you own. Read the sent message in the inbox, braces and all.

---

## 9. Slack

**Used in:** steps 7, 8 and 10. Where reply alerts, bookings and the Monday scoreboard land.

1. Create a Slack app at https://api.slack.com/apps. Give the bot the `chat:write` permission.
2. Install it to your workspace and copy the bot token into `secrets/slack.env`.
3. Invite the bot into each channel it posts to (`/invite @yourbot`). A bot that is not in the
   channel gets `not_in_channel`, and if your code ignores errors, nothing appears.

**Check:** post one test message from a script and see it land.

---

## 10. Calendly

**Used in:** steps 8 and 10.

1. Integrations, API and webhooks: make a personal access token into `secrets/calendly.env`.
2. Webhooks need a paid plan. Subscribe to `invitee.created` and `invitee.canceled`.
3. Calendly's Claude connector can read availability and book a person in directly, so you send
   two times instead of a link.

**Watch for:**
- **Your Calendly reminder emails are set only in the app.** The API cannot change them. If you
  also send reminders from your own email, count both. One booking can easily collect six
  messages in a day across tools.
- A reschedule arrives as a **new** booking with a pointer to the old one. Count it once.
- Count "booked" from Calendly, never from a tracker someone types into. Typed trackers lag.
- Some workflow endpoints return 403 "upgrade to Enterprise". That is a plan limit, not a bug.

**Check:** book yourself a test call through the API or the connector and see the webhook arrive.

---

## 11. Whisper (call transcripts)

**Used in:** step 9.

Either:
```bash
pip install -U openai-whisper    # also needs ffmpeg installed
```
or, faster on a Mac: `brew install whisper-cpp` (the command is `whisper-cli`).

**Watch for:** word timestamps drift on long recordings. Transcribe in 30-second chunks if you
need exact timing. For scoring a call, plain text is enough.

**Check:** transcribe 2 minutes of any recording and read it.

---

## 12. Tracker (Airtable or a Google Sheet)

**Used in:** steps 7 and 10. One row per person who replied: channel, date, what happened next.

Airtable: Builder hub, Personal access tokens. Give it only `data.records:read`,
`data.records:write` and `schema.bases:read`, and only for the one base.

**Rule:** a blank cell means **unknown**, never zero. A blank company size once passed a
"51 to 200 people" filter and a one-person business got a sales call.

---

## 13. Backup AI keys (Gemini, OpenAI)

**Used in:** any step you run as a script.

1. Gemini: https://aistudio.google.com, Get API key. Has a free tier, good for per-row work.
2. OpenAI: https://platform.openai.com, API keys.
3. Use `llm_router_example.py`. It tries Claude, then Gemini, then OpenAI, skips one that is out
   of credit, and **raises an error if all three fail**. Never let a failed AI call return an
   empty answer that looks like "it checked and found nothing".

**Check:** set a wrong Claude key on purpose and confirm the script falls through to Gemini
and says so.
