CREATE TABLE IF NOT EXISTS csv_data
    ( csv_id       UUID PRIMARY KEY, 
      first_name   TEXT,
      last_name TEXT,
      age         TEXT
    );

select * from clifordtesting.csv_data;
CREATE TABLE IF NOT EXISTS json_data
    ( json_id       UUID PRIMARY KEY, 
      first_name   TEXT,
      last_name TEXT,
      age         TEXT
    );
