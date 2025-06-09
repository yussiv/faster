"""User repository"""

from typing import Annotated
from fastapi import Depends

from ..models import User

_data = {
    "1": {
        "id": "1",
        "username": "john",
        "password": "password",
        "email": "john@smith.dev",
    },
    "2": {
        "id": "2",
        "username": "ada",
        "password": "p4ssw0rd",
        "email": "ada@lovelace.dev",
    },
}


class Users:
    def get_all(self) -> list[User]:
        """Get list of User models"""
        return [User(**user) for user in _data.values()]

    def get(self, user_id: str) -> User | None:
        """Get user data"""
        if user_id in _data:
            return User(**_data.get(user_id))
        return None

    def create(self, username: str, password: str, email: str = None) -> User:
        """Add new user to database"""
        user_id = str(len(_data) + 1)
        _data[user_id] = {
            "id": user_id,
            "username": username,
            "email": email,
            "password": password,
        }
        return User(**_data.get(user_id))


UsersDependency = Annotated[Users, Depends()]
