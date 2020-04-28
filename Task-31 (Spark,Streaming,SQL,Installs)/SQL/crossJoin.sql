select * from hive_data as old cross join hive_data as new on old.user_id = new.user_id;
