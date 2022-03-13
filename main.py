from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import datetime

from typing import List

import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Player(BaseModel): #serializer
  id: int
  first_name: str
  last_name: str
  nationality: str
  age: int
  # points: int
  # games_played: int
  
  
conn = psycopg2.connect(host='localhost', database='tennis_club', user='Shahzaib', cursor_factory=RealDictCursor) #real dict cursor gives you the column names too of the database
cursor = conn.cursor()
print('Database Connection was successful')

  

@app.get('/')
def get_players(player: Player):
  cursor.execute(""" SELECT * FROM players  """)
  players = cursor.fetchall()
  return {"data": players}

# --------------------------- ENDPOINT 1 ------------------------------------------------------------
@app.post('/players',status_code=status.HTTP_201_CREATED)
def create_player(player: Player):
  cursor.execute(""" INSERT INTO players (first_name, last_name, age, nationality) VALUES (%s, %s, %s, %s) RETURNING *  """, (player.first_name, player.last_name, player.age, player.nationality))
  # did not use f strings because that leaves us vulnerable to SQL injection
  conn.commit()
  new_player = cursor.fetchone()
  return {"data": new_player}

# ----------------------------- ------------------------------------------------------------

