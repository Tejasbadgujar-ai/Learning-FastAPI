# Video 10 – Create POST Endpoint with Database

## 1. What I Learned in This Video

In this video, I learned how to create a POST API endpoint in FastAPI and save data into a database using SQLAlchemy.

I also learned how to connect the router, controller, DTO, database session, and model.

## 2. APIRouter

`APIRouter` is used to create separate routes for different modules of an application.

Example:

```python
from fastapi import APIRouter

task_routes = APIRouter(prefix="/tasks")
```

Here:

* `APIRouter()` creates a router.
* `prefix="/tasks"` adds `/tasks` before every route inside this router.

## 3. POST Method

POST is an HTTP method used to send data to the server and create a new resource.

Example:

```python
@task_routes.post("/create")
def create_task():
    return {"status": "Task created successfully"}
```

Complete endpoint:

`POST /tasks/create`

## 4. DTO (Data Transfer Object)

DTO defines the structure of data that the API expects from the client.

Example:

```python
from pydantic import BaseModel

class TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False
```

Here:

* `title` must be a string.
* `description` must be a string.
* `is_completed` is a Boolean and its default value is `False`.

DTO also helps FastAPI validate incoming request data.

## 5. Request Body

The request body contains the data sent by the client to the API.

Example JSON:

```json
{
    "title": "Learn FastAPI",
    "description": "Learning database operations",
    "is_completed": false
}
```

FastAPI validates this data using `TaskSchema`.

## 6. Controller

The controller contains the main logic of the API.

Example:

```python
from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel

def create_task(body: TaskSchema, db: Session):

    data = body.model_dump()

    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"]
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "status": "task created successfully",
        "data": new_task
    }
```

### Important concepts

**`body: TaskSchema`**

* Receives request data.
* Uses the DTO schema for validation.

**`db: Session`**

* Receives the database session.
* A session is used to communicate with the database.

**`body.model_dump()`**

* Converts Pydantic model data into a Python dictionary.

**`TaskModel()`**

* Creates a new SQLAlchemy model object.

**`db.add(new_task)`**

* Adds the new object to the database session.
* It does not permanently save it yet.

**`db.commit()`**

* Commits the transaction and saves the changes in the database.

**`db.refresh(new_task)`**

* Refreshes the object with the latest database values, such as its generated ID.

## 7. Dependency Injection – Depends()

FastAPI provides dependency injection through `Depends()`.

It allows us to provide required dependencies, such as a database session, to an endpoint.

Example:

```python
from fastapi import Depends
from src.utils.db import get_db

@task_routes.post("/create")
def create_task(body: TaskSchema, db=Depends(get_db)):
    return controller.create_task(body, db)
```

Here:

* `Depends(get_db)` tells FastAPI to execute the `get_db` dependency.
* `get_db` provides a database session.
* That session is passed to the controller.
* The dependency handles closing the session after the request.

## 8. Router and Controller Connection

The router receives the request and passes the data to the controller.

The controller performs the actual database operation.

Flow:

Client → Router → DTO Validation → Database Dependency → Controller → SQLAlchemy Model → Database

## 9. Testing with Postman

I tested the endpoint using Postman.

Method: POST

URL:

`http://127.0.0.1:8000/tasks/create`

Body → raw → JSON:

```json
{
    "title": "Learn FastAPI",
    "description": "Learning database operations",
    "is_completed": false
}
```

The API returned a successful response.

## 10. Important Things to Remember

* APIRouter helps organize application routes.
* POST is used to create resources.
* DTO defines and validates incoming data.
* `model_dump()` converts Pydantic data into a dictionary.
* SQLAlchemy Session communicates with the database.
* `db.add()` adds an object to the session.
* `db.commit()` saves the transaction.
* `db.refresh()` refreshes the object with database values.
* `Depends()` provides dependencies to FastAPI endpoints.
* Controller contains the business logic.

## 11. What I Practiced

I practiced creating a POST endpoint, receiving JSON data, validating it through a DTO, injecting a database session, creating a SQLAlchemy model object, and saving the data into the database.
