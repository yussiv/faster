"""Server setup"""

from fastapi import FastAPI, APIRouter

from .api import root_controller, user_controller

app = FastAPI()
api_router = APIRouter(prefix="/api")

api_router.include_router(user_controller.router)
app.include_router(root_controller.router)
app.include_router(api_router)
