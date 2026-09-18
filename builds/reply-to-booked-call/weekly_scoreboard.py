#!/usr/bin/env python3
"""weekly_scoreboard.py: your email and LinkedIn numbers for the last three weeks, in two tables.

Rows: new people contacted, positive replies, new people booked, positive reply rate, booking rate.
Columns: the two full Monday-Sunday weeks before this one, then this week so far.

Three rules this script will not bend:
  1. Rates divide by NEW PEOPLE CONTACTED, never by emails sent. Emails sent counts every follow-up
     again and makes your rates look about half their real size.
  2. A booking counts on the day the person BOOKS, not the day of the call. A call set for next
     Tuesday counts this week, because this week's work earned it.
  3. A rebook or a reschedule is not a new person. Only someone booking for the first time counts.

A failed read stops the script with a reason. It never prints a zero it did not measure.

Needs (put them in your shell or a .env you source first):
  SMARTLEAD_API_KEY     Smartlead > Settings > API key
  HEYREACH_API_KEY      HeyReach > Integrations > API
  CALENDLY_API_KEY      Calendly > Integrations > API and webhooks > personal access token
  CALENDLY_EVENT_NAME   the exact name of your sales call event, e.g. "Intro call with Acme"
  SMARTLEAD_NAME_PREFIX optional: only count campaigns whose name starts with this
  POSITIVES_CSV         optional: a CSV with columns date,channel,name (one row per positive reply,
                        channel is Email or LinkedIn). It is also how a booking gets its channel.
                        Without it, those rows show "n/a" and every new booking is listed by name.

    python3 weekly_scoreboard.py
"""
import csv
import datetime as dt
import json
import os
import sys
import time
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/124 Safari/537.36"
SL = "https://server.smartlead.ai/api/v1/"
CAL = "https://api.calendly.com/"
LOOKBACK_DAYS = 180
# Follow-up campaigns that re-contact people who already heard from you. They are not new people.
NOT_NEW_PEOPLE = ("chase", "no-show", "noshow", "reactivation", "follow up", "follow-up", "interested")


def fail(why):
    print("STOPPED: " + why)
    sys.exit(1)


def env(name, required=True):
    v = os.environ.get(name, "").strip()
    if required and not v:
        fail("%s is not set" % name)
    return v


def get_json(req, what, tries=3):
    for attempt in range(1, tries + 1):
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as ex:  # noqa: BLE001 - every failed read stops the table
            if attempt == tries:
                fail("%s read failed after %d tries: %s" % (what, tries, ex))
            time.sleep(5 * attempt)


# ---------- email: Smartlead ----------

def smartlead(path, **q):
    q["api_key"] = env("SMARTLEAD_API_KEY")
    url = SL + path + "?" + urllib.parse.urlencode(q)
    # Smartlead sits behind Cloudflare, which blocks Python's default user agent.
    return get_json(urllib.request.Request(url, headers={"User-Agent": UA}), "Smartlead " + path)


def cold_campaigns():
    camps = smartlead("campaigns")
    if not isinstance(camps, list) or not camps:
        fail("Smartlead campaign list came back empty")
    prefix = env("SMARTLEAD_NAME_PREFIX", required=False)
    out = [c for c in camps
           if not c.get("client_id")
           and (not prefix or (c.get("name") or "").startswith(prefix))
           and not any(w in (c.get("name") or "").lower() for w in NOT_NEW_PEOPLE)
           and c.get("status") != "DRAFTED"]
    if not out:
        fail("no cold campaigns matched")
    return out


def email_new_people(campaigns, start, end):
    """Email 1 sends in the week. Each person gets Email 1 once, so this is new people contacted."""
    total = 0
    for c in campaigns:
        r = smartlead("campaigns/%s/sequence-analytics" % c["id"], start_date=start.isoformat(), end_date=end.isoformat())
        data = r.get("data") if isinstance(r, dict) else None
        if data is None:
            fail("no sequence data for campaign %s" % c["id"])
        if not any(int(x.get("sent_count") or 0) for x in data):
            continue
        seqs = smartlead("campaigns/%s/sequences" % c["id"])
        step1 = {s.get("id") for s in seqs if s.get("seq_number") == 1} if isinstance(seqs, list) else set()
        if not step1:
            fail("campaign %s sent mail but has no step 1" % c["id"])
        total += sum(int(x.get("sent_count") or 0) for x in data if x.get("email_campaign_seq_id") in step1)
    return total


# ---------- LinkedIn: HeyReach ----------

def linkedin_new_people(start, end):
    body = {"accountIds": [], "campaignIds": [],
            "startDate": start.isoformat() + "T00:00:00Z", "endDate": end.isoformat() + "T23:59:59Z"}
    req = urllib.request.Request("https://api.heyreach.io/api/public/stats/GetOverallStats",
                                 data=json.dumps(body).encode(), method="POST",
                                 headers={"X-API-KEY": env("HEYREACH_API_KEY"), "Content-Type": "application/json"})
    r = get_json(req, "HeyReach")
    try:
        return int(r["overallStats"]["uniqueLeadsContacted"])   # connection requests + InMails started
    except (KeyError, TypeError, ValueError):
        fail("HeyReach answered without a new-people count")


# ---------- bookings: Calendly ----------

def calendly(url):
    return get_json(urllib.request.Request(url, headers={"Authorization": "Bearer " + env("CALENDLY_API_KEY"),
                                                         "User-Agent": UA}), "Calendly")


def bookings(since):
    me = calendly(CAL + "users/me")["resource"]["uri"]
    event_name = env("CALENDLY_EVENT_NAME")
    out = []
    url = CAL + "scheduled_events?" + urllib.parse.urlencode(
        {"user": me, "min_start_time": since.isoformat() + "T00:00:00Z", "count": 100})
    while url:
        r = calendly(url)
        for ev in r.get("collection", []):
            if ev.get("name") != event_name:
                continue
            for inv in calendly(ev["uri"] + "/invitees?count=100").get("collection", []):
                out.append({"email": (inv.get("email") or "").lower(), "name": inv.get("name") or "",
                            "booked_on": (inv.get("created_at") or "")[:10],
                            "active": inv.get("status") == "active",
                            "is_reschedule": bool(inv.get("old_invitee")),   # the new slot of a moved call
                            "was_moved": bool(inv.get("rescheduled"))})      # the old slot of a moved call
        url = (r.get("pagination") or {}).get("next_page")   # use Calendly's link; a hand-built one fails
    if not out:
        fail("Calendly returned no bookings for '%s'. Check the event name." % event_name)
    return sorted(out, key=lambda b: b["booked_on"])


def new_people_booked(all_bookings, channel_of, start, end):
    seen, out = set(), {"Email": 0, "LinkedIn": 0, "Other": []}
    for b in all_bookings:
        first_time = b["email"] not in seen
        seen.add(b["email"])
        if not (start.isoformat() <= b["booked_on"] <= end.isoformat()):
            continue
        # A first booking that was later moved shows as cancelled. It still counts, once.
        if first_time and (b["active"] or b["was_moved"]) and not b["is_reschedule"]:
            ch = channel_of.get(b["name"].lower().strip())
            if ch in ("Email", "LinkedIn"):
                out[ch] += 1
            else:
                out["Other"].append(b["name"])
    return out


# ---------- positive replies: your own log ----------

def positives():
    path = env("POSITIVES_CSV", required=False)
    if not path:
        return None, {}
    rows = list(csv.DictReader(open(path)))
    return rows, {r["name"].lower().strip(): r["channel"] for r in rows}


def count_positives(rows, channel, start, end):
    if rows is None:
        return None
    return sum(1 for r in rows if r["channel"] == channel and start.isoformat() <= r["date"][:10] <= end.isoformat())


# ---------- the table ----------

def pct(a, b):
    if a is None or not b:
        return "n/a"
    v = 100.0 * a / b
    return "%.2f%%" % v if v < 1 else "%.1f%%" % v


def table(title, cols):
    lines = [title.ljust(24) + "".join(c["label"].rjust(21) for c in cols)]
    for name, fn in (("New people contacted", lambda c: "{:,}".format(c["reached"])),
                     ("Positive replies", lambda c: "n/a" if c["positive"] is None else str(c["positive"])),
                     ("New people booked", lambda c: "n/a" if c["booked"] is None else str(c["booked"])),
                     ("Positive reply rate", lambda c: pct(c["positive"], c["reached"])),
                     ("Booking rate", lambda c: pct(c["booked"], c["reached"]))):
        lines.append(name.ljust(24) + "".join(fn(c).rjust(21) for c in cols))
    return "\n".join(lines)


def main():
    today = dt.date.today()
    monday = today - dt.timedelta(days=today.weekday())
    weeks = [(monday - dt.timedelta(days=14), monday - dt.timedelta(days=8), ""),
             (monday - dt.timedelta(days=7), monday - dt.timedelta(days=1), "")]
    if today > monday:
        weeks.append((monday, today, " so far"))
    rows, channel_of = positives()
    camps = cold_campaigns()
    books = bookings(today - dt.timedelta(days=LOOKBACK_DAYS))
    email, li, other = [], [], []
    for s, e, tag in weeks:
        label = "%s-%s%s" % (s.strftime("%d %b"), e.strftime("%d %b"), tag)
        nb = new_people_booked(books, channel_of, s, e)
        email.append({"label": label, "reached": email_new_people(camps, s, e),
                      "positive": count_positives(rows, "Email", s, e), "booked": None if rows is None else nb["Email"]})
        li.append({"label": label, "reached": linkedin_new_people(s, e),
                   "positive": count_positives(rows, "LinkedIn", s, e), "booked": None if rows is None else nb["LinkedIn"]})
        other.append("%s: %s" % (label, ", ".join(nb["Other"]) or "none"))
    print("Scoreboard as of %s\n\n%s\n\n%s\n\nNew people booked, channel unknown: %s"
          % (today.isoformat(), table("EMAIL", email), table("LINKEDIN", li), " | ".join(other)))


if __name__ == "__main__":
    main()
