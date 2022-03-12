from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://Shahzaib@localhost/tennis_club",
echo = True

)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)