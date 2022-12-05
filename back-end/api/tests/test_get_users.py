from fastapi.testclient import TestClient

from app import app, prefix

client = TestClient(app)


def test_get_users():
    response = client.get(f"{prefix}/users")
    assert response.status_code == 200
    res = response.json()
    assert all("id" in _ for _ in res)
    assert all("username" in _ for _ in res)
