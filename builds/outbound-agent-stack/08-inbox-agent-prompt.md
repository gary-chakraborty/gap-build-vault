# Agent 8 — Inbox Agent

**What it answers:** what to send back, within five minutes.

Answering fast is what tells a prospect this is a real operation. It is also the
cheapest thing on this whole page to fix.

```
You are my inbox agent. Read my business block above.

I am going to paste a reply from a lead, with the email they were replying to.

Give me three things.

1. THE COLOUR
   GREEN — they are leaning in. Interested, asking how it works, asking a question with
   no objection attached.
   YELLOW — they have not said yes or no. Vague, a soft stall ("check back in Q1"), or
   a real objection (price, trust, "we already have someone").
   RED — a flat no. "Not interested", "remove me", "unsubscribe", with nothing else.

2. ONE LINE ON WHY

3. THE DRAFT TO SEND
   Pick the script that matches the colour AND what they actually said. A positive
   reply and an objection are different scripts. Do not use one for the other.
   Fill it in with their own words, from their own reply.

RULES

- Judge what they said, not how it sounded. A blunt one-liner that asks a real question
  is GREEN, not RED.
- A "no" with a reason attached is YELLOW. They told you something.
- If you genuinely cannot tell, say YELLOW and give me the one question to ask.
- Never put a price in a reply, even when they ask directly. Answer the question
  honestly ("it depends on scope, that is what the call is for") and move to the times.
- Never a calendar link. Two specific times: a day and an hour, both real.
- If they ask three questions, answer all three, in order, then ask for the call.
- If they say the wrong person handles this, do not pitch them. Ask for the name.

Here is the reply:

[PASTE: what you sent, then what they said back]
```

## Wire it up so nothing waits

The prompt above works with copy and paste on day one. If you want it hands-off:

1. A reply lands in your sending tool.
2. A **webhook fires immediately** — nothing polls, nothing waits for someone to open
   the inbox.
3. The reply text goes to Claude with the rules above.
4. The colour, the reason and the draft come back.
5. It posts into Slack, or saves as an unsent draft, with the draft already written.
6. **A person reads it and presses send.**

Step 6 is not optional. An agent that sends on its own will eventually send something
you would not have.

> **Poll nothing.** A schedule that checks every 15 minutes has already lost you 15 of
> your 5 minutes. Trigger on the event.

## What good output looks like

Real reply, from the campaign in this build:

> "wha'ts your number"

```
GREEN
Why: they are asking to be sold to. Asking for the number is the hottest signal there
is, and it means the call, not a quote.
Next: do not put a price in writing. Two times, today or tomorrow.
```

## When it goes wrong

| What you see | What it means | What to do |
|---|---|---|
| A short blunt question came back RED | It judged tone | Paste the definitions back and add "judge the words, not the tone" |
| It quoted a price | Your rules slot was empty | Fill the price rule in your business block. Write "never quote before a call" if that is the rule |
| It offers times you are not free | It cannot see your calendar | Paste your two real open slots into the chat each morning |
| It sent something on its own | You automated past the human step | Set every message node to create a draft, never to send |
| Replies arrive but nothing fires | The webhook was never saved, or it is on the wrong scope | Send yourself a test reply and watch it run. A rail that fails quietly is worse than no rail |
