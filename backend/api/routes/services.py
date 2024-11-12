from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from pydantic import BaseModel
from queries import *
import uuid
from datetime import datetime

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

# @router.post("/businessservice")
# def create_business_service(description: str, price: int, db: Session = Depends(get_db)):
#     # Generate a unique bserviceid
#     bserviceid = f"BS{uuid.uuid4().hex[:8].upper()}"

#     # Set default values
#     createdby = "DEFAULT_BUSINESS_ID"  # You might want to change this to a valid business ID
#     gserviceid = "DEFAULT_GSERVICE_ID"  # You might want to change this to a valid general service ID
#     status = "ACTIVE"
#     duration = 60  # Default duration in minutes
#     createdat = datetime.utcnow()

#     # Create the BusinessService object
#     db_business_service = models.BusinessService(
#         bserviceid=bserviceid,
#         createdby=createdby,
#         gserviceid=gserviceid,
#         description=description,
#         price=price,
#         status=status,
#         duration=duration,
#         createdat=createdat
#     )

#     db.add(db_business_service)
#     db.commit()
#     db.refresh(db_business_service)
#     return db_business_service