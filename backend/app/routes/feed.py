"""Feed endpoints placeholder."""
from datetime import date
from fastapi import APIRouter, HTTPException

from .. import crud, schemas

router = APIRouter()


@router.get("/latest", response_model=schemas.FeedResponse)
def get_latest_feed() -> schemas.FeedResponse:
    latest_date = crud.get_latest_feed_date()
    if latest_date is None:
        raise HTTPException(status_code=404, detail="No feeds available yet")
    articles = crud.get_articles_by_date(latest_date)
    return schemas.FeedResponse(feed_date=latest_date, articles=articles)


@router.get("/{feed_date}", response_model=schemas.FeedResponse)
def get_feed_by_date(feed_date: date) -> schemas.FeedResponse:
    articles = crud.get_articles_by_date(feed_date)
    if not articles:
        raise HTTPException(status_code=404, detail="No feed for requested date")
    return schemas.FeedResponse(feed_date=feed_date, articles=articles)
