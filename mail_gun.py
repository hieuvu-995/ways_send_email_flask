from requests import Response, post
import requests

apiKey = ""
domain = ""
recipient_email = ""


def send_confirmation(self) -> Response:
    # link = request.url_root[:-1] + url_for("userconfirm", user_id=self.id)
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", apiKey),
        data={
            "from": "Excited User <mailgun@domain>",
            "to": [recipient_email],
            "subject": "Hello",
            "text": "Testing some Mailgun awesomness!",
        },
    )
