# Setup checklist

No code, no webhooks, no automation platform. This runs entirely inside a Claude
conversation, with you copying replies in from wherever they already land.

## Where your replies already come from

You don't need a new inbox or a new tool. Replies land in the same two places they
always have:
- **Email replies** show up in your regular email inbox (Gmail, Outlook, whatever you
  already use).
- **LinkedIn replies** show up in your LinkedIn messages.

This build doesn't connect to either one. You copy the reply, paste it into Claude,
get your answer, and paste the answer back. That's the whole loop. It's slower than
an automated pipe, and it's something you can set up today with zero technical setup.

## Copy-paste order, first time

1. In claude.ai, click **Projects** in the left sidebar, then **New project**, and
   name it `Reply Desk`.
2. Put `claude-md-snippet.md`, filled in with your real business details, into
   **Project knowledge** (**Add content**, then **Add text**). Don't move on until
   every bracket is filled.
3. Start a chat inside that project and paste in `triage-prompt.md`.
4. Rename the chat so you'll recognize it later (hover it in the sidebar, click the
   three dots, click **Rename**) so you can find it again tomorrow instead of
   starting over. Project knowledge loads into every new chat in the project, so a
   fresh chat never forgets your business details.
5. Keep `reply-drafting-prompt.md` and `objection-handling-prompt.md` open in two
   more browser tabs, or saved somewhere you can grab them fast. You'll paste one of
   these into the same conversation right after you get a color back.
6. Do one practice run on an old reply you already answered, before you trust it
   with a live lead. Compare what Claude drafts to what you actually sent. If it's
   close, you're set. If it's off, go back and sharpen `claude-md-snippet.md`,
   almost every bad draft traces back to a vague slot in that block.

## Your first week, day by day

**Day 1:** finish the copy-paste order above. Run it on 2 to 3 old replies as a test,
not live leads yet.

**Days 2 to 5:** every time a reply comes in, paste it into the same conversation
with `triage-prompt.md` already loaded. Get the color, then paste in
`reply-drafting-prompt.md` or `objection-handling-prompt.md` depending on what the
triage step told you to do. Read the draft before you send it, this is a co-pilot,
not an autopilot, you're still the one hitting send.

**Somewhere in the middle of the week:** keep a running note (a doc, a spreadsheet,
even a notebook) of the color each reply got and what happened after. You don't need
a fancy tracker, you need to be able to look back and see the pattern.

**End of week 1:** read back through your note. Which colors turned into booked
calls? Which drafts did you have to rewrite before sending? Rewrite the weak slots in
`claude-md-snippet.md` based on what you find, then keep going. The block gets better
every time you fix it against a real reply.

## How you know it's working

You're not re-deciding what to do with a reply from scratch every time one shows up,
and nothing sits for a day because you weren't sure what to say.
