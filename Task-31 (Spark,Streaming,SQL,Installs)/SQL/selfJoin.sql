select * from hive_data as old join hive_data as new on old.user_id = new.user_id limit 10;
