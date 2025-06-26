from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..config.database import Base

class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, index=True)
    cpf_cnpj = Column(String, unique=True, index=True)
    name = Column(String)
    farm_name = Column(String)
    city = Column(String)
    state = Column(String)
    total_area = Column(Float)
    agricultural_area = Column(Float)
    vegetation_area = Column(Float)

    farms = relationship("Farm", back_populates="producer")

class Farm(Base):
    __tablename__ = "farms"

    id = Column(Integer, primary_key=True, index=True)
    producer_id = Column(Integer, ForeignKey("producers.id"))
    name = Column(String)
    city = Column(String)
    state = Column(String)
    total_area = Column(Float)
    agricultural_area = Column(Float)
    vegetation_area = Column(Float)

    producer = relationship("Producer", back_populates="farms")
    cultures = relationship("Culture", back_populates="farm")

class Culture(Base):
    __tablename__ = "cultures"

    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    crop_year = Column(Integer)
    crop_type = Column(String)

    farm = relationship("Farm", back_populates="cultures")

