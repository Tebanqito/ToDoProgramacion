from fastapi import APIRouter
from src.schemas.toDoSchema import toDoCreate, toDoOut, toDoUpdate
from src.database.dbconfig import dbDependency

router = APIRouter(
    prefix="/products",
    tags=["products"],
)