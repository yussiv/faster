from pydantic import BaseModel


class UserUpdateRequest(BaseModel):
    email: str


class UserCreateRequest(BaseModel):
    username: str
    password: str
    email: str | None = None


class UserResponse(BaseModel):
    id: str
    username: str
    email: str | None = None


class UserListResponse(BaseModel):
    users: list[UserResponse]
