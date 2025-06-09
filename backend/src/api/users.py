"""Users router"""

from typing import Annotated
from fastapi import Path
from fastapi.routing import APIRouter

from ..services.user_service import UserServiceDependency
from ..models import User

router = APIRouter(prefix="/users")


@router.get("/")
async def get_users(user_service: UserServiceDependency):
    """Get all usernames"""
    users = user_service.get_users()
    return {"users": users}


@router.get("/{user_id}")
async def get_user(
    user_service: UserServiceDependency,
    user_id: Annotated[str, Path(title="Id of user to find")],
):
    """Get user"""
    user = user_service.get_user(user_id)
    return user


@router.post("/", status_code=201)
async def create_user(user: User, user_service: UserServiceDependency):
    """Create user"""
    user = user_service.create_user(username=user.username, password=user.password)
    return user
