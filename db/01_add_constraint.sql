\c tennis_club


ALTER TABLE players ADD UNIQUE(first_name, last_name);

ALTER TABLE players ADD CONSTRAINT date_of_birth CHECK(date_of_birth < (current_date - interval '16' year));
