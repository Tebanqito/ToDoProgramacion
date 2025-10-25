from sqlalchemy import String,Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.entities.base import Base

class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
