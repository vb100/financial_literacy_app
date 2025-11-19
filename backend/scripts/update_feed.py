"""Manual script to run the daily feed pipeline."""
import asyncio
from datetime import date

from app.pipeline import update_daily_feed


def main() -> None:
    asyncio.run(update_daily_feed(date.today()))


if __name__ == "__main__":
    main()
