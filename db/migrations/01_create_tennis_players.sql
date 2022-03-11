
-- CREATE DATABASE tennis-club;
-- \c tennis-club


CREATE TABLE players (player serial PRIMARY KEY,
  first_name VARCHAR (50) NOT NULL,
  last_name VARCHAR (50) NOT NULL,
  UNIQUE(first_name, last_name),
  date_of_birth DATE NOT NULL,
  check(date_of_birth < (current_date - interval '16' year)),
  nationality VARCHAR (50) NOT NULL,
  player_score INT DEFAULT 1200

);

-- \i ./db/migrations/01_create_tennis_players.sql;