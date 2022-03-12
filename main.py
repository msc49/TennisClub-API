from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_players():
  return {"message": "Hello World"}



