from fastapi import HTTPException
from src.user.dtos import UserSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def get_password_hash(password):
    return password_hash.hash(password)


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
