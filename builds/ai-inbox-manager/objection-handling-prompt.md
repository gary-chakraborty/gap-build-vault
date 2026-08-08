# Objection-handling prompt

Most objections aren't really about what the words say. Someone who says "we can't do
a monthly fee" is often not talking about money at all, they're talking about the
last vendor who took the fee and disappeared. This prompt gets Claude to find the real
reason before it writes a reply, instead of arguing with the surface line.

```
You are diagnosing the real reason behind this objection before writing a reply.

Every objection has layers. The words someone types are the top layer. Under that is
the reason they'd give if you asked "why." Under that is the feeling driving the
reason. Under that is a belief about how the world works. Keep asking "what would make
a person say this" until you hit something that isn't about me at all, it's about
something that happened to them before.

Sort what's underneath into one of five roots:

FEAR: scared of being fooled again, scared of commitment, scared of change, scared of
looking bad for saying yes.
MONEY: either a real budget limit, or money used as a polite way to say no without
saying no.
TRUST: doesn't trust me, my company, the idea, or the process yet.
TIME: either genuinely stretched thin, or time used as a polite deflection.
CONTROL: needs this to feel like their decision. Doesn't want to feel sold to.

Once you've named the root (to yourself, don't say it to them), write a reply that:
1. Acknowledges what they said without arguing or getting defensive.
2. Shows you understand why someone would feel that way.
3. Reframes the situation without attacking their position.
4. Makes the next step (a call, a quick resource) feel low-risk regardless of the
   outcome.
5. Adds one concrete thing that proves you follow through (a guarantee, a real
   result, a specific number).
6. Ends with one question or a soft two-time call offer, never a hard push.

Keep it under 100 words. Longer than a normal reply is fine here, a short reply to
someone who is scared or has been burned before can feel dismissive.

Here's the objection:

[PASTE: the lead's message, and what you sent that got this reply]
```

**Worked example (not a real lead, just to show the shape):**

> Someone writes: *"We looked into something like this before and it just didn't
> work out."*
>
> Layer 1 (what they said): it didn't work before.
> Layer 2 (the reason): a past vendor didn't deliver.
> Layer 3 (the feeling): frustration, and some embarrassment about the money spent.
> Layer 4 (the belief): "people who sell this kind of thing overpromise."
> Root: TRUST, with a thread of FEAR (of being fooled the same way twice).
>
> Reply: *"Makes sense you'd be careful after that; a lot of people we talk to have
> the same story. The difference here is it's written into the agreement, not just a
> promise, so you're not taking our word for it. Worth 15 minutes to see how it's
> actually structured? Thursday at 2pm or Friday at 11am?"*

## The one question that separates a real "no" from a redirect

When a "no" comes with an extra sentence attached, don't treat every extra sentence
the same way. Ask: does this sentence give me something to work with, or does it
close the door?

- **It gives you something to work with** if it names a need, a condition, a
  contrast, or a question ("not now, but we'll need this after we hire someone," "not
  interested, what exactly do you do?"). Treat it as an objection and use the
  framework above.
- **It closes the door** if it's a flat statement with nothing attached, or names a
  fact that rules out working together entirely ("we don't take outside help," "wrong
  person, we don't have that department"). Send one short, polite reply and stop.

One exception: if the "no" also corrects who they actually are or what they actually
do (wrong target, not a flat refusal), that correction is worth one honest follow-up
that fixes the mismatch, not a second copy of the same pitch. If you don't have
anything genuinely specific to offer their real situation, say so plainly and let it
go rather than guessing.
