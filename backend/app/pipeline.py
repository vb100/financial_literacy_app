"""Daily feed pipeline placeholder."""
from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Iterable, List

from .models import Article

KEYWORDS = {
    "career",
    "careers",
    "job",
    "jobs",
    "planning",
    "development",
    "skills",
    "resume",
    "interview",
    "workforce",
}


def _relevance_score(text: str) -> int:
    lowered = text.lower()
    return sum(1 for keyword in KEYWORDS if keyword in lowered)


def select_top_articles(results: Iterable[dict], limit: int = 5) -> List[dict]:
    """Select the top articles based on recency and relevance."""
    cutoff = datetime.utcnow() - timedelta(hours=48)
    scored: List[tuple[float, dict]] = []
    seen_urls: set[str] = set()

    for item in results:
        url = item.get("link")
        title = item.get("title") or ""
        snippet = item.get("snippet") or ""
        if not url or url in seen_urls:
            continue
        published_at = item.get("published_at")
        if isinstance(published_at, datetime) and published_at < cutoff:
            continue
        relevance = _relevance_score(f"{title} {snippet}")
        recency_bonus = 0.0
        if isinstance(published_at, datetime):
            recency_bonus = max(0.0, (published_at - cutoff).total_seconds())
        score = relevance * 1000 + recency_bonus
        scored.append((score, item))
        seen_urls.add(url)

    scored.sort(key=lambda entry: entry[0], reverse=True)
    return [item for _, item in scored[:limit]]


async def update_daily_feed(target_date: date | None = None) -> List[Article]:
    """Placeholder for pipeline implementation."""
    raise NotImplementedError("Pipeline logic will be implemented in future steps")
