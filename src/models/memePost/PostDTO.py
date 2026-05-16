from pydantic import BaseModel
from datetime import datetime

class MemePost(BaseModel):
    title: str
    urlArray: list[str]