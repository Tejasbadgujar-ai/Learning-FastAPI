# Token-Based Authentication - Secure API Endpoints in FastAPI

## 1. Required Imports

```python
from fastapi import HTTPException, Request
from jwt.exceptions import InvalidTokenError
```

### Meaning
- `Request`: Accesses HTTP request headers.
- `HTTPException`: Raises HTTP errors.
- `InvalidTokenError`: Handles invalid JWT token errors.

## 2. Controller Code

File: `src/user/controller.py`

```python
def is_authenticated(request: Request, db: Session):
    try:
        token = request.headers.get("authorization")

        if not token:
            raise HTTPException(
                status_code=401,
                detail="You Are unauthorized."
            )

        token = token.split(" ")[-1]

        data = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = data.get("id")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="You Are unauthorized."
            )

        return user

    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="You Are unauthorized."
        )
```

### Code Explanation

- `request.headers.get("authorization")`: Gets the token from request headers.
- `if not token`: Checks whether the token is missing.
- `token.split(" ")[-1]`: Extracts the actual token.
- `jwt.decode()`: Decodes and verifies the token.
- `data.get("id")`: Retrieves the user ID.
- `db.query()`: Checks whether the user exists in the database.
- `return user`: Returns the authenticated user.
- `try-except`: Handles invalid JWT tokens.
- `HTTPException 401`: Returns an Unauthorized error.

## 3. Router Code

File: `src/user/router.py`

```python
@user_routes.get(
    "/is_auth",
    status_code=200,
    response_model=UserResponseSchema
)
def is_auth(request: Request, db: Session = Depends(get_db)):
    return controller.is_authenticated(request, db)
```

### Code Explanation

- `@user_routes.get()`: Creates a GET endpoint.
- `/is_auth`: Endpoint path.
- `Request`: Receives the HTTP request.
- `Depends(get_db)`: Provides the database session.
- `controller.is_authenticated()`: Connects the router with the controller.
- Also imported `Request` in the router.

## 4. Practical Work – Token Expiration

- Practiced changing token expiration time in the controller.
- Tested 30 seconds and 40 seconds.
- Ran the API using Postman.
- Checked authentication before and after token expiration.

## 5. What I Learned

- JWT token-based authentication.
- Accessing authorization headers using `Request`.
- Decoding and verifying JWT tokens.
- Handling invalid tokens using `try-except`.
- Checking users in the database.
- Connecting controller functions with routers.
- Testing token expiration using Postman.

## 6. Files Updated

- `src/user/controller.py`
- `src/user/router.py`
- `src/tasks/router.py`

## Conclusion

Completed Video 19 and practiced implementing token-based authentication and securing FastAPI endpoints using JWT.
