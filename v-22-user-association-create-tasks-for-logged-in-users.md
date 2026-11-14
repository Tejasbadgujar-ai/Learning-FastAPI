# Video 22: FastAPI User Association - Create Tasks for Logged-in Users

## 1. Introduction

In this video, I learned how to associate tasks with logged-in users and how to manage task access based on user ownership.

I also learned the difference between Authentication and Authorization.

## 2. User Association with Tasks

- Learned how to associate a task with a logged-in user.
- Understood how user information is passed from the router to the controller.
- Used the logged-in user's information to identify task ownership.
- Learned why tasks should be associated with their respective users.

## 3. Get All Tasks

### Router.py
- Added the logged-in user as a parameter in the GET endpoint.
- Passed both the database session and logged-in user to the controller.

### Controller.py
- Updated the `get_all_tasks()` function to accept the user parameter.
- Used the logged-in user's ID to retrieve tasks associated with that user.
- Checked how users can access their own tasks instead of everyone else's tasks.

## 4. Update Task

### Router.py
- Added the logged-in user parameter to the update task endpoint.
- Passed the user information to the controller.

### Controller.py
- Updated the `update_task()` function to accept the user parameter.
- Checked whether the task belongs to the logged-in user.

```python
if one_task.user_id != user.id:
    raise HTTPException(
        status_code=401,
        detail="You Are Not Allow To Update This Task"
    )
```

- If the task does not belong to the logged-in user, an HTTPException is raised.
- This prevents users from updating other users' tasks.

## 5. Delete Task

### Router.py
- Added the logged-in user parameter to the delete task endpoint.
- Passed the database session and user information to the controller.

### Controller.py
- Updated the `delete_task()` function to accept the user parameter.

```python
def delete_task(task_id: int, db: Session, user: UserModel):
```

- Checked whether the task belongs to the logged-in user.

```python
if one_task.user_id != user.id:
    raise HTTPException(
        status_code=401,
        detail="You Are Not Allow To delete This Task"
    )
```

- If the task belongs to another user, deletion is not allowed.
- Understood how task ownership prevents unauthorized deletion.

## 6. Authentication vs Authorization

### Authentication
Authentication means verifying who the user is.

Example:
- User logs in with their credentials.
- The application verifies the user's identity.
- After successful authentication, the user gets access through authentication tokens.

### Authorization
Authorization means checking what an authenticated user is allowed to do.

Example:
- A logged-in user can access their own tasks.
- A user cannot update another user's task.
- A user cannot delete another user's task.

## 7. Testing

Tested the following operations using the database and API:

1. Get All Tasks – Checked tasks associated with the logged-in user.
2. Update Task – Checked whether another user's task could be updated.
3. Delete Task – Checked whether another user's task could be deleted.
4. Tested task ownership using different user IDs.
5. Verified that changing the task ID does not allow unauthorized access to another user's task.

## 8. Files Modified

- `src/tasks/router.py`
- `src/tasks/controller.py`

## 9. What I Learned

- User association with tasks.
- Passing logged-in user information from router to controller.
- Filtering tasks based on user ID.
- Checking task ownership before updating or deleting.
- Preventing unauthorized task access.
- Difference between Authentication and Authorization.
- Using `HTTPException` to handle unauthorized operations.

## Conclusion

In this video, I learned how to associate tasks with logged-in users and implement user-based access control for Get All Tasks, Update Task, and Delete Task operations.
