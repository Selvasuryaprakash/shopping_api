from sqlalchemy import Column, Integer, String, ForeignKey, Text , ARRAY ,DateTime
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