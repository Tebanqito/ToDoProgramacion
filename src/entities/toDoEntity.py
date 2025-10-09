from typing import Optional
from sqlalchemy import String, Float, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.entities.base import Base

class ToDo(Base):
    __tablename__ = "toDo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    isDone: Mapped[bool] = mapped_column(Boolean, default=True)
    importance: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True, index=True)