"""CRUD helpers for Article entities."""
from datetime import date
from typing import Iterable, List, Optional
from sqlmodel import select

from .models import Article
from .db import get_session
from .schemas import ArticleCreate


def get_articles_by_date(target_date: date) -> List[Article]:
    with get_session() as session:
        statement = select(Article).where(Article.feed_date == target_date).order_by(Article.rank.asc())
        return list(session.exec(statement))


def get_latest_feed_date() -> Optional[date]:
    with get_session() as session:
        statement = select(Article.feed_date).order_by(Article.feed_date.desc()).limit(1)
        result = session.exec(statement).first()
        return result


def replace_feed_for_date(target_date: date, articles: Iterable[ArticleCreate]) -> List[Article]:
    """Replace all articles for a given date with the provided set.

    Existing rows for the date are deleted to ensure rank uniqueness and to avoid stale data.
    """

    with get_session() as session:
        # Remove any existing articles for that date
        existing_statement = select(Article).where(Article.feed_date == target_date)
        for record in session.exec(existing_statement):
            session.delete(record)

        created: List[Article] = []
        for payload in articles:
            article = Article(**payload.model_dump())
            session.add(article)
            created.append(article)

        session.commit()
        for article in created:
            session.refresh(article)

        return created


def upsert_article(payload: ArticleCreate) -> Article:
    """Insert or update a single article based on feed_date and url.

    Primarily intended for pipeline use; rank is also part of the uniqueness constraint
    to prevent duplicates within the same daily feed.
    """

    with get_session() as session:
        statement = select(Article).where(
            Article.feed_date == payload.feed_date,
            Article.url == payload.url,
        )
        existing = session.exec(statement).first()

        if existing:
            for key, value in payload.model_dump().items():
                setattr(existing, key, value)
            session.add(existing)
            session.commit()
            session.refresh(existing)
            return existing

        article = Article(**payload.model_dump())
        session.add(article)
        session.commit()
        session.refresh(article)
        return article
