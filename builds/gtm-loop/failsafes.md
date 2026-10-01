# Failsafes: what breaks quietly, step by step

Almost nothing in this loop breaks loudly. A blocked page comes back empty. A load reports
success and stores nothing. A count looks confident and is wrong. Each row below happened on a
real build. The guard is what stops it happening twice.

## The six laws (apply to every step that sends, posts, writes or charges)

1. **A block must be loud.** If a source refuses you, raise an error. Never `return []`.
   "Blocked" and "nothing found" must never look the same.
2. **Read it back.** Never trust a tool's own "OK". After a load, read the count. After a send,
   read the real sent message. After a schedule, read the status.
3. **Lock before you act.** Mark a record "in progress" before the send, so a crash halfway
   cannot send it twice.
4. **Every send has an error route.** A failed send posts an alert. A silent failure looks
   exactly like a quiet day.
5. **Small before big.** 5 test records before 500. 200 list rows before 5,000.
6. **Stop after two surprises.** If a run changes something you did not ask it to change, twice
   in a row, stop and look at the input. Do not retry a third time.

## Step by step

### 1 and 2 · Research and buyer words

| What breaks | What you see | The guard |
|---|---|---|
| A forum or review site blocks the read | "0 posts analysed", report looks complete | The reader raises on a block. A live forum always has posts, so zero is an error |
| A site sends you to a login page instead of blocking | A real page comes back, with no content you wanted | Check for the content you expect, not just the status code |
| A company name matches the wrong website | A confident write-up about a different company | Two checks before using any page: the company's own name appears in the text, and the text says something specific about them |
| Old facts used as current | A report full of numbers with no dates | Every fact carries its publish date. Older than 90 days is marked old, not used as fact |
| You asked for 5 sources and got 1 | A thin report that looks finished | Fewer sources than asked for is a failure, not a smaller result |

### 3 · The offer

| What breaks | What you see | The guard |
|---|---|---|
| A keyword search in an ad library | "Competitor" ads from companies that only mention the word | Search by the advertiser's page ID |
| "They are not running ads" | A zero that is really a parent brand under a different name | A zero is for your own routing only. Never tell a buyer "you are not running ads" |
| Guessing a competitor's ad spend | A spend figure that looks real | Public ad libraries do not publish commercial spend. Do not model one and present it as fact |

### 4 · Who needs it now

| What breaks | What you see | The guard |
|---|---|---|
| A job filter says "posted this week" | Ads that are months old, or gone | Open the ad. The date on the page is the date. On one list, 41% had no live ad |
| A blank field passes a filter | Someone far too small gets a sales call | Blank means unknown. Unknown is dropped, never treated as zero |
| A fact counted as a signal | Almost every company "has a signal" | A signal is a change with a date. "They are a law firm" is not one |
| Silence read as a signal | "Your Instagram has gone quiet" sent to a company with a private account | Never write an absence to a buyer |

### 5 · The list

| What breaks | What you see | The guard |
|---|---|---|
| A billing error logged as "no contact found" | A company marked as having nobody to email | Treat 402, 403, 422 and "insufficient credits" as an outage, never as a miss |
| The verifier blocks your script | 100% errors with credits still in the account | Send a browser user agent before you blame the key |
| One data source only | Hundreds of companies lost that the next source had | Run a waterfall, cheapest first. An empty source is skipped, not fatal |
| Known bad rows ship again | All-caps names, blank cities, the same defects as last time | Mechanical checks before a list is marked ready, not a read-through by eye |

### 6 · Write and send

| What breaks | What you see | The guard |
|---|---|---|
| Missing first or last name (HeyReach) | 200 OK, 0 added, 0 failed | Read the list's total back and compare it with your file |
| No schedule (Smartlead follow-ups, HeyReach) | Status says running. Nothing sends | Set the schedule first, then read the status back as active |
| Different copy loaded as variants of one sequence | Each reason for writing reaches people it does not describe | One reason, one sequence, one list. Variants are only for a true A/B test |
| Variables in the wrong brace style | `{{FIRST_LINE}}` shows up in a sent message | Read one message that actually went out |
| No second touch | Most people get one message and nothing else | Build the bump before you start. Some tools freeze the steps at start |
| Diagnosing too early | Rebuilds of a campaign that was simply warming up | Give a new LinkedIn campaign an hour before you call it broken |

### 7 · Replies

| What breaks | What you see | The guard |
|---|---|---|
| The AI that labels replies runs out of credit | Hours with no alerts at all | Post the card anyway, marked unlabelled |
| A reply alert depends on one platform | Every workflow stops the day it hits its run cap | Reply path on a small relay, plus a backup check a few times a day |
| An old checker kept after you moved the alert path | Every reply looks "missed" | When a path moves, re-point or delete every checker that watched it |
| "Email my colleague instead" read as "wrong person" | A warm handover treated as a no | Keep a test set of tricky replies and run it after any prompt change |
| One webhook for every client | One client's replies land in another's channel | Route on the account or client ID in the payload, never on a name |

### 8 · Booking

| What breaks | What you see | The guard |
|---|---|---|
| Reminders from several tools | One person gets six messages around one call | Count what already went out across every tool before adding a touch |
| An email password expires | Reminder emails stop, nobody notices | Prefer a sender that has no password to babysit, and alert on any failed send |
| A reschedule counted as a new booking | Booked numbers go up for no reason | A booking that points to an old one is the same booking |
| Booked counted from a typed tracker | 3 bookings in a week where the calendar had 9 | Count from the calendar's own records |

### 9 · The call

| What breaks | What you see | The guard |
|---|---|---|
| The most expensive model scores every call | A large bill, no better scores | Best model writes the rubric once. A cheaper model scores every call |
| A booking-call scored against closing skills | A confident, wrong score | Ask "what kind of call was this" before choosing the rubric |
| A brief built from memory | The wrong price or an old guarantee quoted on the call | The brief reads your current offer file, never an older doc |

### 10 · Feeding it back

| What breaks | What you see | The guard |
|---|---|---|
| Emails sent as the bottom number | Every rate looks about half its size | New people reached is the bottom number |
| One blended reply rate | "Things are fine" while one reason carries everything | Split by the reason you wrote to each person |
| A read fails and the report posts anyway | A half-empty scoreboard taken as real | If any source fails, post nothing and say why |
| A test called after 200 sends | A "winner" that is noise | At a reply rate under 1%, you need thousands of sends per side before a winner means anything |

## Your AI calls

Use three providers in a fixed order and skip any that is out of credit. If all three fail,
**raise an error**. A blank AI answer that looks like "it checked and found nothing" is the
most expensive bug in this loop, because nothing tells you it happened. See
`llm_router_example.py`.
