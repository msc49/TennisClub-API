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




@app.get("/")
def get_players():
  return {"message": "Hello World"}



