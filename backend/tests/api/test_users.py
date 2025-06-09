from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_users():
    response = client.get("/api/users")

    assert response.status_code == 200

    content = response.json()

    assert "users" in content
    assert len(content.get("users")) == 2


def test_create_user():
    data = {"username": "foo", "password": "bar"}
    response = client.post("/api/users", json=data)

    assert response.status_code == 201

    created_user = response.json()
    assert created_user.get("username") == "foo"

    # check that added to all users
    new_users = client.get("/api/users").json()

    assert len(new_users.get("users")) == 3

    found = next(
        (user for user in new_users.get("users") if user.get("username") == "foo"), None
    )

    assert found is not None

    # check that can be found by id
    new_user = client.get(f"/api/users/{created_user.get('id')}").json()

    assert new_user == created_user


def test_get_user():
    response = client.get("/api/users/2")

    assert response.status_code == 200
    assert response.json() == {
        "username": "ada",
        "id": "2",
        "email": "ada@lovelace.dev",
    }
