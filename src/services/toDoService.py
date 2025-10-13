from sqlalchemy.orm import Session
from src.schemas.toDoSchemas import ToDoCreate
from src.entities.toDoEntity import Product

def create_new_product(db: Session,
                       toDo: ToDoCreate):
    newTdDo = Product(
        title = toDo.title,
        description = toDo.description,
        isDone = toDo.isDone,
        importance = toDo.importance
    )
    db.add(newTdDo)
    db.commit()
    db.refresh(newTdDo)
    return newTdDo