# The opener-writing prompt

Once a row is verified (see `signal-research-prompt.md`), use this prompt to turn it into a
finished opener. Write your first one by hand if you can, it teaches you the shape faster than
reading about it. After that, this prompt will replicate the shape across the rest of your
rows fast.

## The rules baked into this prompt

- **Under 64 words.** Count them. If the tool goes over, ask it to cut, don't just eyeball it.
- **Line one is the signal**, stated back to the company plainly. Not a compliment, not a
  question, the actual dated event.
- **Line two is the end result that signal implies.** What changes for them because of it.
  Never your pitch. Never your price. Never a meeting ask.
- **7th-grade reading level.** Short sentences. No jargon. Read it out loud, if you'd stumble
  saying it, rewrite it.
- **No bullet points, no calendar link, no company name of yours anywhere in the opener.**

## Banned words and moves

Do not let these into an opener: "leverage," "seamless," "robust," "streamline,"
"game-changer," "revolutionize," "synergy," "circle back," "touch base," "no pressure,"
"just checking in," "honestly," "contract," any price or dollar figure of your own, any
calendar link, any version of "want to hop on a call."

## The prompt

```
Turn this into a cold opener, following the rules exactly.

Company: [name]
Signal: [the dated event]
Why it matters: [your one sentence from the deck]

Rules:
1. Under 64 words total. Count them and tell me the count.
2. Line one states the signal back to them plainly, like you noticed it yourself.
3. Line two is the end result the signal implies for them, in plain words. No pitch.
   No price. No meeting ask. No calendar link.
4. Write at a 7th-grade reading level. Short sentences, no jargon.
5. Do not use any of these words or moves: leverage, seamless, robust, streamline,
   game-changer, revolutionize, synergy, circle back, touch base, no pressure, just
   checking in, honestly, contract, any price, any calendar link, "want to hop on a call."
6. Do not mention my company name or what I sell anywhere in the opener.

Give me the opener as plain text, then the word count on its own line underneath.
```

## Worked example, input and output

**Input:**

```
Company: Harrow Point Logistics
Signal: Opened a new 138,500-square-foot distribution center in Reno, covered in the
local business journal, March 2026.
Why it matters: A facility that size usually outpaces what their current hiring channels
can fill inside a normal ramp-up window.
```

**Output:**

```
Saw Harrow Point's new Reno facility went live last month. A site that size usually
means the ops team is filling warehouse lead and shift supervisor roles faster than the
usual channels can keep up with.

Word count: 36
```

That's the whole job. Feed the tool one verified row at a time, check the word count and the
banned-words list yourself on every output (don't trust the tool's own count blindly), and move
to the next row.

## Labeling it in the deck

Unless you have a specific reason to go further, label every opener as a sample. It proves the
angle without handing over your entire outreach sequence. "Sample opener" is enough, right
under the company's row in the deck.
