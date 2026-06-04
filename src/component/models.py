from sqlalchemy import Column, Date, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database import Base
from src.master_data.models import AuditMixin


class ComponentInstance(Base, AuditMixin):
    __tablename__ = "component_instances"

    master_id = Column(UUID(as_uuid=True), ForeignKey("component_masters.id"))
    equipment_id = Column(UUID(as_uuid=True), ForeignKey("equipments.id"), nullable=True)
    serial_number = Column(String, unique=True, index=True)
    installed_date = Column(Date, nullable=True)
    installed_equipment_hm = Column(Numeric(10, 2), default=0.00)
    current_component_hm = Column(Numeric(10, 2), default=0.00)
    status = Column(String, default="SPARE")

    # Relationships
    master = relationship("ComponentMaster", back_populates="instances")
    equipment = relationship("Equipment", back_populates="components")
