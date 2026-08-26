# Privacy policy

**anypray** · Last updated 26 August 2026

anypray records prayer walks. Recording a walk means recording where you
walked, which is sensitive, and this policy exists to say plainly what happens
to that information.

We are based in New Zealand and handle personal information under the Privacy
Act 2020.

---

## The short version

- You can use anypray **without an account**. In that mode nothing you record
  ever leaves your phone.
- If you sign in, your walks sync so you don't lose them when you change
  phones.
- **The start and end of every route are cut off before anything is uploaded** —
  150 metres from each end by default — because those are usually your home.
- **Nobody can see the path you walked.** Not other walkers, not your group,
  not a church administrator, not us in any product feature. What communities
  see is how many people prayed over an area, never whose route it was.
- We do not sell your information, show you ads, or use advertising trackers.

---

## What anypray records

**Location.** While a walk is recording, anypray reads your phone's GPS
position repeatedly. This is the core function of the app and it cannot be
turned off while recording, though you can pause or stop at any time.

anypray **does not** read your location when you are not recording a walk. There
is no background tracking between walks.

**Steps.** If your phone has a step counter, anypray reads it during a walk and
shows the count as part of the walk summary. Steps never affect the recorded
distance.

**Walk statistics.** Distance, duration, moving time, start and end times.

**Coverage areas.** Your route is converted, on your phone, into a grid of
areas roughly 65 metres across. These record *that* an area was walked, not the
path through it.

**Account details, only if you sign in.** Your email address and a display name.
If you use Sign in with Apple or Google, we receive whatever that provider sends
— you can choose to hide your email address from us when signing in with Apple.

---

## Where it goes

### Without an account

Everything stays in a database on your phone. It is not uploaded, backed up by
us, or readable by us. If you delete the app, it is gone — we cannot recover it
for you.

### With an account

These sync to our servers so you don't lose them:

- Walk statistics
- Coverage areas
- Your profile
- **Clipped** route geometry — see below

**Route clipping.** Before any route leaves your phone, the first and last 150
metres are removed. A prayer walk usually starts and ends at home, and an
uncut route would publish your address. You can lower this in Settings, and
the app makes you confirm you understand the risk before it will let you. The
clipped-off portions still count toward your distance and coverage; they are
simply not stored as a path.

The blur distance is recorded per walk, at the moment the walk starts. Lowering
the setting later does not retroactively un-blur walks you have already
recorded.

---

## Who can see what

| | You | A friend | Your group | Public | A group admin |
|---|---|---|---|---|---|
| Your route | Yes | No\* | No | No | No |
| Walk stats (distance, time, date) | Yes | Yes | Yes | No | Totals only |
| Coverage counts for an area | Yes | Yes | Yes | Yes | Yes |
| Your profile and streak | Yes | Yes | Yes | If public | Yes |

\* Unless you explicitly share a specific walk.

**There is no administrator view of anyone's route.** No report exists, in the
app or internally, that shows which member of a church walked where. Group
reporting is participation counts and coverage totals only.

Coverage counts are aggregated: an area shows how many distinct people prayed
over it on distinct days. Walking the same street three times in one day counts
once.

---

## Who else is involved

**Supabase** hosts our database and handles sign-in. Your synced data is stored
there.

**LINZ Basemaps**, run by Toitū Te Whenua Land Information New Zealand, serves
the map imagery. Your device requests map tiles for the area you are viewing.

**Expo** delivers app updates.

**Apple and Google** operate the app stores and the sign-in providers.

We do not use advertising networks, analytics SDKs, or third-party trackers.

---

## Keeping and deleting

Walks are kept until you delete them or delete your account.

**You can delete your account from inside the app**, in Settings, and also at
[our deletion page](./delete-account.md) without installing anything.

Deleting removes your profile, your walks, your route geometry, and anything you
have written. The **coverage counts you contributed are not reversed** — they are
totals for an area with no person attached, and other people's records depend on
them. The app tells you this before you confirm.

Data on your own device is deleted when you delete the app.

---

## Your rights

Under the Privacy Act 2020 you can ask what personal information we hold about
you, ask us to correct it, and complain to the Office of the Privacy
Commissioner if you think we have mishandled it.

Most of this is available directly in the app. For anything else, contact us.

---

## Children

anypray is not directed at children under 13 and we do not knowingly collect
their information.

---

## Changes

If this policy changes in a way that affects what we do with your information,
we will tell you in the app before the change takes effect.

---

## Contact

**Email:** [ksyong1964@gmail.com](mailto:ksyong1964@gmail.com)

---

*anypray is in beta. The app is provided as-is while we test it, and some
features described here arrive over the course of the beta.*
