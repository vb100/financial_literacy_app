"""Quick smoke test for the Serper news client."""
import asyncio
from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = CURRENT_DIR.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.serper_client import fetch_news_from_serper  # noqa: E402


async def main() -> None:
    items = await fetch_news_from_serper("career planning OR career development", num=3)
    print(f"Got {len(items)} items")
    for item in items:
        print("-", item.get("title"))
        print("  link:", item.get("link"))
        print("  source:", item.get("source"))
        print("  published_at:", item.get("published_at"))


if __name__ == "__main__":
    asyncio.run(main())
