-- \c tennis_club

-- CREATE TABLE players (player serial PRIMARY KEY,
--   first_name VARCHAR (50) NOT NULL,
--   last_name VARCHAR (50) NOT NULL,
--   UNIQUE(first_name, last_name), -- checks if the combination of first name and last name are unique
--   age INT NOT NULL,
--   check(age >= 16), -- checks if the player is old enough
--   nationality VARCHAR (50) NOT NULL,
--   player_score INT DEFAULT 1200,
--   games_played INT DEFAULT 0
  

-- );

-- ALTER TABLE players ADD rank_name VARCHAR(50) NULL;

CREATE TABLE matches(match serial PRIMARY KEY,
winner_id INT REFERENCES players(player),
winner_name VARCHAR(50) REFERENCES players(first_name),
loser_id INT  REFERENCES players(player),
loser_name VARCHAR(50) REFERENCES players(first_name),

);


