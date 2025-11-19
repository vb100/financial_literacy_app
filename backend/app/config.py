"""Application configuration models."""
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central application settings pulled from environment variables."""

    app_name: str = Field(default="Career Compass API", description="Human friendly app name")
    app_version: str = Field(default="0.1.0", description="Application version string")
    environment: str = Field(default="local", description="Deployment environment label")

    serper_api_key: str = Field(default="", description="Serper.dev API key")
    openai_api_key: str = Field(default="", description="OpenAI API key")
    database_url: str = Field(
        default="sqlite:///./career_feed.db",
        description="SQLAlchemy-compatible database URL",
    )
    admin_token: str = Field(default="", description="Simple admin auth token")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_prefix="")


@lru_cache()
def get_settings() -> Settings:
    """Return cached settings instance."""

    return Settings()
