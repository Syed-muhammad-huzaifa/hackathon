from typing import Any, Dict, List, Optional

from backend.retrieval.qdrant_client import search


def build_filter(page_url: Optional[str]) -> Optional[Dict[str, Any]]:
    if not page_url:
        return None
    return {"must": [{"key": "page_url", "match": {"value": page_url}}]}


def retrieve(
    query: str,
    selection: Optional[str] = None,
    page_url: Optional[str] = None,
    limit: int = 5,
    
    include_selection_only: bool = False,
) -> List[Dict[str, Any]]:
    """
    Selection-first, then page, then global.
    """
    results: List[Dict[str, Any]] = []
    try:
        if selection:
            hits = search(selection, limit=limit, filter_payload=build_filter(page_url))
            results.extend(_format_hits(hits))
            if include_selection_only and results:
                return results
        if not results and page_url:
            hits = search(query, limit=limit, filter_payload=build_filter(page_url))
            results.extend(_format_hits(hits))
        if not results:
            hits = search(query, limit=limit)
            results.extend(_format_hits(hits))
    except Exception:
        # In dev/offline environments, proceed without retrieved context.
        return []
    return results


def _format_hits(hits) -> List[Dict[str, Any]]:
    formatted = []
    for hit in hits:
        formatted.append(
            {
                "id": getattr(hit, "id", None),
                "score": getattr(hit, "score", None),
                "payload": getattr(hit, "payload", {}),
            }
        )
    return formatted
