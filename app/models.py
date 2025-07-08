from sqlalchemy import Column, Integer, String, ForeignKey, Text , ARRAY ,DateTime ,Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(25), primary_key=True)
    name = Column(String, nullable=False)
    phone=Column(String(13),unique=True,nullable=False)
    password=Column(String,nullable=False)
    email = Column(String, unique=True, nullable=False)
    status=Column(Integer)
    role = Column(ARRAY)
    privilege = Column(ARRAY)
    createddate = Column(DateTime)

class role(Base):
    __tablename__ = "role"
    id = Column(String(8))
    privilege = Column(ARRAY)

class privilege(Base):
    __tablename__ = "privilege"
    id = Column(String(8))
    name = Column(String)
    routeid = Column(String(8))

class useraddress(Base):
    __tablename__='useraddress'
    id = Column(Integer,autoincrement=True)
    userid = Column(String)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    Distinct = Column(String)
    state = Column(String)
    pincode = Column(String(7))

class products(Base):
    __tablename__='products'
    id = Column(String)
    productsname = Column(String)
    price = Column(Integer)
    originalPrice = Column(Integer)
    image = Column(String)
    category = Column(String)
    rating = Column(String)
    isSale = Column(Boolean)
    volume = Column(Integer)

class userorder(Base):
    __tablename__='userorder'
    id =Column(String)
    userid = Column(String)
    productcode = Column(String)
    orderdate = Column(DateTime)
    Deliverddate = Column(DateTime)
    



