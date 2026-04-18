from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    uuid: str
    username: str
    passwordHash: str
    salt: str
    postList: list[str]
    registrationDate: datetime