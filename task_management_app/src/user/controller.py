from fastapi import HTTPException
from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from pwdlib import PasswordHash
from src.utils.settings import settings
from datetime import datetime, timedelta, timezone
import jwt


password_hash = PasswordHash.recommended()


def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def register(body: UserSchema, db: Session):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name=body.name,
        username=body.username,
        hash_password=hash_password,
        email=body.email,
        mobile_num=body.mobile_num,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "name": new_user.name,
        "username": new_user.username,
        "email": new_user.email,
        "mobile_num": new_user.mobile_num,
        "id": new_user.id,
    }


def login_user(body: LoginSchema, db: Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first()

    if not user or not verify_password(body.password, user.hash_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    exp_time = datetime.now(timezone.utc) + timedelta(minutes=settings.EXP_TIME)

    token = jwt.encode(
        {"id": user.id, "exp": exp_time},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return {"token": token}
