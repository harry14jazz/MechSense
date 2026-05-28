# src/main.py
from fastapi import FastAPI

import src.equipment.models
import src.master_data.models # noqa: F401
from src.config import settings
from src.database import Base, engine

# Perintah untuk men-generate semua tabel ke PostgreSQL
Base.metadata.create_all(bind=engine)

# Inisialisasi Aplikasi FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="SaaS Asset Health Monitoring Backend"
)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": f"Welcome to {settings.PROJECT_NAME} API"
    }
