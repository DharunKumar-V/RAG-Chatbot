# 🧠 RAG AI Chatbot for PDFs & Websites

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-orange?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)
![Groq](https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-RetrievalAugmentedGeneration-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

A **Retrieval-Augmented Generation (RAG) powered AI chatbot web application** that allows users to upload **PDF documents or website URLs** and ask questions about their content.

The system retrieves **relevant contextual information using vector search** and generates responses using **Large Language Models via Groq API**.

This project combines:

- Artificial Intelligence
- Vector Databases
- Semantic Search
- LLM Integration
- Full-Stack Web Development

Users can upload knowledge sources and receive:

- Context-aware AI answers
- Semantic search retrieval
- Real-time streaming responses
- Persistent chat history

---

# 🚀 System Workflow

```
Upload PDF / Website URL
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
Store Embeddings in ChromaDB
        ↓
User Question
        ↓
Vector Similarity Search
        ↓
Relevant Context Retrieval
        ↓
Groq LLM Generation
        ↓
Streaming AI Response
```

---

# 📸 Sample Outputs

### Chat Interface
![Chat UI](assets/ui.png)

---

### Upload PDF
![PDF Upload](assets/pdf.png)

---

### Upload Website
![Website Upload](assets/web.png)

---

### AI Generated Response
![AI Response](assets/response.png)

---

# 🧩 Tech Stack

## 🧠 Artificial Intelligence

![Groq](https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-AI%20Pipeline-green?style=for-the-badge)
![Chroma](https://img.shields.io/badge/ChromaDB-VectorDB-orange?style=for-the-badge)

Core AI components:

- Retrieval Augmented Generation (**RAG**)
- **Groq LLM API**
- **Vector Embeddings**
- **ChromaDB Vector Database**
- **Semantic Similarity Search**

---

## ⚙ Backend

![Python](https://img.shields.io/badge/Python-Backend-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?style=for-the-badge&logo=flask)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange?style=for-the-badge)

Backend built using:

- Python
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- REST API Architecture

---

## 🎨 Frontend

![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Styling-blue?style=for-the-badge&logo=tailwind-css)
![Axios](https://img.shields.io/badge/Axios-API-purple?style=for-the-badge)

Frontend features:

- Modern chat interface
- PDF upload system
- Website knowledge ingestion
- Real-time streaming responses
- Responsive UI design

---

## 🗄 Database

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)

Database stores:

- Users
- Chat sessions
- Chat messages
- Authentication data

---

# 🧠 RAG Architecture

```
User Question
      ↓
Query Embedding
      ↓
Vector Similarity Search
      ↓
Relevant Context Retrieval
      ↓
Prompt Construction
      ↓
Groq LLM API
      ↓
AI Generated Response
```

---

# 🖥 Web Application Features

Users can:

- Upload **PDF documents**
- Add **website URLs as knowledge sources**
- Ask questions about uploaded data
- Receive **context-aware AI responses**
- View **chat history**
- Manage **multiple chat sessions**
- Experience **real-time streaming AI responses**

---

# ⚡ Installation

Clone the repository

```bash
git clone https://github.com/DharunKumar-V/RAG-Chatbot.git
cd RAG-Chatbot
```

---

# Backend Setup

```bash
cd backend

python -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```
GROQ_API_KEY=your_api_key
DATABASE_URL=postgresql://user:password@localhost/db
JWT_SECRET_KEY=secret
CHROMA_PATH=./chroma_db
```

Run backend

```bash
python app.py
```

Backend runs at

```
http://127.0.0.1:5000
```

---

# Frontend Setup

```bash
cd frontend

npm install
npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# 📁 Project Structure

```
rag-chatbot
│
├── backend
│   ├── app.py
│   ├── db.py
│   │
│   ├── models
│   │   ├── chat.py
│   │   └── message.py
│   │
│   ├── routes
│   │   ├── auth_routes.py
│   │   ├── chat_routes.py
│   │   └── upload_routes.py
│   │
│   └── services
│       ├── chroma_service.py
│       ├── llm_service.py
│       ├── pdf_service.py
│       └── web_service.py
│
├── frontend
│   ├── src
│   │   ├── pages
│   │   │   └── Chat.jsx
│   │   ├── components
│   │   └── api.js
│
├── assets
│   ├── chat-ui.png
│   ├── pdf-upload.png
│   ├── url-upload.png
│   └── ai-response.png
│
└── README.md
```

---

# 🔮 Future Improvements

- Multi-document knowledge base
- Document preview support
- Mobile optimized UI
- Docker container deployment
- Cloud deployment
- Knowledge graph integration

---

# 👨‍💻 Author

**Dharun Kumar**

---

# ⭐ Support

If you found this project useful, please consider giving it a **star ⭐ on GitHub**.


Computer Science Engineering Student  
AI • Machine Learning • Full-Stack Development

GitHub  
https://github.com/DharunKumar-V
