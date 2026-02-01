from datetime import datetime
from db import db


class Chat(db.Model):
    __tablename__ = "chats"

    # =========================
    # Primary Key
    # =========================
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # =========================
    # Chat title (auto rename works here)
    # =========================
    title = db.Column(
        db.String(255),
        default="New Chat",
        nullable=False
    )

    # =========================
    # Owner
    # =========================
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # =========================
    # Created time (NEW ⭐)
    # useful for:
    # - sorting chats
    # - showing recent chats
    # - future features
    # =========================
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # =========================
    # Messages relationship
    # =========================
    messages = db.relationship(
        "Message",
        backref="chat",
        cascade="all, delete-orphan",
        lazy=True
    )

    # =========================
    # Debug print (optional nice)
    # =========================
    def __repr__(self):
        return f"<Chat {self.id} - {self.title}>"

