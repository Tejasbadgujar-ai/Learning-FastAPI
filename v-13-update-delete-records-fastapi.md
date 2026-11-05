## FastAPI Update & Delete Records

## 1. Update Task Controller Function

In this video, I created an `update_task()` function in `controller.py` to update an existing task in the database.

* First, I fetched the task using its ID with `db.get()`.
* If the task does not exist, I raised an HTTP 404 exception.
* I converted the request body into a dictionary using `model_dump()`.
* I used `setattr()` to update the task fields dynamically.
* Finally, I committed and refreshed the updated task.

```python
def update_task(body: TaskSchema, task_id: int, db: Session):
    one_task = db.get(TaskModel, task_id)

    if not one_task:
        raise HTTPException(status_code=404, detail="Task Id is Incorrect")

    body = body.model_dump()

    for field, value in body.items():
        setattr(one_task, field, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return {"status": "task updated successfully", "data": one_task}
```

## 2. Delete Task Controller Function

I created a `delete_task()` function to delete an existing task from the database.

* First, I fetched the task using its ID.
* If the task does not exist, I raised an HTTP 404 exception.
* I used `db.delete()` to delete the task.
* I used `db.commit()` to save the changes.

```python
def delete_task(task_id: int, db: Session):
    one_task = db.get(TaskModel, task_id)

    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(one_task)
    db.commit()

    return {"status": "task deleted successfully"}
```

## 3. Update Endpoint in Router

I connected the update controller function with the router using a PUT endpoint.

```python
@task_routes.put("/update_task/{task_id}")
def update_task(body: TaskSchema, task_id: int, db: Session = Depends(get_db)):
    return controller.update_task(body, task_id, db)
```

## 4. Delete Endpoint in Router

I connected the delete controller function with the router using a DELETE endpoint.

```python
@task_routes.delete("/delete_task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return controller.delete_task(task_id, db)
```

## 5. Postman Testing

I tested both endpoints using Postman.

**Update Task:**

* Method: PUT
* URL: `/tasks/update_task/{task_id}`
* Passed the task details in the JSON request body.
* Verified that the task was updated successfully.

**Delete Task:**

* Method: DELETE
* URL: `/tasks/delete_task/{task_id}`
* Verified that the task was deleted successfully.

## 6. What I Learned

* How to update existing database records using SQLAlchemy.
* How to use `setattr()` to update model fields dynamically.
* How to delete database records using `db.delete()`.
* How to create PUT and DELETE endpoints in FastAPI.
* How to connect controller functions with router endpoints.
* How to test update and delete operations using Postman.
