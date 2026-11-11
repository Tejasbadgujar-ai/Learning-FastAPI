from fastapi import FastAPI

from src.tasks.models import TaskModel  # noqa: F401 (needed for create_all)
from src.tasks.router import task_routes
from src.user.models import UserModel  # noqa: F401
from src.user.router import user_routes
from src.utils.db import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(title="Task Management Application")

app.include_router(task_routes)
app.include_router(user_routes)
