from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 [System] Initializing Database...")
    init_db()
    print("✅ [System] Database Initialized and Ready!")
    yield
    print("🛑 [System] Shutting down application...")
