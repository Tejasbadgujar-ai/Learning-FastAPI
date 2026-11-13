from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.user import controller
from src.user.dtos import LoginSchema, UserResponseSchema, UserSchema
from src.user.models import UserModel
from src.utils.db import get_db
from src.utils.helpers import is_authenticated

user_routes = APIRouter(prefix="/user")


@user_routes.post("/register", response_model=UserResponseSchema, status_code=201)
def register(body: UserSchema, db: Session = Depends(get_db)):
    return controller.register(body, db)


@user_routes.post("/login", status_code=200)
def login(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login_user(body, db)


@user_routes.get("/is_auth", response_model=UserResponseSchema)
def is_auth(user: UserModel = Depends(is_authenticated)):
    return user
