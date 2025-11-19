"""Pydantic schemas for API responses."""
from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel


class ArticleBase(BaseModel):
    id: int
    title: str
    url: str
    source: Optional[str]
    summary: Optional[str]
    snippet: Optional[str]
    published_at: Optional[datetime]
    rank: int


class FeedResponse(BaseModel):
    feed_date: date
    articles: List[ArticleBase]
