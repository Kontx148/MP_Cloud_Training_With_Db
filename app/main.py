from pathlib import Path

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from . import models, schemas
from .database import Base, engine, get_db

app = FastAPI(title="Cars API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
STYLES_DIR = FRONTEND_DIR / "styles"


app.mount("/styles", StaticFiles(directory=STYLES_DIR), name="styles")


@app.get("/")
def serve_frontend():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/api")
def read_root():
    return {"message": "Cars API is running"}


@app.post("/cars", response_model=schemas.CarResponse, status_code=201)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = models.Car(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


@app.get("/cars", response_model=list[schemas.CarResponse])
def list_cars(db: Session = Depends(get_db)):
    return db.query(models.Car).order_by(models.Car.id.desc()).all()