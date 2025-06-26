from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.utils import utils
from app.models import schemas, models
from app.config.database import get_db


producer_router = APIRouter(
    tags=["Producers"]
)

@producer_router.get("/")
async def read_root():
    return {"message": "Welcome to the Rural Producer Manager API!"}

@producer_router.post("/producers/", response_model=schemas.Producer)
def create_producer(producer: schemas.ProducerCreate, db: Session = Depends(get_db)):
    if not utils.validate_cpf_cnpj(producer.cpf_cnpj):
        raise HTTPException(status_code=400, detail="Invalid CPF/CNPJ")
    if not utils.validate_farm_area(producer.total_area, producer.agricultural_area, producer.vegetation_area):
        raise HTTPException(status_code=400, detail="Agricultural and vegetation area cannot exceed total area")
    db_producer = models.Producer(cpf_cnpj=producer.cpf_cnpj, name=producer.name, farm_name=producer.farm_name, city=producer.city, state=producer.state, total_area=producer.total_area, agricultural_area=producer.agricultural_area, vegetation_area=producer.vegetation_area)
    db.add(db_producer)
    db.commit()
    db.refresh(db_producer)
    return db_producer

@producer_router.get("/producers/", response_model=List[schemas.Producer])
def read_producers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    producers = db.query(models.Producer).offset(skip).limit(limit).all()
    return producers

@producer_router.get("/producers/{producer_id}", response_model=schemas.Producer)
def read_producer(producer_id: int, db: Session = Depends(get_db)):
    producer = db.query(models.Producer).filter(models.Producer.id == producer_id).first()
    if producer is None:
        raise HTTPException(status_code=404, detail="Producer not found")
    return producer

@producer_router.put("/producers/{producer_id}", response_model=schemas.Producer)
def update_producer(producer_id: int, producer: schemas.ProducerCreate, db: Session = Depends(get_db)):
    db_producer = db.query(models.Producer).filter(models.Producer.id == producer_id).first()
    if db_producer is None:
        raise HTTPException(status_code=404, detail="Producer not found")
    if not utils.validate_cpf_cnpj(producer.cpf_cnpj):
        raise HTTPException(status_code=400, detail="Invalid CPF/CNPJ")
    if not utils.validate_farm_area(producer.total_area, producer.agricultural_area, producer.vegetation_area):
        raise HTTPException(status_code=400, detail="Agricultural and vegetation area cannot exceed total area")
    for key, value in producer.model_dump().items():
        setattr(db_producer, key, value)
    db.commit()
    db.refresh(db_producer)
    return db_producer

@producer_router.delete("/producers/{producer_id}", response_model=schemas.Producer)
def delete_producer(producer_id: int, db: Session = Depends(get_db)):
    db_producer = db.query(models.Producer).filter(models.Producer.id == producer_id).first()
    if db_producer is None:
        raise HTTPException(status_code=404, detail="Producer not found")
    db.delete(db_producer)
    db.commit()
    return db_producer