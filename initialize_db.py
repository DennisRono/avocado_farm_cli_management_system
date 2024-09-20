from sqlalchemy import Boolean, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("sqlite:///avocado_farm.db")


class Avocado_Varieties(Base):
    __tablename__ = "varieties"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class Tree(Base):
    __tablename__ = "trees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    height = Column(Float)
    variety = Column(String)
    leaf_health = Column(String)
    age = Column(Integer)
    diameter = Column(Float)
    pest_infested = Column(Boolean)
    date = Column(Date)


class Irrigation(Base):
    __tablename__ = "irrigation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    volume = Column(Float)
    duration = Column(Float)
    date = Column(Date)


class Harvest(Base):
    __tablename__ = "harvest"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tree_id = Column(String)
    quantity = Column(Float)
    date = Column(Date)


class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Float)
    size = Column(String)
    quality = Column(String)
    date = Column(Date)


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    variety = Column(String)
    quantity = Column(Float)
    cost = Column(Float)
    description = Column(String)
    date = Column(Date)


class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, autoincrement=True)
    buyer_name = Column(String)
    quantity = Column(Float)
    price = Column(Float)
    date = Column(Date)


class Distribution(Base):
    __tablename__ = "distribution"
    id = Column(Integer, primary_key=True, autoincrement=True)
    distributor_name = Column(String)
    quantity = Column(Float)
    date = Column(Date)


def initialize_db():
    Base.metadata.create_all(engine)
