import os
import chromadb
from chromadb.config import Settings


# ======================================================
# ✅ ENV BASED PERSISTENCE (BEST PRACTICE)
# ======================================================
# Local  -> ./chroma_db
# Render -> /var/data/chroma

CHROMA_PATH = os.getenv("CHROMA_PATH", "./chroma_db")

print("📦 Chroma DB path:", CHROMA_PATH)

client = chromadb.Client(
    Settings(
        persist_directory=CHROMA_PATH,
        anonymized_telemetry=False
    )
)


# =========================
# Get collection
# =========================
def get_collection(name):
    return client.get_or_create_collection(name)


# =========================
# Add chunks
# =========================
def add_chunks(collection_name, chunks):
    if not chunks:
        return

    col = get_collection(collection_name)

    start = col.count()
    ids = [str(start + i) for i in range(len(chunks))]

    col.add(
        documents=chunks,
        ids=ids
    )

    print("✅ Stored chunks:", len(chunks))
    print("📊 Total now:", col.count())


# =========================
# Search
# =========================
def search(collection_name, query):
    col = get_collection(collection_name)

    if col.count() == 0:
        return []

    results = col.query(
        query_texts=[query],
        n_results=4
    )

    return results["documents"][0] if results["documents"] else []


# =========================
# Delete collection
# =========================
def delete_collection(name):
    try:
        client.delete_collection(name)
        print("🗑 Deleted:", name)
    except:
        pass

