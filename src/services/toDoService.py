from sqlalchemy.orm import Session
from src.schemas.toDoSchemas import ToDoCreate
from src.entities.toDoEntity import Product

def createNewToDo(db: Session, toDo: ToDoCreate):
    newToDo = Product(
        title = toDo.title,
        description = toDo.description,
        isDone = toDo.isDone,
        importance = toDo.importance
    )
    db.add(newToDo)
    db.commit()
    db.refresh(newToDo)
    return newToDo