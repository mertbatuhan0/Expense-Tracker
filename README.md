# 💸 Expense Tracker API

A lightweight, modern, and production-ready RESTful API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Docker**. This project handles user authentication via **JWT** and provides full CRUD functionality for tracking daily personal expenses.

---

## ✨ Features

* **Authentication & Authorization:** Secure user registration and login using JWT tokens and password hashing (Passlib/Bcrypt).
* **Expense Management:** Create, read, update, and delete expenses tied to authenticated users.
* **Database ORM:** Structured data handling using **SQLAlchemy** with **PostgreSQL**.
* **Containerized Deployment:** Fully Dockerized setup using `Dockerfile` and `docker-compose` for easy spin-up.
* **Interactive API Docs:** Built-in Swagger UI and ReDoc interface powered by FastAPI.

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI (Python 3.11+)
* **Database:** PostgreSQL
* **ORM & Migrations:** SQLAlchemy
* **Authentication:** PyJWT / OAuth2 Password Bearer
* **Containerization:** Docker & Docker Compose

---

## 🧪 Testing (pytest)

This project uses `pytest` with shared fixtures defined in `conftest.py` to avoid repeating setup code across test files.

### Structure

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your machine:
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [Git](https://git-scm.com/)

---


