import os
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.database import Base, get_db
from app.main import app

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()



@pytest.fixture
def signup_user(client):
    response = client.post("/auth/Signup",
    json={
        "username":"test",
        "mail": "test@gmail.com",
        "password": "test123"
    })
    return response


@pytest.fixture
def login_without_token(client):
    response = client.post("/auth/Login",
    json={
        "mail:": "test",
        "password": "test123"
        }
   )

    return response


@pytest.fixture
def login_with_token(client, signup_user):
    response = client.post(
        "/auth/Login",
        json={
            "mail": "test@gmail.com",
            "password": "test123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()

    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    return headers

@pytest.fixture
def create_expense(client, login_with_token):
    response = client.post(
        "/expenses",
        headers=login_with_token,
        json={
            "title": "Test Expense",
            "amount": 100.0
        }
    )
    return response


@pytest.fixture
def get_expense(client, login_with_token,create_expense):
    response = client.get(
        "/expenses",
        headers=login_with_token
    )
    return response


@pytest.fixture
def update_expense(client,login_with_token,create_expense):
    expense_id = create_expense.json()["id"]
    response = client.put(f"/expenses/{expense_id}",
        headers=login_with_token,
        json={
            "title": "Updated Expense",
            "amount": 150.0
        }
    )
    return response

@pytest.fixture
def delete_expense(client, login_with_token, create_expense):
    expense_id = create_expense.json()["id"]
    response = client.delete(f"/expenses/{expense_id}",
        headers=login_with_token
    )
    return response

@pytest.fixture
def test_get_expenses_unauthorized(client):
    response = client.get("/expenses")
    return response

@pytest.fixture
def test_get_non_existent_expense(client, login_with_token):
    response = client.get("/expenses/99999", headers=login_with_token)
    return response