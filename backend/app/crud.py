"""CRUD helpers for Article entities."""
from datetime import date
from typing import List, Optional
from sqlmodel import select

from .models import Article
from .db import get_session


def get_articles_by_date(target_date: date) -> List[Article]:
    with get_session() as session:
        statement = select(Article).where(Article.feed_date == target_date).order_by(Article.rank.asc())
        return list(session.exec(statement))


def get_latest_feed_date() -> Optional[date]:
    with get_session() as session:
        statement = select(Article.feed_date).order_by(Article.feed_date.desc()).limit(1)
        result = session.exec(statement).first()
        return result
