from sqlalchemy import Column, Integer, String, ForeignKey, Text, ARRAY, DateTime, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(25), primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(13), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    status = Column(Integer)
    createddate = Column(DateTime)
    privilege_ids = Column(ARRAY(String),nullable=True)
    # role_ids = Column(ARRAY(String),nullable=True)

    # Relationships
    # roles = relationship("Role", secondary="user_roles", back_populates="users")
    # privileges = relationship("Privilege", secondary="user_privileges", back_populates="users")
    # addresses = relationship("UserAddress", back_populates="user")
    # orders = relationship("UserOrder", back_populates="user")


class Role(Base):
    __tablename__ = "role"

    id = Column(String(8), primary_key=True)
    name = Column(String(50), nullable=False)
    # privileges = relationship("Privilege", secondary="role_privileges", back_populates="roles")
    # users = relationship("User", secondary="user_roles", back_populates="roles")


class Privilege(Base):
    __tablename__ = "privilege"

    id = Column(String(8), primary_key=True)
    name = Column(String(100), nullable=False)
    routeid = Column(String(8))
    # roles = relationship("Role", secondary="role_privileges", back_populates="privileges")
    # users = relationship("User", secondary="user_privileges", back_populates="privileges")


class UserAddress(Base):
    __tablename__ = 'useraddress'

    id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(String(25), ForeignKey('users.id'), nullable=False)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    district = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    pincode = Column(String(7), nullable=False)

    # user = relationship("User", back_populates="addresses")


class Product(Base):
    __tablename__ = 'products'

    id = Column(String(50), primary_key=True)
    productname = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    originalPrice = Column(Integer)
    image = Column(String(255))
    category = Column(String(100))
    rating = Column(String(10))
    isSale = Column(Boolean, default=False)
    volume = Column(Integer)


class UserOrder(Base):
    __tablename__ = 'userorder'

    id = Column(String(50), primary_key=True)
    userid = Column(String(25), ForeignKey('users.id'), nullable=False)
    productcode = Column(String(50), ForeignKey('products.id'), nullable=False)
    orderdate = Column(DateTime, nullable=False)
    delivereddate = Column(DateTime)

    # user = relationship("User", back_populates="orders")
    # product = relationship("Product")

    class Paymentdetails(Base):
    __tablename__ = 'paymentdetails'

    id = Column(String(50), primary_key=True)
    productcode = Column(String(50), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer)
    amount = Column(Integer)
    status = Column(Integer)
    



