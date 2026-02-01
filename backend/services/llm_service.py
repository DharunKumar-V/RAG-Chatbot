import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# NORMAL (kept for safety)
def ask_llm(context, question):

    prompt = f"""
Answer using ONLY this context:

{context}

Question: {question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content


# ⭐ STREAMING VERSION
def ask_llm_stream(context, question):

    prompt = f"""
Answer using ONLY this context:

{context}

Question: {question}
"""

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
