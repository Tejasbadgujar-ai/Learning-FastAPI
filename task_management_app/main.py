from fastapi import FastAPI

from src.utils.db import Base, engine
from src.tasks.models import TaskModel  # noqa: F401 (needed for create_all)
from src.tasks.router import task_routes

Base.metadata.create_all(engine)

app = FastAPI(title="Task Management Application")

app.include_router(task_routes)
