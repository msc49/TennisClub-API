from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Player(BaseModel): #serializer
  id: int
  first_name: str
  last_name: str
  date_of_birth: datetime
  nationality: str
  player_score: int

  class Config:
    orm_model = True




@app.get("/")
def get_players():
  pass

@app.get("/players/{player_id}")
def get_a_player(player_id: int):
  pass


@app.post('/players')
def create_player():
  pass

@app.put("/players/{player_id}")
def update_player(player_id: int):
  pass

@app.delete("/players/{player_id}")
def delete_player(player_id: int):
  pass




