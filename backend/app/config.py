"""Application configuration models."""
from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Central application settings."""

    serper_api_key: str = Field("", env="SERPER_API_KEY")
    openai_api_key: str = Field("", env="OPENAI_API_KEY")
    database_url: str = Field("sqlite:///./career_feed.db", env="DATABASE_URL")
    admin_token: str = Field("", env="ADMIN_TOKEN")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()
