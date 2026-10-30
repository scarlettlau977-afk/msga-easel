"""Dify knowledge-base retrieval for optional RAG context."""
from __future__ import annotations

import httpx


async def retrieve_context(settings: dict[str, str], query: str) -> str:
    base = settings.get("DIFY_API_BASE_URL", "https://api.dify.ai/v1").strip().rstrip("/")
    key = settings.get("DIFY_API_KEY", "").strip()
    dataset = settings.get("DIFY_DATASET_ID", "").strip()
    if not key or not dataset or not query.strip():
        return ""
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.post(
                f"{base}/datasets/{dataset}/retrieve",
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                json={"query": query[:8000], "retrieval_model": {"search_method": "semantic_search", "top_k": 5, "reranking_enable": False, "score_threshold_enabled": False}},
            )
            response.raise_for_status()
            records = response.json().get("records", [])
    except Exception:
        return ""
    chunks = []
    for row in records:
        text = ((row.get("segment") or {}).get("content") or "").strip()
        if text:
            chunks.append(text[:5000])
    return "\n\n".join(chunks)
