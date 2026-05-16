from pydantic import BaseModel
from fastapi import APIRouter, Depends
from src.services import AuthService
from src.models import UserDTO, RegisterDTO, User
from sqlalchemy.orm import Session
from src.database import get_db

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

    @AuthRouter.post("/users/", response_model=User)
    @staticmethod
    def create_user(user: User, db: Session = Depends(get_db)):
        return AuthService.create_user(user, db)

    @AuthRouter.get("/users/", response_model=list[User])
    @staticmethod
    def get_users(db: Session = Depends(get_db)):
        return AuthService.get_users(db)

