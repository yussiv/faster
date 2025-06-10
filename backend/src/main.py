"""Server setup"""

from fastapi import FastAPI, APIRouter

from .api import hello, user_controller

app = FastAPI()
router = APIRouter(prefix="/api")

router.include_router(hello.router)
router.include_router(user_controller.router)
app.include_router(router)
