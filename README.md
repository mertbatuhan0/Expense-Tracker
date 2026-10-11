# Expense Tracker API

REST API for personal expense tracking. Users register, authenticate with JWT, and manage their own expense records.

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.139-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

**Live docs (when running locally):** [Swagger UI](http://localhost:8000/docs) · [ReDoc](http://localhost:8000/redoc)

---

## Overview

Each authenticated user can create, list, update, and delete expenses. Records are scoped to the owner; listing supports title search, amount range, and pagination.

```mermaid
flowchart LR
  Client -->|JSON + JWT| API[FastAPI]
  API --> Auth
  API --> Expenses
  Auth --> DB[(PostgreSQL)]
  Expenses --> DB
```

## Features

- Sign up and login with bcrypt-hashed passwords
- JWT access tokens (Bearer) with a 10-minute expiry
- Expense CRUD isolated per user
- Query filters: `title`, `min_value`, `max_value`, `skip`, `limit`
- PostgreSQL 16, SQLAlchemy, Alembic
- Docker Compose for a one-command local stack
- pytest coverage for auth and expense flows

## Tech stack

| Layer | Tools |
| --- | --- |
| API | FastAPI, Uvicorn |
| Database | PostgreSQL 16, SQLAlchemy 2 |
| Auth | JWT (`python-jose`), HTTP Bearer, bcrypt |
| Migrations | Alembic |
| Tests | pytest, FastAPI TestClient |
| Runtime | Docker, Docker Compose |

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (recommended), or Python 3.14+ and PostgreSQL 16
- Git

## Getting started

### Docker (recommended)

```bash
git clone https://github.com/mertbatuhan0/Expense-Tracker.git
cd Expense-Tracker
docker compose up --build
```

| Service | Address |
| --- | --- |
| API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| PostgreSQL | `localhost:5433` |

Default database credentials in Compose: user `postgres`, password `postgres`, database `expense_tracker`.

### Local Python

1. Start PostgreSQL (or use only the `db` service from Compose).
2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Set environment variables (see below), then run:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Environment variables

| Variable | Purpose | Default |
| --- | --- | --- |
| `DATABASE_URL` | SQLAlchemy connection string | `postgresql://postgres@localhost:5433/expense_tracker` |
| `SECRET_KEY` | JWT signing key | development fallback in code — set this in any real environment |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `TEST_DATABASE_URL` | Database used by pytest | required for tests |

Create a `.env` file in the project root (gitignored). Do not commit secrets.

## Example flow

**1. Sign up**

```bash
curl -X POST http://localhost:8000/auth/Signup \
  -H "Content-Type: application/json" \
  -d '{"mail": "you@example.com", "username": "batuhan", "password": "secret123"}'
```

**2. Log in** and copy `access_token`:

```bash
curl -X POST http://localhost:8000/auth/Login \
  -H "Content-Type: application/json" \
  -d '{"mail": "you@example.com", "password": "secret123"}'
```

**3. Create an expense**

```bash
curl -X POST http://localhost:8000/expenses/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Groceries", "amount": 42}'
```

```mermaid
sequenceDiagram
  participant Client
  participant Auth as /auth
  participant Expenses as /expenses
  Client->>Auth: POST /Signup
  Client->>Auth: POST /Login
  Auth-->>Client: access_token
  Client->>Expenses: Authorization Bearer token
  Expenses-->>Client: expense JSON
```

## API

Interactive documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

### Auth

| Method | Path | Auth | Description |
| --- | --- | --- | --- |
| `POST` | `/auth/Signup` | No | Create an account (`username`, `mail`, `password`) |
| `POST` | `/auth/Login` | No | Return `{ "access_token", "token_type": "bearer" }` |

### Expenses

All expense endpoints require `Authorization: Bearer <token>`.

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/expenses/` | List expenses (`skip`, `limit`, `title`, `min_value`, `max_value`) |
| `GET` | `/expenses/{id}` | Get one expense |
| `POST` | `/expenses/` | Create (`title`, `amount`) |
| `PUT` | `/expenses/{id}` | Update (`title`, `amount`) |
| `DELETE` | `/expenses/{id}` | Delete |

Expense body:

```json
{
  "title": "Groceries",
  "amount": 42
}
```

### Users

`/users` exposes user CRUD. Prefer `/auth/Signup` for registration.

## Tests

Tests use a separate database via `TEST_DATABASE_URL`.

```bash
export TEST_DATABASE_URL=postgresql://postgres:postgres@localhost:5433/expense_tracker_test
pytest
```

Fixtures live in `app/tests/conftest.py`. Suites:

- `app/tests/test_auth.py` — signup and login
- `app/tests/test_expenses.py` — expense CRUD and unauthorized access

## Project structure

```text
app/
  api/endpoints/    # auth, users, expenses routers
  core/security/    # JWT and password hashing
  crud/             # database operations
  db/               # engine and session
  models/           # SQLAlchemy models
  schemas/          # Pydantic schemas
  tests/            # pytest suite
alembic/            # migrations
docker-compose.yml
Dockerfile
requirements.txt
```

## License

Personal / learning project. See the [repository](https://github.com/mertbatuhan0/Expense-Tracker) for source.

