from pydantic import BaseModel
from datetime import datetime

class MemePost(BaseModel):
    uuid: str
    title: str
    posterId: str
    urlArray: list[str]
    postDate: datetime