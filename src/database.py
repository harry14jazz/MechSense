from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData

from src.config import settings

SCHEMA_NAME = "sample_company_1"

engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    echo=True if settings.ENVIRONMENT == "development" else False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata_obj = MetaData(schema=SCHEMA_NAME)
Base = declarative_base(metadata=metadata_obj)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
