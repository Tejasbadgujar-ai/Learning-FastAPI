# Video 14 – Production-Ready FastAPI: Improve Endpoints & Best Practices

## What I Learned

In this video, I learned how to improve FastAPI endpoints using HTTP status codes, response models, and dependency injection.

I worked mainly in three files:

- `src/tasks/dtos.py`
- `src/tasks/controller.py`
- `src/tasks/router.py`

## 1. HTTP Status Codes

HTTP status codes tell the client whether an API request was successful or failed.

| Code | Meaning | Use |
|---|---|---|
| 200 | OK | Data fetched successfully |
| 201 | Created | New task created |
| 204 | No Content | Task deleted without response body |
| 400 | Bad Request | Invalid request |
| 401 | Unauthorized | Authentication required or invalid |
| 403 | Forbidden | Access not allowed |
| 404 | Not Found | Requested task does not exist |

**What I implemented:**

I configured status codes directly in router decorators.

Example:

```python
@task_routes.post("/create", status_code=201)
```

This tells FastAPI to return `201` when a task is successfully created.

## 2. Response Models – dtos.py

I added `TaskResponseSchema` to control which fields should be returned by the API.

```python
class TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False


class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
```

**How it works:**

- `TaskSchema`: Validates incoming data from the client.
- `TaskResponseSchema`: Defines the fields returned to the client.

For example, if the database contains extra fields, FastAPI returns only the fields defined in `TaskResponseSchema`.

This helps prevent unnecessary data from being exposed.

## 3. Using response_model in Router

I added `response_model` to the endpoints to control their response structure.

**Create Task:**

```python
@task_routes.post("/create", response_model=TaskResponseSchema, status_code=201)
```

Returns one task.

**Get All Tasks:**

```python
@task_routes.get("/all_tasks", response_model=List[TaskResponseSchema], status_code=200)
```

`List[TaskResponseSchema]` means the endpoint returns a list of tasks, with each task following the response schema.

**Get One Task:**

```python
@task_routes.get("/one_task/{task_id}", response_model=TaskResponseSchema, status_code=200)
```

Returns one task using the response schema.

**Update Task:**

```python
@task_routes.put("/update_task/{task_id}", response_model=TaskResponseSchema, status_code=200)
```

Returns the updated task using the response schema.

**Delete Task:**

```python
@task_routes.delete("/delete_task/{task_id}", response_model=None, status_code=204)
```

- `response_model=None`: No response model is used.
- `204`: Successful deletion without a response body.

Note: For updating an existing resource, `200` or `204` is generally preferred. Here, `201` is the status code used in the tutorial implementation.

## 4. Database Dependency Injection

I used `Depends(get_db)` consistently in router endpoints.

Example:

```python
def get_all_tasks(db: Session = Depends(get_db)):
    return controller.get_all_tasks(db)
```

- `db: Session` specifies the SQLAlchemy database session type.
- `Depends(get_db)` tells FastAPI to provide a database session.
- The session is passed to the controller.

This avoids manually creating a database session in every endpoint.

## 5. Code Organisation

I improved the separation of responsibilities:

- **Router:** Handles API paths, HTTP methods, status codes, response models, and dependencies.
- **Controller:** Handles database operations.
- **DTOs:** Define request and response schemas.

This makes the application easier to maintain and understand.

## 6. Testing

I tested the updated endpoints and checked their responses.

- POST `/tasks/create` – Verified task creation and `201`.
- GET `/tasks/all_tasks` – Verified task list and `200`.
- GET `/tasks/one_task/{task_id}` – Verified individual task response.
- PUT `/tasks/update_task/{task_id}` – Verified updated task response.
- DELETE `/tasks/delete_task/{task_id}` – Verified deletion and `204` without a response body.

## Key Takeaways

- Learned common HTTP status codes.
- Understood request and response schemas.
- Used `response_model` to control API output.
- Learned `List[TaskResponseSchema]` for multiple records.
- Used `response_model=None` for no-content responses.
- Applied `Depends(get_db)` consistently.
- Improved router, controller, and DTO organisation.
- Tested the updated API endpoints.
