from pydantic import BaseModel
from fastapi import APIRouter, FastAPI
from src.MemeApp.view import auth

class AuthController (BaseModel):


    AuthRouter = APIRouter(prefix="/auth", tags=["Auth"])

    @AuthRouter.post("/login")
    @staticmethod
    def login():


