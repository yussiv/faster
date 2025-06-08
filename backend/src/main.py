"""Server setup"""

from fastapi import FastAPI, APIRouter

from .api import hello, users

app = FastAPI()
router = APIRouter(prefix="/api")

router.include_router(hello.router)
router.include_router(users.router)
app.include_router(router)
