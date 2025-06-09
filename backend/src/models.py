from pydantic import BaseModel, Field


class User(BaseModel):
    id: str | None = None
    username: str
    password: str = Field(exclude=True)
    email: str | None = None


class UserAPIUpdate(BaseModel):
    email: str
