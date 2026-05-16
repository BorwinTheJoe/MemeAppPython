# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI
from src.controllers import AuthRouter
from src.lifecycle import lifespan

app = FastAPI(lifespan=lifespan)

app.include_router(AuthRouter)
