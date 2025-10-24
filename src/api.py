from fastapi import FastAPI
from src.controllers.task_controller import router as task_router

def register_routes(app: FastAPI):
    app.include_router(task_router)