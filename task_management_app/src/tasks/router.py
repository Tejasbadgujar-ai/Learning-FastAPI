from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 

from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create", status_code=201)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)
