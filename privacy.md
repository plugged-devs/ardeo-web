# Privacy policy

**ardeo** · Last updated 23 September 2026

ardeo records prayer walks. Recording a walk means recording where you walked,
which is sensitive, and this policy exists to say plainly what happens to that
information.

We are based in New Zealand and handle personal information under the Privacy
Act 2020.

---

## The short version

- **An account is required.** Every screen sits behind sign-in — Apple, Google,
  or a link emailed to you. There are no passwords.
- **The line you walked never leaves your phone.** Not to your friends, not to
  your group, not to the public, not to us. There is nowhere on our server to
  put it.
- **Every walk you save is uploaded**, including ones you keep private.
  *Private* means nobody else can see it. It does not mean it stays on your
  phone.
- What travels instead of a route line is a **list of grid squares about 65
  metres across** — which squares you passed through, not the path through
  them.
- We do not sell your information, show you ads, or use advertising trackers.
  There is no analytics or tracking library in the app at all.

---

## What ardeo records

**Location.** While a walk is recording, ardeo reads your phone's GPS position
repeatedly. This is the core function of the app and cannot be turned off while
recording, though you can pause or stop at any time.

ardeo **does not read your location when you are not recording a walk.** There
is no tracking between walks.

If you turn on background recording, the app keeps recording while your screen
is off, while you are in other apps, and — on Android — after the operating
system shuts it down or the phone restarts mid-walk. That is asked for
separately from basic location permission, and it has its own setting, because
it is a bigger thing to agree to.

**Steps.** If your phone has a step counter, ardeo reads it during a walk and
shows the count in the walk summary. Steps never affect the recorded distance.

**Walk statistics.** Distance, duration, moving time, start and end times.

**Coverage areas.** Your route is converted, on your phone, into a grid of
hexagons roughly 65 metres across. These record *that* you passed through an
area, not the path you took through it.

**What you write.** A note on a walk, up to 600 characters.

**Marks.** Anything you mark during a walk — the categories you pick, and any
photo you attach — stays on your phone. Marks are not uploaded.

**Your profile.** A display name, a handle, and a photo if you add one.

**Account details.** Your email address, held by our sign-in provider. If you
use Sign in with Apple you can choose to hide it, and we receive a relay
address instead of the real one.

---

## Where it goes

There is one place: our database, hosted by **Supabase in Sydney, Australia**.
Holding New Zealanders' information offshore is something we should tell you
rather than bury, so: it is offshore, it is in Australia, and Supabase holds it
under contract to handle it only as we instruct.

**Every walk you save is uploaded** once the app has worked out its coverage —
the statistics, the note, the grid squares, and which audience you chose. That
includes walks set to private. What stops anyone else reading a private walk is
row-level security enforced by the database itself, not a filter in the app, and
it is tested against a real database rather than a stand-in.

**Your route line is never uploaded, at any setting, to anyone.** The server has
no column to store one. That is deliberate and it is the strongest guarantee in
this policy: the cheapest way to be certain a route is never leaked is to have
nothing to leak.

---

## Who can see what

A finished walk is given to one of four audiences. **They are four separate
audiences, not a ladder.** A friend does not see a walk you shared to a group
they are not in, and a group does not see one you shared to friends.

| | You | Friends | A group you shared to | Anyone signed in |
|---|---|---|---|---|
| The line you walked | On your phone only | Never | Never | Never |
| The grid squares you covered | Yes | If shared to friends | If shared to that group | If shared publicly |
| Distance, duration, date | Yes | If shared to friends | If shared to that group | If shared publicly |
| Your note | Yes | If shared to friends | If shared to that group | If shared publicly |
| Display name, handle, photo | Yes | Yes | Yes | Yes |
| Coverage totals for an area | Yes | Yes | Yes | Yes |

### What sharing a walk actually reveals

A shared walk travels as the list of 65-metre squares it passed through. That is
coarser than a route line — it does not show which side of a street you took, or
where you doubled back, or how long you stood still — but it is still a record
of where you were, with your name on it, for whoever you shared it with.

**It is not trimmed at the ends.** If a walk started at your front door, the
square containing your front door is in that list. The *Hide the start and end
of my walks* setting trims route lines, and no route line is uploaded, so today
that setting does not change what a shared walk reveals. Until it does, treat
sharing a walk that starts at home as telling that audience roughly where you
live.

Keeping a walk private avoids this entirely: a private walk is visible to nobody
but you.

### The coverage map

The coverage map counts every walk, private ones included. That is the point of
it — the ground that was prayed over, not the people who covered it.

What makes that safe is what the coverage figures do not contain: no account,
no walk, and no time finer than a calendar day. A square reports how many
distinct walker-days touched it and the most recent date. Two people on one
street on one day is 2; one person walking it three times in a day is 1. There
is no way to join two squares back into a journey.

### There is no administrator view

No report exists, in the app or internally, that shows which member of a church
walked where. There is no such report because there is no route to build one
from. Group reporting is participation counts and coverage totals.

---

## Finding people, and being found

Signed-in walkers can search for people by handle or display name, three
characters minimum. Your display name, handle and photo are visible to anyone
signed in who finds you.

Friend requests have to be accepted. A pending request grants nothing.

If you add a profile photo, our server re-encodes it to a 512-pixel square
before storing it. Rebuilding the image from its pixels discards every piece of
embedded metadata, including the GPS coordinates a phone camera writes into a
photo. The file you uploaded is never stored, and there is no path by which an
unstripped image can reach our storage.

---

## Who else is involved

**Supabase** — our database, sign-in, and file storage, in Sydney, Australia.

**LINZ Basemaps**, run by Toitū Te Whenua Land Information New Zealand — the map
imagery. Your phone asks LINZ for map tiles covering the area you are looking
at, so LINZ sees which areas you view. It is not sent your walks.

**Expo** — delivers app updates over the air.

**Apple and Google** — the app stores, and the sign-in providers if you use
them.

We do not use advertising networks, analytics SDKs, or third-party trackers.

---

## Keeping and deleting

Walks are kept until you delete them or delete your account.

**To delete your account**, see [our deletion page](./delete-account.md).
Deleting in the app is immediate — you're signed out straight away — and
removal from our servers completes within 30 days.

Deleting removes your profile, your photo, your walks and their statistics,
your notes, and your grid squares. If you're the only owner of a group, the
group — and everyone's membership in it — is deleted along with your account.

The **coverage totals you contributed are not reversed** — a coverage count
records that an area was prayed over on a given day. It has no person attached
to it and cannot be traced back to you, so those counts stay. Other people's
records of their own neighbourhoods are built from the same totals, so
removing yours would corrupt theirs. Nothing that identifies you survives
deletion.

Data held only on your own phone goes when you delete the app. We cannot
recover it for you.

---

## Your rights

Under the Privacy Act 2020 you can ask what personal information we hold about
you, ask us to correct it, and complain to the Office of the Privacy
Commissioner if you think we have mishandled it.

For anything the app does not show you directly, contact us.

---

## Children

ardeo is not directed at children under 13 and we do not knowingly collect their
information.

---

## Changes

If this policy changes in a way that affects what we do with your information,
we will tell you in the app before the change takes effect.

### What changed on 18 September 2026

The app changed a great deal after the first version of this policy was written
on 26 August, and several things it said are no longer true. Rather than edit
them away quietly:

- These pages still carried the old name, **anypray**. The app is **ardeo**.
- There was a mode where you could use it **without an account**, and nothing
  left your phone. There is no longer any such mode — sign-in is required.
- The policy said walks **sync** when you sign in, and that a **clipped route
  line** was uploaded. Neither happens. No route line is uploaded at all, and
  what is uploaded is grid squares.
- The policy implied a private walk stays on your phone. It does not: it is
  uploaded and kept private by the database.
- Groups, friends, handles, profile photos, walk notes and the coverage map did
  not exist yet and are now described above.

### What changed on 23 September 2026

Account deletion moved from an email-only request to in-app self-service, with
email kept as a fallback for a lost phone or lost access to the address you
signed in with. Deleting in the app is immediate — you are signed out right
away, and removal from our servers completes within 30 days, rather than the
7-day human confirmation this page used to describe.

---

## Contact

**Email:** [ksyong1964@gmail.com](mailto:ksyong1964@gmail.com)

---

*ardeo is in beta. The app is provided as-is while we test it, and some features
described here arrive over the course of the beta.*
