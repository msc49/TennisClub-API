from fastapi import FastAPI, status
from pydantic import BaseModel, validator
from datetime import datetime

from typing import List, Optional

import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Player(BaseModel): #serializer
  first_name: str
  last_name: str
  nationality: str
  age: int
  player_score: Optional[int] = 1200
  games_played: Optional[int] = 0
  
  
conn = psycopg2.connect(host='localhost', database='tennis_club', user='Shahzaib', cursor_factory=RealDictCursor) #real dict cursor gives you the column names too of the database
cursor = conn.cursor()
print('Database Connection was successful')

  
# GET ALL
@app.get('/')
def get_players(player: Player):
  cursor.execute(""" SELECT * FROM players  """)
  players = cursor.fetchall()
  return {"data": players}

# --------------------------- ENDPOINT 1 ------------------------------------------------------------
@app.post('/players',status_code=status.HTTP_201_CREATED)
def create_player(player: Player):
  cursor.execute(""" INSERT INTO players (first_name, last_name, age, nationality, player_score, games_played) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *  """, (player.first_name, player.last_name, player.age, player.nationality, player.player_score, player.games_played))
  # did not use f strings because that leaves us vulnerable to SQL injection
  conn.commit()
  new_player = cursor.fetchone()
  return {"data": new_player}

# ----------------------------- ------------------------------------------------------------

# --------------------------- ENDPOINT 2 ------------------------------------------------------------

# GETTING PLAYERS BY NATIONALITY

@app.get('/players/{nationality}')
def get_players_by_nationality(nationality: str, players: Player):
  cursor.execute(""" SELECT * FROM players WHERE nationality = %s  """, (str(nationality), ))
  national_players = cursor.fetchall()
  return {"nationality": national_players}

# GETTING PLAYERS BY RANK NAME
@app.get('/players/rank/{rank_name}')
def get_players_by_nationality(rank_name: str, players: Player):
  cursor.execute(open("./db/03_update_table.sql", "r").read()) #updates our table so the rank_name goes from NULL to whatever is required
  conn.commit() #save changes
  cursor.execute(""" SELECT * FROM players WHERE rank_name = %s  """, (str(rank_name), ))
  national_players = cursor.fetchall()
  return {"{rank_name}": national_players}

  # ----------------------------- ------------------------------------------------------------

  # --------------------------- ENDPOINT 3 ------------------------------------------------------------

class Match(BaseModel):
  winner_id: int
  loser_id: int



#creating a match
@app.post("/matches")
def create_match( matches: Match):
  cursor.execute(""" INSERT INTO matches (winner_id, loser_id) VALUES (%s,%s) RETURNING *
   """,
  (matches.winner_id, matches.loser_id))
  conn.commit()
  new_match = cursor.fetchone()
  return {"data": new_match}