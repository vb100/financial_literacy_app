"""Serper.dev client stub."""
from typing import Any, Dict, List

import httpx

from .config import get_settings

settings = get_settings()
SERPER_ENDPOINT = "https://google.serper.dev/news"


async def fetch_news_from_serper(query: str, num: int = 20) -> List[Dict[str, Any]]:
    """Fetch raw news items from Serper."""
    headers = {"X-API-KEY": settings.serper_api_key, "Content-Type": "application/json"}
    payload = {"q": query, "num": num}
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(SERPER_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
    return data.get("news", [])
