from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ComponentInstanceBase(BaseModel):
    serial_number: str
    installed_date: Optional[date] = None
    installed_equipment_hm: Decimal = Decimal('0.00')
    current_component_hm: Decimal = Decimal('0.00')
    status: str = "SPARE"
    is_active: bool = True

class ComponentInstanceCreate(ComponentInstanceBase):
    master_id: UUID
    equipment_id: Optional[UUID] = None

class ComponentInstanceResponse(ComponentInstanceBase):
    id: UUID
    master_id: UUID
    equipment_id: Optional[UUID]
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
