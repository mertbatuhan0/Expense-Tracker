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

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL & SQLAlchemy ORM
- **Migrations:** Alembic
- **Auth:** PyJWT & Passlib
- **Validation:** Pydantic

## 📌 Features

- User registration & login with JWT authentication
- Create, read, update, and delete expenses
- Expenses are scoped to the authenticated user
- Pagination support (`GET /expenses/?skip=0&limit=10`)
- Filtering support:
  - `min_value` / `max_value` — filter by amount range
  - `title` — search by expense title

## 🔜 Coming Soon

- Refresh token support
- pytest test coverage
- Docker support
- CI/CD with GitHub Actions
- AWS deployment
