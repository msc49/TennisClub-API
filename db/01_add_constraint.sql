\c tennis_club

CREATE TABLE players (player serial PRIMARY KEY,
  first_name VARCHAR (50) NOT NULL,
  last_name VARCHAR (50) NOT NULL,
  UNIQUE(first_name, last_name),
  age INT NOT NULL,
  check(age >= 16),
  nationality VARCHAR (50) NOT NULL,
  player_score INT DEFAULT 1200,
  games_played INT DEFAULT 0

);