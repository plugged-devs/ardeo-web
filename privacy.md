# Privacy policy

**ardeo** · Last updated 24 September 2026

ardeo records prayer walks. Recording a walk means recording where you walked,
which is sensitive, and this policy exists to say plainly what happens to that
information.

---

## Who we are

ardeo is made by **Plugged Worship**, a volunteer ministry group based in New
Zealand. Plugged Worship is not a registered company, church or charitable
trust. In this policy "we" and "us" mean Plugged Worship.

We are the agency responsible for your personal information under the
**Privacy Act 2020**. Our privacy officer can be reached at
**[privacy@ardeo.nz](mailto:privacy@ardeo.nz)**.

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
- **Using ardeo says something about your faith.** An account on a prayer app
  suggests a religious belief, and anyone who can see your profile or your
  walks can draw that conclusion. We treat everything here with that in mind.
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
it is a bigger thing to agree to. The location library that does this keeps its
working data on your phone and sends nothing anywhere itself.

**Steps.** If your phone has a step counter, ardeo reads it during a walk and
shows the count in the walk summary. Steps never affect the recorded distance,
and the count is not uploaded.

**Walk statistics.** Distance, duration, moving time, start and end times.

**Coverage areas.** Your route is converted, on your phone, into a grid of
hexagons roughly 65 metres across. These record *that* you passed through an
area, not the path you took through it.

**What you write.** A note on a walk, up to 600 characters.

**Marks.** Anything you mark during a walk — the categories you pick, and any
photo you attach — stays on your phone. Marks are not uploaded.

**Your profile.** A display name, a handle, and a photo if you add one.

**Groups.** The groups you create or join, your role in each, and — for a group
you run — its name, description, logo and cover picture.

**Account details.** Your email address, and the name your sign-in provider
gives us. If you use Sign in with Apple you can choose to hide your email, and
we receive a relay address instead of the real one.

**Technical information.** When your phone talks to our servers, those servers
see its IP address and record it in their logs, along with the time and what
was asked for. We do not use this to track you; it is how the services
diagnose faults and stop abuse.

---

## Signing in

**Apple** and **Google** sign you in through their own screens on your phone.
They tell us your email address and name, and they know you signed in to ardeo.

**Email links** are sent for us by **Resend**, from `sign-in@ardeo.nz`. To send
one, Resend is given your email address and the message, which contains a
single-use sign-in code that expires after an hour.

---

## Where it goes

Your account, profile, groups and walks are stored in one place: our database,
hosted by **Supabase in Sydney, Australia**.

**Every walk you save is uploaded** once the app has worked out its coverage —
the statistics, the note, the grid squares, and which audience you chose. That
includes walks set to private. What stops anyone else reading a private walk is
row-level security enforced by the database itself, not a filter in the app, and
it is tested against a real database rather than a stand-in.

**Your route line is never uploaded, at any setting, to anyone.** The server has
no column to store one. That is deliberate and it is the strongest guarantee in
this policy: the cheapest way to be certain a route is never leaked is to have
nothing to leak.

If you sign in on a new phone, your saved walks come back to it from our
database — with their statistics and grid squares, but no route line, because
there is none to send.

### Information that leaves New Zealand

Most of the services we rely on are overseas. Supabase holds your data in
Australia; Resend, Expo, Apple, Google, GitHub and Cloudflare are based in the
United States. We use them under their terms of service, which require them to
protect the information they handle for us and to use it only to provide their
service. We do not send any of them your walks except Supabase, which stores
them.

---

## Who can see what

A finished walk is given to one of four audiences. **They are four separate
audiences, not a ladder.** A friend does not see a walk you shared to a group
they are not in, and a group does not see one you shared to friends.

| | You | Friends | A group you shared to | Anyone signed in |
|---|---|---|---|---|
| The line you walked | On your phone only | Never | Never | Never |
| The grid squares you covered | Yes | If shared to friends | If shared to that group | If shared publicly |
| Distance, duration, date and time | Yes | If shared to friends | If shared to that group | If shared publicly |
| Your note | Yes | If shared to friends | If shared to that group | If shared publicly |
| Display name, handle, photo | Yes | Yes | Yes | Yes |
| Coverage totals for an area | Yes | Yes | Yes | Yes |

People in a group can see who else is in it, and each member's role.

### What sharing a walk actually reveals

A shared walk travels as the list of 65-metre squares it passed through. That is
coarser than a route line — it does not show which side of a street you took, or
where you doubled back, or how long you stood still — but it is still a record
of where you were and when, with your name on it, for whoever you shared it
with.

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

We can technically read the database, as whoever runs a service can. We look at
individual accounts only to answer a request you make, to fix a fault, or when
the law requires it.

---

## Finding people, and being found

Signed-in walkers can search for people by handle or display name, three
characters minimum. Your display name, handle and photo are visible to anyone
signed in who finds you.

Friend requests have to be accepted. A pending request grants nothing.

### Photos you upload

A profile photo, and a group's logo or cover picture, are re-encoded by our
server before they are stored: a profile photo or logo as a 512-pixel square, a
cover at 1600 × 900. Rebuilding the image from its pixels discards every piece
of embedded metadata, including the GPS coordinates a phone camera writes into
a photo. The file you uploaded is never stored, and there is no path by which an
unstripped image can reach our storage.

---

## Who else is involved

| Service | What it does for ardeo | What it sees |
|---|---|---|
| **Supabase** (Sydney, Australia) | Database, sign-in and photo storage | Everything described above that is uploaded |
| **Resend** (United States) | Sends sign-in emails | Your email address and the sign-in message |
| **Apple** and **Google** | App stores, and sign-in if you use them | Your account with them, and that you use ardeo |
| **LINZ Basemaps**, run by Toitū Te Whenua Land Information New Zealand | Map imagery | Which areas you look at on the map, and your IP address. Never your walks. |
| **Expo** (United States) | Delivers app updates | Your phone's platform, app version and IP address when it checks for an update |
| **GitHub** (United States) | Hosts this website, including the page a sign-in link opens | Your IP address when you visit. The sign-in code never reaches it: it travels in the part of the link a browser does not send. |
| **Cloudflare** (United States) | Runs the ardeo.nz domain and forwards email sent to it | Messages you send to an `@ardeo.nz` address, on their way to us |

Email you send us arrives in a Google Gmail inbox that Plugged Worship uses.

We do not use advertising networks, analytics SDKs, or third-party trackers.

---

## Keeping and deleting

Walks are kept until you delete them or delete your account.

**To delete your account**, open **Settings → Delete account** in the app, or
see [our deletion page](./delete-account.md) if you no longer have the app.
Deleting in the app takes effect straight away: you are signed out, and your
profile disappears from search, from your friends and from your groups at once.
Everything else is removed from our database within 30 days.

Deleting removes your profile, your photo, your walks and their statistics,
your notes, and your grid squares. If you are the only owner of a group, the
group — and everyone's membership in it — is deleted along with your account.

The **coverage totals you contributed are not reversed** — a coverage count
records that an area was prayed over on a given day. It has no person attached
to it and cannot be traced back to you, so those counts stay. Other people's
records of their own neighbourhoods are built from the same totals, so
removing yours would corrupt theirs.

**Copies outside the live database** do not disappear the same moment. Our
providers' service logs, which can include your email address and IP address,
are kept by those providers for up to 30 days. Supabase's own backups roll over
on its schedule. After those periods, no copy that identifies you remains.

Data held only on your own phone goes when you delete the app. We cannot
recover it for you.

---

## Your rights

Under the Privacy Act 2020 you can:

- **ask what personal information we hold about you**, and for a copy of it
- **ask us to correct it** if it is wrong
- **complain to us**, and if we do not resolve it, to the
  [Office of the Privacy Commissioner](https://www.privacy.org.nz)

Email [privacy@ardeo.nz](mailto:privacy@ardeo.nz). We will answer within 20
working days, as the Act requires, and tell you if we need longer and why. We
may need to confirm the request comes from you before we act on it.

---

## If something goes wrong

If a privacy breach involving your information happens and is likely to cause
serious harm, we will tell you and the Privacy Commissioner as soon as we
practicably can, as the Privacy Act requires, and say what happened and what
you can do.

---

## Children

ardeo is not directed at children under 13 and we do not knowingly collect their
information. If you believe a child under 13 has an account, email
[privacy@ardeo.nz](mailto:privacy@ardeo.nz) and we will delete it.

---

## Changes

When this policy changes, we update this page and the date at the top. If a
change affects what we do with information you have already given us, we will
tell you in the app or by email before it takes effect.

### What changed on 24 September 2026

- The policy now says who is responsible for it — Plugged Worship — and gives a
  privacy contact, `privacy@ardeo.nz`, in place of a personal email address.
- It names every service involved, including Resend for sign-in emails, GitHub
  for this website and Cloudflare for the domain, and says which are overseas.
- It covers group logos and covers, restoring walks to a new phone, and what
  our servers log.
- It says plainly that using ardeo suggests a religious belief.
- It says how long copies outside the live database last after you delete your
  account, how to ask for your information and how quickly we answer, and what
  we do after a breach.
- "Distance, duration, date" is now "date and time": a shared walk shows when it
  was posted.
- The promise to tell you in the app before any change is now a promise to tell
  you in the app or by email before a change that affects your information.

### What changed on 23 September 2026

Account deletion moved from an email-only request to in-app self-service, with
email kept as a fallback for a lost phone or lost access to the address you
signed in with. Deleting in the app is immediate — you are signed out right
away, and removal from our servers completes within 30 days, rather than the
7-day human confirmation this page used to describe.

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

---

## Contact

**Privacy questions and requests:** [privacy@ardeo.nz](mailto:privacy@ardeo.nz)
**Everything else:** [hello@ardeo.nz](mailto:hello@ardeo.nz)
