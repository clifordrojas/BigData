SELECT *, 
SUM(time) OVER (PARTITION BY user_id) as wind

FROM movie_data;
