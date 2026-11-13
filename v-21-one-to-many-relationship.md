# Video 22: Implement One-to-Many Relationship in FastAPI and SQLAlchemy

## 1. Introduction

In this video, I learned how to implement a One-to-Many relationship between Users and Tasks using FastAPI and SQLAlchemy.

One-to-Many means:
- One user can have multiple tasks.
- Each task belongs to one user.
- `user_id` connects tasks with users.

## 2. Install Alembic

Alembic is used to manage database schema changes.

```bash
pip install alembic
```

## 3. Initialize Alembic

```bash
alembic init migrations
```

This creates the Alembic configuration and migrations folder.

## 4. Configure Database Connection in env.py

In `migrations/env.py`, I added:

```python
config.set_main_option("sqlalchemy.url", settings.DB_CONNECTION)
```

This allows Alembic to use the database connection from project settings.

## 5. Update Task DTO

File: `src/tasks/dtos.py`

Added `Optional` import:

```python
from typing import Optional
```

Updated `TaskResponseSchema`:

```python
class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    user_id: Optional[int] = 0
```

This adds the user's ID to the task response schema. `Optional[int]` is used for Python 3.8 compatibility.

## 6. Update Task Model

File: `src/tasks/models.py`

Added a Foreign Key:

```python
user_id = Column(Integer, ForeignKey("user_table.id", ondelete="CASCADE"))
```

This connects each task to a user through the user's ID.

## 7. Update Task Controller

File: `src/tasks/controller.py`

Imported UserModel:

```python
from src.user.models import UserModel
```

Updated the `create_task()` function:

```python
def create_task(body: TaskSchema, db: Session, user: UserModel):
    data = body.model_dump()

    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"],
        user_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task
```

Here, `user.id` assigns the authenticated user's ID to the newly created task.

## 8. Update Task Router

File: `src/tasks/router.py`

Updated the Create Task endpoint to get the authenticated user:

```python
user: UserModel = Depends(is_authenticated)
```

Passed the user to the controller:

```python
return controller.create_task(body, db, user)
```

This ensures the task is created with the logged-in user's ID.

## 9. Database Migration Using Alembic

After updating the SQLAlchemy model, I needed to update the database structure.

### Generate Migration

```bash
alembic revision --autogenerate -m "add user_id to tasks"
```

This generates a migration file based on the model changes.

### Apply Migration

```bash
alembic upgrade head
```

This applies the migration to the database.

**Important:** Generating a migration and applying it are two different steps.

## 10. Alembic Migration Workflow

Whenever database model changes are made:

1. Update the SQLAlchemy model.
2. Generate a migration.
3. Review the generated migration file.
4. Apply migration using `alembic upgrade head`.
5. Verify the database changes.

## 11. What I Learned

- One-to-Many relationship between Users and Tasks.
- How Foreign Keys connect database tables.
- How to associate tasks with authenticated users.
- How to use `Depends(is_authenticated)`.
- How to install and initialize Alembic.
- How to configure Alembic database connection.
- How to generate and apply migrations.
- Difference between generating and applying migrations.

## 12. Conclusion

In this video, I implemented a One-to-Many relationship between Users and Tasks.

I updated the DTO, model, controller and router files. I also configured Alembic, generated a migration and applied the database changes.

Now each task is associated with the authenticated user who created it.
