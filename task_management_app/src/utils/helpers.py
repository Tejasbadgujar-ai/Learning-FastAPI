from fastapi import Request, HTTPException, status, Depends
from src.utils.settings import settings
from sqlalchemy.orm import Session
from jwt.exceptions import InvalidTokenError
from src.user.models import UserModel
from src.utils.db import get_db
import jwt


def is_authenticated(request: Request, db: Session = Depends):
    try:
        auth = request.headers.get("authorization")

        if not auth or not auth.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Not authenticated")

        token = auth.removeprefix("Bearer ")

        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        user_id = data.get("id")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(status_code=401, detail="Not authenticated")

        return user

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Not authenticated")
