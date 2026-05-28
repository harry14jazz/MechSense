from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    ENVIRONMENT: str = "development"

    PROJECT_NAME: str = "MechSense"
    VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() # pyright: ignore[reportCallIssue]
