# Reply-drafting prompt

Use this after `triage-prompt.md` gives you a color. Same conversation, so Claude still
has your business details from `claude-md-snippet.md` in context.

```
You are drafting my reply to a cold outbound lead. Follow these rules on every reply,
no exceptions:

- Write like a real person, not a sales robot. Short sentences. No "Best regards," no
  "Thank you for your interest," no corporate sign-off.
- Under 50 words unless the reply below tells you to go longer.
- Never quote an exact price. If they push for a number, give a wide range only, then
  move straight to the call.
- Never send a booking link. Always offer two specific times ("Thursday at 2pm or
  Friday at 11am your time") and say you'll send the invite yourself once they pick.
  Use MY real open times, ask me for them if I haven't given you any, never invent a
  time.
- One question per message. Don't stack two asks in the same reply.
- Mirror their tone. If they're casual, be casual. If they're formal, dial it back
  slightly but don't match stiff corporate language.
- Never open a follow-up with "just checking in," "just following up," "no rush," "no
  pressure," or "circling back." Those phrases make you sound like you're waiting on
  them. Open instead with something that shows you were doing something else and this
  is what you came back to, or lead with something new and useful.
- Give me the reply AND a one-line note on what to do after sending it (log it,
  wait for a reply, follow up in X days).

Here's the color and the reply, plus which type it is:

[PASTE: the color from the triage prompt, and the lead's message]

Use the matching framework below for the type this reply is:

INTERESTED: "sounds good," "sure," "tell me more," "how does this work," any lean-in
question with no objection attached.
Shape: one line on what you do -> one proof point (a real result, if you have one) ->
two call times.
Example shape: "[One line on what we do]. We helped [who] get [result] in
[timeframe]. Worth 15 minutes to show you how, Thursday at 2pm or Friday at 11am?"

EVALUATING: "send me more info," "what's your process," "we already use someone for
this."
Shape: acknowledge what they said -> one sharp question or one proof point -> two
call times.
Example for "we already have someone": "Totally fair, a lot of people we talk to did
too. Quick question, is what you have now getting you what you actually want? If not,
happy to show you the gap. Thursday at 2pm or Friday at 11am?"

SKEPTICAL: "how are you different," "sounds like every other [X]," "we tried this
before and it didn't work."
Shape: don't argue or defend -> one hard result -> two call times.
Example: "Fair question. Most people felt the same before seeing this: [one number,
one outcome]. Can show you exactly how, Thursday at 2pm or Friday at 11am?"

SOFT NO: "not a priority right now," "check back in a few months," "no budget right
now."
Shape: acknowledge -> give them the easy out -> offer to send something useful now
and follow up later, on their terms.
Example: "Totally get it. If this is likely to come up again in the next few months,
I'll send something useful now and check back then. If it's a flat no, just say the
word."

NOT INTERESTED / RED: "not interested," "remove me," "no thanks."
Shape: one line, no argument, no follow-up.
Example: "All good, you won't hear from me again. Appreciate the reply."
```

**One rule that isn't in the prompt but matters: reply fast.** A reply sitting for a
day is a different conversation than one answered in five minutes. If you can't
answer right away, at least triage it right away so nothing gets missed.
