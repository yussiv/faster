"""Users router"""

from typing import Annotated
from fastapi import Path, HTTPException
from fastapi.routing import APIRouter

from ..services.user_service import UserServiceDependency
from ..models import User, UserAPIUpdate

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
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", status_code=201)
async def create_user(user: User, user_service: UserServiceDependency):
    """Create user"""
    user = user_service.create_user(user)
    return user


@router.put("/{user_id}")
async def update_user(
    data: UserAPIUpdate,
    user_id: Annotated[str, Path(title="Id of user to update")],
    user_service: UserServiceDependency,
):
    """Update user. Username, password or id can not be changed through this API."""
    user = user_service.update_user_email(user_id=user_id, email=data.email)
    return user


@router.delete("/{user_id}", status_code=204)
async def delete_user(
    user_id: Annotated[str, Path(title="Id of user to delete")],
    user_service: UserServiceDependency,
):
    """Delete user"""
    user_service.delete_user(user_id)
    return
