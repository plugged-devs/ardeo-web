# anypray support

**Email:** [ksyong1964@gmail.com](mailto:ksyong1964@gmail.com)

anypray is in beta. If something is wrong, telling us is genuinely useful — a
lot of what we need to fix only shows up on real phones, on real streets.

---

## If you report a problem, please include

1. **Your phone model** — Samsung A54, Pixel 8, iPhone 12, and so on
2. **Whether you have changed any battery settings** for anypray
3. **What you were doing** when it went wrong

The first two matter more than they sound. Most recording failures come down to
one phone manufacturer's battery software, and without knowing the handset we
cannot tell your problem apart from a different one.

---

## The recording stopped partway through my walk

This is almost always the phone's battery manager shutting the app down in the
background. It is the most common problem we see, and it is fixable.

**Samsung:** Settings → Battery → Background usage limits → remove anypray from
*Sleeping apps*

**Xiaomi / Redmi:** Settings → Apps → anypray → Battery saver → *No
restrictions*. Also turn **Autostart** on.

**Oppo / realme:** Settings → Battery → App battery management → anypray →
*Allow background activity*

**Any Android:** Settings → Apps → anypray → Battery → *Unrestricted*

---

## My walk was not saved

Walks under 100 metres or two minutes are discarded on purpose, so that a
mis-tap does not fill your history with empty entries. The app tells you when
this happens.

## The distance looks wrong

anypray ignores GPS readings that imply an impossible walking speed, and pauses
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

Not built yet. anypray currently records walks and keeps your history. The
coverage map is what we are building next.

---

## Privacy

Your route never leaves your phone unless you sign in — and even then, the
first and last 150 metres are cut off first. Nobody can see the path you
walked.

Full detail: [privacy policy](./privacy.md) · [delete your
account](./delete-account.md)
