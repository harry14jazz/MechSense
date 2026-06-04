from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from uuid import UUID
from datetime import datetime
from decimal import Decimal

# --- 1. SITE ---
class SiteBase(BaseModel):
    project_code: Optional[int] = None
    site_code: str = Field(..., description="Kode Site")
    name: str = Field(..., description="Nama Site")
    location: Optional[str] = None
    long_lat: Optional[str] = None
    establishment_year: Optional[int] = None
    end_target_year: Optional[int] = None
    is_active: bool = True

class SiteCreate(SiteBase):
    pass

class SiteResponse(SiteBase):
    id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# --- 2. BRAND ---
class BrandBase(BaseModel):
    brand_code: str
    brand_name: str
    is_active: bool = True

class BrandCreate(BrandBase):
    pass

class BrandResponse(BrandBase):
    id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# --- 3. EQUIPMENT CLASS ---
class EquipmentClassBase(BaseModel):
    class_code: str
    description: str
    primary_metric: Optional[str] = None
    metric_unit: Optional[str] = None
    is_active: bool = True

class EquipmentClassCreate(EquipmentClassBase):
    pass

class EquipmentClassResponse(EquipmentClassBase):
    id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# --- 4. EQUIPMENT MODEL ---
class EquipmentModelBase(BaseModel):
    model_name: str
    standard_metric_value: Optional[float] = None
    is_active: bool = True

class EquipmentModelCreate(EquipmentModelBase):
    brand_id: UUID
    class_id: UUID

class EquipmentModelResponse(EquipmentModelBase):
    id: UUID
    brand_id: UUID
    class_id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# --- 5. COMPONENT MASTER ---
class ComponentMasterBase(BaseModel):
    component_code: str
    name: str
    description: Optional[str] = None
    is_active: bool = True

class ComponentMasterCreate(ComponentMasterBase):
    pass

class ComponentMasterResponse(ComponentMasterBase):
    id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# --- 6. MODEL COMPONENTS (Mapping Target Life) ---
class ModelComponentsBase(BaseModel):
    target_life_hm: Decimal = Field(..., gt=0)
    default_qty: int = Field(default=1, gt=0)
    is_active: bool = True

class ModelComponentsCreate(ModelComponentsBase):
    model_id: UUID
    component_master_id: UUID

class ModelComponentsResponse(ModelComponentsBase):
    id: UUID
    model_id: UUID
    component_master_id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)