from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class ProducerBase(BaseModel):
    cpf_cnpj: str
    name: str
    farm_name: str
    city: str
    state: str
    total_area: float
    agricultural_area: float
    vegetation_area: float

class ProducerCreate(ProducerBase):
    pass

class Producer(ProducerBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class FarmBase(BaseModel):
    producer_id: int
    name: str
    city: str
    state: str
    total_area: float
    agricultural_area: float
    vegetation_area: float

class FarmCreate(FarmBase):
    pass

class Farm(FarmBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class CultureBase(BaseModel):
    farm_id: int
    crop_year: int
    crop_type: str

class CultureCreate(CultureBase):
    pass

class Culture(CultureBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

