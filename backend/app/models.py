"""Database models for the career feed."""
from datetime import datetime, date
from typing import Optional
from sqlalchemy import UniqueConstraint, Index, func
from sqlmodel import Field, SQLModel


class Article(SQLModel, table=True):
    """Represents a summarized article entry."""

    __table_args__ = (
        UniqueConstraint("feed_date", "url", name="uq_feed_date_url"),
        UniqueConstraint("feed_date", "rank", name="uq_feed_date_rank"),
        Index("idx_feed_date_rank", "feed_date", "rank"),
        Index("idx_feed_date_created", "feed_date", "created_at"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    feed_date: date = Field(index=True, description="Date the article belongs to in the daily feed")
    title: str = Field(description="Article headline")
    url: str = Field(description="Canonical article URL")
    source: Optional[str] = Field(default=None, description="Publisher or site name")
    snippet: Optional[str] = Field(default=None, description="Provider snippet or preview text")
    summary: Optional[str] = Field(default=None, description="LLM-generated 2-3 sentence summary")
    published_at: Optional[datetime] = Field(default=None, description="Original publication timestamp if provided")
    rank: int = Field(default=0, description="Position within the daily feed (1-5)")
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Insertion timestamp (UTC)",
        sa_column_kwargs={"server_default": func.now()},
    )
