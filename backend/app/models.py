"""Database models for the career feed."""
from datetime import datetime, date
from typing import Optional
from sqlmodel import Field, SQLModel


class Article(SQLModel, table=True):
    """Represents a summarized article entry."""

    id: Optional[int] = Field(default=None, primary_key=True)
    feed_date: date
    title: str
    url: str
    source: Optional[str] = None
    snippet: Optional[str] = None
    summary: Optional[str] = None
    published_at: Optional[datetime] = None
    rank: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
