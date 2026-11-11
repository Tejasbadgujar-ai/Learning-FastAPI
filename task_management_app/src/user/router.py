from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.user import controller
from src.user.dtos import LoginSchema, UserResponseSchema, UserSchema
from src.utils.db import get_db

user_routes = APIRouter(prefix="/user")


@user_routes.post("/register", response_model=UserResponseSchema, status_code=201)
def register(body: UserSchema, db: Session = Depends(get_db)):
    return controller.register(body, db)


@user_routes.post("/login", status_code=200)
def login(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login_user(body, db)
