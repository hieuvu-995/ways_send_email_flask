from typing import List, Dict, Union
from requests import Response, post
import requests

# from flask import url_for


from app import db

JsonUser = Dict[str, Union[str, str]]


Mailgun_domain = ""
Mailgun_Api_Key = ""
From_Tittle = "Stores Rest API"
From_Email = ""


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    role = db.Column(db.String(50), default="user")
    is_active = db.Column(db.Boolean(), default=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def send_confirmation(self) -> Response:
        # link = request.url_root[:-1] + url_for("userconfirm", user_id=self.id)
        return requests.post(
            "https://api.mailgun.net/v3/domain/messages",
            auth=("api", apiKey),
            data={
                "from": "Excited User <mailgun@domain>",
                "to": [recipient_email],
                "subject": "Hello",
                "text": "Testing some Mailgun awesomness!",
            },
        )

    @classmethod
    def find_by_name(cls, username) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email) -> "UserModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id) -> List["UserModel"]:
        return cls.query.filter_by(id=_id).first()
