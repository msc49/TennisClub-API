Tennis Club API

- using postman to test our api
- postgres as our database


pip install psycopg2-binary 

uvicorn main:app  --reload

pip install sqlalchemy

\i ./db/01_add_constraint.sql


filter through games played >=3 for rank then do unranked players
