"""Admin endpoints placeholder."""
from fastapi import APIRouter, Depends, Header, HTTPException, status

from ..config import get_settings
from ..pipeline import update_daily_feed

router = APIRouter()


def verify_admin_token(x_admin_token: str = Header("")) -> None:
    settings = get_settings()
    if not settings.admin_token or x_admin_token != settings.admin_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid admin token")


@router.post("/refresh", dependencies=[Depends(verify_admin_token)])
async def refresh_feed() -> dict[str, str]:
    await update_daily_feed()
    return {"status": "refresh triggered"}
