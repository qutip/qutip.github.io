import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# ----------------- API KEYS -----------------
# Pinecone
PINECONE_API_KEY = "enter_key"
PINECONE_ENV = "us-east-1"
PINECONE_INDEX_NAME  = "qutip-shrody"


# Groq settings
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "enter_key")
GROQ_MODEL_NAME =  "llama-3.1-8b-instant" #"llama-3.3-70b-versatile"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# embedding 
embedder = SentenceTransformer("intfloat/e5-small-v2")

# init pinecone
pc = Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pc.Index(PINECONE_INDEX_NAME)

# init groq
groq_client = Groq(api_key=GROQ_API_KEY)

class ChatRequest(BaseModel):
    message: str

def embed_text(text: str) -> list[float]:
    """
    Returns a normalized embedding for the given text.
    """
    embedding = embedder.encode(text, normalize_embeddings=True)
    return embedding.tolist()

def retrieve_relevant_docs(query_vector: list[float], top_k: int = 5) -> list[str]:
    """
    Performs a Pinecone vector search. Returns a list of chunk_text strings
    (as stored under metadata["chunk_text"]) for the top_k matches.
    """
    response = index.query(
        namespace="__default__",
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    docs = []
    for match in response.get("matches", []):
        metadata = match.get("metadata", {})
        if "chunk_text" in metadata:
            docs.append(metadata["chunk_text"])
    return docs

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    user_question = request.message.strip()
    if not user_question:
        raise HTTPException(status_code=400, detail="Empty message")

    try:
        q_vec = embed_text(user_question)
        raw_response = index.query(
            namespace="__default__",
            vector=q_vec,
            top_k=5,
            include_metadata=True
        )
        docs = []
        for match in raw_response.get("matches", []):
            if match.get("score", 0) > 0.5: # can be tuned further
                metadata = match.get("metadata", {})
                if "chunk_text" in metadata:
                    docs.append(metadata["chunk_text"])

        # 4) Combine all chunks into a single “context” block
        context = "\n".join(docs) if docs else ""

        print("Filtered Context:\n", context)

        # 5) Build messages: context goes in system message only
        system_message = {
            "role": "system",
            "content": (
                "You are Shrody, an expert assistant for QuTiP's (its an open-source python library for simulating the dynamics of open quantum systems) documentation. "
                "Be friendly, clear, and use bit of emoji. Use only the following context to answer the user's question:\n\n"
                f"{context}\n\n"
                "Always be concise and accurate. If the context does not contain the answer, kindly say so.  Don't guess or invent information."
            )
        }

        user_message = {
            "role": "user",
            "content": user_question
        }

        # 6) Call Groq’s chat endpoint
        chat_completion = groq_client.chat.completions.create(
            messages=[system_message, user_message],
            model=GROQ_MODEL_NAME,
        )

        generated_answer = chat_completion.choices[0].message.content
        return {"response": generated_answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Make sure the module name matches your filename (e.g. if this file is infer_api.py):
    uvicorn.run("infer_api:app", port=5001, reload=True)
