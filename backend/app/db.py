"""Database engine and session setup."""
from sqlmodel import SQLModel, create_engine, Session

from .config import get_settings

settings = get_settings()
engine = create_engine(settings.database_url, echo=False)


def init_db() -> None:
    """Create database tables."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """Yield a session context manager."""
    return Session(engine)
