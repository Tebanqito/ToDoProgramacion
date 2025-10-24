from typing import Optional
from pydantic import BaseModel, ConfigDict

class TaskBase(BaseModel):
    id: int
    name: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class TaskOut(TaskBase):
    id: int
    model_config = ConfigDict(from_attributes=True)