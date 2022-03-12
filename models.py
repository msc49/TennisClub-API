from enum import unique
from database import Base
from sqlalchemy import String, Integer, DateTime, Column, null
from sqlalchemy.orm import column_property

class Player(Base):
  __tablename__ = 'players'
  id = Column(Integer, primary_key=True)
  first_name = Column(String(60),nullable=False)
  last_name = Column(String(60),nullable=False)
  full_name = column_property(first_name + "" + last_name, unique= True) #checks if the person is unique
  date_of_birth = Column(DateTime, nullable=False)
  points = Column(Integer, nullable=False,default=1200)
  nationality = Column(String(60),nullable=False)