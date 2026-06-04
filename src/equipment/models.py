from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database import Base

from src.master_data.models import AuditMixin


class Equipment(Base, AuditMixin):
    __tablename__ = "equipments"
    site_id = Column(UUID(as_uuid=True), ForeignKey("sites.id"))
    model_id = Column(UUID(as_uuid=True), ForeignKey("equipment_models.id"))
    serial_number = Column(String, unique=True, index=True)
    unit_number = Column(String)
    acquisition_date = Column(Date, nullable=True)
    currency = Column(String)
    acquisition_value = Column(Numeric(12, 2), nullable=True)
    current_hm = Column(Numeric(10, 2), default=0.00)
    unit_status = Column(String, default="ACTIVE") # misal: ACTIVE, BREAKDOWN, STANDBY
    unit_priority = Column(Boolean, default=False)

    site = relationship("Site", back_populates="equipments")
    model = relationship("EquipmentModel", back_populates="equipments")
    hm_logs = relationship("HourMeterLog", back_populates="equipment", cascade="all, delete-orphan")
    components = relationship("ComponentInstance", back_populates="equipment")
    status_logs = relationship("EquipmentStatusLog", back_populates="equipment", cascade="all, delete-orphan")


class HourMeterLog(Base, AuditMixin):
    __tablename__ = "hour_meter_logs"

    equipment_id = Column(UUID(as_uuid=True), ForeignKey("equipments.id"))
    hour_meter = Column(Numeric(10, 2), nullable=False)
    submit_date = Column(DateTime(timezone=True))

    equipment = relationship("Equipment", back_populates="hm_logs")

class EquipmentStatusLog(Base, AuditMixin):
    __tablename__ = "equipment_status_logs"

    equipment_id = Column(UUID(as_uuid=True), ForeignKey("equipments.id"))
    status_from = Column(String, nullable=True)
    status_to = Column(String, nullable=False)
    event_timestamp = Column(DateTime(timezone=True), nullable=False)
    reason_code = Column(String, nullable=True) 
    remarks = Column(String, nullable=True)
    hm_at_event = Column(Numeric(10, 2), nullable=True)

    # Relationship
    equipment = relationship("Equipment", back_populates="status_logs")