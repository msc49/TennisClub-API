from database import Base
from sqlalchemy import String, Integer, DateTime, Column, null

class Player(Base):
  __tablename__ = 'players'
  id = Column(Integer, primary_key=True)
  first_name = Column(String(60),nullable=False)
  last_name = Column(String(60),nullable=False)
  date_of_birth = Column(DateTime, nullable=False)
  points = Column(Integer, nullable=False,default=1200)
  nationality = Column(String(60),nullable=False)