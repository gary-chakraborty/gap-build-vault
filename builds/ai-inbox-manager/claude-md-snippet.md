# CLAUDE.md knowledge-base snippet

Paste this block into your own `CLAUDE.md` file, or at the top of a new Claude
conversation if you don't use CLAUDE.md yet. Fill in every bracket with your own
real details before you use `triage-prompt.md` or `reply-drafting-prompt.md`. Don't
skip a slot and leave a placeholder in, an empty slot means Claude guesses, and a
guess in a reply to a real lead is worse than no reply.

```
## My business, for reply triage and drafting

WHAT I SELL: [one or two sentences, plain language, no jargon. Example: "A monthly
bookkeeping service for law firms, including trust account reconciliation."]

WHO I SELL TO: [job titles and company type/size you actually close. Example:
"Owners and managing partners at law firms with 3 to 25 staff."]

MY REAL PROOF POINTS: [one to three real results with real numbers. Don't round
them, and don't use a result you can't back up if someone asks. Example: "Helped
[client type] cut their close time from 19 days to 6." If you don't have a client
result yet, say what you can honestly point to instead, don't invent one.]

HOW I TALK ABOUT PRICE: [your real rule. Example: "Never a number in writing. If
pushed, I give a range of $X to $Y and move to the call." Fill in your real range,
or write "no range yet, always redirect to the call" if you're not ready to quote
one at all.]

MY GUARANTEE (if you have one): [the real terms, in plain language. If you don't
have one, write "no guarantee yet" so Claude doesn't invent one for you.]

HOW I BOOK CALLS: [your real process. Example: "I offer two times from my own
calendar, never a booking link. I book it myself once they pick one."]

MY TONE: [a few words. Example: "Direct, a little informal, never corporate.
Sign off with my first name only."]

THINGS I NEVER SAY: [any words or phrases that are wrong for your business.
Example: "never 'no cost to start,' we always have a starting fee."]
```

**Why every slot matters:** the two prompts in this build lean on this block for
every reply they draft. A generic "we help businesses grow" in the WHAT I SELL slot
produces a generic reply that reads like every other cold DM. The more specific this
block is, the more the drafted replies sound like you and not like a template.

**Update it when something changes.** New proof point, new price, new guarantee,
come back and edit this block. It's the only place these facts live for Claude, it
won't remember last week's version on its own.
