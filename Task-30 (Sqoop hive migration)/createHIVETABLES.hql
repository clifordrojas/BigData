CREATE TABLE hive_data
    ( user_id   INT,
      movie_id  INT,
      rating    INT,
      time      INT
    )
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

CREATE TABLE u_info
    ( num_users   int,
      items  int,
      rating    int
      );

CREATE TABLE u_genre 
( genre  VARCHAR(25),
  genre_id int
);

CREATE TABLE u_occupation 
( occupation VARCHAR(50)
);
