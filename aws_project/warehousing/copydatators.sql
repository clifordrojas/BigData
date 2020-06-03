COPY funny_table
FROM 's3://2020clifordrojas/output/id=B0GtZ37PSPabnVXj1PIVaQ/part-00000-becd4ac0-5415-47c1-8d86-cf270559f374.c000.snappy.parquet'
IAM_ROLE 'arn:aws:iam::225169169799:role/RedShiftFullAccess'
FORMAT AS PARQUET;
