from .schemas import UserResponse
from ..services.models import User


def user_to_user_response(user: User) -> UserResponse:
    """User -> UserResponse mapper"""
    return UserResponse(id=user.id, username=user.username, email=user.email)
