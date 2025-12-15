import os
from typing import List, Optional, Sequence

from fastembed import TextEmbedding
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

try:
    EMBED_MODEL = TextEmbedding()
except Exception:  # noqa: BLE001
    EMBED_MODEL = None
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "docs")


def get_client() -> QdrantClient:
    # Read env at call-time so downstream scripts can load .env before import
    url = os.getenv("QDRANT_URL")
    api_key = os.getenv("QDRANT_API_KEY")
    if url:
        return QdrantClient(url=url, api_key=api_key, timeout=60.0)
    return QdrantClient(timeout=60.0)


def ensure_collection(dim: int) -> None:
    client = get_client()
    existing = [c.name for c in client.get_collections().collections]
    if COLLECTION_NAME not in existing:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
        )


def embed_texts(texts: Sequence[str]) -> List[List[float]]:
    if EMBED_MODEL is None:
        return []
    return list(EMBED_MODEL.embed(texts))


def upsert_chunks(chunks: Sequence[str], metadatas: Optional[Sequence[dict]] = None) -> None:
    vectors = embed_texts(chunks)
    if not vectors:
        return
    ensure_collection(len(vectors[0]))
    client = get_client()
    payloads = metadatas or [{} for _ in chunks]
    points = [
        PointStruct(id=idx, vector=vec, payload=payload)
        for idx, (vec, payload) in enumerate(zip(vectors, payloads, strict=False))
    ]
    client.upsert(collection_name=COLLECTION_NAME, points=points)


def search(query: str, limit: int = 5, filter_payload: Optional[dict] = None):
    vectors = embed_texts([query])
    if not vectors:
        return []
    query_vector = vectors[0]
    client = get_client()
    return client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        query_filter=filter_payload,
        limit=limit,
    )
