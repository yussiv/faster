"""Users router"""

from typing import Annotated
from fastapi import Path, HTTPException
from fastapi.routing import APIRouter

from ..services.user_service import UserServiceDependency
from .schemas import (
    UserUpdateRequest,
    UserCreateRequest,
    UserResponse,
    UserListResponse,
)
from .mapping import user_to_user_response

router = APIRouter(prefix="/users")


@router.get("/", response_model=UserListResponse)
async def get_all_users(user_service: UserServiceDependency):
    """Get all users"""
    users = user_service.get_users()
    user_responses = [user_to_user_response(user) for user in users]
    return UserListResponse(users=user_responses)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_service: UserServiceDependency,
    user_id: Annotated[str, Path(title="Id of user to find")],
):
    """Get user"""
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_to_user_response(user)


@router.post("/", status_code=201, response_model=UserResponse)
async def create_user(user: UserCreateRequest, user_service: UserServiceDependency):
    """Create user"""
    user = user_service.create_user(
        username=user.username, password=user.password, email=user.email
    )
    return user_to_user_response(user)


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    data: UserUpdateRequest,
    user_id: Annotated[str, Path(title="Id of user to update")],
    user_service: UserServiceDependency,
):
    """Update user. Username, password or id can not be changed through this API."""
    user = user_service.update_user_email(user_id=user_id, email=data.email)
    return user_to_user_response(user)


@router.delete("/{user_id}", status_code=204)
async def delete_user(
    user_id: Annotated[str, Path(title="Id of user to delete")],
    user_service: UserServiceDependency,
):
    """Delete user"""
    user_service.delete_user(user_id)
    return
