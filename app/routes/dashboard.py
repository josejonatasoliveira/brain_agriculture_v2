from fastapi import  Depends, APIRouter
from sqlalchemy.orm import Session

from sqlalchemy import func
from app.models import models
from app.config.database import get_db

dash_router = APIRouter(
    tags=["Dashboard"]
)

@dash_router.get("/dashboard/total_farms", response_model=int)
def get_total_farms(db: Session = Depends(get_db)):
    return db.query(models.Farm).count()

@dash_router.get("/dashboard/total_hectares", response_model=float)
def get_total_hectares(db: Session = Depends(get_db)):
    total_area = db.query(func.sum(models.Farm.total_area)).scalar()
    return total_area if total_area is not None else 0.0

@dash_router.get("/dashboard/farms_by_state", response_model=dict)
def get_farms_by_state(db: Session = Depends(get_db)):
    farms_by_state = db.query(models.Farm.state, func.count(models.Farm.id)).group_by(models.Farm.state).all()
    return {state: count for state, count in farms_by_state}

@dash_router.get("/dashboard/farms_by_culture", response_model=dict)
def get_farms_by_culture(db: Session = Depends(get_db)):
    farms_by_culture = db.query(models.Culture.crop_type, func.count(models.Culture.id)).group_by(models.Culture.crop_type).all()
    return {crop_type: count for crop_type, count in farms_by_culture}

@dash_router.get("/dashboard/farms_by_soil_use", response_model=dict)
def get_farms_by_soil_use(db: Session = Depends(get_db)):
    agricultural_area = db.query(func.sum(models.Farm.agricultural_area)).scalar()
    vegetation_area = db.query(func.sum(models.Farm.vegetation_area)).scalar()
    total_area = db.query(func.sum(models.Farm.total_area)).scalar()

    if total_area == 0 or total_area is None:
        return {"agricultural_use": 0.0, "vegetation_use": 0.0, "other_use": 0.0}

    agricultural_percentage = (agricultural_area / total_area) * 100 if agricultural_area is not None else 0.0
    vegetation_percentage = (vegetation_area / total_area) * 100 if vegetation_area is not None else 0.0
    other_percentage = 100.0 - agricultural_percentage - vegetation_percentage

    return {
        "agricultural_use": agricultural_percentage,
        "vegetation_use": vegetation_percentage,
        "other_use": other_percentage
    }