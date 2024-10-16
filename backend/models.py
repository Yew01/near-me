from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base

class MainCategory (Base):
    __tablename__ = "maincategory" 
    mainid = Column(Integer, primary_key=True)
    description = Column(String)
    status = Column(String)

class SubCategory (Base):
    __tablename__ = "subcategory"
    mainid = Column(Integer, ForeignKey('maincategory.mainid'), primary_key=True)
    subid = Column(Integer, primary_key=True) 
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)

class Business(Base):
    __tablename__ = "business"
    accountid = Column(String, primary_key=True)
    businessname = Column(String, nullable=False)
    businessemail = Column(String, nullable=False)
    businesstype = Column(String, nullable=False)
    businesssubtype = Column(String, nullable=False)
    contactnumber = Column(Integer, nullable=False)
    contactperson = Column(String, nullable=False)
    password = Column(String, nullable=False)
    streetaddress = Column(String, nullable=False)
    zipcode = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)

class Freelancer (Base):
    __tablename__ = "freelancer"
    accountid = Column(String, primary_key=True)
    businessname = Column(String, nullable=False)
    businessemail = Column(String, nullable=False)
    businesstype = Column(String, nullable=False)
    businesssubtype = Column(String, nullable=False)
    contactperson = Column(String, nullable=False)
    contactnumber = Column(Integer, nullable=False)
    password = Column(String, nullable=False)
    streetaddress = Column(String, nullable=False)
    zipcode = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)