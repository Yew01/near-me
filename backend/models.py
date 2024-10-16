from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base

class MainCategory (Base):
    __tablename__ = "maincategory" 
    mainid = Column(Integer, primary_key=True)
    description = Column(String)
    status = Column(String)


