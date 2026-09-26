"""Send the ardeo beta invite to everyone in a name,email CSV through Resend.

Dry run by default: renders one preview per recipient into previews/ and sends
nothing. Pass --send to actually send.

  IOS_URL=https://testflight.apple.com/join/hTTK9NY3 \
  FROM='ardeo <hello@ardeo.nz>' \
  RESEND_API_KEY=re_... \
  python3 send_invites.py ../beta-requests.csv [--send]
"""

import csv
import html
import json
import os
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
SUBJECT = "You're in: try ardeo early"
BATCH_SIZE = 100  # Resend's batch endpoint limit


def text_version(name, ios_url):
    return f"""Hi {name},

Thanks for opting in to test ardeo!

We had an awesome time worshipping with you yesterday. We hope you carry the missional heart that God has called and sent you for in your daily lives, and we hope ardeo can be a start!

ardeo 테스트에 참여해 주셔서 감사합니다!

어제 함께 예배드릴 수 있어서 정말 기뻤습니다. 하나님께서 품게 해 주신 선교적 마음을 일상 속에서도 간직하며 살아가시길 바라며, ardeo가 그 시작이 되기를 소망합니다!

Open this email on your iPhone and use the link below.

iPhone
Install Apple's free TestFlight app when it asks, then tap Accept and Install.
{ios_url}

Android
Sorry, the Android beta is still in preparation. We'll email you again once it's ready.

Have any feedback? Submit them through https://forms.gle/fW9oL4fAehYqaG3SA

ardeo · prayer walking in Aotearoa New Zealand
hello@ardeo.nz · https://ardeo.nz/privacy
"""


def render(template, name, ios_url):
    return (template
            .replace("{{name}}", html.escape(name))
            .replace("{{ios_url}}", html.escape(ios_url, quote=True)))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    send = "--send" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)

    ios_url = os.environ.get("IOS_URL", "https://testflight.apple.com/join/hTTK9NY3")
    sender = os.environ.get("FROM", "ardeo <hello@ardeo.nz>")
    if not ios_url.startswith("https://testflight.apple.com/join/"):
        sys.exit("Set IOS_URL to the TestFlight public link (https://testflight.apple.com/join/...).")

    with open(args[0], newline="") as f:
        people = [(r["name"].strip(), r["email"].strip()) for r in csv.DictReader(f)]
    template = (HERE / "beta_invite.html").read_text()

    emails = [{
        "from": sender,
        "to": [email],
        "reply_to": "hello@ardeo.nz",
        "subject": SUBJECT,
        "html": render(template, name or "friend", ios_url),
        "text": text_version(name or "friend", ios_url),
    } for name, email in people]

    if not send:
        out = HERE / "previews"
        out.mkdir(exist_ok=True)
        for i, e in enumerate(emails):
            (out / f"{i:02d}.html").write_text(e["html"])
        print(f"Dry run: {len(emails)} emails rendered to {out}/ from {sender}. Nothing sent.")
        return

    key = os.environ.get("RESEND_API_KEY") or sys.exit("Set RESEND_API_KEY.")
    for start in range(0, len(emails), BATCH_SIZE):
        chunk = emails[start:start + BATCH_SIZE]
        req = urllib.request.Request(
            "https://api.resend.com/emails/batch",
            data=json.dumps(chunk).encode(),
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                # Cloudflare in front of Resend blocks urllib's default User-Agent (error 1010).
                "User-Agent": "ardeo-beta-invite/1.0",
                # Re-running the same batch within 24h won't send it twice. Set RUN_ID to send again.
                "Idempotency-Key": f"{os.environ.get('RUN_ID', 'ardeo-beta-invite')}-{start}-{len(chunk)}",
            },
        )
        try:
            with urllib.request.urlopen(req) as res:
                body = json.load(res)
        except urllib.error.HTTPError as e:
            sys.exit(f"Resend returned {e.code} for the batch starting at {start}: {e.read().decode()}")
        print(f"Sent {len(body.get('data', []))} of {len(chunk)} (batch starting at {start}).")


if __name__ == "__main__":
    main()
