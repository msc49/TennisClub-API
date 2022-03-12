from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# since we will need our data to be persistent, we will use Postgres as our database

app = FastAPI()

class Player(BaseModel):
  first_name: str
  last_name: str
  date_of_birth: datetime
  nationality: str

while True: #our server cannot do anything until it connects to database so we use a while loop to continously trying to connect it it
  try: 
    conn = psycopg2.connect(host='localhost', database='tennis-club', user='Shahzaib', cursor_factory=RealDictCursor) #real dict cursor gives you the column names too of the database
    cursor = conn.cursor()
    print('Database Connection was successful')
    break

  except Exception as error:
    print('Database connection FAILED')
    print("Error: ", error)
    time.sleep(5)


@app.get("/")
def get_players(player: Player):
  cursor.execute(""" SELECT * FROM players  """)
  players = cursor.fetchall()
  return {"data": players}


@app.post("./players")
def create_player(player: Player):
  cursor.execute(""" INSERT INTO players (first_name, last_name, date_of_birth, nationality) VALUES (%s, %s, %s, %s) RETURNING *  """, (player.first_name, player.last_name, player.date_of_birth, player.nationality))
  # did not use f strings because that leaves us vulnerable to SQL injection
  new_player = cursor.fetchone()
  return {"data": new_player}
  
