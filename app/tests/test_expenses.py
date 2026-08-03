from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_expense_without_token():
    response = client.post("/expenses/",
    json={"title":"test",
          "amount":100
    })
    assert response.status_code == 401


def test_create_expense_with_token():
    login_response = client.post("/auth/Login/",
     json={"mail":"test@gmail.com",
           "password":"test"})

    token = login_response.json()["access_token"]

    response = client.post("/expenses/",
    json={"title":"test",
         "amount":100},
    headers={"Authorization":f"Bearer {token}"})

    assert response.status_code == 200