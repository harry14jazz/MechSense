from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from uuid import UUID
from datetime import date, datetime
from decimal import Decimal

# --- 1. EQUIPMENT (UNIT) ---
class EquipmentBase(BaseModel):
    serial_number: str
    unit_number: Optional[str] = None
    acquisition_date: Optional[date] = None
    currency: str = "IDR"
    acquisition_value: Optional[Decimal] = None
    current_hm: Decimal = Decimal('0.00')
    unit_status: str = "ACTIVE"
    unit_priority: bool = False
    is_active: bool = True

class EquipmentCreate(EquipmentBase):
    site_id: UUID
    model_id: UUID

class EquipmentResponse(EquipmentBase):
    id: UUID
    site_id: UUID
    model_id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# --- 2. HOUR METER LOG ---
class HourMeterLogBase(BaseModel):
    hour_meter: Decimal = Field(..., gt=0, description="HM aktual tidak boleh minus")
    submit_date: datetime

class HourMeterLogCreate(HourMeterLogBase):
    equipment_id: UUID

class HourMeterLogResponse(HourMeterLogBase):
    id: UUID
    equipment_id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# --- 3. EQUIPMENT STATUS LOG ---
class EquipmentStatusLogBase(BaseModel):
    status_from: Optional[str] = None
    status_to: str
    event_timestamp: datetime
    reason_code: Optional[str] = None
    remarks: Optional[str] = None
    hm_at_event: Optional[Decimal] = None

class EquipmentStatusLogCreate(EquipmentStatusLogBase):
    equipment_id: UUID

class EquipmentStatusLogResponse(EquipmentStatusLogBase):
    id: UUID
    equipment_id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)