from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

# since we will need our data to be persistent, we will use Postgres as our database

TennisClub = FastAPI()

class Player(BaseModel):
  first_name: str
  last_name: str
  date_of_birth: datetime
  nationality: str
