from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.config import settings

# connect_args is needed for SQLite multi-threading
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

# The session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def init_db():
    # We must import the models here so SQLAlchemy knows what tables to create
    from src import models
    Base.metadata.create_all(bind=engine)

def get_db():
    """Dependency to yield a database session per API request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
