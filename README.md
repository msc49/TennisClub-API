Tennis Club API

- using postman to test our api
- postgres as our database


pip install psycopg2-binary 

uvicorn register_player:TennisClub  --reload

pip install sqlalchemy

\i ./db/01_add_constraint.sql