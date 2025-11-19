"""FastAPI application entrypoint."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .config import get_settings
from .db import init_db
from .routes import admin, feed

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Application lifespan hook to ensure tables exist before serving traffic."""

    init_db()
    yield


app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)

app.include_router(feed.router, prefix="/feed", tags=["feed"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])


@app.get("/health")
async def health() -> dict[str, str]:
    """Simple healthcheck endpoint."""

    return {"status": "ok", "app": settings.app_name, "environment": settings.environment}
