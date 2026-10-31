# Video 9 – SQLAlchemy Models

## 1. Introduction

In this video, I learned how to create SQLAlchemy models and define database tables using Python classes.

SQLAlchemy models help us represent database tables as Python classes.

## 2. Import Required Modules

```python
from sqlalchemy import Column, Integer, String, Boolean
from src.utils.db import Base
```

* `Column`: Defines a database column.
* `Integer`: Defines an integer data type.
* `String`: Defines a string data type.
* `Boolean`: Defines a true/false data type.
* `Base`: Used as the base class for SQLAlchemy models.

## 3. Creating a Task Model

File: `src/tasks/models.py`

```python
from sqlalchemy import Column, Integer, String, Boolean

from src.utils.db import Base


class TaskModel(Base):

    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    description = Column(String)

    is_completed = Column(Boolean, default=False)
```

### Explanation

* `TaskModel`: Python class representing the task table.
* `Base`: Connects the model with SQLAlchemy.
* `__tablename__`: Specifies the database table name.
* `id`: Primary key of the table.
* `title`: Stores the task title.
* `description`: Stores the task description.
* `is_completed`: Stores the task completion status. Its default value is `False`.

## 4. Importing the Model into main.py

Add the following import to `main.py`:

```python
from src.tasks.models import TaskModel
```

This makes the TaskModel available in the main application file.

## 5. Creating Database Tables

```python
Base.metadata.create_all(engine)
```

This command creates database tables based on the SQLAlchemy models if they do not already exist.

## 6. Main.py Code

```python
from fastapi import FastAPI

from src.utils.db import Base, engine

from src.tasks.models import TaskModel

Base.metadata.create_all(engine)

app = FastAPI(title="Task Management Application")
```

## 7. What I Learned

* What SQLAlchemy models are.
* How to create a model using a Python class.
* How to define database columns.
* How to use primary keys.
* How to define Boolean columns.
* How to import models into main.py.
* How to create database tables using `Base.metadata.create_all(engine)`.
