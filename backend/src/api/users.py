"""Users router"""

from typing import Annotated
from fastapi import Path
from fastapi.routing import APIRouter

from ..services.user_service import UserServiceDependency

router = APIRouter(prefix="/users")


@router.get("/")
async def get_users(user_service: UserServiceDependency):
    """Get all usernames"""
    users = user_service.get_users()
    return {"users": users}


@router.get("/{username}")
async def get_user(
    user_service: UserServiceDependency,
    username: Annotated[str, Path(title="Username of user to find")],
):
    """Get user"""
    user = user_service.get_user(username)
    return user


@router.post("/")
async def create_user(
    username: str, password: str, user_service: UserServiceDependency
):
    """Create user"""
    user = user_service.create_user(username, password)
    return user
