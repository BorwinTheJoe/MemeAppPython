from pydantic import BaseModel, ConfigDict
from datetime import datetime

class User(BaseModel):
    uuid: str
    username: str
    passwordHash: str
    postList: list[str]
    registrationDate: datetime

    model_config = ConfigDict(from_attributes = True)
