from pydantic import BaseModel, ConfigDict


class ToDO(BaseModel):
    id: int
    title: str
    description: str
    isDone: bool
    importance: int

    model_config = ConfigDict(from_attributes=True)