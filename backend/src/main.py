"""Server setup"""

from fastapi import FastAPI, APIRouter

from .api import hello

app = FastAPI()
router = APIRouter(prefix="/api")

router.include_router(hello.router)
app.include_router(router)
