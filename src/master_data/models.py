import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database import Base


class AuditMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    is_active = Column(Boolean, default=True)
    created_by = Column(String, default="SYSTEM")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

class Site(Base, AuditMixin):
    __tablename__ = "sites"
    project_code = Column(Integer)
    site_code = Column(String, unique=True, index=True)
    name = Column(String)
    location = Column(String)
    long_lat = Column(String)
    establishment_year = Column(Integer)
    end_target_year = Column(Integer)
    
    equipments = relationship("Equipment", back_populates="site")


class Brand(Base, AuditMixin):
    __tablename__ = "brands"
    brand_code = Column(String, unique=True, index=True) # misal: CAT
    brand_name = Column(String) # misal: CATERPILLAR

    models = relationship("EquipmentModel", back_populates="brand")


class EquipmentClass(Base, AuditMixin):
    __tablename__ = "equipment_classes"

    class_code = Column(String, unique=True, index=True) # misal: OHT
    description = Column(String) # misal: Off Highway Truck
    primary_metric = Column(String) # misal: Payload Capacity
    metric_unit = Column(String) # misal: Ton

    models = relationship("EquipmentModel", back_populates="equipment_class")


class EquipmentModel(Base, AuditMixin):
    __tablename__ = "equipment_models"
    brand_id = Column(UUID(as_uuid=True), ForeignKey("brands.id"))
    class_id = Column(UUID(as_uuid=True), ForeignKey("equipment_classes.id"))
    model_name = Column(String, index=True) # misal: 777D
    standard_metric_value = Column(Float) # misal: 100

    brand = relationship("Brand", back_populates="models")
    equipment_class = relationship("EquipmentClass", back_populates="models")
    equipments = relationship("Equipment", back_populates="model")
