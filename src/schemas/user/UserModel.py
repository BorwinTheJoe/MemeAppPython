from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from src.database import Base

class UserModel(Base):
    __tablename__ = "users"

    uuid: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    passwordHash: Mapped[str]

    # SQLite doesn't support arrays, so we store the list as JSON
    postList: Mapped[list[str]] = mapped_column(JSON)

    registrationDate: Mapped[datetime]