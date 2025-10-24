from sqlalchemy.orm import Session
from src.schemas.task_schema import TaskCreate, TaskUpdate
from src.entities.task_entity import Task

def create_new_task(db: Session,
                       task: TaskCreate):
    new_task = Task(
        name = task.name,
        description = task.description,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task_by_id(db: Session, task_id: int, 
                         task_update: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.name = task_update.name or task.name
        task.description = task_update.description or task.description
        db.commit()
        db.refresh(task)
        return task
    return None

def delete_task_by_id(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False