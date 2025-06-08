"""User service"""

from typing import Annotated
from fastapi import Depends

from ..db.users import UsersDependency
from ..models import User


class UserService:
    """User operations"""

    def __init__(self, db: UsersDependency):
        self.db = db

    def get_user(self, username: str) -> User:
        """get single user"""
        return self.db.get(username)

    def get_users(self) -> list[User]:
        """get all users"""
        return self.db.get_all()

    def create_user(self, username: str, password: str) -> User:
        """create new user"""
        return self.db.create(username, password)


UserServiceDependency = Annotated[UserService, Depends()]
