from fastapi import APIRouter
from src.schemas.task_schema import TaskCreate, TaskOut, TaskUpdate
from src.database.dbconfig import db_dependency
from src.services.task_service import (create_new_task, 
                                          delete_task_by_id, 
                                          get_all_tasks, 
                                          get_task_by_id, 
                                          update_task_by_id)


router = APIRouter(
    prefix="/task",
    tags=["task"],
)

@router.post("/create", response_model=TaskOut, status_code=201)
async def create_task(db: db_dependency, payload: TaskCreate):
    return create_new_task(db, payload)

@router.get("")
async def read_tasks(db: db_dependency):
    return get_all_tasks(db)

@router.get("/{task_id}")
async def read_task(task_id: int, db: db_dependency):
    return get_task_by_id(db, task_id)

@router.put("/update/{task_id}")
async def update_taks(task_id: int, 
                          payload: TaskUpdate, 
                          db: db_dependency):
    return update_task_by_id(db, task_id, payload)

@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: db_dependency):
    return delete_task_by_id(db, task_id)