from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/business")
def get_business(db: Session = Depends(get_db)):
    business = db.query(models.Business).all()
    return business

@router.get("/freelancer")
def get_freelancer(db: Session = Depends(get_db)):
    freelancer = db.query(models.Freelancer).all()
    return freelancer