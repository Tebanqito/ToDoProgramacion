from typing import Optional
from pydantic import BaseModel, ConfigDict

class ToDoBase(BaseModel):
    title: str
    description: str
    isDone: bool = True
    importance: int = None

class ToDoCreate(ProductBase):
    pass

class ToDoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    isDone: Optional[bool] = None
    importance: Optional[int] = None

class ToDoOut(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)