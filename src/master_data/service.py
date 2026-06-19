from sqlalchemy.orm import Session

from src.master_data import models, schemas


def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Brand).offset(skip).limit(limit).all()

def get_brand_by_code(db: Session, brand_code: str):
    return db.query(models.Brand).filter(models.Brand.brand_code == brand_code).first()

def create_brand(db: Session, brand: schemas.BrandCreate):
    db_brand = models.Brand(**brand.model_dump())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand

def get_sites(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Site).offset(skip).limit(limit).all()

def get_site_by_code(db: Session, site_code: str):
    return db.query(models.Site).filter(models.Site.site_code == site_code).first()

def create_site(db: Session, site: schemas.SiteCreate):
    db_site = models.Site(**site.model_dump())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

def get_equipment_classes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EquipmentClass).offset(skip).limit(limit).all()

def get_class_by_code(db: Session, class_code: str):
    return db.query(models.EquipmentClass).filter(models.EquipmentClass.class_code == class_code).first()

def create_equipment_class(db: Session, eq_class: schemas.EquipmentClassCreate):
    db_class = models.EquipmentClass(**eq_class.model_dump())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def get_equipment_models(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EquipmentModel).offset(skip).limit(limit).all()

def get_model_by_name(db: Session, model_name: str):
    return db.query(models.EquipmentModel).filter(models.EquipmentModel.model_name == model_name).first()

def create_equipment_model(db: Session, eq_model: schemas.EquipmentModelCreate):
    db_model = models.EquipmentModel(**eq_model.model_dump())
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model
