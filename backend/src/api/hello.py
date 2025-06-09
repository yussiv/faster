"""Greetings router"""

from fastapi.routing import APIRouter

from ..logger import logger

router = APIRouter(prefix="/hello")


@router.get("/")
async def say_hello():
    """Say hello to the world"""
    logger.info("Hello")
    return {"message": "Hello world"}
