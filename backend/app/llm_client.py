"""LLM summarization client stub."""
from typing import Optional

import httpx

from .config import get_settings

settings = get_settings()
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-3.5-turbo"


async def summarize_article(title: str, snippet: str, url: str, full_text: Optional[str] = None) -> str:
    """Call OpenAI chat completions to summarize an article."""
    content = f"Title: {title}\nSnippet: {snippet}\nURL: {url}\n"
    if full_text:
        content += f"Full Text: {full_text}\n"
    prompt = (
        "Summarize the article above in 2-3 sentences focusing on career planning or development takeaways."
    )
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You summarize career development news succinctly."},
            {"role": "user", "content": content + prompt},
        ],
        "temperature": 0.3,
    }
    headers = {
        "Authorization": f"Bearer {settings.openai_api_key}",
        "Content-Type": "application/json",
    }
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(OPENAI_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
    return data["choices"][0]["message"]["content"].strip()
