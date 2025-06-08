"""Greetings router"""

from fastapi.routing import APIRouter

router = APIRouter(prefix="/hello")


@router.get("/")
async def say_hello():
    """Say hello to the world"""
    return {"message": "Hello world"}
