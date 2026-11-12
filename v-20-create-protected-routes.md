# Video 20 – Create Protected Routes: Secure Endpoints with Authentication in FastAPI

## 1. What I Learned

In this video, I learned how to protect API routes using authentication.

Earlier, users could directly create, view, update, and delete tasks without authentication. Now, users must log in first and get an access token. They must send this token with every protected request.

If the token is missing or invalid, the API returns `401 Not authenticated`.

## 2. Helpers – Authentication Function

I created `is_authenticated` in `src/utils/helpers.py`.

### Code

```python
from fastapi import Request, HTTPException, status, Depends
from src.utils.settings import settings
from sqlalchemy.orm import Session
from jwt.exceptions import InvalidTokenError
from src.user.models import UserModel
from src.utils.db import get_db
import jwt


def is_authenticated(request: Request, db: Session = Depends(get_db)):
    try:
        auth = request.headers.get("authorization")

        if not auth or not auth.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Not authenticated")

        token = auth.replace("Bearer ", "", 1)

        data = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = data.get("id")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(status_code=401, detail="Not authenticated")

        return user

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Not authenticated")
```

### Helpers Function Summary

- `Request` reads the request headers.
- The function gets the `Authorization` header.
- It checks whether the header starts with `Bearer `.
- It extracts the JWT access token.
- `jwt.decode()` validates and decodes the token using the secret key and algorithm.
- It gets the user ID from the token.
- It checks whether the user exists in the database.
- If the token is missing, invalid, or the user does not exist, it returns `401 Not authenticated`.
- If authentication succeeds, it returns the authenticated user.

**Python 3.8 Compatibility:** Python 3.8 does not support `str.removeprefix()`. Therefore, I used `auth.replace("Bearer ", "", 1)` to extract the token.

## 3. Task Router – Protected All Task Routes

In `src/tasks/router.py`, I imported `Depends` and `is_authenticated`.

I added the following authentication dependency to all five task routes:

```python
user = Depends(is_authenticated)
```

I added it alongside the existing database dependency:

```python
db: Session = Depends(get_db)
```

### Routes Protected

1. `POST /tasks/create` – Create a new task.
2. `GET /tasks/all_tasks` – Fetch all tasks.
3. `GET /tasks/one_task/{task_id}` – Fetch one task by ID.
4. `PUT /tasks/update_task/{task_id}` – Update a task.
5. `DELETE /tasks/delete_task/{task_id}` – Delete a task.

### Router Changes Summary

By adding `user = Depends(is_authenticated)` to all five routes, FastAPI checks authentication before allowing the route function to proceed.

- Without a valid token, users cannot access these endpoints.
- The `get_db` dependency provides the database session.
- The `is_authenticated` dependency verifies the user.
- The authenticated user is received through the `user` parameter.

## 4. User Controller – Authentication Updates

I updated the existing authentication code to work with the Bearer authorization header and Python 3.8.

- Read the token from the Authorization header.
- Extracted the token after the `Bearer ` prefix.
- Decoded and validated the JWT.
- Retrieved the user ID from the token.
- Verified the user in the database.
- Returned the authenticated user after successful validation.

## 5. Postman Testing

1. First, I sent the Login API request.
2. I copied the `access_token` from the login response.
3. I opened the protected task API request.
4. I added the following header:

   **Key:** `Authorization`

   **Value:** `Bearer <access_token>`

5. I clicked Send.
6. The protected task API worked with a valid token.
7. Without a valid token, the API returned `401 Not authenticated`.

**Important Concept:**

- JWT is the token format.
- Bearer is the authorization scheme used to send the token.
- The JWT access token is generated during login.
- The same Bearer scheme is used when accessing protected endpoints.

## 6. What I Implemented and Learned

- Learned how authentication protects API endpoints.
- Created the `is_authenticated` helper in `src/utils/helpers.py`.
- Learned how to read the Authorization header.
- Learned how to validate and decode JWT access tokens.
- Learned how to verify users in the database.
- Protected all five task routes using `Depends(is_authenticated)`.
- Tested protected endpoints using Postman.
- Learned the difference between JWT and Bearer.
- Maintained Python 3.8 compatibility by replacing `removeprefix()` with `replace()`.

## Final Summary

In Video 20, I learned how to secure task APIs using JWT authentication. I created an authentication helper, added the authentication dependency to all five task routes, and tested the endpoints using Postman.

Now, users must log in first and send a valid JWT access token through the `Authorization` header using the Bearer scheme before they can create, read, update, or delete tasks.
