from fastapi import FastAPI
from src.api import registerRoutes

app = FastAPI()

registerRoutes(app)