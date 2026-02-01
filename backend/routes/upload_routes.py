from flask import Blueprint, request
from flask_jwt_extended import jwt_required

# ✅ ONLY import from pdf_service now
from services.pdf_service import extract_chunks, extract_chunks_from_url
from services.chroma_service import add_chunks

upload_bp = Blueprint("upload", __name__)


# =========================
# Upload PDF
# =========================
@upload_bp.route("/pdf", methods=["POST"])
@jwt_required()
def upload_pdf():

    file = request.files.get("file")
    chat_id = request.form.get("chat_id")

    if not file:
        return {"error": "No file uploaded"}, 400

    chunks = extract_chunks(file)

    if not chunks:
        return {"error": "No readable text found in PDF"}, 400

    add_chunks(f"chat_{chat_id}", chunks)

    return {
        "msg": "PDF processed",
        "chunks_added": len(chunks)
    }


# =========================
# Upload Website (FAST VERSION)
# =========================
@upload_bp.route("/url", methods=["POST"])
@jwt_required()
def upload_url():

    data = request.json

    url = data.get("url")
    chat_id = data.get("chat_id")

    if not url:
        return {"error": "URL missing"}, 400

    chunks = extract_chunks_from_url(url)

    if not chunks:
        return {"error": "No readable content found"}, 400

    add_chunks(f"chat_{chat_id}", chunks)

    return {
        "msg": "Website processed",
        "chunks_added": len(chunks)
    }
