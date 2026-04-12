from sqlalchemy import Column, Integer, String
from .database import Base


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    color = Column(String(50), nullable=False)
