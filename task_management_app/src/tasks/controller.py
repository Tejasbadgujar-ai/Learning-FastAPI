from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.tasks.dtos import TaskSchema
from src.tasks.models import TaskModel


# controller function to create a task
def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()

    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"]
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"status": "task created successfully....", "data": new_task}


def get_all_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    return {"status": "all tasks", "data": tasks}


def get_one_task(task_id: int, db: Session):
    task = db.get(TaskModel, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"status": "task fetched successfully", "data": task}
