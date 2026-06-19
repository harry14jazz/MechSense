from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.master_data import schemas, service

router = APIRouter(
    prefix="/api/v1/master-data",
    tags=["Master Data"]
)

# --- ENDPOINTS BRAND ---
@router.post("/brands", response_model=schemas.BrandResponse)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    db_obj = service.get_brand_by_code(db, brand_code=brand.brand_code)
    if db_obj:
        raise HTTPException(status_code=400, detail="Brand code already registered")
    return service.create_brand(db=db, brand=brand)

@router.get("/brands", response_model=List[schemas.BrandResponse])
def read_brands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_brands(db, skip=skip, limit=limit)

# --- ENDPOINTS SITE ---
@router.post("/sites", response_model=schemas.SiteResponse)
def create_site(site: schemas.SiteCreate, db: Session = Depends(get_db)):
    db_obj = service.get_site_by_code(db, site_code=site.site_code)
    if db_obj:
        raise HTTPException(status_code=400, detail="Site code already registered")
    return service.create_site(db=db, site=site)

@router.get("/sites", response_model=List[schemas.SiteResponse])
def read_sites(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_sites(db, skip=skip, limit=limit)

# --- ENDPOINTS EQUIPMENT CLASS ---
@router.post("/classes", response_model=schemas.EquipmentClassResponse)
def create_class(eq_class: schemas.EquipmentClassCreate, db: Session = Depends(get_db)):
    db_obj = service.get_class_by_code(db, class_code=eq_class.class_code)
    if db_obj:
        raise HTTPException(status_code=400, detail="Class code already registered")
    return service.create_equipment_class(db=db, eq_class=eq_class)

@router.get("/classes", response_model=List[schemas.EquipmentClassResponse])
def read_classes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_equipment_classes(db, skip=skip, limit=limit)

# --- ENDPOINTS EQUIPMENT MODEL ---
@router.post("/models", response_model=schemas.EquipmentModelResponse)
def create_model(eq_model: schemas.EquipmentModelCreate, db: Session = Depends(get_db)):
    db_obj = service.get_model_by_name(db, model_name=eq_model.model_name)
    if db_obj:
        raise HTTPException(status_code=400, detail="Model name already registered")
    return service.create_equipment_model(db=db, eq_model=eq_model)

@router.get("/models", response_model=List[schemas.EquipmentModelResponse])
def read_models(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_equipment_models(db, skip=skip, limit=limit)
