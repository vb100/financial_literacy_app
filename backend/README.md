# Career Compass Backend

This directory contains the FastAPI backend responsible for fetching, summarizing, and serving daily career-planning news.

## Development Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and set the required environment variables.
4. Initialize the database (will auto-create tables on first run).
5. Start the API server:
   ```bash
   uvicorn app.main:app --reload
   ```
