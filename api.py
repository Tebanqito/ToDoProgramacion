from fastapi import FastAPI
from src.controllers.toDoController import router as toDoRouter

def register_routes(app: FastAPI):
    app.include_router(toDoRouter)