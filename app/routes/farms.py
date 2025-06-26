from typing import List

from fastapi import  Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.models import schemas, models
from app.config.database import get_db

farm_router = APIRouter(
    tags=["Farms"]
)

@farm_router.post("/farms/", response_model=schemas.Farm)
def create_farm(farm: schemas.FarmCreate, db: Session = Depends(get_db)):
    db_farm = models.Farm(producer_id=farm.producer_id, name=farm.name, city=farm.city, state=farm.state, total_area=farm.total_area, agricultural_area=farm.agricultural_area, vegetation_area=farm.vegetation_area)
    db.add(db_farm)
    db.commit()
    db.refresh(db_farm)
    return db_farm

@farm_router.get("/farms/", response_model=List[schemas.Farm])
def read_farms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    farms = db.query(models.Farm).offset(skip).limit(limit).all()
    return farms

@farm_router.get("/farms/{farm_id}", response_model=schemas.Farm)
def read_farm(farm_id: int, db: Session = Depends(get_db)):
    farm = db.query(models.Farm).filter(models.Farm.id == farm_id).first()
    if farm is None:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm

@farm_router.put("/farms/{farm_id}", response_model=schemas.Farm)
def update_farm(farm_id: int, farm: schemas.FarmCreate, db: Session = Depends(get_db)):
    db_farm = db.query(models.Farm).filter(models.Farm.id == farm_id).first()
    if db_farm is None:
        raise HTTPException(status_code=404, detail="Farm not found")
    for key, value in farm.model_dump().items():
        setattr(db_farm, key, value)
    db.commit()
    db.refresh(db_farm)
    return db_farm

@farm_router.delete("/farms/{farm_id}", response_model=schemas.Farm)
def delete_farm(farm_id: int, db: Session = Depends(get_db)):
    db_farm = db.query(models.Farm).filter(models.Farm.id == farm_id).first()
    if db_farm is None:
        raise HTTPException(status_code=404, detail="Farm not found")
    db.delete(db_farm)
    db.commit()
    return db_farm