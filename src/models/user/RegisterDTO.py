from pydantic import BaseModel, EmailStr

class RegisterDTO(BaseModel):
    username: str
    password: str
    email: EmailStr