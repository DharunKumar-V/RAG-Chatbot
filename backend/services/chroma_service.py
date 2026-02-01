import chromadb


# ======================================================
# ✅ TRUE DISK PERSISTENCE (NEW CHROMA WAY)
# ======================================================
client = chromadb.PersistentClient(
    path="./chroma_db"   # ⭐ automatically saves here
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

    print("Stored chunks:", len(chunks))
    print("Total now:", col.count())


# =========================
# Search
# =========================
def search(collection_name, query):
    col = get_collection(collection_name)

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
        print("Deleted:", name)
    except:
        pass


