from fastapi.testclient import TestClient

from src.main import app
from src.models import User

client = TestClient(app)


def _create_user(user_data: dict) -> User:
    create_response = client.post(
        "/api/users",
        json=user_data,
    )
    assert create_response.status_code == 201

    created_user = create_response.json()
    user_id = created_user.get("id")

    found_user = client.get(f"/api/users/{user_id}").json()

    assert found_user is not None
    assert found_user.get("id") == user_id

    return User(
        **found_user,
        password="secret",  # FIXME: separate model for API response with optional password
    )


def test_get_users():
    response = client.get("/api/users")

    assert response.status_code == 200

    content = response.json()

    assert "users" in content
    assert len(content.get("users")) == 2  # TODO: reset users between tests


def test_create_user():
    data = {"username": "foo", "password": "bar"}
    new_user = _create_user(data)
    assert new_user.username == "foo"


def test_get_user():
    response = client.get("/api/users/2")

    assert response.status_code == 200
    assert response.json() == {
        "username": "ada",
        "id": "2",
        "email": "ada@lovelace.dev",
    }


def test_get_non_existent_user():
    response = client.get("/api/users/666")

    assert response.status_code == 404


def test_update_user():
    test_user = _create_user(
        {
            "username": "to_update",
            "password": "secret",
            "email": "to_update@test.local",
        }
    )

    update_response = client.put(
        f"/api/users/{test_user.id}", json={"email": "updated.email@test.local"}
    )

    assert update_response.status_code == 200

    updated_user = client.get(f"/api/users/{test_user.id}").json()

    assert updated_user.get("email") == "updated.email@test.local"


def test_delete_user():
    new_user = _create_user(
        {
            "username": "to_delete",
            "password": "secret",
            "email": "to_delete@test.local",
        }
    )

    response = client.delete(f"/api/users/{new_user.id}")

    assert response.status_code == 204

    not_found_response = client.get(f"/api/users/{new_user.id}")

    assert not_found_response.status_code == 404
