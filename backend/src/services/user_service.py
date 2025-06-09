"""Service for finding and manipulating users"""

from typing import Annotated
from fastapi import Depends

from ..db.users import UsersDependency
from ..models import User


class UserService:
    def __init__(self, db: UsersDependency):
        self.db = db

    def get_user(self, user_id: str) -> User | None:
        """Get single user"""
        return self.db.get(user_id)

    def get_users(self) -> list[User]:
        """Get all users"""
        return self.db.get_all()

    def create_user(self, user: User) -> User:
        """Create new user"""
        return self.db.create(
            username=user.username, password=user.password, email=user.email
        )

    def update_user_email(self, user_id: str, email: str) -> User | None:
        """Update user fields, apart from id, username and password"""
        return self.db.update(user_id=user_id, email=email)

    def delete_user(self, user_id: str):
        """Delete user by id"""
        return self.db.delete(user_id=user_id)


UserServiceDependency = Annotated[UserService, Depends()]
