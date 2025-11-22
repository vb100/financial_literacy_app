# Alembic migrations

This directory houses database migration scripts. To generate or apply migrations, run commands from the `backend/` directory:

```bash
alembic revision --autogenerate -m "description"
alembic upgrade head
```
