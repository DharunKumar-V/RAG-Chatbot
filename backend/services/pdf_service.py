import fitz
import requests
from bs4 import BeautifulSoup


# =========================
# Chunk helper
# =========================
def chunk_text(text, size=250):
    words = text.split()

    if not words:
        return []

    return [
        " ".join(words[i:i + size])
        for i in range(0, len(words), size)
    ]


# =========================
# PDF → chunks
# =========================
def extract_chunks(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()

    return chunk_text(text)


# =========================
# URL → chunks  (FAST + SAFE)
# =========================
def extract_chunks_from_url(url):

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=8)
        res.raise_for_status()
    except:
        return []

    soup = BeautifulSoup(res.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)

    if not text:
        return []

    # 🔥 HARD LIMITS (CRITICAL)
    MAX_CHARS = 50000
    MAX_CHUNKS = 50

    text = text[:MAX_CHARS]

    chunks = chunk_text(text, size=220)

    return chunks[:MAX_CHUNKS]

