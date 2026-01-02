"""Serper.dev client utilities."""
from __future__ import annotations

from datetime import datetime
import logging
from typing import Any, Dict, List, Optional

import httpx

from .config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()
SERPER_ENDPOINT = "https://google.serper.dev/news"


def _parse_published_at(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        logger.warning("Unable to parse published date from Serper: %s", value)
        return None


def _normalize_item(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "title": item.get("title", "").strip(),
        "link": item.get("link"),
        "source": item.get("source"),
        "snippet": item.get("snippet"),
        "published_at": _parse_published_at(item.get("date")),
    }


async def fetch_news_from_serper(query: str, num: int = 20) -> List[Dict[str, Any]]:
    """Fetch and normalize news items from Serper."""
    if not settings.serper_api_key:
        logger.error("SERPER_API_KEY is not configured; returning no results.")
        return []
    headers = {"X-API-KEY": settings.serper_api_key, "Content-Type": "application/json"}
    payload = {"q": query, "num": num}
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(SERPER_ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPError:
        logger.exception("Serper request failed for query=%s", query)
        return []
    except ValueError:
        logger.exception("Serper response was not valid JSON.")
        return []
    items = data.get("news", [])
    if not isinstance(items, list):
        logger.warning("Serper response missing 'news' list; got %s", type(items))
        return []
    normalized = [_normalize_item(item) for item in items]
    return [item for item in normalized if item.get("title") and item.get("link")]
