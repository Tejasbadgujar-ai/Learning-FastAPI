import jwt
from fastapi import Depends, HTTPException, Request
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

from src.user.models import UserModel
from src.utils.db import get_db
from src.utils.settings import settings


def is_authenticated(request: Request, db: Session = Depends(get_db)):
    try:
        auth = request.headers.get("authorization")

        if not auth or not auth.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Not authenticated")

        token = auth.replace("Bearer ", "", 1)

        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        user = db.query(UserModel).filter(UserModel.id == data.get("id")).first()

        if not user:
            raise HTTPException(status_code=401, detail="Not authenticated")

        return user

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Not authenticated")
