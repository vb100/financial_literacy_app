"""Quick smoke test for article selection heuristics."""
from datetime import datetime, timedelta

from app.pipeline import select_top_articles


def main() -> None:
    now = datetime.utcnow()
    sample = [
        {
            "title": "Career planning tips for 2025",
            "link": "https://example.com/career-planning",
            "source": "Example",
            "snippet": "Career development strategies for long-term job growth.",
            "published_at": now - timedelta(hours=4),
        },
        {
            "title": "Sports roundup: local team wins",
            "link": "https://example.com/sports",
            "source": "Example",
            "snippet": "Unrelated sports news.",
            "published_at": now - timedelta(hours=2),
        },
        {
            "title": "Job interview checklist",
            "link": "https://example.com/interview-checklist",
            "source": "Example",
            "snippet": "How to prepare for job interviews and resumes.",
            "published_at": now - timedelta(hours=30),
        },
        {
            "title": "Old career advice",
            "link": "https://example.com/old-career",
            "source": "Example",
            "snippet": "Career development advice from last month.",
            "published_at": now - timedelta(days=5),
        },
    ]
    selected = select_top_articles(sample, limit=3)
    print(f"Selected {len(selected)} items")
    for item in selected:
        print("-", item.get("title"))
        print("  link:", item.get("link"))
        print("  published_at:", item.get("published_at"))


if __name__ == "__main__":
    main()
