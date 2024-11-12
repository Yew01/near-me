from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric, ARRAY, Text, Date,PrimaryKeyConstraint
from database import Base

class MainCategory (Base):
    __tablename__ = "maincategory" 
    mainid = Column(Numeric(4), primary_key=True)
    description = Column(String (255))
    status = Column(String (255))

class SubCategory (Base):
    __tablename__ = "subcategory"
    mainid = Column(Numeric(4), ForeignKey('maincategory.mainid'), primary_key=True)
    subid = Column(Numeric(4), primary_key=True) 
    description = Column(String (255), nullable=False)
    status = Column(String (255), nullable=False)

class GeneralService(Base):
    __tablename__ = "generalservice"
    gserviceid = Column(String (255), primary_key=True)
    mainid = Column(Numeric(4), ForeignKey('maincategory.mainid'), nullable=False)
    subid = Column(Numeric(4), ForeignKey('subcategory.subid'), nullable=False)
    description = Column(String (255), nullable=False)
    status = Column(String (255), nullable=False)

class Users(Base):
    __tablename__ = "users"
    accountid = Column(String (255), primary_key=True)
    username = Column(String (255), nullable=False)
    phonenumber = Column(Numeric (15), nullable=False)
    # signinmethod = Column(String (255), nullable=False)
    email = Column(String (255), nullable=False)
    bod = Column(Date, nullable=False)
    password = Column(String (255), nullable=False)

class Business(Base):
    __tablename__ = "business"
    accountid = Column(String (255), primary_key=True)
    businessname = Column(String (255), nullable=False)
    businessemail = Column(String (255), nullable=False)
    businesstype = Column(Numeric(4), nullable=False)
    businesssubtype = Column(String (255), nullable=False)
    contactnumber = Column(Numeric (15), nullable=False)
    contactperson = Column(String (255), nullable=False)
    password = Column(String (255), nullable=False)
    streetaddress = Column(String (255), nullable=False)
    zipcode = Column(Integer, nullable=False)
    city = Column(String (255), nullable=False)
    state = Column(String (255), nullable=False)
    rating = Column(Numeric(2,1),nullable=False)
    pricerange = Column(Numeric(1), nullable=False)

class Freelancer (Base):
    __tablename__ = "freelancer"
    accountid = Column(String (255), primary_key=True)
    businessname = Column(String (255), nullable=False)
    emailaddress = Column(String (255), nullable=False)
    businesstype = Column(Numeric(4), nullable=False)
    businesssubtype = Column(Numeric(4), nullable=False)
    contactperson = Column(String (255), nullable=False)
    contactnumber = Column(Numeric(15), nullable=False)
    password = Column(String (255), nullable=False)
    streetaddress = Column(String (255), nullable=False)
    zipcode = Column(Integer, nullable=False)
    city = Column(String (255), nullable=False)
    state = Column(String (255), nullable=False)
    rating = Column(Numeric(2,1),nullable=False)
    pricerange = Column(Numeric(1), nullable=False)
    
class BusinessService(Base):
    __tablename__ = "services"
    serviceid = Column(String (255), primary_key=True)
    createdby = Column(String (255), ForeignKey('business.accountid'), nullable=False)
    gserviceid = Column(ARRAY(Text), ForeignKey('generalservice.gserviceid'), nullable=False)
    description = Column(String (255), nullable=False)
    price = Column(Integer, nullable=False)
    filterby = Column(ARRAY(Text), nullable=False)
    status = Column(String (255), nullable=False)
    duration = Column(Numeric(3), nullable=False) 
    createdat = Column(DateTime, nullable=False)
    image = Column(Text, nullable=False)

class Products(Base) :
    __tablename__ = "products"
    productid = Column(String (255), primary_key=True)
    createdby = Column(String (255), nullable=False)
    description = Column(String (255), nullable=False)
    price = Column(Numeric(8,2), nullable=False)
    status = Column(String (255), nullable=False)
    filterby = Column(ARRAY(Text), nullable=False)
    createdat = Column(DateTime, nullable=False)
    image = Column(Text, nullable=False)

class FilterService (Base):
    __tablename__ = "filterservice"
    filterid = Column(String (255), primary_key=True)
    description = Column(String (255), nullable=False)
    status = Column(String (255), nullable=False)

class Cart(Base):
    __tablename__ = "cart"
    createdby = Column(String (255), ForeignKey('users.accountid'), primary_key=True,nullable=False)
    accountid = Column(String (255), primary_key=True,nullable=False)
    productid = Column(String (255), nullable=False)
    description = Column(String (255), nullable=False)
    unitprice = Column(Numeric(8,2), nullable=False)
    quantity = Column(Numeric(2), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('accountid', 'createdby'),
    )
class Orders(Base):
    __tablename__ = "orders"
    orderid = Column(String (255), primary_key=True)
    accountid = Column(String (255), nullable=False)
    createdby = Column(String (255), nullable=False)
    createdat = Column(DateTime, nullable=False)
    totalprice = Column(Numeric(8,2), nullable=False)
    status = Column(String (255), nullable=False)
    appointmentid = Column(String (255), nullable=True)


class OrderItems(Base):
    __tablename__ = "orderitems"
    orderid = Column(String (255), ForeignKey('orders.orderid'),primary_key=True)
    accountid = Column(String (255), ForeignKey('users.accountid'),nullable=False)
    productid = Column(String (255), ForeignKey('products.productid'),nullable=False)
    serviceid = Column(String (255), ForeignKey('services.serviceid'),nullable=False)
    description = Column(String (255), nullable=False)
    unitprice = Column(Numeric(8,2), nullable=False)
    quantity = Column(Numeric(2), nullable=False)
    totalprice = Column(Numeric(8,2), nullable=False)


class Invocie(Base):
    __tablename__ = "invoice"

class Appointment(Base):
    __tablename__ = "appointment"