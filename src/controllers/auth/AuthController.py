from pydantic import BaseModel
from fastapi import APIRouter, FastAPI
from src.services import AuthService
from src.models import UserDTO, RegisterDTO
import uuid
import jwt

AuthRouter = APIRouter(prefix="/auth", tags=["Auth"])

class AuthController (BaseModel):

    @AuthRouter.post("/login")
    @staticmethod
    def login(userDTO: UserDTO):
        return AuthService.login(userDTO)

    @AuthRouter.post("/register")
    @staticmethod
    def register(registerDTO: RegisterDTO):
        return AuthService.login(registerDTO)
