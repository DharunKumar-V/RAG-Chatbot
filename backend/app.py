import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

from db import db

load_dotenv()

app = Flask(__name__)
CORS(app)

# ---------------- CONFIG ----------------
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")

# ---------------- INIT ----------------
db.init_app(app)
jwt = JWTManager(app)

# ---------------- IMPORT MODELS FIRST ----------------
from models.user import User
from models.chat import Chat
from models.message import Message

# ---------------- REGISTER ROUTES ----------------
from routes.auth_routes import auth_bp
from routes.chat_routes import chat_bp
from routes.upload_routes import upload_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(chat_bp, url_prefix="/chat")
app.register_blueprint(upload_bp, url_prefix="/upload")

# ---------------- CREATE TABLES ----------------
with app.app_context():
    db.create_all()

@app.route("/ping")
def ping():
    return {"msg": "pong"}

if __name__ == "__main__":
    app.run(debug=True)

