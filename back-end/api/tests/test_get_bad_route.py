from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_home():
    response = client.get(f"/")
    assert response.status_code == 404
