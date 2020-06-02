COPY funny_table
FROM 's3://2020clifordrojas/output/id=B0GtZ37PSPabnVXj1PIVaQ/value=Chuck Norris once destroyed a city to prove a point When asked Chuck Norris said The point was That I can destroy a city./part-00000-b9bbf066-9274-4c97-b332-648c4d034033.c000.snappy.parquet'
IAM_ROLE 'arn:aws:iam::225169169799:role/aws-service-role/redshift.amazonaws.com/AWSServiceRoleForRedshift'
FORMAT AS PARQUET;