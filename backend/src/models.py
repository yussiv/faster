"""Model classes"""

from pydantic import BaseModel, Field


class User(BaseModel):
    """User Model"""

    username: str
    password: str = Field(exclude=True)
