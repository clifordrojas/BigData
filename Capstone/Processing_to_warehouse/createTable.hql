CREATE EXTERNAL TABLE
weed(
name string, 
ccc string, 
type string, 
thc string,
price double,
eqWeight string,
brand string,
producer_name string,
producer_phone string
)

ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS PARQUET TBLPROPERTIES ("parquet.compression"="SNAPPY");
