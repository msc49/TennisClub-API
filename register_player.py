from datetime import datetime
from tkinter import EXCEPTION
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

# since we will need our data to be persistent, we will use Postgres as our database

TennisClub = FastAPI()

class Player(BaseModel):
  first_name: str
  last_name: str
  date_of_birth: datetime
  nationality: str

try: 
  conn = psycopg2.connect(database='tennis-club', cursor_factory=RealDictCursor) #real dict cursor gives you the column names too of the database
  cursor = conn.cursor()
  print('Database Connection was successful')

except Exception as error:
  print('Database connection FAILED')
  
