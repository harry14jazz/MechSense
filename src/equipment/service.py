# src/equipment/service.py
from sqlalchemy.orm import Session

from src.equipment import models, schemas


def get_equipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Equipment).offset(skip).limit(limit).all()

def create_equipment(db: Session, equipment: schemas.EquipmentCreate):
    db_eq = models.Equipment(**equipment.model_dump())
    db.add(db_eq)
    db.commit()
    db.refresh(db_eq)
    return db_eq

def create_hm_log(db: Session, hm_log: schemas.HourMeterLogCreate):
    db_log = models.HourMeterLog(**hm_log.model_dump())
    db.add(db_log)

    # 2. Update current_hm di tabel Master Equipment (Mazhab Hybrid)
    equipment = db.query(models.Equipment).filter(models.Equipment.id == hm_log.equipment_id).first()
    if equipment:
        # Asumsinya nilai HM yang baru dimasukkan adalah nilai aktual tertinggi di dashboard unit
        equipment.current_hm = hm_log.hour_meter    # pyright: ignore

    db.commit()
    db.refresh(db_log)
    return db_log

def create_status_log(db: Session, status_log: schemas.EquipmentStatusLogCreate):
    db_log = models.EquipmentStatusLog(**status_log.model_dump())
    db.add(db_log)

    equipment = db.query(models.Equipment).filter(models.Equipment.id == status_log.equipment_id).first()
    if equipment:
        equipment.unit_status = status_log.status_to    # pyright: ignore

    db.commit()
    db.refresh(db_log)
    return db_log
