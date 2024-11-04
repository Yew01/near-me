from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from pydantic import BaseModel
from queries import *

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/maincategory")
def get_maincategory(db: Session = Depends(get_db)):
    maincategory = db.query(models.MainCategory).all()
    return maincategory

@router.get("/subcategory")
def get_subcategory(db: Session = Depends(get_db)):
    subcategory = db.query(models.SubCategory).all()
    return subcategory

@router.get("/generalservice")
def get_generalservice(db: Session = Depends(get_db)):
    general_service = db.query(models.GeneralService).all()
    return general_service

@router.get("/generalservice/{mainid}/{subid}")
def get_services(mainid: int, subid: int, db: Session = Depends(get_db)):
    services = get_services_by_main_and_sub_category(db, mainid, subid)
    result = [
        {
            "mainid": service[0],
            "main_description": service[1],
            "subid": service[2],
            "sub_description": service[3],
            "gserviceid": service[4],
            "service_description": service[5]
        }
        for service in services
    ]

    return result


@router.get("/subcategory/{mainid}")
def get_subcategory_by_id(mainid: int, db: Session = Depends(get_db)):
    subcategories = get_subcategory_by_maincategory_id(db, mainid)
    result = [
        {
            "mainid": subcategory[0],
            "main_description": subcategory[1],
            "subid": subcategory[2],
            "sub_description": subcategory[3]
        }
        for subcategory in subcategories
    ]
    
    return result