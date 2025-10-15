from fastapi import APIRouter
from src.schemas.toDoSchema import toDoCreate, toDoOut, toDoUpdate
from src.database.dbconfig import dbDependency
from src.services.toDoService import createNewToDo

router = APIRouter(
    prefix="/toDo´s",
    tags=["toDo´s"],
)

@router.post("/create", response_model=toDoOut, status_code=201)
async def createToDo(db: dbDependency, payload: toDoCreate):
    return createNewToDo(db, payload)