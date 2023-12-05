from sqlalchemy import create_engine, Column, Integer, String, Text, Numeric, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    address = Column(Text)
    phone_number = Column(String)
    email = Column(Text)

class Artisan(Base):
    __tablename__ = 'artisan'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    address = Column(Text)
    email = Column(Text)
    specialization = Column(Text)
    salary = Column(Numeric)

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    material_id = Column(Integer, ForeignKey('material.id'))
    price = Column(Numeric)

    material = relationship('Material')

class ProductArtisan(Base):
    __tablename__ = 'product_artisan'

    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    artisan_id = Column(Integer, ForeignKey('artisan.id'), primary_key=True)

class Material(Base):
    __tablename__ = 'material'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    status = Column(String)
    date = Column(Date)

engine = create_engine("sqlite:///db.sqlite3", echo=True)
