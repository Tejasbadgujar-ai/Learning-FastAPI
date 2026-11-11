# Build Login API with JWT Tokens - User Authentication in FastAPI

## What I Learned

In this video, I learned how to create a Login API in FastAPI using JWT (JSON Web Tokens) for user authentication.

I learned how to verify user credentials, generate JWT access tokens, configure JWT settings, and return the token after successful login.

I worked mainly in the following files:

- `dtos.py`
- `router.py`
- `controller.py`
- `settings.py`
- `.env`

## 1. Login Schema – dtos.py

I created a `LoginSchema` using Pydantic.

It contains two fields:

- `username`
- `password`

```python
class LoginSchema(BaseModel):
    username: str
    password: str
```

This schema validates the login data received from the user.

## 2. Application Settings – settings.py

I added JWT-related configuration settings to the Settings class:

- `SECRET_KEY`: Used to sign the JWT token.
- `ALGORITHM`: Defines the signing algorithm.
- `EXP_TIME`: Defines the token expiration time in minutes.

```python
SECRET_KEY: str
ALGORITHM: str
EXP_TIME: int
```

I added these values to the `.env` file:

```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256
EXP_TIME=30
```

These values are loaded through Pydantic Settings.

## 3. Login Route – router.py

I created a POST login endpoint:

`/user/login`

The route accepts `LoginSchema` as the request body and uses `Depends(get_db)` to get the database session.

```python
@user_routes.post("/login")
def login(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login_user(body, db)
```

It then calls the `login_user()` function from the controller.

## 4. Login Controller – controller.py

I created the `login_user()` function to handle user login.

The function performs these steps:

1. Searches for the user in the database using the entered username.
2. Checks whether the user exists.
3. Verifies the entered password using `verify_password()`.
4. Raises an HTTP 401 error if the credentials are incorrect.
5. Generates a JWT token after successful verification.

```python
user = db.query(UserModel).filter(
    UserModel.username == body.username
).first()
```

Password verification:

```python
verify_password(body.password, user.hash_password)
```

If the credentials are incorrect, `HTTPException` is used to return HTTP 401 Unauthorized.

## 5. Understanding JWT Tokens

JWT stands for JSON Web Token. It is used to securely transfer information between the client and server.

A JWT contains three main parts:

- Header
- Payload
- Signature

### Payload

The payload contains information about the user.

I added:

- `id`: User's database ID.
- `exp`: Token expiration time.

```python
payload = {
    "id": user.id,
    "exp": exp_time
}
```

### Secret Key

Used to sign the JWT token. It must remain private.

### Algorithm

I used the HS256 algorithm to generate the JWT signature.

## 6. Token Expiration

I used Python's `datetime` and `timedelta` to calculate the token expiration time.

```python
from datetime import datetime, timedelta, timezone

exp_time = datetime.now(timezone.utc) + timedelta(
    minutes=settings.EXP_TIME
)
```

- `datetime.utcnow()`: Gets the current UTC date and time.
- `timedelta()`: Represents a duration of time.
- `EXP_TIME`: Defines the token validity in minutes.

I added the expiration time to the JWT payload using `exp`.

## 7. JWT Token Generation

After successful username and password verification, I generated the token using `jwt.encode()`.

```python
token = jwt.encode(
    payload,
    settings.SECRET_KEY,
    algorithm=settings.ALGORITHM
)
```

I passed the following values:

- User ID and expiration time as the payload.
- Secret key.
- Algorithm.

The controller returns the generated access token after successful authentication.

## 8. Testing the Login API Using Postman

I tested the login endpoint using Postman.

Endpoint:

`POST /user/login`

Request Body:

```json
{
    "username": "tejas",
    "password": "123456"
}
```

After successful authentication, the API returned a JWT access token.

I also understood that the user must first register and then use the same username and password to log in successfully.

## Conclusion

In this video, I learned how to build a Login API using JWT authentication in FastAPI.

I understood how to verify user credentials, configure JWT settings, generate access tokens, add user information to the token payload, and set token expiration time using `datetime` and `timedelta`.
