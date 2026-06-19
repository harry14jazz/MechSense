from fastapi import FastAPI
from sqlalchemy import text

import src.component.models  # noqa: F401
import src.equipment.models
import src.master_data.models  # noqa: F401
from src.config import settings
from src.database import SCHEMA_NAME, Base, engine
from src.equipment.router import router as equipment_router
from src.master_data.router import router as master_data_router

with engine.connect() as conn:
    conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME}"))
    conn.commit()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Maximize Your Asset Health Monitoring"
)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": f"Wagwan—{settings.PROJECT_NAME}"
    }

app.include_router(master_data_router)
app.include_router(equipment_router)
