from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    Address = Column(String, primary_key=False)
    first_name = Column(Integer, primary_key=False)
    last_name = Column(Integer, primary_key=False)
    age = Column(Integer, primary_key=False)
    Email Id = Column(String, primary_key=False)

