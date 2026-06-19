# src/equipment/router.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.equipment import models, schemas, service

router = APIRouter(
    prefix="/api/v1/equipments",
    tags=["Equipment Management"]
)

# --- ENDPOINTS EQUIPMENT ---
@router.post("/", response_model=schemas.EquipmentResponse)
def create_equipment(equipment: schemas.EquipmentCreate, db: Session = Depends(get_db)):
    # Kita bisa tambahin validasi misal S/N ga boleh duplikat
    existing_eq = db.query(models.Equipment).filter(models.Equipment.serial_number == equipment.serial_number).first()
    if existing_eq:
        raise HTTPException(status_code=400, detail="Serial Number already exists!")

    return service.create_equipment(db=db, equipment=equipment)

@router.get("/", response_model=List[schemas.EquipmentResponse])
def read_equipments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_equipments(db, skip=skip, limit=limit)

# --- ENDPOINTS LOGS ---
@router.post("/hm-log", response_model=schemas.HourMeterLogResponse)
def add_hm_log(hm_log: schemas.HourMeterLogCreate, db: Session = Depends(get_db)):
    return service.create_hm_log(db=db, hm_log=hm_log)

@router.post("/status-log", response_model=schemas.EquipmentStatusLogResponse)
def add_status_log(status_log: schemas.EquipmentStatusLogCreate, db: Session = Depends(get_db)):
    return service.create_status_log(db=db, status_log=status_log)
