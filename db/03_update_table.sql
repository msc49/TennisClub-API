


update players
  set rank_name = ( CASE
  WHEN games_played < 3  THEN 'Unranked'
  WHEN games_played >= 3 AND player_score <= 2999 THEN 'Bronze'
  WHEN games_played >= 3 AND player_score >= 3000 AND player_score <=4999 THEN 'Silver'
  WHEN games_played >= 3 AND player_score >= 5000 AND player_score <=9999 THEN  'Gold'
  WHEN games_played >= 3 AND player_score >= 10000 THEN  'Supersonic Legend'
  END);