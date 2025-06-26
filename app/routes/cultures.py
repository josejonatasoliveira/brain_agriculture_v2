from typing import List

from fastapi import  Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.models import schemas, models
from app.config.database import get_db

culture_router = APIRouter(
    tags=["Cultures"]
)

@culture_router.post("/cultures/", response_model=schemas.Culture)
def create_culture(culture: schemas.CultureCreate, db: Session = Depends(get_db)):
    db_culture = models.Culture(farm_id=culture.farm_id, crop_year=culture.crop_year, crop_type=culture.crop_type)
    db.add(db_culture)
    db.commit()
    db.refresh(db_culture)
    return db_culture

@culture_router.get("/cultures/", response_model=List[schemas.Culture])
def read_cultures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cultures = db.query(models.Culture).offset(skip).limit(limit).all()
    return cultures

@culture_router.get("/cultures/{culture_id}", response_model=schemas.Culture)
def read_culture(culture_id: int, db: Session = Depends(get_db)):
    culture = db.query(models.Culture).filter(models.Culture.id == culture_id).first()
    if culture is None:
        raise HTTPException(status_code=404, detail="Culture not found")
    return culture

@culture_router.put("/cultures/{culture_id}", response_model=schemas.Culture)
def update_culture(culture_id: int, culture: schemas.CultureCreate, db: Session = Depends(get_db)):
    db_culture = db.query(models.Culture).filter(models.Culture.id == culture_id).first()
    if db_culture is None:
        raise HTTPException(status_code=404, detail="Culture not found")
    for key, value in culture.model_dump().items():
        setattr(db_culture, key, value)
    db.commit()
    db.refresh(db_culture)
    return db_culture

@culture_router.delete("/cultures/{culture_id}", response_model=schemas.Culture)
def delete_culture(culture_id: int, db: Session = Depends(get_db)):
    db_culture = db.query(models.Culture).filter(models.Culture.id == culture_id).first()
    if db_culture is None:
        raise HTTPException(status_code=404, detail="Culture not found")
    db.delete(db_culture)
    db.commit()
    return db_culture