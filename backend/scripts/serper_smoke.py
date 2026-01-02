"""Quick smoke test for the Serper news client."""
import asyncio

from app.serper_client import fetch_news_from_serper


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
