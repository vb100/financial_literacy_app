"""Pydantic schemas for API responses."""
from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class ArticleBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    feed_date: date
    title: str
    url: str
    source: Optional[str]
    summary: Optional[str]
    snippet: Optional[str]
    published_at: Optional[datetime]
    rank: int
    created_at: datetime


class FeedResponse(BaseModel):
    feed_date: date
    articles: List[ArticleBase]


class ArticleCreate(BaseModel):
    feed_date: date
    title: str
    url: str
    source: Optional[str] = None
    snippet: Optional[str] = None
    summary: Optional[str] = None
    published_at: Optional[datetime] = None
    rank: int
