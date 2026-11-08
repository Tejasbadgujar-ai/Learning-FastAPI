# Video 16 – User Registration in FastAPI (Sign Up with Password Hashing)

## What I Learned

In this video, I learned how to create a basic user registration API in FastAPI. I worked on creating the user schema, database model, controller, and router.

## 1. dtos.py

Created a `UserSchema` using Pydantic's `BaseModel` to define and validate user registration details.

```python
from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str
    Mobile_num: int
```

**Explanation:**
- Used `BaseModel` for request data validation.
- Defined name, username, password, email, and mobile number fields.

## 2. models.py

Created a SQLAlchemy user model to define the database table.

```python
from sqlalchemy import Column, Integer, DateTime, Boolean, String
from src.utils.db import Base

class userModel(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    email = Column(String)
    Mobile_num = Column(Integer)
```

**Explanation:**
- Created a table named `user_table`.
- Added columns for user information.
- Made username and hash_password non-nullable.

## 3. controller.py

Created a registration controller to handle incoming user data.

```python
from src.user.dtos import UserSchema
from sqlalchemy.orm import Session

def register(body: UserSchema, db: Session):
    print(body)
    return {"msg": "Resgistration Done"}
```

**Explanation:**
- Accepted registration data using `UserSchema`.
- Accepted a database session using SQLAlchemy `Session`.
- Printed the received user data.
- Returned a registration success message.

## 4. router.py

Created a user registration POST endpoint.

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user.dtos import UserSchema
from src.user import controller

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", status_code=201)
def register(body: UserSchema, db: Session = Depends(get_db)):
    return controller.register(body, db)
```

**Explanation:**
- Created an APIRouter with `/user` prefix.
- Created POST `/register` endpoint.
- Used `Depends(get_db)` to get the database session.
- Connected the router with the registration controller.
- Set the response status code to 201.

## 5. main.py

Imported and included the user router in the main FastAPI application.

```python
from fastapi import FastAPI

from src.tasks.models import TaskModel  # noqa: F401 (needed for create_all)
from src.tasks.router import task_routes
from src.user.router import user_routes
from src.utils.db import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(title="Task Management Application")

app.include_router(task_routes)
app.include_router(user_routes)
```

**Explanation:**
- Imported `user_routes`.
- Registered the user router using `app.include_router(user_routes)`.

## 6. tasks/router.py

- Fixed a spelling mistake in the existing code.
- Saved the corrected file.

## API Endpoint

- Method: POST
- Endpoint: `/user/register`
- Status Code: 201 Created

## What I Understood

I learned how to create a basic user registration structure in FastAPI using Pydantic, SQLAlchemy, controllers, and routers. I also learned how to connect a new user router with the main application.

**Note:** The actual password hashing and saving user details into the database have not yet been implemented in this code.
