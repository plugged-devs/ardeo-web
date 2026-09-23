# ardeo support

**Email:** [hello@ardeo.nz](mailto:hello@ardeo.nz)

ardeo is in beta. If something is wrong, telling us is genuinely useful — a
lot of what we need to fix only shows up on real phones, on real streets.

---

## If you report a problem, please include

1. **Your phone model** — Samsung A54, Pixel 8, iPhone 12, and so on
2. **Whether you have changed any battery settings** for ardeo
3. **What you were doing** when it went wrong

The first two matter more than they sound. Most recording failures come down to
one phone manufacturer's battery software, and without knowing the handset we
cannot tell your problem apart from a different one.

---

## The recording stopped partway through my walk

This is almost always the phone's battery manager shutting the app down in the
background. It is the most common problem we see, and it is fixable.

**Samsung:** Settings → Battery → Background usage limits → remove ardeo from
*Sleeping apps*

**Xiaomi / Redmi:** Settings → Apps → ardeo → Battery saver → *No
restrictions*. Also turn **Autostart** on.

**Oppo / realme:** Settings → Battery → App battery management → ardeo →
*Allow background activity*

**Any Android:** Settings → Apps → ardeo → Battery → *Unrestricted*

---

## My walk was not saved

Walks under 100 metres or two minutes are discarded on purpose, so that a
mis-tap does not fill your history with empty entries. The app tells you when
this happens.

## The distance looks wrong

ardeo ignores GPS readings that imply an impossible walking speed, and pauses
itself if it thinks you have started driving. If a walk finished with a stretch
that looked like driving, the app asks whether to exclude it.

If the distance is wrong in a way this does not explain, please tell us — with
your phone model.

## The app asked for location twice

It asks for basic location permission first, and only later asks to keep
recording while the screen is off. They are separate on purpose: the second is
a bigger ask and should be a deliberate choice, not something bundled in.

## There is a notification I cannot swipe away

That is required. Android will not let an app keep recording in the background
without showing one, and if it could be dismissed, recording would stop with
it. It disappears when you finish your walk.

## Where is the map?

On the Map tab. It fills in the ground that has been prayed over, counted in
squares about 65 metres across. A square counts a walker once per day, however
many times they walked it.

---

## Privacy

The line you walked never leaves your phone, at any setting, to anyone. A walk
you share travels as the 65-metre squares it passed through, never as a route.

A walk you keep private is still uploaded — kept private by the database, not
left on the phone. The privacy policy says exactly what that means.

Full detail: [privacy policy](./privacy.md) · [delete your
account](./delete-account.md)
