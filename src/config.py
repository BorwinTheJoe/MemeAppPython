from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Tell Pydantic to read from the .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Define your variables and their types.
    # You can provide defaults if they might be missing from .env.
    DATABASE_URL: str
    ENVIRONMENT: str
    APP_PORT: int
    SECRET_KEY: str # No default means this is REQUIRED in .env!

settings = Settings()