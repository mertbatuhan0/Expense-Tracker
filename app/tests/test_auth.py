from starlette.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_signup():
    response = client.post("/auth/Signup",
    json ={
        "username":"test",
        "mail":"test@gmail.com",
        "password":"test",
    })

    assert response.status_code == 200

def test_login():
    response = client.post("/auth/Login",
    json={
        "mail":"test@gmail.com",
        "password":"test",
    })

    assert response.status_code == 200