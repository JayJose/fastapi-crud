from fastapi.testclient import TestClient

from app import app, prefix

client = TestClient(app)


def test_home():
    response = client.get(f"{prefix}/")
    assert response.status_code == 200
    assert "welcome to the api" in response.text.lower()
