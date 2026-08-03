# 🎯 Expense Tracker API

A simple and fast RESTful API built with FastAPI, SQLAlchemy, and PostgreSQL to manage personal expenses.

## 🚧 Status: Under Active Development 🚀

**Latest updates:**
- Migrated database from SQLite to PostgreSQL
- Added Alembic for database migrations
- JWT Authentication (login & register) securing `/expenses` endpoints using OAuth2 Bearer tokens
- Linked all expense records directly to the authenticated user ID
- Added pagination (`skip`, `limit`) to the expenses listing endpoint
- Added filtering by amount range (`min_value`, `max_value`) and title search
- Added pytest test coverage for auth and expense endpoints

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL & SQLAlchemy ORM
- **Migrations:** Alembic
- **Auth:** PyJWT & Passlib (bcrypt)
- **Validation:** Pydantic
- **Testing:** pytest & httpx

## 📌 Features

- User registration & login with JWT authentication
- Create, read, update, and delete expenses
- Expenses are scoped to the authenticated user
- Pagination support (`GET /expenses/?skip=0&limit=10`)
- Filtering support:
  - `min_value` / `max_value` — filter by amount range
  - `title` — search by expense title

## 🧪 Running Tests

This project uses `pytest` for automated testing, covering both authentication and expense endpoints (including JWT-protected routes).

```bash
pip install pytest httpx
pytest
```

Test files are located under `app/tests/`:
- `test_auth.py` — registration & login tests
- `test_expenses.py` — expense creation tests (with and without authentication)

## ⚙️ Environment Variables

Create a `.env` file in the project root with:
