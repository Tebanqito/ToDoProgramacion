from fastapi import FastAPI
from src.controllers.toDoController import router as toDoRouter

def registerRoutes(app: FastAPI):
    app.include_router(toDoRouter)