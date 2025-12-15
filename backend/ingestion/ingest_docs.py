"""
Doc ingestion: chunk Markdown from book-source/docs, embed with FastEmbed, upsert to Qdrant.
Loads environment from .env (and .env.example as fallback). Exits early if Qdrant config is missing.
Chunking strategy can be adjusted based on Context7 guidance (token-count/overlap).
"""

import os
import pathlib
import re
from typing import List, Tuple

from dotenv import load_dotenv
from backend.retrieval.qdrant_client import upsert_chunks


def load_markdown(root: str) -> List[Tuple[str, str]]:
    """Return list of (relative_path, content) for markdown docs."""
    paths = pathlib.Path(root).rglob("*.md")
    items: List[Tuple[str, str]] = []
    for p in paths:
        rel = pathlib.Path(root).joinpath(p).resolve().relative_to(pathlib.Path(root).resolve())
        items.append((str(rel), p.read_text(encoding="utf-8", errors="ignore")))
    return items


def chunk_text(text: str, max_words: int = 220, overlap: int = 30) -> List[str]:
    words = re.split(r"\s+", text)
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i : i + max_words]).strip()
        if chunk:
            chunks.append(chunk)
        i += max_words - overlap
    return chunks


def ingest(root: str = "book-source/docs") -> None:
    # Load env from root .env, backend/.env, and example as fallback
    load_dotenv(".env")
    load_dotenv("backend/.env")
    load_dotenv(".env.example")
    load_dotenv("backend/.env.example")
    qdrant_url = os.getenv("QDRANT_URL")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")
    if not qdrant_url:
        raise SystemExit("QDRANT_URL is not set; cannot ingest.")
    if not qdrant_api_key:
        print("Warning: QDRANT_API_KEY not set; ensure your Qdrant instance allows access.")

    docs = load_markdown(root)
    all_chunks = []
    payloads = []
    root_path = pathlib.Path(root).resolve()
    for rel_path, doc in docs:
        chunks = chunk_text(doc)
        page_url = "/" + pathlib.Path(rel_path).with_suffix("").as_posix()
        for chunk in chunks:
            all_chunks.append(chunk)
            payloads.append({"ref": rel_path, "text": chunk, "page_url": page_url})
    upsert_chunks(all_chunks, metadatas=payloads)


if __name__ == "__main__":
    ingest()
