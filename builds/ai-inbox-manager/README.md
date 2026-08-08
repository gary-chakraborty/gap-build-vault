---
title: "Never Lose Another Hot Reply"
oneliner: "Triages, drafts, and books every cold reply so you never lose a hot lead."
tags: [inbox, calls, cold-email, linkedin]
date: 2026-08-08
keyword: INBOX
status: live
---

## What this is

Your outbound inbox, answered the same day, by you, in about ten minutes.

- Sorts every reply into Green, Yellow, or Red in under 10 seconds.
- Writes the exact reply to send back, matched to what they actually said.
- Offers two call times and books the meeting. No calendar link.

## The problem it kills

Sending cold outreach got easy. Answering it did not.

Ten years ago you sent forty emails a week by hand. Now one person sends a thousand. The sending scaled. The replying never did.

So the bottleneck moved. It is not "how do I get replies" anymore. It is "the good reply sat in my inbox for four days."

That is the whole problem. Not lead generation. Not copy. The hot one goes cold while it waits for a free five minutes.

Here is what that actually looks like on a Tuesday.

It is 4pm. You have not opened the outbound inbox since morning. Three replies are sitting there.

One says "interested." It landed six hours ago.

One asks what it costs. You do not want to type a number without thinking, so you leave it.

One is a flat no. It needs nothing from you. But it sits in the same pile, so you keep re-reading all three and answering none.

You close the tab. Client work is due today.

Tomorrow there are five.

Now the cost. Do the arithmetic with your own numbers.

Take what you paid to get one reply. The ad spend, the sending tools, the hour you spent writing the sequence that finally landed. Divide it by the replies you actually got back. That is what one reply cost you.

Now count the ones you answered four days late this month. Multiply.

That is not a marketing number. That is your money, already spent, sitting unanswered in a tab.

And it compounds. Three months of this and you are not running an outbound system. You are running a graveyard of leads who liked you enough to write back.

## How it works

You teach Claude your business once. Then you paste in replies as they come, and it hands back what to do.

Not a piece of software. Nothing to install. No automation to maintain.

Just a conversation you keep open.

1. Paste your business details into Claude once.
2. Paste a lead's reply in when one arrives.
3. Get a color back: Green, Yellow, or Red.
4. Get a drafted reply that matches the color.
5. Read it, fix anything that sounds off, send it.
6. Log the color and what happened.

Green means they want to talk. Yellow means they are interested but stalling. Red means stop spending time here.

## What you get

- [triage-prompt.md](triage-prompt.md): the prompt that reads a reply and hands back a color, the reason, and what to do next.
- [reply-drafting-prompt.md](reply-drafting-prompt.md): the prompt that drafts the actual message to send, by type of reply.
- [objection-handling-prompt.md](objection-handling-prompt.md): the prompt that finds the real reason behind a pushback before writing a reply to it.
- [claude-md-snippet.md](claude-md-snippet.md): the fill-in-the-blanks block that teaches Claude your offer, your ICP, and your rules.
- [setup-checklist.md](setup-checklist.md): the no-code install path and your first week's routine.

## Tools you need

| Tool | What it does here | Free or paid | Link |
|---|---|---|---|
| Claude | Runs the triage, drafting, and objection prompts | Free to start. Pro is $20/mo for higher limits | https://claude.ai |
| Your email inbox | Where cold email replies already land. Nothing to install | Free, whatever you already use | - |
| LinkedIn | Where DM replies already land. Nothing to install | Free | https://linkedin.com |
| A notes doc or spreadsheet | Tracks the color and outcome of each reply | Free. Google Sheets, Notion, or a notebook | - |

## Install it

This takes about 12 minutes. You will not write any code.

1. Go to claude.ai in your browser. Sign up for a free account if you do not have one.
   - You should see an empty chat box with "How can I help you today?" above it.
2. Click the "New chat" button in the top left.
3. Open `claude-md-snippet.md` from this folder. Fill in every bracket with your real details, then copy the whole thing and paste it into the chat box. Press enter.
   - Fill in every bracket. An empty slot means Claude guesses, and a guess in a reply to a real lead is worse than no reply at all.
   - You should see Claude reply saying it understands your business.
4. Open `triage-prompt.md`. Copy it. Paste it into the same chat. Press enter.
   - You should see Claude confirm it is ready to triage replies.
5. Find this chat in the left sidebar. Hover it, click the three dots, and rename it "Inbox" so you can find it tomorrow.
6. Open `reply-drafting-prompt.md` and `objection-handling-prompt.md` in two more browser tabs. Leave them open. You will paste from them later.

How you know it worked: paste in an old reply you already handled yourself. Claude hands back the same color you would have picked, and a draft close to what you actually sent.

## Run it the first time

Paste this into your Inbox chat:

"Hey thanks for reaching out, what's this going to cost roughly?"

Claude should hand back something close to:

> Color: YELLOW
> Why: they are evaluating, not committing, and they asked a direct price question.
> Next: do not quote a number. Acknowledge the question, move to the call.

Now go to your `reply-drafting-prompt.md` tab. Copy it, paste it into the Inbox chat under that result, and press enter.

You should get something close to:

> "Good question. It depends on scope, so it's something we cover on the call. Happy to walk you through it. Thursday at 2pm or Friday at 11am?"

That is the whole loop. Reply in, color out, draft out, send.

The one thing people get wrong: leaving the slots in `claude-md-snippet.md` vague. "We help businesses grow" is vague. A vague slot produces a vague reply that reads like every other cold DM in their inbox.

Go back and fill every slot with your real proof and your real price language before you let a single draft reach a live lead.

## Tell me how it went

I read every one of these. Two minutes, five questions: what you used, how, and what happened. https://form.jotform.com/262191867802059 The best stories become the next build.

## Want this running without doing any of this?

This is one piece of the system we install for B2B service businesses: 15-25 qualified sales calls a month without referrals or hiring a sales team. If you'd rather have the whole thing built for you, grab a call: https://calendly.com/garychakraborty
