import os
import uuid
from collections import defaultdict

import pandas as pd
from unstructured.partition.pdf import partition_pdf
from unstructured.documents.elements import Table
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from tqdm import tqdm

# ----------------- API KEYS -----------------
# Pinecone
PINECONE_API_KEY = "enter-key"
PINECONE_ENV = "us-east-1"
PINECONE_INDEX_NAME  = "qutip-shrody"


# 1. Extract one chunk per PDF page, skip first 10 pages, include tables if present
def extract_chunks_by_page(pdf_path, skip_pages=10):
    elements = partition_pdf(filename=pdf_path)
    pages = defaultdict(list)
    tables = defaultdict(list)

    # Group text & tables by page number
    for el in elements:
        page_no = getattr(el.metadata, "page_number", None)
        if page_no is None or page_no <= skip_pages:
            continue

        if isinstance(el, Table):
            try:
                df = el.to_dataframe()
                md = df.to_markdown(index=False)
                tables[page_no].append(md)
            except Exception:
                tables[page_no].append(el.text.strip())
        elif el.category not in ("PageBreak", "Image"):
            text = el.text.strip()
            if text:
                pages[page_no].append(text)

    # Build one chunk per page
    chunks = []
    for page_no in sorted(set(pages) | set(tables)):
        parts = []
        if pages.get(page_no):
            parts.append("\n\n".join(pages[page_no]))
        if tables.get(page_no):
            for tbl_md in tables[page_no]:
                parts.append("\n\n**Table:**\n\n" + tbl_md)
        joined = "\n\n".join(parts).strip()
        if joined:
            chunks.append({
                "text": joined,
                "page_number": page_no
            })
    return chunks

# 2. Load embedding model
model = SentenceTransformer("intfloat/e5-small-v2")
def get_embedding(text):
    return model.encode([text], normalize_embeddings=True)[0]

# 3. Initialize Pinecone (replace with your key & environment)
pc = Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pc.Index(PINECONE_INDEX_NAME)

# 4. Embed and upsert into Pinecone
def upsert_pdf_by_page(pdf_path, base_doc_id="mydoc"):
    chunks = extract_chunks_by_page(pdf_path, skip_pages=10)
    print(f"🧩 Extracted {len(chunks)} page-level chunks (skipped first 10 pages).")

    vectors = []
    for chunk in tqdm(chunks, desc="Embedding pages"):
        chunk_id = f"{base_doc_id}-page{chunk['page_number']}"
        emb = get_embedding(chunk["text"])
        vectors.append({
            "id": chunk_id,
            "values": emb,
            "metadata": {
                "source": base_doc_id,
                "page_number": chunk["page_number"],
                "chunk_text": chunk["text"]
            }
        })

    # Batch upserts
    batch_size = 50
    for start in range(0, len(vectors), batch_size):
        batch = vectors[start:start+batch_size]
        index.upsert(vectors=batch)
        print(f"✅ Upserted pages {start}–{start + len(batch) - 1}")

if __name__ == "__main__":
    pdf_file = "qutip.pdf"
    doc_id = "qutip-5.1"
    upsert_pdf_by_page(pdf_file, base_doc_id=doc_id)
