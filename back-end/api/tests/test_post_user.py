from fastapi.testclient import TestClient

from app import app, prefix

client = TestClient(app)

new_user = {"username": "jayjose", "password": "swordfish"}


def test_get_users():
    response = client.post(
        f"{prefix}/users",
        json=new_user,
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == new_user["username"]
