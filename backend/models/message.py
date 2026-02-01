from db import db
from datetime import datetime

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)

    role = db.Column(db.String(10))
    content = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    chat_id = db.Column(
        db.Integer,
        db.ForeignKey("chats.id"),
        nullable=False
    )


