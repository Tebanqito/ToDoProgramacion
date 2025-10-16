from fastapi import APIRouter
from src.schemas.toDoSchemas import ToDoCreate, ToDoOut, ToDoUpdate
from src.database.dbConfig import dbDependency
from src.services.toDoService import createNewToDo

router = APIRouter(
    prefix="/toDo´s",
    tags=["toDo´s"],
)

@router.post("/create", response_model=ToDoOut, status_code=201)
async def createToDo(db: dbDependency, payload: ToDoCreate):
    return createNewToDo(db, payload)