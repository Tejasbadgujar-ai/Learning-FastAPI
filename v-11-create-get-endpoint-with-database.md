# Create GET Endpoint with Database – Fetch Data

## What I Learned

In this video, I learned how to fetch existing tasks from the database using a GET endpoint.

Previously, I learned how to create tasks using POST. In this video, I learned how to retrieve all existing tasks from the database.

## 1. Controller.py

I added a new function named `get_all_tasks()` to retrieve all existing tasks from the database.

### Code Added

```python
def get_all_tasks(db: Session):

    tasks = db.query(TaskModel).all()

    return {"status": "all tasks", "data": tasks}
```

### Explanation

* `get_all_tasks(db: Session)`: Creates a function that receives the database session.
* `db.query(TaskModel)`: Fetches records from the TaskModel table.
* `.all()`: Retrieves all available task records.
* `return`: Returns the retrieved tasks with a status message.

**Note:** The existing `create_task()` function was not changed. I only added this new function.

## 2. Router.py

I added a new GET route to fetch all tasks.

### Code Added

```python
@task_routes.get("/all_tasks")
def get_all_tasks(db: Session = Depends(get_db)):
    return controller.get_all_tasks(db)
```

### Explanation

* `@task_routes.get("/all_tasks")`: Creates a GET endpoint.
* `get_all_tasks()`: Handles the incoming GET request.
* `Depends(get_db)`: Provides the database session.
* `controller.get_all_tasks(db)`: Calls the new controller function and passes the database session.

## 3. How It Works

1. The client sends a GET request.
2. The router receives the request.
3. The router calls `get_all_tasks()` from the controller.
4. The controller fetches all tasks from the database.
5. The retrieved tasks are returned to the client.

## 4. Postman Testing

I tested the new GET endpoint using Postman.

Steps:

1. Open Postman.
2. Select GET as the request method.
3. Enter the endpoint URL.
4. Click Send.
5. Check the response and verify the retrieved tasks.

Endpoint:

```text
GET /tasks/all_tasks
```

## 5. Errors and Debugging

While testing, I learned to check the endpoint URL, request method, router configuration and controller function whenever the expected response was not received.

I also learned to check the Postman response to understand the API result.

## 6. What I Learned

* How to create a GET endpoint.
* How to add a new function in the controller.
* How to retrieve all records using SQLAlchemy.
* How to use `.query()` and `.all()`.
* How the router calls the controller function.
* How to test a GET endpoint using Postman.

## Conclusion

In this video, I added a new function in the controller and a GET route in the router to retrieve all existing tasks from the database. I also tested the endpoint using Postman.
