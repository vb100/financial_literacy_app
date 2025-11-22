# Career Compass Backend

This directory contains the FastAPI backend responsible for fetching, summarizing, and serving daily career-planning news.

## Development Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and set the required environment variables (API keys, database URL, admin token, and optional `ENVIRONMENT`).
4. Start the API server (tables will be auto-created during startup):
   ```bash
   uvicorn app.main:app --reload
   ```

## Database migrations

Alembic is configured for managing schema changes. From the `backend/` directory:

```bash
# create a new migration after editing models
alembic revision --autogenerate -m "describe change"

# apply migrations to the configured DATABASE_URL
alembic upgrade head
```

The initial migration (`0001_create_articles`) is already included; running `alembic upgrade head` will create the tables if they do not exist.

## Troubleshooting

- **`ModuleNotFoundError: No module named 'sqlmodel'`** – this means your current
  environment was set up before the latest dependencies were added. Re-run
  `pip install -r requirements.txt` (or simply `pip install sqlmodel`) inside
  your virtual environment to pull in the missing package, then restart the
  server.
