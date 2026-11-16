from fastapi import APIRouter, Depends, Request, BackgroundTasks
from sqlalchemy.orm import Session

from src.user import controller
from src.user.dtos import LoginSchema, UserResponseSchema, UserSchema
from src.user.models import UserModel
from src.utils.db import get_db
from src.utils.helpers import is_authenticated

user_routes = APIRouter(prefix="/user")


@user_routes.post("/register", response_model=UserResponseSchema, status_code=201)
async def register(
    body: UserSchema, bg_task: BackgroundTasks, db: Session = Depends(get_db)
):
    return await controller.register(body, db, bg_task)


@user_routes.post("/login", status_code=200)
def login(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login_user(body, db)


@user_routes.get("/is_auth", response_model=UserResponseSchema)
def is_auth(user: UserModel = Depends(is_authenticated)):
    return user
