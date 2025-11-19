# Career Compass Project Plan

## 10-Day Execution Plan

Day 1: Define project structure, environment setup, and planning artifacts.

Day 2: Implement backend configuration, database models, and FastAPI skeleton with health endpoint.

Day 3: Build Serper client integration and article selection heuristics; add supporting tests or scripts as needed.

Day 4: Implement OpenAI summarization client and integrate summarization flow with proper error handling/logging.

Day 5: Create pipeline logic for `update_daily_feed`, persistence routines, and admin refresh endpoint; validate via manual runs.

Day 6: Implement feed retrieval endpoints (`/feed/latest`, `/feed/{date}`) with pagination-ready schemas and validations.

Day 7: Build CLI/cron script, document scheduling steps, and add environment setup instructions.

Day 8: Scaffold React Native Expo app with navigation, API client, and shared types; ensure configuration via `.env`.

Day 9: Implement Feed and Article Detail screens, loading/error states, and integration with backend API.

Day 10: Perform end-to-end testing, polish UI, add README docs, and prepare deployment guidance for backend and mobile app.

## Proposed Project Structure

```
backend/
  app/
    __init__.py
    main.py
    config.py
    db.py
    models.py
    schemas.py
    crud.py
    serper_client.py
    llm_client.py
    pipeline.py
    routes/
      __init__.py
      feed.py
      admin.py
  scripts/
    update_feed.py
  requirements.txt
  .env.example
  README.md

mobile/
  App.tsx
  app/
    screens/
      FeedScreen.tsx
      ArticleDetailScreen.tsx
    components/
      ArticleCard.tsx
    api/
      client.ts
      feed.ts
    types/
      feed.ts
    hooks/
      useFeed.ts
  package.json
  tsconfig.json
  app.json
  babel.config.js
  .env.example
  README.md
```

This structure keeps backend and frontend concerns separate, ensures clear module boundaries, and supports future growth (tests, CI/CD, etc.).
