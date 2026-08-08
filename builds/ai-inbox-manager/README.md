---
title: "Never Lose Another Hot Reply"
oneliner: "Triages, drafts, and books every cold reply so you never lose a hot lead."
tags: [inbox, calls, cold-email, linkedin]
date: 2026-08-08
keyword: INBOX
status: live
---

## What this is

This is the system that reads every cold email and LinkedIn reply, tells you what to do with it, drafts the message, and gets the call booked.

- Sorts every reply into Green, Yellow, or Red in under 10 seconds.
- Writes the exact reply to send back, matched to what they actually said.
- Offers two call times and books the meeting, no calendar link needed.

## The problem it kills

It's 4pm and you haven't looked at the outbound inbox since this morning. Three replies are sitting there. One just says "interested," and it landed six hours ago. One is asking what this costs, and you don't want to type a number without thinking it through, so you leave it. One is a flat "not interested" that doesn't need anything from you, but it sits in the same list as the other two, so you keep re-reading all three instead of answering any of them.

You close the tab and go back to the client work that's actually due today. Tomorrow there will be five replies waiting instead of three, because today's never got answered either.

Every one of those replies cost you something to get, ad spend, a cold email credit, or an hour spent writing the outreach that finally landed. One widely cited study on lead response time found that leads contacted within five minutes are up to 100 times more likely to actually connect than ones left for half an hour. That "interested" reply sitting six hours already cooled off.

The problem isn't that you don't know what to say. You've said it a hundred times on calls. It's that you don't have five free minutes when the reply lands, so it waits for a five minute window that doesn't show up until the moment has already passed.

## How it works

This runs entirely inside a Claude conversation. You paste in your own business details once, then paste in each reply as it comes. Claude gives you back a color, a drafted reply, and a reminder to offer two call times instead of a calendar link.

1. Paste your business details into Claude once.
2. Paste a lead's reply in when one arrives.
3. Get a color back: Green, Yellow, or Red.
4. Get a drafted reply that matches the color.
5. Read it, adjust if needed, then send it.
6. Log the color and the outcome for the week.

## What you get

- [triage-prompt.md](triage-prompt.md): the prompt that reads a reply and hands back a color, the reason, and what to do next.
- [reply-drafting-prompt.md](reply-drafting-prompt.md): the prompt that drafts the actual message to send, by type of reply.
- [objection-handling-prompt.md](objection-handling-prompt.md): the prompt that finds the real reason behind a pushback before writing a reply to it.
- [claude-md-snippet.md](claude-md-snippet.md): the fill-in-the-blanks block that teaches Claude your offer, your ICP, and your rules.
- [setup-checklist.md](setup-checklist.md): the no-code install path and your first week's routine.

## Tools you need

| Tool | What it does here | Free or paid | Link |
|---|---|---|---|
| Claude | Runs the triage, drafting, and objection prompts | Free to start; Pro is $20/mo if you want higher usage limits | https://claude.ai |
| Your email inbox | Where cold email replies already land, nothing to install | Free, whatever you already use | - |
| LinkedIn | Where DM replies already land, nothing to install | Free | https://linkedin.com |
| A notes doc or spreadsheet | Tracks the color and outcome of each reply | Free, Google Sheets, Notion, or a notebook | - |

## Install it

1. Open Claude at claude.ai, or open the Claude app.
   - Sign up for a free account first if you don't have one.
2. Start a new conversation.
3. Paste in `claude-md-snippet.md`, filled in with your real business details.
   - Fill in every bracket. An empty slot means Claude guesses, and a guess in a reply to a real lead is worse than no reply.
4. Paste `triage-prompt.md` into the same conversation, right after it.
5. Name or pin this conversation so you can find it again tomorrow instead of starting over.
6. Keep `reply-drafting-prompt.md` and `objection-handling-prompt.md` open in separate tabs, ready to paste in once triage tells you which one to use.

How you know it worked: paste in an old reply you already handled, and Claude hands back the same color you'd have picked yourself, plus a draft close to what you actually sent.

## Run it the first time

Paste this into your triage conversation: "Hey thanks for reaching out, what's this going to cost roughly?"

Claude should hand back something close to:

> Color: YELLOW
> Why: they're evaluating, not committing yet, and they asked a direct price question.
> Next: don't quote a number, acknowledge the question, redirect to the call.

Paste that result into `reply-drafting-prompt.md`, and you should get something close to:

> "Good question, it depends on scope so it's something we cover on the call. Happy to walk you through it, Thursday at 2pm or Friday at 11am?"

The one thing people most often get wrong: leaving the `claude-md-snippet.md` slots vague, something like "we help businesses grow," instead of specific. A vague slot produces a vague, generic-sounding reply that reads like every other cold DM. Fix: go back and fill every slot with your real, specific proof point and your real price language before you trust a single draft to a live lead.

## Tell me how it went

I read every one of these. Two minutes, five questions, what you used, how, and what happened: https://form.jotform.com/262191867802059. The best stories become the next build.

## Want this running without doing any of this?

This is one piece of the system we install for B2B service businesses, 15-25 qualified sales calls a month without referrals or hiring a sales team. If you'd rather have the whole thing built for you, grab a call: https://calendly.com/garychakraborty.
