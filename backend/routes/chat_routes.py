from flask import Blueprint, request, Response, stream_with_context
from flask_jwt_extended import jwt_required, get_jwt_identity

from db import db
from models.chat import Chat
from models.message import Message
from services.chroma_service import search, delete_collection
from services.llm_service import ask_llm_stream   # ⭐ STREAM ONLY

chat_bp = Blueprint("chat", __name__)


# =====================================================
# Create chat
# =====================================================
@chat_bp.route("/new", methods=["POST"])
@jwt_required()
def new_chat():
    user_id = int(get_jwt_identity())

    chat = Chat(user_id=user_id, title="New Chat")

    db.session.add(chat)
    db.session.commit()

    return {"chat_id": chat.id}


# =====================================================
# List chats
# =====================================================
@chat_bp.route("/list", methods=["GET"])
@jwt_required()
def list_chats():
    user_id = int(get_jwt_identity())

    chats = (
        Chat.query
        .filter_by(user_id=user_id)
        .order_by(Chat.id.desc())
        .all()
    )

    return {
        "chats": [
            {"id": c.id, "title": c.title or "New Chat"}
            for c in chats
        ]
    }


# =====================================================
# ⭐ ASK QUESTION (STREAMING VERSION ONLY)
# =====================================================
@chat_bp.route("/ask", methods=["POST"])
@jwt_required()
def ask():

    user_id = int(get_jwt_identity())
    data = request.json

    question = data["question"]
    chat_id = data["chat_id"]

    chat = Chat.query.filter_by(id=chat_id, user_id=user_id).first()
    if not chat:
        return {"error": "Invalid chat"}, 403

    docs = search(f"chat_{chat_id}", question)

    if not docs:
        return {"answer": "Upload PDF or website first"}

    context = "\n\n".join(docs)

    # ⭐ AUTO TITLE BEFORE STREAMING
    if not chat.title or chat.title == "New Chat":
        chat.title = question.strip()[:35]
        db.session.commit()

    # =====================================================
    # ⭐ STREAM GENERATOR
    # =====================================================
    def generate():
        answer_text = ""

        for token in ask_llm_stream(context, question):
            answer_text += token
            yield token

        # save history after complete
        db.session.add(Message(role="user", content=question, chat_id=chat_id))
        db.session.add(Message(role="assistant", content=answer_text, chat_id=chat_id))
        db.session.commit()

    return Response(
        stream_with_context(generate()),
        mimetype="text/plain"
    )


# =====================================================
# History
# =====================================================
@chat_bp.route("/history/<int:chat_id>", methods=["GET"])
@jwt_required()
def history(chat_id):

    user_id = int(get_jwt_identity())

    chat = Chat.query.filter_by(id=chat_id, user_id=user_id).first()
    if not chat:
        return {"error": "Invalid chat"}, 403

    msgs = (
        Message.query
        .filter_by(chat_id=chat_id)
        .order_by(Message.id)
        .all()
    )

    return {
        "messages": [
            {"role": m.role, "content": m.content}
            for m in msgs
        ]
    }


# =====================================================
# Rename
# =====================================================
@chat_bp.route("/rename/<int:chat_id>", methods=["PUT"])
@jwt_required()
def rename(chat_id):

    user_id = int(get_jwt_identity())
    title = request.json.get("title", "").strip()

    chat = Chat.query.filter_by(id=chat_id, user_id=user_id).first()
    if not chat:
        return {"error": "Invalid chat"}, 403

    if title:
        chat.title = title
        db.session.commit()

    return {"msg": "renamed"}


# =====================================================
# Delete
# =====================================================
@chat_bp.route("/delete/<int:chat_id>", methods=["DELETE"])
@jwt_required()
def delete(chat_id):

    user_id = int(get_jwt_identity())

    chat = Chat.query.filter_by(id=chat_id, user_id=user_id).first()
    if not chat:
        return {"error": "Invalid chat"}, 403

    delete_collection(f"chat_{chat_id}")

    Message.query.filter_by(chat_id=chat_id).delete()
    db.session.delete(chat)
    db.session.commit()

    return {"msg": "deleted"}
