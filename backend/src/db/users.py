"""User repository"""

from typing import Annotated
from fastapi import Depends

from ..models import User

_data = {"john": {"password": "password"}, "ada": {"password": "p4ssw0rd"}}


class Users:
    """User data operations"""

    def get_all(self) -> list[User]:
        """Get list of User models"""
        return [
            User(**item, username=username) for username, item in list(_data.items())
        ]

    def get(self, username: str | None) -> User | None:
        """Get user data"""
        if username in _data:
            user = _data.get(username)
            return User(**user, username=username)
        return None

    def create(self, username: str, password: str) -> User:
        """Add new user to database"""
        _data[username] = {"password": password}
        return User(username=username, password=password)


UsersDependency = Annotated[Users, Depends()]
