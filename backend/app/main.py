"""FastAPI application entrypoint."""
from fastapi import FastAPI

from .routes import admin, feed

app = FastAPI(title="Career Compass API")

app.include_router(feed.router, prefix="/feed", tags=["feed"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])


@app.get("/health")
async def health() -> dict[str, str]:
    """Simple healthcheck endpoint."""
    return {"status": "ok"}
