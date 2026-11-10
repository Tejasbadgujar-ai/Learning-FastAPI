from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user.dtos import UserSchema, UserResponseSchema, LoginSchema
from src.user import controller

user_routes = APIRouter(prefix="/user")


@user_routes.post("/register", response_model=UserResponseSchema, status_code=201)
def register(body: UserSchema, db: Session = Depends(get_db)):
    return controller.register(body, db)

@user_routes.post("/login", status_code=200)
def login(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login_user(body, db)
