# FastAPI GET Endpoint – Fetch Specific Record from Database by ID

## What I Learned

In this video, I learned how to fetch a specific task from the database using its ID through a GET endpoint.

Previously, I learned how to retrieve all tasks from the database. In this video, I learned how to retrieve only one specific task by passing its ID in the URL.

I worked mainly in two files:

- `controller.py`
- `router.py`

## 1. Controller.py

I imported `HTTPException` from FastAPI and added a new function named `get_one_task()` to fetch a specific task from the database.

### Code Added

```python
from fastapi import HTTPException

def get_one_task(task_id: int, db: Session):
    one_task = db.get(TaskModel, task_id)

    if not one_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "status": "task fetched successfully",
        "data": one_task
    }
```

### Explanation

- `get_one_task(task_id, db)`: Creates a function that receives the task ID and database session.
- `db.get(TaskModel, task_id)`: Fetches the task using its primary key ID. It returns the task if found, otherwise it returns `None`.
- `if not one_task`: Checks whether the requested task exists.
- `HTTPException`: Raises an HTTP error if the task is not found.
- `return`: Returns the specific task with a status message.

The 404 error occurred because I used an incorrect URL in Postman. I used `/tasks/one_tasks/1` instead of the correct endpoint `/tasks/one_task/1`. After correcting the URL, the endpoint worked correctly.

## 2. Router.py

I added a new GET route to fetch a specific task using its ID.

### Code Added

```python
@task_routes.get("/one_task/{task_id}")
def get_one_task(task_id: int, db: Session = Depends(get_db)):
    return controller.get_one_task(task_id, db)
```

### Explanation

- `@task_routes.get("/one_task/{task_id}")`: Creates a GET endpoint with a dynamic task ID.
- `{task_id}`: Accepts the task ID from the URL.
- `task_id: int`: Defines the task ID as an integer.
- `Depends(get_db)`: Provides the database session.
- `controller.get_one_task(task_id, db)`: Calls the controller function and passes the task ID and database session.

## 3. How It Works

1. The client sends a GET request with a specific task ID.
2. The router receives the request.
3. FastAPI extracts the task ID from the URL.
4. The router calls the controller function.
5. The controller searches for the task using its ID.
6. If the task exists, it returns the task details.
7. If the task does not exist, it raises an HTTP 404 exception.

## 4. Endpoint

```text
GET /tasks/one_task/{task_id}
```

Example:

```text
GET /tasks/one_task/1
```

Here, `1` represents the task ID.

## 5. Errors and Debugging

While implementing and testing the endpoint, I encountered a 404 Not Found error.

I checked the endpoint URL, HTTP request method, router configuration, and route registration.

After debugging, I resolved the issue and successfully tested the endpoint.

This helped me understand how to identify and fix routing-related errors in FastAPI.

## 6. What I Learned

- How to create a GET endpoint for a specific database record.
- How to pass an ID through a URL path parameter.
- How to fetch a specific record using SQLAlchemy.
- How to use `.get()` to retrieve a record using its primary key.
- How to connect a router function with a controller function.
- How to use `HTTPException` when a requested task does not exist.
- How to debug and resolve a 404 error.

## 7. Additional Concept Learned

I was also introduced to HTTP status codes and how they represent the result of an API request. Their detailed implementation will be covered in the upcoming tutorial.

## Conclusion

In this video, I added a new function in the controller and a GET route in the router to fetch a specific task from the database using its ID.

I also learned how to handle an incorrect task ID using HTTPException and successfully resolved a 404 error during testing.
