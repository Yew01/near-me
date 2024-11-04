from sqlalchemy.orm import Session
import models

def get_subcategory_by_maincategory_id(db: Session, mainid: int):
    return db.query(
        models.MainCategory.mainid,
        models.MainCategory.description.label('main_description'),
        models.SubCategory.subid,
        models.SubCategory.description.label('sub_description')
    ).join(models.SubCategory, models.MainCategory.mainid == models.SubCategory.mainid) \
     .filter(models.MainCategory.mainid == mainid) \
     .all()


def get_services_by_main_and_sub_category(db: Session, mainid: int, subid: int):
    results = db.query(
        models.GeneralService.mainid,
        models.MainCategory.description.label('main_description'),
        models.GeneralService.subid,
        models.SubCategory.description.label('sub_description'),
        models.GeneralService.gserviceid,
        models.GeneralService.description.label('service_description')
    ).join(models.MainCategory, models.GeneralService.mainid == models.MainCategory.mainid) \
     .join(models.SubCategory, (models.GeneralService.subid == models.SubCategory.subid) & 
                          (models.GeneralService.mainid == models.SubCategory.mainid)) \
     .filter(
         models.GeneralService.mainid == mainid,
         models.SubCategory.subid == subid
     ).all()

    return results

