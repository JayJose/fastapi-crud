from fastapi.testclient import TestClient
from unittest.mock import Mock

from routers.users import add_user
from schemas.users import UserInput, UserOutput
from app import app, prefix

client = TestClient(app)


def test_post_user():
    new_user = {"username": "jayjose", "password": "swordfish"}

    response = client.post(
        f"{prefix}/users",
        json=new_user,
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == new_user["username"]


# TODO: fix this test
# def test_add_user_with_mock_session():
#     new_user = {"username": "harry", "password": "thedog"}
#     mock_session = Mock()
#     input = UserInput(username=new_user["username"], password=new_user["password"])
#     result = add_user(user_input=input, session=mock_session)
#     mock_session.add.assert_called_once()
#     mock_session.commit.assert_called_once()
#     mock_session.refresh.assert_called_once()
#     assert isinstance(result, UserOutput)
#     assert result.username == new_user["username"]
